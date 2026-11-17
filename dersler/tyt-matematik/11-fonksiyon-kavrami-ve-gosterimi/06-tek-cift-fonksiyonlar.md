---
baslik: Tek-Çift Fonksiyonlar
ders: tyt-matematik
sure: 20 dk
kaynak: MEBİ Konu Özeti 1abc2e1bd8
guncelleme: 2026-11-17
---
# Tek-Çift Fonksiyonlar

**Bu dersin sonunda:** $f(-x)$'i hesaplayarak bir fonksiyonun tek mi, çift mi, ikisi de mi olmadığına karar verebilecek, "$f$ çift olduğuna göre $a + b$ kaçtır?" tipi katsayı sorularını çözebilecek ve yarısı verilen bir grafiği simetriyle tamamlayabileceksin.

> **TYT'de yeri:** Sorular üç kalıpta gelir: "$f$ çift (ya da tek) fonksiyon olduğuna göre katsayılar kaçtır?", "$f$ tek ve $f(3) = 4$ ise $f(-3)$ kaçtır?" ve "grafiğin $x \ge 0$ kısmı verilmiştir, $f$ tek olduğuna göre…". Hepsinde aynı iki eşitlik kullanılır.

## Önce hatırla

<details><summary>Doğrusal fonksiyon dersinden: $f(x) = mx + n$ doğrusal fonksiyonunun grafiği $(0, 4)$ ve $(2, 0)$ noktalarından geçiyor. $f(x)$ nedir?</summary>
$(0, 4)$ noktası $y$ eksenini kestiği yer: $n = f(0) = 4$. $(2, 0)$ noktasından: $2m + 4 = 0$, $m = -2$. Sonuç: <b>$f(x) = -2x + 4$</b>.
</details>

<details><summary>Parçalı fonksiyon dersinden: $x < 0$ için $f(x) = x^2$, $x \ge 0$ için $f(x) = 2x + 1$ ise $f(-3) + f(3)$ kaçtır?</summary>
$-3 < 0$ olduğu için birinci kural: $f(-3) = 9$. $3 \ge 0$ olduğu için ikinci kural: $f(3) = 7$. Toplam <b>16</b>. Dikkat: $f(-3)$ ile $f(3)$ farklı çıktı. Bu derste $f(-x)$ ile $f(x)$ arasında hep aynı ilişki olan fonksiyonları göreceksin.
</details>

## Çift fonksiyon

**Örnek.** $f(x) = x^4 - 3x^2 + 5$ için $f(2)$ ve $f(-2)$'yi hesapla.

- $f(2) = 16 - 12 + 5 = 9$
- $f(-2) = (-2)^4 - 3(-2)^2 + 5 = 16 - 12 + 5 = 9$

Aynı çıktı. Bu bir rastlantı değil: $(-x)^4 = x^4$ ve $(-x)^2 = x^2$ olduğu için her $x$'te

$$f(-x) = (-x)^4 - 3(-x)^2 + 5 = x^4 - 3x^2 + 5 = f(x).$$

**Kural.** $f\colon \mathbb{R} \to \mathbb{R}$ fonksiyonunda **her** $x$ için $f(-x) = f(x)$ ise $f$ **çift fonksiyondur**.

- Grafik **$y$ eksenine göre simetriktir**: $(a, b)$ grafikteyse $(-a, b)$ de grafiktedir.
- Polinom kuralda $x$ yalnızca **çift dereceli** terimlerde bulunur: $x^2$, $x^4$, … Sabit terim $x^0$ gibi düşünülür, yani çift fonksiyonda **serbesttir**.
- Örnekler: $x^2$, $x^4 - 3x^2 + 5$, sabit fonksiyon $f(x) = 3$, $|x|$ (çünkü $|-x| = |x|$). İleride göreceğin $\cos x$ de çifttir.

![Koordinat düzleminde y = x² − 3 parabolü. Üzerinde (−2, 1) ve (2, 1) noktaları işaretli, aralarında yatay kesikli çizgi var; y ekseni yeşil renkle ayna olarak vurgulanmış.](gorsel/tyt-matematik/11-06-cift-grafik.svg "x'in işareti değişince y değişmiyor. Grafiği y ekseninden katlarsan iki yarı üst üste gelir.")

## Tek fonksiyon

**Örnek.** $f(x) = x^3 + 2x$ için $f(1)$ ve $f(-1)$'i hesapla.

- $f(1) = 1 + 2 = 3$
- $f(-1) = (-1)^3 + 2(-1) = -1 - 2 = -3$

Çıktılar ters işaretli. Genel olarak $(-x)^3 = -x^3$ olduğu için

$$f(-x) = -x^3 - 2x = -(x^3 + 2x) = -f(x).$$

**Kural.** $f\colon \mathbb{R} \to \mathbb{R}$ fonksiyonunda **her** $x$ için $f(-x) = -f(x)$ ise $f$ **tek fonksiyondur**.

- Grafik **orijine göre simetriktir**: $(a, b)$ grafikteyse $(-a, -b)$ de grafiktedir.
- Polinom kuralda $x$ yalnızca **tek dereceli** terimlerde bulunur: $x$, $x^3$, $x^5$, … **Sabit terim olamaz.**
- $x = 0$ koyarsan $f(0) = -f(0)$, yani tek fonksiyonda her zaman $f(0) = 0$: grafik orijinden geçer.
- Önceki dersle bağlantı: doğrusal $f(x) = mx + n$ fonksiyonu $n = 0$ ise tek, $m = 0$ ise (sabit) çifttir.

![Koordinat düzleminde y = x³ − 3x eğrisi. Üzerinde (2, 2) ve (−2, −2) noktaları işaretli; iki noktayı birleştiren kesikli çizgi orijinden geçiyor.](gorsel/tyt-matematik/11-06-tek-grafik.svg "Bir noktadan orijine, sonra aynı uzunlukta devam edersen eşine ulaşırsın. İki koordinatın da işareti değişir.")

## Ne tek ne çift

**Örnek.** $f(x) = x^2 + x$ tek mi, çift mi?

$f(-x) = (-x)^2 + (-x) = x^2 - x$. Bu ne $f(x) = x^2 + x$'e ne de $-f(x) = -x^2 - x$'e eşit. Sayıyla da gör: $f(1) = 2$, $f(-1) = 0$. Fonksiyon **ne tek ne çifttir**; içinde hem çift hem tek dereceli terim var.

Benzer biçimde $f(x) = x^3 + 1$ tek değildir, çünkü sabit terimi var ($f(0) = 1 \ne 0$).

**Kural.** Çoğu fonksiyon ne tek ne çifttir. Hem tek hem çift olan tek fonksiyon $f(x) = 0$'dır. Karar verirken hep aynı yolu izle:

![Akış şeması: x yerine −x koy, f(−x) neye eşit? f(−x) = f(x) ise çift fonksiyon; f(−x) = −f(x) ise tek fonksiyon; ikisi de değilse ne tek ne çift.](gorsel/tyt-matematik/11-06-karar.svg "Önce f(−x)'i sadeleştir, sonra f(x) ve −f(x) ile karşılaştır. Polinomda kısa yol: üslere bak.")

## Katsayı soruları

**Örnek.** $f(x) = (a - 3)x^3 + 2x^2 + (b + 1)x + 7$ çift fonksiyon olduğuna göre $a$, $b$ ve $f(1)$ kaçtır?

Çift fonksiyonda tek dereceli terim kalamaz; $x^3$ ve $x$ terimlerinin katsayıları sıfır olmalı:

- $a - 3 = 0$, $a = 3$
- $b + 1 = 0$, $b = -1$

Geriye $f(x) = 2x^2 + 7$ kalır ve $f(1) = 9$. Sabit terim $7$'ye dokunmadık: çift fonksiyonda sabit terim kalabilir.

**Örnek.** $f(x) = (m - 1)x^2 + 4x^3 + x + n - 2$ tek fonksiyon olduğuna göre $f(-1)$ kaçtır?

Tek fonksiyonda çift dereceli terim ve sabit terim kalamaz: $m - 1 = 0$, $m = 1$ ve $n - 2 = 0$, $n = 2$. Geriye $f(x) = 4x^3 + x$ kalır; $f(-1) = -4 - 1 = -5$.

**Kural.**

| $f$ çift ise | $f$ tek ise |
|---|---|
| tek dereceli terimlerin katsayıları $0$ | çift dereceli terimlerin katsayıları $0$ |
| sabit terim serbest | sabit terim $0$ |

## Değer soruları ve grafik tamamlama

**Örnek.** $f$ tek, $g$ çift fonksiyondur. $f(3) = 4$ ve $g(3) = -2$ ise $f(-3) + g(-3)$ kaçtır?

$f$ tek: $f(-3) = -f(3) = -4$. $g$ çift: $g(-3) = g(3) = -2$. Toplam $-4 + (-2) = -6$.

**Örnek.** Bir $f$ fonksiyonunun grafiğinin $x \ge 0$ kısmı $(0, 0)$, $(2, 3)$ ve $(4, 1)$ noktalarını birleştiren iki doğru parçasıdır. $f(-3)$ kaçtır?

Önce $f(3)$: $(2, 3)$ ile $(4, 1)$ arasında $x$ 1 artınca $y$ 1 azalır, $f(3) = 2$. Sonra simetri:

- $f$ çift ise $f(-3) = f(3) = 2$.
- $f$ tek ise $f(-3) = -f(3) = -2$.

![Yan yana iki grafik. İkisinde de mavi parça (0, 0)'dan (2, 3)'e, oradan (4, 1)'e gidiyor. Solda yeşil kesikli yansıma (−2, 3) ve (−4, 1) noktalarından geçiyor; sağda (−2, −3) ve (−4, −1) noktalarından geçiyor.](gorsel/tyt-matematik/11-06-tamamla.svg "Mavi parça verilen, yeşil parça senin çizdiğin. Çiftte yalnız x'in işareti, tekte iki koordinatın da işareti değişir.")

**Kural.**

- Çift: $f(-a) = f(a)$, yani $f(a) - f(-a) = 0$. Grafiği $y$ ekseninden aynala.
- Tek: $f(-a) = -f(a)$, yani $f(a) + f(-a) = 0$. Noktayı orijine göre çevir: $(a, b) \to (-a, -b)$.
- Tek fonksiyonda $f(-3) + f(-2) + \dots + f(3)$ gibi simetrik toplamlar $0$'dır.

**İşlemler.** $f(x) = x^3$ (tek) ve $g(x) = x$ (tek) ise $f(x) \cdot g(x) = x^4$ çifttir. İşaret kuralı gibi düşün: tek "eksi", çift "artı" gibidir.

| İşlem | Sonuç |
|---|---|
| tek $\cdot$ tek, çift $\cdot$ çift | çift |
| tek $\cdot$ çift | tek |
| tek $+$ tek | tek |
| çift $+$ çift | çift |

## ÖSYM tuzakları

> **Tek sayıda terim ya da tek katsayı sanmak:** "Tek fonksiyon" adı üslerden gelir. $3x^2 + 5$ çifttir, katsayıları tek olsa bile; $2x^3$ tektir.

> **Sabit terimi unutmak:** $x^3 + x + 2$ tek değildir, çünkü $f(0) = 2 \ne 0$. Tek fonksiyon sorusunda sabit terimi de sıfıra eşitle; çift fonksiyon sorusunda ise sabit terime dokunma.

> **$(-x)^2$'yi $-x^2$ yazmak:** $(-x)^2 = x^2$, ama $-x^2$ başka bir şeydir. $f(-x)$'i hesaplarken $-x$'i hep parantezle yerine koy.

> **Tek fonksiyonu yalnızca $x$ ekseninden aynalamak:** Tekte $(2, 3)$ noktasının eşi $(2, -3)$ değil, $(-2, -3)$'tür. İki koordinatın da işareti değişir.

> **Tek ile çifti karıştırmak:** $f$ tek ve $f(2) = 5$ ise $f(-2) = -5$; $5$ değil. Soruda hangi fonksiyonun tek, hangisinin çift olduğunu en başta işaretle.

## Kendini dene

### Soru 1
Aşağıdaki fonksiyonlardan hangisi çift fonksiyondur?

A) $f(x) = x^3 + x^2$
B) $f(x) = x^4 - 2x^2 + 1$
C) $f(x) = x^3 - x$
D) $f(x) = x^2 + x$
E) $f(x) = 2x + 3$

**Cevap:** B
**Çözüm:** B'de yalnızca $x^4$, $x^2$ ve sabit terim var; hepsi çift dereceli: $f(-x) = x^4 - 2x^2 + 1 = f(x)$. C tektir ($f(-x) = -f(x)$). A ve D'de hem tek hem çift dereceli terim var; E'de hem $x$ hem sabit terim var. Bunlar ne tek ne çifttir.

### Soru 2
$f(x) = (a + 2)x^3 + (b - 1)x^2 + 4x + a + b$ tek fonksiyon olduğuna göre $f(2)$ kaçtır?

A) 8
B) 12
C) 16
D) 20
E) 24

**Cevap:** C
**Çözüm:** Tek fonksiyonda çift dereceli terim ve sabit terim olmaz. $b - 1 = 0$, $b = 1$. $a + b = 0$, $a = -1$. Kural $f(x) = (-1 + 2)x^3 + 4x = x^3 + 4x$. $f(2) = 8 + 8 = 16$. $x^3$ terimini unutup yalnız $4x$'i hesaplayan 8 bulur.

### Soru 3
$f$ tek, $g$ çift fonksiyondur. $f(2) = 3$ ve $g(-2) = 5$ olduğuna göre $f(-2) \cdot g(2)$ çarpımı kaçtır?

A) $-15$
B) $-8$
C) $-2$
D) $8$
E) $15$

**Cevap:** A
**Çözüm:** $f$ tek: $f(-2) = -f(2) = -3$. $g$ çift: $g(2) = g(-2) = 5$. Çarpım $-3 \cdot 5 = -15$. $f$'yi çift sanan $15$ bulur.

## Özet kartı

- Çift: $f(-x) = f(x)$; grafik $y$ eksenine göre simetrik; polinomda yalnız çift dereceli terim ve sabit.
- Tek: $f(-x) = -f(x)$; grafik orijine göre simetrik; polinomda yalnız tek dereceli terim, sabit yok, $f(0) = 0$.
- Karar için $x$ yerine $-x$ koy, sonucu $f(x)$ ve $-f(x)$ ile karşılaştır.
- Çift ise tek dereceli katsayılar $0$; tek ise çift dereceli katsayılar ve sabit terim $0$.
- Grafik tamamlama: çiftte $(a, b) \to (-a, b)$, tekte $(a, b) \to (-a, -b)$.
- tek $\cdot$ tek ve çift $\cdot$ çift çifttir; tek $\cdot$ çift tektir.

## Sonraki adım

Alıştırmaya geç (aşağıdaki düğme). Sonraki ders **Fonksiyonlarda Dört İşlem**; $f + g$, $f \cdot g$ gibi işlemleri orada ayrıntılı göreceksin ve bu dersteki tek-çift tablosu işini hızlandıracak.
