# -*- coding: utf-8 -*-
"""Gộp 3 trang HDSD thành index.html nhiều tab. Chạy: python3 build_tabs.py"""
import html, os

HERE = os.path.dirname(os.path.abspath(__file__))
TABS = [
    ('eoffice', 'E-office · Văn bản đi, trình ký, công văn đến', 'eoffice/index.html'),
    ('bpm', 'BPM · Phiếu có trình ký', 'bpm/index.html'),
    ('esign', 'E-Sign · Ký điện tử', 'esign/index.html'),
]
FIX = '''<script>document.addEventListener('click',function(e){var a=e.target.closest&&e.target.closest('a[href^="#"]');if(!a)return;var id=decodeURIComponent(a.getAttribute('href').slice(1));e.preventDefault();var t=id?document.getElementById(id):null;if(t)t.scrollIntoView({behavior:'smooth',block:'start'});else if(!id)window.scrollTo(0,0)},true);</script>'''
frames, buttons = [], []
for i, (key, label, path) in enumerate(TABS):
    src = open(os.path.join(HERE, path), encoding='utf-8').read() + FIX
    buttons.append('<button type="button" role="tab" id="t-%s" data-k="%s" aria-controls="p-%s" aria-selected="%s">%s</button>'
                   % (key, key, key, 'true' if i == 0 else 'false', html.escape(label)))
    frames.append('<iframe id="p-%s" role="tabpanel" aria-labelledby="t-%s" title="%s"%s srcdoc="%s"></iframe>'
                  % (key, key, html.escape(label), '' if i == 0 else ' hidden', html.escape(src, quote=True)))

page = """<!doctype html>
<html lang="vi">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">
<title>Hướng dẫn sử dụng Base · Trình ký</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Inter:wght@500;600;700&display=swap">
<style>
:root{--bar:#ffffff;--ink:#0f172a;--mute:#475569;--line:#dfe4ee;--navy:#0047cc;--on:#ffffff;color-scheme:light}
*{box-sizing:border-box}
html,body{height:100%;margin:0}
body{background:var(--bar);color:var(--ink);font:500 14px "Inter",system-ui,-apple-system,"Segoe UI",sans-serif;display:flex;flex-direction:column}
.top{display:flex;align-items:center;gap:18px;padding:8px 16px;padding-top:calc(8px + env(safe-area-inset-top,0px));border-bottom:1px solid var(--line);background:var(--bar);flex:none;flex-wrap:wrap}
.brand{display:flex;align-items:center;gap:8px;font-weight:700;font-size:15px;color:#08246b;white-space:nowrap}.brand i{font-style:normal;color:var(--mute);font-weight:500}.brand b{color:#0b6b3a;letter-spacing:.06em}.brand span{color:var(--mute);font-weight:500}
.tabs{display:flex;gap:6px;flex-wrap:wrap}
.tabs button{font:600 13.5px "Inter",system-ui,sans-serif;color:var(--ink);background:transparent;border:1px solid var(--line);border-radius:999px;padding:7px 16px;cursor:pointer}
.tabs button:hover{border-color:var(--navy)}
.tabs button[aria-selected="true"]{background:linear-gradient(135deg,#003cb3,#0047cc 55%,#08246b);border-color:transparent;color:var(--on)}
.tabs button:focus-visible{outline:2px solid var(--navy);outline-offset:2px}
iframe{flex:1;width:100%;border:0;display:block;min-height:0}
iframe[hidden]{display:none}
@media (max-width:600px){.brand span{display:none}.top{gap:10px}.tabs button{padding:6px 12px;font-size:12.5px}}
</style>
</head>
<body>
<header class="top">
  <div class="brand">BASE.VN <span>· Hướng dẫn trình ký</span></div>
  <nav class="tabs" role="tablist" aria-label="Chọn tài liệu">""" + ''.join(buttons) + """</nav>
</header>
""" + '\n'.join(frames) + """
<script>
(function(){
  var btns=[].slice.call(document.querySelectorAll('.tabs button'));
  function show(k,push){
    if(!document.getElementById('p-'+k)) k=btns[0].getAttribute('data-k');
    btns.forEach(function(b){var on=b.getAttribute('data-k')===k;b.setAttribute('aria-selected',on?'true':'false');document.getElementById('p-'+b.getAttribute('data-k')).hidden=!on;});
    if(push && location.hash!=='#'+k){try{history.replaceState(null,'','#'+k)}catch(e){location.hash=k}}
  }
  btns.forEach(function(b){b.addEventListener('click',function(){show(b.getAttribute('data-k'),true)})});
  show((location.hash||'').slice(1),false);
  addEventListener('hashchange',function(){show(location.hash.slice(1),false)});
})();
</script>
</body>
</html>
"""
open(os.path.join(HERE, 'index.html'), 'w', encoding='utf-8').write(page)
print('index.html', os.path.getsize(os.path.join(HERE, 'index.html')))
