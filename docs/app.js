const grid=document.querySelector("#grid");
const radar=document.querySelector("#radar");
const search=document.querySelector("#search");
const type=document.querySelector("#type");
const visibleCount=document.querySelector("#visibleCount");
const counts={actor:document.querySelector("#actorCount"),campaign:document.querySelector("#campaignCount"),requirement:document.querySelector("#requirementCount"),watch:document.querySelector("#watchCount"),reference:document.querySelector("#referenceCount")};
let items=[];
function esc(s){return String(s??"").replace(/[&<>\"]/g,function(c){return {"&":"&amp;","<":"&lt;",">":"&gt;","\"":"&quot;"}[c]})}
function cls(x){const c=(x.category||"").toLowerCase();if(c.includes("state-linked"))return "state";if(c.includes("financial"))return "fin";return "other"}
function friendly(x){return (x.category||x.type||"").replaceAll("-"," ")}
function actorCard(x){return "<article class=\"actor-card\"><div class=\"kicker\"><span class=\"badge "+cls(x)+"\">"+esc(friendly(x))+"</span><span>"+esc(x.confidence||"")+"</span></div><h3>"+esc(x.name)+"</h3><p>"+esc(x.scope)+"</p><div class=\"region\">"+esc(x.region||"Global")+"</div><p><a href=\""+esc(x.source)+"\" target=\"_blank\" rel=\"noreferrer\">Evidence/source ↗</a></p></article>"}
function itemCard(x){const reg=x.region?"<div class=\"region\">"+esc(x.region)+"</div>":"";return "<article class=\"card\"><div class=\"meta\"><span>"+esc(x.type)+"</span><span>"+esc(x.status)+"</span></div><h3>"+esc(x.name)+"</h3><code>"+esc(x.id)+"</code><p><strong>"+esc(friendly(x))+"</strong></p><p>"+esc(x.scope)+"</p>"+reg+"<p><a href=\""+esc(x.source)+"\" target=\"_blank\" rel=\"noreferrer\">Source/object ↗</a></p></article>"}
function renderRadar(){radar.innerHTML=items.filter(function(x){return x.type==="actor"&&x.featured}).map(actorCard).join("")}
function render(){const q=search.value.trim().toLowerCase();const t=type.value;const f=items.filter(function(x){const hay=[x.name,x.id,x.category,x.scope,x.status,x.type,x.region].concat(x.aliases||[]).join(" ").toLowerCase();return(!q||hay.includes(q))&&(!t||x.type===t)});visibleCount.textContent=f.length;grid.innerHTML=f.map(itemCard).join("")}
fetch("data/catalog.json").then(function(r){if(!r.ok)throw new Error("catalog unavailable");return r.json()}).then(function(d){items=d.items||[];Object.entries(counts).forEach(function(pair){pair[1].textContent=items.filter(function(x){return x.type===pair[0]}).length});renderRadar();render()}).catch(function(e){grid.innerHTML="<p>Catalog could not be loaded: "+esc(e.message)+"</p>"});
search.addEventListener("input",render);type.addEventListener("change",render);