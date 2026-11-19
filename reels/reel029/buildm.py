import sys,os,shutil,json
sys.path.insert(0,'/home/claude'); sys.path.insert(0,'/home/claude/metal')
import cta as CTA
from mdraw import *

def rv(pairs):
    out=[]
    for w,t,*c in pairs:
        cc=(' '+c[0]) if c else ''
        out.append(f'<span class="rv{cc}" data-t="{t}">{w}</span>')
    return ' '.join(out)
def W(s,e,hl=None):
    """auto-reveal text from words.json between s and e; hl: dict word->class"""
    hl=hl or {}
    ws=[w for w in WORDS if s-0.05<=w['s']<e]
    return rv([(w['w'],round(w['s'],2),hl[w['w']]) if w['w'] in hl else (w['w'],round(w['s'],2)) for w in ws])
def T(word,after=0,nth=1):
    k=0
    for w in WORDS:
        if w['s']>=after and w['w'].strip('«»,.!?:;—').lower().startswith(word.lower()):
            k+=1
            if k==nth: return round(w['s'],2)
    raise KeyError(word)

def oo(o): return f' data-o="{o}"' if o else ''
def lab(t,txt,o,cls=''): return f'<div class="a" data-t="{t}" data-a="left" data-r="-2"{oo(o)} style="left:70px;top:236px"><div class="label {cls}">{txt}</div></div>'
def title(t,html,o=None,top=330,fs=60,caps=''):
    c=f'<div class="caps" style="margin-bottom:14px">{caps}</div>' if caps else ''
    return f'<div class="a cx" data-t="{t}" data-a="pop"{oo(o)} style="top:{top}px"><div class="card tape" style="width:920px;text-align:center;padding:36px 40px">{c}<div class="serif" style="font-size:{fs}px;line-height:1.18">{html}</div></div></div>'
def ayah(t,src,ar,body,o=None,top=300,fs=46,arfs=54):
    a=f'<div class="arabic" style="font-size:{arfs}px;line-height:1.75;margin-top:12px">{ar}</div>' if ar else ''
    return f'<div class="a cx" data-t="{t}" data-a="pop"{oo(o)} style="top:{top}px"><div class="card tape" style="width:940px;text-align:center;padding:42px 40px 38px"><div class="caps">{src}</div>{a}<div class="serif" style="font-size:{fs}px;line-height:1.25;margin-top:14px">{body}</div></div></div>'
def chip(t,html,top,o=None,left=None,fs=40,a='pop'):
    pos=f'left:{left}px;' if left is not None else ''
    cls='a' if left is not None else 'a cx'
    return f'<div class="{cls}" data-t="{t}" data-a="{a}"{oo(o)} style="{pos}top:{top}px"><div class="chip" style="font-size:{fs}px">{html}</div></div>'
def stamp(t,txt,top,fs=76,o=None,col=''):
    st={'green':'border-color:#7FE0B9;box-shadow:0 0 30px rgba(127,224,185,.3)','copper':'border-color:#EE9A6A;box-shadow:0 0 30px rgba(238,154,106,.3)'}.get(col,'')
    tc={'green':'t-green','copper':'t-terra'}.get(col,'t-gold')
    return f'<div class="a cx" data-t="{t}" data-a="stamp" data-d=".3" data-r="-2"{oo(o)} style="top:{top}px"><div class="stamp" style="font-size:{fs}px;{st}"><span class="{tc}">{txt}</span></div></div>'
def big(t,txt,top,fs=160,cls='mg',o=None,a='pop',extra=''):
    return f'<div class="a cx" data-t="{t}" data-a="{a}"{oo(o)} style="top:{top}px;white-space:nowrap;{extra}"><div class="{cls}" style="font-size:{fs}px;line-height:1">{txt}</div></div>'
def count(t,to,top,fs=260,cls='mg',sub='',o=None,d=1.2):
    s=f'<div class="{cls} count" data-t="{t}" data-d="{d}" data-from="0" data-to="{to}" style="font-size:{fs}px;line-height:1">0</div>'
    if sub: s+=f'<div class="ms" style="font-size:48px;margin-top:6px">{sub}</div>'
    return f'<div class="a cx" data-t="{t}" data-a="pop"{oo(o)} style="top:{top}px;text-align:center;white-space:nowrap">{s}</div>'
def scene(s,e,*items): return f'<section class="scene" data-s="{s}" data-e="{e}">'+''.join(items)+'</section>'

BG=['radial-gradient(ellipse at 50% 35%,#1E2A3A 0%,#0B0E13 70%)','radial-gradient(ellipse at 50% 35%,#2B2416 0%,#0C0B09 70%)',
    'radial-gradient(ellipse at 50% 35%,#16302A 0%,#090F0D 70%)','radial-gradient(ellipse at 50% 35%,#2E1C1A 0%,#0E0909 70%)',
    'radial-gradient(ellipse at 50% 35%,#251F33 0%,#0C0B11 70%)','radial-gradient(ellipse at 50% 35%,#1C2733 0%,#0A0D11 70%)']

def build(reel,src,scenes_html,cuts,banner,cta_t,extra='',dur=None):
    dst=f'/home/claude/{reel}'
    for f in ['style.css','engine.js','metal.js','render.js','snap.js']: shutil.copy(f'/home/claude/metal/{f}',f'{dst}/{f}')
    if not os.path.exists(f'{dst}/fonts'): shutil.copytree('/home/claude/metal/fonts',f'{dst}/fonts')
    os.makedirs(f'{dst}/snaps',exist_ok=True)
    bgl=''.join(f'<div class="bg" data-s="{a}" data-e="{b}" style="background:{BG[i%len(BG)]}"></div>' for i,(a,b) in enumerate(zip([-1]+cuts,cuts+[999])))
    head='''<!doctype html><html><head><meta charset="utf-8"><link rel="stylesheet" href="style.css"><script src="words.js"></script><script src="engine.js"></script>
<style>svg .a{transform-box:fill-box;transform-origin:center}</style></head><body><div id="stage">'''+DEFS
    CTA.SCENE_S=str(cta_t['s'])
    c=CTA.cta(tas=cta_t['tas'],zikr=cta_t['zikr'],extra=extra,havola=cta_t['hav'],btn=cta_t['btn'])
    c=c.replace('color:#8A847A','color:#9AA3AF').replace('font-size:130px;line-height:1"','font-size:130px;line-height:1;color:#F2C861"')
    tas=CTA.TASBEH.replace("'#2E6B5B'","'#7FE0B9'").replace('#D9D1C3','#2C323C').replace("'#E2A63A'","'#F2C861'")
    ban=f'<div id="banner" data-s="{banner[1]}" data-e="{banner[2]}">{banner[0]}</div>'
    page=head+bgl+'<div id="dust"></div><div class="grain"></div><div class="vign"></div>'+ban+scenes_html+c+f'''
<div id="sub" data-hide="{cta_t['s']-.1}"><div id="subbox"></div></div></div>'''+tas+'<script src="metal.js"></script><script>window.render(0)</script></body></html>'
    open(f'{dst}/index.html','w').write(page)
    print('built',reel)

def load_words(reel):
    global WORDS
    WORDS=json.load(open(f'/home/claude/{reel}/words.json'))['words']
    import buildm; buildm.WORDS=WORDS
    return WORDS
