import sys; sys.path.insert(0,'/home/claude')
import cta as C
exec(open('/home/claude/build4.py').read().split('# ---------- reel004 ----------')[0].split('import cta as C')[1])
C.SCENE_S='75.75'
b=bgs([(-1,8.7,'#E9E2D6'),(8.7,19.2,'#F3E9CF'),(19.2,23.3,'#DCE6DA'),(23.3,35.0,'#DAE2E9'),(35.0,44.6,'#F6E1D3'),(44.6,53.9,'#F3E9CF'),(53.9,62.9,'#E5DDEB'),(62.9,66.6,'#DCE6DA'),(66.6,75.75,'#F1E6D6'),(75.75,999,'#F1E6D6')])
bars='''<svg width="{w}" height="{h}" viewBox="0 0 120 120"><rect x="6" y="6" width="108" height="108" rx="8" fill="none" stroke="#4A453F" stroke-width="8"/><path d="M30 6v108M52 6v108M74 6v108M96 6v108" stroke="#4A453F" stroke-width="7"/></svg>'''
scales='''<svg width="{w}" height="{h}" viewBox="0 0 120 110"><path d="M60 12v84M30 100h60M18 30h84" stroke="#2E6B5B" stroke-width="7" stroke-linecap="round"/><path d="M18 30L4 64h28zM102 30L88 64h28z" fill="#E2A63A" stroke="#2E6B5B" stroke-width="4" stroke-linejoin="round"/><circle cx="60" cy="12" r="7" fill="#C4553B"/></svg>'''
def lab(t,txt,cls=''):
    return f'<div class="a" data-t="{t}" data-a="pop" data-r="-3" style="left:80px;top:280px"><div class="label {cls}">{txt}</div></div>'
s=f'''
<div id="banner" data-s="8.7" data-e="75.5">Abu Hanifa boyligini qayerga sarflagan?</div>
<section class="scene" data-s="-1" data-e="8.7">
 <div class="a hand cx" data-t="0.07" data-a="up" style="top:290px;font-size:64px;color:#8A847A;white-space:nowrap">Xalifaning taklifi:</div>
 <div class="a cx" data-t="1.8" data-a="pop" style="top:400px;display:flex;align-items:center;gap:26px">{scales.format(w=170,h=156)}<div class="serif" style="font-size:96px;color:var(--green);white-space:nowrap">BOSH QOZI</div></div>
 <div class="a cx" data-t="4.1" data-a="stamp" data-d=".3" data-r="-5" style="top:620px"><div class="stamp" style="font-size:110px">RAD ETDI</div></div>
 <div class="a cx" data-t="5.7" data-a="drop" style="top:820px;display:flex;align-items:center;gap:24px">{bars.format(w=170,h=170)}<div class="serif" style="font-size:80px;color:#4A453F">qamoq</div></div>
 <div class="a hand cx" data-t="7.1" data-a="up" data-r="-2" style="top:1060px;font-size:84px;color:var(--terra);white-space:nowrap">Bu kim edi?</div>
</section>
<section class="scene" data-s="8.7" data-e="19.2">
 <div class="a cx" data-t="9.2" data-a="pop" data-r="-1" style="top:300px"><div class="card tape" style="width:880px;text-align:center;padding:40px"><div class="caps">Imomi A’zam</div><div class="serif" style="font-size:110px;line-height:1.05;color:var(--green);margin-top:8px">Abu Hanifa</div><div style="font:800 34px Nunito;color:#8A847A;margin-top:8px">hijriy 80 – 150</div></div></div>
 <div class="a" data-t="12.1" data-a="left" data-r="-2" style="left:90px;top:680px"><div class="chip" style="font-size:48px">📚 buyuk olim</div></div>
 <div class="a" data-t="13.5" data-a="right" data-r="2" style="left:520px;top:680px"><div class="chip" style="font-size:48px">💰 boy savdogar</div></div>
 <div class="a hand cx" data-t="15.2" data-a="up" style="top:880px;font-size:64px;color:var(--terra);white-space:nowrap">boyligini qanday sarflagan?</div>
</section>
<section class="scene" data-s="19.2" data-e="23.3">
 {lab(19.25,'1-voqea')}
 <div class="a cx" data-t="19.3" data-a="up" style="top:400px;display:flex;align-items:center;gap:30px"><div class="card" style="width:380px;text-align:center;padding:30px"><div style="font-size:100px;line-height:1">🏠</div><div class="serif" style="font-size:46px;margin-top:10px">oilasiga</div></div><div class="a" data-t="20.9" data-a="pop" style="position:relative;font:900 110px Fraunces;color:var(--terra)">=</div><div class="a card" data-t="22.0" data-a="pop" style="position:relative;width:380px;text-align:center;padding:30px;border:5px solid var(--green)"><div style="font-size:100px;line-height:1">🤲</div><div class="serif" style="font-size:46px;margin-top:10px;color:var(--green)">sadaqaga</div></div></div>
 <div class="a cx" data-t="20.0" data-a="fade" style="top:800px"><div class="caps" style="white-space:nowrap">Zahabiy, «Siyar a’lom an-nubalo»</div></div>
</section>
<section class="scene" data-s="23.3" data-e="35.0">
 {lab(23.35,'2-voqea','gold')}
 <div class="a cx" data-t="24.1" data-a="pop" style="top:400px;display:flex;align-items:baseline;gap:20px"><div class="serif" style="font-size:140px;color:var(--terra);line-height:1"><span class="count" data-t="24.15" data-d=".7" data-from="0" data-to="10000">0</span></div><div style="font:900 54px Nunito;white-space:nowrap">dirham qarz</div></div>
 <div class="a hand cx" data-t="27.0" data-a="up" style="top:600px;font-size:58px;color:#8A847A;white-space:nowrap">uyalganidan yo‘lini o‘zgartirardi…</div>
 <div class="a cx" data-t="32.3" data-a="up" data-r="-1" style="top:730px"><div class="card tape" style="width:860px;text-align:center;padding:34px;border:5px solid var(--green)"><div class="caps" style="margin-bottom:10px">Imom</div><div class="serif" style="font-size:56px;line-height:1.2">{rv([('«Butun',32.42),('qarzni',32.6,'t-terra'),('senga',33.02),('hadya',33.36,'t-green'),('qildim»',33.7,'t-green')])}</div></div></div>
 <div class="a cx" data-t="34.3" data-a="fade" style="top:1040px"><div class="caps">«Uqudul jumon»</div></div>
</section>
<section class="scene" data-s="35.0" data-e="44.6">
 {lab(35.05,'3-voqea · eng ta’sirlisi','terra')}
 <div class="a" data-t="36.3" data-a="left" data-r="-1.5" style="left:90px;top:420px"><div class="chip" style="font-size:46px">🧒 kambag‘al shogird</div></div>
 <div class="a" data-t="38.3" data-a="right" data-r="1.5" style="left:240px;top:560px"><div class="card" style="padding:24px 30px"><div class="caps" style="color:var(--terra)">onasi</div><div class="serif" style="font-size:46px;margin-top:6px">«darsni qo‘y, ishga bor»</div></div></div>
 <div class="a cx" data-t="40.9" data-a="up" style="top:780px"><div class="card tape" style="width:880px;text-align:center;padding:34px;border:5px solid var(--green)"><div class="serif" style="font-size:52px;line-height:1.2">Abu Hanifa ikkalasining <span class="t-green">xarajatini o‘z zimmasiga oldi</span></div></div></div>
</section>
<section class="scene" data-s="44.6" data-e="53.9">
 <div class="a hand cx" data-t="44.65" data-a="up" style="top:290px;font-size:66px;color:#8A847A;white-space:nowrap">o‘sha bola —</div>
 <div class="a cx" data-t="45.4" data-a="stamp" data-d=".35" data-r="-2" style="top:400px"><div style="background:var(--green);color:#fff;font:900 110px Fraunces;padding:14px 50px;border-radius:10px;white-space:nowrap">ABU YUSUF</div></div>
 <div class="a cx" data-t="46.5" data-a="pop" style="top:640px;display:flex;align-items:center;gap:22px">{scales.format(w=120,h=110)}<div class="chip" style="font-size:44px">birinchi bosh qozi</div></div>
 <div class="a cx" data-t="50.2" data-a="up" style="top:850px"><div class="card" style="width:880px;text-align:center;padding:30px"><div class="serif" style="font-size:50px;line-height:1.2">ustozi <span class="t-terra">rad etgan</span> lavozimni — shogirdi <span class="t-green">egalladi</span></div></div></div>
</section>
<section class="scene" data-s="53.9" data-e="62.9">
 <div class="a cx" data-t="54.0" data-a="up" style="top:290px"><div class="card tape" style="width:860px;text-align:center;padding:32px"><div class="serif" style="font-size:58px">haqni deb — <span class="t-terra">qozilikni rad etdi</span></div></div></div>
 <div class="a cx" data-t="57.4" data-a="drop" style="top:540px;display:flex;align-items:center;gap:24px">{bars.format(w=200,h=200)}<div><div class="caps">Xalifa Mansur</div><div class="serif" style="font-size:70px;color:#4A453F">qamoq</div></div></div>
 <div class="a cx" data-t="59.7" data-a="pop" style="top:820px;display:flex;align-items:baseline;gap:18px"><div style="font:900 46px Nunito">hijriy</div><div class="serif" style="font-size:130px;color:var(--terra);line-height:1">150</div><div style="font:900 46px Nunito;white-space:nowrap">— vafot</div></div>
</section>
<section class="scene" data-s="62.9" data-e="66.6">
 <div class="a cx" data-t="62.95" data-a="pop" data-r="-.6" style="top:380px"><div class="card tape ayah">
  <div class="caps">Hadisi sharif · Imom Muslim, 2588</div>
  <div class="arabic" style="font-size:80px;line-height:1.7;margin-top:12px;color:var(--green)">مَا نَقَصَتْ صَدَقَةٌ مِنْ مَالٍ</div>
  <div class="serif" style="font-size:60px;line-height:1.25;margin-top:16px;color:var(--ink)">{rv([('«Sadaqa',64.44,'t-green'),('molni',65.13),('kamaytirmaydi»',65.47,'t-terra')])}</div></div></div>
</section>
<section class="scene" data-s="66.6" data-e="75.75">
 <div class="a" data-t="67.4" data-a="left" data-r="-2" style="left:80px;top:300px"><div class="chip" style="font-size:46px;color:var(--green)">💰 boylik — qo‘lida ✓</div></div>
 <div class="a" data-t="68.9" data-a="right" data-r="2" style="left:300px;top:440px"><div class="chip" style="font-size:46px;color:var(--terra)">❤️ qalbida ✗</div></div>
 <div class="a cx" data-t="70.3" data-a="up" style="top:640px"><div class="card tape" style="width:880px;text-align:center;padding:34px"><div class="serif" style="font-size:54px;line-height:1.2">bugun ham uning ilmi bilan <span class="t-green">millionlab odamlar</span> ibodat qilmoqda</div></div></div>
 <div class="a cx" data-t="74.9" data-a="stamp" data-d=".3" data-r="-3" style="top:960px"><div class="stamp" style="font-size:80px;border-color:var(--green);color:var(--green)">BIZ HAM</div></div>
</section>
'''
extra=f'''<div class="a cx" data-t="75.85" data-a="up" data-o="85.45" style="top:300px;font:900 54px Nunito;color:var(--green);white-space:nowrap">Har kuni — birgalikda</div>
<div class="a cx" data-t="85.55" data-a="pop" style="top:290px;display:flex;gap:22px"><div class="chip" style="font-size:40px">📌 Saqlab qo‘ying</div><div class="a chip" data-t="86.9" data-a="pop" style="position:relative;font-size:40px">📤 Yaqinlaringizga yuboring</div></div>
<div class="a cx" data-t="80.8" data-a="pop" style="top:1220px"><div class="chip" style="font-size:42px;white-space:nowrap;border:4px solid var(--terra)">💬 Izohlarga <span class="t-terra" style="font-size:56px">«+»</span> qoldiring</div></div>
<div class="a hand cx" data-t="82.2" data-a="fade" style="top:1335px;font-size:48px;color:#8A847A">yoki</div>
'''
c=C.cta(tas=76.1,zikr=77.5,extra=extra,havola=82.85,btn=84.0)
c=c.replace('style="top:1250px"><div class="chip"','style="top:1400px"><div class="chip"').replace('style="top:1400px"><div style="background:var(--gold)','style="top:1530px"><div style="background:var(--gold)').replace('top:1560px;font:700','top:1690px;font:700')
c=c.replace('style="top:1070px"><div style="background:var(--terra)','style="top:1060px"><div style="background:var(--terra)')
s+=c+'''
<div id="sub" data-hide="77.4"><div id="subbox"></div></div></div>'''+C.TASBEH+'</body></html>'
open('/home/claude/reel13/index.html','w').write(HEAD+b+s)
print('ok')
