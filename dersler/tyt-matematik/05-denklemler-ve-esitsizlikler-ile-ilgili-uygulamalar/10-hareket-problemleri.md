---
baslik: Hareket Problemleri
ders: tyt-matematik
sure: 25 dk
kaynak: MEBİ Konu Özeti a5770ab95d
guncelleme: 2026-11-17
---
# Hareket Problemleri

**Bu dersin sonunda:** yol = hız $\cdot$ zaman bağıntısıyla birim çevirebilecek, karşılaşma ve yetişme sürelerini bulabilecek ve ortalama hızı doğru hesaplayabileceksin.

> **TYT'de yeri:** Hemen her sınavda bir hareket sorusu olur. Kalıplar: "iki araç birbirine doğru çıkıyor, kaç saat sonra karşılaşır?", "arkadan çıkan araç öndekine ne zaman yetişir?", "gidiş dönüşte ortalama hız kaçtır?". Yeni nesil sorularda bilgi çoğu zaman bir **konum–zaman grafiğiyle** verilir.

## Önce hatırla

<details><summary>Karışım problemlerinden: %20'si tuz olan 40 kg tuzlu su ile %30'u tuz olan 60 kg tuzlu su karıştırılıyor. Yeni karışımın yüzde kaçı tuzdur?</summary>
Tuz miktarları toplanır: $40 \cdot \frac{20}{100} + 60 \cdot \frac{30}{100} = 8 + 18 = 26$ kg. Karışım $100$ kg, tuz oranı <b>%26</b>. Bu derste de aynı fikir var: oranları (hızları) değil, miktarları (yolları ve süreleri) toplayacaksın.
</details>

<details><summary>Karışım problemlerinden: %25'i şeker olan 60 g şerbete kaç gram su eklenirse şeker oranı %20 olur?</summary>
Şeker $60 \cdot \frac{25}{100} = 15$ g, su eklenince değişmez. $15 = \frac{20}{100}(60 + x)$, buradan $60 + x = 75$, $x = 15$ g. Değişmeyen miktarı sabit tutup denklemi kurmak hareket problemlerinde de işe yarar.
</details>

## Yol = hız · zaman

**Örnek.** Bir otomobil saatte 80 km sabit hızla 2,5 saat gidiyor. Kaç km yol alır? Aynı otomobil 150 km'yi saatte 60 km hızla kaç saatte alır?

$X = V \cdot t$ ile: $80 \cdot 2{,}5 = 200$ km. İkinci soruda $t = \frac{X}{V} = \frac{150}{60} = 2{,}5$ saat, yani **2 saat 30 dakika**.

**Kural.** $X$ yol, $V$ hız, $t$ zaman olmak üzere

$$X = V \cdot t \qquad V = \frac{X}{t} \qquad t = \frac{X}{V}$$

Birimler uyumlu olmalı: hız km/sa ise zaman saat, yol km olur.

**Birim çevirme.** $1 \text{ km} = 1000 \text{ m}$, $1 \text{ saat} = 60 \text{ dk} = 3600 \text{ sn}$.

| Hız | m/dk | m/sn |
|---|---|---|
| $72$ km/sa | $\frac{72\,000}{60} = 1200$ | $\frac{72\,000}{3600} = 20$ |
| $54$ km/sa | $900$ | $15$ |

km/sa'yi m/sn'ye çevirmek için $3{,}6$'ya böl; m/sn'yi km/sa'ye çevirmek için $3{,}6$ ile çarp.

**Orantılar.** Aynı bağıntıdan üç sonuç çıkar:

- Hız sabitse yol ile zaman **doğru** orantılıdır (2 katı sürede 2 katı yol).
- Yol sabitse hız ile zaman **ters** orantılıdır.
- Zaman sabitse yol ile hız **doğru** orantılıdır.

**Örnek.** Bir yolu saatte 60 km hızla giden araç, saatte 90 km hızla gidenden 1 saat geç varıyor. Yol kaç km?

Yol $x$ olsun. Süreler farkı 1 saat: $\frac{x}{60} - \frac{x}{90} = 1$. Paydaları eşitle: $\frac{3x - 2x}{180} = 1$, $x = 180$ km. Kontrol: $180 \div 60 = 3$ saat, $180 \div 90 = 2$ saat, fark 1 saat.

## Zıt yönlü hareket: karşılaşma

**Örnek.** A ile B şehirleri arası 420 km. Aynı anda A'dan saatte 80 km, B'den saatte 60 km hızla iki araç birbirine doğru yola çıkıyor. Kaç saat sonra karşılaşırlar?

Her saat aralarındaki uzaklık $80 + 60 = 140$ km azalır. $420 \div 140 = 3$ saat. Karşılaştıklarında A'dan çıkan $240$ km, B'den çıkan $180$ km yol almıştır; toplam $420$.

![Bir doğru parçası: solda A, sağda B, aralarında C noktası. A'daki mavi araç 80 km/sa ile sağa, B'deki sarı araç 60 km/sa ile sola gidiyor. Altta A ile C arası 240 km, C ile B arası 180 km, tamamı 420 km.](gorsel/tyt-matematik/05-10-zit-yon.svg "İki aracın aldığı yollar toplanınca AB uzaklığı çıkar. Her saat aradaki uzaklık 80 + 60 = 140 km kapanır.")

**Kural.** Birbirine doğru giden iki araç için karşılaşma süresi $t$ ise

$$|AB| = (V_1 + V_2) \cdot t$$

**Karşılaşmadan önce ve sonra.** Aynı araçlar için "kaç saat sonra aralarında 70 km olur?" sorusunun **iki** cevabı vardır:

- Karşılaşmadan önce: $(420 - 70) \div 140 = 2{,}5$ saat.
- Karşılaşıp birbirinden uzaklaşırken: $(420 + 70) \div 140 = 3{,}5$ saat.

## Aynı yönlü hareket: yetişme

**Örnek.** Aralarında 60 km bulunan iki araç aynı anda aynı yönde yola çıkıyor. Arkadaki saatte 90 km, öndeki saatte 70 km hızla gidiyor. Arkadaki öndekine kaç saat sonra yetişir?

Arkadaki her saat aradaki uzaklığın $90 - 70 = 20$ km'sini kapatır. $60 \div 20 = 3$ saat. Bu sürede arkadaki $270$ km, öndeki $210$ km gider: $270 = 60 + 210$.

![Bir yol üzerinde A, B ve C noktaları. A'daki mavi araç 90 km/sa, 60 km önündeki B'deki sarı araç 70 km/sa ile aynı yöne gidiyor. Altta B ile C arası 210 km, A ile C arası 270 km.](gorsel/tyt-matematik/05-10-ayni-yon.svg "Arkadaki araç aradaki 60 km'yi ve öndekinin gittiği 210 km'yi birlikte almak zorunda. Bu yüzden hızlar çıkarılır.")

**Kural.** Aynı yönde giden iki araçta $V_1 > V_2$ ve yetişme süresi $t$ ise

$$|AB| = (V_1 - V_2) \cdot t$$

**Biri sonra çıkarsa.** Bir araç saat 09.00'da saatte 60 km hızla yola çıkıyor; saat 10.00'da aynı yerden aynı yöne ikinci araç saatte 80 km hızla çıkıyor. İkinci araç çıktığında birincisi $60 \cdot 1 = 60$ km öndedir. Yetişme süresi $60 \div (80 - 60) = 3$ saat; yani saat **13.00**. Süreyi, ikinci aracın çıktığı andan saydığını unutma.

**Dairesel pist.** Pistte aynı kurallar geçerlidir; yol yerine **pistin çevresi** konur. 400 m'lik pistte aynı noktadan saniyede 5 m ve 3 m hızla koşan iki kişi:

- zıt yönde koşarlarsa $400 \div (5 + 3) = 50$ saniyede karşılaşır,
- aynı yönde koşarlarsa hızlı olan yavaşa $400 \div (5 - 3) = 200$ saniyede yetişir (bir tur fark atar).

## Ortalama hız

**Örnek.** Bir araç 120 km'lik yolu saatte 60 km hızla gidip saatte 40 km hızla geri dönüyor. Gidiş dönüşteki ortalama hızı kaçtır?

Gidiş $120 \div 60 = 2$ saat, dönüş $120 \div 40 = 3$ saat. Toplam yol $240$ km, toplam süre $5$ saat:

$$V_{ort} = \frac{240}{5} = 48 \text{ km/sa}$$

Hızların ortalaması olan 50 **değil**. Araç yavaş giderken daha çok zaman geçirdiği için ortalama yavaş hıza yakındır.

![Grafik: yatay eksen saat, dikey eksen alınan toplam yol. Mavi doğru 0'dan 2. saatte 120 km'ye, sarı doğru 2. saatten 5. saatte 240 km'ye çıkıyor. Kırmızı kesikli doğru başlangıçtan 5. saatte 240 km'ye gidiyor.](gorsel/tyt-matematik/05-10-ortalama-hiz.svg "Ortalama hız, başlangıçla bitişi birleştiren kesikli doğrunun eğimidir. Sarı parça daha uzun sürdüğü için ortalama 50 değil 48 olur.")

**Kural.**

$$V_{ort} = \frac{\text{Toplam yol}}{\text{Toplam zaman}}$$

Aynı yol $V_1$ hızıyla gidilip $V_2$ hızıyla dönülürse (ya da bir yolun **eşit iki yarısı** $V_1$ ve $V_2$ ile alınırsa) kısa yol:

$$V_{ort} = \frac{2 \cdot V_1 \cdot V_2}{V_1 + V_2}$$

Örnekte $\frac{2 \cdot 60 \cdot 40}{100} = 48$. Yolda mola varsa formül kullanılmaz: mola süresi toplam zamana eklenir.

## ÖSYM tuzakları

> **Dakikayı ondalık yazmak:** 2 saat 15 dakika $2{,}15$ saat değil, $2 + \frac{15}{60} = 2{,}25$ saattir. Tersine, $2{,}5$ saat 2 saat 50 dakika değil, 2 saat 30 dakikadır.

> **Zıt yönde hızları çıkarmak, aynı yönde toplamak:** Birbirine doğru gidenlerde aradaki uzaklık hızlar **toplamı** kadar, aynı yönde gidenlerde hızlar **farkı** kadar kapanır.

> **İkinci cevabı unutmak:** "Aralarında 70 km olduğunda" denince karşılaşmadan önceki ve sonraki an ayrı ayrı bulunur. Soru "karşılaştıktan sonra" diyorsa büyük olanı al.

> **Süreyi yanlış andan saymak:** Geç çıkan araç için bulunan yetişme süresi, **o aracın** çıktığı andan başlar. "Saat kaçta?" sorusunda bu süreyi ikinci aracın çıkış saatine ekle.

> **Hızların aritmetik ortalaması:** 60 ve 40 km/sa ile gidiş dönüşte ortalama hız 50 değil 48'dir. Toplam yolu toplam zamana böl.

## Kendini dene

### Soru 1
Saatte 90 km sabit hızla giden bir araç 210 km'lik yolu ne kadar sürede alır?

A) 2 saat 20 dakika
B) 2 saat 30 dakika
C) 2 saat 33 dakika
D) 2 saat 40 dakika
E) 3 saat

**Cevap:** A
**Çözüm:** $t = \frac{210}{90} = \frac{7}{3} = 2 + \frac{1}{3}$ saat. Saatin üçte biri $60 \div 3 = 20$ dakika: 2 saat 20 dakika. $2{,}33$'ü "2 saat 33 dakika" diye okuyan C'yi işaretler.

### Soru 2
Aralarında 40 km bulunan iki araç aynı anda aynı yönde yola çıkıyor. Arkadaki saatte 100 km, öndeki saatte 80 km hızla gidiyor.

Arkadaki araç öndekine yetiştiğinde kaç km yol almış olur?

A) 40
B) 160
C) 200
D) 360
E) 400

**Cevap:** C
**Çözüm:** Aynı yön: yetişme süresi $\frac{40}{100 - 80} = 2$ saat. Arkadaki $100 \cdot 2 = 200$ km gider. 160 km öndekinin aldığı yoldur ($80 \cdot 2$); $200 = 40 + 160$ ile kontrol edilir.

### Soru 3
Bir araç bir yolu saatte 40 km hızla gidip aynı yoldan saatte 60 km hızla geri dönüyor.

Bu aracın gidiş dönüşteki ortalama hızı saatte kaç km'dir?

A) 24
B) 45
C) 48
D) 50
E) 100

**Cevap:** C
**Çözüm:** $V_{ort} = \frac{2 \cdot 40 \cdot 60}{40 + 60} = \frac{4800}{100} = 48$. Kontrol için yolu 120 km al: gidiş 3, dönüş 2 saat; $240 \div 5 = 48$. 50 hızların aritmetik ortalamasıdır, yanlıştır.

## Özet kartı

- $X = V \cdot t$; birimleri uyumlu yaz. km/sa $\div 3{,}6$ = m/sn.
- Yol sabitse hız ile zaman ters orantılıdır.
- Zıt yönde (karşılaşma): $|AB| = (V_1 + V_2) \cdot t$.
- Aynı yönde (yetişme): $|AB| = (V_1 - V_2) \cdot t$. Pistte $|AB|$ yerine pist çevresi.
- $V_{ort} = \frac{\text{toplam yol}}{\text{toplam zaman}}$; gidiş dönüşte $\frac{2V_1V_2}{V_1 + V_2}$.

## Sonraki adım

Alıştırmaya geç (aşağıdaki düğme). Grafikli sorularda önce iki eksenin neyi gösterdiğini oku; bir doğrunun eğimi o aracın hızıdır.
