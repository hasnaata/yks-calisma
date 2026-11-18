---
baslik: Paralelkenarda Açı ve Uzunluk
ders: tyt-matematik
sure: 25 dk
kaynak: MEBİ Konu Özeti c5688aeaf4
guncelleme: 2026-11-18
---
# Paralelkenarda Açı ve Uzunluk

<div class="giris" dir="rtl" lang="ar">

**الدرس ده عن إيه؟** عن متوازي الأضلاع (paralelkenar): الشكل الرباعي اللي كل ضلعين قصاد بعض فيه متوازيين.

- هتعرف إن الأضلاع المتقابلة متساوية، والزوايا المتقابلة متساوية، وكل زاويتين جنب بعض مجموعهم 180 درجة.
- هتتعلم إن القطرين (köşegenler) بينصّفوا بعض، وإن العمودين النازلين من رأسين على القطر بيعملوا مثلثين متطابقين.
- هتشوف إن منصف الزاوية (açıortay) جوه متوازي الأضلاع بيعمل دايمًا مثلث متساوي الساقين (ikizkenar üçgen)، وإن منصفين زاويتين جنب بعض بيقطعوا بعض بزاوية قائمة.

**ليه مهم؟** متوازي الأضلاع هو الأساس بتاع المعين والمستطيل والمربع اللي جايين بعده، وأسئلته في TYT غالبًا بتتحل بمنصف زاوية ومثلث متساوي الساقين.

الدرس ٢٥ دقيقة، وكل قاعدة معاها رسمة ومثال محلول. ارسم الشكل بإيدك وإنت ماشي.

</div>

**Bu dersin sonunda:** paralelkenarda kenar, açı ve köşegen bağıntılarını, köşegene inen dikmeleri ve açıortayların oluşturduğu ikizkenar üçgenleri kullanarak eksik uzunluğu ya da açıyı bulabileceksin.

> **TYT'de yeri:** Paralelkenar soruları çoğunlukla bir açıortay çizer ve bir uzunluk ya da çevre sorar; çözüm, açıortayın paralel kenarlarla oluşturduğu ikizkenar üçgeni görmektir. Köşegenlerin birbirini ortalaması ve ardışık açıların bütünler olması ise hemen her soruda ara adım olarak kullanılır. Eşkenar dörtgen, dikdörtgen ve kare bu derstekilerin hepsini taşır.

## Önce hatırla

<details><summary>Geçen dersten: Tabanları 12 cm ve 8 cm, yüksekliği 5 cm olan bir yamuğun alanı kaç cm²'dir?</summary>
Alan = (alt taban + üst taban) / 2 · yükseklik = (12 + 8) / 2 · 5 = <b>50 cm²</b>. Paralelkenar da bir yamuk gibi düşünülebilir: iki tabanı eşittir.
</details>

<details><summary>Geçen dersten: ABCD yamuğunda [AB] ∥ [DC], köşegenler O'da kesişiyor. A(DOC) = 4 ve A(AOB) = 9 ise A(AOD) kaçtır?</summary>
Yan kenarlara komşu iki üçgenin alanı eşittir ve çarpımları öbür ikisinin çarpımına eşittir: A(AOD) · A(BOC) = 4 · 9 = 36, A(AOD) = A(BOC) olduğu için A(AOD) = <b>6</b>. Bugün paralelkenarda köşegenlerin kesim noktasının çok daha özel olduğunu göreceksin: iki köşegenin de orta noktası.
</details>

## Paralelkenar nedir?

Karşılıklı kenarları paralel olan dörtgene **paralelkenar** denir: $ABCD$ paralelkenarında $[AB] \parallel [DC]$ ve $[AD] \parallel [BC]$. Şekillerde paralel kenarlar aynı sayıda okla gösterilir.

### 1. Karşılıklı kenarlar eşittir

**Örnek 1.** $ABCD$ paralelkenarında $|AB| = 2x + 3$, $|DC| = x + 8$ ve $|AD| = 6$ birimdir. Paralelkenarın çevresi kaç birimdir?

![ABCD paralelkenarı. AB ve DC üzerinde tek ok, AD ve BC üzerinde çift ok. AB kenarında 2x + 3, DC kenarında x + 8, AD kenarında 6 yazıyor; BC soru işaretiyle gösterilmiş.](gorsel/tyt-matematik/25-04-kenarlar.svg "Aynı sayıda ok taşıyan kenarlar paraleldir ve eşittir: tek oklar AB ile DC, çift oklar AD ile BC.")

**Çözüm.**

1. Karşılıklı kenarlar eşittir: $2x + 3 = x + 8 \Rightarrow x = 5$. Demek ki $|AB| = |DC| = 13$.
2. $|BC| = |AD| = 6$.
3. Çevre $= 13 + 6 + 13 + 6 = 2 \cdot (13 + 6) = 38$ birim.

**Kural:** $|AB| = |DC| = a$ ve $|AD| = |BC| = b$ ise

$$\text{Çevre}(ABCD) = 2(a + b)$$

> **Tuzak:** $x = 5$'i bulup durmak ya da çevreyi $a + b = 19$ diye yazmak. Çevre için iki komşu kenarın toplamını **ikiyle** çarp.

### 2. Açılar: karşılıklılar eşit, ardışıklar bütünler

**Örnek 2.** $ABCD$ paralelkenarında $m(\widehat{A}) = (2x + 10)^\circ$ ve $m(\widehat{B}) = (3x + 20)^\circ$'dir. Paralelkenarın açılarını bul.

![ABCD paralelkenarı. A ve C köşelerinde mavi açı yayları, A'da 2x + 10 derece; B ve D köşelerinde yeşil açı yayları, B'de 3x + 20 derece. C ve D'deki açılar soru işaretiyle gösterilmiş.](gorsel/tyt-matematik/25-04-acilar.svg "Aynı renkli açılar karşılıklıdır ve eşittir. Bir mavi ile bir yeşil açının toplamı 180°'dir.")

**Çözüm.**

1. $\widehat{A}$ ile $\widehat{B}$ aynı kenarın ($[AB]$) iki ucundadır, $[AD] \parallel [BC]$ arasında kalırlar: toplamları $180^\circ$'dir.
2. $(2x + 10) + (3x + 20) = 180 \Rightarrow 5x = 150 \Rightarrow x = 30$.
3. $m(\widehat{A}) = 70^\circ$, $m(\widehat{B}) = 110^\circ$.
4. Karşılıklı açılar eşittir: $m(\widehat{C}) = 70^\circ$, $m(\widehat{D}) = 110^\circ$. Kontrol: $70 + 110 + 70 + 110 = 360$.

**Kural:**

$$m(\widehat{A}) = m(\widehat{C}), \qquad m(\widehat{B}) = m(\widehat{D}), \qquad m(\widehat{A}) + m(\widehat{B}) = 180^\circ$$

> **Tuzak:** Ardışık iki açıyı eşitlemek. $2x + 10 = 3x + 20$ yazarsan $x = -10$ çıkar. **Ardışık** açılar bütünler, **karşılıklı** açılar eşittir.

### 3. Köşegenler birbirini ortalar

**Örnek 3.** $ABCD$ paralelkenarında köşegenler $E$ noktasında kesişiyor. $|AE| = x + 4$, $|EC| = 2x - 1$ ve $|BE| = 7$ birimdir. $|AC|$ ve $|BD|$ kaç birimdir?

![ABCD paralelkenarı; mavi AC ve yeşil BD köşegenleri E'de kesişiyor. AE üzerinde x + 4, EC üzerinde 2x − 1, EB üzerinde 7 yazıyor; ED soru işaretiyle gösterilmiş. Mavi parçalarda tek çentik, yeşil parçalarda çift çentik.](gorsel/tyt-matematik/25-04-kosegenler.svg "E her iki köşegenin de orta noktasıdır. Mavi parçalar birbirine, yeşil parçalar birbirine eşittir; ama mavi ile yeşil eşit değildir.")

**Çözüm.**

1. $E$, $[AC]$'nin orta noktasıdır: $x + 4 = 2x - 1 \Rightarrow x = 5$. $|AE| = |EC| = 9$, $|AC| = 18$.
2. $E$, $[BD]$'nin de orta noktasıdır: $|ED| = |BE| = 7$, $|BD| = 14$.

**Neden?** $ABE$ ve $CDE$ üçgenlerinde $|AB| = |CD|$; $[AB] \parallel [DC]$ olduğu için $m(\widehat{EAB}) = m(\widehat{ECD})$ ve $m(\widehat{EBA}) = m(\widehat{EDC})$ (iç ters açılar). Üçgenler eştir (AKA), bu yüzden $|AE| = |EC|$ ve $|BE| = |ED|$.

**Kural:**

$$|AE| = |EC| = \frac{|AC|}{2}, \qquad |BE| = |ED| = \frac{|BD|}{2}$$

> **Tuzak:** Paralelkenarda köşegenler birbirini ortalar ama genelde **eşit değildir** ($18 \ne 14$). Köşegenlerin eşit olması dikdörtgene özgüdür.

### 4. Köşegene inen dikmeler: iki eş üçgen

**Örnek 4.** $ABCD$ paralelkenarında $[DE] \perp [AC]$ ve $[BF] \perp [AC]$'dir ($E$ ve $F$, $[AC]$ üzerinde). $|AD| = 5$, $|DE| = 4$ ve $|EF| = 8$ birimdir. $|AC|$ kaç birimdir?

![ABCD paralelkenarı ve AC köşegeni. D'den AC'ye kırmızı DE dikmesi, B'den AC'ye kırmızı BF dikmesi; E ve F'de dik açı işareti. AED ve CFB üçgenleri mavi boyalı. AD = 5, DE = 4, EF = 8; AE ve FC üzerinde eşitlik çentiği.](gorsel/tyt-matematik/25-04-dikmeler.svg "Mavi üçgenler eştir: AED ve CFB. Bu yüzden iki dikme eşit (4 ve 4), köşegenin iki ucundaki parçalar eşittir (3 ve 3).")

**Çözüm.**

1. $AED$ dik üçgeninde Pisagor: $|AE|^2 = 5^2 - 4^2 = 9 \Rightarrow |AE| = 3$.
2. $AED$ ve $CFB$ üçgenleri eştir: hipotenüsler $|AD| = |CB|$, ve $[AD] \parallel [BC]$ olduğu için $m(\widehat{DAE}) = m(\widehat{BCF})$ (iç ters açılar). Demek ki $|FC| = |AE| = 3$ ve $|BF| = |DE| = 4$.
3. $|AC| = |AE| + |EF| + |FC| = 3 + 8 + 3 = 14$ birim.

**Kural:** $[DE] \perp [AC]$ ve $[BF] \perp [AC]$ ise

$$|DE| = |BF|, \qquad |AE| = |FC|$$

> **Tuzak:** Köşegenin iki ucundaki parçaları ($|AE|$ ve $|FC|$) unutup $|AC| = |EF| = 8$ almak ya da yalnızca bir ucu ekleyip $11$ bulmak.

## Açıortaylar

### 5. Açıortay paralel kenarla ikizkenar üçgen oluşturur

**Örnek 5.** $ABCD$ paralelkenarında $|AB| = 10$ ve $|AD| = 6$ birimdir. $\widehat{A}$'nın açıortayı $[DC]$'yi $K$ noktasında kesiyor. $|KC|$ kaç birimdir?

![ABCD paralelkenarı: AB = 10, AD = 6. A'dan çıkan kırmızı açıortay DC'yi K'de kesiyor. A'daki iki yarım açı ve K'deki DKA açısı alfa ile işaretli. ADK üçgeni mavi boyalı; AD ve DK üzerinde eşitlik çentiği; DK = 6, KC = 4.](gorsel/tyt-matematik/25-04-aciortay-ikizkenar.svg "Üç α eşittir: A'daki ikisi açıortaydan, K'deki iç ters açıdan gelir. ADK üçgeninde iki açı eşit olduğu için |DK| = |AD| = 6.")

**Çözüm.**

1. Açıortay: $m(\widehat{DAK}) = m(\widehat{KAB}) = \alpha$.
2. $[DC] \parallel [AB]$ ve $[AK]$ kesen: $m(\widehat{DKA}) = m(\widehat{KAB}) = \alpha$ (iç ters açılar).
3. $ADK$ üçgeninde $A$ ve $K$'deki açılar eşit, yani üçgen ikizkenardır: $|DK| = |AD| = 6$.
4. $|KC| = |DC| - |DK| = 10 - 6 = 4$ birim.

**Kural:** Paralelkenarda bir köşeden çizilen açıortay karşı kenarı keserse, kesilen kenardan köşeye komşu parça, açının öbür kolu olan kenara eşittir:

$$|DK| = |AD|, \qquad |KC| = |AB| - |AD|$$

> **Tuzak:** İkizkenar üçgenin eşit kenarlarını yanlış eşleştirmek. Eşit olanlar $\widehat{K}$ ile $\widehat{A}$'nın **karşısındaki** kenarlardır: $|AD|$ ve $|DK|$. $|AK|$ (açıortayın kendisi) bunlara eşit değildir.

### 6. Komşu açıların açıortayları diktir

**Örnek 6.** $ABCD$ paralelkenarında $|AB| = 10$ birimdir. $\widehat{A}$ ve $\widehat{B}$'nin açıortayları paralelkenarın içindeki $E$ noktasında kesişiyor. $E$'den $[AD]$'ye paralel çizilen doğru $[AB]$'yi $F$'de kesiyor. $m(\widehat{AEB})$ ve $|EF|$ kaçtır?

![ABCD paralelkenarı: A ve B'nin kırmızı açıortayları E'de kesişiyor, E'de dik açı işareti. ABE üçgeni mavi boyalı. E'den AD'ye paralel yeşil kesikli EF çizilmiş; AF = 5, FB = 5, FE = 5, üçü de yeşil çentikli.](gorsel/tyt-matematik/25-04-aciortaylar.svg "A ile B'nin yarımlarının toplamı 90° olduğu için E'deki açı diktir. F, AB'nin orta noktasıdır ve |FA| = |FB| = |FE| = 5.")

**Çözüm.**

1. $m(\widehat{A}) + m(\widehat{B}) = 180^\circ$, yarımlarının toplamı $90^\circ$'dir. $ABE$ üçgeninde $m(\widehat{AEB}) = 180^\circ - 90^\circ = 90^\circ$.
2. $AFE$ üçgeni: $[FE] \parallel [AD]$ olduğu için $m(\widehat{AEF}) = m(\widehat{DAE})$ (iç ters), bu da $m(\widehat{EAF})$'ye eşittir. Kural 5'teki gibi ikizkenar: $|FE| = |AF|$.
3. Aynı şey $BFE$ üçgeninde: $|FE| = |FB|$.
4. $|AF| = |FB| = |FE|$ olduğundan $F$, $[AB]$'nin orta noktasıdır: $|EF| = \dfrac{10}{2} = 5$ birim.

**Kural:**

$$m(\widehat{AEB}) = 90^\circ, \qquad |EF| = |AF| = |FB| = \frac{|AB|}{2}$$

**Sonuç:** İki açıortay $[DC]$ kenarının **üzerinde** bir $K$ noktasında buluşursa Kural 5 iki kez çalışır: $|DK| = |AD|$ ve $|KC| = |BC| = |AD|$. Bu durumda $|AB| = |DC| = 2|AD|$ olur.

> **Tuzak:** $|EF|$'yi $|AD|$'ye eşit sanmak. $[EF]$, $[AD]$'ye paraleldir ama uzunluğu $|AB|$'nin yarısıdır; $|AD|$ ile ilgisi yoktur.

## Hangi kural ne zaman?

| Soruda verilen | Kullanacağın kural |
|---|---|
| Karşılıklı kenarlar cebirsel | Eşitle: $\lvert AB \rvert = \lvert DC \rvert$, $\lvert AD \rvert = \lvert BC \rvert$ |
| İki açı cebirsel | Ardışıksa toplam $180^\circ$, karşılıklıysa eşit |
| Köşegen parçaları | $E$ iki köşegenin de orta noktası |
| Köşegene dikmeler | $\lvert DE \rvert = \lvert BF \rvert$, $\lvert AE \rvert = \lvert FC \rvert$ |
| Tek açıortay karşı kenarı kesiyor | İkizkenar üçgen: $\lvert DK \rvert = \lvert AD \rvert$ |
| Komşu iki açıortay | Aradaki açı $90^\circ$, $\lvert EF \rvert = \dfrac{\lvert AB \rvert}{2}$ |

## ÖSYM tuzakları

> **Ardışık açıları eşitlemek.** Paralelkenarda yan yana iki açı eşit değil bütünlerdir. Eşitlik yalnızca karşılıklı açılarda vardır.

> **Köşegenleri eşit sanmak.** Köşegenler birbirini ortalar, ama eşit uzunlukta değildir. $|AC| = |BD|$ yalnızca dikdörtgende (ve karede) doğrudur.

> **Açıortayda yanlış ikizkenar.** Açıortay $[DC]$'yi $K$'de kesince eşit olan $|DK|$ ile $|AD|$'dir. $|KC|$'yi $|AD|$'ye eşitlemek ya da $|AK|$'yi kenara eşitlemek yanlıştır.

> **Çevreyi yarım hesaplamak.** Çevre $2(a + b)$'dir; seçeneklerde $a + b$ hazır bekler.

> **Köşegene dikmelerde uç parçaları atlamak.** $|AC| = |AE| + |EF| + |FC|$ ve $|AE| = |FC|$; ortadaki $|EF|$ tek başına köşegen değildir.

## Kendini dene

### Soru 1
$ABCD$ paralelkenarında $m(\widehat{A}) = (3x - 20)^\circ$ ve $m(\widehat{C}) = (x + 40)^\circ$'dir. Buna göre $m(\widehat{B})$ kaç derecedir?

A) 30
B) 70
C) 80
D) 100
E) 110

**Cevap:** E
**Çözüm:** $\widehat{A}$ ile $\widehat{C}$ karşılıklıdır, eşittir: $3x - 20 = x + 40 \Rightarrow x = 30$, $m(\widehat{A}) = 70^\circ$. $\widehat{B}$, $\widehat{A}$'ya ardışıktır: $m(\widehat{B}) = 180^\circ - 70^\circ = 110^\circ$. $30$, $x$'in kendisidir; $70$, $\widehat{A}$'dır. $80$ ve $100$, $\widehat{A}$ ile $\widehat{C}$'yi bütünler sanmaktan gelir ($4x + 20 = 180$, $x = 40$).

### Soru 2
![ABCD paralelkenarı; mavi AC ve yeşil BD köşegenleri E'de kesişiyor. AE üzerinde 2x − 1, EC üzerinde x + 3, DE üzerinde x + 1 yazıyor.](gorsel/tyt-matematik/25-04-kd2.svg "Köşegenler E'de kesişiyor.")

Şekildeki $ABCD$ paralelkenarında köşegenler $E$ noktasında kesişiyor. $|AE| = 2x - 1$, $|EC| = x + 3$ ve $|DE| = x + 1$ birimdir. Buna göre $|AC| + |BD|$ toplamı kaç birimdir?

A) 12
B) 14
C) 19
D) 24
E) 28

**Cevap:** D
**Çözüm:** $E$, $[AC]$'nin orta noktası: $2x - 1 = x + 3 \Rightarrow x = 4$. $|AE| = |EC| = 7$, $|AC| = 14$. $E$, $[BD]$'nin de orta noktası: $|DE| = 5$, $|BD| = 10$. Toplam $14 + 10 = 24$. $12$, iki yarım parçanın toplamıdır ($7 + 5$); $14$ yalnızca $|AC|$'dir; $28$, köşegenleri eşit sanmaktır ($14 + 14$).

### Soru 3
![ABCD paralelkenarı: AD = 5, AB = 12. A ve B'den çıkan kırmızı açıortaylar DC'yi K ve L noktalarında kesiyor; KL soru işaretiyle gösterilmiş.](gorsel/tyt-matematik/25-04-kd3.svg "Açıortaylar paralelkenarın içinde kesişmiyor; DC'yi ayrı noktalarda kesiyor.")

Şekildeki $ABCD$ paralelkenarında $|AD| = 5$ ve $|AB| = 12$ birimdir. $\widehat{A}$ ve $\widehat{B}$'nin açıortayları $[DC]$'yi sırasıyla $K$ ve $L$ noktalarında kesiyor. Buna göre $|KL|$ kaç birimdir?

A) 2
B) 5
C) 6
D) 7
E) 10

**Cevap:** A
**Çözüm:** $A$'nın açıortayı $ADK$ ikizkenar üçgenini oluşturur: $|DK| = |AD| = 5$. $B$'nin açıortayı $BCL$ ikizkenar üçgenini oluşturur: $|LC| = |BC| = 5$. $|KL| = 12 - 5 - 5 = 2$. $7$, yalnızca bir parçayı çıkarmaktır ($12 - 5$); $10$, iki parçanın toplamıdır; $6$, $|AB|$'nin yarısıdır; bu, Kural 6'daki $|EF|$ bağıntısını yanlış yerde kullanmaktır.

## Özet kartı

- Karşılıklı kenarlar eşit ve paralel; çevre $2(a + b)$.
- Karşılıklı açılar eşit, ardışık açılar bütünler ($180^\circ$).
- Köşegenler birbirini ortalar ama genelde eşit değildir.
- Köşegene dikmeler: $|DE| = |BF|$ ve $|AE| = |FC|$ (eş üçgenler).
- Açıortay paralel kenarla ikizkenar üçgen yapar: $|DK| = |AD|$.
- Komşu açıortaylar diktir; $|EF| = |AF| = |FB| = \dfrac{|AB|}{2}$. $[DC]$ üzerinde buluşurlarsa $|AB| = 2|AD|$.

## Sonraki adım

Alıştırmaya geç (aşağıdaki düğme). Sonraki ders: **Eşkenar Dörtgen**. Eşkenar dörtgen, dört kenarı eşit bir paralelkenardır; bugünkü bütün kurallar orada da geçerlidir, üstüne köşegenlerin dik kesişmesi ve açıortay olması eklenir.
