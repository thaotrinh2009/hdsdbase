const { chromium } = require('playwright');
(async () => {
  const b = await chromium.launch(); const out=[];
  for (const app of ['eoffice','bpm','esign']) {
    const f='file://'+__dirname+'/../'+app+'/index.html';
    for (const [w,h,name,theme] of [[1440,900,'d','light'],[390,844,'m','light'],[1440,900,'dk','dark']]) {
      const p = await b.newPage({viewport:{width:w,height:h}, colorScheme: theme});
      const errs=[]; p.on('pageerror',e=>errs.push(e.message));
      await p.goto(f); await p.addStyleTag({content:'html{scroll-behavior:auto!important}'}); await p.waitForTimeout(700);
      const ov = await p.evaluate(()=>document.documentElement.scrollWidth-innerWidth);
      const bg = await p.evaluate(()=>getComputedStyle(document.body).backgroundColor);
      out.push([app,name,'overflow',ov,'bg',bg,'errs',errs.join('|')]);
      const S=async(id,fn)=>{await p.evaluate(i=>document.getElementById(i).scrollIntoView(),id);await p.waitForTimeout(250);await p.screenshot({path:`${__dirname}/qa/${app}_${name}_${fn}.png`})};
      await p.screenshot({path:`${__dirname}/qa/${app}_${name}_top.png`});
      if(name==='d'){
        await S('s-flow','flow'); await S('s-status','status');
        await p.evaluate(()=>document.getElementById('s-matrix').scrollIntoView()); await p.click('.mxr >> nth=1'); await p.waitForTimeout(250); await p.screenshot({path:`${__dirname}/qa/${app}_d_matrix.png`});
        await S(app==='bpm'?'B3':'B4','step');
        await p.evaluate(()=>document.getElementById('s-iss').scrollIntoView()); await p.fill('#isq', app==='bpm'?'khong thay nut trinh ky':'ma dat truong'); await p.waitForTimeout(300); await p.screenshot({path:`${__dirname}/qa/${app}_d_iss.png`});
        out.push([app,'iss', await p.textContent('#iscnt'), await p.evaluate(()=>[...document.querySelectorAll('.iss:not([hidden]) .iq .vi')].slice(0,2).map(x=>x.textContent))]);
        await S('s-setup','setup');
        await p.click('#langB'); await p.waitForTimeout(300);
        const vi = await p.evaluate(()=>{const re=/[ăâđêôơưạảấầẩẫậắằẳẵặẹẻẽếềểễệỉịọỏốồổỗộớờởỡợụủứừửữựỳỵỷỹ]/i;let c=[];const w=document.createTreeWalker(document.body,NodeFilter.SHOW_TEXT);let n;while(n=w.nextNode()){const el=n.parentElement;if(!el||el.closest('script,style'))continue;if(!el.getClientRects().length)continue;if(getComputedStyle(el).display==='none')continue;if(re.test(n.textContent))c.push(n.textContent.trim().slice(0,50))}return c});
        out.push([app,'vi in EN', vi.length, vi.slice(0,60)]);
      }
      await p.close();
    }
  }
  console.log(JSON.stringify(out,null,1)); await b.close();
})();
