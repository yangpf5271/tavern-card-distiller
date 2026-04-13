#!/usr/bin/env python3
"""Extract character card data from SillyTavern card files.

Supports:
- PNG (tEXt, iTXt, zTXt chunks)
- WEBP (EXIF XMP metadata)
- JPEG/JPG (EXIF Comment / XMP)
- JSON (direct card data)

Card specs: V1 (flat), V2 (nested "data"), V3 (ccv3 key, chara_card_v3)

Usage:
    python3 extract_card.py <card_file> [--output-dir <dir>]

Outputs:
    <output-dir>/card_data.json   - Full extracted JSON
    <output-dir>/embedded_images/ - Any embedded images found
"""

import sys
import os
import json
import base64
import struct
import zlib
import argparse
from pathlib import Path


# ─── PNG Parsing ───────────────────────────────────────────────

def read_png_chunks(filepath: str):
    """Read all chunks from a PNG file."""
    chunks = []
    with open(filepath, "rb") as f:
        sig = f.read(8)
        if sig != b"\x89PNG\r\n\x1a\n":
            raise ValueError("Not a valid PNG file")
        while True:
            length_bytes = f.read(4)
            if len(length_bytes) < 4:
                break
            length = struct.unpack(">I", length_bytes)[0]
            chunk_type = f.read(4).decode("ascii", errors="replace")
            data = f.read(length)
            _crc = f.read(4)
            chunks.append((chunk_type, data))
            if chunk_type == "IEND":
                break
    return chunks


def extract_text_chunks(chunks):
    """Extract tEXt, iTXt, and zTXt chunks from PNG."""
    text_data = {}
    for chunk_type, data in chunks:
        try:
            if chunk_type == "tEXt":
                null_idx = data.index(b"\x00")
                keyword = data[:null_idx].decode("latin-1")
                value = data[null_idx + 1:].decode("latin-1")
                text_data[keyword] = value

            elif chunk_type == "zTXt":
                null_idx = data.index(b"\x00")
                keyword = data[:null_idx].decode("latin-1")
                comp_method = data[null_idx + 1]
                compressed = data[null_idx + 2:]
                if comp_method == 0:
                    value = zlib.decompress(compressed).decode("latin-1")
                else:
                    value = compressed.decode("latin-1", errors="replace")
                text_data[keyword] = value

            elif chunk_type == "iTXt":
                null_idx = data.index(b"\x00")
                keyword = data[:null_idx].decode("utf-8")
                rest = data[null_idx + 1:]
                comp_flag = rest[0]
                comp_method = rest[1]
                rest = rest[2:]
                null_idx = rest.index(b"\x00")
                rest = rest[null_idx + 1:]
                null_idx = rest.index(b"\x00")
                rest = rest[null_idx + 1:]
                if comp_flag and comp_method == 0:
                    text = zlib.decompress(rest).decode("utf-8")
                else:
                    text = rest.decode("utf-8")
                text_data[keyword] = text
        except Exception as e:
            print(f"  Warning: Failed to parse {chunk_type} chunk: {e}")
            continue

    return text_data


def extract_from_png(filepath: str) -> dict:
    """Extract character card data from a PNG file."""
    print(f"Reading PNG: {filepath}")
    chunks = read_png_chunks(filepath)
    chunk_types = [c[0] for c in chunks]
    print(f"  Found {len(chunks)} chunks: {', '.join(set(chunk_types))}")

    text_data = extract_text_chunks(chunks)
    print(f"  Text chunk keys: {list(text_data.keys())}")

    if not text_data:
        raise ValueError("No text chunks found in PNG. Not a character card.")

    return decode_card_data(text_data)


# ─── WEBP Parsing ──────────────────────────────────────────────

def extract_from_webp(filepath: str) -> dict:
    """Extract character card data from a WEBP file.

    WEBP files may store card data in:
    - EXIF metadata (UserComment or ImageDescription)
    - XMP metadata (embedded XML with chara/ccv3 data)
    - RIFF chunk with custom metadata
    """
    print(f"Reading WEBP: {filepath}")

    with open(filepath, "rb") as f:
        raw = f.read()

    card = {}

    # Method 1: Search for base64-encoded JSON in raw bytes
    card = _search_raw_for_card(raw)
    if card:
        print("  Found card data via raw byte search")
        return card

    # Method 2: Try exiftool if available
    card = _try_exiftool(filepath)
    if card:
        print("  Found card data via exiftool")
        return card

    # Method 3: Try Pillow EXIF
    card = _try_pillow_exif(filepath)
    if card:
        print("  Found card data via Pillow EXIF")
        return card

    raise ValueError("Could not extract character card data from WEBP file.")


# ─── JPEG Parsing ──────────────────────────────────────────────

def extract_from_jpeg(filepath: str) -> dict:
    """Extract character card data from a JPEG file.

    JPEG files may store card data in:
    - EXIF UserComment
    - EXIF ImageDescription
    - XMP metadata
    - COM (Comment) marker
    """
    print(f"Reading JPEG: {filepath}")

    with open(filepath, "rb") as f:
        raw = f.read()

    card = {}

    # Method 1: Search for base64-encoded JSON in raw bytes
    card = _search_raw_for_card(raw)
    if card:
        print("  Found card data via raw byte search")
        return card

    # Method 2: Try exiftool
    card = _try_exiftool(filepath)
    if card:
        print("  Found card data via exiftool")
        return card

    # Method 3: Try Pillow EXIF
    card = _try_pillow_exif(filepath)
    if card:
        print("  Found card data via Pillow EXIF")
        return card

    raise ValueError("Could not extract character card data from JPEG file.")


# ─── JSON Direct ───────────────────────────────────────────────

def extract_from_json(filepath: str) -> dict:
    """Load character card data directly from a JSON file."""
    print(f"Reading JSON: {filepath}")
    with open(filepath, "r", encoding="utf-8") as f:
        card = json.load(f)
    if not isinstance(card, dict):
        raise ValueError("JSON file does not contain a valid card object.")
    return card


# ─── Shared Extraction Helpers ─────────────────────────────────

def _search_raw_for_card(raw: bytes) -> dict:
    """Search raw file bytes for base64-encoded card JSON.

    Many tools embed the card as a base64 string somewhere in the file.
    We look for known markers like 'chara' followed by base64 data.
    """
    # Look for "chara" keyword followed by base64 data
    for marker in [b"chara\x00", b"ccv3\x00", b"chara:", b"ccv3:"]:
        idx = raw.find(marker)
        if idx >= 0:
            start = idx + len(marker)
            # Skip any null bytes or whitespace
            while start < len(raw) and raw[start:start+1] in (b"\x00", b" ", b"\t", b"\n", b"\r"):
                start += 1
            # Try to find the end of base64 data
            end = start
            b64_chars = set(b"ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/=\n\r")
            while end < len(raw) and raw[end] in b64_chars:
                end += 1
            if end - start > 100:  # Minimum reasonable card size
                try:
                    b64_data = raw[start:end]
                    decoded = base64.b64decode(b64_data).decode("utf-8")
                    return json.loads(decoded)
                except Exception:
                    pass

    # Look for raw JSON with card-like structure
    for pattern in [b'"spec":"chara_card', b'"data":{', b'"char_name":', b'"name":']:
        idx = raw.find(pattern)
        if idx >= 0:
            # Walk back to find opening brace
            brace_start = raw.rfind(b"{", max(0, idx - 500), idx)
            if brace_start >= 0:
                # Try to parse JSON from this point
                for end_offset in [len(raw), brace_start + 100000, brace_start + 50000, brace_start + 10000]:
                    try:
                        text = raw[brace_start:min(end_offset, len(raw))].decode("utf-8", errors="replace")
                        # Find matching closing brace
                        depth = 0
                        for i, ch in enumerate(text):
                            if ch == "{":
                                depth += 1
                            elif ch == "}":
                                depth -= 1
                                if depth == 0:
                                    card = json.loads(text[:i+1])
                                    if isinstance(card, dict) and ("data" in card or "name" in card or "char_name" in card):
                                        return card
                                    break
                    except Exception:
                        continue
    return {}


def _try_exiftool(filepath: str) -> dict:
    """Try to extract card data using exiftool CLI."""
    import subprocess
    try:
        result = subprocess.run(
            ["exiftool", "-b", "-UserComment", filepath],
            capture_output=True, timeout=10
        )
        if result.returncode == 0 and result.stdout:
            data = result.stdout.strip()
            # Try base64 decode
            try:
                decoded = base64.b64decode(data).decode("utf-8")
                return json.loads(decoded)
            except Exception:
                pass
            # Try direct JSON
            try:
                return json.loads(data.decode("utf-8"))
            except Exception:
                pass

        # Try ImageDescription
        result = subprocess.run(
            ["exiftool", "-b", "-ImageDescription", filepath],
            capture_output=True, timeout=10
        )
        if result.returncode == 0 and result.stdout:
            data = result.stdout.strip()
            try:
                decoded = base64.b64decode(data).decode("utf-8")
                return json.loads(decoded)
            except Exception:
                pass
            try:
                return json.loads(data.decode("utf-8"))
            except Exception:
                pass
    except FileNotFoundError:
        pass  # exiftool not installed
    except Exception:
        pass
    return {}


def _try_pillow_exif(filepath: str) -> dict:
    """Try to extract card data using Pillow's EXIF reader."""
    try:
        from PIL import Image
        img = Image.open(filepath)
        exif = img.getexif()
        if exif:
            # UserComment (tag 0x9286) or ImageDescription (tag 0x010E)
            for tag_id in [0x9286, 0x010E]:
                if tag_id in exif:
                    data = exif[tag_id]
                    if isinstance(data, bytes):
                        data = data.decode("utf-8", errors="replace")
                    # Try base64
                    try:
                        decoded = base64.b64decode(data).decode("utf-8")
                        return json.loads(decoded)
                    except Exception:
                        pass
                    # Try direct JSON
                    try:
                        return json.loads(data)
                    except Exception:
                        pass
        # Try info dict (PNG-style text chunks stored by some tools)
        info = getattr(img, "info", {})
        for key in ["chara", "ccv3", "comment"]:
            if key in info:
                val = info[key]
                if isinstance(val, bytes):
                    val = val.decode("utf-8", errors="replace")
                try:
                    decoded = base64.b64decode(val).decode("utf-8")
                    return json.loads(decoded)
                except Exception:
                    pass
                try:
                    return json.loads(val)
                except Exception:
                    pass
    except ImportError:
        pass  # Pillow not installed
    except Exception:
        pass
    return {}


# ─── Card Data Decoding ───────────────────────────────────────

def decode_card_data(text_data: dict) -> dict:
    """Decode character card data from text chunk key-value pairs."""
    card = {}

    # Priority order: ccv3 (V3) > chara (V1/V2) > others
    for key in ["ccv3", "chara"]:
        if key in text_data:
            try:
                raw = text_data[key]
                decoded = base64.b64decode(raw).decode("utf-8")
                card = json.loads(decoded)
                print(f"  Decoded card from '{key}' key (base64)")
                break
            except Exception:
                # Maybe not base64, try direct JSON
                try:
                    card = json.loads(text_data[key])
                    print(f"  Decoded card from '{key}' key (direct JSON)")
                    break
                except Exception:
                    pass

    # Try other keys as JSON
    if not card:
        for key, value in text_data.items():
            try:
                parsed = json.loads(value)
                if isinstance(parsed, dict) and ("name" in parsed or "data" in parsed or "char_name" in parsed):
                    card = parsed
                    print(f"  Decoded card from '{key}' key (JSON)")
                    break
            except (json.JSONDecodeError, ValueError):
                pass

    # Try base64 decode on remaining keys
    if not card:
        for key, value in text_data.items():
            try:
                decoded = base64.b64decode(value).decode("utf-8")
                parsed = json.loads(decoded)
                if isinstance(parsed, dict):
                    card = parsed
                    print(f"  Decoded card from '{key}' key (base64 fallback)")
                    break
            except Exception:
                pass

    if not card:
        raise ValueError("Could not decode character card data from any text chunk.")

    return card


# ─── Card Normalization ───────────────────────────────────────

def normalize_card(card: dict) -> dict:
    """Normalize V1/V2/V3 card format to a unified structure."""
    result = {
        "spec": "unknown",
        "spec_version": "",
        "name": "",
        "description": "",
        "personality": "",
        "first_mes": "",
        "mes_example": "",
        "scenario": "",
        "system_prompt": "",
        "post_history_instructions": "",
        "creator_notes": "",
        "creator_notes_multilingual": {},
        "creator": "",
        "character_version": "",
        "tags": [],
        "alternate_greetings": [],
        "world_book": [],
        "regex_scripts": [],
        "embedded_images": [],
        "assets": [],
        "extensions": {},
        "raw": card,
    }

    # Determine spec version
    data = card.get("data", card)
    spec = card.get("spec", data.get("spec", ""))

    if spec == "chara_card_v3":
        result["spec"] = "v3"
        result["spec_version"] = data.get("spec_version", "3.0")
    elif spec.startswith("chara_card_v"):
        result["spec"] = spec.replace("chara_card_", "")
        result["spec_version"] = spec
    elif "data" in card:
        result["spec"] = "v2"
        result["spec_version"] = "chara_card_v2"
    else:
        result["spec"] = "v1"
        result["spec_version"] = "v1"

    # Core fields
    result["name"] = data.get("name", data.get("char_name", ""))
    result["description"] = data.get("description", data.get("char_persona", ""))
    result["personality"] = data.get("personality", "")
    result["first_mes"] = data.get("first_mes", data.get("char_greeting", ""))
    result["mes_example"] = data.get("mes_example", data.get("example_dialogue", ""))
    result["scenario"] = data.get("scenario", data.get("world_scenario", ""))
    result["system_prompt"] = data.get("system_prompt", "")
    result["post_history_instructions"] = data.get("post_history_instructions", "")
    result["creator_notes"] = data.get("creator_notes", "")
    result["creator"] = data.get("creator", "")
    result["character_version"] = data.get("character_version", "")
    result["tags"] = data.get("tags", [])
    result["alternate_greetings"] = data.get("alternate_greetings", [])

    # V3 multilingual creator notes
    result["creator_notes_multilingual"] = data.get("creator_notes_multilingual", {})

    # V3 source array
    result["source"] = data.get("source", [])

    # V3 group_only_greetings
    result["group_only_greetings"] = data.get("group_only_greetings", [])

    # World book / character book — keep ALL entries including disabled
    char_book = data.get("character_book", {})
    if char_book:
        result["character_book_meta"] = {
            "name": char_book.get("name", ""),
            "description": char_book.get("description", ""),
            "scan_depth": char_book.get("scan_depth"),
            "token_budget": char_book.get("token_budget"),
            "recursive_scanning": char_book.get("recursive_scanning"),
            "extensions": char_book.get("extensions", {}),
        }
        entries = char_book.get("entries", [])
        for entry in entries:
            wb_entry = {
                "keys": entry.get("keys", entry.get("key", [])),
                "secondary_keys": entry.get("secondary_keys", []),
                "content": entry.get("content", ""),
                "enabled": entry.get("enabled", True),
                "position": entry.get("position", "before_char"),
                "name": entry.get("name", entry.get("comment", "")),
                "insertion_order": entry.get("insertion_order", 0),
                "priority": entry.get("priority", entry.get("order", 0)),
                # Extended fields
                "id": entry.get("id", entry.get("uid", None)),
                "comment": entry.get("comment", ""),
                "selective": entry.get("selective", False),
                "constant": entry.get("constant", False),
                "depth": entry.get("depth", 4),
                "role": entry.get("role", None),
                "group": entry.get("group", ""),
                "group_override": entry.get("group_override", False),
                "group_weight": entry.get("group_weight", None),
                "prevent_recursion": entry.get("prevent_recursion", False),
                "delay_until_recursion": entry.get("delay_until_recursion", False),
                "scan_depth": entry.get("scan_depth", None),
                "match_whole_words": entry.get("match_whole_words", None),
                "use_group_scoring": entry.get("use_group_scoring", None),
                "automation_id": entry.get("automation_id", ""),
                "extensions": entry.get("extensions", {}),
            }
            # SillyTavern extensions within entry
            entry_ext = entry.get("extensions", {})
            if entry_ext:
                wb_entry["fav"] = entry_ext.get("fav", False)
                wb_entry["display_index"] = entry_ext.get("display_index", None)
                wb_entry["probability"] = entry_ext.get("probability", 100)
                wb_entry["useProbability"] = entry_ext.get("useProbability", False)
            result["world_book"].append(wb_entry)

    # Extensions
    extensions = data.get("extensions", {})
    result["extensions"] = extensions

    # Regex scripts from extensions
    if "regex_scripts" in extensions:
        result["regex_scripts"] = extensions["regex_scripts"]

    # Embedded images from extensions
    if "embedded_images" in extensions:
        result["embedded_images"] = extensions["embedded_images"]

    # V3 assets (avatar, emotion sprites, backgrounds, etc.)
    if "assets" in data:
        for asset in data.get("assets", []):
            result["assets"].append(asset)
            if asset.get("type", "").startswith("icon") or asset.get("type", "").startswith("image"):
                result["embedded_images"].append(asset)

    # depth_prompt (SillyTavern preset injection point)
    depth_prompt = extensions.get("depth_prompt", {})
    if depth_prompt:
        result["depth_prompt"] = {
            "prompt": depth_prompt.get("prompt", ""),
            "depth": depth_prompt.get("depth", 4),
            "role": depth_prompt.get("role", "system"),
        }
    else:
        result["depth_prompt"] = {}

    # SillyTavern-specific extensions
    st_ext = {}
    for key in ["talkativeness", "fav", "chat", "world"]:
        if key in extensions:
            st_ext[key] = extensions[key]
    if st_ext:
        result["st_extensions"] = st_ext

    return result


# ─── Image Saving ─────────────────────────────────────────────

def save_embedded_images(card_data: dict, output_dir: str):
    """Save embedded images to disk."""
    img_dir = os.path.join(output_dir, "embedded_images")
    saved = []

    for i, img in enumerate(card_data.get("embedded_images", [])):
        if not os.path.exists(img_dir):
            os.makedirs(img_dir)

        img_data = None
        ext = "png"
        name = img.get("name", f"image_{i}") if isinstance(img, dict) else f"image_{i}"

        if isinstance(img, dict):
            uri = img.get("uri", img.get("data", img.get("url", "")))
        elif isinstance(img, str):
            uri = img
        else:
            continue

        if not uri:
            continue

        if uri.startswith("data:image/"):
            header, b64data = uri.split(",", 1)
            if "png" in header:
                ext = "png"
            elif "jpeg" in header or "jpg" in header:
                ext = "jpg"
            elif "gif" in header:
                ext = "gif"
            elif "webp" in header:
                ext = "webp"
            img_data = base64.b64decode(b64data)
        elif uri.startswith("http"):
            saved.append({"name": name, "type": "url", "url": uri})
            continue
        else:
            try:
                img_data = base64.b64decode(uri)
            except Exception:
                continue

        if img_data:
            # Sanitize filename
            safe_name = "".join(c for c in name if c.isalnum() or c in "._- ")[:100]
            filename = f"{safe_name}.{ext}"
            filepath = os.path.join(img_dir, filename)
            with open(filepath, "wb") as f:
                f.write(img_data)
            saved.append({"name": name, "type": "file", "path": filepath})

    return saved


# ─── Main ─────────────────────────────────────────────────────

def detect_format(filepath: str) -> str:
    """Detect file format from magic bytes and extension."""
    ext = Path(filepath).suffix.lower()

    with open(filepath, "rb") as f:
        header = f.read(16)

    if header[:8] == b"\x89PNG\r\n\x1a\n":
        return "png"
    elif header[:4] == b"RIFF" and header[8:12] == b"WEBP":
        return "webp"
    elif header[:2] == b"\xff\xd8":
        return "jpeg"
    elif header[:1] == b"{":
        return "json"
    elif ext in (".webp",):
        return "webp"
    elif ext in (".jpg", ".jpeg"):
        return "jpeg"
    elif ext in (".json",):
        return "json"
    elif ext in (".png",):
        return "png"
    else:
        raise ValueError(f"Unsupported file format: {ext} (magic: {header[:8].hex()})")


def main():
    parser = argparse.ArgumentParser(description="Extract character card from image/JSON file")
    parser.add_argument("card_file", help="Path to the character card file (PNG/WEBP/JPEG/JSON)")
    parser.add_argument("--output-dir", "-o", default=None, help="Output directory (default: same as input)")
    args = parser.parse_args()

    filepath = os.path.expanduser(args.card_file)
    if not os.path.exists(filepath):
        print(f"Error: File not found: {filepath}", file=sys.stderr)
        sys.exit(1)

    output_dir = args.output_dir or os.path.dirname(filepath) or "."
    os.makedirs(output_dir, exist_ok=True)

    # Detect format and extract
    fmt = detect_format(filepath)
    print(f"Detected format: {fmt.upper()}")

    if fmt == "png":
        card = extract_from_png(filepath)
    elif fmt == "webp":
        card = extract_from_webp(filepath)
    elif fmt == "jpeg":
        card = extract_from_jpeg(filepath)
    elif fmt == "json":
        card = extract_from_json(filepath)
    else:
        print(f"Error: Unsupported format: {fmt}", file=sys.stderr)
        sys.exit(1)

    if not card:
        print("Error: Could not extract character card data.", file=sys.stderr)
        sys.exit(1)

    # Normalize
    normalized = normalize_card(card)

    # Summary
    enabled_wb = sum(1 for e in normalized["world_book"] if e.get("enabled", True))
    disabled_wb = sum(1 for e in normalized["world_book"] if not e.get("enabled", True))
    print(f"\n{'='*50}")
    print(f"  Character: {normalized['name']}")
    print(f"  Spec: {normalized['spec']} ({normalized['spec_version']})")
    print(f"  World book: {enabled_wb} enabled + {disabled_wb} disabled = {len(normalized['world_book'])} total")
    print(f"  Embedded images: {len(normalized['embedded_images'])}")
    print(f"  Assets: {len(normalized['assets'])}")
    print(f"  Regex scripts: {len(normalized['regex_scripts'])}")
    print(f"  Alternate greetings: {len(normalized['alternate_greetings'])}")
    print(f"  Has description: {'Yes' if normalized['description'] else 'No (check world book)'}")
    print(f"  Has system_prompt: {'Yes' if normalized['system_prompt'] else 'No'}")
    print(f"  Has post_history: {'Yes' if normalized['post_history_instructions'] else 'No'}")
    print(f"  Has depth_prompt: {'Yes (depth={normalized[\"depth_prompt\"].get(\"depth\", \"?\")})' if normalized.get('depth_prompt', {}).get('prompt') else 'No'}")
    print(f"{'='*50}")

    # Save embedded images
    saved_images = save_embedded_images(normalized, output_dir)
    if saved_images:
        print(f"Saved {len(saved_images)} embedded images")
        normalized["saved_images"] = saved_images

    # Clean output: remove raw binary data, keep everything else
    clean = {}
    for k, v in normalized.items():
        if k == "embedded_images":
            clean["embedded_image_count"] = len(v)
            # Keep URL references but strip base64 data
            clean["embedded_image_refs"] = []
            for img in v:
                if isinstance(img, dict):
                    ref = {kk: vv for kk, vv in img.items() if kk not in ("data", "uri") or (isinstance(vv, str) and vv.startswith("http"))}
                    clean["embedded_image_refs"].append(ref)
        elif k == "raw":
            # Keep raw but strip any large base64 blobs
            clean["raw_keys"] = list(v.keys()) if isinstance(v, dict) else str(type(v))
        else:
            clean[k] = v

    output_path = os.path.join(output_dir, "card_data.json")
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(clean, f, ensure_ascii=False, indent=2)

    print(f"\nSaved card data to: {output_path}")
    return normalized


if __name__ == "__main__":
    main()
