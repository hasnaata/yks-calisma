---
baslik: Kümelerde Fark ve Tümleme İşlemleri · Alıştırma
ders: tyt-matematik
soru: 12
guncelleme: 2026-11-17
---
# Alıştırma: Kümelerde Fark ve Tümleme İşlemleri

Sorular özgündür ve ÖSYM soru tarzında yazılmıştır. Derse bakmadan çöz.

## Isınma

### Soru 1 · Kolay
$A = \{1, 2, 3, 4, 5, 6\}$ ve $B = \{4, 5, 6, 7, 8\}$ olduğuna göre $B \setminus A$ kümesi aşağıdakilerden hangisidir?

A) $\{4, 5, 6\}$
B) $\{7, 8\}$
C) $\{1, 2, 3\}$
D) $\{1, 2, 3, 7, 8\}$
E) $\{1, 2, 3, 4, 5, 6, 7, 8\}$

**Cevap:** B
**Çözüm:** $B \setminus A$, $B$'de olup $A$'da olmayan elemanlardır. $B$'nin elemanlarını gez: $4, 5, 6$ $A$'da var, atılır; $7$ ve $8$ kalır. $B \setminus A = \{7, 8\}$. C seçeneği sırayı karıştırıp $A \setminus B$ yazmaktır; A seçeneği kesişim, E seçeneği birleşimdir.

### Soru 2 · Kolay
$E = \{x \mid x \text{ pozitif tam sayı ve } x \le 12\}$ evrensel kümesinde $A$, 3'ün katlarının kümesidir.

Buna göre $A'$ kümesinin eleman sayısı kaçtır?

A) 3
B) 4
C) 6
D) 8
E) 9

**Cevap:** D
**Çözüm:** $s(E) = 12$. $A = \{3, 6, 9, 12\}$, $s(A) = 4$. $s(A') = s(E) - s(A) = 12 - 4 = 8$. 4, $A$'nın kendi eleman sayısıdır. 12'yi 3'ün katı saymayan $A = \{3, 6, 9\}$ alır ve 9 bulur.

### Soru 3 · Kolay
$E$ evrensel kümesinin boş olmayan $A$ ve $B$ alt kümeleri için $A \ne B$ ve $A \ne E$ olduğu biliniyor.

Buna göre aşağıdakilerden hangisi **her zaman doğrudur**?

A) $A \setminus A = \emptyset$
B) $A \setminus \emptyset = \emptyset$
C) $A \setminus B = B \setminus A$
D) $(A')' = A'$
E) $A \cup A' = A$

**Cevap:** A
**Çözüm:** Bir kümeden kendi elemanlarının hepsi atılırsa geriye eleman kalmaz: $A \setminus A = \emptyset$. B yanlış: boş kümeden fark alınca hiçbir şey atılmaz, $A \setminus \emptyset = A$. C yanlış: $A \ne B$ iken fark değişmeli değildir. D yanlış: iki kez tümleyen $A$'yı verir. E yanlış: $A \cup A' = E$'dir ve $A \ne E$.

## Orta

### Soru 4 · Orta
$A$ ve $B$ kümeleri için

$$s(A) = 14, \quad s(B) = 9, \quad s(A \cup B) = 19$$

olduğuna göre $s(A \setminus B)$ kaçtır?

A) 4
B) 5
C) 10
D) 14
E) 15

**Cevap:** C
**Çözüm:** Önce ortak bölge: $19 = 14 + 9 - s(A \cap B)$, buradan $s(A \cap B) = 23 - 19 = 4$. Sonra $s(A \setminus B) = s(A) - s(A \cap B) = 14 - 4 = 10$. Kontrol: $10 + 4 + 5 = 19$. 5, $s(B \setminus A)$'dır; 4 kesişimdir; 15 ise yalnız birinde olanların sayısıdır ($10 + 5$).

### Soru 5 · Orta
$s(E) = 30$ olan $E$ evrensel kümesinin $A$ ve $B$ alt kümeleri için

$$s(A) = 12, \quad s(B) = 10, \quad s(A \cap B) = 5$$

olduğuna göre $s(A' \cap B')$ kaçtır?

A) 5
B) 7
C) 8
D) 12
E) 13

**Cevap:** E
**Çözüm:** De Morgan: $A' \cap B' = (A \cup B)'$. $s(A \cup B) = 12 + 10 - 5 = 17$, buradan $s\big((A \cup B)'\big) = 30 - 17 = 13$. Ortak bölgeyi çıkarmadan $30 - 22$ yapan 8 bulur. 7, $s(A \setminus B)$; 12 ise yalnız birinde olanların sayısıdır ($7 + 5$).

### Soru 6 · Orta
$A$ ve $B$ kümeleri için

$$A \cup B = \{1, 2, 3, 4, 5, 6, 7, 8, 9\}, \quad A \setminus B = \{1, 2, 3\}, \quad B \setminus A = \{7, 8, 9\}$$

olduğuna göre $A \cap B$ kümesinin elemanlarının toplamı kaçtır?

A) 6
B) 15
C) 21
D) 24
E) 45

**Cevap:** B
**Çözüm:** $A \cup B$ üç ayrık parçadan oluşur: $A \setminus B$, $A \cap B$, $B \setminus A$. İlk ve son parçayı birleşimden atınca ortak bölge kalır: $A \cap B = \{4, 5, 6\}$, toplam $4 + 5 + 6 = 15$. 6, $A \setminus B$'nin; 24, $B \setminus A$'nın; 21, $A = \{1, \ldots, 6\}$'nın; 45 ise birleşimin toplamıdır.

### Soru 7 · Orta
$A$ ve $B$, $E$ evrensel kümesinin herhangi iki alt kümesidir.

Buna göre $A' \setminus B'$ kümesi aşağıdakilerden hangisine eşittir?

A) $A \setminus B$
B) $A \cap B$
C) $(A \cup B)'$
D) $B \setminus A$
E) $A' \cup B$

**Cevap:** D
**Çözüm:** Farkı kesişimle yaz: $X \setminus Y = X \cap Y'$. Burada $A' \setminus B' = A' \cap (B')' = A' \cap B$. Bu, $B$'de olup $A$'da olmayan elemanlardır: $B \setminus A$. A seçeneği, tümleyen işaretlerini atıp sırayı aynen bırakmaktır; tipik hata budur. C seçeneği $A' \cap B'$ kümesidir.

## ÖSYM tarzı

### Soru 8 · ÖSYM tarzı
36 öğrencinin bulunduğu bir sınıfta 15 öğrenci voleybol, 12 öğrenci basketbol takımındadır. 5 öğrenci iki takımda birden oynamaktadır.

Buna göre bu sınıfta iki takımın hiçbirinde oynamayan kaç öğrenci vardır?

A) 9
B) 14
C) 17
D) 19
E) 22

**Cevap:** B
**Çözüm:** En az bir takımda oynayan: $s(V \cup B) = 15 + 12 - 5 = 22$. Hiçbirinde oynamayan: $36 - 22 = 14$. Bölgelerle kontrol: yalnız voleybol $10$, iki takım $5$, yalnız basketbol $7$, hiçbiri $14$; toplam $36$. 9, ortak 5 öğrenciyi iki kez çıkarmaktır ($36 - 27$); 17, yalnız bir takımda oynayanlardır; 22 ise en az bir takımda oynayanlardır.

### Soru 9 · ÖSYM tarzı
Aşağıdaki Venn şemasında $A$ ve $B$, $E$ evrensel kümesinin alt kümeleridir.

![Dikdörtgen E içinde kesişen A ve B daireleri. İki dairenin ortak bölgesi ve dairelerin dışında kalan bölge taralı; yalnız A ve yalnız B bölgeleri boş.](gorsel/tyt-matematik/08-02-soru9.svg "Taralı bölgeler: iki dairenin ortak kısmı ve dairelerin dışı.")

Buna göre taralı bölge aşağıdakilerden hangisiyle gösterilir?

A) $(A \cup B)'$
B) $A' \cap B'$
C) $(A \setminus B) \cup (B \setminus A)$
D) $A \cap B$
E) $\big[(A \setminus B) \cup (B \setminus A)\big]'$

**Cevap:** E
**Çözüm:** Taralı olmayan bölgeler yalnız $A$ ve yalnız $B$ bölgeleridir, yani $(A \setminus B) \cup (B \setminus A)$. Taralı bölge bunun dışında kalan her şeydir: tümleyeni. A ve B seçenekleri aynı kümedir (De Morgan) ve yalnız dairelerin dışını verir, ortak bölgeyi kaçırır. D yalnız ortak bölgedir. C ise tam tersine taralı olmayan kısımdır.

### Soru 10 · ÖSYM tarzı
$X$ ve $Y$ kümeleri için $\oplus$ işlemi

$$X \oplus Y = (X \setminus Y) \cup (Y \setminus X)$$

biçiminde tanımlanıyor. $A = \{1, 2, 3, 4, 5\}$ ve $B = \{4, 5, 6, 7\}$ veriliyor.

Buna göre $(A \oplus B) \oplus B$ kümesinin elemanlarının toplamı kaçtır?

A) 6
B) 13
C) 15
D) 19
E) 22

**Cevap:** C
**Çözüm:** Önce parantez: $A \setminus B = \{1, 2, 3\}$, $B \setminus A = \{6, 7\}$, buradan $A \oplus B = \{1, 2, 3, 6, 7\}$. Şimdi $X = \{1, 2, 3, 6, 7\}$ ile $B = \{4, 5, 6, 7\}$: $X \setminus B = \{1, 2, 3\}$, $B \setminus X = \{4, 5\}$. Sonuç $\{1, 2, 3, 4, 5\}$, toplam $15$. 19, işlemi bir kez yapıp durmaktır ($1 + 2 + 3 + 6 + 7$); 6, yalnız $X \setminus B$'yi almak; 13 ise yalnız $B \setminus A = \{6, 7\}$'nin toplamıdır.

### Soru 11 · ÖSYM tarzı
Bir oteldeki 60 misafirle yapılan ankette her misafire otelin havuzunu ve spor salonunu kullanıp kullanmadığı soruluyor. Sonuçlara göre

- 25 misafir havuzu **kullanmamış**,
- 30 misafir spor salonunu **kullanmamış**,
- 10 misafir ikisini de **kullanmamıştır**.

Buna göre hem havuzu hem spor salonunu kullanan misafir sayısı kaçtır?

A) 5
B) 10
C) 15
D) 20
E) 25

**Cevap:** C
**Çözüm:** Havuzu kullananlar $H$, spor salonunu kullananlar $S$ olsun. Tümleyenden geri dön: $s(H) = 60 - 25 = 35$, $s(S) = 60 - 30 = 30$. İkisini de kullanmayanlar $(H \cup S)'$ olduğundan $s(H \cup S) = 60 - 10 = 50$. Buradan $s(H \cap S) = 35 + 30 - 50 = 15$. Kontrol: yalnız havuz $20$, ikisi $15$, yalnız salon $15$, hiçbiri $10$; toplam $60$. 10'u kullanmayıp $60 - 25 - 30$ yapan 5 bulur; 20 yalnız havuz kullananlardır.

### Soru 12 · ÖSYM tarzı
$s(E) = 20$ olan $E$ evrensel kümesinin $A$ ve $B$ alt kümeleri için $A \subset B$ olduğu biliniyor.

$$s(A') = 15, \quad s(B') = 8$$

olduğuna göre $s(B \setminus A)$ kaçtır?

A) 7
B) 12
C) 15
D) 17
E) 23

**Cevap:** A
**Çözüm:** $s(A) = 20 - 15 = 5$, $s(B) = 20 - 8 = 12$. $A \subset B$ olduğu için $A \cap B = A$, buradan $s(B \setminus A) = s(B) - s(A) = 12 - 5 = 7$. Kısa yol: $B \setminus A$, $A$'nın dışında kalıp $B$'nin dışında kalmayanlardır: $s(A') - s(B') = 15 - 8 = 7$. 12, $s(B)$'dir; 17, $s(A) + s(B)$; 23 ise $s(A') + s(B')$'dir.
