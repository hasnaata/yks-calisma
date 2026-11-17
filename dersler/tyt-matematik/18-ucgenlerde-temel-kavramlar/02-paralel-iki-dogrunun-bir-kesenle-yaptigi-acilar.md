---
baslik: Paralel İki Doğrunun Bir Kesenle Yaptığı Açılar
ders: tyt-matematik
sure: 20 dk
kaynak: MEBİ Konu Özeti 583bb8ac94
guncelleme: 2026-11-17
---
# Paralel İki Doğrunun Bir Kesenle Yaptığı Açılar

**Bu dersin sonunda:** paralel iki doğru ve bir kesenin oluşturduğu sekiz açıdan birini bilince ötekilerin hepsini bulabilecek, "Z" ve kırık çizgi şekillerinde bilinmeyen açıyı tek adımda hesaplayabileceksin.

> **TYT'de yeri:** Geometri bölümünde tek başına bir soru olarak ya da üçgen sorusunun ilk adımı olarak gelir. En sık kalıp: iki paralel arasında kırılan bir çizgi ve "x kaç derecedir?". Açılar bazen $3x - 20^\circ$ gibi ifadelerle verilir; önce hangi açıların eşit, hangilerinin bütünler olduğunu görmek gerekir.

## Önce hatırla

<details><summary>Geçen dersten: Bir açının bütünlerinin ölçüsü, tümlerinin ölçüsünün 3 katıdır. Bu açı kaç derecedir?</summary>
Açı $x$ olsun: $180^\circ - x = 3(90^\circ - x) \Rightarrow 180 - x = 270 - 3x \Rightarrow 2x = 90$, yani açı <b>45°</b>. Kontrol: bütünleri $135^\circ$, tümleri $45^\circ$; $135 = 3 \cdot 45$. Bugün "bütünler" kelimesini çok kullanacaksın: toplamı $180^\circ$ olan iki açı.
</details>

<details><summary>Geçen dersten: İki doğru bir noktada kesişiyor. Oluşan dört açıdan biri 50° ise öbür üç açı kaçar derecedir?</summary>
Ters açılar eşittir: karşısındaki açı <b>50°</b>. Yanındaki iki açı onunla bir doğru açı oluşturur: <b>130°</b> ve <b>130°</b>. Bugün aynı durumu iki kesişim noktasında birden göreceksin.
</details>

## Kesen ve sekiz açı

$d_1$ ve $d_2$ paralel olsun ($d_1 \parallel d_2$). İkisini de kesen $d_3$ doğrusuna **kesen** denir. Her kesişim noktasında dört açı oluşur; toplam sekiz açı vardır.

**Örnek.** Şekilde $d_1 \parallel d_2$ ve $1$ numaralı açı $65^\circ$'dir. Öbür yedi açıyı bul.

![İki yatay paralel doğru d1 ve d2, bunları 65 derecelik eğimle kesen d3 doğrusu. Üst kesişimde 1, 2, 3, 4; alt kesişimde 5, 6, 7, 8 numaralı açılar var. Tek numaralı dar açılar mavi, çift numaralı geniş açılar kırmızı.](gorsel/tyt-matematik/18-02-sekiz-aci.svg "Mavi açıların hepsi 65°, kırmızı açıların hepsi 115°. Sekiz açıda yalnızca iki farklı ölçü vardır.")

**Çözüm.**

1. Üst kesişimde: $3$, $1$'in ters açısıdır: $65^\circ$. $2$ ve $4$, $1$ ile bir doğru açı oluşturur: $180^\circ - 65^\circ = 115^\circ$.
2. Alt kesişim, üsttekinin aynısıdır; çünkü $d_2$, $d_1$'e paraleldir ve kesen ikisini aynı eğimle keser. $5 = 7 = 65^\circ$, $6 = 8 = 115^\circ$.

**Kural:** Paralel iki doğruyu kesen bir doğru yalnızca **iki farklı** açı oluşturur.

$$\text{dar açılar birbirine eşit}, \qquad \text{geniş açılar birbirine eşit}, \qquad \text{dar} + \text{geniş} = 180^\circ$$

Kesen paralellere dik ise sekiz açının hepsi $90^\circ$ olur.

## 1. Eşit açılar: yöndeş, iç ters, dış ters

Sekiz açıdan oluşan çiftlerin adları vardır. Şekle göre:

| Ad | Ne demek? | Çiftler | Ölçüler |
|---|---|---|---|
| Yöndeş | İki kesişimde **aynı konumdaki** açılar (ikisi de sağ üstte gibi) | $1{-}5$, $2{-}6$, $3{-}7$, $4{-}8$ | Eşit |
| İç ters | Paralellerin **arasında**, kesenin **farklı** yanlarında | $3{-}5$, $4{-}6$ | Eşit |
| Dış ters | Paralellerin **dışında**, kesenin **farklı** yanlarında | $1{-}7$, $2{-}8$ | Eşit |

Ad ezberlemek yerine şekle bak: iki açı da dar ya da ikisi de genişse **eşittir**.

**Tersi de doğrudur:** Bir kesen iki doğruyla eşit yöndeş (ya da eşit iç ters) açılar yapıyorsa bu iki doğru paraleldir. Yöndeş açılar $68^\circ$ ile $70^\circ$ ise doğrular paralel **değildir**; şekil paralel gibi görünse bile.

> **Tuzak:** Bu eşitlikler yalnızca doğrular **paralel** ise geçerlidir. Soruda $d_1 \parallel d_2$ yazmıyorsa (ya da şekilde paralellik işareti yoksa) "göz kararı paralel" diye eşitlik kullanma.

## 2. Karşı durumlu açılar: toplam 180°

Paralellerin arasında, kesenin **aynı** yanında kalan iki açıya **karşı durumlu açılar** denir (şekilde $3{-}6$ ve $4{-}5$). Biri dar, öbürü geniştir.

**Örnek.** Şekilde $d_1 \parallel d_2$'dir. $A$'daki açı $2x + 20^\circ$, $B$'deki açı $3x - 40^\circ$ ise bu açılar kaçar derecedir?

![Yatay paralel d1 ve d2 doğrularını A ve B'de kesen bir kesen. Kesenin sağında, iki paralelin arasında A'da 2x + 20 derece (mavi), B'de 3x − 40 derece (kırmızı) işaretli.](gorsel/tyt-matematik/18-02-karsi-durumlu.svg "İki açı da paralellerin arasında ve kesenin sağında: karşı durumlu. Mavi açı geniş (100°), kırmızı açı dar (80°).")

**Çözüm.** İki açı da paralellerin arasında ve kesenin aynı (sağ) yanında; karşı durumludur.

1. $(2x + 20) + (3x - 40) = 180 \Rightarrow 5x - 20 = 180 \Rightarrow x = 40$.
2. $A$'daki açı $2 \cdot 40 + 20 = 100^\circ$, $B$'deki açı $3 \cdot 40 - 40 = 80^\circ$. Kontrol: $100 + 80 = 180$.

**Kural:**

$$\text{karşı durumlu açıların toplamı} = 180^\circ$$

> **Tuzak:** İki açıyı "paralel doğrularda açılar eşittir" diye eşitlersen $2x + 20 = 3x - 40$, $x = 60$ bulursun. Bu yanlış: şekilde biri belirgin biçimde dar, öbürü geniş. Önce **dar mı geniş mi** diye bak, sonra eşitle ya da topla.

## 3. "Z" şekli: iç ters açılar

Paralel iki doğru parçasını birleştiren bir doğru parçası "Z" harfi gibi bir şekil oluşturur.

**Örnek.** $[AB] \parallel [CD]$ ve $m(\widehat{ABC}) = 40^\circ$ ise $x = m(\widehat{BCD})$ kaçtır?

![Üstte A'dan B'ye, altta C'den D'ye paralel iki doğru parçası; B ile C bir çapraz doğru parçasıyla birleşmiş ve Z harfi oluşmuş. B'deki açı 40 derece, C'deki açı x.](gorsel/tyt-matematik/18-02-z-kurali.svg "Z harfinin iki köşesindeki açılar iç ters açıdır: x = 40°.")

**Çözüm.** $[BC]$ bir kesen gibi davranır. $\widehat{ABC}$ ile $\widehat{BCD}$ paralellerin arasında, kesenin farklı yanlarındadır: iç ters açılar. $x = 40^\circ$.

**Kural:** Z şeklinin iki köşesindeki açılar eşittir: $x = y$.

## 4. Kırık çizgi: içteki açı = iki uçtaki açının toplamı

Paralel iki doğru parçası arasında bir çizgi bir kez kırılırsa ok ucuna benzer bir şekil oluşur.

**Örnek.** $[AB] \parallel [CD]$, $m(\widehat{BAE}) = 35^\circ$ ve $m(\widehat{DCE}) = 50^\circ$ ise $m(\widehat{AEC})$ kaçtır?

![Üstte AB, altta CD paralel doğru parçaları. A'dan ve C'den çıkan iki doğru parçası sağdaki E noktasında birleşiyor. A'da 35, C'de 50 derece. E'den geçen kesikli yatay doğru E'deki açıyı 35 ve 50 derecelik iki parçaya bölüyor.](gorsel/tyt-matematik/18-02-kirik-cizgi.svg "E'den paralel çizince iki Z oluşur. Aynı renkli açılar iç ters açıdır, eşittir. E'deki açı 35° + 50° = 85°.")

**Çözüm.** $E$'den $[AB]$'ye paralel bir doğru çiz (kesikli). Bu doğru $E$'deki açıyı ikiye böler.

1. Üst parça, $\widehat{BAE}$ ile iç ters açıdır (üstteki Z): $35^\circ$.
2. Alt parça, $\widehat{DCE}$ ile iç ters açıdır (alttaki Z): $50^\circ$.
3. $m(\widehat{AEC}) = 35^\circ + 50^\circ = 85^\circ$.

**Kural:** Kırılma noktasındaki açı, iki uçtaki açının toplamıdır.

$$m(\widehat{AEC}) = m(\widehat{BAE}) + m(\widehat{DCE})$$

Çizgi birden çok kez kırılıyorsa her kırılma noktasından ayrı bir paralel çiz ve aynı işi tekrarla.

> **Tuzak:** Kural, uçtaki açılar paralel ışınların **E'ye bakan** tarafından ölçülürse geçerlidir ($[AB$ ve $[CD$ ışınları $E$ ile aynı yöne gider). Işınlar $E$'nin ters yönüne gidiyorsa ($B$ ve $D$ solda, $E$ sağda) uçtaki açılar geniş çıkar ve kural değişir: üç açının toplamı $360^\circ$ olur. Bunu da $E$'den paralel çizip karşı durumlu açılarla bulursun.

## ÖSYM tuzakları

> **Dar ile genişi eşitlemek.** İfadeyle verilen iki açıyı eşitlemeden önce şekle bak: biri dar, öbürü genişse toplamları $180^\circ$'dir. Seçeneklerde yanlış denklemin sonucu hazır bekler.

> **$x$'i bulup durmak.** Soru çoğu zaman $x$'i değil bir **açıyı** ister. $x = 40$ bulduysan istenen açı $2x + 20^\circ = 100^\circ$ olabilir.

> **Paralellik verilmeden eşitlik kullanmak.** Eşitlikler ancak $d_1 \parallel d_2$ ise geçerlidir. Soru "hangi doğrular paraleldir?" diye soruyorsa açıların eşit olup olmadığına bakarsın; $68^\circ$ ile $70^\circ$ yakın ama eşit değildir.

> **Kırık çizgide yanlış taraftaki açı.** Uçtaki açılar $E$'ye bakan ışınlarla ölçülmüşse $E = $ toplam; ters yöndeki ışınlarla ölçülmüşse üçünün toplamı $360^\circ$'dir. İki durumu karıştırma; emin değilsen $E$'den paralel çiz.

## Kendini dene

### Soru 1
Paralel iki doğru bir kesenle kesiliyor. Oluşan iç ters açılardan birinin ölçüsü $3x + 10^\circ$, diğerininki $2x + 20^\circ$'dir. Buna göre $x$ kaçtır?

A) 10
B) 20
C) 30
D) 40
E) 50

**Cevap:** A
**Çözüm:** İç ters açılar eşittir: $3x + 10 = 2x + 20 \Rightarrow x = 10$. Açılar $40^\circ$'dir. $30$, açıları toplayıp $180^\circ$'ye eşitlemekten ($5x + 30 = 180$) gelir; $40$ ise açının kendisidir.

### Soru 2
Paralel iki doğru bir kesenle kesiliyor. Karşı durumlu iki açıdan biri öbüründen $40^\circ$ büyüktür. Büyük olan açı kaç derecedir?

A) 40
B) 70
C) 90
D) 110
E) 140

**Cevap:** D
**Çözüm:** Küçük açı $a$ ise $a + (a + 40) = 180 \Rightarrow a = 70$. Büyük açı $70^\circ + 40^\circ = 110^\circ$. $70^\circ$ küçük açıdır; $140^\circ$ ise $180^\circ - 40^\circ$ işleminden gelir.

### Soru 3
![Üstte AB, altta CD paralel doğru parçaları. A'dan ve C'den çıkan doğru parçaları sağdaki E noktasında birleşiyor. A'daki açı 38 derece, C'deki açı x, E'deki açı 3x.](gorsel/tyt-matematik/18-02-kd3.svg "AB ve CD paraleldir.")

Şekilde $[AB] \parallel [CD]$, $m(\widehat{BAE}) = 38^\circ$, $m(\widehat{DCE}) = x$ ve $m(\widehat{AEC}) = 3x$'tir. Buna göre $m(\widehat{AEC})$ kaç derecedir?

A) 19
B) 38
C) 57
D) 76
E) 123

**Cevap:** C
**Çözüm:** Kırılma noktasındaki açı iki uçtaki açının toplamıdır: $3x = x + 38 \Rightarrow 2x = 38 \Rightarrow x = 19$. $m(\widehat{AEC}) = 3 \cdot 19 = 57^\circ$. $19$, $x$'in kendisidir; $123^\circ$ ise $180^\circ - 57^\circ$'dir.

## Özet kartı

- Paralel iki doğru ve bir kesen: dar açılar eşit, geniş açılar eşit, dar + geniş $= 180^\circ$.
- Yöndeş, iç ters ve dış ters açılar **eşittir**; karşı durumlu açıların toplamı $180^\circ$'dir.
- Eşit yöndeş ya da iç ters açı varsa doğrular paraleldir; yoksa değildir.
- Z şekli: iki köşedeki açılar eşittir.
- Kırık çizgi: içteki açı $=$ iki uçtaki açının toplamı. Emin değilsen kırılma noktasından paralel çiz.
- İfadeli sorularda önce "dar mı geniş mi?" diye bak, sonra eşitle ya da 180'e tamamla.

## Sonraki adım

Alıştırmaya geç (aşağıdaki düğme). Sonraki ders: **Üçgende Açılar**. Orada bugünkü iç ters açıları kullanarak üçgenin iç açıları toplamının neden $180^\circ$ olduğunu göreceksin.
