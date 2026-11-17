---
baslik: Kombinasyon ve Geometri · Alıştırma
ders: tyt-matematik
soru: 12
guncelleme: 2026-11-17
---
# Alıştırma: Kombinasyon ve Geometri

Sorular özgündür ve ÖSYM soru tarzında yazılmıştır. Derse bakmadan çöz.

## Isınma

### Soru 1 · Kolay
Düzlemde herhangi üçü doğrusal olmayan 7 nokta veriliyor. Bu noktaların herhangi ikisinden geçen kaç farklı doğru çizilebilir?

A) 14
B) 21
C) 35
D) 42
E) 49

**Cevap:** B
**Çözüm:** Her doğru 2 noktayla belirlenir, sıra önemsizdir: $C(7, 2) = \dfrac{7 \cdot 6}{2} = 21$. 42, 2'ye bölmeyi unutmaktır ($P(7, 2)$); 35, üçgen sayısıdır ($C(7, 3)$).

### Soru 2 · Kolay
Bir çember üzerinde birbirinden farklı 10 nokta vardır. Köşeleri bu noktalardan seçilen kaç farklı dörtgen çizilebilir?

A) 40
B) 45
C) 120
D) 210
E) 5040

**Cevap:** D
**Çözüm:** Çember üzerindeki hiçbir üç nokta doğrusal değildir; her 4'lü seçim bir dörtgen verir: $C(10, 4) = \dfrac{10 \cdot 9 \cdot 8 \cdot 7}{24} = 210$. 45 doğru sayısı ($C(10, 2)$), 120 üçgen sayısı ($C(10, 3)$), 5040 ise sırayı önemli sayan $P(10, 4)$'tür.

### Soru 3 · Kolay
Aynı düzlemde bulunan 6 farklı doğru en çok kaç noktada kesişir?

A) 15
B) 20
C) 30
D) 36
E) 720

**Cevap:** A
**Çözüm:** İki doğru en çok 1 noktada kesişir. Doğru çiftlerinin sayısı $C(6, 2) = 15$; her çift 1 nokta verir: $15$. 30, 2'ye bölmeyi unutmaktır; 20, çift yerine üçlü saymaktır ($C(6, 3)$).

## Orta

### Soru 4 · Orta
Düzlemdeki 9 noktadan 4'ü aynı doğru üzerindedir; bunun dışında hiçbir üçü doğrusal değildir. Bu noktaların en az ikisinden geçen kaç farklı doğru çizilebilir?

A) 30
B) 31
C) 33
D) 36
E) 42

**Cevap:** B
**Çözüm:** Hepsini say: $C(9, 2) = 36$. Aynı doğrudaki 4 noktanın $C(4, 2) = 6$ çifti aynı doğruyu verir; onları çıkar, o doğruyu bir kez ekle: $36 - 6 + 1 = 31$. 30, $+1$'i unutmaktır; 33, çiftler yerine üçlüleri çıkarmaktır ($36 - 4 + 1$); 36, doğrusal noktaları dikkate almamaktır.

### Soru 5 · Orta
$d_1$ ve $d_2$ paralel doğrulardır. $d_1$ üzerinde 4, $d_2$ üzerinde 5 farklı nokta işaretleniyor. Köşeleri bu 9 noktadan seçilen kaç farklı üçgen çizilebilir?

A) 30
B) 40
C) 60
D) 70
E) 84

**Cevap:** D
**Çözüm:** Üç köşe aynı doğrudan seçilemez. $d_1$'den 1, $d_2$'den 2: $4 \cdot C(5, 2) = 4 \cdot 10 = 40$. $d_1$'den 2, $d_2$'den 1: $C(4, 2) \cdot 5 = 6 \cdot 5 = 30$. Toplam $40 + 30 = 70$. Kontrol: $C(9, 3) - C(4, 3) - C(5, 3) = 84 - 4 - 10 = 70$. 30 ve 40 durumlardan yalnız birini saymaktır; 60, dörtgen sayısıdır ($C(4, 2) \cdot C(5, 2)$); 84, doğrusal üçlüleri çıkarmamaktır.

### Soru 6 · Orta
Aynı düzlemde çizilen 5 farklı doğru ile 2 farklı çember en çok kaç noktada kesişir?

A) 12
B) 20
C) 22
D) 30
E) 32

**Cevap:** E
**Çözüm:** Eşleşme türlerini ayrı say. Doğru–doğru: $C(5, 2) = 10$. Çember–çember: $2 \cdot C(2, 2) = 2$. Doğru–çember: her doğru her çemberi en çok 2 noktada keser, $5 \cdot 2 \cdot 2 = 20$. Toplam $10 + 2 + 20 = 32$. 12, doğru–çember kesişimini unutmaktır; 22, doğru–çemberi 1 noktayla saymaktır; 30, iki çemberin kesişimini unutmaktır.

### Soru 7 · Orta
Aynı düzlemde bulunan ve birbiriyle çakışmayan 3 tane beşgen en çok kaç noktada kesişir?

A) 15
B) 18
C) 30
D) 45
E) 60

**Cevap:** C
**Çözüm:** İki beşgen en çok $2 \cdot 5 = 10$ noktada kesişir. Beşgen çiftlerinin sayısı $C(3, 2) = 3$. Toplam $10 \cdot 3 = 30$. 15, kenar sayısını 2 ile çarpmayı unutmaktır ($5 \cdot 3$); 18, üçgen kuralını kullanmaktır ($6 \cdot 3$); 60, çift sayısı yerine $P(3, 2) = 6$ almaktır.

## ÖSYM tarzı

### Soru 8 · ÖSYM tarzı
Bir duvar saatinin kadranında 1'den 12'ye kadar rakamların bulunduğu 12 nokta, bir çember üzerinde yer almaktadır. Bir öğrenci köşeleri bu 12 noktadan seçilen üçgenler çiziyor.

Bu üçgenlerden kaç tanesinin bir köşesi 12 rakamının bulunduğu noktadır?

A) 55
B) 66
C) 110
D) 165
E) 220

**Cevap:** A
**Çözüm:** 12'nin noktası üçgende mutlaka bulunacak. Geriye kalan 11 noktadan 2 köşe seçilir: $C(11, 2) = \dfrac{11 \cdot 10}{2} = 55$. 66, $C(12, 2)$; 110, 2'ye bölmeyi unutmaktır; 165, 12'nin bulunmadığı üçgenlerin sayısıdır ($C(11, 3)$); 220 ise bütün üçgenlerdir ($C(12, 3)$).

### Soru 9 · ÖSYM tarzı
Bir şehir planında birbirine paralel 5 cadde ve bu caddelere dik, birbirine paralel 4 sokak vardır. Şekilde, 2. ve 4. caddeler ile 2. ve 4. sokakların sınırladığı dikdörtgen bölge taranmıştır.

![Yatay 5 cadde ve dikey 4 sokaktan oluşan ızgara. 2. ile 4. cadde ve 2. ile 4. sokak arasındaki dikdörtgen mavi taranmış.](gorsel/tyt-matematik/09-07-soru9.svg "Taralı bölge, iki cadde ve iki sokak seçilerek elde edilen dikdörtgenlerden biridir.")

Kenarları iki caddenin ve iki sokağın üzerinde olan kaç farklı dikdörtgen bölge vardır?

A) 12
B) 20
C) 60
D) 120
E) 126

**Cevap:** C
**Çözüm:** Bir dikdörtgen, üst ve alt kenarı için 2 cadde, sol ve sağ kenarı için 2 sokak seçilerek belirlenir. Sıra önemsiz: $C(5, 2) \cdot C(4, 2) = 10 \cdot 6 = 60$. 12, yalnızca en küçük kareleri saymaktır ($4 \cdot 3$); 20, kavşak sayısıdır ($5 \cdot 4$); 120, sokak seçimini sıralı saymaktır ($10 \cdot P(4, 2)$); 126 ise 9 yoldan herhangi 4'ünü seçmektir ($C(9, 4)$).

### Soru 10 · ÖSYM tarzı
Bir tasarımcı, bir çember üzerine birbirinden farklı noktalar işaretliyor ve bu noktaların her ikisini birer doğru parçasıyla birleştiriyor. Toplam 28 doğru parçası çiziliyor.

Tasarımcı daha sonra köşeleri bu noktalardan seçilen dörtgenleri boyayacaktır. Kaç farklı dörtgen boyanabilir?

A) 8
B) 28
C) 35
D) 56
E) 70

**Cevap:** E
**Çözüm:** Nokta sayısı $n$ olsun: $C(n, 2) = \dfrac{n(n - 1)}{2} = 28 \Rightarrow n(n - 1) = 56 \Rightarrow n = 8$. Dörtgen sayısı $C(8, 4) = \dfrac{8 \cdot 7 \cdot 6 \cdot 5}{24} = 70$. 8, nokta sayısında durmaktır; 56, üçgen sayısıdır ($C(8, 3)$); 35, nokta sayısını 7 bulmaktır ($C(7, 4)$).

### Soru 11 · ÖSYM tarzı
Bir bahçeye 9 fidan, aşağıdaki gibi 3 sıra ve 3 sütun hâlinde, komşu fidanlar arası 2 m olacak biçimde dikilmiştir. Bahçıvan, en az iki fidanın üzerinden geçen her doğru boyunca düz bir sulama hortumu çekecektir.

![3 sıra ve 3 sütun hâlinde dizilmiş 9 yeşil nokta. Yatay ve dikey komşu noktalar arası 2 m.](gorsel/tyt-matematik/09-07-soru11.svg "Fidanlar eşit aralıklı bir kare ızgara oluşturur. Satırlar, sütunlar ve iki köşegen üzerinde üçer fidan vardır.")

Buna göre bahçıvan kaç hortum çeker?

A) 8
B) 12
C) 20
D) 24
E) 36

**Cevap:** C
**Çözüm:** Hepsini say: $C(9, 2) = 36$. Üçer fidan bulunan 8 doğru vardır: 3 satır, 3 sütun, 2 köşegen. Her birinin $C(3, 2) = 3$ çifti aynı doğruyu verir: $36 - 8 \cdot 3 = 12$. Bu 8 doğruyu birer kez geri ekle: $12 + 8 = 20$. 12, geri eklemeyi unutmaktır; 24, köşegenleri gözden kaçırmaktır ($36 - 6 \cdot 3 + 6$); 36, doğrusal fidanları dikkate almamaktır.

### Soru 12 · ÖSYM tarzı
Bir öğrenci, kâğıda 4 farklı çember ve $n$ farklı doğru çiziyor. Bu çember ve doğruların en çok 50 noktada kesişebildiği görülüyor.

Buna göre $n$ kaçtır?

A) 3
B) 4
C) 5
D) 6
E) 7

**Cevap:** B
**Çözüm:** Çember–çember: $2 \cdot C(4, 2) = 12$. Doğru–çember: $n \cdot 4 \cdot 2 = 8n$. Doğru–doğru: $C(n, 2)$. Toplam $C(n, 2) + 8n + 12 = 50$. Seçenekleri dene: $n = 3$ için $3 + 24 + 12 = 39$; $n = 4$ için $6 + 32 + 12 = 50$; $n = 5$ için $10 + 40 + 12 = 62$. Toplam $n$ arttıkça büyüdüğü için tek çözüm $n = 4$.
