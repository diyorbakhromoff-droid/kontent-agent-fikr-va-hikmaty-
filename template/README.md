# Montaj shabloni

- `engine.js` — window.render(t): .scene[data-s,data-e], .bg, .a[data-t,data-a,data-d,data-r,data-o,data-f], .rv (so'z yonishi), .bead, .strike, .dr (SVG chizish), .count, #banner, #sub (subtitr, WORDS dan)
- `style.css` — namunalar uslubi (pastel qog'oz fon, kartochkalar, yorliqlar, shriftlar)
- Yangi video: `reels/reelNNN/index.html` ni oldingisidan nusxalab sahnalarni yangilang; `words.js` ElevenLabs transkripsiya so'z vaqtlaridan quriladi
- Render: shablon fayllari va fonts/ ni reel papkasiga ko'chiring, so'ng `NODE_PATH=$(npm root -g) node render.js <davomiylik> 2` → frames/ → ffmpeg + voice.mp3
