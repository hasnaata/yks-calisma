---
baslik: Çokgenler
ders: tyt-matematik
sure: 20 dk
kaynak: MEBİ Konu Özeti d29c2bb071
guncelleme: 2026-11-18
---
# Çokgenler

<div class="giris" dir="rtl" lang="ar">

**الدرس ده عن إيه؟** عن المضلعات (çokgenler): الشكل اللي ليه ٥ أو ٦ أو ١٠ أضلاع، وإزاي تحسب أقطاره وزواياه من غير ما ترسمه كله.

- هتعرف تعد الأقطار (köşegenler) من رأس واحدة ومن كل الرؤوس، وتقسم المضلع لمثلثات.
- هتتعلم مجموع الزوايا الداخلية (iç açılar toplamı)، وإن مجموع الزوايا الخارجية (dış açılar toplamı) دايمًا ٣٦٠ درجة مهما كان عدد الأضلاع.
- هتحسب زاوية المضلع المنتظم (düzgün çokgen)، وتعرف عدد أضلاعه من زاوية واحدة بس.

**ليه مهم؟** في TYT بييجي سؤال عن البلاط أو روبوت بيلف أو مضلع منتظم جنبه مربع، وكله بيتحل بالقواعد دي في سطرين.

الدرس ٢٠ دقيقة، وكل قاعدة معاها رسمة ومثال محلول. امسك القلم وارسم معانا.

</div>

**Bu dersin sonunda:** kenar sayısı verilen bir çokgenin köşegen sayısını ve açılar toplamını, düzgün bir çokgende de tek bir açıdan kenar sayısını en çok iki adımda bulabileceksin.

> **TYT'de yeri:** Geometri bölümünde çoğu yıl bir çokgen sorusu çıkar. Genelde düzgün beşgen, altıgen ya da sekizgen verilir; yanına bir kare ya da eşkenar üçgen eklenir ve bir açı sorulur. Yeni nesil sorularda aynı bilgi "her köşede dönen robot" ya da "boşluksuz döşenen fayans" olarak gelir.

## Önce hatırla

<details><summary>Geçen dersten: ABC üçgeninde D noktası [BC] üzerinde; |BD| = 3 cm, |DC| = 5 cm ve A(ABD) = 12 cm². A(ADC) kaç cm²'dir?</summary>
İki üçgenin yüksekliği aynıdır ($A$'dan $[BC]$'ye inen dikme). Yükseklikler eşitse alanlar tabanlarla orantılıdır: $\dfrac{12}{A(ADC)} = \dfrac{3}{5} \Rightarrow A(ADC) = 20$ cm². Bugün de çokgenleri köşegenlerle üçgenlere böleceksin.
</details>

<details><summary>Geçen dersten: ABC üçgeninin kenarortayları G noktasında kesişiyor ve A(ABC) = 48 cm². A(GBC) kaç cm²'dir?</summary>
Kenarortaylar üçgeni alanları eşit altı parçaya böler; her parça $48 : 6 = 8$ cm². $GBC$ üçgeni bu parçalardan ikisidir: <b>16 cm²</b>.
</details>

## Çokgen, köşe, kenar, köşegen

Düzlemde herhangi üçü aynı doğru üzerinde olmayan $n$ tane noktayı ($n \ge 3$) sırayla doğru parçalarıyla birleştirip son noktayı ilkine bağlayınca kapalı bir şekil oluşur: **çokgen**. Noktalar **köşe**, doğru parçaları **kenar**dır. Köşe sayısı kenar sayısına eşittir; çokgen bu sayıyla adlandırılır: üçgen, dörtgen, beşgen, altıgen, sekizgen, ongen, onikigen.

Komşu olmayan iki köşeyi birleştiren doğru parçasına **köşegen** denir. Bu derste çokgen dediğimizde bütün iç açıları $180^\circ$'den küçük olan **dışbükey** çokgeni kastediyoruz; TYT soruları da böyledir.

## 1. Köşegen sayısı

**Örnek 1.** $ABCDEF$ altıgeninde (a) $A$ köşesinden kaç köşegen çizilir? (b) Altıgenin toplam kaç köşegeni vardır?

![ABCDEF altıgeni. A köşesinden C, D ve E'ye giden üç köşegen kalın mavi; diğer altı köşegen gri kesikli çizgi.](gorsel/tyt-matematik/23-01-kosegenler.svg "Mavi: A'dan çıkan 3 köşegen. A, kendisine ve iki komşusuna (B ve F) köşegen çizemez. Gri: geri kalan 6 köşegen; toplam 9.")

**Çözüm.**

1. (a) $A$, altı köşeden üçüne köşegen çizemez: **kendisine** ve iki **komşusuna** ($B$ ile $F$; onlarla arasında zaten kenar var). Kalan köşeler $C$, $D$, $E$: $6 - 3 = 3$ köşegen.
2. (b) Her köşeden $3$ köşegen çıkar: $6 \cdot 3 = 18$. Ama her köşegen iki ucundan birer kez sayıldı ($[AC]$ hem $A$'dan hem $C$'den). Gerçek sayı $\dfrac{18}{2} = 9$.

**Kural:** $n$ kenarlı bir çokgende

$$\text{bir köşeden çizilen köşegen sayısı} = n - 3 \qquad \text{toplam köşegen sayısı} = \frac{n(n-3)}{2}$$

> **Tuzak:** İkiye bölmeyi unutursan sonuç tam iki katı çıkar ($18$) ve seçeneklerde hazır bekler. Bir de "herhangi iki köşeyi birleştiren doğru parçası" sayısı $\dfrac{n(n-1)}{2}$'dir; bu sayı kenarları da içerir. Altıgende $15 = 9$ köşegen $+ \, 6$ kenar.

## 2. İç açılar toplamı

Bir köşeden çizilen $n - 3$ köşegen, çokgeni $n - 2$ üçgene böler. Her üçgenin açıları toplamı $180^\circ$ olduğundan çokgenin iç açıları toplamı $(n - 2) \cdot 180^\circ$ olur.

**Örnek 2.** $ABCDE$ beşgeninde $m(\widehat{A}) = 100^\circ$, $m(\widehat{B}) = 120^\circ$, $m(\widehat{C}) = 95^\circ$, $m(\widehat{D}) = 110^\circ$ ve $m(\widehat{E}) = x$'tir. $x$ kaç derecedir?

![ABCDE beşgeni. A'dan C'ye ve D'ye kesikli köşegenler çizilmiş; beşgen 1, 2, 3 numaralı üç üçgene ayrılmış. Açılar: A 100, B 120, C 95, D 110 derece, E'deki açı x.](gorsel/tyt-matematik/23-01-ic-acilar.svg "A'dan çıkan 2 köşegen beşgeni 3 üçgene böler. Üç üçgenin bütün açıları, beşgenin iç açılarını tam olarak oluşturur: 3 · 180° = 540°.")

**Çözüm.**

1. Beşgende $n = 5$: iç açılar toplamı $(5 - 2) \cdot 180^\circ = 540^\circ$.
2. $x = 540^\circ - (100^\circ + 120^\circ + 95^\circ + 110^\circ) = 540^\circ - 425^\circ = 115^\circ$.

**Kural:**

$$\text{iç açılar toplamı} = (n - 2) \cdot 180^\circ$$

Dörtgen $360^\circ$, beşgen $540^\circ$, altıgen $720^\circ$, sekizgen $1080^\circ$. Kenar sayısı bir artınca toplam $180^\circ$ artar.

> **Tuzak:** $(n - 2)$ yerine $n$ ile çarpmak ($5 \cdot 180^\circ = 900^\circ$) ya da $n - 3$ ile çarpmak. Hatırlamanın yolu: üçgende $n = 3$, toplam $180^\circ$ olmalı, yani $(3 - 2) \cdot 180^\circ$.

## 3. Dış açılar toplamı: her zaman 360°

Bir köşede, bir kenarın uzantısı ile komşu kenar arasında kalan açı **dış açı**dır. Aynı köşedeki iç açı ile dış açı yan yanadır: toplamları $180^\circ$.

**Örnek 3.** Beşgen biçimli bir parkın kenarında yürüyen biri, köşelerin dördünde sırayla $70^\circ$, $80^\circ$, $65^\circ$ ve $75^\circ$ sola dönüyor. Beşinci köşede kaç derece dönerse başladığı yöne bakar? O köşedeki iç açı kaçtır?

![Beşgen. Her kenar bir sonraki köşenin ötesine kesikli çizgiyle uzatılmış; köşelerdeki kırmızı dış açılar 70, 80, 65, 75 derece ve x.](gorsel/tyt-matematik/23-01-dis-acilar.svg "Her kırmızı açı, o köşede yürüyenin döndüğü açıdır. Parkı bir kez dolaşınca toplam bir tam tur (360°) dönülür.")

**Çözüm.**

1. Parkı bir kez dolaşıp başlangıçtaki yönüne dönen kişi tam bir tur dönmüştür: dönüşlerin toplamı $360^\circ$.
2. $x = 360^\circ - (70^\circ + 80^\circ + 65^\circ + 75^\circ) = 360^\circ - 290^\circ = 70^\circ$.
3. O köşedeki iç açı $180^\circ - 70^\circ = 110^\circ$.

Kontrol: iç açılar $110^\circ$, $100^\circ$, $115^\circ$, $105^\circ$, $110^\circ$; toplam $540^\circ$.

**Kural:** Her köşeden birer dış açı alınırsa

$$\text{dış açılar toplamı} = 360^\circ \quad (n \text{ ne olursa olsun})$$

> **Tuzak:** Dış açılar toplamı kenar sayısıyla büyümez; üçgende de yirmigende de $360^\circ$'dir. Soru dış açı verip iç açı sorabilir ya da tersini yapabilir: her köşede ikisinin toplamı $180^\circ$.

## 4. Düzgün çokgenler

Bütün kenarları eşit **ve** bütün açıları eşit olan çokgene **düzgün çokgen** denir. Düzgün üçgen eşkenar üçgen, düzgün dörtgen karedir; ötekiler "düzgün beşgen", "düzgün altıgen" diye adlandırılır.

**Örnek 4.** (a) Düzgün sekizgenin bir iç açısı kaç derecedir? (b) Bir iç açısı $140^\circ$ olan düzgün çokgen kaç kenarlıdır?

![Yan yana düzgün beşgen ve düzgün altıgen; kenarlarda eşitlik çentikleri. Beşgenin sağ alt köşesinde mavi 108 ve kırmızı 72 derece, altıgenin sağ alt köşesinde mavi 120 ve kırmızı 60 derece işaretli; alt kenarlar kesikli çizgiyle uzatılmış.](gorsel/tyt-matematik/23-01-duzgun.svg "Her köşede mavi iç açı ile kırmızı dış açı birlikte 180° eder. Düzgün çokgende bütün dış açılar eşit olduğu için önce dış açıyı bul: 360° : n.")

**Çözüm.**

1. (a) Önce dış açı: $\dfrac{360^\circ}{8} = 45^\circ$. İç açı $180^\circ - 45^\circ = 135^\circ$. (Uzun yol: $\dfrac{6 \cdot 180^\circ}{8} = 135^\circ$.)
2. (b) Dış açı $180^\circ - 140^\circ = 40^\circ$. Bütün dış açılar eşit ve toplamları $360^\circ$: $n = \dfrac{360^\circ}{40^\circ} = 9$.

**Kural:** $n$ kenarlı düzgün çokgende

$$\text{bir dış açı} = \frac{360^\circ}{n} \qquad \text{bir iç açı} = \frac{(n-2) \cdot 180^\circ}{n} = 180^\circ - \frac{360^\circ}{n}$$

| Düzgün çokgen | $n$ | Bir dış açı | Bir iç açı |
|---|---|---|---|
| Eşkenar üçgen | 3 | $120^\circ$ | $60^\circ$ |
| Kare | 4 | $90^\circ$ | $90^\circ$ |
| Düzgün beşgen | 5 | $72^\circ$ | $108^\circ$ |
| Düzgün altıgen | 6 | $60^\circ$ | $120^\circ$ |
| Düzgün sekizgen | 8 | $45^\circ$ | $135^\circ$ |

> **Tuzak:** Kenar sayısını bulmak için iç açıyla denklem kurmak yerine **dış açıdan** git: $n = \dfrac{360^\circ}{\text{dış açı}}$. Bir de: yalnızca kenarları eşit olan şekil düzgün değildir. Eşkenar dörtgenin kenarları eşittir ama açıları eşit değildir; dikdörtgenin açıları eşittir ama kenarları eşit değildir.

## 5. Düzgün çokgende köşegen: ikizkenar üçgen

**Örnek 5.** $ABCDEF$ düzgün altıgeninde $[AC]$ köşegeni çiziliyor. $m(\widehat{BAC})$ ve $m(\widehat{ACD})$ kaç derecedir?

![ABCDEF düzgün altıgeni, kenarlarda eşitlik çentikleri. Kırmızı AC köşegeni. ABC üçgeni sarı: B'de 120, A'da ve C'de 30 derece. C'de AC ile CD arasında dik açı işareti, 90 derece.](gorsel/tyt-matematik/23-01-altigen.svg "AB ve BC eşit kenarlardır, bu yüzden ABC ikizkenar üçgendir. C'deki 120°'lik iç açı, köşegenle 30° ve 90° olarak ikiye ayrılır.")

**Çözüm.**

1. $|AB| = |BC|$ (düzgün çokgenin kenarları), yani $ABC$ ikizkenar üçgen. Tepe açısı $m(\widehat{B}) = 120^\circ$.
2. Taban açıları eşit: $m(\widehat{BAC}) = m(\widehat{BCA}) = \dfrac{180^\circ - 120^\circ}{2} = 30^\circ$.
3. $C$'deki iç açı $120^\circ$: $m(\widehat{ACD}) = 120^\circ - 30^\circ = 90^\circ$.

**Kural:** Düzgün çokgende iki komşu kenar ve uçlarını birleştiren köşegen ikizkenar üçgen oluşturur. Bu üçgenin taban açıları **dış açının yarısıdır**: $\dfrac{180^\circ - \text{iç açı}}{2} = \dfrac{\text{dış açı}}{2}$. Düzgün beşgende $36^\circ$, düzgün altıgende $30^\circ$.

> **Tuzak:** Köşegen, çizildiği köşedeki iç açıyı ikiye böler; sorulan parçanın hangisi olduğuna bak. Düzgün altıgende $m(\widehat{BCA}) = 30^\circ$, ama $m(\widehat{ACD}) = 90^\circ$.

## ÖSYM tuzakları

> **Köşegen sayısında ikiye bölmemek.** Her köşegen iki köşeden sayılır. Sekizgende $8 \cdot 5 = 40$ değil, $\dfrac{40}{2} = 20$ köşegen vardır.

> **Dış açılar toplamını kenar sayısına bağlamak.** Dış açılar toplamı her dışbükey çokgende $360^\circ$'dir. $(n - 2) \cdot 180^\circ$ yalnızca iç açılar içindir.

> **İç açıyı dış açı yerine kullanmak.** "Robot her köşede $30^\circ$ dönüyor" ifadesindeki $30^\circ$ dış açıdır; iç açı $150^\circ$'dir. Kenar sayısı $\dfrac{360^\circ}{30^\circ} = 12$.

> **Bir noktada birleşen parçalar.** Fayanslar bir köşede boşluksuz birleşiyorsa o noktadaki **iç açıların** toplamı $360^\circ$'dir. Kare ($90^\circ$) ile iki düzgün sekizgen ($135^\circ + 135^\circ$) bu yüzden tam oturur.

> **Seçenekte ara değer.** Soru açı istiyorsa önce bulduğun $n$'de durma; soru $n$ istiyorsa dış açıda durma.

## Kendini dene

### Soru 1
İç açılarının ölçüleri toplamı $1260^\circ$ olan bir çokgenin bir köşesinden kaç köşegen çizilebilir?

A) 4
B) 6
C) 7
D) 9
E) 27

**Cevap:** B
**Çözüm:** $(n - 2) \cdot 180^\circ = 1260^\circ \Rightarrow n - 2 = 7 \Rightarrow n = 9$. Bir köşeden $n - 3 = 6$ köşegen çizilir. $7$, $n - 2$'de durmak; $9$, kenar sayısının kendisi; $27$ ise toplam köşegen sayısıdır ($\frac{9 \cdot 6}{2}$).

### Soru 2
Bir beşgenin dış açılarının ölçüleri $2$, $3$, $3$, $4$ ve $6$ sayılarıyla orantılıdır. Bu beşgenin en küçük iç açısı kaç derecedir?

A) 20
B) 40
C) 60
D) 100
E) 140

**Cevap:** C
**Çözüm:** Dış açılar toplamı $360^\circ$: $2k + 3k + 3k + 4k + 6k = 18k = 360^\circ \Rightarrow k = 20^\circ$. Dış açılar $40^\circ$, $60^\circ$, $60^\circ$, $80^\circ$, $120^\circ$; iç açılar $140^\circ$, $120^\circ$, $120^\circ$, $100^\circ$, $60^\circ$. En küçük iç açı, en büyük dış açının ($120^\circ$) yanındadır: $60^\circ$. $40^\circ$ en küçük dış açı, $140^\circ$ ise en büyük iç açıdır.

### Soru 3
Bir düzgün çokgenin bir iç açısının ölçüsü, bir dış açısının ölçüsünün $5$ katıdır. Bu çokgenin köşegen sayısı kaçtır?

A) 9
B) 12
C) 27
D) 54
E) 108

**Cevap:** D
**Çözüm:** Dış açı $d$ ise iç açı $5d$; aynı köşede toplamları $180^\circ$: $6d = 180^\circ \Rightarrow d = 30^\circ$. $n = \dfrac{360^\circ}{30^\circ} = 12$. Köşegen sayısı $\dfrac{12 \cdot 9}{2} = 54$. $12$ kenar sayısında durmak, $108$ ikiye bölmeyi unutmak, $9$ ise bir köşeden çizilen köşegen sayısıdır.

## Özet kartı

- Bir köşeden $n - 3$ köşegen çizilir; bu köşegenler çokgeni $n - 2$ üçgene böler.
- Toplam köşegen sayısı $\dfrac{n(n-3)}{2}$: her köşegen iki kez sayıldığı için ikiye bölünür.
- İç açılar toplamı $(n - 2) \cdot 180^\circ$; dış açılar toplamı her zaman $360^\circ$.
- Her köşede iç açı + dış açı $= 180^\circ$.
- Düzgün çokgen: bir dış açı $\dfrac{360^\circ}{n}$; kenar sayısını dış açıdan bul. Beşgen $108^\circ$, altıgen $120^\circ$, sekizgen $135^\circ$.
- Düzgün çokgende iki komşu kenar + köşegen = ikizkenar üçgen; taban açıları dış açının yarısı.

## Sonraki adım

Alıştırmaya geç (aşağıdaki düğme). Sonraki ders: **Dörtgenler ve Özellikleri**. Orada bugünkü $360^\circ$ kuralını dörtgenlerde kullanacak, köşegenlerin dörtgeni nasıl böldüğünü göreceksin.
