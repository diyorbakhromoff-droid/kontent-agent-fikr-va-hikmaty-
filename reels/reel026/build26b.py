import sys;sys.path.insert(0,'/home/claude')
from build2d import *
from doodle import *
T=json.load(open('/home/claude/reel26/times.json'))
t0=T['t0']
D={}
# hook: heart + 4 numbers
g=f'<g transform="translate(250,40) scale(2)">{heart(0.3)}</g>'
for (x,y),t in zip([(110,90),(790,90),(110,400),(790,400)],t0): g+=numc(x,y,str(t0.index(t)+1),t)
D[0]=[box(g,(900,480),0.3,600,900,f=4)]
# S1: book, then week
D[1]=[box(book(10.0),(200,180),10.0,600,420,o=13.5,f=3)]
wk=''
for i,L in enumerate(['D','S','Ch','P','J','Sh','Y']):
    x=10+i*132; d=f'M{x} 40 h112 v112 h-112z'
    wk+=F(d,13.9+i*.08,'#FBF7EE')+P(d,13.8+i*.08,INK,5,.3)+TX(x+56,30,L,14.0+i*.08,GREEN,44)
    wk+=check(x+28,100,58,22.92+i*.14)
wk+=ring(10+6*132+56,96,78,78,19.2,TERRA,7,.5)+TX(820,230,'faqat shu kun?',19.5,TERRA,50)
D[1].append(box(wk,(940,250),13.8,720,940))
# S2: heart with dots -> clean
import random;random.seed(4)
hd=f'<g transform="scale(2.5)">{heart(26.9)}</g>'
pts=[(150,120),(230,100),(300,130),(180,190),(260,200),(330,190),(210,260),(280,270),(240,330),(120,160),(370,150),(250,150)]
for i,(x,y) in enumerate(pts): hd+=FC(x,y,16,T['dots']-.8+i*.12,'#2A2724','pop',o=T['clean']+i*.05)
for i,(x,y) in enumerate([(140,110),(360,120),(250,220),(170,300),(330,290)]): hd+=spark(x,y,22,T['clean']+.3+i*.15)
D[2]=[box(hd,(500,450),26.9,600,520,f=3)]
# S3: tasbeh; plants; phone -> tasbeh
D[3]=[box(tasbeh(42.3),(200,220),42.3,560,330,o=45.5,f=3),
      box(plant(T['plant']),(200,210),T['plant'],720,300,left=150,o=54.5),
      box(plant(49.72,False),(200,210),49.72,720,300,left=630,o=54.5),
      box(phone(54.7)+cross(50,60,100,55.3),(200,210),54.7,740,230,left=160),
      box(arrow(0,60,170,60,55.4),(200,120),55.4,820,220,left=430),
      box(tasbeh(55.8),(200,220),55.8,730,280,left=660,f=3)]
# S4: rug; heart + 1-2-3
D[4]=[box(rug(60.0),(200,240),60.0,560,280,o=64.45,f=3)]
h4=f'<g transform="translate(0,10) scale(1)">{heart(70.96)}</g>'+check(70,70,60,72.2,GREEN,10)
for i in range(3): h4+=numc(300+i*120,95,str(i+1),T['three']+i*.25,TERRA)
D[4].append(box(h4,(600,190),70.96,960,620))
# S5: bricks + heart
bk=bricks(T['stack'])+f'<g transform="translate(110,6) scale(.4)">{heart(T["stack"]+1.6)}</g>'
D[5]=[box(bk,(300,260),T['stack'],650,560,f=2)]
build('reel26','/home/claude/reel26b',D)
print('ok')
