#!/usr/bin/env python3
"""Validate indexed asset paths, hashes, XML, WAV metadata and required resources."""
from pathlib import Path
import hashlib,json,wave,struct,xml.etree.ElementTree as ET
ROOT=Path(__file__).resolve().parents[1];A=ROOT/'assets'
def main():
 index=json.loads((A/'index.json').read_text());errors=[];ids=set();counts={}
 for item in index['items']:
  identity=item['id'];counts[item['kind']]=counts.get(item['kind'],0)+1
  if identity in ids:errors.append('Duplicate ID: '+identity)
  ids.add(identity);path=(A/item['path']).resolve()
  if not path.is_relative_to(A.resolve()) or not path.is_file():errors.append('Missing/unsafe path: '+identity);continue
  if hashlib.sha256(path.read_bytes()).hexdigest()!=item['sha256']:errors.append('Hash differs: '+identity)
  if not item.get('origin') or not item.get('reuse'):errors.append('Missing provenance: '+identity)
  if item['kind']=='fonts':
   if path.read_bytes()[:4] not in [b'\x00\x01\x00\x00',b'OTTO',b'wOFF',b'wOF2']:errors.append('Invalid font signature: '+identity)
   if not item.get('family') or not 1<=item.get('weight_min',0)<=item.get('weight_max',0)<=1000:errors.append('Invalid font metadata: '+identity)
   if not item.get('license_files'):errors.append('Missing font license: '+identity)
  if path.suffix=='.png':
   header=path.read_bytes()[:24]
   if len(header)<24 or header[:8]!=b'\x89PNG\r\n\x1a\n' or header[12:16]!=b'IHDR':errors.append('Invalid PNG header: '+identity)
   else:
    width,height=struct.unpack('>II',header[16:24])
    if not width or not height or width!=item.get('width',width) or height!=item.get('height',height):errors.append('Invalid PNG dimensions: '+identity)
  for relative in item.get('license_files',[]):
   license_path=(A/relative).resolve()
   if not license_path.is_relative_to(A.resolve()) or not license_path.is_file():errors.append('Missing/unsafe license: '+identity)
  try:
   if path.suffix=='.svg':
    if ET.fromstring(path.read_text()).tag.split('}')[-1]!='svg':errors.append('Not an SVG: '+identity)
   if path.suffix=='.wav':
    with wave.open(str(path)) as w:
     if w.getnframes()<=0 or w.getsampwidth()!=2 or w.getnchannels() not in [1,2]:errors.append('Invalid cue PCM: '+identity)
  except (ET.ParseError,wave.Error) as e:errors.append(identity+': '+str(e))
 for name in ['fonts/OFL.txt','fonts/manrope-normal-500.ttf','fonts/manrope-normal-800.ttf','palette.json','runtime/motion.js','runtime/score.js','catalog.html']:
  if not (A/name).is_file():errors.append('Missing resource: '+name)
 catalog=A/'fonts/families.json'
 if not catalog.is_file():errors.append('Missing font family catalog')
 else:
  for family in json.loads(catalog.read_text())['families']:
   for identity in family['asset_ids']:
    if identity not in ids:errors.append('Font catalog refers to missing asset: '+identity)
 vendor=A/'runtime/vendor/three';provenance=vendor/'provenance.json'
 if provenance.exists():
  for name,sha in json.loads(provenance.read_text())['files'].items():
   f=(vendor/name).resolve()
   if not f.is_relative_to(vendor.resolve()) or not f.is_file() or hashlib.sha256(f.read_bytes()).hexdigest()!=sha:errors.append('Three.js vendor file missing or modified: '+name)
 result={'valid':not errors,'counts':counts,'assets':len(ids),'errors':errors,'limit':'File integrity only; not semantic visual/audio quality.'};print(json.dumps(result,indent=2));return bool(errors)
if __name__=='__main__':raise SystemExit(main())
