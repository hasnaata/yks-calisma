---
baslik: Fonksiyon Grafikleri
ders: tyt-matematik
sure: 22 dk
kaynak: MEBİ Konu Özeti b4b0f53717
guncelleme: 2026-11-18
---
# Fonksiyon Grafikleri

<div class="giris" dir="rtl" lang="ar">

**الدرس ده عن إيه؟** عن الرسم البياني للدالة (fonksiyon grafiği): إزاي تقرا منه المعلومة وإزاي ترسمه بإيدك.

- هتعرف تطلّع من الرسم قيمة الدالة، والمجال (tanım kümesi)، والمدى (görüntü kümesi)، وفين الدالة موجبة أو سالبة.
- هترسم الدالة الخطية (doğrusal fonksiyon) والدالة المتعددة القواعد (parçalı fonksiyon)، وتفرّق بين النقطة المليانة والنقطة الفاضية.
- هتتعلم اختبار الخط الرأسي (düşey doğru testi) واختبار الخط الأفقي (yatay doğru testi)، وتعدّ بيهم الحلول بسرعة.

**ليه مهم؟** أغلب أسئلة الدوال في TYT بتيجي على شكل رسم، وكمان أسئلة الحياة اليومية زي خزان مية أو سرعة أو أجرة، فلو عرفت تقرا الرسم صح هتكسب نقط كتير.

حوالي ٢٢ دقيقة، والرسومات هتسهّل عليك كل حاجة. يلا نبدأ!

</div>

**Bu dersin sonunda:** bir fonksiyonun grafiğinden değer, tanım kümesi, görüntü kümesi ve işaret okuyabilecek, doğrusal ve parçalı fonksiyonların grafiğini çizebilecek, düşey ve yatay doğru testlerini uygulayabileceksin.

> **TYT'de yeri:** Fonksiyon sorularının büyük kısmı grafikle gelir: "$f(-2) + f(3)$ kaçtır?", "görüntü kümesinde kaç tam sayı var?", "$f(x) = k$ denkleminin kaç kökü var?", "$f(x) < 0$ olan tam sayılar". Günlük hayat sorularında (depo, hız, ücret) grafik okumak doğrudan bu derstir.

## Önce hatırla

<details><summary>Fonksiyonlarda dört işlemden: $f(x) = x^2 - 1$ ve $g(x) = x + 3$ ise $(f + g)(2) + (f \cdot g)(1)$ kaçtır?</summary>
$(f + g)(2) = f(2) + g(2) = 3 + 5 = 8$. $(f \cdot g)(1) = f(1) \cdot g(1) = 0 \cdot 4 = 0$. Toplam <b>8</b>.
</details>

<details><summary>Fonksiyonlarda dört işlemden: $f\colon [-2, 5] \to \mathbb{R}$ ve $g\colon [0, 7] \to \mathbb{R}$, $g(x) = x - 3$ ise $\frac{f}{g}$ fonksiyonunun en geniş tanım kümesi nedir?</summary>
Önce ortak kısım: $[-2, 5] \cap [0, 7] = [0, 5]$. Bölme olduğu için $g(x) = 0$ yapan $x = 3$ çıkarılır: <b>$[0, 3) \cup (3, 5]$</b>.
</details>

## Grafik nedir?

**Örnek.** $f(x) = 2x - 1$ için birkaç değer hesapla ve $(x, f(x))$ ikililerini yaz:

| $x$ | $-1$ | $0$ | $1$ | $3$ |
|---|---|---|---|---|
| $f(x)$ | $-3$ | $-1$ | $1$ | $5$ |
| Nokta | $(-1, -3)$ | $(0, -1)$ | $(1, 1)$ | $(3, 5)$ |

Bu noktaları koordinat düzleminde işaretleyip tanım kümesindeki **bütün** $x$ değerleri için aynı şeyi yaptığını düşün. Oluşan noktalar kümesi $f$'nin **grafiğidir**.

**Kural.** $f$'nin grafiği $\{(x, f(x)) \mid x \in A\}$ kümesidir. Tanım kümesinin elemanları **yatay** eksende ($x$ ekseni), görüntüler **düşey** eksende ($y$ ekseni) gösterilir.

$$(a, b) \text{ grafiğin üzerinde} \iff f(a) = b$$

> **Tuzak:** $(3, 5)$ noktası grafikte ise $f(3) = 5$'tir, $f(5) = 3$ değil. Birinci bileşen girdi, ikinci bileşen çıktıdır.

## Grafikten okumak: değer, tanım kümesi, görüntü kümesi

**Örnek.** Aşağıda $g$ fonksiyonunun grafiği var.

![Koordinat düzleminde kırık çizgi grafiği: (−3, 2) noktasından (−1, −2)'ye iner, (2, 4)'e çıkar, (5, 1)'e iner. Uçlar dolu nokta. x ekseninde −3 ile 5 arası yeşil bantla, y ekseninde −2 ile 4 arası sarı bantla boyanmış.](gorsel/tyt-matematik/11-08-okuma.svg "Grafiği x eksenine izdüşürürsen tanım kümesini (yeşil), y eksenine izdüşürürsen görüntü kümesini (sarı) bulursun.")

- **Değer okuma:** $g(2)$ için $x = 2$'den yukarı çık, grafiğe değdiğin yerin yüksekliği $4$: $g(2) = 4$. Aynı yolla $g(-1) = -2$, $g(5) = 1$.
- **Tanım kümesi:** Grafik en solda $x = -3$'te, en sağda $x = 5$'te bitiyor ve arada kesinti yok: $[-3, 5]$.
- **Görüntü kümesi:** Grafiğin en alçak noktası $y = -2$, en yüksek noktası $y = 4$; arada her yükseklik kullanılıyor: $[-2, 4]$.

**Kural.** Tanım kümesi, grafiğin noktalarının **birinci bileşenleri** (apsisleri); görüntü kümesi **ikinci bileşenleri** (ordinatları) kümesidir. Grafiği $x$ eksenine "gölge" gibi düşürürsen tanım kümesi, $y$ eksenine düşürürsen görüntü kümesi çıkar.

> **Tuzak:** Görüntü kümesi uç noktaların değerleri değildir. $g(-3) = 2$ ve $g(5) = 1$ ama görüntü kümesi $[1, 2]$ değil, $[-2, 4]$'tür. Grafiğin **en alt** ve **en üst** noktasına bak.

## Doğrusal fonksiyonun grafiğini çizmek

**Örnek.** $f(x) = 2x - 4$ grafiğini çiz.

Bir doğru iki noktayla belirlenir. En pratik iki nokta, eksenleri kestiği noktalardır:

1. $y$ eksenini kestiği nokta: $x = 0$ koy. $f(0) = -4$, nokta $(0, -4)$.
2. $x$ eksenini kestiği nokta: $f(x) = 0$ koy. $2x - 4 = 0$, $x = 2$, nokta $(2, 0)$.
3. İki noktayı işaretle ve birleştirip iki yana uzat.

Kontrol için üçüncü bir nokta: $f(3) = 2$, yani $(3, 2)$ de bu doğrunun üzerindedir.

**Kural.** $f(x) = mx + n$ grafiği bir doğrudur. $y$ eksenini $(0, n)$ noktasında, $x$ eksenini $f(x) = 0$ denkleminin kökünde keser. Doğru eksenlerle bir dik üçgen oluşturuyorsa alanı $\frac{|\text{x kesişimi}| \cdot |\text{y kesişimi}|}{2}$ olur. Burada $\frac{2 \cdot 4}{2} = 4$ birim kare.

> **Tuzak:** "$x$ eksenini kestiği nokta" için $x = 0$ değil, $y = 0$ konur. Eksen adı ile sıfırlanan değişken terstir.

## Parçalı fonksiyonun grafiğini çizmek

**Örnek.** $f\colon [-3, 4] \to \mathbb{R}$,

$$f(x) = \begin{cases} x + 3, & -3 \le x < 1 \\ 2 - x, & 1 \le x \le 4 \end{cases}$$

1. **Kritik noktaları bul:** kuralın değiştiği $x = 1$ ve tanım kümesinin uçları $x = -3$, $x = 4$.
2. **Her parçayı kendi aralığında çiz:**
   - Üst satır: $f(-3) = 0$ (dahil, dolu nokta). $x = 1$'e gelince $1 + 3 = 4$ olurdu ama $x = 1$ bu satıra ait değil: $(1, 4)$ **içi boş** nokta.
   - Alt satır: $f(1) = 1$ (dahil, dolu nokta), $f(4) = -2$ (dahil, dolu nokta).

![Parçalı fonksiyon grafiği. Mavi doğru parçası (−3, 0) dolu noktasından (1, 4) içi boş noktasına çıkıyor. Yeşil doğru parçası (1, 1) dolu noktasından (4, −2) dolu noktasına iniyor. x = 1'de noktalı düşey çizgi var.](gorsel/tyt-matematik/11-08-parcali.svg "x = 1'de iki nokta var: dolu olan (1, 1) fonksiyonun değeridir, boş olan (1, 4) grafiğe ait değildir.")

3. **Görüntü kümesini oku:** Mavi parça $[0, 4)$ yüksekliklerini, yeşil parça $[-2, 1]$ yüksekliklerini kullanıyor. Birleşim $[-2, 4)$. $4$ görüntü kümesinde **yok**, çünkü $(1, 4)$ boş nokta ve başka hiçbir $x$ için $f(x) = 4$ değil.

**Kural.** Parçalı fonksiyonda önce kritik noktaları işaretle, sonra her aralıkta o satırın grafiğini çiz. Aralığa dahil olan uç **dolu**, dahil olmayan uç **içi boş** yuvarlakla gösterilir.

## Grafikten işaret okumak

**Örnek.** Aynı $g$ fonksiyonunda $g(x) > 0$ ve $g(x) < 0$ olan $x$ değerleri hangileri?

![Aynı kırık çizgi grafiği. Grafik x eksenini −2 ve 0'da kesiyor. x ekseninin üstündeki kısımlar mavi, −2 ile 0 arasında x ekseninin altına inen kısım kırmızı boyanmış.](gorsel/tyt-matematik/11-08-isaret.svg "g(x) > 0 sorusu bir yükseklik sorusudur: grafiğin x ekseninin üstünde kaldığı x değerlerine bak.")

Önce grafiğin $x$ eksenini kestiği noktaları bul: $x = -2$ ve $x = 0$. Bunlar $g(x) = 0$ denkleminin kökleridir.

- Grafik $x$ ekseninin **üstünde**: $[-3, -2)$ ve $(0, 5]$. Burada $g(x) > 0$.
- Grafik $x$ ekseninin **altında**: $(-2, 0)$. Burada $g(x) < 0$.

$g(x) < 0$ eşitsizliğini sağlayan tek tam sayı $-1$'dir. $g(x) \le 0$ denseydi kökler de eklenirdi: $-2, -1, 0$.

**Kural.** Grafiğin $x$ ekseninin üstünde kaldığı aralık $f(x) > 0$, altında kaldığı aralık $f(x) < 0$ eşitsizliğinin çözüm kümesidir. $x$ eksenini kestiği noktalar $f(x) = 0$ denkleminin kökleridir.

> **Tuzak:** "$f(x) > 0$" ile "$x > 0$" aynı şey değildir. Birincisi grafiğin **yüksekliğini**, ikincisi noktanın $y$ ekseninin **sağında** olmasını sorar.

## Düşey ve yatay doğru testi

**Örnek.** Aşağıdaki iki grafikten hangisi bir fonksiyon grafiğidir?

![Solda bir çember; kesikli kırmızı düşey bir doğru çemberi iki noktada kesiyor. Sağda yukarı açılan bir eğri, iki kesikli yeşil düşey doğru eğriyi birer noktada kesiyor.](gorsel/tyt-matematik/11-08-dusey-test.svg "Fonksiyonda her x'in tek bir görüntüsü olur. Bir düşey doğru grafiği iki noktada keserse o x için iki görüntü var demektir.")

Çemberde $x = 1$ doğrusu iki noktadan geçer: $x = 1$'in iki görüntüsü var, **fonksiyon değil**. Sağdaki eğride hangi düşey doğruyu çizersen çiz tek noktada keser: **fonksiyon**.

| Test | Nasıl yapılır? | Sonuç |
|---|---|---|
| Düşey doğru testi | Tanım kümesindeki her $x$'ten $y$ eksenine paralel doğru çiz | Her doğru grafiği **tam 1** noktada kesiyorsa bağıntı fonksiyondur |
| Yatay doğru testi (bire bir) | Değer kümesindeki her $y$'den $x$ eksenine paralel doğru çiz | Hiçbiri **1'den fazla** noktada kesmiyorsa fonksiyon bire birdir |
| Yatay doğru testi (örten) | Aynı yatay doğrular | Her biri **en az 1** noktada kesiyorsa fonksiyon örtendir |

**Kural.** Yatay doğru $y = k$ grafiği kaç noktada kesiyorsa $f(x) = k$ denkleminin o kadar kökü vardır. Bu, "kaç kök var?" sorularının en hızlı yoludur.

> **Tuzak:** Aynı $x$'te biri **dolu** biri **boş** iki nokta varsa düşey doğru grafiği yalnızca dolu noktada keser; bağıntı yine fonksiyondur. İkisi de doluysa fonksiyon değildir.

Son bir bağlantı: önceki derste gördüğün gibi grafiği $y$ eksenine göre simetrik olan fonksiyon **çift**, orijine göre simetrik olan fonksiyon **tek** fonksiyondur.

## ÖSYM tuzakları

> **Bileşenleri karıştırmak:** $(4, -1)$ grafikte ise $f(4) = -1$'dir. Tanım kümesini $y$ ekseninden, görüntü kümesini $x$ ekseninden okumak en sık hatadır.

> **Boş noktayı görüntüye katmak:** Parçalı grafikte içi boş noktanın yüksekliği, başka bir $x$ o değeri vermiyorsa görüntü kümesinde yoktur. Görüntüdeki tam sayıları sayarken bu uç bir eksik çıkar.

> **Görüntü kümesini uçlardan okumak:** Grafiğin uç noktaları değil, en alt ve en üst noktaları görüntü kümesinin sınırlarını verir.

> **Eşitsizlikte kökleri unutmak:** $f(x) \le 0$ sorusunda grafiğin $x$ eksenini kestiği noktalar da çözümdür; $f(x) < 0$ sorusunda değildir.

> **Kök saymada köşeyi iki kez saymak:** $y = k$ doğrusu grafiği tam bir köşede kesiyorsa, iki parçanın ortak noktası olduğu için o **tek** köktür.

## Kendini dene

### Soru 1
$f(x) = -2x + 6$ fonksiyonunun grafiği $x$ eksenini $(a, 0)$, $y$ eksenini $(0, b)$ noktasında kesiyor. $a + b$ toplamı kaçtır?

A) 3
B) 6
C) 9
D) 12
E) 15

**Cevap:** C
**Çözüm:** $y$ ekseni için $x = 0$: $b = f(0) = 6$. $x$ ekseni için $f(x) = 0$: $-2x + 6 = 0$, $a = 3$. $a + b = 9$. $a$'yı $-3$ bulan (işaret hatası) $3$'e ulaşır.

### Soru 2
$f\colon [-2, 4] \to \mathbb{R}$,

$$f(x) = \begin{cases} x + 1, & -2 \le x < 1 \\ 5 - x, & 1 \le x \le 4 \end{cases}$$

fonksiyonunun görüntü kümesi aşağıdakilerden hangisidir?

A) $[-2, 4]$
B) $[-1, 2)$
C) $[-1, 4)$
D) $[-1, 4]$
E) $[1, 4]$

**Cevap:** D
**Çözüm:** Üst satır: $f(-2) = -1$ dolu, $x = 1$'de $2$ boş; yükseklikler $[-1, 2)$. Alt satır: $f(1) = 4$ dolu, $f(4) = 1$ dolu; yükseklikler $[1, 4]$. Birleşim $[-1, 4]$. $2$ boş nokta olsa da alt satır $x = 3$'te $2$ değerini verdiği için görüntüdedir. $[-2, 4]$ tanım kümesidir.

### Soru 3
$f\colon [-3, 6] \to \mathbb{R}$, $f(x) = 4 - x$ olduğuna göre $f(x) > 0$ eşitsizliğini sağlayan kaç tam sayı vardır?

A) 3
B) 7
C) 8
D) 9
E) 10

**Cevap:** B
**Çözüm:** Grafik $x$ eksenini $x = 4$'te keser ve azalan bir doğrudur; $x < 4$ için eksenin üstündedir. Tanım kümesiyle birlikte: $-3 \le x < 4$. Tam sayılar $-3, -2, \dots, 3$; toplam 7. $4$'ü de sayan 8, tanım kümesindeki bütün tam sayıları sayan 10 bulur.

## Özet kartı

- $(a, b)$ grafikte $\iff f(a) = b$. Tanım kümesi $x$ ekseninde, görüntü kümesi $y$ ekseninde okunur.
- Görüntü kümesi: grafiğin en alt ve en üst noktası; boş noktalara dikkat.
- Doğru çizmek için iki nokta yeter: $(0, f(0))$ ve $f(x) = 0$ kökü.
- Parçalı grafikte dahil olan uç dolu, dahil olmayan uç içi boş yuvarlak.
- $x$ ekseninin üstü $f(x) > 0$, altı $f(x) < 0$, kesişim noktaları $f(x) = 0$.
- Düşey doğru testi: fonksiyon mu? Yatay doğru $y = k$: $f(x) = k$ kaç kök, bire bir mi, örten mi?

## Sonraki adım

Alıştırmaya geç (aşağıdaki düğme). Sonraki ders **İki Fonksiyonun Bileşkesi**; $f(g(x))$ gibi değerleri çoğu zaman bu dersteki gibi grafikten okuyacaksın.
