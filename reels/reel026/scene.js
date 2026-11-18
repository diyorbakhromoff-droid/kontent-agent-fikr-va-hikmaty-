import * as THREE from './lib/three.js';
import {RoomEnvironment} from './lib/RoomEnvironment.js';
import {RoundedBoxGeometry} from './lib/RoundedBoxGeometry.js';
const W=1080,H=1920;
const cv=document.getElementById('gl');
const R=new THREE.WebGLRenderer({canvas:cv,antialias:true,preserveDrawingBuffer:true});
R.setPixelRatio(1);R.setSize(W,H,false);R.outputColorSpace=THREE.SRGBColorSpace;R.toneMapping=THREE.ACESFilmicToneMapping;R.toneMappingExposure=1.05;
R.shadowMap.enabled=true;R.shadowMap.type=THREE.PCFSoftShadowMap;
const S=new THREE.Scene();S.background=new THREE.Color('#E9E2D6');
{const pm=new THREE.PMREMGenerator(R);S.environment=pm.fromScene(new RoomEnvironment(),0.04).texture;S.environmentIntensity=0.55;}
const cam=new THREE.PerspectiveCamera(38,W/H,0.1,800);
let seed=26;const rnd=()=>{seed=(seed*16807)%2147483647;return (seed-1)/2147483646};
const cl=(x,a=0,b=1)=>Math.max(a,Math.min(b,x)),sm=p=>p*p*(3-2*p),eo=p=>1-Math.pow(1-p,3),eb=p=>{const c=1.70158;return 1+(c+1)*Math.pow(p-1,3)+c*Math.pow(p-1,2)};
S.add(new THREE.HemisphereLight('#fffaf0','#d8cbb8',1.1));
const sun=new THREE.DirectionalLight('#fff4e0',1.6);sun.position.set(30,60,40);sun.castShadow=true;sun.shadow.mapSize.set(2048,2048);
Object.assign(sun.shadow.camera,{left:-60,right:60,top:60,bottom:-60,near:1,far:200});sun.shadow.radius=6;S.add(sun);S.add(sun.target);
const M=(o)=>new THREE.MeshStandardMaterial(Object.assign({roughness:.75,metalness:0},o));
function tex(w,h,draw){const c=document.createElement('canvas');c.width=w;c.height=h;draw(c.getContext('2d'),w,h);const t=new THREE.CanvasTexture(c);t.colorSpace=THREE.SRGBColorSpace;t.anisotropy=8;return t;}
const C={cream:'#FBF5E6',paper:'#F7EEDB',terra:'#C4553B',green:'#2E6B5B',gold:'#E2A63A',ink:'#2A2724',rose:'#E58E7A',sage:'#9DBBA8',sky:'#B9CCE0',lav:'#C9B8DE',peach:'#F2C2A6',stone:'#9A9388'};
// ---------- ground: soft paper floor that catches shadows ----------
const floor=new THREE.Mesh(new THREE.PlaneGeometry(2000,2000),new THREE.ShadowMaterial({opacity:.16}));floor.rotation.x=-Math.PI/2;floor.receiveShadow=true;S.add(floor);
// station x positions
const SX=[0,70,140,210,280,350];
// floating paper confetti + soft bokeh spheres
const conf=[];{const g=new THREE.PlaneGeometry(1.2,.8),cols=[C.terra,C.green,C.gold,C.lav,C.sky,C.peach];
 for(let i=0;i<160;i++){const m=new THREE.Mesh(g,new THREE.MeshStandardMaterial({color:cols[i%6],side:THREE.DoubleSide,roughness:.9}));
  m.position.set(-40+rnd()*440,4+rnd()*40,-40+rnd()*50);m.userData={ph:rnd()*6.28,v:.3+rnd()*.6,ax:rnd()*3};S.add(m);conf.push(m);}}
const bok=[];{const g=new THREE.SphereGeometry(1,20,14);for(let i=0;i<40;i++){const m=new THREE.Mesh(g,new THREE.MeshStandardMaterial({color:[C.peach,C.lav,C.sky,C.sage][i%4],roughness:.4,transparent:true,opacity:.55}));
 const s=1+rnd()*3;m.scale.setScalar(s);m.position.set(-40+rnd()*440,6+rnd()*30,-60-rnd()*40);m.userData={ph:rnd()*6.28};S.add(m);bok.push(m);}}
// ---------- heart geometry ----------
function heartShape(){const s=new THREE.Shape();s.moveTo(0,-3.2);s.bezierCurveTo(-1.2,-2.2,-4.4,-0.6,-4.4,1.6);s.bezierCurveTo(-4.4,3.6,-2.6,4.6,-1.4,4.6);s.bezierCurveTo(-0.6,4.6,0,4.0,0,3.2);
 s.bezierCurveTo(0,4.0,0.6,4.6,1.4,4.6);s.bezierCurveTo(2.6,4.6,4.4,3.6,4.4,1.6);s.bezierCurveTo(4.4,-0.6,1.2,-2.2,0,-3.2);return s;}
const heartG=new THREE.ExtrudeGeometry(heartShape(),{depth:1.6,bevelEnabled:true,bevelSegments:8,bevelSize:.9,bevelThickness:.9,curveSegments:32});heartG.center();
function makeHeart(color){const m=new THREE.Mesh(heartG,M({color,roughness:.35,metalness:.05,emissive:color,emissiveIntensity:.08}));m.castShadow=true;return m;}
// rounded tile with a number/text
function tile(txt,bg,fg,w=4,h=4,d=.9,fs=200){const t=tex(256,256,(c,W,H)=>{c.fillStyle=bg;c.fillRect(0,0,W,H);c.fillStyle=fg;c.font=`700 ${fs}px Fraunces, Georgia, serif`;c.textAlign='center';c.textBaseline='middle';c.fillText(txt,W/2,H/2+12);});
 const mats=[M({color:bg}),M({color:bg}),M({color:bg}),M({color:bg}),M({map:t}),M({color:bg})];const m=new THREE.Mesh(new RoundedBoxGeometry(w,h,d,4,.35),mats);m.castShadow=true;return m;}
// ---------- STATION 0: hook — big heart + 4 orbiting tiles ----------
const st0=new THREE.Group();st0.position.set(SX[0],0,0);S.add(st0);
const heart0=makeHeart(C.rose);heart0.position.set(0,11,0);heart0.scale.setScalar(1.25);st0.add(heart0);
const tiles0=['1','2','3','4'].map((n,i)=>{const tl=tile(n,C.cream,[C.terra,C.green,C.gold,'#6A5AA0'][i]);st0.add(tl);return tl;});
const q0=tile('?',C.green,C.cream,4.5,4.5,1,210);q0.position.set(0,24,0);st0.add(q0);
// pedestal
const ped=(r=7,h=1.2,col=C.paper)=>{const m=new THREE.Mesh(new THREE.CylinderGeometry(r,r*1.04,h,64),M({color:col,roughness:.85}));m.receiveShadow=true;m.castShadow=true;m.position.y=h/2;return m;};
st0.add(ped(8));
// ---------- STATION 1: daily small vs weekly big — calendar blocks + open Quran on rehal ----------
const st1=new THREE.Group();st1.position.set(SX[1],0,0);S.add(st1);st1.add(ped(14,1.2,'#EFE6D2'));
// rehal (X stand) + open book
const book=new THREE.Group();{const wood=M({color:'#B9814E',roughness:.6});
 const leg=new RoundedBoxGeometry(.6,9,7,2,.2);[-1,1].forEach(s=>{const l=new THREE.Mesh(leg,wood);l.rotation.z=s*.55;l.position.set(s*1.6,4.6,0);l.castShadow=true;book.add(l);});
 const cover=new THREE.Mesh(new RoundedBoxGeometry(11,.4,7.6,2,.15),M({color:C.green,roughness:.5}));cover.position.y=7.9;cover.castShadow=true;book.add(cover);
 const pageT=tex(512,360,(c,W,H)=>{c.fillStyle='#FFFBF0';c.fillRect(0,0,W,H);c.strokeStyle=C.gold;c.lineWidth=10;c.strokeRect(18,18,W-36,H-36);c.fillStyle='rgba(42,39,36,.55)';for(let y=70;y<H-50;y+=30){c.fillRect(50,y,W-100,8);} });
 const pg=new THREE.PlaneGeometry(5.2,7,16,1);const pp=pg.attributes.position;for(let i=0;i<pp.count;i++){const x=pp.getX(i);pp.setZ(i,Math.sin((x+2.6)/5.2*Math.PI)*.35);}pg.computeVertexNormals();pg.translate(2.6,0,0);
 const L=new THREE.Mesh(pg,M({map:pageT,side:THREE.DoubleSide,roughness:.9}));L.rotation.set(-Math.PI/2,0,Math.PI);L.position.set(0,8.15,0);book.add(L);
 const Rp=new THREE.Mesh(pg,M({map:pageT,side:THREE.DoubleSide,roughness:.9}));Rp.rotation.set(-Math.PI/2,0,0);Rp.position.set(0,8.15,0);book.add(Rp);
 const flip=new THREE.Mesh(pg,M({map:pageT,side:THREE.DoubleSide,roughness:.9}));flip.position.set(0,8.2,0);book.add(flip);book.userData.flip=flip;}
book.position.set(-5,1.2,2);book.rotation.y=.35;st1.add(book);
// 7 day blocks (doimiy) and one big weekly block
const days=[];for(let i=0;i<7;i++){const b=tile(['D','S','Ch','P','J','Sh','Y'][i],C.cream,C.green,2.2,2.2,2.2,(i==2||i==5)?120:150);b.position.set(5+((i%4))*2.6,2.3+Math.floor(i/4)*2.6,-1+((i/4|0)?.6:0));st1.add(b);days.push(b);}
const weekBig=tile('7',C.lav,'#5A4A86',5,5,5,180);weekBig.position.set(9,3.7,6);st1.add(weekBig);
// ---------- STATION 2: heart with black dots → cleaned by tavba ----------
const st2=new THREE.Group();st2.position.set(SX[2],0,0);S.add(st2);st2.add(ped(9,1.2,'#E6DDEF'));
const heart2=makeHeart(C.rose);heart2.position.set(0,11.5,0);heart2.scale.setScalar(1.35);st2.add(heart2);
const dots=[];{const g=new THREE.SphereGeometry(.55,20,14);const pts=[[-2,2.5],[1.8,1.9],[-.6,.3],[2.6,-.1],[-2.9,.6],[.8,3.4],[-1.4,-1.4],[1.2,-1.6],[0,1.4],[-3.3,2.7],[3.3,2.4],[-.4,-2.6]];
 pts.forEach(([x,y],i)=>{const d=new THREE.Mesh(g,M({color:'#1d1a18',roughness:.9}));d.position.set(x,y,1.75);d.scale.set(1,1,.35);heart2.add(d);dots.push(d);});}
const sparkle=[];{const g=new THREE.OctahedronGeometry(.35);for(let i=0;i<40;i++){const s=new THREE.Mesh(g,new THREE.MeshBasicMaterial({color:i%2?'#FFF1C4':C.gold,transparent:true,opacity:0}));s.userData={a:rnd()*6.28,r:4+rnd()*6,y:4+rnd()*14,sp:.5+rnd()};st2.add(s);sparkle.push(s);}}
// ---------- STATION 3: phone → tasbeh; plants (alive vs dry) ----------
const st3=new THREE.Group();st3.position.set(SX[3],0,0);S.add(st3);st3.add(ped(14,1.2,'#DCE6EE'));
const phone=new THREE.Group();{const body=new THREE.Mesh(new RoundedBoxGeometry(5,9.6,.6,4,.6),M({color:'#2b2d33',roughness:.3,metalness:.4}));body.castShadow=true;phone.add(body);
 const scr=tex(256,480,(c,W,H)=>{const g=c.createLinearGradient(0,0,0,H);g.addColorStop(0,'#6A8FD8');g.addColorStop(1,'#D86AA8');c.fillStyle=g;c.fillRect(0,0,W,H);c.fillStyle='rgba(255,255,255,.85)';for(let i=0;i<5;i++){c.fillRect(20,40+i*86,W-40,64);} });
 const s=new THREE.Mesh(new THREE.PlaneGeometry(4.4,9),new THREE.MeshBasicMaterial({map:scr}));s.position.z=.31;phone.add(s);}
phone.position.set(-6,8,0);st3.add(phone);
const tasbeh=new THREE.Group();{const bg=new THREE.SphereGeometry(.42,16,12),bm=M({color:'#5E8C6E',roughness:.25,metalness:.1}),gm=M({color:C.gold,roughness:.3,metalness:.5});
 for(let i=0;i<33;i++){const a=i/33*Math.PI*2;const b=new THREE.Mesh(bg,i%11==0?gm:bm);b.position.set(Math.sin(a)*3.4,Math.cos(a)*3.4+(Math.cos(a)<0?Math.cos(a)*1.2:0),0);b.castShadow=true;tasbeh.add(b);}
 const tas=new THREE.Mesh(new THREE.CylinderGeometry(.35,.6,1.8,12),gm);tas.position.set(0,-5.8,0);tasbeh.add(tas);}
tasbeh.position.set(-6,9,0);tasbeh.scale.setScalar(.001);st3.add(tasbeh);
function pot(alive){const g=new THREE.Group();const p=new THREE.Mesh(new THREE.CylinderGeometry(1.6,1.2,2.4,24),M({color:C.terra,roughness:.8}));p.position.y=1.2+1.2;p.castShadow=true;g.add(p);
 const st=new THREE.Mesh(new THREE.CylinderGeometry(.12,.15,1,8),M({color:alive?'#4E8A4A':'#8C7A62'}));st.position.y=3.6;g.add(st);g.userData.stem=st;
 const leaves=[];for(let i=0;i<5;i++){const l=new THREE.Mesh(new THREE.SphereGeometry(.7,12,8),M({color:alive?'#6FB36A':'#B9A27A'}));l.scale.set(1,.35,.6);g.add(l);leaves.push(l);}g.userData.leaves=leaves;g.userData.alive=alive;return g;}
const potA=pot(true),potD=pot(false);potA.position.set(5,0,-1);potD.position.set(10,0,2);st3.add(potA);st3.add(potD);
// ---------- STATION 4: dua — prayer rug + tasbeh + "3" ----------
const st4=new THREE.Group();st4.position.set(SX[4],0,0);S.add(st4);st4.add(ped(12,1.2,'#F6E1D3'));
const rugT=tex(512,800,(c,W,H)=>{c.fillStyle=C.green;c.fillRect(0,0,W,H);c.strokeStyle=C.gold;c.lineWidth=16;c.strokeRect(24,24,W-48,H-48);c.lineWidth=6;c.strokeRect(56,56,W-112,H-112);
 c.beginPath();c.moveTo(110,H-110);c.lineTo(110,300);c.quadraticCurveTo(W/2,60,W-110,300);c.lineTo(W-110,H-110);c.stroke();c.fillStyle='rgba(226,166,58,.25)';c.fill();
 c.fillStyle=C.gold;for(let x=40;x<W;x+=40){c.beginPath();c.arc(x,H-30,7,0,6.28);c.fill();}});
const rug=new THREE.Mesh(new THREE.PlaneGeometry(9,14),M({map:rugT,roughness:.95}));rug.rotation.x=-Math.PI/2;rug.position.set(0,1.25,0);rug.receiveShadow=true;st4.add(rug);
const tas4=tasbeh.clone(true);tas4.scale.setScalar(1);tas4.position.set(0,9,-2);st4.add(tas4);
const three=['1','2','3'].map((n,i)=>{const t=tile(n,C.cream,C.terra,3,3,.8,180);t.position.set(-5+i*5,17,-2);t.scale.setScalar(.001);st4.add(t);return t;});
// ---------- STATION 5: habits stacking into tower with heart on top ----------
const st5=new THREE.Group();st5.position.set(SX[5],0,0);S.add(st5);st5.add(ped(10,1.2,'#DCE6DA'));
const cubes=[];const ccols=[C.terra,C.green,C.gold,C.lav,C.sky,C.peach,C.sage,C.rose];
for(let i=0;i<8;i++){const c=new THREE.Mesh(new RoundedBoxGeometry(4.2,1.8,4.2,3,.3),M({color:ccols[i],roughness:.55}));c.castShadow=true;c.receiveShadow=true;st5.add(c);cubes.push(c);}
const heart5=makeHeart(C.rose);heart5.scale.setScalar(.8);st5.add(heart5);
const glow5=new THREE.PointLight('#ffcf88',0,40,1.5);st5.add(glow5);
// ---------- camera path ----------
const K=window.CAMK;const vp=K.map(k=>new THREE.Vector3(...k[1])),vt=K.map(k=>new THREE.Vector3(...k[2]));
const cp=new THREE.CatmullRomCurve3(vp,false,'centripetal'),ct=new THREE.CatmullRomCurve3(vt,false,'centripetal');
function uAt(t){const n=K.length;if(t<=K[0][0])return 0;if(t>=K[n-1][0])return 1;let i=0;while(t>K[i+1][0])i++;const p=(t-K[i][0])/(K[i+1][0]-K[i][0]);const e=.35*p+.65*sm(p);return (i+e)/(n-1);}
const BG=window.BGK;const bgc=new THREE.Color(),bga=new THREE.Color(),bgb=new THREE.Color();
function bgAt(t){let i=0;while(i<BG.length-1&&t>=BG[i+1][0])i++;bga.set(BG[i][1]);if(i<BG.length-1){bgb.set(BG[i+1][1]);bga.lerp(bgb,cl((t-(BG[i+1][0]-.7))/.7));}return bga;}
const T=window.TL;
window.render3d=function(t){
 S.background.copy(bgAt(t));
 const u=uAt(t);cam.position.copy(cp.getPoint(u));cam.lookAt(ct.getPoint(u));
 sun.position.set(cam.position.x+30,60,40);sun.target.position.set(cam.position.x,0,0);
 conf.forEach(m=>{const d=m.userData;m.rotation.set(t*d.v+d.ph,t*d.v*.7+d.ax,0);m.position.y+=Math.sin(t*.8+d.ph)*.004;});
 bok.forEach(m=>{m.position.y+=Math.sin(t*.5+m.userData.ph)*.01;});
 // st0
 heart0.rotation.y=Math.sin(t*.8)*.5;const hb=1+.06*Math.max(0,Math.sin(t*6.2))*Math.exp(-((t*6.2)%6.28)*.2);heart0.scale.setScalar(1.25*hb);
 tiles0.forEach((tl,i)=>{const k=eb(cl((t-T.t0[i])/.5));const a=t*.6+i*Math.PI/2;tl.position.set(Math.cos(a)*10,9+Math.sin(t*1.3+i)*1.2,Math.sin(a)*10);tl.lookAt(cam.position.x-st0.position.x,tl.position.y,cam.position.z);tl.scale.setScalar(Math.max(.001,k));});
 q0.rotation.y=t*1.2;q0.scale.setScalar(Math.max(.001,1-cl((t-T.qOff)/.4)));q0.position.y=24+Math.sin(t*2)*.6;
 // st1: page flip loops, days light up, weekly block topples
 const fl=book.userData.flip;const fp=((t-T.s1)*.9)%1;fl.rotation.set(-Math.PI/2,0,-fp*Math.PI*(t>T.s1?1:0));
 days.forEach((d,i)=>{const k=eb(cl((t-T.days-i*.18)/.4));d.scale.setScalar(Math.max(.001,k));d.position.y=2.3+Math.floor(i/4)*2.6+(1-k)*6;});
 {const k=cl((t-T.weekFall)/.9);weekBig.rotation.z=-sm(k)*Math.PI/2;weekBig.position.y=3.7-sm(k)*1.2;weekBig.position.x=9+sm(k)*2.4;weekBig.material.forEach&&0;}
 // st2: dots appear one by one, then shrink with sparkles
 dots.forEach((d,i)=>{const on=eb(cl((t-T.dots-i*.22)/.3)),off=cl((t-T.clean-i*.06)/.35);d.scale.set(Math.max(.001,on*(1-off)),Math.max(.001,on*(1-off)),.35);});
 const dark=cl((t-T.dots)/2.6)*(1-cl((t-T.clean)/.8));heart2.material.color.set(C.rose).lerp(new THREE.Color('#6b4b48'),dark*.6);heart2.material.emissiveIntensity=.08+.5*cl((t-T.clean)/.6)*(1-cl((t-T.clean-2)/1.5));
 heart2.rotation.y=Math.sin(t*.7)*.35;
 sparkle.forEach(s=>{const d=s.userData;const k=cl((t-T.clean)/.4)*(1-cl((t-T.clean-2.4)/1));s.material.opacity=k;const a=d.a+t*d.sp;s.position.set(Math.cos(a)*d.r,d.y+Math.sin(t*2+d.a),Math.sin(a)*d.r);s.rotation.set(t*2,t*3,0);});
 // st3: phone flips & shrinks → tasbeh grows; alive plant grows, dry plant droops
 {const k=cl((t-T.swap)/.8);phone.rotation.y=sm(k)*Math.PI*2+Math.sin(t)*.2;phone.scale.setScalar(Math.max(.001,1-sm(cl((t-T.swap-.4)/.5))));
  const k2=eb(cl((t-T.swap-.6)/.6));tasbeh.scale.setScalar(Math.max(.001,k2));tasbeh.rotation.z=t*.6;tasbeh.rotation.y=Math.sin(t*.8)*.4;}
 [potA,potD].forEach(p=>{const al=p.userData.alive;const g=al?eo(cl((t-T.plant)/2)):1;const st=p.userData.stem;const hgt=al?.6+g*4.4:2.4;st.scale.y=hgt;st.position.y=2.4+1.2+hgt/2;
  p.userData.leaves.forEach((l,i)=>{const a=i/5*Math.PI*2+t*(al?.4:0);const y=2.4+1.2+hgt*(.4+i*.12);l.position.set(Math.cos(a)*1,y,Math.sin(a)*1);l.rotation.z=al?.3:-1.1;const s=al?(.4+g*.8):.7;l.scale.set(s,s*.35,s*.6);});
  if(!al){st.rotation.z=.5;}});
 // st4
 tas4.rotation.z=t*.5;three.forEach((tl,i)=>{const k=eb(cl((t-T.three-i*.45)/.4));tl.scale.setScalar(Math.max(.001,k));tl.rotation.y=Math.sin(t+i)*.3;tl.position.y=17+Math.sin(t*1.5+i)*.5;});
 // st5: cubes drop and stack, heart lands on top
 cubes.forEach((c,i)=>{const k=cl((t-T.stack-i*.28)/.45);const y=1.2+.9+i*1.85;c.position.set(Math.sin(i*1.7)*.3,y+(1-eo(k))*30,Math.cos(i*1.3)*.3);c.rotation.y=i*.35+(1-k)*2;c.visible=k>0;});
 {const k=cl((t-T.stack-8*.28-.2)/.6);heart5.visible=k>0;heart5.position.set(0,1.2+8*1.85+3.6+(1-eo(k))*25,0);heart5.rotation.y=t*.8;glow5.position.copy(heart5.position);glow5.intensity=60*cl((t-T.stack-2.8)/.8);}
 R.render(S,cam);
};
window.ready3d=true;
