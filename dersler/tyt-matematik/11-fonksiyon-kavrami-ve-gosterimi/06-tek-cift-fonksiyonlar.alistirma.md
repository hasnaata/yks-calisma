---
baslik: Tek-Çift Fonksiyonlar · Alıştırma
ders: tyt-matematik
soru: 12
guncelleme: 2026-11-18
---
# Alıştırma: Tek-Çift Fonksiyonlar

Sorular özgündür ve ÖSYM soru tarzında yazılmıştır. Derse bakmadan çöz.

## Isınma

### Soru 1 · Kolay
$f\colon \mathbb{R} \to \mathbb{R}$ çift fonksiyon ve $f(4) = 7$ olduğuna göre $f(-4) - 2f(4)$ kaçtır?

A) $-21$
B) $-7$
C) $0$
D) $7$
E) $21$

**Cevap:** B
**Çözüm:** $f$ çift olduğundan $f(-4) = f(4) = 7$. İşlem: $7 - 2 \cdot 7 = -7$. $f$'yi tek sanıp $f(-4) = -7$ alan $-7 - 14 = -21$ bulur.

### Soru 2 · Kolay
Aşağıdaki fonksiyonlardan hangisi tek fonksiyondur?

A) $f(x) = x^3 + 1$
B) $f(x) = x^4 + x$
C) $f(x) = x^2 - 3$
D) $f(x) = 2x^5 - x^3$
E) $f(x) = x^3 + x^2$

**Cevap:** D
**Çözüm:** D'de yalnızca tek dereceli terimler var: $f(-x) = -2x^5 + x^3 = -(2x^5 - x^3) = -f(x)$. A'da sabit terim var ($f(0) = 1 \ne 0$). C çifttir. B ve E'de hem tek hem çift dereceli terim bulunduğu için ne tek ne çifttir.

### Soru 3 · Kolay
Aşağıda üç fonksiyonun grafiği verilmiştir.

![Yan yana üç grafik. I: orijinden geçen, soldan sağa sürekli artan, x³'e benzeyen bir eğri. II: kolları yukarı bakan, y ekseninde −2'de en düşük noktası olan bir parabol. III: orijinden geçen, sağa doğru azalan bir doğru.](gorsel/tyt-matematik/11-06-soru3.svg "Her grafiği orijin etrafında yarım tur çevir; hangisi kendisiyle çakışıyor?")

Bu grafiklerden hangileri tek fonksiyona aittir?

A) Yalnız I
B) Yalnız II
C) Yalnız III
D) I ve II
E) I ve III

**Cevap:** E
**Çözüm:** Tek fonksiyonun grafiği orijine göre simetriktir. I ve III orijinden geçer; her $(a, b)$ noktasının eşi $(-a, -b)$ de grafikte. II ise $y$ eksenine göre simetriktir, yani çift fonksiyondur. Orijinden geçen doğru ($y = mx$) da tek fonksiyondur; III'ü eğri olmadığı için eleyen A'yı seçer.

## Orta

### Soru 4 · Orta
$f\colon \mathbb{R} \to \mathbb{R}$,

$$f(x) = (a - 2)x^5 + 3x^4 + (b + 3)x + 1$$

çift fonksiyon olduğuna göre $a - b$ farkı kaçtır?

A) $-6$
B) $-5$
C) $-1$
D) $1$
E) $5$

**Cevap:** E
**Çözüm:** Çift fonksiyonda tek dereceli terim kalamaz. $x^5$'in katsayısı: $a - 2 = 0$, $a = 2$. $x$'in katsayısı: $b + 3 = 0$, $b = -3$. $a - b = 2 - (-3) = 5$. $a + b$'yi hesaplayan $-1$, $b - a$'yı hesaplayan $-5$, $a \cdot b$'yi hesaplayan $-6$ bulur. Sabit terim $1$ çift fonksiyonda kalabilir.

### Soru 5 · Orta
$f\colon \mathbb{R} \to \mathbb{R}$,

$$f(x) = (a + 1)x^4 + 2x^3 + (b - 3)x^2 + x + a + c$$

tek fonksiyon olduğuna göre $a + b + c$ toplamı kaçtır?

A) $-3$
B) $1$
C) $3$
D) $5$
E) $7$

**Cevap:** C
**Çözüm:** Tek fonksiyonda çift dereceli terim ve sabit terim kalamaz. $a + 1 = 0$, $a = -1$. $b - 3 = 0$, $b = 3$. Sabit terim $a + c = 0$, $c = 1$. Toplam $-1 + 3 + 1 = 3$. Kural $f(x) = 2x^3 + x$ olur. $a + c = 0$ eşitliğinden $c = -1$ çıkaran 1; $b = -3$ alan $-3$ bulur.

### Soru 6 · Orta
$f$ tek, $g$ çift fonksiyondur.

$f(3) = 4$ ve $g(3) = -2$ olduğuna göre $2f(-3) - g(-3)$ kaçtır?

A) $-10$
B) $-6$
C) $-2$
D) $6$
E) $10$

**Cevap:** B
**Çözüm:** $f$ tek: $f(-3) = -4$. $g$ çift: $g(-3) = -2$. İşlem: $2 \cdot (-4) - (-2) = -8 + 2 = -6$. $g$'yi de tek sanan $-8 - 2 = -10$; $f$'yi çift sanan $8 + 2 = 10$; ikisini birden ters alan $8 - 2 = 6$ bulur.

### Soru 7 · Orta
$f\colon \mathbb{R} \to \mathbb{R}$ tek, $g\colon \mathbb{R} \to \mathbb{R}$ çift fonksiyondur.

I. $h(x) = f(x) \cdot g(x)$
II. $k(x) = f(x) \cdot f(x)$
III. $m(x) = f(x) + x^3$

fonksiyonlarından hangileri kesinlikle tek fonksiyondur?

A) Yalnız I
B) Yalnız II
C) I ve II
D) I ve III
E) II ve III

**Cevap:** D
**Çözüm:** Her birinde $x$ yerine $-x$ koy.
I. $h(-x) = f(-x) \cdot g(-x) = -f(x) \cdot g(x) = -h(x)$: tek.
II. $k(-x) = (-f(x)) \cdot (-f(x)) = f(x) \cdot f(x) = k(x)$: çift (tek $\cdot$ tek = çift).
III. $m(-x) = -f(x) - x^3 = -(f(x) + x^3) = -m(x)$: tek (tek $+$ tek = tek).
Doğru cevap I ve III.

## ÖSYM tarzı

### Soru 8 · ÖSYM tarzı
$f$ çift, $g$ tek fonksiyondur. Bu fonksiyonlar için

- $f(2) + g(2) = 7$
- $f(-2) + g(-2) = 3$

eşitlikleri veriliyor.

Buna göre $g(2)$ kaçtır?

A) 2
B) 3
C) 4
D) 5
E) 7

**Cevap:** A
**Çözüm:** İkinci eşitlikte $f(-2) = f(2)$ ve $g(-2) = -g(2)$ yaz: $f(2) - g(2) = 3$. Birinci eşitlikle taraf tarafa çıkar: $2g(2) = 7 - 3 = 4$, $g(2) = 2$. Buradan $f(2) = 5$. İkiye bölmeyi unutan 4; $f$ ile $g$'nin rollerini karıştıran 5 bulur.

### Soru 9 · ÖSYM tarzı
$f$ fonksiyonu $[-5, 5]$ aralığında tanımlı bir tek fonksiyondur. Aşağıda $f$'nin grafiğinin yalnızca $[0, 5]$ aralığındaki kısmı çizilmiştir.

![Kareli koordinat düzleminde iki doğru parçası: (0, 0)'dan (2, 4)'e çıkıyor, oradan (5, −2)'ye iniyor. Grafiğin x < 0 kısmı çizilmemiş.](gorsel/tyt-matematik/11-06-soru9.svg "Grafiğin x < 0 kısmını tek fonksiyon kuralıyla kendin tamamla.")

Buna göre $f(x) = -2$ denkleminin $[-5, 5]$ aralığında kaç farklı kökü vardır?

A) 1
B) 2
C) 3
D) 4
E) 5

**Cevap:** C
**Çözüm:** $x \ge 0$ kısmında $f(x) = -2$ yalnızca $x = 5$'te olur (birinci parça $0$ ile $4$ arasında kalır). $x < 0$ için $f(x) = -f(-x)$; $f(x) = -2$ demek $f(-x) = 2$ demektir. Çizili kısımda $f = 2$ olan yerler: birinci parçada $x = 1$, ikinci parçada ($x$ 1 artınca $y$ 2 azalır, $4 \to 2$) $x = 3$. Buradan $x = -1$ ve $x = -3$. Kökler $-3$, $-1$, $5$: 3 tane. Yalnızca çizili kısma bakan 1; grafiği çift fonksiyon gibi $y$ ekseninden aynalayan ($x = -5$) 2 bulur.

### Soru 10 · ÖSYM tarzı
$f(x) = ax^3 + bx^2 + cx + d$ polinom fonksiyonu için her $x$ gerçek sayısında

- $f(x) - f(-x) = 6x^3 - 4x$
- $f(x) + f(-x) = 8x^2 + 2$

eşitlikleri sağlanmaktadır.

Buna göre $f(1)$ kaçtır?

A) 1
B) 4
C) 5
D) 6
E) 12

**Cevap:** D
**Çözüm:** $f(-x) = -ax^3 + bx^2 - cx + d$. Fark alınınca çift dereceli terimler gider: $f(x) - f(-x) = 2ax^3 + 2cx$, yani $2a = 6$, $a = 3$ ve $2c = -4$, $c = -2$. Toplam alınınca tek dereceli terimler gider: $f(x) + f(-x) = 2bx^2 + 2d$, yani $b = 4$, $d = 1$. $f(1) = 3 + 4 - 2 + 1 = 6$. İkiye bölmeyi unutan 12; yalnızca tek kısmı ($3 - 2 = 1$) ya da yalnızca çift kısmı ($4 + 1 = 5$) alan 1 ya da 5; $f(-1)$'i hesaplayan 4 bulur.

### Soru 11 · ÖSYM tarzı
$f\colon \mathbb{R} \to \mathbb{R}$ tek fonksiyondur ve $x \ge 0$ için

$$f(x) = x^2 - 4x$$

kuralıyla tanımlanmıştır.

Buna göre $f(-1) + f(-5)$ toplamı kaçtır?

A) $-8$
B) $-2$
C) $0$
D) $2$
E) $8$

**Cevap:** B
**Çözüm:** Kural yalnızca $x \ge 0$ için verildi; $-1$ ve $-5$'i doğrudan yerine koyamazsın. Tek fonksiyon kuralını kullan: $f(1) = 1 - 4 = -3$, $f(-1) = 3$. $f(5) = 25 - 20 = 5$, $f(-5) = -5$. Toplam $3 + (-5) = -2$. Fonksiyonu çift sanan $-3 + 5 = 2$ bulur.

### Soru 12 · ÖSYM tarzı
Bir tek fonksiyonun grafiği $A(2,\ a + 3)$ ve $B(-2,\ 2a - 9)$ noktalarından geçmektedir.

Buna göre $f(-2)$ kaçtır?

A) $-5$
B) $2$
C) $5$
D) $12$
E) $15$

**Cevap:** A
**Çözüm:** $f(2) = a + 3$ ve $f(-2) = 2a - 9$. Tek fonksiyonda $f(-2) = -f(2)$: $2a - 9 = -a - 3$, $3a = 6$, $a = 2$. $f(-2) = 2 \cdot 2 - 9 = -5$ (kontrol: $f(2) = 5$). $a$'yı cevap sanan 2, $f(2)$'yi veren 5 bulur. Fonksiyonu çift sanıp $2a - 9 = a + 3$ yazan $a = 12$ ve $f(-2) = 15$ bulur.
