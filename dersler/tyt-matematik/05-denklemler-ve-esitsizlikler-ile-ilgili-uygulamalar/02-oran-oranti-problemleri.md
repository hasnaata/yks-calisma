---
baslik: Oran-Orantı Problemleri
ders: tyt-matematik
sure: 20 dk
kaynak: MEBİ Konu Özeti 5b79ab590f
guncelleme: 2026-11-17
---
# Oran-Orantı Problemleri

**Bu dersin sonunda:** bir problemdeki iki çokluğun doğru mu ters mi orantılı olduğuna karar verip doğru çarpımı kurabilecek, bir miktarı verilen sayılarla doğru ya da ters orantılı paylaştırabileceksin.

> **TYT'de yeri:** Her yıl en az bir soru doğrudan orantı kurmaya dayanır: "kaç işçi kaç günde", "erzak kaç gün yeter", "para yaşlarla ters orantılı paylaştırılıyor". Yeni nesil sorularda tarif, dişli, yazıcı gibi günlük durumlar verilir; işlem kısadır, asıl iş orantının türünü doğru seçmektir.

## Önce hatırla

<details><summary>Oran-orantı kavramlarından: $\frac{a}{3} = \frac{b}{5}$ ve $a + b = 40$ ise $a$ kaçtır?</summary>
Orantı sabitine $k$ de: $a = 3k$, $b = 5k$. $3k + 5k = 8k = 40$, $k = 5$. Buradan $a = 15$. (Payların toplamı paydaların toplamına bölününce orantı sabiti değişmez: $\frac{40}{8} = 5$.)
</details>

<details><summary>Oran-orantı kavramlarından: $a$ ile $b$ ters orantılıdır. $a = 6$ iken $b = 10$ ise $a = 15$ iken $b$ kaçtır?</summary>
Ters orantıda çarpım sabittir: $a \cdot b = 6 \cdot 10 = 60$. $15 \cdot b = 60$, $b = 4$.
</details>

## Doğru orantı: bölüm sabit

**Örnek.** 6 kg elma 90 TL ise aynı elmadan 10 kg kaç TL olur?

Elma artarsa ödenecek para da **aynı oranda** artar: doğru orantı. Fiyatın kilograma bölümü sabittir:

$$\frac{90}{6} = \frac{x}{10} \quad\Rightarrow\quad 6 \cdot x = 90 \cdot 10 \quad\Rightarrow\quad x = 150 \text{ TL}$$

Kısa yazım: alt alta yaz, **çapraz** çarp.

| | Elma | Fiyat |
|---|---|---|
| Bilinen | 6 kg | 90 TL |
| İstenen | 10 kg | $x$ |

$6 \cdot x = 10 \cdot 90$ olur.

**Kural.** $a$ ile $b$, $c$ ile $x$ karşılık gelen değerler ve çokluklar doğru orantılıysa $\frac{a}{c} = \frac{b}{x}$, yani $a \cdot x = b \cdot c$ (çapraz çarpım).

TYT'de doğru orantılı tipik çiftler: alınan ürün ile ödenen para, hız sabitken yol ile süre, süre sabitken işçi sayısı ile yapılan iş, yapılan iş ile harcanan süre.

## Ters orantı: çarpım sabit

**Örnek.** 12 işçi bir işi 15 günde bitiriyor. Aynı hızda çalışan 20 işçi bu işi kaç günde bitirir?

İşçi artarsa süre **azalır**: ters orantı. İşin büyüklüğü sabittir ve "işçi × gün" ile ölçülür:

$$12 \cdot 15 = 20 \cdot x \quad\Rightarrow\quad 180 = 20x \quad\Rightarrow\quad x = 9 \text{ gün}$$

Aynı tabloyu kurarsan bu kez **düz** (aynı satırdakileri) çarparsın: $12 \cdot 15 = 20 \cdot x$.

**Kural.** Çokluklar ters orantılıysa karşılık gelen değerlerin çarpımı sabittir: $a \cdot b = c \cdot x$.

Tipik ters orantılı çiftler: yol sabitken hız ile süre, iş sabitken işçi sayısı ile bitirme süresi, yiyecek sabitken kişi sayısı ile yetme süresi.

![İki grafik yan yana. Solda elma kilogramı ile fiyat: orijinden geçen doğru, 6 kg'da 90 TL ve 10 kg'da 150 TL işaretli. Sağda işçi sayısı ile gün: azalan eğri, 12 işçide 15 gün ve 20 işçide 9 gün işaretli.](gorsel/tyt-matematik/05-02-dogru-ters-grafik.svg "Doğru orantının grafiği orijinden geçen bir doğrudur, bölüm sabittir. Ters orantının grafiği azalan bir eğridir, çarpım sabittir.")

### Arada durum değişirse

**Örnek.** 30 kişilik bir kampın yiyeceği 12 gün yetecektir. 6 gün sonra kampa 10 kişi daha katılıyor. Kalan yiyecek kaç gün yeter?

6 gün geçti; kalan yiyecek 30 kişiye **6 gün** yetecek kadardır. Şimdi kişi sayısı 40:

$$30 \cdot 6 = 40 \cdot x \quad\Rightarrow\quad x = \frac{180}{40} = 4{,}5 \text{ gün}$$

**Kural.** Durum yolun ortasında değişiyorsa önce **kalan** miktarı bul, orantıyı yalnızca kalan için kur.

## Hangi orantı? Önce karar ver

Formül ezberlemek yerine her soruda tek bir soru sor: "Biri artınca diğeri ne yapıyor?"

![Karar şeması: iki çokluğu belirle, sonra biri artınca diğeri artıyorsa doğru orantı ve çapraz çarpım, azalıyorsa ters orantı ve düz çarpım.](gorsel/tyt-matematik/05-02-karar.svg "Önce yön, sonra çarpım. Doğru orantıda bölüm, ters orantıda çarpım sabit kalır.")

Dikkat: Her artan ilişki doğru orantı değildir. "Aynı oranda" artmalı. Yaş artınca boy da artar ama 10 yaşındaki çocuk 5 yaşındakinin iki katı boyda değildir; böyle çokluklar orantılı değildir.

## Bir miktarı orantılı paylaştırmak

**Örnek (doğru orantılı).** 360 TL, 3, 4 ve 5 sayılarıyla doğru orantılı paylaştırılıyor. Paylar nedir?

Paylar $3k$, $4k$, $5k$ olur. $3k + 4k + 5k = 12k = 360$, $k = 30$. Paylar $90$, $120$, $150$ TL. Büyük sayıya büyük pay düşer.

**Örnek (ters orantılı).** 180 ceviz, 2, 3 ve 6 sayılarıyla ters orantılı paylaştırılıyor. Paylar nedir?

Ters orantıda pay ile sayının **çarpımı** sabittir: paylar $\frac{k}{2}$, $\frac{k}{3}$, $\frac{k}{6}$.

$$\frac{k}{2} + \frac{k}{3} + \frac{k}{6} = \frac{3k + 2k + k}{6} = k = 180$$

Paylar $90$, $60$, $30$. Küçük sayıya büyük pay düşer.

Kısa yol: ters orantılı paylaştırma, terslerle doğru orantılı paylaştırmadır. $\frac{1}{2}, \frac{1}{3}, \frac{1}{6}$ oranlarını paydaların EKOK'u olan 6 ile genişlet: $3 : 2 : 1$. Toplam 6 parça, bir parça $30$.

![Altı eşit kutudan oluşan şerit, her kutuda 30 yazıyor. İlk üç kutu mavi: 2 ile, 3 parça, 90. Sonraki iki kutu yeşil: 3 ile, 2 parça, 60. Son kutu sarı: 6 ile, 1 parça, 30.](gorsel/tyt-matematik/05-02-ters-paylastirma.svg "2, 3 ve 6 ile ters orantı, 3 : 2 : 1 oranına dönüşür. En küçük sayı olan 2 en çok parçayı alır.")

**Kural.** $x, y, z$ sırasıyla $a, b, c$ ile doğru orantılıysa $x = ak$, $y = bk$, $z = ck$. Ters orantılıysa $x = \frac{k}{a}$, $y = \frac{k}{b}$, $z = \frac{k}{c}$; terslerin paydalarını EKOK ile eşitleyip parça sayısına çevirmek en hızlı yoldur.

## İkiden fazla çokluk: bileşik orantı

**Örnek.** 5 işçi 8 günde 400 parça üretiyor. Aynı hızda çalışan 6 işçi 10 günde kaç parça üretir?

Üretilen parça hem işçi sayısıyla hem gün sayısıyla doğru orantılıdır. Bir işçinin bir günde ürettiği parça sabittir:

$$\frac{400}{5 \cdot 8} = 10 \quad\Rightarrow\quad 6 \cdot 10 \cdot 10 = 600 \text{ parça}$$

**Kural.** İş $=$ işçi sayısı $\times$ süre $\times$ (bir işçinin birim zamandaki işi). Bu üçlüden hangisi istenirse diğerlerini sabit kabul ederek oradan çek. Günlük çalışma saati verilirse süreyi "işçi × gün × saat" olarak say.

## ÖSYM tuzakları

> **Ters orantıda çapraz çarpmak:** "12 işçi 15 günde, 20 işçi kaç günde?" sorusunda $12 \cdot x = 20 \cdot 15$ yazan 25 gün bulur. İşçi arttı, süre artamaz. Sonucu her zaman "mantıklı mı?" diye kontrol et.

> **Geçen süreyi düşmemek:** Erzak ya da iş sorusunda durum ortada değişiyorsa orantıyı toplam süreyle değil kalan süreyle kur. Kampta 6 günü düşmeyen $30 \cdot 12 = 40 \cdot x$ ile 9 gün bulur, doğrusu 4,5 gün.

> **Ters orantılı paylaştırmada büyük sayıya büyük pay vermek:** 2, 3 ve 6 ile ters orantılı paylaştırmada en çok payı 2'ye karşılık gelen kişi alır. Soruda "yaşlarıyla ters orantılı" gibi ifadeyi gördüğünde en küçüğün en çok alacağını hemen not et.

> **Orantılı olmayan çoklukları orantılı sanmak:** Yaş ile boy, bir kenar ile alan gibi çokluklar birlikte artsa da aynı oranda artmaz. Orantı kurmadan önce "iki katına çıkınca diğeri de iki katına çıkıyor mu?" diye sor.

## Kendini dene

### Soru 1
9 metre kumaş 270 TL'dir. Aynı kumaştan 14 metre kaç TL'dir?

A) 360
B) 390
C) 420
D) 450
E) 480

**Cevap:** C
**Çözüm:** Kumaş arttıkça fiyat aynı oranda artar: doğru orantı. Metresi $\frac{270}{9} = 30$ TL, 14 metre $14 \cdot 30 = 420$ TL. Çapraz çarpımla: $9 \cdot x = 14 \cdot 270$, $x = 420$.

### Soru 2
8 işçi bir duvarı 9 günde örmektedir. Aynı hızda çalışan 12 işçi bu duvarı kaç günde örer?

A) 4
B) 6
C) 8
D) 12
E) 13,5

**Cevap:** B
**Çözüm:** İşçi artınca süre azalır: ters orantı, çarpım sabit. $8 \cdot 9 = 72 = 12 \cdot x$, $x = 6$ gün. Çapraz çarpan $\frac{9 \cdot 12}{8} = 13{,}5$ bulur; işçi arttığı hâlde sürenin artması bunun yanlış olduğunu gösterir.

### Soru 3
400 TL, 3, 4 ve 12 sayılarıyla ters orantılı olarak üç kişiye paylaştırılıyor.

Buna göre en çok pay alan kişi kaç TL alır?

A) 50
B) 100
C) 150
D) 175
E) 200

**Cevap:** E
**Çözüm:** Paylar $\frac{k}{3}$, $\frac{k}{4}$, $\frac{k}{12}$. Ortak payda 12: $\frac{4k + 3k + k}{12} = \frac{8k}{12} = 400$, $k = 600$. Paylar $200$, $150$, $50$. En çok alan, en küçük sayı olan 3'e karşılık gelen kişidir: 200 TL. 50, en çok payı 12'ye veren yanlış düşünceden gelir.

## Özet kartı

- Biri artınca diğeri aynı oranda artıyorsa doğru orantı: bölüm sabit, çapraz çarp.
- Biri artınca diğeri aynı oranda azalıyorsa ters orantı: çarpım sabit, düz çarp.
- Durum ortada değişirse önce kalan miktarı bul, orantıyı kalan için kur.
- Doğru orantılı paylaştırma: paylar $ak, bk, ck$. Ters orantılı: $\frac{k}{a}, \frac{k}{b}, \frac{k}{c}$; EKOK ile parçaya çevir.
- Bileşik orantı: iş $=$ işçi $\times$ süre $\times$ verim.
- Sonucu mantıkla kontrol et: işçi artınca süre kısalmalı.

## Sonraki adım

Alıştırmaya geç (aşağıdaki düğme). Sonraki ders **Sayı Problemleri**; problem metnini denkleme çevirirken burada kurduğun orantılar sık sık işine yarayacak.
