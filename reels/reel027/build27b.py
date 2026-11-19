import sys;sys.path.insert(0,'/home/claude')
from build2d import *
from doodle import *
T=json.load(open('/home/claude/reel27/times.json'))
D={}
# hook: heart pointed at 3x, then 4 numbers
g=f'<g transform="translate(270,60) scale(1.8)">{heart(0.4)}</g>'
for (x1,y1,x2,y2,b),t in zip([(60,40,240,150,40),(840,40,660,150,-40),(450,-10,450,50,0)],T['pulse']): g+=arrow(x1,y1,x2,y2,t-.1,GREEN,7,b)
for (x,y),t,n in zip([(90,300),(810,300),(90,440),(810,440)],T['t0'],'1234'): g+=numc(x,y,n,t)
D[0]=[box(g,(900,500),0.4,660,880,f=3)]
# S1: window + phone -> put down
D[1]=[box(window_moon(21.2),(200,240),21.2,640,300,left=110,f=2),
      box(phone(22.32),(220,210),22.32,660,300,left=600,o=25.2),
      box(eye_slash(23.6),(200,120),23.6,960,240,left=420,o=25.2),
      box(phone(25.3,False)+check(150,150,90,25.7),(260,220),25.3,660,320,left=600)]
# S2: blob -> star erases; house; heart
D[2]=[box(blob(T['bad']),(200,160),T['bad'],650,330,left=110,o=32.4),
      box(arrow(0,60,180,60,29.5),(200,120),29.5,720,220,left=430,o=33.2),
      box(star(T['good'])+spark(30,30,20,32.5)+spark(170,40,18,32.7),(200,180),T['good'],640,320,left=640,o=33.2),
      box(house(34.16),(200,200),34.16,640,360,o=38.6,f=2),
      box(heart(T['heart2'])+spark(20,20,18,39.2)+spark(185,30,18,39.4),(200,180),T['heart2'],660,400,f=3)]
# S3: cups -> smile
D[3]=[box(cup(41.68)+cup(41.9,200),(380,180),41.68,650,560,o=47.4),
      box(smile(T['smile']),(200,200),T['smile'],640,380,f=3)]
# S4: plates
D[4]=[box(plate(53.6,'?','#5A4A86')+f'<g transform="translate(140,10)">{coins(54.0)}</g>'+cross(40,30,120,61.9),(200,140),53.6,700,400,left=60,o=T['away']),
      box(plate(55.64,'✓',GREEN),(200,140),55.64,700,400,left=620,f=2)]
# S5: heart with rings
h5=f'<g transform="translate(150,90)">{heart(64.2)}</g>'+ring(250,180,190,150,64.9,GOLD,6,.8)+ring(250,180,230,180,65.4,GOLD,4,.8)
D[5]=[box(h5,(500,360),64.2,700,620,f=3)]
build('reel27','/home/claude/reel27b',D,fixes=[('🚶 navbatda','⏳ navbatda')])
print('ok')
