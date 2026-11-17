---
baslik: Köklü İfadeler ve Özellikleri
ders: tyt-matematik
sure: 25 dk
kaynak: MEBİ Konu Özeti c53a0b0cfd
guncelleme: 2026-11-17
---
# Köklü İfadeler ve Özellikleri

**Bu dersin sonunda:** bir köklü ifadenin tanımlı olup olmadığına karar verebilecek, kökleri sadeleştirip dört işlem yapabilecek, farklı dereceli kökleri karşılaştırabilecek ve paydayı eşlenikle kökten kurtarabileceksin.

> **TYT'de yeri:** Her yıl köklü ifadelerden 1–2 soru gelir. Kalıplar: "işleminin sonucu kaçtır?" (sadeleştir, topla, eşlenikle çarp), "sıralaması hangisidir?" (kökleri aynı biçime getir), "$\sqrt{x^2}$ içeren ifade neye eşittir?" (mutlak değer) ve bir alan ya da uzunluk sorusunda köklü sonuç.

## Önce hatırla

<details><summary>Üslü ifade içeren denklemlerden: $2^{x+3} = 4^{x-1}$ olduğuna göre $x$ kaçtır?</summary>
$4 = 2^2$ yaz: $2^{x+3} = 2^{2x-2}$. Tabanlar eşit, üsler eşit: $x + 3 = 2x - 2$, yani <b>$x = 5$</b>. Kontrol: $2^8 = 256$ ve $4^4 = 256$.
</details>

<details><summary>Üslü eşitsizliklerden: $\left(\frac{1}{2}\right)^{x} < 8$ eşitsizliğinin çözüm kümesi nedir?</summary>
Tabanı 1'den büyük yap: $\frac{1}{2} = 2^{-1}$, $8 = 2^3$. $2^{-x} < 2^3$, taban $2 > 1$, yön aynı: $-x < 3$, <b>$x > -3$</b>. Çözüm kümesi $(-3, \infty)$.
</details>

## Kök nedir?

**Örnek.** $x^2 = 9$ denkleminin iki çözümü vardır: $x = 3$ ve $x = -3$. Ama $\sqrt{9}$ yazınca **yalnızca** $3$ kastedilir; karekök hiçbir zaman negatif değildir. Öbür kök $-\sqrt{9} = -3$ diye yazılır.

$x^3 = -8$ denkleminin tek çözümü vardır: $x = -2$, çünkü $(-2)^3 = -8$. Bunu $\sqrt[3]{-8} = -2$ diye yazarız.

$x^4 = -16$ denkleminin gerçek çözümü **yoktur**: çift kuvvet hiçbir zaman negatif olmaz. Bu yüzden $\sqrt[4]{-16}$ bir gerçek sayı değildir.

**Kural.** $n \ge 2$ tam sayı olmak üzere $x^n = a$ eşitliğini sağlayan $x$'e $a$'nın $n$. **dereceden kökü** denir ve $\sqrt[n]{a}$ ile gösterilir. $\sqrt[2]{a}$ kısaca $\sqrt{a}$ yazılır.

| $x^n = a$ | $a > 0$ | $a = 0$ | $a < 0$ |
|---|---|---|---|
| $n$ tek | $x = \sqrt[n]{a}$ | $x = 0$ | $x = \sqrt[n]{a}$ (negatif) |
| $n$ çift | $x = \sqrt[n]{a}$ ya da $x = -\sqrt[n]{a}$ | $x = 0$ | gerçek çözüm yok |

### Ne zaman tanımlı?

**Örnek.** $\sqrt{5 - x} + \sqrt[4]{x + 2}$ ifadesini tanımlı yapan kaç $x$ tam sayısı vardır?

İki kökün derecesi de çift, öyleyse iki içi de negatif olamaz: $5 - x \ge 0$ ise $x \le 5$; $x + 2 \ge 0$ ise $x \ge -2$. Birlikte $-2 \le x \le 5$: tam sayılar $-2, -1, \dots, 5$, toplam **8** tane.

Aynı soruda $\sqrt[3]{x - 10}$ gibi tek dereceli bir terim olsaydı hiçbir koşul eklemezdi: tek dereceli kökün içi her gerçek sayı olabilir.

![Akış şeması: n'inci dereceden kökte n tek ise kökün içi her sayı olabilir ve x üzeri n'in n'inci kökü x olur. n çift ise kökün içi sıfır ya da pozitif olmalı ve x üzeri n'in n'inci kökü mutlak değer x olur.](gorsel/tyt-matematik/04-03-tek-cift.svg "Kökte ilk soru hep aynıdır: derece tek mi çift mi? Çift derecede içerisi negatif olamaz ve kökten çıkan sayı mutlak değerle çıkar.")

### Kesirli üs: kök aslında bir üstür

$a > 0$ için $\sqrt[n]{a^m} = a^{\frac{m}{n}}$ olur. Örneğin $\sqrt{2} = 2^{\frac{1}{2}}$, $\sqrt[3]{25} = 5^{\frac{2}{3}}$. Köklü bir işlemi bu biçime çevirince önceki dersteki üs kurallarını aynen kullanırsın.

## Kökten çıkarmak: $\sqrt[n]{x^n}$

**Örnek.** $\sqrt{(-3)^2}$ kaçtır? Önce içini hesapla: $(-3)^2 = 9$, $\sqrt{9} = 3$. Sonuç $-3$ değil, $3 = \lvert -3 \rvert$'tür.

$\sqrt[3]{(-2)^3}$ kaçtır? İçi $-8$, küp kökü $-2$. Tek derecede işaret korunur.

**Kural.**

$$\sqrt[n]{x^n} = \begin{cases} x, & n \text{ tek ise} \\ \lvert x \rvert, & n \text{ çift ise} \end{cases}$$

**Örnek.** $x < 2$ olmak üzere $\sqrt{(x - 2)^2} + \sqrt[3]{(x - 5)^3}$ ifadesi neye eşittir?

Karekök mutlak değer verir: $\sqrt{(x - 2)^2} = \lvert x - 2 \rvert$. $x < 2$ olduğundan $x - 2$ negatiftir, $\lvert x - 2 \rvert = 2 - x$. Küp kök işareti korur: $\sqrt[3]{(x - 5)^3} = x - 5$.

$$(2 - x) + (x - 5) = -3$$

Kontrol: $x = 1$ için $\sqrt{1} + \sqrt[3]{-64} = 1 - 4 = -3$.

## Sadeleştirmek: kare çarpanı dışarı al

**Örnek.** $\sqrt{72}$ ifadesini sadeleştir.

$72$'nin içindeki en büyük tam kare çarpanı bul: $72 = 36 \cdot 2$.

$$\sqrt{72} = \sqrt{36} \cdot \sqrt{2} = 6\sqrt{2}$$

Küp kökte tam küp çarpan aranır: $\sqrt[3]{54} = \sqrt[3]{27 \cdot 2} = 3\sqrt[3]{2}$.

Ters yönde, dışarıdaki sayıyı **derecesi kadar kuvvetiyle** içeri alırsın: $2\sqrt{5} = \sqrt{4 \cdot 5} = \sqrt{20}$, $2\sqrt[3]{3} = \sqrt[3]{8 \cdot 3} = \sqrt[3]{24}$.

**Kural.** $x \ge 0$ için $x\sqrt[n]{y} = \sqrt[n]{x^n \cdot y}$. Negatif bir katsayı çift dereceli köke girmez, dışarıda işaret olarak kalır: $-2\sqrt{5} = -\sqrt{20}$.

## Bir kök hangi iki tam sayı arasında?

**Örnek.** $\sqrt{20}$ hangi iki ardışık tam sayı arasındadır?

$20$'nin iki yanındaki tam kareler $16$ ve $25$: $\sqrt{16} < \sqrt{20} < \sqrt{25}$, yani $4 < \sqrt{20} < 5$. $20$, $16$'ya daha yakın olduğu için $\sqrt{20}$ de $4$'e yakındır ($\approx 4{,}47$).

![Sayı doğrusu 3'ten 7'ye. Tam sayıların üstünde karekök 9, karekök 16, karekök 25, karekök 36, karekök 49 yazıyor. Karekök 20 noktası 4 ile 5 arasında, karekök 30 noktası 5 ile 6 arasında.](gorsel/tyt-matematik/04-03-sayi-dogrusu.svg "Her tam sayıyı bir tam karenin kökü olarak düşün. √20, √16 ile √25 arasında kalır; √30, √25 ile √36 arasında kalır.")

**Örnek (sıralama).** $a = 3\sqrt{5}$, $b = 2\sqrt{11}$, $c = 7$ sayılarını sırala.

Hepsini tek bir kökün içine al: $a = \sqrt{45}$, $b = \sqrt{44}$, $c = \sqrt{49}$. Derece aynıysa içi büyük olan büyüktür: $b < a < c$.

## Toplama ve çıkarma: yalnızca benzer kökler

**Örnek.** $\sqrt{50} + \sqrt{18} - \sqrt{8}$ işleminin sonucu kaçtır?

Önce her birini sadeleştir: $\sqrt{50} = 5\sqrt{2}$, $\sqrt{18} = 3\sqrt{2}$, $\sqrt{8} = 2\sqrt{2}$. Artık hepsi $\sqrt{2}$'nin katı; katsayıları topla:

$$5\sqrt{2} + 3\sqrt{2} - 2\sqrt{2} = 6\sqrt{2}$$

**Kural.** $a\sqrt[n]{x} \pm b\sqrt[n]{x} = (a \pm b)\sqrt[n]{x}$. Derece ve kökün içi aynı olmalı. $\sqrt{2} + \sqrt{3}$ daha fazla sadeleşmez.

## Çarpma ve bölme

**Örnek.** $\sqrt{6} \cdot \sqrt{15} = \sqrt{90} = \sqrt{9 \cdot 10} = 3\sqrt{10}$. $\dfrac{\sqrt{48}}{\sqrt{3}} = \sqrt{\dfrac{48}{3}} = \sqrt{16} = 4$.

**Kural.** Dereceler aynıysa içler çarpılır ya da bölünür: $\sqrt[n]{a} \cdot \sqrt[n]{b} = \sqrt[n]{a \cdot b}$, $\dfrac{\sqrt[n]{a}}{\sqrt[n]{b}} = \sqrt[n]{\dfrac{a}{b}}$ ($a, b > 0$).

### Dereceler farklıysa önce eşitle

**Örnek.** $\sqrt{2} \cdot \sqrt[3]{2}$ kaçtır?

Dereceler $2$ ve $3$, ortak derece $6$. Kökün derecesini ve içindeki üssü **aynı sayıyla** çarp:

$$\sqrt{2} = \sqrt[6]{2^3} = \sqrt[6]{8}, \qquad \sqrt[3]{2} = \sqrt[6]{2^2} = \sqrt[6]{4}$$

$$\sqrt[6]{8} \cdot \sqrt[6]{4} = \sqrt[6]{32}$$

Kesirli üsle kontrol: $2^{\frac{1}{2}} \cdot 2^{\frac{1}{3}} = 2^{\frac{5}{6}} = \sqrt[6]{32}$.

**Kural.** $\sqrt[n]{x^m} = \sqrt[n \cdot k]{x^{m \cdot k}}$. Aynı yöntem sıralamada da işe yarar: $\sqrt{2} = \sqrt[6]{8}$, $\sqrt[3]{3} = \sqrt[6]{9}$, $\sqrt[6]{5}$ karşılaştırılınca $\sqrt[6]{5} < \sqrt{2} < \sqrt[3]{3}$ çıkar.

### İç içe kök ve kökün kuvveti

$\sqrt{\sqrt[3]{64}} = \sqrt[6]{64} = 2$: iç içe köklerde dereceler **çarpılır**, $\sqrt[m]{\sqrt[n]{x}} = \sqrt[m \cdot n]{x}$.

$\left(\sqrt[3]{5}\right)^6 = 5^{\frac{6}{3}} = 25$: kökün kuvveti içeri girer, $\left(\sqrt[n]{x}\right)^m = \sqrt[n]{x^m}$.

## Paydayı kökten kurtarmak: eşlenik

**Örnek.** $\dfrac{6}{\sqrt{3}}$ ifadesini paydası köksüz yaz. Pay ve paydayı $\sqrt{3}$ ile çarp: $\dfrac{6\sqrt{3}}{3} = 2\sqrt{3}$.

**Örnek.** $\dfrac{4}{\sqrt{5} - 1}$ ifadesini sadeleştir.

$(\sqrt{5} - 1)(\sqrt{5} + 1) = 5 - 1 = 4$: çarpım köksüz çıkar. Pay ve paydayı $\sqrt{5} + 1$ ile çarp:

$$\frac{4(\sqrt{5} + 1)}{(\sqrt{5} - 1)(\sqrt{5} + 1)} = \frac{4(\sqrt{5} + 1)}{4} = \sqrt{5} + 1$$

**Kural.** Çarpımı köksüz olan iki ifadeden her biri ötekinin **eşleniğidir**. Payda kökten kurtarılırken pay ve payda eşlenikle çarpılır.

| Sayı | Eşleniği | Çarpım |
|---|---|---|
| $\sqrt{a}$ | $\sqrt{a}$ | $a$ |
| $\sqrt{a} + \sqrt{b}$ | $\sqrt{a} - \sqrt{b}$ | $a - b$ |
| $\sqrt{a} - b$ | $\sqrt{a} + b$ | $a - b^2$ |
| $\sqrt[3]{a}$ | $\sqrt[3]{a^2}$ | $a$ |

Çarpımlar iki kare farkından gelir: $(x - y)(x + y) = x^2 - y^2$.

## Özel kök: $\sqrt{a \pm 2\sqrt{b}}$

**Örnek.** $\sqrt{8 + 2\sqrt{15}}$ kaçtır?

Toplamı $8$, çarpımı $15$ olan iki sayı ara: $5$ ve $3$. O zaman $(\sqrt{5} + \sqrt{3})^2 = 5 + 3 + 2\sqrt{15}$ olur. Öyleyse

$$\sqrt{8 + 2\sqrt{15}} = \sqrt{5} + \sqrt{3}$$

![Kenarı karekök 5 artı karekök 3 olan kare dört parçaya bölünmüş: alanı 5 olan mavi kare, alanı 3 olan yeşil kare ve alanı karekök 15 olan iki sarı dikdörtgen.](gorsel/tyt-matematik/04-03-ozel-kok.svg "Büyük karenin alanı 5 + 3 + 2√15 = 8 + 2√15. Kenarı bu alanın kareköküdür: √5 + √3.")

**Örnek (eksi işaretli).** $\sqrt{7 - 2\sqrt{10}}$: toplamı $7$, çarpımı $10$ olan sayılar $5$ ve $2$. Sonuç $\sqrt{5} - \sqrt{2}$. Büyüğü önce yazılır; $\sqrt{2} - \sqrt{5}$ negatif olur, karekök negatif olamaz.

**Örnek (2 görünmüyorsa).** $\sqrt{11 - \sqrt{72}}$: önce $2$'yi oluştur, $\sqrt{72} = 2\sqrt{18}$. Toplamı $11$, çarpımı $18$: $9$ ve $2$. Sonuç $\sqrt{9} - \sqrt{2} = 3 - \sqrt{2}$.

**Kural.** $m + n = a$ ve $m \cdot n = b$ ise $\sqrt{a + 2\sqrt{b}} = \sqrt{m} + \sqrt{n}$ ve $m > n$ için $\sqrt{a - 2\sqrt{b}} = \sqrt{m} - \sqrt{n}$.

## ÖSYM tuzakları

> **$\sqrt{x^2} = x$ yazmak:** Doğrusu $\sqrt{x^2} = \lvert x \rvert$. $x < 0$ verilmişse $\sqrt{x^2} = -x$ olur. Soruda işaret bilgisi varsa bu tuzak kesin vardır.

> **Toplamın kökünü ayırmak:** $\sqrt{9 + 16} = 5$ ama $\sqrt{9} + \sqrt{16} = 7$. Kök çarpımda ve bölümde dağılır, toplamda ve farkta **dağılmaz**.

> **Benzer olmayan kökleri toplamak:** $\sqrt{2} + \sqrt{8} \ne \sqrt{10}$. Önce sadeleştir: $\sqrt{2} + 2\sqrt{2} = 3\sqrt{2}$.

> **Farklı derecede doğrudan çarpmak:** $\sqrt{2} \cdot \sqrt[3]{2} \ne \sqrt[5]{4}$ ya da $\sqrt[6]{4}$. Önce dereceleri eşitle ya da kesirli üsse çevir.

> **Özel kökte sırayı ters yazmak:** $\sqrt{7 - 2\sqrt{10}} = \sqrt{5} - \sqrt{2}$'dir, $\sqrt{2} - \sqrt{5}$ değil. Karekökün sonucu negatif olamaz.

## Kendini dene

### Soru 1
$\sqrt{75} - \sqrt{27} + \sqrt{12}$ işleminin sonucu kaçtır?

A) $2\sqrt{3}$
B) $3\sqrt{3}$
C) $4\sqrt{3}$
D) $2\sqrt{15}$
E) $6\sqrt{3}$

**Cevap:** C
**Çözüm:** Sadeleştir: $\sqrt{75} = 5\sqrt{3}$, $\sqrt{27} = 3\sqrt{3}$, $\sqrt{12} = 2\sqrt{3}$. Katsayılar: $5 - 3 + 2 = 4$, sonuç $4\sqrt{3}$. İçleri doğrudan toplayan $\sqrt{75 - 27 + 12} = \sqrt{60} = 2\sqrt{15}$ bulur; bu yanlıştır.

### Soru 2
$a < 0 < b$ olmak üzere

$$\sqrt{a^2} + \sqrt[3]{b^3} - \sqrt{(a - b)^2}$$

ifadesi aşağıdakilerden hangisine eşittir?

A) $0$
B) $2a$
C) $2b$
D) $2b - 2a$
E) $2a + 2b$

**Cevap:** A
**Çözüm:** $\sqrt{a^2} = \lvert a \rvert = -a$ ($a$ negatif). $\sqrt[3]{b^3} = b$ (tek derece). $a - b$ negatif olduğundan $\sqrt{(a - b)^2} = \lvert a - b \rvert = b - a$. Toplam: $-a + b - (b - a) = 0$. $\sqrt{a^2} = a$ yazan $2a$ bulur; iki karekökü de mutlak değersiz açan $2b$ bulur.

### Soru 3
$$\frac{4}{\sqrt{3} + 1} + \frac{6}{\sqrt{3}}$$

işleminin sonucu kaçtır?

A) $2\sqrt{3} - 2$
B) $4\sqrt{3} - 2$
C) $2\sqrt{3} + 2$
D) $4\sqrt{3}$
E) $4\sqrt{3} + 2$

**Cevap:** B
**Çözüm:** İlk kesri $\sqrt{3} - 1$ ile genişlet: $\dfrac{4(\sqrt{3} - 1)}{3 - 1} = 2\sqrt{3} - 2$. İkinci kesri $\sqrt{3}$ ile genişlet: $\dfrac{6\sqrt{3}}{3} = 2\sqrt{3}$. Toplam $4\sqrt{3} - 2$. Eşleniği $\sqrt{3} + 1$ alıp işareti karıştıran $4\sqrt{3} + 2$ bulur.

## Özet kartı

- Çift dereceli kökün içi negatif olamaz; karekökün sonucu hiçbir zaman negatif değildir.
- $\sqrt[n]{x^n}$: $n$ tekse $x$, $n$ çiftse $\lvert x \rvert$.
- Sadeleştir: en büyük tam kare (küp) çarpanı dışarı al. Toplama yalnızca benzer köklerde yapılır.
- Çarpma ve bölmede dereceler eşit olmalı: $\sqrt[n]{x^m} = \sqrt[nk]{x^{mk}} = x^{\frac{m}{n}}$.
- Payda kökten eşlenikle kurtarılır: $(\sqrt{a} + \sqrt{b})(\sqrt{a} - \sqrt{b}) = a - b$.
- $\sqrt{a \pm 2\sqrt{b}} = \sqrt{m} \pm \sqrt{n}$; $m + n = a$, $mn = b$, büyük önce.

## Sonraki adım

Alıştırmaya geç (aşağıdaki düğme). Gerçek çıkmış soruları görmek için MEBİ'deki bu konunun "Çıkmış Sorular" testini ve ÖSYM'nin yayımladığı TYT kitapçıklarını kullan. Sonraki ders **Köklü İfadeleri İçeren Denklem ve Eşitsizlikler**; orada buradaki tanımlılık koşulunu ve kesirli üs yazımını kullanacaksın.
