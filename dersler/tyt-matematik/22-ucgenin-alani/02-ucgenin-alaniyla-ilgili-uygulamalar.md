---
baslik: Üçgenin Alanıyla İlgili Uygulamalar
ders: tyt-matematik
sure: 25 dk
kaynak: MEBİ Konu Özeti dd9cd726d3
guncelleme: 2026-11-18
---
# Üçgenin Alanıyla İlgili Uygulamalar

<div class="giris" dir="rtl" lang="ar">

**الدرس ده عن إيه؟** عن تطبيقات على مساحة المثلث (üçgenin alanı): إزاي تقارن مساحات مثلثات ببعض من غير ما تحسب كل واحدة لوحدها.

- هتعرف إن المثلثات اللي ليها نفس الارتفاع (yükseklik) نسبة مساحاتها هي نسبة قواعدها (taban)، واللي ليها نفس القاعدة نسبة مساحاتها هي نسبة ارتفاعاتها.
- هتتعلم إن المتوسطات (kenarortay) بتقسم المثلث لست حتت مساحتهم متساوية حوالين مركز الثقل (ağırlık merkezi)، وإن نسبة مساحات المثلثات المتشابهة (benzer üçgenler) هي مربع نسبة التشابه.
- هتحسب المساحة من ضلعين والزاوية اللي بينهم باستخدام الجيب (sinüs).

**ليه مهم؟** أسئلة نسب المساحات دي بتيجي كتير في TYT، وبتتحل في سطرين لو عرفت القاعدة الصح. الغلطة المشهورة إنك تنسى تربّع نسبة التشابه.

الدرس ٢٥ دقيقة، وكل قاعدة معاها رسمة ومثال محلول. بص على الرسومات كويس وهتلاقي الموضوع أسهل مما تتخيل.

</div>

**Bu dersin sonunda:** iki üçgenin alanlarını hesaplamadan oranlayabilecek (ortak yükseklik, ortak taban, ağırlık merkezi, benzerlik) ve iki kenarı ile aradaki açısı bilinen üçgenin alanını $\frac{1}{2} \cdot b \cdot c \cdot \sin A$ ile bulabileceksin.

> **TYT'de yeri:** Geometri sorularında alan çoğu zaman bir oran olarak sorulur: "taralı bölgenin alanı kaçtır?", "$A(ADE)$ kaçtır?" Şekilde bir köşeden karşı kenara çizilmiş bir doğru, bir ağırlık merkezi ya da tabana paralel bir doğru vardır. Hesap kısadır; asıl iş, hangi iki üçgenin ortak yüksekliği ya da ortak açısı olduğunu görmektir.

## Önce hatırla

<details><summary>Geçen dersten: Bir üçgenin bir kenarı 12 birim, bu kenara ait yükseklik 7 birimdir. Alanı kaç birimkaredir?</summary>
$\dfrac{12 \cdot 7}{2} = 42$ birimkare. Formülde yalnızca taban ve yükseklik var. Bugünkü ilk iki kuralın kaynağı bu: yükseklik ortaksa alanı yalnızca taban belirler.
</details>

<details><summary>Geçen dersten: Kenarı 4 birim olan eşkenar üçgenin alanı kaç birimkaredir?</summary>
$\dfrac{a^2\sqrt{3}}{4} = \dfrac{16\sqrt{3}}{4} = 4\sqrt{3}$ birimkare. Bugün aynı sonucu "iki kenar ve aradaki açı" formülüyle de bulacaksın.
</details>

## 1. Aynı yükseklik: alanlar tabanlarla orantılı

**Örnek 1.** $ABC$ üçgeninde $D$ noktası $[BC]$ üzerindedir. $|BD| = 6$, $|DC| = 4$ ve $A(ABC) = 40$ birimkaredir. $A(ABD)$ ve $A(ADC)$ kaçtır?

**Çözüm.**

1. $ABD$ ve $ADC$ üçgenlerinin ikisinin de tepesi $A$, tabanları aynı $BC$ doğrusu üzerinde. Yani ikisinin yüksekliği de aynı $|AH| = h$ parçasıdır.
2. $A(ABD) = \dfrac{6 \cdot h}{2}$ ve $A(ADC) = \dfrac{4 \cdot h}{2}$. Oranları: $\dfrac{A(ABD)}{A(ADC)} = \dfrac{6}{4} = \dfrac{3}{2}$.
3. $40$ birimkareyi $3 : 2$ oranında paylaştır: $A(ABD) = 40 \cdot \dfrac{6}{10} = 24$, $A(ADC) = 40 \cdot \dfrac{4}{10} = 16$.

![ABC üçgeni; A'dan BC'ye kırmızı kesikli h yüksekliği iniyor. D, BC üzerinde; BD = 6, DC = 4. ABD yeşil, alanı 24; ADC mavi, alanı 16.](gorsel/tyt-matematik/22-02-ayni-yukseklik.svg "Tek bir kırmızı yükseklik iki üçgene de aittir. Bu yüzden alanları 6'ya 4 oranında: 24 ve 16.")

**Kural:** Tepesi ortak ve tabanları aynı doğru üzerinde olan üçgenlerin yükseklikleri aynıdır; alanları tabanlarıyla orantılıdır.

$$\frac{A(ABD)}{A(ADC)} = \frac{|BD|}{|DC|}$$

Özel durum: $[AD]$ kenarortaysa ($|BD| = |DC|$) üçgeni **iki eşit alana** böler.

> **Tuzak:** Oranı yanlış parçalarla kurmak. $A(ABD)$, $A(ABC)$'nin $\dfrac{6}{4}$'ü değil, $\dfrac{6}{10}$'udur. Parçayı parçayla, parçayı bütünle karşılaştırdığını karıştırma. Bir de: $|AB|$ ve $|AC|$ kenarlarının oranı bu kuralda işe yaramaz; oranı **tabanlar** verir.

## 2. Ortak taban: alanlar yüksekliklerle orantılı

**Örnek 2.** $ABC$ ve $DBC$ üçgenlerinin tabanı ortaktır: $[BC]$. $A$'dan $BC$ doğrusuna inen yükseklik $|AE| = 8$, $D$'den inen yükseklik $|DF| = 6$ birimdir. $A(ABC) = 36$ ise $A(DBC)$ kaçtır?

**Çözüm.**

1. İki üçgenin tabanı aynı uzunlukta: $|BC|$. Değişen yalnızca yükseklik.
2. $\dfrac{A(ABC)}{A(DBC)} = \dfrac{\frac{|BC| \cdot 8}{2}}{\frac{|BC| \cdot 6}{2}} = \dfrac{8}{6} = \dfrac{4}{3}$.
3. $A(DBC) = 36 \cdot \dfrac{3}{4} = 27$. Kontrol: $36 = \dfrac{|BC| \cdot 8}{2}$ ise $|BC| = 9$; $\dfrac{9 \cdot 6}{2} = 27$.

![Ortak BC = 9 tabanı üzerinde iki üçgen: yeşil ABC, yüksekliği AE = 8; mavi DBC, yüksekliği DF = 6. F, BC'nin C'den ötesine uzatılmış kesikli doğru üzerinde.](gorsel/tyt-matematik/22-02-ortak-taban.svg "Kalın siyah taban iki üçgende ortaktır. Alanları yüksekliklerin oranında: 8'e 6, yani 36 ve 27.")

**Kural:** Tabanları ortak (ya da eşit) olan üçgenlerin alanları yükseklikleriyle orantılıdır.

$$\frac{A(ABC)}{A(DBC)} = \frac{|AE|}{|DF|}$$

Geçen dersten hatırla: $D$, $[BC]$'ye paralel bir doğru üzerinde kayarsa yükseklik değişmez, alan da değişmez.

> **Tuzak:** Yükseklik yerine eğik kenarları oranlamak. $\dfrac{|AB|}{|DB|}$ ya da $\dfrac{|AC|}{|DC|}$ alan oranı **değildir**. Yükseklik dışarıya düşse bile ($F$ noktası gibi) oranlanacak olan, taban doğrusuna inen dik parçalardır.

## 3. Kenarortaylar ve ağırlık merkezi: altı eşit parça

**Örnek 3.** $A(ABC) = 48$ birimkaredir. $D$, $E$, $F$ sırasıyla $[AB]$, $[AC]$, $[BC]$ kenarlarının orta noktaları, $G$ ağırlık merkezidir. $A(GBF)$ ve $A(GBC)$ kaçtır?

**Çözüm.**

1. $[AF]$ kenarortaydır: $A(ABF) = A(AFC) = \dfrac{48}{2} = 24$ (1. kural, eşit tabanlar).
2. $G$, $[AF]$'yi köşeden itibaren $2 : 1$ böler: $|AG| = 2|GF|$. $ABG$ ile $GBF$ üçgenlerinin tepesi ortak ($B$), tabanları $AF$ doğrusu üzerinde. Alanları $2 : 1$: $A(ABG) = 16$, $A(GBF) = 8$.
3. Aynı akıl yürütme her kenarortay için geçerli. Altı küçük üçgenin her biri $8$ birimkare.
4. $GBC$ üçgeni bunların ikisidir: $A(GBC) = 8 + 8 = 16$, yani bütün alanın $\dfrac{1}{3}$'ü.

![ABC üçgeninin üç kenarortayı G ağırlık merkezinde kesişiyor. D, E, F orta noktalar; çentikler eşit parçaları gösteriyor. Oluşan altı küçük üçgenin her birinde S yazıyor; renkler sarı ve mavi sırayla.](gorsel/tyt-matematik/22-02-agirlik-merkezi.svg "Altı parçanın biçimi farklı, alanı aynı: her biri S. G'nin bir kenarla oluşturduğu üçgen iki parçadır: 2S.")

**Kural:** Üç kenarortay üçgeni alanları eşit **altı** üçgene ayırır. $A(ABC) = 6S$ ise:

| Bölge | Alan |
|---|---|
| Küçük üçgenlerden biri, örneğin $GBF$ | $S = \dfrac{A(ABC)}{6}$ |
| $GBC$, $GAC$, $GAB$ | $2S = \dfrac{A(ABC)}{3}$ |
| $ABF$ gibi kenarortayın ayırdığı yarı | $3S = \dfrac{A(ABC)}{2}$ |
| $ADGE$ gibi dörtgen (iki parça) | $2S$ |

> **Tuzak:** $A(GBC)$'yi bütünün yarısı sanmak. Yarısı $ABF$'dir; $G$ ağırlık merkezi olduğu için $GBC$ yalnızca $\dfrac{1}{3}$'tür. Parçaları say: $GBC$ iki parça, $ABF$ üç parça.

## 4. Benzer üçgenler: alan oranı $k^2$

**Örnek 4.** $ABC$ üçgeninde $D \in [AB]$, $E \in [AC]$ ve $[DE] \parallel [BC]$'dir. $|AD| = 4$, $|DB| = 2$ ve $A(ABC) = 18$ birimkaredir. $A(ADE)$ ve $DBCE$ yamuğunun alanı kaçtır?

**Çözüm.**

1. $[DE] \parallel [BC]$ olduğu için $ADE \sim ABC$. Benzerlik oranı küçük üçgenin kenarının büyüğün **aynı kenarına** oranıdır: $k = \dfrac{|AD|}{|AB|} = \dfrac{4}{6} = \dfrac{2}{3}$.
2. Bütün uzunluklar (kenarlar, yükseklikler) $k$ oranında küçülür. Alan iki uzunluğun çarpımı olduğu için $k \cdot k = k^2$ oranında küçülür: $\dfrac{A(ADE)}{A(ABC)} = \left(\dfrac{2}{3}\right)^2 = \dfrac{4}{9}$.
3. $A(ADE) = 18 \cdot \dfrac{4}{9} = 8$. Yamuk: $18 - 8 = 10$.

![ABC üçgeninde BC'ye paralel mavi DE doğru parçası. AD = 4, DB = 2. Üstteki ADE üçgeni mavi, alttaki DBCE yamuğu sarı.](gorsel/tyt-matematik/22-02-benzer.svg "Kenar oranı 4'e 6, yani 2/3. Alan oranı onun karesi: 4/9. Mavi üçgen 8, sarı yamuk 10.")

**Kural:** İki üçgen benzer ve benzerlik oranı $k$ ise

$$\frac{A(\text{küçük})}{A(\text{büyük})} = k^2$$

Kenar, yükseklik, kenarortay, çevre: hepsi $k$ oranında. Yalnızca alan $k^2$ oranında.

> **Tuzak:** İki yanlış birden: $k$'yi $\dfrac{|AD|}{|DB|} = 2$ almak (doğrusu $\dfrac{|AD|}{|AB|}$) ve oranın karesini almayı unutmak. $\dfrac{2}{3}$ ile çarpsaydın $A(ADE) = 12$ bulurdun. Soru yamuğu soruyorsa çıkarmayı da unutma.

## 5. İki kenar ve aradaki açı: $\frac{1}{2} \cdot b \cdot c \cdot \sin A$

**Örnek 5.** $ABC$ üçgeninde $|AB| = 8$, $|AC| = 6$ ve $m(\widehat{A}) = 30^\circ$'dir. $A(ABC)$ kaçtır? $m(\widehat{A}) = 150^\circ$ olsaydı alan ne olurdu?

**Çözüm.**

1. $[AB]$'yi taban al. $C$'den $AB$ doğrusuna dikme indir: $[CH]$.
2. $AHC$ dik üçgeninde $\sin 30^\circ = \dfrac{|CH|}{|AC|}$, yani $|CH| = 6 \cdot \sin 30^\circ = 6 \cdot \dfrac{1}{2} = 3$.
3. $A(ABC) = \dfrac{8 \cdot 3}{2} = 12$. Bunu tek satırda yazarsan: $\dfrac{1}{2} \cdot 8 \cdot 6 \cdot \sin 30^\circ = 12$.
4. $m(\widehat{A}) = 150^\circ$ ise dikme $AB$'nin $A$'dan öteye uzantısına düşer. $AHC$ dik üçgeninde $A$'daki açı $180^\circ - 150^\circ = 30^\circ$ olur; yükseklik yine $6 \cdot \sin 30^\circ = 3$, alan yine $12$.

![Üstte AB = 8, AC = 6 ve A açısı 30 derece olan üçgen; C'den AB'ye kırmızı CH = 3 dikmesi. Altta aynı kenarlarla A açısı 150 derece; dikme AB'nin A'dan öteye uzatılmış kesikli kısmına iniyor, CH yine 3.](gorsel/tyt-matematik/22-02-sinus.svg "İki üçgende de C'nin AB doğrusuna uzaklığı 3. Taban da 8 olduğu için iki alan da 12: sin 150° = sin 30°.")

**Kural:** İki kenarı ve **bu iki kenarın arasındaki** açısı bilinen üçgende

$$A(ABC) = \frac{1}{2} \cdot b \cdot c \cdot \sin A$$

Bir açı ile onun bütünleri aynı alanı verir: $\sin(180^\circ - \alpha) = \sin \alpha$.

| Açı | $30^\circ$ ya da $150^\circ$ | $45^\circ$ ya da $135^\circ$ | $60^\circ$ ya da $120^\circ$ | $90^\circ$ |
|---|---|---|---|---|
| $\sin$ | $\dfrac{1}{2}$ | $\dfrac{\sqrt{2}}{2}$ | $\dfrac{\sqrt{3}}{2}$ | $1$ |

Kontrol: kenarı $a$ olan eşkenar üçgende $\dfrac{1}{2} \cdot a \cdot a \cdot \sin 60^\circ = \dfrac{a^2\sqrt{3}}{4}$, geçen dersteki formül. $\sin A$ en çok $1$ olduğu için iki kenarı belli üçgenin alanı en büyük değerini aradaki açı $90^\circ$ iken alır.

> **Tuzak:** $\sin$ yerine $\cos$ kullanmak ya da $\dfrac{1}{2}$'yi unutmak. $120^\circ$ ve $150^\circ$ gibi geniş açılarda alanı negatif ya da sıfır sanma; $\sin 120^\circ = \dfrac{\sqrt{3}}{2}$, $\sin 150^\circ = \dfrac{1}{2}$. Açı mutlaka iki kenarın **arasındaki** açı olmalı.

## 6. Ortak açılı üçgenler: kenar çarpımlarının oranı

**Örnek 6.** $ABC$ üçgeninde $D \in [AB]$ ve $E \in [AC]$'dir. $|AD| = 3$, $|DB| = 1$, $|AE| = 2$ ve $|EC| = 4$ birimdir. $\dfrac{A(ADE)}{A(ABC)}$ oranı kaçtır?

**Çözüm.**

1. $\widehat{A}$ açısı iki üçgende ortak. $[DE]$, $[BC]$'ye paralel değil; benzerlik yok.
2. İki alanı da 5. kuralla yaz: $A(ADE) = \dfrac{1}{2} \cdot 3 \cdot 2 \cdot \sin A$ ve $A(ABC) = \dfrac{1}{2} \cdot 4 \cdot 6 \cdot \sin A$.
3. Oranlayınca $\dfrac{1}{2}$ ve $\sin A$ sadeleşir: $\dfrac{3 \cdot 2}{4 \cdot 6} = \dfrac{6}{24} = \dfrac{1}{4}$. Açının kaç derece olduğunu bilmen gerekmedi.

![ABC üçgeninde D, AB üzerinde (AD = 3, DB = 1), E, AC üzerinde (AE = 2, EC = 4). A açısı yayla işaretli. ADE üçgeni mavi, DBCE dörtgeni sarı; DE, BC'ye paralel değil.](gorsel/tyt-matematik/22-02-ortak-aci.svg "Mavi ve bütün üçgen A açısını paylaşıyor. Alan oranı, A'dan çıkan kenarların çarpımlarının oranıdır: 3·2'ye karşı 4·6.")

**Kural:** Bir açısı ortak olan iki üçgende

$$\frac{A(ADE)}{A(ABC)} = \frac{|AD| \cdot |AE|}{|AB| \cdot |AC|}$$

$[DE] \parallel [BC]$ ise iki oran da $k$ olur ve bu formül 4. kuraldaki $k^2$'ye döner.

> **Tuzak:** Parçaları bütün kenar sanmak. Paydada $|DB| \cdot |EC| = 1 \cdot 4$ değil, $|AB| \cdot |AC| = 4 \cdot 6$ vardır. Sonra istenen dörtgense: $A(DBCE) = A(ABC) - A(ADE)$, oranı $\dfrac{3}{4}$.

## Hangi kural ne zaman?

| Şekilde ne görüyorsun? | Kullan |
|---|---|
| Bir köşeden karşı kenara çizilmiş doğru | Alanlar tabanlarla orantılı |
| Aynı tabana farklı yükseklikten bakan iki üçgen | Alanlar yüksekliklerle orantılı |
| Ağırlık merkezi, kenarortaylar | Altı eşit parça: $S$ |
| Tabana paralel doğru | Alan oranı $k^2$ |
| İki kenar ve aradaki açı | $\frac{1}{2} \cdot b \cdot c \cdot \sin A$ |
| İki kenar üzerinde birer nokta, ortak köşe | Kenar çarpımlarının oranı |

## ÖSYM tuzakları

> **Benzerlikte karesini almamak.** Kenarlar $2$ katına çıkınca alan $4$ katına çıkar. Seçeneklerde $k$ ile hesaplanmış yanlış sonuç hemen her zaman vardır.

> **Parça ile bütünü karıştırmak.** $|AD| : |DB| = 2 : 1$ ise $k = \dfrac{|AD|}{|AB|} = \dfrac{2}{3}$'tür, $2$ değil. Aynısı tabanlarda: $|BD| : |DC| = 3 : 2$ ise $A(ABD)$ bütünün $\dfrac{3}{5}$'idir.

> **$A(GBC)$'yi yarı sanmak.** Ağırlık merkezinin bir kenarla kurduğu üçgen bütünün $\dfrac{1}{3}$'üdür. Altı parçayı say.

> **Geniş açıda takılmak.** $\sin 150^\circ = \sin 30^\circ = \dfrac{1}{2}$. "Alan $10$, kenarlar $4$ ve $10$; aradaki açı kaç olabilir?" sorusunda seçeneklerde $30^\circ$ yoksa cevap $150^\circ$'dir.

> **Yanlış açıyı almak.** $\frac{1}{2} \cdot b \cdot c \cdot \sin A$ formülündeki açı, $b$ ve $c$ kenarlarının **arasındaki** açıdır. Başka bir köşenin açısıyla yazılmaz.

## Kendini dene

### Soru 1
$ABC$ üçgeninde $D \in [AB]$, $E \in [AC]$ ve $[DE] \parallel [BC]$'dir. $|AD| = 2$ cm, $|DB| = 4$ cm ve $A(ADE) = 4$ cm² ise $DBCE$ yamuğunun alanı kaç cm²'dir?

A) 8
B) 12
C) 16
D) 32
E) 36

**Cevap:** D
**Çözüm:** $k = \dfrac{|AD|}{|AB|} = \dfrac{2}{6} = \dfrac{1}{3}$, alan oranı $\dfrac{1}{9}$. $A(ABC) = 4 \cdot 9 = 36$, yamuk $36 - 4 = 32$. $36$, çıkarmayı unutmaktır; $8$, karesini almadan ($A(ABC) = 12$) bulunur; $16$ ve $12$ ise $k$'yi $\dfrac{|AD|}{|DB|} = \dfrac{1}{2}$ alıp $A(ABC) = 16$ bulmaktan gelir.

### Soru 2
$ABC$ üçgeninin ağırlık merkezi $G$'dir. $AG$ doğrusu $[BC]$'yi $D$ noktasında kesiyor. $A(ABC) = 60$ birimkare ise $A(GBD)$ kaç birimkaredir?

A) 10
B) 12
C) 15
D) 20
E) 30

**Cevap:** A
**Çözüm:** $G$'den geçtiği için $[AD]$ kenarortaydır; $D$, $[BC]$'nin orta noktası. Üç kenarortay üçgeni altı eşit parçaya ayırır ve $GBD$ bunlardan biridir: $\dfrac{60}{6} = 10$. $20$, $A(GBC)$'dir (iki parça); $30$, $A(ABD)$'dir (üç parça).

### Soru 3
$ABC$ üçgeninde $|AB| = 10$ cm, $|AC| = 4$ cm ve $m(\widehat{A}) = 135^\circ$'dir. $A(ABC)$ kaç cm²'dir?

A) 10
B) $10\sqrt{2}$
C) $10\sqrt{3}$
D) 20
E) $20\sqrt{2}$

**Cevap:** B
**Çözüm:** $\sin 135^\circ = \sin 45^\circ = \dfrac{\sqrt{2}}{2}$. $A(ABC) = \dfrac{1}{2} \cdot 10 \cdot 4 \cdot \dfrac{\sqrt{2}}{2} = 10\sqrt{2}$. $20\sqrt{2}$, $\dfrac{1}{2}$'yi unutmaktır; $10\sqrt{3}$, $\sin 120^\circ$ ile karıştırmak; $10$ ise $\sin 150^\circ$ değerini kullanmaktır.

## Özet kartı

- Tepesi ortak, tabanları aynı doğruda: alan oranı = taban oranı. Kenarortay alanı ikiye böler.
- Tabanı ortak: alan oranı = yükseklik oranı.
- Kenarortaylar altı eşit parça verir: her biri $\dfrac{A}{6}$; $A(GBC) = \dfrac{A}{3}$.
- Benzerlik oranı $k$ ise alan oranı $k^2$; $k$ parçanın **bütüne** oranıdır.
- $A = \frac{1}{2} \cdot b \cdot c \cdot \sin A$; $\sin(180^\circ - \alpha) = \sin \alpha$.
- Ortak açılı üçgenler: alan oranı = ortak köşeden çıkan kenarların çarpımlarının oranı.

## Sonraki adım

Alıştırmaya geç (aşağıdaki düğme). Sonraki konu: **Çokgenler**. Bir çokgeni köşegenlerle üçgenlere bölmek, iç açılar toplamını ve alanı bulmanın temel yoludur; bugünkü alan oranları orada da işine yarayacak.
