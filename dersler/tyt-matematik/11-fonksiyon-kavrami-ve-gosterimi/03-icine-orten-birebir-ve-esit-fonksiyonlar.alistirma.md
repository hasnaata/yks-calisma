---
baslik: İçine, Örten, Birebir ve Eşit Fonksiyonlar · Alıştırma
ders: tyt-matematik
soru: 12
guncelleme: 2026-11-17
---
# Alıştırma: İçine, Örten, Birebir ve Eşit Fonksiyonlar

Sorular özgündür ve ÖSYM soru tarzında yazılmıştır. Derse bakmadan çöz.

## Isınma

### Soru 1 · Kolay
Aşağıda $f\colon A \to B$ fonksiyonu ok şemasıyla verilmiştir.

![Ok şeması: A kümesinde 1, 2, 3, 4; B kümesinde 5, 6, 7, 8. Oklar: 1'den 6'ya, 2'den 5'e, 3'ten 8'e, 4'ten 6'ya.](gorsel/tyt-matematik/11-03-soru1.svg "Hem boşta kalan elemana hem iki ok alan elemana bak.")

Buna göre $f$ için aşağıdakilerden hangisi doğrudur?

A) İçine ve bire birdir.
B) Örten ve bire birdir.
C) Örtendir, bire bir değildir.
D) İçinedir, bire bir değildir.
E) Fonksiyon değildir.

**Cevap:** D
**Çözüm:** $7$'ye hiç ok gelmiyor: $f(A) = \{5, 6, 8\} \ne B$, yani $f$ içinedir. $6$'ya hem $1$'den hem $4$'ten ok geliyor: $f(1) = f(4)$, yani bire bir değildir. $A$'nın her elemanından tek ok çıktığı için fonksiyondur.

### Soru 2 · Kolay
$A = \{1, 2, 3, 4\}$ ve $B = \{a, b, c\}$ olduğuna göre aşağıdakilerden hangisi $A$'dan $B$'ye örten bir fonksiyondur?

A) $\{(1, a),\ (2, b),\ (3, c),\ (4, a)\}$
B) $\{(1, a),\ (2, b),\ (3, a),\ (4, b)\}$
C) $\{(1, a),\ (2, b),\ (3, c)\}$
D) $\{(1, c),\ (2, c),\ (3, c),\ (4, c)\}$
E) $\{(1, a),\ (1, b),\ (2, c),\ (3, a),\ (4, b)\}$

**Cevap:** A
**Çözüm:** A'da her elemanın tek görüntüsü var ve görüntü kümesi $\{a, b, c\} = B$: örten fonksiyon. B'de $c$, D'de $a$ ve $b$ boşta kalır (içine). C'de $4$'ün görüntüsü yok, E'de $1$'in iki görüntüsü var; ikisi fonksiyon değildir.

### Soru 3 · Kolay
$A = \{-1, 0, 1\}$ olmak üzere $f\colon A \to \mathbb{R}$, $f(x) = x^3$ fonksiyonu veriliyor. Aynı kümede tanımlı aşağıdaki $g$ fonksiyonlarından hangisi $f$'ye eşittir?

A) $g(x) = x^2$
B) $g(x) = x$
C) $g(x) = |x|$
D) $g(x) = 2x$
E) $g(x) = -x$

**Cevap:** B
**Çözüm:** $f(-1) = -1$, $f(0) = 0$, $f(1) = 1$. $g(x) = x$ de aynı üç değeri verir, bu yüzden $f = g$. $x^2$ ve $|x|$, $x = -1$ için $1$ verir; $2x$, $x = 1$ için $2$ verir; $-x$, $x = 1$ için $-1$ verir.

## Orta

### Soru 4 · Orta
$s(A) = 3$ ve $s(B) = 5$ olduğuna göre $A$'dan $B$'ye kaç tane bire bir fonksiyon tanımlanabilir?

A) 15
B) 60
C) 120
D) 125
E) 243

**Cevap:** B
**Çözüm:** $A$'nın elemanlarına sırayla görüntü seç: ilki için 5, ikincisi için kalan 4, üçüncüsü için kalan 3 seçenek. $5 \cdot 4 \cdot 3 = 60$. $5^3 = 125$ bütün fonksiyonların sayısı, $3^5 = 243$ üssü ters koymak, $5! = 120$ çarpanı fazla almak, $15$ ise $5 \cdot 3$ çarpımıdır.

### Soru 5 · Orta
$s(A) = s(B) = 4$ olduğuna göre $A$'dan $B$'ye tanımlanabilecek içine fonksiyonların sayısı kaçtır?

A) 24
B) 64
C) 232
D) 256
E) 280

**Cevap:** C
**Çözüm:** Bütün fonksiyonlar $4^4 = 256$ tane. $s(A) = s(B)$ olduğu için örten olanlar tam olarak bire bir olanlardır: $4! = 24$. İçine olanlar: $256 - 24 = 232$. $24$ örten fonksiyon sayısı, $256$ bütün fonksiyonlar, $280$ ise çıkarmak yerine toplamaktır.

### Soru 6 · Orta
$A = \{1, 2\}$ olmak üzere $f, g\colon A \to \mathbb{R}$, $f(x) = ax + b$ ve $g(x) = x^2 + 1$ fonksiyonları eşittir. Buna göre $a \cdot b$ çarpımı kaçtır?

A) $-6$
B) $-3$
C) $-2$
D) $2$
E) $3$

**Cevap:** B
**Çözüm:** $f = g$ ise $A$'nın her elemanında değerler eşit. $x = 1$: $a + b = 1 + 1 = 2$. $x = 2$: $2a + b = 4 + 1 = 5$. Taraf tarafa çıkar: $a = 3$, $b = -1$. $a \cdot b = -3$. $g(x)$'teki $+1$'i unutan $a + b = 1$, $2a + b = 4$ bulur ve $3 \cdot (-2) = -6$ der.

### Soru 7 · Orta
$f\colon [-1, 3] \to [a, b]$, $f(x) = 5 - 2x$ fonksiyonu örtendir. Buna göre $b - a$ farkı kaçtır?

A) $-8$
B) $-6$
C) $4$
D) $6$
E) $8$

**Cevap:** E
**Çözüm:** Örten olduğu için $[a, b]$ görüntü kümesidir. Sınırların görüntüleri: $f(-1) = 5 + 2 = 7$, $f(3) = 5 - 6 = -1$. Fonksiyon azalan olduğundan küçük değer $-1$, büyük değer $7$: $[a, b] = [-1, 7]$, $b - a = 8$. $a = f(-1)$, $b = f(3)$ diye sırayla eşleyen $-1 - 7 = -8$ bulur; $6$ ise $a + b$'dir.

## ÖSYM tarzı

### Soru 8 · ÖSYM tarzı
Bir şifreleme yönteminde alfabenin ilk altı harfi sıra numaralarıyla, yani $A = \{1, 2, 3, 4, 5, 6\}$ kümesinin elemanlarıyla gösteriliyor. Her harf bir $f$ kuralıyla bir doğal sayıya çevriliyor. Şifrenin geri çözülebilmesi için **farklı harflerin farklı sayılara** gitmesi gerekiyor.

Buna göre aşağıdaki kurallardan hangisiyle yazılan şifre her zaman geri çözülebilir?

A) $f(x)$: $x$'in 5'e bölümünden kalan
B) $f(x) = (x - 3)^2$
C) $f(x) = 7 - x$
D) $f(x) = |2x - 7|$
E) $f(x) = x \cdot (7 - x)$

**Cevap:** C
**Çözüm:** İstenen, $f$'nin $A$ üzerinde bire bir olmasıdır. C'de görüntüler $6, 5, 4, 3, 2, 1$; hepsi farklı. Diğerlerinde aynı sayıya giden iki harf var: A'da $f(1) = f(6) = 1$; B'de $f(2) = f(4) = 1$; D'de $f(3) = f(4) = 1$; E'de $f(1) = f(6) = 6$.

### Soru 9 · ÖSYM tarzı
Aşağıda gerçek sayılardan gerçek sayılara tanımlı üç fonksiyonun grafiği verilmiştir. Grafikler her iki yönde aynı biçimde sürmektedir.

![Üç grafik. I: soldan sağa inen bir doğru. II: yukarı açılan, orijinden geçen ve tepe noktası x ekseninin altında olan bir parabol. III: soldan sağa sürekli yükselen, orijinden geçen bir eğri.](gorsel/tyt-matematik/11-03-soru9.svg "Her grafiği x eksenine paralel doğrularla kesmeyi dene.")

Buna göre bu fonksiyonlardan hangileri bire birdir?

A) Yalnız I
B) Yalnız II
C) I ve II
D) I ve III
E) I, II ve III

**Cevap:** D
**Çözüm:** Yatay doğru testi uygula. I hep azalıyor, III hep artıyor; ikisinde de her yatay doğru grafiği en çok bir kez keser, bire birdir. II'de örneğin $x$ ekseni parabolü iki noktada keser; iki farklı $x$ aynı değere gider, bire bir değildir.

### Soru 10 · ÖSYM tarzı
Bir restoranda 1'den 5'e kadar numaralı 5 boş masa vardır. Gelen 3 aile masalara yerleştirilecektir. Her aile bir masaya oturur ve bir masaya en fazla bir aile oturur; yani aileleri masalara eşleyen fonksiyon bire birdir. Pencere kenarındaki 1 numaralı masanın **boş kalmaması** isteniyor.

Buna göre kaç farklı yerleştirme yapılabilir?

A) 12
B) 24
C) 36
D) 48
E) 60

**Cevap:** C
**Çözüm:** Bütün bire bir yerleştirmeler: $5 \cdot 4 \cdot 3 = 60$. 1 numaralı masanın boş kaldığı yerleştirmelerde aileler kalan 4 masaya yerleşir: $4 \cdot 3 \cdot 2 = 24$. İstenen: $60 - 24 = 36$. Kontrol: 1 numaralı masaya oturacak aile 3 yolla seçilir, diğer iki aile kalan 4 masaya $4 \cdot 3 = 12$ yolla oturur: $3 \cdot 12 = 36$. Aileyi seçmeyi unutan $12$, masanın boş kaldığı durumu sayan $24$ bulur.

### Soru 11 · ÖSYM tarzı
Bir hesap makinesinde iki tuş vardır: K tuşu ekrandaki sayının karesini, E tuşu ise sayının 2 fazlasını ekrana yazar. Bir $A$ kümesindeki her sayı için iki tuş aynı sonucu veriyor; yani $A$'dan $\mathbb{R}$'ye tanımlı $f(x) = x^2$ ve $g(x) = x + 2$ fonksiyonları eşittir.

$A$ kümesi bu koşulu sağlayan en geniş küme olduğuna göre elemanlarının çarpımı kaçtır?

A) $-2$
B) $-1$
C) $1$
D) $2$
E) $3$

**Cevap:** A
**Çözüm:** $f = g$ için $A$'nın her elemanında $x^2 = x + 2$ olmalı. $x^2 - x - 2 = 0 \implies (x - 2)(x + 1) = 0$, $x = 2$ ya da $x = -1$. En geniş küme $A = \{-1, 2\}$; çarpım $-1 \cdot 2 = -2$. Kontrol: $f(-1) = 1 = g(-1)$, $f(2) = 4 = g(2)$. $1$, elemanların toplamıdır.

### Soru 12 · ÖSYM tarzı
$f\colon A \to B$ bir fonksiyon, $s(A) = 5$ ve $s(B) = 4$ olsun. Buna göre

I. $f$ bire bir olamaz.
II. $f$ örten olabilir.
III. $f$ içine olabilir.

ifadelerinden hangileri doğrudur?

A) Yalnız I
B) Yalnız II
C) I ve II
D) II ve III
E) I, II ve III

**Cevap:** E
**Çözüm:** I: 5 elemana 4 farklı görüntü yetmez; en az iki eleman aynı yere gider. Doğru. II: Örneğin iki eleman aynı görüntüye, kalan üçü diğer üç elemana gidebilir; görüntü kümesi $B$ olur. Doğru. III: Bütün elemanlar aynı elemana giderse (sabit fonksiyon) $B$'de boşta eleman kalır. Doğru. "$s(A) > s(B)$ ise içine olamaz" sanan C'yi seçer; oysa eleman sayısı yalnızca bire bir olmayı engeller.
