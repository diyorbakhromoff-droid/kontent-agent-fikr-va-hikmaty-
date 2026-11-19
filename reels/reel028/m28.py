import sys; sys.path.insert(0,'/home/claude/metal')
import buildm
from buildm import *
load_words('reel28'); W=buildm.W
h=[]
# S0 hook
h.append(scene(-1,12.5,
  big(0.0,'ERTAGA',300,150,'mg'),
  big(0.64,'nima bo‘ladi?',470,72,'ms',o=9.0),
  box(calendar(0.3,'ERTAGA')+qmark(1.2,G,120).replace('y="175"','y="185"'),(200,210),0.3,580,300,o=3.4,f=3),
  box(crystal(3.6),(200,190),3.6,640,280,left=40,o=9.0,f=3),
  chip(3.7,'🔮 folbin',920,o=9.0,left=80,fs=34),
  box(zodiac(4.64),(200,200),4.64,640,280,left=400,o=9.0,f=3),
  chip(4.7,'♈ goroskop',920,o=9.0,left=420,fs=34),
  box(coffee(6.16),(180,180),6.16,650,260,left=770,o=9.0,f=3),
  chip(6.2,'☕ kofe foli',920,o=9.0,left=770,fs=34),
  title(9.16,W(9.1,12.4,{'Payg‘ambarimiz':'t-gold','bilmaganlar.':'t-terra'}),top=640,fs=58),
  stamp(11.36,'BILMAGANLAR',1000,84,col='copper')))
# S1 g'ayb
h.append(scene(12.5,19.2,
  big(12.56,'G‘AYB',300,190,'mg'),
  chip(13.4,'= ko‘zimizdan yashirin narsalar',540,fs=40),
  box(eye_veil(13.6),(220,160),13.6,680,560,f=3),
  chip(15.92,'🕰 kelajak',1130,left=70,fs=40),
  chip(16.88,'📜 taqdir',1130,left=400,fs=40),
  chip(17.72,'💭 qalbdagi sirlar',1260,fs=40)))
# S2 An'om 59
h.append(scene(19.2,26.0,
  ayah(19.25,'An’om surasi · 59-oyat','وَعِندَهُ مَفَاتِحُ الْغَيْبِ لَا يَعْلَمُهَا إِلَّا هُوَ',W(21.1,25.9,{'kalitlari':'t-gold','faqat':'t-terra','U':'t-terra'}),fs=50),
  box(key(21.76)+f'<g transform="translate(300,-10)">{lock(22.5)}</g>',(470,190),21.76,820,820,f=3),
  stamp(24.44,'FAQAT U BILADI',1170,70)))
# S3 Bukhari 4697 five keys
items=[('ertaga','📅',calendar,(200,210),29.64,'ertangi kun'),('ona','🌱',seed,(180,160),31.12,'ona qornidagi'),
       ('yomg','🌧',cloud_rain,(180,140),33.12,'yomg‘ir vaqti'),('vafot','📍',pin,(180,180),34.96,'vafot joyi'),('qiy','⏳',hourglass,(180,200),37.2,'Qiyomat soati')]
pos=[(60,560),(400,560),(740,560),(230,900),(570,900)]
k=[]
for (n,em,fn,vb,t,lb),(x,y) in zip(items,pos):
    g=fn(t) if fn!=calendar else calendar(t,'')
    k.append(box(g,vb,t,y,200,left=x+40,f=2))
    k.append(chip(t+.2,lb,y+215,left=x,fs=30))
h.append(scene(26.0,42.4,
  title(26.0,'G‘aybning <span class="t-gold">kalitlari</span> — <span class="t-terra">beshta</span>',caps='Imom Buxoriy · 4697',top=290,fs=60),
  *k, stamp(39.84,'FAQAT ALLOH BILADI',1250,64)))
# S4 A'rof 188
h.append(scene(42.4,51.6,
  title(42.4,'Hatto Payg‘ambarimizga <span class="t-gold">buyurilgan</span>:',o=45.2,top=300,fs=56),
  ayah(45.28,'A’rof surasi · 188-oyat','',W(45.2,51.5,{'g‘aybni':'t-gold','yaxshilik':'t-green','yomonlik':'t-terra'}),top=300,fs=50),
  box(chest(46.96),(220,180),46.96,820,380,left=80,f=3),
  box(shield(49.36,G,check(60,100,80,50.3)),(200,200),49.36,800,340,left=640,f=3)))
# S5 folbin + Muslim 2230
h.append(scene(51.6,63.28,
  title(51.6,'Unda <span class="t-terra">folbin</span> qanday biladi?',o=56.9,top=300,fs=62),
  box(crystal(52.16,S,crack=53.8),(200,190),52.16,560,420,o=56.9,f=3),
  stamp(53.8,'BILMAYDI!',1050,96,o=56.9,col='copper'),
  ayah(57.0,'Imom Muslim · 2230','',W(57.5,62.9,{'folbinga':'t-terra','qirq':'t-gold','kecha':'t-gold'}),top=300,fs=48),
  count(60.64,40,700,250,'mg','kecha',d=1.0),
  chip(61.68,'🕌 namozi qabul qilinmaydi',1080,fs=42)))
# S6 istixora
h.append(scene(63.28,74.32,
  title(63.28,'Kelajakdan <span class="t-terra">xavotirdamisiz</span>?',o=65.0,top=300,fs=62),
  title(65.12,'Folbin o‘rniga — <span class="t-green">istixora</span>',caps='Imom Buxoriy · 1166',top=300,fs=62),
  box(rug(66.08),(200,240),66.08,560,230,left=170,f=3),
  big(67.28,'2',560,230,'mg',extra='left:640px;transform:none'),
  chip(67.5,'rakat namoz',840,left=560,fs=40),
  ayah(69.88,'Duo','فَإِنَّكَ تَعْلَمُ وَلَا أَعْلَمُ وَأَنْتَ عَلَّامُ الْغُيُوبِ',W(69.8,74.2,{'bilasan,':'t-gold','biluvchisan.»':'t-gold'}),top=980,fs=46,arfs=48)))
# S7 xulosa
h.append(scene(74.32,79.6,
  title(74.32,W(74.3,75.9,{'shart':'t-terra'}),top=300,fs=60),
  box(pillar(76.32),(200,240),76.32,560,300,f=2),
  title(76.32,W(76.3,79.5,{'biladigan':'t-gold','suyanish':'t-green','kifoya.':'t-green'}),top=900,fs=56)))
extra=f'''<div class="a cx" data-t="{T('Videoni',80)}" data-a="pop" style="top:290px;display:flex;gap:22px"><div class="chip" style="font-size:34px">📌 Saqlab qo‘ying</div><div class="a chip" data-t="{T('yaqinlaringizga',85)}" data-a="pop" style="position:relative;font-size:34px">📤 Yaqinlarga yuboring</div></div>
<div class="a cx" data-t="{T('izohlarga',80)}" data-a="pop" data-o="{T('sahifamiz',80)-.2}" style="top:1250px"><div class="chip" style="font-size:42px">💬 Izohlarga <span class="t-gold" style="font-size:56px">«+»</span> qoldiring</div></div>'''
cuts=[12.5,19.2,26.0,42.4,51.6,63.28,74.32,79.6]
build('reel28','',''.join(h),cuts,('G‘aybni kim biladi?',12.5,79.5),
      {'s':79.6,'tas':80.2,'zikr':T('Zikr',80),'hav':T('sahifamiz',80),'btn':T('havola',80)},extra)
