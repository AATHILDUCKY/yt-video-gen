#!/usr/bin/env python3
"""Search the small asset index, copy selected files, or cache named reusable assets."""
import argparse,hashlib,json,re,shutil,sys,wave
import xml.etree.ElementTree as ET
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1];BANK=ROOT/'assets';INDEX=BANK/'index.json'
def digest(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def save(path,data):
 temp=path.with_suffix(path.suffix+'.tmp');temp.write_text(json.dumps(data,indent=2));temp.replace(path)
def main():
 p=argparse.ArgumentParser(description=__doc__);sub=p.add_subparsers(dest='action',required=True)
 s=sub.add_parser('search');s.add_argument('query',nargs='?',default='');s.add_argument('--kind');s.add_argument('--limit',type=int,default=8)
 s=sub.add_parser('copy');s.add_argument('ids',nargs='+');s.add_argument('--project',type=Path,required=True)
 s=sub.add_parser('cache');s.add_argument('file',type=Path);s.add_argument('--name',required=True);s.add_argument('--tags',nargs='+',required=True);s.add_argument('--source',required=True);s.add_argument('--license',required=True);s.add_argument('--source-url');s.add_argument('--license-file',type=Path);s.add_argument('--attribution');s.add_argument('--kind',choices=['icons','props','connectors','illustrations','avatars','photos','logos','sfx'],default='illustrations')
 a=p.parse_args();index=json.loads(INDEX.read_text());items=index['items']
 if a.action=='search':
  words=a.query.lower().split();rank=[]
  for item in items:
   hay=' '.join([item['id']]+item['tags']).lower();score=sum(w in hay for w in words)
   if (not a.kind or item['kind']==a.kind) and (not words or score):rank.append((score,item))
  rank.sort(key=lambda x:(-x[0],x[1]['id']));print(json.dumps([{k:i[k] for k in ['id','path','tags']} for _,i in rank[:max(1,min(a.limit,50))]],indent=2));return
 if a.action=='copy':
  selected=[]
  for asset_id in a.ids:
   item=next((x for x in items if x['id']==asset_id),None)
   if not item:raise ValueError('Unknown asset: '+asset_id)
   source=(BANK/item['path']).resolve()
   if not source.is_relative_to(BANK.resolve()) or digest(source)!=item['sha256']:raise ValueError('Asset path/hash mismatch: '+asset_id)
   licenses=[]
   for relative in item.get('license_files',[]):
    license_path=(BANK/relative).resolve()
    if not license_path.is_relative_to(BANK.resolve()) or not license_path.is_file():raise ValueError('Missing/unsafe license: '+asset_id)
    licenses.append((relative,license_path))
   selected.append((item,source,licenses))
  out=a.project.resolve();manifest=out/'asset-manifest.json';records=json.loads(manifest.read_text()) if manifest.exists() else []
  for item,source,licenses in selected:
   target=out/'assets'/item['path'];target.parent.mkdir(parents=True,exist_ok=True)
   if target.exists() and digest(target)!=item['sha256']:raise ValueError('Refusing to overwrite different project asset: '+str(target))
   for relative,license_path in licenses:
    destination=out/'assets'/relative;destination.parent.mkdir(parents=True,exist_ok=True)
    if destination.exists() and digest(destination)!=digest(license_path):raise ValueError('Refusing to overwrite different license: '+str(destination))
    shutil.copy2(license_path,destination)
   shutil.copy2(source,target);record={**item,'project_path':str(target.relative_to(out))};records=[x for x in records if x.get('id')!=item['id']]+[record]
  save(manifest,records);print(json.dumps({'copied':[x[0]['id'] for x in selected],'manifest':str(manifest)}));return
 source=a.file.resolve();suffix=source.suffix.lower()
 if suffix not in ['.svg','.png','.jpg','.jpeg','.webp','.wav']:raise ValueError('Use SVG/PNG/JPEG/WebP/WAV assets.')
 if a.kind=='sfx' and suffix!='.wav':raise ValueError('Cache effects as PCM WAV; decode other formats first.')
 audio={}
 if suffix=='.wav':
  with wave.open(str(source)) as w:
   if w.getnframes()<=0 or w.getsampwidth()!=2 or w.getnchannels() not in [1,2]:raise ValueError('Use nonempty 16-bit mono/stereo PCM WAV.')
   audio={'duration_seconds':round(w.getnframes()/w.getframerate(),6),'sample_rate':w.getframerate(),'channels':w.getnchannels()}
 if a.license_file and not a.license_file.is_file():raise ValueError('License file does not exist.')
 if not re.fullmatch('[a-z0-9]+(?:-[a-z0-9]+)*',a.name):raise ValueError('Use a descriptive lowercase hyphenated name.')
 if suffix=='.svg':
  text=source.read_text()
  try: element=ET.fromstring(text)
  except ET.ParseError as error:raise ValueError('Invalid SVG XML.') from error
  if element.tag.split('}')[-1]!='svg':raise ValueError('Expected an SVG root element.')
  if re.search(r'<script|<foreignObject|(?:href|url)\s*[=:(]\s*[\"\']?https?[:/]|\bon\w+\s*=',text,re.I):raise ValueError('Cache self-contained SVG artwork without scripts or remote references.')
 sha=digest(source);existing=next((x for x in items if x['sha256']==sha),None)
 if existing:print(json.dumps({'reused':existing['id']}));return
 directory=BANK/'soundeffects'/'generated' if a.kind=='sfx' else BANK/a.kind
 name=a.name;target=directory/(name+suffix)
 if target.exists():name+='-'+sha[:8];target=directory/(name+suffix)
 if target.exists() and digest(target)!=sha:raise ValueError('Version-name collision; choose a new name.')
 identity=a.kind+'/'+name
 if any(x['id']==identity for x in items):name+='-'+sha[:8];target=directory/(name+suffix);identity=a.kind+'/'+name
 if any(x['id']==identity for x in items):raise ValueError('Asset ID collision; choose another name.')
 target.parent.mkdir(parents=True,exist_ok=True);shutil.copy2(source,target)
 item={'id':identity,'path':str(target.relative_to(BANK)),'kind':a.kind,'tags':a.tags,'origin':a.source,'reuse':a.license,'palette':[],'sha256':sha,**audio}
 if a.source_url:item['source_url']=a.source_url
 if a.attribution:item['attribution_text']=a.attribution
 if a.license_file:
  lic=BANK/'licenses'/(digest(a.license_file)[:16]+'.txt');lic.parent.mkdir(exist_ok=True);shutil.copy2(a.license_file,lic);item['license_files']=[str(lic.relative_to(BANK))]
 items.append(item);save(INDEX,index);print(json.dumps({'cached':item['id'],'path':str(target)}))
if __name__=='__main__':
 try:main()
 except (ValueError,OSError,KeyError) as e:print(str(e),file=sys.stderr);raise SystemExit(1)
