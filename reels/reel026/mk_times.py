import json,sys
sys.path.insert(0,'/home/claude')
exec(open('/home/claude/build4.py').read().split('# ---------- reel004 ----------')[0].split('import cta as C')[1])
T={'t0':[5.0,5.3,5.6,5.9],'qOff':4.9,'s1':9.0,'days':22.9,'weekFall':21.36,'s2':25.68,'dots':30.2,'clean':37.6,'s3':41.04,'swap':54.64,'plant':48.96,'s4':58.56,'three':75.12,'s5':76.24,'stack':76.5,'cta':81.32,'end':93.7,'ctaTas':81.9,'ctaZikr':83.12,'ctaHav':88.08,'ctaBtn':89.6}
def lab(t,txt,o,cls=''): return f'<div class="a" data-t="{t}" data-a="left" data-o="{o}" data-r="-2" style="left:70px;top:236px"><div class="label {cls}">{txt}</div></div>'
def title(t,html,o,top=330,fs=62): return f'<div class="a cx" data-t="{t}" data-a="pop" data-o="{o}" data-r="-.6" style="top:{top}px"><div class="card tape" style="width:900px;text-align:center;padding:34px 40px"><div class="serif" style="font-size:{fs}px;line-height:1.15">{html}</div></div></div>'
def ayah(t,src,ar,body,o,top=320,fs=46):
    a=f'<div class="arabic" style="font-size:54px;line-height:1.7;margin-top:10px;color:var(--green)">{ar}</div>' if ar else ''
    return f'<div class="a cx" data-t="{t}" data-a="pop" data-o="{o}" data-r="-.5" style="top:{top}px"><div class="card tape ayah"><div class="caps">{src}</div>{a}<div class="serif" style="font-size:{fs}px;line-height:1.25;margin-top:14px;color:var(--ink)">{body}</div></div></div>'
def chip(t,html,top,o=None,left=None,fs=42,r=-1):
    oo=f' data-o="{o}"' if o else ''
    pos=f'left:{left}px' if left is not None else ''
    cls='a' if left is not None else 'a cx'
    return f'<div class="{cls}" data-t="{t}" data-a="pop" data-r="{r}"{oo} style="{pos};top:{top}px"><div class="chip" style="font-size:{fs}px">{html}</div></div>'
def hand(t,txt,top,o=None,col='var(--green)',fs=64):
    oo=f' data-o="{o}"' if o else ''
    return f'<div class="a hand cx" data-t="{t}" data-a="up" data-r="-2"{oo} style="top:{top}px;font-size:{fs}px;color:{col};white-space:nowrap">{txt}</div>'
def stamp(t,txt,top,col='terra',fs=80):
    st='' if col=='terra' else 'border-color:var(--green);color:var(--green);'
    return f'<div class="a cx" data-t="{t}" data-a="stamp" data-d=".3" data-r="-3" style="top:{top}px"><div class="stamp" style="font-size:{fs}px;{st}">{txt}</div></div>'
h=[]
h.append(f'<div id="banner" data-s="9.0" data-e="81.2">Iymon sustlashmasligi uchun 4 tavsiya</div>')
# HOOK
h.append('<section class="scene" data-s="-1" data-e="9.0">')
h.append(title(0.0,'Iymon <span class="t-terra">sustlashmasligi</span> uchun','',260,70).replace(' data-o=""',''))
h.append(hand(2.4,'qanday tavsiyalar bor?',480))
h.append(stamp(4.92,'4 TA TAVSIYA',1180))
h.append(chip(6.28,'⏱ har biri — kuniga bir necha daqiqa',1330,fs=38))
h.append('</section>')
# S1
h.append('<section class="scene" data-s="9.0" data-e="25.68">')
h.append(lab(9.0,'1-tavsiya',25.6))
h.append(title(9.9,'Oz bo‘lsa ham, <span class="t-terra">doimiy</span> qiling',13.55))
h.append(ayah(13.6,'Imom Buxoriy, 6464','',rv([('«Allohga',13.68),('eng',14.36),('sevimli',14.56,'t-terra'),('amal',15.12,'t-terra'),('—',15.76),('oz',15.92),('bo‘lsa',16.04),('ham,',16.4),('doimiy',16.84,'t-green'),('qilinganidir»',17.28,'t-green')]),25.6))
h.append(hand(18.4,'Misol:',1150,o=25.6,col='var(--terra)',fs=56))
h.append(chip(19.2,'❌ haftada bir marta — uzoq',1240,o=25.6,fs=38,r=1))
h.append(chip(22.92,'✅ har kuni — bitta sahifa',1340,o=25.6,fs=38,r=-1))
h.append('</section>')
# S2
h.append('<section class="scene" data-s="25.68" data-e="41.04">')
h.append(lab(25.68,'2-tavsiya',41.0,'terra'))
h.append(title(26.64,'Gunohdan keyin <span class="t-terra">darhol</span> tavba',33.75))
h.append(chip(29.12,'⚫ gunoh — qalbda qora nuqta',1220,o=33.75,fs=38,r=1))
h.append(chip(31.64,'✨ tavba — uni tozalaydi',1320,o=33.75,fs=38))
h.append(ayah(33.8,'Misol · Imom Termiziy, 3334','',rv([('Kimnidir',34.56),('g‘iybat',35.0,'t-terra'),('qilib',35.36),('qo‘ydingizmi?',35.56)]),41.0,330,50))
h.append(stamp(37.6,'ASTAG‘FIRULLOH',1230,'green',72))
h.append(hand(39.36,'nuqta qotib qolmasin',1380,o=41.0,col='var(--terra)',fs=56))
h.append('</section>')
# S3
h.append('<section class="scene" data-s="41.04" data-e="58.56">')
h.append(lab(41.04,'3-tavsiya',58.5,'gold'))
h.append(title(41.92,'Tilingizni <span class="t-green">zikrdan</span> bo‘shatmang',45.55))
h.append(ayah(45.6,'Imom Buxoriy, 6407','',rv([('«Robbini',45.6),('zikr',46.12,'t-green'),('qiladigan',46.32,'t-green'),('va',47.04),('qilmaydigan',47.2),('kishining',47.84),('misoli —',48.28),('tirik',48.96,'t-green'),('va',49.52),('o‘likning',49.72,'t-terra'),('misoli',50.28),('kabidir»',50.6)]),58.5))
h.append(hand(51.48,'Misol:',1150,o=58.5,col='var(--terra)',fs=56))
h.append(chip(52.24,'⏳ navbatda',1240,o=54.6,left=80,fs=38,r=-2))
h.append(chip(53.73,'🚗 tirbandlikda',1240,o=54.6,left=560,fs=38,r=2))
h.append(chip(54.64,'📱 ➜ 📿 telefon o‘rniga',1240,o=58.5,fs=38))
h.append(hand(55.84,'«Subhanalloh, Alhamdulillah»',1340,o=58.5,fs=58))
h.append('</section>')
# S4
h.append('<section class="scene" data-s="58.56" data-e="76.24">')
h.append(lab(58.56,'4-tavsiya',76.2))
h.append(title(59.52,'Shu duoni <span class="t-terra">ko‘p</span> qiling',64.45))
h.append(ayah(64.5,'Imom Termiziy, 2140','يَا مُقَلِّبَ الْقُلُوبِ ثَبِّتْ قَلْبِي عَلَى دِينِكَ','<div class="hand" style="font-size:44px;color:var(--terra);margin-bottom:6px">Yo muqollibal qulub, sabbit qalbiy ‘ala diynik</div>'+rv([('«Ey',68.83),('qalblarni',69.04,'t-terra'),('o‘zgartiruvchi',69.6),('Zot,',70.32),('qalbimni',70.96,'t-green'),('diningda',71.6),('sobit',72.16,'t-green'),('qil»',72.56)]),76.2,300,44))
h.append(chip(73.24,'🕌 har namozdan keyin — <span class="t-terra">3 marta</span>',1250,o=76.2,fs=40))
h.append('</section>')
# S5
h.append('<section class="scene" data-s="76.24" data-e="81.32">')
h.append(title(76.24,'Iymon — katta ishlar bilan emas,<br><span class="t-green">har kungi kichik odatlar</span> bilan saqlanadi','',300,56).replace(' data-o=""',''))
h.append('</section>')
T['html']='\n'.join(h)
extra='''<div class="a cx" data-t="90.84" data-a="pop" style="top:290px;display:flex;gap:22px"><div class="chip" style="font-size:34px">📌 Saqlab qo‘ying</div><div class="a chip" data-t="92.32" data-a="pop" style="position:relative;font-size:34px">📤 Yaqinlarga yuboring</div></div>'''
T['ctaExtra']=extra
json.dump(T,open('/home/claude/reel26/times.json','w'),ensure_ascii=False)
print('ok')
