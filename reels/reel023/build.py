src=open('/home/claude/build17b.py').read()
exec(src.split("moon='<svg")[0])
C.SCENE_S='100.36'
CSS2='''
#dark{position:absolute;inset:0;background:#000;pointer-events:none;opacity:0}
#birds{position:absolute;inset:0;pointer-events:none}
'''
HEAD=HEAD.replace('</style>',CSS2+'</style>')
KAABA='''<svg width="{w}" height="{h}" viewBox="0 0 240 230" style="overflow:visible"><defs><linearGradient id="kb{i}" x1="0" x2="0" y1="0" y2="1"><stop offset="0" stop-color="#1C1A18"/><stop offset="1" stop-color="#0A0908"/></linearGradient></defs>
<ellipse class="kglow" cx="120" cy="200" rx="150" ry="26" fill="rgba(233,199,114,.18)" style="filter:blur(10px)"/>
<path d="M30 60L120 30L210 60V190L120 220L30 190Z" fill="url(#kb{i})" stroke="rgba(233,199,114,.5)" stroke-width="2"/>
<path d="M120 30V220" stroke="rgba(233,199,114,.25)" stroke-width="2"/>
<path d="M30 92L120 64L210 92V108L120 80L30 108Z" fill="#D4AF5F"/>
<rect x="140" y="140" width="34" height="56" fill="#C9A24E" transform="skewY(-18) translate(0,52)"/></svg>'''
def kaaba(i,w=300): return KAABA.format(i=i,w=w,h=int(w*230/240))
ELE='''<svg width="{w}" height="{h}" viewBox="0 0 300 220" style="overflow:visible"><g fill="rgba(233,199,114,.10)" stroke="#E9C772" stroke-width="5" stroke-linejoin="round" stroke-linecap="round">
<path d="M70 70Q80 30 140 30Q210 30 232 70Q246 96 236 120L232 180H208L204 140Q170 150 130 146L126 180H102L98 140Q80 132 72 116Z"/>
<path d="M232 70Q262 60 272 90Q280 120 270 160Q266 176 254 170" fill="none"/>
<path d="M226 66Q200 60 196 92Q194 116 220 118" fill="rgba(233,199,114,.18)"/>
<circle cx="246" cy="84" r="4" fill="#E9C772" stroke="none"/>
<path d="M70 80Q52 90 56 112" fill="none"/></g></svg>'''
def ele(w=300): return ELE.format(w=w,h=int(w*220/300))
CAMELS=''.join(f'<div class="a" data-t="{22.96+i*.12:.2f}" data-a="rise" style="position:relative;font-size:64px">🐪</div>' for i in range(6))
s=f'''
<div id="banner" data-s="9.5" data-e="100.3">Ka‘bani kim himoya qildi?</div>
<section class="scene" data-s="-1" data-e="9.56">
 <div class="a cx cap" data-t="0.05" data-a="wide" data-ls=".42" style="top:250px">Fil yili</div>
 {rule(0.3,300)}
 <div class="a cx" data-t="0.1" data-a="zoom" data-d=".7" style="top:400px">{kaaba(1,340)}</div>
 <div class="a" data-t="0.4" data-a="rise" style="left:60px;top:500px"><div class="elw">{ele(220)}</div></div>
 {kw([('Fillari',0.0,True),('bor',0.56,False),('qo‘shin',1.36,False)],82,800,o='3.5')}
 <div class="a cx it" data-t="1.76" data-a="blur" data-o="3.5" style="top:910px;font-size:62px;white-space:nowrap">Ka‘bani <span class="g">buzishga keldi</span></div>
 <div class="a cx it" data-t="3.56" data-a="blur" data-o="6.95" style="top:840px;font-size:62px;white-space:nowrap">Makkaliklar jang qilmadi —</div>
 <div class="a cx h" data-t="5.39" data-a="blur" data-o="6.95" style="top:940px;font-size:74px;white-space:nowrap">tog‘larga chiqib ketishdi</div>
 <div class="a cx it" data-t="7.0" data-a="blur" style="top:820px;font-size:62px;white-space:nowrap">Unda Ka‘bani</div>
 <div class="a cx h g glow" data-t="8.08" data-a="zoom" data-d=".5" style="top:920px;font-size:120px;white-space:nowrap">kim himoya qildi?</div>
</section>
<section class="scene" data-s="9.56" data-e="21.24">
 <div class="a cx cap" data-t="9.6" data-a="wide" data-ls=".42" style="top:300px">Yaman</div>
 {rule(9.8,350)}
 {kw([('Abraha',10.24,True),('degan',10.8,False),('hukmdor',11.08,False)],96,420)}
 <div class="a cx it" data-t="11.84" data-a="blur" style="top:570px;font-size:62px;white-space:nowrap">ulkan cherkov qurdi</div>
 <div class="a cx" data-t="13.6" data-a="rise" style="top:690px"><div class="glass frame" style="width:880px"><div class="h" style="font-size:56px;line-height:1.25">{rv([('Arablar',13.84),('Ka‘ba',14.4,'t-terra'),('o‘rniga',14.8),('unga',15.28,'t-terra'),('kelishini',15.6),('xohladi',16.0)])}</div></div></div>
 <div class="a" data-t="17.4" data-a="rise" style="left:0;top:1000px;width:1080px;display:flex;justify-content:center;gap:40px">{ele(170)}{ele(170)}{ele(170)}</div>
 <div class="a cx h g glow" data-t="19.76" data-a="zoom" style="top:1200px;font-size:92px;white-space:nowrap">Makkaga yo‘l oldi</div>
</section>
<section class="scene" data-s="21.24" data-e="30.44">
 <div class="a cx cap" data-t="21.28" data-a="wide" data-ls=".42" style="top:300px">Makka chetida</div>
 {rule(21.5,350)}
 {kw([('Qurayshning',22.4,False),('tuyalarini',22.96,True),('tortib',23.52,False),('oldi',24.0,False)],62,420)}
 <div class="a cx" data-t="22.9" data-a="none" style="top:560px;display:flex;gap:18px">{CAMELS}</div>
 <div class="a cx it" data-t="24.68" data-a="blur" style="top:720px;font-size:58px;white-space:nowrap;color:#BFAF90">Ular orasida Payg‘ambarimizning bobolari</div>
 <div class="a cx h g glow" data-t="27.28" data-a="zoom" style="top:820px;font-size:110px;white-space:nowrap">Abdulmuttolib</div>
 <div class="a cx" data-t="28.4" data-a="rise" style="top:1010px"><div class="glass" style="padding:24px 50px;display:flex;align-items:center;gap:20px"><span class="h g count" data-t="28.4" data-d=".9" data-from="0" data-to="200" style="font-size:110px;line-height:1">0</span><span class="h" style="font-size:60px">ta tuyasi</span></div></div>
</section>
<section class="scene" data-s="30.44" data-e="48.18">
 <div class="a cx it" data-t="30.48" data-a="blur" data-o="40.85" style="top:270px;font-size:58px;white-space:nowrap">Abdulmuttolib faqat <span class="g">tuyalarini so‘radi</span></div>
 <div class="a cx cap" data-t="34.72" data-a="wide" data-ls=".42" data-o="40.85" style="top:420px">Abraha hayron bo‘ldi</div>
 <div class="a cx" data-t="36.4" data-a="rise" data-o="40.85" style="top:500px"><div class="glass frame" style="width:920px"><div class="h" style="font-size:62px;line-height:1.2">{rv([('«Men',36.56),('Ka‘bani',36.8,'t-terra'),('buzgani',37.36,'t-terra'),('keldim,',37.84),('sen',38.56),('esa',38.92),('tuyalaringni',39.08,'t-terra'),('so‘rayapsanmi?»',39.68)])}</div></div></div>
 <div class="a cx cap" data-t="40.88" data-a="wide" data-ls=".42" style="top:300px">Abdulmuttolib dedi</div>
 {rule(41.0,350)}
 {kw([('«Men',42.52,False),('tuyalarning',42.88,False),('egasiman.',43.52,True)],80,430)}
 <div class="a cx" data-t="44.5" data-a="zoom" style="top:600px">{kaaba(2,260)}</div>
 {kw([('Uyning',44.56,False),('esa',45.04,False),('O‘z',45.44,True),('Egasi',45.72,True),('bor»',46.16,False)],84,880)}
 <div class="a cx it g glow" data-t="46.72" data-a="blur" style="top:1010px;font-size:66px;white-space:nowrap">U himoya qiladi</div>
</section>
<section class="scene" data-s="48.18" data-e="60.04">
 <div class="a cx cap" data-t="48.2" data-a="wide" data-ls=".42" style="top:300px">Ertasi kuni</div>
 {rule(48.4,350)}
 <div class="a cx" data-t="48.6" data-a="rise" style="top:420px"><div class="bigele">{ele(380)}</div></div>
 <div class="a cx h" data-t="50.08" data-a="blur" data-o="57.1" style="top:760px;font-size:70px;white-space:nowrap">Ka‘ba tomonga <span class="g">qadam bosmadi</span></div>
 <div class="a cx it" data-t="52.16" data-a="blur" data-o="57.1" style="top:880px;font-size:56px;white-space:nowrap;color:#BFAF90">boshqa tarafga — yurardi</div>
 <div class="a cx it" data-t="54.28" data-a="blur" data-o="57.1" style="top:970px;font-size:56px;white-space:nowrap">Makkaga — <span class="g">cho‘kib o‘tirardi</span></div>
 <div class="a cx it" data-t="57.12" data-a="blur" style="top:820px;font-size:64px;white-space:nowrap">Shunda osmonni</div>
 <div class="a cx h g glow" data-t="58.32" data-a="zoom" data-d=".5" style="top:920px;font-size:112px;white-space:nowrap">qushlar qopladi</div>
</section>
<section class="scene" data-s="60.04" data-e="72.66">
 {card(60.1,'Fil surasi · 1, 3–5','أَلَمْ تَرَ كَيْفَ فَعَلَ رَبُّكَ بِأَصْحَابِ الْفِيلِ ۝ وَأَرْسَلَ عَلَيْهِمْ طَيْرًا أَبَابِيلَ ۝ تَرْمِيهِم بِحِجَارَةٍ مِّن سِجِّيلٍ ۝ فَجَعَلَهُمْ كَعَصْفٍ مَّأْكُولٍ',rv([('«Robbingiz',60.08),('fil',60.72,'t-terra'),('egalarini',61.08,'t-terra'),('nima',61.56),('qilganini',61.8),('ko‘rmadingizmi?',62.32),('Ularning',63.56),('ustiga',64.12),('to‘da-to‘da',64.56,'t-terra'),('qushlarni',65.24,'t-terra'),('yubordi.',65.76),('Ularni',66.64),('sopol',67.04,'t-terra'),('toshlar',67.52,'t-terra'),('bilan',68.0),('otdi.',68.24),('Va',69.04),('ularni',69.28),('yeb',69.6),('tashlangan',69.88),('ekin',70.56,'t-terra'),('poyasidek',70.88,'t-terra'),('qilib',71.56),('qo‘ydi»',71.8)]),380,52,52)}
</section>
<section class="scene" data-s="72.66" data-e="78.2">
 <div class="rays" id="rays1"></div>
 <div class="a cx it" data-t="72.68" data-a="blur" style="top:420px;font-size:70px;white-space:nowrap">Aynan shu yili —</div>
 <div class="a cx h g glow" data-t="74.4" data-a="zoom" data-d=".6" style="top:540px;font-size:150px;white-space:nowrap">Fil yili</div>
 {rule(75.4,760)}
 <div class="a cx h" data-t="76.08" data-a="blur" style="top:820px;font-size:70px;white-space:nowrap">Payg‘ambarimiz <span class="g">dunyoga keldilar</span></div>
 <div class="a cx cap" data-t="76.6" data-a="wide" data-ls=".42" style="top:960px;color:#9C8E74">sollallohu alayhi va sallam</div>
</section>
<section class="scene" data-s="78.2" data-e="87.6">
 <div class="a cx it" data-t="78.24" data-a="blur" style="top:270px;font-size:60px;white-space:nowrap">Ko‘p yillar o‘tib, <span class="g">Hudaybiyada</span></div>
 <div class="a cx it" data-t="80.24" data-a="blur" style="top:370px;font-size:56px;white-space:nowrap;color:#BFAF90">u zotning tuyalari cho‘kib qoldi</div>
 {card(83.2,'Buxoriy, 2731','حَبَسَهَا حَابِسُ الْفِيلِ',rv([('«Uni',84.12),('filni',84.48,'t-terra'),('to‘xtatgan',84.88,'t-terra'),('Zot',85.6,'t-terra'),('to‘xtatdi»',85.92)]),520,74,70)}
</section>
<section class="scene" data-s="87.6" data-e="96.6">
 {kw([('Qurayshda',87.76,False),('na',88.52,False),('qo‘shin,',88.68,False),('na',89.36,False),('kuch',89.6,False),('bor',89.92,False),('edi',90.16,False)],62,330)}
 <div class="a cx it" data-t="90.72" data-a="blur" style="top:460px;font-size:60px;white-space:nowrap">Lekin</div>
 <div class="a cx h g glow" data-t="91.28" data-a="zoom" style="top:550px;font-size:110px;white-space:nowrap">Uyning Egasi bor edi</div>
 <div class="a cx it" data-t="93.2" data-a="blur" style="top:780px;font-size:58px;white-space:nowrap">Sizda ham</div>
 <div class="a cx h" data-t="94.08" data-a="zoom" style="top:870px;font-size:84px;white-space:nowrap">«bunga kuchim yetmaydi»</div>
 <div class="a cx it" data-t="95.3" data-a="blur" style="top:990px;font-size:58px;white-space:nowrap">degan muammo bormi?</div>
</section>
<section class="scene" data-s="96.6" data-e="100.36">
 <div class="rays" id="rays2"></div>
 {kw([('Kuchingiz',96.96,False),('yetmagan',97.52,False),('joyda',98.0,False)],96,520)}
 {rule(98.3,680)}
 <div class="a cx h g glow" data-t="98.64" data-a="zoom" data-d=".5" style="top:760px;font-size:112px;white-space:nowrap">Allohning kuchi</div>
 <div class="a cx h g glow" data-t="99.52" data-a="zoom" data-d=".4" style="top:890px;font-size:112px;white-space:nowrap">yetadi</div>
</section>
'''
extra='''<div class="a cx it g glow" data-t="100.4" data-a="blur" data-o="111.6" style="top:290px;font-size:62px;white-space:nowrap">Har kuni zikr — Allohga suyanish</div>
<div class="a cx" data-t="111.64" data-a="rise" style="top:290px;display:flex;gap:22px"><div class="chip" style="font-size:36px">📌 Saqlab qo‘ying</div><div class="a chip" data-t="113.2" data-a="rise" style="position:relative;font-size:36px">📤 Yaqinlaringizga yuboring</div></div>
<div class="a cx" data-t="106.5" data-a="zoom" style="top:1220px"><div class="chip" style="font-size:38px;white-space:nowrap;border:2px solid #E9C772">💬 Izohlarga <span class="g" style="font-size:54px">«+»</span> qoldiring</div></div>
<div class="a hand cx" data-t="108.24" data-a="blur" style="top:1330px;font-size:46px;color:#9C8E74">yoki</div>
'''
c=C.cta(tas=101.0,zikr=103.68,extra=extra,havola=108.8,btn=110.5)
c=c.replace('style="top:1250px"><div class="chip"','style="top:1395px"><div class="chip"').replace('style="top:1400px"><div style="background:var(--gold)','style="top:1520px"><div style="background:var(--gold)').replace('top:1560px;font:700','top:1680px;font:700')
c=c.replace('style="top:1070px"><div style="background:var(--terra);color:#fff;font:900 84px Fraunces;padding:22px 46px;border-radius:8px;white-space:nowrap;box-shadow:0 12px 26px rgba(150,60,40,.25)">ZIKR MARAFONI',
 'style="top:1060px"><div class="h g glow" style="font-size:118px;white-space:nowrap;letter-spacing:.04em">Zikr marafoni')
c=c.replace('background:var(--gold);font:900 56px Nunito;padding:28px 56px;border-radius:60px;white-space:nowrap;box-shadow:0 8px 0 #B9812A,0 18px 30px rgba(120,80,20,.25)',
 'background:linear-gradient(180deg,#F8E3A6,#D4AF5F 55%,#B48A3C);color:#1A1408;font:700 50px Mont;padding:28px 60px;border-radius:60px;white-space:nowrap;box-shadow:0 0 40px rgba(233,199,114,.45),0 18px 30px rgba(0,0,0,.4)')
c=c.replace('color:#7D776D;white-space:nowrap">Telegram','color:#9C8E74;white-space:nowrap">Telegram').replace('font:700 30px Nunito','font:600 28px Mont')
c=c.replace('style="font-size:130px;line-height:1">0</div><div style="font:800 28px Nunito;color:#8A847A">/ 33</div>','style="font-size:140px;line-height:1;color:#F3E7CF">0</div><div style="font:600 24px Mont;color:#9C8E74">/ 33</div>')
TAS=C.TASBEH.replace("'#E2A63A':'#2E6B5B'","'#FFF1C4':'#D4AF5F'").replace('data-off="rgba(233,199,114,.14)"','data-off="rgba(233,199,114,.14)"').replace('data-off="#D9D1C3"','data-off="rgba(233,199,114,.14)"').replace('stroke="#C4553B"','stroke="#E9C772"')
CUSTOM='''<script>(function(){
const cl=(x,a=0,b=1)=>Math.max(a,Math.min(b,x));
let seed=23;const rnd=()=>{seed=(seed*16807)%2147483647;return (seed-1)/2147483646};
const fx=document.getElementById('fx'),f=fx.getContext('2d');
const P=[...Array(140)].map(()=>({x:rnd()*1080,y:rnd()*1920,s:.6+rnd()*2.2,v:8+rnd()*26,a:.15+rnd()*.5,ph:rnd()*6.28}));
const B=[...Array(70)].map(()=>({x0:-200-rnd()*900,y:120+rnd()*700,v:260+rnd()*200,s:10+rnd()*14,ph:rnd()*6.28}));
const ST=[...Array(90)].map(()=>({x:60+rnd()*960,d:rnd()*2.2,v:600+rnd()*500}));
const TINT=[[-9,[50,30,10]],[9.56,[30,22,14]],[21.24,[48,32,12]],[30.44,[40,22,12]],[48.18,[24,20,30]],[60.04,[10,26,52]],[72.66,[60,42,12]],[78.2,[14,30,40]],[87.6,[14,22,50]],[96.6,[50,36,12]],[100.36,[40,28,12]]];
function tint(t){let i=0;while(i<TINT.length-1&&t>=TINT[i+1][0])i++;const a=TINT[i][1];if(i==TINT.length-1)return a;const b=TINT[i+1][1],k=cl((t-(TINT[i+1][0]-.5))/1);return a.map((v,j)=>v+(b[j]-v)*k)}
const scenes=[...document.querySelectorAll('.scene')],star=document.getElementById('star');
const rays=[...document.querySelectorAll('.rays')],elw=[...document.querySelectorAll('.elw')],big=[...document.querySelectorAll('.bigele')],kg=[...document.querySelectorAll('.kglow')];
const R=window.render;
window.render=function(t){R(t);
 const [r,g,b]=tint(t);const gr=f.createRadialGradient(540,820,40,540,820,1250);gr.addColorStop(0,`rgb(${r|0},${g|0},${b|0})`);gr.addColorStop(1,'#04050A');f.fillStyle=gr;f.fillRect(0,0,1080,1920);
 P.forEach(p=>{const y=((p.y-t*p.v)%1920+1920)%1920,x=p.x+Math.sin(t*.4+p.ph)*20;f.globalAlpha=p.a*(.6+.4*Math.sin(t*2+p.ph));f.fillStyle='#E9C772';f.beginPath();f.arc(x,y,p.s,0,6.283);f.fill();});
 // birds flock 57.2-73
 const bk=cl((t-57.2)/.8)*(1-cl((t-72.4)/1));
 if(bk>0){f.strokeStyle='#F3E7CF';f.lineWidth=3;f.lineCap='round';B.forEach(o=>{const x=o.x0+(t-57.2)*o.v,y=o.y+Math.sin(t*2+o.ph)*14;if(x<-60||x>1140)return;const w=Math.sin(t*14+o.ph)*o.s*.6;f.globalAlpha=bk*.85;f.beginPath();f.moveTo(x-o.s,y-w);f.quadraticCurveTo(x-o.s*.4,y-2,x,y);f.quadraticCurveTo(x+o.s*.4,y-2,x+o.s,y-w);f.stroke();});
  // falling stones 63-70
  const sk=cl((t-62.8)/.5)*(1-cl((t-70.5)/.8));if(sk>0)ST.forEach(s=>{const y=((t-62.8-s.d)*s.v)%1600;if(y<0)return;f.globalAlpha=sk*.8;f.fillStyle='#C9714E';f.beginPath();f.arc(s.x,300+y,4,0,6.283);f.fill();});}
 f.globalAlpha=1;
 star.style.transform=`rotate(${t*2.2}deg) scale(${1+.04*Math.sin(t*.3)})`;
 scenes.forEach(sc=>{const s=+sc.dataset.s,e=Math.min(+sc.dataset.e,s+14);const k=cl((t-s)/(e-s));sc.style.transform=`scale(${1+.035*k})`;});
 elw.forEach(x=>x.style.transform=`translateX(${Math.min(t,9)*5}px)`);
 // big elephant: walks, then kneels at 54.3
 big.forEach(x=>{const kn=cl((t-54.4)/.7);x.style.transformOrigin='50% 100%';x.style.transform=`translateY(${kn*40+Math.sin(t*3)*4*(1-kn)}px) scaleY(${1-kn*.18}) rotate(${Math.sin(t*1.6)*1.5*(1-kn)}deg)`;});
 kg.forEach(k=>k.style.opacity=.6+.4*Math.sin(t*2));
 rays.forEach(x=>x.style.transform=`rotate(${t*3}deg)`);
};})();</script>'''
s+=c+'''
<div id="dark"></div><div id="sub" data-hide="100.3"><div id="subbox"></div></div></div>'''+CUSTOM+TAS+'</body></html>'
open('/home/claude/reel23/index.html','w').write(HEAD+BG+s)
print('ok')
