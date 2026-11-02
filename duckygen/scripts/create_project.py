#!/usr/bin/env python3
"""Create a portable 16:9 sketch-film authoring scaffold, never a finished explainer."""
import argparse,base64,html,json,subprocess,shutil
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
def main():
 p=argparse.ArgumentParser(description=__doc__);p.add_argument('--output',type=Path,required=True);p.add_argument('--title',required=True);p.add_argument('--duration',type=float,default=180);p.add_argument('--bpm',type=float,default=120);p.add_argument('--mode',choices=['explainer','beat-led'],default='explainer');p.add_argument('--assets',nargs='+',default=['props/document-page','props/server-rack','props/browser-window','icons/shield','icons/key','connectors/arrow-curve-right']);p.add_argument('--font',default='manrope',help='Primary family ID from assets/fonts/families.json');p.add_argument('--heading-font',help='Optional headline family ID');p.add_argument('--accent-font',help='Optional code/data or annotation family ID');p.add_argument('--channel-logo-asset',default='logos/channel-sample',help='Cached channel logo ID; empty string omits it');a=p.parse_args()
 if not 1<=a.duration<=7200 or abs(a.duration*60-round(a.duration*60))>.0001:p.error('Use 1–7200 seconds aligned to 60fps.')
 if not 30<=a.bpm<=240:p.error('Use 30–240 BPM.')
 out=a.output.resolve()
 if out.is_relative_to(ROOT):p.error('Create output outside the skill package.')
 if out.exists() and any(out.iterdir()):p.error('Output must be a new or empty folder.')
 out.mkdir(parents=True,exist_ok=True)
 # The sample needs these two props; explicitly include rather than load the whole bank.
 families={x['id']:x for x in json.loads((ROOT/'assets/fonts/families.json').read_text())['families']}
 roles={'body':a.font,'heading':a.heading_font or a.font}
 if a.accent_font:roles['accent']=a.accent_font
 for slug in roles.values():
  if slug not in families:p.error('Unknown font family '+slug+'; choose '+', '.join(families))
 font_ids=list(dict.fromkeys(identity for slug in roles.values() for identity in families[slug]['asset_ids']))
 ids=list(dict.fromkeys(a.assets+['props/document-page','props/server-rack']+font_ids+([a.channel_logo_asset] if a.channel_logo_asset else [])))
 subprocess.run(['python3',str(ROOT/'scripts/asset_tool.py'),'copy',*ids,'--project',str(out)],check=True)
 items=json.loads((ROOT/'assets/index.json').read_text())['items'];bank={}
 for identity in ids:
  item=next(x for x in items if x['id']==identity)
  mime={'.svg':'image/svg+xml','.png':'image/png','.jpg':'image/jpeg','.jpeg':'image/jpeg','.webp':'image/webp'}.get(Path(item['path']).suffix.lower())
  if mime:bank[identity]='data:'+mime+';base64,'+base64.b64encode((ROOT/'assets'/item['path']).read_bytes()).decode()
 font='';font_checks=[];typography={}
 for identity in font_ids:
  item=next(x for x in items if x['id']==identity);encoded=base64.b64encode((ROOT/'assets'/item['path']).read_bytes()).decode();lo=item['weight_min'];hi=item['weight_max'];weight=str(lo) if lo==hi else f'{lo} {hi}'
  font+=f'@font-face{{font-family:"{item["family"]}";src:url(data:font/ttf;base64,{encoded});font-weight:{weight};font-style:normal;font-display:block}}'
  font_checks.append({'family':item['family'],'weight':lo})
 for role,slug in roles.items():
  target=500 if role=='body' else 800
  candidates=[x for x in items if x['id'] in families[slug]['asset_ids']]
  choices=[max(x['weight_min'],min(target,x['weight_max'])) for x in candidates]
  typography[role]={'family':families[slug]['family'],'weight':min(choices,key=lambda w:abs(w-target))}
 (out/'typography.json').write_text(json.dumps({'roles':typography,'family_ids':roles,'font_asset_ids':font_ids},indent=2))
 cfg={'title':a.title,'duration':a.duration,'bpm':a.bpm,'isDemo':True,'loop':False,'reviewMode':'beats' if a.mode=='beat-led' else 'shots','mode':a.mode,'palette':json.loads((ROOT/'assets/palette.json').read_text()),'typography':typography,'fontChecks':font_checks,'channelLogoAsset':a.channel_logo_asset or None}
 shots=[{'id':f'demo-{i}','start':i*a.duration/3,'end':(i+1)*a.duration/3,'spoken_idea':'AUTHORING DEMO — replace with researched spoken idea','asset_ids':[ids[0]]} for i in range(3)]
 data={'config':cfg,'assets':bank,'shots':shots,'captions':[]}
 body='''<!doctype html><html><head><meta charset="utf-8"><title>__TITLE__</title><style>__FONT__
html,body{margin:0;width:100%;height:100%;overflow:hidden;background:#FAF9F6;color:#292C27;font-family:"__BODYFONT__"}body{display:flex;flex-direction:column}canvas{width:100%;height:100%;object-fit:contain;min-height:0}#controls{display:none;height:68px;flex:none;align-items:center;gap:18px;padding:0 25px;background:#FAF9F6;font:16px "__BODYFONT__"}body.player #controls{display:flex}body.player canvas{height:calc(100% - 68px)}button{background:#D76A4E;color:#292C27;padding:12px 25px;border:0;border-radius:5px;font:600 16px "__BODYFONT__"}input[type=range]{flex:1;accent-color:#D76A4E}
</style></head><body><canvas id="film" width="1920" height="1080"></canvas><audio id="soundtrack" preload="auto"></audio><div id="controls"><button id="play">Play</button><input id="scrub" type="range" min="0" step=".01"><span id="clock"></span><label><input id="cc" type="checkbox" checked>Captions</label></div><script id="film-data" type="application/json">__DATA__</script><script>__MOTION__\n__SCORE__</script><script>
const data=JSON.parse(document.getElementById('film-data').textContent),config=data.config,canvas=document.getElementById('film'),ctx=canvas.getContext('2d'),images={};let captionsOn=true;
function type(text,x,y,size=70,color=config.palette.ink,align='left',role='heading'){const face=config.typography[role]||config.typography.body;ctx.font=`${face.weight} ${size}px "${face.family}"`;ctx.fillStyle=color;ctx.textAlign=align;ctx.textBaseline='middle';ctx.fillText(text,x,y)}
function drawAsset(id,x,y,w,h,{progress=1,ink}={}){const img=images[id+(ink||'')];if(!img)return;Motion.reveal(ctx,x,y,w,h,progress,()=>ctx.drawImage(img,x,y,w,h))}
// AUTHORING DEMO ONLY. Replace this entire story and all demo text/shot timings.
function drawFilm(t){const section=Math.min(2,Math.floor(t/config.duration*3)),local=t-section*config.duration/3,p=Motion.exp(local/(config.duration/3));
 type('AUTHORING DEMO',110,130,30,config.palette.coral);type(['A document.','A request.','A system.'][section],110,280,110);ctx.save();Motion.camera(ctx,{x:960,y:540,zoom:1+.025*local/(config.duration/3)});
 if(section<2){ctx.save();ctx.translate(1050,570);ctx.rotate(-.04+.08*p);drawAsset('props/document-page',-220,-250,440,500,{progress:Motion.exp(local/.6)});ctx.restore();if(section===1){ctx.strokeStyle=config.palette.coral;ctx.lineWidth=5;ctx.beginPath();ctx.moveTo(300,600);ctx.bezierCurveTo(470,390,650,500,780,590);ctx.stroke()}}
 else{drawAsset('props/server-rack',1050,335,400,500,{progress:Motion.exp(local/.6)});type('REPLACE THE DEMO',110,660,40,config.palette.green)}ctx.restore();}
window.seek=function(t){t=Motion.clamp(Number(t)||0,0,config.duration);ctx.setTransform(1,0,0,1,0,0);ctx.globalAlpha=1;ctx.filter='none';ctx.fillStyle=config.palette.paper;ctx.fillRect(0,0,1920,1080);ctx.save();drawFilm(t);ctx.restore();if(captionsOn){const cue=data.captions.find(x=>x.start<=t&&t<x.end);if(cue){const lines=cue.text.split('\\n');lines.forEach((line,i)=>type(line,960,950+i*45,36,config.palette.ink,'center','body'))}}return t};
window.filmConfig=config;window.filmShots=data.shots;window.renderSoundtrack=()=>composeScore({duration:config.duration,bpm:config.bpm,changes:data.shots.map(x=>x.start),riser:config.mode==='beat-led'});
const voice=document.getElementById('soundtrack'),play=document.getElementById('play'),scrub=document.getElementById('scrub');scrub.max=config.duration;
if(new URLSearchParams(location.search).has('player'))document.body.classList.add('player');
play.onclick=async()=>{if(voice.paused){if(!voice.getAttribute('src'))voice.src='data:audio/wav;base64,'+await renderSoundtrack();if(voice.currentTime>=config.duration-.01)voice.currentTime=0;await voice.play();play.textContent='Pause'}else{voice.pause();play.textContent='Play'}};scrub.oninput=()=>{if(voice.src)voice.currentTime=+scrub.value;seek(+scrub.value)};document.getElementById('cc').onchange=e=>{captionsOn=e.target.checked;seek(+scrub.value)};
function previewLoop(){if(!voice.paused){seek(voice.currentTime);scrub.value=voice.currentTime}document.getElementById('clock').textContent=(+scrub.value).toFixed(1)+' / '+config.duration+'s';requestAnimationFrame(previewLoop)}
window.motionFilmReady=Promise.all([document.fonts.ready,...config.fontChecks.map(f=>document.fonts.load(`${f.weight} 36px "${f.family}"`).then(loaded=>{if(!loaded.length)throw new Error('Font failed to load: '+f.family);return loaded})),...Object.entries(data.assets).flatMap(([id,url])=>(url.startsWith('data:image/svg+xml')?[null,config.palette.coral,config.palette.green]:[null]).map(ink=>new Promise((resolve,reject)=>{const img=new Image();img.onload=()=>{images[id+(ink||'')]=img;resolve()};img.onerror=reject;img.src=ink?'data:image/svg+xml;base64,'+btoa(atob(url.split(',')[1]).replaceAll('#292C27',ink)):url})))]).then(()=>{seek(0);requestAnimationFrame(previewLoop);return true});
</script></body></html>'''
 text=body.replace('__TITLE__',html.escape(a.title)).replace('__FONT__',font).replace('__BODYFONT__',html.escape(typography['body']['family'],quote=True)).replace('__DATA__',json.dumps(data).replace('<','\\u003c')).replace('__MOTION__',(ROOT/'assets/runtime/motion.js').read_text()).replace('__SCORE__',(ROOT/'assets/runtime/score.js').read_text())
 (out/'film.html').write_text(text);(out/'watch.html').write_text('<!doctype html><html><head><title>Film preview</title><style>html,body,iframe{margin:0;width:100%;height:100%;border:0;background:#FAF9F6}</style></head><body><iframe src="film.html?player=1" allow="autoplay"></iframe></body></html>')
 (out/'edit-plan.json').write_text(json.dumps({'duration':a.duration,'shots':shots,'phrases':[]},indent=2));(out/'video.project.json').write_text(json.dumps({'title':a.title,'entry':'film.html','output':'final.mp4','is_demo':True,'duration':a.duration,'width':1920,'height':1080,'fps':60},indent=2))
 print('Created '+str(out)+'/film.html — authoring demo, not a completed narrated video.')
if __name__=='__main__':main()
