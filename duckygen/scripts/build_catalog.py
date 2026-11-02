#!/usr/bin/env python3
"""Refresh the lazy-loading visual/audio catalog without regenerating any assets."""
from pathlib import Path
import json,html
ROOT=Path(__file__).resolve().parents[1];A=ROOT/'assets';escape=html.escape
def main():
 items=json.loads((A/'index.json').read_text())['items'];groups={}
 for item in items:groups.setdefault(item['kind'],[]).append(item)
 body=[]
 for kind,assets in groups.items():
  body.append('<h2>'+escape(kind)+f' ({len(assets)})</h2><main>')
  for x in assets:
   identity=escape(x['id']);path=escape(x['path'],quote=True)
   if kind=='fonts':media='<p>'+escape(x['family'])+'</p>'
   elif kind=='sfx':media=f'<audio controls preload="none" src="{path}"></audio>'
   else:media=f'<img loading="lazy" src="{path}" alt="{identity}">'
   body.append('<figure data-search="'+escape(' '.join([x['id'],*x.get('tags',[])]).lower(),quote=True)+'">'+media+'<figcaption>'+identity+'</figcaption><small>'+escape(x.get('reuse',''))+'</small></figure>')
  body.append('</main>')
 text='''<!doctype html><meta charset="utf-8"><title>Duckygen asset library</title><style>body{margin:30px;background:#FAF9F6;color:#292C27;font:16px sans-serif}input{padding:12px;width:min(600px,80%);font:inherit}main{display:grid;grid-template-columns:repeat(auto-fit,minmax(190px,1fr));gap:18px}figure{margin:0;padding:12px;border-bottom:2px solid #D76A4E;min-width:0}img{width:100%;height:150px;object-fit:contain}audio{width:100%}figcaption{margin:12px 0;overflow-wrap:anywhere}small{font-size:11px;opacity:.75}figure[hidden]{display:none}</style><h1>Duckygen · reusable asset library</h1><p>Palette-matched drawings, contextual photos, licensed sounds and fonts. Use only relevant assets; preserve selected source/license records.</p><input aria-label="Filter assets" placeholder="Search actor, server, paper, click…" oninput="document.querySelectorAll('figure').forEach(f=>f.hidden=!f.dataset.search.includes(this.value.toLowerCase()))">'''+''.join(body)
 (A/'catalog.html').write_text(text);print('Catalog refreshed:',len(items),'indexed assets; no artwork/audio regenerated.')
if __name__=='__main__':main()
