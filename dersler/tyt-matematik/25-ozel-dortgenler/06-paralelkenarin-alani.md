---
baslik: Paralelkenarın Alanı
ders: tyt-matematik
sure: 25 dk
kaynak: MEBİ Konu Özeti beacc4f03a
guncelleme: 2026-11-18
---
# Paralelkenarın Alanı

<div class="giris" dir="rtl" lang="ar">

**الدرس ده عن إيه؟** عن مساحة متوازي الأضلاع (paralelkenarın alanı): إزاي تحسبها، وإزاي الخطوط اللي جوّاه بتقسّمها لأجزاء.

- هتعرف إن المساحة هي القاعدة (taban) مضروبة في الارتفاع (yükseklik) النازل عليها، وإنك تقدر تحسبها كمان من ضلعين والزاوية اللي بينهم بجيب الزاوية (sinüs).
- هتتعلم إن القطر (köşegen) بيقسم الشكل نصّين متساويين، والقطرين مع بعض بيقسموه أربع مثلثات مساحتهم واحدة.
- هتشوف إن نقطة على ضلع أو جوّه الشكل بتعمل مثلثات مجموعها نص المساحة، وإزاي تحسب المثلث اللي بين نقط المنتصف (orta nokta).

**ليه مهم؟** أسئلة المساحة في TYT مش محتاجة حسابات طويلة، محتاجة بس إنك تشوف النص والربع والتمن في الرسمة.

الدرس ٢٥ دقيقة، وكل قاعدة معاها رسمة ومثال محلول. امسك ورقة وقلم وارسم معانا.

</div>

**Bu dersin sonunda:** paralelkenarın alanını taban ve yükseklikten ya da iki kenar ve aradaki açıdan hesaplayabilecek, köşegenlerin ve iç noktaların ayırdığı parçaların alanlarını toplam alan cinsinden bulabileceksin.

> **TYT'de yeri:** Paralelkenar alan soruları çoğu zaman bir iç nokta, kenar üzerinde bir nokta ya da orta noktalar verir ve bir parçanın alanını sorar. Hesap azdır; asıl iş, parçanın bütünün yarısı, dörtte biri ya da sekizde biri olduğunu görmektir. Taban ve yükseklik ile $a \cdot b \cdot \sin \alpha$ formülü ise ara adım olarak sık kullanılır.

## Önce hatırla

<details><summary>Geçen dersten: Köşegenleri 6 cm ve 8 cm olan bir eşkenar dörtgenin bir kenarı ve alanı kaçtır?</summary>
Köşegenler birbirini dik keser ve ortalar: yarılar 3 ve 4, kenar $\sqrt{3^2 + 4^2} = 5$, yani <b>5 cm</b>. Alan = köşegenlerin çarpımının yarısı = 6 · 8 / 2 = <b>24 cm²</b>.
</details>

<details><summary>Geçen dersten: Bir eşkenar dörtgende D köşesinden [AB]'ye inen yükseklik 4,8 cm ise D'den [BC]'ye inen yükseklik kaç cm'dir?</summary>
Eşkenar dörtgenin yükseklikleri eşittir: <b>4,8 cm</b>. Bugün nedenini göreceksin: alan = kenar · yükseklik ve bütün kenarlar eşit olduğu için yükseklikler de eşit çıkar. (Yukarıdaki eşkenar dörtgende 24 = 5 · 4,8.)
</details>

## Temel formüller

### 1. Alan = taban · yükseklik

**Örnek 1.** $ABCD$ paralelkenarında $|AB| = 12$ ve $|AD| = 10$ birimdir. $[DH] \perp [AB]$ ve $|DH| = 8$ birimdir. $[BK] \perp [AD]$ olduğuna göre paralelkenarın alanı ve $|BK|$ kaçtır?

![ABCD paralelkenarı: AB = 12, AD = 10. D'den AB'ye kırmızı DH = 8 dikmesi, B'den AD'ye yeşil BK dikmesi çizilmiş; BK soru işaretiyle gösterilmiş. H ve K'de dik açı işareti.](gorsel/tyt-matematik/25-06-taban-yukseklik.svg "Her kenarın kendi yüksekliği vardır: kırmızı 8, AB tabanına aittir; yeşil BK, AD tabanına aittir.")

**Çözüm.**

1. $[DH]$, $[AB]$ tabanına ait yüksekliktir: $A(ABCD) = |AB| \cdot |DH| = 12 \cdot 8 = 96$ birimkare.
2. Aynı alanı $[AD]$ tabanı ve ona ait yükseklik $[BK]$ ile de yazabilirsin: $|AD| \cdot |BK| = 96$.
3. $10 \cdot |BK| = 96 \Rightarrow |BK| = 9{,}6$ birim.

**Neden?** $ADH$ dik üçgenini kesip $[BC]$ kenarının yanına taşırsan şekil, tabanı $12$ ve yüksekliği $8$ olan bir dikdörtgene döner. Alan değişmez.

**Kural:** $a = |AB|$, $b = |AD|$; $h_a$ ve $h_b$ bu kenarlara ait yükseklikler olsun.

$$A(ABCD) = a \cdot h_a = b \cdot h_b$$

Kısa kenara ait yükseklik daha uzundur ($10 < 12$ iken $9{,}6 > 8$).

> **Tuzak:** Yüksekliği yanlış kenarla çarpmak: $|AD| \cdot |DH| = 10 \cdot 8 = 80$ yanlıştır, $8$ yalnızca $[AB]$'ye aittir. Bir de üçgen alışkanlığıyla ikiye bölmek: paralelkenarda **ikiye bölme yoktur**, $48$ değil $96$.

### 2. İki kenar ve aradaki açı: $a \cdot b \cdot \sin \alpha$

**Örnek 2.** $ABCD$ paralelkenarında $|AB| = 8$, $|AD| = 6$ birim ve $m(\widehat{ABC}) = 120^\circ$'dir. Paralelkenarın alanı kaç birimkaredir?

![ABCD paralelkenarı: AB = 8, AD = 6. A'da mavi 60 derece, B'de yeşil 120 derece yayı. D'den AB'ye kırmızı kesikli h yüksekliği iniyor, H'de dik açı işareti.](gorsel/tyt-matematik/25-06-sinus.svg "ADH dik üçgeninde h, 60 derecelik açının karşısındaki kenardır: h = 6 · sin 60°.")

**Çözüm.**

1. Ardışık açılar bütünlerdir: $m(\widehat{DAB}) = 180^\circ - 120^\circ = 60^\circ$.
2. $ADH$ dik üçgeninde $h = |AD| \cdot \sin 60^\circ = 6 \cdot \dfrac{\sqrt{3}}{2} = 3\sqrt{3}$.
3. $A(ABCD) = |AB| \cdot h = 8 \cdot 3\sqrt{3} = 24\sqrt{3}$ birimkare.

**Kural:** İki komşu kenar $a$, $b$ ve aralarındaki açı $\alpha$ ise

$$A(ABCD) = a \cdot b \cdot \sin \alpha$$

Geniş açı verilirse onun bütünleri olan dar açıyı kullanabilirsin; sonuç aynıdır, çünkü $\sin 120^\circ = \sin 60^\circ$ (birim çemberde $\sin(180^\circ - \alpha) = \sin \alpha$).

> **Tuzak:** Üçgendeki $\dfrac{1}{2} \cdot a \cdot b \cdot \sin \alpha$ formülünü buraya taşımak. Paralelkenarda $\dfrac{1}{2}$ **yoktur**: $12\sqrt{3}$ değil $24\sqrt{3}$. $\sin$ yerine $\cos$ yazmak da ($8 \cdot 6 \cdot \frac{1}{2} = 24$) sık yapılan bir yanlıştır.

## Alanı bölen çizgiler

### 3. Köşegen: iki eş yarı, dört eşit üçgen

**Örnek 3.** $ABCD$ paralelkenarında köşegenler $E$ noktasında kesişiyor. $A(BEC) = 14$ birimkare olduğuna göre $A(ABCD)$ ve $A(ABD)$ kaçtır?

![ABCD paralelkenarı; AC ve BD köşegenleri E'de kesişiyor. Oluşan dört üçgenin her birinde S yazıyor: AEB ve CED mavi, BEC ve DEA yeşil. Köşegen parçalarında eşitlik çentikleri var.](gorsel/tyt-matematik/25-06-kosegen.svg "Mavi ve yeşil üçgenlerin biçimi farklı ama alanları aynıdır: her biri bütünün dörtte biri.")

**Çözüm.**

1. $E$, $[AC]$'nin orta noktasıdır. $ABE$ ve $CBE$ üçgenlerinin tabanları eşittir ($|AE| = |EC|$) ve $B$'den $[AC]$'ye inen yükseklik ortaktır, yani alanları eşittir.
2. Aynı akıl yürütme dört üçgenin hepsine uyar: $A(AEB) = A(BEC) = A(CED) = A(DEA) = 14$.
3. $A(ABCD) = 4 \cdot 14 = 56$ birimkare. $ABD$ üçgeni iki parçadan oluşur: $A(ABD) = 28 = \dfrac{56}{2}$.

**Kural:**

$$A(ABC) = A(ADC) = \frac{A(ABCD)}{2}, \qquad A(AEB) = A(BEC) = A(CED) = A(DEA) = \frac{A(ABCD)}{4}$$

> **Tuzak:** "Bu dört üçgen yalnızca eşkenar dörtgende eşittir" sanmak. Üçgenler her paralelkenarda **eş değildir** (biçimleri farklı) ama **alanları** her zaman eşittir.

### 4. Kenar üzerinde bir nokta: üçgen yarıyı alır

**Örnek 4.** $ABCD$ paralelkenarında $|AB| = 16$ birim, yükseklik $5$ birimdir. $E \in [DC]$, $|DE| = 4$ ve $|EC| = 12$ birimdir. $A(AEB)$, $A(ADE)$ ve $A(BEC)$ kaçtır?

![ABCD paralelkenarı: AB = 16, DE = 4, EC = 12. E'den A ve B'ye mavi çizgiler; AEB üçgeni mavi, ADE ve BEC üçgenleri sarı boyalı. E'den AB'ye kırmızı kesikli 5 birimlik yükseklik.](gorsel/tyt-matematik/25-06-kenarda-nokta.svg "Mavi üçgenin tabanı AB, yüksekliği paralelkenarın yüksekliğidir. Bu yüzden mavi, bütünün tam yarısıdır; iki sarı da öbür yarıyı paylaşır.")

**Çözüm.**

1. $A(ABCD) = 16 \cdot 5 = 80$.
2. $AEB$ üçgeninin tabanı $[AB]$, yüksekliği $5$: $A(AEB) = \dfrac{16 \cdot 5}{2} = 40$, yani bütünün yarısı.
3. İki sarı üçgenin yüksekliği de $5$'tir: $A(ADE) = \dfrac{4 \cdot 5}{2} = 10$, $A(BEC) = \dfrac{12 \cdot 5}{2} = 30$.
4. Kontrol: $10 + 30 = 40$, öbür yarı.

**Kural:** $E \in [DC]$ ise

$$A(AEB) = A(ADE) + A(BEC) = \frac{A(ABCD)}{2}$$

İki sarı üçgenin alanları, tabanlarının oranındadır: $A(ADE) : A(BEC) = |DE| : |EC|$.

> **Tuzak:** $E$'nin yeri değişince mavi üçgenin alanının değiştiğini sanmak. $E$, $[DC]$ üzerinde nereye kayarsa kaysın $A(AEB)$ hep yarıdır; değişen yalnızca iki sarının paylaşımıdır.

### 5. İç bir nokta: karşılıklı üçgenler yarıyı paylaşır

**Örnek 5.** $K$, $ABCD$ paralelkenarının iç bölgesinde bir noktadır. $A(AKD) = 12$, $A(BKC) = 20$ ve $A(AKB) = 18$ birimkaredir. $A(DKC)$ ve $A(ABCD)$ kaçtır?

![ABCD paralelkenarı; içteki K noktası dört köşeye birleştirilmiş. AKD üçgeninde 12, BKC üçgeninde 20 (yeşil), AKB üçgeninde 18, DKC üçgeninde soru işareti (mavi) yazıyor.](gorsel/tyt-matematik/25-06-ic-nokta.svg "Aynı renkteki üçgenler karşılıklıdır. Yeşillerin toplamı ile mavilerin toplamı eşittir, ikisi de bütünün yarısıdır.")

**Çözüm.**

1. Karşılıklı iki üçgen $AKD$ ile $BKC$: toplamları bütünün yarısıdır. $12 + 20 = 32$, yani $A(ABCD) = 64$.
2. Öbür karşılıklı çift de yarıdır: $A(AKB) + A(DKC) = 32 \Rightarrow A(DKC) = 32 - 18 = 14$.

**Neden?** $K$'nin $[AB]$'ye uzaklığı $h_1$, $[DC]$'ye uzaklığı $h_2$ olsun; $h_1 + h_2 = h$ (paralelkenarın yüksekliği). $A(AKB) + A(DKC) = \dfrac{a \cdot h_1}{2} + \dfrac{a \cdot h_2}{2} = \dfrac{a \cdot h}{2}$.

**Kural:** $K$ iç bölgede ise

$$A(AKB) + A(DKC) = A(AKD) + A(BKC) = \frac{A(ABCD)}{2}$$

> **Tuzak:** Karşılıklı üçgenleri **eşit** sanmak ($A(DKC) = A(AKB) = 18$). Eşit olan tek tek üçgenler değil, karşılıklı çiftlerin **toplamlarıdır**. Komşu iki üçgeni ($AKB$ ile $BKC$) toplamak da yanlıştır.

### 6. Köşegen üzerinde bir nokta ve kenarlara paraleller

**Örnek 6.** $ABCD$ paralelkenarında $O \in [AC]$'dir. $O$'dan geçen $[NL] \parallel [AB]$ ve $[MK] \parallel [AD]$ doğruları paralelkenarı dört küçük paralelkenara ayırıyor. $A(ANOK) = 32$, $A(OLCM) = 18$ ve $A(DNOM) = 24$ birimkaredir. $A(KBLO)$ ve $A(ABCD)$ kaçtır?

![ABCD paralelkenarı; AC köşegeni kesikli. Köşegen üzerindeki O'dan AB'ye paralel NL ve AD'ye paralel MK çizilmiş. ANOK kırmızı (32), OLCM mavi (18), DNOM yeşil (24), KBLO yeşil (soru işareti).](gorsel/tyt-matematik/25-06-kosegen-paralel.svg "Köşegen kırmızıyı da maviyi de büyük paralelkenarı da ikiye böler. Geriye kalan iki yeşil parça bu yüzden eşittir.")

**Çözüm.**

1. $[AC]$ köşegeni üç paralelkenarı birden ikiye böler: $ABCD$, $ANOK$ ve $OLCM$.
2. $A(ABC) = A(ADC)$. Sağ yarı: $A(AKO) + A(KBLO) + A(OLC)$. Sol yarı: $A(ANO) + A(DNOM) + A(OMC)$.
3. $A(AKO) = A(ANO) = 16$ ve $A(OLC) = A(OMC) = 9$ olduğundan kalanlar eşittir: $A(KBLO) = A(DNOM) = 24$.
4. $A(ABCD) = 32 + 18 + 24 + 24 = 98$ birimkare.

**Kural:** $O \in [AC]$, $[NL] \parallel [DC]$ ve $[MK] \parallel [DA]$ ise

$$A(DNOM) = A(KBLO)$$

> **Tuzak:** Köşegenin **üzerindeki** iki parçayı (kırmızı ve mavi) eşit sanmak. Eşit olanlar köşegenin geçmediği iki parçadır (yeşiller). $O$ köşegen üzerinde değilse bu kural da çalışmaz.

### 7. Orta noktalar: köşeleri çıkar

**Örnek 7.** $ABCD$ paralelkenarının alanı $64$ birimkaredir. $E$, $[DC]$'nin; $F$, $[BC]$'nin orta noktasıdır. $A(AEF)$ kaçtır?

![ABCD paralelkenarı; E, DC'nin, F, BC'nin orta noktası. AEF üçgeni mavi (3S), köşelerdeki ADE (2S), ECF (S) ve ABF (2S) üçgenleri sarı boyalı. DE ve EC'de tek çentik, BF ve FC'de çift çentik.](gorsel/tyt-matematik/25-06-orta-noktalar.svg "Bütün 8S'dir. Sarı köşeler 2S + S + 2S = 5S; geriye mavi üçgen için 3S kalır.")

**Çözüm.** Mavi üçgeni doğrudan hesaplamak zordur; köşelerdeki sarı üçgenleri bütünden çıkar. $|AB| = a$, yükseklik $h$, $a \cdot h = 64$.

1. $A(ADE)$: taban $|DE| = \dfrac{a}{2}$, yükseklik $h$. Alan $\dfrac{a h}{4} = 16$.
2. $A(ABF)$: taban $|AB| = a$, $F$'nin $[AB]$'ye uzaklığı $\dfrac{h}{2}$. Alan $\dfrac{a h}{4} = 16$.
3. $A(ECF)$: taban $|EC| = \dfrac{a}{2}$, $F$'nin $[DC]$'ye uzaklığı $\dfrac{h}{2}$. Alan $\dfrac{a h}{8} = 8$.
4. $A(AEF) = 64 - (16 + 16 + 8) = 24$ birimkare.

**Kural:** $E$ ve $F$ komşu iki kenarın orta noktaları ise bütünü $8S$ al:

$$A(ADE) = A(ABF) = 2S, \qquad A(ECF) = S, \qquad A(AEF) = 3S = \frac{3}{8} \cdot A(ABCD)$$

> **Tuzak:** $A(AEF)$'yi ezbere "yarı" ya da "dörtte bir" sanmak. Orta nokta sorularında güvenli yol hep aynıdır: bütünü $8S$ (ya da uygun bir sayı) al, köşe üçgenlerini taban ve yükseklikten bul, çıkar.

## Hangi kural ne zaman?

| Soruda verilen | Kullanacağın kural |
|---|---|
| Bir kenar ve ona inen dikme | $A = a \cdot h_a$; öbür yükseklik $h_b = \dfrac{A}{b}$ |
| İki kenar ve bir açı | $A = a \cdot b \cdot \sin \alpha$ (geniş açıysa dar komşusunu kullan) |
| Köşegen(ler) | Yarı ya da dörtte bir |
| Bir kenar üzerinde nokta | Karşı kenara dayanan üçgen yarıdır |
| İç bölgede nokta | Karşılıklı üçgenlerin toplamı yarıdır |
| Köşegen üzerinde nokta, kenarlara paraleller | Köşegenin geçmediği iki parça eşittir |
| Orta noktalar | Bütünü $8S$ al, köşeleri çıkar |

## ÖSYM tuzakları

> **Yükseklik ile yan kenarı karıştırmak.** Alan taban ile **dik** yüksekliğin çarpımıdır; eğik kenar ($|AD|$) yükseklik değildir. $|AB| \cdot |AD|$ yalnızca dikdörtgende alanı verir.

> **Gereksiz $\frac{1}{2}$.** Üçgen formülündeki $\frac{1}{2}$ paralelkenarda yoktur: $a \cdot h$ ve $a \cdot b \cdot \sin \alpha$. Seçeneklerde doğru cevabın yarısı hep bekler.

> **Yüksekliği yanlış tabanla eşlemek.** $h_a$, $[AB]$'ye; $h_b$, $[AD]$'ye aittir. $|AD| \cdot h_a$ alan değildir.

> **Karşılıklı üçgenleri eşit sanmak.** İç noktada eşit olan, karşılıklı çiftlerin **toplamlarıdır**; tek tek üçgenler genelde farklıdır.

> **Orta nokta parçasında ezber oran.** $A(AEF)$ bütünün yarısı ya da dörtte biri değil, $\frac{3}{8}$'idir. Emin değilsen köşeleri çıkar.

## Kendini dene

### Soru 1
![ABCD paralelkenarı: AB = 6, AD = 5. D'den AB'ye kırmızı DH = 4 dikmesi, B'den AD'ye yeşil BK dikmesi; BK soru işaretiyle gösterilmiş.](gorsel/tyt-matematik/25-06-kd1.svg "Şekil ölçeklidir.")

Şekildeki $ABCD$ paralelkenarında $[DH] \perp [AB]$, $[BK] \perp [AD]$, $|AB| = 6$, $|AD| = 5$ ve $|DH| = 4$ birimdir. Buna göre $|BK|$ kaç birimdir?

A) 2,4
B) 3
C) 4
D) 4,8
E) 7,5

**Cevap:** D
**Çözüm:** $A(ABCD) = |AB| \cdot |DH| = 6 \cdot 4 = 24$. Aynı alan $|AD| \cdot |BK|$: $5 \cdot |BK| = 24 \Rightarrow |BK| = 4{,}8$. $2{,}4$, alanı yanlışlıkla ikiye bölmektir; $4$, yükseklikleri eşit sanmaktır; $3$, $|AH|$'dir; $7{,}5$ ise oranı ters kurmaktır ($6 \cdot 5 / 4$).

### Soru 2
$ABCD$ paralelkenarında $|AB| = 10$ cm, $|BC| = 6$ cm ve $m(\widehat{ABC}) = 135^\circ$'dir. Buna göre $A(ABCD)$ kaç cm²'dir?

A) $15\sqrt{2}$
B) $30\sqrt{2}$
C) $30\sqrt{3}$
D) 60
E) $60\sqrt{2}$

**Cevap:** B
**Çözüm:** Dar komşu açı $180^\circ - 135^\circ = 45^\circ$. $A = 10 \cdot 6 \cdot \sin 45^\circ = 60 \cdot \dfrac{\sqrt{2}}{2} = 30\sqrt{2}$. $15\sqrt{2}$, üçgen formülündeki $\frac{1}{2}$'yi eklemektir; $60$, sinüsü unutmaktır; $30\sqrt{3}$, açıyı $60^\circ$ almaktır; $60\sqrt{2}$ ise $\sin 45^\circ$'yi $\sqrt{2}$ sanmaktır.

### Soru 3
![ABCD paralelkenarı; içteki K noktası dört köşeye birleştirilmiş. AKD üçgeninde 9, BKC üçgeninde 15, AKB üçgeninde 11, DKC üçgeninde soru işareti yazıyor.](gorsel/tyt-matematik/25-06-kd3.svg "K, paralelkenarın iç bölgesindedir.")

Şekildeki $ABCD$ paralelkenarında $K$ bir iç noktadır. $A(AKD) = 9$, $A(BKC) = 15$ ve $A(AKB) = 11$ birimkaredir. Buna göre $A(DKC)$ kaç birimkaredir?

A) 6
B) 11
C) 13
D) 15
E) 24

**Cevap:** C
**Çözüm:** Karşılıklı çiftlerin toplamı eşittir: $A(AKB) + A(DKC) = A(AKD) + A(BKC) = 9 + 15 = 24$. $A(DKC) = 24 - 11 = 13$. $11$, karşılıklı üçgenleri eşit sanmaktır; $24$, yarının kendisidir; $6$ ise $15 - 9$ farkıdır, kuralla ilgisi yoktur.

## Özet kartı

- $A = a \cdot h_a = b \cdot h_b$; paralelkenarda $\frac{1}{2}$ yok.
- $A = a \cdot b \cdot \sin \alpha$; geniş açıda dar komşusunu kullan.
- Bir köşegen: iki eş yarı. İki köşegen: alanı eşit dört üçgen ($\frac{1}{4}$ er).
- Kenar üzerindeki $E$: $A(AEB)$ yarıdır; öbür iki üçgen yarıyı taban oranında paylaşır.
- İç nokta $K$: karşılıklı üçgenlerin toplamı yarıdır.
- Orta noktalar: bütünü $8S$ al, köşeleri çıkar; $A(AEF) = 3S$.

## Sonraki adım

Alıştırmaya geç (aşağıdaki düğme). Sonraki ders: **Dikdörtgende Açı ve Uzunluk**. Dikdörtgen, açıları dik olan bir paralelkenardır; bugünkü bütün alan kuralları orada da geçerlidir ve yükseklik doğrudan kenarın kendisi olur.
