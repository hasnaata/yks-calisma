---
baslik: Yamukta Açı ve Uzunluk
ders: tyt-matematik
sure: 20 dk
kaynak: MEBİ Konu Özeti b86fd38bf3
guncelleme: 2026-11-18
---
# Yamukta Açı ve Uzunluk

<div class="giris" dir="rtl" lang="ar">

**الدرس ده عن إيه؟** عن شبه المنحرف (yamuk): الشكل الرباعي اللي فيه ضلعين متوازيين، واسمهم القاعدتين (taban).

- هتعرف إن الزاويتين اللي على نفس الضلع الجانبي (yan kenar) مجموعهم دايمًا 180 درجة، وإن منصفاتهم بيتقابلوا بزاوية قايمة.
- هتحسب القاعدة الوسطى (orta taban): نص مجموع القاعدتين.
- هتعرف إن الأقطار (köşegen) بتقسم القاعدة الوسطى لتلات حتت، وكل حتة بتتحسب من القاعدتين على طول.

**ليه مهم؟** شبه المنحرف بييجي في TYT في أسئلة زوايا وأطوال، وكمان في أسئلة من الحياة زي الرفوف والكباري، وأغلبها بيتحل بقاعدة واحدة من دول.

الدرس 20 دقيقة، وكل قاعدة معاها رسمة ومثال محلول. ارسم الشكل معانا وهتلاقيه بسيط.

</div>

**Bu dersin sonunda:** bir yamukta yan kenardaki açılardan, orta tabandan ve köşegenlerin orta taban üzerinde ayırdığı parçalardan bilinmeyen açıyı ya da uzunluğu tek adımda bulabileceksin.

> **TYT'de yeri:** Yamuk soruları iki kalıpta gelir: "x kaç derecedir?" (paralel tabanlar arasındaki açılar) ve "|EF| kaç birimdir?" (orta taban ve köşegenler). Yeni nesil sorularda yamuk bir raf, bir köprü ya da bir bahçe olarak karşına çıkar; kural aynıdır.

## Önce hatırla

<details><summary>Geçen dersten: Bir dörtgenin üç iç açısı 80°, 95° ve 120°'dir. Dördüncü açı kaç derecedir?</summary>
Dörtgenin iç açıları toplamı 360°'dir: 360° − 80° − 95° − 120° = <b>65°</b>. Bugün yamukta bu toplamın iki eş parçaya, 180° + 180°'ye ayrıldığını göreceksin.
</details>

<details><summary>Geçen dersten: ABCD dörtgeninde B ve C açılarının açıortayları E'de kesişiyor. m(A) + m(D) = 150° ise m(BEC) kaç derecedir?</summary>
m(BEC) = (m(A) + m(D)) / 2 = <b>75°</b>. Yamukta yan kenardaki iki açının toplamı 180° olduğu için bu kural bugün hep <b>90°</b> verecek.
</details>

## Yamuk nedir, nerede durur?

**En az iki kenarı paralel** olan dörtgene **yamuk** denir. Paralel kenarlar **tabanlardır** (uzun olan alt taban, kısa olan üst taban); öbür iki kenar **yan kenarlardır**. Bu derste hep $[AB] \parallel [DC]$ alınır: $|AB| = a$ alt taban, $|DC| = c$ üst taban.

![Dörtgenlerin aile şeması: Dörtgen yamuk ve deltoide ayrılır; yamuktan paralelkenar, paralelkenardan dikdörtgen ve eşkenar dörtgen çıkar; eşkenar dörtgen deltoidin de altındadır; dikdörtgen ile eşkenar dörtgen kareye iner.](gorsel/tyt-matematik/25-01-hiyerarsi.svg "Bir oku izleyen her şekil, oktan önceki şeklin özelliklerini taşır. Paralelkenar, dikdörtgen ve kare de birer yamuktur; bugünkü kurallar onlarda da geçerlidir.")

Tanımda "en az" dediği için **paralelkenar da bir yamuktur** (iki çift paralel kenarı var). Dikdörtgen bir paralelkenar, kare hem dikdörtgen hem eşkenar dörtgendir; eşkenar dörtgen aynı zamanda bir deltoittir.

## 1. Yan kenardaki açılar: toplam 180°

**Örnek 1.** $ABCD$ yamuğunda $[AB] \parallel [DC]$, $m(\widehat{A}) = 70^\circ$ ve $m(\widehat{B}) = 55^\circ$'dir. $m(\widehat{D})$ ve $m(\widehat{C})$ kaçtır?

![ABCD yamuğu, AB alt taban, DC üst taban, ikisinde de paralel oku. A'da 70, D'de 110 derece mavi; B'de 55, C'de 125 derece yeşil.](gorsel/tyt-matematik/25-01-acilar.svg "Aynı renkteki iki açı aynı yan kenarın iki ucundadır; toplamları 180°'dir. A ile B'yi toplama: onlar farklı yan kenarlardadır.")

**Çözüm.**

1. $[AD]$ yan kenarı, iki paralel tabanı kesen bir doğrudur. $\widehat{A}$ ile $\widehat{D}$ bu kesenin aynı tarafındaki iç açılardır; toplamları $180^\circ$'dir: $m(\widehat{D}) = 180^\circ - 70^\circ = 110^\circ$.
2. Aynı şey $[BC]$ için: $m(\widehat{C}) = 180^\circ - 55^\circ = 125^\circ$.
3. Kontrol: $70^\circ + 55^\circ + 125^\circ + 110^\circ = 360^\circ$.

**Kural:**

$$m(\widehat{A}) + m(\widehat{D}) = 180^\circ \qquad m(\widehat{B}) + m(\widehat{C}) = 180^\circ$$

Tersi de doğrudur: bir $ABCD$ dörtgeninde **ardışık** iki açının toplamı $180^\circ$ ise (örneğin $m(\widehat{B}) + m(\widehat{C}) = 180^\circ$), o iki köşeden çıkan öbür kenarlar paraleldir ($[AB] \parallel [DC]$); yani dörtgen bir yamuktur.

> **Tuzak:** $180^\circ$ kuralı **aynı yan kenarın** iki ucundaki açılar içindir ($\widehat{A}$ ile $\widehat{D}$). Aynı tabanın iki ucundaki açılar ($\widehat{A}$ ile $\widehat{B}$) için böyle bir kural yoktur; onlar ancak ikizkenar yamukta eşit olur.

## 2. Açıortaylar: 90° ve ikizkenar üçgen

**Örnek 2.** $ABCD$ yamuğunda $[AB] \parallel [DC]$, $m(\widehat{DAB}) = 64^\circ$ ve $|AD| = 6$ cm'dir. $\widehat{A}$'nın açıortayı $[DC]$'yi $E$'de, $\widehat{D}$'nin açıortayı $[AE]$'yi $P$'de kesiyor. $|DE|$ ve $m(\widehat{DPA})$ kaçtır?

![ABCD yamuğu. A'dan çıkan mavi açıortay DC'yi E'de kesiyor; A'daki iki parça 32'şer derece, E'deki DEA açısı da 32 derece. D'den çıkan yeşil açıortay AE'yi P'de dik kesiyor; D'deki iki parça 58'er derece. AD = 6, DE = 6; ADE üçgeni sarı.](gorsel/tyt-matematik/25-01-aciortay.svg "Sarı ADE üçgeninde iki açı 32°: bu üçgen ikizkenardır, |DE| = |AD|. Yeşil açıortay mavi açıortaya diktir.")

**Çözüm.**

1. Açıortay $\widehat{A}$'yı ikiye böler: $m(\widehat{DAE}) = m(\widehat{EAB}) = 32^\circ$.
2. $[DC] \parallel [AB]$ ve $[AE]$ kesen: $\widehat{DEA}$ ile $\widehat{EAB}$ iç ters açıdır, $m(\widehat{DEA}) = 32^\circ$.
3. $ADE$ üçgeninde iki açı $32^\circ$; eş açıların karşısındaki kenarlar eşittir: $|DE| = |AD| = 6$ cm.
4. $m(\widehat{ADC}) = 180^\circ - 64^\circ = 116^\circ$, yarısı $58^\circ$. $ADP$ üçgeninde $m(\widehat{DPA}) = 180^\circ - 32^\circ - 58^\circ = 90^\circ$.

**Kural:**

- Aynı yan kenardaki iki açının açıortayları **dik** kesişir, çünkü $\dfrac{m(\widehat{A}) + m(\widehat{D})}{2} = \dfrac{180^\circ}{2} = 90^\circ$.
- Bir taban açısının açıortayı karşı tabanı keserse **ikizkenar üçgen** oluşur: $|DE| = |AD|$.

> **Tuzak:** Açıortay karşı tabanı kestiğinde eşit olan, kesilen tabandaki parça ile **açıortayın çıktığı köşenin yan kenarıdır** ($|DE| = |AD|$). $|EC|$ ya da $|AE|$ ile karıştırma.

## 3. Orta taban: tabanların ortalaması

Yan kenarların orta noktalarını birleştiren $[EF]$ doğru parçasına **orta taban** denir. Orta taban tabanlara paraleldir.

**Örnek 3.** $ABCD$ yamuğunda $[AB] \parallel [DC]$, $|AB| = 14$ cm, $|DC| = 6$ cm'dir. $E$ ve $F$ sırasıyla $[AD]$ ve $[BC]$'nin orta noktalarıdır. $|EF|$ kaçtır?

![ABCD yamuğu, AB = 14, DC = 6. E ve F yan kenarların orta noktası, eşit parçalar çentikle işaretli. Mavi EF orta tabanı 10. Kesikli BD köşegeni EF'yi L'de kesiyor; EL = 7, LF = 3.](gorsel/tyt-matematik/25-01-orta-taban.svg "Kesikli köşegen orta tabanı iki üçgenin orta tabanına böler: ABD üçgeninde 14'ün yarısı 7, BCD üçgeninde 6'nın yarısı 3. Toplam 10.")

**Çözüm.**

1. $[BD]$ köşegenini çiz; $[EF]$'yi $L$'de kessin.
2. $ABD$ üçgeninde $E$ ve $L$ kenar orta noktalarıdır. Üçgende orta taban üçüncü kenarın yarısıdır: $|EL| = \dfrac{14}{2} = 7$.
3. $BCD$ üçgeninde aynı şekilde $|LF| = \dfrac{6}{2} = 3$.
4. $|EF| = 7 + 3 = 10$ cm.

**Kural:**

$$|EF| = \frac{a + c}{2}$$

Soru tersten de gelir: $|EF| = 10$ ve $|AB| = 14$ verilirse $14 + c = 20$, yani $c = 6$.

> **Tuzak:** Orta taban tabanların **toplamının** yarısıdır, farkının değil. $\dfrac{14 - 6}{2} = 4$ başka bir parçadır (sonraki kural). Ayrıca $E$ ve $F$'nin gerçekten **orta nokta** olduğunu kontrol et; değilse bu formül kullanılmaz.

## 4. Köşegenler orta tabanı üçe böler

**Örnek 4.** Aynı yamukta ($|AB| = 14$, $|DC| = 6$) $[AC]$ köşegeni $[EF]$'yi $K$'de, $[BD]$ köşegeni $L$'de kesiyor. $|EK|$, $|KL|$ ve $|LF|$ kaçtır?

![ABCD yamuğu, AB = 14, DC = 6, iki köşegen kesikli. EF orta tabanı üç parçaya ayrılmış: EK = 3 ve LF = 3 mavi, ortadaki KL = 4 kırmızı.](gorsel/tyt-matematik/25-01-kosegen.svg "İki uçtaki mavi parça küçük tabanın yarısıdır (3), ortadaki kırmızı parça tabanların farkının yarısıdır (4).")

**Çözüm.**

1. $ADC$ üçgeninde $E$ ile $K$ kenar orta noktalarıdır: $|EK| = \dfrac{|DC|}{2} = 3$.
2. $BCD$ üçgeninde $L$ ile $F$ kenar orta noktalarıdır: $|LF| = \dfrac{|DC|}{2} = 3$.
3. $|KL| = |EF| - 3 - 3 = 10 - 6 = 4$. Bunu doğrudan da bulursun: $|EL| = \dfrac{14}{2} = 7$, $|KL| = 7 - 3 = 4$.

**Kural:**

$$|EK| = |LF| = \frac{c}{2} \qquad |KL| = \frac{a - c}{2}$$

> **Tuzak:** Uçtaki parçalar **küçük** tabanın yarısıdır ($\frac{c}{2}$), büyük tabanın değil. Ortadaki parça tabanların farkının **yarısıdır**; ikiye bölmeyi unutursan $a - c = 8$ bulursun.

## ÖSYM tuzakları

> **Yanlış açı çifti.** $m(\widehat{A}) = 70^\circ$ verildiğinde $m(\widehat{B}) = 110^\circ$ yazmak yanlış. $110^\circ$ olan, aynı yan kenardaki $\widehat{D}$'dir.

> **"Paralelkenar yamuk değildir" sanmak.** Tanım "en az iki kenarı paralel" der. Paralelkenar, dikdörtgen ve kare de yamuktur; yamuk kuralları onlarda da çalışır.

> **$x$'te durmak.** Açılar $3x - 10^\circ$ gibi verildiğinde önce $x$ bulunur; soru genelde bir **açıyı** ister. $x$'in değeri seçeneklerde bekler.

> **Orta taban ile $KL$'yi karıştırmak.** $\frac{a + c}{2}$ orta tabanın tamamı, $\frac{a - c}{2}$ köşegenler arasındaki parçadır. Seçeneklerde ikisi de olur.

> **Uçtaki parçaya $\frac{a}{2}$ demek.** $|EK| = \frac{c}{2}$'dir. $\frac{a}{2}$ ise $|EL|$'dir: $E$'den uzaktaki köşegene kadar olan uzunluk.

## Kendini dene

### Soru 1
$ABCD$ yamuğunda $[AB] \parallel [DC]$, $m(\widehat{DAB}) = 2x + 10^\circ$ ve $m(\widehat{ADC}) = 3x - 5^\circ$'dir. Buna göre $m(\widehat{ADC})$ kaç derecedir?

A) 35
B) 70
C) 80
D) 100
E) 105

**Cevap:** D
**Çözüm:** $\widehat{A}$ ile $\widehat{D}$ aynı yan kenardadır: $(2x + 10) + (3x - 5) = 180 \Rightarrow 5x + 5 = 180 \Rightarrow x = 35$. $m(\widehat{ADC}) = 3 \cdot 35 - 5 = 100^\circ$. Kontrol: $m(\widehat{A}) = 80^\circ$, toplam $180^\circ$. $35$ $x$'in kendisidir, $70$ $2x$'tir, $80$ öbür açıdır, $105$ ise $3x$'te durup $5$'i çıkarmamaktır.

### Soru 2
$ABCD$ yamuğunda $[AB] \parallel [DC]$; $E$ ve $F$ sırasıyla $[AD]$ ve $[BC]$'nin orta noktalarıdır. $|EF| = 11$ cm ve $|DC| = 7$ cm ise $|AB|$ kaç cm'dir?

A) 4
B) 9
C) 15
D) 18
E) 22

**Cevap:** C
**Çözüm:** $\dfrac{|AB| + 7}{2} = 11 \Rightarrow |AB| + 7 = 22 \Rightarrow |AB| = 15$. $4$, $11 - 7$ farkıdır; $9$, $11$ ile $7$'nin ortalamasıdır; $18$, $11 + 7$; $22$ ise $7$'yi çıkarmayı unutmaktır.

### Soru 3
![ABCD yamuğu, AB = 16, DC = 6. E ve F yan kenarların orta noktaları; köşegenler EF'yi K ve L'de kesiyor. KL parçası soru işaretiyle kırmızı.](gorsel/tyt-matematik/25-01-kd3.svg "[AC] köşegeni K'de, [BD] köşegeni L'de.")

Şekildeki $ABCD$ yamuğunda $[AB] \parallel [DC]$, $[EF]$ orta taban, $|AB| = 16$ birim ve $|DC| = 6$ birimdir. $[AC]$ ve $[BD]$ köşegenleri $[EF]$'yi $K$ ve $L$ noktalarında kestiğine göre $|KL|$ kaç birimdir?

A) 3
B) 5
C) 8
D) 10
E) 11

**Cevap:** B
**Çözüm:** $|KL| = \dfrac{16 - 6}{2} = 5$. Kontrol: $|EF| = \dfrac{16 + 6}{2} = 11$, uçtaki parçalar $\dfrac{6}{2} = 3$'er; $11 - 3 - 3 = 5$. $3$ uçtaki parçadır, $10$ ikiye bölmeyi unutmaktır, $11$ orta tabanın tamamıdır.

## Özet kartı

- Yamuk: en az iki kenarı paralel dörtgen. Paralelkenar, dikdörtgen ve kare de yamuktur.
- Aynı yan kenardaki iki açı: toplam $180^\circ$ ($\widehat{A} + \widehat{D}$, $\widehat{B} + \widehat{C}$).
- Bu iki açının açıortayları dik kesişir; taban açısının açıortayı karşı tabanı keserse ikizkenar üçgen oluşur.
- Orta taban: $|EF| = \dfrac{a + c}{2}$.
- Köşegenler orta tabanı üçe böler: uçlar $\dfrac{c}{2}$, orta $\dfrac{a - c}{2}$.

## Sonraki adım

Alıştırmaya geç (aşağıdaki düğme). Sonraki ders: **İkizkenar ve Dik Yamuk**. Orada bugünkü kurallara, yan kenarları eşit ya da tabana dik olan yamukların ek özellikleri eklenecek.
