# CLAUDE.md — YKS Çalışma Sistemi

Bu repo, iki öğrencinin 2027 YKS'ye (TYT + AYT Eşit Ağırlık) hazırlanması için bir **ders ve alıştırma sistemidir**.
GitHub Pages üzerinden yayınlanır. Derleme adımı yoktur: sayfalar Markdown dosyalarını tarayıcıda işler.
İki fikir üzerine kuruludur: Karpathy'nin **LLM wiki** düzeni (ham kaynak → Claude'un yazdığı wiki → bu şema dosyası)
ve Matt Pocock'un **/teach** becerisi (`.claude/skills/teach/`). Öğrenci içeriği **Türkçe** yazılır.

## Katmanlar

| Katman | Yer | Kural |
|---|---|---|
| Ham kaynak | `raw/mebi/pdf`, `raw/mebi/metin` (yerel, git dışı), `raw/mebi/agac.txt` | **Asla değiştirme.** Yoksa `python3 tools/indir.py [ders-id]` ile indir. |
| Wiki (içerik) | `dersler/**`, `reference/*.md` | Claude yazar ve günceller. |
| Katalog | `index.md`, `data/mufredat.json` | Elle düzenleme. `python3 tools/mufredat.py` üretir. |
| Günlük | `log.md` | Yalnızca sona ekle. Biçim: `## [YYYY-AA-GG] işlem | başlık` |
| Öğretim durumu | `MISSION.md`, `RESOURCES.md`, `NOTES.md`, `learning-records/` | /teach biçimleri geçerli. |
| Site | `*.html`, `assets/` | Ortak bileşenler `assets/` içinde; derse özel kod yazma. |

Müfredat MEBİ ile birebirdir: 13 ders, 231 konu, 740 alt konu. Her alt konu = bir ders dosyası + bir alıştırma dosyası.
Yolu `data/mufredat.json` içindeki `yol` alanı belirler: `<yol>.md` ve `<yol>.alistirma.md`. Dosya adını kendin uydurma.

## İş akışları

### Ders yaz (ingest)
1. `data/mufredat.json` içinden alt konuyu bul; `pdf` alanındaki kodla `raw/mebi/metin/<pdf>.txt` dosyasını **oku**. Ezberden yazma.
2. Aynı konudaki bir önceki dersi oku ("Önce hatırla" bölümü ona dayanır).
3. `<yol>.md` ve `<yol>.alistirma.md` dosyalarını aşağıdaki biçimde yaz.
4. `python3 tools/mufredat.py` çalıştır, `log.md` dosyasına bir satır ekle.
5. Doğrula: `python3 tools/denetle.py` hatasız bitmeli.

### Güncelle / düzelt
Yanlış bulunan soru ya da bilgi için yalnızca ilgili dosyayı düzelt (cerrahi değişiklik), `guncelleme` tarihini değiştir, `log.md`'ye yaz.

### Denetle (lint)
`python3 tools/denetle.py`: biçim, cevap anahtarı dağılımı, eksik dosya. Ayrıca istenirse içerik denetimi: derslerde çelişki, kaynakla uyumsuzluk, eksik çapraz bağlantı.

### Öğret (/teach)
Öğrenci soru sorduğunda `.claude/skills/teach/SKILL.md` geçerlidir. Bu repoya özgü farklar:
dersler HTML değil **Markdown**'dır ve `dersler/` altındadır; görünüm `assets/` bileşenlerinden gelir.
Öğrencinin kanıtlanmış kazanımı ya da düzeltilen yanılgısı için `learning-records/` kaydı aç.

## Ders biçimi (`<yol>.md`)

Ön madde: `baslik, ders, sure, kaynak, guncelleme`. Sonra sırayla:

1. `# Başlık` ve **"Bu dersin sonunda:"** tek cümlelik somut kazanım.
2. Alıntı kutusunda **sınavdaki yeri** (hangi soru kalıbı gelir).
3. `## Önce hatırla`: önceki dersten 1–2 geri çağırma sorusu, `<details>` içinde cevap (aralıklı tekrar).
4. Konu anlatımı: kısa bölümler, **tablolar**, formüller KaTeX (`$...$`, `$$...$$`). Bir ders 15–25 dakikada biter.
5. `## ÖSYM tuzakları`: alıntı kutularında tipik yanlışlar.
6. `## Kendini dene`: 3 soru (soru biçimi aşağıda).
7. `## Özet kartı`: en çok 6 madde.
8. `## Sonraki adım`.

Dil: öğrenciler 17 ve 19 yaşında; "sen" diye hitap et, kısa ve net yaz, çocukça ya da süslü anlatma.
Terimler MEB ders kitabındaki gibi kullanılır (örn. "ototrof (üretici)").

## Alıştırma biçimi (`<yol>.alistirma.md`)

10 soru, üç bölüm: `## Isınma` (3, Kolay), `## Orta` (3), `## ÖSYM tarzı` (4). Sayısal derslerde 12 soruya çıkılabilir.

```
### Soru 7 · ÖSYM tarzı
Soru kökü. Olumsuz ifadeler **kalın** yazılır.

A) …
B) …
C) …
D) …
E) …

**Cevap:** C
**Çözüm:** Neden doğru, çeldiriciler neden yanlış.
```

Kurallar:
- Beş seçenek (A–E), her biri kendi satırında, tek doğru cevap.
- Seçenekler benzer uzunlukta; doğru cevap biçimden anlaşılmasın. Doğru cevap harfleri dosya içinde dağılsın.
- Her sayısal sorunun çözümünü yazmadan önce **hesabı kendin yap ve kontrol et**.
- **ÖSYM çıkmış sorularını kopyalama.** ÖSYM soruları teliflidir. Sorular özgün olur, ÖSYM tarzında yazılır.
  Gerçek çıkmış sorular için site MEBİ'nin "Çıkmış Sorular" testine ve ÖSYM'nin resmî kitapçıklarına bağlantı verir.
- MEB konu özetlerini de kopyalama; kaynak olarak kullan, kendi cümlelerinle yaz.

## Gizlilik

Site herkese açıktır. Öğrencilerin adını, yaşını ya da kişisel bilgisini repoya yazma. İlerleme yalnızca öğrencinin tarayıcısında tutulur.

## Çalışma ilkeleri (Karpathy yönergeleri)

1. **Yazmadan önce düşün.** Varsayımını açık söyle; belirsizse sor; daha basit bir yol varsa öner.
2. **Önce sadelik.** İstenenden fazlasını yapma; tek kullanımlık soyutlama, istenmemiş ayar ekleme.
3. **Cerrahi değişiklik.** Yalnızca gerekeni değiştir; komşu içeriği "iyileştirme"; mevcut biçeme uy.
4. **Hedefe göre çalış.** Başarı ölçütünü tanımla, doğrulanana kadar döngüye devam et (burada: `tools/denetle.py` + sayfayı tarayıcıda aç).

## Yerelde çalıştırma

```
python3 -m http.server 8799     # sonra http://127.0.0.1:8799
```
