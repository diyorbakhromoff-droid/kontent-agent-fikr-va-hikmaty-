// metallic extras: shine sweep var + gold dust, deterministic in t
(function(){
  const R=window.render;
  let dust=[];
  function initDust(){const d=document.getElementById('dust');if(!d)return;let s=7;const rnd=()=>{s=(s*16807)%2147483647;return s/2147483647};
    for(let i=0;i<70;i++){const n=document.createElement('i');const r=2+rnd()*7;n.style.width=n.style.height=(r*2)+'px';d.appendChild(n);
      dust.push({n,x:rnd()*1080,y:rnd()*1920,v:8+rnd()*26,ph:rnd()*6.28,a:.25+rnd()*.6,w:rnd()*30});}}
  window.render=function(t){
    if(!dust.length)initDust();
    const st=document.getElementById('stage');
    const p=((t*0.32)%1.6)/1.6; st.style.setProperty('--sx',(150-p*200)+'%');
    dust.forEach(d=>{const y=((d.y-t*d.v)%1920+1920)%1920;const x=d.x+Math.sin(t*.4+d.ph)*d.w;
      d.n.style.transform=`translate(${x}px,${y}px)`;d.n.style.opacity=d.a*(.55+.45*Math.sin(t*1.7+d.ph));});
    R(t);
  };
})();
