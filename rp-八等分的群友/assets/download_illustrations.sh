#!/bin/zsh
# Batch download illustrations from catbox.moe
# Uses a temp file for dedup instead of associative arrays

DEST="/Users/zhangleiandhim/.claude/skills/rp-八等分的群友/assets/illustrations"
mkdir -p "$DEST"
SEEN_FILE=$(mktemp)
SUCCESS=0
FAIL=0
SKIP=0

download() {
  local filename="$1"
  local hash="$2"
  local url="https://files.catbox.moe/${hash}.png"
  local outfile="${DEST}/${filename}"

  # Skip if already downloaded
  if [[ -f "$outfile" && -s "$outfile" ]]; then
    SKIP=$((SKIP + 1))
    return
  fi

  # Skip duplicate hashes
  if grep -q "^${hash}$" "$SEEN_FILE" 2>/dev/null; then
    SKIP=$((SKIP + 1))
    return
  fi
  echo "$hash" >> "$SEEN_FILE"

  curl -sL --max-time 30 -o "$outfile" "$url"
  if [[ -f "$outfile" && -s "$outfile" ]]; then
    SUCCESS=$((SUCCESS + 1))
    echo "OK: $filename"
  else
    FAIL=$((FAIL + 1))
    rm -f "$outfile"
    echo "FAIL: $filename ($url)"
  fi
}

# 神宫寺七海 (18)
download "神宫寺无人的教室wlkl8o.png" "wlkl8o"
download "神宫寺湿身qv73uy.png" "qv73uy"
download "神宫寺大腿4hn6wt.png" "4hn6wt"
download "神宫寺坐下1n26q4.png" "1n26q4"
download "神宫寺教室3cwenp.png" "3cwenp"
download "神宫寺走廊jmkihe.png" "jmkihe"
download "神宫寺站立做爱j424aa.png" "j424aa"
download "神宫寺站立做爱高潮b7nqsh.png" "b7nqsh"
download "神宫寺正常位做爱14zjaj.png" "14zjaj"
download "神宫寺正常位做爱高潮9g63bm.png" "9g63bm"
download "神宫寺口交pukb6.png" "pukb6"
download "神宫寺乳交口交q2vuqc.png" "q2vuqc"
download "神宫寺乳交ve304z.png" "ve304z"
download "神宫寺家中正常位做爱3ww80a.png" "3ww80a"
download "神宫寺家中做爱后2b24dn.png" "2b24dn"
download "神宫寺教室做爱后s1dznx.png" "s1dznx"
download "神宫寺教室正常位做爱kn2wzt.png" "kn2wzt"
download "神宫寺按捺不住441qa2.png" "441qa2"

# 和琪由希 (20)
download "和琪由希保健室坐py04h1.png" "py04h1"
download "和琪由希保健室内衣ebqsf3.png" "ebqsf3"
download "和琪由希家中qk4n4g.png" "qk4n4g"
download "和琪由希家中口交voc1ss.png" "voc1ss"
download "和琪由希保健室马脸口交0fj0tn.png" "0fj0tn"
download "和琪由希染发口交ne1qz6.png" "ne1qz6"
download "和琪由希家中脱鞋uwt1z5.png" "uwt1z5"
download "和琪由希家中内衣6kaf6b.png" "6kaf6b"
download "和琪由希保健室脱衣lxr3e4.png" "lxr3e4"
download "和琪由希染发乳交9byu73.png" "9byu73"
download "和琪由希抖S坐姿ck8u19.png" "ck8u19"
download "和琪由希保健室足交9htmyd.png" "9htmyd"
download "和琪由希脱鞋和丝袜p38nk3.png" "p38nk3"
download "和琪由希抬脚gg92b7.png" "gg92b7"
download "和琪由希闻脚g0zyxc.png" "g0zyxc"
download "和琪由希小穴摩擦n1m24d.png" "n1m24d"
download "射进和琪由希的鞋子vwtr2v.png" "vwtr2v"
download "和琪由希插入小穴msprgs.png" "msprgs"
download "和琪由希玩弄龟头pdbzur.png" "pdbzur"
download "和琪由希足交f0cxmg.png" "f0cxmg"

# 高坂樱月 (20)
download "高坂樱月巨乳cajz78.png" "cajz78"
download "高坂樱月邂逅qb31bo.png" "qb31bo"
download "高坂樱月主动搭讪qr00ye.png" "qr00ye"
download "高坂樱月汗湿g41es9.png" "g41es9"
download "高坂樱月脱掉内衣6nwedx.png" "6nwedx"
download "高坂樱月学校做爱后cjyczw.png" "cjyczw"
download "高坂樱月乳交7p7y4s.png" "7p7y4s"
download "高坂樱月乳交加口交nr8det.png" "nr8det"
download "高坂樱月乳交加口交射精dv18pl.png" "dv18pl"
download "高坂樱月站立做爱z2xmml.png" "z2xmml"
download "高坂樱月坐下xtxzz6.png" "xtxzz6"
download "高坂樱月不满bn7j7d.png" "bn7j7d"
download "高坂樱月诱惑4ojrz.png" "4ojrz"
download "高坂樱月按捺不住推倒xs73g6.png" "xs73g6"
download "高坂樱月走廊邂逅9h0chh.png" "9h0chh"
download "高坂樱月嫉妒09g9q0.png" "09g9q0"
download "高坂樱月湿身xbsl37.png" "xbsl37"
download "高坂樱月正常位做爱nkiiw9.png" "nkiiw9"
download "高坂樱月冷漠drt5ga.png" "drt5ga"

# 千紘蟾子 (15)
download "千紘蟾子湿身露出本性mtmgfz.png" "mtmgfz"
download "千紘蟾子坏笑解开衣服6fq27c.png" "6fq27c"
download "千紘蟾子湿身坐在椅子上坏笑5vyk10.png" "5vyk10"
download "千紘蟾子被霸凌后cehdul.png" "cehdul"
download "千紘蟾子被霸凌后二lujshv.png" "lujshv"
download "千紘蟾子纽扣崩开8fokxp.png" "8fokxp"
download "千紘蟾子向老师告状e0cusf.png" "e0cusf"
download "千紘蟾子哭泣tprsxc.png" "tprsxc"
download "千紘蟾子被安慰2gr8kz.png" "2gr8kz"
download "千紘蟾子换丝袜gyd5lo.png" "gyd5lo"
download "千紘蟾子教室托腮jnu4g5.png" "jnu4g5"
download "千紘蟾子教室不耐烦9zi0ys.png" "9zi0ys"
download "千紘蟾子离开教室bg41gh.png" "bg41gh"
download "千紘蟾子长发sfqq99.png" "sfqq99"
download "千紘蟾子长发坐在椅子上害羞4fp3j9.png" "4fp3j9"

# 美铃 (29)
download "美铃家中玩弄龟头c8b6uq.png" "c8b6uq"
download "美铃家中黑丝足交51nw7k.png" "51nw7k"
download "美铃家中裸足足交dc936v.png" "dc936v"
download "美铃家中裸足玩弄射精8fmug5.png" "8fmug5"
download "美铃家中吞下精液4vprk5.png" "4vprk5"
download "美铃淫靡口交wejw4m.png" "wejw4m"
download "美铃乳交口交结束后z6hz0y.png" "z6hz0y"
download "美铃乳交口交bwhtwq.png" "bwhtwq"
download "美铃乳交口交射精28kmmg.png" "28kmmg"
download "美铃口交结束后gv7wn5.png" "gv7wn5"
download "美铃家中口交itucaf.png" "itucaf"
download "美铃家中口交射精v5gqja.png" "v5gqja"
download "美铃学校看腋下e8xwig.png" "e8xwig"
download "美铃SNS自拍8chqqt.png" "8chqqt"
download "美铃泳池泳衣5t5l5c.png" "5t5l5c"
download "美铃露出腋下27njjc.png" "27njjc"
download "美铃奔跑oi98p3.png" "oi98p3"
download "美铃吐舌头自拍kjlhlm.png" "kjlhlm"
download "美铃教训学生puk3dd.png" "puk3dd"
download "美铃给你看胸部2cfjcv.png" "2cfjcv"
download "美铃追逐yrql4v.png" "yrql4v"
download "美铃私密空间裸体1v0lof.png" "1v0lof"
download "美铃帅气kx2lzu.png" "kx2lzu"
download "美铃给你看内衣lrzkjv.png" "lrzkjv"
download "美铃穿学生制服1v0e7y.png" "1v0e7y"
download "美铃教室独处txb0cm.png" "txb0cm"
download "美铃家中开门mn0iw4.png" "mn0iw4"
download "美铃家中拥抱k74f16.png" "k74f16"
download "美铃上班wsxe2z.png" "wsxe2z"

# 后藤冬 (28)
download "后藤冬训练fmh67u.png" "fmh67u"
download "后藤冬放学偶遇2encyj.png" "2encyj"
download "后藤冬休息室ofkdkh.png" "ofkdkh"
download "后藤冬大街躲雨fb8imr.png" "fb8imr"
download "后藤冬大街雨停wo7osq.png" "wo7osq"
download "后藤冬天台ovdeio.png" "ovdeio"
download "后藤冬背心lmv8r9.png" "lmv8r9"
download "后藤冬学生运动服xfgoxj.png" "xfgoxj"
download "后藤冬家中rd8mqo.png" "rd8mqo"
download "后藤冬雨天偶遇azjesb.png" "azjesb"
download "后藤冬大街跑步结束ut2hxe.png" "ut2hxe"
download "后藤冬大街跑步ekzbw0.png" "ekzbw0"
download "后藤冬大街训练b39fwa.png" "b39fwa"
download "后藤冬小巷追逐7b5dtq.png" "7b5dtq"
download "后藤冬马拉松夜间fnss29.png" "fnss29"
download "后藤冬大街马拉松z87zhi.png" "z87zhi"
download "后藤冬训练时被打扰tgc54c.png" "tgc54c"
download "后藤冬微笑y1nyt8.png" "y1nyt8"
download "后藤冬被老师训斥3qg273.png" "3qg273"
download "后藤冬家中看腋下0beasc.png" "0beasc"
download "后藤冬大街惊讶00ut7g.png" "00ut7g"
download "后藤冬家中独处yyt7bd.png" "yyt7bd"
download "后藤冬感兴趣wxfay3.png" "wxfay3"
download "后藤冬家中害羞h5syvf.png" "h5syvf"
download "后藤冬比赛结束lrpt8p.png" "lrpt8p"
download "后藤冬室内训练z98ldv.png" "z98ldv"
download "后藤冬和你赛跑od9w2j.png" "od9w2j"
download "后藤冬操场偶遇hl1zi4.png" "hl1zi4"

# 爱丽丝 (23)
download "掐爱丽丝的脖子m9ic1m.png" "m9ic1m"
download "爱丽丝半裸9dlxsu.png" "9dlxsu"
download "爱丽丝担心3szv2w.png" "3szv2w"
download "爱丽丝给你看黑丝脚76yt3h.png" "76yt3h"
download "爱丽丝做爱后偷拍gi6ed8.png" "gi6ed8"
download "爱丽丝家中给你看脚6avo81.png" "6avo81"
download "爱丽丝教室给你看白丝脚1sxtjs.png" "1sxtjs"
download "爱丽丝保健室给你看脚tvvu1c.png" "tvvu1c"
download "爱丽丝准备做爱60vg7i.png" "60vg7i"
download "爱丽丝淫靡泳衣pp45im.png" "pp45im"
download "爱丽丝露出小穴930p8s.png" "930p8s"
download "爱丽丝坐在床上sqf89z.png" "sqf89z"
download "爱丽丝女上位做爱ptnfk7.png" "ptnfk7"
download "爱丽丝女上位做爱高潮gotqro.png" "gotqro"
download "爱丽丝支配puae1h.png" "puae1h"
download "爱丽丝微笑u9o7i3.png" "u9o7i3"
download "爱丽丝生气6s7nsg.png" "6s7nsg"
download "爱丽丝背对你yqucit.png" "yqucit"
download "爱丽丝难过ni2yjb.png" "ni2yjb"
download "爱丽丝大街偶遇ebepz9.png" "ebepz9"
download "爱丽丝夜晚约会t6cvau.png" "t6cvau"
download "爱丽丝坏笑d7p3j7.png" "d7p3j7"
download "爱丽丝坏笑诱惑7mxsnb.png" "7mxsnb"

# 豆咪 (9)
download "豆咪巨大黄豆形态ipwenm.png" "ipwenm"
download "娇小豆咪形态nw04ee.png" "nw04ee"
download "豆咪娇小猫娘形态v5f1qp.png" "v5f1qp"
download "豆咪娇小猫娘形态捏耳朵ff1ug1.png" "ff1ug1"
download "豆咪巨大猫娘形态i9929e.png" "i9929e"
download "豆咪猫娘形态无聊zh8fkl.png" "zh8fkl"
download "豆咪巨大猫娘形态聊天xanen0.png" "xanen0"
download "豆咪巨大猫娘微笑114gy4.png" "114gy4"
download "豆咪巨大猫娘形态聆听wgdctf.png" "wgdctf"

rm -f "$SEEN_FILE"

echo ""
echo "===== Download Complete ====="
echo "Success: $SUCCESS"
echo "Failed: $FAIL"
echo "Skipped (duplicate/existing): $SKIP"
echo "Total unique attempted: $((SUCCESS + FAIL))"
