#!/usr/bin/env python3
"""Rebuild Duckygen's curated v2 props; keeps stable IDs and named animation layers."""
from pathlib import Path
import json,hashlib,shutil,xml.etree.ElementTree as ET
ROOT=Path(__file__).resolve().parents[1];A=ROOT/'assets'
INK='#292C27';PAPER='#FAF9F6';CORAL='#D76A4E';GREEN='#17684F'
def path(d,fill='none',stroke=INK,width=3.2,extra=''):
 return f'<path d="{d}" fill="{fill}" stroke="{stroke}" stroke-width="{width}" {extra}/>'
def rect(x,y,w,h,fill=PAPER,r=5):return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{r}" fill="{fill}" stroke="{INK}" stroke-width="3.2"/>'
def circle(x,y,r,fill=CORAL,stroke=INK):return f'<circle cx="{x}" cy="{y}" r="{r}" fill="{fill}" stroke="{stroke}" stroke-width="2.5"/>'
def wrap(body,detail='',accent='',shadow='',view='0 0 320 260'):
 return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="{view}" fill="none" stroke-linecap="round" stroke-linejoin="round" data-duckygen-style="editorial-sketch-v2"><g id="shadow" opacity=".12">{shadow}</g><g id="body">{body}</g><g id="detail">{detail}</g><g id="accent">{accent}</g></svg>'
def main():
 art={}
 art['document-page']=wrap(path('M82 29Q80 27 79 33L75 218Q76 224 83 224L241 220L244 70L204 29Z',PAPER)+path('M204 29L201 73L244 70',CORAL),path('M101 96L210 94M100 121L220 119M100 146L186 144M99 172L211 170M98 197L165 196',width=2.7),path('M100 65L167 64',stroke=CORAL,width=6),path('M87 39L256 78L254 231L88 235Z',INK))
 keyboard=''.join(path(f'M{x} 187L{x+7} 203',stroke=INK,width=2) for x in range(81,247,19))
 art['laptop-workstation']=wrap(path('M60 39Q58 32 65 32L258 41Q264 42 264 49L255 177L51 167Z',PAPER)+path('M73 48L247 56L240 159L65 151Z',PAPER)+path('M51 167L255 177L292 220Q293 225 285 225L26 212Q18 211 25 205Z',CORAL),keyboard+path('M69 190L259 201M125 211L193 214',width=2)+path('M98 82L82 96L98 110M208 88L224 103L208 117M158 80L143 120',stroke=CORAL,width=4),circle(163,48,2,INK),path('M34 218L285 234L302 226L278 218Z',INK))
 serverbody=path('M93 26L217 33L237 51L234 226L91 222Z',PAPER)+path('M217 33L237 51L234 226L216 214Z',CORAL)
 detail=''
 for y in [52,104,156]:
  detail+=rect(107,y,94,43,PAPER,4)+path(f'M119 {y+14}L163 {y+14}M119 {y+23}L163 {y+23}M119 {y+32}L147 {y+32}',width=2)+circle(186,y+21,4,GREEN)
 art['server-rack']=wrap(serverbody,detail,path('M106 208L202 210',width=2),path('M99 37L248 56L246 236L102 233Z',INK))
 art['browser-window']=wrap(path('M36 45Q36 36 46 36L278 41Q286 42 286 51L282 219L33 214Z',PAPER)+path('M36 45L286 51L285 80L35 75Z',CORAL),circle(51,58,3,PAPER)+circle(65,59,3,PAPER)+circle(79,59,3,PAPER)+path('M100 59L196 62',stroke=PAPER,width=4)+path('M65 111L127 112M64 128L108 129M65 174L250 178',width=2.5)+rect(191,102,61,52,PAPER,7)+path('M142 136C157 111 174 111 185 124M174 116L185 124L176 131',stroke=CORAL,width=3),path('M64 195L136 197',stroke=CORAL,width=5),path('M45 47L295 54L294 230L44 225Z',INK))
 art['hot-wallet']=wrap(path('M66 76L246 68L258 208L64 215Z',CORAL)+path('M66 76L66 53L233 42L246 68Z',PAPER)+path('M71 86L247 78L254 200L70 206Z',PAPER)+path('M252 117L205 120Q197 121 198 130L200 162Q200 168 207 168L255 165Z',CORAL),circle(216,143,6,PAPER)+path('M87 109L170 105M87 123L145 120',width=2.4),circle(137,57,22,PAPER)+path('M137 44L137 68M129 49Q145 43 145 52Q145 58 132 58Q126 59 130 65L144 64',stroke=CORAL,width=2.5),path('M73 84L270 77L271 218L76 226Z',INK))
 art['database-stack']=wrap(path('M75 63C73 29 245 29 246 65L246 197C244 232 74 231 74 195Z',PAPER)+path('M75 63C75 99 246 100 246 65C244 29 76 28 75 63Z',CORAL),path('M74 106C74 140 245 142 246 108M74 151C74 185 245 185 246 153',width=3)+path('M91 105L91 120M90 151L90 165M90 191L90 203',stroke=CORAL,width=4),circle(222,124,3,GREEN)+circle(222,167,3,GREEN)+circle(222,207,3,GREEN),path('M88 58L260 69L259 207Q174 249 84 217Z',INK))
 cloud=path('M74 148C25 147 30 83 75 88C79 31 159 23 184 68C222 43 265 76 257 108C297 134 267 170 235 166L76 163Z',PAPER)
 art['cloud-network']=wrap(cloud,path('M102 162L102 202L160 203L160 169M220 164L220 203L160 203',width=3)+circle(102,212,13,PAPER)+circle(160,212,13,PAPER)+circle(220,212,13,PAPER),path('M91 117C114 91 141 83 169 87',stroke=CORAL,width=6)+circle(222,126,9,CORAL),path('M65 102C51 135 65 177 91 174L244 179L275 154L247 150Z',INK))
 back=path('M114 30L252 39L244 204L111 195Z',CORAL)+path('M86 44L226 48L222 217L82 213Z',PAPER)
 art['stacked-files']=wrap(back+path('M61 65L195 60L204 234L67 238Z',PAPER),path('M83 102L174 98M84 126L175 122M85 151L158 148M86 177L175 174M87 203L145 200',width=2.5),path('M82 84L145 82',stroke=CORAL,width=5),path('M73 76L211 69L218 244L78 248Z',INK))
 art['security-boundary']=wrap(path('M160 25L250 60L246 139C243 181 205 216 160 239C114 215 78 181 74 139L70 60Z',CORAL)+path('M160 42L234 72L231 136C228 170 198 201 160 221C121 201 91 170 89 136L86 72Z',PAPER),path('M112 126L146 160L210 91',stroke=GREEN,width=9),path('M110 77L140 65',stroke=CORAL,width=3),path('M170 32L260 67L258 150Q222 222 170 249L162 238Q245 196 246 139L250 60Z',INK))
 bank=path('M43 84L158 27L277 91Z',CORAL)+path('M55 99L265 104L264 118L54 113Z',PAPER)+path('M43 220L275 225L286 240L33 234Z',CORAL)
 for x in [70,122,174,226]:bank+=path(f'M{x} 114L{x+25} 115L{x+24} 218L{x-1} 217Z',PAPER)
 art['exchange-building']=wrap(bank,path('M86 129L85 204M138 130L137 205M190 131L189 207M242 133L241 208',width=1.8),circle(159,69,13,PAPER),path('M63 110L280 115L283 231L53 227Z',INK))
 phone=rect(101,20,126,225,PAPER,18)+path('M133 34L192 34',width=4)+path('M113 57L215 57L215 214L113 214Z',PAPER)
 art['phone-notification']=wrap(phone,path('M133 230L192 230',width=4)+path('M78 102L241 102L241 158L196 158L181 179L177 158L78 158Z',CORAL),path('M96 120L217 120M96 137L184 137',stroke=PAPER,width=4)+circle(218,62,13,GREEN),path('M113 28L239 37L239 250L112 252Z',INK))
 art['timeline-strip']=wrap(path('M36 64L281 64L281 216L36 216Z',PAPER)+path('M36 65L281 65L281 89L36 89Z',CORAL),path('M52 109L52 199M97 109L97 199M143 109L143 199M189 109L189 199M235 109L235 199M267 109L267 199',stroke=INK,width=1.2)+rect(54,110,84,28,CORAL,3)+rect(140,110,105,28,PAPER,3)+rect(83,150,148,22,PAPER,3)+path('M58 187L66 182L74 193L83 179L92 191L102 185L110 196L120 179L132 190L141 181L150 194L163 179L176 193L185 185L197 192L209 180L220 191L237 184',stroke=GREEN,width=2),path('M165 49L165 215',stroke=CORAL,width=3)+path('M157 48L173 48L165 59Z',CORAL),path('M46 74L291 75L291 227L46 228Z',INK))
 # Preserve verified map/token geometry from the prior source while improving staging.
 archive=A/'sources/duckygen-v1';archive.mkdir(parents=True,exist_ok=True)
 for name in ['bitcoin-token','ether-token','transaction-packet','world-map-outline']:
  original=archive/(name+'.svg');current=A/'props'/(name+'.svg')
  if not original.exists():shutil.copy2(current,original)
  root=ET.fromstring(original.read_text());inside=''.join(ET.tostring(e,encoding='unicode') for e in root);view=root.attrib['viewBox']
  if name=='world-map-outline':
   inside=inside.replace('stroke-width=".7"','stroke-width="2.4"')
   body=path('M18 49L302 47L303 212L17 215Z',PAPER)+f'<svg x="23" y="61" width="274" height="133" viewBox="{view}" fill="none" stroke="{INK}">{inside}</svg>';accent=path('M35 207L106 206',stroke=CORAL,width=4);shadow=path('M25 57L309 55L311 221L24 223Z',INK)
  elif name=='transaction-packet':
   body=f'<svg x="17" y="18" width="286" height="224" viewBox="{view}" fill="none" stroke="{INK}">{inside}</svg>';accent='';shadow='<ellipse cx="160" cy="215" rx="113" ry="11" fill="'+INK+'"/>'
  else:
   body=f'<svg x="60" y="27" width="200" height="200" viewBox="{view}" fill="none" stroke="{INK}">{inside}</svg>';accent='';shadow='<ellipse cx="169" cy="143" rx="83" ry="83" fill="'+INK+'"/>' 
  art[name]=wrap(body,accent=accent,shadow=shadow)
 index=json.loads((A/'index.json').read_text())
 for name,svg in art.items():
  f=A/'props'/(name+'.svg');ET.fromstring(svg);f.write_text(svg)
  item=next(x for x in index['items'] if x['id']=='props/'+name);item.update(sha256=hashlib.sha256(f.read_bytes()).hexdigest(),style_revision=2,style='editorial-sketch-v2',layers=['shadow','body','detail','accent'])
  item['origin']=item.get('origin','Original Duckygen artwork')+'; refined Duckygen v2 layer composition' if 'refined Duckygen v2' not in item.get('origin','') else item['origin']
 (A/'index.json').write_text(json.dumps(index,indent=2)+'\n');print('Refined',len(art),'props; stable IDs and named layers preserved.')
if __name__=='__main__':main()
