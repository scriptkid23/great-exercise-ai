(this["webpackJsonpmy-app"]=this["webpackJsonpmy-app"]||[]).push([[0],{25:function(e,t,n){e.exports=n(50)},30:function(e,t,n){},32:function(e,t,n){},50:function(e,t,n){"use strict";n.r(t);var r=n(0),a=n.n(r),o=n(17),c=n.n(o),i=(n(30),n(3)),u=n.n(i),s=n(18),l=n(5),f=n(19),d=(n(32),n(21)),m=n(20),p=n.n(m);function h(){var e=Object(f.a)(["\n      background-color: ",";\n      height: ","px;\n      width: ","px;\n      margin: ","px;\n      z-index: ",";\n"]);return h=function(){return e},e}var v=d.a.div(h(),(function(e){return e.color}),(function(e){return e.size}),(function(e){return e.size}),(function(e){return e.margin}),(function(e){return e.zindex}));var g=function(){var e=window.innerWidth,t=a.a.useState([]),n=Object(l.a)(t,2),r=n[0],o=n[1],c=a.a.useState(3),i=Object(l.a)(c,2),f=i[0],d=i[1],m=0,h=function t(){++m<r.length&&function(t){var n=t[0],r=t[1],a=t[2];window.setTimeout((function(){for(var t=0;t<n.length;t+=1){var o=document.getElementById("disc-"+n[t]);console.log(o),o.style.left="180px",o.style.transform="rotate(0deg)"}for(var c=0;c<r.length;c+=1){var i=document.getElementById("disc-"+r[c]);i.style.left=e-800+"px",i.style.transform="rotate(360deg)"}for(var u=0;u<a.length;u+=1){var s=document.getElementById("disc-"+a[u]);s.style.left=e-500+"px",s.style.transform="rotate(720deg)"}}),1e3)}(r[m]),setTimeout(t,1e3)},g=function(){var e=Object(s.a)(u.a.mark((function e(t){var n;return u.a.wrap((function(e){for(;;)switch(e.prev=e.next){case 0:return e.prev=0,e.next=3,p()({method:"post",url:"http://localhost:5000/process",data:{number_of_disc:t}});case 3:n=e.sent,o(n.data),e.next=10;break;case 7:e.prev=7,e.t0=e.catch(0),alert(e.t0);case 10:case"end":return e.stop()}}),e,null,[[0,7]])})));return function(t){return e.apply(this,arguments)}}();a.a.useEffect((function(){h()}));var y={1:"#14274e",2:"#0e918c",3:"#f6830f",4:"#794c74",5:"#150485",6:"#f0a500",7:"#1a1a2e",8:"#91d18b"};return a.a.createElement("div",{className:"wrapper"},a.a.createElement("div",{className:"anim"},function(){for(var e=[],t=f;t>0;t--)e.push(a.a.createElement(v,{key:t,id:"disc-"+t,zindex:f-t,size:50*t+40,margin:30-23.5*t,color:y[t]}));return e}()),a.a.createElement("form",null,a.a.createElement("input",{placeholder:"Type number of disc",type:"number",onChange:function(e){return d(parseInt(e.target.value,10))}}),a.a.createElement("button",{type:"button",onClick:function(){return g(f)}},"Start")))};Boolean("localhost"===window.location.hostname||"[::1]"===window.location.hostname||window.location.hostname.match(/^127(?:\.(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)){3}$/));c.a.render(a.a.createElement(a.a.StrictMode,null,a.a.createElement(g,null)),document.getElementById("root")),"serviceWorker"in navigator&&navigator.serviceWorker.ready.then((function(e){e.unregister()})).catch((function(e){console.error(e.message)}))}},[[25,1,2]]]);
//# sourceMappingURL=main.051512df.chunk.js.map