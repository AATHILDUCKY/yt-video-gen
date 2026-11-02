// Original Duckygen SI-unit analytic teaching models. No drawing or frame history.
// Each model has deliberately narrow assumptions; see references/physics.md.
function finite(name,x){if(!Number.isFinite(x))throw new TypeError(`${name} must be finite`);return x}
function positive(name,x){finite(name,x);if(x<=0)throw new RangeError(`${name} must be positive`);return x}
function time(t){finite('time',t);if(t<0)throw new RangeError('time must be nonnegative');return t}
function gravity(p={}){const a={x0:0,y0:0,vx0:0,vy0:0,g:9.81,...p};for(const key of ['x0','y0','vx0','vy0'])finite(key,a[key]);positive('g',a.g);return a}
// Uniform downward gravity, y upward, no drag. Continues mathematically through
// the ground; stop at firstGroundContact before drawing a physical collision.
export function projectileState(t,p={}){time(t);const a=gravity(p);return {t,x:a.x0+a.vx0*t,y:a.y0+a.vy0*t-.5*a.g*t*t,vx:a.vx0,vy:a.vy0-a.g*t,ax:0,ay:-a.g}}
// First t>=0 reaching groundY from an initially on/above-ground position.
// A launch upward from the surface returns to the surface at its positive root.
export function firstGroundContact(p={}){const a=gravity(p),groundY=finite('groundY',p.groundY??0),h=a.y0-groundY;if(h<0)throw new RangeError('initial position is below the ground');const v=a.vy0;if(h===0)return v>0?2*v/a.g:0;const d=Math.hypot(v,Math.sqrt(2*a.g*h));return v<0?2*h/(d-v):(v+d)/a.g}
// Linear Hookean spring, equilibrium at x=0, no damping/drive, point mass.
export function oscillatorState(t,{m=1,k=1,x0=1,v0=0}={}){time(t);positive('mass',m);positive('spring constant',k);finite('x0',x0);finite('v0',v0);const omega=Math.sqrt(k/m),a=omega*t,x=x0*Math.cos(a)+v0/omega*Math.sin(a),v=-x0*omega*Math.sin(a)+v0*Math.cos(a);return {t,x,v,a:-k*x/m,omega,period:2*Math.PI/omega,kinetic:.5*m*v*v,potential:.5*k*x*x,energy:.5*m*v*v+.5*k*x*x}}
// 1D instantaneous isolated collision. Velocities are signed in a shared axis.
// Caller establishes contact and approach in geometry before applying this map.
export function collision1D({m1,m2,u1,u2,restitution=1}){positive('m1',m1);positive('m2',m2);finite('u1',u1);finite('u2',u2);finite('restitution',restitution);if(restitution<0||restitution>1)throw new RangeError('passive restitution must be in [0,1]');const total=m1+m2,p=m1*u1+m2*u2,v1=(p-m2*restitution*(u1-u2))/total,v2=(p+m1*restitution*(u1-u2))/total,before=.5*m1*u1*u1+.5*m2*u2*u2,after=.5*m1*v1*v1+.5*m2*v2*v2;return {v1,v2,momentumBefore:p,momentumAfter:m1*v1+m2*v2,kineticBefore:before,kineticAfter:after,internalEnergyGain:before-after}}
// Planar boundary; positive indices, signed incident angle from the normal,
// within (-pi/2, pi/2). Geometrical optics, no absorption/intensity model.
export function snell({n1,n2,theta1}){positive('n1',n1);positive('n2',n2);finite('theta1',theta1);if(Math.abs(theta1)>=Math.PI/2)throw new RangeError('incident angle must be within (-pi/2,pi/2)');const s=n1/n2*Math.sin(theta1),criticalAngle=n1>n2?Math.asin(n2/n1):null;if(Math.abs(s)>1+1e-12)return {totalInternalReflection:true,theta2:null,criticalAngle};return {totalInternalReflection:false,theta2:Math.asin(Math.max(-1,Math.min(1,s))),criticalAngle}}
