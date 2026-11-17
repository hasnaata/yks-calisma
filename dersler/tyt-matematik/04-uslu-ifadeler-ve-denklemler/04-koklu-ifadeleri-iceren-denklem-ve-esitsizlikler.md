---
baslik: Köklü İfadeleri İçeren Denklem ve Eşitsizlikler
ders: tyt-matematik
sure: 20 dk
kaynak: MEBİ Konu Özeti 2aae7edcd1
guncelleme: 2026-11-17
---
# Köklü İfadeleri İçeren Denklem ve Eşitsizlikler

**Bu dersin sonunda:** bilinmeyeni kök içinde olan bir denklemi kuvvet alarak çözüp yabancı kökü sağlamayla eleyebilecek, köklü sayıları sıralayabilecek ve köklü bir eşitsizliği sağlayan tam sayıları sayabileceksin.

> **TYT'de yeri:** Köklü ifadelerden her yıl 1–2 soru gelir. Kalıplar: "$x$ kaçtır?" (kökü yalnız bırak, kare al), "$a$, $b$, $c$ sayılarının sıralaması", "$\sqrt{n}$ hangi iki tam sayı arasında?", "eşitsizliği sağlayan kaç tam sayı var?" ve formülle verilen günlük hayat durumları.

## Önce hatırla

<details><summary>Köklü ifadeler ve özelliklerinden: $\sqrt{48} + \sqrt{27} - \sqrt{12}$ işleminin sonucu kaçtır?</summary>
Kök içindeki en büyük tam kareyi dışarı çıkar: $\sqrt{48} = 4\sqrt{3}$, $\sqrt{27} = 3\sqrt{3}$, $\sqrt{12} = 2\sqrt{3}$. Kökleri aynı olan terimler toplanır: $(4 + 3 - 2)\sqrt{3} = $ <b>$5\sqrt{3}$</b>.
</details>

<details><summary>Köklü ifadeler ve özelliklerinden: $x < 0$ olmak üzere $\sqrt{x^2} + \sqrt[3]{x^3}$ ifadesinin eşiti nedir?</summary>
Çift dereceli kökten çıkan sayı mutlak değerle çıkar: $\sqrt{x^2} = |x| = -x$ (çünkü $x < 0$). Tek dereceli kökte işaret korunur: $\sqrt[3]{x^3} = x$. Toplam $-x + x = $ <b>$0$</b>.
</details>

## Köklü denklem: kökü yalnız bırak, kuvvet al

Bilinmeyeni kök içinde olan denkleme **köklü denklem** denir.

**Örnek.** $\sqrt{x + 4} - 1 = 4$ denklemini çöz.

1. Kökü yalnız bırak: $\sqrt{x + 4} = 5$.
2. İki tarafın karesini al: $x + 4 = 25$, yani $x = 21$.
3. Sağlama: $\sqrt{25} - 1 = 5 - 1 = 4$. Doğru, $x = 21$.

**Örnek (çözüm yok).** $\sqrt{2x - 1} + 7 = 4$ denklemini çöz.

Kökü yalnız bırak: $\sqrt{2x - 1} = -3$. Karekök hiçbir zaman negatif olamaz; bu denklemin **çözümü yoktur**.
Bunu görmeden kare alırsan $2x - 1 = 9$, $x = 5$ bulursun. Sağlama: $\sqrt{9} + 7 = 10 \ne 4$. Sağlamayan bu değere **yabancı kök** denir.

**Örnek (tek dereceli kök).** $\sqrt[3]{x - 2} = -3$ denklemini çöz.

Küpkök negatif olabilir, iki tarafın küpünü al: $x - 2 = -27$, $x = -25$. Kontrol: $\sqrt[3]{-27} = -3$. Tek dereceli kökte kuvvet almak yabancı kök üretmez.

**Kural.**

- Kökü bir tarafta **yalnız** bırak, sonra kök derecesi kadar kuvvet al: $\sqrt[n]{A} = B \Rightarrow A = B^n$.
- $n$ çiftse $\sqrt[n]{A} = B$ için $B \ge 0$ olmalıdır. $B$ negatifse çözüm yoktur.
- Çift dereceli kökte bulduğun her değeri **ilk denklemde** dene.

![Akış şeması: kökü yalnız bırak. Kök derecesi çift değilse doğrudan kuvvet al ve çöz. Çiftse öbür tarafın negatif olup olmadığına bak; negatifse çözüm yok, değilse kuvvet al ve çöz. Sonra bulunan değerin ilk denklemi sağlayıp sağlamadığına bak; sağlamıyorsa yabancı kök olarak at.](gorsel/tyt-matematik/04-04-yontem.svg "Kuvvet almadan önce kökü yalnız bırak; çözdükten sonra sağlamayı atlama. Öbür tarafta x varsa işaretini bilemezsin, bu durumda sağlama şarttır.")

### Öbür tarafta da $x$ varsa

**Örnek.** $\sqrt{x + 7} = x - 5$ denklemini çöz.

Kare al: $x + 7 = (x - 5)^2 = x^2 - 10x + 25$. Düzenle: $x^2 - 11x + 18 = 0$, yani $(x - 2)(x - 9) = 0$. Adaylar $x = 2$ ve $x = 9$.

- $x = 9$: $\sqrt{16} = 4$ ve $9 - 5 = 4$. Geçerli.
- $x = 2$: $\sqrt{9} = 3$ ama $2 - 5 = -3$. $3 \ne -3$, **yabancı kök**.

Çözüm kümesi $\{9\}$.

![Koordinat düzleminde y eşittir kök x artı 7 eğrisi mavi, y eşittir eksi kök x artı 7 eğrisi kesikli kırmızı, y eşittir x eksi 5 doğrusu yeşil. Doğru mavi eğriyi x eşittir 9'da, kırmızı kesikli eğriyi x eşittir 2'de kesiyor.](gorsel/tyt-matematik/04-04-yabanci-kok.svg "Kare alınca denklem eksi kök x artı 7 dalını da kapsar. x = 2, doğrunun kırmızı dalla kesiştiği yerdir; asıl denklemi sağlamaz.")

**Neden yabancı kök çıkar?** $3 \ne -3$ ama $3^2 = (-3)^2$. Kare almak işaret bilgisini siler. Bu yüzden kare aldıktan sonra bulunan değerler ilk denklemi sağlamayabilir.

## Köklü sayıları sıralamak

### Kök dereceleri eşitse: katsayıyı içeri al

**Örnek.** $a = 3\sqrt{5}$, $b = 2\sqrt{11}$, $c = 4\sqrt{3}$ sayılarını sırala.

Katsayıyı karesini alarak kökün içine sok: $a = \sqrt{9 \cdot 5} = \sqrt{45}$, $b = \sqrt{4 \cdot 11} = \sqrt{44}$, $c = \sqrt{16 \cdot 3} = \sqrt{48}$. İçi büyük olan büyüktür: $b < a < c$.

**Kural.** Dereceler eşitse kök içindeki sayı büyük olan büyüktür. Katsayıyı içeri alırken kök derecesi kadar kuvvetini al: $2\sqrt[3]{5} = \sqrt[3]{8 \cdot 5} = \sqrt[3]{40}$.

### Dereceler farklıysa: dereceleri eşitle

**Örnek.** $a = \sqrt{2}$, $b = \sqrt[3]{3}$, $c = \sqrt[6]{6}$ sayılarını sırala.

Dereceler 2, 3, 6; ortak kat 6. Önceki dersteki kuralla $\sqrt[n]{x} = \sqrt[nk]{x^k}$:

$$a = \sqrt[6]{2^3} = \sqrt[6]{8}, \qquad b = \sqrt[6]{3^2} = \sqrt[6]{9}, \qquad c = \sqrt[6]{6}$$

Sıralama: $c < a < b$.

Kısa yol: üçünün de **6. kuvvetini** al ve karşılaştır: $a^6 = 8$, $b^6 = 9$, $c^6 = 6$. Pozitif sayılarda kuvveti büyük olan sayı da büyüktür.

### Kök içleri eşitse: 1'e göre bak

**Örnek.** $\sqrt{7}$, $\sqrt[3]{7}$, $\sqrt[4]{7}$ sayılarını sırala.

Kök içi $7 > 1$. Derece büyüdükçe sayı 1'e yaklaşır, yani küçülür: $\sqrt[4]{7} < \sqrt[3]{7} < \sqrt{7}$ (yaklaşık $1{,}63 < 1{,}91 < 2{,}65$).

Ama kök içi 0 ile 1 arasındaysa sıra döner: $\sqrt{\frac{1}{16}} = \frac{1}{4}$, $\sqrt[4]{\frac{1}{16}} = \frac{1}{2}$. Burada derecesi büyük olan büyüktür.

![Üç eğri: y eşittir karekök x mavi, küpkök x yeşil, dördüncü dereceden kök x kahverengi. Üçü de 1 virgül 1 noktasında kesişiyor. x 1'den büyükken en üstte karekök, x 0 ile 1 arasındayken en üstte dördüncü dereceden kök var.](gorsel/tyt-matematik/04-04-kok-dereceleri.svg "Eğriler x = 1'de yer değiştirir. Kök içi 1'den büyükse derecesi küçük olan, 0 ile 1 arasındaysa derecesi büyük olan sayı daha büyüktür.")

**Kural.** Kök içi eşit ve pozitifse: içi $1$'den büyükse **derecesi küçük olan** büyüktür; içi $0$ ile $1$ arasındaysa **derecesi büyük olan** büyüktür.

### Hangi iki tam sayı arasında?

**Örnek.** $\sqrt{50}$ hangi iki ardışık tam sayı arasındadır?

50'nin iki yanındaki tam kareleri bul: $49 < 50 < 64$. Karekök al: $7 < \sqrt{50} < 8$.
Küpkökte tam küplere bakılır: $64 < 100 < 125$ olduğundan $4 < \sqrt[3]{100} < 5$.

**Örnek (arada kaç tam sayı?).** $\sqrt{20} < n < \sqrt{90}$ koşulunu sağlayan kaç $n$ tam sayısı vardır?

$16 < 20 < 25$, yani $4 < \sqrt{20} < 5$. $81 < 90 < 100$, yani $9 < \sqrt{90} < 10$. Aradaki tam sayılar $5, 6, 7, 8, 9$: **5 tane**.

![Sayı doğrusu 4'ten 10'a. Kök 20, 4 ile 5 arasında; kök 90, 9 ile 10 arasında kırmızı çizgiyle işaretli. Aradaki 5, 6, 7, 8, 9 tam sayıları mavi noktalı.](gorsel/tyt-matematik/04-04-sayi-dogrusu.svg "Önce her köklü sayının iki yanındaki tam kareleri bul, sonra aradaki tam sayıları say.")

### Yaklaşık değer

Kaynak kitaplarda karekök için şu yaklaşık hesap verilir: $a$ sayısından küçük en büyük tam kare $x$, büyük en küçük tam kare $y$ ise

$$\sqrt{a} \approx \sqrt{x} + \frac{a - x}{y - x}$$

**Örnek.** $\sqrt{30}$: $x = 25$, $y = 36$. $\sqrt{30} \approx 5 + \frac{30 - 25}{36 - 25} = 5 + \frac{5}{11} \approx 5{,}45$. Gerçek değer $5{,}477\ldots$; tam kısım ve ilk basamak doğru çıkar. Soruda bu yöntem tanımlanırsa yalnızca formülü uygula.

## Köklü eşitsizlikler

**Örnek.** $\sqrt{x - 1} < 3$ eşitsizliğini sağlayan kaç $x$ tam sayısı vardır?

İki koşul birlikte gerekir:

1. **Tanım koşulu:** kök içi negatif olamaz, $x - 1 \ge 0$, yani $x \ge 1$.
2. **Eşitsizlik:** iki taraf da negatif olmadığından kare alınca yön değişmez: $x - 1 < 9$, yani $x < 10$.

Birlikte $1 \le x < 10$: $x = 1, 2, \dots, 9$, yani **9 tam sayı**. Tanım koşulunu unutan "$x < 10$" yazar ve sonsuz çoklukta tam sayı bulur.

**Örnek.** $2 < \sqrt{x} < 5$ ise $x$ kaç tam sayı değeri alır? Üç taraf da pozitif, kare al: $4 < x < 25$. Tam sayılar $5, \dots, 24$: **20 tane**.

**Kural.** Çift dereceli kökte önce **kök içi $\ge 0$** koşulunu yaz. İki taraf da negatif değilse kare almak eşitsizliğin yönünü değiştirmez. Cevap, iki koşulun kesişimidir.

## ÖSYM tuzakları

> **Kökü yalnız bırakmadan kare almak:** $\sqrt{x + 4} - 1 = 4$ için $x + 4 - 1 = 16$ yazmak yanlıştır. $(a - b)^2 \ne a^2 - b^2$. Önce kökü yalnız bırak.

> **Sağlama yapmamak:** $\sqrt{x + 7} = x - 5$ için $\{2, 9\}$ cevabı yanlıştır; $x = 2$ yabancı köktür. "Köklerin toplamı" sorusunda cevap $11$ değil, $9$ olur.

> **Karekökü negatif bırakmak:** $\sqrt{A} = -3$ gibi bir eşitlik gördüğünde hesap yapma: çözüm yoktur. Ama $\sqrt[3]{A} = -3$ çözülebilir.

> **0 ile 1 arasında sırayı ters kurmak:** "Derecesi küçük kök büyüktür" kuralı kök içi $1$'den büyükken geçerlidir. $0 < x < 1$ ise $x < \sqrt{x} < \sqrt[3]{x}$ olur.

> **Eşitsizlikte tanım koşulunu unutmak:** $\sqrt{x + 2} \le 4$ için $x \le 14$ yazıp durmak yetmez; $x \ge -2$ koşulu da gerekir.

## Kendini dene

### Soru 1
$\sqrt{3x + 1} - 2 = 5$ olduğuna göre $x$ kaçtır?

A) 2
B) 8
C) 12
D) 16
E) 18

**Cevap:** D
**Çözüm:** Kökü yalnız bırak: $\sqrt{3x + 1} = 7$. Kare al: $3x + 1 = 49$, $3x = 48$, $x = 16$. Sağlama: $\sqrt{49} - 2 = 5$. Kare almayı unutup $3x + 1 = 7$ yazan $2$, $-2$'yi karşıya geçirmeyip $3x + 1 = 25$ yazan $8$ bulur.

### Soru 2
$a = 2\sqrt{7}$, $b = 3\sqrt{3}$, $c = \sqrt{26}$ sayılarının doğru sıralaması aşağıdakilerden hangisidir?

A) $a < b < c$
B) $b < c < a$
C) $c < b < a$
D) $c < a < b$
E) $b < a < c$

**Cevap:** C
**Çözüm:** Katsayıları kök içine al: $a = \sqrt{4 \cdot 7} = \sqrt{28}$, $b = \sqrt{9 \cdot 3} = \sqrt{27}$, $c = \sqrt{26}$. Dereceler eşit, içi büyük olan büyük: $c < b < a$. Katsayıyı karesini almadan içeri sokan $a = \sqrt{14}$, $b = \sqrt{9}$ bulur ve yanılır.

### Soru 3
$\sqrt{x + 5} = x - 1$ denkleminin çözüm kümesi aşağıdakilerden hangisidir?

A) $\{-1\}$
B) $\{4\}$
C) $\{-1, 4\}$
D) $\{1, 4\}$
E) $\varnothing$

**Cevap:** B
**Çözüm:** Kare al: $x + 5 = x^2 - 2x + 1$, yani $x^2 - 3x - 4 = 0$, $(x - 4)(x + 1) = 0$. Adaylar $4$ ve $-1$. Sağlama: $x = 4$ için $\sqrt{9} = 3$ ve $4 - 1 = 3$, geçerli. $x = -1$ için $\sqrt{4} = 2$ ama $-1 - 1 = -2$, yabancı kök. Çözüm kümesi $\{4\}$. Sağlama yapmayan C'yi seçer.

## Özet kartı

- Köklü denklemde önce kökü yalnız bırak, sonra kök derecesi kadar kuvvet al.
- Çift dereceli kökte $\sqrt{A} = B$ için $B \ge 0$ olmalı; bulunan her değeri ilk denklemde dene.
- Dereceler eşitse katsayıyı içeri al, içi büyük olan büyüktür. Dereceler farklıysa ortak dereceye çevir ya da ortak kuvvet al.
- Kök içleri eşitse: içi $> 1$ iken derecesi küçük olan, $0 <$ içi $< 1$ iken derecesi büyük olan büyüktür.
- $\sqrt{n}$'nin yerini iki yanındaki tam karelerle bul.
- Köklü eşitsizlikte cevap = tanım koşulu (kök içi $\ge 0$) ile kare alınarak bulunan aralığın kesişimi.

## Sonraki adım

Alıştırmaya geç (aşağıdaki düğme). Gerçek çıkmış soruları görmek için MEBİ'deki bu konunun "Çıkmış Sorular" testini ve ÖSYM'nin yayımladığı TYT kitapçıklarını kullan. Sonraki konu **Oran-Orantı Kavramları ve Özellikleri**; orantı sorularında da denklem kurup çözeceksin.
