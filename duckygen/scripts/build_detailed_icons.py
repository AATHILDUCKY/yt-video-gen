#!/usr/bin/env python3
"""Refine the indexed icon family with layered detail, retaining stable asset IDs."""
from pathlib import Path
import json,hashlib,re,xml.etree.ElementTree as ET
A=Path(__file__).resolve().parents[1]/'assets';INK='#292C27';PAPER='#FAF9F6';CORAL='#D76A4E'
MAPPED={'wallet':'hot-wallet','laptop':'laptop-workstation','server':'server-rack','shield':'security-boundary','file':'document-page','bank':'exchange-building','browser-window':'browser-window','cloud':'cloud-network','cpu-chip':'cpu-processor','database':'database-stack','phone-mobile':'smartphone-device','router-wifi':'network-router','document-stack':'stacked-files','index-cards':'stacked-files','tech-cpu':'cpu-processor','tech-router':'network-router','tech-device-mobile':'smartphone-device','tech-device-desktop':'desktop-computer','tech-shield-check':'security-boundary'}
DETAIL={
 'key':'M7 5A2 2 0 1 0 7 9A2 2 0 1 0 7 5 M15 14L16 13',
 'person':'M9 13Q12 15 15 13 M6 21H18',
 'search':'M4 8Q5 4 9 4 M19 18L21 20',
 'snow':'M12 10L14 12L12 14L10 12Z',
 'lock':'M8 10V7Q8 3 12 3Q16 3 16 7V10 M10 16A2 2 0 1 0 14 16A2 2 0 1 0 10 16',
 'chain':'M5 15L8 12 M17 9L20 6',
 'eye':'M11 10A1.5 1.5 0 1 0 11 13A1.5 1.5 0 1 0 11 10',
 'clock':'M12 3V4 M20 12H21 M12 20V21 M3 12H4',
 'check':'M3 15L8 21 M19 3L22 6',
 'cross':'M3 6L6 3 M18 21L21 18',
 'gate':'M5 6V9 M11 6V9 M19 6V9 M2 19H22',
 'signature':'M3 22H20 M17 7L20 10',
 'globe':'M3 7H21 M3 17H21 M12 2Q5 12 12 22 M12 2Q19 12 12 22',
 'briefcase':'M4 13H20 M10 12V15H14V12',
 'cloud-upload':'M8 17V21 M16 17V21 M10 4H12',
 'cloud-download':'M8 17V21 M16 17V21 M10 4H12',
 'code-brackets':'M3 21H7 M17 3H21',
 'folder':'M4 9H20 M4 18H14',
 'email-envelope':'M4 19L9 14 M20 19L15 14',
 'network-nodes':'M8 11H10 M14 13H16',
 'api-plug':'M5 20H8 M17 4H20',
 'link-broken':'M2 12L5 13 M19 11L22 12',
 'bug-insect':'M9 10H15 M9 14H15 M12 7V19',
 'fingerprint':'M3 20L4 17 M21 4L22 6',
 'warning-triangle':'M6 19H8 M16 19H18',
 'news-page':'M6 6H11V11H6Z M14 6H18 M14 9H18',
 'chart-rise':'M4 17H6 M4 13H6 M4 9H6',
 'chart-bars':'M6 18V20 M12 13V20 M18 8V20',
 'pie-chart':'M5 17L7 15 M17 6L18 4',
 'calendar-date':'M7 12H9 M12 12H14 M7 16H9 M12 16H14',
 'cursor-pointer':'M4 3L4 7',
 'hand-pointer':'M8 18H15 M8 20H15',
 'robot-assistant':'M8 15H16 M8 18H12',
 'brain-network':'M10 8L14 11L11 16',
 'book-open':'M5 7L9 8 M5 11L9 12 M15 8L19 7 M15 12L19 11',
 'filter-funnel':'M7 6H17',
 'play-media':'M4 19H20',
 'headphones-audio':'M5 13V18 M19 13V18',
 'microphone-voice':'M10 6H14 M10 9H14',
 'eye-hidden':'M6 6L8 8 M17 16L19 18',
 'globe-web':'M5 7H19 M5 17H19',
 'battery-energy':'M5 7V17 M20 9V15',
 'package-delivery':'M8 5L17 10 M5 17L8 19',
 'location-pin':'M10 8A2 2 0 1 0 14 8A2 2 0 1 0 10 8',
 'lightbulb-idea':'M9 19H15 M10 22H14',
 'gear-settings':'M11 9A3 3 0 1 0 13 15A3 3 0 1 0 11 9',
 'arrow-transfer':'M4 14H7 M17 10H20',
 'check-circle':'M4 4L6 6 M18 18L20 20',
 'tech-brain':'M10 9L13 12L10 16',
 'tech-api':'M4 21H20',
 'tech-network':'M4 17H20',
 'tech-wifi':'M10 21H14',
 'tech-device-sd-card':'M9 5V9 M12 5V9 M15 5V9',
 'tech-device-usb':'M9 17H15',
 'tech-lock':'M10 15V18 M14 15V18',
 'tech-key':'M4 8A1.5 1.5 0 1 0 7 8A1.5 1.5 0 1 0 4 8',
 'tech-fingerprint':'M4 20L5 18',
 'tech-code':'M4 21H8 M16 3H20',
 'tech-terminal':'M15 17H20',
 'tech-git-branch':'M7 8V10 M7 16V18',
 'tech-brand-open-source':'',
 'tech-cloud-upload':'M4 20H7',
 'tech-cloud-download':'M17 20H20',
 'tech-automation':'M4 5L6 7 M18 17L20 19',
 'tech-chart-line':'M4 17H6 M4 13H6',
 'tech-mail':'M4 18L8 14 M20 18L16 14',
 'tech-search':'M5 9Q5 5 9 5'
}
def main():
 index=json.loads((A/'index.json').read_text());paths=json.loads((A/'vector-paths.json').read_text());count=0
 for item in index['items']:
  if item['kind']!='icons':continue
  name=item['id'].split('/',1)[1]
  if name in MAPPED:
   source=ET.fromstring((A/'props'/(MAPPED[name]+'.svg')).read_text())
   for element in source.iter():
    if 'id' in element.attrib:element.set('id','object-'+element.get('id'))
    if 'stroke-width' in element.attrib:element.set('stroke-width',str(float(element.get('stroke-width'))*1.65))
   inside=''.join(ET.tostring(e,encoding='unicode') for e in source);body=f'<svg x="5" y="7" width="118" height="112" viewBox="{source.attrib["viewBox"]}">{inside}</svg>';detail='';accent=''
  else:
   if name in paths:geometry='<path d="'+paths[name]+'"/>'
   else:
    source=A/'sources/tabler'/(name.removeprefix('tech-')+'.svg');root=ET.fromstring(source.read_text());geometry=''.join(ET.tostring(e,encoding='unicode') for e in root)
   body=f'<svg x="10" y="10" width="108" height="108" viewBox="-3 -3 30 30" fill="none" stroke="{INK}" stroke-width="1.55">{geometry}</svg>'
   extra=DETAIL.get(name,'');detail=f'<svg x="10" y="10" width="108" height="108" viewBox="-3 -3 30 30" fill="none" stroke="{CORAL}" stroke-width=".85"><path d="{extra}"/></svg>' if extra else '';accent=''
  svg=f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 128 128" fill="none" stroke-linecap="round" stroke-linejoin="round" data-duckygen-style="detailed-editorial-icon-v3"><g id="shadow"/><g id="body">{body}</g><g id="detail">{detail}</g><g id="accent">{accent}</g></svg>'
  root=ET.fromstring(svg);ids=[e.get('id') for e in root.iter() if e.get('id')];assert len(ids)==len(set(ids)),name
  f=A/item['path'];f.write_text(svg);item.update(sha256=hashlib.sha256(f.read_bytes()).hexdigest(),style_revision=3,style='detailed-editorial-icon-v3',layers=['shadow','body','detail','accent'],coordinate_space=[128,128]);item['tags']=list(dict.fromkeys(item['tags']+['detailed','layered','video']))
  if name in MAPPED:
   item['origin']='Original Duckygen detailed icon derived from the matching original layered prop: '+MAPPED[name]
   item['derived_from']='props/'+MAPPED[name];item['reuse']='Original artwork; reusable in generated projects without attribution'
   for key in ['source_url','download_url','upstream_revision','original_sha256','license_files']:item.pop(key,None)
  elif name in paths:
   item['origin']='Original Duckygen icon geometry; Duckygen v3 detail pass';item.pop('derived_from',None)
  elif 'Duckygen v3 detail pass' not in item['origin']:item['origin']+='; Duckygen v3 detail pass'
  count+=1
 (A/'index.json').write_text(json.dumps(index,indent=2)+'\n');print('Refined',count,'icons with stable IDs and layered detail.')
if __name__=='__main__':main()
