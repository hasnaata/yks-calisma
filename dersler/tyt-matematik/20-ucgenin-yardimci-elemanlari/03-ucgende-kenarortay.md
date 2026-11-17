---
baslik: Üçgende Kenarortay
ders: tyt-matematik
sure: 20 dk
kaynak: MEBİ Konu Özeti 481bc8bb71
guncelleme: 2026-11-18
---
# Üçgende Kenarortay

**Bu dersin sonunda:** ağırlık merkezinin kenarortayı $2:1$ böldüğünü, orta tabanla birlikte $3:1:2$ oranını ve dik üçgende hipotenüse ait kenarortayın hipotenüsün yarısı olduğunu kullanarak bir uzunluğu ya da açıyı tek adımda bulabileceksin.

> **TYT'de yeri:** Geometride "$G$ ağırlık merkezidir, $|AG| = ?$" kalıbı sık gelir. Çoğu soru iki bilgiden birini ister: ağırlık merkezi kenarortayı köşeden itibaren $2:1$ böler, dik üçgende hipotenüse çizilen kenarortay hipotenüsün yarısıdır. İkincisi çoğu zaman bir ikizkenar üçgen ve bir açı sorusuna dönüşür.

## Önce hatırla

<details><summary>Geçen dersten: ABC üçgeninde [AD] iç açıortaydır (D, [BC] üzerinde). |AB| = 6, |AC| = 9 ve |BC| = 10 ise |BD| kaçtır?</summary>
İç açıortay teoremi: |BD| / |DC| = |AB| / |AC| = 6 / 9 = 2 / 3. 10 birimi 2 : 3 oranında böl: <b>|BD| = 4</b>, |DC| = 6. Açıortay karşı kenarı komşu kenarların oranında böler; bugünkü kenarortay ise karşı kenarı her zaman tam ortadan (1 : 1) böler.
</details>

<details><summary>Geçen dersten: ABC üçgeninde |AB| = 4, |AC| = 6, |BC| = 5. A köşesindeki dış açıortay, [BC]'nin B tarafındaki uzantısını D'de kesiyor. |DB| kaçtır?</summary>
Dış açıortay teoremi: |DB| / |DC| = |AB| / |AC| = 4 / 6. |DB| = x dersen |DC| = x + 5 olur: x / (x + 5) = 2 / 3, yani 3x = 2x + 10 ve <b>|DB| = 10</b>. Bugün de bir doğru parçasını verilen oranda bölüp parçaları bulacaksın.
</details>

## Kenarortay ve ağırlık merkezi

Bir köşeyi karşı kenarın **orta noktasına** birleştiren doğru parçasına **kenarortay** denir. $A$ köşesinden çizilen kenarortayın uzunluğu $V_a$ ile gösterilir; $V_b$ ve $V_c$ de aynı biçimde.

Bir üçgenin üç kenarortayı her zaman üçgenin içinde **tek bir noktada** kesişir. Bu noktaya **ağırlık merkezi** denir ve genellikle $G$ ile gösterilir. Karton bir üçgeni bir kalemin ucunda dengede tutabileceğin nokta budur.

![ABC üçgeni. A'dan BC'nin orta noktası D'ye mavi, B'den AC'nin orta noktası E'ye yeşil, C'den AB'nin orta noktası F'ye kırmızı kenarortay çizilmiş. Üçü G noktasında kesişiyor. Kenarların eş parçaları birer, ikişer ve üçer çentikle işaretli.](gorsel/tyt-matematik/20-03-agirlik-merkezi.svg "Aynı sayıda çentikli parçalar eşittir: D, E ve F orta noktalardır. Üç kenarortay G noktasında kesişir.")

> **Dikkat:** Kenarortay, karşı kenarı ortalar ama açıyı ikiye bölmez, kenara dik de değildir. Bu üçü (kenarortay, açıortay, yükseklik) yalnızca ikizkenar üçgende tepe köşesinden çizilince çakışır.

## 1. Ağırlık merkezi kenarortayı 2 : 1 böler

**Örnek.** $G$, $ABC$ üçgeninin ağırlık merkezidir. $[AD]$ ve $[BE]$ kenarortaydır. $|AD| = 12$ ve $|GE| = 3$ ise $|AG|$, $|GD|$ ve $|BE|$ kaçtır?

**Çözüm.**

1. $G$, $[AD]$'yi köşe tarafı iki pay, kenar tarafı bir pay olacak biçimde böler. $12$'yi $2 + 1 = 3$ paya böl: bir pay $4$.
2. $|AG| = 2 \cdot 4 = 8$, $|GD| = 4$.
3. $[BE]$ üzerinde $|GE| = 3$ bir paydır. $|BG| = 2 \cdot 3 = 6$, $|BE| = 6 + 3 = 9$.

![ABC üçgeninde mavi AD ve yeşil BE kenarortayları G'de kesişiyor. AG 8, GD 4, BG 6, GE 3 olarak yazılmış. C'den çizilen üçüncü kenarortay kesikli ve soluk.](gorsel/tyt-matematik/20-03-iki-kat.svg "Her kenarortayda köşe ile G arası, G ile kenar arasının iki katıdır: 8 = 2 · 4 ve 6 = 2 · 3.")

**Kural:**

$$|AG| = 2\,|GD| \qquad |AG| = \frac{2}{3}V_a \qquad |GD| = \frac{1}{3}V_a$$

Aynı kural $[BE]$ ve $[CF]$ için de geçerlidir. Uzunluklar $x$ ile verilirse ($|AG| = 3x - 1$, $|GD| = x + 1$ gibi) denklem $|AG| = 2\,|GD|$ olur: $3x - 1 = 2x + 2$, $x = 3$, $|AD| = 8 + 4 = 12$.

> **Tuzak:** İki katı olan, **köşe tarafıdır**. $|GD| = 2\,|AG|$ yazmak ya da $G$'yi kenarortayın orta noktası sanmak en sık yapılan hatadır.

## 2. Orta taban ile birlikte: 3 : 1 : 2

$D$ ve $E$, $[AB]$ ile $[AC]$'nin orta noktaları olsun. $[DE]$'ye **orta taban** denir; $[BC]$'ye paraleldir ve onun yarısı kadardır. Orta taban, $A$'dan çizilen $[AF]$ kenarortayını da tam ortadan keser.

**Örnek.** Şekilde $D$, $E$, $F$ kenarların orta noktaları, $G$ ağırlık merkezi, $P$ ise $[DE]$ ile $[AF]$'nin kesişim noktasıdır. $|AF| = 12$ ise $|AP|$, $|PG|$ ve $|GF|$ kaçtır?

![ABC üçgeninde AB'nin orta noktası D, AC'nin orta noktası E; sarı DE orta tabanı. A'dan BC'nin orta noktası F'ye mavi kenarortay çizilmiş. DE, AF'yi P'de kesiyor; G ağırlık merkezi P'nin altında. AP 6, PG 2, GF 4 yazılmış. B'den E'ye kesikli kenarortay G'den geçiyor.](gorsel/tyt-matematik/20-03-orta-taban.svg "Mavi kenarortay yukarıdan aşağı 6, 2 ve 4 parçalarına ayrılır: oran 3 : 1 : 2.")

**Çözüm.**

1. Orta taban $[AF]$'yi ortalar: $|AP| = \dfrac{12}{2} = 6$.
2. Ağırlık merkezi kuralı: $|AG| = \dfrac{2}{3} \cdot 12 = 8$, $|GF| = 4$.
3. $|PG| = |AG| - |AP| = 8 - 6 = 2$.

**Kural:** Köşeden kenara doğru

$$|AP| : |PG| : |GF| = 3 : 1 : 2 \qquad (3k,\ k,\ 2k;\ \ |AF| = 6k)$$

> **Tuzak:** $P$ ile $G$ farklı noktalardır. $P$ orta taban üzerindedir; $G$ ise $P$ ile $F$ arasında, $P$'den biraz aşağıdadır. Sıralama köşeden başlar: $3$, $1$, $2$. $|PG|$ verilip $|AF|$ sorulduğunda $|AF| = 6 \cdot |PG|$ olur.

## 3. Dik üçgende hipotenüse ait kenarortay

**Örnek.** $ABC$ üçgeninde $m(\widehat{B}) = 90^\circ$, $|AB| = 6$, $|BC| = 8$'dir. $E$, $[AC]$'nin orta noktası ise $|BE|$ kaçtır?

**Çözüm.**

1. Pisagor: $|AC| = \sqrt{6^2 + 8^2} = 10$.
2. Hipotenüse ait kenarortay hipotenüsün yarısıdır: $|BE| = \dfrac{10}{2} = 5$.

![B köşesi dik olan ABC üçgeni; AB 6, BC 8. Hipotenüs AC'nin orta noktası E; B'den E'ye yeşil kenarortay. AE, EC ve BE parçalarının her biri 5 ve birer çentikle işaretli.](gorsel/tyt-matematik/20-03-dik-ucgen.svg "E noktası üç köşeye de eşit uzaklıktadır: AE = EC = BE = 5. Bu yüzden EAB ve EBC üçgenleri ikizkenardır.")

**Kural:** $m(\widehat{B}) = 90^\circ$ ve $E$, hipotenüsün orta noktası ise

$$|BE| = |AE| = |EC| = \frac{|AC|}{2}$$

**Açıya etkisi:** $|EB| = |EC|$ olduğu için $EBC$ ikizkenardır: $m(\widehat{EBC}) = m(\widehat{C})$. Aynı biçimde $m(\widehat{EBA}) = m(\widehat{A})$. Örneğin $m(\widehat{C}) = 30^\circ$ ise $m(\widehat{EBC}) = 30^\circ$ ve $m(\widehat{ABE}) = 60^\circ$.

**Tersi de doğrudur:** Bir üçgende bir kenara ait kenarortay o kenarın yarısına eşitse, o kenarın karşısındaki açı $90^\circ$'dir. ($|DA| = |DB| = |DC|$ ise iki ikizkenar üçgenin taban açıları toplanır: $2\alpha + 2\beta = 180^\circ$, yani $\alpha + \beta = 90^\circ$.)

> **Tuzak:** Kural yalnızca **hipotenüse** çizilen kenarortay içindir. Dik kenara çizilen kenarortay o kenarın yarısı değildir. Hipotenüse ait **yükseklik** ile de karıştırma: $6$–$8$–$10$ üçgeninde kenarortay $5$, yükseklik $\dfrac{6 \cdot 8}{10} = 4{,}8$'dir.

## ÖSYM tuzakları

> **$G$'yi orta nokta sanmak.** $|AD| = 12$ ise $|AG| = 6$ değil, $8$'dir. Seçeneklerde $6$ hazır bekler.

> **Oranı ters kurmak.** $|GD| = 5$ verildiyse $|AG| = 10$, $|AD| = 15$'tir. $|AG| = 2{,}5$ bulduysan oranı ters çevirmişsindir.

> **Kenarortayı kenarla karıştırmak.** $|AG| = \dfrac{2}{3}V_a$'dır, $\dfrac{2}{3}|BC|$ değil. Ama $m(\widehat{A}) = 90^\circ$ ise hipotenüse çizilen kenarortay $\dfrac{|BC|}{2}$ olduğu için bu durumda $|AG| = \dfrac{|BC|}{3}$ olur.

> **$P$ ile $G$'yi karıştırmak.** Orta taban kenarortayı ortalar ($P$); ağırlık merkezi ($G$) $P$'nin altındadır. $3 : 1 : 2$ sırası köşeden başlar.

> **Dik açı ipucunu görmemek.** "Dik üçgende hipotenüsün orta noktası" gördüğünde hemen eşit üç parça ve iki ikizkenar üçgen ara; açı sorusu çoğu zaman tek adımda biter.

## Kendini dene

### Soru 1
$G$, $ABC$ üçgeninin ağırlık merkezidir ve $[BE]$ bir kenarortaydır. $|BE| = 15$ ise $|GE|$ kaçtır?

A) 5
B) 7,5
C) 10
D) 15
E) 30

**Cevap:** A
**Çözüm:** $G$, $[BE]$'yi $2 : 1$ böler: $15$'i $3$ paya böl, bir pay $5$. $|BG| = 10$, $|GE| = 5$. $7{,}5$, $G$'yi orta nokta sanmaktır; $10$ ise $|BG|$'dir.

### Soru 2
$ABC$ üçgeninde $m(\widehat{A}) = 90^\circ$, $|AB| = 5$, $|AC| = 12$'dir. $[AD]$, $[BC]$ kenarına ait kenarortay ise $|AD|$ kaçtır?

A) 6
B) 6,5
C) 8,5
D) 12
E) 13

**Cevap:** B
**Çözüm:** $|BC| = \sqrt{5^2 + 12^2} = 13$. $[AD]$ hipotenüse ait kenarortaydır: $|AD| = \dfrac{13}{2} = 6{,}5$. $6$, dik kenar $12$'nin yarısıdır; $13$ hipotenüsün kendisi, $8{,}5$ ise dik kenarların ortalamasıdır.

### Soru 3
$ABC$ üçgeninde $D$ ve $E$ sırasıyla $[AB]$ ve $[AC]$'nin orta noktaları, $[AF]$ ise $[BC]$'ye ait kenarortaydır. $[DE]$ ile $[AF]$, $P$ noktasında kesişiyor ve $G$, üçgenin ağırlık merkezidir. $|AP| = 9$ ise $|GF|$ kaçtır?

A) 3
B) 4,5
C) 6
D) 9
E) 12

**Cevap:** C
**Çözüm:** Köşeden itibaren $|AP| : |PG| : |GF| = 3 : 1 : 2$. $3k = 9 \Rightarrow k = 3$, $|GF| = 2k = 6$. Kontrol: $|AF| = 6k = 18$, $|AG| = \dfrac{2}{3} \cdot 18 = 12$, $|GF| = 18 - 12 = 6$. $3$, $|PG|$'dir; $12$ ise $|AG|$'dir.

## Özet kartı

- Kenarortay, köşeyi karşı kenarın orta noktasına birleştirir. Üç kenarortay ağırlık merkezi $G$'de kesişir.
- $G$, kenarortayı köşeden itibaren $2 : 1$ böler: $|AG| = \dfrac{2}{3}V_a$, $|GD| = \dfrac{1}{3}V_a$.
- Orta taban ile: $|AP| : |PG| : |GF| = 3 : 1 : 2$.
- Dik üçgende hipotenüse ait kenarortay $=$ hipotenüsün yarısı; orta nokta üç köşeye eşit uzaklıktadır.
- Bu durumda $m(\widehat{EBC}) = m(\widehat{C})$: iki ikizkenar üçgen oluşur.
- Tersi: kenarortay, ait olduğu kenarın yarısıysa karşıdaki açı $90^\circ$'dir.

## Sonraki adım

Alıştırmaya geç (aşağıdaki düğme). Sonraki ders: **Üçgende Yükseklik**. Orada köşeden karşı kenara dik inen doğru parçasını ve bugünkü kenarortayla farkını göreceksin.
