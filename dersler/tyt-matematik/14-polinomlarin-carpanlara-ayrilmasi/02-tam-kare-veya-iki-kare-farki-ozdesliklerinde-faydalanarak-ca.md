---
baslik: Tam Kare ve İki Kare Farkı ile Çarpanlara Ayırma
ders: tyt-matematik
sure: 20 dk
kaynak: MEBİ Konu Özeti 1d884531b7
guncelleme: 2026-11-18
---
# Tam Kare ve İki Kare Farkı ile Çarpanlara Ayırma

<div class="giris" dir="rtl" lang="ar">

**الدرس ده عن إيه؟** عن قالبين جاهزين للتحليل (çarpanlara ayırma): المربع الكامل (tam kare) والفرق بين مربعين (iki kare farkı)، وإزاي تشوفهم جوه أي مقدار جبري.

- هتعرف تتأكد إن المقدار مربع كامل: الطرفين مربعات، والحد الأوسط ضعف حاصل ضرب جذورهم.
- هتحلل الفرق بين مربعين، وتعرف إن مجموع مربعين ما بيتحللش.
- هتستخدم القالبين في اختصار الكسور، وحساب أرقام كبيرة من دماغك زي 53 تربيع ناقص 47 تربيع.

**ليه مهم؟** القالبين دول مستخبيين في أغلب أسئلة الجبر في TYT، من اختصار الكسور لحد إيجاد قيمة مقدار من غير ما تعرف كل مجهول لوحده.

هما 20 دقيقة بس، وبعدها هتبص لأي مقدار وتلمح القالب بتاعه على طول.

</div>

**Bu dersin sonunda:** $a^2 \pm 2ab + b^2$ ve $a^2 - b^2$ kalıplarını bir ifadede tanıyıp çarpanlarına ayırabilecek, bu kalıplarla kesir sadeleştirip büyük sayılı işlemleri kafadan yapabileceksin.

> **TYT'de yeri:** Bu iki özdeşlik TYT'de hemen her cebir sorusunun içinde gizlidir: rasyonel ifade sadeleştirme, "$78^2 - 22^2$ kaçtır?" gibi pratik hesap, "ifade tam kare ise $k$ kaçtır?" ve "$a + b$ ile $ab$ verilmiş, $a^2 + b^2$ kaçtır?" kalıpları sık gelir.

## Önce hatırla

<details><summary>Ortak çarpan parantezine alma: $6x^3 - 9x^2$ ifadesini çarpanlarına ayır.</summary>
İki terimde de ortak olan sayı $3$, ortak olan en küçük kuvvet $x^2$'dir. $6x^3 - 9x^2 = 3x^2(2x - 3)$. Kontrol: parantezi dağıtınca ilk ifade geri gelir.
</details>

<details><summary>Gruplandırma: $ax - bx + ay - by$ ifadesini çarpanlarına ayır.</summary>
İlk iki terimden $x$, son iki terimden $y$ paranteze alınır: $x(a - b) + y(a - b)$. Şimdi $(a - b)$ ortak çarpandır: $(a - b)(x + y)$.
</details>

## Çarpanlara ayırma ne demek?

Bir polinomu iki ya da daha fazla polinomun **çarpımı** olarak yazmaya çarpanlara ayırma denir. $R(x) = P(x) \cdot Q(x)$ ise $P(x)$ ve $Q(x)$, $R(x)$'in çarpanlarıdır. Önceki derste ortak çarpanı paranteze aldın. Bu derste iki hazır kalıp öğreneceksin: **tam kare** ve **iki kare farkı**. Bu kalıplar çarpma işleminden geliyor; çarpanlara ayırırken onları sağdan sola okuyacaksın.

## Tam kare

**Örnek.** $(x + 5)^2$ ifadesini aç:

$$(x + 5)^2 = (x + 5)(x + 5) = x^2 + 5x + 5x + 25 = x^2 + 10x + 25$$

Ortada **iki tane** $5x$ var, yani $2 \cdot x \cdot 5$. Şimdi tersini yap: $x^2 + 10x + 25$ verilirse

1. Baş terim $x^2$, karekökü $x$. Son terim $25$, karekökü $5$.
2. Orta terim kontrolü: $2 \cdot x \cdot 5 = 10x$. Tuttu.
3. Sonuç: $x^2 + 10x + 25 = (x + 5)^2$.

Bu kalıbı bir karenin alanıyla görebilirsin: kenarı $a + b$ olan kare dört parçaya ayrılır.

![Kenarı a artı b olan bir kare dört parçaya bölünmüş: sol altta a kare, sağ üstte b kare, diğer iki köşede ab alanlı iki dikdörtgen.](gorsel/tyt-matematik/14-02-tam-kare-alan.svg "Büyük karenin alanı (a + b)². İçinde bir a², bir b² ve iki tane ab var. Orta terimdeki 2 bu iki dikdörtgenden gelir.")

**Örnek.** $9x^2 - 12x + 4$ ifadesini çarpanlarına ayır.

1. $9x^2 = (3x)^2$, $4 = 2^2$.
2. Orta terim: $2 \cdot 3x \cdot 2 = 12x$. İşareti eksi.
3. Sonuç: $9x^2 - 12x + 4 = (3x - 2)^2$.

**Kural.**

$$a^2 + 2ab + b^2 = (a + b)^2 \qquad a^2 - 2ab + b^2 = (a - b)^2$$

Baş ve son terim kare, orta terim bunların köklerinin çarpımının **2 katı** olmalı. Parantezin içindeki işaret orta terimin işaretidir.

**Eksik terimi bulmak.** "$x^2 + kx + 25$ bir tam kare ise $k$ kaçtır?" Kökler $x$ ve $5$, orta terim $\pm 2 \cdot x \cdot 5 = \pm 10x$. Yani $k = 10$ ya da $k = -10$. Soruda "$k$ pozitif" denirse $k = 10$.

> **Tuzak:** $x^2 + 6x + 16$ bir tam kare **değildir**. Uçlar kare ($x^2$ ve $4^2$) ama orta terim $2 \cdot x \cdot 4 = 8x$ olmalıydı. Tam kare demeden önce orta terimi mutlaka kontrol et.

## İki kare farkı

**Örnek.** $(x - 6)(x + 6)$ çarpımını yap:

$$(x - 6)(x + 6) = x^2 + 6x - 6x - 36 = x^2 - 36$$

Ortadaki terimler birbirini götürdü. Tersinden: $x^2 - 36$ görürsen iki karenin farkıdır, $(x - 6)(x + 6)$ diye yazarsın.

Alan modelinde: kenarı $a$ olan kareden kenarı $b$ olan kare kesilir. Kalan parçadaki şerit döndürülüp yana eklenince kenarları $a + b$ ve $a - b$ olan dikdörtgen çıkar.

![Solda kenarı a olan bir kare, sağ üst köşesinden b kare kesilmiş; kalan iki parça sağda yan yana eklenmiş: genişliği a artı b, yüksekliği a eksi b olan dikdörtgen.](gorsel/tyt-matematik/14-02-iki-kare-farki-alan.svg "Kalan alan değişmedi, yalnızca parçalar yer değiştirdi. Yeşil şeridi takip et: döndürülüp sağa eklendi.")

**Daha fazla örnek.**

| İfade | Kareler | Çarpanlar |
|---|---|---|
| $25a^2 - 4b^2$ | $(5a)^2 - (2b)^2$ | $(5a - 2b)(5a + 2b)$ |
| $(x + 2)^2 - 16$ | $(x + 2)^2 - 4^2$ | $(x - 2)(x + 6)$ |
| $x^4 - 81$ | $(x^2)^2 - 9^2$ | $(x - 3)(x + 3)(x^2 + 9)$ |

Son satırda $x^4 - 81 = (x^2 - 9)(x^2 + 9)$ çıkar; $x^2 - 9$ yine iki kare farkı olduğu için bir kez daha ayrılır. $x^2 + 9$ ise bir **toplam**, gerçek sayılarda ayrılmaz.

**Kural.**

$$a^2 - b^2 = (a - b)(a + b)$$

**Sayılarla pratik hesap.** $53^2 - 47^2 = (53 - 47)(53 + 47) = 6 \cdot 100 = 600$. Benzer şekilde $1003 \cdot 997 = (1000 + 3)(1000 - 3) = 1000000 - 9 = 999991$.

> **Tuzak:** $a^2 + b^2$ iki kare **toplamıdır**, $(a + b)(a - b)$ diye ayrılmaz. Arada eksi işareti yoksa bu kalıp kullanılamaz.

## Önce ortak çarpan, sonra kalıp

**Örnek.** $5x^3 - 20x$ ifadesini çarpanlarına ayır.

1. Ortak çarpan: $5x(x^2 - 4)$.
2. Parantez iki kare farkı: $x^2 - 4 = (x - 2)(x + 2)$.
3. Sonuç: $5x(x - 2)(x + 2)$.

**Örnek.** $2x^2 - 12x + 18 = 2(x^2 - 6x + 9) = 2(x - 3)^2$.

![Yöntem akışı: önce ortak çarpanı paranteze al; iki terim kaldıysa iki kare farkı, üç terim kaldıysa uçlar kare ve orta terim 2ab mi diye bak; sonunda çarpanları yine kontrol et.](gorsel/tyt-matematik/14-02-yontem.svg "Her soruda aynı sıra: önce ortak çarpan, sonra terim sayısına göre kalıp, en sonda çıkan çarpanları yeniden yokla.")

**Kesir sadeleştirme.** $\dfrac{x^2 - 9}{x^2 - 6x + 9}$ ifadesini sadeleştir ($x \ne 3$).

$$\frac{x^2 - 9}{x^2 - 6x + 9} = \frac{(x - 3)(x + 3)}{(x - 3)^2} = \frac{x + 3}{x - 3}$$

Sadeleştirme yalnızca **çarpanlar** arasında yapılır; önce pay ve paydayı çarpanlarına ayır.

## Değer bulma

Tam kare açılımı, bilinmeyenleri tek tek bulmadan değer hesaplatır.

**Örnek.** $a + b = 5$ ve $ab = 6$ ise $a^2 + b^2$ kaçtır?

$(a + b)^2 = a^2 + 2ab + b^2 \Rightarrow 25 = a^2 + b^2 + 12 \Rightarrow a^2 + b^2 = 13$.

**Örnek.** $a + b = 6$ ve $a - b = 2$ ise $a^2 - b^2 = 6 \cdot 2 = 12$.

**Kural.** $a^2 + b^2 = (a + b)^2 - 2ab$ ve $a^2 - b^2 = (a - b)(a + b)$.

## ÖSYM tuzakları

> **Orta terimdeki 2'yi unutmak:** $(x + 4)^2 = x^2 + 8x + 16$'dır; $x^2 + 4x + 16$ değil. Kare açarken de, tam kare tanırken de orta terim $2ab$'dir.

> **Kareyi dağıtmak:** $(a + b)^2 \ne a^2 + b^2$. Aradaki $2ab$ unutulursa $a^2 + b^2$ sorularında yanlış sonuç bulunur.

> **İki kare toplamını ayırmaya çalışmak:** $x^2 + 9$ gerçek sayılarda çarpanlarına ayrılmaz. $x^4 - 81$ gibi sorularda son çarpan $x^2 + 9$ olarak kalır.

> **İşi yarıda bırakmak:** $3x^3 - 27x = 3x(x^2 - 9)$ yazıp durma; $x^2 - 9$ yine ayrılır: $3x(x - 3)(x + 3)$.

> **İşaret:** $(x - 3)^2 = (3 - x)^2$'dir, çünkü kare işareti siler. Ama $x - 3 \ne 3 - x$; sadeleştirirken bu fark $-1$ çarpanı doğurur.

## Kendini dene

### Soru 1
$16x^2 - 24x + 9$ ifadesinin çarpanlarına ayrılmış biçimi aşağıdakilerden hangisidir?

A) $(4x + 3)^2$
B) $(8x - 3)^2$
C) $(4x - 3)(4x + 3)$
D) $(4x - 3)^2$
E) $(4x - 9)^2$

**Cevap:** D
**Çözüm:** $16x^2 = (4x)^2$, $9 = 3^2$. Orta terim kontrolü: $2 \cdot 4x \cdot 3 = 24x$, işareti eksi. Sonuç $(4x - 3)^2$. C seçeneği $16x^2 - 9$ eder; A seçeneğinde orta terim artı olur.

### Soru 2
$78^2 - 22^2$ işleminin sonucu kaçtır?

A) 2800
B) 3136
C) 5600
D) 6568
E) 10000

**Cevap:** C
**Çözüm:** İki kare farkı: $(78 - 22)(78 + 22) = 56 \cdot 100 = 5600$. $3136 = 56^2$, farkın karesini almaktan gelir; $6568$ kareleri toplamak, $10000 = 100^2$ ise toplamın karesidir.

### Soru 3
$x^2 + kx + 25$ ifadesi bir tam kare ve $k < 0$ olduğuna göre $k$ kaçtır?

A) $-25$
B) $-10$
C) $-5$
D) $5$
E) $10$

**Cevap:** B
**Çözüm:** Uçların kökleri $x$ ve $5$. Tam kare olması için orta terim $\pm 2 \cdot x \cdot 5 = \pm 10x$ olmalı. $k < 0$ olduğundan $k = -10$; ifade $(x - 5)^2$ olur. $-5$ seçeneği orta terimdeki 2'yi unutmaktır.

## Özet kartı

- $a^2 + 2ab + b^2 = (a + b)^2$ ve $a^2 - 2ab + b^2 = (a - b)^2$.
- Tam kare için uçlar kare, orta terim köklerin çarpımının 2 katı olmalı.
- $a^2 - b^2 = (a - b)(a + b)$; $a^2 + b^2$ ayrılmaz.
- Sıra: önce ortak çarpan, sonra kalıp, sonra çarpanları yeniden kontrol.
- Sayılarda: $53^2 - 47^2 = 6 \cdot 100$ gibi kafadan hesap.
- $a^2 + b^2 = (a + b)^2 - 2ab$.

## Sonraki adım

Alıştırmaya geç (aşağıdaki düğme). Sonraki ders **Tam Küp, İki Küp Toplamı veya Farkı ile Çarpanlara Ayırma**; bu dersteki kalıpların küplü benzerlerini göreceksin.
