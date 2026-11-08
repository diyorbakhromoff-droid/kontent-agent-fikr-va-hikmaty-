import sys; sys.path.insert(0,'/home/claude')
import cta as C
exec(open('/home/claude/build4.py').read().split('# ---------- reel004 ----------')[0].split('import cta as C')[1])
C.SCENE_S='70.4'
b=bgs([(-1,7.6,'#DCE6DA'),(7.6,21.0,'#F3E9CF'),(21.0,34.8,'#DAE2E9'),(34.8,44.9,'#E5DDEB'),(44.9,55.5,'#DCE6DA'),(55.5,62.3,'#F3E9CF'),(62.3,70.4,'#F6E1D3'),(70.4,999,'#F1E6D6')])
palm='''<svg width="{w}" height="{h}" viewBox="0 0 120 150"><path d="M62 60c-4 30-2 60 4 86h-12c-4-28-4-58 2-86z" fill="#9A6B3E"/><path d="M60 58C44 34 20 30 4 40c18-2 34 4 50 20zM60 58c4-26 22-44 46-46-16 10-28 26-40 48zM60 58c18-14 40-14 56 0-20-6-38-2-54 6zM60 58C46 46 26 46 10 58c20-6 34-4 48 4zM60 58c-2-20 4-40 18-52-6 16-10 32-12 52z" fill="#2E6B5B"/><circle cx="56" cy="64" r="5" fill="#E2A63A"/><circle cx="66" cy="66" r="5" fill="#E2A63A"/></svg>'''
globe='''<svg width="{w}" height="{h}" viewBox="0 0 100 100"><circle cx="50" cy="50" r="44" fill="#3F8A73" stroke="#2E6B5B" stroke-width="5"/><ellipse cx="50" cy="50" rx="20" ry="44" fill="none" stroke="#FBF7EE" stroke-width="4"/><path d="M6 50h88M14 28h72M14 72h72M50 6v88" stroke="#FBF7EE" stroke-width="4"/></svg>'''
house='''<svg width="{w}" height="{h}" viewBox="0 0 120 110"><path d="M10 52L60 10l50 42" fill="none" stroke="#C4553B" stroke-width="10" stroke-linecap="round" stroke-linejoin="round"/><rect x="24" y="48" width="72" height="56" fill="#2E6B5B"/><rect x="50" y="68" width="20" height="36" fill="#E2A63A"/></svg>'''
gate='''<svg width="{w}" height="{h}" viewBox="0 0 160 150"><path d="M20 146V70a60 60 0 0 1 120 0v76" fill="none" stroke="#E2A63A" stroke-width="12"/><path d="M44 146V78a36 36 0 0 1 72 0v68" fill="#FBF7EE" stroke="#2E6B5B" stroke-width="8"/><path d="M80 44v102" stroke="#2E6B5B" stroke-width="6"/></svg>'''
palms10=''.join(f'<div class="a" data-t="{57.6+i*0.17:.2f}" data-a="pop" style="position:relative">{palm.format(w=78,h=98)}</div>' for i in range(10))
stairs=''.join(f'<div class="a" data-t="{42.5+i*0.18:.2f}" data-a="up" style="position:relative;width:120px;height:{60+i*70}px;background:{"#C9C2B6" if i==0 else ("#E2A63A" if i==5 else "#3F8A73")};border-radius:8px 8px 0 0"></div>' for i in range(6))
s=f'''
<div id="banner" data-s="7.6" data-e="70.2">Jannatdagi eng past daraja qanday?</div>
<section class="scene" data-s="-1" data-e="7.6">
 <div class="a cx" data-t="0.05" data-a="pop" data-r="-1" style="top:280px"><div class="card tape" style="width:900px;text-align:center;padding:40px">
  <div class="serif" style="font-size:66px;line-height:1.18">Jannatga <span class="t-terra">eng oxirgi</span> kirgan odamga <span class="t-green">qancha joy</span> beriladi?</div></div></div>
 <div class="a cx" data-t="1.0" data-a="pop" data-f="4" style="top:640px">{gate.format(w=300,h=281)}</div>
 <div class="a hand cx" data-t="3.85" data-a="up" data-r="-2" style="top:960px;font-size:80px;color:var(--terra);white-space:nowrap">bilasizmi?</div>
 <div class="a cx" data-t="5.0" data-a="fade" style="top:1110px;font:900 46px Nunito;color:#8A847A;white-space:nowrap">javobi sizni hayratda qoldiradi…</div>
</section>
<section class="scene" data-s="7.6" data-e="21.0">
 <div class="a cx" data-t="7.7" data-a="pop" style="top:280px"><div class="label gold">Buxoriy, 6571 · Muslim, 186</div></div>
 <div class="a" data-t="9.2" data-a="left" data-r="-1.5" style="left:70px;top:420px"><div class="chip" style="font-size:44px">🔥 do‘zaxdan emaklab chiqadi</div></div>
 <div class="a" data-t="12.5" data-a="right" data-r="1.5" style="left:200px;top:580px"><div class="card" style="padding:26px 34px;border:4px solid var(--green)"><div class="caps" style="margin-bottom:8px">Alloh</div><div class="serif" style="font-size:52px">«Borgin, jannatga kir»</div></div></div>
 <div class="a" data-t="15.9" data-a="pop" style="left:90px;top:820px;display:flex;align-items:center;gap:22px">{gate.format(w=140,h=131)}<div class="hand" style="font-size:60px;color:#8A847A">to‘lib qolgandek…</div></div>
 <div class="a" data-t="18.6" data-a="up" data-r="-1" style="left:250px;top:1030px"><div class="card" style="padding:26px 34px"><div class="caps" style="margin-bottom:8px;color:var(--terra)">u kishi</div><div class="serif" style="font-size:52px">«Robbim, u to‘la ekan»</div></div></div>
</section>
<section class="scene" data-s="21.0" data-e="34.8">
 <div class="a cx" data-t="22.4" data-a="up" style="top:280px"><div class="card tape" style="width:880px;text-align:center;padding:30px"><div class="caps" style="margin-bottom:10px">Alloh</div><div class="serif" style="font-size:54px">«Borgin, senga…»</div></div></div>
 <div class="a cx" data-t="23.5" data-a="pop" style="top:520px;display:flex;align-items:center;gap:30px">{globe.format(w=220,h=220)}<div class="a" data-t="24.75" data-a="stamp" data-d=".3" style="position:relative"><div class="serif" style="font-size:150px;color:var(--terra);line-height:1">×10</div></div></div>
 <div class="a cx" data-t="24.0" data-a="up" style="top:770px;font:900 50px Nunito;white-space:nowrap">dunyo va yana o‘n barobari</div>
 <div class="a" data-t="27.5" data-a="up" data-r="-1" style="left:80px;top:880px"><div class="card" style="width:860px;padding:28px 34px"><div class="caps" style="margin-bottom:8px;color:var(--terra)">u kishi hayratdan</div><div class="serif" style="font-size:48px;line-height:1.2">«Sen podshoh bo‘la turib, meni masxara qilyapsanmi?»</div></div></div>
 <div class="a cx" data-t="32.2" data-a="pop" data-r="1" style="top:1180px"><div class="chip" style="font-size:40px">😊 Payg‘ambarimiz (s.a.v.) kuldilar</div></div>
</section>
<section class="scene" data-s="34.8" data-e="44.9">
 <div class="a cx" data-t="36.3" data-a="stamp" data-d=".3" data-r="-3" style="top:300px"><div class="stamp" style="font-size:80px">ENG PAST DARAJA</div></div>
 <div class="a cx" data-t="39.0" data-a="up" style="top:500px;display:flex;align-items:center;gap:20px"><div style="font:900 52px Nunito">=</div>{globe.format(w=110,h=110)}<div class="serif" style="font-size:90px;color:var(--terra)">×10</div></div>
 <div class="a cx" data-t="42.4" data-a="none" style="top:700px;display:flex;align-items:flex-end;gap:16px">{stairs}</div>
 <div class="a hand" data-t="43.4" data-a="pop" data-r="-4" style="left:620px;top:640px;font-size:86px;color:var(--terra)">eng yuqorisi?</div>
</section>
<section class="scene" data-s="44.9" data-e="55.5">
 <div class="a hand cx" data-t="45.0" data-a="up" style="top:270px;font-size:68px;color:var(--terra);white-space:nowrap">Endi eng qizig‘i:</div>
 <div class="a cx" data-t="46.2" data-a="up" style="top:380px"><div class="chip" style="font-size:44px">🌴 jannatdagi bog‘ingiz — <span class="t-green">&nbsp;hozirdan</span></div></div>
 <div class="a cx" data-t="49.3" data-a="pop" data-r="-.6" style="top:530px"><div class="card tape ayah">
  <div class="caps">Hadisi sharif · Imom Termiziy, 3464</div>
  <div class="arabic" style="font-size:54px;line-height:1.75;margin-top:12px;color:var(--green)">مَنْ قَالَ: سُبْحَانَ اللهِ العَظِيمِ وَبِحَمْدِهِ، غُرِسَتْ لَهُ نَخْلَةٌ فِي الجَنَّةِ</div>
  <div class="serif" style="font-size:46px;line-height:1.25;margin-top:14px;color:var(--ink)">{rv([('«Kim',49.46),('«Subhanallohil',49.76,'t-green'),('aziym',50.88,'t-green'),('va',51.28,'t-green'),('bihamdihi»',51.44,'t-green'),('desa,',52.08),('unga',52.88),('jannatda',53.08),('bitta',53.79,'t-terra'),('xurmo',54.08,'t-terra'),('daraxti',54.48,'t-terra'),('ekiladi»',54.8)])}</div></div></div>
 <div class="a cx" data-t="54.1" data-a="pop" style="top:1080px">{palm.format(w=160,h=200)}</div>
</section>
<section class="scene" data-s="55.5" data-e="62.3">
 <div class="a cx" data-t="55.6" data-a="pop" style="top:290px;display:flex;align-items:center;gap:24px"><div class="label" style="font-size:50px">1 zikr</div><div style="font:900 64px Nunito">=</div>{palm.format(w=110,h=137)}</div>
 <div class="a cx" data-t="57.5" data-a="up" style="top:500px;font:900 50px Nunito;white-space:nowrap">kuniga <span class="t-terra">10 marta</span> =</div>
 <div class="a cx" data-t="57.6" data-a="none" style="top:580px;display:flex;gap:4px">{palms10}</div>
 <div class="a cx" data-t="60.2" data-a="pop" style="top:760px;display:flex;align-items:baseline;gap:20px;white-space:nowrap"><div style="font:900 50px Nunito;white-space:nowrap">1 yilda</div><div class="serif" style="font-size:130px;color:var(--green);line-height:1"><span class="count" data-t="60.3" data-d="1.2" data-from="0" data-to="3650">0</span></div><div style="font:900 44px Nunito;white-space:nowrap">ta daraxt</div></div>
 <div class="a cx" data-t="61.6" data-a="stamp" data-d=".3" data-r="-3" style="top:960px"><div class="stamp" style="font-size:80px;border-color:var(--green);color:var(--green)">BUTUN BIR BOG‘</div></div>
</section>
<section class="scene" data-s="62.3" data-e="70.4">
 <div class="a" data-t="62.4" data-a="left" data-r="-1.5" style="left:70px;top:290px"><div class="card" style="width:430px;text-align:center;padding:28px">{house.format(w=130,h=120)}<div style="font:900 34px Nunito;color:#8A847A;margin-top:10px">dunyoda uy</div><div class="serif" style="font-size:62px;color:var(--terra)">yillar</div></div></div>
 <div class="a" data-t="65.0" data-a="right" data-r="1.5" style="left:580px;top:290px"><div class="card" style="width:430px;text-align:center;padding:28px;border:5px solid var(--green)">{palm.format(w=110,h=137)}<div style="font:900 34px Nunito;color:#8A847A;margin-top:4px">jannatda bog‘</div><div class="serif" style="font-size:62px;color:var(--green)">soniyalar</div></div></div>
 <div class="a cx" data-t="68.2" data-a="stamp" data-d=".3" data-r="-2" style="top:820px"><div class="stamp" style="font-size:48px;border-color:var(--green);color:var(--green)">TILINGIZ ZIKRDAN TO‘XTAMASIN</div></div>
</section>
'''
extra=f'''<div class="a cx" data-t="70.5" data-a="up" data-o="80.35" style="top:300px;font:900 54px Nunito;color:var(--green);white-space:nowrap">Har kuni — birgalikda</div>
<div class="a cx" data-t="80.45" data-a="pop" style="top:290px;display:flex;gap:22px"><div class="chip" style="font-size:40px">📌 Saqlab qo‘ying</div><div class="a chip" data-t="81.9" data-a="pop" style="position:relative;font-size:40px">📤 Yaqinlaringizga yuboring</div></div>
<div class="a cx" data-t="76.0" data-a="pop" style="top:1220px"><div class="chip" style="font-size:42px;white-space:nowrap;border:4px solid var(--terra)">💬 Izohlarga <span class="t-terra" style="font-size:56px">«+»</span> qoldiring</div></div>
<div class="a hand cx" data-t="77.4" data-a="fade" style="top:1335px;font-size:48px;color:#8A847A">yoki</div>
'''
c=C.cta(tas=71.1,zikr=72.85,extra=extra,havola=77.9,btn=79.0)
c=c.replace('style="top:1250px"><div class="chip"','style="top:1400px"><div class="chip"').replace('style="top:1400px"><div style="background:var(--gold)','style="top:1530px"><div style="background:var(--gold)').replace('top:1560px;font:700','top:1690px;font:700')
c=c.replace('style="top:1070px"><div style="background:var(--terra)','style="top:1060px"><div style="background:var(--terra)')
s+=c+'''
<div id="sub" data-hide="72.75"><div id="subbox"></div></div></div>'''+C.TASBEH+'</body></html>'
open('/home/claude/reel11/index.html','w').write(HEAD+b+s)
print('ok')
