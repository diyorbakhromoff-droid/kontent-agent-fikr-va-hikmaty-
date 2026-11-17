src=open('/home/claude/build17b.py').read()
exec(src.split("moon='<svg")[0])
C.SCENE_S='91.64'
CSS2='''
#dark{position:absolute;inset:0;background:#000;pointer-events:none;opacity:0}
.xout{position:relative;display:inline-block}
.xout:after{content:"";position:absolute;left:-4%;top:52%;height:7px;width:108%;background:#E0705E;border-radius:4px;transform:scaleX(var(--k,0));transform-origin:left}
'''
HEAD=HEAD.replace('</style>',CSS2+'</style>')
SWORD='''<svg width="{w}" height="{h}" viewBox="0 0 80 320" style="overflow:visible"><defs><linearGradient id="bl{i}" x1="0" x2="1"><stop offset="0" stop-color="#8E9AA6"/><stop offset=".5" stop-color="#F4F7FA"/><stop offset="1" stop-color="#7C8794"/></linearGradient>
<linearGradient id="hl{i}" x1="0" x2="0" y1="0" y2="1"><stop offset="0" stop-color="#F8E3A6"/><stop offset="1" stop-color="#9C7430"/></linearGradient></defs>
<path d="M40 0L52 34L50 222H30L28 34Z" fill="url(#bl{i})"/><path d="M40 8V220" stroke="rgba(255,255,255,.6)" stroke-width="1.5"/>
<rect x="4" y="222" width="72" height="14" rx="7" fill="url(#hl{i})"/><rect x="33" y="236" width="14" height="58" rx="5" fill="#5A3E18"/><circle cx="40" cy="302" r="12" fill="url(#hl{i})"/></svg>'''
def sword(i,w=90,h=360): return SWORD.format(i=i,w=w,h=h)
HOUSE='<svg width="{w}" height="{w}" viewBox="0 0 200 200"><path d="M20 96L100 30L180 96" fill="none" stroke="#E9C772" stroke-width="7" stroke-linejoin="round"/><rect x="42" y="92" width="116" height="90" fill="none" stroke="#E9C772" stroke-width="6"/><path d="M86 182V136Q100 122 114 136V182" fill="rgba(233,199,114,.25)" stroke="#E9C772" stroke-width="5"/><rect class="win" x="58" y="112" width="22" height="22" fill="#FFD877"/><rect class="win" x="120" y="112" width="22" height="22" fill="#FFD877"/></svg>'
PAGE='''<svg width="{w}" height="{h}" viewBox="0 0 240 300"><path d="M20 10H190L222 42V290H20Z" fill="rgba(243,231,207,.10)" stroke="#E9C772" stroke-width="4"/><path d="M190 10V42H222" fill="none" stroke="#E9C772" stroke-width="4"/>
<g stroke="rgba(233,199,114,.55)" stroke-width="5" stroke-linecap="round"><path d="M50 120H192"/><path d="M50 150H192"/><path d="M50 180H192"/><path d="M50 210H192"/><path d="M50 240H150"/></g>
<text x="121" y="92" text-anchor="middle" font-family="Amiri" font-weight="700" font-size="62" fill="#E9C772">طه</text></svg>'''
HEART='<svg width="{w}" height="{w}" viewBox="0 0 200 200"><path class="hpath" d="M100 172C40 128 16 96 16 66C16 40 36 22 60 22C78 22 92 32 100 46C108 32 122 22 140 22C164 22 184 40 184 66C184 96 160 128 100 172Z" fill="rgba(233,199,114,.12)" stroke="#E9C772" stroke-width="6"/></svg>'
s=f'''
<div id="banner" data-s="11.4" data-e="91.6">Qilich bilan chiqdi — iymon bilan qaytdi</div>
<section class="scene" data-s="-1" data-e="11.4">
 <div class="a cx cap" data-t="0.05" data-a="wide" data-ls=".42" style="top:250px">Sahobalar hayotidan</div>
 {rule(0.3,300)}
 <div class="a cx" data-t="1.9" data-a="zoom" data-d=".6" data-o="8.7" style="top:380px"><div class="swd" style="transform:rotate(-20deg)">{sword(1,120,480)}</div></div>
 {kw([('Payg‘ambarimizni',0.28,False),('o‘ldirish',1.08,True),('uchun',1.52,False)],78,900,'line-height:1.1',o='3.7')}
 <div class="a cx it" data-t="2.88" data-a="blur" data-o="3.7" style="top:1010px;font-size:62px;white-space:nowrap">qilich olib <span class="g">uydan chiqdi</span></div>
 <div class="a cx cap" data-t="3.76" data-a="wide" data-ls=".42" data-o="8.7" style="top:900px">bir soatdan keyin</div>
 {kw([('Islomni',6.8,True),('qabul',7.36,True),('qilib',7.68,False),('turardi',7.92,False)],96,970,'line-height:1.1',o='8.7')}
 <div class="a cx it" data-t="8.88" data-a="blur" style="top:420px;font-size:70px;white-space:nowrap;color:#BFAF90">Bu odam —</div>
 <div class="a cx" data-t="9.7" data-a="rise" style="top:560px"><div class="glass frame" style="width:800px">
  <div class="dia" style="left:-8px;top:50%;margin-top:-8px"></div><div class="dia" style="right:-8px;top:50%;margin-top:-8px"></div>
  <div class="arabic g" style="font-size:96px;line-height:1.6">عُمَرُ بْنُ الْخَطَّاب</div>
  <div class="a h g glow" data-t="9.79" data-a="zoom" style="position:relative;font-size:100px;line-height:1;white-space:nowrap">Umar ibn Xattob</div>
  <div class="cap" style="font-size:20px;margin-top:22px;color:#9C8E74">roziyallohu anhu</div></div></div>
</section>
<section class="scene" data-s="11.4" data-e="18.3">
 <div class="a cx h g glow" data-t="11.6" data-a="zoom" data-d=".6" style="top:330px;font-size:150px">Makka</div>
 {rule(11.9,510)}
 {kw([('Musulmonlar',12.56,False),('oz',13.36,True),('va',13.76,False),('kuchsiz',13.88,True)],84,600)}
 <div class="a cx" data-t="12.6" data-a="fade" style="top:740px;display:flex;gap:26px">{''.join(f'<div class="a" data-t="{12.7+i*.12:.2f}" data-a="rise" style="position:relative;width:26px;height:26px;border-radius:50%;background:#E9C772;box-shadow:0 0 14px rgba(233,199,114,.6)"></div>' for i in range(5))}</div>
 <div class="a cx it" data-t="14.88" data-a="blur" style="top:880px;font-size:64px;white-space:nowrap">Umar esa — Qurayshning</div>
 <div class="a cx h g glow" data-t="16.48" data-a="zoom" data-d=".5" style="top:990px;font-size:116px;white-space:nowrap">eng qattiqqo‘l yigiti</div>
</section>
<section class="scene" data-s="18.3" data-e="26.9">
 <div class="a cx cap" data-t="18.35" data-a="wide" data-ls=".42" style="top:300px">Bir kuni</div>
 {rule(18.5,350)}
 <div class="a" data-t="18.96" data-a="rise" style="left:120px;top:430px"><div class="swd2" style="transform:rotate(90deg);transform-origin:center">{sword(2,70,280)}</div></div>
 <div class="a h" data-t="19.5" data-a="blur" style="left:330px;top:560px;font-size:70px;white-space:nowrap">yo‘lga <span class="g">chiqdi</span></div>
 <div class="a cx it" data-t="20.72" data-a="blur" style="top:780px;font-size:60px;white-space:nowrap;color:#BFAF90">Yo‘lda bir kishi to‘xtatdi:</div>
 <div class="a cx" data-t="22.4" data-a="rise" style="top:900px"><div class="glass frame" style="width:900px"><div class="h" style="font-size:66px;line-height:1.2">{rv([('«Avval',22.48),('o‘z',22.88),('uyingga',23.12,'t-terra'),('qara.',23.56,'t-terra'),('Singling',24.24),('va',24.8),('kuyoving',24.92),('ham',25.48),('musulmon',25.68,'t-terra'),('bo‘lgan»',26.12,'t-terra')])}</div></div></div>
</section>
<section class="scene" data-s="26.9" data-e="40.4">
 <div class="a cx" data-t="27.0" data-a="zoom" style="top:300px">{HOUSE.format(w=300)}</div>
 {kw([('Umar',26.96,False),('g‘azab',27.44,True),('bilan',27.84,False)],86,640)}
 <div class="a cx it" data-t="28.08" data-a="blur" style="top:760px;font-size:60px;white-space:nowrap">singlisining uyiga kirdi</div>
 <div class="a cx h" data-t="29.56" data-a="blur" data-o="35.9" style="top:900px;font-size:66px;white-space:nowrap">kuyovini urdi…</div>
 <div class="a cx h" data-t="32.32" data-a="blur" data-o="35.9" style="top:1010px;font-size:66px;white-space:nowrap">singlisining <span style="color:#E0705E">yuziga ham</span></div>
 <div class="a cx it" data-t="35.04" data-a="blur" data-o="35.9" style="top:1120px;font-size:58px;white-space:nowrap;color:#E0705E">yuzidan qon oqdi</div>
 <div class="a cx it" data-t="35.96" data-a="blur" style="top:900px;font-size:66px;white-space:nowrap">Lekin u <span class="g">qo‘rqmadi</span>:</div>
 <div class="a cx" data-t="37.4" data-a="rise" style="top:1030px"><div class="glass frame" style="width:900px"><div class="h g glow" style="font-size:72px;line-height:1.15">«Xohlaganingni qil,<br>biz musulmonmiz!»</div></div></div>
</section>
<section class="scene" data-s="40.4" data-e="53.4">
 <div class="a cx" data-t="40.6" data-a="zoom" data-o="45.2" style="top:300px">{HEART.format(w=260)}</div>
 {kw([('Umarning',41.04,False),('qalbi',41.6,True),('yumshadi',41.92,True)],90,600,o='45.2')}
 <div class="a cx it" data-t="42.83" data-a="blur" data-o="45.2" style="top:760px;font-size:58px;white-space:nowrap">«O‘qiyotgan sahifangizni menga bering»</div>
 <div class="a cx" data-t="45.28" data-a="zoom" data-d=".6" style="top:300px">{PAGE.format(w=300,h=375)}</div>
 <div class="a cx cap" data-t="46.16" data-a="wide" data-ls=".42" style="top:720px">Toha surasi</div>
 <div class="a cx it" data-t="47.96" data-a="blur" style="top:820px;font-size:60px;white-space:nowrap;color:#BFAF90">U o‘qidi va dedi:</div>
 {kw([('«Bu',49.72,False),('qanday',50.08,False),('go‘zal,',50.64,True)],104,930)}
 {kw([('qanday',51.6,False),('ulug‘',52.16,True),('so‘z!»',52.64,True)],104,1060)}
</section>
<section class="scene" data-s="53.4" data-e="59.55">
 <div class="rays" id="rays1"></div>
 <div class="a cx it" data-t="53.6" data-a="blur" style="top:330px;font-size:66px;white-space:nowrap">To‘g‘ri Payg‘ambarimiz oldiga</div>
 <div class="a cx h g glow" data-t="55.08" data-a="zoom" style="top:440px;font-size:110px">bordi</div>
 <div class="a cx cap" data-t="55.87" data-a="wide" data-ls=".42" style="top:660px">bu safar</div>
 <div class="a cx h" data-t="56.56" data-a="blur" style="top:740px;font-size:84px;white-space:nowrap;color:#BFAF90"><span class="xout" data-k0="57.5">o‘ldirish uchun</span>&nbsp; emas</div>
 <div class="a cx h g glow" data-t="58.0" data-a="zoom" data-d=".5" style="top:900px;font-size:96px;white-space:nowrap">iymon keltirish uchun</div>
</section>
<section class="scene" data-s="59.55" data-e="72.76">
 <div class="a cx it" data-t="59.6" data-a="blur" style="top:280px;font-size:60px;white-space:nowrap">Payg‘ambarimiz bundan oldin <span class="g">duo qilgan edilar</span></div>
 {card(62.0,'Termiziy, 3681','اللَّهُمَّ أَعِزَّ الإِسْلاَمَ بِأَحَبِّ هَذَيْنِ الرَّجُلَيْنِ إِلَيْكَ',rv([('«Allohim,',62.28),('Islomni',63.32),('shu',63.8),('ikki',64.12),('kishidan',64.32),('O‘zingga',64.96),('suyuklirog‘i',65.52,'t-terra'),('bilan',66.32),('aziz',66.68,'t-terra'),('qil:',67.0,'t-terra'),('Abu',67.6),('Jahl',67.92),('yoki',68.56),('Umar',69.04,'t-terra'),('bilan»',69.44)]),400,56,56)}
 <div class="a cx it" data-t="70.16" data-a="blur" style="top:1180px;font-size:62px;white-space:nowrap">Duo <span class="g">Umar haqida ijobat bo‘ldi</span></div>
</section>
<section class="scene" data-s="72.76" data-e="78.82">
 <div class="rays" id="rays2"></div>
 <div class="a cx cap" data-t="72.8" data-a="wide" data-ls=".42" style="top:300px">Abdulloh ibn Mas’ud aytadi</div>
 {card(74.0,'Buxoriy, 3684','مَا زِلْنَا أَعِزَّةً مُنْذُ أَسْلَمَ عُمَرُ',rv([('«Umar',74.92),('musulmon',75.36,'t-terra'),('bo‘lganidan',75.92),('beri',76.56),('biz',77.12),('aziz',77.56,'t-terra'),('bo‘ldik»',77.92,'t-terra')]),480,62,70)}
</section>
<section class="scene" data-s="78.82" data-e="87.48">
 <div class="a cx it" data-t="78.84" data-a="blur" style="top:300px;font-size:64px;white-space:nowrap">Siz ham kimnidir</div>
 <div class="a cx h g glow" data-t="80.08" data-a="zoom" style="top:400px;font-size:78px;white-space:nowrap">«u hech qachon o‘zgarmaydi»</div>
 <div class="a cx it" data-t="81.62" data-a="blur" style="top:540px;font-size:60px;white-space:nowrap">deb o‘ylaysizmi?</div>
 <div class="a cx it" data-t="82.8" data-a="blur" style="top:680px;font-size:58px;white-space:nowrap;color:#BFAF90">Umar haqida ham shunday deyishgan</div>
 <div class="a cx" data-t="85.0" data-a="zoom" style="top:800px">{HEART.format(w=220)}</div>
 {kw([('Qalblar',85.0,False),('Allohning',86.0,True),('qo‘lida',86.72,True)],100,1050)}
</section>
<section class="scene" data-s="87.48" data-e="91.64">
 <div class="rays" id="rays3"></div>
 {kw([('Hech',87.52,False),('kimdan',87.8,False),('umidingizni',88.16,True),('uzmang',88.92,True)],104,520,'line-height:1.1')}
 {rule(89.5,790)}
 <div class="a cx it" data-t="89.81" data-a="blur" style="top:840px;font-size:72px;white-space:nowrap">uning uchun</div>
 <div class="a cx h g glow" data-t="90.56" data-a="zoom" data-d=".5" style="top:950px;font-size:130px;white-space:nowrap">duo qiling</div>
</section>
'''
extra='''<div class="a cx it g glow" data-t="91.7" data-a="blur" data-o="101.9" style="top:290px;font-size:62px;white-space:nowrap">Duo va zikr — har kuni birga</div>
<div class="a cx" data-t="101.96" data-a="rise" style="top:290px;display:flex;gap:22px"><div class="chip" style="font-size:36px">📌 Saqlab qo‘ying</div><div class="a chip" data-t="103.5" data-a="rise" style="position:relative;font-size:36px">📤 Yaqiningizga yuboring</div></div>
<div class="a cx" data-t="96.9" data-a="zoom" style="top:1220px"><div class="chip" style="font-size:38px;white-space:nowrap;border:2px solid #E9C772">💬 Izohlarga <span class="g" style="font-size:54px">«+»</span> qoldiring</div></div>
<div class="a hand cx" data-t="98.64" data-a="blur" style="top:1330px;font-size:46px;color:#9C8E74">yoki</div>
'''
c=C.cta(tas=92.4,zikr=94.24,extra=extra,havola=99.2,btn=100.9)
c=c.replace('style="top:1250px"><div class="chip"','style="top:1395px"><div class="chip"').replace('style="top:1400px"><div style="background:var(--gold)','style="top:1520px"><div style="background:var(--gold)').replace('top:1560px;font:700','top:1680px;font:700')
c=c.replace('style="top:1070px"><div style="background:var(--terra);color:#fff;font:900 84px Fraunces;padding:22px 46px;border-radius:8px;white-space:nowrap;box-shadow:0 12px 26px rgba(150,60,40,.25)">ZIKR MARAFONI',
 'style="top:1060px"><div class="h g glow" style="font-size:118px;white-space:nowrap;letter-spacing:.04em">Zikr marafoni')
c=c.replace('background:var(--gold);font:900 56px Nunito;padding:28px 56px;border-radius:60px;white-space:nowrap;box-shadow:0 8px 0 #B9812A,0 18px 30px rgba(120,80,20,.25)',
 'background:linear-gradient(180deg,#F8E3A6,#D4AF5F 55%,#B48A3C);color:#1A1408;font:700 50px Mont;padding:28px 60px;border-radius:60px;white-space:nowrap;box-shadow:0 0 40px rgba(233,199,114,.45),0 18px 30px rgba(0,0,0,.4)')
c=c.replace('color:#7D776D;white-space:nowrap">Telegram','color:#9C8E74;white-space:nowrap">Telegram').replace('font:700 30px Nunito','font:600 28px Mont')
c=c.replace('style="font-size:130px;line-height:1">0</div><div style="font:800 28px Nunito;color:#8A847A">/ 33</div>','style="font-size:140px;line-height:1;color:#F3E7CF">0</div><div style="font:600 24px Mont;color:#9C8E74">/ 33</div>')
TAS=C.TASBEH.replace("'#E2A63A':'#2E6B5B'","'#FFF1C4':'#D4AF5F'").replace('data-off="#D9D1C3"','data-off="rgba(233,199,114,.14)"').replace('stroke="#C4553B"','stroke="#E9C772"')
CUSTOM='''<script>(function(){
const cl=(x,a=0,b=1)=>Math.max(a,Math.min(b,x));
let seed=22;const rnd=()=>{seed=(seed*16807)%2147483647;return (seed-1)/2147483646};
const fx=document.getElementById('fx'),f=fx.getContext('2d');
const P=[...Array(150)].map(()=>({x:rnd()*1080,y:rnd()*1920,s:.6+rnd()*2.2,v:8+rnd()*26,a:.15+rnd()*.5,ph:rnd()*6.28}));
const TINT=[[-9,[52,22,10]],[11.4,[40,28,10]],[18.3,[30,20,12]],[26.9,[56,14,10]],[40.4,[14,30,40]],[53.4,[60,42,12]],[59.55,[10,26,52]],[72.76,[46,34,10]],[78.82,[14,22,50]],[87.48,[50,36,12]],[91.64,[40,28,12]]];
function tint(t){let i=0;while(i<TINT.length-1&&t>=TINT[i+1][0])i++;const a=TINT[i][1];if(i==TINT.length-1)return a;const b=TINT[i+1][1],k=cl((t-(TINT[i+1][0]-.5))/1);return a.map((v,j)=>v+(b[j]-v)*k)}
const scenes=[...document.querySelectorAll('.scene')],star=document.getElementById('star');
const rays=[...document.querySelectorAll('.rays')],strikes=[...document.querySelectorAll('.xout')],swd=[...document.querySelectorAll('.swd')],hearts=[...document.querySelectorAll('.hpath')],wins=[...document.querySelectorAll('.win')];
const R=window.render;
window.render=function(t){R(t);
 const [r,g,b]=tint(t);const gr=f.createRadialGradient(540,820,40,540,820,1250);gr.addColorStop(0,`rgb(${r|0},${g|0},${b|0})`);gr.addColorStop(1,'#04050A');f.fillStyle=gr;f.fillRect(0,0,1080,1920);
 P.forEach(p=>{const y=((p.y-t*p.v)%1920+1920)%1920,x=p.x+Math.sin(t*.4+p.ph)*20;f.globalAlpha=p.a*(.6+.4*Math.sin(t*2+p.ph));f.fillStyle='#E9C772';f.beginPath();f.arc(x,y,p.s,0,6.283);f.fill();});
 f.globalAlpha=1;
 star.style.transform=`rotate(${t*2.2}deg) scale(${1+.04*Math.sin(t*.3)})`;
 scenes.forEach(sc=>{const s=+sc.dataset.s,e=Math.min(+sc.dataset.e,s+14);const k=cl((t-s)/(e-s));sc.style.transform=`scale(${1+.035*k})`;});
 swd.forEach(x=>{const k=cl((t-2)/1.2);x.style.transform=`rotate(${-20+8*Math.sin(t*1.5)}deg) translateY(${-10*k}px)`;x.style.filter=`drop-shadow(0 0 ${10+8*Math.sin(t*4)}px rgba(255,255,255,.35))`;});
 strikes.forEach(x=>x.style.setProperty('--k',cl((t-+x.dataset.k0)/.35)));
 hearts.forEach(h=>{h.style.transformOrigin='100px 100px';h.style.transform=`scale(${1+.05*Math.sin(t*5)})`;});
 wins.forEach((w,i)=>w.style.opacity=.6+.4*Math.sin(t*3+i));
 rays.forEach(x=>x.style.transform=`rotate(${t*3}deg)`);
};})();</script>'''
s+=c+'''
<div id="dark"></div><div id="sub" data-hide="91.6"><div id="subbox"></div></div></div>'''+CUSTOM+TAS+'</body></html>'
open('/home/claude/reel22/index.html','w').write(HEAD+BG+s)
print('ok')
