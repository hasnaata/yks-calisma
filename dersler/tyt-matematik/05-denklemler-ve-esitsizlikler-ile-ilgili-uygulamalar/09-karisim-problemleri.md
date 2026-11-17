---
baslik: Karışım Problemleri
ders: tyt-matematik
sure: 20 dk
kaynak: MEBİ Konu Özeti d329034d67
guncelleme: 2026-11-17
---
# Karışım Problemleri

**Bu dersin sonunda:** saf madde miktarını sabit tutarak su ekleme, buharlaştırma, dökme ve iki karışımı birleştirme sorularını tek denklemle çözebileceksin.

> **TYT'de yeri:** Sık gelmez ama geldiğinde kolay puandır. Kalıplar: "yeni karışımın tuz yüzdesi kaçtır?", "kaç gram su buharlaştırılmalıdır?", "%… lik karışımdan kaç gram eklenmelidir?". Yeni nesil sorularda tuz yerine şeker, alkol, meyve suyu ya da altın ayarı gelir; hesap aynıdır. Asıl sınanan şey yine: **yüzdenin hangi bütünün üzerinden alındığı.**

## Önce hatırla

<details><summary>Kâr-zarar problemlerinden: Bir ürün %20 kârla 180 TL'ye satılıyor. Maliyeti kaç TL'dir?</summary>
Maliyet $100x$ ise satış $120x = 180$, $x = 1{,}5$; maliyet $150$ TL. $180 \cdot 0{,}8 = 144$ yanlıştır, çünkü %20 satışın değil maliyetin yüzdesidir. Bu derste yüzdenin tabanı **karışımın tamamı** olacak.
</details>

<details><summary>Kâr-zarar problemlerinden: Etiket fiyatı maliyetin %50 fazlası olan bir ürün, etiket üzerinden %20 indirimle satılıyor. Kâr yüzdesi kaçtır?</summary>
Maliyet $100x$, etiket $150x$, satış $150x \cdot 0{,}8 = 120x$: **%20 kâr**. $50 - 20 = 30$ değil; her adımda taban değişti. Karışımda da su eklenince taban (karışım) değişir, tuz değişmez.
</details>

## Saf madde yüzdesi

**Örnek.** 200 g tuzlu suyun 30 g'ı tuzdur. Tuz yüzdesi kaçtır?

Tuz yüzdesi, tuzun **karışımın tamamına** oranıdır: $\frac{30}{200} \cdot 100 = 15$, yani **%15**. Su $200 - 30 = 170$ g'dır ve suyun yüzdesi %85'tir.

**Kural.**

$$\text{Saf madde yüzdesi} = \frac{\text{saf madde miktarı}}{\text{karışım miktarı}} \cdot 100$$

Ters yönde: %$a$'lık $M$ gram karışımda saf madde $M \cdot \frac{a}{100}$ gramdır. Karışım problemlerinin hepsi bu satırdan başlar: **önce saf madde miktarını yaz.**

> Tuzu suya bölmek ($\frac{30}{170}$) en sık hatadır. Payda her zaman karışımın tamamıdır: tuz + su.

## Su eklemek, su buharlaştırmak, tuz eklemek

**Örnek.** %20'lik 300 g tuzlu su var; içinde $300 \cdot 0{,}2 = 60$ g tuz bulunur.

- **100 g su eklenirse:** tuz yine 60 g, karışım 400 g: $\frac{60}{400} \cdot 100 = 15$, **%15**.
- **60 g su buharlaşırsa:** tuz yine 60 g, karışım 240 g: $\frac{60}{240} \cdot 100 = 25$, **%25**.
- **20 g tuz eklenirse:** tuz 80 g, karışım 320 g: $\frac{80}{320} \cdot 100 = 25$, **%25**.

![Üç yatay çubuk. Her birinin solunda 60 yazan koyu mavi tuz parçası aynı genişlikte. Başlangıçta açık mavi su 240, toplam 300 g ve yüzde 20. 100 g su eklenince su 340, toplam 400 g ve yüzde 15. 60 g su gidince su 180, toplam 240 g ve yüzde 25.](gorsel/tyt-matematik/05-09-su-ekleme.svg "Koyu parça hiç değişmiyor. Yalnızca su uzayıp kısalıyor; bu yüzden yüzde değişiyor.")

**Kural.** Su eklemek ya da buharlaştırmak **tuz miktarını değiştirmez**, yalnızca karışım miktarını değiştirir. Denklem:

$$\frac{\text{tuz}}{\text{karışım} \pm \text{su}} = \text{yeni oran}$$

Su eklemeyi de karıştırma gibi düşünebilirsin: su, **%0 tuzlu** bir karışımdır; eklenen saf tuz ise **%100 tuzlu** bir karışımdır. Soru suyun yüzdesini soruyorsa tersine, su %100 alınır.

## İki karışımı birleştirmek

**Örnek.** %10'luk 200 g tuzlu su ile %25'lik 100 g tuzlu su karıştırılıyor. Yeni karışımın tuz yüzdesi kaçtır?

Tuzları ayrı ayrı bul, topla, toplam karışıma böl:

$$\text{tuz} = 200 \cdot 0{,}10 + 100 \cdot 0{,}25 = 20 + 25 = 45 \text{ g}, \qquad \frac{45}{300} \cdot 100 = 15$$

Yeni karışım **%15**'liktir; $\frac{10 + 25}{2} = 17{,}5$ değil.

![Üç sütun, yükseklikleri kütleyle orantılı. 200 g ve yüzde 10 olan sütunun altında 20 g tuz; artı; 100 g ve yüzde 25 olan sütunun altında 25 g tuz; eşittir; 300 g ve yüzde 15 olan sütunun altında 45 g tuz.](gorsel/tyt-matematik/05-09-karistirma.svg "Toplanan şey yüzdeler değil, gramlar: 20 + 25 = 45 g tuz, 200 + 100 = 300 g karışım.")

**Kural.** %$x$'lik $A$ gram ile %$y$'lik $B$ gram karıştırılınca %$z$'lik $A + B$ gram oluşur:

$$A \cdot x + B \cdot y = (A + B) \cdot z$$

Bilinmeyen miktar olsa da denklem aynıdır. **Örnek:** %10'luk 300 g tuzlu suya %40'lık tuzlu sudan kaç gram eklenirse %20'lik karışım elde edilir?

$$300 \cdot 10 + m \cdot 40 = (300 + m) \cdot 20 \;\Rightarrow\; 3000 + 40m = 6000 + 20m \;\Rightarrow\; m = 150 \text{ g}$$

Kontrol: tuz $30 + 60 = 90$ g, karışım $450$ g, $\frac{90}{450} = 0{,}2$. Doğru.

## Kısa yol: karışım, çok olana yakındır

Yeni yüzde her zaman iki yüzdenin **arasındadır** ve miktarı çok olan karışımın yüzdesine **daha yakındır**. Uzaklıklar, miktarlarla **ters orantılıdır**.

![Sayı doğrusunda 10, 15 ve 25. 10'un üstünde 200 g, 25'in üstünde 100 g, ortada yeşil karışım noktası 15. Altta 10 ile 15 arası 5, 15 ile 25 arası 10. Üstte: uzaklıklar 1'e 2, miktarlar 2'ye 1.](gorsel/tyt-matematik/05-09-denge.svg "Sayılar tuz yüzdesi. 200 g olan taraf iki kat ağır, karışım ona iki kat yakın: uzaklık 5'e 10.")

İkinci örnekte de böyle: 20, 10'a $10$, 40'a $20$ uzaklıkta; uzaklıklar $1 : 2$ ise miktarlar $2 : 1$, yani $300 : 150$. Bu yol seçenek elemek ve sonucu kontrol etmek için çok hızlıdır. Seçeneklerde iki yüzdenin dışında kalan bir değer varsa hemen ele.

## Dökmek oranı değiştirmez

**Örnek.** %20'lik 500 g tuzlu suyun 100 g'ı dökülüyor, sonra kaba 100 g su ekleniyor. Son tuz yüzdesi kaçtır?

- Dökülen 100 g da %20'liktir; kalan 400 g karışım **hâlâ %20**'liktir. İçindeki tuz $400 \cdot 0{,}2 = 80$ g.
- 100 g su eklenince: $\frac{80}{500} \cdot 100 = 16$, **%16**.

Kütle yine 500 g oldu ama tuz 100'den 80'e düştü; yüzde bu yüzden değişti.

**Kural.** Karışımın bir kısmını dökmek ya da başka kaba aktarmak **yüzdeyi değiştirmez**; yalnızca kalan saf madde miktarını azaltır. Önce kalan saf maddeyi hesapla, sonra eklenenleri işle.

## ÖSYM tuzakları

> **Yüzdelerin ortalamasını almak:** %10'luk 200 g ile %25'lik 100 g karışımı $17{,}5$ değil **%15**'tir. Miktarlar eşit değilse ortalama yanlıştır; gramları topla.

> **Tuzu suya bölmek:** Payda karışımın tamamıdır. "Tuzun suya oranı $\frac{1}{4}$" diyorsa tuz yüzdesi %25 değil, $\frac{1}{1 + 4}$ ile **%20**'dir.

> **Sorulanı karıştırmak:** "Kaç gram su buharlaştırılmalı?" sorusunda son karışımın kütlesini (örneğin 240 g) cevap sanmak. Buharlaşan $300 - 240 = 60$ g'dır.

> **Döküp yerine su koyunca yüzdenin aynı kaldığını sanmak:** Kütle aynı kalır ama tuz azalır. %20'lik 500 g'ın 100 g'ı dökülüp 100 g su eklenince yüzde **16** olur.

> **Su eklemede suyu %100 tuzlu almak:** Tuz yüzdesi soruluyorsa su %0, saf tuz %100'dür. Soru suyun yüzdesini soruyorsa tersi.

## Kendini dene

### Soru 1
250 g tuzlu suyun 50 g'ı tuzdur.

Bu karışımın tuz yüzdesi kaçtır?

A) 15
B) 20
C) 25
D) 40
E) 50

**Cevap:** B
**Çözüm:** $\frac{50}{250} \cdot 100 = 20$. Tuzu suya ($200$ g) bölen $\frac{50}{200}$ ile 25 bulur; 50 ise yüzde değil, tuzun gram cinsinden miktarıdır.

### Soru 2
%30'luk 400 g şekerli sudan bir miktar su buharlaştırılarak karışım %40'lık yapılıyor.

Kaç gram su buharlaştırılmıştır?

A) 50
B) 80
C) 100
D) 120
E) 300

**Cevap:** C
**Çözüm:** Şeker $400 \cdot 0{,}3 = 120$ g ve değişmez. Yeni karışım $M$ ise $\frac{120}{M} = 0{,}4$, $M = 300$ g. Buharlaşan su $400 - 300 = 100$ g. 300 yeni karışımın kütlesidir, buharlaşan su değil; 120 ise şeker miktarıdır.

### Soru 3
%15'lik 300 g tuzlu suya %35'lik tuzlu sudan bir miktar eklenerek %20'lik karışım elde ediliyor.

Kaç gram %35'lik tuzlu su eklenmiştir?

A) 25
B) 50
C) 75
D) 100
E) 150

**Cevap:** D
**Çözüm:** $300 \cdot 15 + m \cdot 35 = (300 + m) \cdot 20$; $4500 + 35m = 6000 + 20m$, $15m = 1500$, $m = 100$ g. Kısa yol: 20, 15'e $5$, 35'e $15$ uzakta; uzaklıklar $1 : 3$ ise miktarlar $3 : 1$, yani $300 : 100$. Kontrol: tuz $45 + 35 = 80$ g, karışım $400$ g, $\frac{80}{400} = 0{,}2$.

## Özet kartı

- Saf madde yüzdesi $= \frac{\text{saf madde}}{\text{karışımın tamamı}} \cdot 100$; payda tuz + su.
- İlk iş: her karışımdaki saf madde miktarını gram olarak yaz.
- Su ekleme ve buharlaştırmada tuz sabit, yalnızca karışım değişir. Su %0, saf tuz %100 tuzludur.
- İki karışım: $A \cdot x + B \cdot y = (A + B) \cdot z$. Yüzdeler değil, gramlar toplanır.
- Yeni yüzde iki yüzdenin arasında ve miktarı çok olana yakındır; uzaklıklar miktarlarla ters orantılı.
- Dökmek yüzdeyi değiştirmez, kalan saf maddeyi azaltır.

## Sonraki adım

Alıştırmaya geç (aşağıdaki düğme). Sonraki derste **hareket problemlerine** geçeceksin; orada da aynı alışkanlık işine yarayacak: sabit kalan büyüklüğü bulup denklemi onun üzerine kurmak.
