---
baslik: Niceleyiciler · Alıştırma
ders: tyt-matematik
soru: 12
guncelleme: 2026-11-17
---
# Alıştırma: Niceleyiciler

Sorular özgündür ve ÖSYM soru tarzında yazılmıştır. Derse bakmadan çöz.

## Isınma

### Soru 1 · Kolay
Aşağıdakilerden hangisi bir açık önermedir?

A) $7$ bir asal sayıdır.
B) $x + 5 = 9$
C) $2 + 3 = 6$
D) Her doğal sayı bir tam sayıdır.
E) $\sqrt{16} = 4$

**Cevap:** B
**Çözüm:** "$x + 5 = 9$" ifadesinin doğruluğu $x$'e bağlıdır: $x = 4$ için doğru, başka değerler için yanlış. Bu yüzden açık önermedir. A ve E doğru, C yanlış birer önermedir; içlerinde değişken yoktur. D'de "her" niceleyicisi vardır; niceleyici açık önermeyi önermeye çevirir ve bu önerme doğrudur.

### Soru 2 · Kolay
$x$ bir tam sayı olmak üzere $p(x)$: "$x^2 \le 4$" açık önermesinin doğruluk kümesi kaç elemanlıdır?

A) 2
B) 3
C) 4
D) 5
E) 6

**Cevap:** D
**Çözüm:** $x^2 \le 4$ eşitsizliğini sağlayan tam sayılar: $-2, -1, 0, 1, 2$; toplam 5. Yalnızca $x^2 = 4$ çözen 2, eşitliği unutup $x^2 < 4$ alan ya da $x$'i doğal sayı sanan 3, $0$'ı atlayan 4 bulur.

### Soru 3 · Kolay
$\exists x \in \mathbb{Z},\ x^2 < 0$ önermesinin değili aşağıdakilerden hangisidir?

A) $\forall x \in \mathbb{Z},\ x^2 \ge 0$
B) $\forall x \in \mathbb{Z},\ x^2 > 0$
C) $\exists x \in \mathbb{Z},\ x^2 \ge 0$
D) $\forall x \in \mathbb{Z},\ x^2 < 0$
E) $\exists x \in \mathbb{Z},\ x^2 > 0$

**Cevap:** A
**Çözüm:** Değil alınırken $\exists$ olur $\forall$, $<$ olur $\ge$; evrensel küme $\mathbb{Z}$ aynı kalır: $\forall x \in \mathbb{Z},\ x^2 \ge 0$. B'de eşitlik durumu kaybolmuş, C'de niceleyici çevrilmemiş, D'de koşul değillenmemiştir. Kontrol: asıl önerme yanlış, A doğru; tam olarak biri doğru.

## Orta

### Soru 4 · Orta
Aşağıdaki önermelerden hangisinin doğruluk değeri 0'dır?

A) $\forall x \in \mathbb{R},\ x^2 + 1 > 0$
B) $\exists x \in \mathbb{N},\ x^2 = x$
C) $\forall x \in \mathbb{Z},\ 2x \ne 7$
D) $\exists x \in \mathbb{Z},\ x^3 = -8$
E) $\forall x \in \mathbb{N},\ x + 1 > 1$

**Cevap:** E
**Çözüm:** E) $0 \in \mathbb{N}$ ve $x = 0$ için $1 > 1$ yanlıştır; bir karşı örnek "her" önermesini yanlış yapar. Diğerleri doğrudur: A) $x^2 \ge 0$ olduğundan $x^2 + 1 \ge 1 > 0$. B) $x = 0$ ya da $x = 1$. C) $2x = 7$ ise $x = 3{,}5$, tam sayı değil; hiçbir tam sayı için $2x = 7$ olmaz. D) $x = -2$.

### Soru 5 · Orta
$E = \{1, 2, 3, \dots, 12\}$ evrensel kümesinde

$p(x)$: "$x$, 3'ün katıdır."
$q(x)$: "$x$ çift sayıdır."

açık önermeleri veriliyor. $p(x) \wedge q'(x)$ açık önermesinin doğruluk kümesindeki elemanların toplamı kaçtır?

A) 12
B) 18
C) 24
D) 30
E) 36

**Cevap:** A
**Çözüm:** $p(x)$'in doğruluk kümesi $\{3, 6, 9, 12\}$. $q'(x)$: "$x$ çift değildir", yani tek: $\{1, 3, 5, 7, 9, 11\}$. "Ve" kesişimdir: $\{3, 9\}$, toplam $12$. $p(x) \wedge q(x)$ alan $6 + 12 = 18$, $p'(x) \wedge q(x)$ alan $2 + 4 + 8 + 10 = 24$, yalnız $p(x)$'e bakan $30$, yalnız $q'(x)$'e bakan $36$ bulur.

### Soru 6 · Orta
$\forall x \in \mathbb{R},\ (x > 1 \Rightarrow x^2 > 1)$ önermesinin değili aşağıdakilerden hangisidir?

A) $\forall x \in \mathbb{R},\ (x \le 1 \Rightarrow x^2 \le 1)$
B) $\exists x \in \mathbb{R},\ (x > 1 \wedge x^2 \le 1)$
C) $\exists x \in \mathbb{R},\ (x \le 1 \wedge x^2 > 1)$
D) $\exists x \in \mathbb{R},\ (x > 1 \Rightarrow x^2 \le 1)$
E) $\forall x \in \mathbb{R},\ (x > 1 \wedge x^2 \le 1)$

**Cevap:** B
**Çözüm:** $\forall$ olur $\exists$. İçteki "ise" önermesinin değili $(p \Rightarrow q)' \equiv p \wedge q'$ kuralıyla alınır: $x > 1 \wedge x^2 \le 1$. Sonuç B. A, koşullunun tersidir ve niceleyici çevrilmemiştir. C'de hipotez de değillenmiştir. D'de "ise" bağlacı korunmuştur; E'de niceleyici çevrilmemiştir.

### Soru 7 · Orta
$x$ bir tam sayı olmak üzere $p(x)$: "$-3 < 2x + 1 \le 9$" açık önermesinin doğruluk kümesindeki elemanların toplamı kaçtır?

A) 5
B) 7
C) 9
D) 10
E) 14

**Cevap:** C
**Çözüm:** Her taraftan 1 çıkar: $-4 < 2x \le 8$. 2'ye böl: $-2 < x \le 4$. Tam sayılar: $-1, 0, 1, 2, 3, 4$; toplam $9$. $-2$'yi dahil eden 7, $4$'ü dışarıda bırakan 5, $x$'i doğal sayı sanan 10 bulur. İkinci adımda 9'dan 1 çıkarmayı unutan ($2x \le 10$) $-1$'den $5$'e kadar toplayıp 14 bulur.

## ÖSYM tarzı

### Soru 8 · ÖSYM tarzı
Bir öğretmen dönem sonunda şunu söylüyor:

"Bu sınıftaki her öğrenci en az bir kitap okudu."

Bu önermenin değili aşağıdakilerden hangisidir?

A) Bu sınıftaki hiçbir öğrenci kitap okumadı.
B) Bu sınıftaki bazı öğrenciler en az bir kitap okudu.
C) Bu sınıftaki her öğrenci hiç kitap okumadı.
D) Bu sınıfta hiç kitap okumamış en az bir öğrenci var.
E) Bu sınıftaki her öğrenci en çok bir kitap okudu.

**Cevap:** D
**Çözüm:** "Her öğrenci $p$" önermesinin değili "en az bir öğrenci $p$ değil" önermesidir. "En az bir kitap okudu" ifadesinin değili "hiç kitap okumadı" olur. Sonuç D. A ve C aynı şeyi söyler (herkes hiç okumadı); bu, "her"in değilini "hiçbir" yazma hatasıdır. B'de koşul değillenmemiş, E'de ise niceleyici değişmemiştir.

### Soru 9 · ÖSYM tarzı
Bir raftaki altı kitabın sayfa sayıları şöyledir:

| Kitap | 1 | 2 | 3 | 4 | 5 | 6 |
|---|---|---|---|---|---|---|
| Sayfa | 120 | 245 | 310 | 96 | 188 | 402 |

Bu raf için aşağıdaki önermeler veriliyor.

I. Her kitabın sayfa sayısı 90'dan fazladır.
II. Bazı kitapların sayfa sayısı tek sayıdır.
III. Hiçbir kitabın sayfa sayısı 400'den fazla değildir.

Bu önermelerden hangileri doğrudur?

A) Yalnız I
B) Yalnız II
C) I ve II
D) I ve III
E) II ve III

**Cevap:** C
**Çözüm:** I) En az sayfalı kitap 96 sayfadır ve $96 > 90$; istisna yok, doğru. II) 245 tek sayıdır; bir örnek yeter, doğru. III) "Hiçbir kitap 400'den fazla değil", "her kitap en çok 400" demektir. 402 sayfalı kitap karşı örnektir; yanlış. Doğru olanlar I ve II.

### Soru 10 · ÖSYM tarzı
$x$ bir tam sayı ve $a$ bir tam sayı olmak üzere

$p(x)$: "$x < a$"
$q(x)$: "$x \ge -2$"

açık önermeleri veriliyor. $p(x) \wedge q(x)$ açık önermesinin doğruluk kümesi 6 elemanlı olduğuna göre $a$ kaçtır?

A) 2
B) 3
C) 4
D) 5
E) 6

**Cevap:** C
**Çözüm:** "Ve" kesişimdir: $-2 \le x < a$. Bu aralıktaki tam sayılar $-2, -1, \dots, a - 1$; sayıları $(a - 1) - (-2) + 1 = a + 2$. $a + 2 = 6$ ise $a = 4$. Kontrol: $a = 4$ için $\{-2, -1, 0, 1, 2, 3\}$, 6 eleman. $x \le a$ sanan $a + 3 = 6$ ile 3 bulur.

### Soru 11 · ÖSYM tarzı
$n$ bir pozitif tam sayı ve $A = \{1, 2, 3, \dots, n\}$ olmak üzere

"$\forall x \in A,\ 3x - 1 < 20$" önermesi **doğru**,
"$\forall x \in A,\ 3x - 1 < 17$" önermesi **yanlıştır**.

Buna göre $n$ kaçtır?

A) 5
B) 6
C) 7
D) 8
E) 9

**Cevap:** B
**Çözüm:** Birinci önerme: $A$'nın her elemanı $3x < 21$, yani $x < 7$ olmalı. $A$'nın en büyük elemanı $n$ olduğundan $n \le 6$. İkinci önerme yanlış: $3x - 1 \ge 17$, yani $x \ge 6$ olan en az bir eleman var (karşı örnek). Bu da $n \ge 6$ demektir. İkisi birlikte $n = 6$. Kontrol: $n = 6$ için $3 \cdot 6 - 1 = 17$; $17 < 20$ doğru, $17 < 17$ yanlış. $x < 7$ bulup $n = 7$ diyen, 7'nin dahil olmadığını gözden kaçırır.

### Soru 12 · ÖSYM tarzı
Aşağıdaki önermelerin hangisinin **değili** doğrudur?

A) $\forall x \in \mathbb{R},\ x^2 \ge 0$
B) $\exists x \in \mathbb{Z},\ x^2 = 9$
C) $\forall x \in \mathbb{N},\ x \ge 0$
D) $\exists x \in \mathbb{N},\ 2x = 6$
E) $\exists x \in \mathbb{R},\ x^2 + 4 = 0$

**Cevap:** E
**Çözüm:** Bir önerme ile değilinden tam olarak biri doğrudur; yani değili doğru olan önerme, kendisi **yanlış** olandır. E) $x^2 + 4 = 0$ ise $x^2 = -4$; hiçbir gerçek sayının karesi negatif olamaz, önerme yanlış. Değili $\forall x \in \mathbb{R},\ x^2 + 4 \ne 0$ doğrudur. Diğerleri doğru önermelerdir, değilleri yanlıştır: A) kare negatif olmaz; B) $x = 3$; C) en küçük doğal sayı $0$; D) $x = 3$.
