import sys; sys.path.insert(0,'/home/claude')
import cta as C
exec(open('/home/claude/build4.py').read().split('# ---------- reel004 ----------')[0].split('import cta as C')[1])
C.SCENE_S='78.35'
b=bgs([(-1,8.8,'#E9E2D6'),(8.8,21.7,'#F3E9CF'),(21.7,27.7,'#DCE6DA'),(27.7,34.5,'#DAD3C8'),(34.5,42.9,'#F1E6D6'),(42.9,52.3,'#E5DDEB'),(52.3,65.9,'#F6E1D3'),(65.9,78.35,'#DAE2E9'),(78.35,999,'#F1E6D6')])
cave='''<svg width="{w}" height="{h}" viewBox="0 0 240 170"><path d="M6 166C10 80 60 12 120 12s110 68 114 154z" fill="#8C7A62"/><path d="M60 166c2-50 26-86 60-86s58 36 60 86z" fill="#3A332B"/><path d="M20 120c16-6 24-20 20-36M210 110c-14-4-20-16-18-30" stroke="#6E604C" stroke-width="6" fill="none" stroke-linecap="round"/></svg>'''
coin='''<svg width="{w}" height="{h}" viewBox="0 0 100 100"><circle cx="50" cy="50" r="44" fill="#C9C9C9" stroke="#8E8E8E" stroke-width="6"/><circle cx="50" cy="50" r="30" fill="none" stroke="#A9A9A9" stroke-width="4"/><path d="M40 40l20 20M60 40L40 60" stroke="#8E8E8E" stroke-width="4"/></svg>'''
zzz='<div class="hand" style="font-size:80px;color:#5B6B74;line-height:.8">z<span style="font-size:60px">z</span><span style="font-size:44px">z</span></div>'
s=f'''
<div id="banner" data-s="8.8" data-e="78.1">309 yil uxlagan yigitlar</div>
<section class="scene" data-s="-1" data-e="8.8">
 <div class="a cx" data-t="0.05" data-a="up" style="top:300px">{cave.format(w=560,h=397)}</div>
 <div class="a" data-t="1.5" data-a="fade" data-f="4" style="left:640px;top:330px">{zzz}</div>
 <div class="a cx" data-t="4.1" data-a="pop" style="top:740px;display:flex;align-items:baseline;gap:20px"><div class="serif" style="font-size:190px;color:var(--terra);line-height:1"><span class="count" data-t="4.2" data-d="1.4" data-from="0" data-to="309">0</span></div><div style="font:900 70px Nunito">yil</div></div>
 <div class="a cx" data-t="7.4" data-a="stamp" data-d=".3" data-r="-3" style="top:1010px"><div class="stamp" style="font-size:84px;border-color:var(--green);color:var(--green)">QUR’ONDA BOR</div></div>
</section>
<section class="scene" data-s="8.8" data-e="21.7">
 <div class="a cx" data-t="8.85" data-a="pop" data-r="-.6" style="top:290px"><div class="card tape ayah">
  <div class="caps">Kahf surasi · 13-oyat</div>
  <div class="arabic" style="font-size:64px;line-height:1.75;margin-top:12px;color:var(--green)">إِنَّهُمْ فِتْيَةٌ آمَنُوا بِرَبِّهِمْ وَزِدْنَاهُمْ هُدًى</div>
  <div class="serif" style="font-size:48px;line-height:1.25;margin-top:14px;color:var(--ink)">{rv([('«Ular',9.79),('Robbiga',10.23),('iymon',10.73,'t-green'),('keltirgan',11.08,'t-green'),('yigitlar',11.58,'t-terra'),('edi',12.12),('va',12.54),('Biz',12.69),('ularning',12.92),('hidoyatini',13.42,'t-green'),('ziyoda',14.0),('qildik»',14.38)])}</div></div></div>
 <div class="a" data-t="15.1" data-a="left" data-r="-2" style="left:80px;top:800px"><div class="chip" style="font-size:44px">🏛 shaharda — butparastlik</div></div>
 <div class="a" data-t="17.3" data-a="right" data-r="2" style="left:260px;top:940px;display:flex;align-items:center;gap:20px">{cave.format(w=180,h=128)}<div class="chip" style="font-size:44px">iymon uchun — g‘orga</div></div>
</section>
<section class="scene" data-s="21.7" data-e="27.7">
 <div class="a hand cx" data-t="20.4" data-a="fade" style="top:290px;font-size:62px;color:var(--green);white-space:nowrap">ularning duosi:</div>
 <div class="a cx" data-t="21.75" data-a="pop" data-r="-.6" style="top:400px"><div class="card tape ayah">
  <div class="caps">Kahf surasi · 10-oyat</div>
  <div class="arabic" style="font-size:58px;line-height:1.75;margin-top:12px;color:var(--green)">رَبَّنَا آتِنَا مِن لَّدُنكَ رَحْمَةً وَهَيِّئْ لَنَا مِنْ أَمْرِنَا رَشَدًا</div>
  <div class="serif" style="font-size:46px;line-height:1.25;margin-top:14px;color:var(--ink)">{rv([('«Robbimiz,',21.84),('bizga',22.81),('O‘z',23.19),('huzuringdan',23.39),('rahmat',24.0,'t-green'),('ato',24.5,'t-green'),('et',24.69,'t-green'),('va',25.15),('ishimizda',25.39),('bizga',25.85),('to‘g‘ri',26.19,'t-terra'),('yo‘lni',26.46,'t-terra'),('oson',26.89),('qil»',27.19)])}</div></div></div>
</section>
<section class="scene" data-s="27.7" data-e="34.5">
 <div class="a cx" data-t="27.75" data-a="pop" style="top:300px">{cave.format(w=620,h=439)}</div>
 <div class="a" data-t="28.3" data-a="fade" data-f="4" style="left:720px;top:320px">{zzz}</div>
 <div class="a cx" data-t="29.4" data-a="pop" style="top:780px"><div class="chip" style="font-size:46px">↻ o‘ngga, chapga ag‘darib turdi</div></div>
 <div class="a cx" data-t="31.35" data-a="up" style="top:920px;display:flex;align-items:center;gap:20px"><div style="font-size:110px;line-height:1">🐕</div><div class="chip" style="font-size:42px">itlari — g‘or og‘zida</div></div>
 <div class="a cx" data-t="28.0" data-a="fade" style="top:1110px"><div class="caps">Kahf surasi · 18-oyat</div></div>
</section>
<section class="scene" data-s="34.5" data-e="42.9">
 <div class="a hand cx" data-t="34.55" data-a="up" style="top:290px;font-size:60px;color:#8A847A;white-space:nowrap">uyg‘onishgach…</div>
 <div class="a" data-t="36.7" data-a="left" data-r="-2" style="left:80px;top:410px"><div class="card" style="padding:28px 34px"><div class="serif" style="font-size:58px">«Qancha uxladik?»</div></div></div>
 <div class="a" data-t="37.9" data-a="right" data-r="2" style="left:170px;top:600px"><div class="card" style="width:820px;padding:28px 34px;border:5px solid var(--green)"><div class="serif" style="font-size:50px">«Bir kun yoki kunning bir qismi»</div></div></div>
 <div class="a cx" data-t="40.4" data-a="pop" style="top:830px;display:flex;align-items:center;gap:24px">{coin.format(w=140,h=140)}<div class="chip" style="font-size:44px">kumush tanga bilan — shaharga</div></div>
 <div class="a cx" data-t="35.0" data-a="fade" style="top:1050px"><div class="caps">Kahf surasi · 19-oyat</div></div>
</section>
<section class="scene" data-s="42.9" data-e="52.3">
 <div class="a cx" data-t="42.95" data-a="pop" data-r="-.6" style="top:290px"><div class="card tape ayah">
  <div class="caps">Kahf surasi · 25-oyat</div>
  <div class="arabic" style="font-size:58px;line-height:1.75;margin-top:12px;color:var(--green)">وَلَبِثُوا فِي كَهْفِهِمْ ثَلَاثَ مِائَةٍ سِنِينَ وَازْدَادُوا تِسْعًا</div>
  <div class="serif" style="font-size:46px;line-height:1.25;margin-top:14px;color:var(--ink)">{rv([('«Ular',42.95),('g‘orlarida',43.27),('uch',43.92,'t-terra'),('yuz',44.15,'t-terra'),('yil',44.38,'t-terra'),('turdilar',44.58),('va',45.23),('yana',45.35),('to‘qqiz',45.65,'t-green'),('yil',46.04,'t-green'),('qo‘shdilar»',46.19)])}</div></div></div>
 <div class="a cx" data-t="47.8" data-a="fade" style="top:780px"><div class="caps">mufassirlar aytadi:</div></div>
 <div class="a cx" data-t="49.0" data-a="pop" style="top:850px;display:flex;align-items:center;gap:22px"><div class="card" style="padding:22px 30px;text-align:center"><div style="font-size:60px;line-height:1">☀️</div><div class="serif" style="font-size:66px">300</div><div style="font:800 28px Nunito;color:#8A847A">quyosh yili</div></div><div class="a" data-t="50.0" data-a="pop" style="position:relative;font:900 90px Fraunces;color:var(--terra)">≈</div><div class="a card" data-t="50.6" data-a="pop" style="position:relative;padding:22px 30px;text-align:center;border:5px solid var(--green)"><div style="font-size:60px;line-height:1">🌙</div><div class="serif" style="font-size:66px;color:var(--green)">309</div><div style="font:800 28px Nunito;color:#8A847A">oy yili</div></div></div>
</section>
<section class="scene" data-s="52.3" data-e="65.9">
 <div class="a hand cx" data-t="52.35" data-a="up" style="top:280px;font-size:64px;color:var(--terra);white-space:nowrap">O‘ylab ko‘ring:</div>
 <div class="a" data-t="54.3" data-a="fade" style="left:90px;top:400px"><div style="position:relative;font:900 52px Nunito;color:#9A9388">🏠 uyi<div class="strike" data-t="54.6"></div></div></div>
 <div class="a" data-t="54.9" data-a="fade" style="left:380px;top:400px"><div style="position:relative;font:900 52px Nunito;color:#9A9388">🏙 shahri<div class="strike" data-t="55.3"></div></div></div>
 <div class="a" data-t="56.1" data-a="fade" style="left:720px;top:400px"><div style="position:relative;font:900 52px Nunito;color:#9A9388">🌍 dunyosi<div class="strike" data-t="56.6"></div></div></div>
 <div class="a cx" data-t="58.4" data-a="pop" style="top:560px"><div class="label gold" style="font-size:54px;padding:24px 40px">🤲 qo‘llarida — faqat bitta duo</div></div>
 <div class="a cx" data-t="61.0" data-a="up" style="top:740px"><div class="card tape" style="width:880px;text-align:center;padding:32px"><div class="serif" style="font-size:52px;line-height:1.2">Alloh ularni <span class="t-green">3 asr</span> asradi va nomlarini <span class="t-terra">Qiyomatgacha</span> o‘qiladigan Kitobga yozdi</div></div></div>
</section>
<section class="scene" data-s="65.9" data-e="78.35">
 <div class="a cx" data-t="65.95" data-a="fade" style="top:290px"><div style="position:relative;font:900 56px Nunito;color:#9A9388;white-space:nowrap">bugun g‘orga qochish shart emas<div class="strike" data-t="67.4"></div></div></div>
 <div class="a" data-t="68.5" data-a="left" data-r="-2" style="left:90px;top:420px"><div class="chip" style="font-size:44px">📱 dunyo shovqini</div></div>
 <div class="a" data-t="69.5" data-a="right" data-r="2" style="left:560px;top:420px"><div class="chip" style="font-size:44px">😴 g‘aflat</div></div>
 <div class="a cx" data-t="72.2" data-a="up" style="top:600px"><div class="card tape" style="width:880px;text-align:center;padding:34px;border:5px solid var(--green)"><div class="serif" style="font-size:54px;line-height:1.2">Alloh uchun tark etilgan hech narsa <span class="t-green">zoe ketmaydi</span></div></div></div>
 <div class="a cx" data-t="75.25" data-a="stamp" data-d=".3" data-r="-2" style="top:930px"><div class="stamp" style="font-size:62px;border-color:var(--green);color:var(--green)">IYMONINGIZNI ASRANG</div></div>
</section>
'''
extra=f'''<div class="a cx" data-t="78.45" data-a="up" data-o="86.95" style="top:300px;font:900 54px Nunito;color:var(--green);white-space:nowrap">Har kuni — birgalikda</div>
<div class="a cx" data-t="87.05" data-a="pop" style="top:290px;display:flex;gap:22px"><div class="chip" style="font-size:40px">📌 Saqlab qo‘ying</div><div class="a chip" data-t="88.4" data-a="pop" style="position:relative;font-size:40px">📤 Yaqinlaringizga yuboring</div></div>
<div class="a cx" data-t="82.65" data-a="pop" style="top:1220px"><div class="chip" style="font-size:42px;white-space:nowrap;border:4px solid var(--terra)">💬 Izohlarga <span class="t-terra" style="font-size:56px">«+»</span> qoldiring</div></div>
<div class="a hand cx" data-t="84.1" data-a="fade" style="top:1335px;font-size:48px;color:#8A847A">yoki</div>
'''
c=C.cta(tas=78.6,zikr=79.85,extra=extra,havola=84.55,btn=85.7)
c=c.replace('style="top:1250px"><div class="chip"','style="top:1400px"><div class="chip"').replace('style="top:1400px"><div style="background:var(--gold)','style="top:1530px"><div style="background:var(--gold)').replace('top:1560px;font:700','top:1690px;font:700')
c=c.replace('style="top:1070px"><div style="background:var(--terra)','style="top:1060px"><div style="background:var(--terra)')
s+=c+'''
<div id="sub" data-hide="79.75"><div id="subbox"></div></div></div>'''+C.TASBEH+'</body></html>'
open('/home/claude/reel15/index.html','w').write(HEAD+b+s)
print('ok')
