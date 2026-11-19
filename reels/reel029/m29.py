import sys; sys.path.insert(0,'/home/claude/metal')
import buildm
from buildm import *
load_words('reel29'); W=buildm.W
h=[]
def flask(t):
    d='M80 20 h40 v50 l45 90 a20 20 0 0 1 -18 30 h-94 a20 20 0 0 1 -18 -30 l45 -90z'
    return F(d,t+.3)+P(d,t,S,6,.6)+glow(100,150,60,t+.5)
# S0 hook
h.append(scene(-1,7.4,
  title(0.0,'Folbinning gapi nega<br>ba’zan <span class="t-gold">to‘g‘ri chiqadi</span>?',top=290,fs=64),
  box(crystal(0.4)+qmark(1.0,G,110).replace('y="175"','y="135"'),(200,190),0.4,620,440,f=4),
  count(4.92,14,1110,140,'mg','asr oldin aytilgan',d=.8)))
# S1 Bukhari 5762
h.append(scene(7.4,23.9,
  chip(7.4,'💬 Sahobalar so‘radi',290,fs=36,o=23.8),
  title(9.92,'«Ular <span class="t-terra">hech narsa</span> emas»',caps='Imom Buxoriy · 5762',top=400,fs=66,o=16.9),
  chip(13.32,'🤔 «Axir ba’zan to‘g‘ri chiqadi-ku?»',720,fs=40,o=16.9),
  box(flask(17.4)+f'<g>{FC(100,40,10,18.3,G)}{FC(100,80,9,18.6,G)}{FC(100,120,8,18.9,G)}</g>',(200,200),17.4,400,300,o=20.8,f=3),
  chip(17.6,'jin so‘zni o‘g‘irlab — folbinga quyadi',740,fs=36,o=20.8),
  box(dots_grid(20.9,(4,6),1.4),(360,360),20.9,420,560,f=1),
  chip(22.16,'<span class="t-gold">1</span> haqiqat + <span class="t-terra">100</span> yolg‘on',1050,fs=48)))
# S2 Bukhari 4800 sky
sky=glow(300,60,260,26.08,'url(#gBlue)')+P('M20 70 C150 30 450 30 580 70',26.1,S,5,.8)+TX(300,40,'OSMON',26.3,S,34,'fade','Nunito',900)
for i in range(5): sky+=FC(300,560-i*90,24,29.6+i*.25,'#3A2A44','pop',o=(34.4 if i==4 else None))+P(circ(300,560-i*90,24),29.6+i*.25,C,4,.3)
sky+=meteor(33.76,560,10,320,190)+spark(320,190,26,34.1,C)
sky+=FC(300,200,9,36.2,G,'pop')+P('M300 210 L300 640',36.3,G,4,2.4)+FC(300,650,12,38.6,G,'pop')
sky+=TX(300,700,'YER · FOLBIN',38.2,G,32,'fade','Nunito',900)
h.append(scene(23.9,40.0,
  title(23.92,'Jin bu so‘zni <span class="t-gold">qayerdan</span> oladi?',caps='Imom Buxoriy · 4800',top=280,fs=58),
  box(sky,(600,720),26.0,540,600)))
# S3 Jin 9
mt=meteor(45.2,40,20,300,200)+meteor(46.4,560,40,330,230)+meteor(47.6,120,0,250,260)+glow(300,240,120,47.9,'url(#gFire)')
h.append(scene(40.0,48.88,
  title(40.0,'Jinlarning <span class="t-gold">o‘zi tan olgan</span>:',o=42.3,top=300,fs=62),
  ayah(42.4,'Jin surasi · 9-oyat','وَأَنَّا كُنَّا نَقْعُدُ مِنْهَا مَقَاعِدَ لِلسَّمْعِ ۖ فَمَن يَسْتَمِعِ الْآنَ يَجِدْ لَهُ شِهَابًا رَّصَدًا',W(42.4,48.8,{'tinglash':'t-gold','olovni':'t-terra'}),fs=46,arfs=46),
  box(mt,(600,300),45.1,930,600)))
# S4 Shuaro
h.append(scene(48.88,55.44,
  ayah(48.9,'Shuaro surasi · 221–222','هَلْ أُنَبِّئُكُمْ عَلَىٰ مَن تَنَزَّلُ الشَّيَاطِينُ ۝ تَنَزَّلُ عَلَىٰ كُلِّ أَفَّاكٍ أَثِيمٍ',W(50.3,55.4,{'yolg‘onchi':'t-terra','gunohkorga':'t-terra'}),fs=48,arfs=46),
  box(arrow(100,0,100,110,52.44,C)+f'<g transform="translate(0,130)">{mask(53.32)}</g>',(200,300),52.4,880,300,f=3)))
# S5 manba
h.append(scene(55.44,61.0,
  title(55.44,'Folbinning <span class="t-gold">manbai</span> — <span class="t-terra">shayton</span>',top=300,fs=64),
  big(58.48,'1',620,260,'mg',extra='left:300px'),
  chip(58.9,'haqiqat',920,left=210,fs=40),
  big(59.76,'100',620,260,'mc',extra='left:720px'),
  chip(60.2,'yolg‘on',920,left=640,fs=40)))
# S6 Muslim 537 / 2230
h.append(scene(61.0,69.73,
  title(61.0,'«Ularning oldiga <span class="t-terra">bormang</span>»',caps='Imom Muslim · 537',o=64.75,top=300,fs=64),
  box(door(63.6)+cross(55,60,90,64.04),(200,230),63.6,560,300,o=64.75,f=2),
  ayah(64.85,'Imom Muslim · 2230','',W(64.8,69.6,{'folbinga':'t-terra','qirq':'t-gold','kecha':'t-gold'}),top=300,fs=48),
  count(67.24,40,700,250,'mg','kecha',d=1.0),
  chip(67.88,'🕌 namozi qabul qilinmaydi',1080,fs=42)))
# S7 nomi har xil
lines=P(circ(100,100,80),70.8,S,5,.5)+P('M50 80 C80 60 120 60 150 90 M50 110 C90 100 120 110 150 130 M70 140 C90 130 110 135 130 150',71.0,G,4,.6)
h.append(scene(69.73,75.72,
  box(coffee(69.73),(180,180),69.73,380,230,left=110,f=2), chip(69.9,'kofe foli',620,left=110,fs=32),
  box(lines,(200,200),70.8,380,230,left=600,f=2), chip(71.0,'qo‘l chizig‘i',620,left=590,fs=32),
  box(cards(71.84),(230,180),71.84,720,260,left=100,f=2), chip(72.0,'karta',940,left=160,fs=32),
  box(zodiac(72.56),(200,200),72.56,700,240,left=610,f=2), chip(72.7,'goroskop',940,left=620,fs=32),
  stamp(73.6,'NOMI HAR XIL — ESHIGI BITTA',1100,52,col='copper')))
# S8 xulosa
h.append(scene(75.72,89.6,
  title(75.72,W(75.7,78.6,{'kelajagini':'t-gold','qaytmaydi.':'t-terra'}),top=290,fs=56),
  box(door(78.84)+glow(100,120,90,80.8,'url(#gFire)')+TX(100,130,'40',79.0,C,70),(200,230),78.84,560,320,o=82.8,f=2),
  chip(80.76,'🚪 eshigini shaytonga ochib qaytadi',960,fs=38,o=82.8),
  box(shield(82.91,G,TX(100,120,'ﷲ',84.0,G,90,'pop','Amiri',700)),(200,200),82.91,560,380,f=3),
  title(83.36,W(82.9,86.9,{'biluvchi':'t-gold','asrovchi':'t-gold','Alloh.':'t-green'}),top=1000,fs=50),
  chip(87.2,'🤲 Kelajagingizni <span class="t-gold">Undan</span> so‘rang',1230,fs=42)))
extra=f'''<div class="a cx" data-t="{T('Videoni',90)}" data-a="pop" style="top:290px;display:flex;gap:22px"><div class="chip" style="font-size:34px">📌 Saqlab qo‘ying</div><div class="a chip" data-t="{T('fol',100)}" data-a="pop" style="position:relative;font-size:34px">📤 Yaqinlarga yuboring</div></div>
<div class="a cx" data-t="{T('izohlarga',90)}" data-a="pop" data-o="{T('sahifamiz',90)-.2}" style="top:1250px"><div class="chip" style="font-size:42px">💬 Izohlarga <span class="t-gold" style="font-size:56px">«+»</span> qoldiring</div></div>'''
cuts=[7.4,23.9,40.0,48.88,55.44,61.0,69.73,75.72,89.6]
build('reel29','',''.join(h),cuts,('Folbin nega to‘g‘ri topadi?',7.4,89.5),
      {'s':89.6,'tas':90.2,'zikr':T('Zikr',90),'hav':T('sahifamiz',90),'btn':T('havola',90)},extra)
