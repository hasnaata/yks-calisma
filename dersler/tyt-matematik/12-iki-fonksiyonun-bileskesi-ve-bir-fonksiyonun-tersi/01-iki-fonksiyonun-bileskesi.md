---
baslik: İki Fonksiyonun Bileşkesi
ders: tyt-matematik
sure: 25 dk
kaynak: MEBİ Konu Özeti 36ad81c827
guncelleme: 2026-11-17
---
# İki Fonksiyonun Bileşkesi

**Bu dersin sonunda:** iki fonksiyonun bileşkesini kuraldan, ok şemasından, tablodan ve grafikten hesaplayabilecek, bileşkesi verilen fonksiyonlardan bilinmeyeni bulabileceksin.

> **TYT'de yeri:** "$(f \circ g)(2)$ kaçtır?" gibi doğrudan hesaplar, grafiği ya da ok şeması verilen iki fonksiyonla bileşke değeri okuma, $(f \circ g)(x)$ ve $f(x)$ verilip $g(x)$'in istenmesi, $f(2x + 1) = \dots$ biçiminde verilen fonksiyondan değer bulma. Yeni nesil sorularda bileşke, art arda uygulanan iki işlem (önce indirim, sonra kupon gibi) olarak gelir.

## Önce hatırla

<details><summary>Fonksiyon grafiklerinden: $f(x) = 2x - 6$ doğrusunun grafiği eksenleri hangi noktalarda keser?</summary>
$y$ eksenini kestiği yerde $x = 0$: $f(0) = -6$, nokta $(0, -6)$. $x$ eksenini kestiği yerde $y = 0$: $2x - 6 = 0$, $x = 3$, nokta $(3, 0)$. Doğrusal fonksiyonun grafiğini çizmek için bu iki nokta yeter.
</details>

<details><summary>Fonksiyon grafiklerinden: Grafiği verilen bir fonksiyonun tanım kümesi ve görüntü kümesi grafikte nasıl okunur?</summary>
Tanım kümesi, grafikteki noktaların birinci bileşenleridir (grafiğin $x$ eksenine izdüşümü). Görüntü kümesi, ikinci bileşenlerdir (grafiğin $y$ eksenine izdüşümü). Grafikte $f(a)$ değeri: $x = a$ noktasındaki grafiğin yüksekliği.
</details>

## Bileşke nedir?

**Örnek.** $f(x) = 2x + 1$ ve $g(x) = x^2$ olsun. Bir sayıya önce $f$, sonra çıkan sonuca $g$ uygulayalım. $x = 3$ için:

$$f(3) = 2 \cdot 3 + 1 = 7, \qquad g(7) = 7^2 = 49$$

Bu iki adımı tek fonksiyon gibi düşünürsek $3$ doğrudan $49$'a gider. Bu yeni fonksiyona **$g$ bileşke $f$** denir ve $g \circ f$ diye yazılır:

$$(g \circ f)(3) = g\big(f(3)\big) = g(7) = 49$$

![Üç elips A, B, C. A'daki 3, yeşil f okuyla B'deki 7'ye; 7, sarı g okuyla C'deki 49'a gidiyor. Altta kırmızı ok A'daki 3'ten doğrudan C'deki 49'a gidiyor ve g∘f diye adlandırılmış.](gorsel/tyt-matematik/12-01-sema.svg "Önce f uygulanır, f'nin sonucu g'ye girer. Kırmızı ok iki adımı tek adımda yapan g∘f fonksiyonudur.")

**Kural.** $f\colon A \to B$ ve $g\colon B \to C$ ise her $x \in A$ için

$$(g \circ f)(x) = g\big(f(x)\big)$$

ile tanımlanan $g \circ f\colon A \to C$ fonksiyonuna $f$ ile $g$'nin **bileşke fonksiyonu** denir. Okunuşu: "g bileşke f". İşlem **sağdan sola** yapılır: önce sağdaki ($f$, içteki), sonra soldaki ($g$, dıştaki).

Bileşkenin tanımlı olması için içteki fonksiyonun sonuçları dıştakinin tanım kümesinde olmalıdır.

Ters sırada: $(f \circ g)(3) = f\big(g(3)\big) = f(9) = 19$. Aynı sayılar, farklı sonuç.

> **Tuzak:** $g \circ f$ yazımında $g$ solda diye önce $g$'yi uygulamak. Sıra hep **sağdan sola**: $\circ$ işaretinin sağındaki fonksiyon önce çalışır.

## Kuralı bulmak ve değişme özelliği

**Örnek.** Aynı $f(x) = 2x + 1$ ve $g(x) = x^2$ için iki bileşkenin kuralını bulalım. İçteki fonksiyonun **bütün ifadesi**, dıştakinin $x$'i yerine yazılır:

$$(f \circ g)(x) = f\big(g(x)\big) = f(x^2) = 2x^2 + 1$$

$$(g \circ f)(x) = g\big(f(x)\big) = g(2x + 1) = (2x + 1)^2 = 4x^2 + 4x + 1$$

Kontrol: $x = 3$ için $2 \cdot 9 + 1 = 19$ ve $4 \cdot 9 + 12 + 1 = 49$. Yukarıdaki sonuçlarla aynı.

**Kural.** Bileşke işleminin **değişme özelliği yoktur**: genellikle $f \circ g \neq g \circ f$. Bazı özel fonksiyonlarda eşit çıkabilir, ama bunu varsayamazsın; hesaplayıp karşılaştırırsın.

> **Tuzak:** $(g \circ f)(x) = (2x + 1)^2$ yerine $2x^2 + 1$ yazmak. İçteki ifadeyi yerine koyarken **parantez** kullan; kare, ifadenin tamamına uygulanır.

> **Tuzak:** $(f \circ g)(x)$ ile $(f \cdot g)(x)$ karışır. Çarpımda $f(x) \cdot g(x) = (2x + 1)x^2$; bileşkede $f(x^2) = 2x^2 + 1$. Bunlar başka fonksiyonlardır.

## Ok şeması ile bileşke

**Örnek.** Aşağıda $f\colon A \to B$ ve $g\colon B \to C$ fonksiyonları ok şemasıyla verilmiş. $g \circ f$ fonksiyonunu liste olarak yazalım.

![Üç elips: A = {−1, 0, 2}, B = {1, 3, 4, 5}, C = {0, 2, 6}. Yeşil f okları: −1'den 3'e, 0'dan 1'e, 2'den 5'e. Sarı g okları: 1'den 0'a, 3'ten 6'ya, 4'ten 2'ye, 5'ten 2'ye.](gorsel/tyt-matematik/12-01-venn.svg "A'daki her elemandan başla: önce yeşil oku, sonra o elemandan çıkan sarı oku izle.")

A'daki her elemandan iki oku art arda izle:

| $x$ | $f(x)$ | $g\big(f(x)\big)$ |
|---|---|---|
| $-1$ | $3$ | $6$ |
| $0$ | $1$ | $0$ |
| $2$ | $5$ | $2$ |

$$g \circ f = \{(-1, 6),\ (0, 0),\ (2, 2)\}$$

B'deki $4$'e $f$'den ok gelmiyor; bu yüzden $g(4) = 2$ bilgisi $g \circ f$ için kullanılmaz.

**Kural.** Ok şemasında $(g \circ f)(a)$ için $a$'dan başla, önce $f$ okunu, sonra varılan elemandan $g$ okunu izle. $g \circ f$ fonksiyonunun tanım kümesi $A$, değer kümesi $C$'dir.

> **Tuzak:** $(g \circ f)(2)$ sorulunca $g(2)$'yi aramak. $2$ önce $f$'ye girer; $g$'ye giren sayı $f(2) = 5$'tir.

## Grafikten bileşke

**Örnek.** Grafikte $f$ (mavi doğru) ve $g$ (yeşil parabol) verilmiş. Kurallarını bilmeden $(g \circ f)(0)$ ve $(f \circ g)(0)$ değerlerini okuyalım.

![Koordinat düzleminde mavi f doğrusu ve yeşil g parabolü. İşaretli noktalar: f üzerinde (0, 2) ve (−3, −1); g üzerinde (2, 1) ve (0, −3).](gorsel/tyt-matematik/12-01-grafik.svg "Bir grafikten okuduğun y değerini, öbür grafikte x değeri olarak kullan.")

- $(g \circ f)(0)$: önce $f(0)$. Mavi doğru $x = 0$'da $y = 2$'de: $f(0) = 2$. Şimdi $x = 2$'ye git, yeşil grafiğin yüksekliği $1$: $g(2) = 1$. Sonuç $\mathbf{1}$.
- $(f \circ g)(0)$: önce $g(0)$. Parabolün tepesi $(0, -3)$: $g(0) = -3$. Şimdi $x = -3$'e git, mavi doğrunun yüksekliği $-1$: $f(-3) = -1$. Sonuç $\mathbf{-1}$.

**Kural.** Grafikte $(g \circ f)(a)$: $f$ grafiğinde $x = a$'daki $y$ değerini oku; bu sayıyı **x eksenine taşı**, orada $g$ grafiğinin yüksekliğini oku.

> **Tuzak:** İlk okuduğun $y$ değerinden yatay giderek ikinci grafiğe ulaşmak. İkinci adımda o sayı artık bir $x$ değeridir; $x$ ekseninde aynı sayıya git, sonra dikey bak.

## Birim fonksiyon ve birleşme özelliği

**Örnek.** $f(x) = x + 1$, $g(x) = 2x$, $h(x) = x^2$ için $(f \circ g \circ h)(3)$ değerini bulalım. Yine sağdan sola:

$$h(3) = 9, \qquad g(9) = 18, \qquad f(18) = 19$$

Parantezi nereye koyarsan koy sonuç aynıdır: $\big((f \circ g) \circ h\big)(3) = \big(f \circ (g \circ h)\big)(3) = 19$. Sıra değişmedikçe gruplama sonucu değiştirmez.

$I(x) = x$ birim fonksiyonu sayıyı değiştirmez: $(f \circ I)(5) = f(5)$ ve $(I \circ f)(5) = f(5)$.

**Kural.**

| Özellik | Yazılışı |
|---|---|
| Değişme yok | $f \circ g \neq g \circ f$ (genellikle) |
| Birleşme var | $f \circ g \circ h = (f \circ g) \circ h = f \circ (g \circ h)$ |
| Birim fonksiyon etkisiz | $f \circ I = I \circ f = f$ |
| Bire bir | $f$ ve $g$ bire bir ise $g \circ f$ de bire birdir |
| Örten | $f$ ve $g$ örten ise $g \circ f$ de örtendir |

## Bileşkeden bilinmeyen fonksiyonu bulmak

TYT'nin en sık kalıbı: bileşke ve fonksiyonlardan biri verilir, öbürü istenir. Önce hangisinin bilinmediğine bak.

![Akış şeması: f∘g verildi, biri bilinmiyor. İçteki g bilinmiyorsa f kuralına g(x) yazılır, eşitlenip g(x) çekilir. Dıştaki f bilinmiyorsa içteki ifade t'ye eşitlenir, x t cinsinden yazılır.](gorsel/tyt-matematik/12-01-bilinmeyen.svg "İçteki bilinmiyorsa onu bilinmeyen gibi çöz; dıştaki bilinmiyorsa içi t'ye eşitle.")

**Örnek 1 (içteki bilinmiyor).** $f(x) = 2x + 1$ ve $(f \circ g)(x) = 6x - 3$ ise $g(x)$ nedir?

$f\big(g(x)\big) = 2 \cdot g(x) + 1$ olduğundan

$$2\,g(x) + 1 = 6x - 3 \;\Rightarrow\; 2\,g(x) = 6x - 4 \;\Rightarrow\; g(x) = 3x - 2$$

Kontrol: $f(3x - 2) = 2(3x - 2) + 1 = 6x - 3$. Doğru.

**Örnek 2 (dıştaki bilinmiyor).** $f(2x + 1) = 4x + 5$ ise $f(x)$ nedir?

İçteki ifadeye $t$ de: $2x + 1 = t$, buradan $x = \frac{t - 1}{2}$.

$$f(t) = 4 \cdot \frac{t - 1}{2} + 5 = 2(t - 1) + 5 = 2t + 3 \;\Rightarrow\; f(x) = 2x + 3$$

**Örnek 3 (yalnızca bir değer isteniyor).** Aynı soruda $f(9)$ istenirse kuralı bulmana gerek yok. İçi $9$ yapan $x$'i bul: $2x + 1 = 9$, $x = 4$. Sonra $f(9) = 4 \cdot 4 + 5 = 21$. Kontrol: $2 \cdot 9 + 3 = 21$.

**Kural.** Bilinmeyen içteyse dıştaki kurala onu yerleştirip denklemi çöz. Bilinmeyen dıştaysa içteki ifadeyi $t$'ye eşitle; tek değer isteniyorsa içi o değere eşitleyip $x$'i bul.

> **Tuzak:** $f(2x + 1) = 4x + 5$ verilince $f(9)$ için $x = 9$ yazıp $41$ bulmak. $9$, fonksiyonun içine giren sayıdır; $x$ değil, $2x + 1$ değeridir.

## ÖSYM tuzakları

> **Sırayı ters çevirmek:** $(f \circ g)(x) = f\big(g(x)\big)$; önce $g$, sonra $f$. Seçeneklerde neredeyse her zaman ters sıranın sonucu da bulunur.

> **Bileşkeyi çarpım sanmak:** $(f \circ g)(2)$ ile $f(2) \cdot g(2)$ farklıdır. $\circ$ işareti "art arda uygula" demektir.

> **Parantezi unutmak:** $g(x) = x^2$ ve $f(x) = x - 3$ ise $(g \circ f)(x) = (x - 3)^2$ olur, $x^2 - 3$ değil.

> **İçteki sayıyı $x$ sanmak:** $f(3x - 2) = \dots$ verildiğinde $f(7)$ için $3x - 2 = 7$ çözülür, $x = 7$ yazılmaz.

> **Değişme özelliği varsaymak:** $f \circ g = g \circ f$ ancak hesaplayıp karşılaştırınca söylenebilir. Bu eşitlik verilirse iki kuralı ayrı ayrı bul, katsayıları eşitle.

## Kendini dene

### Soru 1
$f(x) = x - 3$ ve $g(x) = 2x + 1$ olduğuna göre $(f \circ g)(2)$ kaçtır?

A) $-5$
B) $-1$
C) $2$
D) $4$
E) $7$

**Cevap:** C
**Çözüm:** Önce içteki: $g(2) = 2 \cdot 2 + 1 = 5$. Sonra $f(5) = 5 - 3 = 2$. Ters sırada hesaplayan $(g \circ f)(2) = g(-1) = -1$ bulur; $f(2) \cdot g(2) = -1 \cdot 5 = -5$ çarpım, $f(2) + g(2) = 4$ toplamdır.

### Soru 2
$f(x) = 3x + 2$ ve $(g \circ f)(x) = 6x + 1$ olduğuna göre $g(x)$ aşağıdakilerden hangisidir?

A) $x - 1$
B) $2x + 1$
C) $3x - 1$
D) $2x - 3$
E) $2x + 5$

**Cevap:** D
**Çözüm:** Bilinmeyen $g$ dışta: $g(3x + 2) = 6x + 1$. $3x + 2 = t$ de, $x = \frac{t - 2}{3}$. $g(t) = 6 \cdot \frac{t - 2}{3} + 1 = 2t - 4 + 1 = 2t - 3$. Kontrol: $g(3x + 2) = 2(3x + 2) - 3 = 6x + 1$. $3x - 1$, bileşkeden $f$'yi çıkarmaktır; bileşke çıkarma değildir.

### Soru 3
$f(2x - 1) = 4x + 3$ olduğuna göre $f(5)$ kaçtır?

A) $11$
B) $13$
C) $15$
D) $19$
E) $23$

**Cevap:** C
**Çözüm:** İçi $5$ yapan $x$: $2x - 1 = 5$, $x = 3$. $f(5) = 4 \cdot 3 + 3 = 15$. $x = 5$ yazan $4 \cdot 5 + 3 = 23$ bulur; bu, içteki ifadeyi $x$ sanmaktır.

## Özet kartı

- $(g \circ f)(x) = g\big(f(x)\big)$: sağdan sola, önce içteki $f$, sonra dıştaki $g$.
- Kural bulurken içteki ifadenin tamamını parantezle dıştakinin $x$'i yerine yaz.
- $f \circ g \neq g \circ f$ (genellikle); birleşme özelliği var; $f \circ I = I \circ f = f$.
- Ok şeması ve grafikte: ilk sonucu bir sonraki fonksiyonun **girdisi** ($x$ değeri) yap.
- İçteki bilinmiyorsa denklem kur, $g(x)$'i çek; dıştaki bilinmiyorsa içi $t$'ye eşitle.
- $f(ax + b)$ verilip $f(k)$ istenirse $ax + b = k$ çöz, bulduğun $x$'i yerine yaz.

## Sonraki adım

Alıştırmaya geç (aşağıdaki düğme). Sonraki ders **Bir Fonksiyonun Tersi**; $f$'nin yaptığını geri alan $f^{-1}$ fonksiyonunu ve $f \circ f^{-1} = I$ eşitliğini göreceksin. Bu dersteki "içi $t$'ye eşitle" yöntemi, ters fonksiyon bulmanın da temelidir.
