---
baslik: Mutlak Değer Kavramı ve Özellikleri
ders: tyt-matematik
sure: 20 dk
kaynak: MEBİ Konu Özeti 37851bfa74
guncelleme: 2026-11-17
---
# Mutlak Değer Kavramı ve Özellikleri

**Bu dersin sonunda:** içinin işaretine bakarak mutlak değeri açabilecek, mutlak değerin özellikleriyle ifadeleri sadeleştirebilecek ve $|x - a| + |x - b|$ gibi ifadelerin en küçük değerini kritik noktalarla bulabileceksin.

> **TYT'de yeri:** Mutlak değer neredeyse her TYT'de vardır. En sık kalıplar: "$a < 0 < b$ olduğuna göre … ifadesinin eşiti", sayı doğrusunda yeri verilen harflerle işlem, $\sqrt{x^2}$ içeren sadeleştirme ve "ifadenin alabileceği en küçük değer". Hatanın neredeyse tamamı tek yerden gelir: içinin işaretini kontrol etmeden mutlak değeri açmak.

## Önce hatırla

<details><summary>Eşitsizlik sistemlerinden: $x \ge 0$, $y \ge 0$ ve $x + y \le 4$ sisteminin çözüm bölgesi hangi şekildir, alanı kaç birimkaredir?</summary>
Sistemin çözümü, üç eşitsizliğin bölgelerinin <b>kesişimidir</b>. $x \ge 0$ ve $y \ge 0$ birinci bölgeyi verir; $x + y \le 4$ ise $(4, 0)$ ve $(0, 4)$ noktalarından geçen doğrunun altında kalır. Kesişim köşeleri $(0, 0)$, $(4, 0)$, $(0, 4)$ olan dik üçgendir. Alan $\frac{4 \cdot 4}{2} = $ <b>8</b>.
</details>

<details><summary>Eşitsizlik sistemlerinden: $(1, 1)$ noktası $x - y < 2$ ve $2x + y \ge 4$ sisteminin çözüm kümesinde midir?</summary>
Nokta <b>iki</b> eşitsizliği de sağlamalı. $1 - 1 = 0 < 2$ doğru; ama $2 \cdot 1 + 1 = 3 \ge 4$ yanlış. Bir tanesini sağlamadığı için nokta çözüm kümesinde <b>değildir</b>.
</details>

## Mutlak değer: sıfıra uzaklık

**Örnek.** $-5$ sayısı sayı doğrusunda $0$'dan kaç birim uzaktadır? $5$ birim. $2$ sayısı ise $2$ birim uzaktadır. Uzaklık hiçbir zaman negatif olmaz; bu yüzden $|-5| = 5$ ve $|2| = 2$ yazarız.

Bir gerçek sayının sayı doğrusunda **sıfıra olan uzaklığına** o sayının **mutlak değeri** denir ve $|x|$ ile gösterilir. Aynı fikirle, $a$ ile $b$ arasındaki uzaklık $|a - b|$ olur: $-2$ ile $4$ arası $|-2 - 4| = |-6| = 6$ birimdir. Sırayı değiştirsen de sonuç aynıdır: $|4 - (-2)| = 6$.

![İki sayı doğrusu. Üstte eksi 5'ten 0'a 5 birimlik, 0'dan 2'ye 2 birimlik ok. Altta eksi 2'den 4'e 6 birimlik ok.](gorsel/tyt-matematik/03-07-uzaklik.svg "Mutlak değer bir uzaklıktır: negatif sayının da mutlak değeri pozitiftir. İki sayı arasındaki uzaklık, farklarının mutlak değeridir.")

**Kural (tanım).**

$$|x| = \begin{cases} x, & x \ge 0 \\ -x, & x < 0 \end{cases}$$

Burada $-x$ negatif bir sayı **değildir**: $x = -7$ ise $-x = 7$. "Eksi koymak" negatif sayıyı pozitife çevirir. Tanımdan şunlar çıkar:

- $|x| \ge 0$; $|x| = 0$ yalnızca $x = 0$ iken.
- $|x| \ge x$ (mutlak değer sayının kendisinden küçük olamaz).
- $|x| = x$ ise $x \ge 0$; $|x| = -x$ ise $x \le 0$.

**Örnek.** $|x - 4| = 4 - x$ ise $x$ en çok kaç olabilir? $|x - 4| = -(x - 4)$ demek, içinin sıfır ya da negatif olması demektir: $x - 4 \le 0$, yani $x \le 4$. En büyük değer **4**.

## Mutlak değeri açmak: önce içinin işareti

Mutlak değeri açarken tek soru sorulur: **İçi sıfır ya da pozitif mi?**

![Akış şeması: mutlak değerli ifade, içinin işaretini bul, içi sıfır ya da pozitif mi? Evetse olduğu gibi çıkar, hayırsa başına eksi koyup çıkar, sonra sadeleştir.](gorsel/tyt-matematik/03-07-yontem.svg "Her mutlak değer için ayrı ayrı bu yolu izle. İçi negatifse ifadenin tamamı parantez içine alınıp önüne eksi konur.")

**Örnek 1.** $a < 0 < b$ olduğuna göre $|a| - |b| + |a - b|$ ifadesinin eşiti nedir?

- $a < 0$: $|a| = -a$.
- $b > 0$: $|b| = b$.
- $a - b$: negatiften pozitif çıkıyor, sonuç negatif. $|a - b| = -(a - b) = b - a$.

$$|a| - |b| + |a - b| = -a - b + b - a = -2a$$

Sayıyla kontrol: $a = -1$, $b = 3$ için $1 - 3 + 4 = 2$ ve $-2a = 2$.

**Örnek 2 (köklü sayılar).** $|1 - \sqrt{3}| + |\sqrt{3} - 2|$ kaçtır?

$\sqrt{3} \approx 1{,}73$. Buna göre $1 - \sqrt{3} < 0$ ve $\sqrt{3} - 2 < 0$. İkisi de ters çevrilir:

$$(\sqrt{3} - 1) + (2 - \sqrt{3}) = 1$$

**Örnek 3 (iç içe).** $a < 0$ ise $\big|2a - |3a|\big|$ nedir? **İçten dışa** aç: $3a < 0$ olduğundan $|3a| = -3a$. Böylece $|2a - (-3a)| = |5a|$. $5a < 0$ olduğu için $|5a| = -5a$.

**Kural.** İçi $\ge 0$ ise mutlak değer kaldırılır; içi $< 0$ ise ifade ters işaretlisiyle yazılır. İç içe mutlak değerlerde en içteki önce açılır.

## Mutlak değerin özellikleri

**Örnek.** $|(-3) \cdot 4| = |-12| = 12$ ve $|-3| \cdot |4| = 3 \cdot 4 = 12$. Çarpımın mutlak değeri, mutlak değerlerin çarpımına eşittir. Ama toplamda böyle değil: $|4 + (-6)| = 2$ iken $|4| + |-6| = 10$.

| Özellik | Örnek |
|---|---|
| $\lvert x \cdot y \rvert = \lvert x \rvert \cdot \lvert y \rvert$ | $\lvert -2 \cdot 5 \rvert = 2 \cdot 5 = 10$ |
| $\left\lvert \frac{x}{y} \right\rvert = \frac{\lvert x \rvert}{\lvert y \rvert}$, $y \ne 0$ | $\left\lvert \frac{-12}{3} \right\rvert = \frac{12}{3} = 4$ |
| $\lvert -x \rvert = \lvert x \rvert$, yani $\lvert a - b \rvert = \lvert b - a \rvert$ | $\lvert 2 - 7 \rvert = \lvert 7 - 2 \rvert = 5$ |
| $\lvert x^n \rvert = \lvert x \rvert^n$ ($n$ pozitif tam sayı) | $\lvert (-2)^3 \rvert = 2^3 = 8$ |
| $\lvert x + y \rvert \le \lvert x \rvert + \lvert y \rvert$ | $\lvert 4 + (-6) \rvert = 2 \le 10$ |

Son özellikte eşitlik, $x$ ile $y$ **aynı işaretliyse** (ya da biri $0$ ise) olur; zıt işaretliyse toplam küçülür.

**Kök ile mutlak değer.** $\sqrt{(-5)^2} = \sqrt{25} = 5$; sonuç $-5$ değildir. Karekök hiçbir zaman negatif çıkmaz, bu yüzden:

$$\sqrt{x^2} = |x|$$

**Örnek.** $x < 3$ olduğuna göre $\sqrt{(x - 3)^2} + x$ kaçtır? $\sqrt{(x - 3)^2} = |x - 3|$. $x - 3 < 0$ olduğundan $|x - 3| = 3 - x$. Sonuç $3 - x + x = 3$.

**Kural.** Çarpım, bölüm ve kuvvette mutlak değer parçalara dağıtılabilir; **toplam ve farkta dağıtılamaz.** $\sqrt{x^2}$ gördüğünde $|x|$ yaz, sonra işarete bak.

## Kritik nokta ve en küçük değer

Mutlak değerin içini sıfır yapan $x$ değerine **kritik nokta** denir: $|x - 3|$ için kritik nokta $3$, $|2x + 6|$ için $-3$'tür.

**Örnek 1.** $|x - 3| + 2$ en az kaçtır? $|x - 3| \ge 0$ olduğu için ifade en az $2$ olur; bu değer kritik noktada, $x = 3$ iken alınır.

**Örnek 2.** $|x + 1| + |x - 2|$ en az kaçtır? $|x + 1| = |x - (-1)|$, $x$'in $-1$'e uzaklığıdır; $|x - 2|$ ise $2$'ye uzaklığı. Yani bu ifade, $x$'in iki noktaya uzaklıkları toplamıdır.

![İki sayı doğrusu. Eksi 1 ile 2 arası yeşil. Üstte x = 0,5 için uzaklıklar 1,5 ve 1,5, toplam 3. Altta x = 3,5 için uzaklıklar 4,5 ve 1,5, toplam 6.](gorsel/tyt-matematik/03-07-iki-uzaklik.svg "x iki noktanın arasındayken uzaklıklar toplamı hep iki nokta arasındaki uzaklığa, 3'e eşittir. Dışarı çıkınca fazladan yol eklenir.")

$x$, $-1$ ile $2$ arasındaysa toplam her zaman $2 - (-1) = 3$; dışarıdaysa daha büyük. En küçük değer **3**'tür ve $-1 \le x \le 2$ olan **her** $x$ için alınır.

**Örnek 3.** $|x + 2| + |x| + |x - 3|$ en az kaçtır? Kritik noktalar $-2$, $0$, $3$. Her birini dene:

| $x$ | $\lvert x + 2 \rvert + \lvert x \rvert + \lvert x - 3 \rvert$ |
|---|---|
| $-2$ | $0 + 2 + 5 = 7$ |
| $0$ | $2 + 0 + 3 = 5$ |
| $3$ | $5 + 3 + 0 = 8$ |

En küçüğü **5** ($x = 0$).

![y eşittir mutlak x artı 2 artı mutlak x artı mutlak x eksi 3 grafiği: kırık çizgi, kritik noktalarda kırılıyor; x = −2'de 7, x = 0'da en küçük değer 5, x = 3'te 8.](gorsel/tyt-matematik/03-07-kritik-grafik.svg "Grafik yalnızca kritik noktalarda kırılır, aralarda düz çizgidir. Bu yüzden en küçük değer bir kritik noktada çıkar.")

**Kural.** Mutlak değerlerin toplamı olan ifadenin en küçük değeri bir kritik noktada alınır: bütün kritik noktaları dene, en küçük sonucu seç. İki terimde kısa yol: $|x - a| + |x - b|$ ifadesinin en küçük değeri $|a - b|$'dir.

## ÖSYM tuzakları

> **$-x$'i negatif sanmak:** $x < 0$ iken $|x| = -x$ yazmak doğrudur; $-x$ burada pozitif bir sayıdır. "Mutlak değer negatif olamaz, o hâlde $-x$ yazılmaz" diye düşünüp $|x| = x$ yazma.

> **Toplamı dağıtmak:** $|a - b| = |a| - |b|$ ve $|a + b| = |a| + |b|$ genelde yanlıştır. $|2 - 7| = 5$, ama $|2| - |7| = -5$.

> **$\sqrt{x^2} = x$ yazmak:** $\sqrt{x^2} = |x|$'tir. $x$ negatifse sonuç $-x$ olur.

> **İçinin işaretini tahminle bulmak:** $a < 0 < b$ verildiğinde $a + b$'nin işareti **belli değildir**; $|a|$ ile $|b|$'nin hangisinin büyük olduğuna (sayı doğrusundaki yerlerine) bakmadan açma.

> **Değer ile yeri karıştırmak:** "$|x + 1| + |x - 2|$ ifadesinin en küçük değeri" $3$'tür; bu değer bir tek $x$ için değil, $[-1, 2]$ aralığındaki her $x$ için alınır. Soru kökü hangisini soruyor, oku.

## Kendini dene

### Soru 1
$|-6| + |4 - 9| - |-2| \cdot |3|$ işleminin sonucu kaçtır?

A) $-5$
B) $5$
C) $7$
D) $11$
E) $17$

**Cevap:** B
**Çözüm:** $|-6| = 6$, $|4 - 9| = |-5| = 5$, $|-2| \cdot |3| = 2 \cdot 3 = 6$. Sonuç $6 + 5 - 6 = 5$. $|4 - 9|$'u $-5$ alan $-5$; $|-2| \cdot |3|$'ü $-6$ alan $17$ bulur.

### Soru 2
$x < 0 < y$ olduğuna göre $|x - y| + |x| - |y|$ ifadesinin eşiti aşağıdakilerden hangisidir?

A) $-2x$
B) $2y$
C) $0$
D) $2x$
E) $-2y$

**Cevap:** A
**Çözüm:** $x - y < 0$ olduğundan $|x - y| = y - x$; $|x| = -x$; $|y| = y$. Toplam: $y - x - x - y = -2x$. $|x - y|$'yi $x - y$ diye açan $-2y$; $|x|$'i $x$ diye açan $0$ bulur.

### Soru 3
$|x - 5| + |x + 1|$ ifadesinin alabileceği en küçük değer kaçtır?

A) $4$
B) $5$
C) $6$
D) $7$
E) $10$

**Cevap:** C
**Çözüm:** İfade, $x$'in $5$'e ve $-1$'e uzaklıkları toplamıdır. $x$ bu iki nokta arasındayken toplam, iki nokta arasındaki uzaklığa eşittir: $|5 - (-1)| = 6$. Kritik noktalarla kontrol: $x = 5$ için $0 + 6 = 6$, $x = -1$ için $6 + 0 = 6$. $4$ cevabı $5 - 1$ işleminden, $7$ ise aralıktaki tam sayıları saymaktan gelir.

## Özet kartı

- $|x|$, $x$'in sıfıra uzaklığıdır; $|a - b|$, $a$ ile $b$ arasındaki uzaklıktır. Mutlak değer hiçbir zaman negatif değildir.
- İçi $\ge 0$ ise olduğu gibi çıkar, içi $< 0$ ise başına eksi koy. Her mutlak değere ayrı bak.
- $|xy| = |x||y|$, $\left|\frac{x}{y}\right| = \frac{|x|}{|y|}$, $|x^n| = |x|^n$; ama $|x + y| \le |x| + |y|$.
- $\sqrt{x^2} = |x|$ ve $|a - b| = |b - a|$.
- Mutlak değerli toplamın en küçük değeri bir kritik noktadadır; $|x - a| + |x - b|$ en az $|a - b|$ olur.

## Sonraki adım

Alıştırmaya geç (aşağıdaki düğme). Sonraki ders **Mutlak Değerli Denklemler ve Eşitsizlikler**; orada $|x - 2| = 5$ ya da $|x + 1| < 3$ gibi ifadeleri bu dersteki "uzaklık" fikriyle çözeceksin.
