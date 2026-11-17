---
baslik: Üçgenlerin Benzerliği İle İlgili Uygulamalar
ders: tyt-matematik
sure: 20 dk
kaynak: MEBİ Konu Özeti 21788ad791
guncelleme: 2026-11-17
---
# Üçgenlerin Benzerliği İle İlgili Uygulamalar

**Bu dersin sonunda:** sokak lambası–gölge, tahterevalli, kutulara yaslanan rampa ve çapraz gerilen ip durumlarında iç içe geçmiş benzer üçgenleri görüp tek bir orantıyla bilinmeyen uzunluğu bulabileceksin.

> **TYT'de yeri:** Geometri bölümünde benzerlik çoğu zaman günlük hayat kılığında gelir: bir lambanın oluşturduğu gölge, yaslanmış bir merdiven ya da rampa, bir tahterevalli, iki direk arasına gerilmiş ipler. Şekil karmaşık görünür; ama içinde hemen her zaman bir köşeyi paylaşan, birbirine paralel kenarlı iki üçgen vardır. İş, o iki üçgeni bulup doğru kenarları oranlamaktır.

## Önce hatırla

<details><summary>Geçen dersten: ABC üçgeninde D, [AB] üzerinde; E, [AC] üzerinde ve [DE] ∥ [BC]. |AD| = 2, |DB| = 3, |AE| = 4 ise |EC| kaçtır?</summary>
Temel orantı teoremi: |AD| / |DB| = |AE| / |EC|, yani 2/3 = 4/|EC| ve <b>|EC| = 6</b>. Bugünkü bütün uygulamalar bu teoremin günlük hayattaki karşılığıdır: dik duran bir kişi, bir direk ya da bir destek, büyük üçgenin bir kenarına paralel çizilmiş [DE] gibidir.
</details>

<details><summary>Geçen dersten: ABC üçgeninde D ve E, [AB] ve [AC] kenarlarının orta noktalarıdır. |BC| = 10 ise |DE| kaçtır?</summary>
[DE] orta tabandır, [BC]'ye paraleldir ve uzunluğu onun yarısıdır: <b>|DE| = 5</b>. Bugün desteği tam ortada olan bir tahterevallide aynı bilgiyi kullanacaksın.
</details>

## Hepsinde aynı iskelet

Bu dersteki dört durumun hepsinde şunu ara: **bir köşeyi paylaşan iki dik üçgen** ve bu üçgenlerde **birbirine paralel iki dik kenar** (dik duran kişi ile direk, destek ile yükseklik). Paylaşılan köşedeki açı ortak, dik açılar eşit: A.A. ile benzerler. Sonra her zaman şunu yaz:

$$\frac{\text{küçük üçgende bir kenar}}{\text{büyük üçgende karşılığı}} = \frac{\text{küçük üçgende öbür kenar}}{\text{büyük üçgende karşılığı}}$$

Kenarları **ortak köşeden** ölçmeyi unutma; hataların çoğu buradan çıkar.

## 1. Sokak lambası ve gölge

**Örnek.** $6$ m yüksekliğindeki bir sokak lambasının dibinden $6$ m uzakta, $1{,}5$ m boyunda bir kişi duruyor. Kişinin gölgesi kaç metredir?

![Solda 6 metrelik lamba direği AL, sağında 6 metre uzakta 1,5 metrelik kişi BK. Lambanın tepesi L'den kişinin başı K'ye giden kesikli ışın, yerde C noktasına iniyor. Gölge BC, uzunluğu x.](gorsel/tyt-matematik/19-04-lamba.svg "Işın L'den çıkar, K'nin üstünden geçip yere C'de değer. Küçük CBK üçgeni ile büyük CAL üçgeni C köşesini paylaşır; ikisinin de tabanı C'den ölçülür.")

**Çözüm.**

1. Gölgenin ucu $C$, kişinin ayağı $B$, başı $K$; direğin dibi $A$, lamba $L$. $CBK$ ve $CAL$ üçgenlerinde $\widehat{C}$ ortak, $B$ ve $A$'daki açılar dik: A.A. ile $\triangle CBK \sim \triangle CAL$.
2. Ortak köşe $C$'den ölç: küçük üçgenin tabanı $|CB| = x$, büyük üçgenin tabanı $|CA| = x + 6$.
3. Orantı: $\dfrac{|BK|}{|AL|} = \dfrac{|CB|}{|CA|} \Rightarrow \dfrac{1{,}5}{6} = \dfrac{x}{x + 6}$.
4. İçler dışlar: $6x = 1{,}5x + 9 \Rightarrow 4{,}5x = 9 \Rightarrow x = 2$. Gölge $2$ m.

**Kural:** Lamba yüksekliği $H$, kişinin boyu $h$, kişinin direğe uzaklığı $d$, gölge $s$ ise

$$\frac{h}{H} = \frac{s}{s + d}$$

Kişi lambadan uzaklaştıkça gölgesi uzar. Bu örnekte gölge her zaman uzaklığın üçte biridir: $s = \dfrac{h \cdot d}{H - h} = \dfrac{1{,}5 \cdot 6}{4{,}5} = 2$.

> **Tuzak:** Paydaya $s$ değil $d$ yazmak: $\dfrac{1{,}5}{6} = \dfrac{x}{6}$ ile $x = 1{,}5$ bulunur, yanlıştır. Büyük üçgenin tabanı, direğin dibinden **gölgenin ucuna** kadardır: $s + d$. Güneşte ışınlar paraleldir ve gölge/boy oranı herkes için aynıdır; lambada ışınlar bir noktadan yayılır, bu oran kişinin yerine göre değişir.

## 2. Tahterevalli

**Örnek.** $3{,}6$ m uzunluğundaki bir tahtanın $A$ ucu yerde duruyor. Tahta, $0{,}5$ m yüksekliğindeki dik bir desteğe, $A$ ucundan tahta boyunca $1{,}5$ m uzaktaki $S$ noktasında dayanıyor. Tahtanın havadaki $B$ ucu yerden kaç metre yüksektedir?

![A ucu yerde olan eğik AB tahtası. Tahta, D noktasında yere dik duran 0,5 metrelik DS desteğine S noktasında dayanıyor. AS 1,5 metre, SB 2,1 metre. B'den yere inen kesikli dikme BH, uzunluğu soru işareti.](gorsel/tyt-matematik/19-04-tahterevalli.svg "Destek DS ile B'den inen BH ikisi de yere diktir, yani birbirine paraleldir. ADS ve AHB üçgenleri A köşesini paylaşır.")

**Çözüm.**

1. $B$'den yere dik $[BH]$ çiz. $ADS$ ve $AHB$ üçgenlerinde $\widehat{A}$ ortak, $D$ ve $H$'deki açılar dik: $\triangle ADS \sim \triangle AHB$.
2. Ortak köşe $A$'dan ölç: $|AS| = 1{,}5$, $|AB| = 3{,}6$ (tamamı, $2{,}1$ değil).
3. Orantı: $\dfrac{|DS|}{|HB|} = \dfrac{|AS|}{|AB|} \Rightarrow \dfrac{0{,}5}{|HB|} = \dfrac{1{,}5}{3{,}6} \Rightarrow |HB| = \dfrac{0{,}5 \cdot 3{,}6}{1{,}5} = 1{,}2$ m.

**Kural:** Destek yüksekliği $h$, yerdeki uçtan desteğe tahta boyunca uzaklık $a$, tahtanın boyu $L$ ise havadaki ucun yüksekliği

$$\frac{h \cdot L}{a}$$

Destek **tam ortadaysa** $a = \dfrac{L}{2}$ ve yükseklik $2h$ olur. Bu, geçen dersteki orta tabandır: destek, büyük üçgenin orta tabanı gibi davranır. Tahtanın uzunluğu önemsizdir.

> **Tuzak:** Desteğin öbür yanındaki parçayı ($2{,}1$ m) büyük üçgenin kenarı sanmak. $\dfrac{0{,}5 \cdot 2{,}1}{1{,}5} = 0{,}7$ yanlıştır. Oran her zaman **yerdeki uçtan** ölçülen uzunluklarla kurulur.

## 3. Kutulara yaslanan rampa

**Örnek.** Özdeş kutulardan $2$, $4$ ve $7$ kutuluk üç yığın yapılmış. Düz bir rampa üç yığının da üst köşesine değiyor. $2$ ve $4$ kutuluk yığınların rampaya değdiği köşeler arasındaki yatay uzaklık $30$ cm'dir. $4$ ve $7$ kutuluk yığınlarınki ($a$) kaç cm'dir?

![Yerde P noktasından başlayan mavi rampa, 2, 4 ve 7 kutuluk üç yığının sol üst köşelerine değiyor. 2 ile 4 kutuluk yığınların köşeleri arası 30 cm, 4 ile 7 kutuluk yığınlarınki a.](gorsel/tyt-matematik/19-04-kutular.svg "Rampa düz olduğu için her köşede, yatayda gidilen yol ile yukarı çıkılan yol aynı oranda artar.")

**Çözüm.**

1. Bir kutunun yüksekliğine $k$ de. Başlangıç noktası olarak $2$ kutuluk yığının köşesini al. Oradan $4$ kutuluk yığının köşesine $30$ cm ilerlerken $2k$ yükselinir; $7$ kutuluk yığının köşesine $30 + a$ ilerlerken $5k$ yükselinir.
2. Bu iki dik üçgen ilk köşeyi paylaşır ve dik kenarları paraleldir: benzerdirler.
3. Orantı: $\dfrac{2k}{5k} = \dfrac{30}{30 + a} \Rightarrow 2(30 + a) = 150 \Rightarrow a = 45$ cm.

**Kısa yol:** Rampa düz olduğu için **her kutu boyu, aynı yatay yolla** çıkılır. $2$ kutu için $30$ cm gerekiyorsa $1$ kutu için $15$ cm; $4$'ten $7$'ye $3$ kutu çıkmak için $3 \cdot 15 = 45$ cm.

**Kural:** Düz bir doğru üzerinde

$$\frac{\text{yükseklik farkı}}{\text{yatay uzaklık}} = \text{sabit}$$

> **Tuzak:** Yerden ölçülen kutu sayılarıyla, yığınlar **arasındaki** uzaklıkları oranlamak. $\dfrac{30}{30 + a} = \dfrac{4}{7}$ ile $a = 22{,}5$ ya da $\dfrac{30}{a} = \dfrac{4}{7}$ ile $a = 52{,}5$ bulunur; ikisi de yanlıştır. Yükseklik yerden ölçülüyorsa uzaklık da rampanın **yere değdiği noktadan** ölçülmelidir; uzaklık yığından yığına ölçülüyorsa yükseklik de **farkla** alınmalıdır.

## 4. Çapraz gerilen ipler

**Örnek.** Aralarında $9$ m bulunan $6$ m ve $3$ m yüksekliğindeki iki dik direğin her birinin tepesinden öbürünün dibine birer ip geriliyor. İplerin kesiştiği $P$ noktası yerden kaç metre yüksektedir?

![Solda 6 metrelik AB direği, sağda 3 metrelik CD direği; dipleri arası 9 metre. A'dan D'ye mavi ip, C'den B'ye yeşil ip. İpler P noktasında kesişiyor; P'den yere inen kırmızı kesikli dikme h.](gorsel/tyt-matematik/19-04-capraz.svg "Kırmızı h, iki direğe de paraleldir. Mavi ip ile D köşesinden, yeşil ip ile B köşesinden birer benzerlik kurulur.")

**Çözüm.** $P$'den yere dik $[PH]$ çiz, $|PH| = h$, $|BH| = y$ olsun. $[PH]$ iki direğe de paraleldir.

1. Yeşil ip, $B$ köşesi: $\triangle BHP \sim \triangle BDC$. $\dfrac{h}{3} = \dfrac{y}{9}$.
2. Mavi ip, $D$ köşesi: $\triangle DHP \sim \triangle DBA$. $\dfrac{h}{6} = \dfrac{9 - y}{9}$.
3. İki eşitliği topla: $\dfrac{h}{3} + \dfrac{h}{6} = \dfrac{y + 9 - y}{9} = 1 \Rightarrow \dfrac{3h}{6} = 1 \Rightarrow h = 2$ m.
4. İstenirse yer de bulunur: $y = 3h = 6$ m. $P$, kısa direğe daha yakındır.

**Kural:** Boyları $a$ ve $b$ olan iki direk için kesişme yüksekliği

$$h = \frac{a \cdot b}{a + b} \qquad \text{ya da} \qquad \frac{1}{h} = \frac{1}{a} + \frac{1}{b}$$

Direkler arasındaki uzaklık sonucu **değiştirmez**; soruda verilse de çoğu zaman yalnızca seni şaşırtmak içindir.

> **Tuzak:** Direklerin ortalamasını almak: $\dfrac{6 + 3}{2} = 4{,}5$ yanlıştır. $h$ her zaman **kısa direkten de kısadır**. Sonucun kısa direkten büyük çıktıysa hata yapmışsın demektir.

## ÖSYM tuzakları

> **Tabanı ortak köşeden ölçmemek.** Lambada büyük üçgenin tabanı $s + d$'dir, $d$ değil. Tahterevallide büyük üçgenin kenarı tahtanın tamamıdır, desteğin ötesindeki parça değil.

> **Paralel ışın ile noktasal ışığı karıştırmak.** Güneşte (paralel ışın) boy/gölge oranı herkes için aynıdır. Lambada (tek noktadan çıkan ışık) bu oran, kişinin lambaya uzaklığına bağlıdır.

> **Yükseklik ile yükseklik farkını karıştırmak.** Rampa sorularında uzaklıklar yığınlar arasında verilmişse kutu sayılarının **farkı** kullanılır.

> **Ortalama almak.** Çapraz iplerin kesişme yüksekliği $\dfrac{ab}{a + b}$'dir; $\dfrac{a + b}{2}$ seçeneklerde hazır bekler.

> **Fazladan verilen uzunluk.** Çapraz iplerde direkler arası uzaklık, tahterevallide tahtanın boyu (destek ortadaysa) sonucu etkilemez. Her veriyi kullanmak zorunda değilsin.

## Kendini dene

### Soru 1
$6$ m yüksekliğindeki bir sokak lambasının dibinden $7$ m uzakta, $1{,}8$ m boyundaki bir kişi duruyor. Bu kişinin lamba ışığıyla oluşan gölgesi kaç metredir?

A) 2,1
B) 3
C) 4,2
D) 7
E) 10

**Cevap:** B
**Çözüm:** Gölge $x$ ise $\dfrac{1{,}8}{6} = \dfrac{x}{x + 7} \Rightarrow 6x = 1{,}8x + 12{,}6 \Rightarrow 4{,}2x = 12{,}6 \Rightarrow x = 3$. $2{,}1$, paydaya $x + 7$ yerine $7$ yazmaktır ($\frac{1{,}8 \cdot 7}{6}$); $10$ ise gölgenin ucunun direğe uzaklığıdır ($3 + 7$).

### Soru 2
Aralarında $5$ m bulunan $2$ m ve $3$ m yüksekliğindeki iki dik direğin her birinin tepesinden öbürünün dibine birer ip geriliyor. İplerin kesiştiği nokta yerden kaç metre yüksektedir?

A) 1,2
B) 1,5
C) 2,5
D) 3
E) 5

**Cevap:** A
**Çözüm:** $h = \dfrac{2 \cdot 3}{2 + 3} = \dfrac{6}{5} = 1{,}2$. Kontrol: $\dfrac{1}{1{,}2} = \dfrac{5}{6} = \dfrac{1}{2} + \dfrac{1}{3}$. $2{,}5$ ortalamadır; kısa direkten (2 m) büyük olduğu için olamaz. $5$ m uzaklık sonucu etkilemez.

### Soru 3
Yerdeki $P$ noktasından başlayan düz bir rampa, $40$ cm yüksekliğindeki bir kutunun üst köşesine değiyor. Bu köşenin $P$'ye yatay uzaklığı $1{,}2$ m'dir. Rampa üzerinde, $P$'ye yatay uzaklığı $3$ m olan noktanın yerden yüksekliği kaç cm'dir?

A) 60
B) 80
C) 100
D) 120
E) 180

**Cevap:** C
**Çözüm:** İki dik üçgen $P$ köşesini paylaşır: $\dfrac{40}{y} = \dfrac{1{,}2}{3} \Rightarrow y = \dfrac{40 \cdot 3}{1{,}2} = 100$ cm. $60$, uzaklığı kutudan ölçmektir ($\frac{40 \cdot 1{,}8}{1{,}2}$); $120$ ise $40$'ı $3$ ile çarpıp $1{,}2$'ye bölmeyi unutmaktır.

## Özet kartı

- Her uygulamada bir köşeyi paylaşan, dik kenarları paralel iki dik üçgen ara; A.A. ile benzerdirler.
- Uzunlukları her zaman **ortak köşeden** ölç.
- Lamba ve gölge: $\dfrac{h}{H} = \dfrac{s}{s + d}$.
- Tahterevalli: havadaki uç $= \dfrac{h \cdot L}{a}$; destek ortadaysa $2h$.
- Düz rampa: yükseklik farkı / yatay uzaklık sabittir.
- Çapraz ipler: $h = \dfrac{ab}{a + b}$, direkler arası uzaklıktan bağımsız ve kısa direkten kısa.

## Sonraki adım

Alıştırmaya geç (aşağıdaki düğme). Sonraki konu: **Üçgenin Yardımcı Elemanları**, ilk ders **Üçgende Açıortay ve Özellikleri**. Orada açıortayın karşı kenarı nasıl orantılı böldüğünü göreceksin; ispatı yine bugünkü benzerlik fikrine dayanır.
