---
baslik: İşçi Problemleri
ders: tyt-matematik
sure: 20 dk
kaynak: MEBİ Konu Özeti f28501b49a
guncelleme: 2026-11-17
---
# İşçi Problemleri

**Bu dersin sonunda:** bir işi kimin ne kadar sürede bitirdiğinden günlük iş miktarını bulup birlikte çalışma, işçi sayısı değişimi, işten ayrılma ve havuz problemlerini tek bir yöntemle çözebileceksin.

> **TYT'de yeri:** Soru genellikle şöyle gelir: "A bir işi 6 günde, B 12 günde bitiriyor; birlikte kaç günde?", "birlikte 4 gün çalıştıktan sonra biri ayrılıyor…", "musluk doldururken gider açık unutulmuş…". Bazen bir grafik ya da tabloyla verilir. Her sorunun anahtarı aynıdır: **süreleri değil, birim zamanda yapılan işleri topla.**

## Önce hatırla

<details><summary>Yaş problemlerinden: Bir annenin yaşı kızının yaşının 3 katıdır. 10 yıl sonra annenin yaşı kızının yaşının 2 katı olacaktır. Kızın şimdiki yaşı kaçtır?</summary>
Kız $x$, anne $3x$ yaşında olsun. 10 yıl sonra ikisi de 10 yaş büyür: $3x + 10 = 2(x + 10)$, buradan $x = 10$. Kontrol: şimdi 10 ve 30; 10 yıl sonra 20 ve 40. Bu derste de aynı fikir var: her durumu ayrı yaz, sonra denklemi kur.
</details>

<details><summary>Yaş problemlerinden: İki kardeşin yaşları farkı 6'dır. 4 yıl sonra yaşları toplamı 30 olacaktır. Büyük kardeş şimdi kaç yaşındadır?</summary>
Büyük $x$ ise küçük $x - 6$. 4 yıl sonra toplam $2 \cdot 4 = 8$ artar: $x + (x - 6) + 8 = 30$, $2x = 28$, $x = 14$. Yaş farkının hiç değişmediğini hatırla; bu derste değişmeyen şey de bir işçinin **günlük hızı** olacak.
</details>

## Bir günde yapılan iş

**Örnek.** Bir boyacı bir odayı tek başına 8 saatte boyuyor. 3 saatte odanın ne kadarını boyar, geriye ne kadarı kalır?

İşin tamamına 1 dersek boyacı saatte $\frac{1}{8}$ iş yapar. 3 saatte $3 \cdot \frac{1}{8} = \frac{3}{8}$'ini boyar; geriye $1 - \frac{3}{8} = \frac{5}{8}$ kalır.

**Kural.** Bir işi tek başına $x$ günde bitiren biri **1 günde $\frac{1}{x}$'ini**, $a$ günde $\frac{a}{x}$'ini yapar. Yapılan iş = hız $\times$ süre.

## Birlikte çalışma

**Örnek.** Ali bir işi 6 günde, Bora aynı işi 12 günde bitiriyor. İkisi birlikte bu işi kaç günde bitirir?

*Kesirle:* Bir günde Ali $\frac{1}{6}$, Bora $\frac{1}{12}$ iş yapar. Birlikte günlük iş toplanır:

$$\frac{1}{6} + \frac{1}{12} = \frac{2}{12} + \frac{1}{12} = \frac{3}{12} = \frac{1}{4} \quad\Rightarrow\quad 4 \text{ gün}$$

*Birimle (daha hızlı):* İşe $\text{EKOK}(6, 12) = 12$ birim de. Ali günde $12 \div 6 = 2$, Bora günde $12 \div 12 = 1$ birim yapar. Birlikte günde 3 birim: $12 \div 3 = 4$ gün.

![On iki kutudan oluşan şerit dört gruba ayrılmış. Her grupta iki mavi kutu Ali'nin, bir sarı kutu Bora'nın bir günlük işi. Grupların altında 1. gün, 2. gün, 3. gün, 4. gün yazıyor.](gorsel/tyt-matematik/05-06-birlikte.svg "Her gün 2 mavi ve 1 sarı birim dolar. 12 birimlik iş 4 günde biter.")

**Kural.** Tek başına $a$ ve $b$ günde bitirenler birlikte $t$ günde bitiriyorsa

$$\frac{1}{a} + \frac{1}{b} = \frac{1}{t}$$

Pratik yol: işe süreler EKOK'u kadar birim de, günlük birimleri topla, toplam birimi böl. Birlikte süre, **en hızlı kişinin süresinden bile kısadır** (burada $4 < 6$).

## Hızlar arasındaki oran verilirse

**Örnek.** Bir usta, çırağının 2 katı hızla çalışıyor. İkisi birlikte bir işi 8 günde bitiriyor. Çırak bu işi tek başına kaç günde bitirir?

Çırak günde $k$ birim yapsın; usta $2k$ yapar. Birlikte günde $3k$, 8 günde $24k$ birim: işin tamamı $24k$. Çırak tek başına $24k \div k = 24$ günde, usta $24k \div 2k = 12$ günde bitirir.

**Kural.** "2 kat hızlı" ise süresi **yarıdır**. Hızlara $k$, $2k$ de; işi (birlikte hız) $\times$ (birlikte süre) olarak bul.

## İşçi sayısı ve süre: ters orantı

**Örnek.** Aynı güçteki 6 işçi bir işi 10 günde bitiriyor. Aynı işi 4 işçi kaç günde bitirir?

İş $6 \cdot 10 = 60$ "işçi-gün"dür. 4 işçi: $60 \div 4 = 15$ gün. İşçi azaldı, süre arttı: ters orantı.

**Örnek.** 3 işçi 2 duvarı 8 günde örüyor. Aynı güçteki 6 işçi 5 duvarı kaç günde örer?

Bir duvar $\frac{3 \cdot 8}{2} = 12$ işçi-gün. 5 duvar $60$ işçi-gün, 6 işçi ile $60 \div 6 = 10$ gün.

**Kural.** Aynı güçteki işçiler için

$$\frac{\text{işçi sayısı} \cdot \text{süre}}{\text{iş miktarı}} = \text{sabit}$$

İşçi sayısı ile süre ters, iş miktarı ile süre doğru orantılıdır.

## Biri işi bırakırsa

**Örnek.** A bir işi 10 günde, B 15 günde bitiriyor. İkisi birlikte 4 gün çalıştıktan sonra A işi bırakıyor. Kalan işi B kaç günde bitirir?

İşe $\text{EKOK}(10, 15) = 30$ birim de. A günde 3, B günde 2 birim yapar.

- Birlikte 4 gün: $4 \cdot (3 + 2) = 20$ birim.
- Kalan: $30 - 20 = 10$ birim.
- B tek başına: $10 \div 2 = 5$ gün.

![Zaman çizelgesi. A'nın şeridi 0 ile 4. gün arasında, B'nin şeridi 0 ile 9. gün arasında. 4. günde kırmızı kesikli çizgi: A ayrılıyor. Altta: ilk 4 günde 20 birim, kalan 10 birim B ile 5 günde biter.](gorsel/tyt-matematik/05-06-ayrilma.svg "Her aralıkta kim çalışıyorsa onun hızını yaz. B ayrıldıktan sonra 5 gün daha çalışır; iş toplam 9 günde biter.")

**Kural.** Çalışanlar değişiyorsa işi **zaman aralıklarına böl**: her aralıkta (o aralıkta çalışanların günlük işi) $\times$ (gün). Aralıkların toplamı işin tamamıdır. Soru "kalan iş kaç günde" mi, "iş toplam kaç günde" mi, oku.

## Havuz: dolduran artı, boşaltan eksi

**Örnek.** Bir musluk boş havuzu 6 saatte dolduruyor. Havuzun dibindeki gider, dolu havuzu 9 saatte boşaltıyor. Havuz boşken ikisi birlikte açılırsa havuz kaç saatte dolar?

Musluk saatte $\frac{1}{6}$ doldurur, gider saatte $\frac{1}{9}$ boşaltır. Gider ters yönde çalışır, **çıkarılır**:

$$\frac{1}{6} - \frac{1}{9} = \frac{3}{18} - \frac{2}{18} = \frac{1}{18} \quad\Rightarrow\quad 18 \text{ saat}$$

![Grafik: yatay eksen saat, dikey eksen havuzdaki su. Mavi doğru 6. saatte doluya ulaşıyor: yalnız musluk. Kırmızı doğru 18. saatte doluya ulaşıyor: musluk ve gider birlikte.](gorsel/tyt-matematik/05-06-havuz.svg "Gider açıkken doğru yatıklaşır: saatte yalnızca 1/18 dolar, havuz 6 değil 18 saatte dolar.")

**Kural.** Havuz problemi bir işçi problemidir: dolduranların hızı **artı**, boşaltanların hızı **eksi** işaretle toplanır. Sonuç pozitifse havuz dolar; süre = 1 $\div$ (net hız).

## ÖSYM tuzakları

> **Süreleri toplamak ya da ortalamasını almak:** 6 ve 12 günde bitirenler için "18 gün" ya da "9 gün" yazmak. Birlikte süre, en hızlı kişinin süresinden kısadır; doğru cevap 4 gün. Toplanan şey süre değil, günlük iştir.

> **Birim sayısını gün sanmak:** İşe 30 birim deyip kalanı 10 birim bulduktan sonra "10 gün" işaretlemek. Kalan birimi, çalışanın günlük birimine bölmeyi unutma.

> **İşçi sayısı ile süreyi doğru orantı sanmak:** 6 işçi 10 günde bitiriyorsa 4 işçi daha az günde bitirmez; daha uzun sürer (15 gün).

> **Gideri eklemek ya da süreleri çıkarmak:** Musluk 6, gider 9 saatte ise $\frac{1}{6} + \frac{1}{9}$ yazmak ya da $9 - 6 = 3$ saat demek. Gider suyu azaltır: hızlar çıkarılır, cevap 18 saat.

> **"Kalan" ile "toplam"ı karıştırmak:** B'nin kalan işi bitirdiği süre 5 gün, işin bittiği toplam süre 9 gündür. Seçeneklerde ikisi de bulunur.

## Kendini dene

### Soru 1
Deniz bir işi 10 günde, Ece aynı işi 15 günde bitirebiliyor.

Buna göre ikisi birlikte bu işi kaç günde bitirir?

A) 6
B) 8
C) 12,5
D) 15
E) 25

**Cevap:** A
**Çözüm:** İşe $\text{EKOK}(10, 15) = 30$ birim de. Deniz günde 3, Ece günde 2 birim yapar; birlikte günde 5 birim. $30 \div 5 = 6$ gün. 12,5 sürelerin ortalaması, 25 toplamıdır; ikisi de 10'dan büyük olduğu için hemen elenir.

### Soru 2
Aynı güçteki 10 işçi bir işi 6 günde bitiriyor.

Bu işin 4 günde bitmesi için aynı güçte kaç işçi çalışmalıdır?

A) 8
B) 12
C) 15
D) 18
E) 24

**Cevap:** C
**Çözüm:** İş $10 \cdot 6 = 60$ işçi-gün. 4 günde bitmesi için $60 \div 4 = 15$ işçi gerekir. Süre kısaldığına göre işçi sayısı artmalıdır; 10'dan az olan 8 bu yüzden elenir.

### Soru 3
Bir musluk boş bir depoyu 4 saatte dolduruyor. Deponun dibindeki musluk ise dolu depoyu 12 saatte boşaltıyor.

Depo boşken iki musluk birlikte açılırsa depo kaç saatte dolar?

A) 3
B) 6
C) 8
D) 12
E) 16

**Cevap:** B
**Çözüm:** Saatte net dolan kısım $\frac{1}{4} - \frac{1}{12} = \frac{3}{12} - \frac{1}{12} = \frac{2}{12} = \frac{1}{6}$; depo 6 saatte dolar. Hızları toplayan $\frac{1}{4} + \frac{1}{12} = \frac{1}{3}$ ile 3 saat; süreleri çıkaran $12 - 4 = 8$ saat bulur.

## Özet kartı

- $x$ günde biten işin 1 günde $\frac{1}{x}$'i yapılır; yapılan iş = hız $\times$ süre.
- Birlikte çalışmada günlük işler toplanır: $\frac{1}{a} + \frac{1}{b} = \frac{1}{t}$. Hızlısı: işe süreler EKOK'u kadar birim de.
- Birlikte süre, en hızlı kişinin süresinden kısadır.
- Aynı güçteki işçilerde (işçi $\cdot$ süre) / iş sabittir; işçi sayısı ile süre ters orantılıdır.
- Çalışanlar değişiyorsa işi zaman aralıklarına böl, her aralığın işini topla.
- Havuzda dolduran artı, boşaltan eksi: süre = 1 $\div$ net hız.

## Sonraki adım

Alıştırmaya geç (aşağıdaki düğme). Sonraki ders **Yüzde Problemleri**; orada da bütünü kolay bir sayı (100) seçerek işlemi kesirsiz yapacaksın, tıpkı burada işe EKOK kadar birim dediğin gibi.
