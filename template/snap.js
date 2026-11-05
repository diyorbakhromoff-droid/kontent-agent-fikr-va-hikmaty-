const { chromium } = require('playwright');
(async()=>{
  const times=process.argv.slice(2).map(Number);
  const b=await chromium.launch();const p=await b.newPage({viewport:{width:1080,height:1920}});
  await p.goto('file://'+__dirname+'/index.html');await p.evaluate(()=>document.fonts.ready);
  for(const t of times){await p.evaluate(t=>window.render(t),t);await p.screenshot({path:`snaps/t${t}.jpg`,type:'jpeg',quality:80});}
  await b.close();
})();
