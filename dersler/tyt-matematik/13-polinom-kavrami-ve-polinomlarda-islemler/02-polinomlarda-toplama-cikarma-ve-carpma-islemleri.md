---
baslik: Polinomlarda Toplama, Çıkarma ve Çarpma İşlemleri
ders: tyt-matematik
sure: 20 dk
kaynak: MEBİ Konu Özeti 176317e2fa
guncelleme: 2026-11-18
---
# Polinomlarda Toplama, Çıkarma ve Çarpma İşlemleri

**Bu dersin sonunda:** iki polinomu toplayıp çıkarabilecek, çarpabilecek, çarpımı açmadan istenen bir terimin katsayısını bulabilecek ve işlem sonucunun derecesini hesaplayabileceksin.

> **TYT'de yeri:** Bu işlemler tek başına nadiren soru olur; ama bölme, çarpanlara ayırma ve özdeşlik sorularının her adımında kullanılır. Doğrudan gelen kalıplar: "çarpımda $x^2$'li terimin katsayısı kaçtır?", "$P(x) \cdot Q(x)$ polinomunun derecesi kaçtır?" ve katsayılar toplamı ya da sabit terim isteyen kısa sorular.

## Önce hatırla

<details><summary>Polinom Kavramı dersinden: P(x) = 3x⁴ − 2x³ + x − 5 polinomunun derecesi, baş katsayısı, sabit terimi ve katsayılar toplamı kaçtır?</summary>
Derece <b>4</b>, baş katsayı <b>3</b>, sabit terim $P(0) = $ <b>−5</b>, katsayılar toplamı $P(1) = 3 - 2 + 1 - 5 = $ <b>−3</b>. Bugün bu iki kısa yolu ($x = 1$ ve $x = 0$ yazmak) çarpım polinomlarında da kullanacaksın.
</details>

<details><summary>Polinom Kavramı dersinden: P(x) = (a − 3)x³ + 2x² + 5 polinomu ikinci dereceden ise a kaçtır?</summary>
İkinci dereceden olması için $x^3$'lü terim yok olmalı: $a - 3 = 0$, <b>a = 3</b>. Katsayısı sıfır olan terim polinomda yoktur; toplama ve çıkarmada derecenin düşmesi de buna dayanır.
</details>

## 1. Toplama ve çıkarma

**Örnek.** $P(x) = 3x^3 - 2x^2 + 5x - 1$ ve $Q(x) = x^3 + 4x^2 - 7$ olsun.

**Toplama.** Aynı dereceli terimler (benzer terimler) bir araya getirilir, katsayıları toplanır:

$$P(x) + Q(x) = (3 + 1)x^3 + (-2 + 4)x^2 + 5x + (-1 - 7) = 4x^3 + 2x^2 + 5x - 8$$

**Çıkarma.** $P(x) - Q(x)$ yazınca eksi işareti $Q(x)$'in **bütün** terimlerine dağıtılır: $-Q(x) = -x^3 - 4x^2 + 7$. Sonra toplama gibi devam edilir:

$$P(x) - Q(x) = 2x^3 - 6x^2 + 5x + 6$$

![Dört sütunlu tablo: x küp, x kare, x ve sabit. İlk satır P(x): 3x küp, eksi 2x kare, 5x, eksi 1. Kırmızı ikinci satır eksi Q(x): eksi x küp, eksi 4x kare, 0, artı 7. Çizginin altında yeşil sonuç: 2x küp, eksi 6x kare, 5x, artı 6.](gorsel/tyt-matematik/13-02-cikarma-sutun.svg "Çıkarmayı, Q(x) polinomunun her teriminin işaretini değiştirip toplamak gibi yap. Q(x) içinde x'li terim yok, onun yerine 0 yazıldı; sabit terim −7 iken +7 oldu.")

**Kural.** Polinomlar toplanırken ya da çıkarılırken yalnızca **aynı dereceli** terimlerin katsayıları toplanır ya da çıkarılır. $x^3$ ile $x^2$ birleştirilemez.

### Toplamın derecesi

$\text{der}[P(x)] = n$, $\text{der}[Q(x)] = m$ ve $n > m$ ise en büyük dereceli terimi değiştirecek başka terim yoktur:

$$\text{der}[P(x) \pm Q(x)] = n$$

Dereceler **eşitse** baş katsayılar birbirini götürebilir. Örneğin $P(x) = 2x^3 + x$, $Q(x) = 2x^3 - 5$ için $P(x) - Q(x) = x + 5$; ikisi de 3. dereceden ama fark 1. dereceden. Yani toplamın derecesi en büyük dereceyi **geçemez**, ama ondan küçük olabilir.

## 2. Çarpma

**Örnek.** $(2x - 3)(x^2 + 4x - 1)$ çarpımını bul.

Birinci polinomun **her terimi**, ikincinin **her terimiyle** çarpılır. $2$ terim $\times$ $3$ terim $= 6$ çarpım çıkar:

![Çarpım tablosu: üstte x kare, artı 4x, eksi 1; solda 2x ve eksi 3. Hücreler: 2x küp, 8x kare, eksi 2x; eksi 3x kare, eksi 12x, artı 3. Aynı dereceli hücreler aynı renkte.](gorsel/tyt-matematik/13-02-carpim-tablosu.svg "Her hücre, satırındaki terim ile sütunundaki terimin çarpımı. Aynı renkteki hücreler benzer terimdir: onları topla.")

$$= 2x^3 + 8x^2 - 2x - 3x^2 - 12x + 3 = 2x^3 + 5x^2 - 14x + 3$$

**Kural.** $P(x) \cdot Q(x)$ işleminde her terim her terimle çarpılır, sonra benzer terimler toplanır ve sonuç $x$'in azalan kuvvetlerine göre yazılır. Bir sayıyla çarpmada ($k \cdot P(x)$) her terim $k$ ile çarpılır.

### Çarpımı açmadan bir katsayı bulmak

**Örnek.** $(x^2 - 3x + 2)(2x^2 + x - 5)$ çarpımında $x^2$'li terimin katsayısı kaçtır?

Bütün çarpımı açmana gerek yok. Üsleri toplamı $2$ eden terim çiftlerini seç:

| Birinciden | İkinciden | Çarpım |
|---|---|---|
| $x^2$ | $-5$ | $-5x^2$ |
| $-3x$ | $x$ | $-3x^2$ |
| $2$ | $2x^2$ | $4x^2$ |

Katsayı: $-5 - 3 + 4 = -4$.

### Çarpımda katsayılar toplamı ve sabit terim

$x = 1$ yazınca $P(1) \cdot Q(1)$ elde edilir. Yani çarpımın katsayılar toplamı, katsayılar toplamlarının **çarpımıdır**. Aynı şekilde çarpımın sabit terimi, sabit terimlerin çarpımıdır.

Yukarıdaki örnekte: $(2 - 3)(1 + 4 - 1) = -1 \cdot 4 = -4$ ve açılmış hâlde $2 + 5 - 14 + 3 = -4$. Sabit terim: $(-3)(-1) = 3$. İkisi de tutuyor.

## 3. Derece kuralları

**Örnek.** $\text{der}[P(x)] = 3$ ve $\text{der}[Q(x)] = 2$ olsun. $P(x) = x^3$, $Q(x) = x^2$ gibi en basit hâlleriyle düşün:

| İfade | En büyük terim | Derece |
|---|---|---|
| $P(x) \cdot Q(x)$ | $x^3 \cdot x^2 = x^5$ | $3 + 2 = 5$ |
| $5 \cdot P(x)$ | $5x^3$ | $3$ |
| $P^2(x)$ | $(x^3)^2 = x^6$ | $3 \cdot 2 = 6$ |
| $P(x^2)$ | $(x^2)^3 = x^6$ | $3 \cdot 2 = 6$ |
| $P(Q(x))$ | $(x^2)^3 = x^6$ | $3 \cdot 2 = 6$ |
| $P(x) + Q(x)$ | $x^3$ | $3$ |

![Kavram haritası: der P eşittir n, der Q eşittir m. Toplama ve çıkarmada büyük olan n; çarpmada toplanır, n artı m; kuvvet ve bileşkede çarpılır, n çarpı k ve n çarpı m.](gorsel/tyt-matematik/13-02-derece-kurallari.svg "Burada n > m. Toplamada büyük derece kalır, çarpmada dereceler toplanır, kuvvet ve bileşkede çarpılır.")

**Kural.** $\text{der}[P(x)] = n$, $\text{der}[Q(x)] = m$, $k$ pozitif tam sayı olsun:

- $\text{der}[P(x) \cdot Q(x)] = n + m$
- $\text{der}[c \cdot P(x)] = n$ ($c \ne 0$ bir sayı)
- $\text{der}[P^k(x)] = \text{der}[P(x^k)] = n \cdot k$
- $\text{der}[P(Q(x))] = n \cdot m$

## ÖSYM tuzakları

> **Eksiyi yalnızca ilk terime dağıtmak:** $P(x) - (x^2 - 3x + 4)$ işleminde $-x^2 - 3x + 4$ yazmak yanlıştır; doğrusu $-x^2 + 3x - 4$. Çıkarılan polinomu önce paranteze al.

> **Çarpımın derecesini çarpmak:** $\text{der}[P(x) \cdot Q(x)]$ dereceler **toplamıdır**: $3$ ile $4$ için $7$, $12$ değil. Çarpma ise kuvvet ve bileşkede yapılır: $\text{der}[P^2(x)] = 2n$, $n^2$ değil.

> **Eşit derecede düşmeyi unutmak:** İki polinom aynı dereceden ise toplamları ya da farkları daha küçük dereceli olabilir. "Toplam 1. dereceden" deniyorsa yüksek dereceli terimlerin katsayıları sıfır olmalıdır.

> **Katsayılar toplamını toplamak:** $P(x) \cdot Q(x)$ polinomunun katsayılar toplamı $P(1) + Q(1)$ değil, $P(1) \cdot Q(1)$'dir.

> **Kareyi dağıtmak:** $(x + 3)^2 = x^2 + 9$ yanlıştır. $(x + 3)(x + 3) = x^2 + 6x + 9$; ortadaki $6x$ iki çapraz çarpımdan gelir.

## Kendini dene

### Soru 1
$P(x) = x^2 - 4x + 3$ ve $Q(x) = 2x^2 + x - 5$ olduğuna göre $P(x) - Q(x)$ polinomu aşağıdakilerden hangisidir?

A) $-x^2 - 3x - 2$
B) $3x^2 - 3x - 2$
C) $x^2 + 5x - 8$
D) $-x^2 - 5x + 8$
E) $-x^2 - 5x - 2$

**Cevap:** D
**Çözüm:** $-Q(x) = -2x^2 - x + 5$. Toplarsak: $(1 - 2)x^2 + (-4 - 1)x + (3 + 5) = -x^2 - 5x + 8$. A seçeneği eksiyi yalnızca ilk terime dağıtmaktır; B iki polinomu toplamaktır; C ise $Q(x) - P(x)$ işlemidir.

### Soru 2
$(x^2 + 2x - 3)(3x - 1)$ çarpımında $x$'li terimin katsayısı kaçtır?

A) $-11$
B) $-9$
C) $-7$
D) $-2$
E) $7$

**Cevap:** A
**Çözüm:** Üsleri toplamı 1 olan çiftler: $2x \cdot (-1) = -2x$ ve $(-3) \cdot 3x = -9x$. Katsayı $-2 - 9 = -11$. Çarpımın tamamı $3x^3 + 5x^2 - 11x + 3$'tür. Çiftlerden yalnızca birini alan $-9$ ya da $-2$, bir işareti kaçıran $7$ bulur.

### Soru 3
$\text{der}[P(x)] = 4$ ve $\text{der}[Q(x)] = 3$ olduğuna göre $P(x^2) \cdot Q(x) - x \cdot P(x)$ polinomunun derecesi kaçtır?

A) 7
B) 8
C) 11
D) 12
E) 24

**Cevap:** C
**Çözüm:** $\text{der}[P(x^2)] = 4 \cdot 2 = 8$, çarpımda dereceler toplanır: $\text{der}[P(x^2) \cdot Q(x)] = 8 + 3 = 11$. $\text{der}[x \cdot P(x)] = 1 + 4 = 5$. Farkın derecesi büyük olandır: $11$. $24$, çarpımda dereceleri çarpmaktan gelir.

## Özet kartı

- Toplama ve çıkarmada yalnızca aynı dereceli terimler birleşir; çıkarmada eksi bütün terimlere dağılır.
- $n > m$ ise $\text{der}[P \pm Q] = n$; dereceler eşitse sonuç daha küçük dereceli olabilir.
- Çarpmada her terim her terimle çarpılır; tek bir katsayı için yalnızca üsleri toplamı istenen sayı olan çiftleri çarp.
- Çarpımın katsayılar toplamı $P(1) \cdot Q(1)$, sabit terimi $P(0) \cdot Q(0)$.
- $\text{der}[P \cdot Q] = n + m$; $\text{der}[P^k] = \text{der}[P(x^k)] = n \cdot k$; $\text{der}[P(Q(x))] = n \cdot m$.

## Sonraki adım

Alıştırmaya geç (aşağıdaki düğme). Sonraki ders **Polinomlarda Bölme İşlemi**; bölmede her adımda bu dersteki çarpma ve çıkarmayı yapacaksın.
