const { chromium } = require('playwright');const serve=require('./serve.js');
const DUR=+process.argv[2], FPS=30, W=+process.argv[3]||2, START=+process.argv[4]||0;
(async()=>{const srv=await serve();const url=`http://127.0.0.1:${srv.address().port}/index.html`;
  const N=Math.round(DUR*FPS); const b=await chromium.launch({args:['--use-gl=angle','--use-angle=swiftshader','--enable-unsafe-swiftshader','--ignore-gpu-blocklist']}); const t0=Date.now();
  await Promise.all([...Array(W)].map(async(_,w)=>{
    const p=await b.newPage({viewport:{width:1080,height:1920}});
    await p.goto(url); await p.evaluate(()=>document.fonts.ready); await p.waitForFunction(()=>window.ready3d,null,{timeout:60000});
    for(let f=START+w;f<N;f+=W){ await p.evaluate(t=>window.render(t),f/FPS);
      await p.screenshot({path:__dirname+`/frames/${String(f).padStart(5,'0')}.jpg`,type:'jpeg',quality:90});
      if(w===0&&f%150===0) console.log('frame',f,'/',N,((Date.now()-t0)/1000).toFixed(0)+'s'); }
  }));
  await b.close(); srv.close(); console.log('DONE',N);
})();
