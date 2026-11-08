import sys; sys.path.insert(0,'/home/claude')
import cta as C
exec(open('/home/claude/build4.py').read().split('# ---------- reel004 ----------')[0].split('import cta as C')[1])
C.SCENE_S='76.2'
b=bgs([(-1,11.3,'#F1E6D6'),(11.3,17.0,'#DCE6DA'),(17.0,23.75,'#F3E9CF'),(23.75,32.0,'#DAE2E9'),(32.0,42.3,'#E5DDEB'),(42.3,50.2,'#F6E1D3'),(50.2,60.8,'#DCE6DA'),(60.8,64.4,'#DAE2E9'),(64.4,70.45,'#F3E9CF'),(70.45,76.2,'#E5DDEB'),(76.2,999,'#F1E6D6')])
P='<svg width="{w}" height="{h}" viewBox="0 0 60 94"><circle cx="30" cy="18" r="16" fill="{c}"/><path d="M4 92c0-26 10-44 26-44s26 18 26 44z" fill="{c}"/></svg>'
scroll='''<svg width="{w}" height="{h}" viewBox="0 0 120 140"><rect x="18" y="16" width="84" height="108" rx="6" fill="#FBF7EE" stroke="#2E6B5B" stroke-width="5"/><rect x="10" y="8" width="100" height="16" rx="8" fill="#E2A63A"/><rect x="10" y="116" width="100" height="16" rx="8" fill="#E2A63A"/><path d="M34 46h52M34 62h52M34 78h40M34 94h46" stroke="#C9C2B6" stroke-width="5" stroke-linecap="round"/></svg>'''
key='''<svg width="{w}" height="{h}" viewBox="0 0 120 60"><circle cx="26" cy="30" r="20" fill="none" stroke="{c}" stroke-width="10"/><path d="M46 30h66M92 30v18M106 30v14" stroke="{c}" stroke-width="10" stroke-linecap="round"/></svg>'''
door='''<svg width="{w}" height="{h}" viewBox="0 0 100 150"><rect x="8" y="6" width="84" height="140" rx="4" fill="#C4553B"/><rect x="18" y="16" width="64" height="56" rx="3" fill="#D9705A"/><rect x="18" y="80" width="64" height="56" rx="3" fill="#D9705A"/><circle cx="74" cy="80" r="6" fill="#E2A63A"/></svg>'''
bird='''<svg width="{w}" height="{h}" viewBox="0 0 120 80"><path d="M10 44c18-4 30 2 40 12 6-22 24-40 54-44-10 10-14 22-14 34 0 18-16 30-38 30-20 0-34-14-42-32z" fill="{c}"/><circle cx="84" cy="40" r="4" fill="#FBF7EE"/><path d="M98 40l16 4-16 6z" fill="#E2A63A"/></svg>'''
heart='<svg width="{w}" height="{h}" viewBox="0 0 100 90"><path d="M50 86C20 64 4 48 4 28 4 14 15 4 28 4c9 0 17 5 22 13C55 9 63 4 72 4c13 0 24 10 24 24 0 20-16 36-46 58z" fill="#C4553B"/></svg>'
fam=''.join(f'<div style="position:relative">{P.format(w=w,h=int(w*1.56),c=c)}</div>' for w,c in [(70,'#2E6B5B'),(56,'#E2A63A'),(70,'#C4553B'),(48,'#3F8A73'),(62,'#2E6B5B')])

s=f'''
<div id="banner" data-s="11.3" data-e="76.0">Rizq yozilgan bo‘lsa, nega harakat qilaman?</div>
<section class="scene" data-s="-1" data-e="11.3">
 <div class="a hand cx" data-t="0.3" data-a="up" style="top:290px;font-size:66px;color:var(--green);white-space:nowrap">hali onangiz qornida ekaningizda…</div>
 <div class="a cx" data-t="2.1" data-a="pop" data-r="-1.5" style="top:410px"><div class="card tape" style="width:800px;padding:30px 36px;display:flex;align-items:center;gap:30px">{scroll.format(w=150,h=175)}<div><div class="serif" style="font-size:96px;line-height:1;color:var(--green)">RIZQINGIZ</div><div style="font:900 50px Nunito;margin-top:8px">yozib qo‘yilgan</div></div></div></div>
 <div class="a" data-t="4.75" data-a="left" data-r="-2" style="left:110px;top:790px"><div class="chip" style="font-size:52px;color:var(--green)">💰 keng</div></div>
 <div class="a" data-t="5.75" data-a="right" data-r="2" style="left:620px;top:790px"><div class="chip" style="font-size:52px;color:var(--terra)">🪙 tor</div></div>
 <div class="a hand cx" data-t="3.64" data-a="fade" style="top:660px;font-size:62px;color:#8A847A;white-space:nowrap">unda nega birovniki…</div>
 <div class="a hand cx" data-t="6.8" data-a="up" data-r="-2" style="top:1010px;font-size:80px;color:var(--terra);white-space:nowrap">Ko‘paytirsa bo‘ladimi?</div>
 <div class="a cx" data-t="8.1" data-a="stamp" data-d=".3" data-r="-4" style="top:1150px"><div class="stamp" style="border-color:var(--green);color:var(--green)">BO‘LADI!</div></div>
</section>
<section class="scene" data-s="11.3" data-e="17.0">
 <div class="a cx" data-t="11.4" data-a="pop" data-r="-.6" style="top:300px"><div class="card tape ayah" style="width:900px">
  <div class="caps">Hadisi sharif · Imom Buxoriy, 3208</div>
  <div class="serif" style="font-size:56px;line-height:1.25;margin-top:22px">{rv([('Ona',11.42),('qornidagi',11.64),('bolaga',12.22),('farishta',12.58,'t-green'),('yuboriladi',12.91),('va',13.67),('yozib',15.89),('qo‘yiladi:',16.17)])}</div></div></div>
 <div class="a" data-t="14.05" data-a="pop" data-r="-3" style="left:80px;top:800px"><div class="label">amali</div></div>
 <div class="a" data-t="14.8" data-a="stamp" data-d=".3" data-r="2" style="left:360px;top:780px"><div class="label gold" style="font-size:64px;padding:26px 40px">RIZQI</div></div>
 <div class="a" data-t="15.55" data-a="pop" data-r="3" style="left:730px;top:800px"><div class="label terra">ajali</div></div>
 <div class="a cx" data-t="12.6" data-a="pop" data-f="4" style="top:1000px">{scroll.format(w=200,h=233)}</div>
</section>
<section class="scene" data-s="17.0" data-e="23.75">
 <div class="a" data-t="17.05" data-a="left" style="left:90px;top:300px"><div class="chip" style="font-size:50px">Rizq <span class="t-green">— yozilgan ✓</span></div></div>
 <div class="a" data-t="19.3" data-a="up" style="left:90px;top:470px;display:flex;align-items:center;gap:34px">{door.format(w=150,h=225)}<div class="serif" style="font-size:60px;line-height:1.2">qaysi <span class="t-terra">eshikdan</span><br>kirib keladi?</div></div>
 <div class="a cx" data-t="21.3" data-a="stamp" data-d=".3" data-r="-2" style="top:800px"><div class="stamp" style="font-size:66px">AMALINGIZGA BOG‘LIQ</div></div>
 <div class="a cx" data-t="22.7" data-a="up" style="top:1010px;display:flex;align-items:center;gap:26px"><div class="serif" style="font-size:110px;color:var(--green)">3</div><div style="font:900 64px Nunito">ta kalit</div></div>
 <div class="a cx" data-t="22.98" data-a="pop" style="top:1170px;display:flex;gap:30px">{key.format(w=160,h=80,c="#2E6B5B")}{key.format(w=160,h=80,c="#E2A63A")}{key.format(w=160,h=80,c="#C4553B")}</div>
</section>
<section class="scene" data-s="23.75" data-e="32.0">
 <div class="a" data-t="23.8" data-a="pop" data-r="-3" style="left:90px;top:290px;display:flex;align-items:center;gap:22px"><div class="label">1-kalit</div>{key.format(w=120,h=60,c="#2E6B5B")}</div>
 <div class="a" data-t="24.68" data-a="stamp" data-d=".3" style="left:560px;top:270px"><div class="serif" style="font-size:110px;line-height:1;color:var(--green)">TAQVO</div></div>
 <div class="a cx" data-t="25.4" data-a="pop" data-r="-.6" style="top:470px"><div class="card tape ayah">
  <div class="caps">Taloq surasi · 2–3-oyatlar</div>
  <div class="arabic" style="font-size:62px;line-height:1.8;margin-top:14px;color:var(--green)">وَمَن يَتَّقِ اللَّهَ يَجْعَل لَّهُ مَخْرَجًا<br>وَيَرْزُقْهُ مِنْ حَيْثُ لَا يَحْتَسِبُ</div></div></div>
 <div class="a card cx" data-t="26.3" data-a="up" data-r=".6" style="top:930px;width:900px;text-align:center;padding:34px 40px">
  <div class="serif" style="font-size:50px;line-height:1.25">{rv([('«Kim',26.42),('Allohdan',26.55,'t-green'),('qo‘rqsa,',27.05,'t-green'),('U',27.75),('unga',27.93),('chiqish',28.14,'t-terra'),('yo‘lini',28.44,'t-terra'),('qilib',28.76),('beradi',29.02),('va',29.53),('uni',29.67),('o‘ylamagan',29.96,'t-terra'),('tomonidan',30.51,'t-terra'),('rizqlantiradi.»',31.05)])}</div></div>
</section>
<section class="scene" data-s="32.0" data-e="42.3">
 <div class="a" data-t="32.05" data-a="pop" data-r="-3" style="left:70px;top:290px;display:flex;align-items:center;gap:22px"><div class="label gold">2-kalit</div>{key.format(w=120,h=60,c="#E2A63A")}</div>
 <div class="a" data-t="33.04" data-a="stamp" data-d=".3" style="left:470px;top:278px"><div class="serif" style="font-size:96px;line-height:1;color:var(--green)">ISTIG‘FOR</div></div>
 <div class="a cx" data-t="33.9" data-a="pop" data-r="-.6" style="top:460px"><div class="card tape ayah">
  <div class="caps">Nuh surasi · 10–12-oyatlar</div>
  <div class="arabic" style="font-size:66px;line-height:1.8;margin-top:14px;color:var(--green)">فَقُلْتُ اسْتَغْفِرُوا رَبَّكُمْ إِنَّهُ كَانَ غَفَّارًا</div></div></div>
 <div class="a card cx" data-t="35.7" data-a="up" data-r=".6" style="top:820px;width:900px;text-align:center;padding:32px 40px">
  <div class="serif" style="font-size:52px;line-height:1.25">{rv([('«Robbingizdan',35.8),('mag‘firat',36.36,'t-green'),('so‘rang.»',36.8,'t-green')])}</div></div>
 <div class="a" data-t="38.4" data-a="pop" data-r="-3" style="left:70px;top:1080px"><div class="chip" style="font-size:44px">🌧 yomg‘ir</div></div>
 <div class="a" data-t="39.78" data-a="pop" data-r="2" style="left:390px;top:1100px"><div class="chip" style="font-size:44px">💰 mol-mulk</div></div>
 <div class="a" data-t="40.62" data-a="pop" data-r="-2" style="left:740px;top:1080px"><div class="chip" style="font-size:44px">👨‍👩‍👧 farzand</div></div>
</section>
<section class="scene" data-s="42.3" data-e="50.2">
 <div class="a" data-t="42.35" data-a="pop" data-r="-3" style="left:70px;top:290px;display:flex;align-items:center;gap:22px"><div class="label terra">3-kalit</div>{key.format(w=120,h=60,c="#C4553B")}</div>
 <div class="a cx" data-t="43.3" data-a="stamp" data-d=".3" style="top:420px"><div class="serif" style="font-size:100px;line-height:1;color:var(--terra)">QARINDOSHLIK</div></div>
 <div class="a cx" data-t="43.6" data-a="up" style="top:560px;display:flex;align-items:flex-end;gap:14px">{fam}</div>
 <div class="a cx" data-t="44.3" data-a="pop" data-r="-.6" style="top:720px"><div class="card tape ayah">
  <div class="caps">Hadisi sharif · Imom Buxoriy, 5986</div>
  <div class="arabic" style="font-size:52px;line-height:1.8;margin-top:12px;color:var(--green)">مَنْ سَرَّهُ أَنْ يُبْسَطَ لَهُ فِي رِزْقِهِ أَوْ يُنْسَأَ لَهُ فِي أَثَرِهِ فَلْيَصِلْ رَحِمَهُ</div>
  <div class="serif" style="font-size:46px;line-height:1.25;margin-top:20px;color:var(--ink)">{rv([('«Kim',45.6),('rizqi',45.82,'t-green'),('kengayishini',46.07,'t-green'),('va',46.84),('umri',47.05),('uzayishini',47.34),('istasa,',47.78),('qarindoshlik',48.4,'t-terra'),('aloqasini',49.02,'t-terra'),('bog‘lasin.»',49.49,'t-terra')])}</div></div></div>
</section>
<section class="scene" data-s="50.2" data-e="60.8">
 <div class="a" data-t="50.3" data-a="up" style="left:90px;top:290px;font:900 56px Nunito;white-space:nowrap">…va hammasi</div>
 <div class="a" data-t="51.45" data-a="stamp" data-d=".3" data-r="-3" style="left:470px;top:270px"><div class="stamp" style="font-size:76px;border-color:var(--green);color:var(--green)">+ HARAKAT</div></div>
 <div class="a cx" data-t="52.7" data-a="pop" data-r="-.6" style="top:470px"><div class="card tape ayah">
  <div class="caps">Hadisi sharif · Imom Termiziy, 2344</div>
  <div class="arabic" style="font-size:58px;line-height:1.8;margin-top:12px;color:var(--green)">لَرَزَقَكُمْ كَمَا يَرْزُقُ الطَّيْرَ تَغْدُو خِمَاصًا وَتَرُوحُ بِطَانًا</div>
  <div class="serif" style="font-size:46px;line-height:1.25;margin-top:20px;color:var(--ink)">{rv([('«Agar',52.8),('Allohga',53.09),('haqiqiy',53.6,'t-green'),('tavakkul',54.0,'t-green'),('qilsangiz,',54.44),('qushlarni',55.17),('rizqlantirganidek',55.64),('sizni',56.51),('ham',56.84),('rizqlantirardi»',57.02)])}</div></div></div>
 <div class="a" data-t="58.25" data-a="left" style="left:80px;top:1130px;display:flex;align-items:center;gap:14px">{bird.format(w=120,h=80,c="#9A9388")}<div style="font:900 42px Nunito;color:#8A847A;white-space:nowrap">ertalab och</div></div>
 <div class="a" data-t="59.35" data-a="right" style="left:560px;top:1130px;display:flex;align-items:center;gap:14px">{bird.format(w=120,h=80,c="#2E6B5B")}<div style="font:900 42px Nunito;color:var(--green);white-space:nowrap">kechqurun to‘q</div></div>
</section>
<section class="scene" data-s="60.8" data-e="64.4">
 <div class="a hand cx" data-t="60.9" data-a="up" style="top:320px;font-size:72px;color:var(--terra);white-space:nowrap">E’tibor bering:</div>
 <div class="a cx" data-t="61.75" data-a="fade" style="top:480px"><div style="position:relative;font:900 66px Nunito;color:#9A9388;white-space:nowrap">uyada kutib o‘tirmaydi<div class="strike" data-t="62.9"></div></div></div>
 <div class="a cx" data-t="63.4" data-a="drop" style="top:640px">{bird.format(w=330,h=220,c="#2E6B5B")}</div>
 <div class="a cx" data-t="63.6" data-a="stamp" data-d=".3" data-r="-3" style="top:920px"><div class="stamp" style="border-color:var(--green);color:var(--green)">UCHIB CHIQADI</div></div>
</section>
<section class="scene" data-s="64.4" data-e="70.45">
 <div class="a cx" data-t="64.45" data-a="pop" data-r="-1" style="top:300px"><div class="card tape" style="width:880px;text-align:center;padding:40px">
  <div class="serif" style="font-size:62px;line-height:1.2">Rizqingizni <span class="t-green">hech kim</span> ololmaydi</div></div></div>
 <div class="a cx" data-t="66.9" data-a="up" style="top:600px">{door.format(w=180,h=270)}</div>
 <div class="a" data-t="68.0" data-a="stamp" data-d=".3" data-r="-4" style="left:70px;top:940px"><div class="stamp" style="font-size:70px;border-color:var(--green);color:var(--green)">OCHASIZ</div></div>
 <div class="a hand" data-t="68.7" data-a="fade" style="left:470px;top:1110px;font-size:60px;color:#8A847A">yoki</div>
 <div class="a" data-t="69.6" data-a="stamp" data-d=".3" data-r="4" style="left:610px;top:940px"><div class="stamp" style="font-size:70px">YOPASIZ</div></div>
</section>
<section class="scene" data-s="70.45" data-e="76.2">
 <div class="a hand cx" data-t="70.6" data-a="up" style="top:300px;font-size:68px;color:var(--green);white-space:nowrap">eng oson kalit —</div>
 <div class="a cx" data-t="71.75" data-a="pop" data-f="4" style="top:420px">{key.format(w=360,h=180,c="#E2A63A")}</div>
 <div class="a cx" data-t="73.7" data-a="stamp" data-d=".3" data-r="-2" style="top:660px"><div class="serif" style="font-size:110px;color:var(--terra);white-space:nowrap">tilingizda</div></div>
 <div class="a" data-t="74.6" data-a="left" data-r="-3" style="left:110px;top:880px"><div class="label" style="font-size:56px">Istig‘for</div></div>
 <div class="a" data-t="75.55" data-a="right" data-r="3" style="left:590px;top:880px"><div class="label gold" style="font-size:56px">Zikr</div></div>
</section>
'''
extra=f'''<div class="a cx" data-t="76.3" data-a="up" data-o="89.75" style="top:300px;font:900 54px Nunito;color:var(--green);white-space:nowrap">Har kuni — birgalikda</div>
<div class="a cx" data-t="89.9" data-a="pop" style="top:290px;display:flex;gap:22px"><div class="chip" style="font-size:40px">📌 Saqlab qo‘ying</div><div class="a chip" data-t="91.3" data-a="pop" style="position:relative;font-size:40px">📤 Yaqiningizga yuboring</div></div>
<div class="a cx" data-t="85.7" data-a="pop" style="top:1220px"><div class="chip" style="font-size:42px;white-space:nowrap;border:4px solid var(--terra)">💬 Izohlarga <span class="t-terra" style="font-size:56px">«+»</span> qoldiring</div></div>
<div class="a hand cx" data-t="87.1" data-a="fade" style="top:1335px;font-size:48px;color:#8A847A">yoki</div>
'''
c=C.cta(tas=80.35,zikr=78.45,extra=extra,havola=87.45,btn=88.6)
c=c.replace('style="top:1250px"><div class="chip"','style="top:1400px"><div class="chip"').replace('style="top:1400px"><div style="background:var(--gold)','style="top:1530px"><div style="background:var(--gold)').replace('top:1560px;font:700','top:1690px;font:700')
c=c.replace('style="top:1070px"><div style="background:var(--terra)','style="top:1060px"><div style="background:var(--terra)')
s+=c+'''
<div id="sub" data-hide="78.3"><div id="subbox"></div></div></div>'''+C.TASBEH+'</body></html>'
open('/home/claude/reel8/index.html','w').write(HEAD+b+s)
print('ok')
