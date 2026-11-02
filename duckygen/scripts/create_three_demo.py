#!/usr/bin/env python3
"""Create a self-contained silent 3D authoring example, never a completed news video."""
from pathlib import Path
import argparse,json,base64,shutil
ROOT=Path(__file__).resolve().parents[1]
def main():
 p=argparse.ArgumentParser(description=__doc__);p.add_argument('--output',type=Path,required=True);a=p.parse_args();out=a.output.resolve()
 if out.is_relative_to(ROOT):p.error('Create the demo outside the skill package.')
 if out.exists() and any(out.iterdir()):p.error('Use a new or empty folder.')
 out.mkdir(parents=True,exist_ok=True)
 vendor=ROOT/'assets/runtime/vendor/three';info=json.loads((vendor/'provenance.json').read_text());module=(vendor/info['module']).read_text();core=(vendor/info['core']).read_text();helper=(ROOT/'assets/runtime/three-visualizer.mjs').read_text()
 data={'module':module,'core':core,'helper':helper,'coreName':info['core']}
 font=base64.b64encode((ROOT/'assets/fonts/manrope-normal-800.ttf').read_bytes()).decode()
 html='''<!doctype html><meta charset="utf-8"><title>Duckygen 3D mechanism example</title><style>@font-face{font-family:Manrope;src:url(data:font/ttf;base64,__FONT__);font-weight:800}html,body{margin:0;background:#FAF9F6}canvas{width:100vw;height:100vh;object-fit:contain}</style><canvas id="film" width="1920" height="1080"></canvas><script id="modules" type="application/json">__DATA__</script><script>
window.filmConfig={duration:8,bpm:96,isDemo:true,reviewMode:'shots'};window.filmShots=[{start:0,end:3.6,id:'blocked'},{start:3.6,end:8,id:'authorized'}];
window.motionFilmReady=(async()=>{const data=JSON.parse(document.getElementById('modules').textContent);const url=s=>URL.createObjectURL(new Blob([s],{type:'application/javascript'}));const coreUrl=url(data.core);const mod=data.module.replaceAll('./'+data.coreName,coreUrl);const THREE=await import(url(mod));const {createAuthorizationVisualization}=await import(url(data.helper));const viz=createAuthorizationVisualization(THREE);await document.fonts.load('800 32px Manrope');const c=document.getElementById('film'),ctx=c.getContext('2d');
 window.seek=t=>{const state=viz.seek(t);ctx.fillStyle='#FAF9F6';ctx.fillRect(0,0,1920,1080);ctx.drawImage(viz.canvas,0,0);ctx.font='800 62px Manrope';ctx.fillStyle='#292C27';ctx.fillText('Authorization controls the next step.',110,130);ctx.font='800 26px Manrope';ctx.fillStyle='#D76A4E';ctx.fillText('ILLUSTRATIVE AUTHORIZATION FLOW',110,185);ctx.font='800 32px Manrope';ctx.fillStyle='#292C27';ctx.textAlign='center';ctx.fillText('CLIENT',state.labels.client,875);ctx.fillText('AUTHORIZATION',state.labels.authorization,875);ctx.fillText('SERVER',state.labels.server,875);ctx.font='800 38px Manrope';ctx.fillText(state.phase==='blocked'?'An unapproved request stops at the boundary.':state.phase==='received'?'The approved request reaches the server.':'After approval, the gate permits this request.',960,950);ctx.textAlign='left';return t};window.seek(0);return true})();</script>'''
 html=html.replace('__FONT__',font).replace('__DATA__',json.dumps(data).replace('<','\\u003c'));(out/'film.html').write_text(html)
 shutil.copy2(vendor/'LICENSE.txt',out/'THREE-LICENSE.txt');shutil.copy2(ROOT/'assets/fonts/OFL.txt',out/'FONT-OFL.txt');(out/'README.md').write_text('Silent 8-second authoring example. Not a completed video. Exposes window.seek(t) and motionFilmReady. Open film.html via a local server or the bundled renderer. Replace this illustrative mechanism with the actual researched explanation; retain Three.js/font licenses. No narration or music is included.\n');print('Created self-contained Three.js authoring example:',out)
if __name__=='__main__':main()
