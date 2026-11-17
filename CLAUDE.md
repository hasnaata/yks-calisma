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

1. `# Başlık`, hemen altında **Arapça giriş kutusu** (aşağıda), sonra **"Bu dersin sonunda:"** tek cümlelik somut kazanım.
2. Alıntı kutusunda **sınavdaki yeri** (hangi soru kalıbı gelir).
3. `## Önce hatırla`: önceki dersten 1–2 geri çağırma sorusu, `<details>` içinde cevap (aralıklı tekrar).
4. Konu anlatımı: kısa bölümler, **görseller** (aşağıdaki kurallar), **tablolar**, formüller KaTeX (`$...$`, `$$...$$`). Bir ders 15–25 dakikada biter.
5. `## ÖSYM tuzakları`: alıntı kutularında tipik yanlışlar.
6. `## Kendini dene`: 3 soru (soru biçimi aşağıda).
7. `## Özet kartı`: en çok 6 madde.
8. `## Sonraki adım`.

### Arapça giriş kutusu

Her dersin başında, `# Başlık` satırının hemen altında, öğrenciler ve velileri için **Mısır Arapçası (ammiye)** ile yazılmış kısa bir tanıtım bulunur. Dersin geri kalanı Türkçe kalır.

```
<div class="giris" dir="rtl" lang="ar">

**الدرس ده عن إيه؟** …

- هتعرف …
- هتتعلم …

**ليه مهم؟** …

</div>
```

- 6–8 kısa satır: ders ne hakkında, öğrenci ne öğrenecek (2–3 madde), sınavda neden önemli, bir cümle teşvik. Açılış ve kapanış etiketinden sonra/önce boş satır bırak (içi Markdown olarak işlenir).
- Doğal, sıcak Mısır lehçesi (fusha değil); abartılı ya da çocukça olmasın. İsim, yaş, kişisel bilgi yazma.
- Sınavda geçecek ana terimler **Türkçe** (Latin harfleriyle) kalır; ilk geçtiği yerde Arapça karşılığı yanında verilir: `الكربوهيدرات (karbonhidratlar)`. Formül ve `$` kullanma.
- Yalnızca dersin kendisinde olan bilgiyi söyle; yeni bilgi ekleme.

Dil: öğrenciler 17 ve 19 yaşında; "sen" diye hitap et, kısa ve net yaz, çocukça ya da süslü anlatma.
Terimler MEB ders kitabındaki gibi kullanılır (örn. "ototrof (üretici)").

## Görseller

Yalnızca metin yetmez: her derste **3–5 görsel** bulunur. Site açık temalıdır (koyu tema yok).

| Tür | Ne zaman | Nasıl |
|---|---|---|
| Şema | Sınıflandırma, süreç, döngü, karşılaştırma | **Pele** (`mcp__pele__render_mermaid`, `theme: light`) ile `.svg`; Mermaid kaynağı aynı adla `.mmd` olarak saklanır; sonra `python3 tools/gorsel.py renk <dosya>` |
| Fotoğraf, mikroskop görüntüsü, 3B model | Gerçek canlı, yapı, molekül, olay | `python3 tools/gorsel.py ara "..."` (İngilizce ara), `python3 tools/gorsel.py indir "File:..." <hedef>` |

- Dosya yeri ve adı: `gorsel/<ders-id>/<konu no>-<alt konu no>-<kisa-ad>.<uzantı>` (örn. `gorsel/tyt-biyoloji/03-01-glikoz-3b.png`).
- Derse ekleme, kendi paragrafında tek satır: `![Görseli görmeyen için açıklama](gorsel/.../ad.svg "Alt yazı: öğrenci neye bakmalı?")`. Alt yazıda çift tırnak kullanma.
- **Şemalar sade olur:** en çok 9 kutu, kutu başına en çok 4 kelime, mümkünse yukarıdan aşağı (`flowchart TD`), doğal genişlik 700 pikseli geçmez. Tabloyu şemaya kopyalama; şema yalnızca iskeleti gösterir. Vurgu için `classDef` ile site renkleri kullanılabilir (`#1f5fbf`, `#e8f0fc`, `#e3f4e9/#1c7c45`, `#fdf3d8/#8a5a00`, `#fbe9e7/#b3261e`).
- **Yalnızca özgür lisanslı görsel** (Wikimedia Commons: kamu malı, CC0, CC BY, CC BY-SA). Google'dan ya da başka siteden görsel alma. `indir` komutu lisansı denetler ve `gorsel/ATIF.md` dosyasına atıf yazar; CC BY ve CC BY-SA görsellerde alt yazının sonuna da `Görsel: Yazar, Lisans.` ekle.
- Üzerinde Türkçe olmayan etiket bulunan çizimleri kullanma (tek harf ve simge olabilir). Etiketli yapı gerekiyorsa şemayı kendin üret.
- Her görseli eklemeden önce **gör**: fotoğraf dosyasını aç; şema için `python3 tools/gorsel.py bak <dosya>` çıktısındaki PNG'ye bak (telefon boyutu). Yazı okunmuyor, taşıyor ya da görsel dersteki bilgiyle çelişiyorsa kullanma.
- Örnek ders: `dersler/tyt-biyoloji/03-canlilarin-yapisinda-bulunan-organik-bilesikler/01-organik-bilesiklerin-genel-ozellikleri-karbonhidratlar.md`.

### Matematik ve geometri şekilleri

Grafik, sayı doğrusu, Venn şeması, geometrik şekil gibi **ölçülü** çizimler Pele ile değil **matplotlib** ile üretilir.

- Kaynak: `gorsel/<ders-id>/<ad>.py`; ortak stil `tools/cizim.py` (başındaki açıklamayı oku: `sekil`, `eksenler`, `sayi_dogrusu`, `nokta`, `aci`, `kaydet`, renk sabitleri). Çalıştırma: `.venv/bin/python gorsel/<ders-id>/<ad>.py` (aynı adla `.svg` üretir). `.py` kaynağı depoda kalır.
- Şekil **doğru ölçekli** olur: verilen uzunluk ve açılar gerçekten o değerlerde çizilir; "şekil ölçekli değildir" gerektiren çizim yapma. Köşe adları (A, B, C), verilen uzunluklar ve açılar etiketlenir; etiketler çizgilerin üstüne binmez.
- Yazı Türkçe; ondalık ayırıcı virgül; eksi işareti "−". Renkler `cizim.py` sabitlerinden.
- Geometri derslerinde **her kural için bir şekil** bulunur; şekle dayanan sorularda (derste ve alıştırmada) şekil soruya eklenir. Bir soru şekilsiz anlaşılmıyorsa şekli olmadan yazma.
- Pele şemaları matematikte yalnızca kavram haritası, karar adımları ve yöntem akışı için kullanılır.
- Gerçek fotoğraf yalnızca konuyu günlük hayata bağlıyorsa eklenir (zorunlu değil). Matematik derslerinde görsel sayısı 2–5.

### Matematik yazımı

- Bütün matematik KaTeX ile: `$...$` satır içi, `$$...$$` blok. Ondalık sayı `$2{,}5$`, çarpma `\cdot`, kesir `\frac{a}{b}`.
- Her kural için önce **çözümlü örnek**, sonra kural. Çözümler adım adım yazılır.
- Sayısal her sonucu yazmadan önce hesapla **doğrula** (`.venv/bin/python` ile `sympy` ya da doğrudan hesap). Alıştırmalar 12 soru: 3 Kolay, 4 Orta, 5 ÖSYM tarzı.
- ÖSYM tarzı sorular TYT'nin "yeni nesil" biçimindedir: kısa bir günlük hayat durumu ya da tanımlanan bir işlem verilir, işlem yükü azdır, akıl yürütme ister.
- Seçenekler küçükten büyüğe sıralanır (ÖSYM böyle yapar); doğru cevap harfleri dosya içinde dağılır.
- Kör denetim: `python3 tools/kor.py <yol>` alıştırmayı cevapsız yazdırır.

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
