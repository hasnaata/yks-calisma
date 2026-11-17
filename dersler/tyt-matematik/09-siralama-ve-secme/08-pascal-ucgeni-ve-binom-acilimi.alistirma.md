---
baslik: Pascal Üçgeni ve Binom Açılımı · Alıştırma
ders: tyt-matematik
soru: 12
guncelleme: 2026-11-17
---
# Alıştırma: Pascal Üçgeni ve Binom Açılımı

Sorular özgündür ve ÖSYM soru tarzında yazılmıştır. Derse bakmadan çöz.

## Isınma

### Soru 1 · Kolay
Pascal üçgeninde $(x + y)^6$ açılımının katsayılarını veren satırdaki en büyük sayı kaçtır?

A) 15
B) 20
C) 35
D) 64
E) 70

**Cevap:** B
**Çözüm:** $n = 6$ satırı: $1, 6, 15, 20, 15, 6, 1$. En büyük sayı ortadaki $C(6, 3) = 20$'dir. 15 ortanın bir yanındaki sayıdır; 35, satırı bir aşağı kaydırıp $n = 7$ satırının ($C(7, 3)$) ortasını almaktır; 64 satırın toplamı $2^6$'dır; 70 ise $n = 8$ satırının ortasıdır.

### Soru 2 · Kolay
$(x + y)^9$ ifadesinin açılımında kaç terim vardır?

A) 9
B) 10
C) 11
D) 18
E) 512

**Cevap:** B
**Çözüm:** $(x + y)^n$ açılımında $n + 1$ terim vardır: $9 + 1 = 10$. Terimler $x^9, x^8y, \dots, y^9$; $y$'nin üssü 0'dan 9'a kadar 10 değer alır. 9, ilk terimi ($y^0$) saymamaktır; 512 ise katsayılar toplamı $2^9$'dur.

### Soru 3 · Kolay
$(2x + 3)^4$ ifadesinin açılımındaki katsayılar toplamı kaçtır?

A) 16
B) 81
C) 125
D) 256
E) 625

**Cevap:** E
**Çözüm:** Katsayılar toplamı için $x = 1$ yazılır: $(2 \cdot 1 + 3)^4 = 5^4 = 625$. 16, $(x + y)^n$'e özgü $2^n$ kuralını burada kullanmaktır; 81 sabit terimdir ($x = 0$); 125 ise üssü 3 almaktır.

## Orta

### Soru 4 · Orta
$(x - 2)^5$ ifadesinin açılımında $x^3$'lü terimin katsayısı kaçtır?

A) $-80$
B) $-40$
C) 10
D) 40
E) 80

**Cevap:** D
**Çözüm:** Genel terim $C(5, r)\, x^{5 - r} (-2)^r$. $5 - r = 3 \Rightarrow r = 2$. Katsayı $C(5, 2) \cdot (-2)^2 = 10 \cdot 4 = 40$. $(-2)^2$ pozitiftir; $-40$ işaret hatasıdır. 10, $(-2)^2$ çarpanını unutmaktır. $-80$, $r = 3$ alınarak bulunan $x^2$'li terimin katsayısıdır ($10 \cdot (-8)$).

### Soru 5 · Orta
$\left(x + \dfrac{2}{x}\right)^6$ ifadesinin açılımındaki sabit terim kaçtır?

A) 20
B) 60
C) 160
D) 240
E) 320

**Cevap:** C
**Çözüm:** Genel terim $C(6, r)\, x^{6 - r} \cdot \dfrac{2^r}{x^r} = C(6, r)\, 2^r\, x^{6 - 2r}$. Sabit terimde $6 - 2r = 0$, yani $r = 3$: $C(6, 3) \cdot 2^3 = 20 \cdot 8 = 160$. 20, $2^3$ çarpanını unutmaktır; 60, $r = 2$ ile bulunan $x^2$'li terimin katsayısıdır; 240, $r = 4$ ile bulunan $x^{-2}$'li terimin katsayısıdır; 320 ise $2^3$ yerine $2^4$ yazmaktır.

### Soru 6 · Orta
$(3x - y)^4$ ifadesi $x$'in azalan kuvvetlerine göre açıldığında baştan 3. terim aşağıdakilerden hangisidir?

A) $-108x^3y$
B) $-54x^2y^2$
C) $18x^2y^2$
D) $36x^2y^2$
E) $54x^2y^2$

**Cevap:** E
**Çözüm:** Baştan 3. terim için $r = 2$: $C(4, 2)\,(3x)^2\,(-y)^2 = 6 \cdot 9x^2 \cdot y^2 = 54x^2y^2$. $(-y)^2$ pozitiftir; $-54x^2y^2$ işaret hatasıdır. $18x^2y^2$, $(3x)^2$ yerine $3x^2$ yazmaktır. $36x^2y^2$, katsayıyı $C(4, 3) = 4$ almaktır. $-108x^3y$ ise $r = 1$ ile bulunan 2. terimdir.

### Soru 7 · Orta
$(x^2 - 2x + 3)^5$ ifadesinin açılımında katsayılar toplamı ile sabit terimin toplamı kaçtır?

A) 32
B) 211
C) 243
D) 275
E) 8019

**Cevap:** D
**Çözüm:** Katsayılar toplamı: $x = 1$ yaz, $(1 - 2 + 3)^5 = 2^5 = 32$. Sabit terim: $x = 0$ yaz, $3^5 = 243$. Toplam $32 + 243 = 275$. 211, iki sayıyı çıkarmaktır; 32 ve 243 yalnızca birini bulmaktır; 8019 ise eksi işaretini görmeyip $(1 + 2 + 3)^5 = 7776$ alıp 243 eklemektir.

## ÖSYM tarzı

### Soru 8 · ÖSYM tarzı
Bir oyuncakta en üstten bırakılan top, şekildeki çivilerin her birine çarptığında ya sola ya sağa sapıp bir alt sıradaki çivilerden birine çarpar. Son sıradaki çiviye çarpan top yine sola ya da sağa sapıp alttaki 6 bölmeden birine düşer. Topun her sıradaki sağ–sol tercihlerinin farklı her dizisi farklı bir yol sayılmaktadır.

![Üçgen biçiminde dizilmiş çiviler: en üstte 1, altında 2, 3, 4 ve 5 çivi. Tepede bir top. En altta 1'den 6'ya numaralı 6 bölme; 3 ve 4 numaralı bölmeler mavi.](gorsel/tyt-matematik/09-08-soru8.svg "Top 5 kez sola ya da sağa sapar. 3 ve 4 numaralı bölmeler ortadaki bölmelerdir.")

Buna göre topun 3 ya da 4 numaralı bölmeye düştüğü kaç farklı yol vardır?

A) 10
B) 15
C) 20
D) 32
E) 64

**Cevap:** C
**Çözüm:** Top 5 çiviye çarpar ve her seferinde sola ya da sağa sapar: toplam $2^5 = 32$ yol. $k$ numaralı bölmeye düşmek için 5 sapmanın tam $k - 1$ tanesi sağa olmalıdır; bu, Pascal üçgeninin $n = 5$ satırındaki $C(5, k - 1)$ sayısıdır. 3 numaralı bölme: $C(5, 2) = 10$; 4 numaralı bölme: $C(5, 3) = 10$. Toplam $10 + 10 = 20$. 10 yalnızca bir bölmeyi saymaktır; 15, satırı $n = 6$ alıp $C(6, 2)$ yazmaktır; 32 bütün yollardır; 64 ise 6 bölmeyi 6 sapma sanıp $2^6$ yazmaktır.

### Soru 9 · ÖSYM tarzı
Bir öğrenci Pascal üçgeninin satırlarını tek tek toplayıp her satırın yanına toplamını yazıyor. Bir satırın yanına 256 yazdığını görüyor.

Buna göre bu satırdaki en büyük sayı kaçtır?

A) 28
B) 56
C) 64
D) 70
E) 128

**Cevap:** D
**Çözüm:** $n$. satırın toplamı $2^n$'dir: $2^n = 256 \Rightarrow n = 8$. $n = 8$ satırı $1, 8, 28, 56, 70, 56, 28, 8, 1$; en büyük sayı ortadaki $C(8, 4) = 70$'tir. 128, toplamın yarısını en büyük sayı sanmaktır; 56 ve 28 ortanın yanındaki sayılardır; 64 ise $2^6$'dır.

### Soru 10 · ÖSYM tarzı
Bir öğrenci $(2x - y)^6$ ifadesini $x$'in azalan kuvvetlerine göre açıp terimleri soldan sağa numaralandırıyor. Baştan ve sondan eşit uzaklıkta olan terime "ortadaki terim" diyor.

Buna göre ortadaki terimin katsayısı kaçtır?

A) $-160$
B) $-20$
C) 20
D) 160
E) 240

**Cevap:** A
**Çözüm:** $n = 6$ için açılımda 7 terim var; ortadaki terim 4. terimdir, yani $r = \frac{6}{2} = 3$: $C(6, 3)\,(2x)^3\,(-y)^3 = 20 \cdot 8x^3 \cdot (-y^3) = -160x^3y^3$. Katsayı $-160$. 160, $(-y)^3$'teki eksiyi kaybetmektir; $-20$, $(2x)^3$'teki $8$'i unutmaktır; 240 ise $r = 2$ alınarak bulunan 3. terimin katsayısıdır ($15 \cdot 16$).

### Soru 11 · ÖSYM tarzı
$a$ pozitif bir gerçek sayı olmak üzere $(x + a)^5$ ifadesinin açılımında $x^3$'lü terimin katsayısı 90'dır.

Buna göre aynı açılımda $x^4$'lü terimin katsayısı kaçtır?

A) 15
B) 27
C) 30
D) 45
E) 270

**Cevap:** A
**Çözüm:** $x^3$'lü terim $r = 2$: $C(5, 2)\, a^2 = 10a^2 = 90 \Rightarrow a^2 = 9 \Rightarrow a = 3$ ($a > 0$). $x^4$'lü terim $r = 1$: $C(5, 1) \cdot a = 5 \cdot 3 = 15$. 45, $a$ yerine $a^2 = 9$ kullanmaktır; 30, $C(5, 2) \cdot a$ yazmaktır; 270 ise $x^2$'li terimin katsayısıdır ($C(5, 3) \cdot 27$); 27, $a^3$'tür.

### Soru 12 · ÖSYM tarzı
Bir öğrenci $101 = 100 + 1$ yazarak $101^4$ sayısını hesap makinesi kullanmadan binom açılımıyla buluyor.

Buna göre $101^4$ sayısının rakamları toplamı kaçtır?

A) 5
B) 8
C) 16
D) 32
E) 64

**Cevap:** C
**Çözüm:** $(100 + 1)^4 = 1 \cdot 100^4 + 4 \cdot 100^3 + 6 \cdot 100^2 + 4 \cdot 100 + 1 = 100\,000\,000 + 4\,000\,000 + 60\,000 + 400 + 1 = 104\,060\,401$. Katsayılar tek basamaklı olduğu ve sıfırlar araya girdiği için rakamlar Pascal'ın $n = 4$ satırıdır: $1 + 4 + 6 + 4 + 1 = 16$ (bu da $2^4$'tür). 5, terim sayısını almaktır; 8 ve 32, satırı $n = 3$ ya da $n = 5$ almaktır; 64 ise $2^6$'dır.
