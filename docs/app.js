const grid = document.querySelector("#grid");
const radar = document.querySelector("#radar");
const search = document.querySelector("#search");
const type = document.querySelector("#type");
const visibleCount = document.querySelector("#visibleCount");
const actorCount = document.querySelector("#actorCount");
const referenceCount = document.querySelector("#referenceCount");
const threatCount = document.querySelector("#threatCount");
let items = [];

function esc(s) {
  return String(s ?? "").replace(/[&<>"']/g, c => ({
    "&":"&amp;","<":"&lt;",">":"&gt;",'"':"&quot;","'":"&#039;"
  }[c]));
}

function classFor(item) {
  const c = (item.category || "").toLowerCase();
  if (c.includes("state-linked")) return "state";
  if (c.includes("financial")) return "fin";
  return "other";
}

function friendlyClass(item) {
  const c = (item.category || "").replaceAll("-", " ");
  return c || item.type;
}

function renderRadar() {
  const featured = items.filter(x => x.type === "actor" && x.featured);
  radar.innerHTML = featured.map(x => `
    <article class="actor-card">
      <div class="kicker">
        <span class="badge ${classFor(x)}">${esc(friendlyClass(x))}</span>
        <span>${esc(x.confidence || "")}</span>
      </div>
      <h3>${esc(x.name)}</h3>
      <p>${esc(x.scope)}</p>
      <div class="region">${esc(x.region || "Global")}</div>
      <p><a href="${esc(x.source)}" target="_blank" rel="noreferrer">Evidence/source ↗</a></p>
    </article>
  `).join("");
}

function render() {
  const q = search.value.trim().toLowerCase();
  const t = type.value;
  const filtered = items.filter(x => {
    const hay = [
      x.name,x.id,x.category,x.scope,x.status,x.type,x.region,
      ...(x.aliases || [])
    ].join(" ").toLowerCase();
    return (!q || hay.includes(q)) && (!t || x.type === t);
  });

  visibleCount.textContent = filtered.length;
  grid.innerHTML = filtered.map(x => `
    <article class="card">
      <div class="meta">
        <span>${esc(x.type)}</span>
        <span>${esc(x.status)}</span>
      </div>
      <h3>${esc(x.name)}</h3>
      <code>${esc(x.id)}</code>
      <p><strong>${esc(friendlyClass(x))}</strong></p>
      <p>${esc(x.scope)}</p>
      ${x.region ? `<div class="region">${esc(x.region)}</div>` : ""}
      <p><a href="${esc(x.source)}" target="_blank" rel="noreferrer">Primary/source reference ↗</a></p>
    </article>
  `).join("");
}

fetch("data/catalog.json")
  .then(r => {
    if (!r.ok) throw new Error("catalog unavailable");
    return r.json();
  })
  .then(data => {
    items = data.items || [];
    actorCount.textContent = items.filter(x => x.type === "actor").length;
    referenceCount.textContent = items.filter(x => x.type === "reference").length;
    threatCount.textContent = items.filter(x => x.type === "threat").length;
    renderRadar();
    render();
  })
  .catch(err => {
    grid.innerHTML = `<p>Catalog could not be loaded: ${esc(err.message)}</p>`;
  });

search.addEventListener("input", render);
type.addEventListener("change", render);
