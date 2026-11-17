---
baslik: Bir Fonksiyonun Tersi
ders: tyt-matematik
sure: 25 dk
kaynak: MEBİ Konu Özeti 9f29a60f53
guncelleme: 2026-11-18
---
# Bir Fonksiyonun Tersi

<div class="giris" dir="rtl" lang="ar">

**الدرس ده عن إيه؟** عن الدالة العكسية (ters fonksiyon): إزاي ترجّع الدالة من النتيجة للرقم اللي دخل فيها، كأنك بتلغي العملية.

- هتعرف إمتى الدالة يبقى ليها عكسية: لازم تكون أحادية وشاملة (bire bir ve örten).
- هتتعلم تجيب قاعدة العكسية، وتحسب قيمة واحدة منها من غير ما تجيب القاعدة، وتستخدم طريقة مختصرة للدالة الكسرية (kesirli fonksiyon).
- هتشوف العكسية مع تركيب الدوال (bileşke)، وإن رسمتها بتبقى متماثلة مع رسمة الدالة حوالين منصّف الربع الأول والتالت.

**ليه مهم؟** في TYT بييجي سؤال مباشر على قيمة العكسية، أو سؤال من الجيل الجديد فيه عملية لازم ترجعها لورا، وأشهر غلطة إنك تحسب الدالة نفسها بدل عكسيتها.

الدرس ٢٥ دقيقة، وكل قاعدة فيه معاها مثال محلول خطوة بخطوة. خدها بالراحة وهتلاقيها سهلة.

</div>

**Bu dersin sonunda:** bire bir ve örten bir fonksiyonun tersini kuraldan, ok şemasından ve grafikten bulabilecek, $f^{-1}(a)$ değerini kuralı bulmadan hesaplayabilecek ve tersi bileşke sorularında kullanabileceksin.

> **TYT'de yeri:** "$f(x) = 3x - 2$ ise $f^{-1}(7)$ kaçtır?" gibi doğrudan değer soruları, $f^{-1}(x)$ kuralının seçeneklerden seçilmesi, $(f \circ g)^{-1}$ ve $f \circ f^{-1}$ içeren bileşke soruları, grafikten $f^{-1}$ değeri okuma. Yeni nesil sorularda ters fonksiyon, bir işlemi geri almak olarak gelir: ödenen ücretten gidilen yolu, ekrandaki sonuçtan girilen sayıyı bulmak gibi.

## Önce hatırla

<details><summary>İki fonksiyonun bileşkesinden: $f(x) = x + 4$ ve $g(x) = 3x$ ise $(g \circ f)(2)$ kaçtır?</summary>
Sağdan sola: önce içteki $f$. $f(2) = 6$, sonra $g(6) = 18$. Sonuç $18$. Ters sırada ($f$'yi dışta) hesaplasaydın $f\big(g(2)\big) = f(6) = 10$ bulurdun.
</details>

<details><summary>İki fonksiyonun bileşkesinden: $f(x - 1) = 2x + 3$ ise $f(x)$ nedir?</summary>
Dıştaki $f$ bilinmiyor; içi $t$'ye eşitle: $x - 1 = t$, $x = t + 1$. $f(t) = 2(t + 1) + 3 = 2t + 5$, yani $f(x) = 2x + 5$. Kontrol: $f(x - 1) = 2(x - 1) + 5 = 2x + 3$. Bu "içi $t$'ye eşitle, $x$'i çek" adımı bugün ters fonksiyonun da temeli olacak.
</details>

## Ters fonksiyon nedir?

**Örnek.** $A = \{1, 2, 3\}$, $B = \{1, 4, 7\}$ ve $f\colon A \to B$, $f(x) = 3x - 2$ olsun. $f(1) = 1$, $f(2) = 4$, $f(3) = 7$. Şimdi okların hepsini **ters çevir**: $B$'deki her eleman, geldiği $A$ elemanına geri gitsin.

![Solda f: A = {1, 2, 3} kümesinden B = {1, 4, 7} kümesine yeşil oklar, 1'den 1'e, 2'den 4'e, 3'ten 7'ye. Sağda f⁻¹: B'den A'ya sarı oklar, 1'den 1'e, 4'ten 2'ye, 7'den 3'e. Altta f(2) = 4 ve f⁻¹(4) = 2 yazıyor.](gorsel/tyt-matematik/12-02-ok-semasi.svg "f'nin her oku ters çevrilince f⁻¹ elde edilir. f 2'yi 4'e götürüyorsa f⁻¹ 4'ü 2'ye geri getirir.")

Ters çevrilmiş oklar yine bir fonksiyon oluşturur: $B$'nin her elemanından tam bir ok çıkıyor. Bu fonksiyona $f$'nin **ters fonksiyonu** denir ve $f^{-1}$ ("f üzeri eksi bir" ya da "f'nin tersi") diye yazılır.

$$f = \{(1, 1),\ (2, 4),\ (3, 7)\} \qquad f^{-1} = \{(1, 1),\ (4, 2),\ (7, 3)\}$$

**Kural.** $f\colon A \to B$ bire bir ve örten ise $f^{-1}\colon B \to A$ vardır ve

$$f(a) = b \iff f^{-1}(b) = a \qquad\qquad (a, b) \in f \iff (b, a) \in f^{-1}$$

$f$'nin tanım kümesi, $f^{-1}$'in görüntü kümesi olur; $f$'nin değer kümesi de $f^{-1}$'in tanım kümesi.

> **Tuzak:** $f^{-1}(x)$ yazısındaki $-1$ bir üs değildir. $f^{-1}(x) \neq \frac{1}{f(x)}$. Yukarıdaki örnekte $f^{-1}(4) = 2$ iken $\frac{1}{f(4)}$ anlamsızdır ($4 \notin A$).

## Hangi fonksiyonun tersi vardır?

**Örnek.** $f(x) = x^2$ ve $f\colon \{-2, 2, 3\} \to \{4, 9\}$ olsun. $f(-2) = 4$ ve $f(2) = 4$.

![A = {−2, 2, 3}, B = {4, 9}. −2 ve 2'den çıkan iki kırmızı ok da 4'e gidiyor, 3'ten çıkan yeşil ok 9'a gidiyor. Altta kırmızı yazı: f⁻¹(4) = −2 mi, 2 mi?](gorsel/tyt-matematik/12-02-tersinmez.svg "İki ok aynı elemana geliyor. Oklar ters çevrilince 4'ten iki ok çıkar; bu bir fonksiyon değildir.")

Okları ters çevirince $4$'ten iki ok çıkar: $4 \to -2$ ve $4 \to 2$. Bir elemanın iki görüntüsü olamayacağı için bu bağıntı fonksiyon **değildir**. Benzer şekilde $f$ örten olmasaydı, $B$'de ok gelmeyen bir eleman kalırdı ve ters çevrilince ondan hiç ok çıkmazdı.

**Kural.** Bir fonksiyonun tersinin de fonksiyon olması için fonksiyon **bire bir ve örten** olmalıdır. Sorularda "$f$ bire bir ve örten" ifadesi görürsen, bu "tersi vardır" demektir.

## Kuralı bulmak

**Örnek.** $f(x) = 3x - 2$ için $f^{-1}(x)$'i bulalım. $f$ bir sayıyı önce $3$ ile çarpıyor, sonra $2$ çıkarıyor. Geri almak için son yapılan işlemden başlayıp her işlemi tersine çeviririz: önce $2$ ekle, sonra $3$'e böl.

![Üst satır f: 2, 3 ile çarpılıp 6 oluyor, 2 çıkarılıp 4 oluyor. Alt satır f⁻¹ sağdan sola: 4'e 2 eklenip 6, 3'e bölünüp 2.](gorsel/tyt-matematik/12-02-islem-zinciri.svg "f⁻¹ işlemleri ters sırada ve ters yönde yapar: çıkarma toplamaya, çarpma bölmeye döner.")

Aynı şeyi cebirle yapalım. $y = f(x)$ yaz ve $x$'i yalnız bırak:

$$y = 3x - 2 \;\Rightarrow\; y + 2 = 3x \;\Rightarrow\; x = \frac{y + 2}{3}$$

$y = f(x)$ ise $x = f^{-1}(y)$ olduğundan $f^{-1}(y) = \frac{y + 2}{3}$. Değişkenin adı önemli değil; $y$ yerine $x$ yazarız:

$$f^{-1}(x) = \frac{x + 2}{3}$$

Kontrol: $f(2) = 4$ ve $f^{-1}(4) = \frac{6}{3} = 2$.

**Kural.** $f^{-1}(x)$ bulmak için: $y = f(x)$ yaz, $x$'i $y$ cinsinden çek, sonra $y$ yerine $x$ yaz.

**Yalnızca bir değer isteniyorsa kural bulma.** $f(x) = 3x - 2$ için $f^{-1}(7)$ sorulursa, $f^{-1}(7) = a$ de. Bu, $f(a) = 7$ demektir:

$$3a - 2 = 7 \;\Rightarrow\; a = 3 \qquad\Rightarrow\qquad f^{-1}(7) = 3$$

> **Tuzak:** $f^{-1}(7)$ sorulunca $f(7) = 19$ hesaplamak. $f^{-1}(7)$, "$f$ hangi sayıyı $7$'ye götürür?" sorusunun cevabıdır; $7$ burada bir **çıktıdır**.

## Kesirli fonksiyonun tersi

**Örnek.** $f(x) = \dfrac{2x + 1}{x - 3}$ için $f^{-1}(x)$'i bulalım.

$$y = \frac{2x + 1}{x - 3} \;\Rightarrow\; yx - 3y = 2x + 1 \;\Rightarrow\; yx - 2x = 3y + 1 \;\Rightarrow\; x(y - 2) = 3y + 1$$

$$x = \frac{3y + 1}{y - 2} \qquad\Rightarrow\qquad f^{-1}(x) = \frac{3x + 1}{x - 2}$$

Kontrol: $f(4) = \frac{9}{1} = 9$ ve $f^{-1}(9) = \frac{28}{7} = 4$.

Her seferinde bu işlemi yapmak yerine kısa yolu kullanabilirsin. Sonuca dikkatle bak: paydaki $x$'in katsayısı $2$ ile paydadaki sabit terim $-3$ **yer değiştirmiş ve işaret değiştirmiş** ($3x$ ve $-2$ olmuş); paydaki sabit $1$ ile paydadaki $x$'in katsayısı $1$ yerinde kalmış.

**Kural.** $c \neq 0$ olmak üzere

$$f(x) = \frac{ax + b}{cx + d} \quad\Rightarrow\quad f^{-1}(x) = \frac{-dx + b}{cx - a}$$

$a$ ile $d$ yer ve işaret değiştirir; $b$ ve $c$ yerinde kalır. Burada $f\colon \mathbb{R} - \left\{-\frac{d}{c}\right\} \to \mathbb{R} - \left\{\frac{a}{c}\right\}$; yani $f$'nin tanım kümesinden çıkan sayı paydayı sıfır yapan $-\frac{d}{c}$, $f^{-1}$'inkinden çıkan sayı $\frac{a}{c}$ olur. Örnekte $3$ ve $2$.

> **Tuzak:** $a$ ile $d$'nin yerini değiştirip işaretlerini değiştirmeyi unutmak. $\frac{2x + 1}{x - 3}$ için $\frac{-3x + 1}{x + 2}$ ya da $\frac{-3x + 1}{x - 2}$ yazmak yanlıştır; $-d = 3$ ve $-a = -2$ olur.

## Bileşke ile ters

**Örnek 1.** $f(x) = 3x - 2$ ve $f^{-1}(x) = \frac{x + 2}{3}$ için $(f \circ f^{-1})(x)$ hesaplayalım:

$$f\big(f^{-1}(x)\big) = 3 \cdot \frac{x + 2}{3} - 2 = x$$

Bir işlem yapıp hemen geri alınca sayı değişmez. Sonuç birim fonksiyondur.

**Örnek 2.** $f(x) = 2x + 1$ ve $g(x) = x - 3$ için $(f \circ g)^{-1}(7)$ kaçtır?

1. yol: $(f \circ g)(x) = 2(x - 3) + 1 = 2x - 5$. $2a - 5 = 7$ ise $a = 6$.

2. yol: $(f \circ g)$ önce $g$'yi, sonra $f$'yi uygular. Geri alırken önce $f$'yi, sonra $g$'yi geri alırız: $f^{-1}(7) = 3$, sonra $g^{-1}(3) = 6$. Yani $(f \circ g)^{-1}(7) = g^{-1}\big(f^{-1}(7)\big) = 6$.

Bu, çorap ve ayakkabı gibidir: önce çorap, sonra ayakkabı giyilir; çıkarırken önce ayakkabı, sonra çorap.

**Örnek 3.** $f(x) = 2x + 1$ ve $(f \circ g)(x) = 6x - 3$ ise $g(x)$ nedir? $f\big(g(x)\big) = 6x - 3$ eşitliğinin iki yanına $f^{-1}$ uygula:

$$g(x) = f^{-1}(6x - 3) = \frac{(6x - 3) - 1}{2} = 3x - 2$$

Önceki derste aynı soruyu denklem kurarak çözmüştük; sonuç aynı.

**Kural.**

| Özellik | Yazılışı |
|---|---|
| Ters ile bileşke birim fonksiyondur | $f \circ f^{-1} = f^{-1} \circ f = I$ |
| Tersin tersi kendisidir | $(f^{-1})^{-1} = f$ |
| Bileşkenin tersi, terslerin ters sıradaki bileşkesidir | $(f \circ g)^{-1} = g^{-1} \circ f^{-1}$ |
| Bileşkeden içteki fonksiyon | $f \circ g = h \Rightarrow g = f^{-1} \circ h$ |
| Bileşkeden dıştaki fonksiyon | $f \circ g = h \Rightarrow f = h \circ g^{-1}$ |

$(f^{-1})^{-1} = f$ şunu da söyler: kural olarak $f^{-1}$ verilirse $f(a)$ değeri, $f^{-1}(x) = a$ denklemi çözülerek bulunur.

> **Tuzak:** $(f \circ g)^{-1} = f^{-1} \circ g^{-1}$ yazmak. Sıra ters döner. Örnek 2'de bu yanlış sıra $f^{-1}\big(g^{-1}(7)\big) = f^{-1}(10) = \frac{9}{2}$ verir.

## Grafikte ters fonksiyon

**Örnek.** $f(x) = 2x - 4$ ise $f^{-1}(x) = \frac{x + 4}{2}$. $f(3) = 2$ olduğundan $(3, 2)$ noktası $f$'nin grafiğinde, $(2, 3)$ noktası $f^{-1}$'in grafiğindedir. Bileşenler yer değiştirdi.

![Koordinat düzleminde mavi f doğrusu (0, −4) ve (3, 2) noktalarından, sarı f⁻¹ doğrusu (−4, 0) ve (2, 3) noktalarından geçiyor. Gri kesikli y = x doğrusu. İki doğru (4, 4) noktasında kesişiyor; (3, 2) ile (2, 3) noktaları y = x'e göre karşılıklı.](gorsel/tyt-matematik/12-02-simetri.svg "Her (a, b) noktası y = x doğrusunun öbür yanında (b, a) noktasına karşılık gelir. f'nin y eksenini kestiği −4, f⁻¹'in x eksenini kestiği yer olur.")

**Kural.** $y = f(x)$ ile $y = f^{-1}(x)$ grafikleri **$y = x$ doğrusuna göre simetriktir**. Grafikten $f^{-1}(b)$ okumak için $b$'yi **$y$ ekseninde** bul, yatay git, grafiğe değdiğin yerin $x$ değerini oku.

> **Tuzak:** Grafikten $f^{-1}(b)$ istenince $b$'yi $x$ ekseninde aramak. O okuma $f(b)$'yi verir. Tersin girdisi, $f$'nin $y$ eksenindeki çıktısıdır.

## ÖSYM tuzakları

> **Ters ile çarpmaya göre tersi karıştırmak:** $f^{-1}(x)$, $\frac{1}{f(x)}$ değildir. Seçeneklerde $\frac{1}{f(x)}$ hep bulunur.

> **$f^{-1}(a)$ yerine $f(a)$ hesaplamak:** $f^{-1}(a)$ için $f(x) = a$ denklemini çöz. Tek değer isteniyorsa kuralı bulmak zorunda değilsin.

> **Bileşkenin tersinde sırayı korumak:** $(f \circ g)^{-1} = g^{-1} \circ f^{-1}$. Son yapılan işlem ilk geri alınır.

> **Kesirli fonksiyonda işareti unutmak:** $\frac{ax + b}{cx + d}$ ifadesinin tersinde $a$ ve $d$ yer **ve** işaret değiştirir: $\frac{-dx + b}{cx - a}$.

> **Grafikte ekseni karıştırmak:** $f^{-1}(b)$ için $b$ $y$ ekseninde aranır, cevap $x$ ekseninden okunur.

## Kendini dene

### Soru 1
$f(x) = 4x - 3$ olduğuna göre $f^{-1}(9)$ kaçtır?

A) $\frac{1}{33}$
B) $\frac{3}{2}$
C) $3$
D) $12$
E) $33$

**Cevap:** C
**Çözüm:** $f^{-1}(9) = a$ ise $f(a) = 9$: $4a - 3 = 9$, $a = 3$. $33$, $f(9)$ değeridir; $\frac{1}{33}$ ise $\frac{1}{f(9)}$. $\frac{3}{2}$, $\frac{9 - 3}{4}$ işleminden, yani işareti çevirmeden gelir; $12$, yalnızca $9 + 3$ yapıp bölmeyi unutmaktır.

### Soru 2
$f(x) = \dfrac{3x - 1}{x + 2}$ olduğuna göre $f^{-1}(x)$ aşağıdakilerden hangisidir?

A) $\dfrac{x + 2}{3x - 1}$
B) $\dfrac{2x - 1}{x - 3}$
C) $\dfrac{-2x + 1}{x - 3}$
D) $\dfrac{-2x - 1}{x - 3}$
E) $\dfrac{2x + 1}{x + 3}$

**Cevap:** D
**Çözüm:** $a = 3$, $b = -1$, $c = 1$, $d = 2$. Kural: $\frac{-dx + b}{cx - a} = \frac{-2x - 1}{x - 3}$. Kontrol: $f(1) = \frac{2}{3}$ ve $\frac{-\frac{4}{3} - 1}{\frac{2}{3} - 3} = \frac{-\frac{7}{3}}{-\frac{7}{3}} = 1$. A seçeneği $\frac{1}{f(x)}$'tir; C, $b$'nin işaretini de değiştirmektir.

### Soru 3
$f(x) = x + 5$ ve $g(x) = 2x$ olduğuna göre $(f \circ g)^{-1}(11)$ kaçtır?

A) $\frac{1}{2}$
B) $3$
C) $6$
D) $16$
E) $27$

**Cevap:** B
**Çözüm:** $(f \circ g)^{-1}(11) = g^{-1}\big(f^{-1}(11)\big)$. $f^{-1}(11) = 6$, $g^{-1}(6) = 3$. Kontrol: $(f \circ g)(3) = f(6) = 11$. Sırayı korumak $f^{-1}\big(g^{-1}(11)\big) = f^{-1}\left(\frac{11}{2}\right) = \frac{1}{2}$ verir; $27$ ise $(f \circ g)(11)$ değeridir.

## Özet kartı

- $f$ bire bir ve örten ise $f^{-1}$ vardır; $f(a) = b \iff f^{-1}(b) = a$.
- Kural: $y = f(x)$ yaz, $x$'i çek, $y$ yerine $x$ yaz. Tek değer için $f(a) = b$ denklemini çöz.
- $f^{-1}(x) \neq \frac{1}{f(x)}$.
- $\frac{ax + b}{cx + d}$ için ters $\frac{-dx + b}{cx - a}$: $a$ ile $d$ yer ve işaret değiştirir.
- $f \circ f^{-1} = I$, $(f^{-1})^{-1} = f$, $(f \circ g)^{-1} = g^{-1} \circ f^{-1}$.
- $f$ ve $f^{-1}$ grafikleri $y = x$ doğrusuna göre simetriktir; $(a, b) \in f \iff (b, a) \in f^{-1}$.

## Sonraki adım

Alıştırmaya geç (aşağıdaki düğme). Sonraki ders **Fonksiyon Grafikleri ile İlgili Uygulamalar**; grafikten değer, bileşke ve ters okumayı problemlerde kullanacaksın.
