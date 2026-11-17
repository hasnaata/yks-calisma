---
baslik: EBOB-EKOK Problemleri
ders: tyt-matematik
sure: 20 dk
kaynak: MEBİ Konu Özeti b7d1686991
guncelleme: 2026-11-18
---
# EBOB-EKOK Problemleri

<div class="giris" dir="rtl" lang="ar">

**الدرس ده عن إيه؟** عن المسائل الكلامية اللي بتتحل بالعامل المشترك الأكبر (EBOB) أو المضاعف المشترك الأصغر (EKOK)، والأهم: إزاي تعرف من كلام السؤال تستخدم أنهي واحد فيهم.

- هتعرف إن تقسيم حاجة كبيرة لقطع متساوية وأكبر ما يمكن (زي أرض لقطع مربعة أو زيت في أزايز) بيحتاج EBOB، وإن تجميع قطع صغيرة لأصغر مربع أو مكعب بيحتاج EKOK.
- هتحل مسائل الحاجات اللي بتتكرر، زي أتوبيسات بتتحرك كل كام دقيقة: هيتحركوا مع بعض تاني إمتى؟
- هتتعلم مسائل باقي القسمة (kalanlı bölme): رقم بيدّي نفس الباقي لما يتقسم على كذا رقم، وإزاي تلاقي المقسوم عليه لما الباقي يكون معروف.

**ليه مهم؟** في TYT كل سنة بييجي سؤال واحد على الأقل من النوع ده. الحساب نفسه سهل، والشطارة كلها إنك تختار الأداة الصح وما تقعش في فخ إنك تكتب طول القطعة وهو سايلك عن عدد القطع.

20 دقيقة بس، والأمثلة محلولة خطوة بخطوة ومعاها رسومات. خدها بهدوء وهتلاقيها أسهل ما انت متخيل.

</div>

**Bu dersin sonunda:** bir problemde EBOB mu EKOK mu gerektiğini sorunun dilinden anlayıp parçalama, birleştirme, aynı anda tekrar etme ve kalanlı bölme problemlerini çözebileceksin.

> **TYT'de yeri:** Her yıl en az bir soru gelir: "kare parsellere ayırma", "eş şişelere doldurma", "eş kartonlarla kare oluşturma", "otobüsler yeniden ne zaman birlikte kalkar?" ve "her birine bölününce aynı kalanı veren sayı" kalıpları en sık görülenlerdir. İşlem kolaydır; asıl iş doğru aracı seçmektir.

## Önce hatırla

<details><summary>EBOB-EKOK Kavramı ve Özellikleri'nden: 24 ve 36 sayılarının EBOB'u ve EKOK'u kaçtır?</summary>
$24 = 2^3 \cdot 3$, $36 = 2^2 \cdot 3^2$. EBOB için ortak tabanlardan üssü <b>küçük</b> olanlar: $2^2 \cdot 3 = 12$. EKOK için bütün tabanlardan üssü <b>büyük</b> olanlar: $2^3 \cdot 3^2 = 72$.
</details>

<details><summary>EBOB-EKOK Kavramı ve Özellikleri'nden: İki pozitif tam sayının çarpımı 540, EBOB'u 6'dır. EKOK'u kaçtır?</summary>
$a \cdot b = \text{EBOB}(a, b) \cdot \text{EKOK}(a, b)$ olduğundan $540 = 6 \cdot \text{EKOK}$, yani EKOK = <b>90</b>.
</details>

## EBOB mu, EKOK mu?

Problemi çözmeden önce tek bir soru sor: **büyük bir şeyi mi parçalıyorum, küçük şeyleri mi birleştiriyorum?**

![Akış şeması: Soru ne istiyor? Bütünü eş parçalara bölmekse EBOB, parça en büyük. Parçaları birleştirmekse EKOK, bütün en küçük. Olaylar tekrar ediyorsa EKOK, ortak periyot.](gorsel/tyt-matematik/02-06-yontem.svg "Parçalamak EBOB, birleştirmek ve tekrar eden olaylar EKOK ister.")

Kısa ipucu: aranan sayı verilen sayılardan **küçükse** (onları bölüyorsa) EBOB, **büyükse** (onların katıysa) EKOK.

## Parçalama: EBOB

**Örnek 1.** Kenarları 72 m ve 48 m olan dikdörtgen bir bahçe, hiç boş yer kalmadan eş ve **en büyük** kare parsellere ayrılacak. Kaç parsel olur?

Karenin kenarı $k$ olsun. Kareler kenarlara tam sığmalı: $k$ hem 72'yi hem 48'i bölmeli. En büyük $k$ istendiği için

$$k = \text{EBOB}(72, 48) = 24 \text{ m}$$

Uzun kenara $72 : 24 = 3$, kısa kenara $48 : 24 = 2$ kare sığar. Parsel sayısı $3 \cdot 2 = 6$.

![72 metreye 48 metrelik dikdörtgen bahçe, 3 sütun 2 satır halinde 24 metrelik altı kareye bölünmüş.](gorsel/tyt-matematik/02-06-kare-parsel.svg "Kare kenarı iki kenarı da bölmeli. Parsel sayısı, her kenara sığan kare sayılarının çarpımıdır.")

Aynı bahçenin çevresine köşelerde de birer ağaç olacak biçimde, eşit ve en geniş aralıklarla ağaç dikilecekse aralık yine $\text{EBOB}(72, 48) = 24$ m olur. Kapalı bir çevrede ağaç sayısı aralık sayısına eşittir: $\dfrac{2(72 + 48)}{24} = 10$ ağaç.

**Örnek 2.** 120 L zeytinyağı, 180 L ayçiçek yağı ve 210 L mısırözü yağı birbirine karıştırılmadan eş hacimli şişelere doldurulacak. Bütün şişeler tam dolu olacak. En az kaç şişe gerekir?

Şişe sayısı **en az** olsun diye şişe hacmi **en büyük** seçilir: $\text{EBOB}(120, 180, 210) = 30$ L.

Şişe sayısı: $\dfrac{120}{30} + \dfrac{180}{30} + \dfrac{210}{30} = 4 + 6 + 7 = 17$.

**Kural.** Bir bütünü eş parçalara ayırırken parça **en büyük** (parça sayısı **en az**) isteniyorsa parça büyüklüğü verilen sayıların EBOB'udur. Parça sayısı için her sayıyı EBOB'a bölüp sonuçları **topla** (ayrı ayrı doldurma) ya da **çarp** (alanı ya da hacmi bölme). Depoyu eş küplere ayırmada üç kenarın EBOB'u alınır, küp sayısı üç bölümün çarpımıdır.

## Birleştirme: EKOK

**Örnek 3.** Kenarları 18 cm ve 12 cm olan eş dikdörtgen kartonlar, üst üste binmeden ve aynı yönde yan yana dizilerek **en küçük** kare oluşturulacak. Kaç karton gerekir?

Karenin kenarı $K$ olsun. Yatayda 18'lik kenarlar, dikeyde 12'lik kenarlar tam sığmalı: $K$ hem 18'in hem 12'nin katı. En küçük $K$:

$$K = \text{EKOK}(18, 12) = 36 \text{ cm}$$

Yatayda $36 : 18 = 2$, dikeyde $36 : 12 = 3$ karton. Toplam $2 \cdot 3 = 6$ karton.

![Solda 18 santimetreye 12 santimetrelik bir dikdörtgen karton; ok ile sağda 2 sütun 3 satır halinde altı kartondan oluşan 36 santimetrelik kare.](gorsel/tyt-matematik/02-06-kare-birlestirme.svg "Karenin kenarı iki kenarın da katı olmalı. En küçük kare için EKOK alınır.")

Eş tuğlalardan (dikdörtgenler prizması) en küçük küp yapmada da aynı yol izlenir: küpün kenarı üç kenarın EKOK'u, tuğla sayısı üç bölümün çarpımıdır.

**Kural.** Küçük eş parçaları birleştirerek **en küçük** kare ya da küp elde etmek için kenar uzunluklarının EKOK'u alınır. Gereken parça sayısı = her yönde sığan parça sayılarının çarpımı.

## Tekrar eden olaylar: EKOK

**Örnek 4.** Bir duraktan üç hat otobüsü sırasıyla 12, 15 ve 20 dakikada bir kalkıyor. Üçü **ilk kez** saat 08.00'de birlikte kalktı. Üçü birlikte **üçüncü kez** saat kaçta kalkar?

Her otobüs kendi periyodunun katlarında kalkar. Üçünün birlikte kalktığı anlar ortak katlardır; ilk ortak kat

$$\text{EKOK}(12, 15, 20) = 60 \text{ dakika}$$

![Üç satırlık zaman çizgisi: 12 dakikalık hat 0, 12, 24, 36, 48, 60'ta; 15 dakikalık hat 0, 15, 30, 45, 60'ta; 20 dakikalık hat 0, 20, 40, 60'ta kalkıyor. 0 ve 60. dakikalar kırmızı çerçeveyle işaretli.](gorsel/tyt-matematik/02-06-otobus-zamanlari.svg "Üç satırda da nokta olan ilk an 60. dakikadır. Birlikte kalkışlar 60 dakikada bir tekrar eder.")

Birlikte kalkışlar 08.00, 09.00, 10.00 … Birinci kez 08.00 (başlangıç) olduğu için üçüncü kez $2 \cdot 60 = 120$ dakika sonra: **10.00**.

**Kural.** Belirli aralıklarla tekrar eden olaylar EKOK zamanında bir aynı anda gerçekleşir. Başlangıç anı birinci kez sayılırsa $n$. kez için geçen süre $(n - 1) \cdot \text{EKOK}$ olur. Soru "başladıktan sonra $n$. kez" diyorsa başlangıç sayılmaz ve süre $n \cdot \text{EKOK}$ olur; soru kökünü dikkatle oku. Pistte koşan atletlerin başlangıçta yeniden buluşması, ışıkların birlikte yanması ve makinelerin birlikte ürün vermesi de bu kalıptır.

## Kalanlı bölme problemleri

**Örnek 5.** Bir sayı 4'e, 6'ya ve 9'a bölündüğünde **her seferinde 1** kalanını veriyor. Bu özellikteki 100'den büyük en küçük sayı kaçtır?

Sayıdan 1 çıkarırsan üçüne de tam bölünür: $x - 1$, EKOK'un katıdır. $\text{EKOK}(4, 6, 9) = 36$, yani $x = 36k + 1$. Değerler: 37, 73, **109**, … Cevap 109.

**Örnek 6.** Bir sayı 4'e bölününce 3, 6'ya bölününce 5, 9'a bölününce 8 kalanını veriyor. Bu özellikteki en küçük pozitif sayı kaçtır?

Kalanlar farklı ama her biri bölenden **1 eksik**. Sayıya 1 eklersen üçüne de tam bölünür: $x + 1 = 36k$, $x = 36k - 1$. En küçük pozitif değer $36 - 1 = 35$.

**Örnek 7.** 75 ile 110 sayıları bir $d$ doğal sayısına bölündüğünde kalanlar sırasıyla 3 ve 2'dir. $d$ en çok kaçtır?

Kalanları çıkarınca tam bölme olur: $d$, $75 - 3 = 72$ ile $110 - 2 = 108$ sayılarını böler. En büyük $d = \text{EBOB}(72, 108) = 36$. Kalanlar 36'dan küçük olduğu için sonuç geçerlidir.

**Kural.**
- Her bölende **aynı kalan** $r$: $x = \text{EKOK} \cdot k + r$.
- Kalanlar bölenden hep **aynı miktar eksik** ($m$): $x = \text{EKOK} \cdot k - m$.
- Bölen aranıyorsa: önce kalanları çıkar, sonra EBOB al; kalanların bölenden küçük olduğunu kontrol et.

## ÖSYM tuzakları

> **Kenarı yazıp sayıyı istemek:** "Kaç parsel?", "kaç şişe?", "kaç karton?" sorusunda EBOB ya da EKOK'un kendisini işaretlemek en sık yapılan hatadır. EBOB/EKOK parçanın ya da bütünün **boyutudur**; sayı için bir adım daha var.

> **Toplamak ile çarpmayı karıştırmak:** Ayrı sıvıları şişelere doldururken şişe sayıları **toplanır** ($4 + 6 + 7$). Alanı ya da hacmi kareye, küpe bölerken sayılar **çarpılır** ($3 \cdot 2$).

> **"n. kez"de başlangıcı yanlış saymak:** Soru 08.00'i "ilk kez" diye veriyorsa üçüncü kez için $3 \cdot 60$ değil $2 \cdot 60$ dakika eklenir. "Başladıktan sonra üçüncü kez" deniyorsa başlangıç sayılmaz, $3 \cdot 60$ dakika eklenir.

> **EKOK yerine çarpım:** 12, 15 ve 20 dakikalık otobüsler $12 \cdot 15 \cdot 20$ dakikada değil, $\text{EKOK} = 60$ dakikada birlikte kalkar. Sayılar aralarında asal değilse çarpım EKOK'tan büyüktür.

> **Kalanı çıkarmadan EBOB almak:** Örnek 7'de $\text{EBOB}(75, 110) = 5$ bulunur ve yanlıştır. Önce kalanlar çıkarılır.

## Kendini dene

### Soru 1
Uzunlukları 90 cm, 150 cm ve 210 cm olan üç kumaş, hiç artmayacak biçimde eş uzunlukta parçalara kesilecek. Parça uzunluğu santimetre cinsinden tam sayı ve olabildiğince büyük olacak.

Buna göre toplam kaç parça elde edilir?

A) 9
B) 12
C) 15
D) 21
E) 30

**Cevap:** C
**Çözüm:** Parça uzunluğu en büyük olacağı için $\text{EBOB}(90, 150, 210) = 30$ cm. Parça sayısı: $\dfrac{90}{30} + \dfrac{150}{30} + \dfrac{210}{30} = 3 + 5 + 7 = 15$. 30 parça uzunluğudur, parça sayısı değil.

### Soru 2
Bir öğrenci 4 günde bir, arkadaşı ise 6 günde bir kütüphaneye gidiyor. İkisi bir pazartesi günü kütüphanede karşılaştı.

İkisi kütüphanede ilk kez yeniden aynı gün bulunduklarında hangi gün olur?

A) Salı
B) Perşembe
C) Cuma
D) Cumartesi
E) Pazar

**Cevap:** D
**Çözüm:** İkisi $\text{EKOK}(4, 6) = 12$ günde bir aynı gün gider. $12 = 7 \cdot 1 + 5$; pazartesiden 5 gün sonra **cumartesi**. EKOK yerine çarpımı ($24$ gün) alan $24 = 7 \cdot 3 + 3$ ile perşembe bulur.

### Soru 3
Bir okuldaki öğrenciler 4'erli, 5'erli ya da 6'şarlı gruplara ayrıldığında her seferinde 2 öğrenci artıyor. Öğrenci sayısı 100 ile 150 arasındadır.

Buna göre öğrenci sayısı kaçtır?

A) 112
B) 118
C) 122
D) 128
E) 142

**Cevap:** C
**Çözüm:** Öğrenci sayısından 2 çıkarınca 4, 5 ve 6'ya tam bölünür: $x - 2 = 60k$. $\text{EKOK}(4, 5, 6) = 60$, $x = 60k + 2$: 62, **122**, 182 … 100 ile 150 arasındaki tek değer 122. Kontrol: $122 = 4 \cdot 30 + 2 = 5 \cdot 24 + 2 = 6 \cdot 20 + 2$.

## Özet kartı

- Büyük bütünü eş, en büyük parçalara ayırmak: **EBOB**.
- Küçük eş parçalarla en küçük kare ya da küp kurmak: **EKOK**.
- Tekrar eden olayların yeniden aynı anda olması: **EKOK**; başlangıç birinci kezse $n$. kez için $(n - 1) \cdot \text{EKOK}$.
- Aynı kalan $r$: $x = \text{EKOK} \cdot k + r$; hep $m$ eksik: $x = \text{EKOK} \cdot k - m$.
- Bölen aranıyorsa önce kalanları çıkar, sonra EBOB al.
- EBOB/EKOK boyutu verir; parça sayısı için bir adım daha at.

## Sonraki adım

Alıştırmaya geç (aşağıdaki düğme). Sonraki ders **Periyodik Problemler**; bu dersteki "tekrar eden olaylar" fikrini günler, saatler ve tekrar eden dizilerle genişleteceksin.
