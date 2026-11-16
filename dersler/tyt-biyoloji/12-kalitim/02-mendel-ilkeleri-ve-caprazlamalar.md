---
baslik: Mendel İlkeleri ve Çaprazlamalar
ders: tyt-biyoloji
sure: 25 dk
kaynak: MEBİ Konu Özeti 3b0d17daba
guncelleme: 2026-11-16
---
# Mendel İlkeleri ve Çaprazlamalar

**Bu dersin sonunda:** monohibrit ve dihibrit çaprazlamaları kurup genotip ve fenotip oranlarını bulabilecek, çok karakterli çaprazlamalarda istenen yavrunun olasılığını "her karakteri ayrı çaprazla, sonra çarp" yöntemiyle hesaplayabilecek ve kontrol çaprazlamasının sonucunu yorumlayabileceksin.

> **TYT'de yeri:** Kalıtımın en çok soru çıkan dersidir. Kalıplar: "Bu çaprazlamadan şu genotipte/fenotipte yavru oluşma olasılığı kaçtır?", "Kaç çeşit genotip ve fenotip oluşur?", "Hangi sonuç hangi Mendel ilkesini destekler?" ve kontrol çaprazlaması yorumu.

## Önce hatırla

<details><summary>Geçen dersten: AaBbDD genotipli birey kaç çeşit gamet oluşturur? ABD gametini hangi olasılıkla oluşturur?</summary>
Heterozigot karakter sayısı 2 olduğundan $2^2 = 4$ çeşit gamet. ABD gametinin olasılığı $\frac{1}{2} \cdot \frac{1}{2} \cdot 1 = \frac{1}{4}$. Bugün iki bireyin gametlerini birleştireceksin; çarpım kuralı aynen geçerli.
</details>

## Mendel neden bezelye kullandı?

Mendel, bezelyelerle yaptığı çaprazlamalarla genetiğin temelini atmıştır. Bezelye bu iş için uygundur çünkü:

- hızlı ürer ve her nesilde çok sayıda yavru verir,
- erkek ve dişi organ aynı çiçekte olduğundan **kendi kendini dölleyebilir** (arı döl elde etmek kolaydır),
- yapay (çapraz) döllenmeye uygundur,
- gözle kolayca ayırt edilen, birbirine zıt özellikler taşır (Mendel yedi karakter seçmiştir: tohum şekli, tohum rengi, çiçek rengi gibi).

Çaprazlamalarda kullanılan kısaltmalar: **P** = ata (ebeveyn) bireyler, **G** = gametler, **F₁** = birinci kuşak, **F₂** = ikinci kuşak. Aynı genotipteki iki bireyin çaprazlanmasına **kendileştirme** denir.

## Monohibrit çaprazlama

Bir karakter bakımından heterozigot iki bireyin çaprazlanmasıdır (Aa × Aa).

**1. adım: arı döllerin çaprazlanması.** Mor çiçek aleli A (baskın), beyaz çiçek aleli a (çekinik) olsun.

$$\text{P: } AA \times aa \quad\Rightarrow\quad \text{G: } A \text{ ve } a \quad\Rightarrow\quad F_1\text{: tümü } Aa \text{ (mor)}$$

F₁'in tamamı mor çiçeklidir: beyaz alel vardır ama gizlenmiştir.

**2. adım: F₁ × F₁.** Gametleri Punnett karesine yerleştir: satırlara bir ebeveynin, sütunlara diğerinin gametleri yazılır; kutulara yavru genotipleri gelir.

| | A ($\frac{1}{2}$) | a ($\frac{1}{2}$) |
|---|---|---|
| **A** ($\frac{1}{2}$) | AA | Aa |
| **a** ($\frac{1}{2}$) | Aa | aa |

| Sonuç | Oran | Olasılık |
|---|---|---|
| Genotip | 1 AA : 2 Aa : 1 aa | $\frac{1}{4}$, $\frac{2}{4}$, $\frac{1}{4}$ |
| Fenotip | 3 mor : 1 beyaz | $\frac{3}{4}$, $\frac{1}{4}$ |

Ezberlemen gereken dört temel çaprazlama:

| Çaprazlama | Genotip oranı | Fenotip oranı (baskın : çekinik) |
|---|---|---|
| AA × aa | tümü Aa | tümü baskın |
| Aa × Aa | 1 AA : 2 Aa : 1 aa | 3 : 1 |
| Aa × aa | 1 Aa : 1 aa | 1 : 1 |
| AA × Aa | 1 AA : 1 Aa | tümü baskın |

## Dihibrit çaprazlama

İki karakter bakımından heterozigot iki bireyin çaprazlanmasıdır (SsDd × SsDd). Bezelyede sarı tohum S, yeşil tohum s; düzgün tohum D, buruşuk tohum d olsun.

$$\text{P: } SSDD \times ssdd \quad\Rightarrow\quad F_1\text{: tümü } SsDd \text{ (sarı, düzgün)}$$

Her F₁ bireyi dört çeşit gameti eşit olasılıkla oluşturur: SD, Sd, sD, sd (her biri $\frac{1}{4}$).

| | SD | Sd | sD | sd |
|---|---|---|---|---|
| **SD** | SSDD | SSDd | SsDD | SsDd |
| **Sd** | SSDd | SSdd | SsDd | Ssdd |
| **sD** | SsDD | SsDd | ssDD | ssDd |
| **sd** | SsDd | Ssdd | ssDd | ssdd |

16 kutuyu sayarsan F₂ fenotip oranı:

| Fenotip | Kutu sayısı | Olasılık |
|---|---|---|
| Sarı, düzgün | 9 | $\frac{9}{16}$ |
| Sarı, buruşuk | 3 | $\frac{3}{16}$ |
| Yeşil, düzgün | 3 | $\frac{3}{16}$ |
| Yeşil, buruşuk | 1 | $\frac{1}{16}$ |

Fenotip oranı **9 : 3 : 3 : 1**, genotip oranı 1 : 2 : 2 : 4 : 1 : 2 : 1 : 2 : 1 (dokuz çeşit genotip). Ebeveynlerde hiç görülmeyen sarı-buruşuk ve yeşil-düzgün bezelyelerin ortaya çıkması, iki karakterin alellerinin gametlere birbirinden bağımsız dağıldığını gösterir.

## Kısa yol: her karakteri ayrı çaprazla, sonra çarp

Sınavda 16 kutu çizmeye vaktin olmaz. Genler bağımsızsa her karakteri **tek başına** çaprazla, istenen sonucun olasılığını bul, sonra olasılıkları **çarp**.

**Çözümlü örnek 1.** AaBb × AaBb çaprazlamasından aaBb genotipli yavru oluşma olasılığı kaçtır?

- Aa × Aa → aa olasılığı $\frac{1}{4}$
- Bb × Bb → Bb olasılığı $\frac{2}{4} = \frac{1}{2}$
- Birlikte: $\frac{1}{4} \cdot \frac{1}{2} = \frac{1}{8}$

**Çözümlü örnek 2.** AaBbDd × AabbDd çaprazlamasından üç karakter bakımından da baskın fenotipli yavru oluşma olasılığı kaçtır?

- Aa × Aa → baskın fenotip $\frac{3}{4}$
- Bb × bb → baskın fenotip $\frac{1}{2}$
- Dd × Dd → baskın fenotip $\frac{3}{4}$
- Birlikte: $\frac{3}{4} \cdot \frac{1}{2} \cdot \frac{3}{4} = \frac{9}{32}$

**Çeşit sayıları da aynı yolla bulunur:** her karakterin verdiği çeşit sayılarını çarp.

**Çözümlü örnek 3.** AaBb × aaBb çaprazlamasında kaç çeşit genotip ve fenotip oluşur?

- Aa × aa → 2 genotip (Aa, aa), 2 fenotip
- Bb × Bb → 3 genotip (BB, Bb, bb), 2 fenotip
- Genotip çeşidi: $2 \cdot 3 = 6$; fenotip çeşidi: $2 \cdot 2 = 4$

İki ebeveyn de **aynı** $n$ karakter bakımından heterozigotsa (kendileştirme gibi) hazır formüller kullanılabilir:

| İstenen | Formül | AaBb × AaBb için |
|---|---|---|
| Fenotip çeşidi | $2^n$ | $2^2 = 4$ |
| Genotip çeşidi | $3^n$ | $3^2 = 9$ |
| Punnett karesindeki kutu (birleşme) sayısı | $4^n$ | $4^2 = 16$ |

## Kontrol (test) çaprazlaması

Baskın fenotipli bir bireyin homozigot mu (DD) yoksa heterozigot mu (Dd) olduğunu anlamak için yapılır. Birey, **homozigot çekinik** (dd) bir bireyle çaprazlanır.

| Bilinmeyen birey | Çaprazlama | Yavrular |
|---|---|---|
| DD ise | DD × dd | Tümü baskın fenotipli (Dd) |
| Dd ise | Dd × dd | $\frac{1}{2}$ baskın (Dd), $\frac{1}{2}$ çekinik (dd) |

- Yavrular arasında **tek bir çekinik fenotipli** birey bile varsa bilinmeyen birey **kesinlikle heterozigottur**.
- Yavruların hepsi baskın fenotipliyse birey **büyük olasılıkla** homozigottur (yavru sayısı arttıkça güven artar, ama kesinlik yoktur).

## Mendel ilkeleri

| İlke | Ne söyler? | Dayanağı |
|---|---|---|
| **Baskınlık** | Heterozigot bireyde alellerden yalnızca biri (baskın olan) fenotipte etkisini gösterir. | Aa mor çiçeklidir. |
| **Benzerlik** | Bir karakter bakımından farklı iki arı dölün çaprazlanmasından oluşan F₁ bireylerinin hepsi birbirine benzer. | AA × aa → tümü Aa |
| **Ayrılma** | Bir alel çiftinin üyeleri mayozda birbirinden ayrılır ve gametlere eşit olasılıkla gider; gamet her çiftten yalnız bir alel taşır. | Aa → $\frac{1}{2}$ A, $\frac{1}{2}$ a |
| **Bağımsız açılım** | Farklı karakterleri kontrol eden genler gametlere birbirinden bağımsız dağılır. Nedeni, homolog kromozom çiftlerinin mayozda bağımsız ayrılmasıdır. | SsDd → SD, Sd, sD, sd |

Mendel ilkeleri **bağımsız genler** için geçerlidir. Bağlı genler bağımsız açılım ilkesine uymaz.

## ÖSYM tuzakları

> **"Baskın fenotipli yavrular arasından seçilen birey" denirse payda değişir.** Aa × Aa çaprazlamasında herhangi bir yavrunun heterozigot olma olasılığı $\frac{2}{4}$'tür. Ama yavrunun baskın fenotipli olduğu **biliniyorsa** aa ihtimali elenir: geriye 1 AA ve 2 Aa kalır, olasılık $\frac{2}{3}$ olur.

> **Oran, kesin sayı değildir.** 3 : 1 oranı çok sayıda yavruda beklenen dağılımdır. Dört yavrunun üçü baskın, biri çekinik olmak zorunda değildir; her yavru bir öncekinden bağımsızdır.

> **$2^n$ ve $3^n$ formülleri her çaprazlamada kullanılmaz.** Yalnızca iki ebeveyn de aynı karakterler bakımından heterozigotsa geçerlidir. AaBb × aaBb gibi durumlarda her karakteri ayrı hesaplayıp çarp.

> **Kontrol çaprazlamasında oran $\frac{1}{2}$'dir, $\frac{1}{4}$ değil.** Dd × dd çaprazlamasında çekinik fenotipli yavru olasılığı %50'dir. %25, Dd × Dd çaprazlamasına aittir.

## Kendini dene

### Soru 1
Homozigot baskın bir bezelye ile homozigot çekinik bir bezelyenin çaprazlanmasından oluşan F₁ bireyleri için aşağıdakilerden hangisi doğrudur?

A) Yarısı baskın, yarısı çekinik fenotiplidir.
B) Tamamı homozigot baskın genotiplidir.
C) Dörtte biri çekinik fenotiplidir.
D) Tamamı heterozigot genotiplidir.
E) Üç farklı genotip görülür.

**Cevap:** D
**Çözüm:** AA yalnızca A, aa yalnızca a gameti verir. Yavruların tamamı Aa genotipli ve baskın fenotiplidir (benzerlik ilkesi).

### Soru 2
Aa × Aa çaprazlamasından homozigot çekinik bir yavru oluşma olasılığı kaçtır?

A) $\frac{1}{4}$
B) $\frac{1}{2}$
C) $\frac{3}{4}$
D) $\frac{1}{8}$
E) $\frac{2}{3}$

**Cevap:** A
**Çözüm:** Her ebeveyn a gametini $\frac{1}{2}$ olasılıkla verir: $\frac{1}{2} \cdot \frac{1}{2} = \frac{1}{4}$. Punnett karesindeki dört kutudan yalnızca biri aa'dır.

### Soru 3
Genleri bağımsız olan AaBb genotipli iki bireyin çaprazlanmasından oluşabilecek fenotip ve genotip çeşidi sayıları sırasıyla aşağıdakilerin hangisinde verilmiştir?

A) 2 – 4
B) 4 – 4
C) 4 – 16
D) 9 – 16
E) 4 – 9

**Cevap:** E
**Çözüm:** Her karakter 2 fenotip ve 3 genotip verir. Fenotip çeşidi $2 \cdot 2 = 4$, genotip çeşidi $3 \cdot 3 = 9$. 16, Punnett karesindeki kutu sayısıdır; çeşit sayısı değildir.

## Özet kartı

- Aa × Aa: genotip 1 : 2 : 1, fenotip 3 : 1. Aa × aa: 1 : 1.
- AaBb × AaBb: fenotip 9 : 3 : 3 : 1; 4 fenotip, 9 genotip, 16 kutu.
- Çok karakterde: her karakteri ayrı çaprazla, olasılıkları (ya da çeşit sayılarını) çarp.
- Kontrol çaprazlaması: bilinmeyen baskın birey × homozigot çekinik; çekinik yavru çıkarsa kesin heterozigot.
- İlkeler: baskınlık, benzerlik, ayrılma, bağımsız açılım; yalnızca bağımsız genlerde geçerli.
- "Baskın fenotipliler arasından" denirse payda 3 olur: heterozigot olasılığı $\frac{2}{3}$.

## Sonraki adım

Alıştırmaya geç (aşağıdaki düğme).
