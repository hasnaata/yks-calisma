---
baslik: Tam Küp, İki Küp Toplamı ve Farkı ile Çarpanlara Ayırma
ders: tyt-matematik
sure: 20 dk
kaynak: MEBİ Konu Özeti c49f4ae1ab
guncelleme: 2026-11-18
---
# Tam Küp, İki Küp Toplamı ve Farkı ile Çarpanlara Ayırma

<div class="giris" dir="rtl" lang="ar">

**الدرس ده عن إيه؟** عن التحليل باستخدام التكعيب: مكعب مجموع حدّين أو الفرق بينهم (tam küp)، ومجموع مكعبين والفرق بين مكعبين (iki küp toplamı ve farkı).

- هتحفظ فك مكعب المجموع والفرق، والمعاملات اللي بتمشي 1 و 3 و 3 و 1، وتعرف تشوف المقدار ده من غير ما تفكّه.
- هتحلّل مجموع مكعبين والفرق بينهم بقاعدة الإشارات السهلة: نفس الإشارة، عكسها، وبعدين موجب على طول.
- هتعرف تطلع قيمة مجموع المكعبات لو معاك المجموع وحاصل الضرب، وتختصر كسور وحسابات بأرقام كبيرة.

**ليه مهم؟** في TYT بييجي سؤال "أنهي واحد من دول عامل (çarpan) للمقدار؟" أو اختصار كسر أو حساب سريع، وهنا الحفظ الصح للقاعدة بيوفّر عليك وقت كتير.

الدرس ٢٠ دقيقة، وأغلبه أمثلة محلولة خطوة بخطوة. خد نفسك وابدأ.

</div>

**Bu dersin sonunda:** $(a \pm b)^3$ açılımını ve $a^3 \pm b^3$ kalıbını bir ifadede tanıyıp çarpanlarına ayırabilecek, "$a + b$ ile $ab$ verilmiş, $a^3 + b^3$ kaçtır?" sorularını tek satırda çözebileceksin.

> **TYT'de yeri:** "Aşağıdakilerden hangisi bu ifadenin bir çarpanıdır?", küplü kesirleri sadeleştirme, "$x + \frac{1}{x}$ verilmiş, $x^3 + \frac{1}{x^3}$ kaçtır?" ve büyük sayılarla verilen "kafadan hesapla" soruları bu dersin kalıplarıdır. Küp kalıpları kare kalıplarından daha az gelir ama geldiğinde ezber gerektirir.

## Önce hatırla

<details><summary>Tam kare: $x^2 - 14x + 49$ ifadesini çarpanlarına ayır.</summary>
$x^2 = x \cdot x$, $49 = 7^2$. Orta terim kontrolü: $2 \cdot x \cdot 7 = 14x$, işareti eksi. Sonuç $(x - 7)^2$.
</details>

<details><summary>İki kare farkı: $97^2 - 3^2$ işlemini kafadan yap.</summary>
$97^2 - 3^2 = (97 - 3)(97 + 3) = 94 \cdot 100 = 9400$.
</details>

## İki terimin toplamının küpü

**Örnek.** $(x + 2)^3$ ifadesini aç. Küp, üç kez çarpmaktır; önce kareyi al, sonra bir kez daha çarp:

$$(x + 2)^3 = (x + 2)(x^2 + 4x + 4) = x^3 + 4x^2 + 4x + 2x^2 + 8x + 8 = x^3 + 6x^2 + 12x + 8$$

Katsayılara bak: $x^3$, $3 \cdot x^2 \cdot 2 = 6x^2$, $3 \cdot x \cdot 2^2 = 12x$, $2^3 = 8$. Kalıp $1, 3, 3, 1$.

**Kural.**

$$(a + b)^3 = a^3 + 3a^2b + 3ab^2 + b^3$$

Bu kalıp bir küpün hacmidir: kenarı $a + b$ olan küp, her kenarı $a$ ve $b$ diye bölünürse 8 parçaya ayrılır.

![Kenarı a artı b olan küp, aralarında boşluk bırakılarak sekiz kutuya ayrılmış. Bir büyük mavi küp a küp, üç yeşil kutu a kare b, üç sarı kutu a b kare, bir küçük kırmızı küp b küp. Yanda renklere göre sayılar: 1, 3, 3, 1.](gorsel/tyt-matematik/14-03-kup-parcalari.svg "Parçaları renklerine göre say: 1 büyük küp, 3 yeşil, 3 sarı, 1 küçük küp. Katsayılardaki 1, 3, 3, 1 buradan gelir. Bir yeşil kutu arkada kaldığı için görünmüyor.")

## İki terimin farkının küpü

**Örnek.** $(2x - 1)^3$ ifadesini aç. Kalıba $a = 2x$, $b = 1$ yaz; eksi işareti $b$'nin tek kuvvetlerinde çıkar:

$$(2x - 1)^3 = (2x)^3 - 3(2x)^2 \cdot 1 + 3 \cdot 2x \cdot 1^2 - 1^3 = 8x^3 - 12x^2 + 6x - 1$$

**Kural.**

$$(a - b)^3 = a^3 - 3a^2b + 3ab^2 - b^3$$

İşaretler $+, -, +, -$ diye sırayla değişir.

**Tersinden: tam küpü tanımak.** $x^3 - 9x^2 + 27x - 27$ verilsin.

1. Dört terim var, uçlar küp: $x^3$ ve $27 = 3^3$. Kökler $x$ ve $3$.
2. İkinci terim: $3 \cdot x^2 \cdot 3 = 9x^2$. Üçüncü terim: $3 \cdot x \cdot 3^2 = 27x$. İkisi de tuttu.
3. İşaretler $+, -, +, -$ olduğu için sonuç $(x - 3)^3$.

> **Tuzak:** $(a + b)^3 \ne a^3 + b^3$. Küpü terimlere dağıtırsan ortadaki $3a^2b + 3ab^2$ kaybolur. Örneğin $(1 + 1)^3 = 8$ ama $1^3 + 1^3 = 2$.

## İki küp toplamı ve farkı

**Örnek.** $(x + 2)(x^2 - 2x + 4)$ çarpımını yap:

$$x^3 - 2x^2 + 4x + 2x^2 - 4x + 8 = x^3 + 8$$

Ortadaki terimler birbirini götürdü, geriye yalnızca iki küp kaldı. Tersinden: $x^3 + 8 = x^3 + 2^3$ görürsen $(x + 2)(x^2 - 2x + 4)$ yazarsın.

**Kural.**

$$a^3 + b^3 = (a + b)(a^2 - ab + b^2) \qquad a^3 - b^3 = (a - b)(a^2 + ab + b^2)$$

İşaretleri ezberlemenin kolay yolu: ilk parantez **aynı** işareti alır, ortadaki $ab$ **ters** işareti alır, $b^2$ **hep artıdır**.

![İki satır: a küp artı b küp eşittir a artı b çarpı a kare eksi ab artı b kare; a küp eksi b küp eşittir a eksi b çarpı a kare artı ab artı b kare. Parantez içindeki işaretlerin altında aynı, ters ve hep artı etiketleri var.](gorsel/tyt-matematik/14-03-isaret-kalibi.svg "Soldaki işaret ilk paranteze aynen geçer, ab'nin önüne tersi gelir, b²'nin önü her zaman artıdır.")

**Daha fazla örnek.**

| İfade | Küpler | Çarpanlar |
|---|---|---|
| $27x^3 - 1$ | $(3x)^3 - 1^3$ | $(3x - 1)(9x^2 + 3x + 1)$ |
| $8a^3 + 125$ | $(2a)^3 + 5^3$ | $(2a + 5)(4a^2 - 10a + 25)$ |
| $x^3 - 64$ | $x^3 - 4^3$ | $(x - 4)(x^2 + 4x + 16)$ |

İkinci parantezdeki $a^2 \pm ab + b^2$ gerçek sayılarda bir daha ayrılmaz; orada dur.

> **Tuzak:** İkinci parantezin ortasında $ab$ vardır, $2ab$ **değil**. $x^3 - 8 = (x - 2)(x^2 + 2x + 4)$'tür; $(x - 2)(x^2 + 4x + 4)$ yazarsan tam kareyle karıştırmış olursun.

## Önce ortak çarpan, sonra kalıp

**Örnek.** $2x^4 - 16x$ ifadesini çarpanlarına ayır.

1. Ortak çarpan: $2x(x^3 - 8)$.
2. Parantez küp farkı: $x^3 - 8 = (x - 2)(x^2 + 2x + 4)$.
3. Sonuç: $2x(x - 2)(x^2 + 2x + 4)$.

**Örnek.** $x^6 - 1$ hem kare farkı ($(x^3)^2 - 1^2$) hem küp farkıdır ($(x^2)^3 - 1^3$). Önce **kare farkı** ile başla, daha çok parçaya ayrılır:

$$x^6 - 1 = (x^3 - 1)(x^3 + 1) = (x - 1)(x^2 + x + 1)(x + 1)(x^2 - x + 1)$$

![Yöntem akışı: önce ortak çarpanı al; iki terim kaldıysa kare mi küp mü diye bak, kareyse iki kare farkı, küpse küp toplamı ya da farkı; dört terim kaldıysa katsayılar 1, 3, 3, 1 kalıbında mı diye bak ve tam küp yaz; sonunda çarpanları yine yokla.](gorsel/tyt-matematik/14-03-yontem.svg "Terim sayısı kalıbı seçer: iki terimde kare ya da küp farkı, dört terimde tam küp.")

**Kesir sadeleştirme.** $x \ne \pm 2$ için

$$\frac{x^3 - 8}{x^2 - 4} = \frac{(x - 2)(x^2 + 2x + 4)}{(x - 2)(x + 2)} = \frac{x^2 + 2x + 4}{x + 2}$$

## Değer bulma

Tam küp açılımı ortak çarpanla düzenlenirse iki kullanışlı eşitlik çıkar:

$$a^3 + b^3 = (a + b)^3 - 3ab(a + b) \qquad a^3 - b^3 = (a - b)^3 + 3ab(a - b)$$

**Örnek.** $a + b = 4$ ve $ab = 3$ ise $a^3 + b^3$ kaçtır?

$a^3 + b^3 = 4^3 - 3 \cdot 3 \cdot 4 = 64 - 36 = 28$. Kontrol: sayılar $1$ ve $3$; $1 + 27 = 28$.

**Örnek.** $x + \dfrac{1}{x} = 3$ ise $x^3 + \dfrac{1}{x^3}$ kaçtır?

Burada $a = x$, $b = \frac{1}{x}$ ve $ab = 1$. Sonuç: $3^3 - 3 \cdot 1 \cdot 3 = 27 - 9 = 18$.

**Sayılarla pratik hesap.** $\dfrac{37^3 + 13^3}{50}$ işleminde $37 + 13 = 50$ olduğunu fark et:

$$\frac{(37 + 13)(37^2 - 37 \cdot 13 + 13^2)}{50} = 1369 - 481 + 169 = 1057$$

## ÖSYM tuzakları

> **Küpü dağıtmak:** $(x + 2)^3 = x^3 + 8$ değildir. Doğrusu $x^3 + 6x^2 + 12x + 8$; ortadaki iki terim unutulmaz.

> **3 katsayısını unutmak:** $(x + 3)^3$ açılımında ikinci terim $3 \cdot x^2 \cdot 3 = 9x^2$'dir, $3x^2$ değil. Katsayılar $1, 3, 3, 1$.

> **İkinci parantezde $2ab$ yazmak:** $a^3 - b^3 = (a - b)(a^2 + ab + b^2)$. Ortada tek $ab$ vardır; $2ab$ tam kareye aittir.

> **İşaretleri karıştırmak:** $a^3 + b^3$ ifadesinde ikinci parantez $a^2 - ab + b^2$ olur. Kural: aynı, ters, hep artı.

> **Değer bulmada $3ab(a + b)$'yi eksik çıkarmak:** $a^3 + b^3 = (a + b)^3 - 3ab(a + b)$. Yalnızca $3ab$ ya da yalnızca $ab(a + b)$ çıkarmak yanlış sonuç verir.

## Kendini dene

### Soru 1
$125x^3 + 1$ ifadesinin çarpanlarına ayrılmış biçimi aşağıdakilerden hangisidir?

A) $(5x + 1)^3$
B) $(5x + 1)(25x^2 + 5x + 1)$
C) $(5x + 1)(25x^2 - 5x + 1)$
D) $(5x - 1)(25x^2 + 5x + 1)$
E) $(5x + 1)(25x^2 - 10x + 1)$

**Cevap:** C
**Çözüm:** $125x^3 = (5x)^3$, $1 = 1^3$. Küp toplamı: $(5x + 1)\big((5x)^2 - 5x \cdot 1 + 1^2\big) = (5x + 1)(25x^2 - 5x + 1)$. B seçeneğinde ortadaki işaret ters olmamış, E seçeneğinde $ab$ yerine $2ab$ yazılmış, A seçeneği ise tam küptür ve açılınca ortada terimler çıkar.

### Soru 2
$x^3 - 6x^2 + 12x - 8$ ifadesinin $x = 12$ için değeri kaçtır?

A) 8
B) 100
C) 512
D) 1000
E) 1728

**Cevap:** D
**Çözüm:** Uçlar $x^3$ ve $2^3$; $3 \cdot x^2 \cdot 2 = 6x^2$ ve $3 \cdot x \cdot 2^2 = 12x$. İşaretler $+, -, +, -$ olduğundan ifade $(x - 2)^3$'tür. $x = 12$ için $10^3 = 1000$. $1728 = 12^3$ yalnızca ilk terimdir; $100$ ise küp yerine kare almaktır.

### Soru 3
$a + b = 5$ ve $ab = 4$ olduğuna göre $a^3 + b^3$ kaçtır?

A) 65
B) 85
C) 105
D) 125
E) 185

**Cevap:** A
**Çözüm:** $a^3 + b^3 = (a + b)^3 - 3ab(a + b) = 125 - 3 \cdot 4 \cdot 5 = 125 - 60 = 65$. Kontrol: sayılar $1$ ve $4$; $1 + 64 = 65$. $125$ çıkarmayı unutmak, $185$ çıkarmak yerine eklemek, $105$ ise $ab$'nin işaretini karıştırmaktır ($5 \cdot 21$).

## Özet kartı

- $(a + b)^3 = a^3 + 3a^2b + 3ab^2 + b^3$; katsayılar $1, 3, 3, 1$.
- $(a - b)^3 = a^3 - 3a^2b + 3ab^2 - b^3$; işaretler sırayla değişir.
- $a^3 + b^3 = (a + b)(a^2 - ab + b^2)$, $a^3 - b^3 = (a - b)(a^2 + ab + b^2)$: aynı, ters, hep artı.
- İkinci parantezin ortasında $ab$ vardır, $2ab$ değil; bu parantez bir daha ayrılmaz.
- Sıra: önce ortak çarpan; $x^6 - 1$ gibi ifadelerde önce kare farkı.
- $a^3 + b^3 = (a + b)^3 - 3ab(a + b)$.

## Sonraki adım

Alıştırmaya geç (aşağıdaki düğme). Sonraki ders **Üç Terimli İfadelerin Çarpanlarına Ayrılması**; $x^2 + bx + c$ biçimindeki ifadeleri iki çarpana ayıracaksın.
