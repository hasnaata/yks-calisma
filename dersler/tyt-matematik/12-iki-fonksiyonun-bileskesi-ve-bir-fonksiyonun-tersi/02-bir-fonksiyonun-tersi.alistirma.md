---
baslik: Bir Fonksiyonun Tersi · Alıştırma
ders: tyt-matematik
soru: 12
guncelleme: 2026-11-17
---
# Alıştırma: Bir Fonksiyonun Tersi

Sorular özgündür ve ÖSYM soru tarzında yazılmıştır. Derse bakmadan çöz.

## Isınma

### Soru 1 · Kolay
Aşağıda $f\colon A \to B$ fonksiyonu ok şemasıyla verilmiştir.

![A = {1, 2, 3, 4} ve B = {2, 5, 6, 8}. Yeşil oklar: 1'den 5'e, 2'den 8'e, 3'ten 2'ye, 4'ten 6'ya.](gorsel/tyt-matematik/12-02-soru1.svg "f⁻¹ için oku tersinden izle: hangi elemandan gelen ok 2'ye varıyor?")

Buna göre $f^{-1}(2) + f(2)$ toplamı kaçtır?

A) $6$
B) $8$
C) $10$
D) $11$
E) $16$

**Cevap:** D
**Çözüm:** $f^{-1}(2)$: $B$'deki $2$'ye gelen ok $A$'daki $3$'ten çıkıyor, $f^{-1}(2) = 3$. $f(2)$: $A$'daki $2$'den çıkan ok $8$'e gidiyor, $f(2) = 8$. Toplam $3 + 8 = 11$. İkisini de $f$ gibi okuyan $8 + 8 = 16$, ikisini de ters okuyan $3 + 3 = 6$ bulur; $f^{-1}(2)$ yerine $2$ yazan $10$ bulur.

### Soru 2 · Kolay
$f(x) = 5x + 2$ olduğuna göre $f^{-1}(x)$ aşağıdakilerden hangisidir?

A) $5x - 2$
B) $\dfrac{x + 2}{5}$
C) $\dfrac{x - 5}{2}$
D) $\dfrac{1}{5x + 2}$
E) $\dfrac{x - 2}{5}$

**Cevap:** E
**Çözüm:** $y = 5x + 2 \Rightarrow y - 2 = 5x \Rightarrow x = \frac{y - 2}{5}$. $y$ yerine $x$ yazılır: $f^{-1}(x) = \frac{x - 2}{5}$. Kontrol: $f(1) = 7$, $f^{-1}(7) = \frac{5}{5} = 1$. D seçeneği $\frac{1}{f(x)}$'tir, ters fonksiyon değildir; B, $2$'yi geri alırken işareti çevirmemektir.

### Soru 3 · Kolay
$f(x) = \dfrac{x + 7}{3}$ olduğuna göre $f^{-1}(4)$ kaçtır?

A) $-1$
B) $\frac{11}{3}$
C) $5$
D) $12$
E) $19$

**Cevap:** C
**Çözüm:** $f^{-1}(4) = a$ ise $f(a) = 4$: $\frac{a + 7}{3} = 4$, $a + 7 = 12$, $a = 5$. $\frac{11}{3}$, $f(4)$ değeridir. $-1$, $\frac{4 - 7}{3}$ işleminden (geri alma sırasını karıştırmaktan); $19$, $3 \cdot 4 + 7$ işleminden (çıkarma yerine toplamaktan) gelir.

## Orta

### Soru 4 · Orta
$f(x) = \dfrac{2x - 3}{x + 4}$ olduğuna göre $f^{-1}(x)$ aşağıdakilerden hangisidir?

A) $\dfrac{-4x - 3}{x - 2}$
B) $\dfrac{4x - 3}{x - 2}$
C) $\dfrac{-4x + 3}{x - 2}$
D) $\dfrac{-4x - 3}{x + 2}$
E) $\dfrac{x + 4}{2x - 3}$

**Cevap:** A
**Çözüm:** $a = 2$, $b = -3$, $c = 1$, $d = 4$. $\frac{ax + b}{cx + d}$'nin tersi $\frac{-dx + b}{cx - a} = \frac{-4x - 3}{x - 2}$. Kontrol: $f(1) = -\frac{1}{5}$ ve $\frac{\frac{4}{5} - 3}{-\frac{1}{5} - 2} = \frac{-\frac{11}{5}}{-\frac{11}{5}} = 1$. B, $d$'nin işaretini değiştirmemek; C, $b$'nin işaretini de değiştirmek; D, $a$'nın işaretini değiştirmemektir. E ise $\frac{1}{f(x)}$'tir.

### Soru 5 · Orta
$f(3x - 1) = 6x + 5$ olduğuna göre $f^{-1}(13)$ kaçtır?

A) $\frac{4}{3}$
B) $3$
C) $10$
D) $33$
E) $83$

**Cevap:** B
**Çözüm:** $f^{-1}(13) = a$ ise $f(a) = 13$. $6x + 5 = 13$ için $x = \frac{4}{3}$; bu durumda $f$'nin içi $3 \cdot \frac{4}{3} - 1 = 3$. Yani $f(3) = 13$ ve $f^{-1}(13) = 3$. Başka yol: $3x - 1 = t$ ile $f(t) = 2t + 7$; $2a + 7 = 13$, $a = 3$. $\frac{4}{3}$ içi hesaplamayı unutmaktır; $33 = f(13)$, $83 = 6 \cdot 13 + 5$; $10$ ise $\frac{13 + 7}{2}$ işleminden gelir.

### Soru 6 · Orta
$f(x) = 3x - 1$ ve $g(x) = x + 4$ olduğuna göre $(f \circ g)^{-1}(8)$ kaçtır?

A) $-1$
B) $\frac{5}{3}$
C) $3$
D) $4$
E) $35$

**Cevap:** A
**Çözüm:** $(f \circ g)^{-1}(8) = g^{-1}\big(f^{-1}(8)\big)$. $f(a) = 8$ için $3a - 1 = 8$, $a = 3$; $g(b) = 3$ için $b + 4 = 3$, $b = -1$. Kontrol: $(f \circ g)(-1) = f(3) = 8$. Sırayı korumak $f^{-1}\big(g^{-1}(8)\big) = f^{-1}(4) = \frac{5}{3}$ verir. $3$ ve $4$ yalnızca bir fonksiyonu geri almaktır; $35 = (f \circ g)(8)$.

### Soru 7 · Orta
$f^{-1}(x) = \dfrac{x + 3}{2}$ ve $g(x) = x^2$ olduğuna göre $(g \circ f)(4)$ kaçtır?

A) $5$
B) $\frac{49}{4}$
C) $16$
D) $25$
E) $29$

**Cevap:** D
**Çözüm:** $(f^{-1})^{-1} = f$. $y = \frac{x + 3}{2} \Rightarrow x = 2y - 3$, yani $f(x) = 2x - 3$. $f(4) = 5$, $g(5) = 25$. Verilen kuralı $f$ sanan $g\left(\frac{7}{2}\right) = \frac{49}{4}$ bulur. $5$, $g$'yi uygulamayı unutmak; $16 = g(4)$; $29 = f\big(g(4)\big) = f(16)$ ise sırayı ters çevirmektir.

## ÖSYM tarzı

### Soru 8 · ÖSYM tarzı
Bir şehirde taksi ücreti, açılış ücreti $25$ TL ve kilometre başına $15$ TL olarak hesaplanmaktadır. $x$ kilometrelik yolculuğun ücreti $f(x) = 15x + 25$ TL'dir.

Can'ın yolculuğu için $190$ TL, Deniz'in yolculuğu için $130$ TL ödenmiştir.

Buna göre $f^{-1}(190) - f^{-1}(130)$ farkı kaçtır?

A) $\frac{7}{3}$
B) $4$
C) $7$
D) $11$
E) $18$

**Cevap:** B
**Çözüm:** $f^{-1}$ ödenen ücretten gidilen yolu verir. $15a + 25 = 190 \Rightarrow a = 11$; $15b + 25 = 130 \Rightarrow b = 7$. Fark $11 - 7 = 4$ km. Açılış ücreti iki yolculukta da ödendiği için kısa yol: $\frac{190 - 130}{15} = 4$. Önce ücretleri çıkarıp sonra $f^{-1}(60) = \frac{60 - 25}{15} = \frac{7}{3}$ hesaplayan, açılış ücretini iki kez düşmüş olur. $18$ ise iki yolu toplamaktır.

### Soru 9 · ÖSYM tarzı
$f\colon [-2, 3] \to [-3, 5]$ bire bir ve örten fonksiyonunun grafiği aşağıda verilmiştir. Grafik, işaretli noktaları birleştiren doğru parçalarından oluşmaktadır.

![Koordinat düzleminde mavi kırık çizgi f: (−2, −3), (0, 2), (2, 3) ve (3, 5) noktalarını birleştiriyor. Noktalardan eksenlere kesikli çizgiler iniyor.](gorsel/tyt-matematik/12-02-soru9.svg "f⁻¹ değeri için sayıyı y ekseninde bul, grafiğe yatay git, x değerini oku.")

Buna göre $(f^{-1} \circ f^{-1})(3)$ değeri kaçtır?

A) $-3$
B) $0$
C) $2$
D) $3$
E) $5$

**Cevap:** B
**Çözüm:** $(f^{-1} \circ f^{-1})(3) = f^{-1}\big(f^{-1}(3)\big)$. $y = 3$ değerini alan nokta $(2, 3)$: $f^{-1}(3) = 2$. $y = 2$ değerini alan nokta $(0, 2)$: $f^{-1}(2) = 0$. Sonuç $0$. Tek adımda kalan $2$, $3$'ü $x$ ekseninde arayıp $f(3)$ okuyan $5$ bulur. İkinci adımda $f$ uygulayan $f(2) = 3$ bulur.

### Soru 10 · ÖSYM tarzı
$f$ doğrusal bir fonksiyondur. $f^{-1}$ fonksiyonunun grafiği $(1, 3)$ ve $(5, 4)$ noktalarından geçmektedir.

Buna göre $f(2)$ kaçtır?

A) $-3$
B) $-\frac{1}{2}$
C) $2$
D) $\frac{13}{4}$
E) $\frac{11}{3}$

**Cevap:** A
**Çözüm:** $(1, 3) \in f^{-1}$ ise $(3, 1) \in f$; $(5, 4) \in f^{-1}$ ise $(4, 5) \in f$. $f(x) = mx + n$: $3m + n = 1$ ve $4m + n = 5$. Çıkarınca $m = 4$, $n = -11$. $f(x) = 4x - 11$, $f(2) = -3$. Noktaları doğrudan $f$'nin noktası sanan $f^{-1}(2) = \frac{13}{4}$ bulur. Yalnız bir noktanın bileşenlerini çeviren $-\frac{1}{2}$ ya da $\frac{11}{3}$ bulur.

### Soru 11 · ÖSYM tarzı
Bir hesap makinesindeki $T$ tuşu, ekrandaki $x$ sayısını ($x \neq 2$)

$$\frac{ax + 3}{x - 2}$$

sayısına çevirmektedir. Ekrandaki hangi sayıyla başlanırsa başlansın, $T$ tuşuna art arda iki kez basıldığında ekranda başlangıçtaki sayı görülmektedir.

Buna göre $a$ kaçtır?

A) $-3$
B) $-2$
C) $-\frac{1}{2}$
D) $\frac{1}{2}$
E) $2$

**Cevap:** E
**Çözüm:** İki kez basınca sayı geri geliyorsa ikinci basış birincinin yaptığını geri alıyor: $T \circ T = I$, yani $T^{-1} = T$. $T(x) = \frac{ax + 3}{x - 2}$ için $T^{-1}(x) = \frac{2x + 3}{x - a}$. İkisinin eşit olması için $a = 2$ olmalı. Kontrol: $a = 2$ iken $T(5) = \frac{13}{3}$ ve $T\left(\frac{13}{3}\right) = \frac{\frac{26}{3} + 3}{\frac{7}{3}} = \frac{35}{7} = 5$. $-2$, ters alırken $d$'nin işaretini değiştirmeyi unutmaktan gelir.

### Soru 12 · ÖSYM tarzı
Bir oyunda iki makine vardır:

- $F$ makinesi kendisine verilen sayıyı $3$ ile çarpıp $4$ ekler.
- $G$ makinesi kendisine verilen sayının yarısını verir.

Ece bir sayıyı önce $F$ makinesine verdi, çıkan sayıyı $G$ makinesine verdi ve son olarak $11$ sayısını elde etti.

Buna göre Ece'nin başlangıçta verdiği sayı kaçtır?

A) $\frac{7}{3}$
B) $\frac{14}{3}$
C) $6$
D) $\frac{37}{2}$
E) $22$

**Cevap:** C
**Çözüm:** $F(x) = 3x + 4$, $G(x) = \frac{x}{2}$; Ece'nin işlemi $(G \circ F)(x) = 11$. Geri almak için son makineden başla: $G^{-1}(11) = 22$, sonra $F^{-1}(22) = \frac{22 - 4}{3} = 6$. Kontrol: $F(6) = 22$, $G(22) = 11$. Ters sırada geri alan $G^{-1}\big(F^{-1}(11)\big) = 2 \cdot \frac{7}{3} = \frac{14}{3}$ bulur. $\frac{7}{3}$ yalnızca $F$'yi, $22$ yalnızca $G$'yi geri almaktır; $\frac{37}{2}$ ise $11$'i makinelere ileri yönde vermektir.
