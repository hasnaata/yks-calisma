---
baslik: Polinomlarda Bölme İşlemi
ders: tyt-matematik
sure: 20 dk
kaynak: MEBİ Konu Özeti 188ef0d5f1
guncelleme: 2026-11-18
---
# Polinomlarda Bölme İşlemi

<div class="giris" dir="rtl" lang="ar">

**الدرس ده عن إيه؟** عن قسمة كثيرات الحدود (polinomlarda bölme): إزاي تقسم كثيرة حدود على تانية وتطلّع خارج القسمة (bölüm) والباقي (kalan).

- هتتعلم القسمة المطوّلة (uzun bölme) خطوة بخطوة: تقسم، تضرب، تطرح، ولو فيه حد ناقص تحط مكانه صفر.
- هتعرف تجيب درجة خارج القسمة ودرجة الباقي من غير ما تقسم أصلًا.
- هتستخدم علاقة القسمة (bölme eşitliği) عشان تلاقي كثيرة الحدود نفسها، أو مجموع معاملاتها، أو معامل مجهول لما القسمة تبقى من غير باقي.

**ليه مهم؟** في TYT نادرًا ما بييجي سؤال قسمة مطوّلة لوحده، لكن علاقة القسمة دي بتتسأل كتير، والدرس الجاي كله مبني عليها.

هو ٢٠ دقيقة بس؛ امسك ورقة وقلم وامشي مع الأمثلة، وهتلاقيها أسهل مما متخيّل.

</div>

**Bu dersin sonunda:** bir polinomu uzun bölmeyle bölüp bölümü ve kalanı bulabilecek, bölme eşitliğini $P(x) = Q(x) \cdot B(x) + K(x)$ kullanarak bilinmeyen polinomu ya da katsayıyı bulabilecek ve bölüm ile kalanın derecesini bölme yapmadan söyleyebileceksin.

> **TYT'de yeri:** Uzun bölme sorusu tek başına az gelir; asıl gelen, bölme eşitliğidir: "Bölen, bölüm ve kalan verilmiş, $P(x)$'in katsayılar toplamı kaçtır?", "Kalanın derecesi en çok kaç olabilir?", "Tam bölünüyorsa $a$ kaçtır?" Bir sonraki dersteki kalan bulma kısa yolları da bu eşitliğe dayanır.

## Önce hatırla

<details><summary>Polinomlarda toplama ve çıkarmadan: P(x) = 2x³ − x + 4 ve Q(x) = x³ + 3x² − 5 ise P(x) − Q(x) polinomunun derecesi ve baş katsayısı kaçtır?</summary>
Aynı dereceli terimleri alt alta yaz, $Q(x)$'in her teriminin işaretini değiştir: $P(x) - Q(x) = x^3 - 3x^2 - x + 9$. Derece <b>3</b>, baş katsayı <b>1</b>. Sabit terimde $4 - (-5) = 9$ olduğuna dikkat et.
</details>

<details><summary>Polinomlarda çarpmadan: (2x − 1)(x² + 3x − 4) çarpımında x² teriminin katsayısı kaçtır?</summary>
Yalnızca $x^2$ veren çarpımları topla: $2x \cdot 3x = 6x^2$ ve $(-1) \cdot x^2 = -x^2$. Katsayı $6 - 1 = $ <b>5</b>. Çarpımın derecesi de $1 + 2 = 3$ olur: çarpmada dereceler toplanır.
</details>

## Bölme eşitliği

**Örnek (sayılarla).** $47$'yi $6$'ya bölelim: bölüm $7$, kalan $5$. Bunu tek satırda yazarız:

$$47 = 6 \cdot 7 + 5, \qquad 5 < 6$$

Kalan bölenden küçük olmak zorunda; kalan $6$ ya da daha büyük olsaydı bölmeye devam ederdik.

Polinomda da aynısı geçerlidir. Burada "küçük" demek **derecesi küçük** demektir.

**Kural.** $\text{der}[P(x)] \ge \text{der}[Q(x)]$ olmak üzere $P(x)$ polinomu $Q(x)$ polinomuna bölündüğünde

$$P(x) = Q(x) \cdot B(x) + K(x)$$

| Ad | Gösterim |
|---|---|
| Bölünen | $P(x)$ |
| Bölen | $Q(x)$ |
| Bölüm | $B(x)$ |
| Kalan | $K(x)$ |

Bu eşitliğe **bölme eşitliği** denir. Kalan için koşul: $\text{der}[K(x)] < \text{der}[Q(x)]$. $K(x) = 0$ ise $P(x)$, $Q(x)$'e **tam (kalansız) bölünür**.

## Uzun bölme adım adım

**Örnek.** $P(x) = 2x^3 - 3x^2 + 4x - 1$ polinomunu $x - 2$ ile bölelim.

1. Baş terimleri böl: $\dfrac{2x^3}{x} = 2x^2$. Bu, bölümün ilk terimi.
2. $2x^2$ ile böleni çarp: $2x^2(x - 2) = 2x^3 - 4x^2$. Bunu alta yaz ve **çıkar**: $-3x^2 - (-4x^2) = x^2$. Geriye $x^2 + 4x - 1$ kalır.
3. Yine baş terimleri böl: $\dfrac{x^2}{x} = x$. Çarp: $x(x - 2) = x^2 - 2x$. Çıkar: $4x - (-2x) = 6x$. Geriye $6x - 1$ kalır.
4. $\dfrac{6x}{x} = 6$. Çarp: $6(x - 2) = 6x - 12$. Çıkar: $-1 - (-12) = 11$.
5. $11$'in derecesi $0$, bölenin derecesi $1$. Kalanın derecesi küçük olduğu için bölme biter.

![Uzun bölme düzeni: solda 2x küp eksi 3x kare artı 4x eksi 1, sağ üstte bölen x eksi 2, altında mavi kutuda bölüm 2x kare artı x artı 6. Solda kırmızı satırlar çıkarılan çarpımlar, en altta yeşil kutuda kalan 11.](gorsel/tyt-matematik/13-03-uzun-bolme.svg "Her kırmızı satır, bölümdeki bir terim ile bölenin çarpımıdır ve üstteki satırdan çıkarılır. Terimler derecelerine göre aynı sütunda durur.")

Sonuç: bölüm $B(x) = 2x^2 + x + 6$, kalan $K(x) = 11$.

**Kontrol (bölme eşitliği):** $(x - 2)(2x^2 + x + 6) + 11 = 2x^3 + x^2 + 6x - 4x^2 - 2x - 12 + 11 = 2x^3 - 3x^2 + 4x - 1$. Doğru.

**Kural.** Her turda üç iş yapılır: **böl** (baş terimi baş terime), **çarp** (bulduğunu bölenle), **çıkar** (alttaki satırın bütün işaretlerini değiştirerek). Kalanın derecesi bölenin derecesinden küçük olunca durulur.

![Akış şeması: azalan kuvvetlere göre sırala, eksik terime 0 yaz, baş terimi baş terime böl, bölenle çarp ve alta yaz, çıkar ve işaretleri değiştir; kalanın derecesi bölenden küçük değilse başa dön, küçükse bölme biter.](gorsel/tyt-matematik/13-03-bolme-adimlari.svg "Döngü, kalanın derecesi bölenin derecesinden küçük olana kadar sürer. Kırmızı kutu en çok hata yapılan adımdır.")

## Eksik terimli bölme

**Örnek.** $P(x) = x^4 - 3x^2 + 2x + 5$ polinomunu $x^2 + x - 1$ ile bölelim.

$P(x)$'te $x^3$ terimi yok. Sütunlar kaymasın diye onu $0x^3$ olarak yazarız: $x^4 + 0x^3 - 3x^2 + 2x + 5$.

![Uzun bölme: x üzeri 4 artı sarı kutu içinde 0 x küp eksi 3x kare artı 2x artı 5, bölen x kare artı x eksi 1, bölüm x kare eksi x eksi 1, kalan yeşil kutuda 2x artı 4.](gorsel/tyt-matematik/13-03-eksik-terim.svg "Sarı kutudaki 0x³ yazılmasaydı x³ terimleri yanlış sütuna düşerdi. Bölen ikinci dereceden olduğu için kalan birinci dereceden olabilir.")

- $\dfrac{x^4}{x^2} = x^2$; çarp: $x^4 + x^3 - x^2$; çıkar: $-x^3 - 2x^2 + 2x + 5$.
- $\dfrac{-x^3}{x^2} = -x$; çarp: $-x^3 - x^2 + x$; çıkar: $-x^2 + x + 5$.
- $\dfrac{-x^2}{x^2} = -1$; çarp: $-x^2 - x + 1$; çıkar: $2x + 4$.

Bölüm $x^2 - x - 1$, kalan $2x + 4$. Kalanın derecesi $1 < 2$, bölme biter.

**Kural.** Bölmeye başlamadan önce bölüneni ve böleni azalan kuvvetlere göre sırala; eksik dereceye $0$ katsayılı terim yaz.

## Bölüm ve kalanın derecesi

**Örnek.** $P(x)$ 7. dereceden, $Q(x)$ 3. dereceden bir polinom. $P(x)$, $Q(x)$'e bölününce bölümün ve kalanın derecesi ne olabilir?

- Bölme eşitliğinde $Q(x) \cdot B(x)$ çarpımı $P(x)$ ile aynı derecededir. Çarpmada dereceler toplanır: $3 + \text{der}[B(x)] = 7$, yani $\text{der}[B(x)] = 4$.
- Kalanın derecesi bölenin derecesinden küçük: $\text{der}[K(x)] < 3$. Kalan en çok **2.** dereceden olabilir (daha küçük de olabilir, $0$ da olabilir).

**Kural.**

| Bilgi | Formül |
|---|---|
| Bölümün derecesi | $\text{der}[B(x)] = \text{der}[P(x)] - \text{der}[Q(x)]$ |
| Kalanın derecesi | $\text{der}[K(x)] < \text{der}[Q(x)]$; en çok $\text{der}[Q(x)] - 1$ |
| Bölen birinci dereceden | Kalan sabit sayıdır |

## Bölme eşitliğiyle P(x)'i kullanmak

**Örnek.** $P(x)$ polinomu $x^2 - 3$ ile bölündüğünde bölüm $x + 2$, kalan $2x - 1$'dir. $P(x)$'in katsayılar toplamı kaçtır?

Önce kalan uygun mu bak: $\text{der}(2x - 1) = 1 < 2$. Bölme eşitliği:

$$P(x) = (x^2 - 3)(x + 2) + 2x - 1$$

Katsayılar toplamı $P(1)$'dir; açmaya gerek yok:

$$P(1) = (1 - 3)(1 + 2) + 2 - 1 = -6 + 1 = -5$$

İstersen aç ve kontrol et: $P(x) = x^3 + 2x^2 - x - 7$, katsayılar toplamı $1 + 2 - 1 - 7 = -5$.

**Kural.** Bölen, bölüm ve kalan biliniyorsa $P(x)$ de bilinir. $P(1)$, $P(0)$ gibi değerler için eşitliğe doğrudan sayı yaz; **kalanı eklemeyi unutma**.

## Tam bölünme ve bilinmeyen katsayı

**Örnek.** $P(x) = x^3 + ax^2 - 5x + 6$ polinomu $x - 1$ ile tam bölünüyorsa $a$ kaçtır?

Uzun bölmeyi $a$ harfiyle yap:

- $\dfrac{x^3}{x} = x^2$; çarp: $x^3 - x^2$; çıkar: $(a + 1)x^2 - 5x + 6$.
- $\dfrac{(a + 1)x^2}{x} = (a + 1)x$; çarp: $(a + 1)x^2 - (a + 1)x$; çıkar: $(a - 4)x + 6$.
- $\dfrac{(a - 4)x}{x} = a - 4$; çarp: $(a - 4)x - (a - 4)$; çıkar: $6 + a - 4 = a + 2$.

Kalan $a + 2$. Tam bölünme için kalan $0$: $a + 2 = 0$, $a = -2$.

Kontrol: $x^3 - 2x^2 - 5x + 6 = (x - 1)(x^2 - x - 6)$.

**Kural.** "Tam bölünür" demek "kalan sıfırdır" demektir. Kalanı harfle bul, sıfıra eşitle. Kalan birinci dereceden çıkarsa ($mx + n$) iki katsayının da sıfır olması gerekir: $m = 0$ ve $n = 0$.

## ÖSYM tuzakları

> **Çıkarırken yalnızca ilk terimin işaretini değiştirmek:** $(x^2 + 4x - 1) - (x^2 - 2x)$ işleminde sonuç $2x - 1$ değil $6x - 1$'dir. Alttaki satırın **bütün** terimlerinin işareti değişir.

> **Eksik terimi atlamak:** $x^4 - 3x^2 + 2x + 5$ polinomunu bölerken $0x^3$ yazmazsan $x^3$ terimleri $x^2$ sütununa kayar ve bütün sonuç bozulur.

> **Bölümün derecesini bölerek bulmak:** 6. dereceden polinom 2. dereceden polinoma bölünürse bölüm $6 : 2 = 3$. değil, $6 - 2 = 4.$ dereceden olur. Dereceler çıkarılır.

> **Kalanın derecesini bölenle aynı almak:** $x^2 + 1$ ile bölmede $x^2$ ya da $x^2 + 5$ kalan olamaz. Kalanın derecesi bölenin derecesinden **küçük** olmalı; burada kalan en çok $ax + b$ biçimindedir.

> **Bölme eşitliğinde kalanı unutmak:** $P(x) = (x^2 - 3)(x + 2) + 2x - 1$ için $P(1) = -6$ değil $-6 + 1 = -5$'tir.

## Kendini dene

### Soru 1
$P(x)$ polinomu $x^2 + 1$ polinomuna bölünüyor.

Buna göre aşağıdakilerden hangisi bu bölmede elde edilen kalan **olamaz**?

A) $7$
B) $-x$
C) $2x - 3$
D) $x^2$
E) $x + 4$

**Cevap:** D
**Çözüm:** Bölen $x^2 + 1$ ikinci dereceden, bu yüzden kalanın derecesi en çok 1 olabilir: kalan $ax + b$ biçimindedir. $7$, $-x$, $2x - 3$ ve $x + 4$ bu biçime uyar. $x^2$ ikinci dereceden olduğu için kalan olamaz; bölmeye bir tur daha devam edilir.

### Soru 2
$P(x) = x^3 - x^2 + 2x + 5$ polinomunun $x - 1$ ile bölümünden kalan kaçtır?

A) 3
B) 5
C) 7
D) 9
E) 11

**Cevap:** C
**Çözüm:** $\frac{x^3}{x} = x^2$; çarp: $x^3 - x^2$; çıkar: $2x + 5$ (çünkü $-x^2 - (-x^2) = 0$). $\frac{2x}{x} = 2$; çarp: $2x - 2$; çıkar: $5 - (-2) = 7$. Bölüm $x^2 + 2$, kalan 7. Son çıkarmada işaret değiştirmeyi unutan $5 - 2 = 3$, sabit terimi kalan sanan 5 bulur.

### Soru 3
$P(x)$ polinomu $x^2 + 2x$ ile bölündüğünde bölüm $x + 1$, kalan $4x + 3$'tür.

Buna göre $P(x)$ polinomunun katsayılar toplamı kaçtır?

A) 3
B) 6
C) 7
D) 12
E) 13

**Cevap:** E
**Çözüm:** Bölme eşitliği: $P(x) = (x^2 + 2x)(x + 1) + 4x + 3$. Katsayılar toplamı $P(1) = (1 + 2)(1 + 1) + 4 + 3 = 6 + 7 = 13$. Kalanı unutan 6, yalnızca kalanı hesaplayan 7, sabit terimi ($P(0) = 3$) bulan 3 der.

## Özet kartı

- Bölme eşitliği: $P(x) = Q(x) \cdot B(x) + K(x)$ ve $\text{der}[K(x)] < \text{der}[Q(x)]$.
- Uzun bölme: sırala, eksik terime $0$ yaz; sonra böl, çarp, çıkar (bütün işaretleri değiştir).
- $\text{der}[B(x)] = \text{der}[P(x)] - \text{der}[Q(x)]$; bölen birinci dereceden ise kalan sabit sayıdır.
- Tam bölünme: kalan $0$. Kalan $mx + n$ ise $m = n = 0$.
- Bölen, bölüm ve kalan verilirse $P(1)$, $P(0)$ gibi değerleri eşitliğe sayı yazarak bul; kalanı ekle.

## Sonraki adım

Alıştırmaya geç (aşağıdaki düğme). Sonraki ders **Polinomlarda Bölme İşlemi Yapmadan Kalan Bulma**; orada bu dersteki bölme eşitliğine akıllıca $x$ değerleri yazarak kalanı tek satırda bulacaksın.
