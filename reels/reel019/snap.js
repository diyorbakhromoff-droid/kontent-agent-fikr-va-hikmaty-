const { chromium } = require('playwright');const serve=require('./serve.js');
(async()=>{
  const times=process.argv.slice(2).map(Number);const srv=await serve();const url=`http://127.0.0.1:${srv.address().port}/index.html`;
  const b=await chromium.launch({args:['--use-gl=angle','--use-angle=swiftshader','--enable-unsafe-swiftshader','--ignore-gpu-blocklist']});const p=await b.newPage({viewport:{width:1080,height:1920}});
  p.on('pageerror',e=>console.log('ERR',e.message));p.on('console',m=>{if(m.type()==='error')console.log('CONSOLE',m.text())});
  await p.goto(url);await p.evaluate(()=>document.fonts.ready);await p.waitForFunction(()=>window.ready3d,null,{timeout:60000});
  for(const t of times){const t0=Date.now();await p.evaluate(t=>window.render(t),t);await p.screenshot({path:__dirname+`/snaps/t${t}.jpg`,type:'jpeg',quality:82});console.log(t,Date.now()-t0,'ms');}
  await b.close();srv.close();
})();
