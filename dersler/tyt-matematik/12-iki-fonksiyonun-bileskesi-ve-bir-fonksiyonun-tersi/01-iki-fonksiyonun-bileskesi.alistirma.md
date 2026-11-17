---
baslik: İki Fonksiyonun Bileşkesi · Alıştırma
ders: tyt-matematik
soru: 12
guncelleme: 2026-11-17
---
# Alıştırma: İki Fonksiyonun Bileşkesi

Sorular özgündür ve ÖSYM soru tarzında yazılmıştır. Derse bakmadan çöz.

## Isınma

### Soru 1 · Kolay
$f(x) = 3x - 2$ ve $g(x) = x^2 + 1$ olduğuna göre $(g \circ f)(2)$ kaçtır?

A) 5
B) 9
C) 13
D) 17
E) 20

**Cevap:** D
**Çözüm:** Önce içteki $f$: $f(2) = 3 \cdot 2 - 2 = 4$. Sonra $g(4) = 4^2 + 1 = 17$. Ters sırayla hesaplayan $(f \circ g)(2) = f(5) = 13$ bulur. $20 = f(2) \cdot g(2)$ çarpım, $9 = f(2) + g(2)$ toplamdır; $5$ ise yalnızca $g(2)$ değeridir.

### Soru 2 · Kolay
Aşağıda $f\colon A \to B$ ve $g\colon B \to C$ fonksiyonları ok şemasıyla verilmiştir.

![Üç elips: A = {1, 2, 3}, B = {4, 5, 6}, C = {7, 8, 9}. Yeşil f okları: 1'den 5'e, 2'den 4'e, 3'ten 6'ya. Sarı g okları: 4'ten 9'a, 5'ten 7'ye, 6'dan 8'e.](gorsel/tyt-matematik/12-01-soru2.svg "Önce yeşil f okunu, sonra varılan elemandan çıkan sarı g okunu izle.")

Buna göre $(g \circ f)(2) + (g \circ f)(3)$ toplamı kaçtır?

A) 10
B) 13
C) 15
D) 16
E) 17

**Cevap:** E
**Çözüm:** $f(2) = 4$, $g(4) = 9$; yani $(g \circ f)(2) = 9$. $f(3) = 6$, $g(6) = 8$; yani $(g \circ f)(3) = 8$. Toplam $17$. Yalnızca $f$ oklarında kalan $f(2) + f(3) = 10$ bulur; $15$, $(g \circ f)(1) + (g \circ f)(3) = 7 + 8$ toplamıdır.

### Soru 3 · Kolay
$f(x) = x + 4$ ve $g(x) = 2x$ olduğuna göre $(f \circ g)(x)$ aşağıdakilerden hangisidir?

A) $2x + 4$
B) $2x + 8$
C) $3x + 4$
D) $2x^2 + 8x$
E) $x + 6$

**Cevap:** A
**Çözüm:** $(f \circ g)(x) = f\big(g(x)\big) = f(2x) = 2x + 4$. $2x + 8$, ters sıradaki $(g \circ f)(x) = 2(x + 4)$ kuralıdır. $2x^2 + 8x$ çarpım $(f \cdot g)(x)$, $3x + 4$ toplam $(f + g)(x)$ kuralıdır.

## Orta

### Soru 4 · Orta
$f(x) = ax + 2$ ve $g(x) = 3x - 1$ fonksiyonları için $f \circ g = g \circ f$ olduğuna göre $a$ kaçtır?

A) $-3$
B) $-1$
C) $1$
D) $3$
E) $7$

**Cevap:** A
**Çözüm:** $(f \circ g)(x) = a(3x - 1) + 2 = 3ax - a + 2$. $(g \circ f)(x) = 3(ax + 2) - 1 = 3ax + 5$. $x$'li terimler zaten eşit; sabitleri eşitle: $-a + 2 = 5$, $a = -3$. Kontrol: $a = -3$ için iki kural da $-9x + 5$ olur. $3$, işaret hatasıdır; $7$, $-a + 2$ ifadesini $a - 2$ diye yazmaktan gelir.

### Soru 5 · Orta
Aşağıda $f$ ve $g$ doğrusal fonksiyonlarının grafikleri verilmiştir.

![Koordinat düzleminde iki doğru. Mavi f doğrusu (0, 3) ve (3, 0) noktalarından, yeşil g doğrusu (0, −1) ve (2, 3) noktalarından geçiyor.](gorsel/tyt-matematik/12-01-soru5.svg "İşaretli noktalar doğruların geçtiği tam sayı koordinatlı noktalardır.")

Buna göre $(f \circ g)(2) + (g \circ f)(2)$ toplamı kaçtır?

A) 1
B) 2
C) 3
D) 4
E) 5

**Cevap:** A
**Çözüm:** $(f \circ g)(2)$: grafikten $g(2) = 3$, sonra $f(3) = 0$. $(g \circ f)(2)$: mavi doğru $x = 2$'de $y = 1$, yani $f(2) = 1$; yeşil doğru $x = 1$'de $y = 1$, yani $g(1) = 1$. Toplam $0 + 1 = 1$. (Kurallar $f(x) = 3 - x$, $g(x) = 2x - 1$; aynı sonucu verir.) $4 = f(2) + g(2)$, $3 = f(2) \cdot g(2)$ yanlış işlemlerdir.

### Soru 6 · Orta
$f(x) = 2x - 3$ ve $(f \circ g)(x) = 4x + 5$ olduğuna göre $g(1)$ kaçtır?

A) 3
B) 4
C) 6
D) 8
E) 9

**Cevap:** C
**Çözüm:** Bilinmeyen $g$ içte. $f\big(g(x)\big) = 2\,g(x) - 3 = 4x + 5$, buradan $2\,g(x) = 4x + 8$, $g(x) = 2x + 4$. $g(1) = 6$. Kontrol: $f(6) = 9$ ve $(f \circ g)(1) = 4 + 5 = 9$. $9$, $(f \circ g)(1)$ değerinde kalmaktır; $3$, $-3$'ü karşıya geçirirken işaret hatası yapınca bulunan $g(x) = 2x + 1$'den gelir.

### Soru 7 · Orta
$f(2x + 1) = 6x - 5$ olduğuna göre $f(7)$ kaçtır?

A) 3
B) 13
C) 19
D) 37
E) 43

**Cevap:** B
**Çözüm:** İçi $7$ yapan $x$: $2x + 1 = 7$, $x = 3$. $f(7) = 6 \cdot 3 - 5 = 13$. Kontrol: $f(x) = 3x - 8$ ve $3 \cdot 7 - 8 = 13$. $x = 7$ yazan $37$, $x = 3$'te duran $3$ bulur; $x$'i $\frac{7 + 1}{2} = 4$ diye yanlış çözen $19$ bulur.

## ÖSYM tarzı

### Soru 8 · ÖSYM tarzı
Bir mağazada liste fiyatı 400 TL olan bir montta iki kampanya birlikte kullanılabiliyor:

- **İndirim:** fiyatın %25'i düşülür.
- **Kupon:** fiyattan 60 TL düşülür.

Kasada önce indirim sonra kupon uygulanırsa ödenen tutar, önce kupon sonra indirim uygulanırsa ödenen tutardan kaç TL azdır?

A) 0
B) 15
C) 25
D) 45
E) 60

**Cevap:** B
**Çözüm:** İndirim $f(x) = 0{,}75x$, kupon $g(x) = x - 60$. Önce indirim, sonra kupon: $(g \circ f)(400) = g(300) = 240$. Önce kupon, sonra indirim: $(f \circ g)(400) = f(340) = 255$. Fark $255 - 240 = 15$. Kupon önce uygulanırsa 60 TL'nin de %25'i düşer gibi olur; kazanç $60$ yerine $45$ TL'ye iner. $0$ diyen, bileşkede değişme özelliği olduğunu sanmıştır.

### Soru 9 · ÖSYM tarzı
Bir sayı oyununda üç kart vardır:

- **K1:** sayıyı 2 ile çarpar.
- **K2:** sayıya 3 ekler.
- **K3:** sayının karesini alır.

Başlangıç sayısı 2'dir. Oyuncu her kartı birer kez, istediği sırayla kullanır; her kart bir önceki kartın sonucuna uygulanır.

Buna göre oyunun sonunda elde edilebilecek en büyük sayı kaçtır?

A) 11
B) 19
C) 49
D) 50
E) 100

**Cevap:** E
**Çözüm:** Kare alma sayıyı en çok büyüttüğü için en sona bırakılır; önce sayı olabildiğince büyütülür. K2, sonra K1, sonra K3: $2 + 3 = 5$, $5 \cdot 2 = 10$, $10^2 = 100$. Diğer sıralar: K1-K2-K3 ile $(4 + 3)^2 = 49$, K2-K3-K1 ile $25 \cdot 2 = 50$, K1-K3-K2 ile $16 + 3 = 19$, K3-K1-K2 ile $8 + 3 = 11$, K3-K2-K1 ile $7 \cdot 2 = 14$. En büyüğü $100$.

### Soru 10 · ÖSYM tarzı
$[-3, 4]$ aralığında tanımlı $f$ fonksiyonunun grafiği aşağıda verilmiştir. Grafik, işaretli noktaları birleştiren doğru parçalarından oluşur.

![Koordinat düzleminde kırık çizgi grafik: (−3, 0) noktasından (−1, 3)'e çıkıyor, (2, 0)'a iniyor, (4, 2)'ye çıkıyor. Grafik y eksenini (0, 2)'de kesiyor.](gorsel/tyt-matematik/12-01-soru10.svg "Grafik −3 ile 4 arasında tanımlıdır; uç noktalar dahildir.")

Buna göre $(f \circ f)(x) = 0$ eşitliğini sağlayan kaç farklı $x$ değeri vardır?

A) 1
B) 2
C) 3
D) 4
E) 5

**Cevap:** C
**Çözüm:** $f\big(f(x)\big) = 0$ ise $f(x)$, $f$'yi sıfır yapan bir sayıdır. Grafikte $f(t) = 0$ olan yerler $t = -3$ ve $t = 2$. Yani $f(x) = -3$ ya da $f(x) = 2$ olmalı. Grafik hiç $x$ ekseninin altına inmediği için $f(x) = -3$ olamaz. $y = 2$ yatay doğrusu grafiği üç yerde keser: $-3$ ile $-1$ arasında ($x = -\frac{5}{3}$), $x = 0$ ve $x = 4$. Toplam $3$ değer. $2$ diyen, $f(x) = 0$ denkleminin köklerinde kalmıştır.

### Soru 11 · ÖSYM tarzı
Bir hesap makinesindeki T tuşu, ekrandaki $x$ sayısını $mx + n$ sayısına dönüştürüyor ($m > 0$). T tuşuna art arda iki kez basıldığında, başlangıçtaki her $x$ sayısı $4x + 9$ sayısına dönüşüyor.

Buna göre ekranda 1 varken T tuşuna bir kez basılırsa ekranda hangi sayı görünür?

A) $-11$
B) $-7$
C) $3$
D) $5$
E) $13$

**Cevap:** D
**Çözüm:** $f(x) = mx + n$ ise iki basış $(f \circ f)(x) = m(mx + n) + n = m^2x + mn + n$. Bu $4x + 9$'a eşit: $m^2 = 4$ ve $m > 0$ olduğundan $m = 2$; $2n + n = 9$, $n = 3$. $f(1) = 2 + 3 = 5$. Kontrol: $f(5) = 13 = 4 \cdot 1 + 9$. $13$, iki basışın sonucudur. $m > 0$ koşulunu kullanmayan $m = -2$, $n = -9$ ile $-11$ bulur.

### Soru 12 · ÖSYM tarzı
$\{1, 2, 3, 4, 5\}$ kümesinde tanımlı $f$ ve $g$ fonksiyonlarının değerleri aşağıdaki tabloda verilmiştir.

| $x$ | 1 | 2 | 3 | 4 | 5 |
|---|---|---|---|---|---|
| $f(x)$ | 3 | 4 | 1 | 4 | 2 |
| $g(x)$ | 2 | 5 | 4 | 1 | 3 |

Buna göre $(f \circ g)(x) = 4$ eşitliğini sağlayan $x$ değerlerinin toplamı kaçtır?

A) 1
B) 2
C) 3
D) 4
E) 6

**Cevap:** D
**Çözüm:** $f\big(g(x)\big) = 4$ için $g(x)$, $f$'yi $4$ yapan bir sayı olmalı. Tabloda $f(2) = 4$ ve $f(4) = 4$; yani $g(x) = 2$ ya da $g(x) = 4$. $g(1) = 2$ ve $g(3) = 4$; $x = 1$ ve $x = 3$. Toplam $4$. $6 = 2 + 4$, $f(x) = 4$ denkleminin çözümlerini toplamaktır; $1$ ise ters sıradaki $(g \circ f)(x) = 4$ denkleminin tek çözümüdür.
