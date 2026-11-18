import sys,json; sys.path.insert(0,'/home/claude')
import cta as C
exec(open('/home/claude/build4.py').read().split('# ---------- reel004 ----------')[0].split('import cta as C')[1])
T=json.load(open('/home/claude/reel26/times.json'))
s1,s2,s3,s4,s5,cta,END=T['s1'],T['s2'],T['s3'],T['s4'],T['s5'],T['cta'],T['end']
C.SCENE_S=str(cta)
X=[0,70,140,210,280,350]
def st(i,dx,dy,dz,lx=0,ly=0,lz=0):
    f=1.55
    return [X[i]+lx+(dx-lx)*f,ly+(dy-ly)*1.25,lz+(dz-lz)*f],[X[i]+lx,ly,lz]
K=[]
def k(t,i,*a): p,l=st(i,*a);K.append([round(t,2),p,l])
# hook: close low on heart, pull back to see orbit
k(0,0, 3,10,22, 0,11,0); k(T['t0'][3]+.2,0, -8,16,30, 0,12,0); k(s1-.8,0, 14,22,36, 0,12,0)
# st1: swoop down to book, then over to days & weekly block
k(s1+.3,1, -14,18,22, -4,8,0); k(T['days']-.2,1, -4,14,24, 0,7,0); k(T['weekFall']+.4,1, 10,10,20, 8,4,2); k(s2-.6,1, 16,16,26, 6,5,0)
# st2: heart dots — push in, orbit around during clean
k(s2+.3,2, -10,14,22, 0,11,0); k(T['dots']+1.5,2, 0,12,22, 0,11.5,0); k(T['clean'],2, 6,12,21, 0,11.5,0); k(s3-.6,2, 12,16,22, 0,11,0)
# st3: phone → tasbeh, plants
k(s3+.3,3, -16,12,26, -2,7,0); k(T['plant']+.5,3, 8,9,20, 7,4,0); k(T['swap']+1,3, -6,10,22, -3,8,0); k(s4-.6,3, 14,14,24, 4,6,0)
# st4: rug + tasbeh + 1-2-3
k(s4+.3,4, -10,22,26, 0,8,0); k(T['three'],4, 0,16,22, 0,13,0); k(s5-.6,4, 8,20,26, 0,10,0)
# st5: tower
k(s5+.3,5, -12,10,30, 0,10,0); k(T['stack']+2.6,5, 4,20,34, 0,14,0); k(cta,5, 10,34,40, 0,30,0); k(END+5,5, -10,40,46, 0,36,0)
BG=[[-9,'#E9E2D6'],[s1,'#F3E9CF'],[s2,'#E5DDEB'],[s3,'#DAE2E9'],[s4,'#F6E1D3'],[s5,'#DCE6DA'],[cta,'#F1E6D6']]
HEAD2=HEAD.replace('<script src="engine.js"></script>','<script src="engine.js"></script><script>window.CAMK=%s;window.BGK=%s;window.TL=%s;</script><script type="module" src="scene.js"></script>'%(json.dumps(K),json.dumps(BG),json.dumps(T)))
HEAD2=HEAD2.replace('</style>','''#gl{position:absolute;inset:0;width:1080px;height:1920px}
.soft{position:absolute;inset:0;pointer-events:none;background:linear-gradient(180deg,rgba(251,245,230,.0) 60%,rgba(251,245,230,.35) 100%)}
</style>''')
s=T.get('html','')
c=C.cta(tas=T['ctaTas'],zikr=T['ctaZikr'],extra=T.get('ctaExtra',''),havola=T['ctaHav'],btn=T['ctaBtn'])
out=HEAD2+'<canvas id="gl" width="1080" height="1920"></canvas><div class="soft"></div><div class="grain"></div><div class="vign"></div>'+s+c+f'''
<div id="sub" data-hide="{cta-.1}"><div id="subbox"></div></div></div>
<script>(function(){{const R=window.render;window.render=function(t){{if(window.render3d)window.render3d(t);R(t);}};}})();</script>'''+C.TASBEH+'</body></html>'
open('/home/claude/reel26/index.html','w').write(out);print('ok',len(K))
