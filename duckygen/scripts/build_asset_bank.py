#!/usr/bin/env python3
"""Rebuild this skill's original vector/cue bank; not a per-project dependency."""
from pathlib import Path
import json,hashlib,math,wave,importlib.util
import numpy as np
ROOT=Path(__file__).resolve().parents[1];A=ROOT/'assets'
PALETTE={'paper':'#FAF9F6','ink':'#292C27','coral':'#D76A4E','green':'#17684F'}

def svg(path,view='-2 -2 28 28',accent=''):
 return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="{view}" fill="none" stroke-linecap="round" stroke-linejoin="round"><path d="{path}" stroke="#292C27" stroke-width="1.45"/><path d="{path}" transform="translate(.27 -.17)" stroke="#292C27" stroke-width=".52" opacity=".17"/>{accent}</svg>'''

def main():
 items=[]
 curated={x['id']:x for x in json.loads((A/'index.json').read_text())['items']} if (A/'index.json').exists() else {}
 def add(cat,name,content,tags,ext='svg'):
  directory=A/'soundeffects'/'generated' if cat=='sfx' else A/cat
  f=directory/(name+'.'+ext)
  previous=curated.get(cat+'/'+name)
  if previous and previous.get('style_revision',1)>=2 and f.is_file():
   if hashlib.sha256(f.read_bytes()).hexdigest()!=previous['sha256']:raise ValueError('Curated asset changed; review/update its index before rebuilding: '+str(f))
   items.append(previous);return
  f.parent.mkdir(parents=True,exist_ok=True);f.write_bytes(content if isinstance(content,bytes) else content.encode())
  items.append({'id':cat+'/'+name,'path':str(f.relative_to(A)),'kind':cat,'tags':tags,'palette':list(PALETTE.values()) if ext=='svg' else [],'origin':'Original locally authored duckygen asset','reuse':'Reusable in generated projects; no attribution required for original art/cues','sha256':hashlib.sha256(f.read_bytes()).hexdigest()})
 paths=json.loads((A/'vector-paths.json').read_text())
 for name,d in paths.items():add('icons',name,svg(d),name.replace('-',' ').split()+['sketch','tech'])
 props={
 'document-page':('M20 8L112 11L142 39L139 170L16 166Z M112 11L111 41L142 39 M33 63L118 65 M32 82L113 85 M31 103L120 104 M31 124L95 126 M30 145L117 147','0 0 160 180','document file paper text'),
 'laptop-workstation':('M34 23L169 19L178 122L26 127Z M42 32L162 30L169 114L36 118Z M26 127L178 122L199 151L7 157Z M40 136L167 133 M49 144L159 141 M60 57L137 55 M61 73L148 72 M60 89L119 86','0 0 210 170','laptop computer device workstation'),
 'server-rack':('M43 13L139 17L144 178L35 181Z M51 29L129 32L130 63L48 61Z M47 77L132 79L133 110L45 108Z M43 125L134 126L136 159L42 157Z M61 43L106 44 M58 90L106 91 M56 140L107 141','0 0 180 195','server cloud infrastructure compute'),
 'browser-window':('M9 18L193 14L196 145L8 149Z M9 46L194 44 M22 31L25 31 M36 31L39 31 M50 30L53 30 M28 70L119 67 M27 91L166 87 M28 117L149 114','0 0 210 165','browser web interface window'),
 'hot-wallet':('M18 45L156 39L162 141L17 145Z M18 45L20 24L151 19L156 39 M161 77L122 79L124 113L162 111 M135 96L140 95 M39 67L99 64 M39 85L84 82','0 0 185 170','wallet money crypto funds'),
 'database-stack':('M26 38C25 8 155 8 156 38C155 65 26 66 26 38 M26 38L23 141C24 174 158 175 160 141L156 38 M25 82C27 111 157 109 158 79 M24 119C24 148 159 146 159 116','0 0 185 185','database data storage layers'),
 'cloud-network':('M36 104C-6 106 4 42 47 55C47 -9 141 -4 142 58C194 46 197 111 149 110Z M61 115L60 157 M109 115L110 157 M40 157L78 157 M91 157L130 157','0 0 185 180','cloud network server online'),
 'stacked-files':('M19 41L117 41L120 170L17 169Z M41 23L137 22L139 151 M61 8L157 7L159 132 M34 69L100 70 M34 92L101 92 M33 115L88 114 M33 138L102 139','0 0 180 185','documents stack files knowledge'),
 'security-boundary':('M86 8L151 33L150 89C151 131 119 159 88 177C55 157 26 134 25 91L25 34Z M54 89L79 117L128 57','0 0 180 190','security boundary shield trust'),
 'exchange-building':('M12 63L94 14L180 61Z M14 163L180 161 M27 72L26 151 M63 72L62 151 M101 72L100 151 M140 72L139 151 M176 72L175 151','0 0 195 180','bank exchange funds company building'),
 'phone-notification':('M52 8L131 10L129 178L48 177Z M71 157L107 157 M34 43L149 43L149 100L110 100L94 120L87 100L34 100Z M48 61L131 61 M48 79L115 79','0 0 180 190','phone alert message notification'),
 'timeline-strip':('M10 90L195 89 M25 80L25 100 M80 80L80 100 M135 80L135 100 M190 80L190 100 M25 51L79 50L80 76L24 76Z M100 25L173 25L173 75L100 75Z M29 119L106 120 M29 137L165 137','0 0 210 160','timeline editor sequence time')}
 for name,(d,view,tags) in props.items():add('props',name,svg(d,view),tags.split()+['sketch'])
 conns={
 'arrow-curve-right':'M7 47C24 8 85 6 118 26 M101 9L118 26L97 32',
 'arrow-curve-left':'M119 47C101 8 44 6 10 26 M27 9L10 26L31 32',
 'arrow-straight':'M7 31L119 30 M102 16L119 30L101 46',
 'arrow-down':'M63 5L62 57 M46 40L62 57L79 40',
 'loop-arrow':'M99 38C126 -2 20 -6 16 28C12 57 96 64 99 38 M86 50L99 38L108 54',
 'underline-swoop':'M6 39C35 33 87 32 122 35 M19 43C48 39 79 39 104 42',
 'circle-emphasis':'M111 15C75 -5 13 6 7 31C-2 61 114 66 122 31C126 19 120 11 107 8',
 'bracket-focus':'M28 7L10 9L9 55L29 56 M98 8L118 9L119 55L97 56'}
 for name,d in conns.items():add('connectors',name,svg(d,'0 0 128 64'),name.split('-')+['sketch','motion'])
 spec=importlib.util.spec_from_file_location('audio',ROOT/'scripts/explainer_audio.py');mod=importlib.util.module_from_spec(spec);spec.loader.exec_module(mod)
 cues={'click-soft':'click','tap-contact':'tap','paper-turn':'paper','marker-write':'marker','transition-swipe':'swipe','resolution-chime':'chime'}
 rate=24000
 def wav_bytes(a):
  import io
  out=io.BytesIO();a=mod.fade(a.astype(float),rate)
  a*=.5/max(abs(a).max(),1e-9)
  with wave.open(out,'wb') as w:w.setparams((1,2,rate,0,'NONE',''));w.writeframes((a*32767).astype('<i2').tobytes())
  return out.getvalue()
 for name,kind in cues.items():add('sfx',name,wav_bytes(mod.synth(kind,rate)),[kind,'synthetic','cue'],'wav')
 for name,f0,f1,d in [('zoom-in',180,900,.28),('zoom-out',900,150,.3),('reveal-pop',400,160,.16),('impact-low',95,38,.3)]:
  t=np.arange(round(d*rate))/rate;phase=2*np.pi*(f0*t+(f1-f0)*t*t/(2*d));a=np.sin(phase)*np.sin(np.pi*t/d)**2*np.exp(-t*(9 if name=='impact-low' else 4));add('sfx',name,wav_bytes(a),name.split('-')+['synthetic','cue'],'wav')
 known={x['id'] for x in items}
 if (A/'index.json').exists():items += [x for x in json.loads((A/'index.json').read_text())['items'] if x['id'] not in known]
 (A/'palette.json').write_text(json.dumps(PALETTE,indent=2));(A/'index.json').write_text(json.dumps({'version':1,'palette':PALETTE,'items':items},indent=2))
 cards=''.join(f'<figure><img src="{x["path"]}"><figcaption>{x["id"]}</figcaption></figure>' for x in items if x['kind'] not in ['sfx','fonts'])
 soundcards=''.join(f'<p>{x["id"]} <audio controls preload="none" src="{x["path"]}"></audio></p>' for x in items if x['kind']=='sfx')
 (A/'catalog.html').write_text('<!doctype html><meta charset="utf-8"><title>Duckygen original sketch assets</title><style>@font-face{font-family:Manrope;src:url(fonts/manrope-normal-500.ttf)}body{margin:30px;background:#FAF9F6;color:#292C27;font-family:Manrope}h1{font-size:32px}main{display:grid;grid-template-columns:repeat(8,1fr);gap:12px}figure{margin:0;padding:10px;min-height:130px;border-bottom:2px solid #D76A4E}img{width:100%;height:95px}figcaption{font-size:11px;word-break:break-word}</style><h1>Duckygen · original sketch asset library</h1><p>#D76A4E · #292C27 · #FAF9F6 · optional #17684F</p><main>'+cards+'</main><h2>Procedural sound cues</h2>'+soundcards)
 print(json.dumps({'icons':len(paths),'props':len(props),'connectors':len(conns),'sfx':len(cues)+4,'total':len(items)}))
if __name__=='__main__':main()
