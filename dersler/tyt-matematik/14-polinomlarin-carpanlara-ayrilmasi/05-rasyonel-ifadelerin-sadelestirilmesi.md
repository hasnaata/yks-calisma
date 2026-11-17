---
baslik: Rasyonel İfadelerin Sadeleştirilmesi
ders: tyt-matematik
sure: 20 dk
kaynak: MEBİ Konu Özeti 9dbdbe4d4b
guncelleme: 2026-11-18
---
# Rasyonel İfadelerin Sadeleştirilmesi

<div class="giris" dir="rtl" lang="ar">

**الدرس ده عن إيه؟** عن الكسور الجبرية (rasyonel ifade): كسر البسط والمقام بتوعه كثيرات حدود، وإزاي تختصره (sadeleştirme) بعد ما تحلّله.

- هتتعلم تحلّل البسط والمقام لعوامل (çarpanlara ayırma) وتشيل العامل المشترك بس، مش الحدود.
- هتعرف تجيب القيم اللي بتخلّي الكسر غير معرّف (tanımsız) من المقام قبل الاختصار، وتاخد بالك من الإشارة لما العامل يبقى مقلوب.
- هتجمع وتطرح وتضرب وتقسم الكسور دي خطوة بخطوة.

**ليه مهم؟** سؤال "اختصر المقدار ده" بييجي في TYT كل سنة تقريبًا، والاختيارات فيها دايمًا الغلطة المشهورة والإجابة بالإشارة العكسية.

٢٠ دقيقة بس، ولو مسكت ترتيب الخطوات هتلاقي الأسئلة دي بقت سهلة عليك.

</div>

**Bu dersin sonunda:** pay ve paydası polinom olan bir ifadeyi çarpanlarına ayırıp sadeleştirebilecek, bu ifadelerle dört işlemi yapabilecek ve ifadeyi tanımsız yapan değerleri bulabileceksin.

> **TYT'de yeri:** "İfadesinin sadeleştirilmiş biçimi aşağıdakilerden hangisidir?" kalıbı TYT'de neredeyse her yıl gelir. Soruda iki üç rasyonel ifade çarpılır, bölünür ya da toplanır; seçeneklerdeki kısa sonuç, bütün pay ve paydaları doğru ayırıp ortak çarpanları silince çıkar. Bazen de büyük bir sayı verilir ve önce sadeleştirip sonra yerine koyman beklenir.

## Önce hatırla

<details><summary>Geçen dersten: $x^2 + x - 20$ ifadesini çarpanlarına ayır.</summary>
Çarpımı $-20$, toplamı $+1$ olan sayılar $5$ ve $-4$. Sonuç $(x + 5)(x - 4)$. Toplam pozitif olduğu için büyük sayı ($5$) pozitiftir.
</details>

<details><summary>Geçen dersten: $2x^2 - 7x + 3$ ifadesini çarpanlarına ayır.</summary>
$2x^2 = 2x \cdot x$, $3 = (-1) \cdot (-3)$. Satırlar $2x, -1$ ve $x, -3$: çaprazlar $2x \cdot (-3) + x \cdot (-1) = -7x$. Tuttu: $(2x - 1)(x - 3)$. Bu derste her sorunun ilk adımı bu ayırma olacak.
</details>

## Rasyonel ifade ve tanımsız değerler

**Örnek.** $\dfrac{12}{18}$ kesrini sadeleştirirken pay ve paydayı çarpanlarına ayırırsın: $\dfrac{2 \cdot 6}{3 \cdot 6} = \dfrac{2}{3}$. Ortak çarpan $6$ silinir. Polinomlarda da aynısını yapacaksın; tek fark çarpanların $x - 3$, $x + 2$ gibi ifadeler olmasıdır.

$P(x)$ ve $Q(x)$ birer polinom, $Q(x) \ne 0$ olmak üzere $\dfrac{P(x)}{Q(x)}$ biçimindeki ifadelere **rasyonel ifade** denir.

Paydayı sıfır yapan değerler için ifade **tanımsızdır**. Örneğin $\dfrac{x + 1}{x^2 - 4}$ ifadesinde $x^2 - 4 = (x - 2)(x + 2)$ olduğundan $x = 2$ ve $x = -2$ için ifade tanımsızdır. Payın sıfır olması sorun değildir: $x = -1$ için ifadenin değeri $0$'dır.

## 1. Çarpanlara ayır, ortak çarpanı sil

**Örnek.** $\dfrac{x^2 - 9}{x^2 + x - 6}$ ifadesini sadeleştir.

1. Payı ayır (iki kare farkı): $x^2 - 9 = (x - 3)(x + 3)$.
2. Paydayı ayır (üç terimli): $x^2 + x - 6 = (x + 3)(x - 2)$.
3. Tanımsız değerleri not et: $x \ne -3$, $x \ne 2$.
4. Ortak çarpan $x + 3$'ü sil: $\dfrac{(x - 3)(x + 3)}{(x + 3)(x - 2)} = \dfrac{x - 3}{x - 2}$.

Kontrol: $x = 4$ için ilk ifade $\frac{7}{14} = \frac{1}{2}$, sonuç $\frac{1}{2}$. Tuttu.

![Pay iki kutu: x eksi 3 ve x artı 3. Payda iki kutu: x eksi 2 ve x artı 3. İki x artı 3 kutusunun üstü çizili; sağda kalan kesir x eksi 3 bölü x eksi 2, altında x eşit değil eksi 3 ve x eşit değil 2.](gorsel/tyt-matematik/14-05-carpan-kutulari.svg "Pay ve payda kutulara ayrılınca ortak kutu hem üstten hem alttan silinir. Silinen kutunun sıfır yaptığı değer yine yasaktır.")

**Kural.** Önce pay ve paydanın **tamamını** çarpanlarına ayır; yalnızca hem payda hem paydada **çarpan** olarak duran ifadeleri sil.

> **Tuzak:** $\dfrac{x + 5}{x + 3}$ ifadesinde $x$'leri silip $\dfrac{5}{3}$ yazmak. $x$ burada çarpan değil, toplamın bir **terimidir**. Pay ya da payda bir toplamsa önce çarpanlarına ayrılmalı; ayrılmıyorsa ifade sadeleşmez.

![Solda yeşil kutu: 5 çarpı x bölü 3 çarpı x eşittir 5 bölü 3, x eşittir 1 için 5 bölü 3. Sağda kırmızı kutu: x artı 5 bölü x artı 3, 5 bölü 3 değildir; x eşittir 1 için 6 bölü 4, yani 3 bölü 2 çıkar.](gorsel/tyt-matematik/14-05-terim-carpan.svg "Emin değilsen bir sayı koy: x = 1 için iki taraf eşit çıkmıyorsa silme yanlıştır.")

### Silinen çarpan ne olur?

**Örnek.** $y = \dfrac{x^2 - 4}{x - 2}$ ifadesini sadeleştir: $\dfrac{(x - 2)(x + 2)}{x - 2} = x + 2$. Ama $x = 2$ için ilk ifade $\frac{0}{0}$ olur, tanımsızdır. Sonuç "$x \ne 2$ olmak üzere $x + 2$"dir.

![Koordinat düzleminde y eşittir x artı 2 doğrusu; x eşittir 2, y eşittir 4 noktasında içi boş bir daire var.](gorsel/tyt-matematik/14-05-delikli-grafik.svg "Grafik y = x + 2 doğrusudur, ama (2, 4) noktası boştur: sadeleştirme tanımsız değeri yok etmez.")

**Kural.** Tanımsız değerler **sadeleştirmeden önceki** paydaya bakılarak bulunur.

> **Tuzak:** "İfadeyi tanımsız yapan $x$ değerleri" sorulduğunda sadeleşmiş sonucun paydasına bakmak. $\dfrac{x^2 - 9}{x^2 + x - 6}$ için cevap yalnızca $2$ değil, $-3$ ve $2$'dir.

## 2. Ters işaretli çarpanlar

**Örnek.** $\dfrac{6 - 3x}{x^2 - 4}$ ifadesini sadeleştir.

1. Pay: $6 - 3x = 3(2 - x) = -3(x - 2)$.
2. Payda: $x^2 - 4 = (x - 2)(x + 2)$.
3. Sil: $\dfrac{-3(x - 2)}{(x - 2)(x + 2)} = \dfrac{-3}{x + 2}$.

Kontrol: $x = 0$ için $\frac{6}{-4} = -\frac{3}{2}$, sonuç $-\frac{3}{2}$. Tuttu.

**Kural.** $a - b = -(b - a)$, yani $\dfrac{a - b}{b - a} = -1$. Ters sıralı bir çarpanı silerken önüne bir eksi gelir. Buna karşılık $x + 2$ ile $2 + x$ aynı ifadedir; işaret değişmez.

> **Tuzak:** $2 - x$ ile $x - 2$'yi aynı çarpan sanıp eksiyi kaybetmek. ÖSYM seçeneklerinde doğru cevabın işaretçe tersi hep bulunur.

## 3. Çarpma ve bölme

**Örnek (çarpma).** $\dfrac{x^2 + 5x + 6}{x^2 - 1} \cdot \dfrac{x - 1}{x + 3}$ işleminin sonucunu bul.

Önce çarpma yapma; her parçayı ayır:

$$\frac{(x + 2)(x + 3)}{(x - 1)(x + 1)} \cdot \frac{x - 1}{x + 3} = \frac{x + 2}{x + 1}$$

$x + 3$ ve $x - 1$ çarpanları biri payda, biri paydada olduğu için silinir. Kontrol: $x = 2$ için $\frac{20}{3} \cdot \frac{1}{5} = \frac{4}{3}$, sonuç $\frac{2 + 2}{2 + 1} = \frac{4}{3}$. Tuttu.

**Örnek (bölme).** $\dfrac{x^2 - 1}{x^2 - 2x} : \dfrac{x + 1}{x - 2}$ işleminin sonucunu bul.

Bölen kesri ters çevirip çarp:

$$\frac{(x - 1)(x + 1)}{x(x - 2)} \cdot \frac{x - 2}{x + 1} = \frac{x - 1}{x}$$

Kontrol: $x = 3$ için $\frac{8}{3} : \frac{4}{1} = \frac{2}{3}$, sonuç $\frac{2}{3}$. Tuttu.

**Kural.** Çarpmada paylar paya, paydalar paydaya yazılır; ama çarpmayı açmadan önce sadeleştir. Bölmede **yalnızca bölen** (ikinci kesir) ters çevrilir:

$$\frac{P}{Q} : \frac{R}{T} = \frac{P}{Q} \cdot \frac{T}{R}$$

> **Tuzak:** Bölmede ters çevirmeyi unutmak ya da birinci kesri çevirmek. Ayrıca bölenin payı da sıfır olamaz: yukarıdaki örnekte $x \ne -1$ de gerekir, çünkü $x + 1$ ters çevrilince paydaya geçer.

## 4. Toplama ve çıkarma

**Örnek.** $\dfrac{x}{x - 3} - \dfrac{9}{x^2 - 3x}$ işleminin sonucunu bul.

1. Paydaları ayır: $x - 3$ ve $x(x - 3)$. Ortak payda $x(x - 3)$.
2. Birinci kesri $x$ ile genişlet: $\dfrac{x \cdot x}{x(x - 3)} - \dfrac{9}{x(x - 3)} = \dfrac{x^2 - 9}{x(x - 3)}$.
3. Payı yine ayır ve sadeleştir: $\dfrac{(x - 3)(x + 3)}{x(x - 3)} = \dfrac{x + 3}{x}$.

Kontrol: $x = 1$ için $\frac{1}{-2} - \frac{9}{-2} = 4$, sonuç $\frac{1 + 3}{1} = 4$. Tuttu.

**Kural.** Toplama ve çıkarmada önce paydaları çarpanlarına ayır, en küçük ortak paydayı bul, payları birleştir. Payda çıkan ifade çoğu zaman yeniden ayrılır ve bir sadeleştirme daha gelir.

> **Tuzak:** Çıkarmada eksi işaretini payın **tamamına** dağıtmamak. $\dfrac{2x}{D} - \dfrac{x + 1}{D} = \dfrac{2x - x - 1}{D}$; $\dfrac{2x - x + 1}{D}$ değil.

Paydalar yalnızca işaretçe farklıysa birini $-1$ ile düzelt: $\dfrac{1}{x - 3} + \dfrac{1}{3 - x} = \dfrac{1}{x - 3} - \dfrac{1}{x - 3} = 0$.

![Altı adımlı yöntem akışı: bölmeyi çarpmaya çevir, pay ve paydaları ayır, tanımsız değerleri yaz, gerekirse paydaları eşitle, ortak çarpanları sadeleştir, bir sayıyla kontrol et.](gorsel/tyt-matematik/14-05-yontem.svg "Her rasyonel ifade sorusunda aynı sıra. Mavi adım, yani çarpanlara ayırma, işin kendisidir.")

## ÖSYM tuzakları

> **Terim silmek:** $\dfrac{x^2 + 4}{x + 2} \ne x + 2$. Pay ve payda birer toplamdır ve $x^2 + 4$ gerçek sayılarda ayrılmaz; sadeleşme yoktur. Yalnızca çarpanlar silinir.

> **İşareti kaybetmek:** $\dfrac{x - 5}{5 - x} = -1$, $1$ değil. Seçeneklerde doğru cevabın eksilisi mutlaka bulunur.

> **Tanımsız değeri sadeleşmiş hâlden bulmak:** $\dfrac{x^2 - 1}{x^2 + x - 2}$ sadeleşince $\dfrac{x + 1}{x + 2}$ olur, ama ilk ifade $x = 1$ için de tanımsızdır.

> **Önce açıp sonra ayırmaya çalışmak:** Çarpma sorusunda paydaları çarpıp dördüncü dereceden bir polinom elde edersen geri ayırmak çok zordur. Hep **önce ayır, sonra sil**.

> **Bölmede yanlış kesri çevirmek:** $\dfrac{A}{B} : \dfrac{C}{D}$ işleminde ters dönen $\dfrac{C}{D}$'dir.

## Kendini dene

### Soru 1
$\dfrac{x^2 + 4x}{x^2 - 16}$ ifadesinin sadeleştirilmiş biçimi aşağıdakilerden hangisidir?

A) $\dfrac{x}{x + 4}$
B) $\dfrac{x}{x - 4}$
C) $\dfrac{4x}{x - 4}$
D) $\dfrac{x + 4}{x - 4}$
E) $-\dfrac{x}{4}$

**Cevap:** B
**Çözüm:** Pay $x(x + 4)$, payda $(x - 4)(x + 4)$. Ortak çarpan $x + 4$ silinir: $\dfrac{x}{x - 4}$. E seçeneği $x^2$'leri terim olarak silmekten gelir ($\frac{4x}{-16}$). A seçeneğinde yanlış çarpan silinmiştir.

### Soru 2
$\dfrac{3 - x}{x^2 - 9}$ ifadesinin sadeleştirilmiş biçimi aşağıdakilerden hangisidir?

A) $\dfrac{1}{x + 3}$
B) $\dfrac{1}{x - 3}$
C) $-\dfrac{1}{x - 3}$
D) $-\dfrac{1}{x + 3}$
E) $-1$

**Cevap:** D
**Çözüm:** $3 - x = -(x - 3)$ ve $x^2 - 9 = (x - 3)(x + 3)$. $\dfrac{-(x - 3)}{(x - 3)(x + 3)} = -\dfrac{1}{x + 3}$. A seçeneği eksiyi kaybetmektir. Kontrol: $x = 0$ için $\frac{3}{-9} = -\frac{1}{3}$ ve $-\frac{1}{0 + 3} = -\frac{1}{3}$.

### Soru 3
$\dfrac{1}{x - 2} - \dfrac{4}{x^2 - 4}$ işleminin sonucu aşağıdakilerden hangisidir?

A) $\dfrac{1}{x + 2}$
B) $\dfrac{1}{x - 2}$
C) $\dfrac{-3}{x^2 - 4}$
D) $\dfrac{x - 2}{x + 2}$
E) $\dfrac{x + 6}{x^2 - 4}$

**Cevap:** A
**Çözüm:** Ortak payda $(x - 2)(x + 2)$. Birinci kesir $x + 2$ ile genişler: $\dfrac{x + 2 - 4}{(x - 2)(x + 2)} = \dfrac{x - 2}{(x - 2)(x + 2)} = \dfrac{1}{x + 2}$. C seçeneği payları genişletmeden çıkarmaktır ($1 - 4$). E seçeneği eksiyi dağıtmadan $x + 2 + 4$ yazmaktır.

## Özet kartı

- Rasyonel ifade $\dfrac{P(x)}{Q(x)}$; $Q(x) = 0$ yapan değerler için tanımsız.
- Tanımsız değerleri **sadeleştirmeden önce** paydaya bakarak bul.
- Önce pay ve paydayı tamamen ayır; yalnızca ortak **çarpanları** sil, terimleri silme.
- $\dfrac{a - b}{b - a} = -1$: ters sıralı çarpan bir eksi bırakır.
- Bölmede yalnızca böleni ters çevir; çarpmada açmadan önce sadeleştir.
- Toplama ve çıkarmada paydaları ayırıp eşitle; çıkan payı yine ayır.

## Sonraki adım

Alıştırmaya geç (aşağıdaki düğme). Sonraki konu **İkinci Dereceden Bir Bilinmeyenli Denklemler**; orada da ilk adım çarpanlara ayırmak olacak, ama bu kez çarpımı sıfıra eşitleyip kökleri bulacaksın.
