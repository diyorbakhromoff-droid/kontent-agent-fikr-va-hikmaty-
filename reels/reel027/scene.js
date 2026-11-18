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
const heart0=makeHeart(C.rose);heart0.material=heart0.material.clone();heart0.position.set(0,11,0);heart0.scale.setScalar(1.25);st0.add(heart0);
const tiles0=['1','2','3','4'].map((n,i)=>{const tl=tile(n,C.cream,[C.terra,C.green,C.gold,'#6A5AA0'][i]);st0.add(tl);return tl;});
const q0=tile('?',C.green,C.cream,4.5,4.5,1,210);q0.position.set(0,24,0);st0.add(q0);
// pedestal
const ped=(r=7,h=1.2,col=C.paper)=>{const m=new THREE.Mesh(new THREE.CylinderGeometry(r,r*1.04,h,64),M({color:col,roughness:.85}));m.receiveShadow=true;m.castShadow=true;m.position.y=h/2;return m;};
st0.add(ped(8));

// ---------- STATION 1: night room — alone with phone ----------
const st1=new THREE.Group();st1.position.set(SX[1],0,0);S.add(st1);
{const wallM=M({color:'#E8DCC8',roughness:.95}),floorM=M({color:'#CDB89A',roughness:.9});
 const fl=new THREE.Mesh(new THREE.BoxGeometry(22,.6,18),floorM);fl.position.y=.3;fl.receiveShadow=true;st1.add(fl);
 const bw=new THREE.Mesh(new THREE.BoxGeometry(22,16,.6),wallM);bw.position.set(0,8.3,-9);bw.receiveShadow=true;st1.add(bw);
 const lw=new THREE.Mesh(new THREE.BoxGeometry(.6,16,18),wallM);lw.position.set(-11,8.3,0);lw.receiveShadow=true;st1.add(lw);
 // window with night sky + moon
 const winT=tex(256,320,(c,W,H)=>{const g=c.createLinearGradient(0,0,0,H);g.addColorStop(0,'#2B3A67');g.addColorStop(1,'#5A6FA8');c.fillStyle=g;c.fillRect(0,0,W,H);c.fillStyle='#FFF4D6';c.beginPath();c.arc(170,90,38,0,6.28);c.fill();c.fillStyle='#3a4a7a';c.beginPath();c.arc(186,80,34,0,6.28);c.fill();c.fillStyle='rgba(255,255,255,.8)';for(let i=0;i<30;i++){c.fillRect(Math.random()*W,Math.random()*H*.7,2,2);}c.strokeStyle='#C9A76A';c.lineWidth=10;c.strokeRect(5,5,W-10,H-10);c.beginPath();c.moveTo(W/2,0);c.lineTo(W/2,H);c.moveTo(0,H/2);c.lineTo(W,H/2);c.stroke();});
 const win=new THREE.Mesh(new THREE.PlaneGeometry(6,7.5),new THREE.MeshBasicMaterial({map:winT}));win.position.set(3,9.5,-8.65);st1.add(win);
 // rug, low sofa/cushion, side table with lamp
 const rug=new THREE.Mesh(new THREE.CylinderGeometry(5.5,5.5,.12,40),M({color:C.terra,roughness:1}));rug.position.set(0,.66,1);rug.receiveShadow=true;st1.add(rug);
 const cush=new THREE.Mesh(new RoundedBoxGeometry(9,2.2,3.6,3,.8),M({color:C.green,roughness:.9}));cush.position.set(-3,1.7,-5.6);cush.castShadow=true;st1.add(cush);
 const back=new THREE.Mesh(new RoundedBoxGeometry(9,3.4,1.2,3,.5),M({color:C.green,roughness:.9}));back.position.set(-3,3.4,-7.6);st1.add(back);
 const tbl=new THREE.Mesh(new THREE.CylinderGeometry(1.4,1.4,3,24),M({color:'#B9814E'}));tbl.position.set(4.5,2.1,-5.5);tbl.castShadow=true;st1.add(tbl);
 const shade=new THREE.Mesh(new THREE.CylinderGeometry(.9,1.5,1.8,24,1,true),new THREE.MeshStandardMaterial({color:'#FFF1C4',emissive:'#FFD58A',emissiveIntensity:.9,side:THREE.DoubleSide}));shade.position.set(4.5,5.4,-5.5);st1.add(shade);
 const pole=new THREE.Mesh(new THREE.CylinderGeometry(.1,.1,1.6,8),M({color:C.ink}));pole.position.set(4.5,4.2,-5.5);st1.add(pole);
 const lamp=new THREE.PointLight('#FFC870',0,40,1.4);lamp.position.set(4.5,5.4,-5.5);st1.add(lamp);st1.userData.lamp=lamp;}
const phone1=new THREE.Group();{const body=new THREE.Mesh(new RoundedBoxGeometry(2.2,4.2,.3,4,.3),M({color:'#2b2d33',roughness:.3,metalness:.4}));body.castShadow=true;phone1.add(body);
 const scr=tex(128,240,(c,W,H)=>{const g=c.createLinearGradient(0,0,0,H);g.addColorStop(0,'#7FA3E8');g.addColorStop(1,'#E87FB8');c.fillStyle=g;c.fillRect(0,0,W,H);c.fillStyle='rgba(255,255,255,.8)';for(let i=0;i<5;i++)c.fillRect(10,20+i*44,W-20,30);});
 const sc=new THREE.Mesh(new THREE.PlaneGeometry(1.9,3.9),new THREE.MeshBasicMaterial({map:scr}));sc.position.z=.16;phone1.add(sc);}
phone1.position.set(-3,3.6,-5.2);phone1.rotation.x=-1.1;st1.add(phone1);
const glowP=new THREE.PointLight('#9DB7FF',0,14,1.5);glowP.position.set(-3,5,-4.5);st1.add(glowP);
// ---------- STATION 2: dark block wiped by a bright block ----------
const st2=new THREE.Group();st2.position.set(SX[2],0,0);S.add(st2);st2.add(ped(10,1.2,'#E6DDEF'));
const badB=new THREE.Mesh(new RoundedBoxGeometry(5,5,5,4,.6),M({color:'#3a3330',roughness:.6}));badB.castShadow=true;st2.add(badB);
const goodB=new THREE.Mesh(new RoundedBoxGeometry(5.4,5.4,5.4,4,.6),M({color:C.gold,roughness:.35,metalness:.2,emissive:'#E2A63A',emissiveIntensity:.15}));goodB.castShadow=true;st2.add(goodB);
const heart2=makeHeart(C.rose);heart2.scale.setScalar(.7);st2.add(heart2);
const sparkle=[];{const g=new THREE.OctahedronGeometry(.35);for(let i=0;i<40;i++){const s=new THREE.Mesh(g,new THREE.MeshBasicMaterial({color:i%2?'#FFF1C4':C.gold,transparent:true,opacity:0}));s.userData={a:rnd()*6.28,r:4+rnd()*6,y:3+rnd()*12,sp:.5+rnd()};st2.add(s);sparkle.push(s);}}
// ---------- STATION 3: good character — teacups + smile tiles ----------
const st3=new THREE.Group();st3.position.set(SX[3],0,0);S.add(st3);st3.add(ped(12,1.2,'#DCE6EE'));
function cup(col){const g=new THREE.Group();const b=new THREE.Mesh(new THREE.CylinderGeometry(1.5,1.1,2.2,32,1,true),M({color:col,side:THREE.DoubleSide,roughness:.4}));b.position.y=1.1;b.castShadow=true;g.add(b);
 const bot=new THREE.Mesh(new THREE.CircleGeometry(1.1,32),M({color:col}));bot.rotation.x=-Math.PI/2;g.add(bot);
 const tea=new THREE.Mesh(new THREE.CircleGeometry(1.4,32),M({color:'#B5652E',roughness:.2}));tea.rotation.x=-Math.PI/2;tea.position.y=1.9;g.add(tea);
 const h=new THREE.Mesh(new THREE.TorusGeometry(.6,.15,10,20,Math.PI*1.2),M({color:col}));h.position.set(1.6,1.2,0);h.rotation.z=-.6;g.add(h);
 const sau=new THREE.Mesh(new THREE.CylinderGeometry(2.4,2.1,.25,32),M({color:C.cream}));sau.position.y=-.1;sau.receiveShadow=true;g.add(sau);return g;}
const cupA=cup(C.cream),cupB=cup(C.sky);cupA.position.set(-3.5,1.35,1);cupB.position.set(3.5,1.35,-1);st3.add(cupA);st3.add(cupB);
const steam=[];{const g=new THREE.SphereGeometry(.35,10,8);for(let i=0;i<24;i++){const m=new THREE.Mesh(g,new THREE.MeshBasicMaterial({color:'#ffffff',transparent:true,opacity:.0}));m.userData={c:i%2?cupA:cupB,ph:rnd()};st3.add(m);steam.push(m);}}
const smileT=tex(256,256,(c,W,H)=>{c.fillStyle=C.gold;c.fillRect(0,0,W,H);c.fillStyle=C.ink;c.beginPath();c.arc(88,100,16,0,6.28);c.arc(168,100,16,0,6.28);c.fill();c.strokeStyle=C.ink;c.lineWidth=16;c.lineCap='round';c.beginPath();c.arc(128,120,62,.35,Math.PI-.35);c.stroke();});
const smiles=[0,1,2].map(i=>{const m=new THREE.Mesh(new RoundedBoxGeometry(3,3,.8,4,.4),[M({color:C.gold}),M({color:C.gold}),M({color:C.gold}),M({color:C.gold}),M({map:smileT}),M({color:C.gold})]);m.castShadow=true;m.position.set(-5+i*5,12,0);m.scale.setScalar(.001);st3.add(m);return m;});
// ---------- STATION 4: two plates — doubtful one slides away ----------
const st4=new THREE.Group();st4.position.set(SX[4],0,0);S.add(st4);st4.add(ped(12,1.2,'#F6E1D3'));
function plate(){const g=new THREE.Group();const p=new THREE.Mesh(new THREE.CylinderGeometry(3,2.4,.4,40),M({color:'#FFFFFF',roughness:.3}));p.castShadow=true;p.receiveShadow=true;g.add(p);const r=new THREE.Mesh(new THREE.TorusGeometry(2.7,.12,8,40),M({color:C.gold,metalness:.5,roughness:.3}));r.rotation.x=Math.PI/2;r.position.y=.22;g.add(r);return g;}
const plQ=plate(),plOk=plate();plQ.position.set(-4,1.6,0);plOk.position.set(4,1.6,0);st4.add(plQ);st4.add(plOk);
const qT=tile('?',C.lav,'#5A4A86',2.6,2.6,2.6,180);qT.position.set(0,1.6,0);plQ.add(qT);
const okT=tile('✓',C.sage,C.green,2.6,2.6,2.6,170);okT.position.set(0,1.6,0);plOk.add(okT);
const coins=[];{const g=new THREE.CylinderGeometry(.7,.7,.2,24);for(let i=0;i<5;i++){const c=new THREE.Mesh(g,M({color:C.gold,metalness:.6,roughness:.3}));c.position.set(-1.6+i*.2,.35+i*.22,1.4);plQ.add(c);coins.push(c);}}
// ---------- STATION 5: glowing heart in a ring of light ----------
const st5=new THREE.Group();st5.position.set(SX[5],0,0);S.add(st5);st5.add(ped(9,1.2,'#DCE6DA'));
const heart5=makeHeart(C.rose);heart5.position.set(0,11,0);heart5.scale.setScalar(1.1);st5.add(heart5);
const ring5=new THREE.Mesh(new THREE.TorusGeometry(8,.25,12,96),M({color:C.gold,emissive:C.gold,emissiveIntensity:.6,metalness:.5,roughness:.3}));ring5.position.set(0,11,0);st5.add(ring5);
const glow5=new THREE.PointLight('#ffcf88',0,40,1.5);glow5.position.set(0,11,6);st5.add(glow5);

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
 // st0 heart pulses 3 times at "uch marta ishora"
 tiles0.forEach((tl,i)=>{const k=eb(cl((t-T.t0[i])/.5));const a=t*.6+i*Math.PI/2;tl.position.set(Math.cos(a)*10,9+Math.sin(t*1.3+i)*1.2,Math.sin(a)*10);tl.lookAt(cam.position.x-st0.position.x,tl.position.y,cam.position.z);tl.scale.setScalar(Math.max(.001,k));});
 {let p=0;T.pulse.forEach(pt=>{const d=t-pt;if(d>0&&d<.6)p=Math.max(p,Math.sin(d/.6*Math.PI));});heart0.scale.setScalar(1.25*(1+.18*p));heart0.material.emissiveIntensity=.08+.6*p;heart0.rotation.y=Math.sin(t*.8)*.5;}
 q0.rotation.y=t*1.2;q0.scale.setScalar(Math.max(.001,1-cl((t-T.qOff)/.4)));q0.position.y=24+Math.sin(t*2)*.6;
 // st1 night room: lamp + phone glow, phone tilts down (put away) at T.phoneDown
 st1.userData.lamp.intensity=50;{const k=cl((t-T.phoneDown)/.8);glowP.intensity=30*(1-k)*(.8+.2*Math.sin(t*9));phone1.rotation.x=-1.1-sm(k)*.45;phone1.position.y=3.6-sm(k)*.6;}
 // st2: bad block drops, good block drops on it; bad shrinks
 {const kb=cl((t-T.bad)/.6);badB.position.set(0,1.2+2.5+(1-eo(kb))*25,0);badB.visible=kb>0;badB.rotation.y=.4;
  const kg=cl((t-T.good)/.6);goodB.visible=kg>0;goodB.position.set(0,1.2+2.7+5+(1-eo(kg))*25-5*sm(cl((t-T.good-.6)/1)),0);goodB.rotation.y=.4+t*.2*(kg>=1?1:0);
  const ks=cl((t-T.good-.3)/1);badB.scale.setScalar(Math.max(.001,1-sm(ks)));
  const kh=eb(cl((t-T.heart2)/.6));heart2.position.set(0,1.2+5.4+3.6+Math.sin(t*2)*.4,0);heart2.scale.setScalar(Math.max(.001,.7*kh));heart2.rotation.y=t*.8;
  sparkle.forEach(s=>{const d=s.userData;const k=cl((t-T.good-.4)/.4)*(1-cl((t-T.good-3)/1));s.material.opacity=k;const a=d.a+t*d.sp;s.position.set(Math.cos(a)*d.r,d.y+Math.sin(t*2+d.a),Math.sin(a)*d.r);s.rotation.set(t*2,t*3,0);});}
 // st3: steam + smiles pop
 steam.forEach((m,i)=>{const d=m.userData;const ph=((t*.35+d.ph)%1);const c=d.c.position;m.position.set(c.x+Math.sin(ph*6+i)*.4,c.y+2.2+ph*5,c.z);m.material.opacity=.5*Math.sin(ph*Math.PI);m.scale.setScalar(.6+ph*1.4);});
 smiles.forEach((m,i)=>{const k=eb(cl((t-T.smile-i*.35)/.4));m.scale.setScalar(Math.max(.001,k));m.position.y=12+Math.sin(t*1.6+i)*.6;m.rotation.y=Math.sin(t+i)*.35;});
 // st4: doubtful plate slides away & fades at T.away; ok plate rises
 {const k=cl((t-T.away)/1.1);plQ.position.set(-4-sm(k)*14,1.6+Math.sin(k*Math.PI)*3,0+sm(k)*4);plQ.rotation.z=sm(k)*.8;plQ.scale.setScalar(Math.max(.001,1-sm(cl((t-T.away-.6)/.6))));
  qT.rotation.y=t*.9;okT.rotation.y=-t*.6;const k2=eo(cl((t-T.away-.4)/.8));plOk.position.set(4-4*k2,1.6+k2*1.5,0);}
 // st5
 heart5.rotation.y=t*.7;ring5.rotation.set(Math.PI/2+Math.sin(t*.6)*.3,t*.4,0);glow5.intensity=40*cl((t-T.s5)/1);heart5.material.emissiveIntensity=.08+.25*cl((t-T.s5)/1);
 R.render(S,cam);
};
window.ready3d=true;
