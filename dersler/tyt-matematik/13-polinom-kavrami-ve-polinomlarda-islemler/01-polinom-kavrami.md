---
baslik: Polinom Kavramı
ders: tyt-matematik
sure: 20 dk
kaynak: MEBİ Konu Özeti b24c173fec
guncelleme: 2026-11-17
---
# Polinom Kavramı

**Bu dersin sonunda:** bir ifadenin polinom olup olmadığını söyleyebilecek, derece, baş katsayı ve sabit terimi bulabilecek, $P(1)$, $P(0)$ ve $P(-1)$ ile katsayı toplamlarını hesaplayabilecek ve eşit polinomlarda bilinmeyen katsayıları bulabileceksin.

> **TYT'de yeri:** Polinom sorularının çoğu bu dersteki birkaç fikre dayanır: "Bu ifade polinom ise $n$ kaç farklı değer alır?", "$P(x+2)$ verilmiş, $P(x)$'in katsayılar toplamı kaçtır?", "Sabit polinomsa $P(2025)$ kaçtır?", "İki polinom eşitse $a + b$ kaçtır?" Hesap azdır; doğru yere doğru sayıyı yazmak önemlidir.

## Önce hatırla

<details><summary>Fonksiyon grafiklerinden: Doğrusal bir f fonksiyonunun grafiği (0, 4) ve (2, 10) noktalarından geçiyor. f(5) kaçtır?</summary>
Eğim $m = \frac{10 - 4}{2 - 0} = 3$, $y$ eksenini kestiği yer $4$. Kural $f(x) = 3x + 4$, bu yüzden $f(5) = 15 + 4 = $ <b>19</b>.
</details>

<details><summary>Doğrusal hikâyelerden: 20 cm boyundaki bir mum her saat 2,5 cm kısalıyor. Mumun boyu kaç saat sonra 5 cm olur?</summary>
Boy $h(t) = 20 - 2{,}5t$. $20 - 2{,}5t = 5$ ise $2{,}5t = 15$, $t = $ <b>6 saat</b>. Burada bağımsız değişken zaman, bağımlı değişken mumun boyudur.
</details>

## Polinom nedir?

**Örnek.** Aşağıdaki ifadelerden hangileri polinomdur?

| İfade | Üsleri yaz | Polinom mu? |
|---|---|---|
| $2x^3 - 5x + 1$ | $x^3, x^1, x^0$ | Evet |
| $\sqrt{3}\,x^2 + \frac{x}{2}$ | $x^2, x^1$ | Evet (katsayılar $\sqrt{3}$ ve $\frac{1}{2}$) |
| $7$ | $7 = 7x^0$ | Evet |
| $x^2 + \frac{1}{x}$ | $\frac{1}{x} = x^{-1}$ | Hayır |
| $\sqrt{x} + 4$ | $\sqrt{x} = x^{\frac{1}{2}}$ | Hayır |

Her terimi $a \cdot x^k$ biçimine getirip yalnızca **üsse** baktık. Katsayı kesir ya da köklü sayı olabilir; üs ise $0, 1, 2, 3, \dots$ olmak zorunda.

**Kural.** $n$ bir doğal sayı ve $a_n, a_{n-1}, \dots, a_1, a_0$ gerçek sayılar olmak üzere

$$P(x) = a_n x^n + a_{n-1} x^{n-1} + \dots + a_1 x + a_0$$

biçimindeki ifadeye **polinom (çok terimli)** denir. $a_n, \dots, a_0$ sayıları polinomun **katsayılarıdır**. Polinomlar $P(x)$, $Q(x)$, $R(x)$ gibi harflerle gösterilir.

![Akış şeması: her terimi ayrı incele; x'in üssü doğal sayı mı diye sor; hepsinde evetse polinom, biri bile değilse polinom değil; polinomda katsayı kesir ya da kök olabilir.](gorsel/tyt-matematik/13-01-polinom-mu.svg "Karar yalnızca x'in üssüne bakılarak verilir. Tek bir terimin üssü negatif ya da kesirliyse ifade polinom olmaz.")

**Örnek (parametreli).** $P(x) = x^{\frac{12}{n}} + 3x^{n-2} - 5$ bir polinom ise $n$'nin alabileceği değerlerin toplamı kaçtır?

1. $n - 2$ doğal sayı olmalı: $n \ge 2$ ve $n$ tam sayı.
2. $\frac{12}{n}$ doğal sayı olmalı: $n$, 12'nin pozitif böleni.
3. İkisi birlikte: $n \in \{2, 3, 4, 6, 12\}$.

Toplam $2 + 3 + 4 + 6 + 12 = 27$. Dikkat: $n = 2$ için $3x^0 = 3$ olur; bu bir sabit terimdir ve sorun çıkarmaz.

## Derece, baş katsayı, sabit terim

**Örnek.** $P(x) = 4x^2 - 7x^5 + 3 - x$ polinomunu inceleyelim. Önce üslere göre büyükten küçüğe diz:

$$P(x) = -7x^5 + 4x^2 - x + 3$$

![P(x) eşittir eksi 7 x üzeri 5 artı 4 x kare eksi x artı 3 ifadesi; eksi 7 kutu içinde baş katsayı, 5 üssü derece, 3 sabit terim olarak işaretli; toplam 4 terim.](gorsel/tyt-matematik/13-01-polinom-parcalari.svg "Baş katsayı en büyük üslü terimin katsayısıdır ve işaretiyle birlikte alınır: burada 7 değil −7.")

| Kavram | Tanım | Bu örnekte |
|---|---|---|
| Derece, $\text{der}[P(x)]$ | $x$'in en büyük üssü | $5$ |
| Baş katsayı | En büyük dereceli terimin katsayısı | $-7$ |
| Sabit terim | $x$ içermeyen terim ($a_0$) | $3$ |
| Terim sayısı | Katsayısı sıfır olmayan terim sayısı | $4$ |

**Örnek (parametreli).** $P(x) = (a - 2)x^3 + (b + 1)x^2 + 4x - 1$ polinomu ikinci dereceden ve baş katsayısı $5$ ise $a + b$ kaçtır?

İkinci dereceden olduğu için $x^3$ terimi yok olmalı: $a - 2 = 0$, $a = 2$. Baş katsayı artık $x^2$'nin katsayısı: $b + 1 = 5$, $b = 4$. Sonuç $a + b = 6$.

**Kural.** Derece istenen sayıdan büyük üslü terimlerin katsayıları $0$ olur; derecedeki terimin katsayısı $0$ olamaz, o baş katsayıdır.

## Katsayılar toplamı ve sabit terim

**Örnek.** $P(x) = 2x^3 - 5x^2 + x + 4$ olsun.

- $x = 1$ yazınca her $x^k$ terimi $1$ olur, geriye katsayılar kalır: $P(1) = 2 - 5 + 1 + 4 = 2$. Bu, **katsayılar toplamıdır**.
- $x = 0$ yazınca $x$ içeren her terim silinir: $P(0) = 4$. Bu, **sabit terimdir**.
- $x = -1$ yazınca tek dereceli terimlerin işareti değişir, çift derecelilerinki değişmez: $P(-1) = -2 - 5 - 1 + 4 = -4$.

![Tablo: 2x küp, eksi 5x kare, x ve 4 terimleri; x eşittir 1 satırında 2, eksi 5, 1, 4 ve toplam 2; x eşittir eksi 1 satırında eksi 2, eksi 5, eksi 1, 4 ve toplam eksi 4. Tek dereceli sütunlar kırmızı, çift dereceliler yeşil.](gorsel/tyt-matematik/13-01-bir-eksi-bir.svg "Yeşil sütunlar (çift derece, sabit terim dahil) iki satırda aynı; kırmızı sütunlar (tek derece) işaret değiştirir.")

$P(1)$ ile $P(-1)$ toplanınca tek dereceliler birbirini götürür, çift dereceliler iki kez sayılır:

- Çift dereceli terimlerin katsayıları toplamı: $\dfrac{P(1) + P(-1)}{2} = \dfrac{2 + (-4)}{2} = -1$. Kontrol: $-5 + 4 = -1$.
- Tek dereceli terimlerin katsayıları toplamı: $\dfrac{P(1) - P(-1)}{2} = \dfrac{2 - (-4)}{2} = 3$. Kontrol: $2 + 1 = 3$.

**Kural.**

| İstenen | Yap |
|---|---|
| Katsayılar toplamı | $P(1)$ |
| Sabit terim | $P(0)$ |
| Çift dereceli terimlerin katsayıları toplamı | $\frac{P(1) + P(-1)}{2}$ |
| Tek dereceli terimlerin katsayıları toplamı | $\frac{P(1) - P(-1)}{2}$ |

Sabit terim $a_0 x^0$ olduğu için **çift dereceli** sayılır.

**Örnek (içi değişmiş polinom).** $P(x - 2) = x^2 + 3x - 1$ ise $P(x)$'in katsayılar toplamı ve sabit terimi kaçtır?

Katsayılar toplamı $P(1)$'dir. Parantezin içi $1$ olmalı: $x - 2 = 1$, yani $x = 3$ yazılır.
$$P(1) = 3^2 + 3 \cdot 3 - 1 = 17$$
Sabit terim $P(0)$'dır. $x - 2 = 0$, yani $x = 2$ yazılır.
$$P(0) = 2^2 + 3 \cdot 2 - 1 = 9$$

**Kural.** $P(\text{içi})$ verilmişse, istenen değeri bulmak için önce **içi istenen sayıya eşitle**, çıkan $x$'i sağ tarafa yaz.

## Sabit polinom ve sıfır polinomu

**Örnek.** $P(x) = (a - 4)x^2 + (b + 1)x + 6$ bir sabit polinom ise $P(10)$ kaçtır?

Sabit polinomda $x$ içeren terim kalmaz: $a - 4 = 0$ ve $b + 1 = 0$. Geriye $P(x) = 6$ kalır. $x$ yerine ne yazarsan yaz sonuç aynı: $P(10) = 6$.

| Polinom | Örnek | Derece |
|---|---|---|
| Sabit polinom | $P(x) = c$, $c \ne 0$ | $0$ |
| Sıfır polinomu | $P(x) = 0$ | Belirsiz (tanımsız) |

**Kural.** $P(x) = c$ ve $c \ne 0$ ise derece $0$'dır. Bütün katsayıları sıfır olan $P(x) = 0$ polinomunun derecesi belirsizdir.

## Eşit polinomlar

**Örnek.** $(a + 1)x^2 + 3x + c = 4x^2 + (b - 2)x - 5$ ise $a + b + c$ kaçtır?

Aynı dereceli terimlerin katsayıları eşleşir.

![İki polinom alt alta; a artı 1 x kare ile 4 x kare, 3x ile b eksi 2 x, c ile eksi 5 oklarla eşleştirilmiş. Altında a artı 1 eşittir 4, 3 eşittir b eksi 2, c eşittir eksi 5 yazıyor.](gorsel/tyt-matematik/13-01-esit-polinom.svg "Aynı renkteki katsayılar aynı dereceli terimlerindir; her eşleşme bir denklem verir.")

$a + 1 = 4 \Rightarrow a = 3$, $\quad b - 2 = 3 \Rightarrow b = 5$, $\quad c = -5$. Sonuç $a + b + c = 3$.

**Kural.** İki polinom eşitse dereceleri aynıdır ve aynı dereceli terimlerin katsayıları karşılıklı eşittir. Bir tarafta olmayan terimin katsayısı $0$ kabul edilir.

**Kısa yol: uygun $x$ yazmak.** "Her $x$ için" $a(x - 1) + b(x + 2) = 5x + 1$ ise $a$ ve $b$ kaçtır?

Eşitlik her $x$ için doğru olduğundan parantezlerden birini sıfır yapan değerleri seç:
- $x = 1$: $a \cdot 0 + b \cdot 3 = 6$, yani $b = 2$.
- $x = -2$: $a \cdot (-3) + b \cdot 0 = -9$, yani $a = 3$.

Kontrol: $3(x - 1) + 2(x + 2) = 5x + 1$.

## ÖSYM tuzakları

> **Katsayıya bakıp karar vermek:** $\sqrt{2}\,x^3 + \frac{x}{5}$ polinomdur; kök ve kesir katsayıdadır. Polinomu bozan $\sqrt{x}$, $\frac{1}{x}$, $x^{-2}$ gibi **üssü** doğal sayı olmayan terimlerdir.

> **Baş katsayıyı ilk yazılan terimden almak:** $3x^2 - 7x^5 + 1$ polinomunun baş katsayısı $3$ değil $-7$'dir. Önce üslere göre diz, işareti de al.

> **$P(x - 2)$'de $x = 1$ yazmak:** Bu $P(-1)$'i verir, katsayılar toplamını değil. Katsayılar toplamı için **içi** $1$ yap: $x - 2 = 1$, $x = 3$.

> **Sabit terimi tek dereceli saymak:** $a_0 = a_0 x^0$ ve $0$ çift sayıdır. Çift dereceli katsayılar toplamına sabit terim de girer.

> **Sabit polinom ile sıfır polinomunu karıştırmak:** $P(x) = 6$ polinomunun derecesi $0$'dır; $P(x) = 0$ polinomunun derecesi belirsizdir.

> **Üssün $0$ olabileceğini unutmak:** Doğal sayılar $0$'dan başlar. $x^{n-2}$ teriminde $n - 2 = 0$, yani $n = 2$ olabilir; terim sabit sayı olur.

## Kendini dene

### Soru 1
Aşağıdakilerden hangisi bir polinomdur?

A) $x^2 + \frac{2}{x}$
B) $\sqrt{x} - 3x$
C) $\sqrt{5}\,x^3 - \frac{x}{4}$
D) $x^{-2} + 1$
E) $x^{\frac{3}{2}} + x$

**Cevap:** C
**Çözüm:** Üslere bak. A'da $\frac{2}{x} = 2x^{-1}$, B'de $\sqrt{x} = x^{\frac{1}{2}}$, D'de $x^{-2}$, E'de $x^{\frac{3}{2}}$ var; hiçbirinin üssü doğal sayı değil. C'de üsler $3$ ve $1$; $\sqrt{5}$ ve $-\frac{1}{4}$ yalnızca katsayıdır. Polinom C'dir.

### Soru 2
$P(x) = 3x^4 - x^5 + 2x - 6$ polinomunun derecesi ile baş katsayısının toplamı kaçtır?

A) 2
B) 4
C) 6
D) 7
E) 8

**Cevap:** B
**Çözüm:** Sırala: $P(x) = -x^5 + 3x^4 + 2x - 6$. Derece $5$, baş katsayı $-1$. Toplam $5 + (-1) = 4$. İlk yazılan terimi ($3x^4$) alan $4 + 3 = 7$, işareti unutan $5 + 1 = 6$, derece 5 ile ilk katsayı 3'ü toplayan $8$ bulur.

### Soru 3
$P(x + 1) = x^3 - 2x + 5$ olduğuna göre $P(x)$ polinomunun katsayılar toplamı ile sabit teriminin toplamı kaçtır?

A) 6
B) 9
C) 10
D) 11
E) 12

**Cevap:** D
**Çözüm:** Katsayılar toplamı $P(1)$: $x + 1 = 1$, $x = 0$; $P(1) = 0 - 0 + 5 = 5$. Sabit terim $P(0)$: $x + 1 = 0$, $x = -1$; $P(0) = -1 + 2 + 5 = 6$. Toplam $5 + 6 = 11$. Sağ tarafa doğrudan $x = 1$ ve $x = 0$ yazan $4 + 5 = 9$ bulur.

## Özet kartı

- Polinomda $x$'in bütün üsleri doğal sayıdır ($0, 1, 2, \dots$); katsayı herhangi bir gerçek sayı olabilir.
- Derece en büyük üs; baş katsayı o terimin katsayısı (işaretiyle); sabit terim $P(0)$.
- Katsayılar toplamı $P(1)$; çift derecelilerin toplamı $\frac{P(1) + P(-1)}{2}$, tek derecelilerin $\frac{P(1) - P(-1)}{2}$.
- $P(\text{içi})$ verilmişse içi istenen sayıya eşitle, çıkan $x$'i yaz.
- Sabit polinom $P(x) = c \ne 0$: derece $0$. Sıfır polinomu: derece belirsiz.
- Eşit polinomlarda aynı dereceli katsayılar eşittir; "her $x$ için" eşitlikte işe yarayan $x$ değerleri yazılabilir.

## Sonraki adım

Alıştırmaya geç (aşağıdaki düğme). Sonraki ders **Polinomlarda Toplama, Çıkarma ve Çarpma İşlemleri**; orada derece ve baş katsayının işlemlerle nasıl değiştiğini göreceksin.
