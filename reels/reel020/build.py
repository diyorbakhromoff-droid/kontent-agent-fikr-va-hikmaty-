src=open('/home/claude/build17b.py').read()
exec(src.split("moon='<svg")[0])   # CSS, HEAD, BG, rule, kw, card, rv, C
C.SCENE_S='77.98'
CSS2='''
.ruler{display:flex;gap:12px;justify-content:center}
.door{width:84px;height:140px;border:2px solid rgba(212,175,95,.5);border-bottom:none;border-radius:46px 46px 0 0;background:linear-gradient(180deg,rgba(233,199,114,.10),rgba(233,199,114,.02));display:flex;align-items:flex-end;justify-content:center;padding-bottom:16px;font-size:34px}
.step{display:flex;align-items:center;gap:30px;width:900px}
.num{width:96px;height:96px;flex:none;border-radius:50%;border:2px solid #E9C772;display:flex;align-items:center;justify-content:center;font:600 54px Corm;color:#E9C772;box-shadow:0 0 24px rgba(233,199,114,.35)}
#dark{position:absolute;inset:0;background:#000;pointer-events:none;opacity:0}
'''
HEAD=HEAD.replace('</style>',CSS2+'</style>')
LAMP='''<svg width="{w}" height="{w}" viewBox="0 0 200 200" style="overflow:visible">
<defs><radialGradient id="fl{i}" cx=".5" cy=".7" r=".6"><stop offset="0" stop-color="#FFFBE8"/><stop offset=".45" stop-color="#FFD877"/><stop offset="1" stop-color="#E8892C"/></radialGradient>
<linearGradient id="lb{i}" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#F8E3A6"/><stop offset=".55" stop-color="#C9A24E"/><stop offset="1" stop-color="#7A5A20"/></linearGradient></defs>
<circle class="lglow" cx="100" cy="70" r="90" fill="rgba(255,206,110,.22)" style="filter:blur(18px)"/>
<g class="flame" style="transform-origin:100px 96px"><path d="M100 30C86 56 84 76 100 96C116 76 114 56 100 30Z" fill="url(#fl{i})"/><path d="M100 58C94 70 94 82 100 92C106 82 106 70 100 58Z" fill="#FFFDF2"/></g>
<path class="smoke" d="M100 92C92 70 110 56 100 30C92 14 104 0 98 -20" fill="none" stroke="rgba(220,220,220,.5)" stroke-width="5" stroke-linecap="round" opacity="0"/>
<rect x="95" y="94" width="10" height="14" fill="#5A4318"/>
<path d="M28 116Q100 104 168 112Q184 114 192 104Q196 120 176 128Q140 168 100 168Q52 168 32 136Q22 124 28 116Z" fill="url(#lb{i})"/>
<path d="M30 132Q10 130 12 116Q14 104 30 112" fill="none" stroke="#C9A24E" stroke-width="7"/>
<ellipse cx="100" cy="174" rx="44" ry="8" fill="#7A5A20"/></svg>'''
def lamp(i,w): return LAMP.format(i=i,w=w)
BOWL='<svg width="{w}" height="{h}" viewBox="0 0 200 120"><path d="M20 50H180Q172 110 100 112Q28 110 20 50Z" fill="none" stroke="#E9C772" stroke-width="5"/><path d="M14 50H186" stroke="#E9C772" stroke-width="5" stroke-linecap="round"/>{steam}</svg>'
STEAM='<g class="steam" fill="none" stroke="rgba(243,231,207,.55)" stroke-width="4" stroke-linecap="round"><path d="M70 40C60 26 80 18 70 2"/><path d="M100 40C90 26 110 18 100 2"/><path d="M130 40C120 26 140 18 130 2"/></g>'
EYE='<svg width="220" height="140" viewBox="0 0 220 140"><path d="M10 70Q110 -10 210 70Q110 150 10 70Z" fill="none" stroke="#BFAF90" stroke-width="5"/><circle cx="110" cy="70" r="26" fill="#BFAF90"/><path class="dr" data-t="70.24" data-d=".4" d="M30 125L190 15" stroke="#E0705E" stroke-width="7" stroke-linecap="round"/></svg>'
doors=''.join(f'<div class="a door" data-t="{13.36+i*.17:.2f}" data-a="rise" data-d=".4" style="position:relative"><span class="a" data-t="{17.79+i*.08:.2f}" data-a="zoom" style="position:relative">💧</span></div>' for i in range(9))
s=f'''
<div id="banner" data-s="10.5" data-e="77.9">Chiroqni nega o‘chirishdi?</div>
<section class="scene" data-s="-1" data-e="10.5">
 <div class="a cx cap" data-t="0.05" data-a="wide" data-ls=".42" style="top:250px">Sahobalar hayotidan</div>
 {rule(0.3,300)}
 {kw([('Bir',0,False),('er-xotin',0.32,False),('mehmon',0.84,True),('olib',1.8,False),('keldi',1.96,False)],92,380,'line-height:1.1')}
 <div class="a cx" data-t="2.6" data-a="zoom" data-d=".7" style="top:600px">{lamp(1,460)}</div>
 <div class="a cx it" data-t="4.8" data-a="blur" data-o="6.6" style="top:1110px;font-size:72px;white-space:nowrap">ayol <span class="g">chiroqni o‘chirdi</span></div>
 <div class="a cx h g glow" data-t="6.68" data-a="zoom" data-d=".45" data-o="7.55" style="top:1080px;font-size:220px;line-height:1">Nega?</div>
 <div class="a cx it" data-t="7.6" data-a="blur" style="top:1040px;font-size:62px;white-space:nowrap">Javobi uchun Alloh</div>
 <div class="a cx h g glow" data-t="9.04" data-a="zoom" data-d=".6" style="top:1130px;font-size:120px;white-space:nowrap">oyat nozil qildi</div>
</section>
<section class="scene" data-s="10.5" data-e="20.18">
 <div class="a cx cap" data-t="10.55" data-a="wide" data-ls=".42" style="top:300px">Madina</div>
 {rule(10.7,350)}
 {kw([('och',11.12,True),('bir',11.44,False),('odam',11.6,False),('keldi',11.92,False)],96,410)}
 <div class="a cx it" data-t="12.64" data-a="blur" style="top:580px;font-size:56px;white-space:nowrap;color:#BFAF90">Payg‘ambarimiz ayollarining uylariga…</div>
 <div class="a cx ruler" data-t="13.3" data-a="none" style="top:700px">{doors}</div>
 <div class="a cx" data-t="15.72" data-a="rise" style="top:960px">{card(0,'Hammasidan bitta javob','',rv([('«Uyda',17.79),('suvdan',18.12,'t-terra'),('boshqa',18.52),('hech',18.96),('narsa',19.2,'t-terra'),('yo‘q»',19.52,'t-terra')]),0,40,58).replace('class="a cx" data-t="0" data-a="rise"','class=""').replace('style="top:0px"','')}</div>
</section>
<section class="scene" data-s="20.18" data-e="29.94">
 <div class="a cx cap" data-t="20.25" data-a="wide" data-ls=".42" style="top:300px">Payg‘ambarimiz so‘radilar</div>
 {rule(20.5,350)}
 {kw([('«Bu',22.04,False),('kecha',22.24,False),('kim',22.68,True),('uni',22.88,False),('mehmon',23.0,True),('qiladi?»',23.4,True)],104,420,'line-height:1.08')}
 <div class="a cx it" data-t="24.2" data-a="blur" style="top:720px;font-size:60px;white-space:nowrap">Ansoriylardan bir sahoba <span class="g">turdi</span></div>
 <div class="a cx" data-t="26.28" data-a="rise" style="top:880px"><div class="glass frame" style="width:760px">
  <div class="dia" style="left:-8px;top:50%;margin-top:-8px"></div><div class="dia" style="right:-8px;top:50%;margin-top:-8px"></div>
  <div class="cap" style="font-size:20px">rivoyatlarning birida</div>
  <div class="arabic g" style="font-size:84px;line-height:1.6;margin-top:14px">أَبُو طَلْحَة</div>
  <div class="a h g glow" data-t="28.24" data-a="zoom" style="position:relative;font-size:120px;line-height:1">Abu Talha</div>
  <div class="cap" style="font-size:20px;margin-top:20px;color:#9C8E74">roziyallohu anhu</div></div></div>
</section>
<section class="scene" data-s="29.94" data-e="40.74">
 <div class="a cx cap" data-t="30.0" data-a="wide" data-ls=".42" style="top:290px">Uyda</div>
 {rule(30.2,340)}
 <div class="a" data-t="31.8" data-a="rise" style="left:90px;top:410px"><div class="glass h" style="padding:22px 40px;font-size:62px;white-space:nowrap">«Nimamiz bor?»</div></div>
 <div class="a" data-t="32.93" data-a="rise" style="right:90px;top:560px"><div class="glass h" style="padding:22px 40px;font-size:62px;white-space:nowrap">«Faqat <span class="g">bolalarning ovqati</span>»</div></div>
 <div class="a cx" data-t="34.68" data-a="rise" style="top:790px"><div class="step"><div class="num">1</div><div class="h" style="font-size:66px">Bolalarni uxlatib qo‘y</div></div></div>
 <div class="a cx" data-t="36.61" data-a="rise" style="top:940px"><div class="step"><div class="num">2</div><div class="h" style="font-size:66px">Chiroqni <span class="g">o‘chir</span></div></div></div>
 <div class="a cx" data-t="38.64" data-a="rise" style="top:1090px"><div class="step"><div class="num">3</div><div class="h" style="font-size:66px">Biz ham <span class="g">yegandek</span> bo‘lamiz</div></div></div>
</section>
<section class="scene" data-s="40.74" data-e="48.34">
 <div class="a cx it" data-t="40.76" data-a="blur" style="top:300px;font-size:84px;white-space:nowrap;color:#8E8370">Qorong‘ida…</div>
 <div class="a cx" data-t="41.33" data-a="zoom" style="top:470px;text-align:center">{BOWL.format(w=380,h=228,steam=STEAM)}<div class="h" style="font-size:54px;margin-top:8px">mehmon — <span class="g">to‘yib ovqatlandi</span></div></div>
 <div class="a" data-t="43.12" data-a="rise" style="left:0;top:880px;width:1080px;display:flex;justify-content:center;gap:80px">{BOWL.format(w=230,h=138,steam='')}{BOWL.format(w=230,h=138,steam='')}</div>
 <div class="a cx h" data-t="43.92" data-a="blur" style="top:1050px;font-size:58px;white-space:nowrap;color:#BFAF90">er-xotin — bo‘sh qo‘l bilan</div>
 <div class="a cx h g glow" data-t="47.28" data-a="zoom" data-d=".5" style="top:1170px;font-size:110px;white-space:nowrap">och yotishdi</div>
</section>
<section class="scene" data-s="48.34" data-e="54.2">
 <div class="rays" id="rays1"></div>
 <div class="a cx cap" data-t="48.36" data-a="wide" data-ls=".42" style="top:300px">Ertalab</div>
 {card(49.6,'Buxoriy, 3798 · Muslim, 2054','',rv([('«Alloh',50.64),('ikkingizning',51.12),('bu',51.92),('kechagi',52.08),('ishingizdan',52.64),('rozi',53.2,'t-terra'),('bo‘ldi»',53.52,'t-terra')]),560,40,74)}
</section>
<section class="scene" data-s="54.2" data-e="65.06">
 <div class="a cx it" data-t="54.24" data-a="blur" style="top:250px;font-size:64px;white-space:nowrap">Va shu haqda <span class="g">oyat tushdi</span></div>
 {card(55.08,'Hashr surasi · 9-oyat','وَيُؤْثِرُونَ عَلَىٰ أَنفُسِهِمْ وَلَوْ كَانَ بِهِمْ خَصَاصَةٌ ۚ وَمَن يُوقَ شُحَّ نَفْسِهِ فَأُولَٰئِكَ هُمُ الْمُفْلِحُونَ',rv([('«O‘zlari',56.03),('muhtoj',56.48,'t-terra'),('bo‘lsalar',56.92),('ham,',57.48),('boshqalarni',57.8),('o‘zlaridan',58.44),('ustun',59.04,'t-terra'),('qo‘yadilar.',59.44,'t-terra'),('Kim',60.44),('nafsining',60.6),('baxilligidan',61.12),('saqlansa,',61.76),('ana',62.84),('o‘shalar',63.0),('najot',63.52,'t-terra'),('topuvchilardir»',63.92,'t-terra')]),390,56,54)}
</section>
<section class="scene" data-s="65.06" data-e="74.7">
 <div class="a cx" data-t="65.44" data-a="zoom" style="top:330px">{BOWL.format(w=300,h=180,steam=STEAM)}</div>
 <div class="a cx h" data-t="66.83" data-a="blur" style="top:540px;font-size:70px;white-space:nowrap">bitta tovoq ovqat, <span class="g">xolos</span></div>
 <div class="a cx" data-t="69.36" data-a="rise" style="top:700px">{EYE}</div>
 <div class="a cx it" data-t="69.84" data-a="blur" style="top:870px;font-size:62px;white-space:nowrap;color:#BFAF90">hech kim ko‘rmadi</div>
 <div class="a cx it" data-t="71.08" data-a="blur" style="top:1040px;font-size:56px;white-space:nowrap">Qorong‘ida qilingan amalni esa</div>
 <div class="a cx h g glow" data-t="73.12" data-a="zoom" data-d=".6" style="top:1130px;font-size:120px;white-space:nowrap">Alloh ko‘rib turdi</div>
</section>
<section class="scene" data-s="74.7" data-e="77.98">
 <div class="rays" id="rays2"></div>
 {kw([('Eng',74.76,False),('katta',74.96,True),('amal',75.36,True)],130,560)}
 {rule(75.8,740)}
 <div class="a cx it" data-t="75.92" data-a="blur" style="top:800px;font-size:72px;white-space:nowrap">hech kim ko‘rmaganda</div>
 <div class="a cx h g glow" data-t="77.0" data-a="zoom" data-d=".5" style="top:900px;font-size:110px;white-space:nowrap">qilingani</div>
</section>
'''
extra='''<div class="a cx it g glow" data-t="78.05" data-a="blur" data-o="90.4" style="top:290px;font-size:62px;white-space:nowrap">Yashirin zikr — yashirin amal</div>
<div class="a cx" data-t="90.52" data-a="rise" style="top:290px;display:flex;gap:22px"><div class="chip" style="font-size:36px">📌 Saqlab qo‘ying</div><div class="a chip" data-t="91.84" data-a="rise" style="position:relative;font-size:36px">📤 Yaqiningizga yuboring</div></div>
<div class="a cx" data-t="85.44" data-a="zoom" style="top:1220px"><div class="chip" style="font-size:38px;white-space:nowrap;border:2px solid #E9C772">💬 Izohlarga <span class="g" style="font-size:54px">«+»</span> qoldiring</div></div>
<div class="a hand cx" data-t="87.04" data-a="blur" style="top:1330px;font-size:46px;color:#9C8E74">yoki</div>
'''
c=C.cta(tas=79.0,zikr=82.24,extra=extra,havola=87.68,btn=89.72)
c=c.replace('style="top:1250px"><div class="chip"','style="top:1395px"><div class="chip"').replace('style="top:1400px"><div style="background:var(--gold)','style="top:1520px"><div style="background:var(--gold)').replace('top:1560px;font:700','top:1680px;font:700')
c=c.replace('style="top:1070px"><div style="background:var(--terra);color:#fff;font:900 84px Fraunces;padding:22px 46px;border-radius:8px;white-space:nowrap;box-shadow:0 12px 26px rgba(150,60,40,.25)">ZIKR MARAFONI',
 'style="top:1060px"><div class="h g glow" style="font-size:118px;white-space:nowrap;letter-spacing:.04em">Zikr marafoni')
c=c.replace('background:var(--gold);font:900 56px Nunito;padding:28px 56px;border-radius:60px;white-space:nowrap;box-shadow:0 8px 0 #B9812A,0 18px 30px rgba(120,80,20,.25)',
 'background:linear-gradient(180deg,#F8E3A6,#D4AF5F 55%,#B48A3C);color:#1A1408;font:700 50px Mont;padding:28px 60px;border-radius:60px;white-space:nowrap;box-shadow:0 0 40px rgba(233,199,114,.45),0 18px 30px rgba(0,0,0,.4)')
c=c.replace('color:#7D776D;white-space:nowrap">Telegram','color:#9C8E74;white-space:nowrap">Telegram').replace('font:700 30px Nunito','font:600 28px Mont')
c=c.replace('style="font-size:130px;line-height:1">0</div><div style="font:800 28px Nunito;color:#8A847A">/ 33</div>','style="font-size:140px;line-height:1;color:#F3E7CF">0</div><div style="font:600 24px Mont;color:#9C8E74">/ 33</div>')
TAS=C.TASBEH.replace("'#E2A63A':'#2E6B5B'","'#FFF1C4':'#D4AF5F'").replace('data-off="#D9D1C3"','data-off="rgba(233,199,114,.14)"').replace('stroke="#C4553B"','stroke="#E9C772"')
CUSTOM='''<script>(function(){
const cl=(x,a=0,b=1)=>Math.max(a,Math.min(b,x)),eo=p=>1-Math.pow(1-p,3);
let seed=11;const rnd=()=>{seed=(seed*16807)%2147483647;return (seed-1)/2147483646};
const fx=document.getElementById('fx'),f=fx.getContext('2d');
const P=[...Array(150)].map(()=>({x:rnd()*1080,y:rnd()*1920,s:.6+rnd()*2.2,v:8+rnd()*26,a:.15+rnd()*.5,ph:rnd()*6.28}));
const S=[...Array(220)].map(()=>({x:rnd()*1080,y:rnd()*1300,s:.5+rnd()*1.6,ph:rnd()*6.28}));
const TINT=[[-9,[46,30,8]],[10.5,[10,22,52]],[20.18,[14,34,40]],[29.94,[44,28,10]],[40.74,[6,8,22]],[48.34,[70,44,12]],[54.2,[8,36,40]],[65.06,[14,20,56]],[74.7,[44,32,10]],[77.98,[40,28,12]]];
function tint(t){let i=0;while(i<TINT.length-1&&t>=TINT[i+1][0])i++;const a=TINT[i][1];if(i==TINT.length-1)return a;const b=TINT[i+1][1],k=cl((t-(TINT[i+1][0]-.5))/1);return a.map((v,j)=>v+(b[j]-v)*k)}
const scenes=[...document.querySelectorAll('.scene')],star=document.getElementById('star'),dark=document.getElementById('dark');
const flames=[...document.querySelectorAll('.flame')],glows=[...document.querySelectorAll('.lglow')],smokes=[...document.querySelectorAll('.smoke')],steams=[...document.querySelectorAll('.steam')];
const rays=[...document.querySelectorAll('.rays')];
const R=window.render;
window.render=function(t){R(t);
 const [r,g,b]=tint(t);const gr=f.createRadialGradient(540,820,40,540,820,1250);gr.addColorStop(0,`rgb(${r|0},${g|0},${b|0})`);gr.addColorStop(1,'#04050A');f.fillStyle=gr;f.fillRect(0,0,1080,1920);
 const night=cl((t-10.4)/.6)*(1-cl((t-20)/.6))+cl((t-40.6)/.6)*(1-cl((t-48.2)/.8));
 if(night>0)S.forEach(s=>{f.globalAlpha=night*(.3+.6*Math.abs(Math.sin(t*1.3+s.ph)));f.fillStyle='#FFF6DA';f.beginPath();f.arc(s.x,s.y,s.s,0,6.283);f.fill();});
 const pd=t>40.7&&t<48.3?.25:1;
 P.forEach(p=>{const y=((p.y-t*p.v)%1920+1920)%1920,x=p.x+Math.sin(t*.4+p.ph)*20;f.globalAlpha=pd*p.a*(.6+.4*Math.sin(t*2+p.ph));f.fillStyle='#E9C772';f.beginPath();f.arc(x,y,p.s,0,6.283);f.fill();});
 f.globalAlpha=1;
 star.style.transform=`rotate(${t*2.2}deg) scale(${1+.04*Math.sin(t*.3)})`;
 scenes.forEach(sc=>{const s=+sc.dataset.s,e=Math.min(+sc.dataset.e,s+14);const k=cl((t-s)/(e-s));sc.style.transform=`scale(${1+.035*k})`;});
 // lamp: flicker, then blown out at 5.6
 const out=cl((t-5.6)/.35);
 flames.forEach((fl,i)=>{const fk=1+.06*Math.sin(t*23+i)+.04*Math.sin(t*37);fl.style.transform=`scale(${(1-out)*fk},${(1-out*.7)*fk})`;fl.style.opacity=1-out;});
 glows.forEach(gw=>gw.style.opacity=(1-out)*(.8+.2*Math.sin(t*17)));
 smokes.forEach(sm=>{const k=cl((t-5.65)/1.6);sm.setAttribute('opacity',k>0&&k<1?(1-k)*.8:0);sm.style.transform=`translateY(${-k*40}px)`;});
 // darkness after lamp out, and in the dark-meal scene
 let d=out*(1-cl((t-6.6)/.5))*.55+cl((t-40.6)/.5)*(1-cl((t-47.1)/.6))*.35;dark.style.opacity=d;
 steams.forEach((st,i)=>{st.style.transform=`translateY(${-((t*14+i*7)%18)}px)`;st.style.opacity=.5+.5*Math.sin(t*2+i);});
 rays.forEach(x=>x.style.transform=`rotate(${t*3}deg)`);
};})();</script>'''
s+=c+'''
<div id="dark"></div><div id="sub" data-hide="77.95"><div id="subbox"></div></div></div>'''+CUSTOM+TAS+'</body></html>'
open('/home/claude/reel20/index.html','w').write(HEAD+BG+s)
print('ok')
