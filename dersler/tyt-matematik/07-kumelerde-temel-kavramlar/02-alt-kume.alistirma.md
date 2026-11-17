---
baslik: Alt Küme · Alıştırma
ders: tyt-matematik
soru: 12
guncelleme: 2026-11-17
---
# Alıştırma: Alt Küme

Sorular özgündür ve ÖSYM soru tarzında yazılmıştır. Derse bakmadan çöz.

## Isınma

### Soru 1 · Kolay
$A = \{1, 2, \{3\}\}$ olduğuna göre aşağıdakilerden hangisi **yanlıştır**?

A) $\emptyset \subseteq A$
B) $\{3\} \subseteq A$
C) $\{3\} \in A$
D) $\{1, 2\} \subseteq A$
E) $\{\{3\}\} \subseteq A$

**Cevap:** B
**Çözüm:** $A$'nın elemanları $1$, $2$ ve $\{3\}$. $\{3\} \subseteq A$ olması için $3 \in A$ olmalı; ama $3$ tek başına listede yok, bu yüzden B yanlıştır. A doğru: boş küme her kümenin alt kümesidir. C doğru: $\{3\}$ listede bir eleman. D doğru: $1$ ve $2$ elemandır. E doğru: tek elemanı $\{3\}$ ve $\{3\} \in A$.

### Soru 2 · Kolay
5 elemanlı bir kümenin öz alt küme sayısı kaçtır?

A) 10
B) 15
C) 16
D) 30
E) 31

**Cevap:** E
**Çözüm:** Alt küme sayısı $2^5 = 32$. Öz alt kümelerde yalnızca kümenin kendisi çıkarılır: $32 - 1 = 31$. Boş kümeyi de çıkaran 30, üssü 4 alan 15 ya da 16 bulur.

### Soru 3 · Kolay
$A = \{x \mid x \in \mathbb{N},\ x < 3\}$ olduğuna göre aşağıdakilerden hangisi $A$'nın alt kümesi **değildir**?

A) $\{1, 3\}$
B) $\{0\}$
C) $\{0, 2\}$
D) $\emptyset$
E) $\{0, 1, 2\}$

**Cevap:** A
**Çözüm:** Doğal sayılar $0$'dan başlar: $A = \{0, 1, 2\}$. A seçeneğindeki $3$, $A$'nın elemanı değil ($x < 3$); bu yüzden $\{1, 3\} \not\subseteq A$. B ve C'deki elemanlar $A$'da var. $\emptyset$ her kümenin, E ise $A$'nın kendisi olduğu için alt kümesidir. $0$'ı unutan B ya da C'yi seçer.

## Orta

### Soru 4 · Orta
$A = \{a, b, c, d, e, f\}$ kümesinin alt kümelerinden kaç tanesinde $a$ bulunur, $b$ bulunmaz?

A) 4
B) 8
C) 16
D) 32
E) 64

**Cevap:** C
**Çözüm:** $a$ kesin var, $b$ kesin yok; ikisinin de tek seçeneği kalır. Serbest elemanlar $c$, $d$, $e$, $f$: $2^4 = 16$. Yalnızca $a$ koşuluna bakan $2^5 = 32$, bütün alt kümeleri sayan $2^6 = 64$ bulur.

### Soru 5 · Orta
$A = \{k, l, m, n, p\}$ kümesinin en az 2 elemanlı kaç alt kümesi vardır?

A) 10
B) 26
C) 27
D) 31
E) 32

**Cevap:** B
**Çözüm:** Bütün alt kümeler $2^5 = 32$. İstenmeyenler: boş küme (1 tane) ve tek elemanlı alt kümeler (5 tane). Sonuç $32 - 1 - 5 = 26$. Boş kümeyi çıkarmayı unutan 27, yalnızca boş kümeyi çıkaran 31 bulur. 10, tam 2 elemanlı alt kümelerin sayısıdır.

### Soru 6 · Orta
$A = \{x \mid x \in \mathbb{Z},\ -2 < x \le 2\}$ kümesinin alt küme sayısı kaçtır?

A) 4
B) 8
C) 15
D) 16
E) 32

**Cevap:** D
**Çözüm:** $x$ tam sayı, $-2$ dahil değil, $2$ dahil: $A = \{-1, 0, 1, 2\}$, $s(A) = 4$. Alt küme sayısı $2^4 = 16$. $-2$'yi de alan $2^5 = 32$, $0$'ı unutan $2^3 = 8$, öz alt kümeyi sayan 15 bulur.

### Soru 7 · Orta
$A = \{1, \{1\}, \{1, 2\}, \emptyset\}$ kümesinin öz alt küme sayısı kaçtır?

A) 15
B) 16
C) 30
D) 31
E) 32

**Cevap:** A
**Çözüm:** En dıştaki süslü parantezin içinde dört parça var: $1$, $\{1\}$, $\{1, 2\}$ ve $\emptyset$. Hepsi farklı elemanlardır, $s(A) = 4$. Öz alt küme sayısı $2^4 - 1 = 15$. $\{1, 2\}$'yi iki eleman sayıp $s(A) = 5$ alan 31 ya da 32 bulur; 16 alt küme sayısıdır.

## ÖSYM tarzı

### Soru 8 · ÖSYM tarzı
Aşağıdaki Venn şemasında $A$ ve $B$ kümeleri gösterilmiştir.

![Büyük elips B, içinde mavi küçük elips A. A'nın içinde 1 ve 2; B'nin içinde, A'nın dışında 3, 4 ve 5 var.](gorsel/tyt-matematik/07-02-soru8.svg "A'nın elemanları 1 ve 2; B'nin elemanları 1, 2, 3, 4, 5.")

Buna göre $A \subseteq K \subseteq B$ ve $K \neq B$ koşullarını sağlayan kaç farklı $K$ kümesi vardır?

A) 3
B) 6
C) 7
D) 8
E) 31

**Cevap:** C
**Çözüm:** $A = \{1, 2\}$, $B = \{1, 2, 3, 4, 5\}$. $A \subseteq K$ olduğu için $1$ ve $2$ kesin $K$'de. $K \subseteq B$ olduğu için $K$, $B$ dışından eleman alamaz. Serbest elemanlar $3$, $4$, $5$: $2^3 = 8$ küme. Bunlardan biri $\{1, 2, 3, 4, 5\} = B$ ve $K \neq B$ isteniyor: $8 - 1 = 7$. $K \neq B$ koşulunu unutan 8, $K = A$'yı da atan 6 bulur; 31, $B$'nin bütün öz alt kümeleridir.

### Soru 9 · ÖSYM tarzı
Bir pizzacıda her pizzada domates sosu ve peynir bulunur. Müşteri bunlara ek olarak sucuk, sosis, mantar, zeytin, mısır ve biber malzemelerinden istediklerini seçebilir. Bir müşteri malzeme seçerken şu iki kurala uyuyor:

- Sucuk ile sosisten yalnız birini seçiyor.
- Mantarı mutlaka seçiyor.

Buna göre bu müşteri ek malzemeleri kaç farklı biçimde seçebilir?

A) 8
B) 16
C) 24
D) 32
E) 64

**Cevap:** B
**Çözüm:** Ek malzemeler 6 elemanlı bir küme; her seçim bu kümenin bir alt kümesidir. Mantar kesin var (1 seçenek). Sucuk ile sosisten yalnız biri: sucuk var sosis yok ya da sosis var sucuk yok (2 seçenek). Zeytin, mısır, biber serbest: $2^3 = 8$. Sonuç $2 \cdot 8 = 16$. "Yalnız biri"ni "en az biri" gibi okuyup ikisinin birlikte seçilmesini de sayan $3 \cdot 8 = 24$, sucuk ve sosisi serbest bırakan $2^5 = 32$ bulur.

### Soru 10 · ÖSYM tarzı
$K$, $L$ ve $M$ kümeleri için

$$K \subseteq L, \quad L \subseteq M, \quad M \subseteq K$$

bağıntıları doğrudur. $K = \{2, 5, a\}$ ve $M = \{b, 3, 5\}$ olduğuna göre $a \cdot b$ çarpımı kaçtır?

A) 2
B) 3
C) 4
D) 5
E) 6

**Cevap:** E
**Çözüm:** $K \subseteq L$ ve $L \subseteq M$ ise geçişmeden $K \subseteq M$. $M \subseteq K$ de verildiği için $K = M$: $\{2, 5, a\} = \{b, 3, 5\}$. $M$'de $3$ var, $K$'de de olmalı; $2 \neq 3$ ve $5 \neq 3$ olduğu için $a = 3$. $K$'de $2$ var, $M$'de de olmalı; $3 \neq 2$ ve $5 \neq 2$ olduğu için $b = 2$. Kontrol: $K = M = \{2, 3, 5\}$. Çarpım $3 \cdot 2 = 6$.

### Soru 11 · ÖSYM tarzı
Bir öğretmen 3 kız ve 3 erkek öğrenciden oluşan 6 kişilik bir gruptan bir proje ekibi oluşturacaktır. Ekipte en az bir kız öğrenci bulunması şartıyla ekip istenen sayıda öğrenciden oluşabilir.

Buna göre öğretmen kaç farklı ekip oluşturabilir?

A) 7
B) 8
C) 49
D) 56
E) 63

**Cevap:** D
**Çözüm:** Her ekip, 6 kişilik grubun bir alt kümesidir: toplam $2^6 = 64$. Hiç kız bulunmayan alt kümeler yalnızca erkeklerden seçilir: $2^3 = 8$ (boş küme dahil). En az bir kız bulunanlar $64 - 8 = 56$. Bu ekiplerin hepsinde en az bir kişi olduğu için boş küme zaten sayılmaz. 63 bütün boş olmayan ekiplerdir; 49 ($7 \cdot 7$) hem kız hem erkek bulunan ekiplerdir, yalnızca kızlardan oluşan 7 ekibi dışarıda bırakır.

### Soru 12 · ÖSYM tarzı
$A$ ve $B$ kümeleri için $A \subseteq B$ ve $s(B) = s(A) + 2$'dir.

$B$ kümesinin alt kümelerinden 48 tanesi $A$ kümesinin alt kümesi **değildir**.

Buna göre $B$ kümesi kaç elemanlıdır?

A) 4
B) 5
C) 6
D) 7
E) 8

**Cevap:** C
**Çözüm:** $s(A) = n$ olsun, $s(B) = n + 2$. $A \subseteq B$ olduğu için $A$'nın bütün alt kümeleri $B$'nin de alt kümesidir. $B$'nin $A$'nın alt kümesi olmayan alt kümeleri: $2^{n+2} - 2^n = 4 \cdot 2^n - 2^n = 3 \cdot 2^n$. $3 \cdot 2^n = 48$, $2^n = 16$, $n = 4$. $s(B) = 4 + 2 = 6$. Kontrol: $2^6 - 2^4 = 64 - 16 = 48$. 4, $A$'nın eleman sayısıdır.
