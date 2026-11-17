---
baslik: Kesir Problemleri
ders: tyt-matematik
sure: 20 dk
kaynak: MEBİ Konu Özeti d33a576a81
guncelleme: 2026-11-17
---
# Kesir Problemleri

**Bu dersin sonunda:** "bir sayının $\frac{a}{b}$'si" ve "kalanın $\frac{c}{d}$'si" gibi ifadeleri denkleme çevirebilecek, bilinmeyeni paydaların EKOK'u ile seçerek kesirsiz işlem yapabilecek; kap, tel ve iş bölüşme problemlerini çözebileceksin.

> **TYT'de yeri:** Hemen her sınavda en az bir soru kesirle kurulur: "parasının $\frac{1}{3}$'ünü harcadı, kalanın $\frac{1}{4}$'ünü…", "kabın $\frac{2}{5}$'i doluyken…", "telin bir ucundan kesilince orta noktası…". İşlem kısadır; puan, kesrin **neyin** kesri olduğunu doğru okuyandadır.

## Önce hatırla

<details><summary>Sayı problemlerinden: Bir sayının 3 katının 7 eksiği, aynı sayının 5 fazlasına eşittir. Bu sayı kaçtır?</summary>
Sayı $x$ olsun: $3x - 7 = x + 5$. Buradan $2x = 12$, $x = 6$. Kontrol: $3 \cdot 6 - 7 = 11$ ve $6 + 5 = 11$.
</details>

<details><summary>Sayı problemlerinden: Bir otoparkta otomobil ve motosikletlerden oluşan 25 araç var. Toplam tekerlek sayısı 80 ise kaç motosiklet vardır?</summary>
Motosiklet sayısı $m$ ise otomobil $25 - m$ olur. $4(25 - m) + 2m = 80$, $100 - 2m = 80$, $m = 10$. Bir çokluğu $x$, ötekini "toplam eksi $x$" diye yazmak bu derste de işine yarayacak.
</details>

## "'sı", "'ünün 'si": kesri çarpmaya çevir

**Örnek.** $180$'in $\frac{2}{9}$'u kaçtır?

"'sı" kelimesi **çarpma** demektir: $180 \cdot \frac{2}{9} = 40$.

**Örnek.** Bir sayının $\frac{2}{3}$'ünün $\frac{3}{4}$'ü $18$ ise sayı kaçtır?

Sayı $x$ olsun. Kesirler art arda çarpılır:

$$x \cdot \frac{2}{3} \cdot \frac{3}{4} = 18 \quad\Rightarrow\quad \frac{x}{2} = 18 \quad\Rightarrow\quad x = 36$$

**Örnek.** Bir sayının $\frac{3}{5}$'i, $\frac{2}{5}$'inden $12$ fazladır. Sayı kaçtır?

İki kesrin farkı sayının $\frac{1}{5}$'idir ve bu fark $12$'ye karşılık gelir: $\frac{x}{5} = 12$, $x = 60$.

**Kural.** "$x$ sayısının $\frac{a}{b}$'si" $= x \cdot \frac{a}{b}$. "'ünün 'si" zincirinde bütün kesirler çarpılır. Bir kesir bir miktara karşılık geliyorsa ($\frac{a}{b}x = m$) bütün, $x = m \cdot \frac{b}{a}$ olur.

## Bilinmeyeni EKOK ile seç

**Örnek.** Bir sayının $\frac{1}{4}$'ü ile $\frac{1}{6}$'sının toplamı $30$'dur. Sayı kaçtır?

Paydalar 4 ve 6, $\text{EKOK}(4, 6) = 12$. Sayıya $x$ yerine $12x$ de; kesirler kaybolur:

$$\frac{12x}{4} + \frac{12x}{6} = 3x + 2x = 5x = 30 \quad\Rightarrow\quad x = 6$$

Sayı $12x = 72$. Kontrol: $72$'nin $\frac{1}{4}$'ü $18$, $\frac{1}{6}$'sı $12$; toplam $30$.

**Kural.** Soruda birden çok payda varsa bütüne **paydaların EKOK'u kadar $x$** de ($k$ = EKOK ise bütün $kx$). Her parça tam katsayılı çıkar, hesap hızlanır. Sonunda bulduğun $x$'i değil, istenen çokluğu ($kx$ gibi) yazmayı unutma.

## "Kalanın" kesri

TYT'de en çok buradan puan kaybedilir: ikinci kesir bütünün değil, **o anda kalan** miktarın kesridir.

**Örnek.** Bir öğrenci harçlığının $\frac{1}{3}$'ünü kitaba, kalanın $\frac{1}{4}$'ünü sinemaya harcıyor ve geriye $150$ TL kalıyor. Harçlık kaç TL'dir?

Paydalar 3 ve 4; harçlığa $12x$ de.

- Kitap: $12x \cdot \frac{1}{3} = 4x$. Kalan $8x$.
- Sinema: kalanın $\frac{1}{4}$'ü, $8x \cdot \frac{1}{4} = 2x$. Kalan $6x$.
- $6x = 150 \Rightarrow x = 25$. Harçlık $12x = 300$ TL.

![On iki eşit kutudan oluşan şerit: ilk dört kutu mavi, kitap, tümün üçte biri; sonraki iki kutu sarı, sinema, kalanın dörtte biri; son altı kutu yeşil, kalan 150 TL. Üstte kitaptan sonra kalan sekiz parça okla gösterilmiş.](gorsel/tyt-matematik/05-04-kalanin.svg "Sinema payı 12 parçanın değil, kitaptan sonra kalan 8 parçanın dörtte biridir: 2 parça.")

Kısa yol: her adımda kalan oranı çarp. $1 - \frac{1}{3} = \frac{2}{3}$, sonra $1 - \frac{1}{4} = \frac{3}{4}$; kalan $\frac{2}{3} \cdot \frac{3}{4} = \frac{1}{2}$. Harçlığın yarısı $150$ ise harçlık $300$.

**Kural.** "Kalanın $\frac{c}{d}$'si harcandı" ise kalan $\left(1 - \frac{c}{d}\right)$ ile çarpılır. Art arda harcamalarda kalan, kalan oranlarının **çarpımıdır**; kesirler bütünden çıkarılmaz.

## Farklı hızlarla biten iş

**Örnek.** Bir öğrenci bir kitabın $\frac{2}{5}$'ini günde 30 sayfa, kalanını günde 45 sayfa okuyarak 16 günde bitiriyor. Kitap kaç sayfadır?

Kitaba $5x$ sayfa de. İlk kısım $2x$ sayfa, ikinci kısım $3x$ sayfa. Gün = sayfa ÷ günlük hız:

$$\frac{2x}{30} + \frac{3x}{45} = 16 \quad\Rightarrow\quad \frac{x}{15} + \frac{x}{15} = 16 \quad\Rightarrow\quad x = 120$$

Kitap $5x = 600$ sayfa. Kontrol: $240 \div 30 = 8$ gün, $360 \div 45 = 8$ gün; toplam 16 gün.

**Kural.** İş farklı hızlarla bölümlere ayrılıyorsa her bölüm için **süre = miktar ÷ hız** yaz ve süreleri topla. Hızların ortalamasını almak yanlıştır.

## Dolu-boş kap

**Örnek.** Bir sürahi $\frac{1}{3}$'ü suyla doluyken $900$ g, $\frac{3}{4}$'ü doluyken $1400$ g geliyor. Boş sürahi kaç gramdır?

Sürahinin kendi kütlesi iki durumda da aynıdır; değişen yalnızca sudur. Ağırlık farkı, su farkıdır:

$$\frac{3}{4} - \frac{1}{3} = \frac{5}{12} \text{ su} \;=\; 1400 - 900 = 500 \text{ g}$$

$\frac{1}{12}$'si $100$ g ise sürahiyi dolduran su $1200$ g. $\frac{1}{3}$'ü dolu iken su $400$ g, sürahi $900 - 400 = 500$ g.

![Yan yana iki dikey kap, her biri on iki eşit parçaya bölünmüş. Soldaki dört parça dolu, altında 900 g. Sağdaki dokuz parça dolu, altında 1400 g; fazla olan beş parça yeşil ve yanında 5 parça eşittir 500 g yazıyor.](gorsel/tyt-matematik/05-04-surahi.svg "İki tartım arasındaki fark yalnızca yeşil 5 parçalık sudan gelir. Kabın kendi kütlesi farkta yok olur.")

**Kural.** İki durum verilen kap sorularında **farkı al**: kesirlerin farkı, ağırlıkların farkına karşılık gelir. Önce tam dolu sıvıyı bul, sonra boş kabı.

## Telin orta noktası

**Örnek.** Bir telin bir ucundan $\frac{1}{5}$'i kesilince telin orta noktası $12$ cm yer değiştiriyor. Telin ilk boyu kaç cm'dir?

Tel $x$ cm olsun. Bir uçtan kesilen parça $\frac{x}{5}$. Orta nokta, kesilen uzunluğun **yarısı** kadar öbür uca doğru kayar:

$$\frac{x}{5} \cdot \frac{1}{2} = 12 \quad\Rightarrow\quad \frac{x}{10} = 12 \quad\Rightarrow\quad x = 120 \text{ cm}$$

![İki yatay tel. Üstteki 120 cm, orta noktası işaretli. Alttakinin sol ucundan 24 cm kesilmiş; yeni orta nokta sağa kaymış, iki orta arası 12 cm kayma olarak gösterilmiş.](gorsel/tyt-matematik/05-04-tel.svg "24 cm kesildi, orta nokta yalnızca 12 cm kaydı: kayma, kesilen parçanın yarısıdır.")

**Kural.** Bir uçtan $k$ cm kesilirse orta nokta $\frac{k}{2}$ kayar. İki uçtan kesilirse kaymalar ters yönlüdür: net kayma $\frac{|k_1 - k_2|}{2}$.

## ÖSYM tuzakları

> **"Kalanın" kesrini bütünden almak:** Harçlık örneğinde $1 - \frac{1}{3} - \frac{1}{4} = \frac{5}{12}$ yazan, $150$'yi $\frac{5}{12}$'ye eşitleyip $360$ TL bulur. Doğrusu $\frac{2}{3} \cdot \frac{3}{4} = \frac{1}{2}$, cevap $300$ TL.

> **$x$'i cevap sanmak:** Bütüne $12x$ dedikten sonra $x = 25$ bulup "25" işaretlemek. Seçeneklerde $x$'in değeri hep bulunur; istenen çokluğu yeniden oku.

> **Orta noktanın kesilen kadar kaydığını sanmak:** Bir uçtan $24$ cm kesilen telin orta noktası $24$ değil $12$ cm kayar. Yarıyı unutan, telin boyunu gerçek boyun yarısı bulur ($120$ yerine $60$).

> **Kabın kütlesini unutmak:** "$\frac{1}{3}$'ü dolu iken 900 g" demek suyun 900 g olduğu anlamına gelmez; bu, kap ile suyun toplamıdır. Önce iki durumun farkını al.

## Kendini dene

### Soru 1
$240$ sayısının $\frac{3}{8}$'inin $\frac{2}{3}$'ü kaçtır?

A) 45
B) 60
C) 80
D) 90
E) 120

**Cevap:** B
**Çözüm:** Kesirler art arda çarpılır: $240 \cdot \frac{3}{8} = 90$, $90 \cdot \frac{2}{3} = 60$. 90 yalnızca ilk adımın sonucudur; 80 ise $240 \cdot \frac{1}{3}$ gibi yanlış bir kesirle bulunur.

### Soru 2
Bir öğrenci parasının $\frac{2}{5}$'iyle ayakkabı, kalan paranın $\frac{1}{3}$'üyle tişört alıyor ve geriye $240$ TL kalıyor.

Buna göre öğrencinin başlangıçtaki parası kaç TL'dir?

A) 360
B) 480
C) 540
D) 600
E) 900

**Cevap:** D
**Çözüm:** Paraya $15x$ de. Ayakkabı $6x$, kalan $9x$. Tişört kalanın $\frac{1}{3}$'ü: $3x$; kalan $6x = 240$, $x = 40$. Para $15x = 600$ TL. Kısa yol: kalan oran $\frac{3}{5} \cdot \frac{2}{3} = \frac{2}{5}$, $\frac{2}{5}$'i $240$ ise tamamı $600$. 900, iki kesri de bütünden çıkarıp $1 - \frac{2}{5} - \frac{1}{3} = \frac{4}{15}$ yazmaktan gelir.

### Soru 3
Bir telin bir ucundan $\frac{1}{4}$'ü kesildiğinde telin orta noktası $9$ cm yer değiştiriyor.

Buna göre telin ilk boyu kaç cm'dir?

A) 36
B) 54
C) 72
D) 96
E) 144

**Cevap:** C
**Çözüm:** Tel $x$ cm ise kesilen $\frac{x}{4}$; orta nokta bunun yarısı kadar kayar: $\frac{x}{8} = 9$, $x = 72$ cm. Kaymayı kesilen parçaya eşit sanan $\frac{x}{4} = 9$ ile 36 bulur.

## Özet kartı

- "'sı" çarpmadır; "'ünün 'si" zincirinde bütün kesirler çarpılır.
- Birden çok payda varsa bütüne paydaların EKOK'u kadar $x$ de; sonunda istenen çokluğu yaz.
- "Kalanın" kesri: kalan oranlar çarpılır, kesirler bütünden çıkarılmaz.
- Farklı hızlarla biten işte her bölümün süresini (miktar ÷ hız) ayrı yazıp topla.
- Dolu-boş kapta iki durumun farkını al: kesir farkı = ağırlık farkı.
- Bir uçtan $k$ kesilen telin orta noktası $\frac{k}{2}$ kayar.

## Sonraki adım

Alıştırmaya geç (aşağıdaki düğme). Sonraki ders **Yaş Problemleri**; orada da bilinmeyeni akıllıca seçmek ve "şimdi–sonra" durumlarını ayrı yazmak işini kolaylaştıracak.
