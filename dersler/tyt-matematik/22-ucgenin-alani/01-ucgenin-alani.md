---
baslik: Üçgenin Alanı
ders: tyt-matematik
sure: 25 dk
kaynak: MEBİ Konu Özeti f7d58464ab
guncelleme: 2026-11-18
---
# Üçgenin Alanı

<div class="giris" dir="rtl" lang="ar">

**الدرس ده عن إيه؟** عن مساحة المثلث (üçgenin alanı): إزاي تحسبها من أي ضلع تختاره قاعدة (taban) ومن الارتفاع (yükseklik) النازل عليه.

- هتعرف ليه المساحة دايمًا نص حاصل ضرب القاعدة في الارتفاع، وإن الأضلاع التلاتة بيدّوا نفس المساحة.
- هتتعلم إن في المثلث القائم (dik üçgen) الضلعين القائمين هما القاعدة والارتفاع، وإن في المثلث المنفرج (geniş açılı üçgen) الارتفاع ممكن ينزل برّه المثلث.
- هتحسب الارتفاع بفيثاغورس (Pisagor) لما ميكونش مكتوب، زي في المثلث المتساوي الساقين (ikizkenar) والمتساوي الأضلاع (eşkenar).

**ليه مهم؟** المساحة بتيجي في أسئلة هندسة كتير في TYT، سواء لوحدها أو جوه سؤال أكبر، وأغلب الغلط بيبقى من نسيان القسمة على اتنين أو إنك تاخد ضلع مايل بدل الارتفاع.

الدرس ٢٥ دقيقة، وكل قاعدة معاها رسمة ومثال محلول. امسك ورقة وقلم وامشي معانا خطوة بخطوة.

</div>

**Bu dersin sonunda:** bir üçgende herhangi bir kenarı taban seçip o kenara ait yüksekliği (içeride, kenar üzerinde ya da dışarıda) bularak alanı hesaplayabileceksin.

> **TYT'de yeri:** Geometri sorularının büyük kısmında bir yerde alan geçer. Soru ya doğrudan "alanı kaç birimkaredir?" diye sorar ya da alanı bir ara adım olarak kullanır: iki farklı kenarla alan yazılır, bilinmeyen yükseklik bulunur. Geniş açılı üçgende dışarıya düşen yükseklik ve kareli zemine çizilmiş üçgenler sık görülür.

## Önce hatırla

<details><summary>Geçen dersten: Birim çember üzerindeki K noktası 2. bölgededir ve apsisi −3/5'tir. K'nin ordinatı kaçtır?</summary>
Birim çemberde her nokta için x² + y² = 1. y² = 1 − 9/25 = 16/25, yani y = 4/5 ya da −4/5. 2. bölgede ordinat pozitiftir: <b>4/5</b>. Bunu bulmak için K'den x eksenine bir dikme indirip dik üçgende Pisagor kullandın. Bugün de dikmeler ve Pisagor her yerde.
</details>

<details><summary>Geçen dersten: Birim çemberde OK yarıçapı x ekseninin pozitif yönüyle α dar açısını yapıyor. K'den x eksenine inen dikmenin uzunluğu nedir?</summary>
K'nin koordinatları (cos α, sin α) olduğu için dikmenin uzunluğu <b>sin α</b>'dır. Bu dikme, O, K ve A(1, 0) noktalarının oluşturduğu üçgenin OA tabanına ait <b>yüksekliğidir</b>. Bugün yüksekliği taban ile çarpıp alanı bulacaksın.
</details>

## 1. Temel kural: taban çarpı yükseklik bölü 2

**Örnek 1.** $ABC$ üçgeninde $[AH] \perp [BC]$, $|BC| = 10$ birim ve $|AH| = 6$ birimdir. $A(ABC)$ kaç birimkaredir?

**Çözüm.**

1. Taban $[BC]$, bu tabana ait yükseklik $[AH]$: $A$ köşesinden $[BC]$'ye inen dik parça.
2. Üçgeni, tabanı $10$ ve yüksekliği $6$ olan bir dikdörtgenin içine yerleştir. $[AH]$ dikdörtgeni iki parçaya böler; $[AB]$ ve $[AC]$ bu parçaların her birini tam ortadan ikiye keser.
3. Dikdörtgenin alanı $10 \cdot 6 = 60$. Üçgen bunun yarısıdır: $A(ABC) = \dfrac{10 \cdot 6}{2} = 30$ birimkare.

![Tabanı BC = 10, yüksekliği AH = 6 olan ABC üçgeni; çevresinde kesikli çizgiyle 10 x 6 dikdörtgen. Üçgenin içi mavi, dikdörtgenin üçgen dışında kalan iki köşe parçası sarı boyalı.](gorsel/tyt-matematik/22-01-dikdortgen.svg "Sarı parçalar, AH'nin iki yanındaki mavi parçalarla birebir aynıdır. Üçgen, dikdörtgenin tam yarısı: 60'ın yarısı 30.")

**Kural:** Bir kenara ait yükseklik, karşı köşeden o kenara (gerekirse uzantısına) inen dik parçadır. $a = |BC|$ kenarına ait yükseklik $h_a$ ile gösterilir.

$$A(ABC) = \frac{a \cdot h_a}{2}$$

Formülde yalnızca taban ve yükseklik var. Bu yüzden tabanı ve yüksekliği aynı olan iki üçgenin alanı eşittir, biçimleri ne kadar farklı olursa olsun. Şekilde $A$ köşesini $[BC]$'ye paralel bir doğru üzerinde kaydırsan yükseklik hep $6$ kalır, alan da hep $30$.

> **Tuzak:** İkiye bölmeyi unutmak. $10 \cdot 6 = 60$ dikdörtgenin alanıdır, üçgeninki değil. İkinci sık yanlış: yükseklik yerine eğik bir kenarı almak. $|AC|$ ile $|BC|$'nin çarpımının yarısı alan **değildir**; çarpılan iki uzunluk birbirine dik olmalı.

## 2. Üç kenar, üç yükseklik, tek alan

**Örnek 2.** Kenarları $|AB| = 13$, $|BC| = 14$ ve $|AC| = 15$ olan $ABC$ üçgeninde $A$'dan $[BC]$'ye inen yükseklik $12$'dir. $B$'den $[AC]$'ye inen yükseklik ($h_b$) kaçtır?

**Çözüm.**

1. Tabanı $[BC]$ seç: $A(ABC) = \dfrac{14 \cdot 12}{2} = 84$.
2. Aynı üçgenin alanını tabanı $[AC]$ seçerek de yazabilirsin: $A(ABC) = \dfrac{15 \cdot h_b}{2}$.
3. İkisi aynı alandır: $\dfrac{15 \cdot h_b}{2} = 84 \Rightarrow h_b = \dfrac{168}{15} = 11{,}2$.

![Kenarları 13, 14, 15 olan ABC üçgeni. A'dan BC'ye kırmızı AH = 12 yüksekliği, B'den AC'ye yeşil BF yüksekliği iniyor; F, AC üzerinde.](gorsel/tyt-matematik/22-01-uc-yukseklik.svg "Kırmızı yükseklik 14'lük kenara, yeşil yükseklik 15'lik kenara aittir. Uzun kenarın yüksekliği kısadır: 11,2 < 12.")

**Kural:** Hangi kenarı taban seçersen seç alan değişmez.

$$A(ABC) = \frac{a \cdot h_a}{2} = \frac{b \cdot h_b}{2} = \frac{c \cdot h_c}{2} \qquad\Rightarrow\qquad a \cdot h_a = b \cdot h_b = c \cdot h_c$$

Kenar ile yüksekliğin çarpımı sabit olduğu için **en uzun kenarın yüksekliği en kısadır**, en kısa kenarın yüksekliği en uzundur. Örnekte $13$'lük kenara ait yükseklik $\dfrac{168}{13} \approx 12{,}9$ ile en uzundur.

> **Tuzak:** Yükseklikleri kenarlarla **doğru** orantılı sanmak. "$15$'lik kenarın yüksekliği $14$'lükten büyüktür" diye $12 \cdot \dfrac{15}{14}$ yazmak yanlıştır. Orantı terstir: kenar büyüdükçe yükseklik küçülür.

## 3. Dik üçgen: dik kenarlar birbirinin yüksekliği

**Örnek 3.** $[AB] \perp [AC]$, $|AB| = 12$ ve $|AC| = 16$ olan $ABC$ üçgeninin alanı kaçtır? $A$'dan hipotenüse inen yükseklik kaçtır?

**Çözüm.**

1. $[AB]$, $[AC]$'ye diktir. Yani $[AC]$'yi taban alırsan yüksekliği $[AB]$'nin kendisidir: $A(ABC) = \dfrac{12 \cdot 16}{2} = 96$.
2. Hipotenüs: $|BC|^2 = 12^2 + 16^2 = 400 \Rightarrow |BC| = 20$.
3. Hipotenüsü taban al: $\dfrac{20 \cdot |AH|}{2} = 96 \Rightarrow |AH| = \dfrac{192}{20} = 9{,}6$.

![A'da dik açılı ABC üçgeni: AB = 12 ve AC = 16 dik kenarları mavi ve kalın, BC = 20 hipotenüs. A'dan BC'ye kesikli kırmızı AH = 9,6 yüksekliği.](gorsel/tyt-matematik/22-01-dik.svg "Mavi iki kenar birbirine diktir: biri taban, öbürü yükseklik. Hipotenüsün yüksekliği ayrıca çizilmesi gereken kesikli kırmızı parçadır.")

**Kural:** $[AB] \perp [AC]$ ise

$$A(ABC) = \frac{|AB| \cdot |AC|}{2} = \frac{|BC| \cdot h_a}{2}$$

Bu eşitlik geçen dersten tanıdık: $|AB| \cdot |AC| = |BC| \cdot h_a$. Hipotenüse ait yüksekliği bulmanın en kısa yolu budur.

> **Tuzak:** Dik kenar ile hipotenüsü çarpmak: $\dfrac{16 \cdot 20}{2} = 160$ yanlıştır, çünkü $[AC]$ ile $[BC]$ birbirine dik değildir. Dik üçgende çarpılacak iki kenar, **dik açıyı yapan** iki kenardır.

## 4. Geniş açılı üçgen: yükseklik dışarıya düşer

**Örnek 4.** $ABC$ üçgeninde $\widehat{B}$ geniş açıdır. $A$'dan $BC$ doğrusuna inen dikmenin ayağı $H$, $B$'nin dışında kalıyor. $|HB| = 4$, $|BC| = 6$ ve $|AH| = 8$ ise $A(ABC)$ kaçtır?

**Çözüm.**

1. $\widehat{B}$ geniş olduğu için $A$'dan inen dikme $[BC]$ kenarına değil, onun $B$'den öteye **uzantısına** iner. Yükseklik yine $|AH| = 8$'dir.
2. Taban yalnızca $[BC]$'dir: $A(ABC) = \dfrac{6 \cdot 8}{2} = 24$.
3. Kontrol: büyük dik üçgen $AHC$'nin alanı $\dfrac{10 \cdot 8}{2} = 40$, dışarıdaki $AHB$'ninki $\dfrac{4 \cdot 8}{2} = 16$. Fark: $40 - 16 = 24$. Tutuyor.

![B'de geniş açılı ABC üçgeni (mavi). CB kenarı B'nin ötesine kesikli çizgiyle uzatılmış; A'dan bu uzantıya kırmızı AH = 8 dikmesi iniyor. HB = 4, BC = 6. AHB üçgeni sarı.](gorsel/tyt-matematik/22-01-genis.svg "Yükseklik üçgenin dışında, ama alan yalnızca mavi üçgenin alanıdır: taban 6, yükseklik 8. Sarı parça hesaba girmez.")

**Kural:** Geniş açılı üçgende dar açılı iki köşeden inen yükseklikler dışarıya, karşı kenarların uzantısına düşer. Formül değişmez: taban yalnızca kenarın kendisidir.

| Üçgen | Yükseklikler nerede? |
|---|---|
| Dar açılı | Üçü de üçgenin içinde |
| Dik açılı | İkisi dik kenarların kendisi, hipotenüsünki içeride |
| Geniş açılı | Geniş açıdan inen içeride, öbür ikisi dışarıda |

> **Tuzak:** Tabana dışarıdaki parçayı eklemek: $\dfrac{(6 + 4) \cdot 8}{2} = 40$, $ABC$'nin değil $AHC$'nin alanıdır. Ayrıca $|AB|$ eğik kenarını yükseklik sanma; yükseklik her zaman tabanın doğrusuna **dik** inen parçadır.

## 5. Yükseklik verilmemişse: Pisagor ile bul

**Örnek 5.** (a) $|AB| = |AC| = 5$ ve $|BC| = 8$ olan ikizkenar üçgenin alanı kaçtır? (b) Kenarı $6$ olan eşkenar üçgenin alanı kaçtır?

**Çözüm.**

1. (a) İkizkenar üçgende tepe köşesinden tabana inen yükseklik tabanı **iki eşit** parçaya böler: $|BH| = |HC| = 4$.
2. $ABH$ dik üçgeninde Pisagor: $|AH|^2 = 5^2 - 4^2 = 9 \Rightarrow |AH| = 3$. Alan: $\dfrac{8 \cdot 3}{2} = 12$.
3. (b) Eşkenar üçgende de yükseklik tabanı ikiye böler: parçalar $3$ ve $3$. $h^2 = 6^2 - 3^2 = 27 \Rightarrow h = 3\sqrt{3}$. (Bu, $30^\circ$–$60^\circ$–$90^\circ$ üçgenidir.)
4. Alan: $\dfrac{6 \cdot 3\sqrt{3}}{2} = 9\sqrt{3}$.

![Solda kenarları 5, 5, 8 olan ikizkenar ABC üçgeni; A'dan tabana inen AH = 3 yüksekliği tabanı 4 ve 4 olarak bölüyor. Sağda kenarı 6 olan eşkenar DEF üçgeni; D'den inen DK = 3 kök 3 yüksekliği tabanı 3 ve 3 olarak bölüyor.](gorsel/tyt-matematik/22-01-ikizkenar-eskenar.svg "İki üçgende de kırmızı yükseklik tabanın tam ortasına iner. Böylece yarım taban, yükseklik ve yan kenar bir dik üçgen kurar: 3-4-5 ve 3, 3√3, 6.")

**Kural:** Yükseklik verilmemişse onu bir dik üçgenin kenarı olarak gör ve Pisagor ile bul. Kenarı $a$ olan eşkenar üçgende:

$$h = \frac{a\sqrt{3}}{2} \qquad A = \frac{a^2\sqrt{3}}{4}$$

Kontrol: $a = 6$ için $\dfrac{36\sqrt{3}}{4} = 9\sqrt{3}$.

> **Tuzak:** İkizkenar üçgende yan kenarı yükseklik sanmak: $\dfrac{8 \cdot 5}{2} = 20$ yanlıştır. Pisagor'da da tabanın **yarısını** kullan; $5^2 - 8^2$ negatif çıkar, bu da yanlış yolda olduğunu gösterir.

## ÖSYM tuzakları

> **İkiye bölmeyi unutmak.** Taban çarpı yükseklik dikdörtgenin alanıdır. Seçeneklerde doğru cevabın iki katı hemen her zaman bulunur.

> **Eğik kenarı yükseklik sanmak.** Çarptığın iki uzunluk birbirine dik mi? Değilse biri yükseklik değildir.

> **Dışarıdaki parçayı tabana katmak.** Geniş açılı üçgende yükseklik uzantıya iner; taban yine yalnızca kenarın kendisidir.

> **Yükseklikleri kenarlarla doğru orantılı sanmak.** $a \cdot h_a = b \cdot h_b$: kenar büyüdükçe yüksekliği küçülür.

> **Tepe kaydırılınca alan değişir sanmak.** Taban sabit ve karşı köşe tabana paralel bir doğru üzerinde kayıyorsa yükseklik değişmez, alan da değişmez. Üçgenin biçimi ve çevresi ise değişir.

## Kendini dene

### Soru 1
![C'de geniş açılı ABC üçgeni. BC = 5, BC doğrusu C'nin ötesine kesikli çizgiyle uzatılmış, CH = 3. A'dan bu uzantıya kırmızı AH = 4 dikmesi iniyor. AC = 5.](gorsel/tyt-matematik/22-01-kd1.svg "H noktası BC doğrusu üzerinde, C'nin ötesindedir.")

Şekilde $H$, $BC$ doğrusu üzerindedir; $[AH] \perp [BH]$, $|BC| = 5$, $|CH| = 3$, $|AH| = 4$ ve $|AC| = 5$ birimdir. Buna göre $A(ABC)$ kaç birimkaredir?

A) 6
B) 10
C) 12,5
D) 16
E) 20

**Cevap:** B
**Çözüm:** Taban $[BC]$, yükseklik dışarıya inen $[AH]$: $A(ABC) = \dfrac{5 \cdot 4}{2} = 10$. Kontrol: $A(ABH) - A(ACH) = \dfrac{8 \cdot 4}{2} - \dfrac{3 \cdot 4}{2} = 16 - 6 = 10$. $16$, tabana $|CH|$'yi eklemektir; $6$ dışarıdaki $ACH$ üçgeninin alanı; $12{,}5$ eğik $[AC]$ kenarını yükseklik sanmak; $20$ ise ikiye bölmeyi unutmaktır.

### Soru 2
Bir üçgenin iki kenarının uzunlukları $10$ cm ve $15$ cm'dir. $15$ cm'lik kenara ait yükseklik $8$ cm ise $10$ cm'lik kenara ait yükseklik kaç cm'dir?

A) 16/3
B) 8
C) 12
D) 15
E) 24

**Cevap:** C
**Çözüm:** Alan: $\dfrac{15 \cdot 8}{2} = 60$. Öbür kenarla: $\dfrac{10 \cdot h}{2} = 60 \Rightarrow h = 12$. Kısa yol: $10 \cdot h = 15 \cdot 8$. $16/3$, yükseklikleri kenarlarla doğru orantılı sanmaktır ($8 \cdot \frac{10}{15}$); $24$ ise alanı ikiye bölmeden $120$ almaktır.

### Soru 3
İkizkenar bir $ABC$ üçgeninde $|AB| = |AC| = 13$ cm ve $|BC| = 10$ cm'dir. Bu üçgenin alanı kaç cm²'dir?

A) 30
B) 60
C) 65
D) 78
E) 120

**Cevap:** B
**Çözüm:** $A$'dan inen yükseklik tabanı $5$ ve $5$'e böler. $h^2 = 13^2 - 5^2 = 144 \Rightarrow h = 12$. Alan: $\dfrac{10 \cdot 12}{2} = 60$. $65$, yan kenarı yükseklik sanmak ($\frac{10 \cdot 13}{2}$); $78$, yan kenarı taban sanmak ($\frac{13 \cdot 12}{2}$); $30$, yarım tabanla hesaplamak; $120$ ise ikiye bölmeyi unutmaktır.

## Özet kartı

- $A(ABC) = \dfrac{a \cdot h_a}{2}$: yükseklik, karşı köşeden taban doğrusuna inen **dik** parçadır.
- Her kenar taban olabilir: $a \cdot h_a = b \cdot h_b = c \cdot h_c$. Uzun kenarın yüksekliği kısadır.
- Dik üçgen: alan, iki dik kenarın çarpımının yarısıdır.
- Geniş açılı üçgen: iki yükseklik dışarıya düşer; taban yine yalnızca kenarın kendisidir.
- Yükseklik verilmemişse Pisagor ile bul. Eşkenar üçgen: $h = \dfrac{a\sqrt{3}}{2}$, $A = \dfrac{a^2\sqrt{3}}{4}$.
- Taban ve yükseklik aynıysa alan aynıdır; tepe tabana paralel kayınca alan değişmez.

## Sonraki adım

Alıştırmaya geç (aşağıdaki düğme). Sonraki ders: **Üçgenin Alanıyla İlgili Uygulamalar**. Orada aynı yüksekliğe sahip üçgenlerin alan oranlarını, kenarortayın üçgeni nasıl böldüğünü ve iki kenar ile aradaki açıdan alan bulmayı göreceksin.
