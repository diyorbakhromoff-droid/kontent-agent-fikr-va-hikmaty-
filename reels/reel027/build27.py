import sys,json; sys.path.insert(0,'/home/claude')
import cta as C
exec(open('/home/claude/build4.py').read().split('# ---------- reel004 ----------')[0].split('import cta as C')[1])
T=json.load(open('/home/claude/reel27/times.json'))
s1,s2,s3,s4,s5,cta,END=T['s1'],T['s2'],T['s3'],T['s4'],T['s5'],T['cta'],T['end']
C.SCENE_S=str(cta)
X=[0,70,140,210,280,350]
def st(i,dx,dy,dz,lx=0,ly=0,lz=0):
    f=1.55
    return [X[i]+lx+(dx-lx)*f,ly+(dy-ly)*1.25,lz+(dz-lz)*f],[X[i]+lx,ly,lz]
K=[]
def k(t,i,*a): p,l=st(i,*a);K.append([round(t,2),p,l])
# hook
k(0,0, 3,12,30, 0,11,0); k(T['pulse'][0],0, 0,11,20, 0,11,0); k(13.0,0, -8,16,30, 0,12,0); k(s1-.8,0, 14,22,36, 0,12,0)
# st1 room: wide establishing then push to phone on cushion
k(s1+.3,1, 14,14,30, -1,5,-4); k(T['phoneDown']-.5,1, 2,8,14, -3,4,-5); k(s2-.6,1, -6,10,18, 0,6,-5)
# st2 blocks
k(s2+.3,2, -12,14,26, 0,7,0); k(T['good']+1.2,2, 6,12,24, 0,8,0); k(T['heart2']+.5,2, 0,16,22, 0,11,0); k(s3-.6,2, 10,16,26, 0,10,0)
# st3 cups + smiles
k(s3+.3,3, -14,10,22, 0,4,0); k(T['smile'],3, 0,12,26, 0,8,0); k(s4-.6,3, 12,16,26, 0,9,0)
# st4 plates
k(s4+.3,4, -12,12,20, 0,3,0); k(T['away']-.6,4, 0,10,18, 0,3,0); k(s5-.35,4, 3,9,16, 0,4,0)
# st5 heart + ring
k(s5+.3,5, -10,12,26, 0,11,0); k(cta,5, 6,14,30, 0,12,0); k(END+5,5, -8,30,40, 0,26,0)
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
open('/home/claude/reel27/index.html','w').write(out);print('ok',len(K))
