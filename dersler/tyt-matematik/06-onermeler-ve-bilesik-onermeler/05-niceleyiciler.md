---
baslik: Niceleyiciler
ders: tyt-matematik
sure: 20 dk
kaynak: MEBİ Konu Özeti 2f5c308f94
guncelleme: 2026-11-18
---
# Niceleyiciler

<div class="giris" dir="rtl" lang="ar">

**الدرس ده عن إيه؟** عن الكلمتين "كل" و"بعض" في المنطق، يعني المُكمِّمات (niceleyiciler)، وإزاي بيحوّلوا جملة فيها متغير لعبارة نقدر نقول عليها صح أو غلط.

- هتعرف يعني إيه العبارة المفتوحة (açık önerme)، وإزاي تطلّع مجموعة الصدق بتاعتها (doğruluk kümesi)، وليه بتفرق لو المتغير عدد طبيعي ولا عدد صحيح.
- هتفهم إن جملة "لكل" (her) بيوقّعها مثال مضاد (karşı örnek) واحد بس، وجملة "بعض" (bazı) بيكفّيها مثال واحد عشان تبقى صح.
- هتتعلم تكتب النفي (değili) صح: "كل" بتبقى "بعض"، والشرط نفسه بيتعكس، والمجموعة الشاملة بتفضل زي ما هي.

**ليه مهم؟** في TYT بييجي سؤال "أنهي عبارة صح؟" أو "نفي العبارة دي إيه؟"، وغلطة مشهورة إن نفي "كل" يبقى "ولا واحد"، وده غلط هتتعلم تتجنبه.

الدرس ٢٠ دقيقة بس، ولو مسكت الفكرة دي هتلاقي الأسئلة دي سهلة جدًا.

</div>

**Bu dersin sonunda:** bir açık önermenin doğruluk kümesini bulabilecek, "her" ($\forall$) ve "bazı" ($\exists$) ile kurulan önermelerin doğru mu yanlış mı olduğuna karar verebilecek ve bu önermelerin değilini doğru yazabileceksin.

> **TYT'de yeri:** Üç kalıp gelir: "Aşağıdaki önermelerden hangisi doğrudur?" (her seçenekte bir $\forall$ ya da $\exists$), "Önermenin değili hangisidir?" ve "Açık önermenin doğruluk kümesi kaç elemanlıdır?" Günlük dilde de sorulur: "Her öğrenci…" cümlesinin değilini seçmen istenir.

## Önce hatırla

<details><summary>İki yönlü koşullu önermeden: p ≡ 1 ve q ≡ 0 ise p ⇔ q ve p′ ⇔ q önermelerinin doğruluk değerleri nedir?</summary>
"Ancak ve ancak" bağlacı, iki taraf <b>aynı</b> değerdeyse 1, farklıysa 0 verir. $p \Leftrightarrow q \equiv 1 \Leftrightarrow 0 \equiv 0$. $p' \Leftrightarrow q \equiv 0 \Leftrightarrow 0 \equiv 1$. Bu, $(p \Leftrightarrow q)' \equiv p' \Leftrightarrow q$ özelliğine bir örnektir.
</details>

<details><summary>İki yönlü koşullu önermeden: p ⇔ q önermesini iki "ise" önermesiyle yaz. p ≡ 0, q ≡ 1 için değeri nedir?</summary>
$p \Leftrightarrow q \equiv (p \Rightarrow q) \wedge (q \Rightarrow p)$. Burada $p \Rightarrow q \equiv 0 \Rightarrow 1 \equiv 1$, $q \Rightarrow p \equiv 1 \Rightarrow 0 \equiv 0$. "Ve" bağlacında biri 0 ise sonuç <b>0</b>.
</details>

## Açık önerme ve doğruluk kümesi

**Örnek.** $x$ bir tam sayı olsun ve $p(x)$: "$x^2 < 10$" verilsin.

Bu cümle $x$ bilinmeden ne doğru ne yanlıştır; $x$'e değer verince karar verilir:

- $p(3)$: $9 < 10$, doğru. $p(3) \equiv 1$.
- $p(4)$: $16 < 10$, yanlış. $p(4) \equiv 0$.
- $p(-3)$: $9 < 10$, doğru. $p(-3) \equiv 1$.

$p(x)$'i doğru yapan tam sayıların hepsi: $\{-3, -2, -1, 0, 1, 2, 3\}$. Yedi eleman.

Aynı soruda $x$ bir **doğal sayı** olsaydı negatifler hiç aday olmazdı: $\{0, 1, 2, 3\}$, dört eleman.

![İki sayı doğrusu. Üstte x tam sayı: eksi 3'ten 3'e kadar yedi nokta dolu, eksi 5, eksi 4, 4 ve 5 boş. Altta x doğal sayı: yalnızca 0, 1, 2, 3 dolu; negatif sayılarda nokta yok.](gorsel/tyt-matematik/06-05-dogruluk-kumesi.svg "Açık önerme aynı, x'in alındığı küme farklı. Doğal sayılarda negatifler hiç aday değildir, bu yüzden doğruluk kümesi küçülür.")

**Kural.**

- İçinde değişken bulunan ve değişkene verilen değere göre doğru ya da yanlış olan ifadeye **açık önerme** denir; $p(x)$ ile gösterilir.
- $p(x)$'i doğru yapan elemanların kümesi, $p(x)$'in **doğruluk kümesidir**. $a$ bu kümedeyse $p(a) \equiv 1$, değilse $p(a) \equiv 0$.
- Her denklem ve eşitsizlik bir açık önermedir; **çözüm kümesi doğruluk kümesidir.** Örneğin $x \in \mathbb{R}$ için "$2x - 1 = 7$" önermesinin doğruluk kümesi $\{4\}$, "$x^2 + 1 = 0$" önermesininki $\varnothing$'dir.
- Doğruluk kümesi, $x$'in hangi kümeden ($\mathbb{N}$, $\mathbb{Z}$, $\mathbb{R}$…) seçildiğine bağlıdır. Bu kümeye **evrensel küme** ($E$) denir.

### Bileşik açık önermeler

**Örnek.** $E = \{1, 2, \dots, 10\}$, $p(x)$: "$x$ asaldır", $q(x)$: "$x$ tektir".

Doğruluk kümeleri: $P = \{2, 3, 5, 7\}$ ve $Q = \{1, 3, 5, 7, 9\}$.

![E kümesi 1'den 10'a. p asal dairesi ve q tek dairesi kesişiyor. Yalnız p bölgesinde 2, kesişimde 3, 5, 7, yalnız q bölgesinde 1 ve 9, dışarıda 4, 6, 8, 10.](gorsel/tyt-matematik/06-05-venn.svg "Yeşil bölge p(x) ∧ q(x) önermesinin doğruluk kümesidir. Asal olup tek olmayan yalnızca 2'dir.")

- $p(x) \wedge q(x)$: iki koşul birlikte, yani kesişim: $\{3, 5, 7\}$.
- $p(x) \vee q(x)$: en az biri, yani birleşim: $\{1, 2, 3, 5, 7, 9\}$.
- $p(x) \wedge q'(x)$: asal ama tek değil: $\{2\}$.

**Kural.** "Ve" kesişimdir, "veya" birleşimdir, değil ($p'(x)$) ise $E$ içinde tümleyendir.

## "Her" ve "bazı" niceleyicileri

**Örnek.** Dört önermeye bak. Artık $x$'e tek tek değer vermiyoruz; cümle bütün kümeden söz ediyor.

| Önerme | Okunuşu | Değer | Neden? |
|---|---|---|---|
| $\forall x \in \mathbb{Z},\ x^2 \ge 0$ | Her tam sayının karesi 0'dan büyük ya da 0'a eşittir. | 1 | İstisna yok. |
| $\forall x \in \mathbb{Z},\ x^2 > 0$ | Her tam sayının karesi 0'dan büyüktür. | 0 | $x = 0$ için $0 > 0$ yanlış. |
| $\exists x \in \mathbb{Z},\ x + 7 = 3$ | Bazı tam sayıların 7 fazlası 3'tür. | 1 | $x = -4$ |
| $\exists x \in \mathbb{N},\ x + 7 = 3$ | Bazı doğal sayıların 7 fazlası 3'tür. | 0 | $-4 \notin \mathbb{N}$, başka aday yok. |

İkinci satırı **tek bir sayı** (0) çürüttü. Üçüncü satırı **tek bir sayı** ($-4$) doğruladı.

![Dört kutu. Her kutu evrensel küme, mavi daireli noktalar doğruluk kümesinde. Her için: bütün noktalar içerideyse 1, bir nokta dışarıdaysa 0. Bazı için: bir nokta içerideyse 1, hiçbiri içeride değilse 0.](gorsel/tyt-matematik/06-05-her-bazi.svg "D, doğruluk kümesidir. Her: tek bir istisna yeter, önerme yanlış olur. Bazı: tek bir örnek yeter, önerme doğru olur.")

**Kural.**

- **Her** (bütün, tamamı) anlamındaki $\forall$ simgesine **evrensel niceleyici** denir. $\forall x,\ p(x)$ ancak doğruluk kümesi $E$'nin tamamıysa doğrudur. Yanlış olduğunu göstermek için **bir karşı örnek** yeter.
- **Bazı** (en az bir) anlamındaki $\exists$ simgesine **varlıksal niceleyici** denir. $\exists x,\ p(x)$ ancak doğruluk kümesi boş değilse doğrudur. Doğru olduğunu göstermek için **bir örnek** yeter.
- Niceleyici, açık önermeyi önermeye çevirir: "$x^2 > 0$" açık önermedir, "$\forall x \in \mathbb{Z},\ x^2 > 0$" ise yanlış bir önermedir.
- "Bazı" kelimesi "en az bir" demektir; "birden çok" ya da "hepsi değil" demek değildir.

Sembolden cümleye çevirirken sırayı koru: önce niceleyici ve küme, sonra koşul. Örneğin $\forall x \in \mathbb{Z}^-,\ x^3 < 0$: "Her negatif tam sayının küpü sıfırdan küçüktür." ve $\exists x \in \mathbb{R},\ 2x - 3 \ge 5$: "Bazı gerçek sayıların 2 katının 3 eksiği 5'e eşit ya da 5'ten büyüktür."

## Niceleyicili önermenin değili

**Örnek 1.** $\forall x \in \mathbb{R},\ x^2 + 1 > 2x$ önermesinin değilini yaz ve hangisinin doğru olduğunu bul.

"Her sayı bunu sağlar" sözünü çürütmek için "sağlamayan en az bir sayı var" demek gerekir:

$$\left(\forall x \in \mathbb{R},\ x^2 + 1 > 2x\right)' \equiv \exists x \in \mathbb{R},\ x^2 + 1 \le 2x$$

$x = 1$ için $2 \le 2$ doğrudur; değili 1, asıl önerme 0'dır. (Kontrol: $x^2 + 1 - 2x = (x - 1)^2$ ve bu $x = 1$ için sıfırdır.)

![Üst satırda her x gerçek sayı için x kare artı 1 büyüktür 2x. Alt satırda bazı x için x kare artı 1 küçük eşittir 2x. Her işaretinden bazı işaretine ve büyüktür işaretinden küçük eşittir işaretine kırmızı ok; küme ve ifadeler aynı kalıyor.](gorsel/tyt-matematik/06-05-degil-alma.svg "Değil alırken yalnızca iki şey değişir: niceleyici ve koşul. Evrensel küme ile ifadeler olduğu gibi kalır.")

**Örnek 2.** $\exists x \in \mathbb{Z},\ (x > 2 \wedge x \le 5)$ önermesinin değili nedir?

Niceleyici döner, içteki "ve" önermesine De Morgan uygulanır:

$$\forall x \in \mathbb{Z},\ (x \le 2 \vee x > 5)$$

Asıl önerme doğrudur ($x = 3$), değili yanlıştır ($x = 3$ karşı örnek).

**Kural.**

$$\left(\forall x,\ p(x)\right)' \equiv \exists x,\ p'(x) \qquad \left(\exists x,\ p(x)\right)' \equiv \forall x,\ p'(x)$$

| Gösterim | $\forall$ | $\exists$ | $=$ | $\ne$ | $<$ | $>$ | $\le$ | $\ge$ | $\wedge$ | $\vee$ |
|---|---|---|---|---|---|---|---|---|---|---|
| Değili | $\exists$ | $\forall$ | $\ne$ | $=$ | $\ge$ | $\le$ | $>$ | $<$ | $\vee$ | $\wedge$ |

- Evrensel küme ($x \in \mathbb{R}$ kısmı) **değişmez**.
- İçeride "ise" varsa Koşullu Önerme dersindeki kuralı kullan: $(p \Rightarrow q)' \equiv p \wedge q'$.
- Bir önerme ile değilinden **tam olarak biri** doğrudur. Bulduğun değili bu yolla kontrol edebilirsin.

Günlük dilde: "Bu sınıftaki her öğrenci gözlük takar." önermesinin değili "Bu sınıftaki bazı öğrenciler gözlük takmaz." (en az bir öğrenci gözlük takmaz) olur. "Hiçbir öğrenci gözlük takmaz." değildir. "Hiçbir $x$ için $p(x)$" demek "$\forall x,\ p'(x)$" demektir.

## ÖSYM tuzakları

> **"Her"in değilini "hiçbir" yazmak:** "Her öğrenci geçti." önermesinin değili "Hiçbir öğrenci geçmedi." değil, "Bazı öğrenciler geçmedi." önermesidir. Tek bir kalan öğrenci önermeyi yanlış yapar.

> **Yalnızca niceleyiciyi çevirmek:** $(\forall x,\ x > 3)'$ için "$\exists x,\ x > 3$" yazmak yanlıştır. Niceleyici **ve** koşul birlikte değişir: $\exists x,\ x \le 3$.

> **$>$ işaretinin değilini $<$ yazmak:** Eşitlik durumu değile geçer: $>$ olur $\le$, $<$ olur $\ge$.

> **Evrensel kümeyi gözden kaçırmak:** $\forall x \in \mathbb{N},\ x \ge 1$ yanlıştır, çünkü $0 \in \mathbb{N}$. $\exists x \in \mathbb{Z},\ 2x = 5$ yanlıştır, çünkü $2{,}5 \notin \mathbb{Z}$. Önce $x$'in nereden seçildiğine bak.

> **Bir örnekle "her" önermesini doğrulamak:** $\forall x$ önermesini birkaç sayıda denemek yetmez; tek bir istisna yeter. Tersine, $\exists x$ önermesi için tek bir örnek bulman yeterlidir.

## Kendini dene

### Soru 1
$x$ bir doğal sayı olmak üzere $p(x)$: "$3x - 2 < 10$" açık önermesinin doğruluk kümesi kaç elemanlıdır?

A) 3
B) 4
C) 5
D) 6
E) 7

**Cevap:** B
**Çözüm:** $3x - 2 < 10 \Rightarrow 3x < 12 \Rightarrow x < 4$. Doğal sayılar: $0, 1, 2, 3$; toplam 4. $0$'ı unutan 3, $x \le 4$ alan 5 bulur.

### Soru 2
Aşağıdaki önermelerden hangisinin doğruluk değeri 1'dir?

A) $\forall x \in \mathbb{N},\ x > 0$
B) $\exists x \in \mathbb{Z},\ x^2 = 2$
C) $\forall x \in \mathbb{R},\ x^2 > x$
D) $\exists x \in \mathbb{N},\ x + 4 = 1$
E) $\exists x \in \mathbb{Z},\ 2x + 1 = -5$

**Cevap:** E
**Çözüm:** E) $2x = -6$, $x = -3 \in \mathbb{Z}$; bir örnek yeter, doğru. A) $x = 0$ karşı örnek. B) $x^2 = 2$ ise $x = \pm\sqrt{2}$, tam sayı değil. C) $x = 0$ için $0 > 0$ yanlış (ya da $x = \frac{1}{2}$: $\frac{1}{4} > \frac{1}{2}$ yanlış). D) $x = -3 \notin \mathbb{N}$.

### Soru 3
$\exists x \in \mathbb{Z},\ (x^2 = 4 \wedge x < 0)$ önermesinin değili aşağıdakilerden hangisidir?

A) $\forall x \in \mathbb{Z},\ (x^2 \ne 4 \wedge x \ge 0)$
B) $\exists x \in \mathbb{Z},\ (x^2 \ne 4 \vee x \ge 0)$
C) $\forall x \in \mathbb{Z},\ (x^2 \ne 4 \vee x \ge 0)$
D) $\forall x \in \mathbb{Z},\ (x^2 \ne 4 \vee x > 0)$
E) $\exists x \in \mathbb{Z},\ (x^2 = 4 \vee x \ge 0)$

**Cevap:** C
**Çözüm:** $\exists$ olur $\forall$; içte De Morgan: $=$ olur $\ne$, $<$ olur $\ge$, $\wedge$ olur $\vee$. Sonuç C. A'da "ve" çevrilmemiş, B ve E'de niceleyici çevrilmemiş, D'de $<$ işaretinin değili $>$ yazılmış.

## Özet kartı

- Açık önermenin doğruluk kümesi = onu doğru yapan elemanlar = denklemin ya da eşitsizliğin çözüm kümesi. $E$'ye ($\mathbb{N}$, $\mathbb{Z}$, $\mathbb{R}$) dikkat et.
- $p(x) \wedge q(x)$ kesişim, $p(x) \vee q(x)$ birleşim, $p'(x)$ tümleyen.
- $\forall x,\ p(x)$: doğruluk kümesi $E$'nin tamamı olmalı; bir karşı örnek onu yanlış yapar.
- $\exists x,\ p(x)$: doğruluk kümesi boş olmamalı; bir örnek onu doğru yapar.
- $(\forall x,\ p(x))' \equiv \exists x,\ p'(x)$ ve $(\exists x,\ p(x))' \equiv \forall x,\ p'(x)$; küme aynı kalır.
- $>$ değili $\le$, $<$ değili $\ge$; "her"in değili "hiçbir" değil, "bazı … değil".

## Sonraki adım

Alıştırmaya geç (aşağıdaki düğme). Sonraki ders **Tanım, Aksiyom, Teorem ve İspat Kavramları**; "ise" önermelerinin matematikte teorem olarak nasıl kullanıldığını ve ispatın ne demek olduğunu göreceksin.
