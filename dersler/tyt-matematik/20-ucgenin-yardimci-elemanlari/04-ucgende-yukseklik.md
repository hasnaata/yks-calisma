---
baslik: Üçgende Yükseklik
ders: tyt-matematik
sure: 25 dk
kaynak: MEBİ Konu Özeti c7d83b5a70
guncelleme: 2026-11-17
---
# Üçgende Yükseklik

**Bu dersin sonunda:** yüksekliğin ayırdığı iki dik üçgende Pisagor'u kullanabilecek, "kenar × yükseklik" eşitliğiyle bilinmeyen yüksekliği bulabilecek, yüksekliklerin kesim noktasının nerede olduğunu üçgenin türünden söyleyebileceksin.

> **TYT'de yeri:** Yükseklik tek başına az sorulur ama geometri sorularının çoğunda bir adım olarak karşına çıkar: Pisagor için dik üçgen kurmak, alan hesaplamak, "bir noktanın bir doğruya en kısa uzaklığı" gibi günlük hayat soruları. Yeni nesil sorularda yükseklik çoğu zaman "en kısa yol" ya da "dik inen boru" diye gizlenir.

## Önce hatırla

<details><summary>Geçen dersten: ABC üçgeninde [AD] kenarortay, G ağırlık merkezi ve |AD| = 12 cm'dir. |AG| ve |GD| kaç cm'dir?</summary>
<b>|AG| = 8, |GD| = 4</b>. Ağırlık merkezi kenarortayı köşeden itibaren $2 : 1$ oranında böler. Bugün eşkenar üçgende yüksekliklerin de aynı noktada kesiştiğini göreceksin; bu oran orada yeniden işine yarayacak.
</details>

<details><summary>Geçen dersten: ABC dik üçgeninde m(B) = 90° ve |AC| = 10 cm'dir. B köşesinden hipotenüse çizilen kenarortay kaç cm'dir?</summary>
<b>5 cm</b>. Hipotenüse ait kenarortay hipotenüsün yarısıdır. Bugün aynı köşeden hipotenüse inen <b>yüksekliği</b> öğreneceksin; ikisi farklı doğru parçalarıdır ve seçeneklerde birbirinin yerine konur.
</details>

## 1. Yükseklik nedir?

Bir köşeden karşı kenara (ya da karşı kenarın uzantısına) **dik** inen doğru parçasına o kenara ait **yükseklik** denir. Dikmenin kenarı kestiği noktaya **dikme ayağı** denir. $A$'dan $[BC]$'ye inen yükseklik $h_a$ diye yazılır; benzer biçimde $h_b$, $h_c$.

**Örnek.** $ABC$ üçgeninde $[AH] \perp [BC]$, $|AB| = 13$, $|BH| = 5$ ve $|HC| = 9$'dur. $|AH|$ ve $|AC|$ kaçtır?

![ABC üçgeni: A'dan BC'ye dik inen kırmızı AH yüksekliği, H'de dik açı işareti. AB 13, AC 15, BH 5, HC 9 birim. Yüksekliğin solundaki ABH üçgeni mavi, sağındaki AHC üçgeni yeşil boyalı.](gorsel/tyt-matematik/20-04-yukseklik.svg "Yükseklik üçgeni iki dik üçgene ayırır: mavi ABH ve yeşil AHC. İkisinin ortak dik kenarı h_a'dır.")

**Çözüm.**

1. $ABH$ dik üçgeninde Pisagor: $|AH| = \sqrt{13^2 - 5^2} = \sqrt{144} = 12$.
2. $AHC$ dik üçgeninde Pisagor: $|AC| = \sqrt{12^2 + 9^2} = \sqrt{225} = 15$.

**Kural:** Yükseklik, üçgeni ortak bir dik kenarı olan iki dik üçgene ayırır. Bir taraftan yüksekliği bul, öbür tarafa taşı.

$$h_a^2 = |AB|^2 - |BH|^2 = |AC|^2 - |HC|^2$$

> **Tuzak:** $|AC|$ için $12 + 9 = 21$ yazmak. Dik üçgende hipotenüs, dik kenarların toplamı değildir; Pisagor gerekir.

## 2. Kenar × yükseklik sabittir

Alan $= \dfrac{\text{taban} \cdot \text{yükseklik}}{2}$. Üçgenin hangi kenarını taban seçersen seç alan aynıdır. Bu yüzden:

**Örnek.** Aynı üçgende $|BC| = 14$, $|AC| = 15$ ve $h_a = 12$. $B$'den $[AC]$'ye inen $h_b$ kaçtır?

![Aynı ABC üçgeni: mavi AH yüksekliği 12 birim, BC 14 birim. B'den AC'ye dik inen yeşil BE yüksekliği, E'de dik açı işareti ve h_b = ? etiketi. AC 15 birim.](gorsel/tyt-matematik/20-04-kenar-yukseklik.svg "Mavi yükseklik 14 birimlik tabana, yeşil yükseklik 15 birimlik tabana aittir. Taban uzadıkça ona ait yükseklik kısalır.")

**Çözüm.**

1. Alan, $[BC]$ taban olarak: $\dfrac{14 \cdot 12}{2} = 84$.
2. Aynı alan, $[AC]$ taban olarak: $\dfrac{15 \cdot h_b}{2} = 84 \Rightarrow h_b = \dfrac{168}{15} = 11{,}2$.

Kısaca: $14 \cdot 12 = 15 \cdot h_b$.

**Kural:**

$$a \cdot h_a = b \cdot h_b = c \cdot h_c = 2 \cdot \text{Alan}$$

- Yükseklik ile kenar **ters orantılıdır**: en uzun kenara ait yükseklik en kısa, en kısa kenara ait yükseklik en uzundur.
- Kenarlar $2 : 3 : 4$ ise yükseklikler $\dfrac{1}{2} : \dfrac{1}{3} : \dfrac{1}{4} = 6 : 4 : 3$ olur.

> **Tuzak:** Yüksekliği kenarla **doğru** orantılı sanmak. Yukarıdaki örnekte $h_b = 12 \cdot \dfrac{15}{14}$ yazarsan $12$'den büyük bir sayı bulursun; oysa daha uzun kenara daha kısa yükseklik düşer.

## 3. Yükseklik üçgenin dışına düşebilir

Geniş açılı üçgende, dar açılı köşeden inen dikme karşı kenarın **uzantısına** düşer.

**Örnek.** $ABC$ üçgeninde $\widehat{B}$ geniş açıdır. $A$'dan $[CB$ uzantısına inen dikmenin ayağı $H$'dir. $|AH| = 12$, $|AB| = 13$, $|BC| = 11$ ise $|AC|$ kaçtır?

![Geniş açılı ABC üçgeni mavi boyalı. CB kenarı B'nin ötesine kesikli çizgiyle uzatılmış; A'dan bu uzantıya dik inen kırmızı AH, 12 birim. AB 13, HB 5, BC 11 birim. AC kenarında soru işareti.](gorsel/tyt-matematik/20-04-genis.svg "H noktası üçgenin dışında, [CB]'nin uzantısındadır. AHC büyük dik üçgeninin yatay kenarı 5 + 11 = 16'dır.")

**Çözüm.**

1. $AHB$ dik üçgeninde: $|HB| = \sqrt{13^2 - 12^2} = 5$.
2. $H$, $B$, $C$ bu sırayla dizili: $|HC| = 5 + 11 = 16$.
3. $AHC$ dik üçgeninde: $|AC| = \sqrt{12^2 + 16^2} = \sqrt{400} = 20$.

Bu üçgenin alanı da yine taban × yükseklik / 2'dir: $\dfrac{11 \cdot 12}{2} = 66$. Yükseklik dışarıda olsa da $[BC]$'ye aittir.

**Kural:** Geniş açılı üçgende, geniş açının iki yanındaki köşelerden inen yükseklikler dışarı düşer. Dikme ayağının yerini belirle, sonra parçaları **topla**.

> **Tuzak:** $|HC| = 11 - 5 = 6$ yazmak. $H$ dışarıdayken $[HC]$, $[HB]$ ile $[BC]$'nin toplamıdır. Şekli çizmeden çıkarma ya da toplama yapma.

## 4. Diklik merkezi

Üçgenin üç yüksekliği (ya da uzantıları) tek bir noktada kesişir. Bu noktaya **diklik merkezi** denir; burada $K$ ile göstereceğiz.

**Örnek.** $ABC$ üçgeninde $m(\widehat{A}) = 90^\circ$. Yükseklikler nerede kesişir?

**Çözüm.** $[AB] \perp [AC]$ olduğu için $B$'den $[AC]$'ye inen dikme $[BA]$'nın kendisidir; $C$'den $[AB]$'ye inen dikme de $[CA]$'dır. Bu iki yükseklik $A$'da buluşur. Üçüncü yükseklik de $A$'dan çıkar. Diklik merkezi $A$ köşesidir.

![Yan yana üç üçgen. Dar açılı üçgende üç renkli yükseklik içeride K noktasında kesişiyor. Dik açılı üçgende iki yükseklik dik kenarların kendisi, K dik açılı A köşesinde. Geniş açılı üçgende yüksekliklerin uzantıları noktalı çizgilerle üçgenin dışında, A'nın üstündeki K noktasında buluşuyor.](gorsel/tyt-matematik/20-04-diklik-merkezi.svg "Aynı renk, aynı köşeden inen yüksekliktir. Geniş açılıda kesikli çizgiler kenar uzantıları, noktalı çizgiler yükseklik uzantılarıdır.")

**Kural:**

| Üçgen | Diklik merkezi $K$ |
|---|---|
| Dar açılı | Üçgenin **içinde** |
| Dik açılı | Dik açının bulunduğu **köşede** |
| Geniş açılı | Üçgenin **dışında**, geniş açının arkasında |

> **Tuzak:** Diklik merkezi ile ağırlık merkezini karıştırmak. Ağırlık merkezi kenarortayların kesim noktasıdır ve **her zaman** içeridedir; diklik merkezi dışarıda da olabilir.

## 5. İkizkenar ve eşkenar üçgende yükseklik

**Örnek 1.** $|AB| = |AC| = 10$ ve $|BC| = 12$ olan ikizkenar üçgende $A$'dan inen yükseklik kaçtır?

**Çözüm.** İkizkenar üçgende **tepe** köşesinden ($A$) inen yükseklik tabanı iki eş parçaya böler: $|BH| = |HC| = 6$. $ABH$ dik üçgeninde $|AH| = \sqrt{10^2 - 6^2} = 8$.

**Örnek 2.** Bir kenarı $6$ olan eşkenar üçgenin yüksekliği kaçtır? Yüksekliklerin kesim noktası $A$ köşesine ne kadar uzaktadır?

**Çözüm.**

1. Yükseklik tabanı ortadan böler: $|BF| = 3$. Pisagor: $h = \sqrt{6^2 - 3^2} = \sqrt{27} = 3\sqrt{3}$.
2. Eşkenar üçgende yükseklikler aynı zamanda kenarortaydır; kesim noktası $G$, ağırlık merkezidir. $|AG| = \dfrac{2}{3} \cdot 3\sqrt{3} = 2\sqrt{3}$, $|GF| = \sqrt{3}$.

![Solda ikizkenar ABC üçgeni: AB ve AC 10 birim, tek çentikli. Kırmızı AH yüksekliği 8 birim; BH ve HC 6'şar birim, çift çentikli; A'daki açı iki eş parçaya bölünmüş. Sağda kenarları 6 birim olan eşkenar üçgen: üç köşeden inen üç renkli yükseklik içerideki G noktasında kesişiyor.](gorsel/tyt-matematik/20-04-ikizkenar-eskenar.svg "İkizkenarda tepe köşesinden inen yükseklik hem tabanı hem tepe açısını ikiye böler. Eşkenarda üç yükseklik de eşittir ve ağırlık merkezinde kesişir.")

**Kural:**

- İkizkenar üçgende ($|AB| = |AC|$) $A$'dan inen $[AH]$ hem **yükseklik**, hem **kenarortay**, hem **açıortaydır**: $|BH| = |HC|$ ve $m(\widehat{BAH}) = m(\widehat{HAC})$.
- Eşkenar üçgende üç yükseklik eşittir; her biri aynı zamanda kenarortay ve açıortaydır. Bir kenarı $a$ ise

$$h = \frac{a\sqrt{3}}{2}$$

- Eşkenar üçgende diklik merkezi = ağırlık merkezi: köşeye uzaklık $\dfrac{2h}{3}$, kenara uzaklık $\dfrac{h}{3}$.

> **Tuzak:** İkizkenar üçgende "yükseklik = kenarortay" yalnızca **eşit kenarların birleştiği** köşeden inen yükseklik için doğrudur. $B$'den inen yükseklik $[AC]$'yi ortadan bölmez.

## ÖSYM tuzakları

> **Hipotenüse ait yükseklik ≠ hipotenüse ait kenarortay.** Dik kenarları $6$ ve $8$ olan dik üçgende hipotenüse ait kenarortay $5$, yükseklik ise $\dfrac{6 \cdot 8}{10} = 4{,}8$'dir. İkisi de seçeneklerde bulunur.

> **Dışarı düşen dikmede parçaları çıkarmak.** Dikme ayağı uzantıdaysa uzun dik kenar, iki parçanın **toplamıdır**.

> **Alanda taban ile yüksekliği karıştırmak.** Alan, bir kenar ile **o kenara ait** yüksekliğin çarpımının yarısıdır. $|AB|$ ile $h_a$'yı çarpmak yanlıştır.

> **Kenar–yükseklik oranını ters kurmak.** Kenarlar $2 : 3 : 4$ ise yükseklikler $4 : 3 : 2$ değil, $6 : 4 : 3$'tür. Oran kenarların **terslerinin** oranıdır.

> **Eşkenarda $\sqrt{3}$ ya da $2$'yi unutmak.** Kenarı $8$ olan eşkenar üçgenin yüksekliği $4\sqrt{3}$'tür; $8\sqrt{3}$ ve $4$ seçeneklerde bekler.

## Kendini dene

### Soru 1
$ABC$ üçgeninde $[AH] \perp [BC]$ ve $H$, $[BC]$ üzerindedir. $|AB| = 15$, $|AH| = 12$ ve $|HC| = 16$ ise $|BC|$ kaçtır?

A) 16
B) 20
C) 21
D) 25
E) 28

**Cevap:** D
**Çözüm:** $ABH$ dik üçgeninde $|BH| = \sqrt{15^2 - 12^2} = \sqrt{81} = 9$. $|BC| = 9 + 16 = 25$. $20$, $|AC| = \sqrt{12^2 + 16^2}$ değeridir; $28$ ise $12 + 16$ toplamıdır.

### Soru 2
Bir $ABC$ üçgeninde $|BC| = 12$, $|AC| = 9$ ve $A$'dan $[BC]$'ye inen yükseklik $6$'dır. $B$'den $[AC]$'ye inen yükseklik kaçtır?

A) 4,5
B) 6
C) 8
D) 9
E) 12

**Cevap:** C
**Çözüm:** $a \cdot h_a = b \cdot h_b$: $12 \cdot 6 = 9 \cdot h_b \Rightarrow h_b = 8$. Kontrol: daha kısa kenara ($9$) daha uzun yükseklik ($8 > 6$) düşer. $4{,}5$, oranı ters kurmaktır ($6 \cdot 9 / 12$).

### Soru 3
Eşkenar üçgen biçimindeki bir levhanın yüksekliklerinin kesim noktası, levhanın bir köşesine $4\sqrt{3}$ cm uzaklıktadır. Levhanın bir kenarı kaç cm'dir?

A) 8
B) 12
C) 16
D) 24
E) 36

**Cevap:** B
**Çözüm:** Eşkenar üçgende yüksekliklerin kesim noktası ağırlık merkezidir; köşeye uzaklığı yüksekliğin $\dfrac{2}{3}$'üdür: $h = \dfrac{3}{2} \cdot 4\sqrt{3} = 6\sqrt{3}$. $\dfrac{a\sqrt{3}}{2} = 6\sqrt{3} \Rightarrow a = 12$. $8$, $4\sqrt{3}$'ü yüksekliğin tamamı sanmaktır; $16$, yarısı sanmaktır; $36$ ise çevredir.

## Özet kartı

- Yükseklik, köşeden karşı kenara ya da uzantısına **dik** inen doğru parçasıdır; ayağına dikme ayağı denir.
- Yükseklik üçgeni iki dik üçgene ayırır: iki tarafta Pisagor, ortak kenar $h$.
- $a \cdot h_a = b \cdot h_b = c \cdot h_c = 2 \cdot \text{Alan}$; uzun kenara kısa yükseklik düşer.
- Diklik merkezi: dar açılıda içte, dik açılıda dik köşede, geniş açılıda dışta.
- İkizkenarda tepe köşesinden inen yükseklik = kenarortay = açıortay.
- Eşkenarda $h = \dfrac{a\sqrt{3}}{2}$; kesim noktası köşeye $\dfrac{2h}{3}$ uzaklıktadır.

## Sonraki adım

Alıştırmaya geç (aşağıdaki düğme). Sonraki ders: **Üçgende Kenar Orta Dikme**. Orada dikme bu kez köşeden değil, kenarın orta noktasından çıkacak; yükseklikle farkına dikkat et.
