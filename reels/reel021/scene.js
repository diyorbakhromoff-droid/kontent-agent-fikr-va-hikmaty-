import * as THREE from './lib/three.js';
import {RoomEnvironment} from './lib/RoomEnvironment.js';
const W=1080,H=1920;
const cv=document.getElementById('gl');
const R=new THREE.WebGLRenderer({canvas:cv,antialias:true,preserveDrawingBuffer:true});
R.setPixelRatio(1);R.setSize(W,H,false);R.outputColorSpace=THREE.SRGBColorSpace;R.toneMapping=THREE.ACESFilmicToneMapping;R.toneMappingExposure=0.95;
const SKY='#0c1424';
const S=new THREE.Scene();S.background=new THREE.Color(SKY);S.fog=new THREE.FogExp2(SKY,0.0008);
{const pm=new THREE.PMREMGenerator(R);S.environment=pm.fromScene(new RoomEnvironment(),0.04).texture;S.environmentIntensity=0.12;}
const cam=new THREE.PerspectiveCamera(42,W/H,0.5,5000);
let seed=21;const rnd=()=>{seed=(seed*16807)%2147483647;return (seed-1)/2147483646};
const cl=(x,a=0,b=1)=>Math.max(a,Math.min(b,x)),sm=p=>p*p*(3-2*p),eo=p=>1-Math.pow(1-p,3);
S.add(new THREE.HemisphereLight('#8aa0cc','#1e1810',0.65));
const moon=new THREE.DirectionalLight('#c4d4ff',0.55);moon.position.set(-300,500,-250);S.add(moon);
const warm=new THREE.DirectionalLight('#ffd9a0',0.4);warm.position.set(250,200,400);S.add(warm);
function tex(w,h,draw,rep){const c=document.createElement('canvas');c.width=w;c.height=h;draw(c.getContext('2d'),w,h);const t=new THREE.CanvasTexture(c);t.colorSpace=THREE.SRGBColorSpace;if(rep){t.wrapS=t.wrapT=THREE.RepeatWrapping;t.repeat.set(rep[0],rep[1]);}t.anisotropy=8;return t;}
const M=(o)=>new THREE.MeshStandardMaterial(o);
const gold=M({color:'#f0c860',metalness:.85,roughness:.25,emissive:'#9a6c14',emissiveIntensity:1.0});
const stone=M({color:'#d9cbaa',roughness:.85,emissive:'#3e3626',emissiveIntensity:.45});
const stoneD=M({color:'#bfae8a',roughness:.9,emissive:'#352d1f',emissiveIntensity:.45});
// ground, hills, stars
const ground=new THREE.Mesh(new THREE.PlaneGeometry(8000,8000),M({color:'#141a24',roughness:1}));ground.rotation.x=-Math.PI/2;ground.position.y=-14;S.add(ground);
{const g=new THREE.BufferGeometry(),p=[];for(let i=0;i<1600;i++){const a=rnd()*6.283,e=0.12+rnd()*1.35,r=3000;p.push(Math.cos(a)*Math.cos(e)*r,Math.sin(e)*r,Math.sin(a)*Math.cos(e)*r);}g.setAttribute('position',new THREE.Float32BufferAttribute(p,3));S.add(new THREE.Points(g,new THREE.PointsMaterial({color:'#e2eaff',size:2.2,sizeAttenuation:false,fog:false,transparent:true,opacity:.8})));}
// Mount of Olives (east) + city
{const hill=new THREE.Mesh(new THREE.SphereGeometry(900,40,20,0,Math.PI*2,0,Math.PI/2),M({color:'#20242a',roughness:1,emissive:'#0c0e12',emissiveIntensity:.5}));hill.scale.set(.6,.12,1.4);hill.position.set(900,-14,0);S.add(hill);}
{const g=new THREE.BoxGeometry(1,1,1),wm=tex(64,64,(c)=>{c.fillStyle='#2a2a2c';c.fillRect(0,0,64,64);for(let y=6;y<64;y+=14)for(let x=6;x<64;x+=14){c.fillStyle=Math.random()<.4?'#ffcf86':'#38363a';c.fillRect(x,y,5,6);}}),N=520;
 const im=new THREE.InstancedMesh(g,M({color:'#b9ab90',emissive:'#ffffff',emissiveMap:wm,map:wm,emissiveIntensity:.5,roughness:.9}),N);const o=new THREE.Object3D();let k=0;
 while(k<N){const x=-900+rnd()*1500,z=-900+rnd()*1800;if(x>-200&&x<200&&z>-290&&z<290)continue;if(x>220)continue;const h=6+rnd()*16;o.position.set(x,h/2-14+ (x<-200?0:0),z);o.scale.set(14+rnd()*20,h+14,14+rnd()*20);o.updateMatrix();im.setMatrixAt(k++,o.matrix);}S.add(im);}
// ---- compound ----
const X0=-150,X1=150,Z0=-245,Z1=245;
const pave=tex(512,512,(c,w,h)=>{c.fillStyle='#cbbd9c';c.fillRect(0,0,w,h);for(let i=0;i<400;i++){c.fillStyle=`rgba(${120+Math.random()*60|0},${110+Math.random()*50|0},${80+Math.random()*40|0},.25)`;c.fillRect(Math.random()*w,Math.random()*h,30+Math.random()*60,20+Math.random()*40);}c.strokeStyle='rgba(90,80,60,.35)';c.lineWidth=2;for(let i=0;i<=8;i++){c.beginPath();c.moveTo(i*64,0);c.lineTo(i*64,h);c.stroke();c.beginPath();c.moveTo(0,i*64);c.lineTo(w,i*64);c.stroke();}},[12,20]);
const paveM=M({map:pave,roughness:.8,emissive:'#3a3428',emissiveIntensity:.45});
// main courtyard (minus marwani patch SE)
const MX0=60,MX1=X1,MZ0=150,MZ1=Z1; // marwani region
{const sh=new THREE.Shape([new THREE.Vector2(X0,-Z0),new THREE.Vector2(X0,-Z1),new THREE.Vector2(MX0,-Z1),new THREE.Vector2(MX0,-MZ0),new THREE.Vector2(X1,-MZ0),new THREE.Vector2(X1,-Z0)]);
 const g=new THREE.ShapeGeometry(sh);const uv=g.attributes.uv;for(let i=0;i<uv.count;i++){uv.setXY(i,(uv.getX(i)-X0)/300,(uv.getY(i)+Z1)/490);}g.rotateX(-Math.PI/2);
 const m=new THREE.Mesh(g,paveM);m.position.y=0;S.add(m);}
const patchM=M({map:pave,roughness:.8,emissive:'#3a3428',emissiveIntensity:.45,transparent:true,side:THREE.DoubleSide});
const patch=new THREE.Mesh(new THREE.PlaneGeometry(MX1-MX0,MZ1-MZ0),patchM);patch.rotation.x=-Math.PI/2;patch.position.set((MX0+MX1)/2,0.02,(MZ0+MZ1)/2);S.add(patch);
// below-ground box sides (visible at edges) dark
{const bm=M({color:'#3a3226',roughness:1,emissive:'#1a160f',emissiveIntensity:.4});[[X1-X0,1,0,Z0],[X1-X0,1,0,Z1],[1,Z1-Z0,X0,0],[1,Z1-Z0,X1,0]].forEach(([w,d,x,z])=>{const m=new THREE.Mesh(new THREE.BoxGeometry(w,14,d),bm);m.position.set(x,-7.05,z);S.add(m);});const bot=new THREE.Mesh(new THREE.PlaneGeometry(X1-X0,Z1-Z0),bm);bot.rotation.x=-Math.PI/2;bot.position.y=-13.9;S.add(bot);}
// Marwani hall (underground, beneath patch)
const marw=new THREE.Group();{const fl=new THREE.Mesh(new THREE.PlaneGeometry(MX1-MX0-4,MZ1-MZ0-4),M({color:'#8a1f28',roughness:.95,emissive:'#3a0a0e',emissiveIntensity:.6}));fl.rotation.x=-Math.PI/2;fl.position.set((MX0+MX1)/2,-11.9,(MZ0+MZ1)/2);marw.add(fl);
 const pier=new THREE.BoxGeometry(2.2,6,2.2),arch=new THREE.TorusGeometry(3.6,.8,6,16,Math.PI);const pm=M({color:'#e2d4b0',roughness:.8,emissive:'#6a5838',emissiveIntensity:.6});
 for(let x=MX0+8;x<MX1-4;x+=10)for(let z=MZ0+8;z<MZ1-4;z+=13){const p=new THREE.Mesh(pier,pm);p.position.set(x,-9,z);marw.add(p);if(z+13<MZ1-4){const a=new THREE.Mesh(arch,pm);a.rotation.y=Math.PI/2;a.position.set(x,-6,z+6.5);a.scale.set(1,.85,1.6);marw.add(a);}}
 const lamp=new THREE.PointLight('#ffcf88',0,160,1.2);lamp.position.set((MX0+MX1)/2,-5,(MZ0+MZ1)/2);marw.add(lamp);marw.userData.lamp=lamp;}
S.add(marw);
// outer walls (crenellated)
const wallT=tex(1024,128,(c,w,h)=>{c.fillStyle='#cdbb94';c.fillRect(0,0,w,h);for(let y=0;y<h;y+=16)for(let x=(y/16%2)*20;x<w;x+=40){c.strokeStyle='rgba(90,75,50,.35)';c.strokeRect(x,y,40,16);}for(let x=0;x<w;x+=32){c.clearRect(x,0,14,14);}},[1,1]);
function wall(len,x,z,ry,hgt=16){const t=wallT.clone();t.needsUpdate=true;t.wrapS=THREE.RepeatWrapping;t.repeat.set(len/120,1);const m=new THREE.Mesh(new THREE.BoxGeometry(len,hgt,3),M({map:t,roughness:.9,emissive:'#3a3020',emissiveIntensity:.5,alphaTest:.5}));m.position.set(x,hgt/2-3,z);m.rotation.y=ry;S.add(m);return m;}
wall(300,0,Z0,0,14);wall(300,0,Z1,0,20);wall(490,X0,0,Math.PI/2,14);wall(490,X1,0,Math.PI/2,22);
// riwaq porticoes along W and N (inside)
{const arT=tex(512,128,(c,w,h)=>{c.fillStyle='#d8c8a2';c.fillRect(0,0,w,h);const n=8,s=w/n;for(let i=0;i<n;i++){const x=i*s+s*.15,ww=s*.7;c.fillStyle='#ffd590';c.beginPath();c.moveTo(x,h);c.lineTo(x,h*.45);c.arc(x+ww/2,h*.45,ww/2,Math.PI,0);c.lineTo(x+ww,h);c.fill();}});
 const mk=(len,x,z,ry)=>{const t=arT.clone();t.needsUpdate=true;t.wrapS=THREE.RepeatWrapping;t.repeat.set(len/60,1);const m=new THREE.Mesh(new THREE.PlaneGeometry(len,8),M({map:t,emissive:'#ffffff',emissiveMap:t,emissiveIntensity:.35,roughness:.8,side:THREE.DoubleSide}));m.position.set(x,4,z);m.rotation.y=ry;S.add(m);};
 mk(260,-10,Z0+6,0);mk(420,X0+6,-20,Math.PI/2);}
// olive & cypress trees
{const N=240,tg=new THREE.SphereGeometry(3.2,8,6),im=new THREE.InstancedMesh(tg,M({color:'#3e5a34',roughness:1,emissive:'#14200f',emissiveIntensity:.6}),N),o=new THREE.Object3D();let k=0;
 while(k<N){const x=X0+10+rnd()*280,z=Z0+12+rnd()*470;if(x>-95&&x<65&&z>-115&&z<55)continue;if(x>-50&&x<25&&z>150)continue;if(x>MX0&&z>MZ0)continue;o.position.set(x,3,z);const s=.7+rnd()*.7;o.scale.set(s,s*(rnd()<.2?2.4:1),s);o.updateMatrix();im.setMatrixAt(k++,o.matrix);}S.add(im);}
// ---- raised platform with qanatir (arcades) ----
const PX=-15,PZ=-30,PW=150,PD=160,PH=4;
const plat=new THREE.Mesh(new THREE.BoxGeometry(PW,PH,PD),M({map:pave,color:'#fff6e6',roughness:.7,emissive:'#5a5040',emissiveIntensity:.55}));plat.position.set(PX,PH/2,PZ);S.add(plat);
function qanatir(x,z,ry){const g=new THREE.Group();for(let i=-1;i<=1;i++){const c=new THREE.Mesh(new THREE.CylinderGeometry(.5,.5,6,10),stone);c.position.set(i*4,PH+3,0);g.add(c);}for(let i=-1;i<1;i++){const a=new THREE.Mesh(new THREE.TorusGeometry(2,.45,6,14,Math.PI),stone);a.position.set(i*4+2,PH+6,0);g.add(a);}g.position.set(x,0,z);g.rotation.y=ry;S.add(g);}
qanatir(PX,PZ+PD/2-2,0);qanatir(PX,PZ-PD/2+2,0);qanatir(PX-PW/2+2,PZ,Math.PI/2);qanatir(PX+PW/2-2,PZ,Math.PI/2);qanatir(PX-40,PZ+PD/2-2,0);qanatir(PX+40,PZ-PD/2+2,0);
// ---- Dome of the Rock ----
const DX=PX,DZ=PZ,DR=27,DWH=11;
const tileT=tex(1024,256,(c,w,h)=>{c.fillStyle='#e9e2d0';c.fillRect(0,0,w,h*.42);const gr=c.createLinearGradient(0,h*.42,0,h);gr.addColorStop(0,'#1f5f9a');gr.addColorStop(1,'#163f6e');c.fillStyle=gr;c.fillRect(0,h*.42,w,h*.58);
 c.fillStyle='#2d86b8';for(let x=0;x<w;x+=16)for(let y=h*.46;y<h;y+=16){if((x/16+y/16)%2<1)c.fillRect(x+2,y+2,12,12);}
 const n=7,s=w/n;for(let i=0;i<n;i++){const x=i*s+s*.3,ww=s*.4;c.fillStyle='#0c1c30';c.beginPath();c.moveTo(x,h*.86);c.lineTo(x,h*.6);c.arc(x+ww/2,h*.6,ww/2,Math.PI,0);c.lineTo(x+ww,h*.86);c.fill();c.strokeStyle='#e8c070';c.lineWidth=3;c.stroke();c.fillStyle='rgba(255,210,140,.75)';c.fill();}
 c.fillStyle='#e8c070';c.fillRect(0,h*.42-6,w,6);c.fillRect(0,h*.9,w,4);c.fillStyle='#0c1c30';c.fillRect(0,h*.92,w,h*.08);c.fillStyle='#e8c070';c.font='bold 22px serif';for(let x=10;x<w;x+=60)c.fillText('۞',x,h-4);});
const domMats=[];
const domeG=new THREE.Group();
{const wallM=M({map:tileT,roughness:.55,emissive:'#ffffff',emissiveMap:tileT,emissiveIntensity:.35,transparent:true,side:THREE.DoubleSide});domMats.push(wallM);
 const oct=new THREE.Mesh(new THREE.CylinderGeometry(DR,DR,DWH,8,1,true),wallM);oct.rotation.y=Math.PI/8;oct.position.y=PH+DWH/2;domeG.add(oct);
 const roofM=M({color:'#c9c4b8',roughness:.7,emissive:'#2c2a26',emissiveIntensity:.4,transparent:true});domMats.push(roofM);
 const roofR=new THREE.Mesh(new THREE.CylinderGeometry(12,DR,3,8,1),roofM);roofR.rotation.y=Math.PI/8;roofR.position.y=PH+DWH+1.5;domeG.add(roofR);
 const drumT=tex(512,128,(c,w,h)=>{c.fillStyle='#1d5c96';c.fillRect(0,0,w,h);const n=8,s=w/n;for(let i=0;i<n;i++){const x=i*s+s*.32,ww=s*.36;c.fillStyle='#ffd590';c.beginPath();c.moveTo(x,h*.85);c.lineTo(x,h*.45);c.arc(x+ww/2,h*.45,ww/2,Math.PI,0);c.lineTo(x+ww,h*.85);c.fill();}c.fillStyle='#e8c070';c.fillRect(0,0,w,6);c.fillRect(0,h-6,w,6);});
 const drumM=M({map:drumT,emissive:'#ffffff',emissiveMap:drumT,emissiveIntensity:.4,roughness:.5,transparent:true});domMats.push(drumM);
 const drum=new THREE.Mesh(new THREE.CylinderGeometry(11.5,11.5,8,32,1,true),drumM);drum.position.y=PH+DWH+3+4;domeG.add(drum);
 const gM=gold.clone();gM.transparent=true;domMats.push(gM);
 const dome=new THREE.Mesh(new THREE.SphereGeometry(11.6,48,24,0,Math.PI*2,0,Math.PI/2),gM);dome.scale.y=1.18;dome.position.y=PH+DWH+11;domeG.add(dome);
 const fin=new THREE.Mesh(new THREE.CylinderGeometry(.3,.5,4,8),gM);fin.position.y=PH+DWH+11+14.5;domeG.add(fin);
 const cr=new THREE.Mesh(new THREE.TorusGeometry(1.2,.25,8,20,Math.PI*1.4),gM);cr.rotation.z=Math.PI*.8;cr.position.y=PH+DWH+11+17.6;domeG.add(cr);
 // the Rock inside
 const rg=new THREE.IcosahedronGeometry(9,3);const p=rg.attributes.position;for(let i=0;i<p.count;i++){const v=new THREE.Vector3().fromBufferAttribute(p,i);const n=1+.18*Math.sin(v.x*.9)*Math.cos(v.z*.7)+.1*Math.sin(v.y*2.1);v.multiplyScalar(n);p.setXYZ(i,v.x,v.y,v.z);}rg.computeVertexNormals();
 const rock=new THREE.Mesh(rg,M({color:'#9a8466',roughness:.95,emissive:'#4a3a24',emissiveIntensity:.5,flatShading:true}));rock.scale.set(1.4,.42,1.1);rock.position.y=PH+1.5;domeG.add(rock);domeG.userData.rock=rock;
 const rl=new THREE.PointLight('#ffd590',0,70,1.4);rl.position.y=PH+12;domeG.add(rl);domeG.userData.rl=rl;
 // inner colonnade ring
 for(let i=0;i<16;i++){const a=i/16*Math.PI*2;const c=new THREE.Mesh(new THREE.CylinderGeometry(.5,.5,DWH,8),stone);c.position.set(Math.cos(a)*15,PH+DWH/2,Math.sin(a)*15);domeG.add(c);}
}
domeG.position.set(DX,0,DZ);domeG.scale.set(1.15,1.15,1.15);S.add(domeG);
// ---- Dome of the Chain ----
const CX=DX+44,CZ=DZ-2;const chain=new THREE.Group();
{const cm=M({color:'#e6dcc4',roughness:.6,emissive:'#4a4234',emissiveIntensity:.5});for(let i=0;i<11;i++){const a=i/11*Math.PI*2;const c=new THREE.Mesh(new THREE.CylinderGeometry(.35,.35,5,8),cm);c.position.set(Math.cos(a)*6,PH+2.5,Math.sin(a)*6);chain.add(c);}
 const roof=new THREE.Mesh(new THREE.CylinderGeometry(4.2,6.8,1.6,6),M({color:'#3d6e8c',emissive:'#14303e',emissiveIntensity:.6,roughness:.5}));roof.position.y=PH+5.8;chain.add(roof);
 const d=new THREE.Mesh(new THREE.SphereGeometry(3.6,24,12,0,Math.PI*2,0,Math.PI/2),M({color:'#7f8a92',metalness:.6,roughness:.35,emissive:'#2a3038',emissiveIntensity:.5}));d.position.y=PH+6.6;chain.add(d);
 const f=new THREE.Mesh(new THREE.CylinderGeometry(.15,.25,2,6),gold);f.position.y=PH+11;chain.add(f);}
chain.position.set(CX,0,CZ);S.add(chain);
// ---- Qibli mosque ----
const QX0=-42,QX1=14,QZ0=160,QZ1=242,QH=13;const qib=new THREE.Group();
{const fT=tex(512,256,(c,w,h)=>{c.fillStyle='#d6c7a2';c.fillRect(0,0,w,h);const n=7,s=w/n;for(let i=0;i<n;i++){const x=i*s+s*.12,ww=s*.76;c.fillStyle='#2a2216';c.beginPath();c.moveTo(x,h);c.lineTo(x,h*.45);c.arc(x+ww/2,h*.45,ww/2,Math.PI,0);c.lineTo(x+ww,h);c.fill();c.fillStyle='rgba(255,200,120,.85)';c.beginPath();c.moveTo(x+8,h);c.lineTo(x+8,h*.5);c.arc(x+ww/2,h*.5,ww/2-8,Math.PI,0);c.lineTo(x+ww-8,h);c.fill();}c.fillStyle='#b09a70';c.fillRect(0,0,w,12);});
 const sT=tex(512,128,(c,w,h)=>{c.fillStyle='#cdbd96';c.fillRect(0,0,w,h);for(let i=0;i<14;i++){const x=i*w/14+10;c.fillStyle='#ffcf86';c.beginPath();c.moveTo(x,h*.8);c.lineTo(x,h*.45);c.arc(x+8,h*.45,8,Math.PI,0);c.lineTo(x+16,h*.8);c.fill();}});
 const sM=M({map:sT,emissive:'#ffffff',emissiveMap:sT,emissiveIntensity:.35,roughness:.8});
 const body=new THREE.Mesh(new THREE.BoxGeometry(QX1-QX0,QH,QZ1-QZ0),[sM,sM,M({color:'#9c9890',roughness:.6}),stone,stone,sM]);body.position.set((QX0+QX1)/2,QH/2,(QZ0+QZ1)/2);qib.add(body);
 const fac=new THREE.Mesh(new THREE.PlaneGeometry(QX1-QX0,QH),M({map:fT,emissive:'#ffffff',emissiveMap:fT,emissiveIntensity:.45,roughness:.8}));fac.position.set((QX0+QX1)/2,QH/2,QZ0-.6);fac.rotation.y=Math.PI;qib.add(fac);
 const leadM=M({color:'#8d939a',metalness:.55,roughness:.4,emissive:'#22262a',emissiveIntensity:.5});
 const roof=new THREE.Mesh(new THREE.CylinderGeometry(1,1,1,3,1),leadM);roof.scale.set((QX1-QX0)/2*1.1,QZ1-QZ0,7);roof.rotation.set(Math.PI/2,0,Math.PI/2*0);
 const pr=new THREE.BufferGeometry();{const w2=(QX1-QX0)/2,L=QZ1-QZ0-14,y0=QH,y1=QH+6;const v=[-w2,y0,0, w2,y0,0, 0,y1,0, -w2,y0,L, w2,y0,L, 0,y1,L];pr.setAttribute('position',new THREE.Float32BufferAttribute(v,3));pr.setIndex([0,2,1,3,4,5,0,3,5,0,5,2,1,2,5,1,5,4]);pr.computeVertexNormals();}
 const pm=new THREE.Mesh(pr,new THREE.MeshStandardMaterial({color:'#6f757c',metalness:.4,roughness:.6,emissive:'#15181b',emissiveIntensity:.4,side:THREE.DoubleSide}));pm.position.set((QX0+QX1)/2,0,QZ0);qib.add(pm);
 const drum=new THREE.Mesh(new THREE.CylinderGeometry(8.5,8.5,4,32),M({color:'#cdbd96',emissive:'#4a4232',emissiveIntensity:.5}));drum.position.set((QX0+QX1)/2,QH+2,QZ1-10);qib.add(drum);
 const dome=new THREE.Mesh(new THREE.SphereGeometry(8.6,40,20,0,Math.PI*2,0,Math.PI/2),leadM);dome.scale.y=1.05;dome.position.set((QX0+QX1)/2,QH+4,QZ1-10);qib.add(dome);qib.userData.dome=dome;
 const f=new THREE.Mesh(new THREE.CylinderGeometry(.2,.35,3,6),gold);f.position.set((QX0+QX1)/2,QH+14,QZ1-10);qib.add(f);}
S.add(qib);
// ---- minarets (square) ----
const mWhite=M({color:'#e0d4b6',roughness:.7,emissive:'#4a4232',emissiveIntensity:.5});
const band=M({color:'#ffd78a',emissive:'#ffc060',emissiveIntensity:1.5});
const minarets=[];
function minaret(x,z,h=38){const g=new THREE.Group();const b=new THREE.Mesh(new THREE.BoxGeometry(6,h,6),mWhite);b.position.y=h/2;g.add(b);
 const bal=new THREE.Mesh(new THREE.BoxGeometry(8,1.2,8),mWhite);bal.position.y=h*.72;g.add(bal);const l=new THREE.Mesh(new THREE.BoxGeometry(8.2,.4,8.2),band);l.position.y=h*.72+.8;g.add(l);
 const top=new THREE.Mesh(new THREE.CylinderGeometry(2.4,2.4,5,12),mWhite);top.position.y=h+2.5;g.add(top);const d=new THREE.Mesh(new THREE.SphereGeometry(2.5,16,8,0,Math.PI*2,0,Math.PI/2),M({color:'#7f8a92',metalness:.6,roughness:.35,emissive:'#2a3038',emissiveIntensity:.5}));d.position.y=h+5;g.add(d);
 const f=new THREE.Mesh(new THREE.CylinderGeometry(.12,.2,2.4,6),gold);f.position.y=h+8.5;g.add(f);
 const halo=new THREE.Mesh(new THREE.TorusGeometry(6,.3,6,40),new THREE.MeshBasicMaterial({color:'#e8c070',transparent:true,opacity:0,blending:THREE.AdditiveBlending,depthWrite:false}));halo.rotation.x=Math.PI/2;halo.position.y=h*.72+1;g.add(halo);g.userData.halo=halo;
 g.position.set(x,0,z);S.add(g);minarets.push(g);return g;}
minaret(X0+4,Z0+4,40);minaret(X0+4,10,36);minaret(X0+12,Z1-4,34);minaret(60,Z0+4,36);
// ---- gates (11 open) + Bab ar-Rahma ----
const gates=[];const gateM=new THREE.MeshBasicMaterial({color:'#ffd27a',transparent:true,opacity:.0,blending:THREE.AdditiveBlending,depthWrite:false,side:THREE.DoubleSide});
[[X0,-215],[X0,-170],[X0,-120],[X0,-60],[X0,-15],[X0,40],[X0,100],[X0,150],[-90,Z0],[-20,Z0],[110,Z0]].forEach(([x,z])=>{const gm=new THREE.Mesh(new THREE.PlaneGeometry(5,8),gateM.clone());gm.position.set(x+(x===X0?1.8:0),4,z+(z===Z0?1.8:0));if(x===X0)gm.rotation.y=Math.PI/2;S.add(gm);
 const ar=new THREE.Mesh(new THREE.TorusGeometry(2.6,.35,6,14,Math.PI),gold);ar.position.copy(gm.position);ar.position.y=8;ar.rotation.y=gm.rotation.y;S.add(ar);gates.push(gm);});
const rahma=new THREE.Group();{const b=new THREE.Mesh(new THREE.BoxGeometry(10,15,22),stoneD);b.position.y=7.5-3;rahma.add(b);
 [-5.5,5.5].forEach(zz=>{const d=new THREE.Mesh(new THREE.SphereGeometry(3.6,20,10,0,Math.PI*2,0,Math.PI/2),M({color:'#9a9a96',roughness:.6,emissive:'#2a2a28',emissiveIntensity:.5}));d.position.set(0,12,zz);rahma.add(d);
  const a=new THREE.Mesh(new THREE.TorusGeometry(3.6,.6,6,16,Math.PI),stone);a.rotation.y=Math.PI/2;a.position.set(5.2,6,zz);rahma.add(a);const fill=new THREE.Mesh(new THREE.CircleGeometry(3.2,16,0,Math.PI),M({color:'#8a7a5a',emissive:'#2a2216',emissiveIntensity:.5,side:THREE.DoubleSide}));fill.rotation.y=Math.PI/2;fill.position.set(5.3,6,zz);rahma.add(fill);const fl=new THREE.Mesh(new THREE.PlaneGeometry(6.4,6),fill.material);fl.rotation.y=Math.PI/2;fl.position.set(5.3,3,zz);rahma.add(fl);});}
rahma.position.set(X1+4,0,-60);S.add(rahma);
// ---- area outline ----
const outline=new THREE.LineLoop(new THREE.BufferGeometry().setFromPoints([new THREE.Vector3(X0,17,Z0),new THREE.Vector3(X1,17,Z0),new THREE.Vector3(X1,17,Z1),new THREE.Vector3(X0,17,Z1)]),new THREE.LineBasicMaterial({color:'#ffe1a0',transparent:true,opacity:0}));S.add(outline);
const areaFill=new THREE.Mesh(new THREE.PlaneGeometry(X1-X0,Z1-Z0),new THREE.MeshBasicMaterial({color:'#e8c070',transparent:true,opacity:0,blending:THREE.AdditiveBlending,depthWrite:false}));areaFill.rotation.x=-Math.PI/2;areaFill.position.y=.4;S.add(areaFill);
// ---- Isra light beam ----
const beam=new THREE.Mesh(new THREE.CylinderGeometry(3,7,1600,24,1,true),new THREE.MeshBasicMaterial({color:'#fff0c8',transparent:true,opacity:0,blending:THREE.AdditiveBlending,depthWrite:false,side:THREE.DoubleSide,fog:false}));beam.position.set(DX,800,DZ);S.add(beam);
// highlight halo (generic)
const ring=new THREE.Mesh(new THREE.TorusGeometry(1,.03,8,96),new THREE.MeshBasicMaterial({color:'#ffe1a0',transparent:true,opacity:0,blending:THREE.AdditiveBlending,depthWrite:false}));ring.rotation.x=Math.PI/2;S.add(ring);
const ring2=ring.clone();ring2.material=ring.material.clone();S.add(ring2);
// lights
const domeL=new THREE.PointLight('#ffd590',2,140,1.3);domeL.position.set(DX,50,DZ+20);S.add(domeL);
const qibL=new THREE.PointLight('#ffcf88',1.2,120,1.3);qibL.position.set(-14,30,150);S.add(qibL);
// people
const NP=420,people=new THREE.InstancedMesh(new THREE.CapsuleGeometry(.32,1.1,3,6),M({color:'#ffffff',roughness:.6,emissive:'#9aa0aa',emissiveIntensity:.5}),NP);const PP=[];
for(let i=0;i<NP;i++){let x,z;do{x=X0+8+rnd()*284;z=Z0+8+rnd()*474;}while((x>PX-PW/2-2&&x<PX+PW/2+2&&z>PZ-PD/2-2&&z<PZ+PD/2+2)||(x>QX0-2&&x<QX1+2&&z>QZ0-2)||(x>MX0&&z>MZ0));PP.push({x,z,a:rnd()*6.28,v:.3+rnd()*.7});}
S.add(people);
// ---- camera ----
const K=window.CAMK;const vp=K.map(k=>new THREE.Vector3(...k[1])),vt=K.map(k=>new THREE.Vector3(...k[2]));
const cp=new THREE.CatmullRomCurve3(vp,false,'centripetal'),ct=new THREE.CatmullRomCurve3(vt,false,'centripetal');
function uAt(t){const n=K.length;if(t<=K[0][0])return 0;if(t>=K[n-1][0])return 1;let i=0;while(t>K[i+1][0])i++;const p=(t-K[i][0])/(K[i+1][0]-K[i][0]);const e=.45*p+.55*sm(p);return (i+e)/(n-1);}
const proj=new THREE.Vector3();
window.project=(x,y,z)=>{proj.set(x,y,z).project(cam);return [(proj.x+1)/2*W,(1-proj.y)/2*H,proj.z];};
window.ANCH={qibli:[(QX0+QX1)/2,QH+14,QZ1-10],dome:[DX,PH+DWH+26,DZ],rock:[DX,PH+4,DZ],chain:[CX,PH+9,CZ],marwani:[(MX0+MX1)/2,-6,(MZ0+MZ1)/2],minaret:[X0+4,44,Z0+4],rahma:[X1+4,14,-60],area:[0,0,0]};
const T=window.TL;
const HL={hook:[DX,PH+DWH+3,DZ,32],qibli:[(QX0+QX1)/2,QH+1,QZ1-10,14],dome:[DX,PH+DWH+3,DZ,32],chain:[CX,PH+.5,CZ,10],marwani:[(MX0+MX1)/2,.5,(MZ0+MZ1)/2,50],rahma:[X1+4,1,-60,16]};
function win(a,b,f=.8){return cl((t0-a)/f)*(1-cl((t0-b)/f));}let t0=0;
window.render3d=function(t){t0=t;
 const u=uAt(t);cam.position.copy(cp.getPoint(u));cam.lookAt(ct.getPoint(u));
 // Isra beam
 const bk=win(T.beam0,T.beam1,1.2);beam.material.opacity=bk*(.35+.1*Math.sin(t*3));beam.scale.set(1+.1*Math.sin(t*2),1,1+.1*Math.sin(t*2));domeG.userData.rl.intensity=0;
 // area outline
 const ak=Math.max(win(T.area0,T.area1,.8),win(T.area2,T.area3,.8));outline.material.opacity=ak;areaFill.material.opacity=ak*.16*(1+.4*Math.sin(t*3));
 // highlight ring
 let hk=0,hp=null;for(const [k,v] of Object.entries(HL)){const w=win(T['h_'+k][0],T['h_'+k][1],.6);if(w>hk){hk=w;hp=v;}}
 if(hp){const ph=(t*.7)%1,ph2=(ph+.5)%1;ring.position.set(hp[0],hp[1],hp[2]);ring2.position.copy(ring.position);ring.scale.setScalar(hp[3]*(.8+ph*.6));ring2.scale.setScalar(hp[3]*(.8+ph2*.6));ring.material.opacity=hk*(1-ph);ring2.material.opacity=hk*(1-ph2);}else{ring.material.opacity=0;ring2.material.opacity=0;}
 gold.emissiveIntensity=.85+.6*win(T.h_dome[0],T.h_dome[1]);
 // rock reveal: dome transparent
 const rk=win(T.rock0,T.rock1,.8);domMats.forEach(m=>{m.opacity=1-.85*rk;m.depthWrite=rk<.5;});domeG.userData.rl.intensity=5*rk;
 // marwani reveal
 const mk=win(T.h_marwani[0],T.h_marwani[1]+1.5,.8);patchM.opacity=1-.9*mk;patchM.depthWrite=mk<.5;marw.userData.lamp.intensity=4*mk;
 // minarets halos
 const mn=win(T.minar0,T.minar1,.5);minarets.forEach((m,i)=>{const k=mn*cl((t-T.minar0-i*.25)/.4);m.userData.halo.material.opacity=k*(.6+.4*Math.sin(t*4));});
 // gates glow
 const gk=win(T.gate0,T.gate1,.5);gates.forEach((g,i)=>{g.material.opacity=gk*cl((t-T.gate0-i*.12)/.3)*.8;});
 // people
 const o=new THREE.Object3D();for(let i=0;i<NP;i++){const p=PP[i];const x=p.x+Math.cos(p.a)*t*p.v,z=p.z+Math.sin(p.a)*t*p.v;o.position.set(x,.9,z);o.updateMatrix();people.setMatrixAt(i,o.matrix);}people.instanceMatrix.needsUpdate=true;
 R.render(S,cam);
};
window.ready3d=true;
