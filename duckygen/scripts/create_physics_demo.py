#!/usr/bin/env python3
"""Create a silent, seekable free-fall authoring study; not a narrated final lesson."""
import argparse,base64,json,pathlib,shutil
S=pathlib.Path(__file__).resolve().parents[1]
def main():
 p=argparse.ArgumentParser(description=__doc__);p.add_argument('--output',required=True,type=pathlib.Path);a=p.parse_args();out=a.output.resolve();out.mkdir(parents=True,exist_ok=True)
 for f in ['film.html','model-verification.json']:
  if (out/f).exists():p.error('Use a new output folder; existing studies are not overwritten.')
 shutil.copy2(S/'assets/fonts/OFL.txt',out/'FONT-LICENSE.txt')
 font=base64.b64encode((S/'assets/fonts/manrope-normal-500.ttf').read_bytes()).decode();bold=base64.b64encode((S/'assets/fonts/manrope-normal-800.ttf').read_bytes()).decode();module=(S/'assets/runtime/physics-models.mjs').read_text()
 html='''<!doctype html><meta charset="utf-8"><title>Duckygen · physical motion study</title><style>@font-face{font-family:Manrope;src:url(data:font/ttf;base64,__FONT__);font-weight:500}@font-face{font-family:Manrope;src:url(data:font/ttf;base64,__BOLD__);font-weight:800}html,body{margin:0;background:#FAF9F6}canvas{width:100vw;height:100vh;object-fit:contain;display:block}</style><canvas id="film" width="1920" height="1080"></canvas><script id="model" type="application/json">__MODULE__</script><script>
const canvas=document.querySelector('#film'),c=canvas.getContext('2d'),P='#FAF9F6',K='#292C27',R='#D76A4E',G='#17684F';let physics,impact;
const text=(v,x,y,size=34,col=K,w=500)=>{c.font=`${w} ${size}px Manrope`;c.fillStyle=col;c.textAlign='left';c.textBaseline='middle';c.fillText(v,x,y)};
const line=(x,y,u,v,col=K,w=3)=>{c.beginPath();c.moveTo(x,y);c.lineTo(u,v);c.strokeStyle=col;c.lineWidth=w;c.stroke()};
function arrow(x,y,length,col){line(x,y,x,y+length,col,5);line(x,y+length,x-9,y+length-15,col,5);line(x,y+length,x+9,y+length-15,col,5)}
window.filmConfig={title:'Why heavier objects do not fall faster in a vacuum',duration:6.8,bpm:120,isDemo:true,reviewMode:'shots',loop:false};window.filmShots=[{start:0,end:.8},{start:.8,end:2.82},{start:2.82,end:3.6},{start:3.6,end:6.8}];window.filmReviewTimes=[1,1.5,2,2.5,2.819275,4.5];
window.seek=t=>{t=Math.max(0,Math.min(6.8,t));const tau=Math.min(impact,Math.max(0,t-.8)),state=physics.projectileState(tau,{y0:20,g:9.81}),y=761-state.y*22;
c.fillStyle=P;c.fillRect(0,0,1920,1080);text('Does a heavier object fall faster?',100,110,68,K,800);text('UNIFORM GRAVITY  ·  NO AIR RESISTANCE  ·  START FROM REST',105,197,25,R,800);
line(130,800,1100,800,K,5);line(200,360,200,800,'#d5d3cb',3);for(let h=0;h<=20;h+=5){line(190,800-h*22,210,800-h*22,K,3);text(h+' m',100,800-h*22,24)}
for(const [x,m,col] of [[480,1,R],[890,4,K]]){c.beginPath();c.arc(x,y,39,0,Math.PI*2);c.fillStyle=col;c.fill();text(m+' kg',x-48,265,38,col,800);if(tau<impact){arrow(x+70,y+10,m*24,col);text('F = '+(m*9.81).toFixed(2)+' N',x-100,880,29,col);arrow(x-80,y+10,48,G)}else{text('first contact',x-92,875,27,G,800)}}
text('Same acceleration',1240,360,42,K,800);text('a = F / m = mg / m',1240,439,33);text('a = g = 9.81 m/s²',1240,505,36,G,800);text('Weight increases with mass.',1240,598,28);text('Acceleration stays the same.',1240,648,28);text('Green arrows: acceleration',1240,725,24,G);text('Other arrows: weight',1240,770,24);
if(t>=3.6){c.fillStyle=P;c.fillRect(90,840,1700,175);text('t = √(2h/g) = √(40/9.81) = 2.019 s',110,900,43,G,800);text('Both reach the ground together in this model.',110,975,42,K,800)}else{text('Physical time  '+Math.min(impact,Math.max(0,Math.round(t*60)/60-.8)).toFixed(3)+' s',115,978,33);text(tau===impact?'FROZEN AT FIRST CONTACT':'Positions use y = h − ½gt²; no decorative easing.',700,978,27,tau===impact?G:K)}
text('Silent authoring study · 20 m drop · impact dynamics are not modeled',105,1040,22,'#66695f');window.physicsState={physicalTime:tau,height:state.y,impactTime:impact,phase:tau===impact?'first-contact-freeze':'free-flight'};return window.physicsState};
window.motionFilmReady=(async()=>{await Promise.all([document.fonts.load('500 30px Manrope'),document.fonts.load('800 68px Manrope')]);await document.fonts.ready;physics=await import(URL.createObjectURL(new Blob([JSON.parse(document.querySelector('#model').textContent)],{type:'text/javascript'})));impact=physics.firstGroundContact({y0:20,g:9.81});seek(0);return true})();
</script>'''
 html=html.replace('__FONT__',font).replace('__BOLD__',bold).replace('__MODULE__',json.dumps(module).replace('</','<\\/'));(out/'film.html').write_text(html)
 (out/'model-verification.json').write_text(json.dumps(dict(question='Do heavier test masses fall faster in uniform gravity without air resistance?',assumptions=['Uniform g=9.81 m/s²','No air resistance','Release from rest at y=20 m','Same physical clock; y is lower-surface clearance upward; marker size schematic','Model stops at first ground contact; held frame is labeled'],equation='y=h-0.5*g*t^2; contactTime=sqrt(2*h/g)',expected_contact_time=(40/9.81)**.5,expected_incoming_speed=(40*9.81)**.5,units={'height':'m','time':'s','speed':'m/s','force':'N'},sources=['https://www1.grc.nasa.gov/beginners-guide-to-aeronautics/free-fall-without-air-resistance/'],scope='Silent authoring/validation example, not a finished narrated video'),indent=2));print(out/'film.html')
if __name__=='__main__':main()
