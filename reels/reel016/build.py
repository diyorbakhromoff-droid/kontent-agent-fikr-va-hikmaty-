import sys; sys.path.insert(0,'/home/claude')
import cta as C
exec(open('/home/claude/build4.py').read().split('# ---------- reel004 ----------')[0].split('import cta as C')[1])
C.SCENE_S='78.45'
b=bgs([(-1,7.35,'#F1E6D6'),(7.35,21.9,'#F3E9CF'),(21.9,26.8,'#E5DDEB'),(26.8,33.7,'#DCE6DA'),(33.7,53.3,'#DAE2E9'),(53.3,60.5,'#F6E1D3'),(60.5,69.8,'#DCE6DA'),(69.8,78.45,'#F3E9CF'),(78.45,999,'#F1E6D6')])
shield='''<svg width="{w}" height="{h}" viewBox="0 0 100 120"><path d="M50 6L90 20v34c0 30-18 50-40 60C28 104 10 84 10 54V20z" fill="{c}"/><path d="M34 60l12 12 22-26" fill="none" stroke="#FBF7EE" stroke-width="9" stroke-linecap="round" stroke-linejoin="round"/></svg>'''
scroll='''<svg width="{w}" height="{h}" viewBox="0 0 120 140"><rect x="18" y="16" width="84" height="108" rx="6" fill="#FBF7EE" stroke="#8C7A62" stroke-width="5"/><rect x="10" y="8" width="100" height="16" rx="8" fill="#C9A76A"/><rect x="10" y="116" width="100" height="16" rx="8" fill="#C9A76A"/><path d="M34 46h52M34 62h52M34 78h40M34 94h46" stroke="#C9C2B6" stroke-width="5" stroke-linecap="round"/></svg>'''
def step(t,ico,txt,top,col='var(--ink)'):
    return f'<div class="a" data-t="{t}" data-a="left" style="left:110px;top:{top}px;display:flex;align-items:center;gap:22px"><div style="font-size:70px;line-height:1">{ico}</div><div class="chip" style="font-size:42px;color:{col}">{txt}</div></div>'
s=f'''
<div id="banner" data-s="7.35" data-e="78.2">Cho‘chqa go‘shti nega harom?</div>
<section class="scene" data-s="-1" data-e="7.35">
 <div class="a cx" data-t="0.05" data-a="pop" data-r="-1" style="top:300px"><div class="card tape" style="width:880px;text-align:center;padding:40px"><div class="serif" style="font-size:76px;line-height:1.15">Cho‘chqa go‘shti nega <span class="t-terra">harom?</span></div></div></div>
 <div class="a cx" data-t="1.9" data-a="fade" style="top:640px"><div style="position:relative;font:900 62px Nunito;color:#9A9388;white-space:nowrap">«chunki u iflos»<div class="strike" data-t="4.7"></div></div></div>
 <div class="a cx" data-t="5.0" data-a="stamp" data-d=".3" data-r="-3" style="top:800px"><div class="stamp" style="font-size:70px;border-color:var(--green);color:var(--green)">JAVOB CHUQURROQ</div></div>
</section>
<section class="scene" data-s="7.35" data-e="21.9">
 <div class="a cx" data-t="7.4" data-a="pop" data-r="-.6" style="top:290px"><div class="card tape ayah">
  <div class="caps">Baqara surasi · 173-oyat</div>
  <div class="arabic" style="font-size:50px;line-height:1.8;margin-top:12px;color:var(--green)">إِنَّمَا حَرَّمَ عَلَيْكُمُ الْمَيْتَةَ وَالدَّمَ وَلَحْمَ الْخِنزِيرِ وَمَا أُهِلَّ بِهِ لِغَيْرِ اللَّهِ</div>
  <div class="serif" style="font-size:42px;line-height:1.25;margin-top:12px;color:var(--ink)">{rv([('«Sizlarga',8.36),('o‘limtik,',8.97),('qon,',9.87),('cho‘chqa',10.39,'t-terra'),('go‘shti',10.77,'t-terra'),('va',11.44),('Allohdan',11.66),('boshqasining',12.16),('nomi',12.75),('bilan',13.01),('so‘yilgan',13.23),('narsa',13.68),('harom',14.24,'t-terra'),('qilindi»',14.54,'t-terra')])}</div></div></div>
 <div class="a cx" data-t="15.7" data-a="up" style="top:800px;font:900 46px Nunito;white-space:nowrap">Qur’onda <span class="t-terra">4 marta</span>:</div>
 <div class="a cx" data-t="16.3" data-a="none" style="top:880px;display:flex;gap:14px">
  <div class="a chip" data-t="16.3" data-a="pop" style="position:relative;font-size:32px">Baqara 173</div><div class="a chip" data-t="16.5" data-a="pop" style="position:relative;font-size:32px">Moida 3</div><div class="a chip" data-t="16.7" data-a="pop" style="position:relative;font-size:32px">An’om 145</div><div class="a chip" data-t="16.9" data-a="pop" style="position:relative;font-size:32px">Nahl 115</div></div>
 <div class="a cx" data-t="20.1" data-a="stamp" data-d=".3" data-r="-2" style="top:1020px"><div class="stamp" style="font-size:56px">«CHUNKI U NOPOKDIR»</div></div>
</section>
<section class="scene" data-s="21.9" data-e="26.8">
 <div class="a cx" data-t="21.95" data-a="up" style="top:300px;font:900 54px Nunito;white-space:nowrap">Qiziq tomoni:</div>
 <div class="a cx" data-t="24.6" data-a="pop" style="top:400px;display:flex;align-items:center;gap:26px">{scroll.format(w=170,h=198)}<div><div class="serif" style="font-size:72px;white-space:nowrap">Tavrotda ham</div><div class="caps" style="margin-top:8px">Levitlar, 11:7</div></div></div>
 <div class="a cx" data-t="22.8" data-a="stamp" data-d=".3" data-r="-2" style="top:700px"><div class="stamp" style="font-size:62px;border-color:var(--green);color:var(--green)">FAQAT ISLOMDA EMAS</div></div>
</section>
<section class="scene" data-s="26.8" data-e="33.7">
 <div class="a cx" data-t="26.85" data-a="up" style="top:290px;font:900 50px Nunito;white-space:nowrap">mo‘min uchun asosiy sabab —</div>
 <div class="a cx" data-t="28.55" data-a="stamp" data-d=".3" style="top:390px"><div style="background:var(--green);color:#fff;font:900 90px Fraunces;padding:16px 48px;border-radius:10px;white-space:nowrap">ALLOHNING AMRI</div></div>
 <div class="a cx" data-t="30.0" data-a="fade" style="top:640px"><div style="position:relative;font:900 70px Nunito;color:#9A9388;white-space:nowrap">«nega?»<div class="strike" data-t="30.7"></div></div></div>
 <div class="a cx" data-t="31.2" data-a="up" style="top:790px"><div class="card tape" style="width:860px;text-align:center;padding:32px;border:5px solid var(--green)"><div class="serif" style="font-size:60px">«Eshitdik va itoat qildik»</div><div class="caps" style="margin-top:8px">Baqara, 285</div></div></div>
</section>
<section class="scene" data-s="33.7" data-e="53.3">
 <div class="a cx" data-t="33.75" data-a="pop" style="top:280px"><div class="label">🔬 ilm ham hikmatni ochmoqda</div></div>
 <div class="a cx" data-t="37.7" data-a="fade" style="top:400px"><div class="caps" style="white-space:nowrap">Jahon sog‘liqni saqlash tashkiloti (JSST)</div></div>
 {step(40.3,'🥩','yaxshi pishmagan go‘sht',470)}
 {step(42.6,'🪱','tasmasimon chuvalchang',600)}
 {step(45.1,'🧠','lichinkalari miyaga tushsa',730)}
 {step(46.9,'⚠️','neyrotsistitserkoz',860,'var(--terra)')}
 <div class="a cx" data-t="50.7" data-a="stamp" data-d=".3" data-r="-2" style="top:1020px"><div class="card" style="width:900px;text-align:center;padding:26px;border:5px solid var(--terra)"><div class="serif" style="font-size:44px;line-height:1.2">oldini olsa bo‘ladigan epilepsiyaning <span class="t-terra">eng ko‘p uchraydigan sababi</span></div></div></div>
</section>
<section class="scene" data-s="53.3" data-e="60.5">
 <div class="a cx" data-t="53.35" data-a="up" style="top:300px"><div class="card tape" style="width:860px;text-align:center;padding:34px"><div class="serif" style="font-size:56px">hukm faqat <span class="t-terra">sog‘liq uchun emas</span></div></div></div>
 <div class="a cx" data-t="56.9" data-a="pop" style="top:560px;display:flex;align-items:center;gap:20px"><div style="font-size:90px;line-height:1">🔥</div><div class="chip" style="font-size:46px">qanchalik yaxshi pishirilmasin</div></div>
 <div class="a cx" data-t="58.9" data-a="stamp" data-d=".3" data-r="-3" style="top:780px"><div class="stamp" style="font-size:54px">HAROM — HAROMLIGICHA</div></div>
</section>
<section class="scene" data-s="60.5" data-e="69.8">
 <div class="a" data-t="60.5" data-a="left" data-r="-1.5" style="left:80px;top:290px"><div class="card" style="width:600px;padding:28px 32px;display:flex;align-items:center;gap:22px"><div style="font-size:90px;line-height:1">🩺</div><div><div class="caps">shifokor</div><div class="serif" style="font-size:52px">«buni yemang»</div></div></div></div>
 <div class="a" data-t="63.2" data-a="pop" data-r="3" style="left:720px;top:330px"><div class="label">ishonamiz ✓</div></div>
 <div class="a cx" data-t="64.0" data-a="up" style="top:560px"><div class="card tape" style="width:880px;text-align:center;padding:34px;border:5px solid var(--green)"><div class="serif" style="font-size:52px;line-height:1.2">Bizni <span class="t-green">yaratgan</span> va bizni bizdan <span class="t-green">yaxshiroq biladigan</span> Zotning amriga-chi?</div></div></div>
 <div class="a cx" data-t="68.2" data-a="stamp" data-d=".3" data-r="-2" style="top:900px"><div class="stamp" style="font-size:60px;border-color:var(--green);color:var(--green)">UNDAN HAM KO‘PROQ</div></div>
</section>
<section class="scene" data-s="69.8" data-e="78.45">
 <div class="a cx" data-t="69.85" data-a="up" style="top:300px"><div class="card tape" style="width:860px;text-align:center;padding:32px"><div class="serif" style="font-size:54px">Alloh foydali narsani <span class="t-terra">hech qachon</span> to‘smaydi</div></div></div>
 <div class="a cx" data-t="72.4" data-a="pop" data-f="4" style="top:560px">{shield.format(w=220,h=264,c="#2E6B5B")}</div>
 <div class="a cx" data-t="73.9" data-a="up" style="top:860px;font:900 52px Nunito;white-space:nowrap">har bir taqiq ortida — <span class="t-green">himoya</span></div>
 <div class="a cx" data-t="75.6" data-a="fade" style="top:960px"><div class="hand" style="font-size:56px;color:#8A847A;white-space:nowrap">bugun anglaymizmi yoki ertaga…</div></div>
</section>
'''
extra=f'''<div class="a cx" data-t="78.55" data-a="up" data-o="86.95" style="top:300px;font:900 54px Nunito;color:var(--green);white-space:nowrap">Har kuni — birgalikda</div>
<div class="a cx" data-t="87.05" data-a="pop" style="top:290px;display:flex;gap:22px"><div class="chip" style="font-size:40px">📌 Saqlab qo‘ying</div><div class="a chip" data-t="88.4" data-a="pop" style="position:relative;font-size:40px">📤 Yaqiningizga yuboring</div></div>
<div class="a cx" data-t="82.8" data-a="pop" style="top:1220px"><div class="chip" style="font-size:42px;white-space:nowrap;border:4px solid var(--terra)">💬 Izohlarga <span class="t-terra" style="font-size:56px">«+»</span> qoldiring</div></div>
<div class="a hand cx" data-t="84.2" data-a="fade" style="top:1335px;font-size:48px;color:#8A847A">yoki</div>
'''
c=C.cta(tas=78.7,zikr=80.0,extra=extra,havola=84.6,btn=85.8)
c=c.replace('style="top:1250px"><div class="chip"','style="top:1400px"><div class="chip"').replace('style="top:1400px"><div style="background:var(--gold)','style="top:1530px"><div style="background:var(--gold)').replace('top:1560px;font:700','top:1690px;font:700')
c=c.replace('style="top:1070px"><div style="background:var(--terra)','style="top:1060px"><div style="background:var(--terra)')
s+=c+'''
<div id="sub" data-hide="79.9"><div id="subbox"></div></div></div>'''+C.TASBEH+'</body></html>'
open('/home/claude/reel16/index.html','w').write(HEAD+b+s)
print('ok')
