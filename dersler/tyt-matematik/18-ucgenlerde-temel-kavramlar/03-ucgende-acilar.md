---
baslik: Üçgende Açılar
ders: tyt-matematik
sure: 20 dk
kaynak: MEBİ Konu Özeti 340c464f4a
guncelleme: 2026-11-17
---
# Üçgende Açılar

**Bu dersin sonunda:** iç açılar toplamı, dış açı kuralı, "ok" şekli ve yükseklik–açıortay kuralıyla bir üçgendeki bilinmeyen açıyı en çok iki adımda bulabileceksin.

> **TYT'de yeri:** Geometri bölümünün ilk sorularında hemen her yıl bir "x kaç derecedir?" sorusu çıkar. Çoğu, iç açı toplamı ile dış açı kuralını art arda kullanarak çözülür. Bu ders sonraki bütün üçgen konularının temelidir.

## Önce hatırla

<details><summary>Geçen dersten: d₁ ∥ d₂ ve bir kesen d₁ ile 65°'lik açı yapıyor. Bu açının iç ters açısı ve karşı durumlu açısı kaç derecedir?</summary>
İç ters açısı <b>65°</b> (iç ters açılar eşittir), karşı durumlu açısı <b>115°</b> (karşı durumlu açıların toplamı 180°'dir). Bugün iç ters açıları, üçgenin iç açı toplamının neden 180° olduğunu göstermek için kullanacaksın.
</details>

<details><summary>Geçen dersten: [AB] ∥ [CD]. Aralarındaki kırık çizgi [AB] ile 30°, [CD] ile 45° yapıyor. Kırılma noktasındaki açı kaç derecedir?</summary>
30° + 45° = <b>75°</b>. Kırılma noktasındaki açı, iki uçtaki açının toplamıdır. Bugünkü "ok" şekli kuralı da aynı mantıkla çalışır.
</details>

## Üçgen ve gösterim

Aynı düzlemde bulunan ve aynı doğru üzerinde olmayan üç noktayı birleştiren doğru parçalarının oluşturduğu şekle **üçgen** denir. $A$, $B$, $C$ köşeler; $[AB]$, $[BC]$, $[CA]$ kenarlardır. $A$ köşesindeki iç açının ölçüsü $m(\widehat{A})$ ya da $m(\widehat{BAC})$ diye yazılır.

## 1. İç açılar toplamı: 180°

**Örnek.** Bir $ABC$ üçgeninde $m(\widehat{A}) = 70^\circ$ ve $m(\widehat{B}) = 45^\circ$ ise $m(\widehat{C})$ kaçtır?

**Çözüm.** $m(\widehat{C}) = 180^\circ - 70^\circ - 45^\circ = 65^\circ$.

**Neden 180°?** $A$'dan $[BC]$'ye paralel bir $d$ doğrusu çiz. $d$ üzerinde $A$'nın solunda oluşan açı $\widehat{B}$ ile, sağında oluşan açı $\widehat{C}$ ile iç ters açıdır; yani eşittir. $A$'daki üç açı yan yana bir doğru açı oluşturur: $45^\circ + 70^\circ + 65^\circ = 180^\circ$.

![ABC üçgeni: B'de 45, C'de 65, A'da 70 derece. A'dan BC'ye paralel kesikli d doğrusu geçiyor; d ile AB arasında 45, d ile AC arasında 65 derece işaretli.](gorsel/tyt-matematik/18-03-ic-acilar.svg "Aynı renkli açılar iç ters açıdır, eşittir. A noktasında mavi, kırmızı ve yeşil açı yan yana bir doğru açı (180°) oluşturur.")

**Kural:**

$$m(\widehat{A}) + m(\widehat{B}) + m(\widehat{C}) = 180^\circ$$

- Bu yüzden bir üçgende **en çok bir** dik ya da geniş açı bulunur. İki açı 90° olsaydı üçüncüye yer kalmazdı.
- Açılar oranla verilirse ($2:3:4$ gibi) önce $2k + 3k + 4k = 180^\circ$ ile $k$'yı bul ($k = 20^\circ$), sonra istenen açıyı hesapla: $40^\circ$, $60^\circ$, $80^\circ$.

## 2. Dış açı

Bir kenarı köşenin ötesine uzattığında, uzantı ile komşu kenar arasında kalan açıya **dış açı** denir.

**Örnek.** $ABC$ üçgeninde $m(\widehat{A}) = 50^\circ$ ve $m(\widehat{B}) = 60^\circ$. $[BC]$ kenarı $C$'nin ötesine uzatılıyor. $C$ köşesindeki dış açı kaç derecedir?

**Çözüm (uzun yol).** $m(\widehat{C}) = 180^\circ - 50^\circ - 60^\circ = 70^\circ$. İç açı ile dış açı bir doğru üzerinde yan yana olduğu için dış açı $180^\circ - 70^\circ = 110^\circ$.

**Çözüm (kısa yol).** Dış açı, kendisine komşu olmayan iki iç açının toplamıdır: $50^\circ + 60^\circ = 110^\circ$.

![ABC üçgeni: iç açılar A'da 50, B'de 60, C'de 70 derece. Her köşede bir kenar kesikli çizgiyle uzatılmış; dış açılar A'da 130, B'de 120, C'de 110 derece.](gorsel/tyt-matematik/18-03-dis-acilar.svg "Mavi: iç açılar, kırmızı: dış açılar. C'deki 110°, A ile B'nin toplamıdır (50 + 60). Üç kırmızı açının toplamı 360°'dir.")

**Kural:**

$$\text{dış açı} = \text{komşu olmayan iki iç açının toplamı}$$

$$\text{dış açılar toplamı} = 360^\circ$$

Neden 360°? Her köşede iç açı + dış açı $= 180^\circ$. Üç köşede bu $540^\circ$ eder; bundan iç açıların $180^\circ$'sini çıkarınca $360^\circ$ kalır. Şekilde: $130^\circ + 120^\circ + 110^\circ = 360^\circ$.

> **Tuzak:** Dış açı, **yanındaki** iç açıya değil, **karşıdaki** iki iç açının toplamına eşittir. Yanındaki iç açıyla toplamı $180^\circ$'dir.

## 3. "Ok" şekli (içbükey dörtgen)

Bir üçgenin içine bir $D$ noktası alıp $B$ ve $C$'yi $D$'ye bağlayınca ok ucuna benzeyen bir şekil oluşur.

**Örnek.** Şekilde $m(\widehat{BAC}) = 40^\circ$, $m(\widehat{ABD}) = 25^\circ$, $m(\widehat{ACD}) = 30^\circ$. $m(\widehat{BDC})$ kaçtır?

![Ok biçimli şekil: A tepede 40 derece, B'de AB ile BD arasında 25 derece, C'de AC ile CD arasında 30 derece, içerideki D noktasında 95 derece. BD kesikli çizgiyle uzatılıp AC'yi E'de kesiyor; E'deki açı 65 derece.](gorsel/tyt-matematik/18-03-ok-sekli.svg "İki adım: önce ABE üçgeninde E'deki dış açı 40 + 25 = 65°, sonra DEC üçgeninde D'deki dış açı 65 + 30 = 95°.")

**Çözüm.** $[BD]$'yi uzat, $[AC]$'yi $E$'de kessin.

1. $ABE$ üçgeninde $\widehat{BEC}$ dış açıdır: $m(\widehat{BEC}) = 40^\circ + 25^\circ = 65^\circ$.
2. $DEC$ üçgeninde $\widehat{BDC}$ dış açıdır: $m(\widehat{BDC}) = 65^\circ + 30^\circ = 95^\circ$.

**Kural:** İçteki açı, üç uçtaki açının toplamıdır.

$$m(\widehat{BDC}) = m(\widehat{A}) + m(\widehat{ABD}) + m(\widehat{ACD})$$

> **Tuzak:** Kural, $D$'deki **içteki** açı ($95^\circ$) içindir. $D$'nin öbür tarafındaki büyük açı ($360^\circ - 95^\circ = 265^\circ$) ile karıştırma. Soru tersten de gelir: $95^\circ$ verilir, uçtaki açılardan biri sorulur.

## 4. Yükseklik ile açıortay arasındaki açı

$[AH]$ **yükseklik**: $A$'dan $[BC]$'ye dik iner. $[AE]$ **açıortay**: $\widehat{A}$'yı iki eş parçaya böler.

**Örnek.** $ABC$ üçgeninde $m(\widehat{B}) = 72^\circ$, $m(\widehat{C}) = 38^\circ$. $[AH] \perp [BC]$ ve $[AE]$ açıortaydır. $m(\widehat{HAE}) = \alpha$ kaçtır?

![ABC üçgeni: B'de 72, C'de 38 derece. A'dan BC'ye dik inen mavi AH yüksekliği ve H'de dik açı işareti; A'dan çizilen yeşil AE açıortayı. AH ile AE arasındaki küçük açı alfa olarak işaretli.](gorsel/tyt-matematik/18-03-yukseklik-aciortay.svg "Yükseklik (mavi) büyük açıya yakın olan B tarafına düşer; açıortay (yeşil) ondan sonra gelir. Aradaki α açısı 17°'dir.")

**Çözüm.**

1. $m(\widehat{A}) = 180^\circ - 72^\circ - 38^\circ = 70^\circ$; açıortay olduğu için $m(\widehat{BAE}) = 35^\circ$.
2. $ABH$ dik üçgeninde $m(\widehat{BAH}) = 180^\circ - 90^\circ - 72^\circ = 18^\circ$.
3. $\alpha = 35^\circ - 18^\circ = 17^\circ$.

**Kısa yol:** $\alpha = \dfrac{72^\circ - 38^\circ}{2} = 17^\circ$.

**Kural:** Aynı köşeden çizilen yükseklik ile açıortay arasındaki açı, diğer iki köşedeki açıların farkının yarısıdır.

$$m(\widehat{HAE}) = \frac{|m(\widehat{B}) - m(\widehat{C})|}{2}$$

> **Tuzak:** Formülde tepe açısı ($\widehat{A}$) **yoktur**; yalnızca öbür iki açı vardır. Toplamın değil **farkın** yarısıdır. $m(\widehat{B}) = m(\widehat{C})$ ise fark $0$ olur: yükseklik ile açıortay çakışır.

## ÖSYM tuzakları

> **Yanındaki iç açıyla eşitlemek.** "$C$'deki dış açı $118^\circ$ ise $m(\widehat{C}) = 118^\circ$" yanlış. $m(\widehat{C}) = 62^\circ$'dir; $118^\circ$ ise $m(\widehat{A}) + m(\widehat{B})$'ye eşittir.

> **Dış açılar toplamında her köşeden bir açı alınır.** Bir köşede iki dış açı vardır ama bunlar ters açıdır, eşittir. Toplam $360^\circ$ ancak her köşeden **bir** dış açı alınınca çıkar.

> **$x$'i bulup durmak.** Açılar $2x + 10^\circ$, $3x$, $x + 20^\circ$ gibi verilirse önce $x$ bulunur; soru genelde bir **açıyı** ister. Seçeneklerde $x$'in değeri de bulunur.

> **Ok şeklinde yanlış açı.** $D$'deki açı uçtaki üç açının toplamıdır; içbükey taraftaki büyük açı değildir.

> **Yükseklik–açıortay formülüne tepe açısını katmak.** $\dfrac{m(\widehat{A})}{2}$ ya da $m(\widehat{B}) - m(\widehat{C})$ (ikiye bölmeden) seçeneklerde hazır bekler.

## Kendini dene

### Soru 1
Bir üçgenin iç açılarının ölçüleri $2x + 10^\circ$, $3x$ ve $x + 20^\circ$'dir. Bu üçgenin en büyük iç açısı kaç derecedir?

A) 25
B) 45
C) 60
D) 75
E) 85

**Cevap:** D
**Çözüm:** $(2x + 10) + 3x + (x + 20) = 180 \Rightarrow 6x + 30 = 180 \Rightarrow x = 25$. Açılar $60^\circ$, $75^\circ$, $45^\circ$; en büyüğü $75^\circ$. A seçeneği $x$'in kendisidir.

### Soru 2
$ABC$ üçgeninde $[BC]$ kenarı $C$'nin ötesine $D$ noktasına kadar uzatılıyor. $m(\widehat{ACD}) = 130^\circ$ ve $m(\widehat{A}) = 70^\circ$ ise $m(\widehat{B})$ kaç derecedir?

A) 50
B) 55
C) 60
D) 110
E) 130

**Cevap:** C
**Çözüm:** $\widehat{ACD}$, $C$'deki dış açıdır ve komşu olmayan iki iç açının toplamına eşittir: $70^\circ + m(\widehat{B}) = 130^\circ \Rightarrow m(\widehat{B}) = 60^\circ$. $50^\circ$ ise $m(\widehat{C})$'dir ($180^\circ - 130^\circ$).

### Soru 3
$ABC$ üçgeninde $m(\widehat{B}) = 80^\circ$ ve $m(\widehat{C}) = 30^\circ$'dir. $[AH] \perp [BC]$ ve $[AE]$, $\widehat{A}$'nın açıortayıdır ($H$ ve $E$, $[BC]$ üzerinde). $m(\widehat{HAE})$ kaç derecedir?

A) 10
B) 25
C) 35
D) 50
E) 55

**Cevap:** B
**Çözüm:** Kısa yol: $\dfrac{80^\circ - 30^\circ}{2} = 25^\circ$. Kontrol: $m(\widehat{A}) = 70^\circ$, $m(\widehat{BAE}) = 35^\circ$, $m(\widehat{BAH}) = 90^\circ - 80^\circ = 10^\circ$, fark $35^\circ - 10^\circ = 25^\circ$. $50^\circ$ ikiye bölmeyi unutmaktır; $35^\circ$ ise $\widehat{A}$'nın yarısıdır.

## Özet kartı

- İç açılar toplamı $180^\circ$; bir üçgende en çok bir dik ya da geniş açı olur.
- Dış açı = komşu olmayan iki iç açının toplamı; yanındaki iç açıyla toplamı $180^\circ$.
- Her köşeden birer dış açı: toplam $360^\circ$.
- Ok şekli: içteki açı = uçtaki üç açının toplamı.
- Yükseklik ile açıortay arası: $\dfrac{|m(\widehat{B}) - m(\widehat{C})|}{2}$.

## Sonraki adım

Alıştırmaya geç (aşağıdaki düğme). Sonraki ders: **İkizkenar ve Eşkenar Üçgende Açı Özellikleri**. Orada bugünkü kurallara "eş kenarların karşısındaki açılar eşittir" bilgisi eklenecek.
