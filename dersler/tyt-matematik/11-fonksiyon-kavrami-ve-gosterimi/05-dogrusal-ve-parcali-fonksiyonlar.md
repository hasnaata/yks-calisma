---
baslik: Doğrusal ve Parçalı Fonksiyonlar
ders: tyt-matematik
sure: 20 dk
kaynak: MEBİ Konu Özeti 260cbab73e
guncelleme: 2026-11-18
---
# Doğrusal ve Parçalı Fonksiyonlar

<div class="giris" dir="rtl" lang="ar">

**الدرس ده عن إيه؟** عن نوعين من الدوال بيتكرروا كتير: الدالة الخطية (doğrusal fonksiyon) اللي رسمها خط مستقيم، والدالة المعرّفة على فترات (parçalı fonksiyon) اللي ليها قاعدة مختلفة في كل فترة.

- هتعرف تطلّع قاعدة الدالة الخطية من قيمتين بس أو من الرسم، وتفهم معنى الميل (eğim) ونقطة التقاطع مع محور الصادات.
- هتتعلم تختار السطر الصح في الدالة المعرّفة على فترات، خصوصًا عند النقطة الحرجة (kritik nokta)، وتحل معادلة وتتأكد إن الحل جوه فترته.
- هتكتب مسائل التعريفة المتدرّجة (kademeli ücret) زي فاتورة المية أو الجراج على شكل دالة.

**ليه مهم؟** في TYT الدالة الخطية غالبًا بتيجي جوه مسألة من الحياة اليومية زي "اشتراك ثابت وفوقه سعر لكل وحدة"، والدالة المعرّفة على فترات بتيجي في حساب قيم وتعريفات متدرّجة.

الدرس ٢٠ دقيقة بس وفيه أمثلة محلولة خطوة بخطوة، يلا بينا.

</div>

**Bu dersin sonunda:** iki değerden ya da grafikten doğrusal fonksiyonun kuralını bulabilecek, parçalı fonksiyonda doğru parçayı seçerek değer ve denklem çözebilecek, kademeli ücret problemlerini fonksiyonla kurabileceksin.

> **TYT'de yeri:** Doğrusal fonksiyon çoğu zaman günlük hayat sorusunun içinde gelir: "sabit ücret + birim başına ücret", "düzenli azalan miktar". Parçalı fonksiyonda "$f(2) + f(5)$ kaçtır?", "$f(x) = 3$ denkleminin çözümleri" ve kademeli tarife (su, elektrik, otopark) soruları sık çıkar.

## Önce hatırla

<details><summary>Birim ve sabit fonksiyondan: $f\colon \mathbb{R} \to \mathbb{R}$, $f(x) = (a - 2)x + b + 1$ sabit fonksiyon ve $f(5) = 4$ ise $a + b$ kaçtır?</summary>
Sabit fonksiyonun kuralında $x$ bulunmaz: $a - 2 = 0$, $a = 2$. O zaman her $x$ için $f(x) = b + 1 = 4$, $b = 3$. $a + b = 5$.
</details>

<details><summary>Birim ve sabit fonksiyondan: $f(x) = \frac{2x + 3}{4x + k}$ sabit fonksiyon ise $k$ kaçtır?</summary>
Katsayılar orantılı olmalı: $\frac{2}{4} = \frac{3}{k}$, $k = 6$. Kontrol: $\frac{2x + 3}{4x + 6} = \frac{2x + 3}{2(2x + 3)} = \frac{1}{2}$, gerçekten sabit.
</details>

## Doğrusal fonksiyon

**Örnek.** Bir spor salonunda kayıt ücreti 300 TL, her ders 50 TL. $x$ derse giden kişinin ödediği tutar $f(x) = 50x + 300$ olur. 8 ders için $f(8) = 50 \cdot 8 + 300 = 700$ TL.

İki sayının anlamına bak:

- $50$: her fazladan derste tutar **ne kadar artar**. Bu, $x$'in katsayısıdır.
- $300$: hiç derse gitmeyen kişinin ödediği, yani $f(0)$. Bu, sabit terimdir.

**Kural.** $m, n \in \mathbb{R}$ olmak üzere $f(x) = mx + n$ biçimindeki fonksiyona **doğrusal fonksiyon** denir. Grafiği bir doğrudur.

| Sayı | Anlamı | Grafikte |
|---|---|---|
| $m$ ($x$'in katsayısı) | $x$ 1 artınca $f(x)$'in değişimi | Doğrunun **eğimi** |
| $n$ (sabit terim) | $f(0) = n$ | Doğru $y$ eksenini $(0, n)$'de keser |

Önceki dersle bağ: $m = 0$ ise $f(x) = n$ **sabit fonksiyon** olur, grafiği yatay doğrudur. $m = 1$, $n = 0$ ise $f(x) = x$ **birim fonksiyon** olur.

Kural $x^2$ gibi terimler içeriyorsa doğrusal olması için o terimlerin katsayısı $0$ olmalı. Örneğin $f(x) = (a - 3)x^2 + 2x + a$ doğrusal ise $a = 3$ ve $f(x) = 2x + 3$ olur.

## İki değerden kuralı bulmak

**Örnek.** $f$ doğrusal, $f(2) = 7$ ve $f(5) = 16$ ise $f(x)$ nedir?

1. $x$, $2$'den $5$'e $3$ arttı; $f(x)$, $7$'den $16$'ya $9$ arttı. $x$ 1 artınca $f(x)$ $\frac{9}{3} = 3$ artar: $m = 3$.
2. $f(2) = 3 \cdot 2 + n = 7$, $n = 1$.
3. $f(x) = 3x + 1$.

| $x$ | 2 | 5 | 8 | 11 |
|---|---|---|---|---|
| $f(x)$ | 7 | 16 | 25 | 34 |

Tabloya bak: $x$ eşit adımlarla artınca $f(x)$ de **eşit adımlarla** artar. Kuralı yazmadan da $f(11) = 34$ bulunabilir.

**Kural.** $f$ doğrusal ise $m = \dfrac{f(b) - f(a)}{b - a}$. Sonra bilinen bir değeri yerine yazarak $n$ bulunur.

> **Tuzak:** Doğrusal fonksiyon, doğru orantı değildir. $f(2) = 7$ diye $f(4) = 14$ olmaz; $f(4) = 3 \cdot 4 + 1 = 13$. Doğru orantı yalnızca $n = 0$ iken geçerlidir.

## Grafikten kuralı okumak

**Örnek.** Grafiği aşağıdaki doğru olan $f$ için $f(6)$ kaçtır?

![Koordinat düzleminde yükselen bir doğru. Doğru x eksenini −3'te, y eksenini 2'de kesiyor. (0, 2) noktasından 3 birim sağa ve 2 birim yukarı giden kesikli yeşil adım çizilmiş, (3, 4) noktasına varıyor.](gorsel/tyt-matematik/11-05-dogru-grafik.svg "Önce y eksenini kestiği noktayı oku (n), sonra bir adımda ne kadar sağa, ne kadar yukarı gidildiğine bak (m).")

1. Doğru $y$ eksenini $2$'de kesiyor: $n = 2$.
2. $(0, 2)$ noktasından 3 birim sağa gidince doğru 2 birim yükseliyor: $m = \frac{2}{3}$.
3. $f(x) = \frac{2}{3}x + 2$, $f(6) = 4 + 2 = 6$.

Kontrol: $f(-3) = -2 + 2 = 0$; doğru gerçekten $x$ eksenini $-3$'te kesiyor.

**Kural.** Doğru $(0, n)$ ve $(p, 0)$ noktalarından geçiyorsa $n$ doğrudan okunur, $m = \frac{0 - n}{p - 0} = -\frac{n}{p}$ olur. Sağa doğru yükselen doğruda $m > 0$, alçalan doğruda $m < 0$.

## Parçalı fonksiyon

**Örnek.** $f\colon \mathbb{R} \to \mathbb{R}$,

$$f(x) = \begin{cases} x + 2, & x < 1 \\ 5 - x, & x \ge 1 \end{cases}$$

Her değer için önce $x$'in **hangi aralıkta** olduğuna bak, sonra yalnızca o satırın kuralını kullan:

- $f(-2)$: $-2 < 1$, üst satır: $-2 + 2 = 0$.
- $f(1)$: $1 \ge 1$, alt satır: $5 - 1 = 4$. (Üst satır $3$ verirdi; ama $x = 1$ üst satıra ait değil.)
- $f(3)$: $3 \ge 1$, alt satır: $5 - 3 = 2$.
- $f(f(0))$: önce $f(0) = 0 + 2 = 2$, sonra $f(2) = 5 - 2 = 3$.

**Kural.** Tanım kümesinin farklı aralıklarında farklı kurallarla verilen fonksiyona **parçalı (parçalı tanımlı) fonksiyon** denir. Kuralın değiştiği noktalara (burada $x = 1$) ve aralıkların uç noktalarına **kritik nokta** denir. Kritik noktada hangi satırın geçerli olduğunu $\le$ ve $<$ işaretleri söyler.

![Parçalı fonksiyonun grafiği. Solda y = x + 2 doğrusu x = 1'e kadar yükseliyor ve (1, 3) noktasında içi boş daireyle bitiyor. Sağda y = 5 − x doğrusu (1, 4) noktasındaki dolu daireden başlayıp alçalıyor. Kesikli y = 3 doğrusu grafiği yalnızca (2, 3) noktasında kesiyor.](gorsel/tyt-matematik/11-05-parcali-grafik.svg "x = 1 noktasında dolu daire f(1) değerini gösterir, boş daire grafiğe ait değildir. y = 3 doğrusu grafiğe yalnızca x = 2'de dokunur.")

**Denklem çözmek.** Aynı fonksiyonda $f(x) = 3$ için her satırı ayrı çöz, sonra bulduğun $x$'in o satırın aralığında olup olmadığını kontrol et:

- Üst satır: $x + 2 = 3$, $x = 1$. Ama üst satır $x < 1$ için geçerli; $1$ **atılır**.
- Alt satır: $5 - x = 3$, $x = 2$. $2 \ge 1$, **geçerli**.

Tek çözüm $x = 2$. Grafikte de $y = 3$ doğrusu $(1, 3)$'teki boş daireye değiyor ama o nokta grafiğe ait değil.

## Kademeli ücret: günlük hayatta parçalı fonksiyon

**Örnek.** Bir belediye suyu şöyle fiyatlıyor: ilk 10 m³ için m³ başına 8 TL, 10 m³'ü aşan her m³ için 12 TL. 15 m³ kullanan hane ne öder?

İlk 10 m³: $10 \cdot 8 = 80$ TL. Kalan 5 m³: $5 \cdot 12 = 60$ TL. Toplam $140$ TL. Bunu fonksiyonla yazarsak:

$$f(x) = \begin{cases} 8x, & 0 \le x \le 10 \\ 80 + 12(x - 10), & x > 10 \end{cases}$$

![Su faturası grafiği. Yatay eksende m³, dikey eksende TL. Orijinden (10, 80) noktasına kadar mavi, daha az dik bir doğru; oradan sonra daha dik yeşil bir doğru. (15, 140) noktası işaretli.](gorsel/tyt-matematik/11-05-tarife.svg "Grafik 10 m³'te kırılır: oradan sonra her m³ daha pahalı olduğu için doğru dikleşir. Kırılma noktasında iki parça aynı değeri (80 TL) verir.")

Ters soru: Fatura 200 TL ise $200 > 80$ olduğundan kullanım 10 m³'ü aşmıştır. $80 + 12(x - 10) = 200$, $x - 10 = 10$, $x = 20$ m³.

**Kural.** Kademeli ücrette ikinci parçanın kuralı "ilk kademenin tamamı + aşan kısım $\times$ yeni fiyat" biçimindedir. Toplam tutar verilirse önce hangi kademede olduğunu sınır değeriyle karşılaştırarak bul.

## ÖSYM tuzakları

> **Kritik noktada yanlış satır:** $x < 1$ ve $x \ge 1$ verilmişse $f(1)$ alt satırdan hesaplanır. Eşitlik işareti hangi satırdaysa kritik nokta o satıra aittir.

> **Çözümü kontrol etmemek:** Parçalı fonksiyonda $f(x) = k$ çözerken bir satırdan çıkan $x$, o satırın aralığında değilse çözüm değildir. Yukarıdaki örnekte $x = 1$ bu yüzden atıldı.

> **Doğrusalı orantı sanmak:** Taksi, abonelik gibi sabit ücretli durumlarda iki katı yol iki katı ücret demek değildir. Önce $m$ ve $n$'yi bul.

> **Yüksek fiyatı bütün miktara uygulamak:** 15 m³ su için $15 \cdot 12 = 180$ TL yazmak yanlıştır. Yeni fiyat yalnızca sınırı aşan kısma uygulanır: $140$ TL.

> **Grafikte boş daireyi okumak:** Bir $x$ değerinde hem boş hem dolu daire varsa fonksiyonun değeri **dolu** dairedir.

## Kendini dene

### Soru 1
$f$ doğrusal bir fonksiyon, $f(0) = -4$ ve $f(2) = 2$ olduğuna göre $f(5)$ kaçtır?

A) 5
B) 7
C) 11
D) 13
E) 15

**Cevap:** C
**Çözüm:** $n = f(0) = -4$. $x$ 2 artınca $f(x)$ 6 artmış: $m = \frac{6}{2} = 3$. $f(x) = 3x - 4$, $f(5) = 15 - 4 = 11$. $15$, sabit terimi unutmaktır; $5$ ise $f(2) = 2$'den orantı kurmaktır.

### Soru 2
$$f(x) = \begin{cases} 3x - 1, & x < 2 \\ x^2 + 2, & x \ge 2 \end{cases}$$

olduğuna göre $f(2) + f(3)$ toplamı kaçtır?

A) 13
B) 14
C) 16
D) 17
E) 20

**Cevap:** D
**Çözüm:** $2 \ge 2$ olduğu için $f(2)$ alt satırdan: $4 + 2 = 6$. $f(3) = 9 + 2 = 11$. Toplam $17$. $f(2)$'yi üst satırdan ($5$) hesaplayan $16$'yı bulur.

### Soru 3
Bir otoparkta ilk 2 saat için toplam 50 TL, sonraki her saat için 20 TL ödeniyor. Aracını 7 saat park eden biri kaç TL öder?

A) 100
B) 140
C) 150
D) 170
E) 190

**Cevap:** C
**Çözüm:** İlk 2 saat 50 TL; kalan $7 - 2 = 5$ saat için $5 \cdot 20 = 100$ TL. Toplam $150$ TL. $190$, 50 TL'nin üstüne 7 saatin hepsi için 20 TL eklemektir (ilk 2 saat iki kez ödenir); $140$ ise her saati 20 TL saymaktır.

## Özet kartı

- Doğrusal fonksiyon: $f(x) = mx + n$; $m$ eğim (1 adımdaki artış), $n = f(0)$.
- İki değerden: $m = \frac{f(b) - f(a)}{b - a}$, sonra $n$. $x$ eşit adımla artarsa $f(x)$ de eşit adımla artar.
- $m = 0$ sabit fonksiyon, $m = 1$ ve $n = 0$ birim fonksiyon.
- Parçalı fonksiyonda önce $x$'in aralığını bul, yalnızca o satırı kullan; kritik noktada $\le$ işaretine bak.
- $f(x) = k$ çözümlerini kendi aralığıyla kontrol et.
- Kademeli ücret: ilk kademenin tamamı + aşan kısım $\times$ yeni fiyat.

## Sonraki adım

Alıştırmaya geç (aşağıdaki düğme). Sonraki ders **Tek-Çift Fonksiyonlar**; orada bir fonksiyonun grafiğinin eksenlere ve orijine göre simetrisine bakacaksın.
