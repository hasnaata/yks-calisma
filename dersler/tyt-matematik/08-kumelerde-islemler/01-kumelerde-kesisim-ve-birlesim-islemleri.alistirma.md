---
baslik: Kümelerde Kesişim ve Birleşim İşlemleri · Alıştırma
ders: tyt-matematik
soru: 12
guncelleme: 2026-11-18
---
# Alıştırma: Kümelerde Kesişim ve Birleşim İşlemleri

Sorular özgündür ve ÖSYM soru tarzında yazılmıştır. Derse bakmadan çöz.

## Isınma

### Soru 1 · Kolay
$A = \{1, 3, 5, 7, 9\}$ ve $B = \{3, 6, 9, 12\}$ olduğuna göre $A \cap B$ kümesi aşağıdakilerden hangisidir?

A) $\{3\}$
B) $\{3, 9\}$
C) $\{1, 3, 9\}$
D) $\{3, 6, 9\}$
E) $\{1, 3, 5, 6, 7, 9, 12\}$

**Cevap:** B
**Çözüm:** Kesişim, iki kümede de bulunan elemanlardır. $A$'nın elemanlarını tek tek $B$'de ara: $1$ yok, $3$ var, $5$ yok, $7$ yok, $9$ var. $A \cap B = \{3, 9\}$. E seçeneği birleşimdir; D seçeneği $6$'yı da alır ama $6 \notin A$.

### Soru 2 · Kolay
$A = \{a, b, c, d\}$ ve $B = \{c, d, e, f, g\}$ olduğuna göre $A \cup B$ kümesinin eleman sayısı kaçtır?

A) 2
B) 5
C) 6
D) 7
E) 9

**Cevap:** D
**Çözüm:** $A \cup B = \{a, b, c, d, e, f, g\}$; ortak $c$ ve $d$ bir kez yazılır. $s(A \cup B) = 7$. Bağıntıyla: $4 + 5 - 2 = 7$. 9, ortak elemanları iki kez saymaktır; 2 ise kesişimin eleman sayısıdır.

### Soru 3 · Kolay
$s(A) = 3$, $s(B) = 5$ ve $A \subset B$ olduğuna göre aşağıdakilerden hangisi doğrudur?

A) $A \cap B = B$
B) $A \cup B = A$
C) $A \cap \emptyset = A$
D) $A \cup B = A \cap B$
E) $A \cup B = B$

**Cevap:** E
**Çözüm:** $A \subset B$ ise $A$'nın her elemanı $B$'dedir. Ortak elemanlar $A$'nın kendisi olur: $A \cap B = A$; birleşime yeni eleman eklenmez: $A \cup B = B$. A ve B seçenekleri kümelerin yerini karıştırır ($s(A) \ne s(B)$ olduğu için yanlıştır). $A \cap \emptyset = \emptyset$'dir, $A$ değil. D seçeneği $A = B$ olmasını gerektirir.

## Orta

### Soru 4 · Orta
$A$ ve $B$ kümeleri için

$$s(A) = 12, \quad s(B) = 9, \quad s(A \cup B) = 17$$

olduğuna göre $s(A \cap B)$ kaçtır?

A) 4
B) 5
C) 8
D) 13
E) 21

**Cevap:** A
**Çözüm:** $s(A \cup B) = s(A) + s(B) - s(A \cap B)$ ise $17 = 12 + 9 - s(A \cap B)$, yani $s(A \cap B) = 21 - 17 = 4$. Kontrol: yalnız $A$ $= 8$, ortak $= 4$, yalnız $B$ $= 5$; toplam $17$. 8 ve 5 "yalnız" bölgelerin sayılarıdır, 21 ise çıkarma yapılmadan bulunan toplamdır.

### Soru 5 · Orta
$A$, 24'ün pozitif bölenlerinin kümesi; $B$, 30'un pozitif bölenlerinin kümesidir.

Buna göre $A \cup B$ kümesinin eleman sayısı kaçtır?

A) 4
B) 8
C) 12
D) 16
E) 20

**Cevap:** C
**Çözüm:** $A = \{1, 2, 3, 4, 6, 8, 12, 24\}$, $s(A) = 8$. $B = \{1, 2, 3, 5, 6, 10, 15, 30\}$, $s(B) = 8$. Ortak elemanlar $\{1, 2, 3, 6\}$ (bunlar $\text{EBOB}(24, 30) = 6$'nın bölenleridir), $s(A \cap B) = 4$. $s(A \cup B) = 8 + 8 - 4 = 12$. 16, ortak elemanları iki kez saymaktır; 4 kesişimdir.

### Soru 6 · Orta
$A = \{1, 2, 3, 4\}$, $B = \{3, 4, 5\}$ ve $C = \{4, 5, 6\}$ olduğuna göre $A \cap (B \cup C)$ kümesinin elemanlarının toplamı kaçtır?

A) 4
B) 7
C) 10
D) 15
E) 18

**Cevap:** B
**Çözüm:** Önce parantez: $B \cup C = \{3, 4, 5, 6\}$. Sonra $A$ ile kesişim: $\{1, 2, 3, 4\} \cap \{3, 4, 5, 6\} = \{3, 4\}$. Toplam $3 + 4 = 7$. Dağılma özelliğiyle kontrol: $(A \cap B) \cup (A \cap C) = \{3, 4\} \cup \{4\} = \{3, 4\}$. Parantezi yok sayıp $(A \cap B) \cup C = \{3, 4, 5, 6\}$ alan 18, $A \cap B \cap C = \{4\}$ alan 4, $A \cup (B \cap C) = \{1, 2, 3, 4, 5\}$ alan 15 bulur.

### Soru 7 · Orta
$s(A) = 10$ ve $s(B) = 7$ olan $A$ ve $B$ kümeleri için $s(A \cup B)$ değerinin alabileceği en büyük değer ile en küçük değerin toplamı kaçtır?

A) 17
B) 20
C) 24
D) 27
E) 34

**Cevap:** D
**Çözüm:** $s(A \cup B) = 17 - s(A \cap B)$. Ortak eleman sayısı en az 0'dır (ayrık kümeler): o zaman $s(A \cup B) = 17$, en büyük değer. Ortak eleman en çok küçük kümenin eleman sayısı kadar olabilir, yani 7 ($B \subseteq A$): o zaman $s(A \cup B) = 10$, en küçük değer. Toplam $17 + 10 = 27$. En küçük değeri 7 sanan 24, iki değeri de 17 alan 34 bulur.

## ÖSYM tarzı

### Soru 8 · ÖSYM tarzı
30 kişilik bir sınıftaki her öğrenci satranç ve müzik kulüplerinden en az birine kayıtlıdır. Satranç kulübüne 17, müzik kulübüne 21 öğrenci kayıtlıdır.

Buna göre iki kulübe birden kayıtlı öğrenci sayısı kaçtır?

A) 4
B) 8
C) 9
D) 13
E) 17

**Cevap:** B
**Çözüm:** Satranç kümesi $S$, müzik kümesi $M$ olsun. Her öğrenci en az birine kayıtlı olduğu için $s(S \cup M) = 30$. $30 = 17 + 21 - s(S \cap M)$, buradan $s(S \cap M) = 38 - 30 = 8$. Kontrol: yalnız satranç $9$, iki kulüp $8$, yalnız müzik $13$; toplam $30$. 9 ve 13 "yalnız" bölgelerin sayılarıdır; iki kulübe birden kayıtlı olanları sormaz.

### Soru 9 · ÖSYM tarzı
Aşağıdaki Venn şemasında $A$ ve $B$ kümelerinin bölgelerindeki eleman sayıları verilmiştir.

![Kesişen iki daire. Yalnız A bölgesinde x artı 3, ortak bölgede x, yalnız B bölgesinde 2x eksi 1 yazıyor.](gorsel/tyt-matematik/08-01-soru9.svg "Her ifade o bölgedeki eleman sayısıdır.")

$s(A \cup B) = 26$ olduğuna göre $s(B)$ kaçtır?

A) 6
B) 11
C) 15
D) 17
E) 20

**Cevap:** D
**Çözüm:** $s(A \cup B)$ üç bölgenin toplamıdır: $(x + 3) + x + (2x - 1) = 4x + 2 = 26$, buradan $x = 6$. $s(B)$ = ortak + yalnız $B$ $= x + (2x - 1) = 3x - 1 = 17$. Kontrol: yalnız $A$ $= 9$, ortak $= 6$, yalnız $B$ $= 11$; $9 + 6 + 11 = 26$. 11 yalnız $B$'dir, ortak bölgeyi unutmaktır; 15 ise $s(A)$'dır.

### Soru 10 · ÖSYM tarzı
Ali'nin müzik çalma listesinde 18, Ece'ninkinde 15 şarkı vardır. İki liste birleştirilip aynı şarkılar yalnız bir kez yazılınca 25 şarkılık yeni bir liste elde ediliyor.

Buna göre Ece'nin listesinde olup Ali'nin listesinde olmayan kaç şarkı vardır?

A) 7
B) 8
C) 10
D) 15
E) 17

**Cevap:** A
**Çözüm:** Ali'nin listesi $A$, Ece'ninki $E$ olsun. Birleşik liste $A \cup E$: $25 = 18 + 15 - s(A \cap E)$, yani iki listede ortak $33 - 25 = 8$ şarkı var. Ece'nin listesinde olup Ali'ninkinde olmayanlar: $15 - 8 = 7$. 8 ortak şarkı sayısıdır; 10 Ali'de olup Ece'de olmayanlardır; 17 ise yalnız bir listede bulunan şarkıların toplamıdır ($10 + 7$).

### Soru 11 · ÖSYM tarzı
$A$, $B$ ve $C$ boş olmayan kümeler olmak üzere

$$A \cup B = A \quad \text{ve} \quad B \cap C = C$$

eşitlikleri veriliyor.

Buna göre aşağıdakilerden hangisi **kesinlikle** doğrudur?

A) $A \cap B = A$
B) $B \cup C = C$
C) $A \cup C = C$
D) $A \cap C = \emptyset$
E) $A \cap C = C$

**Cevap:** E
**Çözüm:** $A \cup B = A$ ise $B$'nin her elemanı $A$'dadır: $B \subseteq A$. $B \cap C = C$ ise $C$'nin her elemanı $B$'dedir: $C \subseteq B$. Buradan $C \subseteq B \subseteq A$, yani $C \subseteq A$ ve $A \cap C = C$ her zaman doğrudur. A, B ve C seçenekleri yalnızca ilgili kümeler eşitse doğrudur: $A \cap B = B$ olur, $A$ değil; $B \cup C = B$ ve $A \cup C = A$ olur. $C$ boş olmadığı ve $A$'nın içinde kaldığı için $A \cap C$ boş olamaz.

### Soru 12 · ÖSYM tarzı
40 kişilik bir kurs merkezinde resim kursuna 26, müzik kursuna 21 kişi kayıtlıdır. Merkezdeki bazı kişiler bu iki kursun hiçbirine kayıtlı olmayabilir.

İki kursa birden kayıtlı kişi sayısının alabileceği en küçük değer $a$, en büyük değer $b$ olduğuna göre $a + b$ toplamı kaçtır?

A) 7
B) 21
C) 28
D) 33
E) 47

**Cevap:** C
**Çözüm:** Resim $R$, müzik $M$ olsun. $s(R \cap M) = 26 + 21 - s(R \cup M) = 47 - s(R \cup M)$. Ortak sayı en küçük olsun diye birleşim en büyük olmalı; birleşim 40 kişiyi geçemez: $a = 47 - 40 = 7$. Ortak sayı en çok küçük kursun kişi sayısı kadar olabilir (müzik kursundakilerin hepsi resim kursunda da ise): $b = 21$; bu durumda $s(R \cup M) = 26 \le 40$, mümkün. $a + b = 28$. Ortak sayının en az 0 olabileceğini sanan 21, kursların toplamını alan 47 bulur.
