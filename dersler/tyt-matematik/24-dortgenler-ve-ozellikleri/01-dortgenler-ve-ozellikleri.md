---
baslik: Dörtgenler ve Özellikleri
ders: tyt-matematik
sure: 25 dk
kaynak: MEBİ Konu Özeti 78b28ad897
guncelleme: 2026-11-18
---
# Dörtgenler ve Özellikleri

<div class="giris" dir="rtl" lang="ar">

**الدرس ده عن إيه؟** عن الشكل الرباعي (dörtgen): أي شكل مقفول ليه أربع رؤوس وأربع أضلاع، والقواعد اللي بتمشي على أي رباعي مهما كان شكله.

- هتعرف الفرق بين الرباعي المحدب (dışbükey) والمقعر (içbükey)، وإن مجموع الزوايا الداخلية (iç açılar) 360 درجة، والخارجية (dış açılar) كمان 360.
- هتتعلم قاعدتين لمنصفات الزوايا (açıortay): لما يكونوا لزاويتين جنب بعض، ولما يكونوا لزاويتين قصاد بعض.
- هتشوف إيه اللي بيحصل لما الأقطار (köşegenler) تتقاطع متعامدة، ولما توصل نقط منتصف الأضلاع (orta noktalar) ببعض.

**ليه مهم؟** أسئلة الرباعي العام بتيجي في TYT، وأغلبها بيتحل بقاعدة واحدة من دول في سطرين. وكمان الدرس ده أساس دروس شبه المنحرف (yamuk) ومتوازي الأضلاع (paralelkenar) الجاية.

الدرس 25 دقيقة، وكل قاعدة معاها رسمة ومثال محلول. امسك ورقة وقلم وامشي معانا خطوة بخطوة.

</div>

**Bu dersin sonunda:** bir dörtgende bilinmeyen açıyı iç ve dış açı toplamından, açıortaylar arasındaki açıyı iki kısa kuraldan, eksik kenarı ya da çevreyi de köşegen özelliklerinden en çok iki adımda bulabileceksin.

> **TYT'de yeri:** Geometri bölümünde "herhangi bir dörtgen" sorusu genelde bir şekil verir ve bir açı ya da uzunluk ister. En sık gelenler: iç açılar toplamı (özellikle içbükey dörtgende), iki açıortay arasındaki açı ve köşegenleri dik kesişen dörtgende kenar bağıntısı. Bu kurallar sonraki özel dörtgen derslerinde de her an işe yarar.

## Önce hatırla

<details><summary>Geçen dersten: Bir beşgenin iç açılarının ölçüleri toplamı kaç derecedir?</summary>
$(n - 2) \cdot 180^\circ$ formülünde $n = 5$: $3 \cdot 180^\circ =$ <b>540°</b>. Bugün aynı formülü $n = 4$ için kullanacaksın: $2 \cdot 180^\circ = 360^\circ$.
</details>

<details><summary>Geçen dersten: Bir düzgün çokgenin bir dış açısı 40° ise bu çokgen kaç kenarlıdır?</summary>
Her çokgenin dış açıları toplamı $360^\circ$'dir: $360^\circ \div 40^\circ =$ <b>9</b> kenar. Dörtgenin dış açıları toplamı da $360^\circ$ olacak.
</details>

## Dörtgen nedir?

Herhangi üçü aynı doğru üzerinde olmayan dört noktayı sırayla birleştirince oluşan kapalı şekle **dörtgen** denir. $ABCD$ dörtgeninin 4 köşesi, 4 kenarı ve 2 köşegeni vardır: $[AC]$ ve $[BD]$. Köşeler **sırayla** okunur; $[AB]$ ile $[CD]$ karşılıklı kenarlardır, $\widehat{A}$ ile $\widehat{C}$ karşılıklı açılardır.

- **Dışbükey dörtgen:** her iç açısı $180^\circ$'den küçüktür. İki köşegeni de dörtgenin içindedir.
- **İçbükey dörtgen:** bir iç açısı $180^\circ$'den büyüktür. Köşegenlerden biri dörtgenin dışında kalır.

![Solda dışbükey ABCD dörtgeni, iki köşegeni de içeride kesikli çizgilerle çizilmiş. Sağda içbükey ABCD dörtgeni; D noktası içeri göçmüş, D'deki iç açı kırmızı yayla gösterilmiş ve 180 dereceden büyük. BD köşegeni içeride, AC köşegeni dışarıda.](gorsel/tyt-matematik/24-01-turler.svg "Sağdaki şekilde D'deki iç açı dörtgenin içinden ölçülür ve 180°'den büyüktür. AC köşegeninin dışarıda kaldığına dikkat et.")

Soru aksini söylemiyorsa dörtgen **dışbükey** kabul edilir.

## 1. İç açılar ve dış açılar: ikisi de 360°

**Örnek 1.** $ABCD$ dörtgeninde $m(\widehat{A}) = 95^\circ$, $m(\widehat{B}) = 70^\circ$, $m(\widehat{C}) = 110^\circ$. $m(\widehat{D})$ kaçtır?

**Çözüm.** $m(\widehat{D}) = 360^\circ - (95^\circ + 70^\circ + 110^\circ) = 360^\circ - 275^\circ = 85^\circ$.

**Neden 360°?** $[AC]$ köşegeni dörtgeni iki üçgene böler. Her üçgenin iç açıları toplamı $180^\circ$; iki üçgende $360^\circ$. Geçen dersteki formülle de aynı: $(4 - 2) \cdot 180^\circ = 360^\circ$.

**Örnek 2.** Aynı dörtgende her köşede bir kenarı uzat. $A$, $B$, $C$ köşelerindeki dış açılar $85^\circ$, $110^\circ$, $70^\circ$'dir. $D$'deki dış açı kaçtır?

**Çözüm.** Dış açılar toplamı $360^\circ$: $360^\circ - (85^\circ + 110^\circ + 70^\circ) = 95^\circ$. Kontrol: $D$'deki iç açı $85^\circ$, dış açı $180^\circ - 85^\circ = 95^\circ$.

![ABCD dörtgeni. İç açılar mavi: A'da 95, B'de 70, C'de 110, D'de 85 derece. AC köşegeni kesikli. Her köşede bir kenar kırmızı kesikli çizgiyle uzatılmış; dış açılar kırmızı: A'da 85, B'de 110, C'de 70, D'de 95 derece.](gorsel/tyt-matematik/24-01-acilar.svg "Mavi: iç açılar, toplam 360°. Kırmızı: dış açılar, toplam yine 360°. Her köşede mavi ile kırmızı yan yanadır, toplamları 180°'dir.")

**Kural:**

$$m(\widehat{A}) + m(\widehat{B}) + m(\widehat{C}) + m(\widehat{D}) = 360^\circ \qquad \text{dış açılar toplamı} = 360^\circ$$

- Her köşede iç açı + dış açı $= 180^\circ$.
- **İçbükey dörtgende de** iç açılar toplamı $360^\circ$'dir; $180^\circ$'den büyük açı da bu toplama girer. Örnek: üç açısı $30^\circ$, $45^\circ$, $50^\circ$ olan içbükey dörtgenin dördüncü iç açısı $360^\circ - 125^\circ = 235^\circ$'dir. O köşenin dış taraftaki açısı $360^\circ - 235^\circ = 125^\circ$; bu da "Üçgende Açılar" dersindeki ok şekli kuralıdır ($30^\circ + 45^\circ + 50^\circ$).

> **Tuzak:** İçbükey dörtgende soru "iç açı" diyorsa cevap $180^\circ$'den **büyüktür**. Dış taraftaki küçük açıyı ($125^\circ$) yazmak en sık yapılan hatadır.

## 2. Komşu iki açının açıortayları

**Örnek 3.** $ABCD$ dörtgeninde $m(\widehat{A}) = 120^\circ$, $m(\widehat{B}) = 90^\circ$, $m(\widehat{C}) = 70^\circ$, $m(\widehat{D}) = 80^\circ$. $\widehat{B}$ ve $\widehat{C}$'nin açıortayları $E$ noktasında kesişiyor. $m(\widehat{BEC})$ kaçtır?

![ABCD dörtgeni: A'da 120, D'de 80 derece. B'deki 90 derecelik açı yeşil BE açıortayıyla 45 ve 45 dereceye, C'deki 70 derecelik açı yeşil CE açıortayıyla 35 ve 35 dereceye bölünmüş. İki açıortay E'de buluşuyor; E'deki açı 100 derece.](gorsel/tyt-matematik/24-01-komsu-aciortay.svg "BEC üçgeninde 45° + 35° + 100° = 180°. E'deki 100°, açıortayı çizilmeyen A ve D açılarının ortalamasıdır.")

**Çözüm.**

1. $m(\widehat{EBC}) = 90^\circ \div 2 = 45^\circ$, $m(\widehat{ECB}) = 70^\circ \div 2 = 35^\circ$.
2. $BEC$ üçgeninde $m(\widehat{BEC}) = 180^\circ - 45^\circ - 35^\circ = 100^\circ$.

**Kısa yol:** $m(\widehat{BEC}) = \dfrac{120^\circ + 80^\circ}{2} = 100^\circ$.

**Kural:** Komşu iki açının ($\widehat{B}$, $\widehat{C}$) açıortayları arasındaki açı, **öbür iki** açının toplamının yarısıdır.

$$m(\widehat{BEC}) = \frac{m(\widehat{A}) + m(\widehat{D})}{2}$$

Neden? $\dfrac{m(\widehat{B}) + m(\widehat{C})}{2} = \dfrac{360^\circ - m(\widehat{A}) - m(\widehat{D})}{2} = 180^\circ - \dfrac{m(\widehat{A}) + m(\widehat{D})}{2}$. Bunu $180^\circ$'den çıkarınca kural çıkar.

> **Tuzak:** Formüle açıortayı çizilen $\widehat{B}$ ve $\widehat{C}$ **girmez**. $\dfrac{m(\widehat{B}) + m(\widehat{C})}{2} = 80^\circ$ bulup durma: bu, $BEC$ üçgenindeki öbür iki açının toplamıdır. $E$'deki açı $180^\circ - 80^\circ = 100^\circ$'dir.

## 3. Karşılıklı iki açının açıortayları

**Örnek 4.** $ABCD$ dörtgeninde $m(\widehat{A}) = 110^\circ$, $m(\widehat{B}) = 100^\circ$, $m(\widehat{C}) = 70^\circ$, $m(\widehat{D}) = 80^\circ$. $[BF]$, $\widehat{B}$'nin; $[DE]$, $\widehat{D}$'nin açıortayıdır ve $B$, $E$, $F$ doğrusaldır. $m(\widehat{DEF})$ kaçtır?

![ABCD dörtgeni: A'da 110, C'de 70 derece. B'nin açıortayı BF yeşil çizgi, CD kenarındaki F noktasına gidiyor; D'nin açıortayı DE yeşil çizgi, BF üzerindeki E noktasında bitiyor. B'deki ve D'deki eş açılar çentiklerle işaretli. E'de DE ile EF arasındaki açı 20 derece.](gorsel/tyt-matematik/24-01-karsi-aciortay.svg "Çentik sayısı aynı olan açılar eştir. İki açıortay arasındaki dar açı 20°: açıortayı çizilmeyen A ile C'nin farkının yarısı.")

**Çözüm.**

1. $m(\widehat{ABE}) = 100^\circ \div 2 = 50^\circ$, $m(\widehat{ADE}) = 80^\circ \div 2 = 40^\circ$.
2. $ABED$ dörtgeninde iç açılar toplamı $360^\circ$: $m(\widehat{BED}) = 360^\circ - 110^\circ - 50^\circ - 40^\circ = 160^\circ$.
3. $B$, $E$, $F$ doğrusal: $m(\widehat{DEF}) = 180^\circ - 160^\circ = 20^\circ$.

**Kısa yol:** $m(\widehat{DEF}) = \dfrac{110^\circ - 70^\circ}{2} = 20^\circ$.

**Kural:** Karşılıklı iki açının ($\widehat{B}$, $\widehat{D}$) açıortayları arasındaki dar açı, **öbür iki** açının farkının yarısıdır.

$$m(\widehat{DEF}) = \frac{|m(\widehat{A}) - m(\widehat{C})|}{2}$$

$m(\widehat{A}) = m(\widehat{C})$ ise fark $0$ olur: iki açıortay **paraleldir** (ya da aynı doğru üzerindedir). Tersi de doğrudur: açıortaylar paralel ise $m(\widehat{A}) = m(\widehat{C})$.

> **Tuzak:** Bu kuralda **fark** vardır, komşu açıortay kuralında **toplam**. Hangisinin geleceğini, açıortayı çizilen köşelerin komşu mu karşılıklı mı olduğu belirler.

## 4. Köşegenleri dik kesişen dörtgen

**Örnek 5.** $ABCD$ dörtgeninde $[AC] \perp [BD]$, $|AB| = 8$, $|BC| = 4$, $|CD| = 11$. $|AD| = x$ kaçtır?

![Köşegenleri O noktasında dik kesişen ABCD dörtgeni; köşegenler kırmızı, O'da dik açı işareti var. AB kenarı 8 ve CD kenarı 11 mavi; BC kenarı 4 ve AD kenarı x yeşil yazılmış.](gorsel/tyt-matematik/24-01-dik-kosegen.svg "Aynı renkli kenarlar karşılıklıdır. Mavilerin kareleri toplamı yeşillerin kareleri toplamına eşittir: 64 + 121 = 16 + x².")

**Çözüm.** $|AB|^2 + |CD|^2 = |BC|^2 + |AD|^2$:

$$8^2 + 11^2 = 4^2 + x^2 \Rightarrow 64 + 121 = 16 + x^2 \Rightarrow x^2 = 169 \Rightarrow x = 13$$

**Neden?** Köşegenler $O$'da kesişsin: $|OA| = a$, $|OB| = b$, $|OC| = c$, $|OD| = d$. Dört dik üçgende Pisagor: $|AB|^2 = a^2 + b^2$, $|CD|^2 = c^2 + d^2$, $|BC|^2 = b^2 + c^2$, $|AD|^2 = a^2 + d^2$. İki toplam da $a^2 + b^2 + c^2 + d^2$'ye eşittir.

**Kural:** Köşegenler dik kesişiyorsa karşılıklı kenarların kareleri toplamı eşittir.

$$[AC] \perp [BD] \;\Rightarrow\; |AB|^2 + |CD|^2 = |BC|^2 + |AD|^2$$

> **Tuzak:** Eşitliğin her iki yanında **karşılıklı** kenarlar vardır ($AB$ ile $CD$, $BC$ ile $AD$). Komşu kenarları eşleştirmek ya da kareleri almadan $8 + 11 = 4 + x$ yazmak yanlıştır ($x = 15$ çıkar).

## 5. Kenarların orta noktalarını birleştirmek

**Örnek 6.** $ABCD$ dörtgeninde $|AC| = 10$, $|BD| = 14$. $E$, $F$, $G$, $H$ sırasıyla $[AB]$, $[BC]$, $[CD]$, $[DA]$ kenarlarının orta noktalarıdır. $EFGH$ dörtgeninin çevresi kaçtır?

![ABCD dörtgeni, AC köşegeni mavi kesikli ve 10, BD köşegeni yeşil kesikli ve 14. Kenar orta noktaları E, F, G, H kırmızı EFGH dörtgeniyle birleştirilmiş. EF ve HG kenarları 5, FG ve EH kenarları 7 yazılmış.](gorsel/tyt-matematik/24-01-orta-noktalar.svg "EF ve HG, AC köşegenine paraleldir ve onun yarısıdır (5). FG ve EH, BD köşegenine paraleldir ve onun yarısıdır (7).")

**Çözüm.**

1. $ABC$ üçgeninde $E$ ve $F$ orta noktadır; $[EF]$ orta tabandır: $[EF] \parallel [AC]$ ve $|EF| = 10 \div 2 = 5$. $ACD$ üçgeninde aynı şekilde $|HG| = 5$.
2. $ABD$ ve $BCD$ üçgenlerinde: $|EH| = |FG| = 14 \div 2 = 7$.
3. $\text{Ç}(EFGH) = 5 + 7 + 5 + 7 = 24$.

**Kural:** Kenar orta noktalarını birleştiren $EFGH$ bir **paralelkenardır**; kenarları köşegenlere paralel ve onların yarısıdır.

$$\text{Ç}(EFGH) = |AC| + |BD|$$

> **Tuzak:** Çevre, köşegenlerin toplamına **eşittir**; yarısına değil. Yarım olan, tek bir kenardır: $|EF| = \dfrac{|AC|}{2}$.

## ÖSYM tuzakları

> **İçbükey dörtgende küçük açıyı yazmak.** $180^\circ$'den büyük iç açı da $360^\circ$'lik toplama girer. Soru "iç açı" diyorsa cevap $180^\circ$'den büyüktür.

> **Dış açıyı iç açı sanmak.** Dış açılar toplamından bulunan değer o köşenin **dış** açısıdır. İç açı için $180^\circ$'den çıkar.

> **Açıortay kurallarını karıştırmak.** Komşu köşelerin açıortayları: öbür iki açının **toplamının** yarısı. Karşılıklı köşelerin açıortayları: öbür iki açının **farkının** yarısı. İki kuralda da açıortayı çizilen açılar formüle girmez.

> **Dik köşegende yanlış eşleştirme.** Karelerin toplamı **karşılıklı** kenarlarda eşittir. Kenarların kendileri (kare almadan) eşit toplanmaz.

> **Orta nokta dörtgeninde ikiye bölmek.** $\text{Ç}(EFGH) = |AC| + |BD|$. Seçeneklerde $\dfrac{|AC| + |BD|}{2}$ ve $2(|AC| + |BD|)$ hazır bekler.

## Kendini dene

### Soru 1
Bir dörtgenin iç açılarının ölçüleri $2x$, $3x - 10^\circ$, $x + 40^\circ$ ve $4x - 30^\circ$'dir. Bu dörtgenin en büyük iç açısı kaç derecedir?

A) 36
B) 72
C) 98
D) 108
E) 114

**Cevap:** E
**Çözüm:** $2x + (3x - 10) + (x + 40) + (4x - 30) = 360 \Rightarrow 10x = 360 \Rightarrow x = 36$. Açılar $72^\circ$, $98^\circ$, $76^\circ$, $114^\circ$; toplamları $360^\circ$, en büyüğü $114^\circ$. A seçeneği $x$'in kendisidir; $108$ ise $3x - 10$ yazarken $-10$'u unutmaktır ($3x = 108$).

### Soru 2
$ABCD$ dörtgeninde $\widehat{B}$ ve $\widehat{C}$'nin açıortayları $E$ noktasında kesişiyor. $m(\widehat{A}) = 105^\circ$ ve $m(\widehat{D}) = 95^\circ$ ise $m(\widehat{BEC})$ kaç derecedir?

A) 5
B) 50
C) 80
D) 100
E) 105

**Cevap:** D
**Çözüm:** Komşu açıortaylar: $m(\widehat{BEC}) = \dfrac{105^\circ + 95^\circ}{2} = 100^\circ$. Kontrol: $m(\widehat{B}) + m(\widehat{C}) = 160^\circ$, yarısı $80^\circ$, $BEC$ üçgeninde $180^\circ - 80^\circ = 100^\circ$. $80^\circ$ son çıkarmayı unutmak, $5^\circ$ ise karşılıklı açıortay kuralını (farkın yarısı) kullanmaktır.

### Soru 3
$ABCD$ dörtgeninde $|AC| = 12$ ve $|BD| = 16$'dır. $E$, $F$, $G$, $H$ sırasıyla $[AB]$, $[BC]$, $[CD]$, $[DA]$ kenarlarının orta noktalarıdır. $EFGH$ dörtgeninin çevresi kaçtır?

A) 14
B) 24
C) 28
D) 48
E) 56

**Cevap:** C
**Çözüm:** $|EF| = |HG| = 12 \div 2 = 6$, $|FG| = |EH| = 16 \div 2 = 8$. $\text{Ç}(EFGH) = 6 + 8 + 6 + 8 = 28 = |AC| + |BD|$. $14$ toplamın yarısı, $56$ ise iki katıdır.

## Özet kartı

- İç açılar toplamı $360^\circ$ (içbükeyde de); dış açılar toplamı $360^\circ$.
- İçbükey dörtgende bir iç açı $180^\circ$'den büyüktür.
- Komşu $\widehat{B}$, $\widehat{C}$ açıortayları: $m(\widehat{BEC}) = \dfrac{m(\widehat{A}) + m(\widehat{D})}{2}$.
- Karşılıklı $\widehat{B}$, $\widehat{D}$ açıortayları: aradaki dar açı $\dfrac{|m(\widehat{A}) - m(\widehat{C})|}{2}$; $\widehat{A} = \widehat{C}$ ise paralel.
- $[AC] \perp [BD]$ ise $|AB|^2 + |CD|^2 = |BC|^2 + |AD|^2$.
- Kenar orta noktaları paralelkenar oluşturur: $\text{Ç}(EFGH) = |AC| + |BD|$.

## Sonraki adım

Alıştırmaya geç (aşağıdaki düğme). Sonraki ders: **Yamukta Açı ve Uzunluk**. Orada bugünkü kurallara "iki kenar paralel" bilgisi eklenecek.
