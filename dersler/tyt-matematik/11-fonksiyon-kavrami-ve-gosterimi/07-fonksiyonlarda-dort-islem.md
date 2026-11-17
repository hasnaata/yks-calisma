---
baslik: Fonksiyonlarda Dört İşlem
ders: tyt-matematik
sure: 20 dk
kaynak: MEBİ Konu Özeti 4e05a4ffc0
guncelleme: 2026-11-17
---
# Fonksiyonlarda Dört İşlem

**Bu dersin sonunda:** iki fonksiyonun toplamını, farkını, çarpımını, bölümünü ve bir fonksiyonun sabitle çarpımını kuraldan, listeden ya da grafikten hesaplayabilecek, bu yeni fonksiyonların tanım kümesini doğru belirleyebileceksin.

> **TYT'de yeri:** "$(f + g)(2)$ kaçtır?", "$(3f - 2g)(1)$ kaçtır?" gibi doğrudan hesaplar; $(f + g)(x)$ ve $(f - g)(x)$ verilip $f(x)$'in istenmesi; $\frac{f}{g}$ fonksiyonunun tanım kümesi; grafikten ya da tablodan değer okuyup işlem yapma. Sorular kısa ama tuzaklıdır: parantez, ortak tanım kümesi ve paydayı sıfır yapan değer.

## Önce hatırla

<details><summary>Tek-çift fonksiyonlardan: $f(x) = (a - 2)x^3 + 4x^2 + (b + 1)x + 5$ çift fonksiyon ise $a + b$ kaçtır?</summary>
Çift fonksiyonun kuralında yalnızca çift dereceli terimler bulunur; tek dereceli terimlerin katsayısı $0$ olmalı: $a - 2 = 0$, $a = 2$ ve $b + 1 = 0$, $b = -1$. $a + b = 1$.
</details>

<details><summary>Tek-çift fonksiyonlardan: $f\colon \mathbb{R} \to \mathbb{R}$ tek fonksiyon ve $f(3) = 5$ ise $f(-3) + f(0)$ kaçtır?</summary>
Tek fonksiyonda $f(-x) = -f(x)$: $f(-3) = -5$. $x = 0$ yazınca $f(0) = -f(0)$, yani $f(0) = 0$. Toplam $-5$.
</details>

## Toplama ve çıkarma

**Örnek.** $f, g\colon \mathbb{R} \to \mathbb{R}$, $f(x) = x^2 + 1$ ve $g(x) = 3x - 2$ olsun.

İki fonksiyonun toplamı, **aynı $x$** için iki değerin toplamıdır:

$$(f + g)(x) = f(x) + g(x) = x^2 + 1 + 3x - 2 = x^2 + 3x - 1$$

$(f + g)(2) = 4 + 6 - 1 = 9$. Kuralı yazmadan da olur: $f(2) = 5$, $g(2) = 4$, toplam $9$.

Farkta $g(x)$'in **tamamı** çıkarılır, bu yüzden parantez şart:

$$(f - g)(x) = x^2 + 1 - (3x - 2) = x^2 - 3x + 3$$

$(f - g)(2) = 4 - 6 + 3 = 1$. Kontrol: $f(2) - g(2) = 5 - 4 = 1$.

**Kural.** $f\colon A \to \mathbb{R}$, $g\colon B \to \mathbb{R}$ ve $A \cap B \neq \varnothing$ ise

$$(f + g)(x) = f(x) + g(x), \qquad (f - g)(x) = f(x) - g(x), \qquad x \in A \cap B$$

Grafikte toplam, her $x$ için iki yüksekliğin üst üste konmasıdır:

![Koordinat düzleminde üç doğru: mavi f, yeşil g ve kırmızı f + g. x = 2'de mavi şerit 0'dan 3'e (f(2) = 3), üstüne yeşil şerit 3'ten 4'e (g(2) = 1) eklenmiş; kırmızı doğru (2, 4) noktasından geçiyor.](gorsel/tyt-matematik/11-07-toplam-grafik.svg "Burada f(x) = x + 1, g(x) = 2 − x/2. x = 2'de f'nin yüksekliğine g'nin yüksekliği eklenince f + g'nin noktası bulunur.")

> **Tuzak:** $x^2 + 1 - 3x - 2$ yazmak (parantezi unutmak) $(f - g)(2)$ için $-3$ verir. Çıkarılan fonksiyonun her terimi işaret değiştirir.

## Sabitle çarpma

**Örnek.** Aynı $f$ ve $g$ için $(3f - 2g)(1)$ kaçtır?

$f(1) = 2$, $g(1) = 1$. Önce değerleri bul, sonra katsayılarla çarp:

$$(3f - 2g)(1) = 3 \cdot f(1) - 2 \cdot g(1) = 6 - 2 = 4$$

**Kural.** $c \in \mathbb{R}$ için $(c \cdot f)(x) = c \cdot f(x)$. Sabit, fonksiyonun **değerini** çarpar; $x$'e dokunmaz.

> **Tuzak:** $(3f)(1)$ ile $f(3)$ aynı şey değildir. $(3f)(1) = 3 \cdot f(1) = 6$, oysa $f(3) = 10$.

## Çarpma ve bölme

**Örnek.** Aynı $f$ ve $g$ için:

- $(f \cdot g)(-1) = f(-1) \cdot g(-1) = 2 \cdot (-5) = -10$.
- $\left(\dfrac{f}{g}\right)(2) = \dfrac{f(2)}{g(2)} = \dfrac{5}{4}$.
- $\left(\dfrac{f}{g}\right)(x) = \dfrac{x^2 + 1}{3x - 2}$, ama yalnızca $g(x) \neq 0$ iken: $3x - 2 = 0$ yapan $x = \frac{2}{3}$ tanım kümesinden çıkar.

**Kural.** $x \in A \cap B$ için

$$(f \cdot g)(x) = f(x) \cdot g(x), \qquad \left(\frac{f}{g}\right)(x) = \frac{f(x)}{g(x)}, \quad g(x) \neq 0$$

$f^2$ yazımı $f \cdot f$ demektir: $f^2(x) = \big(f(x)\big)^2$.

> **Tuzak:** $(f \cdot g)(x)$, $f(g(x))$ değildir. Çarpımda iki değer **aynı $x$'te** hesaplanıp çarpılır; $g$'nin sonucu $f$'ye verilmez. ($f(g(x))$ bileşke fonksiyondur, ayrı bir derstir.)

## Tanım kümesi: ortak elemanlar

**Örnek.** Fonksiyonlar liste olarak verilsin:

$f = \{(1, 3), (2, 5), (3, 0), (4, 2)\}$, $\quad g = \{(2, 4), (3, 2), (4, 0), (5, 6)\}$

$f$'nin tanım kümesi $A = \{1, 2, 3, 4\}$, $g$'ninki $B = \{2, 3, 4, 5\}$. İşlem yalnızca ikisinde de olan elemanlarda yapılır: $A \cap B = \{2, 3, 4\}$. $1$ için $g(1)$, $5$ için $f(5)$ yoktur.

![İki kesişen küme: A'da yalnız 1, B'de yalnız 5, kesişimde 2, 3 ve 4. Kesişim yeşil boyalı, 4 kırmızı halka içinde. Altta A kesişim B eşittir 2, 3, 4 ve f/g için 4 atılır yazıyor.](gorsel/tyt-matematik/11-07-ortak-kume.svg "f + g, f − g ve f · g kesişimin üç elemanında tanımlı. f/g'de g(4) = 0 olduğu için 4 de atılır.")

| $x$ | $f(x)$ | $g(x)$ | $f + g$ | $f \cdot g$ | $\frac{f}{g}$ | $\frac{g}{f}$ |
|---|---|---|---|---|---|---|
| 2 | 5 | 4 | 9 | 20 | $\frac{5}{4}$ | $\frac{4}{5}$ |
| 3 | 0 | 2 | 2 | 0 | $0$ | tanımsız |
| 4 | 2 | 0 | 2 | 0 | tanımsız | $0$ |

Tabloya dikkat: $\frac{f}{g}$ fonksiyonunun tanım kümesi $\{2, 3\}$, $\frac{g}{f}$ fonksiyonununki $\{2, 4\}$. **Paydanın** sıfır olduğu yer atılır; payın sıfır olması sorun değildir, bölüm $0$ olur.

**Kural verilince.** $f(x) = x + 3$ ve $g(x) = x^2 - 4$ ($\mathbb{R}$'de) ise $\frac{f}{g}$ için $x^2 - 4 = 0$ yapan $x = -2$ ve $x = 2$ atılır:

![Sayı doğrusu −4'ten 4'e mavi boyalı. −2 ve 2'de kırmızı içi boş noktalar (g(−2) = 0, g(2) = 0), −3'te yeşil dolu nokta ((f/g)(−3) = 0).](gorsel/tyt-matematik/11-07-bolum-tanim.svg "f/g'nin tanım kümesi ℝ − {−2, 2}. Payı sıfır yapan −3 atılmaz.")

$$\frac{f}{g}\colon \mathbb{R} \setminus \{-2, 2\} \to \mathbb{R}$$

**Kural.** $f \pm g$ ve $f \cdot g$ için tanım kümesi $A \cap B$; $\frac{f}{g}$ için $A \cap B$'den $g(x) = 0$ yapan değerler de çıkarılır.

## Toplam ve farktan fonksiyonu bulmak

**Örnek.** $(f + g)(x) = 5x + 1$ ve $(f - g)(x) = x + 7$ ise $f(x)$ ve $g(x)$ nedir?

İki eşitliği alt alta yaz:

$$\begin{aligned} f(x) + g(x) &= 5x + 1 \\ f(x) - g(x) &= x + 7 \end{aligned}$$

Topla: $2f(x) = 6x + 8$, $f(x) = 3x + 4$. Çıkar: $2g(x) = 4x - 6$, $g(x) = 2x - 3$.

Kontrol: $(3x + 4) + (2x - 3) = 5x + 1$ ve $(3x + 4) - (2x - 3) = x + 7$.

**Kural.** $f = \dfrac{(f + g) + (f - g)}{2}$, $\quad g = \dfrac{(f + g) - (f - g)}{2}$. Bu, denklem sistemindeki yok etme yöntemidir.

**Önceki dersle bağ.** $f$ çift, $g$ tek ve $f(x) + g(x) = x^2 + 3x + 2$ olsun. $x$ yerine $-x$ yaz: $f(-x) + g(-x) = f(x) - g(x) = x^2 - 3x + 2$. Şimdi toplam ve fark elinde: $f(x) = x^2 + 2$, $g(x) = 3x$. Kısaca: çift dereceli terimler $f$'ye, tek dereceli terimler $g$'ye gider; **sabit terim çift** taraftadır.

## ÖSYM tuzakları

> **Farkta parantez:** $(f - g)(x)$ yazarken $g(x)$'i parantez içine al. $x^2 + 1 - (3x - 2) = x^2 - 3x + 3$; parantezsiz yazan $x^2 - 3x - 1$ bulur.

> **Çarpımı bileşke sanmak:** $(f \cdot g)(0) = f(0) \cdot g(0)$; $f(g(0))$ değil. Aynı şekilde $f^2(x) = \big(f(x)\big)^2$; $f(f(x))$ değil.

> **Sabitle çarpımı içeri sokmak:** $(2f)(x) = 2f(x)$; $f(2x)$ değil.

> **Tanım kümesinde birleşim almak:** $f + g$ ancak **iki fonksiyonun da** tanımlı olduğu yerde vardır: $A \cup B$ değil, $A \cap B$.

> **Yanlış paydayı sıfırlamak:** $\frac{f}{g}$ için $g(x) = 0$ yapan değerler atılır, $f(x) = 0$ yapanlar kalır. $\frac{g}{f}$ sorulursa durum tersine döner.

## Kendini dene

### Soru 1
$f(x) = 2x - 1$ ve $g(x) = x^2 + 3$ olduğuna göre $(f - g)(2)$ kaçtır?

A) $-4$
B) $2$
C) $4$
D) $10$
E) $21$

**Cevap:** A
**Çözüm:** $f(2) = 3$, $g(2) = 7$; $(f - g)(2) = 3 - 7 = -4$. $2$, parantezi unutup $2x - 1 - x^2 + 3$ yazmaktır; $4$, $(g - f)(2)$; $10$, $(f + g)(2)$; $21$ ise $(f \cdot g)(2)$ değeridir.

### Soru 2
$f = \{(-1, 4), (0, 2), (1, 6), (2, 3)\}$ ve $g = \{(0, 5), (1, 0), (2, 1), (3, 7)\}$ olduğuna göre $\frac{f}{g}$ fonksiyonunun tanım kümesi aşağıdakilerden hangisidir?

A) $\{0, 1, 2\}$
B) $\{-1, 0, 2, 3\}$
C) $\{-1, 3\}$
D) $\{0, 2\}$
E) $\{-1, 0, 1, 2, 3\}$

**Cevap:** D
**Çözüm:** Ortak elemanlar $\{0, 1, 2\}$. $g(1) = 0$ olduğu için $1$ atılır: $\{0, 2\}$. $\{0, 1, 2\}$, paydayı kontrol etmemektir; $\{-1, 0, 1, 2, 3\}$ ise kesişim yerine birleşim almaktır.

### Soru 3
$(f + g)(x) = 4x + 6$ ve $(f - g)(x) = 2x - 2$ olduğuna göre $f(2)$ kaçtır?

A) 6
B) 8
C) 12
D) 14
E) 16

**Cevap:** B
**Çözüm:** Topla: $2f(x) = 6x + 4$, $f(x) = 3x + 2$, $f(2) = 8$. $16$, $2f(2)$ değerinde kalıp ikiye bölmeyi unutmaktır; $6$, $g(2)$ değeridir ($g(x) = x + 4$); $14$ ise $(f + g)(2)$ değeridir.

## Özet kartı

- $(f \pm g)(x) = f(x) \pm g(x)$, $(f \cdot g)(x) = f(x) \cdot g(x)$, $(c f)(x) = c \cdot f(x)$: hep **aynı $x$**.
- $\left(\frac{f}{g}\right)(x) = \frac{f(x)}{g(x)}$, yalnızca $g(x) \neq 0$ iken.
- Tanım kümesi: $A \cap B$; bölümde paydayı sıfır yapanlar da çıkar.
- Farkta parantez; $(f \cdot g)(x) \neq f(g(x))$; $(2f)(x) \neq f(2x)$.
- $(f + g)$ ve $(f - g)$ verilirse topla ve ikiye böl: $f$ çıkar.
- $f$ çift, $g$ tek ise $f + g$ kuralında çift dereceli terimler ve sabit $f$'ye, tek dereceliler $g$'ye aittir.

## Sonraki adım

Alıştırmaya geç (aşağıdaki düğme). Sonraki ders **Fonksiyon Grafikleri**; grafikten değer okumayı bu dersteki işlemlerle birleştireceksin. Biraz sonra gelen **İki Fonksiyonun Bileşkesi** dersinde ise "$f \cdot g$ ile $f(g(x))$ aynı değil" dediğimiz fark önem kazanacak.
