---
baslik: Fonksiyon Kavramı ve Gösterimi · Alıştırma
ders: tyt-matematik
soru: 12
guncelleme: 2026-11-17
---
# Alıştırma: Fonksiyon Kavramı ve Gösterimi

Sorular özgündür ve ÖSYM soru tarzında yazılmıştır. Derse bakmadan çöz.

## Isınma

### Soru 1 · Kolay
$A = \{1, 2, 3\}$ ve $B = \{a, b, c, d\}$ olduğuna göre aşağıdaki bağıntılardan hangisi $A$'dan $B$'ye bir fonksiyondur?

A) $\{(1, a),\ (2, b)\}$
B) $\{(1, a),\ (1, b),\ (2, c),\ (3, d)\}$
C) $\{(a, 1),\ (b, 2),\ (c, 3)\}$
D) $\{(1, a),\ (2, b),\ (3, c),\ (4, d)\}$
E) $\{(1, c),\ (2, c),\ (3, c)\}$

**Cevap:** E
**Çözüm:** E'de $1$, $2$ ve $3$'ün her birinin tam bir görüntüsü var ($c$). Hepsinin aynı elemana gitmesi sorun değildir. A'da $3$ boşta kalır; B'de $1$'in iki görüntüsü var; C, $B$'den $A$'ya yazılmıştır; D'de $4 \notin A$.

### Soru 2 · Kolay
Aşağıda $f\colon A \to B$ fonksiyonu ok şemasıyla verilmiştir.

![Ok şeması: A kümesinde 1, 2, 3, 4; B kümesinde 2, 5, 7, 9, 11. Oklar: 1'den 5'e, 2'den 7'ye, 3'ten 5'e, 4'ten 9'a.](gorsel/tyt-matematik/11-01-soru2.svg "Hangi elemanlara ok geldiğine bak.")

Buna göre $f$'nin görüntü kümesi kaç elemanlıdır?

A) 2
B) 3
C) 4
D) 5
E) 6

**Cevap:** B
**Çözüm:** Ok gelen elemanlar $5$, $7$ ve $9$: $f(A) = \{5, 7, 9\}$, 3 eleman. $5$'e iki ok gelse de bir kez sayılır. 4, tanım kümesinin; 5, değer kümesinin eleman sayısıdır.

### Soru 3 · Kolay
$A = \{-1, 0, 2\}$ olmak üzere $f\colon A \to \mathbb{R}$, $f(x) = 3x - 2$ fonksiyonunun görüntü kümesi aşağıdakilerden hangisidir?

A) $\{-5, -2, 4\}$
B) $\{-5, 2, 4\}$
C) $\{-1, -2, 4\}$
D) $\{-1, 0, 2\}$
E) $\{1, -2, 4\}$

**Cevap:** A
**Çözüm:** $f(-1) = -3 - 2 = -5$, $f(0) = -2$, $f(2) = 6 - 2 = 4$. Görüntü kümesi $\{-5, -2, 4\}$. D seçeneği tanım kümesidir; B, $f(0)$'ı $2$ almak; C, $3 \cdot (-1) - 2$ işlemini $-3 + 2$ yapmaktır.

## Orta

### Soru 4 · Orta
$s(A) = 3$ ve $s(B) = 4$ olduğuna göre $A$'dan $B$'ye kaç farklı fonksiyon tanımlanabilir?

A) 7
B) 12
C) 24
D) 64
E) 81

**Cevap:** D
**Çözüm:** $A$'nın 3 elemanının her biri için 4 seçenek var: $4 \cdot 4 \cdot 4 = 4^3 = 64$. Üssü ters koyan $3^4 = 81$, görüntüleri farklı seçmeye çalışan $4 \cdot 3 \cdot 2 = 24$, çarpan $12$, toplayan $7$ bulur.

### Soru 5 · Orta
$A = \{1, 2, 3, 4\}$ ve $B = \{a, b, c\}$ olmak üzere $A$'dan $B$'ye tanımlanan fonksiyonlardan kaç tanesinde $f(1) = a$ olur?

A) 9
B) 12
C) 27
D) 64
E) 81

**Cevap:** C
**Çözüm:** $f(1)$ sabit, seçim yok. Kalan $2$, $3$, $4$ elemanlarının her biri için 3 seçenek: $3^3 = 27$. Koşulu görmeyen $3^4 = 81$, üssü ters koyan $4^3 = 64$ bulur.

### Soru 6 · Orta
$A = \{-1, 0, 2\}$ olmak üzere

$$f = \{(-1, 3),\ (2, a - 1),\ (0, 5),\ (2, 7)\}$$

bağıntısı $A$'dan $\mathbb{R}$'ye bir fonksiyondur. Buna göre $a$ kaçtır?

A) 4
B) 5
C) 6
D) 7
E) 8

**Cevap:** E
**Çözüm:** $2$ iki ikilide birinci bileşen. Fonksiyonda $2$'nin tek görüntüsü olacağından ikinci bileşenler eşittir: $a - 1 = 7$, $a = 8$. $7$, $a - 1$ ifadesindeki $-1$'i unutmaktır; $6$, $a - 1$'i yanlışlıkla $0$'ın görüntüsü $5$'e eşitlemek, $4$ ise $-1$'in görüntüsü $3$'e eşitlemektir.

### Soru 7 · Orta
$A = \{-2, -1, 0, 1, 2\}$ ve $B = \{0, 1, 2, 3, 4\}$ olmak üzere $f\colon A \to B$, $f(x) = x^2$ fonksiyonu veriliyor.

Buna göre aşağıdakilerden hangisi **yanlıştır**?

A) Görüntü kümesi değer kümesine eşittir.
B) $f(-2) = f(2)$'dir.
C) Görüntü kümesi 3 elemanlıdır.
D) $3$, değer kümesinde vardır ama görüntü kümesinde yoktur.
E) Tanım kümesi 5 elemanlıdır.

**Cevap:** A
**Çözüm:** Görüntüler: $f(\pm 2) = 4$, $f(\pm 1) = 1$, $f(0) = 0$. Görüntü kümesi $\{0, 1, 4\}$, 3 eleman (C doğru). $2$ ve $3$ değer kümesinde var ama hiçbir elemanın görüntüsü değil (D doğru); bu yüzden görüntü kümesi değer kümesine eşit değildir, A yanlıştır. B ve E de doğrudur.

## ÖSYM tarzı

### Soru 8 · ÖSYM tarzı
Bir okulda 5 öğrencinin her biri satranç, tiyatro ve müzik kulüplerinden **tam olarak birine** yazılacaktır. Bir kulübe birden çok öğrenci yazılabilir ya da hiç öğrenci yazılmayabilir.

Öğrencilerden Ece ile Deniz'in aynı kulübe yazılması istendiğine göre, yazılım kaç farklı biçimde yapılabilir?

A) 15
B) 27
C) 81
D) 125
E) 243

**Cevap:** C
**Çözüm:** Her öğrenciyi bir kulübe eşlemek, 5 elemanlı kümeden 3 elemanlı kümeye bir fonksiyondur. Ece ile Deniz aynı kulübe gideceği için ikisi tek eleman gibi düşünülür: 4 serbest seçim, $3^4 = 81$. Koşulu görmeyen $3^5 = 243$, üssü ters koyan $5^3 = 125$ bulur.

### Soru 9 · ÖSYM tarzı
400 öğrencisi olan bir okulda $Ö$ öğrenciler kümesi, $M$ yılın 12 ayının kümesi ve $\mathbb{N}$ doğal sayılar kümesidir. Her öğrencinin farklı bir okul numarası vardır.

I. Her öğrenciyi doğduğu aya eşleyen kural ($Ö \to M$)
II. Her ayı o ayda doğan öğrenciye eşleyen kural ($M \to Ö$)
III. Her öğrenciyi okul numarasına eşleyen kural ($Ö \to \mathbb{N}$)

Bu kurallardan hangileri fonksiyondur?

A) Yalnız I
B) Yalnız III
C) I ve II
D) I ve III
E) I, II ve III

**Cevap:** D
**Çözüm:** I: Her öğrencinin tek bir doğum ayı vardır; fonksiyon. III: Her öğrencinin tek bir okul numarası vardır; fonksiyon. II: 400 öğrenci 12 aya dağıldığından bazı aylarda birden çok öğrenci doğmuştur ($12 \cdot 33 = 396 < 400$). Bu ayın birden çok görüntüsü olur; fonksiyon değildir.

### Soru 10 · ÖSYM tarzı
$A$ ve $B$ kümeleri için $s(A) > s(B) > 1$ olmak üzere $A$'dan $B$'ye tam olarak 81 farklı fonksiyon tanımlanabilmektedir.

Buna göre $s(A) + s(B)$ toplamı kaçtır?

A) 6
B) 7
C) 11
D) 12
E) 82

**Cevap:** B
**Çözüm:** $s(A) = m$, $s(B) = n$ ise $n^m = 81$. $81 = 3^4 = 9^2 = 81^1$. $m > n > 1$ koşulunu yalnızca $n = 3$, $m = 4$ sağlar ($9^2$'de $2 < 9$; $81^1$'de $m = 1$). Toplam $4 + 3 = 7$. $9^2$'yi alan 11, $81^1$'i alan 82, çarpan 12 bulur.

### Soru 11 · ÖSYM tarzı
Bir okulda 1, 2 ve 3 numaralı üç öğretmen, 1, 2, 3 ve 4 numaralı dört sınıftan birine nöbetçi olarak atanacaktır. Her öğretmen tek bir sınıfa atanır; bir sınıfa birden çok öğretmen atanabilir ya da hiç atanmayabilir. Hiçbir öğretmen kendi numarasıyla aynı numaralı sınıfa atanmayacaktır.

Buna göre atama kaç farklı biçimde yapılabilir?

A) 24
B) 27
C) 36
D) 64
E) 81

**Cevap:** B
**Çözüm:** Atama, öğretmenler kümesinden sınıflar kümesine bir fonksiyondur. Her öğretmen kendi numaralı sınıf dışındaki 3 sınıftan birini alır: $3 \cdot 3 \cdot 3 = 27$. Koşulu görmeyen $4^3 = 64$, öğretmenleri farklı sınıflara koyan $4 \cdot 3 \cdot 2 = 24$, üssü ters koyan $3^4 = 81$ bulur.

### Soru 12 · ÖSYM tarzı
$A = \{1, 2, 3, 4\}$ olmak üzere $f\colon A \to \mathbb{Z}$ fonksiyonu

$$f = \{(1, a),\ (2, 3),\ (3, a + 2),\ (4, 5)\}$$

biçiminde tanımlanıyor. $f$'nin görüntü kümesi **3 elemanlı** olduğuna göre $a$'nın alabileceği değerlerin toplamı kaçtır?

A) 1
B) 4
C) 5
D) 6
E) 9

**Cevap:** D
**Çözüm:** Görüntüler $a$, $3$, $a + 2$, $5$. Dört görüntüden tam iki tanesi eşit olmalı. $a \ne a + 2$ her zaman. Olasılıklar: $a = 3$ ise görüntüler $3, 3, 5, 5$; küme $\{3, 5\}$, 2 eleman (olmaz). $a = 5$ ise $\{3, 5, 7\}$, 3 eleman. $a + 2 = 3$, yani $a = 1$ ise $\{1, 3, 5\}$, 3 eleman. $a + 2 = 5$ yine $a = 3$ demektir. Uygun değerler $1$ ve $5$, toplam $6$. $a = 3$'ü de katan 9 bulur.
