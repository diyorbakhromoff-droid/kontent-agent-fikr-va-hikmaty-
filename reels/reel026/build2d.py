import sys,json,os,shutil
sys.path.insert(0,'/home/claude')
import cta as C
exec(open('/home/claude/build4.py').read().split('# ---------- reel004 ----------')[0].split('import cta as C')[1])

def build(src,dst,doodles,fixes=()):
    T=json.load(open(f'/home/claude/{src}/times.json'))
    os.makedirs(dst,exist_ok=True)
    for f in ['style.css','engine.js','words.js','words.json']: shutil.copy(f'/home/claude/{src}/{f}',f'{dst}/{f}')
    for d in ['fonts','audio']:
        if not os.path.exists(f'{dst}/{d}'): shutil.copytree(f'/home/claude/{src}/{d}',f'{dst}/{d}')
    for f in ['render.js','snap.js']: shutil.copy(f'/home/claude/reel9/{f}',f'{dst}/{f}')
    os.makedirs(f'{dst}/snaps',exist_ok=True)
    s1,s2,s3,s4,s5,cta=T['s1'],T['s2'],T['s3'],T['s4'],T['s5'],T['cta']
    C.SCENE_S=str(cta)
    b=bgs([(-1,s1,'#E9E2D6'),(s1,s2,'#F3E9CF'),(s2,s3,'#E5DDEB'),(s3,s4,'#DAE2E9'),(s4,s5,'#F6E1D3'),(s5,cta,'#DCE6DA'),(cta,999,'#F1E6D6')])
    html=T['html']
    for a,bb in fixes: html=html.replace(a,bb)
    parts=html.split('</section>')
    out=''
    for i,p in enumerate(parts[:-1]): out+=p+''.join(doodles.get(i,[]))+'</section>'
    out+=parts[-1]
    head=HEAD.replace('</style>','svg .a{transform-box:fill-box;transform-origin:center}</style>')
    c=C.cta(tas=T['ctaTas'],zikr=T['ctaZikr'],extra=T.get('ctaExtra',''),havola=T['ctaHav'],btn=T['ctaBtn'])
    page=head+b+out+c+f'''
<div id="sub" data-hide="{cta-.1}"><div id="subbox"></div></div></div>'''+C.TASBEH+'</body></html>'
    open(f'{dst}/index.html','w').write(page)
    return T
