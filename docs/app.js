const grid = document.querySelector("#grid");
const search = document.querySelector("#search");
const type = document.querySelector("#type");
const count = document.querySelector("#count");
let items = [];

function esc(s) {
  return String(s ?? "").replace(/[&<>"']/g, c => ({
    "&":"&amp;","<":"&lt;",">":"&gt;",'"':"&quot;","'":"&#039;"
  }[c]));
}

function render() {
  const q = search.value.trim().toLowerCase();
  const t = type.value;
  const filtered = items.filter(x => {
    const hay = [x.name,x.id,x.category,x.scope,x.status,x.type].join(" ").toLowerCase();
    return (!q || hay.includes(q)) && (!t || x.type === t);
  });
  count.textContent = filtered.length;
  grid.innerHTML = filtered.map(x => `
    <article class="card">
      <div class="meta"><span>${esc(x.type)}</span><span>${esc(x.status)}</span></div>
      <h2>${esc(x.name)}</h2>
      <code>${esc(x.id)}</code>
      <p><strong>${esc(x.category)}</strong></p>
      <p>${esc(x.scope)}</p>
      <a href="${esc(x.source)}" target="_blank" rel="noreferrer">Primary/source reference ↗</a>
    </article>
  `).join("");
}

fetch("data/catalog.json")
  .then(r => {
    if (!r.ok) throw new Error("catalog unavailable");
    return r.json();
  })
  .then(data => { items = data.items || []; render(); })
  .catch(err => {
    grid.innerHTML = `<p>Catalog could not be loaded: ${esc(err.message)}</p>`;
  });

search.addEventListener("input", render);
type.addEventListener("change", render);
