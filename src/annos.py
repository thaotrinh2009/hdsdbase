# -*- coding: utf-8 -*-
"""Ghim số + khung + làm mờ lên ảnh chụp. Vị trí ghim tìm bằng chữ (OCR cache ở ocr/*.json)
hoặc toạ độ (x0,y0,x1,y1) theo ảnh gốc 1280px.
Spec: A[key] = dict(m=[(1,'Trình ký'), (2,'Gửi ký',2), (3,(x0,y0,x1,y1))], blur=['email', (x0,y0,x1,y1)], S=1.35)"""
from PIL import Image, ImageDraw, ImageFont, ImageFilter
import os, json, re, unicodedata, sys

HERE = os.path.dirname(os.path.abspath(__file__))
RAW = os.path.join(HERE, 'raw')
OUT = os.path.join(HERE, 'img_out')
WEB = os.path.join(HERE, 'web')
FONT = '/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf'
PIN = (0, 71, 204)
BOX = (0, 104, 255)


def nd(s):
    s = unicodedata.normalize('NFD', s.replace('đ', 'd').replace('Đ', 'D'))
    s = ''.join(c for c in s if unicodedata.category(c) != 'Mn').lower()
    return re.sub(r'[^a-z0-9/#+.]', '', s)


_O = {}


def words(key):
    if key not in _O:
        _O[key] = json.load(open(os.path.join(HERE, 'ocr', key + '.json')))
    return _O[key]


def locate(key, phrase, occ=1):
    ws = words(key)
    toks = [nd(t) for t in phrase.split()]
    toks = [t for t in toks if t]
    hits = []
    for i in range(len(ws)):
        ok, j, k, box = True, i, 0, None
        while k < len(toks):
            if j >= len(ws):
                ok = False
                break
            w = nd(ws[j][0])
            if not w:
                j += 1
                continue
            t = toks[k]
            if w == t or (len(t) >= 3 and (w.startswith(t) or t.startswith(w) and len(w) >= 3)) or (k == len(toks) - 1 and w.startswith(t)):
                x0, y0, x1, y1 = ws[j][1:5]
                if box and (abs(y0 - box[1]) > 14 or x0 - box[2] > 40):
                    ok = False
                    break
                box = (x0, y0, x1, y1) if not box else (min(box[0], x0), min(box[1], y0), max(box[2], x1), max(box[3], y1))
                j += 1
                k += 1
            elif box and len(w) <= 2:
                j += 1
            else:
                ok = False
                break
        if ok and box:
            hits.append(box)
    if len(hits) < occ:
        raise KeyError(f'{key}: không thấy "{phrase}" (#{occ}); có {len(hits)}')
    return hits[occ - 1]


def font(sz):
    return ImageFont.truetype(FONT, sz)


def resolve(key, spec, pad=5):
    if isinstance(spec, tuple) and len(spec) == 4 and all(isinstance(v, (int, float)) for v in spec):
        return spec
    if isinstance(spec, str):
        b = locate(key, spec)
    else:
        b = locate(key, spec[0], spec[1])
    return (b[0] - pad, b[1] - pad, b[2] + pad, b[3] + pad)


def render(key):
    a = A.get(key, {})
    src = [f for f in os.listdir(RAW) if f.rsplit('.', 1)[0] == key][0]
    im = Image.open(os.path.join(RAW, src)).convert('RGB')
    for spec in a.get('blur', []):
        b = resolve(key, spec, 2)
        b = tuple(int(v) for v in b)
        reg = im.crop(b).filter(ImageFilter.GaussianBlur(7))
        im.paste(reg, b[:2])
    crop = a.get('crop')
    if crop:
        im = im.crop(crop)
    ox, oy = (crop[0], crop[1]) if crop else (0, 0)
    S = a.get('S', 1.35)
    im = im.resize((int(im.width * S), int(im.height * S)), Image.LANCZOS)
    im = im.filter(ImageFilter.UnsharpMask(radius=1.2, percent=80, threshold=2))
    ov = Image.new('RGBA', im.size, (0, 0, 0, 0))
    d = ImageDraw.Draw(ov)
    f = font(19)
    marks = []
    for m in a.get('m', []):
        n, spec = m[0], m[1] if len(m) == 2 else (m[1], m[2])
        b = resolve(key, spec)
        b = ((b[0] - ox) * S, (b[1] - oy) * S, (b[2] - ox) * S, (b[3] - oy) * S)
        d.rounded_rectangle(b, radius=9, outline=BOX + (230,), width=2, fill=BOX + (16,))
        marks.append((n, b))
    for n, b in marks:
        r = 16
        cx, cy = max(r + 2, b[0] - 4), max(r + 2, b[1] - 4)
        d.ellipse((cx - r - 3, cy - r - 3, cx + r + 3, cy + r + 3), fill=(255, 255, 255, 255))
        d.ellipse((cx - r, cy - r, cx + r, cy + r), fill=PIN + (255,))
        t = str(n)
        w = d.textlength(t, font=f)
        d.text((cx - w / 2, cy - 12), t, font=f, fill=(255, 255, 255, 255))
    im = Image.alpha_composite(im.convert('RGBA'), ov).convert('RGB')
    os.makedirs(OUT, exist_ok=True)
    os.makedirs(WEB, exist_ok=True)
    im.save(os.path.join(OUT, key + '.jpg'), quality=90, subsampling=0, optimize=True)
    im.save(os.path.join(WEB, key + '.webp'), 'WEBP', quality=82, method=6)
    return key, im.size


from annos_spec import A  # noqa: E402

if __name__ == '__main__':
    keys = sys.argv[1:] or sorted(f.rsplit('.', 1)[0] for f in os.listdir(RAW))
    bad = []
    for k in keys:
        try:
            render(k)
        except KeyError as e:
            bad.append(str(e))
    print('ok', len(keys) - len(bad))
    print('\n'.join(bad))
