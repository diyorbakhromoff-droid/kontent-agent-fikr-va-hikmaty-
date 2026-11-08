import sys, math, random; sys.path.insert(0,'/home/claude')
import cta as C
exec(open('/home/claude/build4.py').read().split('# ---------- reel004 ----------')[0].split('import cta as C')[1])
C.SCENE_S='85.25'
FONTS=''.join(f"@font-face{{font-family:Corm;font-weight:{w};font-style:{st};src:url(fonts/cormorant-garamond-latin-{w}-{st}.woff2)}}" for w in (500,600,700) for st in ('normal','italic'))
FONTS+="@font-face{font-family:Corm;font-weight:600;src:url(fonts/cormorant-garamond-latin-ext-600-normal.woff2);unicode-range:U+0100-024F}"
FONTS+="@font-face{font-family:Corm;font-weight:600;font-style:italic;src:url(fonts/cormorant-garamond-latin-ext-600-italic.woff2);unicode-range:U+0100-024F}"
FONTS+=''.join(f"@font-face{{font-family:Mont;font-weight:{w};src:url(fonts/montserrat-latin-{w}-normal.woff2)}}" for w in (500,600,700,800))
FONTS+="@font-face{font-family:Ruqaa;font-weight:700;src:url(fonts/aref-ruqaa-arabic-700-normal.woff2)}"
CSS=FONTS+'''
:root{--terra:#E9C772;--ivory:#F3E7CF;--goldA:#F8E3A6;--goldB:#C9A24E}
html,body{background:#05060A}
#stage{color:var(--ivory)}
#fx{position:absolute;inset:0}
.grain{opacity:.07;mix-blend-mode:screen}.grain2{opacity:.05;mix-blend-mode:screen}
.vign{background:radial-gradient(ellipse at 50% 45%,rgba(0,0,0,0) 45%,rgba(0,0,0,.55) 100%)}
.g{background:linear-gradient(180deg,#FFF1C4 0%,#E9C772 45%,#B48A3C 100%);-webkit-background-clip:text;background-clip:text;color:transparent}
.glow{filter:drop-shadow(0 0 18px rgba(233,199,114,.45)) drop-shadow(0 0 2px rgba(255,240,200,.6))}
.h{font-family:Corm;font-weight:600;line-height:1.02;letter-spacing:-.5px}
.it{font-family:Corm;font-style:italic;font-weight:600}
.cap{font:600 25px/1 Mont;letter-spacing:.42em;text-transform:uppercase;color:#C9A45C;white-space:nowrap}
.mont{font-family:Mont;font-weight:600}
.glass{background:linear-gradient(160deg,rgba(255,255,255,.075),rgba(255,255,255,.02));border:1.5px solid rgba(212,175,95,.38);border-radius:26px;box-shadow:0 30px 60px rgba(0,0,0,.45),inset 0 1px 0 rgba(255,255,255,.08)}
.frame{position:relative;padding:46px 46px 42px;text-align:center}
.frame:before{content:"";position:absolute;inset:12px;border:1px solid rgba(212,175,95,.28);border-radius:18px;pointer-events:none}
.dia{position:absolute;width:16px;height:16px;background:#E9C772;transform:rotate(45deg);box-shadow:0 0 14px rgba(233,199,114,.8)}
.rule{display:flex;align-items:center;gap:18px;justify-content:center}
.rule i{display:block;height:1.5px;width:120px;background:linear-gradient(90deg,transparent,#C9A45C)}
.rule i:last-child{background:linear-gradient(90deg,#C9A45C,transparent)}
.rule b{display:block;width:10px;height:10px;background:#E9C772;transform:rotate(45deg)}
.arabic{font-family:Amiri;font-weight:700;direction:rtl}
.ruq{font-family:Ruqaa;font-weight:700;direction:rtl}
.rv{color:rgba(243,231,207,.22)} .rv.on{color:var(--ivory)} .rv.t-terra.on{color:#E9C772}
.t-terra{color:#E9C772}
.serif{font-family:Corm;font-weight:600}
#banner{background:none;box-shadow:none;color:#C9A45C;font:600 22px/1 Mont;letter-spacing:.36em;text-transform:uppercase;padding:10px 0;border-top:1px solid rgba(212,175,95,.45);border-bottom:1px solid rgba(212,175,95,.45);top:140px}
#sub{top:1520px}
#subbox{background:rgba(6,7,12,.62);border:1px solid rgba(212,175,95,.28);border-radius:16px;box-shadow:0 18px 40px rgba(0,0,0,.4);font:600 40px/1.15 Mont;padding:18px 30px}
#subbox:before{display:none}
#subbox span{color:var(--ivory)} #subbox span.up{color:rgba(243,231,207,.32)} #subbox span.cur{color:#E9C772}
.chip{background:linear-gradient(160deg,rgba(255,255,255,.08),rgba(255,255,255,.02));color:var(--ivory);border:1.5px solid rgba(212,175,95,.4);box-shadow:0 20px 40px rgba(0,0,0,.4);font-family:Mont;font-weight:600}
.hand{font-family:Corm;font-style:italic;font-weight:600}
.x{display:inline-block;color:#E0705E;font-weight:700}
.bar{height:12px;border-radius:8px;transform-origin:left center;position:relative}
.bar:after{content:"";position:absolute;right:-9px;top:-6px;width:24px;height:24px;border-radius:50%;background:inherit;box-shadow:0 0 22px 4px currentColor}
.rays{position:absolute;left:50%;top:50%;width:2600px;height:2600px;margin:-1300px 0 0 -1300px;background:repeating-conic-gradient(from 0deg,rgba(233,199,114,.06) 0 4deg,rgba(0,0,0,0) 4deg 15deg);-webkit-mask:radial-gradient(circle,#000 0,transparent 60%);mask:radial-gradient(circle,#000 0,transparent 60%)}
'''
HEAD=f'''<!doctype html><html><head><meta charset="utf-8"><link rel="stylesheet" href="style.css"><script src="words.js"></script><script src="engine.js"></script><style>{CSS}</style></head><body><div id="stage">'''
BG='<canvas id="fx" width="1080" height="1920"></canvas><div id="star" style="position:absolute;left:50%;top:46%;width:1500px;height:1500px;margin:-750px 0 0 -750px;opacity:.07"><svg viewBox="0 0 200 200" width="1500" height="1500"><g fill="none" stroke="#E9C772" stroke-width=".5"><rect x="45" y="45" width="110" height="110"/><rect x="45" y="45" width="110" height="110" transform="rotate(45 100 100)"/><circle cx="100" cy="100" r="36"/><circle cx="100" cy="100" r="78"/><rect x="62" y="62" width="76" height="76" transform="rotate(22.5 100 100)"/><rect x="62" y="62" width="76" height="76" transform="rotate(67.5 100 100)"/></g></svg></div><div class="grain"></div><div class="grain2"></div><div class="vign"></div>'
def rule(t,top,o=''):
    oo=f' data-o="{o}"' if o else ''
    return f'<div class="a cx rule" data-t="{t}" data-a="blur"{oo} style="top:{top}px"><i></i><b></b><i></i></div>'
def kw(words,size,top,extra='',o=''):
    sp=' '.join(f'<span class="a{" g glow" if g else ""}" data-t="{t}" data-a="blur" style="position:relative;display:inline-block">{w}</span>' for w,t,g in words)
    oo=f' data-o="{o}"' if o else ''
    return f'<div class="a cx h" data-t="0" data-a="none"{oo} style="top:{top}px;width:980px;text-align:center;font-size:{size}px;{extra}">{sp}</div>'
def card(t,label,arab,trans,top,asz=58,tsz=50,o=''):
    oo=f' data-o="{o}"' if o else ''
    return f'''<div class="a cx" data-t="{t}" data-a="rise"{oo} style="top:{top}px"><div class="glass frame" style="width:940px">
 <div class="dia" style="left:-8px;top:50%;margin-top:-8px"></div><div class="dia" style="right:-8px;top:50%;margin-top:-8px"></div>
 <div class="cap">{label}</div>
 <div class="arabic g" style="font-size:{asz}px;line-height:1.9;margin-top:22px">{arab}</div>
 <div class="rule" style="margin:8px 0 14px"><i style="width:80px"></i><b></b><i style="width:80px"></i></div>
 <div class="h" style="font-size:{tsz}px;line-height:1.18">{trans}</div></div></div>'''
moon='<svg width="{s}" height="{s}" viewBox="0 0 60 60"><path d="M34 4a26 26 0 1 0 22 40A22 22 0 1 1 34 4z" fill="url(#mg)" /></svg>'
ring=''
for i in range(12):
    a=-math.pi/2+i*2*math.pi/12; x=540+300*math.cos(a)-38; y=640+300*math.sin(a)-38
    ring+=f'<div class="a glow" data-t="{57.1+i*0.07:.2f}" data-a="zoom" data-d=".45" style="left:{x:.0f}px;top:{y:.0f}px">{moon.format(s=76)}</div>'
def brow(t,name,n,w,col,top,dim=False):
    op='opacity:.42;' if dim else ''
    return f'''<div class="a" data-t="{t}" data-a="rise" style="left:40px;top:{top}px;{op}display:flex;align-items:center;gap:26px">
 <div class="h" style="width:300px;font-size:54px;text-align:right;white-space:nowrap">{name}</div>
 <div class="bar gw" data-t="{t+.1}" data-d=".9" style="width:{w}px;background:{col};color:{col}"></div>
 <div class="h count g" data-t="{t+.1}" data-d=".9" data-from="0" data-to="{n}" style="font-size:78px;margin-left:14px">0</div></div>'''
TX='style="font:600 34px Mont;letter-spacing:.3em;fill:#F3E7CF"'
def pan(pid,name,ar,tn,tc):
    return f'''<g id="{pid}"><path class="dr" data-t="{tn-.4}" data-d=".6" d="M0 0L-112 170M0 0L112 170" stroke="#C9A45C" stroke-width="2.5" fill="none"/>
 <path class="dr" data-t="{tn-.1}" data-d=".6" d="M-140 170Q0 250 140 170Z" stroke="#E9C772" stroke-width="3.5" fill="rgba(233,199,114,.08)"/>
 <text class="sv" data-t="{tn}" x="0" y="310" text-anchor="middle" {TX}>{name}</text>
 <text class="sv" data-t="{tn+.1}" x="0" y="392" text-anchor="middle" style="font:700 66px Ruqaa;fill:#E9C772">{ar}</text>
 <text class="sv count" data-t="{tc}" data-d="1.1" data-from="0" data-to="115" x="0" y="520" text-anchor="middle" fill="url(#gg)" style="font:600 150px Corm;filter:drop-shadow(0 0 14px rgba(233,199,114,.5))">0</text></g>'''
scale=f'''<svg width="900" height="675" viewBox="0 0 800 600" style="overflow:visible">
<defs><linearGradient id="gg" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#FFF1C4"/><stop offset=".5" stop-color="#E9C772"/><stop offset="1" stop-color="#B48A3C"/></linearGradient></defs>
<path class="dr" data-t="16.5" data-d=".7" d="M400 150V545" stroke="#E9C772" stroke-width="5" fill="none"/>
<path class="dr" data-t="16.7" data-d=".7" d="M270 560H530M310 545H490" stroke="#E9C772" stroke-width="5" fill="none" stroke-linecap="round"/>
<g id="beam"><path class="dr" data-t="16.8" data-d=".7" d="M100 140H700" stroke="#F3D98E" stroke-width="6" fill="none" stroke-linecap="round"/></g>
<circle id="rip" cx="400" cy="140" r="20" fill="none" stroke="#E9C772" stroke-width="3" opacity="0"/>
<circle class="dr" data-t="16.9" data-d=".4" cx="400" cy="140" r="16" fill="#05060A" stroke="#E9C772" stroke-width="5"/>
{pan('panL','DUNYO','الدنيا',16.6,17.5)}{pan('panR','OXIRAT','الآخرة',19.4,20.45)}
</svg>'''
s=f'''
<svg width="0" height="0" style="position:absolute"><defs><linearGradient id="mg" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#FFF1C4"/><stop offset="1" stop-color="#C9A24E"/></linearGradient></defs></svg>
<div id="banner" data-s="9.6" data-e="85.0">Qur’on shifrlari · tarozidagi so‘zlar</div>
<section class="scene" data-s="-1" data-e="9.55">
 <div id="tex" class="arabic" style="position:absolute;inset:0;opacity:.09;font-size:46px;line-height:96px;color:#E9C772;white-space:nowrap;overflow:hidden;padding-top:40px">{'<br>'.join(['بِسْمِ اللَّهِ الرَّحْمَٰنِ الرَّحِيمِ ۝ الْحَمْدُ لِلَّهِ رَبِّ الْعَالَمِينَ ۝ الرَّحْمَٰنِ الرَّحِيمِ ۝ مَالِكِ يَوْمِ الدِّينِ ۝ إِيَّاكَ نَعْبُدُ']*20)}</div>
 <div id="scan" style="position:absolute;left:0;width:1080px;height:220px;top:-300px;background:linear-gradient(180deg,rgba(233,199,114,0),rgba(233,199,114,.16) 48%,rgba(255,240,200,.55) 50%,rgba(233,199,114,.16) 52%,rgba(233,199,114,0));mix-blend-mode:screen"></div>
 <div class="a cx cap" data-t="0.05" data-a="wide" data-ls=".42" style="top:300px">Qur’on shifrlari · III</div>
 {rule(0.3,350)}
 {kw([('Qur’ondagi',0.07,False),('har',0.72,True),('bir',1.04,True),('so‘z',1.2,True)],100,430)}
 {kw([('sanab',1.6,False),('chiqildi',1.88,False)],100,545)}
 <div class="a cx cap" data-t="2.8" data-a="blur" style="top:760px;color:#9C8E74">Natija</div>
 <div class="a cx it g glow" data-t="3.28" data-a="blur" data-d=".7" style="top:800px;font-size:96px;white-space:nowrap">hayratlanarli</div>
 <div class="a cx" data-t="5.6" data-a="none" style="top:960px"><svg width="300" height="200" viewBox="0 0 300 200"><g fill="none" stroke="#E9C772" stroke-width="3" stroke-linecap="round"><path class="dr" data-t="5.6" data-d=".5" d="M150 20V180M100 186H200"/><path class="dr" data-t="5.9" data-d=".5" d="M40 40H260"/><path class="dr" data-t="6.2" data-d=".5" d="M40 40L10 110M40 40L70 110M0 110Q40 140 80 110M260 40L230 110M260 40L290 110M220 110Q260 140 300 110"/></g></svg></div>
 <div class="a cx h g glow" data-t="7.36" data-a="zoom" data-d=".6" style="top:1190px;font-size:120px;white-space:nowrap">aynan bir xil</div>
</section>
<section class="scene" data-s="9.55" data-e="16.45">
 <div class="a cx h g glow count" data-t="9.65" data-d="2.0" data-from="0" data-to="6236" style="top:250px;font-size:250px;line-height:1">0</div>
 <div class="a cx cap" data-t="9.9" data-a="wide" data-ls=".42" style="top:520px">oyat</div>
 <canvas id="grid" width="900" height="720" style="position:absolute;left:90px;top:610px"></canvas>
 <div class="a cx it" data-t="12.2" data-a="blur" style="top:1355px;font-size:60px;white-space:nowrap">butun Qur’on — <span class="g">bitta ekranda</span></div>
 <div class="a cx" data-t="14.75" data-a="zoom" data-o="16.3" style="top:1010px"><div class="glass mont" style="padding:20px 34px;font-size:40px;white-space:nowrap;background:rgba(5,6,10,.8)">1 nuqta <span class="g">=</span> 1 oyat</div></div>
</section>
<section class="scene" data-s="16.45" data-e="24.05">
 <div class="a cx" data-t="16.5" data-a="none" style="top:290px">{scale}</div>
 <div class="a cx h g glow" data-t="21.9" data-a="zoom" data-d=".55" style="top:1060px;font-size:130px;white-space:nowrap">115 = 115</div>
 <div class="a cx it" data-t="22.6" data-a="blur" style="top:1230px;font-size:60px;white-space:nowrap">tarozi to‘liq muvozanatda</div>
</section>
<section class="scene" data-s="24.05" data-e="32.55">
 <div class="a cx cap" data-t="24.1" data-a="wide" data-ls=".42" style="top:290px">Alloh Payg‘ambarimizga</div>
 {rule(24.3,340)}
 <svg class="a" data-t="31.7" data-a="none" style="left:0;top:600px" width="1080" height="200"><path class="dr" data-t="31.7" data-d=".5" d="M500 100H580" stroke="#E9C772" stroke-width="3"/></svg>
 <div class="a" data-t="25.45" data-a="rise" style="left:70px;top:420px"><div class="glass" style="width:440px;height:560px;display:flex;flex-direction:column;align-items:center;justify-content:center;gap:6px">
  <div class="ruq g glow" style="font-size:150px;line-height:1.1">قل</div><div class="it" style="font-size:66px">«Ayt!»</div>
  <div class="h g count" data-t="26.24" data-d="1.2" data-from="0" data-to="332" style="font-size:170px;line-height:1">0</div><div class="cap" style="font-size:22px">marta</div></div></div>
 <div class="a" data-t="29.25" data-a="rise" style="left:570px;top:420px"><div class="glass" style="width:440px;height:560px;display:flex;flex-direction:column;align-items:center;justify-content:center;gap:6px">
  <div class="ruq g glow" style="font-size:150px;line-height:1.1">قالوا</div><div class="it" style="font-size:66px">«Dedilar»</div>
  <div class="h g count" data-t="30.9" data-d="1.2" data-from="0" data-to="332" style="font-size:170px;line-height:1">0</div><div class="cap" style="font-size:22px">marta</div></div></div>
 <div class="a cx" data-t="31.85" data-a="zoom" style="top:640px"><div style="width:120px;height:120px;border-radius:50%;background:#05060A;border:3px solid #E9C772;box-shadow:0 0 40px rgba(233,199,114,.6);display:flex;align-items:center;justify-content:center"><span class="h g" style="font-size:96px;line-height:1">=</span></div></div>
 <div class="a cx it" data-t="28.4" data-a="blur" style="top:1050px;font-size:56px;white-space:nowrap;color:#BFAF90">buyruq va javob</div>
</section>
<section class="scene" data-s="32.55" data-e="44.15">
 <div class="a cx it" data-t="32.6" data-a="blur" style="top:270px;font-size:66px;white-space:nowrap">Eng ko‘p tilga olingan <span class="g">payg‘ambarlar</span></div>
 {rule(32.9,370)}
 {brow(34.45,'Muso a.s.',136,440,'#E9C772',440)}
 {brow(36.5,'Ibrohim a.s.',69,223,'#BFAF90',565,True)}
 {brow(36.9,'Nuh a.s.',43,139,'#BFAF90',690,True)}
 {brow(37.55,'Iso a.s.',25,81,'#6FE0B8',815)}
 {brow(39.9,'Odam a.s.',25,81,'#6FE0B8',940)}
 <svg class="a" data-t="42.2" data-a="none" style="left:620px;top:820px" width="60" height="230"><path class="dr" data-t="42.2" data-d=".45" d="M4 10H30V220H4" fill="none" stroke="#6FE0B8" stroke-width="3"/></svg>
 <div class="a" data-t="42.4" data-a="blur" style="left:690px;top:880px"><div class="glass h" style="padding:14px 30px;font-size:64px;white-space:nowrap;color:#6FE0B8;border-color:rgba(111,224,184,.5)">25 = 25</div></div>
 <div class="a cx it g glow" data-t="43.0" data-a="zoom" data-d=".6" style="top:1160px;font-size:140px;white-space:nowrap">Tasodifmi?</div>
</section>
<section class="scene" data-s="44.15" data-e="55.3">
 {card(44.2,'Oli Imron surasi · 59-oyat','إِنَّ مَثَلَ عِيسَىٰ عِندَ اللَّهِ كَمَثَلِ آدَمَ',rv([('«Alloh',46.34),('huzurida',46.64),('Isoning',47.36,'t-terra'),('misoli',48.04),('Odamning',48.64,'t-terra'),('misoli',49.24),('kabidir»',49.56)]),270,64,56)}
 <div class="a" data-t="50.44" data-a="rise" style="left:110px;top:800px;display:flex;align-items:baseline;gap:24px"><div class="h" style="font-size:62px;white-space:nowrap">Odam a.s.</div><div class="mont" style="font-size:38px;color:#BFAF90;white-space:nowrap">ota <span class="a x" data-t="51.2" data-a="zoom" data-d=".3" style="position:relative">✕</span> &nbsp;ona <span class="a x" data-t="52.08" data-a="zoom" data-d=".3" style="position:relative">✕</span></div></div>
 <div class="a" data-t="53.2" data-a="rise" style="left:110px;top:920px;display:flex;align-items:baseline;gap:24px"><div class="h" style="font-size:62px;white-space:nowrap">Iso a.s.</div><div class="mont" style="font-size:38px;color:#BFAF90;white-space:nowrap">ota <span class="a x" data-t="54.08" data-a="zoom" data-d=".3" style="position:relative">✕</span></div></div>
 <div class="a cx it g glow" data-t="54.4" data-a="blur" style="top:1090px;font-size:64px;white-space:nowrap">ikkisi ham — mo‘jizaviy yaratilish</div>
</section>
<section class="scene" data-s="55.3" data-e="62.93">
 <svg class="a" data-t="55.35" data-a="none" style="left:0;top:100px" width="1080" height="1080"><circle class="dr" data-t="55.4" data-d="1.4" cx="540" cy="540" r="300" fill="none" stroke="rgba(233,199,114,.45)" stroke-width="2" transform="rotate(-90 540 540)"/><circle class="dr" data-t="55.6" data-d="1.4" cx="540" cy="540" r="225" fill="none" stroke="rgba(233,199,114,.18)" stroke-width="1.5"/></svg>
 {ring}
 <div class="a cx" data-t="55.35" data-a="blur" style="top:470px;text-align:center"><div class="cap">«Oy» · <span class="ruq" style="font-size:44px;letter-spacing:0;color:#E9C772">شهر</span></div></div>
 <div class="a cx h g glow count" data-t="57.1" data-d=".9" data-from="0" data-to="12" style="top:530px;font-size:230px;line-height:1">0</div>
 <div class="a cx cap" data-t="56.0" data-a="blur" style="top:780px;font-size:20px;color:#9C8E74">birlik shaklda</div>
 {card(58.2,'Tavba surasi · 36-oyat','إِنَّ عِدَّةَ الشُّهُورِ عِندَ اللَّهِ اثْنَا عَشَرَ شَهْرًا',rv([('«Alloh',59.78),('huzurida',60.04),('oylarning',60.8),('soni',61.36),('o‘n',61.84,'t-terra'),('ikkitadir»',62.0,'t-terra')]),1000,52,50)}
</section>
<section class="scene" data-s="62.93" data-e="76.92">
 <div class="rays" id="rays1"></div>
 {kw([('Bu',62.98,False),('raqamlar',63.16,False),('—',63.5,False),('Qur’onning',63.81,False),('yagona',64.4,True),('mo‘jizasi',64.88,False),('emas',65.56,False)],96,360,'line-height:1.08','67.95')}
 <div class="a cx it g glow" data-t="66.05" data-a="blur" data-o="67.95" style="top:690px;font-size:70px;white-space:nowrap">lekin ular o‘ylashga chaqiradi</div>
 <div class="a cx mont" data-t="64.0" data-a="blur" data-o="67.95" style="top:1180px;width:880px;text-align:center;font-size:24px;line-height:1.5;color:#8E8370;letter-spacing:.04em">* Sanoq so‘zning qaysi shakli hisoblanishiga qarab farq qilishi mumkin. Manba: Quranic Arabic Corpus</div>
 {card(68.1,'Niso surasi · 82-oyat','أَفَلَا يَتَدَبَّرُونَ الْقُرْآنَ ۚ وَلَوْ كَانَ مِنْ عِندِ غَيْرِ اللَّهِ لَوَجَدُوا فِيهِ اخْتِلَافًا كَثِيرًا',rv([('«Qur’on',69.26),('haqida',69.64),('o‘ylab',70.03,'t-terra'),('ko‘rmaydilarmi?',70.36,'t-terra'),('Agar',71.64),('u',71.92),('Allohdan',72.16),('boshqa',72.72),('tomondan',73.12),('bo‘lganida,',73.52),('unda',74.6),('ko‘p',74.88),('ziddiyat',75.12,'t-terra'),('topgan',75.6),('bo‘lardilar»',75.96)]),300,52,50)}
</section>
<section class="scene" data-s="76.92" data-e="85.25">
 <div class="a cx it" data-t="76.97" data-a="blur" style="top:250px;font-size:84px;white-space:nowrap">Sizningcha, <span class="g">qaysi biri?</span></div>
 {rule(77.3,370)}
'''
tiles=[(79.56,85,450,'115','dunyo = oxirat'),(80.64,555,450,'332','«ayt» = «dedilar»'),(81.89,85,800,'25','Iso = Odam'),(83.12,555,800,'12','oylar soni')]
for t,x,y,n,cpt in tiles:
    s+=f'<div class="a" data-t="{t}" data-a="zoom" data-d=".5" style="left:{x}px;top:{y}px"><div class="glass" style="width:440px;height:310px;display:flex;flex-direction:column;align-items:center;justify-content:center"><div class="h g glow" style="font-size:150px;line-height:1">{n}</div><div class="cap" style="font-size:20px;letter-spacing:.25em;margin-top:10px;color:#BFAF90">{cpt}</div></div></div>\n'
s+='''<div class="a cx" data-t="83.96" data-a="rise" style="top:1180px"><div class="glass mont" style="padding:20px 38px;font-size:40px;white-space:nowrap">💬 Izohlarda yozing</div></div>
</section>
'''
extra=f'''<div class="a cx it g glow" data-t="85.3" data-a="blur" data-o="91.6" style="top:290px;font-size:64px;white-space:nowrap">Har kuni — birgalikda</div>
<div class="a cx" data-t="91.7" data-a="rise" style="top:290px;display:flex;gap:22px"><div class="chip" style="font-size:36px">📌 Saqlab qo‘ying</div><div class="a chip" data-t="92.5" data-a="rise" style="position:relative;font-size:36px">📤 Yaqiningizga yuboring</div></div>
<div class="a cx" data-t="88.85" data-a="zoom" style="top:1220px"><div class="chip" style="font-size:38px;white-space:nowrap;border:2px solid #E9C772">💬 Izohlarga <span class="g" style="font-size:54px">«+»</span> qoldiring</div></div>
<div class="a hand cx" data-t="90.4" data-a="blur" style="top:1330px;font-size:46px;color:#9C8E74">yoki</div>
'''
c=C.cta(tas=85.4,zikr=87.25,extra=extra,havola=90.75,btn=91.9)
c=c.replace('style="top:1250px"><div class="chip"','style="top:1395px"><div class="chip"').replace('style="top:1400px"><div style="background:var(--gold)','style="top:1520px"><div style="background:var(--gold)').replace('top:1560px;font:700','top:1680px;font:700')
c=c.replace('style="top:1070px"><div style="background:var(--terra);color:#fff;font:900 84px Fraunces;padding:22px 46px;border-radius:8px;white-space:nowrap;box-shadow:0 12px 26px rgba(150,60,40,.25)">ZIKR MARAFONI',
 'style="top:1060px"><div class="h g glow" style="font-size:118px;white-space:nowrap;letter-spacing:.04em">Zikr marafoni')
c=c.replace('background:var(--gold);font:900 56px Nunito;padding:28px 56px;border-radius:60px;white-space:nowrap;box-shadow:0 8px 0 #B9812A,0 18px 30px rgba(120,80,20,.25)',
 'background:linear-gradient(180deg,#F8E3A6,#D4AF5F 55%,#B48A3C);color:#1A1408;font:700 50px Mont;padding:28px 60px;border-radius:60px;white-space:nowrap;box-shadow:0 0 40px rgba(233,199,114,.45),0 18px 30px rgba(0,0,0,.4)')
c=c.replace('color:#7D776D;white-space:nowrap">Telegram','color:#9C8E74;white-space:nowrap">Telegram').replace('font:700 30px Nunito','font:600 28px Mont')
c=c.replace('style="font-size:130px;line-height:1">0</div><div style="font:800 28px Nunito;color:#8A847A">/ 33</div>','style="font-size:140px;line-height:1;color:#F3E7CF">0</div><div style="font:600 24px Mont;color:#9C8E74">/ 33</div>')
TAS=C.TASBEH.replace("'#E2A63A':'#2E6B5B'","'#FFF1C4':'#D4AF5F'").replace('data-off="#D9D1C3"','data-off="rgba(233,199,114,.14)"').replace('stroke="#C4553B"','stroke="#E9C772"')
CUSTOM='''<script>(function(){
const cl=(x,a=0,b=1)=>Math.max(a,Math.min(b,x)),eo=p=>1-Math.pow(1-p,3),ei=p=>p<.5?2*p*p:1-Math.pow(-2*p+2,2)/2;
let seed=7;const rnd=()=>{seed=(seed*16807)%2147483647;return (seed-1)/2147483646};
const fx=document.getElementById('fx'),f=fx.getContext('2d');
const P=[...Array(160)].map(()=>({x:rnd()*1080,y:rnd()*1920,s:.6+rnd()*2.2,v:8+rnd()*26,a:.15+rnd()*.5,ph:rnd()*6.28}));
const S=[...Array(220)].map(()=>({x:rnd()*1080,y:rnd()*1300,s:.5+rnd()*1.6,ph:rnd()*6.28}));
const TINT=[[-9,[40,30,10]],[9.55,[14,22,60]],[16.45,[6,42,36]],[24.05,[46,28,8]],[32.55,[14,24,64]],[44.15,[40,18,52]],[55.3,[6,12,46]],[62.93,[8,34,44]],[76.92,[40,28,10]],[85.25,[42,30,12]]];
function tint(t){let i=0;while(i<TINT.length-1&&t>=TINT[i+1][0])i++;const a=TINT[i][1];if(i==TINT.length-1)return a;const b=TINT[i+1][1],k=cl((t-(TINT[i+1][0]-.5))/1);return a.map((v,j)=>v+(b[j]-v)*k)}
const cv=document.getElementById('grid'),gx=cv.getContext('2d');const COLS=88,N=6236,SP=10;
const D=[...Array(N)].map((_,i)=>{const r=Math.floor(i/COLS),c=i%COLS;const an=rnd()*6.28,rr=500+rnd()*700;return {tx:6+c*SP,ty:6+r*SP,sx:450+Math.cos(an)*rr,sy:360+Math.sin(an)*rr,d:(r/71)*1.3+rnd()*.35,b:rnd()}});
const svs=[...document.querySelectorAll('.sv')],gws=[...document.querySelectorAll('.gw')],scenes=[...document.querySelectorAll('.scene')];
const beam=document.getElementById('beam'),pL=document.getElementById('panL'),pR=document.getElementById('panR'),rip=document.getElementById('rip');
const scan=document.getElementById('scan'),tex=document.getElementById('tex'),star=document.getElementById('star'),rays=document.getElementById('rays1'),ban=document.getElementById('banner');
const R=window.render;
window.render=function(t){R(t);
 const [r,g,b]=tint(t);const gr=f.createRadialGradient(540,820,40,540,820,1250);gr.addColorStop(0,`rgb(${r|0},${g|0},${b|0})`);gr.addColorStop(1,'#04050A');f.fillStyle=gr;f.fillRect(0,0,1080,1920);
 const night=cl((t-55.0)/.6)*(1-cl((t-62.7)/.6));
 if(night>0)S.forEach(s=>{f.globalAlpha=night*(.35+.65*Math.abs(Math.sin(t*1.3+s.ph)));f.fillStyle='#FFF6DA';f.beginPath();f.arc(s.x,s.y,s.s,0,6.283);f.fill();});
 P.forEach(p=>{const y=((p.y-t*p.v)%1920+1920)%1920,x=p.x+Math.sin(t*.4+p.ph)*20;f.globalAlpha=p.a*(.6+.4*Math.sin(t*2+p.ph));f.fillStyle='#E9C772';f.beginPath();f.arc(x,y,p.s,0,6.283);f.fill();});
 f.globalAlpha=1;
 star.style.transform=`rotate(${t*2.2}deg) scale(${1+.04*Math.sin(t*.3)})`;
 scenes.forEach(sc=>{const s=+sc.dataset.s,e=Math.min(+sc.dataset.e,s+14);const k=cl((t-s)/(e-s));sc.style.transform=`scale(${1+.035*k})`;});
 if(scan){const k=cl(t/2.9);scan.style.top=(-260+k*2300)+'px';tex.style.transform=`translateX(${-t*14}px)`;}
 // grid
 if(t>9.4&&t<16.6){gx.clearRect(0,0,900,720);const T=t-9.65;
  for(let i=0;i<N;i++){const d=D[i],p=eo(cl((T-d.d)/.75));if(p<=0)continue;const x=d.sx+(d.tx-d.sx)*p,y=d.sy+(d.ty-d.sy)*p;
   const sh=p>=1?(.55+.45*Math.abs(Math.sin(t*1.7+d.b*40))):1;gx.globalAlpha=p*sh;gx.fillStyle=d.b>.92?'#FFF1C4':'#D4AF5F';gx.fillRect(x-2.6,y-2.6,5.2,5.2);}
  gx.globalAlpha=1;
  if(t>14.6){const k=eo(cl((t-14.6)/.5)),d=D[3150];gx.strokeStyle='#FFF1C4';gx.lineWidth=3;gx.fillStyle='#FFF1C4';gx.shadowColor='#E9C772';gx.shadowBlur=30;
   gx.beginPath();gx.arc(d.tx,d.ty,5+9*k,0,6.283);gx.fill();gx.beginPath();gx.arc(d.tx,d.ty,10+48*k,0,6.283);gx.globalAlpha=1-k*.4;gx.stroke();gx.shadowBlur=0;gx.globalAlpha=1;}}
 // scale
 let a=-9*eo(cl((t-17.5)/.8));if(t>20.45){const q=cl((t-20.45)/1.4);a=-9*(1-q)+Math.sin(q*Math.PI*3)*4*(1-q);}
 const rad=a*Math.PI/180;beam.setAttribute('transform',`rotate(${a} 400 140)`);
 pL.setAttribute('transform',`translate(${400-300*Math.cos(rad)} ${140-300*Math.sin(rad)})`);pR.setAttribute('transform',`translate(${400+300*Math.cos(rad)} ${140+300*Math.sin(rad)})`);
 const rq=cl((t-21.85)/1.2);rip.setAttribute('r',20+260*eo(rq));rip.setAttribute('opacity',rq>0&&rq<1?(1-rq):0);
 svs.forEach(e=>e.style.opacity=cl((t-+e.dataset.t)/.35));
 gws.forEach(e=>e.style.transform=`scaleX(${eo(cl((t-+e.dataset.t)/+(e.dataset.d||.8)))})`);
 if(rays)rays.style.transform=`rotate(${t*3}deg)`;
 if(ban){ban.style.transform=ban.style.transform.replace(/rotate\\([^)]*\\)/,'');}
};})();</script>'''
s+=c+'''
<div id="sub" data-hide="85.2"><div id="subbox"></div></div></div>'''+CUSTOM+TAS+'</body></html>'
open('/home/claude/reel17/index.html','w').write(HEAD+BG+s)
print('ok')
