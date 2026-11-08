import sys; sys.path.insert(0,'/home/claude')
import cta as C
exec(open('/home/claude/build4.py').read().split('# ---------- reel004 ----------')[0].split('import cta as C')[1])
C.SCENE_S='76.85'
b=bgs([(-1,6.6,'#E9E2D6'),(6.6,14.0,'#F3E9CF'),(14.0,21.7,'#E5DDEB'),(21.7,33.3,'#DAE2E9'),(33.3,41.3,'#F1E6D6'),(41.3,45.5,'#DCE6DA'),(45.5,55.5,'#F3E9CF'),(55.5,66.1,'#DAE2E9'),(66.1,76.85,'#F6E1D3'),(76.85,999,'#F1E6D6')])
shield='''<svg width="{w}" height="{h}" viewBox="0 0 100 120"><path d="M50 6L90 20v34c0 30-18 50-40 60C28 104 10 84 10 54V20z" fill="{c}"/><path d="M50 22l26 9v24c0 20-12 34-26 41-14-7-26-21-26-41V31z" fill="#FBF7EE" opacity=".35"/></svg>'''
warn='''<svg width="{w}" height="{h}" viewBox="0 0 100 90"><path d="M50 6l46 80H4z" fill="#E2A63A" stroke="#C4553B" stroke-width="5" stroke-linejoin="round"/><path d="M50 34v26" stroke="#2A2724" stroke-width="9" stroke-linecap="round"/><circle cx="50" cy="72" r="5" fill="#2A2724"/></svg>'''
dots=''.join(f'<div style="width:26px;height:26px;border-radius:50%;background:{"#2E6B5B" if i in (0,7) else "#C9C2B6"}"></div><div style="width:46px;height:5px;background:#C9C2B6"></div>' for i in range(8))[:-len('<div style="width:46px;height:5px;background:#C9C2B6"></div>')]
def cal(t,big,small,col,left,top,r):
    return f'''<div class="a" data-t="{t}" data-a="pop" data-r="{r}" style="left:{left}px;top:{top}px"><div class="card" style="width:430px;padding:0;overflow:hidden;text-align:center"><div style="background:{col};color:#fff;font:900 34px Nunito;padding:12px">1 KUN</div><div style="padding:18px 10px 22px"><div style="font:800 34px Nunito;color:#8A847A">=</div><div class="serif" style="font-size:66px;line-height:1.05;color:{col}">{big}</div><div style="font:800 30px Nunito;color:#8A847A">{small}</div></div></div></div>'''
s=f'''
<div id="banner" data-s="6.6" data-e="76.6">Dajjoldan qanday himoyalanamiz?</div>
<section class="scene" data-s="-1" data-e="6.6">
 <div class="a cx" data-t="0.05" data-a="up" style="top:300px;display:flex;justify-content:space-between;width:900px;font:900 40px Nunito"><span class="t-green">Nuh (a.s.)</span><span class="t-green">Muhammad (s.a.v.)</span></div>
 <div class="a cx" data-t="0.4" data-a="fade" style="top:370px;display:flex;align-items:center">{dots}</div>
 <div class="a hand cx" data-t="1.6" data-a="up" style="top:440px;font-size:64px;color:#8A847A;white-space:nowrap">har bir payg‘ambar…</div>
 <div class="a cx" data-t="3.4" data-a="pop" data-f="4" style="top:580px">{warn.format(w=260,h=234)}</div>
 <div class="a cx" data-t="3.6" data-a="up" style="top:860px"><div class="card tape" style="width:860px;text-align:center;padding:32px"><div class="serif" style="font-size:58px;line-height:1.2"><span class="t-terra">bitta kishidan</span> ogohlantirgan</div></div></div>
 <div class="a cx" data-t="5.3" data-a="stamp" data-d=".3" data-r="-3" style="top:1110px"><div class="stamp" style="font-size:96px">U KIM?</div></div>
</section>
<section class="scene" data-s="6.6" data-e="14.0">
 <div class="a cx" data-t="6.65" data-a="pop" data-r="-.6" style="top:300px"><div class="card tape ayah">
  <div class="caps">Hadisi sharif · Imom Buxoriy, 7131</div>
  <div class="arabic" style="font-size:60px;line-height:1.75;margin-top:12px;color:var(--green)">مَا بُعِثَ نَبِيٌّ إِلَّا أَنْذَرَ أُمَّتَهُ الأَعْوَرَ الكَذَّابَ</div>
  <div class="serif" style="font-size:48px;line-height:1.25;margin-top:16px;color:var(--ink)">{rv([('«Har',6.69),('bir',6.87),('payg‘ambar',7.13),('o‘z',7.77),('ummatini',8.07),('bir',8.64,'t-terra'),('ko‘zli',8.83,'t-terra'),('yolg‘onchidan',9.13,'t-terra'),('ogohlantirgan»',9.81)])}</div></div></div>
 <div class="a cx" data-t="10.9" data-a="up" style="top:860px;font:900 50px Nunito;white-space:nowrap">ikki ko‘zi orasida:</div>
 <div class="a cx" data-t="12.4" data-a="stamp" data-d=".3" data-r="-3" style="top:960px"><div class="stamp" style="font-size:100px">«KOFIR»</div></div>
</section>
<section class="scene" data-s="14.0" data-e="21.7">
 <div class="a cx" data-t="14.5" data-a="stamp" data-d=".35" data-r="-2" style="top:290px"><div style="background:var(--ink);color:#FBF7EE;font:900 120px Fraunces;padding:16px 56px;border-radius:10px;letter-spacing:4px">DAJJOL</div></div>
 <div class="a cx" data-t="15.4" data-a="pop" data-r="-.6" style="top:560px"><div class="card tape ayah">
  <div class="caps">Hadisi sharif · Imom Muslim, 2946</div>
  <div class="arabic" style="font-size:54px;line-height:1.75;margin-top:12px;color:var(--green)">مَا بَيْنَ خَلْقِ آدَمَ إِلَى قِيَامِ السَّاعَةِ خَلْقٌ أَكْبَرُ مِنَ الدَّجَّالِ</div>
  <div class="serif" style="font-size:48px;line-height:1.25;margin-top:16px;color:var(--ink)">{rv([('«Odam',16.8),('alayhissalom',17.09),('yaratilganidan',17.66),('to',18.41),('Qiyomatgacha',18.68),('Dajjoldan',19.66,'t-terra'),('kattaroq',20.3,'t-terra'),('fitna',20.75,'t-terra'),('yo‘q»',21.06)])}</div></div></div>
</section>
<section class="scene" data-s="21.7" data-e="33.3">
 <div class="a hand cx" data-t="21.8" data-a="up" style="top:280px;font-size:64px;color:var(--terra);white-space:nowrap">eng hayratlanarlisi — uning kunlari</div>
 <div class="a cx" data-t="25.0" data-a="pop" style="top:390px;display:flex;align-items:baseline;gap:20px"><div class="serif" style="font-size:150px;line-height:1;color:var(--green)"><span class="count" data-t="25.05" data-d=".5" data-from="0" data-to="40">0</span></div><div style="font:900 60px Nunito">kun</div><div class="caps" style="margin-left:20px;white-space:nowrap">Muslim, 2937</div></div>
 {cal(26.8,'1 yil','dek','#C4553B',90,620,-2)}
 {cal(28.25,'1 oy','dek','#E2A63A',560,620,2)}
 {cal(29.85,'1 hafta','dek','#2E6B5B',90,960,1.5)}
 <div class="a" data-t="31.0" data-a="pop" data-r="-1.5" style="left:560px;top:1010px"><div class="chip" style="font-size:36px;width:430px;justify-content:center">qolgani — oddiy kunlar</div></div>
</section>
<section class="scene" data-s="33.3" data-e="41.3">
 <div class="a" data-t="33.4" data-a="left" style="left:80px;top:290px"><div class="label gold">Sahobalar so‘radilar:</div></div>
 <div class="a card" data-t="34.6" data-a="up" data-r="-1" style="left:80px;top:430px;width:800px;padding:34px 40px">
  <div class="serif" style="font-size:52px;line-height:1.25">{rv([('«Yildek',34.74,'t-terra'),('uzun',35.17,'t-terra'),('kunda',35.4,'t-terra'),('bir',35.92),('kunlik',36.08),('namoz',36.38),('yetadimi?»',36.76)])}</div></div>
 <div class="a card" data-t="38.4" data-a="up" data-r="1" style="left:200px;top:780px;width:800px;padding:34px 40px;border:5px solid var(--green)">
  <div class="caps" style="margin-bottom:10px">Payg‘ambarimiz (s.a.v.)</div>
  <div class="serif" style="font-size:54px;line-height:1.25">{rv([('«Yo‘q,',38.47,'t-terra'),('vaqtini',39.02,'t-green'),('chamalab',39.43,'t-green'),('o‘qiysizlar»',39.81)])}</div></div>
</section>
<section class="scene" data-s="41.3" data-e="45.5">
 <div class="a hand cx" data-t="41.4" data-a="up" style="top:360px;font-size:70px;color:var(--green);white-space:nowrap">O‘ylab ko‘ring:</div>
 <div class="a cx" data-t="42.4" data-a="up" style="top:500px"><div class="card tape" style="width:860px;text-align:center;padding:34px"><div class="serif" style="font-size:56px;line-height:1.2">hatto eng katta <span class="t-terra">fitna</span> kunlarida ham</div></div></div>
 <div class="a cx" data-t="44.6" data-a="stamp" data-d=".3" data-r="-3" style="top:800px"><div class="stamp" style="font-size:76px;border-color:var(--green);color:var(--green)">NAMOZ TO‘XTAMAYDI</div></div>
</section>
<section class="scene" data-s="45.5" data-e="55.5">
 <div class="a hand cx" data-t="45.6" data-a="up" style="top:270px;font-size:66px;color:var(--terra);white-space:nowrap">Undan qanday himoyalanamiz?</div>
 <div class="a cx" data-t="48.9" data-a="pop" style="top:380px;display:flex;align-items:center;gap:26px">{shield.format(w=110,h=132,c="#2E6B5B")}<div class="serif" style="font-size:70px;white-space:nowrap">2 ta qalqon</div>{shield.format(w=110,h=132,c="#E2A63A")}</div>
 <div class="a" data-t="50.15" data-a="pop" data-r="-3" style="left:90px;top:570px"><div class="label">1-qalqon</div></div>
 <div class="a cx" data-t="50.9" data-a="pop" data-r="-.6" style="top:680px"><div class="card tape ayah">
  <div class="caps">Hadisi sharif · Imom Muslim, 809</div>
  <div class="arabic" style="font-size:52px;line-height:1.75;margin-top:12px;color:var(--green)">مَنْ حَفِظَ عَشْرَ آيَاتٍ مِنْ أَوَّلِ سُورَةِ الْكَهْفِ عُصِمَ مِنَ الدَّجَّالِ</div>
  <div class="serif" style="font-size:46px;line-height:1.25;margin-top:14px;color:var(--ink)">{rv([('«Kim',51.09),('Kahf',51.32,'t-green'),('surasining',51.62,'t-green'),('dastlabki',52.15,'t-green'),('o‘n',52.76,'t-terra'),('oyatini',52.98,'t-terra'),('yod',53.43),('olsa,',53.66),('Dajjoldan',54.19),('saqlanadi»',54.72,'t-green')])}</div></div></div>
</section>
<section class="scene" data-s="55.5" data-e="66.1">
 <div class="a" data-t="55.6" data-a="pop" data-r="-3" style="left:90px;top:280px;display:flex;align-items:center;gap:18px"><div class="label gold">2-qalqon</div>{shield.format(w=70,h=84,c="#E2A63A")}</div>
 <div class="a cx" data-t="56.5" data-a="pop" data-r="-1" style="top:420px"><div class="label">🕌 Har namozda · tashahhuddan keyin</div></div>
 <div class="a cx" data-t="58.0" data-a="pop" data-r="-.6" style="top:560px"><div class="card tape ayah">
  <div class="caps">Duo · Imom Muslim, 588</div>
  <div class="arabic" style="font-size:44px;line-height:1.8;margin-top:10px;color:var(--green)">اللَّهُمَّ إِنِّي أَعُوذُ بِكَ مِنْ عَذَابِ جَهَنَّمَ، وَمِنْ عَذَابِ الْقَبْرِ، وَمِنْ فِتْنَةِ الْمَحْيَا وَالْمَمَاتِ، وَمِنْ شَرِّ فِتْنَةِ الْمَسِيحِ الدَّجَّالِ</div>
  <div class="serif" style="font-size:42px;line-height:1.28;margin-top:16px;color:var(--ink)">{rv([('«Allohim,',58.6),('do‘zax',59.36),('azobidan,',59.77),('qabr',60.57),('azobidan,',60.91),('hayot',61.74),('va',62.08),('o‘lim',62.26),('fitnasidan',62.49),('va',63.32),('Dajjol',63.47,'t-terra'),('fitnasidan',63.92,'t-terra'),('Sendan',64.64,'t-green'),('panoh',65.06,'t-green'),('so‘rayman»',65.28,'t-green')])}</div></div></div>
</section>
<section class="scene" data-s="66.1" data-e="76.85">
 <div class="a hand cx" data-t="66.2" data-a="up" style="top:280px;font-size:62px;color:#8A847A;white-space:nowrap">qachon chiqishini bilmaymiz…</div>
 <div class="a cx" data-t="69.0" data-a="stamp" data-d=".3" data-r="-2" style="top:410px"><div class="stamp" style="font-size:64px;border-color:var(--green);color:var(--green)">QALQON BUGUNDAN</div></div>
 <div class="a cx" data-t="69.6" data-a="pop" data-f="4" style="top:600px">{shield.format(w=200,h=240,c="#2E6B5B")}</div>
 <div class="a" data-t="70.85" data-a="left" data-r="-2" style="left:70px;top:900px"><div class="chip" style="font-size:42px">📖 Kahfning 10 oyati</div></div>
 <div class="a" data-t="72.35" data-a="right" data-r="2" style="left:400px;top:1030px"><div class="chip" style="font-size:42px">🤲 namozdagi duo</div></div>
 <div class="a" data-t="74.2" data-a="left" data-r="-1.5" style="left:110px;top:1160px"><div class="chip" style="font-size:42px">📿 zikr qiluvchi qalb</div></div>
</section>
'''
extra=f'''<div class="a cx" data-t="76.95" data-a="up" data-o="85.95" style="top:300px;font:900 54px Nunito;color:var(--green);white-space:nowrap">Har kuni — birgalikda</div>
<div class="a cx" data-t="86.05" data-a="pop" style="top:290px;display:flex;gap:22px"><div class="chip" style="font-size:40px">📌 Saqlab qo‘ying</div><div class="a chip" data-t="87.5" data-a="pop" style="position:relative;font-size:40px">📤 Yaqinlaringizga yuboring</div></div>
<div class="a cx" data-t="81.7" data-a="pop" style="top:1220px"><div class="chip" style="font-size:42px;white-space:nowrap;border:4px solid var(--terra)">💬 Izohlarga <span class="t-terra" style="font-size:56px">«+»</span> qoldiring</div></div>
<div class="a hand cx" data-t="83.0" data-a="fade" style="top:1335px;font-size:48px;color:#8A847A">yoki</div>
'''
c=C.cta(tas=77.4,zikr=78.6,extra=extra,havola=83.5,btn=84.7)
c=c.replace('style="top:1250px"><div class="chip"','style="top:1400px"><div class="chip"').replace('style="top:1400px"><div style="background:var(--gold)','style="top:1530px"><div style="background:var(--gold)').replace('top:1560px;font:700','top:1690px;font:700')
c=c.replace('style="top:1070px"><div style="background:var(--terra)','style="top:1060px"><div style="background:var(--terra)')
s+=c+'''
<div id="sub" data-hide="78.5"><div id="subbox"></div></div></div>'''+C.TASBEH+'</body></html>'
open('/home/claude/reel10/index.html','w').write(HEAD+b+s)
print('ok')
