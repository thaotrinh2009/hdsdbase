import pytesseract, json, os, sys
from PIL import Image
from concurrent.futures import ProcessPoolExecutor
HERE=os.path.dirname(os.path.abspath(__file__)); RAW=os.path.join(HERE,'raw'); OUT=os.path.join(HERE,'ocr')
os.makedirs(OUT,exist_ok=True)
def run(f):
    k=f.rsplit('.',1)[0]; p=os.path.join(OUT,k+'.json')
    if os.path.exists(p): return k
    im=Image.open(os.path.join(RAW,f)).convert('L'); im=im.resize((im.width*2,im.height*2),Image.LANCZOS)
    d=pytesseract.image_to_data(im,lang='vie',config='--psm 11',output_type=pytesseract.Output.DICT)
    w=[(d['text'][i],d['left'][i]//2,d['top'][i]//2,(d['left'][i]+d['width'][i])//2,(d['top'][i]+d['height'][i])//2,d['block_num'][i],d['line_num'][i]) for i in range(len(d['text'])) if d['text'][i].strip()]
    json.dump(w,open(p,'w'),ensure_ascii=False); return k
fs=sorted(os.listdir(RAW))
with ProcessPoolExecutor(8) as ex:
    for k in ex.map(run,fs): pass
print('done',len(fs))
