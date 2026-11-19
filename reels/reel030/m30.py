import sys; sys.path.insert(0,'/home/claude/metal')
import buildm
from buildm import *
load_words('reel30'); W=buildm.W
h=[]
wv=''.join(P(f'M{160+i*30} {60-i*14} C{190+i*34} {80} {190+i*34} {120} {160+i*30} {140+i*14}',2.4+i*.2,G,5,.35) for i in range(3))
wv+=''.join(P(f'M{40-i*30} {60-i*14} C{10-i*34} {80} {10-i*34} {120} {40-i*30} {140+i*14}',2.5+i*.2,G,5,.35) for i in range(3))
# S0 hook
h.append(scene(-1,10.9,
  title(0.0,'Jinlar ham <span class="t-gold">Qur’on</span> tinglaydi?',top=290,fs=66),
  box(f'<g transform="translate(0,10)">{book(1.84)}</g>'+wv,(200,200),1.84,560,460,f=3),
  ayah(7.5,'Jin surasi · 1-oyat','إِنَّا سَمِعْنَا قُرْآنًا عَجَبًا',W(7.5,10.8,{'ajoyib':'t-gold','Qur’onni':'t-gold'}),top=1010,fs=50,arfs=56)))
# S1 4 fakt
h.append(scene(10.9,13.9,
  big(11.04,'JINLAR HAQIDA',520,70,'ms'),
  count(12.28,4,640,300,'mg','ta fakt',d=.8)))
# S2 fakt1
row=f'<g transform="translate(20,0)">{rays(19.76)}</g>'+TX(100,200,'nur',20.0,G,40,'fade','Nunito',900)
row+=f'<g transform="translate(330,-10)">{flame(20.64)}</g>'+TX(400,200,'olov',20.9,C,40,'fade','Nunito',900)
row+=f'<g transform="translate(610,30)">{soil(22.72)}</g>'+TX(700,200,'tuproq',23.0,S,40,'fade','Nunito',900)
h.append(scene(13.9,25.3,
  lab(13.92,'1-fakt',25.2), title(14.8,'Ular <span class="t-gold">insondan oldin</span> yaratilgan',caps='Hijr · 27 &nbsp;|&nbsp; Imom Muslim · 2996',top=330,fs=58),
  chip(19.09,'🕊 farishtalar',640,left=60,fs=34), chip(20.64,'🔥 jinlar',640,left=420,fs=34), chip(22.72,'🌍 Odam',640,left=760,fs=34),
  box(row,(800,220),19.7,760,900)))
# S3 fakt2
h.append(scene(25.3,35.2,
  lab(25.36,'2-fakt',35.1,'terra'), title(26.44,'Ular ham <span class="t-green">ibodat</span> uchun yaratilgan',caps='Zoriyot · 56',top=330,fs=58),
  box(crescent_dome(27.52),(200,170),27.52,600,360,f=3),
  chip(30.32,'<span class="t-green">✓</span> musulmonlari',1000,left=80,fs=40),
  chip(31.6,'<span class="t-terra">✗</span> zolimlari',1000,left=600,fs=40),
  stamp(33.08,'IBLIS HAM — JINLARDAN',1150,58,col='copper'),
  chip(33.6,'Jin · 14 &nbsp;|&nbsp; Kahf · 50',1290,fs=30)))
# S4 fakt3
h.append(scene(35.2,43.96,
  lab(35.2,'3-fakt',43.9,'gold'), title(36.16,'Ular ham <span class="t-gold">ovqatlanadi</span>',caps='Imom Muslim · 450',top=330,fs=62),
  chip(38.48,'🍽 «Bismillah»',580,fs=46),
  box(bone(40.36)+f'<g class="a" data-a="fade" data-t="41.76" data-d=".6" style="opacity:0">{bone_gold(41.76)}</g>'+spark(30,20,16,42.2)+spark(175,100,16,42.4)+spark(110,0,14,42.6),(200,120),40.36,760,560,f=3),
  chip(42.16,'suyak → go‘shtga to‘lib, rizq bo‘ladi',1130,fs=38)))
# S5 fakt4
st=staff(46.92)+termite(49.12)+f'<g class="a" data-a="fade" data-t="49.2" data-d="1.5" style="opacity:0">'+''.join(FC(84+i*10,190-i*30,4,49.4+i*.3,C,'pop') for i in range(5))+'</g>'
h.append(scene(43.96,53.28,
  lab(43.96,'4-fakt',53.2,'green'), title(44.88,'Ular <span class="t-gold">g‘aybni</span> bilmaydi',caps='Saba · 14',top=330,fs=62),
  box(st,(200,240),46.92,560,340,left=110,f=2),
  chip(47.4,'Sulaymon a.s. vafot etdi…',640,left=430,fs=34),
  chip(49.12,'…jinlar esa bilmadi',760,left=470,fs=34),
  chip(50.44,'⛏ og‘ir ishni davom ettirdi',880,left=430,fs=34),
  stamp(51.6,'G‘AYBNI BILMAYDI',1110,64)))
# S6 qo'rqish kerakmi
h.append(scene(53.28,65.5,
  title(53.28,'Ulardan <span class="t-terra">qo‘rqish</span> kerakmi?',o=57.3,top=330,fs=64),
  big(55.36,'YO‘Q!',620,220,'mg',o=57.3),
  ayah(57.4,'Baqara · 102','وَمَا هُم بِضَارِّينَ بِهِ مِنْ أَحَدٍ إِلَّا بِإِذْنِ اللَّهِ',W(57.4,61.5,{'iznisiz':'t-gold','zarar':'t-terra'}),top=300,fs=50,arfs=48),
  box(shield(58.72,G,check(60,100,80,59.9)),(200,200),58.72,760,300,left=110,f=3),
  box(web(62.8)+cross(40,40,120,63.6),(200,200),62.8,760,300,left=650,f=2),
  ayah(61.92,'Niso · 76','إِنَّ كَيْدَ الشَّيْطَانِ كَانَ ضَعِيفًا',W(62.7,65.4,{'zaifdir.»':'t-green'}),top=1110,fs=44,arfs=44)))
# S7 himoya
h.append(scene(65.5,81.5,
  title(65.52,'Himoya — <span class="t-green">juda oddiy</span>',caps='Imom Muslim · 2018 &nbsp;|&nbsp; Imom Buxoriy · 2311',top=300,fs=62),
  box(door(67.6)+TX(100,90,'Bismillah',69.92,G,23,'pop','Nunito',900),(200,230),67.6,580,300,left=110,f=2),
  chip(67.6,'🏠 uyga kirganda',880,left=70,fs=34,o=75.8),
  chip(68.72,'🍽 ovqatlanganda',990,left=70,fs=34,o=75.8),
  chip(71.33,'👋 shayton: «tunash ham, ovqat ham yo‘q»',1130,fs=34,o=75.8),
  box(moon_stars(75.88),(210,180),75.88,600,320,left=620,f=3),
  chip(76.8,'📖 Oyatal kursi — uxlashdan oldin',890,fs=38),
  box(shield(79.44),(200,200),79.44,1000,240,f=3),
  chip(80.16,'tong otguncha qo‘riqchi',1250,fs=36)))
# S8 xulosa
h.append(scene(81.5,92.5,
  title(81.52,W(81.5,83.9,{'qo‘rqqan':'t-terra','eshik':'t-terra'}),top=300,fs=56),
  title(84.32,W(84.3,87.5,{'suyangan':'t-gold','qo‘rqmaydi.':'t-green'}),top=560,fs=56),
  box(pillar(85.0),(200,240),85.0,800,220,f=2),
  big(90.96,'BITTA ZOT',1110,110,'mg')))
extra=f'''<div class="a cx" data-t="{T('Videoni',92)}" data-a="pop" style="top:290px;display:flex;gap:22px"><div class="chip" style="font-size:34px">📌 Saqlab qo‘ying</div><div class="a chip" data-t="{T('yaqinlaringizga',92)}" data-a="pop" style="position:relative;font-size:34px">📤 Yaqinlarga yuboring</div></div>
<div class="a cx" data-t="{T('izohlarga',92)}" data-a="pop" data-o="{T('sahifamiz',92)-.2}" style="top:1250px"><div class="chip" style="font-size:42px">💬 Izohlarga <span class="t-gold" style="font-size:56px">«+»</span> qoldiring</div></div>'''
cuts=[10.9,13.9,25.3,35.2,43.96,53.28,65.5,81.5,92.5]
build('reel30','',''.join(h),cuts,('Jinlar haqida 4 ta fakt',10.9,92.4),
      {'s':92.5,'tas':93.1,'zikr':T('Zikr',92),'hav':T('sahifamiz',92),'btn':T('havola',92)},extra)
