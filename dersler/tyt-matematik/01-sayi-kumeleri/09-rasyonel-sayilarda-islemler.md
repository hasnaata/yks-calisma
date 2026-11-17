---
baslik: Rasyonel Sayılarda İşlemler
ders: tyt-matematik
sure: 25 dk
kaynak: MEBİ Konu Özeti 7999b16dd9
guncelleme: 2026-11-17
---
# Rasyonel Sayılarda İşlemler

**Bu dersin sonunda:** kesirlerle dört işlemi doğru sırayla yapabilecek, iç içe (merdiven) kesirleri sadeleştirebilecek ve "kalanın $\frac{2}{3}$'ü" gibi ifadeleri doğru çarpıma çevirebileceksin.

> **TYT'de yeri:** Kesir işlemleri her yıl 1–2 doğrudan soru olarak gelir: "işleminin sonucu kaçtır?", iç içe kesir, ardışık çarpımda sadeleşme. Daha önemlisi, problem sorularının neredeyse hepsi sonunda bir kesir işlemine dönüşür. Burada yapılan küçük bir hata (ters çevirmeyi unutmak, işlem sırasını karıştırmak) bütün soruyu götürür.

## Önce hatırla

<details><summary>Ondalık ve devirli ondalık sayılardan: $1{,}2\overline{3}$ sayısını en sade kesir olarak yaz.</summary>
Sayının tamamı $123$, devretmeyen kısım $12$. Virgülden sonra 1 devreden (9) ve 1 devretmeyen (0) basamak var: $\frac{123 - 12}{90} = \frac{111}{90} =$ <b>$\frac{37}{30}$</b>.
</details>

<details><summary>Ondalık ve devirli ondalık sayılardan: $0{,}24 : 0{,}008$ işleminin sonucu kaçtır?</summary>
Bölende 3 basamak var; pay ve paydayı $1000$ ile çarp: $\frac{0{,}24}{0{,}008} = \frac{240}{8} =$ <b>30</b>.
</details>

## Toplama ve çıkarma: önce paydalar

**Örnek.** $\frac{1}{2} + \frac{1}{3}$ kaçtır?

Yarım ile üçte bir aynı büyüklükte parçalar değildir; doğrudan toplanamaz. İkisini de **altıda birlere** bölersek parçalar eşitlenir: $\frac{1}{2} = \frac{3}{6}$, $\frac{1}{3} = \frac{2}{6}$. Toplam $\frac{5}{6}$.

![Beş yatay şerit: yarısı boyalı şerit, üçte biri boyalı şerit; altta bu ikisi altı eş parçaya bölünmüş hâlde 3 ve 2 parça boyalı; en altta toplam, altı parçanın beşi boyalı.](gorsel/tyt-matematik/01-09-payda-esitleme.svg "Paydayı eşitlemek parçaları aynı boya getirmektir. Parçalar eşitlenince yalnızca sayılır: 3 + 2 = 5 altıda bir.")

**Örnek.** $\frac{5}{6} + \frac{7}{15}$ kaçtır?

$\text{EKOK}(6, 15) = 30$. Birinci kesri $5$ ile, ikinciyi $2$ ile genişlet:

$$\frac{5}{6} + \frac{7}{15} = \frac{25}{30} + \frac{14}{30} = \frac{39}{30} = \frac{13}{10}$$

**Kural.** Paydalar eşit değilse **EKOK'ta** eşitle, payları topla (çıkar), ortak paydayı aynen yaz:

$$\frac{a}{b} + \frac{c}{d} = \frac{a \cdot d + b \cdot c}{b \cdot d}$$

Bu genel formül her zaman doğrudur ama $b \cdot d$ büyük bir sayı verir; EKOK ile çalışmak sonraki sadeleştirmeyi kısaltır.

**Tam sayılı kesir.** $2\frac{1}{3} - 1\frac{3}{4}$ işleminde önce bileşik kesre çevir: $2\frac{1}{3} = \frac{2 \cdot 3 + 1}{3} = \frac{7}{3}$, $1\frac{3}{4} = \frac{7}{4}$. Sonra

$$\frac{7}{3} - \frac{7}{4} = \frac{28}{12} - \frac{21}{12} = \frac{7}{12}$$

> **Tuzak:** $\frac{5}{6} + \frac{7}{15} = \frac{5 + 7}{6 + 15} = \frac{12}{21}$ yazmak. Paydalar **asla** toplanmaz. Kontrol: $\frac{5}{6}$ tek başına $\frac{12}{21} \approx 0{,}57$'den büyük; toplam ondan küçük olamaz.

## Çarpma: pay paya, payda paydaya

**Örnek.** $\frac{2}{3} \cdot \frac{3}{4}$ kaçtır?

Bir karenin $\frac{3}{4}$'ünü boya, sonra boyalı kısmın $\frac{2}{3}$'ünü al. Kare $3 \cdot 4 = 12$ küçük kareye bölünür; ortak kısım $2 \cdot 3 = 6$ küçük kare: $\frac{6}{12} = \frac{1}{2}$.

![Dört sütun ve üç satıra bölünmüş bir kare. Soldaki üç sütun mavi (dörtte üç), alttaki iki satır yeşil (üçte iki). İkisinin ortak bölgesi kırmızı çerçeveli altı küçük kare.](gorsel/tyt-matematik/01-09-carpma-alan.svg "Paylar çarpılınca ortak bölgedeki kare sayısı (2 · 3 = 6), paydalar çarpılınca bütündeki kare sayısı (3 · 4 = 12) çıkar.")

**Örnek.** $2\frac{1}{4} \cdot \frac{8}{15}$ kaçtır?

Önce bileşik kesir: $2\frac{1}{4} = \frac{9}{4}$. Çarpmadan önce **çapraz sadeleştir**: $9$ ile $15$'i $3$'e, $8$ ile $4$'ü $4$'e böl.

$$\frac{9}{4} \cdot \frac{8}{15} = \frac{3}{1} \cdot \frac{2}{5} = \frac{6}{5}$$

**Kural.** $\dfrac{a}{b} \cdot \dfrac{c}{d} = \dfrac{a \cdot c}{b \cdot d}$. Çarpmada payda eşitlemek gerekmez. Herhangi bir paydaki sayı herhangi bir paydadaki sayıyla sadeleşebilir; önce sadeleştirmek büyük sayılarla uğraşmayı önler.

**"…'ü" demek çarpmak demektir.** "$60$'ın $\frac{2}{3}$'ü" $= 60 \cdot \frac{2}{3} = 40$; "$\frac{3}{4}$'ün $\frac{2}{3}$'ü" $= \frac{3}{4} \cdot \frac{2}{3} = \frac{1}{2}$.

> **Tuzak:** $2\frac{1}{4} \cdot 4$ işleminde yalnızca tam kısmı çarpıp $8\frac{1}{4}$ yazmak. $2\frac{1}{4}$ aslında $2 + \frac{1}{4}$'tür; ikisi de çarpılır: $\frac{9}{4} \cdot 4 = 9$. Tam sayılı kesri **önce** bileşik kesre çevir.

## Bölme: ikinciyi ters çevir, çarp

**Örnek.** $\frac{3}{4} : \frac{1}{8}$ kaçtır?

Soru şudur: $\frac{3}{4}$'ün içine $\frac{1}{8}$'lik kaç parça sığar? Sayı doğrusunda $0$'dan $\frac{3}{4}$'e $\frac{1}{8}$'lik adımlarla git: **6** adım.

![0 ile 1 arası sekiz eş parçaya bölünmüş sayı doğrusu. 0'dan dörtte üçe kadar kırmızı; üstünde 1'den 6'ya numaralı altı yay, her biri sekizde birlik bir adım.](gorsel/tyt-matematik/01-09-bolme-sigma.svg "Bölme, kaç parça sığar sorusudur. Sekizde birlik adımları say: dörtte üçe 6 adımda varılır.")

Aynı sonucu kural da verir: $\frac{3}{4} : \frac{1}{8} = \frac{3}{4} \cdot \frac{8}{1} = 6$.

**Örnek.** $\frac{3}{4} : \frac{9}{8}$ kaçtır? Birinci kesir aynen kalır, ikinci ters çevrilir:

$$\frac{3}{4} : \frac{9}{8} = \frac{3}{4} \cdot \frac{8}{9} = \frac{1}{1} \cdot \frac{2}{3} = \frac{2}{3}$$

**Kural.** $\dfrac{a}{b} : \dfrac{c}{d} = \dfrac{a}{b} \cdot \dfrac{d}{c} = \dfrac{a \cdot d}{b \cdot c}$ ($c \ne 0$). Ters çevrilen **yalnızca bölen** (ikinci kesir). Tam sayılı kesir varsa yine önce bileşik kesre çevir.

> **Tuzak:** Birinci kesri ya da ikisini birden ters çevirmek. $\frac{3}{4} : \frac{9}{8}$ için birinciyi çeviren $\frac{4}{3} \cdot \frac{9}{8} = \frac{3}{2}$ bulur; bu, sorunun tersi olan $\frac{9}{8} : \frac{3}{4}$'tür.

## İşlem sırası

Birden çok işlem varsa sıra, tam sayılardaki sıranın aynısıdır.

![Yukarıdan aşağı beş adım: tam sayılı kesri bileşik kesre çevir, parantez içi, çarpma ve bölme soldan sağa, toplama ve çıkarma EKOK ile, sonucu sadeleştir.](gorsel/tyt-matematik/01-09-islem-yolu.svg "Çarpma ile bölme aynı basamaktadır: hangisi soldaysa önce o yapılır.")

**Örnek.** $\left[\left(\frac{1}{2} - \frac{1}{5}\right) \cdot \frac{10}{9}\right] : \frac{2}{3}$ kaçtır?

1. İç parantez: $\frac{1}{2} - \frac{1}{5} = \frac{5}{10} - \frac{2}{10} = \frac{3}{10}$.
2. Köşeli parantez: $\frac{3}{10} \cdot \frac{10}{9} = \frac{3}{9} = \frac{1}{3}$.
3. Bölme: $\frac{1}{3} : \frac{2}{3} = \frac{1}{3} \cdot \frac{3}{2} = \frac{1}{2}$.

**Örnek.** $\frac{5}{6} : \frac{2}{3} : \frac{5}{4}$ kaçtır? Parantez yok, iki bölme var: **soldan sağa**.

$$\left(\frac{5}{6} \cdot \frac{3}{2}\right) : \frac{5}{4} = \frac{5}{4} : \frac{5}{4} = 1$$

**Kural.** Parantez → çarpma ve bölme (soldan sağa) → toplama ve çıkarma (soldan sağa).

> **Tuzak:** Sağdaki bölmeyi önce yapmak. $\frac{5}{6} : \left(\frac{2}{3} : \frac{5}{4}\right) = \frac{5}{6} : \frac{8}{15} = \frac{25}{16}$ olur; sonuç değişir. Parantez yoksa sağdan başlama.

## İç içe (merdiven) kesirler

**Örnek.** $1 - \cfrac{1}{1 + \cfrac{1}{1 + \frac{1}{2}}}$ kaçtır?

En alttaki kesirden başla, yukarı doğru çık:

1. $1 + \frac{1}{2} = \frac{3}{2}$
2. $\frac{1}{3/2} = \frac{2}{3}$, sonra $1 + \frac{2}{3} = \frac{5}{3}$
3. $\frac{1}{5/3} = \frac{3}{5}$
4. $1 - \frac{3}{5} = \frac{2}{5}$

**Kural.** $\dfrac{1}{\;a/b\;} = \dfrac{b}{a}$: 1'in bir kesre bölümü, o kesrin tersidir. Merdivende hep **en alttan** başla ve her basamakta tek bir kesre indir.

## Kesrin kesri: "tamamının" mı, "kalanın" mı?

**Örnek.** Bir depodaki suyun önce $\frac{1}{4}$'ü, sonra **kalanın** $\frac{2}{3}$'ü kullanılıyor. Deponun ne kadarı kalır?

İlk adımdan sonra $1 - \frac{1}{4} = \frac{3}{4}$ kalır. Bunun $\frac{2}{3}$'ü kullanılırsa $\frac{1}{3}$'ü kalır:

$$\frac{3}{4} \cdot \frac{1}{3} = \frac{1}{4}$$

Soru "**tamamının** $\frac{2}{3}$'ü" deseydi kalan $1 - \frac{1}{4} - \frac{2}{3} = \frac{1}{12}$ olurdu.

**Kural.** "Kalanın $\frac{p}{q}$'su kullanıldı" → geriye kalanın $\left(1 - \frac{p}{q}\right)$'su kalır; ardışık adımlarda bu oranlar **çarpılır**. "Tamamının" denince hepsi aynı bütünden düşülür.

## ÖSYM tuzakları

> **Paydaları toplamak:** $\frac{a}{b} + \frac{c}{d} \ne \frac{a + c}{b + d}$. Toplama ve çıkarmada payda eşitlenir; yalnızca çarpmada paydalar çarpılır.

> **Tam sayılı kesirde yalnızca tam kısmı işlemek:** $3\frac{1}{2} \cdot 2 = 7$'dir, $6\frac{1}{2}$ değil. İşlemden önce bileşik kesre çevir.

> **Yanlış kesri ters çevirmek:** Bölmede yalnızca **bölen** (ikinci kesir) ters çevrilir.

> **Çarpma–bölmede sağdan başlamak:** $a : b \cdot c = \frac{a}{b} \cdot c$'dir, $\frac{a}{b \cdot c}$ değil.

> **"Kalanın" kelimesini atlamak:** "Kalanın $\frac{1}{3}$'ü" ile "tamamının $\frac{1}{3}$'ü" farklı sayılardır. Soru kökünde bu kelimenin altını çiz.

## Kendini dene

### Soru 1
$\dfrac{2}{3} - \dfrac{1}{4} + \dfrac{5}{6}$ işleminin sonucu kaçtır?

A) $\frac{6}{13}$
B) $\frac{5}{9}$
C) $1$
D) $\frac{5}{4}$
E) $\frac{3}{2}$

**Cevap:** D
**Çözüm:** $\text{EKOK}(3, 4, 6) = 12$: $\frac{8}{12} - \frac{3}{12} + \frac{10}{12} = \frac{15}{12} = \frac{5}{4}$. Payları ve paydaları ayrı ayrı işleyen $\frac{2 - 1 + 5}{3 + 4 + 6} = \frac{6}{13}$ bulur; $\frac{5}{12} + \frac{5}{6}$ adımında paydaları toplayan $\frac{10}{18} = \frac{5}{9}$ bulur.

### Soru 2
$1\dfrac{1}{2} : \dfrac{3}{4} \cdot \dfrac{1}{6}$ işleminin sonucu kaçtır?

A) $\frac{1}{9}$
B) $\frac{3}{16}$
C) $\frac{1}{3}$
D) $2$
E) $12$

**Cevap:** C
**Çözüm:** $1\frac{1}{2} = \frac{3}{2}$. Soldan sağa: $\frac{3}{2} : \frac{3}{4} = \frac{3}{2} \cdot \frac{4}{3} = 2$, sonra $2 \cdot \frac{1}{6} = \frac{1}{3}$. Önce çarpmayı yapan $\frac{3}{2} : \frac{1}{8} = 12$ bulur; ters çevirmeyi unutan $\frac{3}{2} \cdot \frac{3}{4} \cdot \frac{1}{6} = \frac{3}{16}$ bulur; $1\frac{1}{2}$'yi $\frac{1}{2}$ diye okuyan $\frac{1}{9}$, son çarpmayı unutan $2$ bulur.

### Soru 3
Bir öğrenci harçlığının $\frac{2}{5}$'ini kitaba, kalanın $\frac{1}{3}$'ünü yemeğe harcıyor ve geriye $120$ TL kalıyor.

Buna göre öğrencinin harçlığı kaç TL'dir?

A) $200$
B) $300$
C) $360$
D) $450$
E) $600$

**Cevap:** B
**Çözüm:** Kitaptan sonra $\frac{3}{5}$ kalır. Bunun $\frac{1}{3}$'ü harcanınca $\frac{2}{3}$'ü kalır: $\frac{3}{5} \cdot \frac{2}{3} = \frac{2}{5}$. Harçlığın $\frac{2}{5}$'i $120$ TL ise harçlık $120 : \frac{2}{5} = 120 \cdot \frac{5}{2} = 300$ TL. "Kalanın" kelimesini atlayıp $1 - \frac{2}{5} - \frac{1}{3} = \frac{4}{15}$ kullanan $450$ bulur.

## Özet kartı

- Toplama, çıkarma: paydaları EKOK'ta eşitle, payları topla; paydalar toplanmaz.
- Çarpma: pay paya, payda paydaya; önce çapraz sadeleştir.
- Bölme: birinci aynen, ikinci (bölen) ters, sonra çarp.
- Tam sayılı kesri her işlemden önce bileşik kesre çevir.
- Sıra: parantez → çarpma ve bölme soldan sağa → toplama ve çıkarma; merdiven kesirde en alttan başla.
- "Kalanın" oranları çarpılır; "tamamının" oranları aynı bütünden düşülür.

## Sonraki adım

Alıştırmaya geç (aşağıdaki düğme). Sonraki konu **Bölünebilme Kuralları**; ilk ders **Tam Sayılarda Kalanlı Bölme İşlemi**. Kesirleri sadeleştirirken kullandığın ortak bölen fikri orada kurala dönüşecek.
