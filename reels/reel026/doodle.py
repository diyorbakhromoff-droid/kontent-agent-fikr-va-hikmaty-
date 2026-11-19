# Hand-drawn "daftar" doodles for the 2D paper engine (paths with class dr draw progressively).
INK='#2A2724'; TERRA='#C4553B'; GREEN='#2E6B5B'; GOLD='#E2A63A'; GREY='#9A9388'; PEACH='#F2B8A2'; SAGE='#BFD6C6'; LAV='#CFC3E6'
HEART='M100 168 C40 126 10 92 10 58 C10 30 32 12 58 12 C78 12 92 24 100 40 C108 24 122 12 142 12 C168 12 190 30 190 58 C190 92 160 126 100 168Z'

def P(d,t,c=INK,w=6,dur=.6,fill='none',extra=''):
    return f'<path class="dr" data-t="{t:.2f}" data-d="{dur}" d="{d}" fill="{fill}" stroke="{c}" stroke-width="{w}" stroke-linecap="round" stroke-linejoin="round" {extra}/>'
def F(d,t,c,op=1):  # fill that fades in
    return f'<path class="a" data-a="fade" data-t="{t:.2f}" data-d=".5" d="{d}" fill="{c}" style="opacity:0" fill-opacity="{op}"/>'
def FC(cx,cy,r,t,c,a='fade',o=None):
    oo=f' data-o="{o}"' if o else ''
    return f'<circle class="a" data-a="{a}" data-t="{t:.2f}" data-d=".4"{oo} cx="{cx}" cy="{cy}" r="{r}" fill="{c}" style="opacity:0"/>'
def TX(x,y,txt,t,c=INK,fs=60,a='fade'):
    return f'<text class="a" data-a="{a}" data-t="{t:.2f}" data-d=".4" x="{x}" y="{y}" text-anchor="middle" font-family="Caveat" font-weight="700" font-size="{fs}" fill="{c}" style="opacity:0">{txt}</text>'

def box(svg_inner,vb,t,top,w,left=None,o=None,f=0,r=0):
    vw,vh=vb; h=round(w*vh/vw)
    oo=f' data-o="{o}"' if o else ''
    ff=f' data-f="{f}"' if f else ''
    pos=f'left:{left}px;' if left is not None else ''
    cls='a' if left is not None else 'a cx'
    return f'<div class="{cls}" data-t="{t:.2f}" data-a="none" data-r="{r}"{oo}{ff} style="{pos}top:{top}px"><svg width="{w}" height="{h}" viewBox="0 0 {vw} {vh}" style="overflow:visible">{svg_inner}</svg></div>'

def heart(t,fill=PEACH,stroke=TERRA):
    return F(HEART,t+.5,fill)+P(HEART,t,stroke,7,.9)+P('M52 46 C44 52 40 62 42 72',t+.9,'#fff',6,.3)

def arrow(x1,y1,x2,y2,t,c=INK,w=6,bend=0):
    mx,my=(x1+x2)/2+bend,(y1+y2)/2-abs(bend)*.3
    import math
    a=math.atan2(y2-my,x2-mx); L=26
    h1=(x2-L*math.cos(a-.5),y2-L*math.sin(a-.5)); h2=(x2-L*math.cos(a+.5),y2-L*math.sin(a+.5))
    return P(f'M{x1} {y1} Q{mx} {my} {x2} {y2}',t,c,w,.45)+P(f'M{h1[0]:.0f} {h1[1]:.0f} L{x2} {y2} L{h2[0]:.0f} {h2[1]:.0f}',t+.4,c,w,.2)

def check(x,y,s,t,c=GREEN,w=9):
    return P(f'M{x} {y} l{s*.35:.0f} {s*.35:.0f} l{s*.65:.0f} {-s*.75:.0f}',t,c,w,.35)
def cross(x,y,s,t,c=TERRA,w=9):
    return P(f'M{x} {y} l{s} {s}',t,c,w,.25)+P(f'M{x+s} {y} l{-s} {s}',t+.2,c,w,.25)
def ring(cx,cy,rx,ry,t,c=TERRA,w=6,dur=.6):
    return P(f'M{cx-rx} {cy} a{rx} {ry} 0 1 0 {2*rx} 0 a{rx} {ry} 0 1 0 {-2*rx} 0',t,c,w,dur)
def spark(cx,cy,s,t,c=GOLD,w=6):
    return P(f'M{cx} {cy-s} L{cx} {cy+s}',t,c,w,.2)+P(f'M{cx-s} {cy} L{cx+s} {cy}',t+.1,c,w,.2)+P(f'M{cx-s*.6} {cy-s*.6} L{cx+s*.6} {cy+s*.6}',t+.2,c,w*.7,.2)+P(f'M{cx+s*.6} {cy-s*.6} L{cx-s*.6} {cy+s*.6}',t+.25,c,w*.7,.2)
def numc(cx,cy,n,t,c=GREEN):
    return FC(cx,cy,40,t+.2,'#FBF7EE')+P(f'M{cx-40} {cy} a40 40 0 1 0 80 0 a40 40 0 1 0 -80 0',t,c,6,.35)+TX(cx,cy+20,n,t+.25,c,58)

def book(t):
    s=F('M100 40 C70 24 40 22 14 30 L14 150 C40 142 70 144 100 160 Z',t+.6,'#FBF5E6')+F('M100 40 C130 24 160 22 186 30 L186 150 C160 142 130 144 100 160 Z',t+.6,'#FBF5E6')
    s+=P('M100 40 C70 24 40 22 14 30 L14 150 C40 142 70 144 100 160',t,INK,6,.6)+P('M100 40 C130 24 160 22 186 30 L186 150 C160 142 130 144 100 160',t+.2,INK,6,.6)+P('M100 40 L100 160',t+.5,INK,5,.3)
    for i in range(4):
        y=58+i*20
        s+=P(f'M30 {y} C50 {y-4} 70 {y-2} 88 {y+4}',t+.8+i*.12,GREEN,4,.25)+P(f'M112 {y+4} C130 {y-2} 150 {y-4} 170 {y}',t+.85+i*.12,GREEN,4,.25)
    s+=P('M60 175 L100 160 L140 175',t+.9,'#8C7A62',7,.3)
    return s

def tasbeh(t,n=11,col=GREEN):
    import math
    s=''
    for i in range(n):
        a=math.pi*(.15+.7*i/(n-1))*2- math.pi*.5
        x=100+70*math.cos(a); y=90+70*math.sin(a)
        s+=FC(round(x),round(y),13,t+i*.05,col,'pop')
    s+=P('M100 160 L100 196',t+.5,GOLD,6,.2)+FC(100,204,10,t+.6,GOLD,'pop')
    return s

def plant(t,alive=True):
    c=GREEN if alive else '#A08A6A'
    s=F('M60 150 L140 150 L130 200 L70 200 Z',t+.4,'#E0A684')+P('M60 150 L140 150 L130 200 L70 200 Z',t,INK,6,.4)
    if alive:
        s+=P('M100 150 C100 110 100 80 100 40',t+.4,c,7,.4)
        s+=F('M100 100 C70 90 60 70 64 56 C84 60 98 76 100 100Z',t+.8,'#9CCB9A')+P('M100 100 C70 90 60 70 64 56 C84 60 98 76 100 100Z',t+.7,c,5,.3)
        s+=F('M100 80 C130 70 140 50 136 36 C116 40 102 56 100 80Z',t+.9,'#9CCB9A')+P('M100 80 C130 70 140 50 136 36 C116 40 102 56 100 80Z',t+.8,c,5,.3)
        s+=F('M100 44 C90 30 92 16 100 8 C108 16 110 30 100 44Z',t+1.0,'#9CCB9A')+P('M100 44 C90 30 92 16 100 8 C108 16 110 30 100 44Z',t+.95,c,5,.3)
    else:
        s+=P('M100 150 C104 120 96 100 112 82 C122 70 128 74 132 86',t+.4,c,7,.5)
        s+=P('M104 118 C86 116 76 124 72 136',t+.8,c,5,.3)+P('M110 92 C120 100 126 112 124 124',t+.9,c,5,.3)
    return s

def phone(t,glow=True):
    s=F('M60 10 h80 a14 14 0 0 1 14 14 v170 a14 14 0 0 1 -14 14 h-80 a14 14 0 0 1 -14 -14 v-170 a14 14 0 0 1 14 -14z',t+.4,'#3A3836')
    if glow: s+=F('M60 30 h80 v150 h-80z',t+.6,'#BFE3F2')
    s+=P('M60 10 h80 a14 14 0 0 1 14 14 v170 a14 14 0 0 1 -14 14 h-80 a14 14 0 0 1 -14 -14 v-170 a14 14 0 0 1 14 -14z',t,INK,6,.5)
    if glow:
        for i,(x1,x2) in enumerate([(160,190),(166,200),(160,190)]):
            y=60+i*40; s+=P(f'M{x1} {y} L{x2} {y-10+i*10}',t+.7+i*.1,GOLD,5,.2)
            s+=P(f'M{200-x1} {y} L{200-x2} {y-10+i*10}',t+.75+i*.1,GOLD,5,.2)
    return s

def rug(t):
    s=F('M30 20 h140 v200 h-140z',t+.5,'#E9A089')+F('M48 40 h104 v160 h-104z',t+.6,'#F6E1D3')
    s+=P('M30 20 h140 v200 h-140z',t,INK,6,.6)+P('M100 60 C70 70 64 100 64 120 L136 120 C136 100 130 70 100 60Z',t+.6,GREEN,6,.4)
    for i in range(7): s+=P(f'M{38+i*21} 220 l0 18',t+.9+i*.04,TERRA,5,.15)+P(f'M{38+i*21} 20 l0 -18',t+.9+i*.04,TERRA,5,.15)
    return s

def window_moon(t):
    s=F('M20 20 h160 v200 h-160z',t+.4,'#334A6E')+P('M20 20 h160 v200 h-160z',t,INK,7,.5)+P('M100 20 v200 M20 120 h160',t+.4,INK,6,.4)
    s+=F('M140 50 a28 28 0 1 0 0 56 a22 22 0 1 1 0 -56z',t+.8,'#F6E7B5')
    for x,y in [(50,50),(70,170),(150,170),(60,95)]: s+=FC(x,y,4,t+.9,'#F6E7B5','pop')
    return s

def eye_slash(t):
    s=F('M20 60 C60 10 140 10 180 60 C140 110 60 110 20 60Z',t+.3,'#FBF7EE')+P('M20 60 C60 10 140 10 180 60 C140 110 60 110 20 60Z',t,INK,6,.5)
    s+=FC(100,60,22,t+.4,INK,'pop')+P('M30 110 L170 10',t+.6,TERRA,8,.3)
    return s

def blob(t):
    d='M60 40 C90 10 140 20 150 50 C175 60 170 110 140 120 C120 150 70 150 55 120 C25 115 20 70 60 40Z'
    s=F(d,t+.3,'#4A4540')
    for i in range(6): s+=P(f'M{50+i*16} {60+(i%2)*20} C{70+i*12} {40+i*10} {90+i*8} {120-i*6} {120+i*4} {90+(i%3)*10}',t+i*.06,INK,6,.25)
    return s

def star(t,c=GOLD):
    d='M100 10 L122 70 L186 72 L134 110 L152 172 L100 136 L48 172 L66 110 L14 72 L78 70Z'
    return F(d,t+.4,'#F4D27A')+P(d,t,c,6,.6)

def house(t):
    s=F('M40 90 h120 v100 h-120z',t+.4,'#BFD6C6')+P('M20 100 L100 26 L180 100',t,TERRA,9,.4)+P('M40 90 v100 h120 v-100',t+.3,INK,6,.4)
    s+=F('M86 130 h28 v60 h-28z',t+.6,GOLD)+P('M150 40 v30',t+.5,INK,6,.2)
    return s

def cup(t,x=0):
    s=F(f'M{x+30} 70 h110 c0 60 -20 90 -55 90 c-35 0 -55 -30 -55 -90z',t+.4,'#FBF7EE')
    s+=P(f'M{x+30} 70 h110 c0 60 -20 90 -55 90 c-35 0 -55 -30 -55 -90z',t,INK,6,.5)+F(f'M{x+38} 80 h94 c-2 10 -4 16 -6 22 h-82 c-2 -6 -4 -12 -6 -22z',t+.5,'#C98A5A')
    s+=P(f'M{x+140} 90 c30 0 30 40 -4 44',t+.4,INK,6,.3)+P(f'M{x+20} 170 h130',t+.5,INK,6,.3)
    for i in range(3): s+=P(f'M{x+60+i*25} 55 c-10 -12 10 -20 0 -34',t+.8+i*.1,GREY,5,.3)
    return s

def smile(t,c=GOLD):
    s=FC(100,100,84,t+.3,'#F7DC86')+P('M16 100 a84 84 0 1 0 168 0 a84 84 0 1 0 -168 0',t,INK,7,.6)
    s+=FC(72,82,10,t+.5,INK,'pop')+FC(128,82,10,t+.55,INK,'pop')+P('M60 118 C80 150 120 150 140 118',t+.7,TERRA,8,.4)
    return s

def plate(t,mark,c):
    s=F('M10 100 a90 34 0 1 0 180 0 a90 34 0 1 0 -180 0',t+.3,'#FBF7EE')+P('M10 100 a90 34 0 1 0 180 0 a90 34 0 1 0 -180 0',t,INK,6,.5)+P('M40 100 a60 20 0 1 0 120 0 a60 20 0 1 0 -120 0',t+.4,GREY,4,.4)
    s+=TX(100,90,mark,t+.6,c,110,'pop')
    return s

def coins(t):
    s=''
    for i in range(4): s+=F(f'M{20} {60-i*14} a40 12 0 1 0 80 0 a40 12 0 1 0 -80 0',t+i*.12,'#E9C46A')+P(f'M{20} {60-i*14} a40 12 0 1 0 80 0 a40 12 0 1 0 -80 0',t+i*.12,'#9A7420',4,.3)
    return s

def bricks(t,n=8,c=(GREEN,GOLD,TERRA,'#8FB5A6')):
    s=''
    pos=[(20,200),(110,200),(200,200),(65,150),(155,150),(20,100),(110,100),(200,100)][:n]
    for i,(x,y) in enumerate(pos):
        d=f'M{x} {y} h84 v44 h-84z'; s+=F(d,t+i*.18+.15,c[i%len(c)],.85)+P(d,t+i*.18,INK,5,.25)
    return s
