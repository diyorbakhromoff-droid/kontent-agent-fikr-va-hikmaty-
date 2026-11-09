import * as THREE from './lib/three.js';
import {RoomEnvironment} from './lib/RoomEnvironment.js';
const W=1080,H=1920;
const cv=document.getElementById('gl');
const R=new THREE.WebGLRenderer({canvas:cv,antialias:true,preserveDrawingBuffer:true});
R.setPixelRatio(1);R.setSize(W,H,false);R.outputColorSpace=THREE.SRGBColorSpace;R.toneMapping=THREE.ACESFilmicToneMapping;R.toneMappingExposure=0.95;
const S=new THREE.Scene();S.background=new THREE.Color('#0b1220');S.fog=new THREE.FogExp2('#0b1220',0.0009);
{const pm=new THREE.PMREMGenerator(R);S.environment=pm.fromScene(new RoomEnvironment(),0.04).texture;S.environmentIntensity=0.1;}
const cam=new THREE.PerspectiveCamera(42,W/H,0.5,4000);
let seed=11;const rnd=()=>{seed=(seed*16807)%2147483647;return (seed-1)/2147483646};
const cl=(x,a=0,b=1)=>Math.max(a,Math.min(b,x)),sm=p=>p*p*(3-2*p),eo=p=>1-Math.pow(1-p,3);
// lights
S.add(new THREE.HemisphereLight('#7f98c8','#1a1410',0.6));
const moon=new THREE.DirectionalLight('#bcd0ff',0.55);moon.position.set(-300,500,-200);S.add(moon);
const warm=new THREE.DirectionalLight('#ffd9a0',0.35);warm.position.set(200,180,400);S.add(warm);
function tex(w,h,draw,rep){const c=document.createElement('canvas');c.width=w;c.height=h;draw(c.getContext('2d'),w,h);const t=new THREE.CanvasTexture(c);t.colorSpace=THREE.SRGBColorSpace;if(rep){t.wrapS=t.wrapT=THREE.RepeatWrapping;t.repeat.set(rep[0],rep[1]);}t.anisotropy=8;return t;}
const M=(o)=>new THREE.MeshStandardMaterial(o);
// ground + stars
const ground=new THREE.Mesh(new THREE.PlaneGeometry(6000,6000),M({color:'#0e1626',roughness:1}));ground.rotation.x=-Math.PI/2;ground.position.y=-0.2;S.add(ground);
{const g=new THREE.BufferGeometry(),p=[];for(let i=0;i<1400;i++){const a=rnd()*6.283,e=0.15+rnd()*1.3,r=2500;p.push(Math.cos(a)*Math.cos(e)*r,Math.sin(e)*r,Math.sin(a)*Math.cos(e)*r);}g.setAttribute('position',new THREE.Float32BufferAttribute(p,3));S.add(new THREE.Points(g,new THREE.PointsMaterial({color:'#dfe8ff',size:2.2,sizeAttenuation:false,fog:false,transparent:true,opacity:.8})));}
// plaza (marble)
const marble=tex(512,512,(c,w,h)=>{c.fillStyle='#e6e2d8';c.fillRect(0,0,w,h);c.strokeStyle='rgba(150,140,120,.45)';c.lineWidth=3;for(let i=0;i<=4;i++){c.beginPath();c.moveTo(i*128,0);c.lineTo(i*128,h);c.stroke();c.beginPath();c.moveTo(0,i*128);c.lineTo(w,i*128);c.stroke();}
 c.strokeStyle='rgba(180,150,90,.35)';c.lineWidth=2;for(let i=0;i<4;i++)for(let j=0;j<4;j++){const x=i*128+64,y=j*128+64;c.beginPath();c.moveTo(x,y-40);c.lineTo(x+40,y);c.lineTo(x,y+40);c.lineTo(x-40,y);c.closePath();c.stroke();}},[60,60]);
const plaza=new THREE.Mesh(new THREE.PlaneGeometry(420,520),M({map:marble,roughness:.55,emissive:'#3a3a44',emissiveIntensity:.3}));plaza.rotation.x=-Math.PI/2;plaza.position.set(0,0,20);S.add(plaza);
// city blocks around
{const g=new THREE.BoxGeometry(1,1,1),wm=tex(64,64,(c)=>{c.fillStyle='#1a2233';c.fillRect(0,0,64,64);for(let y=4;y<64;y+=10)for(let x=4;x<64;x+=10){c.fillStyle=Math.random()<.45?'#ffcf86':'#273149';c.fillRect(x,y,5,6);}}),N=260;
 const im=new THREE.InstancedMesh(g,M({color:'#2a3448',emissive:'#ffffff',emissiveMap:wm,map:wm,emissiveIntensity:.55,roughness:.9}),N);const o=new THREE.Object3D();let k=0;
 while(k<N){const x=(rnd()-.5)*1700,z=(rnd()-.5)*1700;if(Math.abs(x)<260&&z>-300&&z<330)continue;if(x>200&&x<420&&z>40&&z<300)continue;const h=10+rnd()*45;o.position.set(x,h/2,z);o.scale.set(20+rnd()*30,h,20+rnd()*30);o.rotation.y=0;o.updateMatrix();im.setMatrixAt(k++,o.matrix);}S.add(im);}
// ---- mosque ----
const MW=180,MD=300,MH=16,Z0=-140; // x -90..90, z -140..160 (south=+z, qibla)
const wallTex=(n)=>tex(1024,128,(c,w,h)=>{c.fillStyle='#ece4cf';c.fillRect(0,0,w,h);const s=w/n;for(let i=0;i<n;i++){const x=i*s+s*.2,ww=s*.6;c.fillStyle='#ffca78';c.beginPath();c.moveTo(x,h*.86);c.lineTo(x,h*.42);c.arc(x+ww/2,h*.42,ww/2,Math.PI,0);c.lineTo(x+ww,h*.86);c.fill();c.strokeStyle='#b89150';c.lineWidth=3;c.stroke();}c.fillStyle='#c9b48a';c.fillRect(0,0,w,10);c.fillRect(0,h-8,w,8);});
const wallE=tex(1024,128,(c,w,h)=>{c.fillStyle='#000';c.fillRect(0,0,w,h);});
function wall(len,n,x,z,ry){const t=wallTex(n);const m=new THREE.Mesh(new THREE.PlaneGeometry(len,MH),M({map:t,emissive:'#ffffff',emissiveMap:t,emissiveIntensity:.42,roughness:.7,side:THREE.DoubleSide}));m.position.set(x,MH/2,z);m.rotation.y=ry;S.add(m);return m;}
wall(MW,18,0,Z0+MD,0);wall(MW,18,0,Z0,Math.PI);wall(MD,30,-MW/2,Z0+MD/2,-Math.PI/2);wall(MD,30,MW/2,Z0+MD/2,Math.PI/2);
// interior floor: red carpet
const carpet=tex(256,256,(c,w,h)=>{c.fillStyle='#7c1d24';c.fillRect(0,0,w,h);c.strokeStyle='rgba(230,190,120,.35)';c.lineWidth=4;for(let y=0;y<h;y+=64){c.beginPath();c.moveTo(0,y);c.lineTo(w,y);c.stroke();}c.fillStyle='rgba(0,0,0,.15)';for(let x=0;x<w;x+=32)c.fillRect(x,0,2,h);},[30,50]);
const floor=new THREE.Mesh(new THREE.PlaneGeometry(MW-1,MD-1),M({map:carpet,roughness:.95,emissive:'#2a0508',emissiveIntensity:.3}));floor.rotation.x=-Math.PI/2;floor.position.set(0,.15,Z0+MD/2);S.add(floor);
// columns (old part)
{const g=new THREE.CylinderGeometry(.55,.55,MH,10),cap=new THREE.CylinderGeometry(.95,.55,1,10);const n=[];for(let x=-84;x<=84;x+=14)for(let z=48;z<=150;z+=13){if(x>20&&x<60&&z>78&&z<132)continue;if(x>-28&&x<20&&z>96&&z<130)continue;n.push([x,z]);}
 const a=new THREE.InstancedMesh(g,M({color:'#f2ede2',roughness:.5,emissive:'#5a5040',emissiveIntensity:.3}),n.length),b=new THREE.InstancedMesh(cap,M({color:'#d9b36a',metalness:.7,roughness:.35,emissive:'#5a4310',emissiveIntensity:.5}),n.length);const o=new THREE.Object3D();
 n.forEach(([x,z],i)=>{o.position.set(x,MH/2,z);o.updateMatrix();a.setMatrixAt(i,o.matrix);o.position.set(x,MH-1,z);o.updateMatrix();b.setMatrixAt(i,o.matrix);});S.add(a,b);}
// roof (fades for cutaway)
const roofMats=[];
const roofMat=M({color:'#d8d1c0',roughness:.8,emissive:'#2a2620',emissiveIntensity:.4,transparent:true});roofMats.push(roofMat);
const roof=new THREE.Mesh(new THREE.BoxGeometry(MW+2,1.2,MD+2),roofMat);roof.position.set(0,MH+.6,Z0+MD/2);S.add(roof);
const silver=M({color:'#d6dbe2',metalness:.55,roughness:.3,emissive:'#2a3038',emissiveIntensity:.45,transparent:true});roofMats.push(silver);
{const g=new THREE.SphereGeometry(7,24,12,0,Math.PI*2,0,Math.PI/2),dr=new THREE.CylinderGeometry(7.2,7.2,2,24);const pos=[];for(let x=-60;x<=60;x+=30)for(let z=Z0+40;z<=Z0+MD-60;z+=40)pos.push([x,z]);pos.push([4,Z0+MD-18]);
 const im=new THREE.InstancedMesh(g,silver,pos.length),id=new THREE.InstancedMesh(dr,silver,pos.length),o=new THREE.Object3D();pos.forEach(([x,z],i)=>{o.position.set(x,MH+2.2,z);o.updateMatrix();im.setMatrixAt(i,o.matrix);o.position.set(x,MH+1.6,z);o.updateMatrix();id.setMatrixAt(i,o.matrix);});S.add(im,id);}
// minarets
const gold=M({color:'#e6c27a',metalness:.9,roughness:.25,emissive:'#7a5a18',emissiveIntensity:.8});
const mWhite=M({color:'#efe9dc',roughness:.6,emissive:'#4a4436',emissiveIntensity:.45});
const band=M({color:'#ffd78a',emissive:'#ffc060',emissiveIntensity:1.6});
function crescent(sz){const g=new THREE.Group();const c=new THREE.Mesh(new THREE.TorusGeometry(sz,sz*.22,8,24,Math.PI*1.35),gold);c.rotation.z=Math.PI*.82;c.position.y=sz*1.1;g.add(c);const b=new THREE.Mesh(new THREE.SphereGeometry(sz*.35,12,8),gold);g.add(b);const r=new THREE.Mesh(new THREE.CylinderGeometry(sz*.08,sz*.08,sz*.6,6),gold);r.position.y=sz*.4;g.add(r);return g;}
function minaret(x,z,h=104){const g=new THREE.Group();const b=new THREE.Mesh(new THREE.CylinderGeometry(5.5,5.5,h*.32,8),mWhite);b.position.y=h*.16;g.add(b);
 const s=new THREE.Mesh(new THREE.CylinderGeometry(3.6,4.4,h*.5,16),mWhite);s.position.y=h*.32+h*.25;g.add(s);
 [h*.32,h*.6,h*.82].forEach((y,i)=>{const bl=new THREE.Mesh(new THREE.CylinderGeometry(5.6-i*.6,4.6-i*.6,1.6,16),mWhite);bl.position.y=y;g.add(bl);const l=new THREE.Mesh(new THREE.TorusGeometry(5.4-i*.6,.22,6,24),band);l.rotation.x=Math.PI/2;l.position.y=y+.9;g.add(l);});
 const t=new THREE.Mesh(new THREE.CylinderGeometry(2.6,3.2,h*.18,16),mWhite);t.position.y=h*.82+h*.09;g.add(t);
 const cone=new THREE.Mesh(new THREE.ConeGeometry(2.8,8,16),gold);cone.position.y=h+3;g.add(cone);const cr=crescent(1.8);cr.position.y=h+7.5;g.add(cr);g.position.set(x,0,z);S.add(g);return g;}
[[-90,Z0],[90,Z0],[-90,Z0+MD],[90,Z0+MD],[-90,Z0+150],[90,Z0+150],[-30,Z0+MD],[30,Z0+MD+0.1],[-30,Z0],[30,Z0]].forEach(([x,z],i)=>minaret(x,z,i<4?110:96));
// green dome over hujra (x~40,z~105)
const HX=40,HZ=104;
const green=M({color:'#1f7a5a',roughness:.4,metalness:.2,emissive:'#1f7a5a',emissiveIntensity:.55});
const gd=new THREE.Group();{const drum=new THREE.Mesh(new THREE.CylinderGeometry(9,9.6,6,32),M({color:'#1d6b50',emissive:'#0f3d2c',emissiveIntensity:.7}));drum.position.y=MH+3;gd.add(drum);
 const dome=new THREE.Mesh(new THREE.SphereGeometry(9,40,20,0,Math.PI*2,0,Math.PI/2),green);dome.scale.y=1.25;dome.position.y=MH+6;gd.add(dome);
 const sp=new THREE.Mesh(new THREE.CylinderGeometry(.4,.6,4,8),gold);sp.position.y=MH+18.5;gd.add(sp);const cr=crescent(1.6);cr.position.y=MH+20.5;gd.add(cr);
 const base=new THREE.Mesh(new THREE.BoxGeometry(22,2,22),M({color:'#1d6b50',emissive:'#0f3d2c',emissiveIntensity:.6}));base.position.y=MH+1;gd.add(base);}
gd.position.set(HX,0,HZ);S.add(gd);
const halo=new THREE.Mesh(new THREE.TorusGeometry(13,.35,8,64),new THREE.MeshBasicMaterial({color:'#e6c27a',transparent:true,opacity:0,blending:THREE.AdditiveBlending,depthWrite:false}));halo.rotation.x=Math.PI/2;halo.position.set(HX,MH+9,HZ);S.add(halo);
const halo2=halo.clone();halo2.material=halo.material.clone();S.add(halo2);
const gl=new THREE.PointLight('#5dffb8',0,60,1.6);gl.position.set(HX,MH+14,HZ);S.add(gl);
// hujra enclosure with gold grille
const grille=tex(256,256,(c,w,h)=>{c.fillStyle='#14523d';c.fillRect(0,0,w,h);c.strokeStyle='#e6c27a';c.lineWidth=5;for(let i=-w;i<w*2;i+=32){c.beginPath();c.moveTo(i,0);c.lineTo(i+h,h);c.stroke();c.beginPath();c.moveTo(i,h);c.lineTo(i+h,0);c.stroke();}c.lineWidth=10;c.strokeRect(5,5,w-10,h-10);},[3,1]);
const hj=new THREE.Mesh(new THREE.BoxGeometry(22,9,22),M({map:grille,emissive:'#ffffff',emissiveMap:grille,emissiveIntensity:.35,metalness:.4,roughness:.4}));hj.position.set(HX,4.5,HZ);S.add(hj);
// Rawda green carpet
const rwT=tex(256,256,(c,w,h)=>{c.fillStyle='#2a6e4c';c.fillRect(0,0,w,h);c.strokeStyle='rgba(230,194,122,.5)';c.lineWidth=3;for(let y=0;y<h;y+=64){c.beginPath();c.moveTo(0,y);c.lineTo(w,y);c.stroke();}c.fillStyle='rgba(255,255,255,.06)';for(let x=0;x<w;x+=32)for(let y=0;y<h;y+=64){c.beginPath();c.arc(x+16,y+28,10,Math.PI,0);c.fill();}},[6,4]);
const rawM=M({map:rwT,roughness:.9,emissive:'#1f7a5a',emissiveIntensity:.2});
const rawda=new THREE.Mesh(new THREE.PlaneGeometry(46,30),rawM);rawda.rotation.x=-Math.PI/2;rawda.position.set(4,.25,108);S.add(rawda);
// minbar
const minbar=new THREE.Group();{for(let i=0;i<7;i++){const s=new THREE.Mesh(new THREE.BoxGeometry(3,1+i*.9,1.4),mWhite);s.position.set(0,(1+i*.9)/2,-i*1.3);minbar.add(s);}
 const k=new THREE.Mesh(new THREE.BoxGeometry(3.4,3.4,2.6),gold);k.position.set(0,8.6,-9);minbar.add(k);const c=new THREE.Mesh(new THREE.ConeGeometry(2.4,4.5,8),gold);c.position.set(0,12.5,-9);minbar.add(c);
 const rail=new THREE.Mesh(new THREE.BoxGeometry(.3,1.2,10),gold);rail.position.set(1.6,5,-4.5);rail.rotation.x=.55;minbar.add(rail);const r2=rail.clone();r2.position.x=-1.6;minbar.add(r2);}
minbar.position.set(-22,0,124);minbar.rotation.y=Math.PI;S.add(minbar);
// mihrab on qibla wall
const mihT=tex(256,384,(c,w,h)=>{c.fillStyle='#e6c27a';c.fillRect(0,0,w,h);c.fillStyle='#14523d';c.beginPath();c.moveTo(40,h-20);c.lineTo(40,150);c.arc(w/2,150,w/2-40,Math.PI,0);c.lineTo(w-40,h-20);c.fill();c.fillStyle='#e6c27a';c.font='bold 46px serif';c.textAlign='center';c.fillText('۞',w/2,200);});
const mih=new THREE.Mesh(new THREE.PlaneGeometry(8,12),M({map:mihT,emissive:'#ffffff',emissiveMap:mihT,emissiveIntensity:.5}));mih.position.set(-6,6,Z0+MD-.6);mih.rotation.y=Math.PI;S.add(mih);
// suffa platform north of hujra
const suffa=new THREE.Group();{const p=new THREE.Mesh(new THREE.BoxGeometry(20,1.2,9),M({color:'#efe6d2',roughness:.6,emissive:'#4a4436',emissiveIntensity:.4}));p.position.y=.6;suffa.add(p);
 const rl=new THREE.Mesh(new THREE.BoxGeometry(20,.2,.2),gold);rl.position.set(0,2.2,-4.4);suffa.add(rl);for(let i=-9;i<=9;i+=3){const pp=new THREE.Mesh(new THREE.BoxGeometry(.2,1.6,.2),gold);pp.position.set(i,1.6,-4.4);suffa.add(pp);}}
suffa.position.set(HX,0,HZ-22);S.add(suffa);
// Bab al-Salam door (west wall, z=100)
const door=new THREE.Group();{[-5.2,5.2].forEach(zz=>{const pl=new THREE.Mesh(new THREE.BoxGeometry(1.6,10.5,1.2),gold);pl.position.set(0,5.25,zz);door.add(pl);});const ar=new THREE.Mesh(new THREE.TorusGeometry(5.2,.6,8,24,Math.PI),gold);ar.rotation.y=Math.PI/2;ar.position.y=10.5;door.add(ar);const tymp=new THREE.Mesh(new THREE.CircleGeometry(4.6,24,0,Math.PI),M({color:'#14523d',emissive:'#14523d',emissiveIntensity:.6,side:THREE.DoubleSide}));tymp.rotation.y=Math.PI/2;tymp.position.set(-.3,10.5,0);door.add(tymp);
 const wood=M({color:'#4a2c14',roughness:.6,emissive:'#2a1406',emissiveIntensity:.5});
 const lL=new THREE.Group(),lR=new THREE.Group();const lf=new THREE.Mesh(new THREE.BoxGeometry(.5,10,4.4),wood);lf.position.set(0,5,2.2);lL.add(lf);const rf=lf.clone();rf.position.set(0,5,-2.2);lR.add(rf);
 lL.position.set(-1,0,-4.4);lR.position.set(-1,0,4.4);door.add(lL,lR);door.userData={lL,lR};
 const glowD=new THREE.Mesh(new THREE.PlaneGeometry(8.6,10),new THREE.MeshBasicMaterial({color:'#ffd27a',transparent:true,opacity:.0,blending:THREE.AdditiveBlending,depthWrite:false,side:THREE.DoubleSide}));glowD.rotation.y=Math.PI/2;glowD.position.set(-.2,5,0);door.add(glowD);door.userData.glow=glowD;}
door.position.set(-MW/2-.4,0,100);S.add(door);
// umbrellas
const umb=[];{const pole=new THREE.CylinderGeometry(.6,.8,22,10),can=new THREE.ConeGeometry(13,3.2,4,1,true);const fab=M({color:'#fbf8f0',roughness:.6,side:THREE.DoubleSide,emissive:'#8a8270',emissiveIntensity:.3});const pm=M({color:'#d8d2c4',metalness:.4,roughness:.5});
 const pos=[];for(let x=-180;x<=180;x+=26)for(let z=-170;z<=260;z+=26){const inM=Math.abs(x)<MW/2+12&&z>Z0-12&&z<Z0+MD+12;if(inM)continue;if(Math.abs(x)>200)continue;pos.push([x,z]);}
 pos.forEach(([x,z])=>{const p=new THREE.Mesh(pole,pm);p.position.set(x,11,z);S.add(p);const c=new THREE.Mesh(can,fab);c.position.set(x,22,z);c.rotation.y=Math.PI/4;S.add(c);umb.push({c,d:Math.hypot(x+100,z-120)});});}
// Baqi' (east-southeast)
const BX=330,BZ=140;{const bg=new THREE.Mesh(new THREE.PlaneGeometry(200,220),M({color:'#6a5a42',roughness:1,emissive:'#2a2418',emissiveIntensity:.4}));bg.rotation.x=-Math.PI/2;bg.position.set(BX,.3,BZ);S.add(bg);
 const wm=M({color:'#d8ccb0',roughness:.7,emissive:'#4a4232',emissiveIntensity:.5});[[0,-110,200,1],[0,110,200,1],[-100,0,1,220],[100,0,1,220]].forEach(([x,z,w,d])=>{const m=new THREE.Mesh(new THREE.BoxGeometry(w+2,4,d+2),wm);m.position.set(BX+x,2,BZ+z);S.add(m);});
 const N=900,st=new THREE.InstancedMesh(new THREE.BoxGeometry(.45,.6,1.1),M({color:'#bdb6a8',roughness:.8,emissive:'#3a362e',emissiveIntensity:.5}),N),o=new THREE.Object3D();for(let i=0;i<N;i++){o.position.set(BX+(rnd()-.5)*188,.45,BZ+(rnd()-.5)*206);o.rotation.y=(rnd()-.5)*.3;o.updateMatrix();st.setMatrixAt(i,o.matrix);}S.add(st);
 const pth=new THREE.Mesh(new THREE.PlaneGeometry(6,206),M({color:'#c8bca0',emissive:'#4a4232',emissiveIntensity:.5}));pth.rotation.x=-Math.PI/2;pth.position.set(BX,.35,BZ);S.add(pth);
 const lamp=new THREE.PointLight('#ffcf88',1.2,260,1.3);lamp.position.set(BX,40,BZ);S.add(lamp);}
// people (instanced capsules)
const NP=520,people=new THREE.InstancedMesh(new THREE.CapsuleGeometry(.32,1.1,3,6),M({color:'#ffffff',roughness:.6,emissive:'#9aa0aa',emissiveIntensity:.5}),NP);const PP=[];
for(let i=0;i<NP;i++){let x,z;do{x=(rnd()-.5)*400;z=-200+rnd()*470;}while(Math.abs(x)<MW/2+4&&z>Z0-4&&z<Z0+MD+4);PP.push({x,z,a:rnd()*6.28,v:.6+rnd()*1.2});}
S.add(people);
// pilgrimage path dots: entrance -> rawda -> muwajaha -> exit (Bab al-Baqi)
const PATH=[[-96,100],[-86,100],[-40,104],[-4,110],[20,118],[40,119],[60,118],[78,112],[96,112],[130,118],[200,130],[250,140]];
const pts=[];{for(let i=0;i<PATH.length-1;i++){const [x1,z1]=PATH[i],[x2,z2]=PATH[i+1];const L=Math.hypot(x2-x1,z2-z1),n=Math.max(1,Math.round(L/2.6));for(let k=0;k<n;k++)pts.push([x1+(x2-x1)*k/n,z1+(z2-z1)*k/n]);}}
const dots=new THREE.InstancedMesh(new THREE.CylinderGeometry(.55,.55,.12,12),new THREE.MeshBasicMaterial({color:'#ffd77a'}),pts.length);{const o=new THREE.Object3D();pts.forEach(([x,z],i)=>{o.position.set(x,.45,z);o.scale.set(0,0,0);o.updateMatrix();dots.setMatrixAt(i,o.matrix);});}S.add(dots);
// interior warm lights
const il=new THREE.PointLight('#ffcf88',0,140,1.2);il.position.set(10,12,104);S.add(il);
// ---- camera path ----
const K=window.CAMK; // [[t,[px,py,pz],[tx,ty,tz]],...]
const vp=K.map(k=>new THREE.Vector3(...k[1])),vt=K.map(k=>new THREE.Vector3(...k[2]));
const cp=new THREE.CatmullRomCurve3(vp,false,'centripetal'),ct=new THREE.CatmullRomCurve3(vt,false,'centripetal');
function uAt(t){const n=K.length;if(t<=K[0][0])return 0;if(t>=K[n-1][0])return 1;let i=0;while(t>K[i+1][0])i++;const p=(t-K[i][0])/(K[i+1][0]-K[i][0]);const e=.45*p+.55*sm(p);return (i+e)/(n-1);}
const proj=new THREE.Vector3();
window.project=(x,y,z)=>{proj.set(x,y,z).project(cam);return [(proj.x+1)/2*W,(1-proj.y)/2*H,proj.z];};
window.ANCH={bab:[-92,9,100],rawda:[4,1,108],minbar:[-22,13,115],muwajaha:[40,6,116],dome:[HX,MH+16,HZ],suffa:[HX,2,HZ-22],umb:[-100,24,180],baqi:[BX,4,BZ]};
const T=window.TL;
window.render3d=function(t){
 const u=uAt(t);cam.position.copy(cp.getPoint(u));cam.lookAt(ct.getPoint(u));
 // cutaway roof
 const cut=cl((t-T.cutIn)/1.5)*(1-cl((t-T.cutOut)/1.5));roofMats.forEach(m=>{m.opacity=1-.93*cut;m.depthWrite=cut<.5;});
 il.intensity=3.5*cut;rawM.emissiveIntensity=.2+.55*cl((t-T.rawda)/1)*(1-cl((t-T.cutOut)/1.5));
 // door
 const dk=eo(cl((t-T.door)/1.6));door.userData.lL.rotation.y=-dk*1.4;door.userData.lR.rotation.y=dk*1.4;door.userData.glow.material.opacity=dk*.75*(1-cl((t-T.door-4)/1));
 // dome halo
 const hk=cl((t-T.dome)/1)*(1-cl((t-T.dome-7)/1));const ph=((t-T.dome)*.6)%1;halo.material.opacity=hk*(1-ph)*.9;halo.scale.setScalar(1+ph*.9);
 const ph2=(ph+.5)%1;halo2.material.opacity=hk*(1-ph2)*.9;halo2.scale.setScalar(1+ph2*.9);gl.intensity=6*hk+1;green.emissiveIntensity=.55+.5*hk;
 // umbrellas opening
 umb.forEach(o=>{const k=eo(cl((t-T.umb-o.d*.012)/1.6));const a=.12+.88*k;o.c.scale.set(a,1.9-.9*k,a);o.c.position.y=22-(1-k)*4.5;});
 // path dots
 const show=Math.floor(pts.length*cl((t-T.path0)/(T.path1-T.path0)));const o=new THREE.Object3D();
 for(let i=0;i<pts.length;i++){const s=i<show?1+.25*Math.sin(t*4-i*.4):0;o.position.set(pts[i][0],.45,pts[i][1]);o.scale.set(s,1,s);o.updateMatrix();dots.setMatrixAt(i,o.matrix);}dots.instanceMatrix.needsUpdate=true;
 // people
 for(let i=0;i<NP;i++){const p=PP[i];const x=p.x+Math.cos(p.a)*t*p.v,z=p.z+Math.sin(p.a)*t*p.v;o.position.set(x,.9,z);o.scale.set(1,1,1);o.updateMatrix();people.setMatrixAt(i,o.matrix);}people.instanceMatrix.needsUpdate=true;
 R.render(S,cam);
};
window.ready3d=true;
