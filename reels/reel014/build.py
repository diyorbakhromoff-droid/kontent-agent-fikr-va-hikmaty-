import sys; sys.path.insert(0,'/home/claude')
import cta as C
exec(open('/home/claude/build4.py').read().split('# ---------- reel004 ----------')[0].split('import cta as C')[1])
C.SCENE_S='79.5'
b=bgs([(-1,9.8,'#DAE2E9'),(9.8,24.3,'#E3EBEE'),(24.3,32.9,'#CBD6DE'),(32.9,42.5,'#F3E9CF'),(42.5,53.4,'#DCE6DA'),(53.4,62.3,'#E5DDEB'),(62.3,69.0,'#F3E9CF'),(69.0,79.5,'#DAE2E9'),(79.5,999,'#F1E6D6')])
whale='''<svg width="{w}" height="{h}" viewBox="0 0 220 120"><path d="M20 70c0-30 40-52 90-52 46 0 78 20 88 42l18-18c-2 16-4 26-10 34 6 8 8 18 10 34l-18-18c-12 18-44 28-84 28-54 0-94-20-94-50z" fill="{c}"/><circle cx="56" cy="58" r="6" fill="#FBF7EE"/><path d="M36 84c20 10 50 12 76 6" stroke="#FBF7EE" stroke-width="4" fill="none" stroke-linecap="round" opacity=".6"/></svg>'''
waves='''<svg width="{w}" height="{h}" viewBox="0 0 400 60"><path d="M0 30c25-20 50-20 75 0s50 20 75 0 50-20 75 0 50 20 75 0 50-20 75 0 50 20 25 0" fill="none" stroke="{c}" stroke-width="8" stroke-linecap="round"/></svg>'''
ship='''<svg width="{w}" height="{h}" viewBox="0 0 160 130"><path d="M78 10v80" stroke="#4A453F" stroke-width="6"/><path d="M82 16l50 60H82z" fill="#FBF7EE" stroke="#4A453F" stroke-width="4"/><path d="M10 92h140l-22 30H32z" fill="#C4553B"/></svg>'''
def zbox(t,txt,bg,left,top,col='#FBF7EE'):
    return f'<div class="a" data-t="{t}" data-a="pop" style="left:{left}px;top:{top}px"><div style="width:300px;height:300px;border-radius:16px;background:{bg};display:flex;align-items:center;justify-content:center;text-align:center;box-shadow:0 14px 30px rgba(20,30,40,.25)"><div style="font:900 44px Nunito;color:{col};line-height:1.15">{txt}</div></div></div>'
s=f'''
<div id="banner" data-s="9.8" data-e="79.3">Baliq qornidan qutqargan duo</div>
<section class="scene" data-s="-1" data-e="9.8">
 <div class="a cx" data-t="0.05" data-a="fade" style="top:300px">{waves.format(w=900,h=80,c="#3F8A73")}</div>
 <div class="a cx" data-t="1.8" data-a="up" data-f="4" style="top:420px">{whale.format(w=520,h=284,c="#2E6B5B")}</div>
 <div class="a hand cx" data-t="2.5" data-a="fade" style="top:730px;font-size:60px;color:#5B6B74;white-space:nowrap">dengiz tubida, baliq qornida…</div>
 <div class="a cx" data-t="4.4" data-a="stamp" data-d=".3" data-r="-3" style="top:840px"><div class="stamp" style="font-size:100px;border-color:var(--green);color:var(--green)">1 TA DUO</div></div>
 <div class="a cx" data-t="6.6" data-a="up" style="top:1060px"><div class="card tape" style="width:880px;text-align:center;padding:30px"><div class="serif" style="font-size:48px;line-height:1.2">bugun ham <span class="t-terra">ijobat bo‘ladigan</span> eng kuchli duolardan</div></div></div>
</section>
<section class="scene" data-s="9.8" data-e="24.3">
 <div class="a cx" data-t="10.2" data-a="pop" style="top:290px"><div class="label" style="font-size:52px">Yunus alayhissalom</div></div>
 <div class="a" data-t="13.1" data-a="left" data-r="-2" style="left:80px;top:430px"><div class="chip" style="font-size:44px">✗ qavmi rad etdi</div></div>
 <div class="a" data-t="16.5" data-a="right" style="left:470px;top:410px">{ship.format(w=220,h=179)}</div>
 <div class="a hand" data-t="17.1" data-a="fade" style="left:100px;top:570px;font-size:54px;color:#5B6B74;white-space:nowrap">odamlar to‘la kema…</div>
 <div class="a cx" data-t="18.2" data-a="up" style="top:700px"><div class="card tape ayah" style="width:880px;padding:30px 36px"><div class="caps">Soffot surasi · 141–142-oyatlar</div><div class="serif" style="font-size:50px;line-height:1.25;margin-top:12px">{rv([('qur’a',19.67,'t-terra'),('unga',20.14,'t-terra'),('chiqdi…',20.33,'t-terra'),('dengizga',21.05),('tashlandi',21.53)])}</div></div></div>
 <div class="a cx" data-t="22.9" data-a="drop" style="top:1010px">{whale.format(w=380,h=207,c="#2E6B5B")}</div>
</section>
<section class="scene" data-s="24.3" data-e="32.9">
 <div class="a hand cx" data-t="24.35" data-a="up" style="top:290px;font-size:66px;color:#3E4C55;white-space:nowrap">Endi tasavvur qiling…</div>
 <div class="a cx" data-t="25.5" data-a="fade" style="top:390px"><div class="caps" style="color:#3E4C55">mufassirlar aytadi:</div></div>
 {zbox(26.85,'tun<br>zulmati','#5B6B74',70,480)}
 {zbox(27.9,'dengiz<br>zulmati','#3E4C55',390,560)}
 {zbox(29.2,'baliq qorni<br>zulmati','#22292E',700,640)}
 <div class="a cx" data-t="30.0" data-a="stamp" data-d=".3" style="top:1010px"><div class="serif" style="font-size:96px;color:#22292E;white-space:nowrap">3 zulmat</div></div>
</section>
<section class="scene" data-s="32.9" data-e="42.5">
 <div class="a cx" data-t="30.8" data-a="fade" style="top:270px;font:900 46px Nunito;color:#5B6B74;white-space:nowrap">shu zulmatlar ichida u nido qildi:</div>
 <div class="a cx" data-t="32.9" data-a="pop" data-r="-.6" style="top:360px"><div class="card tape ayah">
  <div class="caps">Anbiyo surasi · 87-oyat</div>
  <div class="arabic" style="font-size:70px;line-height:1.75;margin-top:12px;color:var(--green)">لَا إِلَٰهَ إِلَّا أَنتَ سُبْحَانَكَ إِنِّي كُنتُ مِنَ الظَّالِمِينَ</div>
  <div class="hand" style="font-size:52px;line-height:1.2;margin-top:10px;color:var(--terra)">{rv([('La',32.95),('ilaha',33.31),('illa',33.82),('anta,',34.18),('subhanaka,',34.91),('inni',36.0),('kuntu',36.36),('minaz-zolimin',36.73)])}</div>
  <div class="serif" style="font-size:44px;line-height:1.25;margin-top:14px;color:var(--ink)">{rv([('«Sendan',37.94),('o‘zga',38.33),('iloh',38.62),('yo‘q,',38.91),('Sen',39.42,'t-green'),('poksan,',39.64,'t-green'),('men',40.44),('o‘zimga',40.58),('zulm',40.95,'t-terra'),('qiluvchilardan',41.2,'t-terra'),('bo‘ldim»',41.82)])}</div></div></div>
</section>
<section class="scene" data-s="42.5" data-e="53.4">
 <div class="a cx" data-t="42.55" data-a="pop" data-r="-.6" style="top:290px"><div class="card tape ayah">
  <div class="caps">Anbiyo surasi · 88-oyat</div>
  <div class="arabic" style="font-size:56px;line-height:1.75;margin-top:12px;color:var(--green)">فَاسْتَجَبْنَا لَهُ وَنَجَّيْنَاهُ مِنَ الْغَمِّ وَكَذَٰلِكَ نُنجِي الْمُؤْمِنِينَ</div>
  <div class="serif" style="font-size:46px;line-height:1.25;margin-top:14px;color:var(--ink)">{rv([('«Biz',43.53),('uning',43.82),('duosini',44.0),('ijobat',44.44,'t-green'),('qildik',44.84,'t-green'),('va',45.31),('uni',45.49),('g‘amdan',45.64),('qutqardik.',46.04),('Mo‘minlarni',46.8,'t-terra'),('ham',47.38,'t-terra'),('shunday',47.53),('qutqaramiz»',47.82)])}</div></div></div>
 <div class="a cx" data-t="49.5" data-a="stamp" data-d=".3" data-r="-3" style="top:990px"><div class="stamp" style="font-size:80px">MO‘MINLARNI HAM</div></div>
 <div class="a cx" data-t="51.4" data-a="up" style="top:1180px"><div class="chip" style="font-size:42px">faqat Yunus (a.s.) uchun emas</div></div>
</section>
<section class="scene" data-s="53.4" data-e="62.3">
 <div class="a hand cx" data-t="53.45" data-a="up" style="top:280px;font-size:62px;color:var(--terra);white-space:nowrap">eng ta’sirli oyat:</div>
 <div class="a cx" data-t="55.3" data-a="pop" data-r="-.6" style="top:390px"><div class="card tape ayah">
  <div class="caps">Soffot surasi · 143–144-oyatlar</div>
  <div class="arabic" style="font-size:52px;line-height:1.8;margin-top:12px;color:var(--green)">فَلَوْلَا أَنَّهُ كَانَ مِنَ الْمُسَبِّحِينَ لَلَبِثَ فِي بَطْنِهِ إِلَىٰ يَوْمِ يُبْعَثُونَ</div>
  <div class="serif" style="font-size:44px;line-height:1.25;margin-top:14px;color:var(--ink)">{rv([('«Agar',55.47),('u',55.71),('tasbeh',55.85,'t-green'),('aytuvchilardan',56.29,'t-green'),('bo‘lmaganida,',56.95),('qayta',57.85),('tiriladigan',58.18),('kungacha',58.76,'t-terra'),('uning',59.42),('qornida',59.6),('qolib',60.0),('ketardi»',60.29)])}</div></div></div>
 <div class="a cx" data-t="61.05" data-a="stamp" data-d=".3" data-r="-3" style="top:1000px"><div class="stamp" style="font-size:72px;border-color:var(--green);color:var(--green)">UNI ZIKR QUTQARDI</div></div>
</section>
<section class="scene" data-s="62.3" data-e="69.0">
 <div class="a cx" data-t="62.35" data-a="pop" data-r="-.6" style="top:340px"><div class="card tape ayah">
  <div class="caps">Hadisi sharif · Imom Termiziy, 3505</div>
  <div class="arabic" style="font-size:54px;line-height:1.75;margin-top:12px;color:var(--green)">لَمْ يَدْعُ بِهَا رَجُلٌ مُسْلِمٌ فِي شَيْءٍ قَطُّ إِلَّا اسْتَجَابَ اللَّهُ لَهُ</div>
  <div class="serif" style="font-size:46px;line-height:1.25;margin-top:14px;color:var(--ink)">{rv([('«Qaysi',63.66),('musulmon',64.0),('biror',64.51),('narsa',64.84),('haqida',65.09),('shu',65.45,'t-green'),('duo',65.64,'t-green'),('bilan',65.89),('duo',66.11),('qilsa,',66.29),('Alloh',66.91),('albatta',67.38,'t-terra'),('uni',67.82),('ijobat',68.0,'t-terra'),('qiladi»',68.36,'t-terra')])}</div></div></div>
</section>
<section class="scene" data-s="69.0" data-e="79.5">
 <div class="a hand cx" data-t="69.05" data-a="up" style="top:280px;font-size:60px;color:#3E4C55;white-space:nowrap">hayotingizdagi zulmat…</div>
 <div class="a" data-t="71.15" data-a="pop" data-r="-3" style="left:80px;top:400px"><div class="chip" style="font-size:44px;background:#5B6B74;color:#fff">💸 qarz</div></div>
 <div class="a" data-t="71.7" data-a="pop" data-r="2" style="left:380px;top:420px"><div class="chip" style="font-size:44px;background:#3E4C55;color:#fff">🤒 kasallik</div></div>
 <div class="a" data-t="72.6" data-a="pop" data-r="-2" style="left:760px;top:400px"><div class="chip" style="font-size:44px;background:#22292E;color:#fff">😔 g‘am</div></div>
 <div class="a cx" data-t="73.2" data-a="up" style="top:580px"><div class="card tape" style="width:900px;text-align:center;padding:32px"><div class="caps">shu duoni yod oling</div><div class="arabic" style="font-size:58px;line-height:1.7;margin-top:8px;color:var(--green)">لَا إِلَٰهَ إِلَّا أَنتَ سُبْحَانَكَ إِنِّي كُنتُ مِنَ الظَّالِمِينَ</div></div></div>
 <div class="a cx" data-t="77.7" data-a="stamp" data-d=".3" data-r="-3" style="top:960px"><div class="stamp" style="font-size:90px;border-color:var(--green);color:var(--green)">NAJOT</div></div>
</section>
'''
extra=f'''<div class="a cx" data-t="79.55" data-a="up" data-o="89.4" style="top:300px;font:900 54px Nunito;color:var(--green);white-space:nowrap">Zikr qiluvchilardan bo‘ling</div>
<div class="a cx" data-t="89.5" data-a="pop" style="top:290px;display:flex;gap:22px"><div class="chip" style="font-size:40px">📌 Saqlab qo‘ying</div><div class="a chip" data-t="90.9" data-a="pop" style="position:relative;font-size:40px">📤 Yaqiningizga yuboring</div></div>
<div class="a cx" data-t="85.35" data-a="pop" style="top:1220px"><div class="chip" style="font-size:42px;white-space:nowrap;border:4px solid var(--terra)">💬 Izohlarga <span class="t-terra" style="font-size:56px">«+»</span> qoldiring</div></div>
<div class="a hand cx" data-t="86.7" data-a="fade" style="top:1335px;font-size:48px;color:#8A847A">yoki</div>
'''
c=C.cta(tas=80.0,zikr=82.4,extra=extra,havola=87.1,btn=88.4)
c=c.replace('style="top:1250px"><div class="chip"','style="top:1400px"><div class="chip"').replace('style="top:1400px"><div style="background:var(--gold)','style="top:1530px"><div style="background:var(--gold)').replace('top:1560px;font:700','top:1690px;font:700')
c=c.replace('style="top:1070px"><div style="background:var(--terra)','style="top:1060px"><div style="background:var(--terra)')
s+=c+'''
<div id="sub" data-hide="82.3"><div id="subbox"></div></div></div>'''+C.TASBEH+'</body></html>'
open('/home/claude/reel14/index.html','w').write(HEAD+b+s)
print('ok')
