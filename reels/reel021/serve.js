const http=require('http'),fs=require('fs'),path=require('path');
const T={'.html':'text/html','.js':'text/javascript','.css':'text/css','.woff2':'font/woff2','.mp3':'audio/mpeg'};
module.exports=()=>new Promise(r=>{const s=http.createServer((q,res)=>{const f=path.join(__dirname,decodeURIComponent(q.url.split('?')[0]));fs.readFile(f,(e,d)=>{if(e){res.writeHead(404);return res.end();}res.writeHead(200,{'Content-Type':T[path.extname(f)]||'application/octet-stream'});res.end(d);});});s.listen(0,'127.0.0.1',()=>r(s));});
