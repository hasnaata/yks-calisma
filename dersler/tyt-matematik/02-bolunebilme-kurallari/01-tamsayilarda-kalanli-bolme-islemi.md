---
baslik: Tamsayılarda Kalanlı Bölme İşlemi
ders: tyt-matematik
sure: 20 dk
kaynak: MEBİ Konu Özeti 8aa2f97a11
guncelleme: 2026-11-18
---
# Tamsayılarda Kalanlı Bölme İşlemi

<div class="giris" dir="rtl" lang="ar">

**الدرس ده عن إيه؟** عن القسمة اللي فيها باقي (kalanlı bölme): المقسوم (bölünen) والمقسوم عليه (bölen) وخارج القسمة (bölüm) والباقي (kalan)، وإزاي تربطهم كلهم في علاقة واحدة.

- هتعرف إن المقسوم بيساوي المقسوم عليه في خارج القسمة زائد الباقي، وإن الباقي دايمًا أصغر من المقسوم عليه.
- هتتعلم تجيب أكبر وأصغر قيمة للمقسوم، وتحل مسائل القسمة المتتالية بالتعويض.
- هتلاقي باقي مجموع أو فرق أو حاصل ضرب أو عدد مرفوع لأُس من غير ما تعرف الأعداد نفسها، بالبواقي بس.

**ليه مهم؟** في كل امتحان TYT بييجي سؤال أو اتنين على الموضوع ده، وقابلية القسمة (bölünebilme) و EBOB-EKOK مبنيين عليه.

هو ٢٠ دقيقة بس، وكل قاعدة معاها مثال محلول خطوة بخطوة، فخد وقتك وهتلاقيه سهل.

</div>

**Bu dersin sonunda:** bir bölme işlemini $A = B \cdot C + K$ eşitliğine çevirip bilinmeyeni bulabilecek, kalanın alabileceği değerleri sınırlayabilecek ve büyük bir ifadenin kalanını yalnızca kalanlarla hesaplayabileceksin.

> **TYT'de yeri:** Her sınavda doğrudan ya da dolaylı 1–2 soru gelir. "Bölünen en çok/en az kaçtır?", "Bu ifadenin 7 ile bölümünden kalan kaçtır?" ve "paketlere koyunca … tane artıyor" diye başlayan günlük hayat soruları en sık kalıplardır. Bölünebilme, EBOB-EKOK ve periyodik problemler bu dersin üzerine kurulur.

## Önce hatırla

<details><summary>Rasyonel sayılarda işlemlerden: $\frac{2}{3} + \frac{3}{4}$ işleminin sonucu kaçtır?</summary>
Paydalar EKOK'ta, yani 12'de eşitlenir: $\frac{8}{12} + \frac{9}{12} = \frac{17}{12}$.
</details>

<details><summary>Rasyonel sayılarda işlemlerden: $\frac{5}{6} : \frac{10}{9}$ işleminin sonucu kaçtır?</summary>
Birinci kesir aynen yazılır, ikinci ters çevrilip çarpılır: $\frac{5}{6} \cdot \frac{9}{10} = \frac{45}{60} = \frac{3}{4}$.
</details>

## Bölmenin dört parçası

**Örnek.** 47 cevizi 6 kişiye eşit ve olabildiğince çok paylaştır. Her kişi 7 ceviz alır ($6 \cdot 7 = 42$), 5 ceviz artar. 5 ceviz 6 kişiye birer tane daha vermeye yetmez, paylaştırma burada biter.

![Bölme düzeni: solda 47, sağ üstte 6, altında 7; 47'nin altında 42 çıkarılmış ve en altta kalan 5. Altta 47 eşittir 6 çarpı 7 artı 5 yazıyor.](gorsel/tyt-matematik/02-01-bolme-semasi.svg "Her parçanın adı ve rengi ayrı. Alttaki eşitlik bütün bölme sorularının başlangıç noktasıdır.")

Aynı paylaşımı sayı doğrusunda düşün: 0'dan 6'şar adım atarak 47'ye gidiyorsun. 7 tam adım seni 42'ye götürür; geriye kalan 5 birim bir adım daha atmaya yetmez.

![Sayı doğrusu: 0'dan 42'ye kadar 6'şar birimlik yedi yay, 42 ile 47 arası kırmızıyla işaretli ve kalan 5 yazıyor.](gorsel/tyt-matematik/02-01-sayi-dogrusu.svg "Bölüm, atılan tam adım sayısıdır (7). Kalan, son adımdan sonra artan parçadır (5) ve her zaman bir adımdan kısadır.")

**Kural.** $B \ne 0$ olmak üzere $A$ sayısı $B$'ye bölündüğünde bölüm $C$, kalan $K$ ise

$$A = B \cdot C + K \qquad 0 \le K < B$$

Yani **Bölünen = Bölen · Bölüm + Kalan** ve kalan bölenden küçüktür. $K = 0$ ise $A$, $B$'ye **tam bölünür**.

## Kalanın sınırı: en büyük ve en küçük bölünen

**Örnek.** Bir $A$ doğal sayısı 9'a bölündüğünde bölüm 5 ise $A$ en az ve en çok kaçtır?

$A = 9 \cdot 5 + K$ ve kalan $0 \le K \le 8$. En küçük kalanla $A = 45$, en büyük kalanla $A = 45 + 8 = 53$.

**Örnek.** Bir $A$ doğal sayısı $B$'ye bölündüğünde bölüm 4, kalan 9 ise $A$ en az kaçtır?

Kalan 9 olduğuna göre bölen 9'dan büyüktür: $B \ge 10$. $A = 4B + 9$ en küçük $B$ ile en küçük olur: $A = 4 \cdot 10 + 9 = 49$.

**Kural.** Bölen $B$ ise kalan en çok $B - 1$ olur. Kalan $K$ verilmişse bölen en az $K + 1$'dir.

## Bölünen ve bölen ortak bir sayının katıysa

**Örnek.** 4'e tam bölünen bir $A$ sayısı 12'ye bölündüğünde kalan $K$ olsun. $K$ hangi değerleri alabilir?

$K = A - 12C$. $A$ da $12C$ de 4'ün katı, farkları da 4'ün katıdır. $K < 12$ olduğundan $K \in \{0, 4, 8\}$. Deneme: $40 = 12 \cdot 3 + 4$, $44 = 12 \cdot 3 + 8$, $48 = 12 \cdot 4 + 0$.

**Kural.** Bölünen ve bölen aynı $k$ sayısının katıysa kalan da $k$'nın katıdır.

## Bölen ile bölümün yer değiştirmesi

**Örnek.** $47 = 6 \cdot 7 + 5$. Çarpmanın sırası önemsiz, yani $47 = 7 \cdot 6 + 5$ diye de yazabilirsin. Kalan 5, yeni bölen 7'den küçük olduğu için bu da geçerli bir bölmedir: 47'nin 7'ye bölümünden bölüm 6, kalan yine 5.

Karşı örnek: $29 = 6 \cdot 4 + 5$. Burada kalan 5, bölüm 4'ten büyük. 29'u 4'e bölersen kalan 5 olamaz (kalan 4'ten küçük olmalı): $29 = 4 \cdot 7 + 1$.

**Kural.** Kalan bölümden küçükse bölen ile bölüm yer değiştirdiğinde kalan değişmez.

## Ardışık bölmeler

**Örnek.** $A$ sayısı 5'e bölündüğünde bölüm $B$, kalan 3; $B$ sayısı 4'e bölündüğünde bölüm $C$, kalan 2'dir. $A$ sayısının 20 ile bölümünden kalan kaçtır?

![İki bölme düzeni yan yana: A bölü 5, bölüm B, kalan 3; B bölü 4, bölüm C, kalan 2. Birincinin bölümünden ikincinin bölünenine ok var. Altta A eşittir 20C artı 13.](gorsel/tyt-matematik/02-01-ardisik-bolme.svg "Birinci bölmenin bölümü, ikinci bölmenin bölünenidir. Her bölmeyi eşitlik olarak yaz, sonra içten dışa yerine koy.")

Her bölmeyi eşitlik olarak yaz: $A = 5B + 3$ ve $B = 4C + 2$. İkinciyi birincide yerine koy:

$$A = 5(4C + 2) + 3 = 20C + 10 + 3 = 20C + 13$$

$13 < 20$ olduğu için $A$'nın 20 ile bölümünden kalan **13**'tür. Kontrol: $C = 1$ için $B = 6$, $A = 33$ ve $33 = 20 \cdot 1 + 13$.

**Kural.** Birden fazla bölme verilirse hepsini $A = B \cdot C + K$ biçiminde yaz ve yerine koyma yöntemiyle $A$'yı en son bölüm cinsinden bul. Yeni bölen, bölenlerin çarpımıdır ($5 \cdot 4 = 20$).

## Kalanlarla işlem

**Örnek.** $A$ sayısının 7 ile bölümünden kalan 3, $B$ sayısının 7 ile bölümünden kalan 5'tir. Sayıları bilmeden şu kalanları bulabilirsin:

| İfade | Kalanlarla işlem | 7 ile bölümünden kalan |
|---|---|---|
| $A + B$ | $3 + 5 = 8$ | $8 = 7 + 1$, kalan $1$ |
| $A \cdot B$ | $3 \cdot 5 = 15$ | $15 = 14 + 1$, kalan $1$ |
| $A - B$ | $3 - 5 = -2$ | $-2 + 7 = 5$, kalan $5$ |
| $A^2$ | $3^2 = 9$ | $9 = 7 + 2$, kalan $2$ |

Kontrol için $A = 10$, $B = 12$ al: $A + B = 22$ (kalan 1), $A \cdot B = 120 = 7 \cdot 17 + 1$ (kalan 1), $A - B = -2$ (kalan 5), $A^2 = 100 = 7 \cdot 14 + 2$ (kalan 2). Hepsi tutuyor.

![Akış şeması: her sayının kalanını bul, sayılar yerine kalanları yaz, işlemi kalanlarla yap. Sonuç bölen ya da daha büyükse bölene böl, negatifse bölenin katını ekle, 0 ile bölen arasındaysa cevap odur.](gorsel/tyt-matematik/02-01-kalan-yontemi.svg "Son adımı atlama: bulduğun sayı 0 ile bölen arasında değilse henüz kalan değildir.")

**Kural.** $M$ ve $N$'nin $x$ ile bölümünden kalanlar $m$ ve $n$ ise $M + N$, $M - N$, $M \cdot N$ ve $M^a$ ifadelerinin $x$ ile bölümünden kalanları sırasıyla $m + n$, $m - n$, $m \cdot n$ ve $m^a$ sayılarının $x$ ile bölümünden kalanlara eşittir.

**Kuvvette kısa yol.** $13^{20}$ sayısının 6 ile bölümünden kalan: $13 = 6 \cdot 2 + 1$, kalan 1. $1^{20} = 1$, cevap **1**. Kalan 1'e ya da küçük bir sayıya dönüşüyorsa kuvvet kolaylaşır: $2^3 = 8$'in 7 ile bölümünden kalan 1 olduğu için $2^{10} = (2^3)^3 \cdot 2$ sayısının 7 ile bölümünden kalan $1 \cdot 2 = 2$'dir.

## ÖSYM tuzakları

> **Kalanı bölenden büyük ya da eşit almak:** "9'a bölümünden bölüm 5" olan en büyük sayı $9 \cdot 5 + 9 = 54$ değildir; kalan en çok 8, cevap $53$.

> **Bölenin kalandan büyük olduğunu unutmak:** Kalan 9 verilmişse bölen 9 olamaz. "En az" sorularında bölen olarak $K + 1$ seçilir.

> **Kalanla işlemde son adımı atlamak:** $3 \cdot 5 = 15$ bulup "kalan 15" demek yanlıştır; 7'den küçük olana kadar 7 çıkarırsın: kalan 1. Sonuç negatifse ($3 - 5 = -2$) bölen eklersin: kalan 5.

> **Negatif bölünende kalanı negatif yazmak:** $-17$'nin 5 ile bölümünden kalan $-2$ değildir. Kalan hiçbir zaman negatif olmaz: $-17 = 5 \cdot (-4) + 3$, kalan 3.

> **Yer değiştirmeyi her zaman doğru sanmak:** Bölen ile bölüm ancak kalan bölümden küçükse yer değiştirebilir.

## Kendini dene

### Soru 1
Bir $A$ doğal sayısının 8 ile bölümünden bölüm 11, kalan 5'tir. Buna göre $A$ kaçtır?

A) 83
B) 88
C) 93
D) 96
E) 99

**Cevap:** C
**Çözüm:** Bölünen = Bölen · Bölüm + Kalan: $A = 8 \cdot 11 + 5 = 88 + 5 = 93$. Kalanı eklemeyi unutan 88, kalanı çıkaran 83 bulur.

### Soru 2
$A$ sayısının 9 ile bölümünden kalan 5, $B$ sayısının 9 ile bölümünden kalan 7'dir. Buna göre $A \cdot B + A - B$ ifadesinin 9 ile bölümünden kalan kaçtır?

A) 2
B) 3
C) 5
D) 6
E) 8

**Cevap:** D
**Çözüm:** Sayılar yerine kalanları yaz: $5 \cdot 7 + 5 - 7 = 35 - 2 = 33$. $33 = 9 \cdot 3 + 6$, kalan 6. Yalnızca $A \cdot B$'nin kalanını alan 8 ($35 = 27 + 8$), $A - B$ yerine $A + B$ alan 2 ($47 = 45 + 2$) bulur.

### Soru 3
$A$ sayısının 7 ile bölümünden bölüm $B$, kalan 2'dir. $B$ sayısının 3 ile bölümünden bölüm $C$, kalan 1'dir. Buna göre $A$ sayısının 21 ile bölümünden kalan kaçtır?

A) 2
B) 3
C) 7
D) 8
E) 9

**Cevap:** E
**Çözüm:** $A = 7B + 2$ ve $B = 3C + 1$. Yerine koy: $A = 7(3C + 1) + 2 = 21C + 9$. $9 < 21$ olduğu için kalan 9. Kalanları toplayan 3, eşitlikleri ters kuran ($3 \cdot 2 + 1$) 7 bulur.

## Özet kartı

- Bölünen = Bölen · Bölüm + Kalan ve $0 \le \text{Kalan} < \text{Bölen}$.
- Kalan en çok bölen − 1; kalan $K$ ise bölen en az $K + 1$.
- Bölünen ve bölen $k$'nın katıysa kalan da $k$'nın katıdır.
- Kalan bölümden küçükse bölen ile bölüm yer değiştirir, kalan aynı kalır.
- Ardışık bölmelerde her bölmeyi eşitlik yaz, yerine koy.
- Toplam, fark, çarpım ve kuvvette sayılar yerine kalanlarla işlem yap; sonucu 0 ile bölen arasına getir.

## Sonraki adım

Alıştırmaya geç (aşağıdaki düğme). Sonraki ders **Bölünebilme Kuralları 1**; bir sayının 2, 3, 4, 5, 9 gibi sayılarla bölümünden kalanı bölme yapmadan bulmayı öğreneceksin.
