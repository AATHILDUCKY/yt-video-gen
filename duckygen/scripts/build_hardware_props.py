#!/usr/bin/env python3
"""Build original, palette-matched layered hardware props for Duckygen."""
from pathlib import Path
import json,hashlib,xml.etree.ElementTree as ET
from build_refined_props import path,rect,circle,wrap,INK,PAPER,CORAL,GREEN
A=Path(__file__).resolve().parents[1]/'assets'
def group(name,content):return f'<g id="{name}">{content}</g>'
def ellipse(x,y,rx,ry):return f'<ellipse cx="{x}" cy="{y}" rx="{rx}" ry="{ry}" fill="{INK}"/>'
def screen(x,y,w,h,name='screen'):return group(name,rect(x,y,w,h,PAPER,4))
def slots(x,y,n,width=20):return ''.join(path(f'M{x+i*width} {y}L{x+i*width} {y+10}',width=2) for i in range(n))
def main():
 art={}
 def add(name,body,detail='',accent='',shadow='',tags=(),anchors=None):art[name]=(wrap(body,detail,accent,shadow),list(tags),anchors or {'left':[60,130],'right':[260,130]})
 monitor=rect(42,35,237,153,PAPER,11)+path('M53 47L268 47L268 168L53 168Z',PAPER)+path('M143 188L143 213L116 226L205 226L178 213L178 188Z',CORAL)
 add('desktop-computer',monitor,group('screen',path('M69 149L69 66L139 66',stroke=CORAL,width=5))+group('status-light',circle(259,178,3,GREEN)),path('M55 176L225 176',width=2),ellipse(160,234,102,8),['desktop','computer','monitor','workstation'],{'screen':[160,108],'left':[42,111],'right':[279,111]})
 tower=path('M104 27L215 34L242 54L239 231L101 225Z',PAPER)+path('M215 34L242 54L239 231L214 211Z',CORAL)
 add('computer-tower',tower,group('drive-bays',rect(118,54,79,20,PAPER,3)+rect(118,83,79,20,PAPER,3))+group('vent',path('M120 168L194 168M120 179L194 179M120 190L194 190M120 201L169 201',width=2))+group('power-button',circle(158,131,12,PAPER)+path('M158 120L158 130',stroke=CORAL,width=3)),group('ports',rect(120,151,16,5,INK,1)+rect(145,151,16,5,INK,1)),ellipse(173,239,84,8),['desktop','computer','tower','hardware','pc'],{'left':[101,130],'right':[240,130]})
 dual=group('left-monitor',rect(22,39,130,110,PAPER,7)+screen(31,48,112,82,'left-screen')+path('M77 149L77 172L55 183L120 183L98 172L98 149Z',CORAL))+group('right-monitor',rect(168,39,130,110,PAPER,7)+screen(177,48,112,82,'right-screen')+path('M222 149L222 172L200 183L265 183L243 172L243 149Z',CORAL))
 add('dual-monitor-workstation',dual,group('keyboard',path('M60 204L246 204L264 228L44 228Z',PAPER)+path('M65 213L244 213M61 220L249 220',width=2))+group('screen-markers',path('M46 67L66 67M46 78L111 78M193 67L211 67M193 78L258 78',stroke=CORAL,width=3)),group('mouse',path('M278 207C266 207 266 232 278 232C291 232 291 207 278 207Z',PAPER)+path('M278 208L278 218',width=2)),ellipse(160,239,135,7),['desktop','computer','dual','monitor','workstation','developer'],{'left':[22,96],'right':[298,96]})
 laptop=path('M61 33L260 42L251 172L50 163Z',CORAL)+screen(69,46,178,111)+path('M50 163L251 172L291 219L24 209Z',PAPER)
 keys=''.join(path(f'M{x} 178L{x+10} 196',width=1.7) for x in range(70,251,18))
 add('laptop-open',laptop,group('keyboard',keys+path('M64 185L259 194',width=1.7))+group('trackpad',path('M135 198L187 200L193 210L129 208Z',PAPER)),group('webcam',circle(160,40,2,PAPER))+path('M82 144L139 144',stroke=CORAL,width=4),ellipse(158,229,128,7),['laptop','computer','open','device','screen'],{'screen':[157,101],'left':[51,111],'right':[255,111]})
 add('laptop-closed',path('M40 92L252 64L293 162L74 198L27 111Z',PAPER)+path('M74 198L293 162L293 175L73 213L27 126L27 111Z',CORAL),path('M47 110L242 85M85 199L277 168',width=2)+group('charging-port',path('M49 148L60 169',width=4)),group('lid-detail',path('M150 129L168 126',stroke=CORAL,width=5)),ellipse(164,224,124,8),['laptop','computer','closed','hardware'],{'left':[28,122],'right':[292,170]})
 blade=path('M31 93L242 66L291 100L79 132Z',CORAL)+path('M31 93L79 132L79 194L31 154Z',PAPER)+path('M79 132L291 100L291 162L79 194Z',PAPER)
 fans=''.join(circle(x,154-(x-105)*.15,10,PAPER)+path(f'M{x-5} {154-(x-105)*.15}L{x+5} {154-(x-105)*.15}',width=2) for x in [110,142,174])
 add('server-blade',blade,group('fans',fans)+group('ports',path('M209 132L228 129L228 145L209 148Z',INK)+path('M240 127L260 124L260 140L240 143Z',INK)),group('status-lights',circle(272,147,3,GREEN)),ellipse(170,213,125,10),['server','blade','rack','compute','hosting'],{'input':[260,132],'output':[225,139]})
 racks=''
 for n,x in enumerate([38,123,208]):
  racks+=group('rack-'+str(n+1),rect(x,43,74,177,PAPER,5)+path(f'M{x+60} 44L{x+74} 44L{x+74} 219L{x+60} 219Z',CORAL))
  for y in [59,100,141,182]:racks+=rect(x+10,y,42,26,PAPER,3)+path(f'M{x+17} {y+8}L{x+33} {y+8}M{x+17} {y+16}L{x+30} {y+16}',width=1.6)+circle(x+43,y+14,2.3,GREEN)
 add('data-center-racks',racks,group('floor',path('M22 231L297 231',width=2)),shadow=ellipse(160,237,139,8),tags=['server','data','center','datacenter','racks','infrastructure'],anchors={'left':[38,130],'right':[282,130]})
 router=path('M61 139L231 120L279 163L101 189L54 160Z',PAPER)+path('M101 189L279 163L279 186L101 214L54 184L54 160Z',CORAL)
 add('network-router',router,group('antennas',path('M86 140L72 47Q71 41 77 40Q84 39 85 47L99 139M222 122L234 39Q235 33 241 34Q247 35 246 42L234 128',fill=PAPER))+group('ports',path('M151 190L163 188M178 186L190 184M205 182L217 180',width=4)),group('wireless-signal',path('M128 96Q161 66 194 91M140 108Q161 90 182 105',stroke=CORAL,width=4)),ellipse(167,227,119,8),['router','network','wifi','wireless','internet'],{'left':[57,172],'right':[278,175],'antenna':[161,91]})
 switch=path('M30 91L253 75L291 106L66 128Z',CORAL)+path('M66 128L291 106L291 175L66 200L30 168L30 91Z',PAPER)+path('M30 91L66 128L66 200L30 168Z',CORAL)
 ports=''
 for i in range(7):
  x=83+i*27;y=143-i*2.9;ports+=path(f'M{x} {y}L{x+17} {y-2}L{x+17} {y+16}L{x} {y+18}Z',INK)
 add('network-switch',switch,group('ports',ports),group('status-lights',''.join(circle(91+i*27,178-i*2.9,2.2,GREEN) for i in range(7))),ellipse(170,219,126,8),['switch','network','ethernet','ports','infrastructure'],{'input':[92,151],'output':[254,134]})
 pins=''
 for i in range(6):
  z=106+i*21;pins+=path(f'M{z} 67L{z} 44M{z} 194L{z} 217M91 {80+i*21}L68 {80+i*21}M229 {80+i*21}L252 {80+i*21}',stroke=CORAL,width=5)
 add('cpu-processor',group('pins',pins)+rect(90,66,140,129,PAPER,9)+rect(108,84,104,93,CORAL,4),group('die',rect(127,103,66,55,PAPER,3)+path('M138 116L181 116M138 127L171 127M138 138L181 138',width=2)),shadow=path('M99 75L241 75L241 204L99 204Z',INK),tags=['cpu','processor','chip','silicon','hardware','compute'],anchors={'left':[68,130],'right':[252,130],'top':[160,44]})
 gpu=path('M31 72L265 62L282 88L282 187L33 197Z',CORAL)+path('M40 88L268 80L268 175L41 185Z',PAPER)+path('M73 195L230 189L230 205L74 211Z',PAPER)
 fans=''
 for x in [107,210]:fans+=circle(x,135,35,PAPER)+circle(x,135,9,CORAL)+path(f'M{x} 105L{x+8} 126M{x+27} 147L{x+8} 139M{x-25} 152L{x-8} 140M{x-21} 114L{x-7} 128',width=3)
 add('gpu-card',gpu,group('fans',fans)+group('edge-connector',slots(82,197,8,18)),path('M32 69L22 69L22 213L38 213',width=5),ellipse(160,228,135,8),['gpu','graphics','card','hardware','ai','compute'],{'left':[22,141],'right':[282,139]})
 drive=path('M84 43L212 43L237 67L237 217L83 217Z',PAPER)+path('M212 43L237 67L237 217L212 200Z',CORAL)
 add('external-drive',drive,group('platter',circle(151,122,46,PAPER)+circle(151,122,16,CORAL))+group('read-arm',path('M184 170L154 126L146 132',width=5)),group('status-light',circle(111,192,4,GREEN))+group('port',rect(153,188,38,8,INK,2)),ellipse(160,232,87,8),['drive','disk','storage','backup','hard','hardware'],{'port':[172,192],'left':[83,132],'right':[237,132]})
 phone=rect(99,19,123,225,PAPER,19)+screen(110,46,101,169)
 add('smartphone-device',phone,group('speaker',path('M139 33L182 33',width=4))+group('home-indicator',path('M139 230L181 230',width=4)),group('screen-accent',path('M125 198L159 198',stroke=CORAL,width=5))+group('side-button',path('M223 84L223 112',stroke=CORAL,width=5)),ellipse(163,248,75,5),['smartphone','phone','mobile','device','app'],{'screen':[160,130],'left':[99,130],'right':[222,130]})
 tablet=rect(39,34,244,182,PAPER,15)+screen(52,47,217,150)
 add('tablet-device',tablet,group('camera',circle(161,40,2,INK))+group('home-indicator',path('M132 205L191 205',width=4)),group('stylus',path('M291 79L300 81L274 204L267 213L266 201Z',CORAL))+path('M66 178L111 178',stroke=CORAL,width=5),ellipse(166,231,126,7),['tablet','device','screen','stylus','drawing'],{'screen':[160,123],'left':[39,125],'right':[283,125]})
 index=json.loads((A/'index.json').read_text())
 for name,(svg,tags,anchors) in art.items():
  ET.fromstring(svg);f=A/'props'/(name+'.svg');f.write_text(svg)
  item={'id':'props/'+name,'path':str(f.relative_to(A)),'kind':'props','tags':tags+['sketch','hardware','layered','coral'],'palette':[PAPER,INK,CORAL,GREEN],'origin':'Original Duckygen hardware illustration; authored as layered SVG','reuse':'Original artwork; reusable in generated projects without attribution','style_revision':2,'style':'editorial-sketch-v2','layers':['shadow','body','detail','accent'],'anchors':anchors,'coordinate_space':[320,260],'sha256':hashlib.sha256(f.read_bytes()).hexdigest()}
  previous=next((i for i,x in enumerate(index['items']) if x['id']==item['id']),None)
  if previous is None:index['items'].append(item)
  else:index['items'][previous]=item
 (A/'index.json').write_text(json.dumps(index,indent=2)+'\n');print('Created',len(art),'layered hardware SVGs.')
if __name__=='__main__':main()
