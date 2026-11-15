# -*- coding: utf-8 -*-
"""Build 1 trang HDSD từ một module nội dung.
Chạy: python3 build.py content_eoffice   → ../site/<app>/index.html"""
import base64, json, os, re, html, unicodedata, sys, importlib

HERE = os.path.dirname(os.path.abspath(__file__))
C = importlib.import_module(sys.argv[1] if len(sys.argv) > 1 else 'content_eoffice')
WEB = os.path.join(HERE, 'web')
CIRC = '①②③④⑤⑥⑦⑧⑨⑩'


def L(vi, en, tag='span'):
    return f'<{tag} class="vi">{vi}</{tag}><{tag} class="en">{en}</{tag}>'


def LP(p, tag='span'):
    return L(p[0], p[1], tag)


def nodia(s):
    s = re.sub('<[^>]+>', ' ', s)
    s = unicodedata.normalize('NFD', s.replace('đ', 'd').replace('Đ', 'D'))
    return ''.join(c for c in s if unicodedata.category(c) != 'Mn').lower()


def pins(s):
    return re.sub('[①-⑩]', lambda m: f'<i class="pin">{CIRC.index(m.group(0)) + 1}</i>', s)


_IMG = {}


def img_uri(key):
    if key not in _IMG:
        b = open(os.path.join(WEB, key + '.webp'), 'rb').read()
        _IMG[key] = 'data:image/webp;base64,' + base64.b64encode(b).decode()
    return _IMG[key]


def fig(key, cap=None):
    link = C.IMG_LINK.get(key)
    lk = ((' · ' if cap else '') + f'<a href="{link}" target="_blank" rel="noopener">{L("Mở màn hình này ↗", "Open this screen ↗")}</a>') if link else ''
    cp = (LP(cap) if cap else '') + lk
    img_uri(key)
    from PIL import Image
    w, h = Image.open(os.path.join(WEB, key + '.webp')).size
    z = ' zoomshot' if w < 1300 else ''
    return (f'<figure class="shot{z}"><div class="win"><i></i><i></i><i></i></div><img data-k="{key}" width="{w}" height="{h}" alt="{key}" data-zoom>'
            f'<figcaption>{cp}</figcaption></figure>')


ROLE = {r['id']: r for r in C.ROLES}
ISS = {i['id']: i for i in C.ISSUES}
STEPN = {s['id']: s for s in C.STEPS}


# ---------- Lưu đồ swimlane (sinh từ C.FLOW) ----------
def flow():
    F = C.FLOW
    W, LW, TOP = 1290, 150, 50
    lanes = F['lanes']  # (key, vi, en, color)
    LH = 104
    cols = [s['id'] for s in C.STEPS]
    CW = (W - LW) / len(cols)
    X = lambda i: LW + CW * i + CW / 2
    Y = {k[0]: TOP + LH * n + LH / 2 for n, k in enumerate(lanes)}
    H = TOP + LH * len(lanes) + 10
    NW = min(128, CW - 14)
    o = [f'<svg class="flow" viewBox="0 0 {W} {H}" role="img" aria-label="Lưu đồ">', '<defs>']
    for mid, c in [('ar', '#94a3b8'), ('arR', '#ff3b5c'), ('arB', '#0047cc'), ('arG', '#16a34a')]:
        o.append(f'<marker id="{mid}" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0,0L10,5L0,10z" fill="{c}"/></marker>')
    o.append('</defs>')
    for n, (k, vi, en, col) in enumerate(lanes):
        y = TOP + LH * n
        o.append(f'<rect x="0" y="{y}" width="{W}" height="{LH}" class="lane{n % 2}"/>')
        o.append(f'<rect x="0" y="{y}" width="5" height="{LH}" fill="{col}"/>')
        o.append(f'<text x="16" y="{y + LH / 2 + 5}" class="lt"><tspan class="vi">{vi}</tspan><tspan class="en">{en}</tspan></text>')
    for i, c in enumerate(cols):
        o.append(f'<a href="#{c}" class="colh"><text x="{X(i)}" y="22" text-anchor="middle" class="ch">{c}</text>'
                 f'<text x="{X(i)}" y="40" text-anchor="middle" class="cs"><tspan class="vi">{C.SHORT[c][0]}</tspan><tspan class="en">{C.SHORT[c][1]}</tspan></text></a>')
    pos = {}
    for nd in F['nodes']:
        nid, i, lane, vi, en = nd[:5]
        cls = nd[5] if len(nd) > 5 else 'n'
        dx = nd[6] if len(nd) > 6 else 0
        x, y = X(i) + dx, Y[lane]
        pos[nid] = (x, y)
        o.append(f'<a href="#{cols[i]}" class="nd"><rect x="{x - NW / 2}" y="{y - 26}" width="{NW}" height="52" rx="10" class="{cls}"/>'
                 f'<text x="{x}" y="{y - 3}" text-anchor="middle" class="nt"><tspan class="vi">{vi[0]}</tspan><tspan class="en">{en[0]}</tspan></text>'
                 f'<text x="{x}" y="{y + 14}" text-anchor="middle" class="nt2"><tspan class="vi">{vi[1]}</tspan><tspan class="en">{en[1]}</tspan></text></a>')
    mk = {'': 'ar', 'or': 'arB', 'gr': 'arG', 'rj': 'arR'}
    tc = {'': 'lb', 'or': 'lb ort', 'gr': 'lb gt', 'rj': 'lb rjt'}
    h = NW / 2
    for e in F['edges']:
        a, b = e[0], e[1]
        cls = e[2] if len(e) > 2 else ''
        lab = e[3] if len(e) > 3 else None
        dash = e[4] if len(e) > 4 else False
        off = e[5] if len(e) > 5 else 0
        (x1, y1), (x2, y2) = pos[a], pos[b]
        if abs(y1 - y2) < 1:
            sx, ex = (x1 + h, x2 - h - 2) if x2 > x1 else (x1 - h, x2 + h + 2)
            sy = ey = y1 + off
            path = f'M{sx},{sy} L{ex},{ey}'
            lx, ly = (sx + ex) / 2, sy - 8
        elif abs(x1 - x2) < 1:
            sx = ex = x1 + off
            sy, ey = (y1 + 27, y2 - 29) if y2 > y1 else (y1 - 27, y2 + 29)
            path = f'M{sx},{sy} L{ex},{ey}'
            lx, ly = sx + 6, (sy + ey) / 2
        else:
            up = y2 < y1
            sx = x1 + off
            sy = y1 - 27 if up else y1 + 27
            ym = y2 + LH / 2 if up else y2 - LH / 2
            ex = x2 + off
            ey = y2 + 29 if up else y2 - 29
            path = f'M{sx},{sy} L{sx},{ym} L{ex},{ym} L{ex},{ey}'
            lx, ly = (sx + ex) / 2, ym - 5
        da = ' stroke-dasharray="5 4"' if dash else ''
        o.append(f'<path d="{path}" class="ln {cls}" fill="none" marker-end="url(#{mk[cls]})"{da}/>')
        if lab:
            anchor = 'start' if abs(x1 - x2) < 1 else 'middle'
            if abs(x1 - x2) >= 1 and abs(y1 - y2) >= 1:
                lw = 6.6 * max(len(lab[0]), len(lab[1])) + 8
                o.append(f'<rect x="{lx - lw / 2}" y="{ly - 11}" width="{lw}" height="15" rx="4" class="lbg"/>')
            o.append(f'<text x="{lx}" y="{ly}" text-anchor="{anchor}" class="{tc[cls]}"><tspan class="vi">{lab[0]}</tspan><tspan class="en">{lab[1]}</tspan></text>')
    o.append('</svg>')
    return ''.join(o)


def matrix():
    h = ['<div class="tblw"><table class="mx"><thead><tr><th>' + L('Vai trò', 'Role') + '</th>']
    for s in C.STEPS:
        h.append(f'<th><a href="#{s["id"]}" class="mxs" data-step="{s["id"]}">{s["id"]}</a><small>{LP(C.SHORT[s["id"]])}</small></th>')
    h.append('</tr></thead><tbody>')
    for r in C.ROLES:
        h.append(f'<tr><th><button class="mxr" data-role="{r["id"]}" style="--rc:{r["color"]}"><i></i>{LP(r["name"])}</button><small>{LP(r["desc"])}</small></th>')
        for s in C.STEPS:
            v = C.RMAP[s['id']].get(r['id'], '')
            sym = {'m': '●', 'p': '○', '': '·'}[v]
            tip = C.RDO.get(s['id'], {}).get(r['id'])
            tt = f' title="{html.escape(tip[0])}"' if tip else ''
            h.append(f'<td class="m{v}"{tt} style="--rc:{r["color"]}">{sym}</td>')
        h.append('</tr>')
    h.append('</tbody></table></div><p class="legend">● ' + L('làm chính', 'main') + ' &nbsp; ○ ' + L('phối hợp / xem', 'collaborate / view') + ' &nbsp; · ' + L('không tham gia', 'not involved') + '</p>')
    return ''.join(h)


def rail():
    o = ['<div class="rail">']
    for s in C.STEPS:
        who = ''.join(f'<span class="chip" style="--rc:{ROLE[k]["color"]}">{LP(ROLE[k]["short"])}</span>' for k, v in C.RMAP[s['id']].items() if v == 'm')
        o.append(f'<a class="rc" href="#{s["id"]}" data-step="{s["id"]}"><b>{s["id"]}</b><span class="rt">{LP(s["title"])}</span>'
                 f'<span class="ra">{LP(s["app"])} · {LP(s["dur"])}</span><span class="who">{who}</span><span class="rnote"></span></a>')
    o.append('</div>')
    return ''.join(o)


def jnav():
    rs = ''.join(f'<button class="jr" data-role="{r["id"]}" style="--rc:{r["color"]}"><i></i>{LP(r["short"])}<em>{sum(1 for s in C.STEPS if C.RMAP[s["id"]].get(r["id"]))}</em></button>' for r in C.ROLES)
    ss = ''.join(f'<a class="js" href="#{s["id"]}" data-step="{s["id"]}">{s["id"]}</a>' for s in C.STEPS)
    return (f'<div id="jnav"><div class="jrow"><span class="jl">{L("Vị trí", "Role")}</span>{rs}<button id="jnext">{L("Bước tiếp của tôi ↓", "My next step ↓")}</button></div>'
            f'<div class="jrow"><span class="jl">{L("Bước", "Step")}</span>{ss}<span id="jncur"></span></div></div>')


def steps_html():
    o = []
    for s in C.STEPS:
        sid = s['id']
        roles = ''.join(f'<span class="chip" style="--rc:{ROLE[k]["color"]}">{LP(ROLE[k]["short"])}{" &nbsp;○" if v == "p" else ""}</span>' for k, v in C.RMAP[sid].items() if v)
        links = ''.join(f'<a href="{u}" target="_blank" rel="noopener">{LP(t)} ↗</a>' for t, u in s['links'])
        w5 = ''.join(f'<div><b>{LP(a)}</b><span>{LP(b)}</span></div>' for a, b in s['w5'])
        acts = []
        n = 0
        for (vi, en), key in s['acts']:
            if key == '__h':
                acts.append(f'<li class="ash" id="{sid}-{len(acts)}">{L(vi, en)}</li>')
                continue
            n += 1
            acts.append(f'<li><span class="an">{n}</span><div class="at">{pins(L(vi, en, "p"))}</div>' + (fig(key) if key else '') + '</li>')
        errs = ''.join(f'<li><a href="#{e}" class="isslink" data-iss="{e}">{LP(ISS[e]["q"])}</a></li>' for e in s['errs'])
        done = ''.join(f'<li>{LP(d)}</li>' for d in s['done'])
        rdo = ''.join(f'<p class="rdo" data-role="{k}" style="--rc:{ROLE[k]["color"]}"><b>{LP(ROLE[k]["short"])}</b> {L("ở bước này:", "here:")} {LP(v)}</p>' for k, v in C.RDO[sid].items())
        o.append(f'''<section class="step" id="{sid}" data-step="{sid}">
<header class="sh"><span class="sid">{sid}</span><h3>{LP(s["title"])}</h3></header>
<div class="pills">{roles}<span class="pill">{LP(s["app"])}</span><span class="pill">⏱ {LP(s["dur"])}</span></div>
<div class="lbar"><span>{L("Mở trên Base:", "Open on Base:")}</span>{links}</div>
<div class="rnote2">{rdo}<p class="rdo none">{L("Vai trò bạn chọn không tham gia bước này.", "Your role is not involved in this step.")}</p></div>
<div class="w5">{w5}</div>
<div class="ailine">✦ <b>{L("Dùng AI ở bước này", "Use AI here")}</b> — {LP(s["ai"])}</div>
<h4>{L("Cách làm", "How to")}</h4><ol class="acts">{"".join(acts)}</ol>
<div class="tri"><div><h5>{L("Sau đó", "Next")}</h5><p>{LP(s["after"])}</p></div>
<div><h5>{L("Lỗi hay gặp", "Common issues")}</h5><ul>{errs}</ul></div>
<div><h5>{L(f"Xong {sid} khi", f"{sid} is done when")}</h5><ul class="chk">{done}</ul></div></div>
</section>''')
    return ''.join(o)


def benefits():
    o = ['<div class="ben">']
    for key, t, d, lab, num, before in C.BEN:
        cls = 'ok' if lab[0] == 'Chắc chắn' else 'tg'
        lk = f'<a href="{C.IMG_LINK[key]}" target="_blank" rel="noopener">{L("Xem trên Base ↗", "View on Base ↗")}</a>' if key in C.IMG_LINK else ''
        o.append(f'<div class="bc"><div class="bt"><h4>{LP(t)}</h4><p>{LP(d)}</p><p class="num"><span class="lab {cls}">{LP(lab)}</span>{LP(num)}</p>'
                 f'<p class="bef">{L("Trước:", "Before:")} <s>{LP(before)}</s></p>{lk}</div>{fig(key)}</div>')
    o.append('</div>')
    A = C.AIBLK
    k = ''.join(f'<div><b>{LP(b) if isinstance(b, tuple) else b}</b><span>{LP(s)}</span><em>{LP(e)}</em></div>' for b, s, e in A['kpi'])
    o.append(f'<div class="aiblk"><div class="aih"><span>✦ AI</span><h4>{LP(A["title"])}</h4><p>{LP(A["desc"])}</p><div class="aik">{k}</div></div>'
             f'<div class="aiimgs">{"".join(fig(x) for x in A["imgs"])}</div></div>')
    return ''.join(o)


def statuses():
    S = C.STATUS
    a = '<span class="sa">→</span>'.join(f'<span class="st" style="--sc:{c}">{L(v, e)}</span>' for v, e, c in S['main'])
    b = ''.join(f'<span class="st" style="--sc:{c}">{L(v, e)}</span>' for v, e, c in S['side'])
    return f'<div class="stl">{a}</div><div class="stl2">{b}<span class="stn">{LP(S["note"])}</span></div>'


def ai():
    q = ''.join(f'<tr><td><span class="chip" style="--rc:{ROLE[r]["color"]}">{LP(ROLE[r]["short"])}</span></td><td>{LP(t)}</td><td><button class="cpy" data-copy="{html.escape(t[0])}">{L("Chép", "Copy")}</button></td></tr>' for r, t in C.AI_QS)
    A = C.AIMAP
    mp = ''.join(f'<div><h5>{LP(t)}</h5><p>{LP(d)}</p></div>' for t, d in A['map'])
    figs = ''.join(fig(k, cap) for k, cap in A['figs'])
    return (f'<div class="aimap">{mp}</div><div class="g2">{figs}</div>'
            f'<h4>{L("Câu hỏi mẫu theo vai trò", "Sample prompts by role")}</h4><div class="tblw"><table class="aiq">{q}</table></div>'
            f'<h4>{L("5 nguyên tắc", "5 rules")}</h4><ol class="rules">{"".join(f"<li>{LP(r)}</li>" for r in A["rules"])}</ol>')


def issues():
    chips = f'<button class="if on" data-r="">{L("Tất cả", "All")}</button>' + ''.join(f'<button class="if" data-r="{r["id"]}" style="--rc:{r["color"]}">{LP(r["short"])}</button>' for r in C.ROLES)
    cards = []
    for i in C.ISSUES:
        rc = ''.join(f'<span class="chip" style="--rc:{ROLE[k]["color"]}">{LP(ROLE[k]["short"])}</span>' for k in i['roles'])
        idx = nodia(' '.join([i['q'][0], i['q'][1], i['cause'][0], i['fix'][0], i['kw'], i['tag'][0]]))
        cause = '' if i['cause'][0] == '—' else f'<p><b>{L("Nguyên nhân:", "Cause:")}</b> {LP(i["cause"])}</p>'
        qi = nodia(i['q'][0] + ' ' + i['q'][1] + ' ' + i['kw'])
        tgt = i['step']
        lk = L('Xem hướng dẫn', 'See guide') + f' {tgt} →'
        cards.append(f'''<details class="iss" id="{i["id"]}" data-roles="{" ".join(i["roles"])}" data-idx="{html.escape(idx)}" data-q="{html.escape(qi)}">
<summary><span class="itag">{LP(i["tag"])}</span><span class="iq">{LP(i["q"])}</span>{rc}</summary>
<div class="ib"><div>{cause}<p class="fix"><b>{L("Cách xử lý:", "Fix:")}</b> {LP(i["fix"])}</p>
<p class="ilk"><a href="#{tgt}">{lk}</a></p></div>{fig(i["img"])}</div></details>''')
    ph = C.PAGE.get('issph', ('Gõ vấn đề, vd: không thấy nút Trình ký, lỗi mã đặt trường…', 'Type a problem, e.g. no Trình ký button, anchor error…'))
    return (f'<div class="isbar"><input id="isq" type="search" placeholder="{ph[0]}" data-ph-en="{ph[1]}" autocomplete="off">'
            f'<div class="ifs">{chips}</div><span id="iscnt"></span></div><div id="isl">{"".join(cards)}</div>'
            f'<p id="isnone" hidden>{L("Không thấy tình huống phù hợp. Thử từ khác, hoặc liên hệ Quản trị app.", "No match. Try other words or contact the app admin.")}</p>')


def setup():
    o = []
    for s in C.SETUP:
        if s.get('h'):
            o.append(f'<h4 class="suh">{LP(s["h"])}</h4>')
            continue
        o.append(f'<div class="su" id="{s["id"]}"><div class="sut"><span class="sid">{s["id"]}</span><h4>{LP(s["title"])}</h4>{pins(L(s["body"][0], s["body"][1], "p"))}</div>{fig(s["img"])}</div>')
    o.append(f'<h4>{LP(C.PAGE["checklist"])}</h4><ul class="chk">' + ''.join(f'<li>{LP(c)}</li>' for c in C.CHECKLIST) + '</ul>')
    return ''.join(o)


def toc():
    P = C.PAGE
    parts = [
        ('I', '#2563eb', ('Tổng quan', 'Overview'), [('s-flow', P['t_flow']), ('s-status', P['t_status']), ('s-ben', P['t_ben'])]),
        ('II', '#0e9f6e', ('Hướng dẫn chi tiết', 'Step-by-step'), [('s-matrix', P['t_matrix'])] + [(s['id'], (f'{s["id"]} · ' + s['title'][0], f'{s["id"]} · ' + s['title'][1])) for s in C.STEPS] + [('s-ai', P['t_ai'])]),
        ('III', '#e5383b', ('Gặp vấn đề?', 'Troubleshooting'), [('s-iss', P['t_iss'])]),
        ('IV', '#7c3aed', ('Setup cho Quản trị', 'Admin setup'), [(s['id'], (f'{s["id"]} · ' + s['title'][0], f'{s["id"]} · ' + s['title'][1])) for s in C.SETUP if not s.get('h')]),
    ]
    o = []
    for n, c, t, items in parts:
        li = ''.join(f'<a href="#{a}">{LP(b)}</a>' for a, b in items)
        o.append(f'<details open class="tp" style="--pc:{c}"><summary><b>{n}</b> {LP(t)}</summary>{li}</details>')
    return ''.join(o)


def band(n, title, sub):
    return f'<div class="part"><span class="eyebrow">{L("PHẦN", "PART")} {n}</span><h2>{LP(title)}</h2><p>{LP(sub)}</p></div>'


def h3lead(t, lead):
    return f'<h3>{LP(t)}</h3>' + (f'<p class="lead">{LP(lead)}</p>' if lead else '')


def hero():
    P = C.PAGE
    kp = ''.join(f'<div><b>{b}</b>{LP(t)}</div>' for b, t in P['kpi']).replace('{{nimg}}', str(len(_IMG))).replace('{{niss}}', str(len(C.ISSUES)))
    from PIL import Image
    hw, hh = Image.open(os.path.join(WEB, P['hero_img'] + '.webp')).size
    return (f'<section class="hero" id="hero"><div><span class="eyebrow">{LP(P["eyebrow"])}</span><h2>{LP(P["hero_h"])}</h2>'
            f'<p class="lead">{LP(P["hero_lead"])}</p>'
            f'<div class="ctas"><a class="btn pri" href="#s-flow">{L("Xem Lưu Đồ", "See The Flow")}</a><a class="btn" href="#s-matrix">{L("Tìm việc của bạn", "Find your part")}</a>'
            f'<a class="btn" href="#s-iss">{L("Gặp vấn đề?", "Stuck?")}</a></div><div class="kpi">{kp}</div></div>'
            f'<div class="mock"><div class="win"><i></i><i></i><i></i></div><img data-k="{P["hero_img"]}" width="{hw}" height="{hh}" alt="hero" data-zoom>'
            f'<div class="float"><i></i>{LP(P["hero_float"])}</div></div></section>')


def main():
    t = open(os.path.join(HERE, 'template.html'), encoding='utf-8').read()
    P = C.PAGE
    img_uri(P['hero_img'])
    R = {
        '{{toc}}': toc(), '{{flow}}': flow(), '{{status}}': statuses(), '{{ben}}': benefits(), '{{matrix}}': matrix(),
        '{{rail}}': rail(), '{{jnav}}': jnav(), '{{steps}}': steps_html(), '{{ai}}': ai(), '{{issues}}': issues(), '{{setup}}': setup(),
        '{{band1}}': band('I', ('Tổng quan', 'Overview'), P['band1']),
        '{{band2}}': band('II', ('Hướng dẫn chi tiết', 'Step-by-step guide'), P['band2']),
        '{{band3}}': band('III', ('Gặp vấn đề?', 'Troubleshooting'), P['band3']),
        '{{band4}}': band('IV', ('Setup cho Quản trị app', 'Admin setup'), P['band4']),
        '{{P:sflow}}': h3lead(P['t_flow'], P['l_flow']) + '<div class="flowbox">',
        '{{P:flowcards}}': '<div class="cards3">' + ''.join(f'<div><b>{LP(a)}</b>{LP(b)}</div>' for a, b in P['flowcards']) + '</div>',
        '{{P:sstatus}}': h3lead(P['t_status'], P.get('l_status')),
        '{{P:sben}}': h3lead(P['t_ben'], P['l_ben']),
        '{{P:smatrix}}': h3lead(P['t_matrix'], (('Bấm tên vai trò để chọn (nhớ cho lần sau). Bấm cột B để tới bước.', 'Click a role to select it (remembered). Click a B column to jump.'))),
        '{{P:sai}}': h3lead(P['t_ai'], P.get('l_ai')),
        '{{P:siss}}': h3lead(P['t_iss'], (('Gõ triệu chứng (không cần dấu), lọc theo vai trò, bấm để mở cách xử lý kèm ảnh.', 'Type the symptom, filter by role, open for the fix with a screenshot.'))),
        '{{P:ssetup}}': h3lead(P['t_setup'], P['l_setup']),
        '{{P:footer}}': LP(P['footer']), '{{P:h1}}': LP(P['h1']), '{{P:title}}': P['title'][0],
        '{{app}}': P['app'],
    }
    R['{{hero}}'] = hero()
    t = t.replace('{{hero}}', R.pop('{{hero}}'))
    RM = {'map': C.RMAP, 'steps': [s['id'] for s in C.STEPS], 'colors': {r['id']: r['color'] for r in C.ROLES},
          'rdo': {k: {r: v[0] for r, v in d.items()} for k, d in C.RDO.items()}, 'rdoen': {k: {r: v[1] for r, v in d.items()} for k, d in C.RDO.items()}}
    for k, v in R.items():
        t = t.replace(k, v)
    t = t.replace('{{rolemap}}', json.dumps(RM, ensure_ascii=False))
    t = t.replace('{{imgs}}', json.dumps(_IMG).replace('</', '<\\/'))
    left = re.findall(r'\{\{(?:P:)?[a-z0-9]+\}\}', t)
    assert not left, left
    out = os.path.join(HERE, '..', P['app'])
    os.makedirs(out, exist_ok=True)
    open(os.path.join(out, 'index.html'), 'w', encoding='utf-8').write(t)
    print(P['app'], 'size MB', round(len(t.encode()) / 1e6, 2), 'imgs', len(_IMG))


if __name__ == '__main__':
    main()
