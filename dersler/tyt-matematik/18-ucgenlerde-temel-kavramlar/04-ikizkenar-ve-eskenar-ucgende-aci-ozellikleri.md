---
baslik: İkizkenar ve Eşkenar Üçgende Açı Özellikleri
ders: tyt-matematik
sure: 20 dk
kaynak: MEBİ Konu Özeti a49e51e874
guncelleme: 2026-11-17
---
# İkizkenar ve Eşkenar Üçgende Açı Özellikleri

**Bu dersin sonunda:** şekilde eş kenarları görünce karşılarındaki eş açıları yazabilecek, ikizkenar ve eşkenar üçgenleri art arda kullanarak bilinmeyen açıyı bulabileceksin.

> **TYT'de yeri:** Geometri açı sorularının çoğunda şekilde çentikle işaretlenmiş eş kenarlar bulunur. Soru, "eş kenarların karşısındaki açılar eşittir" bilgisini bir ya da iki kez kullanmanı ister. Eşkenar üçgen görünce her açının $60^\circ$ olduğunu yazmak ilk adımdır.

## Önce hatırla

<details><summary>Geçen dersten: ABC üçgeninde m(A) = 55° ve m(B) = 60°'dir. C köşesindeki dış açı kaç derecedir?</summary>
55° + 60° = <b>115°</b>. Dış açı, komşu olmayan iki iç açının toplamıdır. Bugün bu kuralı ikizkenar üçgenlerde çok kullanacaksın.
</details>

<details><summary>Geçen dersten: ABC üçgeninde m(B) = 70°, m(C) = 40°. A'dan çizilen yükseklik ile açıortay arasındaki açı kaç derecedir?</summary>
(70° − 40°) / 2 = <b>15°</b>. Bugün m(B) = m(C) olan üçgenleri göreceksin: fark 0 olur, yani yükseklik ile açıortay aynı doğru parçasıdır.
</details>

## Üçgen çeşitleri (kenarlarına göre)

| Üçgen | Kenarlar | Açılar |
|---|---|---|
| Çeşitkenar | Üçü de farklı | Üçü de farklı |
| İkizkenar | İkisi eşit | Eş kenarların karşısındaki iki açı eşit |
| Eşkenar | Üçü eşit | Üçü de $60^\circ$ |

Şekillerde eş kenarlar aynı sayıda **çentikle** gösterilir. Çentiği gördüğün an karşısındaki açıları eşit yaz.

## 1. İkizkenar üçgende taban açıları eşittir

**Örnek 1.** $ABC$ üçgeninde $|AB| = |AC|$ ve $m(\widehat{A}) = 40^\circ$'dir. $m(\widehat{B})$ ve $m(\widehat{C})$ kaçtır?

**Çözüm.**

1. $|AB| = |AC|$ olduğundan bu kenarların karşısındaki açılar eşittir: $m(\widehat{B}) = m(\widehat{C}) = x$ de.
2. İç açılar toplamı: $40^\circ + x + x = 180^\circ \Rightarrow 2x = 140^\circ \Rightarrow x = 70^\circ$.

![İkizkenar ABC üçgeni: AB ve AC kenarlarında birer çentik var. Tepe A'da 40 derece, tabandaki B ve C köşelerinde 70'er derece.](gorsel/tyt-matematik/18-04-ikizkenar.svg "Çentikli iki yan kenar eşit, bu yüzden karşılarındaki yeşil taban açıları da eşit: 70° ve 70°. Mavi açı tepe açısıdır.")

**Adlar:** Eşit kenarlar $[AB]$ ve $[AC]$ **yan kenarlar**, üçüncü kenar $[BC]$ **taban**dır. $\widehat{B}$ ve $\widehat{C}$ **taban açıları**, $\widehat{A}$ **tepe açısı**dır.

**Kural:**

$$|AB| = |AC| \iff m(\widehat{B}) = m(\widehat{C})$$

$$\text{tepe açısı} = 180^\circ - 2 \cdot \text{taban açısı}, \qquad \text{taban açısı} = \frac{180^\circ - \text{tepe açısı}}{2}$$

- Kural iki yönlüdür: iki açısı eşit olan üçgen de ikizkenardır.
- Bir açısı bilinen ikizkenar üçgenin bütün açıları bulunur. Örneğin taban açısı $65^\circ$ ise tepe açısı $180^\circ - 130^\circ = 50^\circ$'dir.

> **Tuzak:** "Bir açısı $50^\circ$ olan ikizkenar üçgen" dendiğinde bu açının tepe mi taban mı olduğu söylenmemiştir. İki durum vardır: tepe $50^\circ$ ise açılar $50^\circ, 65^\circ, 65^\circ$; taban $50^\circ$ ise $50^\circ, 50^\circ, 80^\circ$. Verilen açı $90^\circ$ ya da daha büyükse yalnızca tepe açısı olabilir, çünkü iki tane geniş açı bir üçgene sığmaz.

## 2. Tepeden inen yükseklik: hem açıortay hem kenarortay

**Örnek 2.** $ABC$ üçgeninde $|AB| = |AC|$, $m(\widehat{A}) = 50^\circ$ ve $|BC| = 12$ birimdir. $[AH] \perp [BC]$ olduğuna göre $m(\widehat{BAH})$ ve $|BH|$ kaçtır?

**Çözüm.**

1. Taban açıları: $m(\widehat{B}) = m(\widehat{C}) = \dfrac{180^\circ - 50^\circ}{2} = 65^\circ$.
2. $ABH$ dik üçgeninde $m(\widehat{BAH}) = 180^\circ - 90^\circ - 65^\circ = 25^\circ$. Aynı hesap $ACH$'de de $25^\circ$ verir: $[AH]$, $\widehat{A}$'yı iki eş parçaya böler.
3. Şekil $[AH]$ doğrusuna göre simetriktir; $H$, $[BC]$'nin orta noktasıdır: $|BH| = |HC| = 6$.

![İkizkenar ABC üçgeni: tepe A'dan tabana dik inen mavi AH yüksekliği. A'daki açı 25 ve 25 dereceye bölünmüş, B ve C'de 65'er derece, H'de dik açı işareti; BH ve HC 6'şar birim ve çift çentikli.](gorsel/tyt-matematik/18-04-yukseklik.svg "Mavi AH aynı anda üç iş yapar: tabana diktir (yükseklik), tepe açısını 25° + 25° diye ikiye böler (açıortay), tabanı 6 + 6 diye ikiye böler (kenarortay).")

**Kural:** İkizkenar üçgende **tepe köşesinden** çizilen yükseklik, aynı zamanda açıortay ve kenarortaydır.

$$m(\widehat{BAH}) = m(\widehat{HAC}) = \frac{m(\widehat{A})}{2}, \qquad |BH| = |HC| = \frac{|BC|}{2}$$

Geçen dersteki formülle bağlantı: yükseklik ile açıortay arasındaki açı $\dfrac{65^\circ - 65^\circ}{2} = 0^\circ$; ikisi çakışır.

> **Tuzak:** Bu özellik yalnızca **tepe** köşesinden (eş kenarların birleştiği köşeden) inen doğru parçası için geçerlidir. $B$'den $[AC]$'ye inen yükseklik, genelde $\widehat{B}$'yi ikiye bölmez.

## 3. Eşkenar üçgen: her açı 60°

**Örnek 3.** $ABC$ eşkenar üçgendir. $[BC]$ kenarı $C$'nin ötesine, $|CD| = |CA|$ olacak biçimde $D$ noktasına kadar uzatılıyor. $m(\widehat{BAD})$ kaçtır?

**Çözüm.**

1. Eşkenar üçgende üç açı eşittir: $3x = 180^\circ \Rightarrow$ her açı $60^\circ$.
2. $\widehat{ACD}$, $C$'deki dış açıdır: $180^\circ - 60^\circ = 120^\circ$.
3. $|CA| = |CD|$ olduğundan $ACD$ ikizkenardır, tepesi $C$: $m(\widehat{CAD}) = m(\widehat{CDA}) = \dfrac{180^\circ - 120^\circ}{2} = 30^\circ$.
4. $m(\widehat{BAD}) = 60^\circ + 30^\circ = 90^\circ$.

![Eşkenar ABC üçgeni: üç kenarda birer çentik, B'de ve A'da 60 derece. BC kırmızı CD parçasıyla uzatılmış, CD de tek çentikli. C'deki dış açı 120, A'daki CAD açısı ve D'deki açı 30'ar derece.](gorsel/tyt-matematik/18-04-eskenar.svg "Dört kenarın hepsi eşit (tek çentik). Kırmızı ACD ikizkenar üçgeninin tepe açısı 120°, taban açıları 30°'dir; A'daki toplam açı 60° + 30° = 90° olur.")

**Kural:** Eşkenar üçgende $|AB| = |BC| = |CA|$ ve

$$m(\widehat{A}) = m(\widehat{B}) = m(\widehat{C}) = 60^\circ$$

- Her dış açısı $120^\circ$'dir.
- Bir açısı $60^\circ$ olan ikizkenar üçgen eşkenardır: tepe $60^\circ$ ise taban açıları $\dfrac{120^\circ}{2} = 60^\circ$; taban $60^\circ$ ise tepe $180^\circ - 120^\circ = 60^\circ$.

> **Tuzak:** Eşkenar üçgenin kenarına eklenen yeni üçgende $60^\circ$'yi unutma. Örnekte $m(\widehat{BAD})$ soruluyor; yalnızca $30^\circ$ yazan, $\widehat{BAC}$'deki $60^\circ$'yi eklemeyi unutmuş olur.

## 4. Art arda ikizkenar üçgenler

**Örnek 4.** $D$ noktası $[BC]$ üzerindedir. $|AB| = |AD| = |DC|$ ve $m(\widehat{C}) = 32^\circ$'dir. $m(\widehat{BAC})$ kaçtır?

**Çözüm.**

1. $|DA| = |DC|$: $ADC$ ikizkenar, $m(\widehat{DAC}) = m(\widehat{C}) = 32^\circ$.
2. $\widehat{ADB}$, $ADC$ üçgeninin dış açısıdır: $32^\circ + 32^\circ = 64^\circ$.
3. $|AB| = |AD|$: $ABD$ ikizkenar, $m(\widehat{ABD}) = m(\widehat{ADB}) = 64^\circ$.
4. $m(\widehat{BAD}) = 180^\circ - 64^\circ - 64^\circ = 52^\circ$.
5. $m(\widehat{BAC}) = 52^\circ + 32^\circ = 84^\circ$.

![ABC üçgeni, D noktası BC üzerinde. AB, AD ve DC kenarları tek çentikli. C'de ve DAC açısında 32'şer derece mavi; D'deki ADB açısı ve B'deki açı 64'er derece kırmızı; BAD açısı 52 derece yeşil.](gorsel/tyt-matematik/18-04-zincir.svg "Sağdaki ikizkenar üçgenin taban açıları 32°; soldaki ikizkenara geçerken D'deki dış açı iki katına çıkar: 64°.")

**Kural:** İkizkenar üçgenin taban açısı $x$ ise, tabanı uzatınca tepe köşesinde oluşan dış açı $2x$'tir (dış açı = iki taban açısının toplamı). Zincir sorularında açılar $x$, $2x$, $3x$… diye büyür; her yeni ikizkenar üçgende yeni bir eşitlik yazarsın.

> **Tuzak:** Eşit kenarları doğru eşleştir. $|AD| = |DC|$ ise eşit açılar $D$'nin **karşısındaki** değil, $A$ ve $C$'deki açılardır. Önce "eşit kenarlar hangi köşede birleşiyor?" diye bak; o köşe tepedir, eşit açılar öbür iki köşededir.

## ÖSYM tuzakları

> **Tepe mi taban mı?** Hangi açının verildiği söylenmemişse iki durumu da dene. Seçeneklerde genelde yalnızca birinin sonucu bulunur; ikisinin toplamı sorulursa ikisini de hesapla.

> **Eşit açıyı yanlış köşeye koymak.** $|AB| = |AC|$ ise $m(\widehat{B}) = m(\widehat{C})$'dir, $m(\widehat{A})$ değil. Eşit açılar, eşit kenarların **karşısındadır**.

> **İkiye bölmeyi unutmak.** Tepe açısı verildiğinde taban açısı $\dfrac{180^\circ - \text{tepe}}{2}$'dir. $180^\circ - \text{tepe}$ değeri, iki taban açısının **toplamıdır**; seçeneklerde hazır bekler.

> **Eşkenar üçgeni görmemek.** Çentiklerin üçü de aynıysa ya da ikizkenar üçgenin bir açısı $60^\circ$ ise üçgen eşkenardır; bütün açılar $60^\circ$'dir.

## Kendini dene

### Soru 1
$ABC$ üçgeninde $|AB| = |AC|$'dir. $[BC]$ kenarı $C$'nin ötesine uzatıldığında $C$'de oluşan dış açı $125^\circ$ oluyor. $m(\widehat{A})$ kaç derecedir?

A) 35
B) 55
C) 70
D) 110
E) 125

**Cevap:** C
**Çözüm:** $m(\widehat{C}) = 180^\circ - 125^\circ = 55^\circ$. $|AB| = |AC|$ olduğundan $m(\widehat{B}) = 55^\circ$. $m(\widehat{A}) = 180^\circ - 2 \cdot 55^\circ = 70^\circ$. Kontrol: dış açı $= m(\widehat{A}) + m(\widehat{B}) = 70^\circ + 55^\circ = 125^\circ$. $55^\circ$ taban açısıdır, $110^\circ$ ise iki taban açısının toplamı.

### Soru 2
Bir iç açısı $30^\circ$ olan bir ikizkenar üçgenin en büyük iç açısı aşağıdakilerden hangisi **olabilir**?

A) 30
B) 60
C) 90
D) 105
E) 120

**Cevap:** E
**Çözüm:** İki durum var. $30^\circ$ tepe açısıysa açılar $30^\circ, 75^\circ, 75^\circ$; en büyüğü $75^\circ$ (seçeneklerde yok). $30^\circ$ taban açısıysa açılar $30^\circ, 30^\circ, 120^\circ$; en büyüğü $120^\circ$. $105^\circ$, iki taban açısını $75^\circ$ sanıp $180^\circ - 75^\circ$ hesaplamaktan gelir.

### Soru 3
$D$ noktası $ABC$ üçgeninin $[BC]$ kenarı üzerindedir. $|AB| = |AD| = |DC|$ ve $m(\widehat{B}) = 70^\circ$'dir. $m(\widehat{C})$ kaç derecedir?

A) 30
B) 35
C) 40
D) 70
E) 75

**Cevap:** B
**Çözüm:** $|AB| = |AD|$ olduğundan $m(\widehat{ADB}) = m(\widehat{B}) = 70^\circ$. $\widehat{ADB}$, $ADC$ üçgeninin dış açısıdır ve $|DA| = |DC|$ olduğundan iki eşit taban açısının toplamıdır: $2 \cdot m(\widehat{C}) = 70^\circ \Rightarrow m(\widehat{C}) = 35^\circ$. $40^\circ$, $m(\widehat{BAD})$; $75^\circ$ ise $m(\widehat{BAC}) = 40^\circ + 35^\circ$ değeridir.

## Özet kartı

- Eş kenarların karşısındaki açılar eşittir; iki açısı eşit üçgen ikizkenardır.
- Taban açısı $= \dfrac{180^\circ - \text{tepe}}{2}$; tepe $= 180^\circ - 2 \cdot \text{taban}$.
- Tepe köşesinden inen yükseklik = açıortay = kenarortay.
- Eşkenar üçgende her iç açı $60^\circ$, her dış açı $120^\circ$; bir açısı $60^\circ$ olan ikizkenar üçgen eşkenardır.
- Açının tepe mi taban mı olduğu belli değilse iki durumu da dene.
- Zincirde: ikizkenarın tepesindeki dış açı, taban açısının 2 katıdır.

## Sonraki adım

Alıştırmaya geç (aşağıdaki düğme). Sonraki ders: **Üçgende Açı-Kenar Bağıntıları**. Bugün "eşit kenar karşısında eşit açı" gördün; orada "büyük kenar karşısında büyük açı" kuralını öğreneceksin.
