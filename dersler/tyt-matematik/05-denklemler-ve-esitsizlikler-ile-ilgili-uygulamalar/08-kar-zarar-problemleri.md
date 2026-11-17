---
baslik: Kâr-Zarar Problemleri
ders: tyt-matematik
sure: 20 dk
kaynak: MEBİ Konu Özeti a5221a5e18
guncelleme: 2026-11-17
---
# Kâr-Zarar Problemleri

**Bu dersin sonunda:** kâr ve zarar yüzdesini maliyet üzerinden, zam ve indirimi etiket fiyatı üzerinden hesaplayıp maliyete $100x$ diyerek "zam, indirim, kâr" zincirlerini tek denklemle çözebileceksin.

> **TYT'de yeri:** Her yıl en az bir soru gelir. Kalıplar: "yüzde kaç kârla satılmıştır?", "maliyeti kaç TL'dir?", "etiket fiyatına %… indirim yapılınca yine de %… kâr ediliyor", "önce zam sonra indirim" ve tanesi ya da kilosu üzerinden toplu alım satım. Asıl sınanan şey: **yüzdenin neyin üzerinden alındığı.**

## Önce hatırla

<details><summary>Yüzde problemlerinden: Bir sayının %30'u 36 ise aynı sayının %45'i kaçtır?</summary>
Sayıya $100x$ de: $30x = 36$, $x = 1{,}2$. Sayının %45'i $45x = 45 \cdot 1{,}2 = 54$. Sayının kendisini ($120$) bulmana bile gerek yoktu. Bu derste maliyete hep $100x$ diyeceksin.
</details>

<details><summary>Yüzde problemlerinden: A sayısı B sayısının %125'i ise B sayısı A sayısının yüzde kaçıdır?</summary>
$B = 100$ dersen $A = 125$. $B$, $A$'nın $\frac{100}{125} \cdot 100 = 80$, yani **%80**'idir; %75 değil. Yüzde, hangi sayının üzerinden alındığına göre değişir. Bu derste de tuzak bu: kâr maliyet üzerinden, indirim etiket üzerinden alınır.
</details>

## Kâr, zarar ve kâr yüzdesi

**Örnek.** Bir kırtasiyeci tanesini 80 TL'ye aldığı bir çantayı 100 TL'ye satıyor. Başka bir çantayı ise 80 TL'ye alıp 60 TL'ye satıyor.

- Birinci çanta: kâr $= 100 - 80 = 20$ TL. Kâr yüzdesi $= \frac{20}{80} \cdot 100 = 25$, yani **%25 kâr**.
- İkinci çanta: zarar $= 80 - 60 = 20$ TL. Zarar yüzdesi $= \frac{20}{80} \cdot 100 = 25$, yani **%25 zarar**.

Kâr da zarar da 20 TL; ikisinde de 20, satış fiyatına değil **80'e (maliyete)** bölündü.

![Üç çift sütun. Her çiftte solda 80 yazan mavi maliyet sütunu, sağda sarı satış sütunu. Birincide satış 100, üstte taralı yeşil 20'lik kâr parçası. İkincide satış 60, üstte kırmızı kesikli 20'lik eksik parça. Üçüncüde satış 80, iki sütun eşit.](gorsel/tyt-matematik/05-08-kar-zarar.svg "Kesikli çizgi maliyet düzeyi. Satış bu çizginin üstündeyse kâr, altındaysa zarar, tam üzerindeyse ne kâr ne zarar.")

**Kural.**

| | Tanım | Yüzdesi |
|---|---|---|
| Kâr | Satış fiyatı $-$ Maliyet | $\frac{\text{Kâr}}{\text{Maliyet}} \cdot 100$ |
| Zarar | Maliyet $-$ Satış fiyatı | $\frac{\text{Zarar}}{\text{Maliyet}} \cdot 100$ |

Kâr ve zarar yüzdesi **her zaman maliyet üzerinden** hesaplanır. Satış fiyatı maliyete eşitse ne kâr ne zarar vardır.

## Maliyete 100x demek

**Örnek.** Bir ürün %25 kârla 150 TL'ye satılıyor. Maliyeti kaç TL'dir?

Maliyet $100x$ olsun. %25 kâr, maliyetin %25'i kadar fazla demektir: satış $= 100x + 25x = 125x$.

$$125x = 150 \quad\Rightarrow\quad x = 1{,}2 \quad\Rightarrow\quad \text{maliyet} = 100x = 120 \text{ TL}$$

Kontrol: $150 - 120 = 30$ TL kâr; $\frac{30}{120} = 0{,}25$. Doğru.

**Örnek.** Bir ürün %10 zararla 270 TL'ye satılıyor. Maliyeti kaç TL'dir?

Maliyet $100x$; %10 zarar: satış $= 100x - 10x = 90x = 270$, $x = 3$, maliyet $= 300$ TL.

**Kural.** Maliyet $100x$ ise

$$\%a \text{ kârla satış} = (100 + a)x \qquad \%a \text{ zararla satış} = (100 - a)x$$

Satış fiyatı verilmişse bu ifadeyi ona eşitle. Kısa yol: maliyet $= \text{satış} \cdot \frac{100}{100 + a}$.

## Zam ve indirim: etiket fiyatı üzerinden

**Örnek.** Etiket fiyatı 400 TL olan bir ayakkabıya %15 indirim yapılıyor; aynı mağazada etiket fiyatı 400 TL olan bir bota %10 zam geliyor.

- Ayakkabı: $400 - 400 \cdot \frac{15}{100} = 400 \cdot \frac{85}{100} = 340$ TL.
- Bot: $400 + 400 \cdot \frac{10}{100} = 400 \cdot \frac{110}{100} = 440$ TL.

**Kural.** Fiyatı $A$ olan ürüne

$$\%x \text{ indirim: } A \cdot \frac{100 - x}{100} \qquad \%x \text{ zam: } A \cdot \frac{100 + x}{100}$$

Zam ve indirim **satış (etiket) fiyatı** üzerinden yapılır; maliyetle ilgisi yoktur. İşlem kolaylığı için etiket fiyatına $100x$ denebilir.

## Art arda zam ve indirim

**Örnek.** 100 TL'lik bir ürüne önce %20 zam, sonra yeni fiyata %20 indirim yapılıyor. Son fiyat kaç TL'dir?

Zam: $100 \cdot 1{,}2 = 120$. İndirim **120'nin** %20'si, yani 24 TL: $120 - 24 = 96$ TL. Fiyat başa dönmedi; **%4 düştü.**

![Üç sütun: 100 TL ilk fiyat, 120 TL zamlı fiyat, 96 TL indirimli fiyat. 100'de kesikli çizgi. Okların üstünde artı 20 ve eksi 24 yazıyor; son sütunun üstünde 4 TL eksik.](gorsel/tyt-matematik/05-08-zam-indirim.svg "Zam 100'ün yüzde 20'si, indirim 120'nin yüzde 20'si. Tabanlar farklı olduğu için +20 ile −24 birbirini götürmez.")

**Kural.** Art arda yüzde değişimler **toplanmaz, çarpanlar çarpılır**:

$$A \cdot \frac{100 + a}{100} \cdot \frac{100 - b}{100}$$

Aynı oranda zam ve indirim (sırası ne olursa olsun) fiyatı hep düşürür.

## Maliyet, etiket, satış zinciri

**Örnek.** Bir satıcı ürünlerin etiket fiyatını maliyetin %40 fazlası olarak belirliyor. Kampanyada etiket fiyatı üzerinden %25 indirim yapıyor. Satıcı bu satışta yüzde kaç kâr eder?

Maliyete $100x$ de; her adımda yüzdenin **tabanını** yaz.

- Etiket: maliyetin %40 fazlası $\Rightarrow 140x$.
- Satış: etiketin %25 eksiği $\Rightarrow 140x \cdot \frac{75}{100} = 105x$.
- Kâr: $105x - 100x = 5x$; maliyet $100x$ olduğu için **%5 kâr**.

![Soldan sağa üç kutu: Maliyet 100x, Etiket 140x, Satış 105x. Birinci okun üstünde artı yüzde 40, altında maliyetin; ikinci okun üstünde eksi yüzde 25, altında etiketin. Altta: 140x çarpı 0,75 eşittir 105x, kâr 5x, yani yüzde 5 kâr.](gorsel/tyt-matematik/05-08-zincir.svg "Her okun altındaki kelimeye bak: zam maliyete, indirim etikete uygulanır. 40 − 25 = 15 hesabı yanlıştır.")

**Kural.** Maliyet $100x$ ile başla, her adımı bir öncekinin üzerine çarpan olarak uygula, sonda satışı $100x$ ile karşılaştır. Satış $(100 + k)x$ çıktıysa %$k$ kâr, $(100 - k)x$ çıktıysa %$k$ zarar vardır.

## Tanesi ya da kilosu üzerinden alım satım

**Örnek.** Bir manav limonların 3 tanesini 10 TL'ye alıp 4 tanesini 15 TL'ye satıyor. Yüzde kaç kâr eder?

3 ile 4'ün EKOK'u 12. 12 limon alırken $4 \cdot 10 = 40$ TL öder, satarken $3 \cdot 15 = 45$ TL alır. Kâr $5$ TL:

$$\frac{5}{40} \cdot 100 = 12{,}5 \quad\Rightarrow\quad \%12{,}5 \text{ kâr}$$

**Kural.** Alış ve satış farklı sayıda tane için verilmişse **aynı sayıda ürün** al: tane sayılarının EKOK'u kadar ürünün toplam maliyetini ve toplam satışını karşılaştır. Bozulan, çürüyen ürün varsa maliyet **hepsi** için, satış yalnızca **kalanlar** için yazılır.

## ÖSYM tuzakları

> **Kârı satışa bölmek:** 80 TL'ye alınıp 100 TL'ye satılan üründe kâr yüzdesi $\frac{20}{100}$ ile %20 değil, $\frac{20}{80}$ ile **%25**'tir. Seçeneklerde ikisi de olur.

> **Yüzdeleri toplayıp çıkarmak:** "Maliyetin %40 fazlasına etiket, etikette %25 indirim" için $40 - 25 = 15$ demek. İndirimin tabanı etiket ($140x$) olduğu için cevap **%5** kârdır.

> **Aynı oranda zam ve indirim fiyatı başa döndürür sanmak:** %20 zam ve ardından %20 indirim fiyatı **%4 düşürür**. "Değişmez" seçeneği çeldiricidir.

> **Satış fiyatından geriye yüzde düşmek:** %25 kârla 150 TL'ye satılan ürünün maliyeti $150 \cdot 0{,}75 = 112{,}5$ değil, $\frac{150}{1{,}25} = 120$ TL'dir. %25, 150'nin değil maliyetin yüzdesidir.

> **Aynı fiyata satılan iki üründe kâr ve zararın birbirini götüreceğini sanmak:** Biri %20 kârla, öbürü %20 zararla aynı fiyata satılırsa maliyetler farklıdır (zararlı olanın maliyeti büyüktür); toplamda zarar edilir.

## Kendini dene

### Soru 1
Bir mağaza 160 TL'ye aldığı bir gömleği 200 TL'ye satıyor.

Bu satıştaki kâr yüzdesi kaçtır?

A) 20
B) 25
C) 30
D) 40
E) 60

**Cevap:** B
**Çözüm:** Kâr $200 - 160 = 40$ TL. Kâr yüzdesi maliyet üzerinden: $\frac{40}{160} \cdot 100 = 25$. Kârı satış fiyatına bölen $\frac{40}{200}$ ile 20 bulur.

### Soru 2
Fiyatı 250 TL olan bir ürüne önce %20 zam yapılıyor, ardından yeni fiyat üzerinden %20 indirim yapılıyor.

Ürünün son fiyatı kaç TL'dir?

A) 200
B) 225
C) 230
D) 240
E) 250

**Cevap:** D
**Çözüm:** Zamlı fiyat $250 \cdot 1{,}2 = 300$ TL. İndirim 300'ün %20'si, 60 TL: $300 - 60 = 240$ TL. Kısaca $250 \cdot 1{,}2 \cdot 0{,}8 = 250 \cdot 0{,}96 = 240$. Zam ile indirimin birbirini götürdüğünü sanan 250 der.

### Soru 3
Bir satıcı bir ürünün etiket fiyatını maliyetin %50 fazlası olarak belirliyor. Ürünü etiket fiyatı üzerinden %20 indirimle sattığında 36 TL kâr ediyor.

Bu ürünün maliyeti kaç TL'dir?

A) 120
B) 144
C) 180
D) 216
E) 240

**Cevap:** C
**Çözüm:** Maliyet $100x$, etiket $150x$, satış $150x \cdot 0{,}8 = 120x$. Kâr $120x - 100x = 20x = 36$, $x = 1{,}8$; maliyet $100x = 180$ TL. Kontrol: satış $216$ TL, $216 - 180 = 36$. Kârı $50 - 20 = 30$ yüzde sanan $36 \div 0{,}3 = 120$ bulur; 216 ise satış fiyatıdır.

## Özet kartı

- Kâr = satış $-$ maliyet; zarar = maliyet $-$ satış. Yüzdeleri **maliyet** üzerinden hesaplanır.
- Maliyete $100x$ de: %$a$ kârla satış $(100 + a)x$, %$a$ zararla satış $(100 - a)x$.
- Zam ve indirim **etiket (satış) fiyatı** üzerinden: %$x$ indirimde $A \cdot \frac{100 - x}{100}$, %$x$ zamda $A \cdot \frac{100 + x}{100}$.
- Art arda değişimlerde yüzdeler toplanmaz, çarpanlar çarpılır. Aynı oranda zam ve indirim fiyatı düşürür.
- Zincirde her adımın tabanını yaz: maliyet → etiket → satış.
- Tane hesabında EKOK kadar ürün al; çürüyen varsa maliyet hepsine, satış kalana.

## Sonraki adım

Alıştırmaya geç (aşağıdaki düğme). Sonraki derste **karışım problemlerinde** de aynı fikir sürecek: bir yüzdenin hangi bütünün üzerinden alındığını bulmak.
