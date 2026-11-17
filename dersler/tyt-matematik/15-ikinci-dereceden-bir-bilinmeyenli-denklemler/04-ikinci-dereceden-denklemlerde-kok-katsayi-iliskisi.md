---
baslik: İkinci Dereceden Denklemlerde Kök-Katsayı İlişkisi
ders: tyt-matematik
sure: 22 dk
kaynak: MEBİ Konu Özeti a0df19a8b4
guncelleme: 2026-11-18
---
# İkinci Dereceden Denklemlerde Kök-Katsayı İlişkisi

<div class="giris" dir="rtl" lang="ar">

**الدرس ده عن إيه؟** عن العلاقة بين الجذور والمعاملات (kök-katsayı ilişkisi) في معادلة الدرجة التانية: إزاي تعرف حاجات كتير عن الجذرين من غير ما تحل المعادلة أصلًا.

- هتعرف تطلّع مجموع الجذرين (kökler toplamı) وحاصل ضربهم (kökler çarpımı) من المعاملات على طول.
- هتتعلم تكوّن المعادلة لو عندك جذريها، وتحسب مقادير زي مجموع مربعي الجذرين من المجموع والضرب بس.
- هتحل أسئلة فيها شرط على الجذور، زي إن جذر يبقى 3 أضعاف التاني، أو إن الجذرين أطوال أضلاع مستطيل.

**ليه مهم؟** في TYT أسئلة الموضوع ده ليها قوالب ثابتة بتتكرر، وأغلب الغلط بيبقى في إشارة السالب في المجموع أو إنك تنسى تقسم على المعامل الأول.

هما 22 دقيقة بس، وهتطلع منهم بطريقة توفر عليك وقت كبير في الامتحان. يلا بينا.

</div>

**Bu dersin sonunda:** kökleri hiç bulmadan köklerin toplamını ve çarpımını katsayılardan okuyabilecek, kökleri verilen denklemi kurabilecek ve $x_1^2 + x_2^2$, $\frac{1}{x_1} + \frac{1}{x_2}$ gibi ifadeleri yalnızca toplam ve çarpımla hesaplayabileceksin.

> **TYT'de yeri:** "Kökler toplamı kaçtır?", "kökleri $-2$ ve $5$ olan denklem hangisidir?", "$x_1^2 + x_2^2$ kaçtır?" ve "bir kökü diğerinin 3 katı olduğuna göre $m$ kaçtır?" kalıpları gelir. Kökler bir dikdörtgenin kenarları olarak da verilebilir; çevre, alan ve köşegen yine toplam ile çarpımdan bulunur.

## Önce hatırla

<details><summary>Geçen dersten: $x^2 - 6x + k = 0$ denkleminin çakışık iki kökü olduğuna göre $k$ kaçtır? Kök kaçtır?</summary>
Çakışık kök için $\Delta = 0$: $(-6)^2 - 4 \cdot 1 \cdot k = 36 - 4k = 0$, $k = 9$. Denklem $x^2 - 6x + 9 = (x - 3)^2 = 0$, çakışık kök $x = 3$ (formülle $-\frac{b}{2a} = \frac{6}{2} = 3$).
</details>

<details><summary>Geçen dersten: $2x^2 + 3x + 5 = 0$ denkleminin kaç gerçek kökü vardır?</summary>
$\Delta = 3^2 - 4 \cdot 2 \cdot 5 = 9 - 40 = -31 < 0$. Gerçek kökü <b>yoktur</b>, Ç $= \varnothing$. Bu derste kökler toplamını katsayılardan okuyacaksın; ama önce böyle bir denklemde gerçek kök olmadığını görmen gerekir.
</details>

## Kökler toplamı ve çarpımı

**Örnek.** $2x^2 - 7x + 3 = 0$ denkleminin köklerinin toplamını ve çarpımını bul.

1. Önce kökleri bularak yap: $(2x - 1)(x - 3) = 0$, kökler $x_1 = \frac{1}{2}$ ve $x_2 = 3$.
2. Toplam: $\frac{1}{2} + 3 = \frac{7}{2}$. Çarpım: $\frac{1}{2} \cdot 3 = \frac{3}{2}$.
3. Şimdi katsayılara bak: $a = 2$, $b = -7$, $c = 3$. $-\frac{b}{a} = \frac{7}{2}$ ve $\frac{c}{a} = \frac{3}{2}$. Aynı sonuçlar.

**Neden böyle?** Kök formülünde $x_1 = \frac{-b + \sqrt{\Delta}}{2a}$ ve $x_2 = \frac{-b - \sqrt{\Delta}}{2a}$. Toplarken $+\sqrt{\Delta}$ ile $-\sqrt{\Delta}$ birbirini götürür: $x_1 + x_2 = \frac{-2b}{2a} = -\frac{b}{a}$. Çarpınca iki kare farkı çıkar: $x_1 \cdot x_2 = \frac{b^2 - \Delta}{4a^2} = \frac{b^2 - (b^2 - 4ac)}{4a^2} = \frac{4ac}{4a^2} = \frac{c}{a}$.

**Kural.** $a \ne 0$ olmak üzere $ax^2 + bx + c = 0$ denkleminin kökleri $x_1$ ve $x_2$ ise

$$x_1 + x_2 = -\frac{b}{a} \qquad x_1 \cdot x_2 = \frac{c}{a}$$

Toplamda eksi işareti **var**, çarpımda **yok**. İkisinde de bölen $a$'dır.

![Bir parabol x eksenini x1 eşittir yarım ve x2 eşittir 3 noktalarında kesiyor. Aralarındaki orta nokta 7 bölü 4'te kesikli dikey çizgiyle gösterilmiş. Altta x1 artı x2 eşittir 7 bölü 2 eşittir eksi b bölü a yazıyor.](gorsel/tyt-matematik/15-04-kok-ortasi.svg "y = 2x² − 7x + 3 grafiği. Kökler orta noktaya eşit uzaklıktadır; orta nokta toplamın yarısıdır: −b/2a. Δ = 0 iken iki kök bu noktada birleşir; geçen dersteki çakışık kök formülü buradan gelir.")

**Kısa yol.** $3x^2 + 5x - 7 = 0$ için hesap yapmadan: $x_1 + x_2 = -\frac{5}{3}$, $x_1 \cdot x_2 = -\frac{7}{3}$. Çarpım negatifse kökler **ters işaretlidir** (biri pozitif, biri negatif). Geçen dersteki "$a$ ile $c$ ters işaretliyse iki farklı kök vardır" kuralı da buradan görülür.

## Kökleri verilen denklemi kurmak

**Örnek.** Kökleri $-2$ ve $5$ olan ikinci dereceden denklemi yaz.

1. Toplam: $T = -2 + 5 = 3$.
2. Çarpım: $Ç = (-2) \cdot 5 = -10$.
3. $x^2 - Tx + Ç = 0$ biçimine yerleştir: $x^2 - 3x - 10 = 0$.

Kontrol: $(x + 2)(x - 5) = x^2 - 3x - 10$. Tuttu.

**Örnek.** Kökleri $2 + \sqrt{3}$ ve $2 - \sqrt{3}$ olan denklemi yaz.

$T = 4$ (köklü kısımlar götürür). $Ç = 2^2 - (\sqrt{3})^2 = 4 - 3 = 1$. Denklem $x^2 - 4x + 1 = 0$. Geçen derste kök formülüyle çözdüğün denklem tam olarak buydu.

**Kural.** Kökleri $x_1$ ve $x_2$ olan denklem

$$x^2 - (x_1 + x_2)\,x + x_1 \cdot x_2 = 0, \qquad \text{yani} \qquad x^2 - Tx + Ç = 0$$

Bu denklemi sıfırdan farklı bir sayıyla çarpmak kökleri değiştirmez. Kökler kesirliyse paydaları yok etmek için genişlet: kökleri $\frac{1}{2}$ ve $3$ olan denklem $x^2 - \frac{7}{2}x + \frac{3}{2} = 0$, yani $2x^2 - 7x + 3 = 0$.

## Kökleri bulmadan ifade hesaplamak

**Örnek.** $x^2 - 5x + 3 = 0$ denkleminin kökleri $x_1$ ve $x_2$'dir. Kökler $\frac{5 \pm \sqrt{13}}{2}$ gibi uğraştırıcı sayılardır; onları hiç yazmadan şunları bul.

Önce $T = x_1 + x_2 = 5$, $Ç = x_1 \cdot x_2 = 3$.

- $x_1^2 + x_2^2$: $(x_1 + x_2)^2 = x_1^2 + 2x_1x_2 + x_2^2$ olduğundan $x_1^2 + x_2^2 = T^2 - 2Ç = 25 - 6 = 19$.
- $\frac{1}{x_1} + \frac{1}{x_2}$: paydaları eşitle, $\frac{x_1 + x_2}{x_1 x_2} = \frac{T}{Ç} = \frac{5}{3}$.
- $x_1^2 x_2 + x_1 x_2^2$: ortak çarpan $x_1x_2$, $Ç \cdot T = 3 \cdot 5 = 15$.
- $(x_1 - x_2)^2 = T^2 - 4Ç = 25 - 12 = 13$.

**Kural.** İfadeyi önce $T$ ve $Ç$ cinsinden yaz, sonra sayıları yerleştir.

| İfade | $T$ ve $Ç$ ile |
|---|---|
| $x_1^2 + x_2^2$ | $T^2 - 2Ç$ |
| $\frac{1}{x_1} + \frac{1}{x_2}$ | $\frac{T}{Ç}$ |
| $x_1^2 x_2 + x_1 x_2^2$ | $Ç \cdot T$ |
| $(x_1 - x_2)^2$ | $T^2 - 4Ç$ |
| $(x_1 + 1)(x_2 + 1)$ | $Ç + T + 1$ |

![Akış: Soruda ne verilmiş? Kökler verilmişse x kare eksi Tx artı Ç eşittir 0 kur. Katsayılar verilmişse T eşittir eksi b bölü a, Ç eşittir c bölü a bul, sonra ifadeyi T ve Ç ile yaz. Köklerle ilgili bir koşul verilmişse koşulu T ve Ç ile birlikte çöz.](gorsel/tyt-matematik/15-04-yontem.svg "Bu dersteki her soru üç yoldan birine girer. Ortadaki yolda kökleri bulmaya hiç gerek yoktur.")

## Köklerle ilgili koşul verilirse

**Örnek.** $x^2 + kx - 6 = 0$ denkleminin bir kökü $2$'dir. $k$ ve diğer kök kaçtır?

1. Kök, denklemi sağlar: $2^2 + 2k - 6 = 0$, $2k = 2$, $k = 1$.
2. Diğer kökü çarpımdan bul: $2 \cdot x_2 = \frac{-6}{1}$, $x_2 = -3$.
3. Kontrol: toplam $2 + (-3) = -1 = -\frac{k}{1}$. Tuttu.

**Örnek.** $x^2 - 10x + m = 0$ denkleminin köklerinden biri diğerinin 4 katıdır. $m$ kaçtır?

1. Kökler $x_2$ ve $4x_2$ olsun. Toplam: $x_2 + 4x_2 = 10$, $x_2 = 2$; diğer kök $8$.
2. Çarpım: $m = 2 \cdot 8 = 16$.
3. Kontrol: $\Delta = 100 - 64 = 36 > 0$, iki farklı kök gerçekten var.

**Kural.** Koşulu kökler cinsinden yaz, toplam ya da çarpım denklemiyle birlikte çöz. Sık gelen koşullar:

| Koşul | Anlamı |
|---|---|
| Kökler ters işaretli | $Ç < 0$, yani $a$ ile $c$ ters işaretli |
| Kökler birbirinin ters işaretlisi ($x_1 = -x_2$) | $T = 0$, yani $b = 0$ |
| Kökler çarpmaya göre birbirinin tersi ($x_1 \cdot x_2 = 1$) | $Ç = 1$, yani $c = a$ |

**Kökler bir uzunluksa.** Bir dikdörtgenin kenar uzunlukları $x^2 - 7x + 11 = 0$ denkleminin kökleridir. Kenarları bulmadan:

- Çevre $= 2(x_1 + x_2) = 2 \cdot 7 = 14$.
- Alan $= x_1 \cdot x_2 = 11$.
- Köşegen: Pisagor'dan $d^2 = x_1^2 + x_2^2 = T^2 - 2Ç = 49 - 22 = 27$, $d = 3\sqrt{3}$.

![Kenarları x1 ve x2 olan dikdörtgen; bir köşeden karşı köşeye kesikli çizgiyle d köşegeni çizilmiş.](gorsel/tyt-matematik/15-04-dikdortgen.svg "Kenarlar yaklaşık 4,6 ve 2,4 birimdir; ama soru için bu sayılara gerek yok. Köşegenin karesi kenarların kareleri toplamıdır: T² − 2Ç.")

## ÖSYM tuzakları

> **Toplamda işareti unutmak:** $x^2 - 7x + 12 = 0$ için $x_1 + x_2 = -\frac{-7}{1} = 7$'dir, $-7$ değil. Eksi işareti yalnızca toplamda var; çarpım $\frac{c}{a} = 12$.

> **$a$'ya bölmeyi unutmak:** $3x^2 - 12x - 5 = 0$ denkleminde toplam $12$ değil $\frac{12}{3} = 4$'tür. $a = 1$ değilse her iki formülde de $a$'ya böl.

> **Denklem kurarken işaret:** Kökleri $-2$ ve $5$ olan denklem $x^2 - 3x - 10 = 0$'dır. $T$ önüne eksi gelir; $x^2 + 3x - 10 = 0$ yazan kökleri $2$ ve $-5$ olan denklemi yazmış olur.

> **$x_1^2 + x_2^2 \ne T^2$:** $(x_1 + x_2)^2$ açılınca $2x_1x_2$ çıkar. $x^2 - 5x + 3 = 0$ için cevap $25$ değil $25 - 6 = 19$.

> **Önce Δ'ya bak:** $x^2 + x + 5 = 0$ denkleminde $\Delta = -19 < 0$; gerçek kök yoktur, "gerçek köklerin toplamı $-1$" demek yanlıştır. $x^2 - 6x + 9 = 0$ denkleminde $\Delta = 0$; çözüm kümesi $\{3\}$'tür. "Çözüm kümesinin elemanları toplamı" sorulursa cevap $6$ değil $3$'tür.

## Kendini dene

### Soru 1
$2x^2 + 8x - 5 = 0$ denkleminin kökleri $x_1$ ve $x_2$ olduğuna göre $x_1 + x_2 + x_1 \cdot x_2$ toplamı kaçtır?

A) $-9$
B) $-\frac{13}{2}$
C) $-\frac{3}{2}$
D) $\frac{3}{2}$
E) $\frac{13}{2}$

**Cevap:** B
**Çözüm:** $a$ ile $c$ ters işaretli, iki kök var. $x_1 + x_2 = -\frac{8}{2} = -4$, $x_1 \cdot x_2 = \frac{-5}{2}$. Toplam: $-4 - \frac{5}{2} = -\frac{13}{2}$. Çarpımda $a$'ya bölmeyi unutan $-4 - 5 = -9$, toplamın işaretini kaçıran $4 - \frac{5}{2} = \frac{3}{2}$ bulur.

### Soru 2
Kökleri $-3$ ve $\frac{1}{2}$ olan ikinci dereceden denklem aşağıdakilerden hangisidir?

A) $2x^2 - 5x - 3 = 0$
B) $2x^2 + 5x + 3 = 0$
C) $2x^2 - 5x + 3 = 0$
D) $x^2 + 5x - 3 = 0$
E) $2x^2 + 5x - 3 = 0$

**Cevap:** E
**Çözüm:** $T = -3 + \frac{1}{2} = -\frac{5}{2}$, $Ç = -3 \cdot \frac{1}{2} = -\frac{3}{2}$. $x^2 - Tx + Ç = 0$: $x^2 + \frac{5}{2}x - \frac{3}{2} = 0$. $2$ ile genişlet: $2x^2 + 5x - 3 = 0$. Kontrol: $(x + 3)(2x - 1) = 2x^2 + 5x - 3$. A seçeneği $T$'nin işaretini karıştırmaktır; onun kökleri $3$ ve $-\frac{1}{2}$'dir.

### Soru 3
$x^2 - 8x + m = 0$ denkleminin köklerinden biri diğerinin 3 katı olduğuna göre $m$ kaçtır?

A) $4$
B) $8$
C) $12$
D) $15$
E) $16$

**Cevap:** C
**Çözüm:** Kökler $x_2$ ve $3x_2$: toplam $4x_2 = 8$, $x_2 = 2$, diğer kök $6$. $m = Ç = 2 \cdot 6 = 12$. Kontrol: $\Delta = 64 - 48 = 16 > 0$. $16$, kökleri eşit sanmanın ($4 \cdot 4$), $15$ ise kökleri $3$ ve $5$ almanın sonucudur.

## Özet kartı

- $ax^2 + bx + c = 0$ için $x_1 + x_2 = -\frac{b}{a}$, $x_1 \cdot x_2 = \frac{c}{a}$.
- Kökleri verilen denklem: $x^2 - Tx + Ç = 0$; kesirliyse paydayla genişlet.
- $x_1^2 + x_2^2 = T^2 - 2Ç$, $\frac{1}{x_1} + \frac{1}{x_2} = \frac{T}{Ç}$, $(x_1 - x_2)^2 = T^2 - 4Ç$.
- Bir kök verilirse önce denklemde yerine koy, diğer kökü toplamdan ya da çarpımdan bul.
- $Ç < 0$ ise kökler ters işaretli; $b = 0$ ise kökler birbirinin ters işaretlisi; $c = a$ ise çarpımları $1$.
- Sonuç vermeden önce $\Delta$ ile köklerin gerçekten var olduğunu kontrol et.

## Sonraki adım

Alıştırmaya geç (aşağıdaki düğme). Sonraki ders **Karmaşık Sayılar**; $\Delta < 0$ olduğunda "gerçek kök yok" dediğin denklemlerin köklerini yeni bir sayı kümesinde yazacaksın.
