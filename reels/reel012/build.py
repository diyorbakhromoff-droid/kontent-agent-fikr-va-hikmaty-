import sys; sys.path.insert(0,'/home/claude')
import cta as C
exec(open('/home/claude/build4.py').read().split('# ---------- reel004 ----------')[0].split('import cta as C')[1])
C.SCENE_S='76.7'
b=bgs([(-1,7.25,'#F1E6D6'),(7.25,28.7,'#F3E9CF'),(28.7,33.45,'#DAE2E9'),(33.45,39.9,'#DCE6DA'),(39.9,46.7,'#F6E1D3'),(46.7,50.7,'#F3E9CF'),(50.7,60.3,'#E5DDEB'),(60.3,66.7,'#DCE6DA'),(66.7,76.7,'#DAE2E9'),(76.7,999,'#F1E6D6')])
def imom(name,t,left,top,col,r=0):
    return f'<div class="a" data-t="{t}" data-a="pop" data-r="{r}" style="left:{left}px;top:{top}px"><div class="card" style="padding:22px 30px;text-align:center;border-top:10px solid {col}"><div class="caps" style="color:#8A847A">Imom</div><div class="serif" style="font-size:52px;white-space:nowrap">{name}</div></div></div>'
arrow='<svg width="70" height="90" viewBox="0 0 70 90"><path d="M35 5v60" stroke="#C4553B" stroke-width="8" stroke-linecap="round"/><path d="M12 50l23 30 23-30" fill="none" stroke="#C4553B" stroke-width="8" stroke-linecap="round" stroke-linejoin="round"/></svg>'
s=f'''
<div id="banner" data-s="7.25" data-e="76.5">Qur’on bitta — mazhab nega to‘rtta?</div>
<section class="scene" data-s="-1" data-e="7.25">
 <div class="a" data-t="0.07" data-a="left" data-r="-1.5" style="left:110px;top:290px"><div class="chip" style="font-size:54px">📖 Qur’on — <span class="t-green">&nbsp;bitta</span></div></div>
 <div class="a" data-t="1.28" data-a="right" data-r="1.5" style="left:250px;top:430px"><div class="chip" style="font-size:54px">🌙 Payg‘ambar — <span class="t-green">&nbsp;bitta</span></div></div>
 <div class="a" data-t="2.56" data-a="left" data-r="-1" style="left:150px;top:570px"><div class="chip" style="font-size:54px">🕌 Namoz — <span class="t-green">&nbsp;bitta</span></div></div>
 <div class="a cx" data-t="4.2" data-a="stamp" data-d=".35" data-r="-3" style="top:760px"><div class="stamp" style="font-size:110px">4 MAZHAB?</div></div>
 <div class="a hand cx" data-t="5.9" data-a="up" style="top:980px;font-size:76px;color:#8A847A;white-space:nowrap">bu bo‘linish emasmi?</div>
</section>
<section class="scene" data-s="7.25" data-e="28.7">
 <div class="a" data-t="7.3" data-a="pop" data-r="-2" style="left:80px;top:270px;display:flex;gap:16px;align-items:center"><div class="label">Javobi — bitta voqeada</div><div class="caps" style="white-space:nowrap">Buxoriy, 946</div></div>
 <div class="a hand" data-t="9.36" data-a="fade" style="left:90px;top:380px;font-size:50px;color:#8A847A;white-space:nowrap">Ahzob jangidan keyin…</div>
 <div class="a cx" data-t="12.1" data-a="up" data-r="-.5" style="top:460px"><div class="card tape" style="width:900px;padding:30px 36px;text-align:center"><div class="caps" style="margin-bottom:10px">Payg‘ambarimiz (s.a.v.)</div><div class="serif" style="font-size:46px;line-height:1.25">{rv([('«Hech',12.24),('kim',12.48),('asr',12.8,'t-terra'),('namozini',13.04,'t-terra'),('Bani',13.64,'t-green'),('Qurayzaga',13.92,'t-green'),('yetmaguncha',14.48),('o‘qimasin»',15.15)])}</div></div></div>
 <div class="a cx" data-t="16.48" data-a="pop" style="top:750px"><div class="chip" style="font-size:40px">🕒 yo‘lda asr vaqti kirdi</div></div>
 <div class="a" data-t="18.1" data-a="left" data-r="-2" style="left:50px;top:880px"><div class="card" style="width:470px;padding:24px 26px;border-top:10px solid var(--green)"><div class="caps">1-guruh</div><div class="serif" style="font-size:40px;line-height:1.2;margin-top:6px">«Yetib borganda o‘qiymiz»</div></div></div>
 <div class="a" data-t="20.6" data-a="right" data-r="2" style="left:560px;top:880px"><div class="card" style="width:470px;padding:24px 26px;border-top:10px solid var(--gold)"><div class="caps" style="color:var(--gold)">2-guruh</div><div class="serif" style="font-size:40px;line-height:1.2;margin-top:6px">«Shoshilishimizni istaganlar» — yo‘lda o‘qidi</div></div></div>
 <div class="a cx" data-t="27.1" data-a="stamp" data-d=".3" data-r="-2" style="top:1190px"><div class="stamp" style="font-size:52px;border-color:var(--green);color:var(--green)">HECH BIRINI KOYIMADILAR</div></div>
</section>
<section class="scene" data-s="28.7" data-e="33.45">
 <div class="a hand cx" data-t="28.75" data-a="up" style="top:300px;font-size:74px;color:var(--terra);white-space:nowrap">Ko‘rdingizmi?</div>
 <div class="a cx" data-t="29.7" data-a="pop" style="top:440px"><div class="label gold" style="font-size:60px;padding:26px 44px">bitta so‘z</div></div>
 <div class="a" data-t="30.5" data-a="fade" style="left:330px;top:600px;transform:rotate(30deg)">{arrow}</div>
 <div class="a" data-t="30.5" data-a="fade" style="left:680px;top:600px;transform:rotate(-30deg)">{arrow}</div>
 <div class="a" data-t="30.7" data-a="pop" data-r="-2" style="left:120px;top:720px"><div class="chip" style="font-size:44px">1-tushunish</div></div>
 <div class="a" data-t="30.9" data-a="pop" data-r="2" style="left:600px;top:720px"><div class="chip" style="font-size:44px">2-tushunish</div></div>
 <div class="a cx" data-t="31.56" data-a="stamp" data-d=".3" data-r="-2" style="top:900px"><div class="stamp" style="font-size:44px;border-color:var(--green);color:var(--green)">IKKALASI HAM TO‘G‘RI NIYATDA</div></div>
</section>
<section class="scene" data-s="33.45" data-e="39.9">
 <div class="a cx" data-t="33.5" data-a="stamp" data-d=".3" style="top:300px"><div style="background:var(--green);color:#fff;font:900 96px Fraunces;padding:14px 50px;border-radius:10px;white-space:nowrap">MAZHAB =</div></div>
 <div class="a cx" data-t="34.8" data-a="up" style="top:500px"><div class="card tape" style="width:880px;text-align:center;padding:36px"><div class="serif" style="font-size:58px;line-height:1.2"><span class="t-green">Qur’on va Sunnatni</span> tushunishning <span class="t-terra">ilmiy yo‘li</span></div></div></div>
 <div class="a" data-t="37.5" data-a="fade" style="left:110px;top:820px"><div style="position:relative;font:900 54px Nunito;color:#9A9388;white-space:nowrap">yangi din<div class="strike" data-t="38.0"></div></div></div>
 <div class="a" data-t="38.5" data-a="fade" style="left:560px;top:820px"><div style="position:relative;font:900 54px Nunito;color:#9A9388;white-space:nowrap">yangi qoida<div class="strike" data-t="39.0"></div></div></div>
</section>
<section class="scene" data-s="39.9" data-e="46.7">
 <div class="a hand cx" data-t="39.95" data-a="up" style="top:290px;font-size:70px;color:var(--terra);white-space:nowrap">Misol:</div>
 <div class="a" data-t="40.5" data-a="left" data-r="-1.5" style="left:70px;top:420px"><div class="card" style="width:440px;text-align:center;padding:30px"><div style="font-size:110px;line-height:1">💊</div><div class="serif" style="font-size:48px;margin-top:10px">dori — <span class="t-green">bitta</span></div></div></div>
 <div class="a" data-t="43.4" data-a="right" data-r="1.5" style="left:570px;top:420px"><div class="card" style="width:440px;text-align:center;padding:30px;border:5px solid var(--green)"><div style="font-size:110px;line-height:1">🩺</div><div class="serif" style="font-size:44px;margin-top:10px;line-height:1.15">qanday ichishni <span class="t-green">shifokor</span> aytadi</div></div></div>
 <div class="a cx" data-t="44.8" data-a="fade" style="top:860px"><div style="position:relative;font:900 50px Nunito;color:#9A9388;white-space:nowrap">har kim o‘ziga retsept yozmaydi<div class="strike" data-t="45.9"></div></div></div>
</section>
<section class="scene" data-s="46.7" data-e="50.7">
 <div class="a cx" data-t="46.75" data-a="pop" data-r="-.6" style="top:320px"><div class="card tape ayah">
  <div class="caps">Nahl surasi · 43-oyat</div>
  <div class="arabic" style="font-size:66px;line-height:1.75;margin-top:12px;color:var(--green)">فَاسْأَلُوا أَهْلَ الذِّكْرِ إِن كُنتُمْ لَا تَعْلَمُونَ</div>
  <div class="serif" style="font-size:52px;line-height:1.25;margin-top:16px;color:var(--ink)">{rv([('«Agar',47.8),('bilmasangiz,',48.0),('ahli',49.04,'t-green'),('zikrdan',49.4,'t-green'),('so‘ranglar»',49.84,'t-terra')])}</div></div></div>
</section>
<section class="scene" data-s="50.7" data-e="60.3">
 <div class="a cx" data-t="50.8" data-a="up" style="top:270px;font:900 54px Nunito;white-space:nowrap">4 imom — <span class="t-terra">raqib emas</span></div>
 {imom('Molik',54.9,330,370,'#2E6B5B',-1)}
 <div class="a" data-t="55.4" data-a="fade" style="left:500px;top:560px">{arrow}</div>
 {imom('Shofe’iy',54.0,300,660,'#E2A63A',1)}
 <div class="a" data-t="56.9" data-a="fade" style="left:500px;top:850px">{arrow}</div>
 {imom('Ahmad',56.48,330,950,'#C4553B',-1)}
 <div class="a hand" data-t="55.6" data-a="fade" style="left:600px;top:575px;font-size:44px;color:#8A847A">ustoz → shogird</div>
 <div class="a hand" data-t="57.0" data-a="fade" style="left:600px;top:865px;font-size:44px;color:#8A847A">ustoz → shogird</div>
 <div class="a" data-t="59.2" data-a="stamp" data-d=".3" data-r="-6" style="left:60px;top:1160px"><div class="stamp" style="font-size:66px;border-color:var(--green);color:var(--green)">HURMAT</div></div>
</section>
<section class="scene" data-s="60.3" data-e="66.7">
 <div class="a cx" data-t="60.35" data-a="pop" data-r="-.6" style="top:300px"><div class="card tape ayah">
  <div class="caps">Hadisi sharif · Imom Buxoriy, 7352</div>
  <div class="arabic" style="font-size:48px;line-height:1.8;margin-top:12px;color:var(--green)">إِذَا حَكَمَ الْحَاكِمُ فَاجْتَهَدَ ثُمَّ أَصَابَ فَلَهُ أَجْرَانِ، وَإِذَا حَكَمَ فَاجْتَهَدَ ثُمَّ أَخْطَأَ فَلَهُ أَجْرٌ</div>
  <div class="serif" style="font-size:44px;line-height:1.25;margin-top:14px;color:var(--ink)">{rv([('«Hakim',61.64),('ijtihod',62.0,'t-green'),('qilib',62.52),('to‘g‘ri',62.8),('topsa',63.12),('—',63.6),('ikki',63.81,'t-green'),('ajr,',64.0,'t-green'),('xato',64.48),('qilsa',64.8),('ham',65.16),('—',65.44),('bitta',65.6,'t-terra'),('ajr',65.84,'t-terra'),('oladi»',66.0)])}</div></div></div>
 <div class="a" data-t="63.8" data-a="left" data-r="-2" style="left:90px;top:940px"><div class="chip" style="font-size:44px;color:var(--green)">✓ to‘g‘ri → 2 ajr</div></div>
 <div class="a" data-t="65.6" data-a="right" data-r="2" style="left:560px;top:940px"><div class="chip" style="font-size:44px;color:var(--terra)">✗ xato → 1 ajr</div></div>
</section>
<section class="scene" data-s="66.7" data-e="76.7">
 <div class="a cx" data-t="66.75" data-a="pop" data-r="-1" style="top:290px"><div class="card tape" style="width:860px;text-align:center;padding:34px"><div class="serif" style="font-size:62px;line-height:1.2">Mazhab bizni <span class="t-terra">bo‘lmaydi</span></div></div></div>
 <div class="a cx" data-t="68.2" data-a="up" style="top:520px;font:900 50px Nunito;color:var(--green);white-space:nowrap">aksincha —</div>
 <div class="a" data-t="69.0" data-a="left" data-r="-2" style="left:80px;top:630px"><div class="chip" style="font-size:44px">📚 dinni tartib bilan</div></div>
 <div class="a" data-t="70.3" data-a="right" data-r="2" style="left:330px;top:760px"><div class="chip" style="font-size:44px">👨‍🏫 ishonchli ustozlar orqali</div></div>
 <div class="a cx" data-t="75.2" data-a="stamp" data-d=".3" data-r="-2" style="top:960px"><div class="stamp" style="font-size:56px;border-color:var(--green);color:var(--green)">BOSHQASINI HURMAT QILING</div></div>
</section>
'''
extra=f'''<div class="a cx" data-t="76.8" data-a="up" data-o="86.15" style="top:300px;font:900 54px Nunito;color:var(--green);white-space:nowrap">Har kuni — birgalikda</div>
<div class="a cx" data-t="86.25" data-a="pop" style="top:290px;display:flex;gap:22px"><div class="chip" style="font-size:40px">📌 Saqlab qo‘ying</div><div class="a chip" data-t="87.7" data-a="pop" style="position:relative;font-size:40px">📤 Yaqiningizga yuboring</div></div>
<div class="a cx" data-t="81.5" data-a="pop" style="top:1220px"><div class="chip" style="font-size:42px;white-space:nowrap;border:4px solid var(--terra)">💬 Izohlarga <span class="t-terra" style="font-size:56px">«+»</span> qoldiring</div></div>
<div class="a hand cx" data-t="82.9" data-a="fade" style="top:1335px;font-size:48px;color:#8A847A">yoki</div>
'''
c=C.cta(tas=77.1,zikr=78.4,extra=extra,havola=83.5,btn=84.7)
c=c.replace('style="top:1250px"><div class="chip"','style="top:1400px"><div class="chip"').replace('style="top:1400px"><div style="background:var(--gold)','style="top:1530px"><div style="background:var(--gold)').replace('top:1560px;font:700','top:1690px;font:700')
c=c.replace('style="top:1070px"><div style="background:var(--terra)','style="top:1060px"><div style="background:var(--terra)')
s+=c+'''
<div id="sub" data-hide="78.3"><div id="subbox"></div></div></div>'''+C.TASBEH+'</body></html>'
open('/home/claude/reel12/index.html','w').write(HEAD+b+s)
print('ok')
