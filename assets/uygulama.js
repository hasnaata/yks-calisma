/* Ortak uygulama kodu. Derleme adımı yok: sayfalar Markdown dosyalarını tarayıcıda işler.
   İlerleme yalnızca bu tarayıcıda (localStorage) tutulur; sunucuya hiçbir şey gönderilmez. */
const SINAV_TARIHI = new Date('2027-06-19T10:15:00+03:00'); // TYT
const ARALIKLAR = [1, 3, 7, 16, 35]; // aralıklı tekrar (gün)
/* Ders rengi ve simgesi: anahtar, ders kimliğinin sınav ön eki atılmış hâlidir. */
const DERS_GORSEL = {
  'biyoloji': ['#2f855a', 'M5 19c0-8 5-13 14-14 0 9-5 14-14 14zM5 19l7-7'],
  'cografya': ['#b7791f', 'M12 3a9 9 0 1 0 0 18 9 9 0 0 0 0-18zM3 12h18M12 3c3 3 3 15 0 18M12 3c-3 3-3 15 0 18'],
  'din-kulturu-ve-ahlak-bilgisi': ['#6b46c1', 'M12 6c-2-1.5-5-2-8-1.5v13c3-.5 6 0 8 1.5 2-1.5 5-2 8-1.5v-13c-3-.5-6 0-8 1.5zM12 6v13'],
  'felsefe': ['#2b6cb0', 'M9 18h6M10 21h4M12 3a6 6 0 0 0-4 10.5c.7.7 1 1.5 1 2.5h6c0-1 .3-1.800 1-2.5A6 6 0 0 0 12 3z'],
  'fizik': ['#c53030', 'M12 11a1 1 0 1 0 0 2 1 1 0 0 0 0-2zM12 3c2.500 0 4.500 4 4.500 9s-2 9-4.500 9-4.500-4-4.500-9 2-9 4.500-9zM4.200 7.500c1.250-2.170 5.750-1.900 10.050.600s6.800 6.230 5.550 8.400-5.750 1.900-10.050-.600-6.800-6.230-5.550-8.400z'],
  'kimya': ['#b83280', 'M9 3h6M10 3v6l-5 9a2 2 0 0 0 2 3h10a2 2 0 0 0 2-3l-5-9V3M7.500 15h9'],
  'matematik': ['#c05621', 'M4 7h6M7 4v6M14 7h6M5 15l5 5M10 15l-5 5M14 16h6M14 19h6'],
  'tarih': ['#2c5282', 'M6 3h12M6 21h12M7 3c0 5 10 5 10 9s-10 4-10 9M17 3c0 5-10 5-10 9s10 4 10 9'],
  'turkce': ['#0f766e', 'M4 20l4-1 11-11-3-3L5 16l-1 4zM14 6l3 3'],
  'turk-dili-ve-edebiyati': ['#0f766e', 'M4 20l4-1 11-11-3-3L5 16l-1 4zM14 6l3 3'],
};
const dersGorsel = (id) => { const [renk, yol] = DERS_GORSEL[id.replace(/^(tyt|ayt)-/, '')] || ['#1f5fbf', 'M4 12h16']; return { renk, simge: `<span class="simge" aria-hidden="true"><svg viewBox="0 0 24 24"><path d="${yol}"/></svg></span>` }; };
const $ = (s, k = document) => k.querySelector(s);
const el = (ad, ozellik = {}, ic = '') => { const e = document.createElement(ad); Object.assign(e, ozellik); if (ic) e.innerHTML = ic; return e; };
const bugun = () => new Date().toISOString().slice(0, 10);
const gunEkle = (g) => { const d = new Date(); d.setDate(d.getDate() + g); return d.toISOString().slice(0, 10); };

/* ---------- Profil ve ilerleme ---------- */
const Depo = {
  oku(k, v) { try { return JSON.parse(localStorage.getItem(k)) ?? v; } catch { return v; } },
  yaz(k, v) { try { localStorage.setItem(k, JSON.stringify(v)); } catch {} },
};
const Profil = {
  liste: () => Depo.oku('yks.profiller', ['Öğrenci 1', 'Öğrenci 2']),
  secili: () => Depo.oku('yks.secili', 0),
  sec(i) { Depo.yaz('yks.secili', i); location.reload(); },
  adlandir() {
    const l = Profil.liste(), i = Profil.secili();
    const ad = prompt('Bu profilin adı (yalnızca bu cihazda saklanır):', l[i]);
    if (ad && ad.trim()) { l[i] = ad.trim().slice(0, 20); Depo.yaz('yks.profiller', l); location.reload(); }
  },
};
const Ilerleme = {
  anahtar: () => 'yks.ilerleme.' + Profil.secili(),
  hepsi() { return Depo.oku(this.anahtar(), {}); },
  al(yol) { return this.hepsi()[yol] || {}; },
  guncelle(yol, degisim) { const h = this.hepsi(); h[yol] = { ...(h[yol] || {}), ...degisim }; Depo.yaz(this.anahtar(), h); return h[yol]; },
  /* Alıştırma bitince: puanı yaz, bir sonraki tekrar tarihini belirle. %70 altı ise aralık sıfırlanır. */
  alistirmaBitti(yol, dogru, toplam) {
    const k = this.al(yol), basarili = dogru / toplam >= 0.7;
    const adim = basarili ? Math.min((k.adim ?? -1) + 1, ARALIKLAR.length - 1) : 0;
    Seri.isle();
    return this.guncelle(yol, { puan: dogru, toplam, son: bugun(), adim, sonraki: gunEkle(ARALIKLAR[adim]),
      deneme: (k.deneme || 0) + 1 });
  },
};

/* Seri: üst üste kaç gün en az bir alıştırma bitirildi. */
const Seri = {
  anahtar: () => 'yks.seri.' + Profil.secili(),
  isle() { const s = Depo.oku(this.anahtar(), {}), t = bugun(); if (s.son === t) return;
    Depo.yaz(this.anahtar(), { son: t, gun: s.son === gunEkle(-1) ? (s.gun || 0) + 1 : 1 }); },
  gun() { const s = Depo.oku(this.anahtar(), {}); return s.son === bugun() || s.son === gunEkle(-1) ? s.gun || 0 : 0; },
};

/* ---------- Müfredat ---------- */
let _muf;
async function mufredat() { return _muf ??= await (await fetch('data/mufredat.json')).json(); }
const altKonular = (ders) => ders.konular.flatMap(k => k.altkonular.map(a => ({ ...a, konu: k.ad, ders })));
const hazir = (a) => a.ders && a.alistirma;

/* ---------- Üst çubuk ---------- */
function ustCubuk() {
  const l = Profil.liste(), s = Profil.secili();
  const h = el('header', { className: 'ust' }, `<div class="ic">
    <a class="logo" href="index.html">YKS Çalışma Sistemi</a>
    <nav aria-label="Rehber"><a href="sayfa.html?f=reference/yks-sinav-yapisi.md">Sınav rehberi</a>
    <a href="sayfa.html?f=reference/nasil-calisilir.md">Nasıl çalışılır?</a></nav>
    <select aria-label="Profil" id="profilSec">${l.map((a, i) => `<option value="${i}" ${i == s ? 'selected' : ''}>${a}</option>`).join('')}
      <option value="ad">Adı değiştir…</option></select></div>`);
  document.body.prepend(h);
  $('#profilSec').onchange = (e) => e.target.value === 'ad' ? Profil.adlandir() : Profil.sec(+e.target.value);
}

/* ---------- Markdown + matematik ---------- */
function onMadde(metin) {
  const m = /^---\n([\s\S]*?)\n---\n/.exec(metin); const bilgi = {};
  if (!m) return { bilgi, govde: metin };
  m[1].split('\n').forEach(s => { const i = s.indexOf(':'); if (i > 0) bilgi[s.slice(0, i).trim()] = s.slice(i + 1).trim(); });
  return { bilgi, govde: metin.slice(m[0].length) };
}
/* Matematiği ($...$ ve $$...$$) Markdown işleyicisinden korur, sonra KaTeX ile çizer. */
function md(kaynak, satirIci = false) {
  const parcalar = [];
  const sakla = (tex, blok) => { parcalar.push({ tex, blok }); return `\u0000M${parcalar.length - 1}\u0000`; };
  let s = kaynak.replace(/\$\$([\s\S]+?)\$\$/g, (_, t) => sakla(t, true))
                .replace(/\$(?!\s)([^$\n]+?)\$/g, (_, t) => sakla(t.trim(), false));
  s = satirIci ? marked.parseInline(s) : marked.parse(s);
  /* Tek başına duran görsel -> <figure>. Başlık (title) alt yazı olur; .svg şemalar yana kayabilir. */
  s = s.replace(/<p>(<img [^>]*>)<\/p>/g, (_, img) => {
    const alt = (/alt="([^"]*)"/.exec(img) || [])[1] || '', baslik = (/title="([^"]*)"/.exec(img) || [])[1] || '';
    const sema = /src="[^"]*\.svg"/.test(img);
    return `<figure class="sekil"><div class="kaydir" ${sema ? 'tabindex="0"' : ''}>${img.replace('<img ', `<img loading="lazy" ${sema ? 'class="sema" onload="this.style.setProperty(\'--enaz\', Math.round(this.naturalWidth*0.62)+\'px\')" ' : ''}`).replace(/ title="[^"]*"/, '')}</div>${baslik || alt ? `<figcaption>${baslik || alt}</figcaption>` : ''}</figure>`;
  });
  s = s.replace(/<table>/g, '<div class="tablo" tabindex="0"><table>').replace(/<\/table>/g, '</table></div>');
  return s.replace(/\u0000M(\d+)\u0000/g, (_, i) => {
    const p = parcalar[+i];
    try { return katex.renderToString(p.tex, { displayMode: p.blok, throwOnError: false }); } catch { return p.tex; }
  });
}

/* ---------- Soru biçimi ----------
   ### Soru 1            (başlık; "### Soru 1 · Kolay" gibi etiket alabilir)
   Soru kökü…
   A) …  B) …  (her seçenek kendi satırında, A–E)
   **Cevap:** C
   **Çözüm:** …
*/
function sorulariAyir(govde) {
  const sorular = [], cikti = [], satirlar = govde.split('\n');
  const isle = (baslik, ic) => {
    const c = /\*\*Cevap:\*\*\s*([A-E])/.exec(ic), ilk = ic.search(/^A\)\s/m);
    if (!c || ilk < 0) { cikti.push(baslik, ic); return; }
    const secenekler = ic.slice(ilk, c.index).split(/^(?=[A-E]\)\s)/m).filter(x => x.trim())
      .map(x => ({ harf: x[0], metin: x.slice(2).trim() }));
    sorular.push({ kok: ic.slice(0, ilk).trim(), secenekler, cevap: c[1],
      cozum: ic.slice(c.index + c[0].length).replace(/^\s*\*\*Çözüm:\*\*\s*/, '').trim(),
      etiket: baslik.replace(/^### Soru\s*\d*\s*[·–-]?\s*/, '').trim() });
    cikti.push('', `<div class="soru" data-i="${sorular.length - 1}"></div>`, '');
  };
  let baslik = null, tampon = [];
  for (const s of [...satirlar, '## ']) {
    if (/^#{2,3} /.test(s)) {
      if (baslik !== null) isle(baslik, tampon.join('\n'));
      baslik = null; tampon = [];
      if (/^### Soru\b/.test(s)) { baslik = s; continue; }
    }
    if (baslik !== null) tampon.push(s); else cikti.push(s);
  }
  cikti.pop();
  return { govde: cikti.join('\n'), sorular };
}
/* Soruları etkileşimli karta çevirir. bitince(dogru, toplam) hepsi yanıtlanınca çağrılır. */
function sorulariKur(kap, sorular, bitince) {
  let dogru = 0, yanit = 0;
  kap.querySelectorAll('.soru').forEach((d, sira) => {
    const s = sorular[+d.dataset.i];
    d.innerHTML = `<div class="no">Soru ${sira + 1}${s.etiket ? ' · ' + s.etiket : ''}</div><div class="kok">${md(s.kok)}</div>
      <div class="secenekler">${s.secenekler.map(o => `<button class="sec" data-h="${o.harf}"><b>${o.harf})</b><span>${md(o.metin, true)}</span></button>`).join('')}</div>
      <div class="cozum" aria-live="polite"><p class="ui"><b>Doğru cevap: ${s.cevap}</b></p>${md(s.cozum)}</div>`;
    d.querySelectorAll('button.sec').forEach(b => b.onclick = () => {
      if (d.classList.contains('bitti')) return;
      d.classList.add('bitti'); yanit++;
      const isaret = (x, yazi) => x.insertAdjacentHTML('beforeend', `<span class="durum">${yazi}</span>`);
      d.querySelectorAll('button.sec').forEach(x => { x.disabled = true; if (x.dataset.h === s.cevap) { x.classList.add('dogru'); isaret(x, 'Doğru cevap'); } });
      if (b.dataset.h === s.cevap) dogru++; else { b.classList.add('yanlis'); isaret(b, 'Senin cevabın'); }
      if (yanit === sorular.length && bitince) bitince(dogru, sorular.length);
    });
  });
}
/* Veri yüklenemediğinde gösterilen ortak hata kutusu. */
const yuklemeHatasi = (kap) => kap.innerHTML = '<p class="bilgi">İçerik yüklenemedi. İnternet bağlantını kontrol edip <a href="">sayfayı yenile</a>.</p>';
async function metinAl(yol) { const r = await fetch(yol); if (!r.ok) throw new Error(yol + ' bulunamadı'); return r.text(); }
const karistir = (d) => { for (let i = d.length - 1; i > 0; i--) { const j = Math.floor(Math.random() * (i + 1)); [d[i], d[j]] = [d[j], d[i]]; } return d; };
