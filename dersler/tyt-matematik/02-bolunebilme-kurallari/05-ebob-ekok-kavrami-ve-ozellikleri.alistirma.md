---
baslik: EBOB-EKOK Kavramı ve Özellikleri · Alıştırma
ders: tyt-matematik
soru: 12
guncelleme: 2026-11-17
---
# Alıştırma: EBOB-EKOK Kavramı ve Özellikleri

Sorular özgündür ve ÖSYM soru tarzında yazılmıştır. Derse bakmadan çöz.

## Isınma

### Soru 1 · Kolay
$\text{EBOB}(60, 84)$ kaçtır?

A) 4
B) 6
C) 12
D) 24
E) 420

**Cevap:** C
**Çözüm:** $60 = 2^2 \cdot 3 \cdot 5$, $84 = 2^2 \cdot 3 \cdot 7$. Ortak tabanlar 2 ve 3, küçük üsler $2^2$ ve $3$: $\text{EBOB} = 4 \cdot 3 = 12$. 420 bu sayıların EKOK'udur; 4 ve 6 ortak bölendir ama en büyüğü değildir.

### Soru 2 · Kolay
$A = 2^3 \cdot 3^2 \cdot 5$ ve $B = 2^2 \cdot 3^4 \cdot 7$ olduğuna göre $\text{EKOK}(A, B)$ aşağıdakilerden hangisidir?

A) $2^2 \cdot 3^2$
B) $2^3 \cdot 3^4$
C) $2^2 \cdot 3^2 \cdot 5 \cdot 7$
D) $2^3 \cdot 3^2 \cdot 5 \cdot 7$
E) $2^3 \cdot 3^4 \cdot 5 \cdot 7$

**Cevap:** E
**Çözüm:** EKOK için bütün tabanlar (2, 3, 5, 7) alınır ve her birinin büyük üssü seçilir: $2^3 \cdot 3^4 \cdot 5 \cdot 7$. A seçeneği EBOB'dur. B yalnızca ortak tabanları almak, C küçük üsleri seçmek, D ise 3'ün üssünü yanlış seçmektir.

### Soru 3 · Kolay
$\dfrac{84}{126}$ kesrinin en sade hâli $\dfrac{a}{b}$ olduğuna göre $a + b$ kaçtır?

A) 5
B) 10
C) 15
D) 30
E) 35

**Cevap:** A
**Çözüm:** $84 = 2^2 \cdot 3 \cdot 7$, $126 = 2 \cdot 3^2 \cdot 7$, $\text{EBOB} = 2 \cdot 3 \cdot 7 = 42$. $\dfrac{84 : 42}{126 : 42} = \dfrac{2}{3}$, $a + b = 5$. EBOB yerine yalnızca 6'ya bölen $\dfrac{14}{21}$ ile 35, 7'ye bölen $\dfrac{12}{18}$ ile 30, 14'e bölen $\dfrac{6}{9}$ ile 15 bulur; bu kesirler henüz sade değildir.

## Orta

### Soru 4 · Orta
İki pozitif tam sayının EBOB'u 8, EKOK'u 240'tır. Sayılardan biri 48 olduğuna göre diğeri kaçtır?

A) 5
B) 20
C) 30
D) 40
E) 60

**Cevap:** D
**Çözüm:** İki sayı için $a \cdot b = \text{EBOB} \cdot \text{EKOK}$: $48 \cdot b = 8 \cdot 240 = 1920$, $b = 40$. Kontrol: $48 = 2^4 \cdot 3$, $40 = 2^3 \cdot 5$; EBOB $2^3 = 8$, EKOK $2^4 \cdot 3 \cdot 5 = 240$. EBOB'u unutup $240 : 48$ yapan 5, $240 : 8$ yapan 30 bulur.

### Soru 5 · Orta
180 ve 240 sayılarının kaç tane ortak pozitif böleni vardır?

A) 6
B) 10
C) 12
D) 18
E) 20

**Cevap:** C
**Çözüm:** Ortak bölenler EBOB'un bölenleridir. $180 = 2^2 \cdot 3^2 \cdot 5$, $240 = 2^4 \cdot 3 \cdot 5$, $\text{EBOB} = 2^2 \cdot 3 \cdot 5 = 60$. $60$'ın pozitif bölen sayısı $(2 + 1)(1 + 1)(1 + 1) = 12$. 18, 180'in; 20, 240'ın bölen sayısıdır.

### Soru 6 · Orta
12, 20 ve 45 sayılarının üçüne de tam bölünen üç basamaklı kaç doğal sayı vardır?

A) 1
B) 2
C) 3
D) 4
E) 5

**Cevap:** E
**Çözüm:** Üç sayının ortak katları EKOK'un katlarıdır. $12 = 2^2 \cdot 3$, $20 = 2^2 \cdot 5$, $45 = 3^2 \cdot 5$; $\text{EKOK} = 2^2 \cdot 3^2 \cdot 5 = 180$. Üç basamaklı katları: $180, 360, 540, 720, 900$; toplam 5. EKOK'u yanlışlıkla $2^3 \cdot 3^2 \cdot 5 = 360$ alan 2 bulur.

### Soru 7 · Orta
$a < b$ olmak üzere $a$ ve $b$ pozitif tam sayıları için

$$\text{EBOB}(a, b) = 6 \quad \text{ve} \quad \text{EKOK}(a, b) = 90$$

dır. $a \ne 6$ olduğuna göre $a + b$ kaçtır?

A) 36
B) 48
C) 60
D) 90
E) 96

**Cevap:** B
**Çözüm:** $a = 6m$, $b = 6n$ ($m < n$, aralarında asal) ve $\text{EKOK} = 6mn = 90$, yani $mn = 15$. Olasılıklar $(m, n) = (1, 15)$ ve $(3, 5)$. $a \ne 6$ olduğundan $m = 3$, $n = 5$: $a = 18$, $b = 30$, $a + b = 48$. Kontrol: $\text{EBOB}(18, 30) = 6$, $\text{EKOK}(18, 30) = 90$. Koşulu gözden kaçıran $6 + 90 = 96$ bulur.

## ÖSYM tarzı

### Soru 8 · ÖSYM tarzı
Pozitif tam sayılar için $\triangle$ işlemi

$$a \triangle b = \frac{\text{EKOK}(a, b)}{\text{EBOB}(a, b)}$$

biçiminde tanımlanıyor.

Buna göre $(12 \triangle 18) \triangle 10$ işleminin sonucu kaçtır?

A) 3
B) 6
C) 10
D) 15
E) 30

**Cevap:** D
**Çözüm:** Önce parantez: $\text{EKOK}(12, 18) = 36$, $\text{EBOB}(12, 18) = 6$, $12 \triangle 18 = 6$. Sonra $6 \triangle 10$: $\text{EKOK}(6, 10) = 30$, $\text{EBOB}(6, 10) = 2$, sonuç $15$. 6 ilk adımda durmak, 30 ikinci adımda EBOB'a bölmeyi unutmaktır.

### Soru 9 · ÖSYM tarzı
Aşağıdaki Venn şemasında $A$ ve $B$ pozitif tam sayılarının asal çarpanları gösterilmiştir. Her asal çarpan, kaç kez çarpılıyorsa o kadar yazılmıştır; kesişimdekiler iki sayıda da vardır.

![İki kesişen çember: A ve B. Yalnız A bölgesinde 3 ve 7, kesişimde 2, 2 ve 5, yalnız B bölgesinde 2 ve 11.](gorsel/tyt-matematik/02-05-soru9.svg "Kesişimdeki çarpanlar iki sayıda da var. Her bölgedeki çarpanları tek tek oku.")

Buna göre $\dfrac{\text{EKOK}(A, B)}{\text{EBOB}(A, B)}$ oranı kaçtır?

A) 42
B) 231
C) 462
D) 924
E) 9 240

**Cevap:** C
**Çözüm:** EBOB kesişimdekilerin çarpımı: $2 \cdot 2 \cdot 5 = 20$. EKOK şekildeki bütün çarpanların çarpımı: $3 \cdot 7 \cdot 2 \cdot 2 \cdot 5 \cdot 2 \cdot 11 = 9\,240$. Oran $9\,240 : 20 = 462$; bu, kesişim dışındaki çarpanların çarpımıdır: $3 \cdot 7 \cdot 2 \cdot 11 = 462$. ($A = 420$, $B = 440$.) Yalnız B'deki 2'yi atlayan 231 bulur; 9 240 EKOK'un kendisidir.

### Soru 10 · ÖSYM tarzı
Bir öğretmen 48 kalem ve 72 silgiyi bir gruptaki öğrencilere dağıtacaktır. Her öğrenci eşit sayıda kalem ve eşit sayıda silgi alacak, hiç kalem ya da silgi artmayacaktır.

Gruptaki öğrenci sayısı en az 2 olduğuna göre bu sayı kaç farklı değer alabilir?

A) 6
B) 7
C) 8
D) 12
E) 24

**Cevap:** B
**Çözüm:** Öğrenci sayısı hem 48'i hem 72'yi bölmeli; yani ortak bölendir ve ortak bölenler EBOB'un bölenleridir. $48 = 2^4 \cdot 3$, $72 = 2^3 \cdot 3^2$, $\text{EBOB} = 2^3 \cdot 3 = 24$. 24'ün bölenleri $1, 2, 3, 4, 6, 8, 12, 24$; 8 tane. "En az 2" koşulu 1'i dışarıda bırakır: 7 değer. 1'i sayan 8 bulur; 24 öğrenci sayısının en büyük değeridir, kaç değer alabileceği değil.

### Soru 11 · ÖSYM tarzı
$a$ ve $b$ ardışık iki pozitif tam sayıdır.

$$\text{EKOK}(a, b) = 156$$

olduğuna göre $a + b$ kaçtır?

A) 25
B) 32
C) 43
D) 55
E) 80

**Cevap:** A
**Çözüm:** Ardışık iki sayının 1'den başka ortak böleni yoktur; aralarında asaldırlar. Bu yüzden $\text{EKOK} = a \cdot b = 156$. $156 = 2^2 \cdot 3 \cdot 13 = 12 \cdot 13$ ve 12 ile 13 ardışıktır. $a + b = 25$. Diğer seçenekler $156 = 6 \cdot 26 = 4 \cdot 39 = 3 \cdot 52 = 2 \cdot 78$ ayrışımlarından gelir; bu çiftler ardışık değildir.

### Soru 12 · ÖSYM tarzı
$x$ pozitif bir tam sayı ve $x < 100$ olmak üzere

$$\text{EBOB}(x, 36) = 12$$

eşitliğini sağlayan kaç farklı $x$ değeri vardır?

A) 3
B) 4
C) 5
D) 6
E) 8

**Cevap:** D
**Çözüm:** EBOB 12 olduğuna göre $x = 12k$. $36 = 12 \cdot 3$ olduğundan $k$ ile $3$ aralarında asal olmalı; $k$ 3'ün katı olursa EBOB $36$ olur. $12k < 100$ için $k \in \{1, 2, \dots, 8\}$; bunlardan 3'ün katı olan $3$ ve $6$ çıkar. Kalan $k = 1, 2, 4, 5, 7, 8$: $x \in \{12, 24, 48, 60, 84, 96\}$, 6 değer. 100'den küçük bütün 12'nin katlarını sayan 8 bulur ($36$ ve $72$ için EBOB 36'dır).
