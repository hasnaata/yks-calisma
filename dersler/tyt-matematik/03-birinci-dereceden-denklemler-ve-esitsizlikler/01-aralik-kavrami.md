---
baslik: Aralık Kavramı
ders: tyt-matematik
sure: 20 dk
kaynak: MEBİ Konu Özeti 5d54cb82db
guncelleme: 2026-11-17
---
# Aralık Kavramı

**Bu dersin sonunda:** bir eşitsizliği aralıkla yazıp sayı doğrusunda gösterebilecek, bir aralıktaki tam sayıları sayabilecek ve iki aralığın kesişimini, birleşimini, farkını ve tümleyenini bulabileceksin.

> **TYT'de yeri:** Aralık tek başına nadiren soru olur; ama eşitsizlik, mutlak değer ve fonksiyon sorularının cevabı hep bir aralıktır. "Bu aralıkta kaç tam sayı var?", "iki koşulu birlikte sağlayan değerler" ve "uç nokta dahil mi?" kalıpları sık gelir.

## Önce hatırla

<details><summary>Periyodik problemlerden: Bugün salı. 100 gün sonra hangi gün olur?</summary>
Günler 7'de bir tekrar eder, bu yüzden yalnızca kalana bakılır: $100 = 7 \cdot 14 + 2$. Salıdan 2 gün sonra: <b>perşembe</b>.
</details>

<details><summary>Periyodik problemlerden: Biri 6 günde bir, diğeri 9 günde bir nöbet tutan iki kişi ilk kez pazartesi birlikte nöbet tutuyor. Üçüncü kez birlikte hangi gün nöbet tutarlar?</summary>
Birlikte nöbet $\text{EKOK}(6, 9) = 18$ günde bir gelir. İlk nöbet sayıldığı için 2 tur daha var: $2 \cdot 18 = 36$ gün. $36 = 7 \cdot 5 + 1$, pazartesiden 1 gün sonra: <b>salı</b>.
</details>

## Aralık nedir?

**Örnek.** Bir ilaç en az 2 °C, en çok 8 °C'de saklanmalı. Uygun sıcaklık $x$ ise $2 \le x \le 8$ olur. Burada $x$ yalnızca 2, 3, 4… değil; $2{,}5$ ya da $7{,}91$ gibi aradaki **bütün gerçek sayılar** olabilir. Bu kümeyi kısaca $[2, 8]$ diye yazarız.

Sayı doğrusunda iki farklı nokta arasındaki bütün gerçek sayılardan oluşan kümeye **aralık** denir. Aralığı uç noktalarının **dahil olup olmamasına** göre yazarız:

- Köşeli parantez `[ ]`: uç nokta **dahil**. Sayı doğrusunda **dolu** nokta.
- Normal parantez `( )`: uç nokta **dahil değil**. Sayı doğrusunda **içi boş** nokta.

![Dört sayı doğrusu alt alta: hepsinde −2 ile 3 arası boyalı. Birincide iki uç da dolu, ikincide ikisi de boş, üçüncüde −2 dolu 3 boş, dördüncüde −2 boş 3 dolu.](gorsel/tyt-matematik/03-01-aralik-turleri.svg "Uç noktalar aynı, aralıklar farklı. Dolu nokta dahil, boş nokta dahil değil demektir.")

| Eşitsizlik | Aralık | Adı |
|---|---|---|
| $a \le x \le b$ | $[a, b]$ | Kapalı aralık |
| $a < x < b$ | $(a, b)$ | Açık aralık |
| $a \le x < b$ | $[a, b)$ | Yarı açık aralık |
| $a < x \le b$ | $(a, b]$ | Yarı açık aralık |

Bu gösterimlerde hep $a < b$ ve küçük sayı solda yazılır. Yarı açık aralığa **yarı kapalı** da denir.

## Aralıktaki tam sayıları saymak

**Örnek.** $[-3, 4)$ aralığında kaç tam sayı var?

$-3$ dahil, $4$ dahil değil. Tam sayılar: $-3, -2, -1, 0, 1, 2, 3$. Toplam **7** tane.

Aynı uçlarla karşılaştır:

| Aralık | Tam sayılar | Sayı |
|---|---|---|
| $[-3, 4]$ | $-3, \dots, 4$ | $4 - (-3) + 1 = 8$ |
| $[-3, 4)$ ya da $(-3, 4]$ | bir uç eksik | $4 - (-3) = 7$ |
| $(-3, 4)$ | iki uç eksik | $4 - (-3) - 1 = 6$ |

**Kural.** $a$ ve $b$ tam sayıysa: kapalı aralıkta $b - a + 1$, yarı açıkta $b - a$, açıkta $b - a - 1$ tam sayı vardır.

Toplam sorulursa kısa yol: $[-3, 4)$ içindeki tam sayılarda $-3$ ile $3$, $-2$ ile $2$, $-1$ ile $1$ birbirini götürür. Toplam $0$ olur.

**Uçlar tam sayı değilse.** $\left[-\frac{7}{3}, \frac{9}{2}\right)$ aralığında $-\frac{7}{3} \approx -2{,}33$ ve $\frac{9}{2} = 4{,}5$. İçteki tam sayılar $-2, -1, 0, 1, 2, 3, 4$; toplam **7**. Uç tam sayı değilse parantezin köşeli ya da normal olması sonucu değiştirmez.

## Sınırsız aralıklar

**Örnek.** "$x$, $1$'den büyük bir gerçek sayı" ifadesi $x > 1$ demektir. Sağ tarafta sınır yoktur; bunu $\infty$ (sonsuz) ile yazarız: $(1, \infty)$.

![Dört sayı doğrusu: 1'de boş nokta ve sağa ok; 1'de dolu nokta ve sağa ok; 1'de dolu nokta ve sola ok; iki yöne de uzanan tam boyalı doğru.](gorsel/tyt-matematik/03-01-sinirsiz-araliklar.svg "Sonsuz tarafta nokta yok, ok var. Sonsuz bir sayı olmadığı için o taraf hep normal parantezle yazılır.")

| Eşitsizlik | Aralık |
|---|---|
| $x > a$ | $(a, \infty)$ |
| $x \ge a$ | $[a, \infty)$ |
| $x < a$ | $(-\infty, a)$ |
| $x \le a$ | $(-\infty, a]$ |
| Bütün gerçek sayılar | $\mathbb{R} = (-\infty, \infty)$ |

**Kural.** $\infty$ ve $-\infty$ birer sayı değildir, aralığa dahil edilemez. Bu yüzden onların yanında **her zaman normal parantez** kullanılır: $[1, \infty]$ yazımı yanlıştır.

Bir ucu kapalı, öbür ucu sonsuz olan aralığa (örneğin $[1, \infty)$) **ışın** da denir.

Dikkat: $(1, \infty)$ aralığının **en küçük elemanı yoktur** ($1{,}1$; $1{,}01$; $1{,}001$… hep daha küçüğü var). Ama bu aralıktaki **en küçük tam sayı** $2$'dir. Soruda "gerçek sayı" mı "tam sayı" mı dendiğine bak.

## Kesişim, birleşim ve fark

**Örnek.** $A = [-3, 4)$ ve $B = (1, 6]$ olsun. İki aralığı **aynı ölçekte alt alta** çiz, sonra her işlemi doğrudan oku.

![Alt alta beş sayı doğrusu: A eksi 3'ten 4'e, B 1'den 6'ya; altında A kesişim B 1'den 4'e açık, A birleşim B eksi 3'ten 6'ya kapalı, A fark B eksi 3'ten 1'e kapalı.](gorsel/tyt-matematik/03-01-kesisim-birlesim-fark.svg "Her uç noktada kendine sor: bu sayı A'da mı, B'de mi? A fark B kümesinde 1'in dolu olduğuna dikkat et: 1, B'de değil.")

- $A \cap B$ (ikisinde de olanlar): $1$ ile $4$ arası. $1 \notin B$, $4 \notin A$; iki uç da boş. $A \cap B = (1, 4)$.
- $A \cup B$ (en az birinde olanlar): $-3$'ten $6$'ya kesintisiz. $-3 \in A$, $6 \in B$. $A \cup B = [-3, 6]$.
- $A \setminus B$ (A'da olup B'de olmayanlar): $-3$'ten $1$'e. $1$, $B$'de **değil**, yani çıkarılmaz: $A \setminus B = [-3, 1]$.
- $B \setminus A$: $4$'ten $6$'ya. $4$, $A$'da değil: $B \setminus A = [4, 6]$.

**Kural.** Uç nokta için tek soru vardır: "Bu sayı istenen kümenin koşulunu sağlıyor mu?" Kesişimde iki kümede de, birleşimde en az birinde olmalı; farkta birinci kümede olup ikincide **olmamalı**.

## Tümleyen

**Örnek.** $A = [-2, 5)$ ise $\mathbb{R} \setminus A$ (A'nın tümleyeni) nedir?

$A$'da olmayan sayılar: $-2$'den küçükler ve $5$ ile $5$'ten büyükler. $-2 \in A$ olduğu için tümleyende yoktur; $5 \notin A$ olduğu için tümleyende vardır:

$$\mathbb{R} \setminus A = (-\infty, -2) \cup [5, \infty)$$

![İki sayı doğrusu: üstte A, eksi 2 dolu 5 boş. Altta tümleyeni: eksi 2 boş noktadan sola ok, 5 dolu noktadan sağa ok.](gorsel/tyt-matematik/03-01-tumleyen.svg "Tümleyen alınınca her uç noktanın durumu tersine döner: dolu olan boş, boş olan dolu olur.")

**Kural.** Tümleyende uçlar ters döner: `[` olan `)` olur, `)` olan `[` olur.

## ÖSYM tuzakları

> **Uçları kontrol etmeden saymak:** $(-3, 4)$ ile $[-3, 4]$ aralığındaki tam sayı sayısı farklıdır (6 ve 8). Saymadan önce iki ucu tek tek kontrol et.

> **Sonsuza köşeli parantez:** $[2, \infty]$ ya da $[-\infty, 5)$ yazımları yanlıştır. Sonsuzun yanı hep `(` ya da `)`.

> **Farkta ucu yanlış kapatmak:** $[-3, 4) \setminus (1, 6]$ işleminde cevap $[-3, 1)$ değil $[-3, 1]$'dir; çünkü $1$, $(1, 6]$ kümesinde yoktur ve çıkarılmaz.

> **Gerçek sayı ile tam sayıyı karıştırmak:** "$x > 1$ olan en küçük $x$ gerçek sayısı" yoktur; "en küçük $x$ tam sayısı" $2$'dir. Soru kökünü dikkatli oku.

## Kendini dene

### Soru 1
$-3 \le x < 2$ eşitsizliğini sağlayan $x$ gerçek sayılarının kümesi aşağıdakilerden hangisidir?

A) $(-3, 2)$
B) $[-3, 2]$
C) $[-3, 2)$
D) $(-3, 2]$
E) $(-\infty, 2)$

**Cevap:** C
**Çözüm:** $-3$ eşitlikle verildiği için dahildir (köşeli parantez); $2$ için kesin eşitsizlik olduğundan dahil değildir (normal parantez). Küme $[-3, 2)$ olur.

### Soru 2
$\left(-\frac{5}{2}, 4\right]$ aralığında kaç tam sayı vardır?

A) 6
B) 7
C) 8
D) 9
E) 10

**Cevap:** B
**Çözüm:** $-\frac{5}{2} = -2{,}5$ olduğundan en küçük tam sayı $-2$; $4$ dahil. Tam sayılar: $-2, -1, 0, 1, 2, 3, 4$. Toplam 7. Uç tam sayı olmadığı için $-2{,}5$'in dahil olup olmaması önemli değildir.

### Soru 3
$A = (-\infty, 3]$ ve $B = (-1, \infty)$ olduğuna göre $A \cap B$ kümesi aşağıdakilerden hangisidir?

A) $(-1, 3)$
B) $[-1, 3]$
C) $(-\infty, \infty)$
D) $[-1, 3)$
E) $(-1, 3]$

**Cevap:** E
**Çözüm:** İki koşul birlikte: $x \le 3$ ve $x > -1$. Ortak kısım $-1$ ile $3$ arası. $-1 \notin B$ olduğu için açık, $3 \in A$ ve $3 \in B$ olduğu için kapalı: $(-1, 3]$. $(-\infty, \infty)$ birleşimdir, kesişim değil.

## Özet kartı

- Köşeli parantez = dahil = dolu nokta; normal parantez = dahil değil = boş nokta.
- $\infty$ ve $-\infty$ yanında hep normal parantez.
- $a$, $b$ tam sayıysa tam sayı sayısı: $[a, b]$ için $b - a + 1$, yarı açıkta $b - a$, $(a, b)$ için $b - a - 1$.
- Kesişim, birleşim, fark: aralıkları aynı ölçekte alt alta çiz, her ucu ayrı kontrol et.
- Tümleyende uç noktaların durumu ters döner.

## Sonraki adım

Alıştırmaya geç (aşağıdaki düğme). Sonraki ders **Birinci Dereceden Bir Bilinmeyenli Denklemler**; eşitsizlik çözdüğünde cevabı bu dersteki aralık gösterimiyle yazacaksın.
