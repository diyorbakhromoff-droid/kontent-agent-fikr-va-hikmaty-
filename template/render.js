const { chromium } = require('playwright');
const DUR=+process.argv[2]||78, FPS=30, W=+process.argv[3]||2;
(async()=>{
  const N=Math.round(DUR*FPS); const b=await chromium.launch(); const t0=Date.now();
  await Promise.all([...Array(W)].map(async(_,w)=>{
    const p=await b.newPage({viewport:{width:1080,height:1920}});
    await p.goto('file://'+__dirname+'/index.html'); await p.evaluate(()=>document.fonts.ready);
    for(let f=w;f<N;f+=W){ await p.evaluate(t=>window.render(t),f/FPS);
      await p.screenshot({path:`frames/${String(f).padStart(5,'0')}.jpg`,type:'jpeg',quality:92});
      if(w===0&&f%300===0) console.log('frame',f,'/',N,((Date.now()-t0)/1000).toFixed(0)+'s'); }
  }));
  await b.close(); console.log('DONE',N);
})();
