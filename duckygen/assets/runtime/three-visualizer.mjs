/* Original Duckygen illustrative 3D mechanism; all visible state derives from seek(t). */
export function createAuthorizationVisualization(THREE,{width=1920,height=1080}={}) {
 const colors={paper:0xFAF9F6,ink:0x292C27,coral:0xD76A4E,green:0x17684F};
 const renderer=new THREE.WebGLRenderer({alpha:true,antialias:true,preserveDrawingBuffer:true});
 renderer.setPixelRatio(1);renderer.setSize(width,height,false);renderer.setClearColor(0x000000,0);
 const scene=new THREE.Scene();const aspect=width/height;
 const camera=new THREE.OrthographicCamera(-7*aspect/1.777,7*aspect/1.777,4,-4,.1,100);camera.position.set(9,6,14);camera.lookAt(0,.5,0);
 const root=new THREE.Group();scene.add(root);
 const geometries=new Set(),materials=new Set();
 function box(w,h,d,color=colors.paper){
  const geo=new THREE.BoxGeometry(w,h,d);const mat=new THREE.MeshBasicMaterial({color});geometries.add(geo);materials.add(mat);
  const mesh=new THREE.Mesh(geo,mat);const edgeGeo=new THREE.EdgesGeometry(geo);const edgeMat=new THREE.LineBasicMaterial({color:colors.ink});geometries.add(edgeGeo);materials.add(edgeMat);mesh.add(new THREE.LineSegments(edgeGeo,edgeMat));return mesh;
 }
 const client=new THREE.Group();client.position.set(-4.5,.15,0);root.add(client);
 const display=box(2,1.3,.16);display.position.y=.8;client.add(display);
 const base=box(2.3,.15,1.2,colors.coral);base.position.set(0,0,.4);client.add(base);
 const stand=box(.25,.5,.3,colors.coral);stand.position.y=.3;client.add(stand);
 const server=new THREE.Group();server.position.set(4.5,.75,0);root.add(server);server.add(box(1.65,2.7,1.2));
 const panels=[];for(let i=0;i<3;i++){const face=box(1.3,.58,.12,i===0?colors.coral:colors.paper);face.position.set(0,.82-i*.8,.68);server.add(face);panels.push(face)}
 const gate=new THREE.Group();gate.position.set(0,.65,0);root.add(gate);
 for(const z of [-1,1]){const post=box(.18,3,.18,colors.coral);post.position.z=z;gate.add(post)}
 const lintel=box(.18,.18,2.2,colors.coral);lintel.position.y=1.5;gate.add(lintel)
 const barrier=box(.12,2.6,1.8,colors.coral);gate.add(barrier);
 const packet=box(.35,.25,.23,colors.coral);root.add(packet);
 const start=new THREE.Vector3(-3.3,.65,0),end=new THREE.Vector3(3.5,.65,0);
 const path=new THREE.CubicBezierCurve3(start,new THREE.Vector3(-1.8,.65,.65),new THREE.Vector3(1.8,.65,.65),end);
 const lineGeo=new THREE.TubeGeometry(path,80,.022,5,false);const lineMat=new THREE.MeshBasicMaterial({color:colors.ink});geometries.add(lineGeo);materials.add(lineMat);root.add(new THREE.Mesh(lineGeo,lineMat));
 const arrow=new THREE.Mesh(new THREE.ConeGeometry(.1,.25,5),lineMat);geometries.add(arrow.geometry);arrow.position.copy(end);arrow.rotation.z=-Math.PI/2;root.add(arrow);
 const clamp=v=>Math.max(0,Math.min(1,v));const ease=v=>{v=clamp(v);return v*v*(3-2*v)};
 function seek(t){
  t=Number.isFinite(t)?Math.max(0,t):0;
  const approved=t>=3.6;const local=approved?t-3.6:t;
  const p=approved?.38+.62*ease((local-.65)/2.6):Math.min(.38,ease(local/2.8));
  packet.position.copy(path.getPointAt(p));packet.quaternion.identity();
  barrier.position.y=approved?ease(local/.65)*3.2:0;
  barrier.visible=!approved||local<.65;
  const arrived=approved&&local>=3.25;packet.visible=!arrived;
  panels[0].material.color.setHex(arrived?colors.green:colors.coral);
  root.rotation.y=-.05+Math.min(t,8)*.008;
  camera.zoom=1+Math.min(t,8)*.005;camera.updateProjectionMatrix();renderer.render(scene,camera);
  const labelX=x=>(new THREE.Vector3(x,.5,0).applyMatrix4(root.matrixWorld).project(camera).x*.5+.5)*width;
  return {phase:arrived?'received':approved?'authorized':'blocked',packetProgress:p,illustrative:true,labels:{client:labelX(-4.5),authorization:labelX(0),server:labelX(4.5)}};
 }
 function dispose(){geometries.forEach(g=>g.dispose());materials.forEach(m=>m.dispose());renderer.dispose()}
 return {canvas:renderer.domElement,seek,dispose,scene,camera};
}
