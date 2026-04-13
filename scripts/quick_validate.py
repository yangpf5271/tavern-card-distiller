#!/usr/bin/env python3
"""Validate a generated RP skill directory for completeness and correctness.

Checks:
- SKILL.md exists and contains required sections
- Frontmatter format (name must be hyphen-case)
- references/ directory with at least world_book.md
- chat_history/ directory exists
- user_profile.json exists
- assets/ directory exists

Usage:
    python3 quick_validate.py <skill_directory>

Exit codes:
    0 = all checks passed
    1 = warnings only
    2 = failures found
"""

import sys
import os
import re
import json
import argparse


class ValidationResult:
    def __init__(self):
        self.passes = []
        self.warnings = []
        self.failures = []

    def ok(self, msg):
        self.passes.append(msg)

    def warn(self, msg):
        self.warnings.append(msg)

    def fail(self, msg):
        self.failures.append(msg)

    def print_report(self):
        print("\n" + "=" * 50)
        print("  Skill 验证报告")
        print("=" * 50)

        if self.passes:
            print(f"\n  PASS ({len(self.passes)})")
            for msg in self.passes:
                print(f"    ✓ {msg}")

        if self.warnings:
            print(f"\n  WARN ({len(self.warnings)})")
            for msg in self.warnings:
                print(f"    ⚠ {msg}")

        if self.failures:
            print(f"\n  FAIL ({len(self.failures)})")
            for msg in self.failures:
                print(f"    ✗ {msg}")

        print("\n" + "-" * 50)
        total = len(self.passes) + len(self.warnings) + len(self.failures)
        if self.failures:
            print(f"  结果: FAIL ({len(self.failures)} failures, {len(self.warnings)} warnings, {len(self.passes)} passed / {total} total)")
        elif self.warnings:
            print(f"  结果: WARN ({len(self.warnings)} warnings, {len(self.passes)} passed / {total} total)")
        else:
            print(f"  结果: PASS (all {total} checks passed)")
        print("=" * 50)

    @property
    def exit_code(self):
        if self.failures:
            return 2
        if self.warnings:
            return 1
        return 0


def validate_skill(skill_dir: str) -> ValidationResult:
    r = ValidationResult()

    # 1. Directory exists
    if not os.path.isdir(skill_dir):
        r.fail(f"目录不存在: {skill_dir}")
        return r
    r.ok("Skill 目录存在")

    # 2. SKILL.md exists
    skill_md = os.path.join(skill_dir, "SKILL.md")
    if not os.path.isfile(skill_md):
        r.fail("SKILL.md 不存在")
        return r
    r.ok("SKILL.md 存在")

    # 3. Read and validate SKILL.md
    with open(skill_md, "r", encoding="utf-8") as f:
        content = f.read()

    # 3a. Frontmatter
    fm_match = re.match(r"^---\n(.*?)\n---", content, re.DOTALL)
    if not fm_match:
        r.fail("SKILL.md 缺少 YAML frontmatter")
    else:
        fm = fm_match.group(1)
        # name field
        name_match = re.search(r"^name:\s*(.+)$", fm, re.MULTILINE)
        if not name_match:
            r.fail("Frontmatter 缺少 name 字段")
        else:
            name = name_match.group(1).strip()
            if re.match(r"^[a-z0-9-]+$", name):
                r.ok(f"name 字段格式正确: {name}")
            else:
                r.warn(f"name 字段应为 hyphen-case: {name}")

        # description field
        if "description:" in fm:
            r.ok("Frontmatter 包含 description")
        else:
            r.warn("Frontmatter 缺少 description 字段")

    # 3b. Required sections in SKILL.md
    required_sections = [
        ("核心规则", "核心规则"),
        ("用户身份系统", "用户身份系统"),
        ("聊天历史系统", "聊天历史系统"),
        ("启动菜单", "启动菜单"),
        ("角色设定", "角色设定"),
        ("插图系统", "插图系统"),
        ("剧情建议系统", "剧情建议系统"),
        ("参考资料", "参考资料"),
    ]
    for section_id, section_name in required_sections:
        if section_id in content:
            r.ok(f"包含章节: {section_name}")
        else:
            r.warn(f"缺少章节: {section_name}")

    optional_sections = [
        ("状态系统", "状态系统"),
        ("写作风格", "写作风格指导"),
        ("默认开场白", "默认开场白"),
    ]
    for section_id, section_name in optional_sections:
        if section_id in content:
            r.ok(f"包含可选章节: {section_name}")

    # 4. user_profile.json
    profile = os.path.join(skill_dir, "user_profile.json")
    if os.path.isfile(profile):
        try:
            with open(profile, "r", encoding="utf-8") as f:
                data = json.load(f)
            if isinstance(data, dict):
                r.ok("user_profile.json 格式正确")
            else:
                r.warn("user_profile.json 不是 JSON 对象")
        except json.JSONDecodeError:
            r.warn("user_profile.json JSON 解析失败")
    else:
        r.warn("user_profile.json 不存在（首次使用时会创建）")

    # 4b. config.json
    config_path = os.path.join(skill_dir, "config.json")
    if os.path.isfile(config_path):
        try:
            with open(config_path, "r", encoding="utf-8") as f:
                cfg = json.load(f)
            if isinstance(cfg, dict) and "max_words" in cfg and "writing_style" in cfg:
                r.ok(f"config.json 格式正确 (max_words={cfg['max_words']}, style={cfg['writing_style']})")
            else:
                r.warn("config.json 缺少必要字段 (max_words / writing_style)")
        except json.JSONDecodeError:
            r.warn("config.json JSON 解析失败")
    else:
        r.warn("config.json 不存在（将使用默认值）")

    # 5. chat_history/ directory
    ch_dir = os.path.join(skill_dir, "chat_history")
    if os.path.isdir(ch_dir):
        r.ok("chat_history/ 目录存在")
        sessions = [f for f in os.listdir(ch_dir) if f.startswith("session_") and f.endswith(".md")]
        if sessions:
            r.ok(f"  包含 {len(sessions)} 个历史会话")
    else:
        r.warn("chat_history/ 目录不存在")

    # 6. references/ directory
    ref_dir = os.path.join(skill_dir, "references")
    if os.path.isdir(ref_dir):
        r.ok("references/ 目录存在")
        ref_files = os.listdir(ref_dir)
        if ref_files:
            for rf in sorted(ref_files):
                r.ok(f"  包含: {rf}")
        else:
            r.warn("references/ 目录为空")

        # world_book.md is the most important
        if "world_book.md" in ref_files:
            r.ok("  world_book.md 存在")
        else:
            r.warn("  缺少 world_book.md（角色设定可能不完整）")
    else:
        r.warn("references/ 目录不存在")

    # 7. assets/ directory
    assets_dir = os.path.join(skill_dir, "assets")
    if os.path.isdir(assets_dir):
        r.ok("assets/ 目录存在")
        img_dir = os.path.join(assets_dir, "embedded_images")
        if os.path.isdir(img_dir):
            imgs = os.listdir(img_dir)
            if imgs:
                r.ok(f"  包含 {len(imgs)} 张内置插图")
    else:
        r.ok("assets/ 目录不存在（无内置插图）")

    # 8. Check {{user}} placeholder handling
    if "user_profile.json" in content:
        r.ok("SKILL.md 引用了 user_profile.json（{{user}} 处理）")
    elif "{{user}}" in content:
        r.warn("SKILL.md 包含 {{user}} 但未引用 user_profile.json")

    return r


def main():
    parser = argparse.ArgumentParser(description="Validate RP skill directory")
    parser.add_argument("skill_dir", help="Path to the skill directory")
    args = parser.parse_args()

    skill_dir = os.path.expanduser(args.skill_dir)
    print(f"验证 Skill: {skill_dir}")

    result = validate_skill(skill_dir)
    result.print_report()
    sys.exit(result.exit_code)


if __name__ == "__main__":
    main()
