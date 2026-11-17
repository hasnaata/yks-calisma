---
baslik: Alt Küme
ders: tyt-matematik
sure: 20 dk
kaynak: MEBİ Konu Özeti 0e9a9d8a87
guncelleme: 2026-11-18
---
# Alt Küme

<div class="giris" dir="rtl" lang="ar">

**الدرس ده عن إيه؟** عن المجموعة الجزئية (alt küme): إمتى نقول إن مجموعة جوّه مجموعة تانية، وإزاي نعدّ كل المجموعات الجزئية من غير ما نكتبها واحدة واحدة.

- هتفرّق بين "عنصر في المجموعة" (eleman) و"مجموعة جزئية منها"، وده بالذات اللي ناس كتير بتغلط فيه.
- هتعرف تحسب عدد المجموعات الجزئية والمجموعات الجزئية الفعلية (öz alt küme)، وكمان اللي فيها عناصر معيّنة أو مافيهاش.
- هتفهم إمتى مجموعتين يبقوا متساويين (eşit kümeler).

**ليه مهم؟** عدد المجموعات الجزئية هو أكتر حتة بتيجي من أسئلة المجموعات (kümeler) في TYT، وغالبًا في شكل موقف من الحياة زي اختيار مكونات من منيو أو تكوين فريق.

الدرس ٢٠ دقيقة بس، والفكرة كلها سؤال واحد بتسأله لكل عنصر: موجود ولا مش موجود؟ يلا بينا.

</div>

**Bu dersin sonunda:** "eleman" ile "alt küme" ilişkisini karıştırmadan yazabilecek, $n$ elemanlı bir kümenin alt küme ve öz alt küme sayısını, belli elemanları içeren ya da içermeyen alt kümelerin sayısını bulabilecek ve iki kümenin eşitliğini kullanabileceksin.

> **TYT'de yeri:** Kümeler sorularının en sık gelen parçası alt küme sayısıdır. "$a$ bulunan, $b$ bulunmayan kaç alt küme var?", "en az 2 elemanlı kaç alt küme var?", "hangisi doğrudur: $\in$ mi $\subseteq$ mi?" kalıpları ve menüden malzeme seçmek, ekip kurmak gibi günlük hayat durumları gelir.

## Önce hatırla

<details><summary>Kümelerde temel kavramlar dersinden: $A = \{1, \{2, 3\}, \emptyset\}$ kümesi kaç elemanlıdır?</summary>
En dıştaki süslü parantezin içinde virgülle ayrılmış üç parça var: $1$, $\{2, 3\}$ ve $\emptyset$. İç küme tek eleman sayılır, $\emptyset$ da burada bir elemandır. <b>$s(A) = 3$</b>.
</details>

<details><summary>Kümelerde temel kavramlar dersinden: $B = \{x \mid x \in \mathbb{N},\ 2x + 1 < 9\}$ kümesini liste yöntemiyle yaz.</summary>
$2x + 1 < 9$ ise $x < 4$. Doğal sayılar $0$'dan başlar: <b>$B = \{0, 1, 2, 3\}$</b>, $s(B) = 4$.
</details>

## Alt küme nedir?

**Örnek.** $A = \{1, 2\}$ ve $B = \{1, 2, 3, 4\}$ olsun. $A$'nın her elemanına tek tek bak: $1 \in B$, $2 \in B$. $A$'nın $B$'de olmayan hiçbir elemanı yok. O hâlde $A$, $B$'nin **alt kümesidir**: $A \subseteq B$.

![Büyük bir elips B, içinde mavi küçük bir elips A. A'nın içinde 1 ve 2, B'nin içinde A'nın dışında 3 ve 4 var.](gorsel/tyt-matematik/07-02-venn-alt-kume.svg "A'nın elipsi bütünüyle B'nin içinde. A'nın dışarı taşan hiçbir elemanı yok.")

**Kural.** $A$'nın her elemanı $B$'nin de elemanıysa $A \subseteq B$ yazılır, "$A$, $B$'nin alt kümesidir" diye okunur. Aynı durum $B \supseteq A$ ("$B$, $A$'yı kapsar") diye de yazılır. $A$'nın en az bir elemanı $B$'de yoksa $A \not\subseteq B$ yazılır.

Ders kitaplarında ve sorularda alt küme için $A \subset B$ yazımı da kullanılır. $\subseteq$ işaretindeki alt çizgi "iki küme eşit de olabilir" demektir.

### Eleman mı, alt küme mi?

**Örnek.** $A = \{1, \{2\}, 3\}$ kümesinin elemanları $1$, $\{2\}$ ve $3$'tür.

| İfade | Doğru mu? | Neden |
|---|---|---|
| $\{2\} \in A$ | Doğru | $\{2\}$ listede bir eleman. |
| $\{2\} \subseteq A$ | Yanlış | Bunun için $2 \in A$ olmalı; $2$ tek başına listede yok. |
| $\{\{2\}\} \subseteq A$ | Doğru | Tek elemanı $\{2\}$ ve $\{2\} \in A$. |
| $\{1, 3\} \subseteq A$ | Doğru | $1 \in A$ ve $3 \in A$. |
| $\{1, 3\} \in A$ | Yanlış | $\{1, 3\}$ listede yazılı değil. |

**Kural.** $\in$ işaretinin solunda **bir eleman**, $\subseteq$ işaretinin solunda **bir küme** durur. "$X \subseteq A$ mı?" sorusunda $X$'in süslü parantezini aç ve içindeki her parçanın $A$'nın listesinde yazılı olup olmadığına bak.

> **Tuzak:** $3 \in A$ doğruysa $\{3\} \subseteq A$ da doğrudur; ama $\{3\} \in A$ ancak $\{3\}$ listede ayrıca yazılıysa doğrudur. Süslü parantez eklemek ilişkiyi değiştirir.

## Alt kümenin üç özelliği

**Örnek.** $A = \{5, 7\}$ olsun.

- $\emptyset \subseteq A$: Boş kümenin $A$'da olmayan bir elemanı yok, çünkü hiç elemanı yok. Bu yüzden boş küme **her kümenin** alt kümesidir.
- $A \subseteq A$: $A$'nın her elemanı elbette $A$'dadır. **Her küme kendisinin** alt kümesidir.
- $A \subseteq \{5, 7, 9\}$ ve $\{5, 7, 9\} \subseteq \{5, 7, 9, 11\}$ ise $A \subseteq \{5, 7, 9, 11\}$ olur.

Üçüncü özelliğe **geçişme** denir: iç içe kutular gibi düşün.

![İç içe üç elips: en dışta C, onun içinde yeşil B, B'nin içinde mavi A.](gorsel/tyt-matematik/07-02-gecisme.svg "A, B'nin içinde; B de C'nin içinde. Öyleyse A, C'nin de içindedir.")

**Kural.** Her $A$ kümesi için $\emptyset \subseteq A$ ve $A \subseteq A$. $A \subseteq B$ ve $B \subseteq C$ ise $A \subseteq C$.

## Alt küme sayısı

**Örnek.** $\{a, b, c\}$ kümesinin bütün alt kümelerini yaz.

Her eleman için tek bir soru sor: "Bu eleman alt kümede var mı, yok mu?" $a$ için 2 seçenek, $b$ için 2, $c$ için 2 seçenek var.

![Soldan sağa dallanan ağaç. Her basamakta a, b, c için var ve yok diye iki dal açılıyor; sağda sekiz alt küme: a b c, a b, a c, a, b c, b, c ve boş küme.](gorsel/tyt-matematik/07-02-agac.svg "Yeşil dal var, kırmızı dal yok demek. Her eleman seçenek sayısını ikiye katlar; hepsine yok diyen dal boş kümeyi verir.")

Sekiz alt küme: $\emptyset$, $\{a\}$, $\{b\}$, $\{c\}$, $\{a, b\}$, $\{a, c\}$, $\{b, c\}$, $\{a, b, c\}$. Sayı $2 \cdot 2 \cdot 2 = 2^3 = 8$.

| $s(A)$ | 0 | 1 | 2 | 3 | 4 | 5 | 6 |
|---|---|---|---|---|---|---|---|
| Alt küme sayısı | 1 | 2 | 4 | 8 | 16 | 32 | 64 |

Bir kümenin kendisi dışındaki bütün alt kümelerine **öz alt küme** denir. $\{a, b, c\}$ kümesinin öz alt kümeleri yukarıdaki listeden $\{a, b, c\}$ çıkarılınca kalan 7 kümedir. $\emptyset$ öz alt kümedir.

**Kural.** $s(A) = n$ ise

$$\text{alt küme sayısı} = 2^n, \qquad \text{öz alt küme sayısı} = 2^n - 1.$$

**Örnek.** $A = \{a, b, c, d\}$ kümesinin **en az 2 elemanlı** kaç alt kümesi vardır?

Hepsini yazmak yerine istemediklerini çıkar. Toplam $2^4 = 16$. İstenmeyenler: boş küme (1 tane) ve tek elemanlılar ($\{a\}, \{b\}, \{c\}, \{d\}$, 4 tane). Sonuç $16 - 1 - 4 = 11$.

> **Tuzak:** Öz alt küme sayısında yalnızca kümenin kendisi çıkarılır, $\emptyset$ çıkarılmaz: $2^n - 1$, $2^n - 2$ değil. "En az 1 elemanlı" ya da "boş olmayan" denirse çıkarılan $\emptyset$'dir.

## Belli elemanları içeren alt kümeler

**Örnek.** $A = \{a, b, c, d, e\}$ kümesinin kaç alt kümesinde $a$ **bulunur**, $b$ **bulunmaz**?

$a$ için karar verilmiş (var), $b$ için de karar verilmiş (yok). Bu iki elemanın tek seçeneği kalır. Serbest kalan $c$, $d$, $e$ için ikişer seçenek var.

![Beş kutu: yeşil a kutusunun üstünde 1 ve altında kesin var; kırmızı b kutusunun üstünde 1 ve altında kesin yok; mavi c, d, e kutularının üstünde 2 ve altında serbest yazıyor. Altta 1 çarpı 1 çarpı 2 çarpı 2 çarpı 2 eşittir 8.](gorsel/tyt-matematik/07-02-sabit-serbest.svg "Koşulu olan elemanların tek seçeneği var. Yalnızca serbest elemanlar sayıyı ikiye katlar.")

Sonuç $2^3 = 8$.

**Kural.** Koşul verilen elemanları ayır, geriye kalan $k$ serbest eleman için cevap $2^k$'dir. $n$ elemanlı kümede $r$ tane elemanın durumu belliyse cevap $2^{n-r}$ olur.

Aynı kümede "veya" ile "yalnız biri" sorularını karşılaştır. $a$ ile $b$ için dört durum var; $c$, $d$, $e$ her durumda serbesttir ve $2^3 = 8$ seçenek verir:

| $a$ | $b$ | Alt küme sayısı |
|---|---|---|
| var | yok | 8 |
| yok | var | 8 |
| var | var | 8 |
| yok | yok | 8 |

- "$a$ **veya** $b$ bulunur": ilk üç satır, $3 \cdot 8 = 24$. Kısa yol: hepsinden ikisinin de bulunmadığı satırı çıkar, $32 - 8 = 24$.
- "$a$ ile $b$'den **yalnız biri** bulunur" ("$a$ **ya da** $b$ bulunur"): ilk iki satır, $2 \cdot 8 = 16$.

**Kural.** "En az biri bulunur" türü sorularda tümleme yolu en kısasıdır: (bütün alt kümeler) $-$ (hiçbiri bulunmayan alt kümeler).

**Örnek.** $A = \{1, 2\}$ ve $B = \{1, 2, 3, 4\}$ için $A \subseteq K \subseteq B$ koşulunu sağlayan kaç $K$ kümesi vardır?

$K$, $A$'yı kapsadığı için $1$ ve $2$ kesin var. $K$, $B$'nin alt kümesi olduğu için $B$'de olmayan bir eleman alamaz. Serbest kalanlar $3$ ve $4$: $2^2 = 4$ küme. Bunlar $\{1, 2\}$, $\{1, 2, 3\}$, $\{1, 2, 4\}$, $\{1, 2, 3, 4\}$.

## İki kümenin eşitliği

**Örnek.** $\{a + 1, 4\} = \{7, b\}$ olduğuna göre $a$ ve $b$ kaçtır?

İki küme eşitse elemanları aynıdır. Sol kümede $7$ olmalı; $4 \neq 7$ olduğu için $a + 1 = 7$, $a = 6$. Sağ kümede $4$ olmalı; $7 \neq 4$ olduğu için $b = 4$.

**Kural.** Elemanları tamamen aynı olan kümelere **eşit kümeler** denir: $A = B$. Eşit değilse $A \neq B$ yazılır. İki kümenin eşit olması, her birinin öbürünün alt kümesi olmasıyla aynı şeydir:

$$(A \subseteq B \ \text{ve}\ B \subseteq A) \iff A = B$$

Bu yüzden $A \subseteq B$, $B \subseteq C$ ve $C \subseteq A$ verilirse geçişmeden $A \subseteq C$ çıkar; $C \subseteq A$ ile birlikte $A = C$, sonra $A = B = C$ bulunur.

## ÖSYM tuzakları

> **$\in$ ile $\subseteq$ karıştırmak:** $A = \{1, \{2\}\}$ ise $\{2\} \in A$ doğru, $\{2\} \subseteq A$ yanlıştır ($2 \notin A$). Süslü parantezin içini aç ve listeyle karşılaştır.

> **Öz alt kümede boş kümeyi atmak:** 5 elemanlı kümenin öz alt küme sayısı $2^5 - 1 = 31$'dir; 30 değil. Yalnızca kümenin kendisi çıkarılır.

> **"Veya" ile "yalnız biri"ni karıştırmak:** 5 elemanlı kümede "$a$ veya $b$ bulunan" 24, "yalnız biri bulunan" 16 alt küme vardır. "Veya" ikisinin birlikte bulunmasını da kapsar.

> **Eleman sayısını yanlış almak:** $\{1, \{1, 2\}, \emptyset\}$ kümesi 3 elemanlıdır, alt küme sayısı $2^3 = 8$'dir. İç kümeyi açıp 4 eleman sayan 16 bulur.

## Kendini dene

### Soru 1
$A = \{2, 4, 6, 8\}$ kümesinin alt kümelerinden kaç tanesinde $4$ bulunur?

A) 4
B) 8
C) 12
D) 15
E) 16

**Cevap:** B
**Çözüm:** $4$'ün durumu belli (var). Serbest kalan $2$, $6$, $8$ için ikişer seçenek: $2^3 = 8$. 16 bütün alt kümelerin sayısıdır; bunların yarısında $4$ bulunur, yarısında bulunmaz.

### Soru 2
$A = \{1, \{2\}, 3\}$ olduğuna göre aşağıdakilerden hangisi doğrudur?

A) $2 \in A$
B) $\{2\} \subseteq A$
C) $\{1, 3\} \in A$
D) $\{\{2\}, 3\} \subseteq A$
E) $\{3\} \in A$

**Cevap:** D
**Çözüm:** $A$'nın elemanları $1$, $\{2\}$ ve $3$. D'deki kümenin elemanları $\{2\}$ ve $3$; ikisi de $A$'nın elemanı, bu yüzden alt kümedir. A ve B yanlış, çünkü $2$ tek başına $A$'da yok. C ve E yanlış, çünkü $\{1, 3\}$ ve $\{3\}$ listede eleman olarak yazılı değil; bunlar $A$'nın alt kümesidir, elemanı değil.

### Soru 3
$A = \{a, b, c, d, e\}$ kümesinin alt kümelerinden kaç tanesinde $a$ veya $b$ bulunur?

A) 8
B) 16
C) 24
D) 28
E) 32

**Cevap:** C
**Çözüm:** Bütün alt kümeler $2^5 = 32$. $a$ ve $b$'nin ikisinin de bulunmadığı alt kümelerde yalnızca $c$, $d$, $e$ serbest: $2^3 = 8$. Sonuç $32 - 8 = 24$. 16, yalnız birinin bulunduğu durumdur; "veya" ikisinin birlikte bulunmasını da kapsar.

## Özet kartı

- $A \subseteq B$: $A$'nın her elemanı $B$'de. $\in$ elemanla, $\subseteq$ kümeyle kullanılır.
- $\emptyset \subseteq A$, $A \subseteq A$; $A \subseteq B$ ve $B \subseteq C$ ise $A \subseteq C$.
- $s(A) = n$: alt küme sayısı $2^n$, öz alt küme sayısı $2^n - 1$.
- Belli elemanlar sabit, kalan $k$ eleman serbest: $2^k$ alt küme.
- "En az biri bulunur": hepsi eksi hiçbiri bulunmayanlar.
- $A \subseteq B$ ve $B \subseteq A$ ise $A = B$.

## Sonraki adım

Alıştırmaya geç (aşağıdaki düğme). Sonraki konu **Kümelerde İşlemler**; ilk dersi **Kümelerde Kesişim ve Birleşim İşlemleri**. İki kümenin ortak elemanlarını ve bütün elemanlarını Venn şemasıyla bulacaksın.
