#!/usr/bin/env python3
"""Search/verify the bundled Lemo library, or fetch one pinned demo's source only."""
import argparse,concurrent.futures,hashlib,json,pathlib,re,shutil,urllib.request
SKILL=pathlib.Path(__file__).resolve().parents[1];LIB=SKILL/'companions/lemo-opuscar'
def main():
 p=argparse.ArgumentParser(description=__doc__);sp=p.add_subparsers(dest='command',required=True);ls=sp.add_parser('list');ls.add_argument('query',nargs='?',default='');sp.add_parser('verify');f=sp.add_parser('fetch-demo');f.add_argument('slug');f.add_argument('--project',type=pathlib.Path,required=True);a=p.parse_args();meta=json.loads((LIB/'upstream.json').read_text());index=json.loads((LIB/'style-index.json').read_text())
 if a.command=='list':
  terms=a.query.casefold().split();matches=[r for r in index if all(t in ' '.join([r['slug'],r['name'],r['chinese'],r['category']]).casefold() for t in terms)]
  print(json.dumps(matches,indent=2,ensure_ascii=False));return 0
 if a.command=='verify':
  for f,h in meta['files'].items():
   dest=(LIB/f).resolve();assert dest.is_relative_to(LIB.resolve());assert hashlib.sha256(dest.read_bytes()).hexdigest()==h,f
  assert len({r['slug'] for r in index})==len(index)
  for r in index:assert (LIB/r['path']).is_file(),r['slug']
  print(json.dumps(dict(verified=True,upstream_files=len(meta['files']),published_styles=len(index),revision=meta['revision']),indent=2));return 0
 if a.slug not in {r['slug'] for r in index}:p.error('Choose a published slug with the list command.')
 project=a.project.resolve()
 if project.is_relative_to(SKILL.resolve()):p.error('Download reference source into a project, not the installed skill.')
 target=project/'lemo-reference'/a.slug;prefix=f'styles/{a.slug}/demo/';api='https://api.github.com/repos/lemomo-ai/lemo-opuscar/git/trees/'+meta['revision']+'?recursive=1'
 tree=json.load(urllib.request.urlopen(api,timeout=45));assert not tree.get('truncated'),'GitHub tree was truncated'
 extensions={'.md','.js','.mjs','.cjs','.py','.sh','.json','.html','.css','.glsl','.vert','.frag','.txt','.wgsl'}
 selected=[r for r in tree['tree'] if r['type']=='blob' and r['path'].startswith(prefix) and (pathlib.PurePosixPath(r['path']).suffix.lower() in extensions or pathlib.PurePosixPath(r['path']).name.upper() in {'LICENSE','CREDITS','NOTICE'})]
 if not selected:p.error('No demo source files are available at this revision.')
 if sum(r.get('size',0) for r in selected)>50*1024*1024:p.error('Demo source exceeds 50 MiB; choose a narrower technique manually.')
 def fetch(row):
  rel=pathlib.PurePosixPath(row['path'][len(prefix):]);assert not rel.is_absolute() and '..' not in rel.parts
  b=urllib.request.urlopen(f"https://raw.githubusercontent.com/lemomo-ai/lemo-opuscar/{meta['revision']}/{row['path']}",timeout=45).read();assert hashlib.sha1(b'blob '+str(len(b)).encode()+b'\0'+b).hexdigest()==row['sha'];return rel,b
 # Fetch and verify all bytes before writing, so network errors do not leave a
 # reference that falsely appears complete. Existing edited files are preserved.
 with concurrent.futures.ThreadPoolExecutor(max_workers=6) as pool:files=list(pool.map(fetch,selected))
 planned=[]
 for rel,b in files:
  if rel.name in {'AGENTS.md','SKILL.md','CLAUDE.md'}:rel=rel.with_name(rel.stem+'.upstream.md')
  dest=target.joinpath(*rel.parts)
  if not dest.resolve().is_relative_to(target.resolve()):p.error('A reference path escapes the target directory.')
  if dest.exists() and dest.read_bytes()!=b:p.error('Refusing to overwrite edited reference: '+str(dest))
  planned.append((dest,b))
 target.mkdir(parents=True,exist_ok=True);hashes={}
 for dest,b in planned:dest.parent.mkdir(parents=True,exist_ok=True);dest.write_bytes(b);hashes[str(dest.relative_to(target))]=hashlib.sha256(b).hexdigest()
 shutil.copy2(LIB/'upstream/LICENSE',target/'LEMO-CODE-LICENSE.txt')
 (target/'reference-provenance.json').write_text(json.dumps(dict(repository=meta['repository'],revision=meta['revision'],slug=a.slug,files=hashes,scope='Source reference only; no media/runtime/model downloads or execution; inspect before adapting. Individual third-party notices remain applicable.'),indent=2))
 print(f'Fetched {len(files)} pinned source files into {target}; nothing was executed.');return 0
if __name__=='__main__':raise SystemExit(main())
