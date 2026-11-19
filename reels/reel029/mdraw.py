# Metallic glowing line-art for the dark metal engine. Strokes draw progressively (.dr), fills fade (.a fade).
import math
DEFS='''<svg width="0" height="0" style="position:absolute"><defs>
<linearGradient id="gG" gradientUnits="userSpaceOnUse" x1="0" y1="0" x2="60" y2="220" spreadMethod="reflect"><stop offset="0" stop-color="#FFF4C9"/><stop offset=".35" stop-color="#F2C861"/><stop offset=".55" stop-color="#B9862C"/><stop offset=".8" stop-color="#F7D88A"/><stop offset="1" stop-color="#FFF0B8"/></linearGradient>
<linearGradient id="gS" gradientUnits="userSpaceOnUse" x1="0" y1="0" x2="60" y2="220" spreadMethod="reflect"><stop offset="0" stop-color="#FFFFFF"/><stop offset=".35" stop-color="#D7DDE4"/><stop offset=".55" stop-color="#7F8996"/><stop offset=".8" stop-color="#E3E8EE"/><stop offset="1" stop-color="#FFFFFF"/></linearGradient>
<linearGradient id="gC" gradientUnits="userSpaceOnUse" x1="0" y1="0" x2="60" y2="220" spreadMethod="reflect"><stop offset="0" stop-color="#FFD9C2"/><stop offset=".35" stop-color="#EE9A6A"/><stop offset=".55" stop-color="#9C4524"/><stop offset=".8" stop-color="#F0A47A"/><stop offset="1" stop-color="#FFD0B3"/></linearGradient>
<linearGradient id="gE" gradientUnits="userSpaceOnUse" x1="0" y1="0" x2="60" y2="220" spreadMethod="reflect"><stop offset="0" stop-color="#DFFFF1"/><stop offset=".35" stop-color="#7FE0B9"/><stop offset=".55" stop-color="#1E7A57"/><stop offset=".8" stop-color="#8FE8C4"/><stop offset="1" stop-color="#D2FBE8"/></linearGradient>
<linearGradient id="gD" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#2A303A"/><stop offset="1" stop-color="#11151B"/></linearGradient>
<radialGradient id="gGlow"><stop offset="0" stop-color="#FFE7A0" stop-opacity=".55"/><stop offset="1" stop-color="#FFE7A0" stop-opacity="0"/></radialGradient>
<radialGradient id="gBlue"><stop offset="0" stop-color="#9FD3FF" stop-opacity=".5"/><stop offset="1" stop-color="#9FD3FF" stop-opacity="0"/></radialGradient>
<radialGradient id="gFire"><stop offset="0" stop-color="#FFE3A0"/><stop offset=".4" stop-color="#F28A3C"/><stop offset="1" stop-color="#9C2A10" stop-opacity="0"/></radialGradient>
<filter id="fg" filterUnits="userSpaceOnUse" x="-2000" y="-2000" width="5000" height="5000"><feGaussianBlur stdDeviation="3.5" result="b"/><feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge></filter>
</defs></svg>'''
G,S,C,E='url(#gG)','url(#gS)','url(#gC)','url(#gE)'
DARK='url(#gD)'

def P(d,t,c=G,w=6,dur=.6,glow=True):
    f=' filter="url(#fg)"' if glow else ''
    return f'<path class="dr" data-t="{t:.2f}" data-d="{dur}" d="{d}" fill="none" stroke="{c}" stroke-width="{w}" stroke-linecap="round" stroke-linejoin="round"{f}/>'
def F(d,t,c=DARK,op=1,o=None):
    oo=f' data-o="{o}"' if o else ''
    return f'<path class="a" data-a="fade" data-t="{t:.2f}" data-d=".5"{oo} d="{d}" fill="{c}" fill-opacity="{op}" style="opacity:0"/>'
def FC(cx,cy,r,t,c=G,a='pop',o=None,op=1):
    oo=f' data-o="{o}"' if o else ''
    return f'<circle class="a" data-a="{a}" data-t="{t:.2f}" data-d=".4"{oo} cx="{cx}" cy="{cy}" r="{r}" fill="{c}" fill-opacity="{op}" style="opacity:0"/>'
def TX(x,y,txt,t,c=G,fs=60,a='pop',fam='Fraunces',w=900,o=None):
    oo=f' data-o="{o}"' if o else ''
    return f'<text class="a" data-a="{a}" data-t="{t:.2f}" data-d=".4"{oo} x="{x}" y="{y}" text-anchor="middle" font-family="{fam}" font-weight="{w}" font-size="{fs}" fill="{c}" style="opacity:0">{txt}</text>'
def glow(cx,cy,r,t,c='url(#gGlow)',o=None):
    return FC(cx,cy,r,t,c,'fade',o)
def circ(cx,cy,r): return f'M{cx-r} {cy} a{r} {r} 0 1 0 {2*r} 0 a{r} {r} 0 1 0 {-2*r} 0'

def box(inner,vb,t,top,w,left=None,o=None,f=0,r=0,a='none'):
    vw,vh=vb; h=round(w*vh/vw)
    oo=f' data-o="{o}"' if o else ''
    ff=f' data-f="{f}"' if f else ''
    pos=f'left:{left}px;' if left is not None else ''
    cls='a' if left is not None else 'a cx'
    return f'<div class="{cls}" data-t="{t:.2f}" data-a="{a}" data-r="{r}"{oo}{ff} style="{pos}top:{top}px"><svg width="{w}" height="{h}" viewBox="0 0 {vw} {vh}" style="overflow:visible">{inner}</svg></div>'

def arrow(x1,y1,x2,y2,t,c=G,w=6,bend=0):
    mx,my=(x1+x2)/2+bend,(y1+y2)/2-abs(bend)*.3
    a=math.atan2(y2-my,x2-mx); L=24
    h1=(x2-L*math.cos(a-.5),y2-L*math.sin(a-.5)); h2=(x2-L*math.cos(a+.5),y2-L*math.sin(a+.5))
    return P(f'M{x1} {y1} Q{mx} {my} {x2} {y2}',t,c,w,.45)+P(f'M{h1[0]:.0f} {h1[1]:.0f} L{x2} {y2} L{h2[0]:.0f} {h2[1]:.0f}',t+.4,c,w,.2)
def check(x,y,s,t,c=E,w=10): return P(f'M{x} {y} l{s*.35:.0f} {s*.35:.0f} l{s*.65:.0f} {-s*.75:.0f}',t,c,w,.35)
def cross(x,y,s,t,c=C,w=10): return P(f'M{x} {y} l{s} {s}',t,c,w,.25)+P(f'M{x+s} {y} l{-s} {s}',t+.2,c,w,.25)
def ring(cx,cy,r,t,c=G,w=5,dur=.7): return P(circ(cx,cy,r),t,c,w,dur)
def spark(cx,cy,s,t,c=G,w=5):
    return P(f'M{cx} {cy-s} L{cx} {cy+s}',t,c,w,.2)+P(f'M{cx-s} {cy} L{cx+s} {cy}',t+.1,c,w,.2)
def numc(cx,cy,n,t,c=G):
    return FC(cx,cy,42,t+.1,DARK,'pop')+P(circ(cx,cy,42),t,c,5,.35)+TX(cx,cy+20,n,t+.25,c,56)

# ---------- icons (each in its own viewBox, ~200 wide) ----------
def key(t,c=G):
    s=glow(60,60,70,t+.4)+F(circ(60,60,40),t+.3)+P(circ(60,60,40),t,c,8,.5)+P(circ(60,60,16),t+.3,c,6,.3)
    s+=P('M100 60 L230 60',t+.4,c,10,.4)+P('M190 60 L190 92 M215 60 L215 84',t+.7,c,9,.3)
    return s  # vb 250x120
def lock(t,c=S):
    s=F('M20 70 h120 v100 h-120z',t+.3)+P('M20 70 h120 v100 h-120z',t,c,7,.5)+P('M45 70 v-25 a35 35 0 0 1 70 0 v25',t+.3,c,7,.4)
    s+=FC(80,112,10,t+.6,c)+P('M80 120 v22',t+.7,c,7,.2)
    return s  # 160x180
def calendar(t,label='ERTAGA',c=G):
    s=F('M10 30 h180 v170 h-180z',t+.3)+P('M10 30 h180 v170 h-180z',t,c,6,.5)+P('M10 75 h180',t+.3,c,6,.3)+P('M55 14 v30 M145 14 v30',t+.4,c,7,.2)
    s+=TX(100,64,label,t+.5,c,30,'fade','Nunito',900)
    return s  # 200x210
def qmark(t,c=G,fs=170): return TX(100,175,'?',t,c,fs,'pop')
def crystal(t,c=S,crack=None):
    s=glow(100,95,95,t+.3,'url(#gBlue)')+F(circ(100,95,75),t+.3,'#1B2A3E',.9)+P(circ(100,95,75),t,c,7,.6)
    s+=P('M60 70 a45 45 0 0 1 40 -30',t+.6,'#FFFFFF',5,.3,False)
    s+=F('M50 175 h100 l-14 -26 h-72z',t+.4)+P('M50 175 h100 l-14 -26 h-72z',t+.2,G,6,.4)
    if crack: s+=P('M100 22 l-12 30 l18 18 l-16 28 l14 22',crack,C,6,.35)
    return s  # 200x190
def coffee(t,c=S):
    s=F('M30 70 h110 c0 60 -20 90 -55 90 c-35 0 -55 -30 -55 -90z',t+.3)+P('M30 70 h110 c0 60 -20 90 -55 90 c-35 0 -55 -30 -55 -90z',t,c,6,.5)
    s+=P('M140 90 c30 0 30 40 -4 44',t+.4,c,6,.3)+P('M20 170 h130',t+.5,c,6,.3)
    for i in range(3): s+=P(f'M{60+i*25} 55 c-10 -12 10 -20 0 -34',t+.7+i*.1,G,4,.3)
    return s  # 180x180
def zodiac(t,c=G):
    s=P(circ(100,100,85),t,c,5,.6)+P(circ(100,100,55),t+.3,c,4,.5)
    for i in range(12):
        a=i*math.pi/6; s+=P(f'M{100+55*math.cos(a):.0f} {100+55*math.sin(a):.0f} L{100+85*math.cos(a):.0f} {100+85*math.sin(a):.0f}',t+.5+i*.03,c,3,.15)
    s+=spark(100,100,22,t+.9,c,4)
    return s  # 200x200
def cards(t,c=S):
    s=''
    for i,(x,r) in enumerate([(40,-14),(80,0),(120,14)]):
        d=f'M{x} 30 h70 v110 h-70z'
        s+=f'<g transform="rotate({r} {x+35} 150)">'+F(d,t+i*.1+.2)+P(d,t+i*.1,c,5,.4)+TX(x+35,100,'★',t+.4+i*.1,G,40)+'</g>'
    return s  # 230x180
def eye_veil(t,c=S):
    s=F('M10 80 C60 20 160 20 210 80 C160 140 60 140 10 80Z',t+.3)+P('M10 80 C60 20 160 20 210 80 C160 140 60 140 10 80Z',t,c,6,.5)
    s+=FC(110,80,26,t+.4,G)+P('M20 150 C70 120 150 120 200 150',t+.6,G,5,.4)+P('M20 10 C70 40 150 40 200 10',t+.7,G,5,.4)
    return s  # 220x160
def cloud_rain(t,c=S):
    s=F('M40 90 a30 30 0 0 1 20 -50 a40 40 0 0 1 76 6 a28 28 0 0 1 24 44z',t+.3)+P('M40 90 a30 30 0 0 1 20 -50 a40 40 0 0 1 76 6 a28 28 0 0 1 24 44z',t,c,6,.5)
    for i in range(4): s+=P(f'M{60+i*25} 108 l-8 22',t+.5+i*.08,'url(#gS)',5,.2)
    return s  # 180x140
def pin(t,c=G):
    s=F('M90 170 C60 120 40 95 40 70 a50 50 0 0 1 100 0 C140 95 120 120 90 170Z',t+.3)+P('M90 170 C60 120 40 95 40 70 a50 50 0 0 1 100 0 C140 95 120 120 90 170Z',t,c,6,.6)+FC(90,70,16,t+.5,c)
    return s  # 180x180
def hourglass(t,c=G):
    s=P('M40 20 h100 M40 180 h100',t,c,7,.3)+P('M50 20 C50 80 130 80 130 100 C130 120 50 120 50 180 M130 20 C130 80 50 80 50 100 C50 120 130 120 130 180',t+.2,S,5,.7)
    s+=F('M70 150 l20 -30 l20 30 z',t+.6,G)
    return s  # 180x200
def seed(t,c=E):
    s=glow(90,90,70,t+.3)+F(circ(90,95,48),t+.3)+P(circ(90,95,48),t,c,6,.5)+FC(90,95,14,t+.5,G)+P('M90 47 C80 25 95 12 110 10',t+.6,c,5,.3)
    return s  # 180x160
def chest(t,c=G):
    s=F('M20 80 h180 v90 h-180z',t+.3)+P('M20 80 h180 v90 h-180z',t,c,6,.5)+P('M20 80 C20 30 200 30 200 80',t+.3,c,6,.4)+P('M20 110 h180',t+.5,c,5,.3)
    s+=F('M95 100 h30 v30 h-30z',t+.6,G)+glow(110,60,80,t+.7)
    for i in range(3): s+=spark(60+i*50,40-i*6,10,t+.8+i*.1)
    return s  # 220x180
def shield(t,c=G,inner=None):
    d='M100 10 L180 40 C180 110 150 160 100 190 C50 160 20 110 20 40Z'
    s=glow(100,100,110,t+.4)+F(d,t+.3)+P(d,t,c,7,.7)
    if inner: s+=inner
    return s  # 200x200
def moon_stars(t,c=G):
    s=F('M130 20 A70 70 0 1 0 130 160 A48 70 0 0 1 130 20Z',t+.3,G,.95)+glow(110,90,90,t+.3)
    for x,y in [(170,40),(190,110),(30,30)]: s+=spark(x,y,10,t+.6)
    return s  # 210x180
def rug(t):
    s=F('M30 20 h140 v200 h-140z',t+.4,'#3A2016')+P('M30 20 h140 v200 h-140z',t,C,6,.6)+P('M100 60 C70 70 64 100 64 120 L136 120 C136 100 130 70 100 60Z',t+.5,G,6,.4)
    for i in range(7): s+=P(f'M{38+i*21} 220 l0 18',t+.8+i*.04,G,4,.15)
    return s  # 200x240
def pillar(t,c=S):
    s=P('M60 40 h80 M50 20 h100 M60 200 h80 M50 220 h100',t,G,8,.4)+F('M70 40 h60 v160 h-60z',t+.3)+P('M70 40 v160 M130 40 v160 M90 50 v140 M110 50 v140',t+.3,c,4,.5)
    return s+glow(100,120,120,t+.6)  # 200x240
def book(t,c=G):
    s=F('M100 40 C70 24 40 22 14 30 L14 150 C40 142 70 144 100 160 Z',t+.4)+F('M100 40 C130 24 160 22 186 30 L186 150 C160 142 130 144 100 160 Z',t+.4)
    s+=P('M100 40 C70 24 40 22 14 30 L14 150 C40 142 70 144 100 160',t,c,6,.6)+P('M100 40 C130 24 160 22 186 30 L186 150 C160 142 130 144 100 160',t+.15,c,6,.6)+P('M100 40 L100 160',t+.4,c,5,.3)
    for i in range(4):
        y=58+i*20; s+=P(f'M30 {y} C50 {y-4} 70 {y-2} 88 {y+4}',t+.7+i*.1,S,3,.25,False)+P(f'M112 {y+4} C130 {y-2} 150 {y-4} 170 {y}',t+.75+i*.1,S,3,.25,False)
    return glow(100,95,110,t+.5)+s  # 200x170
def waves(t,c=G,n=3):
    s=''
    for i in range(n):
        r=30+i*28; s+=P(f'M{-r*.7:.0f} {-r*.7:.0f} A{r} {r} 0 0 1 {-r*.7:.0f} {r*.7:.0f}'.replace('M-','M-'),t+i*.2,c,5,.3)
    return s
def flame(t):
    d='M60 170 C20 150 15 100 45 70 C50 95 60 100 62 100 C55 70 70 35 95 15 C95 50 125 70 125 110 C125 145 100 170 60 170Z'
    return glow(70,110,90,t+.3,'url(#gFire)')+F(d,t+.3,C,.85)+P(d,t,G,5,.6)  # 140x180
def rays(t):
    s=glow(80,80,80,t+.2)+FC(80,80,26,t+.2,'#FFF6D8')
    for i in range(12):
        a=i*math.pi/6; s+=P(f'M{80+36*math.cos(a):.0f} {80+36*math.sin(a):.0f} L{80+66*math.cos(a):.0f} {80+66*math.sin(a):.0f}',t+.3+i*.03,G,5,.15)
    return s  # 160x160
def soil(t):
    d='M10 140 C30 80 70 60 90 60 C110 60 150 80 170 140Z'
    return F(d,t+.3,'#6B4A2E')+P(d,t,C,6,.5)+P('M50 110 c10 -6 20 -6 30 0 M100 100 c10 -6 20 -6 30 0',t+.5,G,4,.3)  # 180x150
def crescent_dome(t):
    s=F('M40 160 v-40 a60 60 0 0 1 120 0 v40z',t+.3)+P('M40 160 v-40 a60 60 0 0 1 120 0 v40z M20 160 h160',t,G,6,.6)
    s+=P('M100 60 v-24',t+.5,G,5,.2)+F('M108 14 a14 14 0 1 0 0 22 a11 11 0 1 1 0 -22z',t+.6,G)
    return s  # 200x170
def bone(t,c=S):
    d='M40 60 a18 18 0 1 1 22 -20 L138 40 a18 18 0 1 1 22 20 a18 18 0 1 1 -22 20 L62 80 a18 18 0 1 1 -22 -20z'
    return F(d,t+.3,'#2A2F38')+P(d,t,c,6,.6)  # 200x120
def bone_gold(t):
    d='M40 60 a18 18 0 1 1 22 -20 L138 40 a18 18 0 1 1 22 20 a18 18 0 1 1 -22 20 L62 80 a18 18 0 1 1 -22 -20z'
    return glow(100,60,100,t)+F(d,t,G,.95)
def staff(t,c=G):
    s=P('M100 10 C80 10 75 40 95 40 L95 230',t,c,8,.7)
    return s  # 200x240
def termite(t):
    s=''
    for i,dx in enumerate([0,16,32]): s+=FC(80+dx,200,9-i,t+i*.08,C)
    s+=P('M74 194 l-10 -8 M74 206 l-10 8',t+.3,C,3,.15,False)
    return s
def web(t,c=S):
    s=''
    for i in range(8):
        a=i*math.pi/4; s+=P(f'M100 100 L{100+90*math.cos(a):.0f} {100+90*math.sin(a):.0f}',t+i*.04,c,3,.25,False)
    for r in (30,55,80):
        pts=' L'.join(f'{100+r*math.cos(i*math.pi/4):.0f} {100+r*math.sin(i*math.pi/4):.0f}' for i in range(9))
        s+=P('M'+pts,t+.4+r/200,c,3,.4,False)
    return s  # 200x200
def door(t,c=G):
    s=F('M40 20 h120 v200 h-120z',t+.3)+P('M40 20 h120 v200 h-120z',t,c,7,.6)+FC(140,125,8,t+.5,c)
    return s  # 200x230
def mask(t):
    d='M30 40 C70 20 130 20 170 40 C170 110 140 150 100 150 C60 150 30 110 30 40Z'
    return F(d,t+.3,'#2A1A16')+P(d,t,C,6,.6)+P('M60 75 c10 -10 25 -10 35 0 M105 75 c10 -10 25 -10 35 0',t+.4,C,5,.3)+P('M70 115 c20 12 40 12 60 0',t+.6,C,5,.3)  # 200x170
def dots_grid(t,hl=(4,6),dur=1.6):
    s=''
    for i in range(100):
        r,cc=divmod(i,10); x=20+cc*36; y=20+r*36
        if (r,cc)==hl: continue
        s+=FC(x,y,9,t+ (i/100)*dur,'#5B6270','fade')
    x=20+hl[1]*36; y=20+hl[0]*36
    s+=glow(x,y,46,t+dur+.2)+FC(x,y,15,t+dur+.2,G)
    return s  # 360x360
def meteor(t,x1,y1,x2,y2):
    return P(f'M{x1} {y1} L{x2} {y2}',t,C,6,.35)+FC(x2,y2,10,t+.3,'url(#gFire)','pop')
