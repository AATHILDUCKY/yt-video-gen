/* Original deterministic helpers. All visual state is derived from the supplied time. */
window.Motion=Object.freeze({
 clamp:(v,a=0,b=1)=>Math.max(a,Math.min(b,v)),
 exp(t,k=7){t=Math.max(0,Math.min(1,t));return (1-Math.exp(-k*t))/(1-Math.exp(-k))},
 spring(t,{frequency=3.2,damping=.86}={}){if(t<=0)return 0;const z=Math.max(.7,Math.min(.999,damping)),w=2*Math.PI*frequency,d=w*Math.sqrt(1-z*z);return 1-Math.exp(-z*w*t)*(Math.cos(d*t)+z*w/d*Math.sin(d*t))},
 lerp:(a,b,p)=>a+(b-a)*p,
 bezierEase(t,x1=.22,y1=0,x2=.18,y2=1){
  if(![t,x1,y1,x2,y2].every(Number.isFinite)||x1<0||x1>1||x2<0||x2>1)throw Error('Invalid easing control points');
  t=Math.max(0,Math.min(1,t));if(t===0||t===1)return t;
  const cubic=(u,a,b)=>3*(1-u)*(1-u)*u*a+3*(1-u)*u*u*b+u*u*u;
  let lo=0,hi=1;for(let i=0;i<24;i++){const m=(lo+hi)/2;if(cubic(m,x1,x2)<t)lo=m;else hi=m}
  return cubic((lo+hi)/2,y1,y2);
 },
 route(control,{steps=100}={}){
  if(control.length!==4||control.some(p=>p.length!==2||!p.every(Number.isFinite)))throw Error('Route needs four finite [x,y] cubic control points');
  steps=Math.max(12,Math.min(500,Math.round(steps)));const c=control.map(p=>p.slice());
  const sample=t=>{const s=1-t;return {x:s*s*s*c[0][0]+3*s*s*t*c[1][0]+3*s*t*t*c[2][0]+t*t*t*c[3][0],y:s*s*s*c[0][1]+3*s*s*t*c[1][1]+3*s*t*t*c[2][1]+t*t*t*c[3][1]}};
  let length=0,prev=sample(0);const table=[{t:0,length:0}];
  for(let i=1;i<=steps;i++){const t=i/steps,p=sample(t);length+=Math.hypot(p.x-prev.x,p.y-prev.y);table.push({t,length});prev=p}
  function at(progress){
   const distance=Math.max(0,Math.min(1,progress))*length;let lo=0,hi=table.length-1;
   while(hi-lo>1){const m=(lo+hi)>>1;if(table[m].length<distance)lo=m;else hi=m}
   const a=table[lo],b=table[hi],fraction=b.length===a.length?0:(distance-a.length)/(b.length-a.length),t=a.t+(b.t-a.t)*fraction,s=1-t;
   const dx=3*s*s*(c[1][0]-c[0][0])+6*s*t*(c[2][0]-c[1][0])+3*t*t*(c[3][0]-c[2][0]);
   const dy=3*s*s*(c[1][1]-c[0][1])+6*s*t*(c[2][1]-c[1][1])+3*t*t*(c[3][1]-c[2][1]);
   return {...sample(t),angle:Math.atan2(dy,dx),t};
  }
  return Object.freeze({length,at});
 },
 flowState(t,{start=0,draw=.28,travel=.85,settle=.16}={}){
  if(![t,start,draw,travel,settle].every(Number.isFinite)||draw<=0||travel<=0||settle<=0)throw Error('Use finite times and positive flow durations');
  const clamp=p=>Math.max(0,Math.min(1,p));const local=t-start;
  return {line:clamp(local/draw),packet:clamp((local-draw)/travel),packetVisible:local>=draw&&local<draw+travel,arrival:clamp((local-draw-travel)/settle),arrived:local>=draw+travel};
 },
 drawFlow(ctx,route,{progress=1,stroke='#292C27',width=4,head=12}={}){
  progress=Math.max(0,Math.min(1,progress));if(progress<=0)return;
  const first=route.at(0),last=route.at(progress),steps=Math.max(2,Math.ceil(route.length*progress/8));ctx.save();ctx.strokeStyle=stroke;ctx.lineWidth=width;ctx.lineCap='round';ctx.lineJoin='round';ctx.beginPath();ctx.moveTo(first.x,first.y);
  for(let i=1;i<=steps;i++){const p=route.at(progress*i/steps);ctx.lineTo(p.x,p.y)}ctx.stroke();
  if(head>0){ctx.translate(last.x,last.y);ctx.rotate(last.angle);ctx.beginPath();ctx.moveTo(-head,-head*.52);ctx.lineTo(0,0);ctx.lineTo(-head,head*.52);ctx.stroke()}ctx.restore();
 },
 morphPoints(a,b,p){if(a.length!==b.length||a.some((x,i)=>x.length!==b[i].length))throw Error('Morph topology/point count differs');return a.map((x,i)=>x.map((v,j)=>v+(b[i][j]-v)*p))},
 coverRadius:(w,h,x=w/2,y=h/2)=>Math.max(Math.hypot(x,y),Math.hypot(w-x,y),Math.hypot(x,h-y),Math.hypot(w-x,h-y))+2,
 impact(t,pixels=3){if(t<0||t>.2)return {x:0,y:0};const a=Math.min(6,Math.max(0,pixels))*Math.exp(-t*32);return {x:a*Math.sin(t*150),y:a*.5*Math.sin(t*113)}},
 velocity(position,t,dt=1/240){const a=position(t-dt),b=position(t+dt),x=(b.x-a.x)/(2*dt),y=(b.y-a.y)/(2*dt);return {x,y,speed:Math.hypot(x,y),angle:Math.atan2(y,x)}},
 camera(ctx,{x=960,y=540,zoom=1,rotation=0}={}){ctx.translate(960,540);ctx.rotate(rotation);ctx.scale(zoom,zoom);ctx.translate(-x,-y)},
 reveal(ctx,x,y,w,h,p,draw){ctx.save();ctx.beginPath();ctx.rect(x,y,w*Math.max(0,Math.min(1,p)),h);ctx.clip();draw();ctx.restore()},
 sketchPath(ctx,path,{stroke='#292C27',width=3}={}){const p=new Path2D(path);ctx.save();ctx.strokeStyle=stroke;ctx.lineCap='round';ctx.lineJoin='round';ctx.lineWidth=width;ctx.stroke(p);ctx.translate(.45,-.3);ctx.globalAlpha*=.18;ctx.lineWidth=width*.45;ctx.stroke(p);ctx.restore()}
});
