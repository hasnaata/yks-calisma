---
baslik: EBOB-EKOK Kavramı ve Özellikleri
ders: tyt-matematik
sure: 20 dk
kaynak: MEBİ Konu Özeti 09a0e51875
guncelleme: 2026-11-17
---
# EBOB-EKOK Kavramı ve Özellikleri

**Bu dersin sonunda:** iki ya da daha fazla sayının EBOB'unu ve EKOK'unu asal çarpanlardan hızlıca bulabilecek, $a \cdot b = \text{EBOB} \cdot \text{EKOK}$ özelliğiyle eksik sayıyı hesaplayabilecek ve ortak bölen ya da ortak kat sayısını EBOB ile EKOK'tan okuyabileceksin.

> **TYT'de yeri:** Hemen her sınavda en az bir soru EBOB ya da EKOK ister. Doğrudan "EBOB'u kaçtır?" az gelir; sık kalıplar şunlardır: "EBOB'u 8, EKOK'u 240, biri 48 olan sayı kaçtır?", "üç sayıya da bölünen üç basamaklı kaç sayı vardır?", "ardışık iki sayının EKOK'u verilmiş" ve EBOB, EKOK ile tanımlanmış yeni bir işlem.

## Önce hatırla

<details><summary>Asal Çarpanlar'dan: 84 sayısını asal çarpanlarına ayır.</summary>
$84 = 2 \cdot 42 = 2 \cdot 2 \cdot 21 = 2 \cdot 2 \cdot 3 \cdot 7$. Üslü yazımla <b>$84 = 2^2 \cdot 3 \cdot 7$</b>.
</details>

<details><summary>Asal Çarpanlar'dan: $2^3 \cdot 5^2$ sayısının kaç pozitif böleni vardır?</summary>
Her üsse 1 ekleyip çarparsın: $(3 + 1) \cdot (2 + 1) = $ <b>12</b>.
</details>

## Bölen ve kat

$5$, $20$'yi kalansız böler: $5$, $20$'nin bir **bölenidir**; $20$ de $5$'in bir **katıdır**. Bu dersin iki kavramı bu iki kelimenin "ortak" hâlidir: iki sayının **ortak bölenlerinin en büyüğü** ve **ortak katlarının en küçüğü**.

## EBOB: en büyük ortak bölen

**Örnek.** $36$ ile $48$'in ortak bölenleri nelerdir? En büyüğü kaçtır?

İki sayının pozitif bölenlerini yaz, ikisinde de olanları işaretle:

![Üç satır kutu. Birinci satır 36'nın bölenleri, ikinci satır 48'in bölenleri; 1, 2, 3, 4, 6 ve 12 iki satırda da yeşil. Üçüncü satır 12'nin bölenleri: tam olarak aynı yeşil sayılar.](gorsel/tyt-matematik/02-05-ortak-bolenler.svg "Yeşil kutular ortak bölenlerdir. Üçüncü satıra bak: ortak bölenlerin hepsi, en büyükleri olan 12'nin bölenleridir.")

Ortak bölenler $1, 2, 3, 4, 6, 12$; en büyüğü **12**. Yazılışı $\text{EBOB}(36, 48) = 12$.

Liste yöntemi büyük sayılarda yorar. Asıl yöntem asal çarpanlardır.

**Örnek.** $\text{EBOB}(72, 120)$ kaçtır?

$$72 = 2^3 \cdot 3^2 \qquad 120 = 2^3 \cdot 3 \cdot 5$$

| Asal | 72'de üs | 120'de üs | EBOB için (küçük üs) |
|---|---|---|---|
| 2 | 3 | 3 | $2^3$ |
| 3 | 2 | 1 | $3^1$ |
| 5 | 0 | 1 | $5^0 = 1$ |

$\text{EBOB}(72, 120) = 2^3 \cdot 3 = 24$.

**Kural.** Sayıları asal çarpanlarına ayır. **Ortak tabanları al, küçük üslüyü seç** ve çarp. Bir sayıda olmayan asal EBOB'a girmez.

İki sonuç hemen çıkar:

- İki sayının **bütün ortak bölenleri, EBOB'un bölenleridir.** $72$ ile $120$'nin kaç ortak pozitif böleni var diye sorulursa $24 = 2^3 \cdot 3$'ün bölen sayısını bulursun: $(3 + 1)(1 + 1) = 8$.
- Bir kesri **en sade hâline** getirmek için pay ve paydayı EBOB'a bölersin: $\dfrac{72}{120} = \dfrac{72 : 24}{120 : 24} = \dfrac{3}{5}$.

## EKOK: en küçük ortak kat

**Örnek.** $12$ ile $18$'in ortak katlarının en küçüğü kaçtır?

$12$'nin katları: $12, 24, 36, 48, 60, 72, \dots$ $\quad$ $18$'in katları: $18, 36, 54, 72, \dots$

İlk ortak kat **36**: $\text{EKOK}(12, 18) = 36$. Sonraki ortak katlar $72, 108, \dots$; hepsi $36$'nın katı.

Asal çarpanlarla: $12 = 2^2 \cdot 3$, $18 = 2 \cdot 3^2$. Her tabandan **büyük üslüyü** al: $2^2 \cdot 3^2 = 36$.

**Kural.** Sayıları asal çarpanlarına ayır. **Bütün tabanları al, büyük üslüyü seç** ve çarp. Bir sayıda bile olan asal EKOK'a girer.

- İki sayının **bütün ortak katları, EKOK'un katlarıdır.** "$12$'ye ve $18$'e bölünen iki basamaklı sayılar" $36$ ve $72$'dir.
- Kesirleri toplarken paydaları **EKOK'ta** eşitlersin: $\dfrac{5}{12} + \dfrac{7}{18} = \dfrac{15}{36} + \dfrac{14}{36} = \dfrac{29}{36}$.

## İkisi bir arada: Venn şeması

$72$ ve $120$'nin asal çarpanlarını tek tek (üssü açarak) iki çembere yerleştir. Ortak olanlar kesişime girer.

![İki kesişen çember: solda 72, sağda 120. Yalnız solda 3, yalnız sağda 5, kesişimde 2, 2, 2, 3. Altta: kesişimin çarpımı EBOB 24, bütün sayıların çarpımı EKOK 360.](gorsel/tyt-matematik/02-05-asal-venn.svg "Kesişimdeki çarpanların çarpımı EBOB, şekildeki bütün çarpanların çarpımı EKOK. Her çarpan bir kez sayılır.")

- **Kesişim** = EBOB: $2 \cdot 2 \cdot 2 \cdot 3 = 24$.
- **Bütün şekil** = EKOK: $3 \cdot 2 \cdot 2 \cdot 2 \cdot 3 \cdot 5 = 360$.

Üç sayıda da aynı kural geçerlidir: EBOB için üç sayıda ortak olan tabanların en küçük üssü, EKOK için bütün tabanların en büyük üssü. Örneğin $12 = 2^2 \cdot 3$, $20 = 2^2 \cdot 5$, $45 = 3^2 \cdot 5$ için $\text{EBOB} = 1$, $\text{EKOK} = 2^2 \cdot 3^2 \cdot 5 = 180$.

## Özellik 1: çarpım = EBOB · EKOK

**Örnek.** İki pozitif tam sayının EBOB'u 6, EKOK'u 180'dir. Sayılardan biri 36 ise diğeri kaçtır?

Venn şemasında $a$ = kesişim · yalnız $a$, $b$ = kesişim · yalnız $b$. Çarpınca kesişim iki kez, geri kalan her şey bir kez gelir; bu da EBOB · EKOK'tur. Öyleyse

$$36 \cdot b = 6 \cdot 180 \quad\Rightarrow\quad b = \frac{1080}{36} = 30.$$

Kontrol: $\text{EBOB}(36, 30) = 6$, $\text{EKOK}(36, 30) = 180$.

**Kural.** $a$ ve $b$ pozitif tam sayılarsa $a \cdot b = \text{EBOB}(a, b) \cdot \text{EKOK}(a, b)$. **Yalnızca iki sayı için** geçerlidir.

## Özellik 2: EBOB'u dışarı al

**Örnek.** $\text{EBOB}(a, b) = 6$, $\text{EKOK}(a, b) = 90$ ve $a < b$. $a$ ile $b$ hangi sayılar olabilir?

Her iki sayı da 6'nın katı: $a = 6m$, $b = 6n$. $m$ ile $n$ **aralarında asal** olmalı (ortak çarpanları olsaydı EBOB 6'dan büyük olurdu). O zaman $\text{EKOK} = 6 \cdot m \cdot n = 90$, yani $m \cdot n = 15$.

- $m = 1$, $n = 15$: $a = 6$, $b = 90$.
- $m = 3$, $n = 5$: $a = 18$, $b = 30$.

**Kural.** $\text{EBOB}(a, b) = d$ ise $a = d \cdot m$, $b = d \cdot n$ ($m$, $n$ aralarında asal) ve $\text{EKOK}(a, b) = d \cdot m \cdot n$.

## Özellik 3 ve 4: iki özel durum

![İki şekil. Solda ayrık iki çember: 8 için 2, 2, 2 ve 15 için 3, 5; EBOB 1, EKOK 120. Sağda 12'nin çemberi 36'nın çemberinin tamamen içinde: içte 2, 2, 3, dışta 3; EBOB 12, EKOK 36.](gorsel/tyt-matematik/02-05-ozel-durumlar.svg "Solda kesişim boş, bu yüzden EBOB 1 ve EKOK çarpıma eşit. Sağda küçük çember büyüğün içinde, bu yüzden EBOB küçük sayı, EKOK büyük sayı.")

- **Aralarında asal sayılar.** $8 = 2^3$ ile $15 = 3 \cdot 5$'in ortak asalı yok. $\text{EBOB}(8, 15) = 1$, $\text{EKOK}(8, 15) = 8 \cdot 15 = 120$. **Ardışık iki sayı her zaman aralarında asaldır**: $\text{EKOK}(12, 13) = 156$.
- **Biri diğerinin katı.** $36 = 3 \cdot 12$. $12$'nin bütün çarpanları $36$'da da var: $\text{EBOB}(12, 36) = 12$, $\text{EKOK}(12, 36) = 36$.

**Kural.** $a$ ile $b$ aralarında asal ise $\text{EBOB} = 1$, $\text{EKOK} = a \cdot b$. $b$, $a$'nın katı ise $\text{EBOB} = a$ (küçük), $\text{EKOK} = b$ (büyük).

## ÖSYM tuzakları

> **Kuralları karıştırmak:** EBOB için küçük üs, EKOK için büyük üs. $2^3 \cdot 3$ ile $2 \cdot 3^2 \cdot 5$ için EBOB $2 \cdot 3 = 6$'dır; $5$ yalnızca birinde olduğu için EBOB'a girmez ama EKOK'a girer: $2^3 \cdot 3^2 \cdot 5 = 360$.

> **Çarpım özelliğini üç sayıya uygulamak:** $2, 4, 8$ için çarpım $64$, ama $\text{EBOB} \cdot \text{EKOK} = 2 \cdot 8 = 16$. $a \cdot b = \text{EBOB} \cdot \text{EKOK}$ yalnızca iki sayı içindir.

> **Ortak katı çarpımla bulmak:** $12$ ve $18$'e bölünen sayılar $12 \cdot 18 = 216$'nın değil, $\text{EKOK} = 36$'nın katlarıdır. Üç basamaklı ortak katları $216$'nın katlarıyla sayan 4 bulur; doğrusu $36$'nın katlarıdır ve 25 tanedir.

> **$m$ ve $n$'yi aralarında asal seçmemek:** $\text{EBOB} = 6$, $\text{EKOK} = 90$ iken $m \cdot n = 15$; ama $\text{EBOB} = 4$, $\text{EKOK} = 48$ olsaydı $m \cdot n = 12$ ve $m = 2$, $n = 6$ seçilemez (sayılar 8 ve 24 olur, EBOB'ları 8'dir).

## Kendini dene

### Soru 1
$A = 2^3 \cdot 3 \cdot 5^2$ ve $B = 2^2 \cdot 3^3 \cdot 7$ olduğuna göre $\text{EBOB}(A, B)$ kaçtır?

A) 6
B) 12
C) 36
D) 60
E) 180

**Cevap:** B
**Çözüm:** Ortak tabanlar 2 ve 3. Küçük üsler: $2^2$ ve $3^1$. $\text{EBOB} = 4 \cdot 3 = 12$. $5$ yalnızca $A$'da, $7$ yalnızca $B$'de olduğu için EBOB'a girmez. $5$'i de katan $2^2 \cdot 3 \cdot 5 = 60$, $2$'nin üssünü 1 alan $2 \cdot 3 = 6$ bulur.

### Soru 2
İki pozitif tam sayının EBOB'u 4, EKOK'u 60'tır. Sayılardan biri 12 olduğuna göre diğeri kaçtır?

A) 15
B) 16
C) 20
D) 24
E) 30

**Cevap:** C
**Çözüm:** $12 \cdot b = 4 \cdot 60 = 240$, $b = 20$. Kontrol: $12 = 2^2 \cdot 3$, $20 = 2^2 \cdot 5$; EBOB $4$, EKOK $2^2 \cdot 3 \cdot 5 = 60$. EKOK'u 4'e bölen 15 bulur ama $\text{EBOB}(12, 15) = 3$'tür.

### Soru 3
$1 < a < b$ olmak üzere $a$ ve $b$ aralarında asal iki tam sayıdır. $\text{EKOK}(a, b) = 35$ olduğuna göre $b - a$ kaçtır?

A) 2
B) 5
C) 7
D) 12
E) 34

**Cevap:** A
**Çözüm:** Aralarında asal olduklarından $a \cdot b = \text{EKOK} = 35$. $35 = 1 \cdot 35 = 5 \cdot 7$; $a > 1$ olduğundan $a = 5$, $b = 7$. $b - a = 2$. $a = 1$ alan 34 bulur.

## Özet kartı

- EBOB: ortak tabanlar, **küçük** üs. EKOK: bütün tabanlar, **büyük** üs.
- Ortak bölenler = EBOB'un bölenleri; ortak katlar = EKOK'un katları.
- İki sayı için $a \cdot b = \text{EBOB} \cdot \text{EKOK}$ (üç sayıda geçerli değil).
- $\text{EBOB} = d$ ise $a = dm$, $b = dn$, $m$ ile $n$ aralarında asal, $\text{EKOK} = dmn$.
- Aralarında asal (ardışık sayılar dahil): EBOB 1, EKOK çarpım. Biri diğerinin katı: EBOB küçük, EKOK büyük.
- Kesir sadeleştirme EBOB ile, payda eşitleme EKOK ile yapılır.

## Sonraki adım

Alıştırmaya geç (aşağıdaki düğme). Sonraki ders **EBOB-EKOK Problemleri**; bir bahçeyi eşit parsellere bölme, farklı aralıklarla çalan zilleri buluşturma gibi durumlarda EBOB mu EKOK mu gerektiğine karar vermeyi öğreneceksin.
