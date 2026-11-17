src=open('/home/claude/build17b.py').read()
exec(src.split("moon='<svg")[0])
C.SCENE_S='62.6'
CSS2='''
#dark{position:absolute;inset:0;background:#000;pointer-events:none;opacity:0}
.xout{position:relative;display:inline-block}
.xout:after{content:"";position:absolute;left:-4%;top:52%;height:7px;width:108%;background:#E0705E;border-radius:4px;transform:scaleX(var(--k,0));transform-origin:left}
.qrow{display:flex;align-items:center;gap:24px;width:960px;padding:26px 30px}
.qic{width:84px;height:84px;flex:none;border-radius:50%;border:2px solid rgba(233,199,114,.6);display:flex;align-items:center;justify-content:center;font-size:44px}
.men{margin-left:auto;font:700 40px Mont;color:#1A1408;background:linear-gradient(180deg,#F8E3A6,#D4AF5F 55%,#B48A3C);padding:10px 26px;border-radius:40px;white-space:nowrap;box-shadow:0 0 24px rgba(233,199,114,.45)}
'''
HEAD=HEAD.replace('</style>',CSS2+'</style>')
def qrow(t,ic,q,tm,top):
    return f'<div class="a cx" data-t="{t}" data-a="rise" style="top:{top}px"><div class="glass qrow"><div class="qic">{ic}</div><div class="h" style="font-size:50px;white-space:nowrap">{q}</div><div class="a men" data-t="{tm}" data-a="stamp" data-d=".3" style="position:relative">«Men»</div></div></div>'
s=f'''
<div id="banner" data-s="10.2" data-e="62.5">Bir kunda to‘rt savol</div>
<section class="scene" data-s="-1" data-e="10.2">
 <div class="a cx cap" data-t="0.05" data-a="wide" data-ls=".42" style="top:250px">Sahobalar hayotidan</div>
 {rule(0.3,300)}
 <div class="a cx h g glow count" data-t="1.68" data-d=".6" data-from="0" data-to="4" style="top:380px;font-size:300px;line-height:1">0</div>
 <div class="a cx it" data-t="2.08" data-a="blur" style="top:700px;font-size:70px;white-space:nowrap">ta savol</div>
 <div class="a cx it" data-t="3.4" data-a="blur" style="top:840px;font-size:60px;white-space:nowrap;color:#BFAF90">To‘rttasiga ham bitta odam:</div>
 <div class="a cx h g glow" data-t="5.44" data-a="stamp" data-d=".35" style="top:940px;font-size:150px;line-height:1">«Men»</div>
 <div class="a cx it" data-t="7.2" data-a="blur" style="top:1140px;font-size:60px;white-space:nowrap">va u <span class="g">jannat bashoratini</span> oldi</div>
</section>
<section class="scene" data-s="10.2" data-e="31.4">
 <div class="a cx cap" data-t="10.25" data-a="wide" data-ls=".42" style="top:280px">Payg‘ambarimiz so‘radilar</div>
 {rule(10.5,330)}
 {qrow(12.96,'🌙','Bugun kim ro‘za tutdi?',16.36,440)}
 {qrow(17.36,'🤲','Kim janozaga ergashdi?',20.68,660)}
 {qrow(21.68,'🍲','Kim miskinga ovqat berdi?',25.48,880)}
 {qrow(26.48,'🩺','Kim bemorni ko‘rgani bordi?',30.48,1100)}
</section>
<section class="scene" data-s="31.4" data-e="37.4">
 <div class="rays" id="rays1"></div>
 <div class="a cx it" data-t="31.52" data-a="blur" style="top:330px;font-size:64px;white-space:nowrap">Shunda Payg‘ambarimiz dedilar:</div>
 {card(32.4,'Muslim, 1028','مَا اجْتَمَعْنَ فِي امْرِئٍ إِلاَّ دَخَلَ الْجَنَّةَ',rv([('«Bu',33.4),('amallar',33.68),('kimda',34.16),('jamlansa,',34.6,'t-terra'),('albatta',35.6),('jannatga',36.16,'t-terra'),('kiradi»',36.64,'t-terra')]),500,66,72)}
</section>
<section class="scene" data-s="37.4" data-e="58.3">
 {kw([('Hammasi',38.4,False),('bir',39.04,True),('kunda',39.28,True)],100,300,o='47.7')}
 <div class="a cx it" data-t="40.24" data-a="blur" data-o="47.7" style="top:450px;font-size:62px;white-space:nowrap;color:#BFAF90">va hech biri ulkan ish emas</div>
 <div class="a" data-t="41.9" data-a="none" data-o="47.7" style="left:0;top:600px;width:1080px;display:flex;flex-wrap:wrap;justify-content:center;gap:24px 26px">
  <div class="a chip" data-t="42.0" data-a="zoom" style="position:relative;font-size:40px;padding:20px 34px;border-radius:40px">🌙 bir kunlik ro‘za</div>
  <div class="a chip" data-t="43.36" data-a="zoom" style="position:relative;font-size:40px;padding:20px 34px;border-radius:40px">🤲 bitta janoza</div>
  <div class="a chip" data-t="44.8" data-a="zoom" style="position:relative;font-size:40px;padding:20px 34px;border-radius:40px">🍲 bir tovoq ovqat</div>
  <div class="a chip" data-t="46.32" data-a="zoom" style="position:relative;font-size:40px;padding:20px 34px;border-radius:40px">🩺 bitta ziyorat</div></div>
 <div class="a cx it" data-t="47.76" data-a="blur" style="top:300px;font-size:62px;white-space:nowrap">Abu Bakrni Abu Bakr qilgan narsa —</div>
 <div class="a cx h" data-t="50.24" data-a="blur" style="top:430px;font-size:72px;white-space:nowrap;color:#BFAF90"><span class="xout" data-k0="51.4">bitta katta amal</span>&nbsp; emas</div>
 <div class="a cx h g glow" data-t="52.08" data-a="zoom" data-d=".5" style="top:570px;font-size:96px;white-space:nowrap">har kungi kichik amallar</div>
 {rule(54.3,740)}
 <div class="a cx it" data-t="54.72" data-a="blur" style="top:800px;font-size:64px;white-space:nowrap">Siz bugun shu to‘rttasidan</div>
 <div class="a cx h g glow" data-t="56.64" data-a="zoom" style="top:900px;font-size:110px;white-space:nowrap">nechtasini qildingiz?</div>
</section>
<section class="scene" data-s="58.3" data-e="62.6">
 <div class="rays" id="rays2"></div>
 {kw([('Jannat',58.48,True),('yo‘li',58.96,True)],120,460)}
 {rule(59.3,620)}
 <div class="a cx it" data-t="59.6" data-a="blur" style="top:690px;font-size:68px;white-space:nowrap">kichik amallar bir kunda jamlanganda</div>
 <div class="a cx h g glow" data-t="61.76" data-a="zoom" data-d=".5" style="top:810px;font-size:120px;white-space:nowrap">ochiladi</div>
</section>
'''
extra='''<div class="a cx it g glow" data-t="62.7" data-a="blur" data-o="76.1" style="top:290px;font-size:62px;white-space:nowrap">Kichik, lekin ulug‘ amal</div>
<div class="a cx" data-t="76.16" data-a="rise" style="top:290px;display:flex;gap:22px"><div class="chip" style="font-size:36px">📌 Saqlab qo‘ying</div><div class="a chip" data-t="77.76" data-a="rise" style="position:relative;font-size:36px">📤 Yaqinlaringizga yuboring</div></div>
<div class="a cx" data-t="71.2" data-a="zoom" style="top:1220px"><div class="chip" style="font-size:38px;white-space:nowrap;border:2px solid #E9C772">💬 Izohlarga <span class="g" style="font-size:54px">«+»</span> qoldiring</div></div>
<div class="a hand cx" data-t="72.8" data-a="blur" style="top:1330px;font-size:46px;color:#9C8E74">yoki</div>
'''
c=C.cta(tas=63.3,zikr=68.32,extra=extra,havola=73.44,btn=74.9)
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
let seed=25;const rnd=()=>{seed=(seed*16807)%2147483647;return (seed-1)/2147483646};
const fx=document.getElementById('fx'),f=fx.getContext('2d');
const P=[...Array(150)].map(()=>({x:rnd()*1080,y:rnd()*1920,s:.6+rnd()*2.2,v:8+rnd()*26,a:.15+rnd()*.5,ph:rnd()*6.28}));
const TINT=[[-9,[52,36,12]],[10.2,[14,26,48]],[31.4,[60,42,12]],[37.4,[18,30,40]],[58.3,[54,38,12]],[62.6,[40,28,12]]];
function tint(t){let i=0;while(i<TINT.length-1&&t>=TINT[i+1][0])i++;const a=TINT[i][1];if(i==TINT.length-1)return a;const b=TINT[i+1][1],k=cl((t-(TINT[i+1][0]-.5))/1);return a.map((v,j)=>v+(b[j]-v)*k)}
const scenes=[...document.querySelectorAll('.scene')],star=document.getElementById('star');
const rays=[...document.querySelectorAll('.rays')],xs=[...document.querySelectorAll('.xout')];
const R=window.render;
window.render=function(t){R(t);
 const [r,g,b]=tint(t);const gr=f.createRadialGradient(540,820,40,540,820,1250);gr.addColorStop(0,`rgb(${r|0},${g|0},${b|0})`);gr.addColorStop(1,'#04050A');f.fillStyle=gr;f.fillRect(0,0,1080,1920);
 P.forEach(p=>{const y=((p.y-t*p.v)%1920+1920)%1920,x=p.x+Math.sin(t*.4+p.ph)*20;f.globalAlpha=p.a*(.6+.4*Math.sin(t*2+p.ph));f.fillStyle='#E9C772';f.beginPath();f.arc(x,y,p.s,0,6.283);f.fill();});
 f.globalAlpha=1;
 star.style.transform=`rotate(${t*2.2}deg) scale(${1+.04*Math.sin(t*.3)})`;
 scenes.forEach(sc=>{const s=+sc.dataset.s,e=Math.min(+sc.dataset.e,s+14);const k=cl((t-s)/(e-s));sc.style.transform=`scale(${1+.035*k})`;});
 xs.forEach(x=>x.style.setProperty('--k',cl((t-+x.dataset.k0)/.35)));
 rays.forEach(x=>x.style.transform=`rotate(${t*3}deg)`);
};})();</script>'''
s+=c+'''
<div id="dark"></div><div id="sub" data-hide="62.5"><div id="subbox"></div></div></div>'''+CUSTOM+TAS+'</body></html>'
open('/home/claude/reel25/index.html','w').write(HEAD+BG+s)
print('ok')
