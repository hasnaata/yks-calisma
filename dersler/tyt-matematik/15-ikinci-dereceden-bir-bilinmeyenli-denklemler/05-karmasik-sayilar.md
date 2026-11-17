---
baslik: Karmaşık Sayılar
ders: tyt-matematik
sure: 20 dk
kaynak: MEBİ Konu Özeti b4f4d2bc65
guncelleme: 2026-11-17
---
# Karmaşık Sayılar

**Bu dersin sonunda:** $i^2 = -1$ kuralıyla negatif sayıların karekökünü yazabilecek, $i$'nin her kuvvetini dörde bölerek bulabilecek, bir karmaşık sayının gerçek ve sanal kısmını ve eşleniğini söyleyebilecek, $\Delta < 0$ olan ikinci dereceden denklemlerin köklerini karmaşık sayı olarak bulabileceksin.

> **TYT'de yeri:** "$i^{2027}$ kaçtır?", "$i + i^2 + \dots + i^{30}$ toplamı nedir?", "denklemin köklerinden biri hangisidir?" ve "bir kökü $1 + 3i$ olduğuna göre $k$ kaçtır?" kalıpları gelir. Sorular kısa; hata çoğunlukla $i^2$'nin işaretinde ya da kuvvetin kalanında yapılır.

## Önce hatırla

<details><summary>Geçen dersten: $2x^2 - 6x + 5 = 0$ denkleminin kökleri toplamı ve kökleri çarpımı kaçtır?</summary>
$a = 2$, $b = -6$, $c = 5$. Kökler toplamı $x_1 + x_2 = -\frac{b}{a} = -\frac{-6}{2} = 3$, kökler çarpımı $x_1 \cdot x_2 = \frac{c}{a} = \frac{5}{2}$. Dikkat: bu denklemde $\Delta = 36 - 40 = -4 < 0$; gerçek kök yok. Bu derste köklerin nerede olduğunu göreceksin ve toplam ile çarpım formüllerinin onlar için de geçerli olduğunu kullanacaksın.
</details>

<details><summary>Geçen dersten: Kökleri $2$ ve $-5$ olan, $x^2$'nin katsayısı $1$ olan ikinci dereceden denklemi yaz.</summary>
Toplam $T = 2 + (-5) = -3$, çarpım $Ç = 2 \cdot (-5) = -10$. Denklem $x^2 - Tx + Ç = 0$ biçiminde: $x^2 - (-3)x + (-10) = 0$, yani $x^2 + 3x - 10 = 0$. Kontrol: $(x - 2)(x + 5) = x^2 + 3x - 10$.
</details>

## Sanal birim $i$ ve karmaşık sayı

**Örnek.** $x^2 + 16 = 0$ denklemini çöz.

$x^2 = -16$. Karesi negatif olan gerçek sayı yoktur; gerçek sayılarda Ç $= \varnothing$. Yeni bir sayı tanımlarız: karesi $-1$ olan sayıya **sanal sayı birimi** denir ve $i$ ile gösterilir.

$$i = \sqrt{-1}, \qquad i^2 = -1$$

Bununla $\sqrt{-16} = \sqrt{16} \cdot \sqrt{-1} = 4i$ olur. Kontrol: $(4i)^2 = 16 \cdot i^2 = 16 \cdot (-1) = -16$. Denklemin kökleri $x = 4i$ ve $x = -4i$.

Aynı yolla: $\sqrt{-9} = 3i$, $\sqrt{-7} = i\sqrt{7}$, $\sqrt{-12} = i\sqrt{12} = 2\sqrt{3}\,i$.

**Kural.** $a > 0$ ise $\sqrt{-a} = i\sqrt{a}$. $a, b$ gerçek sayılar olmak üzere $z = a + bi$ biçimindeki sayılara **karmaşık sayı** denir.

| $z = a + bi$ | Gerçek kısım $\text{Re}(z)$ | Sanal kısım $\text{Im}(z)$ |
|---|---|---|
| $3 - 5i$ | $3$ | $-5$ |
| $-2 + i$ | $-2$ | $1$ |
| $4i$ | $0$ | $4$ |
| $7$ | $7$ | $0$ |

Karmaşık sayılar kümesi $\mathbb{C}$ ile gösterilir. Son satıra bak: $7 = 7 + 0i$. Her gerçek sayı sanal kısmı $0$ olan bir karmaşık sayıdır, yani $\mathbb{R} \subset \mathbb{C}$.

![İç içe iki küme. Dıştaki mavi küme karmaşık sayılar, içindeki yeşil küme gerçek sayılar. Gerçek sayılar kümesinde eksi 5, üç bölü dört, kök 2 ve pi; dışında kalan kısımda i, 3i, 2 eksi 3i ve kök eksi 9 var.](gorsel/tyt-matematik/15-05-kumeler.svg "Gerçek sayılar karmaşık sayıların içindedir. Sanal kısmı sıfırdan farklı olan sayılar, örneğin 2 − 3i, yeşil kümenin dışında kalır.")

**Örnek.** $z = (m - 2) + (m + 3)i$ bir gerçek sayı olduğuna göre $m$ kaçtır?

Gerçek sayı olması, sanal kısmın $0$ olması demektir: $m + 3 = 0$, $m = -3$. O zaman $z = -5$.

## $i$'nin kuvvetleri

**Örnek.** $i^{27}$ kaçtır?

İlk kuvvetleri tek tek bul:

| $i^0$ | $i^1$ | $i^2$ | $i^3 = i^2 \cdot i$ | $i^4 = i^2 \cdot i^2$ |
|---|---|---|---|---|
| $1$ | $i$ | $-1$ | $-i$ | $(-1)(-1) = 1$ |

$i^4 = 1$ olduğundan her dört adımda değerler başa döner. $27 = 4 \cdot 6 + 3$, yani $i^{27} = (i^4)^6 \cdot i^3 = 1 \cdot (-i) = -i$.

![Bir çember üzerinde dört kutu, saat yönünde: i üzeri 0 eşittir 1, i üzeri 1 eşittir i, i üzeri 2 eşittir eksi 1, i üzeri 3 eşittir eksi i. Her ok i ile çarpmayı gösterir.](gorsel/tyt-matematik/15-05-i-dongusu.svg "Üssü 4'e böl, yalnızca kalana bak. Kalan 0 ise 1, kalan 1 ise i, kalan 2 ise −1, kalan 3 ise −i.")

**Kural.** $n$'nin $4$'e bölümünden kalan $r$ ise $i^n = i^r$.

| Kalan | 0 | 1 | 2 | 3 |
|---|---|---|---|---|
| $i^n$ | $1$ | $i$ | $-1$ | $-i$ |

Örnekler: $i^{50}$: $50 = 4 \cdot 12 + 2$, sonuç $-1$. $i^{100}$: kalan $0$, sonuç $1$.

**Örnek.** $i^{13} + i^{14} + i^{15}$ toplamı kaçtır?

Kalanlar $1, 2, 3$: $i + (-1) + (-i) = -1$.

**Ardışık dört kuvvet:** $i + i^2 + i^3 + i^4 = i - 1 - i + 1 = 0$. Ardışık her dört kuvvetin toplamı $0$'dır. Uzun toplamlarda dörtlü grupları at, artan terimleri topla.

## Eşlenik

**Örnek.** $z = 2 + 7i$ sayısının eşleniğini bul; $z$ ile eşleniğinin toplamını ve çarpımını hesapla.

Eşlenik, sanal kısmın işareti değiştirilerek bulunur: $\overline{z} = 2 - 7i$.

- Toplam: $(2 + 7i) + (2 - 7i) = 4$. Sanal kısımlar birbirini götürür.
- Çarpım: $(2 + 7i)(2 - 7i) = 2^2 - (7i)^2 = 4 - 49i^2 = 4 + 49 = 53$.

**Kural.** $z = a + bi$ ise $\overline{z} = a - bi$.

$$z + \overline{z} = 2a, \qquad z \cdot \overline{z} = a^2 + b^2$$

İkisi de gerçek sayıdır. Diğer örnekler: $\overline{-4i} = 4i$, $\overline{5} = 5$ (gerçek sayının eşleniği kendisidir).

## $\Delta < 0$ olan denklemlerin kökleri

**Örnek.** $x^2 - 4x + 13 = 0$ denklemini karmaşık sayılarda çöz.

1. $a = 1$, $b = -4$, $c = 13$.
2. $\Delta = (-4)^2 - 4 \cdot 1 \cdot 13 = 16 - 52 = -36$. Gerçek kök yok.
3. $\sqrt{\Delta} = \sqrt{-36} = 6i$.
4. $x_{1,2} = \dfrac{-b \pm \sqrt{\Delta}}{2a} = \dfrac{4 \pm 6i}{2} = 2 \pm 3i$.

Ç $= \{2 - 3i,\ 2 + 3i\}$. Kökler birbirinin eşleniğidir. Geçen dersin formülleri de tutar: toplam $4 = -\frac{b}{a}$, çarpım $2^2 + 3^2 = 13 = \frac{c}{a}$.

**Örnek.** $x^2 + 2x + 5 = 0$ denkleminin kökleri? $\Delta = 4 - 20 = -16$, $\sqrt{-16} = 4i$, $x = \dfrac{-2 \pm 4i}{2} = -1 \pm 2i$.

![Akış: katsayıları işaretiyle oku, delta eşittir b kare eksi 4ac hesapla, delta negatifse kök delta eşittir i çarpı kök mutlak delta, x eşittir eksi b artı eksi i kök mutlak delta bölü 2a, kökler eşlenik m artı eksi ni.](gorsel/tyt-matematik/15-05-yontem.svg "Formül aynıdır; değişen tek adım negatif Δ'nın karekökünü i ile yazmaktır.")

**Kural.** Katsayıları gerçek sayı olan $ax^2 + bx + c = 0$ denkleminde $\Delta < 0$ ise kökler $x_{1,2} = \dfrac{-b \pm i\sqrt{|\Delta|}}{2a}$ olur. **Bir kök $m + ni$ ise diğer kök $m - ni$'dir.**

**Örnek.** Katsayıları gerçek, $x^2$'nin katsayısı $1$ olan ve bir kökü $3 - i$ olan denklemi yaz.

Diğer kök eşlenik: $3 + i$. Toplam $T = 6$, çarpım $Ç = 3^2 + 1^2 = 10$. Denklem $x^2 - 6x + 10 = 0$. Kontrol: $\Delta = 36 - 40 = -4$, $x = \frac{6 \pm 2i}{2} = 3 \pm i$.

## ÖSYM tuzakları

> **$i^2$'nin işareti:** $i^2 = -1$'dir. $(3i)^2 = 9i^2 = -9$; $(2 + 7i)(2 - 7i)$ çarpımında $-49i^2 = +49$ olur. Bu adımda işaret kaybeden eşlenik çarpımını $4 - 49 = -45$ bulur.

> **Kökleri çarpmak:** $\sqrt{-4} \cdot \sqrt{-9} \ne \sqrt{36}$. Önce $i$'yi çıkar: $2i \cdot 3i = 6i^2 = -6$. $\sqrt{a} \cdot \sqrt{b} = \sqrt{ab}$ kuralı iki sayı da negatifken çalışmaz.

> **Sanal kısım bir gerçek sayıdır:** $z = 3 - 5i$ için $\text{Im}(z) = -5$'tir, $-5i$ değil; işaret de sanal kısma dahildir.

> **Kuvvette kalan:** $i^{n}$ için üssün kendisine değil, $4$'e bölümünden kalana bakılır. Kalan $0$ ise sonuç $1$'dir, $0$ değil.

> **Paydadaki $2a$:** $\dfrac{4 \pm 6i}{2}$ ifadesinde hem gerçek hem sanal kısım $2$'ye bölünür: $2 \pm 3i$. Yalnızca $4$'ü bölüp $2 \pm 6i$ yazmak sık yapılan hatadır.

## Kendini dene

### Soru 1
$i^{38} + i^{41}$ toplamı aşağıdakilerden hangisidir?

A) $-1 - i$
B) $-1 + i$
C) $0$
D) $1 - i$
E) $1 + i$

**Cevap:** B
**Çözüm:** $38 = 4 \cdot 9 + 2$, kalan $2$: $i^{38} = -1$. $41 = 4 \cdot 10 + 1$, kalan $1$: $i^{41} = i$. Toplam $-1 + i$. $i^2$'yi $1$ sanan $1 + i$ bulur.

### Soru 2
$x^2 - 6x + 10 = 0$ denkleminin karmaşık sayılardaki çözüm kümesi aşağıdakilerden hangisidir?

A) $\{-3 - i,\ -3 + i\}$
B) $\{3 - 2i,\ 3 + 2i\}$
C) $\{3 - i,\ 3 + i\}$
D) $\{6 - 2i,\ 6 + 2i\}$
E) $\varnothing$

**Cevap:** C
**Çözüm:** $\Delta = 36 - 40 = -4$, $\sqrt{-4} = 2i$. $x = \dfrac{6 \pm 2i}{2} = 3 \pm i$. B, sanal kısmı $2$'ye bölmeyi unutmaktır; A, $-b$ yerine $b$ almaktır. E gerçek sayılardaki cevaptır; soru karmaşık sayıları soruyor.

### Soru 3
$z = (2m - 6) + (m + 1)i$ karmaşık sayısının gerçek kısmı $0$ olduğuna göre $z$ aşağıdakilerden hangisidir?

A) $-2i$
B) $2i$
C) $3i$
D) $4i$
E) $7i$

**Cevap:** D
**Çözüm:** $2m - 6 = 0$, $m = 3$. Sanal kısım $m + 1 = 4$, yani $z = 4i$. $m$'yi bulup $z = 3i$ diyen ya da sanal kısmı sıfırlayıp $m = -1$ alan ($z = -8$) yanılır.

## Özet kartı

- $i = \sqrt{-1}$, $i^2 = -1$; $a > 0$ için $\sqrt{-a} = i\sqrt{a}$.
- $z = a + bi$: $\text{Re}(z) = a$, $\text{Im}(z) = b$ (ikisi de gerçek sayı). $\mathbb{R} \subset \mathbb{C}$.
- $i^n$: üssü $4$'e böl; kalan $0, 1, 2, 3$ için $1, i, -1, -i$. Ardışık dört kuvvetin toplamı $0$.
- $\overline{a + bi} = a - bi$; $z + \overline{z} = 2a$, $z \cdot \overline{z} = a^2 + b^2$.
- $\Delta < 0$ ise $x = \dfrac{-b \pm i\sqrt{|\Delta|}}{2a}$; kökler eşleniktir, $m \pm ni$.
- Bir kök $m + ni$ ise denklem $x^2 - 2m\,x + (m^2 + n^2) = 0$.

## Sonraki adım

Alıştırmaya geç (aşağıdaki düğme). Bu ders ikinci dereceden denklemler konusunu kapatıyor. Sonraki konu **Merkezi Eğilim ve Yayılım Ölçüleri**; ilk ders **Merkezi Eğilim Ölçüleri** (aritmetik ortalama, ortanca, tepe değer). Bu konudaki kök formülü, $\Delta$ ve kök-katsayı bağıntılarını karışık tekrar setlerinde yeniden kullanacaksın.
