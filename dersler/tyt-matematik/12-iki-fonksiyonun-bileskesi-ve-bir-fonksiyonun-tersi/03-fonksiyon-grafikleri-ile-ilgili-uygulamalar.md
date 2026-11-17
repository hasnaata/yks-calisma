---
baslik: Fonksiyon Grafikleri ile İlgili Uygulamalar
ders: tyt-matematik
sure: 25 dk
kaynak: MEBİ Konu Özeti 4ea6fcd12f
guncelleme: 2026-11-17
---
# Fonksiyon Grafikleri ile İlgili Uygulamalar

**Bu dersin sonunda:** bir grafikten $f(a)$, $f^{-1}(b)$ ve bileşke değerlerini doğru eksenden okuyabilecek, iki noktası bilinen doğrunun kuralını yazabilecek ve günlük hayattaki doğrusal bir durumu fonksiyona çevirip çözebileceksin.

> **TYT'de yeri:** Grafiği verilen fonksiyonda "$f(2) + f^{-1}(3)$ kaçtır?", "$(f \circ f)(-1)$ kaçtır?", "$f(x) < 0$ koşulunu sağlayan kaç tam sayı var?" kalıpları sık gelir. Yeni nesil sorularda ise iki mumun boyu, iki deponun suyu ya da iki tarifenin ücreti doğru grafikleriyle verilir; eşit olduğu an ya da hangisinin daha avantajlı olduğu sorulur.

## Önce hatırla

<details><summary>Bir fonksiyonun tersinden: $f(x) = 3x - 6$ ise $f^{-1}(x)$ nedir?</summary>
$y = 3x - 6$ yaz ve $x$'i yalnız bırak: $3x = y + 6$, $x = \frac{y + 6}{3}$. Değişkenin adını $x$ yap: $f^{-1}(x) = \frac{x + 6}{3}$. Kontrol: $f(2) = 0$ ve $f^{-1}(0) = \frac{6}{3} = 2$. Fonksiyon $2$'yi $0$'a götürüyor, tersi $0$'ı $2$'ye geri getiriyor.
</details>

<details><summary>Bir fonksiyonun tersinden: Bire bir ve örten bir $f$ için $f(4) = 9$ ise $f^{-1}(9)$ ve $(f \circ f^{-1})(5)$ kaçtır?</summary>
$(4, 9) \in f$ ise $(9, 4) \in f^{-1}$; yani $f^{-1}(9) = 4$. Bir fonksiyon ile tersinin bileşkesi birim fonksiyondur: $(f \circ f^{-1})(5) = 5$. Bu dersin anahtarı ilk eşitliktir: $f(a) = b \iff f^{-1}(b) = a$.
</details>

## Grafikten $f(a)$ ve $f^{-1}(b)$ okumak

**Örnek.** Aşağıdaki grafik, $f\colon [-3, 4] \to [-2, 5]$ fonksiyonuna ait. $f(1)$ ve $f^{-1}(-2)$ değerlerini bulalım.

![Koordinat düzleminde kırık çizgi: (−3, −2) noktasından (0, 1)'e, oradan (1, 3)'e, oradan (4, 5)'e çıkıyor. Mavi kesikli oklar x = 1'den yukarı grafiğe, sonra sola y eksenindeki 3'e gidiyor. Kırmızı kesikli oklar y eksenindeki −2'den sola grafiğe, sonra yukarı x eksenindeki −3'e gidiyor.](gorsel/tyt-matematik/12-03-okuma.svg "Mavi yol f(1) için x ekseninden başlar. Kırmızı yol f⁻¹(−2) için y ekseninden başlar. Aynı grafik, iki yön.")

- $f(1)$: $1$ bir **girdi**, $x$ ekseninde. $x = 1$'den dikey çık, grafiğe değ, yatay git: $y = 3$. Yani $f(1) = 3$.
- $f^{-1}(-2)$: "$f$ hangi sayıyı $-2$'ye götürüyor?" sorusudur. $-2$ bir **görüntü**, $y$ ekseninde. $y = -2$'den yatay git, grafiğe değ, dikey in: $x = -3$. Yani $f^{-1}(-2) = -3$.

Kontrol: $f(-3) = -2$ grafikte görünüyor. Doğru.

**Kural.** $f(a)$ için $a$'yı **x ekseninde**, $f^{-1}(b)$ için $b$'yi **y ekseninde** ara:

$$f(a) = b \iff f^{-1}(b) = a$$

> **Tuzak:** $f^{-1}(-2)$ sorulunca $x = -2$'deki yüksekliği okumak. O değer $f(-2) = -1$'dir, $f^{-1}(-2)$ değil. Önce kendine sor: "Bu sayı girdi mi, görüntü mü?"

## Grafikten bileşke zinciri

**Örnek.** Aynı grafikte $(f \circ f)(-1)$ ve $(f^{-1} \circ f^{-1})(3)$ değerlerini bulalım. Bileşke sağdan sola çalışır.

$(f \circ f)(-1)$:

$$f(-1) = 0 \quad (\text{grafik } x = -1\text{'de } x \text{ eksenini kesiyor}), \qquad f(0) = 1$$

Sonuç $1$.

$(f^{-1} \circ f^{-1})(3)$: önce içteki $f^{-1}(3)$. $3$, $y$ ekseninde: grafikte $y = 3$ olan nokta $(1, 3)$, yani $f^{-1}(3) = 1$. Şimdi $f^{-1}(1)$: $y = 1$ olan nokta $(0, 1)$, yani $f^{-1}(1) = 0$. Sonuç $0$.

**Kural.** Her adımda bulduğun sonuç bir sonraki adımın girdisidir. Sonraki adım $f$ ise o sayıyı **x ekseninde**, $f^{-1}$ ise **y ekseninde** ara.

> **Tuzak:** İkinci adımda eksen değiştirmeyi unutmak. $(f^{-1} \circ f^{-1})(3)$ için $f^{-1}(3) = 1$ bulduktan sonra $x = 1$'e gidip $f(1) = 3$ okursan $(f \circ f^{-1})(3) = 3$ hesaplamış olursun.

## Grafikte işaret: $f(x) > 0$ ve $f^{-1}(x) < 0$

**Örnek 1.** Aynı $f$ için $f(x) > 0$ koşulunu sağlayan kaç $x$ tam sayısı vardır?

$f(x) > 0$, grafiğin **x ekseninin üstünde** olduğu yerdir. Grafik $x = -1$'de ekseni kesiyor ve sonra hep üstte kalıyor: $x \in (-1, 4]$. Tam sayılar $0, 1, 2, 3, 4$; toplam **5**. ($x = -1$'de $f(x) = 0$; sıfır pozitif değildir.)

**Örnek 2.** $f^{-1}(x) < 0$ koşulunu sağlayan $x$ değerleri hangileridir?

Burada $x$, $f^{-1}$'in **girdisi**, yani $f$'nin bir **görüntüsü**dür. $f^{-1}(x) = t$ dersen $f(t) = x$ olur. İstenen $t < 0$: grafiğin $t \in [-3, 0)$ olan parçasına bak ve bu parçanın **y değerlerini** oku.

![Aynı grafik. x ekseninde −3 ile 0 arası yeşil bantla boyanmış, grafiğin bu kısmı kırmızı: (−3, −2) dolu noktasından (0, 1) içi boş noktasına. y ekseninde −2 ile 1 arası sarı bant. Yanında x ∈ [−2, 1) yazıyor.](gorsel/tyt-matematik/12-03-ters-isaret.svg "f⁻¹ değerleri x ekseninde (yeşil), aranan x'ler y ekseninde (sarı). Kırmızı parça ikisini birbirine bağlar.")

$t = -3$ için $x = -2$, $t$ sıfıra yaklaşırken $x$ değeri $1$'e yaklaşır ama $t = 0$ dahil değil. Sonuç $x \in [-2, 1)$.

**Kural.** $f(x) > 0$: grafik x ekseninin üstünde; $f(x) < 0$: altında. Koşul $f^{-1}$ ile verilirse cevap **y ekseninden** okunur: $f^{-1}(x) < 0$ ise $x$, grafiğin sol yarısının ($x < 0$ olan kısmın) görüntüleridir.

> **Tuzak:** $f^{-1}(x) < 0$ sorusuna $f(x) < 0$ gibi davranıp $[-3, -1)$ yazmak. $f^{-1}$ ile gelen her koşulda aranan sayı $y$ eksenindedir.

## Grafikten doğrunun kuralını bulmak

**Örnek.** Doğrusal $f$ fonksiyonunun grafiği $A(-2, 1)$ ve $B(1, 7)$ noktalarından geçiyor. $f(x)$ kuralını, $f(3)$'ü ve $f^{-1}(-3)$'ü bulalım.

![Koordinat düzleminde yükselen bir doğru. Üzerinde A(−2, 1) ve B(1, 7) noktaları. A'dan sağa 3 birimlik yatay kesikli çizgi (Δx = 3), oradan B'ye 6 birimlik dikey kesikli çizgi (Δy = 6). Doğru y eksenini 5'te kesiyor, n = 5 yazıyor.](gorsel/tyt-matematik/12-03-kural.svg "Sağa 3 giderken yukarı 6 çıkıyor: eğim 6/3 = 2. Doğrunun y eksenini kestiği yer n'dir.")

**Yol 1 (eğim).** Doğru $x$'te $3$ birim ilerlerken $y$'de $6$ birim artıyor:

$$m = \frac{y_2 - y_1}{x_2 - x_1} = \frac{7 - 1}{1 - (-2)} = \frac{6}{3} = 2$$

$f(x) = 2x + n$ ve $f(1) = 7$: $2 + n = 7$, $n = 5$. Yani $f(x) = 2x + 5$.

**Yol 2 (denklem sistemi).** $f(x) = mx + n$ kuralına iki noktayı yaz:

$$-2m + n = 1, \qquad m + n = 7$$

Alttan üsttekini çıkar: $3m = 6$, $m = 2$; $n = 5$. Aynı sonuç.

Şimdi değerler: $f(3) = 2 \cdot 3 + 5 = 11$. $f^{-1}(-3)$ için $f(x) = -3$ çöz: $2x + 5 = -3$, $x = -4$. Kontrol: $f(-4) = -8 + 5 = -3$.

**Kural.** Doğrusal fonksiyon $f(x) = mx + n$ biçimindedir. $m$ **eğim** (değişim hızı): $x$ bir birim artınca $f(x)$'in ne kadar değiştiğini söyler. $n = f(0)$, doğrunun **y eksenini kestiği** değerdir. İki nokta kuralı tam olarak belirler.

> **Tuzak:** Eğimi ters yazmak: $\frac{x_2 - x_1}{y_2 - y_1} = \frac{3}{6}$ değil, $\frac{6}{3}$. Pay hep $y$ farkıdır. Bir de işarete dikkat: soldan sağa inen doğrunun eğimi negatiftir.

## Doğrusal fonksiyon hikayeleri

Bağımsız değişken (girdi) her seferinde aynı miktar artarken bağımlı değişken (çıktı) de hep aynı miktar artıyor ya da azalıyorsa durum **doğrusaldır**. Böyle bir hikayede iki şeyi bul:

$$f(x) = \underbrace{\text{değişim hızı}}_{m} \cdot x + \underbrace{\text{başlangıç değeri}}_{n}$$

| Bağımsız değişken ($x$) | Bağımlı değişken $f(x)$ | Başlangıç ($n$) | Hız ($m$) |
|---|---|---|---|
| Yanma süresi | Mumun boyu | İlk boy | Saatte kısalma (negatif) |
| Gidilen yol | Depodaki yakıt | Dolu depo | Km başına harcama (negatif) |
| Satın alınan ürün sayısı | Ödenecek tutar | Sabit ücret | Birim fiyat |
| Deniz seviyesinden yükseklik | Hava sıcaklığı | Deniz seviyesindeki sıcaklık | Her metrede düşüş (negatif) |

**Örnek 1 (iki veriden kural).** Bir dağda $500$ m yükseklikte hava $18\,°\text{C}$, $1500$ m yükseklikte $12\,°\text{C}$ ölçülüyor. Sıcaklık yükseklikle doğrusal değişiyorsa hangi yükseklikte $0\,°\text{C}$ olur?

Hız: $\frac{12 - 18}{1500 - 500} = \frac{-6}{1000}$, yani her $1000$ m'de $6\,°\text{C}$ düşüş. Başlangıç (deniz seviyesi): $500$ m inersen $3\,°\text{C}$ artar, $18 + 3 = 21\,°\text{C}$. Kural $T(h) = 21 - \frac{6h}{1000}$.

$0 = 21 - \frac{6h}{1000}$ ise $h = 3500$ m.

**Örnek 2 (iki doğru kesişiyor).** A mumu $30$ cm boyunda ve $10$ saatte, B mumu $20$ cm boyunda ve $20$ saatte tamamen yanıyor. İkisi aynı anda yakılırsa kaçıncı saatte boyları eşit olur?

![Koordinat düzleminde iki azalan doğru: A mavi, (0, 30)'dan (10, 0)'a; B yeşil, (0, 20)'den (20, 0)'a. İki doğru kırmızı (5, 15) noktasında kesişiyor.](gorsel/tyt-matematik/12-03-mum.svg "Boylar, iki doğrunun kesiştiği anda eşittir. Kesişimden önce A uzun, sonra B uzundur.")

A saatte $30 \div 10 = 3$ cm, B saatte $20 \div 20 = 1$ cm kısalır:

$$A(t) = 30 - 3t, \qquad B(t) = 20 - t$$

$30 - 3t = 20 - t \Rightarrow 10 = 2t \Rightarrow t = 5$ saat. O anda ikisinin boyu $15$ cm.

**Kural.** Hikayede önce $x$'in ve $f(x)$'in ne olduğunu yaz, sonra başlangıç değerini ve hızı bul. İki durum karşılaştırılıyorsa iki kuralı eşitle: eşitlik anı grafiklerin **kesişim noktasıdır**.

> **Tuzak:** Başlangıç değerini, verilen ilk ölçümle karıştırmak. Örnek 1'de $18\,°\text{C}$ başlangıç değil, $500$ m'deki değerdir. Başlangıç, $x = 0$ anındaki değerdir.

## ÖSYM tuzakları

> **Yanlış eksen:** $f(a)$ için $a$ x ekseninde, $f^{-1}(b)$ için $b$ y ekseninde aranır. Seçeneklerde iki eksenin karıştırılmasıyla bulunan sayı hep bulunur.

> **Bileşkede eksen değiştirmemek:** $(f^{-1} \circ f)$ ya da $(f^{-1} \circ f^{-1})$ zincirinde her adımda "şimdi hangi fonksiyon?" diye sor; $f^{-1}$ adımında sayıyı y ekseninde ara.

> **Sıfırı pozitif saymak:** $f(x) > 0$ sorusunda grafiğin x eksenini kestiği noktalar dahil değildir; $f(x) \ge 0$ sorulursa dahildir.

> **Eğimi ters yazmak:** $m = \frac{\Delta y}{\Delta x}$. $\frac{\Delta x}{\Delta y}$ yazan, eğimin tersini bulur.

> **"Kaçıncı saatte" ile "kaç cm" karışması:** Kesişim sorusunda iki sayı bulunur: kesişimin $x$ değeri (zaman) ve $y$ değeri (boy). Soru hangisini istiyor, kökü bir kez daha oku.

## Kendini dene

### Soru 1
Doğrusal $f$ fonksiyonunun grafiği $(0, -2)$ ve $(3, 4)$ noktalarından geçmektedir. Buna göre $f(5)$ kaçtır?

A) $\frac{1}{2}$
B) $3$
C) $6$
D) $8$
E) $10$

**Cevap:** D
**Çözüm:** Eğim $m = \frac{4 - (-2)}{3 - 0} = \frac{6}{3} = 2$. Grafik y eksenini $-2$'de kestiği için $n = -2$: $f(x) = 2x - 2$. $f(5) = 10 - 2 = 8$. $n$'yi unutan $10$, eğimi ters alıp ($\frac{1}{2}$) $f(x) = \frac{x}{2} - 2$ yazan $\frac{1}{2}$ bulur. $6$, $f(4)$ değeridir.

### Soru 2
Doğrusal $f$ fonksiyonunun grafiği x eksenini $-4$'te, y eksenini $2$'de kesmektedir. Buna göre $f^{-1}(3)$ kaçtır?

A) $-2$
B) $1$
C) $2$
D) $\frac{7}{2}$
E) $4$

**Cevap:** C
**Çözüm:** Noktalar $(-4, 0)$ ve $(0, 2)$. $m = \frac{2 - 0}{0 - (-4)} = \frac{1}{2}$, $n = 2$: $f(x) = \frac{x}{2} + 2$. $f^{-1}(3)$ için $f(x) = 3$ çöz: $\frac{x}{2} = 1$, $x = 2$. Kontrol: $f(2) = 1 + 2 = 3$. $\frac{7}{2}$, yanlış yönde hesaplanan $f(3)$ değeridir.

### Soru 3
Bir depoda $120$ litre su vardır ve depoya dakikada $8$ litre su eklenmektedir. Aynı anda ikinci bir depodaki $300$ litre su dakikada $12$ litre boşaltılmaktadır. Kaç dakika sonra iki depodaki su miktarı eşit olur?

A) $6$
B) $9$
C) $15$
D) $22{,}5$
E) $45$

**Cevap:** B
**Çözüm:** $t$ dakika sonra birinci depoda $120 + 8t$, ikincide $300 - 12t$ litre su olur. Eşitle: $120 + 8t = 300 - 12t$, $20t = 180$, $t = 9$. Kontrol: ikisi de $192$ litre. Hızları çıkarıp $180 \div (12 - 8) = 45$ bulan, depolardan biri dolarken öbürünün boşaldığını unutmuştur; $180 \div 12 = 15$ yalnızca bir depoyu hesaba katar.

## Özet kartı

- $f(a)$: $a$ x ekseninde, cevap y ekseninde. $f^{-1}(b)$: $b$ y ekseninde, cevap x ekseninde.
- Bileşke zincirinde her adımın sonucu bir sonraki adımın girdisidir; $f^{-1}$ adımında y eksenine git.
- $f(x) > 0$: grafik x ekseninin üstünde. $f^{-1}$ ile verilen koşulun cevabı y ekseninden okunur.
- Doğru: $f(x) = mx + n$, $m = \frac{y_2 - y_1}{x_2 - x_1}$, $n = f(0)$.
- Hikaye: $f(x) = \text{hız} \cdot x + \text{başlangıç}$; başlangıç $x = 0$ anındaki değerdir.
- İki durum eşitse iki kuralı eşitle; bu, grafiklerin kesişim noktasıdır.

## Sonraki adım

Alıştırmaya geç (aşağıdaki düğme). Bu ders "İki Fonksiyonun Bileşkesi ve Bir Fonksiyonun Tersi" konusunu bitiriyor. Sonraki ders **Polinom Kavramı**; doğrusal fonksiyon $mx + n$, birinci dereceden bir polinomdur.
