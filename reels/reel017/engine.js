// Deterministic timeline engine: window.render(t) positions everything for time t (seconds).
(function(){
  const clamp=(x,a=0,b=1)=>Math.max(a,Math.min(b,x));
  const easeOutCubic=p=>1-Math.pow(1-p,3);
  const easeOutBack=p=>{const c1=1.70158,c3=c1+1;return 1+c3*Math.pow(p-1,3)+c1*Math.pow(p-1,2)};
  const easeInOut=p=>p<.5?2*p*p:1-Math.pow(-2*p+2,2)/2;

  let els=[],scenes=[],bgs=[],rvs=[],beads=[],strikes=[],draws=[],counts=[];
  function init(){
    scenes=[...document.querySelectorAll('.scene')].map(n=>({n,s:+n.dataset.s,e:+n.dataset.e}));
    bgs=[...document.querySelectorAll('.bg')].map(n=>({n,s:+n.dataset.s,e:+n.dataset.e}));
    els=[...document.querySelectorAll('.a')].map((n,i)=>({n,t:+n.dataset.t||0,d:+(n.dataset.d||0.5),a:n.dataset.a||'pop',
      o:n.dataset.o?+n.dataset.o:null,r:+(n.dataset.r||0),f:+(n.dataset.f||0),ph:i*1.37,cx:n.classList.contains('cx')}));
    rvs=[...document.querySelectorAll('.rv')].map(n=>({n,t:+n.dataset.t}));
    beads=[...document.querySelectorAll('.bead')].map(n=>({n,t:+n.dataset.t}));
    strikes=[...document.querySelectorAll('.strike')].map(n=>({n,t:+n.dataset.t,d:+(n.dataset.d||.45)}));
    draws=[...document.querySelectorAll('.dr')].map(n=>{const L=n.getTotalLength?n.getTotalLength():300;n.style.strokeDasharray=L;return {n,t:+n.dataset.t,d:+(n.dataset.d||.6),L}});
    counts=[...document.querySelectorAll('.count')].map(n=>({n,t:+n.dataset.t,d:+(n.dataset.d||1),from:+n.dataset.from,to:+n.dataset.to}));
    buildSubs();
  }
  function winOpacity(t,s,e,f=.35){ if(t<s-f||t>e+f) return 0; return Math.min(clamp((t-s+f)/f),clamp((e+f-t)/f)); }

  function anim(el,t){
    const p=clamp((t-el.t)/el.d);
    let op=1,tx=0,ty=0,sc=1,rot=el.r,bl=0,ls=0;
    switch(el.a){
      case 'pop': op=clamp(p*2.5); sc=.55+.45*easeOutBack(p); break;
      case 'up': op=clamp(p*1.6); ty=(1-easeOutCubic(p))*50; break;
      case 'down': op=clamp(p*1.6); ty=-(1-easeOutCubic(p))*50; break;
      case 'fade': op=easeInOut(p); break;
      case 'left': op=clamp(p*1.6); tx=-(1-easeOutCubic(p))*90; break;
      case 'right': op=clamp(p*1.6); tx=(1-easeOutCubic(p))*90; break;
      case 'stamp': op=clamp(p*3); sc=1+ (1-easeOutCubic(p))*0.9; break;
      case 'drop': op=clamp(p*3); ty=-(1-easeOutBack(p))*120; break;
      case 'none': op=1; break;
      case 'blur': op=clamp(p*1.4); sc=1.08-.08*easeOutCubic(p); bl=(1-easeOutCubic(p))*18; break;
      case 'zoom': op=clamp(p*2); sc=1.55-.55*easeOutCubic(p); bl=(1-easeOutCubic(p))*14; break;
      case 'rise': op=clamp(p*1.5); ty=(1-easeOutCubic(p))*46; bl=(1-easeOutCubic(p))*8; break;
      case 'wide': op=clamp(p*1.5); sc=.92+.08*easeOutCubic(p); ls=(1-easeOutCubic(p)); bl=(1-easeOutCubic(p))*10; break;
    }
    if(t<el.t) op=0;
    if(el.o!==null){ const q=clamp((t-el.o)/.35); op*=1-q; sc*=1+.06*q; bl+=q*12; }
    if(el.f){ ty+=Math.sin(t*1.5+el.ph)*el.f; rot+=Math.sin(t*1.1+el.ph)*el.f*.12; }
    el.n.style.opacity=op; el.n.style.filter=bl>.05?`blur(${bl.toFixed(1)}px)`:''; if(el.a==='wide') el.n.style.letterSpacing=((+(el.n.dataset.ls||0))+ls*0.5).toFixed(3)+'em';
    el.n.style.transform=(el.cx?'translateX(-50%) ':'')+`translate(${tx}px,${ty}px) rotate(${rot}deg) scale(${sc})`;
  }

  // subtitles
  let chunks=[];
  function buildSubs(){
    const W=window.WORDS; if(!W) return;
    chunks=W.chunks.map((c,i)=>{const ws=c.map(k=>W.words[k]);return {ws,s:ws[0].s-0.05,e:0}});
    chunks.forEach((c,i)=>{c.e=i<chunks.length-1?chunks[i+1].s:c.ws[c.ws.length-1].e+.4});
  }
  let lastKey='';
  function subs(t){
    const box=document.getElementById('subbox'),sub=document.getElementById('sub'); if(!box) return;
    const hideAfter=+(sub.dataset.hide||1e9);
    const c=chunks.find(c=>t>=c.s&&t<c.e);
    if(!c||t>hideAfter){sub.style.opacity=0;return;}
    sub.style.opacity=1;
    const key=c.s+'|'+c.ws.map(w=>t>=w.s?(t<w.e+.08?'c':'d'):'u').join('');
    if(key!==lastKey){
      box.innerHTML=c.ws.map(w=>`<span class="${t<w.s?'up':(t<w.e+.08?'cur':'')}">${w.w}</span>`).join(' ');
      lastKey=key;
    }
    const p=clamp((t-c.s)/.18);
    sub.style.transform=`translateX(-50%) translateY(${(1-easeOutCubic(p))*14}px) rotate(-1deg)`;
  }

  window.render=function(t){
    if(!els.length) init();
    scenes.forEach(s=>s.n.style.opacity=winOpacity(t,s.s,s.e,.25));
    bgs.forEach(s=>s.n.style.opacity=winOpacity(t,s.s,s.e,.4));
    els.forEach(e=>anim(e,t));
    rvs.forEach(r=>r.n.classList.toggle('on',t>=r.t));
    beads.forEach(b=>b.n.setAttribute('fill',t>=b.t?b.n.dataset.on:b.n.dataset.off));
    strikes.forEach(s=>s.n.style.transform=`scaleX(${easeOutCubic(clamp((t-s.t)/s.d))})`);
    draws.forEach(d=>d.n.style.strokeDashoffset=d.L*(1-easeInOut(clamp((t-d.t)/d.d))));
    counts.forEach(c=>{const p=easeOutCubic(clamp((t-c.t)/c.d));c.n.textContent=Math.round(c.from+(c.to-c.from)*p)});
    const b=document.getElementById('banner');
    if(b){const op=winOpacity(t,+b.dataset.s,+b.dataset.e,.3);b.style.opacity=op;b.style.transform=`translateX(-50%) rotate(-1.2deg) translateY(${(1-op)*-20}px)`;}
    subs(t);
  };
})();
