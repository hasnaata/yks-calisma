---
baslik: Düzgün Dört Yüzlü
ders: tyt-matematik
sure: 20 dk
kaynak: MEBİ Konu Özeti 0e0c5c451f
guncelleme: 2026-11-18
---
# Düzgün Dört Yüzlü

<div class="giris" dir="rtl" lang="ar">

**الدرس ده عن إيه؟** عن رباعي الأوجه المنتظم (düzgün dört yüzlü): هرم مثلثي (üçgen piramit) كل أوجهه الأربعة مثلثات متساوية الأضلاع (eşkenar üçgen)، وكل أحرفه (ayrıt) نفس الطول.

- هتعرف تحسب ارتفاع الوجه (yan yüz yüksekliği) والمساحة الكلية (yüzey alanı) من طول حرف واحد.
- هتتعلم إزاي تطلّع ارتفاع المجسم (yükseklik) بفيثاغورس (Pisagor) والحجم (hacim) من غير ما تحفظ حاجة كتير.
- هتشوف إزاي رباعي الأوجه ده بيستخبى جوه مكعب (küp)، وإزاي الحجم بيتغير لما الحرف يكبر.

**ليه مهم؟** في TYT السؤال بيدّيك طول واحد بس (حرف، ارتفاع، أو مساحة) ويطلب منك طول تاني أو الحجم، واللي فاهم العلاقات بيحلها في دقيقة.

الدرس ٢٠ دقيقة، وكل قاعدة معاها رسمة ومثال محلول، فخدها خطوة خطوة.

</div>

**Bu dersin sonunda:** bir ayrıtı, yüksekliği ya da yüzey alanı verilen düzgün dört yüzlünün öbür uzunluklarını ve hacmini bulabileceksin.

> **TYT'de yeri:** Düzgün dört yüzlü genelde tek bir uzunlukla verilir (ayrıt, yükseklik, yan yüz yüksekliği ya da ayrıtlar toplamı) ve soru başka birini ya da hacmi ister. "Yeni nesil" sorularda bir küpün köşeleri birleştirilir, eşkenar üçgen bir karton katlanır ya da iki dört yüzlü yapıştırılır.

## Önce hatırla

<details><summary>Geçen dersten: Taban ayrıtı 8, yüksekliği 3 olan kare dik piramidin yan yüz yüksekliği kaçtır?</summary>
Tepeden tabana inen dikme, karenin merkezine düşer. Merkezden bir taban ayrıtının orta noktasına uzaklık $\dfrac{8}{2} = 4$. Dik üçgen: $h_Y^2 = 3^2 + 4^2 = 25$, $h_Y =$ <b>5</b>. Bugün aynı dik üçgen fikrini eşkenar üçgen tabanda kullanacaksın.
</details>

<details><summary>Geçen dersten: Taban ayrıtı 6, yüksekliği 5 olan kare dik piramidin hacmi kaçtır?</summary>
$V = \dfrac{A_T \cdot h}{3} = \dfrac{36 \cdot 5}{3} =$ <b>60</b>. Düzgün dört yüzlü de bir piramittir; hacmi yine "taban alanı çarpı yükseklik bölü 3".
</details>

## Düzgün dört yüzlü nedir?

**Bütün yüzleri eş eşkenar üçgen olan üçgen piramide düzgün dört yüzlü** denir. Bütün ayrıtları eşittir; hangi yüzü tabana koyarsan koy, cisim aynı görünür.

| Eleman | Sayı | Not |
|---|---|---|
| Yüz | 4 | Hepsi kenarı $a$ olan eşkenar üçgen |
| Ayrıt | 6 | 3 taban ayrıtı + 3 yanal ayrıt, hepsi $a$ |
| Köşe | 4 | Her köşede 3 ayrıt ve 3 yüz birleşir |

**Örnek 1.** Bir düzgün dört yüzlünün bütün ayrıtlarının uzunlukları toplamı $42$ cm'dir. Bir ayrıtı kaç cm'dir?

**Çözüm.** 6 ayrıtın hepsi eşittir: $6a = 42 \Rightarrow a = 7$ cm.

![TABC düzgün dört yüzlüsü. Ön yüz TAB açık mavi; arkadaki C köşesine giden üç ayrıt kesikli. Altı ayrıtın her birinin yanında a yazıyor.](gorsel/tyt-matematik/26-04-elemanlar.svg "Altı ayrıtın hepsi a. Kesikli çizgiler arkada kalan ayrıtlardır; onlar da a uzunluğundadır.")

**Kural:** Ayrıtı $a$ olan düzgün dört yüzlünün ayrıtlar toplamı $6a$'dır.

> **Tuzak:** Küpten alışkanlıkla 12'ye bölmek ($42 : 12 = 3{,}5$) ya da yalnızca taban ayrıtlarını sayıp 3'e bölmek ($14$). Dört yüzlüde **4** yüz, **4** köşe, **6** ayrıt vardır.

## 1. Yan yüz yüksekliği ve yüzey alanı

**Örnek 2.** Ayrıtı $4$ cm olan düzgün dört yüzlünün yan yüz yüksekliği ve yüzey alanı kaçtır?

**Çözüm.**

1. Her yüz kenarı $4$ olan eşkenar üçgendir. Yüksekliği kenarı iki eş parçaya böler; Pisagor: $h_Y^2 = 4^2 - 2^2 = 12 \Rightarrow h_Y = 2\sqrt{3}$ cm.
2. Bir yüzün alanı: $\dfrac{4 \cdot 2\sqrt{3}}{2} = 4\sqrt{3}$ cm².
3. Dört eş yüz: $A = 4 \cdot 4\sqrt{3} = 16\sqrt{3}$ cm².

![Kenarı 8 olan büyük eşkenar üçgen; kenarlarının orta noktaları A, B, C kesikli çizgilerle birleşmiş. Ortadaki sarı üçgen taban, çevresindeki üç mavi üçgenin dış köşeleri T. Üstteki üçgende T'den AB'ye kırmızı yükseklik, uzunluğu 2 kök 3.](gorsel/tyt-matematik/26-04-acinim.svg "Açınım: kesikli çizgilerden katlayınca üç T köşesi buluşur. Dört küçük üçgenin toplam alanı yüzey alanıdır.")

**Kural:** Ayrıtı $a$ olan düzgün dört yüzlüde

$$h_Y = \frac{a\sqrt{3}}{2} \qquad \text{bir yüzün alanı} = \frac{a^2\sqrt{3}}{4} \qquad A = 4 \cdot \frac{a^2\sqrt{3}}{4} = a^2\sqrt{3}$$

Tersten de git: yüzey alanı $25\sqrt{3}$ ise $a^2 = 25$, $a = 5$.

> **Tuzak:** Yüzey alanına bir yüzün alanını ($\frac{a^2\sqrt{3}}{4}$) yazıp bırakmak ya da "yanal alan" diye üç yüzü ($\frac{3a^2\sqrt{3}}{4}$) almak. Soru "yüzey alanı" diyorsa **dört** yüzü say.

## 2. Yükseklik

**Örnek 3.** Ayrıtı $6$ cm olan $TABC$ düzgün dört yüzlüsünde $T$'den tabana inen dikmenin ayağı $H$ olsun. $|AH|$ ve $|TH|$ kaçtır?

**Çözüm.**

1. Dört yüzlü düzgün olduğundan $H$, $ABC$ eşkenar üçgeninin **ağırlık merkezidir**. $[BC]$'nin orta noktası $D$ olsun; $[AD]$ kenarortaydır ve aynı zamanda yüksekliktir: $|AD| = \dfrac{6\sqrt{3}}{2} = 3\sqrt{3}$.
2. Ağırlık merkezi kenarortayı köşeden $2 : 1$ oranında böler: $|AH| = \dfrac{2}{3} \cdot 3\sqrt{3} = 2\sqrt{3}$.
3. $[TH]$ tabana dik, bu yüzden $TAH$ üçgeni $H$'de diktir ve hipotenüsü $|TA| = 6$'dır: $|TH|^2 = 6^2 - (2\sqrt{3})^2 = 36 - 12 = 24 \Rightarrow |TH| = 2\sqrt{6}$ cm.

![TABC düzgün dört yüzlüsü, ayrıtları 6. Tabanda A'dan BC'nin orta noktası D'ye yeşil kenarortay; üzerindeki H noktasına kadar olan kısım kalın yeşil ve 2 kök 3. T'den H'ye kırmızı dikme h; H'de dik açı işareti.](gorsel/tyt-matematik/26-04-yukseklik.svg "TAH dik üçgeni: hipotenüs bir ayrıt (6), bir dik kenar AH (kenarortayın üçte ikisi), öbür dik kenar yükseklik.")

**Kural:** Ayrıtı $a$ olan düzgün dört yüzlüde

$$|AH| = \frac{2}{3} \cdot \frac{a\sqrt{3}}{2} = \frac{a\sqrt{3}}{3} \qquad h^2 = a^2 - \frac{a^2}{3} = \frac{2a^2}{3} \qquad h = \frac{a\sqrt{6}}{3}$$

Formülü unutursan $TAH$ dik üçgenini kurman yeter. Yükseklik verilirse tersten git: $h = 4\sqrt{6}$ ise $\dfrac{a\sqrt{6}}{3} = 4\sqrt{6}$, $a = 12$.

> **Tuzak:** $|AH|$ yerine bütün kenarortayı ($|AD| = 3\sqrt{3}$) almak: $36 - 27 = 9$, $h = 3$ yanlıştır. Bir de yüksekliği yan yüz yüksekliğiyle ($3\sqrt{3}$) karıştırmak. $h$ cismin **içinden** iner ve $h_Y$'den kısadır: $2\sqrt{6} \approx 4{,}9 < 3\sqrt{3} \approx 5{,}2$.

## 3. Hacim

**Örnek 4.** Ayrıtı $3\sqrt{2}$ cm olan düzgün dört yüzlünün hacmi kaç cm³'tür?

**Çözüm.**

1. Taban alanı: $\dfrac{(3\sqrt{2})^2\sqrt{3}}{4} = \dfrac{18\sqrt{3}}{4} = \dfrac{9\sqrt{3}}{2}$.
2. Yükseklik: $h = \dfrac{3\sqrt{2} \cdot \sqrt{6}}{3} = \sqrt{12} = 2\sqrt{3}$.
3. Hacim: $V = \dfrac{A_T \cdot h}{3} = \dfrac{1}{3} \cdot \dfrac{9\sqrt{3}}{2} \cdot 2\sqrt{3} = \dfrac{1}{3} \cdot 27 = 9$ cm³.

![Tabanı ABC eşkenar üçgeni olan, yüksekliği h olan üçgen dik prizma ince siyah çizgilerle. İçinde tepesi T üst yüzün ortasında olan mavi dört yüzlü. Taban sarı, T'den tabandaki H'ye kırmızı yükseklik h.](gorsel/tyt-matematik/26-04-hacim.svg "Dört yüzlü, kendisiyle aynı tabanlı ve aynı yükseklikli prizmanın üçte biridir. Prizma bu tür üç eş hacimli piramide bölünebilir.")

**Kural:** Her piramitte olduğu gibi $V = \dfrac{A_T \cdot h}{3}$. Düzgün dört yüzlüde bu,

$$V = \frac{1}{3} \cdot \frac{a^2\sqrt{3}}{4} \cdot \frac{a\sqrt{6}}{3} = \frac{a^3\sqrt{2}}{12}$$

Kontrol: $a = 3\sqrt{2}$ için $\dfrac{(3\sqrt{2})^3 \cdot \sqrt{2}}{12} = \dfrac{54\sqrt{2} \cdot \sqrt{2}}{12} = \dfrac{108}{12} = 9$. Ayrıt $k$ katına çıkarsa yüzey alanı $k^2$, hacim $k^3$ katına çıkar.

> **Tuzak:** $3$'e bölmeyi unutmak ($27$, prizmanın hacmi) ya da taban alanında $4$'e bölmeyi unutmak ($a^2\sqrt{3}$ bütün yüzey alanıdır, bir yüz değil). Hacimde yükseklik olarak $h_Y$ değil $h$ kullanılır.

## 4. Küpün içindeki dört yüzlü

**Örnek 5.** Ayrıtı $3$ cm olan $ABCDEFGH$ küpünde $B$, $D$, $E$, $G$ köşeleri birbirine birleştiriliyor. Oluşan cisim nedir, hacmi kaç cm³'tür?

**Çözüm.**

1. Birleştirilen altı doğru parçasının her biri küpün bir yüzünün köşegenidir: hepsi $3\sqrt{2}$. Altı ayrıtı eşit üçgen piramit, düzgün dört yüzlüdür.
2. Küpten geriye 4 köşe parçası kalır. Örneğin $A$ köşesindeki parça $(B, D, E)$ ile kesilen piramittir: tabanı dik kenarları $3$ olan dik üçgen, yüksekliği $3$. Hacmi $\dfrac{1}{3} \cdot \dfrac{3 \cdot 3}{2} \cdot 3 = \dfrac{9}{2}$.
3. Dört yüzlünün hacmi: $27 - 4 \cdot \dfrac{9}{2} = 27 - 18 = 9$ cm³. Örnek 4'teki dört yüzlüyle aynı: ayrıtı yine $3\sqrt{2}$.

![Ayrıtı 3 olan ABCDEFGH küpü. B, D, E, G köşeleri kırmızı yüzey köşegenleriyle birleşmiş; öndeki BEG yüzü pembe. Arkadaki köşegenler kesikli.](gorsel/tyt-matematik/26-04-kupte.svg "Dört yüzlünün her ayrıtı küpün bir yüz köşegenidir. Küpten kesilen dört köşe parçasının her biri küpün altıda biridir.")

**Kural:** Ayrıtı $a$ olan küpün dört köşesi yüz köşegenleriyle birleşince ayrıtı $a\sqrt{2}$ olan düzgün dört yüzlü oluşur ve

$$V = a^3 - 4 \cdot \frac{a^3}{6} = \frac{a^3}{3}$$

> **Tuzak:** Dört yüzlünün ayrıtını küpün ayrıtı ($a$) sanmak. Ayrıt yüz köşegenidir, $a\sqrt{2}$'dir. Ayrıtı $3$ alırsan $\dfrac{27\sqrt{2}}{12} = \dfrac{9\sqrt{2}}{4}$ bulursun; bu yanlıştır.

## ÖSYM tuzakları

> **Üç farklı "yükseklik".** Ayrıtı $a$ olan dört yüzlüde yan yüz yüksekliği $\frac{a\sqrt{3}}{2}$, tabandaki $|AH|$ uzaklığı $\frac{a\sqrt{3}}{3}$, cismin yüksekliği $\frac{a\sqrt{6}}{3}$'tür. Soru hangisini veriyor, hangisini istiyor; önce bunu yaz.

> **Yüzey alanında 4'e bölmek.** Bir yüzün alanı $\frac{a^2\sqrt{3}}{4}$, dört yüzün alanı $a^2\sqrt{3}$'tür. İkisini karıştırmak 4 katlık hata verir.

> **Hacimde iki bölme.** $V = \frac{a^3\sqrt{2}}{12}$. Formülü uzun yoldan kuruyorsan hem taban alanındaki $4$'ü hem piramitteki $3$'ü unutma.

> **Kat soruları.** Ayrıt 2 katına çıkarsa yüzey alanı 4, hacim 8 katına çıkar. Su dolu dört yüzlü kapta suyun yüksekliği yarıya inerse su, kabın $\frac{1}{8}$'i kadardır.

> **Yapıştırma.** İki eş dört yüzlü bir yüzlerinden yapıştırılırsa yüz sayısı $4 + 4 - 2 = 6$ olur; iki tepe arasındaki uzaklık yüksekliğin 2 katıdır, $2h$.

## Kendini dene

### Soru 1
Yüzey alanı $9\sqrt{3}$ cm² olan düzgün dört yüzlünün yüksekliği kaç cm'dir?

A) $\sqrt{3}$
B) $\sqrt{6}$
C) $\dfrac{3\sqrt{3}}{2}$
D) $3$
E) $2\sqrt{6}$

**Cevap:** B
**Çözüm:** $a^2\sqrt{3} = 9\sqrt{3} \Rightarrow a = 3$. $h = \dfrac{3\sqrt{6}}{3} = \sqrt{6}$. $\sqrt{3}$, $|AH| = \frac{a\sqrt{3}}{3}$ uzaklığıdır; $\frac{3\sqrt{3}}{2}$ yan yüz yüksekliğidir; $3$ ayrıtın kendisidir; $2\sqrt{6}$ ise $9\sqrt{3}$'ü bir yüzün alanı sanıp $a = 6$ bulmaktır.

### Soru 2
![Ayrıtı 6 olan TABC düzgün dört yüzlüsü. D noktası AB'nin orta noktası; AD ve DB 3'er birim. T, D ve C noktalarının oluşturduğu üçgen sarıya boyalı.](gorsel/tyt-matematik/26-04-kd2.svg "D, AB ayrıtının orta noktası. Sarı üçgen TDC.")

Şekildeki $TABC$ düzgün dört yüzlüsünün bir ayrıtı $6$ cm'dir. $D$, $[AB]$'nin orta noktası olduğuna göre $TDC$ üçgeninin alanı kaç cm²'dir?

A) $3\sqrt{6}$
B) $6\sqrt{2}$
C) $9\sqrt{2}$
D) $9\sqrt{3}$
E) $18\sqrt{2}$

**Cevap:** C
**Çözüm:** $[TD]$ ve $[CD]$, $TAB$ ve $CAB$ yüzlerinin yükseklikleridir: ikisi de $3\sqrt{3}$. $T$'den tabana inen dikmenin ayağı $H$, $[CD]$ kenarortayının üzerindedir; yani $[TH]$, $TDC$ üçgeninin $[DC]$ tabanına ait yüksekliğidir: $|TH| = 2\sqrt{6}$. Alan $= \dfrac{3\sqrt{3} \cdot 2\sqrt{6}}{2} = 3\sqrt{18} = 9\sqrt{2}$. $9\sqrt{3}$ bir yüzün alanıdır; $18\sqrt{2}$ dört yüzlünün hacmidir; $6\sqrt{2}$, tabanı $|CH| = 2\sqrt{3}$ almaktır; $3\sqrt{6}$ ise tabanı $|AD| = 3$ almaktır.

### Soru 3
Bir düzgün dört yüzlünün bütün ayrıtlarının uzunlukları toplamı $24$ cm'dir. Bu dört yüzlünün yüzey alanı kaç cm²'dir?

A) $2\sqrt{3}$
B) $4\sqrt{3}$
C) $8\sqrt{3}$
D) $16\sqrt{3}$
E) $36\sqrt{3}$

**Cevap:** D
**Çözüm:** $6a = 24 \Rightarrow a = 4$. $A = a^2\sqrt{3} = 16\sqrt{3}$. $4\sqrt{3}$, yalnız bir yüzün alanıdır (ya da 12 ayrıt sayıp $a = 2$ almaktır); $36\sqrt{3}$, 4 ayrıt sayıp $a = 6$ almaktır; $8\sqrt{3}$ iki yüzün, $2\sqrt{3}$ ise yarım yüzün alanıdır.

## Özet kartı

- Düzgün dört yüzlü: 4 eşkenar üçgen yüz, 6 eş ayrıt, 4 köşe; ayrıtlar toplamı $6a$.
- Yan yüz yüksekliği $\frac{a\sqrt{3}}{2}$, yüzey alanı $a^2\sqrt{3}$.
- Yükseklik $\frac{a\sqrt{6}}{3}$: $TAH$ dik üçgeninden, $|AH| = \frac{a\sqrt{3}}{3}$ (kenarortayın üçte ikisi).
- Hacim $\frac{A_T \cdot h}{3} = \frac{a^3\sqrt{2}}{12}$.
- Küpün dört köşesinden oluşan dört yüzlünün ayrıtı $a\sqrt{2}$, hacmi $\frac{a^3}{3}$.
- Ayrıt $k$ katı olursa alan $k^2$, hacim $k^3$ katı olur.

## Sonraki adım

Alıştırmaya geç (aşağıdaki düğme). Katı cisimler konusu burada bitiyor. Prizma, küp, piramit ve dört yüzlü sorularının hepsinde aynı yolu izle: aradığın uzunluğu hipotenüs ya da dik kenar yapan dik üçgeni bul, sonra alan ya da hacim formülüne koy.
