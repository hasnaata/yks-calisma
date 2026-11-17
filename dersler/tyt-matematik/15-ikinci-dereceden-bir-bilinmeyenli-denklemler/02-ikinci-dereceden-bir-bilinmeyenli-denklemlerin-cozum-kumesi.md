---
baslik: İkinci Dereceden Bir Bilinmeyenli Denklemlerin Çözüm Kümesi
ders: tyt-matematik
sure: 25 dk
kaynak: MEBİ Konu Özeti 38df35be86
guncelleme: 2026-11-18
---
# İkinci Dereceden Bir Bilinmeyenli Denklemlerin Çözüm Kümesi

<div class="giris" dir="rtl" lang="ar">

**الدرس ده عن إيه؟** عن حل معادلة الدرجة التانية في مجهول واحد (ikinci dereceden denklem)، وإزاي تكتب مجموعة الحل (çözüm kümesi) كاملة من غير ما يضيع منك ولا جذر (kök).

- هتتعلم التحليل للعوامل (çarpanlara ayırma) وتساوي كل عامل بالصفر، حتى لو معامل التربيع مش واحد.
- هتعرف تحل بالجذر التربيعي وبإكمال المربع (tam kareye tamamlama) لما التحليل مايمشيش.
- هتستخدم التعويض بمتغير جديد (değişken değiştirme) في معادلات الدرجة الرابعة، وترجع للمجهول الأصلي في الآخر.

**ليه مهم؟** في TYT ممكن ييجي سؤال مباشر عن مجموعة الحل أو مجموع الجذور، بس الأكتر إن مسألة كلامية عن مساحة أو أعمار أو أعداد تتحول لمعادلة زي دي، وساعتها لازم تشيل الجذر السالب أو الكسري اللي مالوش معنى.

هو ٢٥ دقيقة، وكل طريقة معاها مثال محلول خطوة بخطوة. هات ورقة وقلم وحل معاه.

</div>

**Bu dersin sonunda:** ikinci dereceden bir denklemi çarpanlara ayırarak, karekök alarak, tam kareye tamamlayarak ya da değişken değiştirerek çözebilecek ve çözüm kümesini kök kaybetmeden yazabileceksin.

> **TYT'de yeri:** "Çözüm kümesi nedir?", "büyük kök kaçtır?", "kökler toplamı kaçtır?" soruları doğrudan gelir. Daha sık olanı, bir problemi (alan, yaş, tokalaşma, sayı) denkleme çevirip bu derste öğreneceğin yollarla çözmendir. Problemlerde negatif ya da kesirli kökü elemeyi unutma.

## Önce hatırla

<details><summary>Geçen dersten: $x^2 + kx - 12 = 0$ denkleminin bir kökü $3$ olduğuna göre $k$ kaçtır?</summary>
Kök denklemi sağlar, $x = 3$ yaz: $9 + 3k - 12 = 0$, $3k = 3$, $k = 1$. Denklem $x^2 + x - 12 = 0$ olur; bu derste diğer kökün $-4$ olduğunu çarpanlara ayırarak göreceksin.
</details>

<details><summary>Geçen dersten: $x^2 = 5x$ denkleminin iki tarafını $x$'e bölmek neden yanlıştır?</summary>
Bölünce $x = 5$ kalır ve $x = 0$ kökü kaybolur. Doğrusu her şeyi tek tarafa toplamak: $x^2 - 5x = 0$, $x(x - 5) = 0$, Ç $= \{0, 5\}$.
</details>

## Temel fikir: çarpım sıfırsa

**Örnek.** $(2x - 3)(x + 4) = 0$ denklemini çöz.

İki sayının çarpımı $0$ ise bu sayılardan en az biri $0$'dır. Her çarpanı ayrı ayrı sıfıra eşitle:

- $2x - 3 = 0 \Rightarrow x = \frac{3}{2}$
- $x + 4 = 0 \Rightarrow x = -4$

Ç $= \left\{-4, \frac{3}{2}\right\}$.

**Kural.** Önce denklemi **sağ tarafı $0$** olacak biçime getir, sonra sol tarafı çarpanlara ayır ve her çarpanı sıfıra eşitle. Bu dersteki bütün yöntemler bu tek fikre dayanır.

> **Tuzak:** $(x - 2)(x + 1) = 10$ denkleminde "$x - 2 = 10$ ya da $x + 1 = 10$" yazılamaz; bu kural yalnızca sağ taraf $0$ iken çalışır. Doğrusu: çarpımı aç, $x^2 - x - 2 = 10$, yani $x^2 - x - 12 = 0$, $(x - 4)(x + 3) = 0$, Ç $= \{-3, 4\}$. Kontrol: $2 \cdot 5 = 10$ ve $(-5) \cdot (-2) = 10$.

Hangi yolu seçeceğine denklemin biçimine bakarak karar verirsin:

![Yöntem seçme akışı: denklemi sıfıra eşitle. c sıfırsa x parantezine al. Değilse b sıfırsa x kare eşittir k yazıp artı eksi karekök al. Değilse çarpanlara ayrılıyorsa her çarpanı sıfıra eşitle, ayrılmıyorsa tam kareye tamamla.](gorsel/tyt-matematik/15-02-yontem.svg "Önce eksik terime bak: c ya da b sıfırsa iş bir satırda biter. Üç terim de varsa önce çarpanlara ayırmayı dene.")

## Eksik terimli denklemler

**Örnek 1 ($c = 0$).** $3x^2 - 12x = 0$.

Ortak çarpan $3x$: $3x(x - 4) = 0$. Buradan $x = 0$ ya da $x = 4$. Ç $= \{0, 4\}$.

**Örnek 2 ($b = 0$).** $2x^2 - 18 = 0$.

$2x^2 = 18$, $x^2 = 9$. Karesi $9$ olan **iki** sayı var: $x = 3$ ya da $x = -3$. Ç $= \{-3, 3\}$.

**Örnek 3.** $x^2 + 9 = 0$ ise $x^2 = -9$. Hiçbir gerçek sayının karesi negatif olmaz: Ç $= \varnothing$.

**Kural.**

| Biçim | Çözüm |
|---|---|
| $ax^2 + bx = 0$ | $x(ax + b) = 0$, Ç $= \left\{0, -\frac{b}{a}\right\}$ |
| $x^2 = k$, $k > 0$ | Ç $= \{-\sqrt{k}, \sqrt{k}\}$ |
| $x^2 = 0$ | Ç $= \{0\}$ |
| $x^2 = k$, $k < 0$ | Ç $= \varnothing$ |

## Üç terimli: $x^2 + bx + c = 0$

**Örnek.** $x^2 - 2x - 15 = 0$.

Çarpımı $c = -15$, toplamı $b = -2$ olan iki sayı ara. Çarpım negatif, öyleyse sayılardan biri negatif: $-5$ ve $3$ ($-5 \cdot 3 = -15$, $-5 + 3 = -2$).

$(x - 5)(x + 3) = 0$, yani $x = 5$ ya da $x = -3$. Ç $= \{-3, 5\}$.

**Kural.** $a = 1$ ise çarpımı $c$, toplamı $b$ olan $m$ ve $n$ sayılarını bul: $x^2 + bx + c = (x + m)(x + n)$. Kökler $-m$ ve $-n$'dir; işaret ters döner.

## Üç terimli: $ax^2 + bx + c = 0$, $a \ne 1$

**Örnek.** $2x^2 - 5x - 3 = 0$.

1. $2x^2$'yi iki çarpana böl: $2x$ ve $x$. Sabit terim $-3$'ü iki çarpana böl: deneme ile $+1$ ve $-3$.
2. Çapraz çarp ve topla; orta terimi vermeli.

![Çapraz çarpım şeması: solda alt alta 2x ve x, sağda alt alta artı 1 ve eksi 3. Çapraz çizgiler 2x ile eksi 3'ü ve x ile artı 1'i birleştiriyor. 2x çarpı eksi 3 eksi 6x, x çarpı 1 artı x, toplam eksi 5x.](gorsel/tyt-matematik/15-02-capraz.svg "Çarpımları çapraz al, topla. Toplam orta terime (−5x) eşitse çarpanlar satır satır okunur: (2x + 1) ve (x − 3).")

3. Çarpanları **satır satır** oku: $(2x + 1)(x - 3) = 0$.
4. $2x + 1 = 0 \Rightarrow x = -\frac{1}{2}$; $x - 3 = 0 \Rightarrow x = 3$. Ç $= \left\{-\frac{1}{2}, 3\right\}$.

**Kural.** $ax^2 + bx + c = (px + m)(qx + n)$ ise kökler $-\frac{m}{p}$ ve $-\frac{n}{q}$'dur. Çapraz toplam tutmazsa sabit terimin çarpanlarını yer değiştirerek ya da işaretlerini değiştirerek yeniden dene. Bitirince bir kökü denklemde yerine koyup kontrol et.

## Özdeşlikler: iki kare farkı ve tam kare

**Örnek 1.** $4x^2 - 25 = 0$.

İki kare farkı: $(2x - 5)(2x + 5) = 0$. Ç $= \left\{-\frac{5}{2}, \frac{5}{2}\right\}$.

**Örnek 2.** $x^2 - 6x + 9 = 0$.

Tam kare: $(x - 3)^2 = 0$, yani $(x - 3)(x - 3) = 0$. İki çarpan da aynı kökü verir: Ç $= \{3\}$. Böyle köke **çift katlı kök** denir; çözüm kümesine **bir kez** yazılır.

**Örnek 3.** $(x + 1)^2 = 9$.

Karesi $9$ olan sayılar $3$ ve $-3$: $x + 1 = 3$ ya da $x + 1 = -3$. Ç $= \{-4, 2\}$.

**Kural.** $(\dots)^2 = k$ biçiminde, $k > 0$ ise parantezin içi $\sqrt{k}$ **ya da** $-\sqrt{k}$'dır. Eksi tarafı unutan kökün birini kaybeder.

## Tam kareye tamamlama

Çarpımı $c$, toplamı $b$ olan tam sayılar bulunamıyorsa denklemi tam kareye çevir.

**Örnek.** $x^2 + 6x + 4 = 0$.

1. Sabit terimi sağa at: $x^2 + 6x = -4$.
2. $x$'in katsayısının yarısının karesini iki tarafa ekle: $\left(\frac{6}{2}\right)^2 = 9$. $x^2 + 6x + 9 = 5$.
3. Sol taraf tam kare: $(x + 3)^2 = 5$.
4. $x + 3 = \sqrt{5}$ ya da $x + 3 = -\sqrt{5}$.

Ç $= \{-3 - \sqrt{5}, -3 + \sqrt{5}\}$.

**Kural.** $x^2 + bx$ ifadesine $\left(\frac{b}{2}\right)^2$ eklenince $\left(x + \frac{b}{2}\right)^2$ olur. Eklediğin sayıyı **öbür tarafa da** ekle. Sağda negatif sayı kalırsa gerçek kök yoktur. ($a \ne 1$ ise önce bütün denklemi $a$'ya böl.)

## Değişken değiştirme

**Örnek.** $x^4 - 10x^2 + 9 = 0$.

Denklem dördüncü dereceden ama yalnızca $x^4 = (x^2)^2$ ve $x^2$ içeriyor. $x^2 = t$ de:

1. $t^2 - 10t + 9 = 0$, $(t - 1)(t - 9) = 0$, $t = 1$ ya da $t = 9$.
2. **Geri dön:** $x^2 = 1 \Rightarrow x = \pm 1$; $x^2 = 9 \Rightarrow x = \pm 3$.

Ç $= \{-3, -1, 1, 3\}$.

![y eşittir x üzeri 4 eksi 10 x kare artı 9 grafiği, x eksenini eksi 3, eksi 1, 1 ve 3 noktalarında kesiyor.](gorsel/tyt-matematik/15-02-dort-kok.svg "Her t değeri iki x değeri verdi: t = 1 için ±1, t = 9 için ±3. Grafik ekseni dört yerde kesiyor.")

**Örnek.** $x^4 + 3x^2 - 4 = 0$ için $x^2 = t$: $t^2 + 3t - 4 = 0$, $(t + 4)(t - 1) = 0$. $t = -4$ olamaz, çünkü $t = x^2 \ge 0$. Yalnızca $x^2 = 1$: Ç $= \{-1, 1\}$.

**Kural.** Tekrar eden bir ifade ($x^2$, $x + 2$, $x^2 - 2x$ gibi) gördüğünde ona $t$ de, $t$'yi bul, sonra **$x$'e geri dön**. $t = x^2$ ise negatif $t$ değerini ele.

## ÖSYM tuzakları

> **Sağ taraf sıfır değilken çarpanları eşitlemek:** $(x - 2)(x + 1) = 10$ için $x = 12$ ya da $x = 9$ yazmak yanlıştır. Önce açıp sıfıra eşitle.

> **Karekökte eksiyi unutmak:** $x^2 = 16$ ise Ç $= \{4\}$ değil $\{-4, 4\}$'tür. Aynısı $(x - 3)^2 = 16$ için de geçerli: $x - 3 = \pm 4$.

> **Kökün işaretini çarpandan okumak:** $(x - 5)(x + 3) = 0$ denkleminin kökleri $-5$ ve $3$ değil, $5$ ve $-3$'tür. Her çarpanı gerçekten sıfıra eşitle.

> **$t$'de kalmak:** Değişken değiştirdikten sonra $t$ değerlerini cevap sanma. Soru $x$'i soruyor; geri dönmeyi ve $t = x^2 < 0$ olanları elemeyi unutma.

> **Problemde anlamsız kökü bırakmak:** Uzunluk, kişi sayısı, yaş negatif olamaz. Denklemin iki kökü olsa bile problemin cevabı çoğu zaman tektir.

## Kendini dene

### Soru 1
$x^2 + 2x - 24 = 0$ denkleminin çözüm kümesi aşağıdakilerden hangisidir?

A) $\{-4, 6\}$
B) $\{-6, 4\}$
C) $\{-8, 3\}$
D) $\{-3, 8\}$
E) $\{4, 6\}$

**Cevap:** B
**Çözüm:** Çarpımı $-24$, toplamı $2$ olan sayılar $6$ ve $-4$: $(x + 6)(x - 4) = 0$. Kökler $x = -6$ ve $x = 4$. A, kökleri çarpandaki işaretle okumaktır ($x + 6$ çarpanından $6$ değil, $-6$ çıkar). C ve D'de çarpım $-24$ ama toplam $\pm 5$ olur.

### Soru 2
$(x - 3)^2 = 16$ denkleminin köklerinin toplamı kaçtır?

A) $-6$
B) $-1$
C) $3$
D) $6$
E) $7$

**Cevap:** D
**Çözüm:** $x - 3 = 4$ ya da $x - 3 = -4$. Buradan $x = 7$ ya da $x = -1$; toplam $7 + (-1) = 6$. Eksi tarafı unutan yalnızca $7$'yi (E) bulur; B ise yalnızca diğer kök $-1$'dir.

### Soru 3
$x^4 - 3x^2 - 4 = 0$ denkleminin gerçek sayılardaki çözüm kümesi aşağıdakilerden hangisidir?

A) $\{-2, 2\}$
B) $\{-1, 4\}$
C) $\{2\}$
D) $\{-2, -1, 1, 2\}$
E) $\{-4, 1\}$

**Cevap:** A
**Çözüm:** $x^2 = t$ de: $t^2 - 3t - 4 = 0$, $(t - 4)(t + 1) = 0$, $t = 4$ ya da $t = -1$. $x^2 = -1$ gerçek sayılarda olmaz. $x^2 = 4 \Rightarrow x = \pm 2$. B, $t$ değerlerinde kalmaktır; C eksi kökü unutmaktır; D, $t = -1$'i de kabul etmektir.

## Özet kartı

- Önce sağ tarafı $0$ yap; çarpım sıfırsa her çarpan ayrı ayrı sıfıra eşitlenir.
- $c = 0$: $x$ parantezine al, bir kök hep $0$. $b = 0$: $x^2 = k$, iki kök $\pm\sqrt{k}$ (ya da hiç).
- $x^2 + bx + c$: çarpımı $c$, toplamı $b$ olan sayılar; kökler bu sayıların ters işaretlisi.
- $a \ne 1$: çapraz çarpım; çarpanları satır satır oku.
- Ayrılmıyorsa tam kareye tamamla: $\left(\frac{b}{2}\right)^2$'yi iki tarafa ekle.
- Değişken değiştirince $x$'e geri dön; $x^2 = t$ ise $t < 0$ olanı ele.

## Sonraki adım

Alıştırmaya geç (aşağıdaki düğme). Sonraki ders **Diskriminant Kavramı ve Diskriminantın Kullanılması**; denklemi çözmeden kaç gerçek kökü olduğunu tek bir hesapla bulacak ve tam kareye tamamlamanın genel formüle nasıl dönüştüğünü göreceksin.
