// Checks results/invariants, independent of drawing code and render frame order.
import assert from 'node:assert/strict';
import {projectileState,firstGroundContact,oscillatorState,collision1D,snell} from '../assets/runtime/physics-models.mjs';
const close=(a,b,tol=1e-10)=>assert.ok(Math.abs(a-b)<=tol*Math.max(1,Math.abs(a),Math.abs(b)),`${a} differs from ${b}`);let checks=0;
const p={y0:20,vx0:3,vy0:0,g:9.81},T=firstGroundContact(p);close(T,Math.sqrt(40/9.81));close(projectileState(T,p).y,0);close(projectileState(T,p).vy,-Math.sqrt(2*9.81*20));close(projectileState(T,p).x,3*T);checks+=4;
close(firstGroundContact({y0:0,vy0:5,g:10}),1);close(firstGroundContact({y0:0,vy0:-5,g:10}),0);close(firstGroundContact({y0:1,vy0:-1e8,g:10}),1e-8,1e-14);checks+=3;
const apex=projectileState(2,{y0:0,vy0:20,g:10});close(apex.vy,0);close(apex.ay,-10);checks+=2;
for(const t of [0,.1,.5,1,2,3,5]){const q=projectileState(t,p);close(.5*(q.vx*q.vx+q.vy*q.vy)+9.81*q.y,.5*9+9.81*20);checks++}
const o={m:2,k:8,x0:1.5,v0:.4},a=oscillatorState(0,o);close(a.x,o.x0);close(a.v,o.v0);checks+=2;
for(const t of [0,.12,.5,1,2,10,100]){const q=oscillatorState(t,o);close(q.energy,a.energy);close(q.a,-o.k*q.x/o.m);checks+=2}
const elastic=collision1D({m1:2,m2:3,u1:4,u2:-1});close(elastic.momentumBefore,elastic.momentumAfter);close(elastic.kineticBefore,elastic.kineticAfter);checks+=2;
const stick=collision1D({m1:2,m2:3,u1:4,u2:-1,restitution:0});close(stick.v1,stick.v2);close(stick.momentumBefore,stick.momentumAfter);assert.ok(stick.internalEnergyGain>0);checks+=3;
const exchange=collision1D({m1:1,m2:1,u1:3,u2:0});close(exchange.v1,0);close(exchange.v2,3);checks+=2;
const r=snell({n1:1,n2:1.5,theta1:Math.PI/6});close(Math.sin(Math.PI/6),1.5*Math.sin(r.theta2));assert.ok(Math.abs(r.theta2)<Math.PI/6);checks+=2;
assert.equal(snell({n1:1.5,n2:1,theta1:Math.PI/3}).totalInternalReflection,true);close(snell({n1:1,n2:1.5,theta1:0}).theta2,0);checks+=2;
for(const bad of [()=>projectileState(-1),()=>projectileState(1,{g:0}),()=>firstGroundContact({y0:-1}),()=>oscillatorState(1,{m:0}),()=>collision1D({m1:1,m2:1,u1:0,u2:0,restitution:1.1}),()=>snell({n1:1,n2:1,theta1:Math.PI/2})]){assert.throws(bad);checks++}
// Fixed-step RK4 cross-check, independent of analytic spring implementation.
function integrate(dt){let x=o.x0,v=o.v0;const n=Math.round(2/dt);for(let i=0;i<n;i++){const acc=z=>-o.k*z/o.m,k1x=v,k1v=acc(x),k2x=v+dt*k1v/2,k2v=acc(x+dt*k1x/2),k3x=v+dt*k2v/2,k3v=acc(x+dt*k2x/2),k4x=v+dt*k3v,k4v=acc(x+dt*k3x);x+=dt*(k1x+2*k2x+2*k3x+k4x)/6;v+=dt*(k1v+2*k2v+2*k3v+k4v)/6}return x}
const exact=oscillatorState(2,o).x,e1=Math.abs(integrate(.05)-exact),e2=Math.abs(integrate(.025)-exact);assert.ok(e2<e1/10);assert.ok(e2<1e-6);checks+=2;
console.log(JSON.stringify({passed:true,checks,models:['uniform-gravity flight and first contact','linear undamped spring','1D isolated collision','planar Snell refraction'],step_refinement:{coarseError:e1,fineError:e2},scope:'Introductory model helpers; does not validate arbitrary physics, drawings or real hardware.'},null,2));
