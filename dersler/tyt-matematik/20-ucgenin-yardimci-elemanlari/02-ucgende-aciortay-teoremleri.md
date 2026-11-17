---
baslik: Üçgende Açıortay Teoremleri
ders: tyt-matematik
sure: 25 dk
kaynak: MEBİ Konu Özeti c28592a518
guncelleme: 2026-11-17
---
# Üçgende Açıortay Teoremleri

**Bu dersin sonunda:** iç ve dış açıortayın karşı kenarı hangi oranda böldüğünü kullanarak bilinmeyen uzunluğu bulabilecek, katlama sorularında katlama çizgisinin açıortay olduğunu görebilecek ve iç açıortayların kesim noktasıyla oluşan üçgenlerin alanlarını karşılaştırabileceksin.

> **TYT'de yeri:** Geometri bölümünde "$[AD]$ açıortay, $|BD| = ?$" kalıbı en sık gelen uzunluk sorularındandır. Yeni nesil sorularda aynı kural kâğıt katlama, arsa bölme ya da bahçe parselleme gibi bir durumun içine gizlenir. Kural tek satırdır; zor olan, açıortayı şekilde fark etmek ve oranı doğru eşleştirmektir.

## Önce hatırla

<details><summary>Geçen dersten: ABC üçgeninde [BD] ve [CD] iç açıortaydır ve m(A) = 50°'dir. m(BDC) kaç derecedir?</summary>
<b>115°</b>: $m(\widehat{BDC}) = 90^\circ + \dfrac{50^\circ}{2} = 115^\circ$. İki iç açıortayın kesiştiği $D$ noktası iç açıortayların ortak noktasıdır; bugünkü son bölümde bu noktanın kenarlara uzaklıklarını kullanacaksın.
</details>

<details><summary>Geçen dersten: P noktası bir açının açıortayı üzerindedir. P'nin açının bir koluna uzaklığı 4 cm ise öbür koluna uzaklığı kaç cm'dir?</summary>
<b>4 cm</b>. Açıortay üzerindeki her nokta, açının iki koluna eşit uzaklıktadır. Bugünkü iç açıortay teoremi doğrudan bu bilgiden çıkar.
</details>

## 1. İç açıortay teoremi

**Örnek.** $ABC$ üçgeninde $|AB| = 6$, $|AC| = 9$, $|BC| = 10$'dur. $[AD]$, $A$ açısının açıortayıdır ($D \in [BC]$). $|BD|$ ve $|DC|$ kaçtır?

![ABC üçgeni: AB 6, AC 9 birim. A'dan inen kırmızı AD açıortayı A açısını iki eş α açısına bölüyor ve BC'yi D'de kesiyor; BD 4, DC 6 birim. D'den AB ve AC kenarlarına inen iki kesikli dikme h ile işaretli.](gorsel/tyt-matematik/20-02-ic-aciortay.svg "D açıortay üzerinde olduğu için iki kenara uzaklığı aynıdır (h). Mavi ve yeşil üçgenlerin alanları 6 ile 9 gibi orantılıdır; bu yüzden taban parçaları da 4 ile 6 gibi orantılıdır.")

**Çözüm.**

1. Açıortay karşı kenarı, yanındaki kenarlarla aynı oranda böler: $\dfrac{|BD|}{|DC|} = \dfrac{|AB|}{|AC|} = \dfrac{6}{9} = \dfrac{2}{3}$.
2. $|BD| = 2k$, $|DC| = 3k$ de. $2k + 3k = 10 \Rightarrow k = 2$.
3. $|BD| = 4$, $|DC| = 6$.

**Neden böyle?** $D$ açıortay üzerinde olduğu için $[AB]$ ve $[AC]$'ye uzaklıkları eşittir; ikisine de $h$ de. O zaman $A(ABD) = \dfrac{6 \cdot h}{2}$ ve $A(ADC) = \dfrac{9 \cdot h}{2}$; alanlar $6 : 9$ oranındadır. Öte yandan iki üçgenin $A$'dan $[BC]$'ye inen yüksekliği ortaktır; alanları tabanları gibi, yani $|BD| : |DC|$ gibi orantılıdır. İkisi aynı oran olduğuna göre $|BD| : |DC| = 6 : 9$.

**Kural:** $[AD]$ iç açıortay ise

$$\frac{|BD|}{|DC|} = \frac{|AB|}{|AC|} \qquad \text{ve} \qquad \frac{A(ABD)}{A(ADC)} = \frac{|AB|}{|AC|}$$

Eşleştirme: $B$'ye değen parça ($|BD|$), $B$'ye değen kenarla ($|AB|$) eşleşir. Uzun kenarın yanındaki parça da uzundur.

**İkizkenar üçgende:** $|AB| = |AC|$ ise oran $1$ olur, $D$ tam orta noktadır. Tepe açısından tabana çizilen açıortay aynı zamanda **yükseklik** ve **kenarortaydır**. Örneğin $|AB| = |AC| = 10$, $|BC| = 12$ ise $|BD| = 6$ ve $[AD] \perp [BC]$ olduğundan $|AD| = \sqrt{10^2 - 6^2} = 8$.

> **Tuzak:** $\dfrac{|BD|}{|DC|} = \dfrac{|AC|}{|AB|}$ yazmak (oranı ters kurmak). Örnekte bu hata $|BD| = 6$, $|DC| = 4$ verir: uzun kenar $[AC]$'nin yanına kısa parça düşer, bu da yanlıştır. Kontrol: büyük kenarın yanındaki parça büyük olmalı.

## 2. Dış açıortay teoremi

**Örnek.** $ABC$ üçgeninde $|AB| = 9$, $|AC| = 6$, $|BC| = 5$'tir. $A$ köşesindeki dış açının açıortayı, $[BC]$'nin uzantısını $D$ noktasında kesiyor. $|DC|$ kaçtır?

![ABC üçgeni: AB 9, AC 6, BC 5 birim. BA kenarı A'nın ötesine kesikli çizgiyle uzatılmış; A'daki dış açı kırmızı AD ile iki eş β açısına bölünmüş. D, BC'nin C'den sonraki kesikli uzantısında ve CD 10 birim. Mavi kesikli AE iç açıortayı ile kırmızı AD arasında dik açı işareti var.](gorsel/tyt-matematik/20-02-dis-aciortay.svg "D, kısa kenar olan AC tarafında, üçgenin dışındadır. Mavi iç açıortay ile kırmızı dış açıortay her zaman dik kesişir.")

**Çözüm.**

1. Dış açıortay için de oran aynıdır: $\dfrac{|DB|}{|DC|} = \dfrac{|AB|}{|AC|} = \dfrac{9}{6} = \dfrac{3}{2}$.
2. $D$ üçgenin dışında, $C$'nin ötesindedir: $|DB| = |DC| + |BC| = |DC| + 5$.
3. $|DC| = 2k$, $|DB| = 3k$ ise fark $k = 5$. Buradan $|DC| = 10$, $|DB| = 15$.

**Kural:** $A$'daki dış açıortay $[BC]$'nin uzantısını $D$'de kesiyorsa

$$\frac{|DB|}{|DC|} = \frac{|AB|}{|AC|}$$

- $D$, **kısa kenarın** tarafında, üçgenin dışındadır. Burada $|AC| < |AB|$ olduğu için $D$, $C$'nin ötesine düşer.
- İç teoremde parçaların **toplamı** $|BC|$ idi; dış teoremde parçaların **farkı** $|BC|$'dir.
- $|AB| = |AC|$ ise dış açıortay $[BC]$'ye paraleldir, uzantıyı hiç kesmez.
- Aynı köşedeki iç ve dış açıortay diktir: $2\alpha + 2\beta = 180^\circ \Rightarrow \alpha + \beta = 90^\circ$. Örnekte iç açıortay $E$'de keserse $|BE| = 3$, $|EC| = 2$ ve $|ED| = 2 + 10 = 12$ olur.

> **Tuzak:** $|DB| = |DC| - |BC|$ ya da $|DC| + |DB| = |BC|$ yazmak. $D$ dışarıda olduğu için büyük parça, küçük parça ile $|BC|$'nin **toplamıdır**. Önce $D$'nin hangi uca yakın olduğuna karar ver.

## 3. Katlama soruları

Kâğıt katlandığında katlanan parça yerinden kalkar ama boyu ve açıları değişmez. Katlama çizgisi, üst üste gelen iki kenarın arasındaki açıyı ikiye böler: **katlama çizgisi açıortaydır.**

**Örnek.** Üçgen biçimli $ABC$ kâğıdında $|AB| = 6$, $|AC| = 8$, $|BC| = 10$'dur. Kâğıt, $[BA]$ kenarı $[BC]$'nin üzerine gelecek biçimde $B$'den geçen bir çizgi boyunca katlanıyor. $A$ köşesi $[BC]$ üzerinde $A'$ noktasına, katlama çizgisi $[AC]$'yi $D$'de kesiyor. $DA'C$ üçgeninin çevresi kaçtır?

![Kâğıt ABC üçgeni: A'da dik açı, AB 6, AD 3, DC 5. B'den D'ye kırmızı kesikli katlama çizgisi B açısını iki eş parçaya bölüyor. Mavi ABD parçası katlanınca sarı A'BD üçgenine dönüşüyor; A', BC üzerinde, BA' 6, A'C 4, A'D 3 birim ve A' noktasında dik açı var. Kavisli ok A köşesinden A' noktasına gidiyor.](gorsel/tyt-matematik/20-02-katlama-aciortay.svg "Mavi parça katlanıp sarı parçanın üstüne oturur. Katlama çizgisi BD, B açısının açıortayıdır; AD ile A'D eşittir.")

**Çözüm.**

1. $[BA]$, $[BC]$'nin üstüne geldiği için $\widehat{ABD}$ ile $\widehat{DBC}$ eşittir: $[BD]$, $B$'nin açıortayıdır.
2. İç açıortay teoremi ($B$ köşesinden): $\dfrac{|AD|}{|DC|} = \dfrac{|BA|}{|BC|} = \dfrac{6}{10} = \dfrac{3}{5}$. $|AC| = 8$ olduğundan $|AD| = 3$, $|DC| = 5$.
3. Katlanan parça boyunu korur: $|BA'| = |BA| = 6$, $|A'D| = |AD| = 3$. O halde $|A'C| = 10 - 6 = 4$.
4. $\text{Ç}(DA'C) = 3 + 4 + 5 = 12$.

**Kısa yol:** $|A'D| = |AD|$ olduğu için $|A'D| + |DC| = |AC|$. Çevre $= |AC| + |A'C| = 8 + (10 - 6) = 12$. Oranı hesaplamadan da bulunur.

**İkinci tür katlama:** Kâğıt, $B$ ile $C$ üst üste gelecek biçimde katlanırsa katlama çizgisi $[BC]$'yi tam ortadan ve dik keser. Bu çizgi üzerindeki her nokta $B$'ye ve $C$'ye eşit uzaklıktadır: $|DB| = |DC|$, $|FB| = |FC|$.

**Örnek.** $|AB| = 5$, $|AC| = 8$, $|BC| = 9$ olan $ABC$ kâğıdı $B$ ile $C$ çakışacak biçimde katlanıyor; katlama çizgisi $[AC]$'yi $D$'de kesiyor. $ABD$ üçgeninin çevresi kaçtır?

![Kâğıt ABC üçgeni: AB 5, AC 8 birim. BC'nin orta noktası F'den BC'ye dik çıkan kırmızı kesikli katlama çizgisi AC'yi D'de kesiyor. BF ile FC tek çentikle, DB ile DC çift çentikle eş işaretli. ABD üçgeni mavi boyalı.](gorsel/tyt-matematik/20-02-katlama-orta-dikme.svg "Katlama çizgisi BC'yi F'de dik ve ortadan keser. Çift çentikler DB ile DC'nin eşit olduğunu gösterir; mavi ABD üçgeninin çevresinde DB yerine DC yazılabilir.")

**Çözüm.** $\text{Ç}(ABD) = |AB| + |AD| + |DB| = |AB| + |AD| + |DC| = |AB| + |AC| = 5 + 8 = 13$.

**Kural:**

- Bir kenarı başka bir kenarın üstüne katlamak → katlama çizgisi o köşenin **açıortayıdır**, açıortay teoremi kullanılır.
- İki köşeyi çakıştırmak → katlama çizgisi aradaki kenarı **dik ve ortadan** keser; çizgi üzerindeki nokta iki köşeye eşit uzaklıktadır.

> **Tuzak:** Katlanan kenarın yeni yerindeki boyu aynıdır: $|BA'| = |BA|$. $|A'C|$'yi ayrıca hesaplamaya çalışma; $|BC| - |BA|$'dır.

## 4. İç açıortayların kesim noktası ve alanlar

**Örnek.** $ABC$ üçgeninde $|AB| = 13$, $|BC| = 14$, $|CA| = 15$ ve $A(ABC) = 84$'tür. $D$, iç açıortayların kesim noktasıdır. $A(DBC)$ kaçtır?

![ABC üçgeni: AB 13, BC 14, CA 15. İç açıortayların kesim noktası D köşelere kırmızı çizgilerle bağlanmış; oluşan üç üçgenin alanları DAB'de 26 (mavi), DBC'de 28 (sarı), DCA'da 30 (yeşil). D'den BC'ye inen kesikli dikme 4 birim.](gorsel/tyt-matematik/20-02-ic-merkez.svg "Üç küçük üçgenin yüksekliği aynıdır (D'nin kenarlara uzaklığı 4). Bu yüzden alanları tabanları gibi sıralanır: 26, 28, 30.")

**Çözüm.**

1. $D$ üç açıortayın da üzerindedir; bu yüzden üç kenara uzaklığı aynıdır. Bu uzaklığa $r$ de.
2. Üç küçük üçgenin yüksekliği $r$ olduğundan alanları kenarlarla orantılıdır: $13 : 14 : 15$.
3. $13 + 14 + 15 = 42$ parçanın $14$'ü $DBC$'dir: $A(DBC) = 84 \cdot \dfrac{14}{42} = 28$.
4. Benzer biçimde $A(DCA) = 30$, $A(DAB) = 26$. Ayrıca $\dfrac{42 \cdot r}{2} = 84 \Rightarrow r = 4$.

**Kural:** $D$ iç açıortayların kesim noktası ise

$$A(DBC) : A(DCA) : A(DAB) = |BC| : |CA| : |AB|$$

> **Tuzak:** Üç alanı eşit sanmak. Alanları eşit bölen nokta, kenarortayların kesim noktasıdır (ağırlık merkezi); iç açıortayların kesim noktası alanları **kenarlar oranında** böler.

## ÖSYM tuzakları

> **Oranı ters kurmak.** $|BD|$, $B$'ye değen kenar $|AB|$ ile eşleşir. Seçeneklerde $|BD|$ ile $|DC|$'nin yer değiştirmiş hali hep bulunur.

> **Dış açıortayda toplam yerine fark.** $D$ üçgenin dışında olduğundan $|DB| - |DC| = |BC|$'dir. $|DB| + |DC| = |BC|$ yazarsan iç açıortayın değerlerini bulursun.

> **İstenen parçayı karıştırmak.** Bir parçayı bulunca durma; soru $|DB|$'yi mi, $|DC|$'yi mi, yoksa iki açıortay arasındaki $|ED|$'yi mi istiyor, tekrar oku.

> **Katlamada açıortayı görmemek.** "Bir kenar öbür kenarın üzerine gelecek biçimde katlanıyor" cümlesi, "katlama çizgisi açıortaydır" demektir.

> **Alanı eşit paylaştırmak.** İç açıortayla ayrılan iki parçanın ya da iç açıortayların kesim noktasıyla oluşan üç parçanın alanları eşit değil, kenarlarla orantılıdır.

## Kendini dene

### Soru 1
$ABC$ üçgeninde $|AB| = 8$, $|AC| = 12$ ve $|BC| = 15$'tir. $[AD]$, $A$ açısının açıortayı ve $D \in [BC]$ olduğuna göre $|BD|$ kaçtır?

A) 5
B) 6
C) 7,5
D) 9
E) 10

**Cevap:** B
**Çözüm:** $\dfrac{|BD|}{|DC|} = \dfrac{8}{12} = \dfrac{2}{3}$. $|BD| = 2k$, $|DC| = 3k$; $5k = 15 \Rightarrow k = 3$. $|BD| = 6$, $|DC| = 9$. D seçeneği oranı ters kurmaktır; $7{,}5$ ise $D$'yi orta nokta sanmaktır.

### Soru 2
$ABC$ üçgeninde $|AB| = 12$, $|AC| = 8$ ve $|BC| = 7$'dir. $A$ köşesindeki dış açının açıortayı $[BC]$'nin uzantısını $D$ noktasında kesiyor. $|DC|$ kaçtır?

A) 2,8
B) 4,2
C) 7
D) 14
E) 21

**Cevap:** D
**Çözüm:** $|AC| < |AB|$ olduğundan $D$, $C$'nin ötesindedir. $\dfrac{|DB|}{|DC|} = \dfrac{12}{8} = \dfrac{3}{2}$: $|DC| = 2k$, $|DB| = 3k$, fark $k = |BC| = 7$. $|DC| = 14$, $|DB| = 21$. $2{,}8$ ve $4{,}2$, iç açıortayın ayırdığı parçalardır ($|EC|$ ve $|BE|$); $21$ ise $|DB|$'dir.

### Soru 3
Dik kenarları $6$ ve $8$ birim olan bir dik üçgenin iç açıortaylarının kesim noktası $D$'dir. $D$ noktası köşelere birleştirildiğinde, hipotenüs üzerinde oluşan üçgenin alanı kaç birimkaredir?

A) 6
B) 8
C) 10
D) 12
E) 24

**Cevap:** C
**Çözüm:** Hipotenüs $\sqrt{6^2 + 8^2} = 10$, alan $\dfrac{6 \cdot 8}{2} = 24$, kenarlar toplamı $6 + 8 + 10 = 24$. Alanlar kenarlarla orantılı olduğundan hipotenüsteki üçgenin alanı $24 \cdot \dfrac{10}{24} = 10$. $8$, alanı üçe eşit bölmektir; $12$ ise alanın yarısıdır.

## Özet kartı

- İç açıortay: $\dfrac{|BD|}{|DC|} = \dfrac{|AB|}{|AC|}$; parçaların toplamı $|BC|$. Alanlar da aynı oranda.
- İkizkenarda tepe açısından çizilen açıortay aynı zamanda yükseklik ve kenarortaydır.
- Dış açıortay: $\dfrac{|DB|}{|DC|} = \dfrac{|AB|}{|AC|}$; $D$ kısa kenar tarafında, dışarıda; parçaların farkı $|BC|$.
- Aynı köşedeki iç ve dış açıortay diktir.
- Kenarı kenarın üstüne katlamak → katlama çizgisi açıortay. İki köşeyi çakıştırmak → çizgi üzerindeki nokta iki köşeye eşit uzaklıkta.
- İç açıortayların kesim noktası: $A(DBC) : A(DCA) : A(DAB) = |BC| : |CA| : |AB|$.

## Sonraki adım

Alıştırmaya geç (aşağıdaki düğme). Sonraki ders: **Üçgende Kenarortay**. Bugün alanları kenarlar oranında bölen noktayı gördün; orada alanları **eşit** bölen noktayı, ağırlık merkezini öğreneceksin.
