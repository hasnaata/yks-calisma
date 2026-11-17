---
baslik: Rutin Olmayan Problemler
ders: tyt-matematik
sure: 25 dk
kaynak: MEBİ Konu Özeti 50f9db09ce
guncelleme: 2026-11-17
---
# Rutin Olmayan Problemler

**Bu dersin sonunda:** hazır formülü olmayan bir problemde tablo kurarak tam sayı çözümlerini sistematik deneyebilecek, tekrar eden durumlarda örüntüyü bulabilecek ve sonucu verilen işlemleri geriye doğru çözebileceksin.

> **TYT'de yeri:** TYT'de her yıl birkaç soru bu türdendir: bir günlük hayat durumu, birkaç kural ve "en çok kaç?", "en az kaç?", "kaçıncı?" ya da "saat kaçta?" sorusu. İşlem yükü azdır; puanı, verileri düzenleyip **sistemli** düşünen alır.

## Önce hatırla

<details><summary>Hareket problemlerinden: Aralarında 300 km bulunan iki araç aynı anda birbirine doğru saatte 70 km ve 80 km hızla yola çıkıyor. Kaç saat sonra karşılaşırlar?</summary>
Zıt yönde aradaki uzaklık her saat $70 + 80 = 150$ km kapanır. $300 \div 150 = $ <b>2 saat</b>. Bu derste de aynı fikri kullanacaksın: bir durumun "her adımda" ne kadar değiştiğini bulup adımları sayacaksın.
</details>

<details><summary>Hareket problemlerinden: Bir araç bir yolu saatte 60 km hızla gidip saatte 90 km hızla dönüyor. Gidiş dönüşteki ortalama hızı kaçtır?</summary>
$V_{ort} = \frac{2 \cdot 60 \cdot 90}{60 + 90} = \frac{10\,800}{150} = $ <b>72 km/sa</b>. Hızların ortalaması olan 75 değil. Burada olduğu gibi rutin olmayan sorularda da ilk akla gelen kestirme çoğu zaman tuzaktır.
</details>

## Rutin olmayan problem nedir?

Bildiğin bir formülü yerine koyarak çözülemeyen, verileri düzenlemeyi ve bir **strateji** seçmeyi gerektiren problemlerdir. Sayı, örüntü, sayma ya da şekil bilgisi gerekebilir; ama asıl iş, problemi düzenli bir hâle getirmektir. Her soruda aynı sırayı izle:

![Akış şeması: Verileni ve isteneni yaz, sonra Hangi strateji sorusu. Tam sayı ve en çok en az durumunda tablo ya da liste yap; tekrar eden durumda örüntüyü bul; sonuç verilmişse geriye doğru çalış. Üç yol da cevabı soruda kontrol et kutusunda birleşir.](gorsel/tyt-matematik/05-11-yontem.svg "Önce veriyi yaz, sonra soru tipine göre stratejiyi seç. Son adımı, yani kontrolü, hiçbir zaman atlama.")

Bu derste en sık kullanılan üç stratejiyi göreceksin.

## Strateji 1: Tablo yap, tam sayı çözümleri dene

**Örnek.** Bir kırtasiyede kalemler yalnızca 3'lü ve 5'li paketlerle satılıyor. Tam 47 kalem alan biri **en az** kaç paket almıştır? **En çok** kaç paket almış olabilir?

3'lü paket sayısı $x$, 5'li paket sayısı $y$ olsun: $3x + 5y = 47$. Burada $x$ ve $y$ **doğal sayıdır**; kesirli paket olmaz.

Paket sayısını azaltmak için büyük paketten çok almak gerekir; o yüzden $y$'yi en büyük değerinden başlayarak dene. $47 - 5y$ sayısı 3'e bölünüyorsa o satır bir çözümdür:

![Tablo: y değerleri 9'dan 0'a kadar, altında 47 eksi 5y değerleri ve x değerleri. y eşittir 7, 4 ve 1 sütunları yeşil; bu sütunlarda x sırasıyla 4, 9 ve 14. Yeşil sütunlar arasında y eksi 3 okları var.](gorsel/tyt-matematik/05-11-deneme-tablosu.svg "Yalnızca yeşil sütunlar çözümdür. Çözümlerde y üçer üçer, x beşer beşer değişir.")

| $y$ | $x$ | Paket sayısı $x + y$ |
|---|---|---|
| 7 | 4 | **11** (en az) |
| 4 | 9 | 13 |
| 1 | 14 | **15** (en çok) |

En az **11**, en çok **15** paket. Kontrol: $3 \cdot 4 + 5 \cdot 7 = 12 + 35 = 47$.

**Kural.**

- Bilinmeyenlerin **doğal sayı** olduğunu unutma; denklemi kur, bir bilinmeyeni sırayla dene.
- Toplamı en az yapmak için büyük katsayılı bilinmeyeni en büyük, en çok yapmak için en küçük al.
- Bir çözüm bulunca diğerleri düzenli gelir: $3x + 5y$ denkleminde $y$ 3 azalırsa $x$ 5 artar. Tablonun hepsini doldurman gerekmez.
- "Her birinden **en az bir** tane" denirse $0$ değerini tablodan çıkar.

## Strateji 2: Liste yap, örüntüyü bul

**Örnek.** Bir uyarı lambası saat 13.00.00'da ilk kez yanıyor ve sonra her 50 saniyede bir yanıyor.

a) 13.00 ile 13.30 arasında (iki an da dahil) lamba kaç kez **tam dakika başında** yanar?
b) Lamba 30. kez saat kaçta yanar?

a) İlk birkaç yanışı saniye olarak listele: $0, 50, 100, 150, 200, 250, 300, \dots$ Tam dakika başı 60'ın katı demektir. Hem 50'nin hem 60'ın katı olan ilk sayı $\text{EKOK}(50, 60) = 300$ saniye, yani 5 dakika.

![Zaman çizelgesi: 13.00 ile 13.05 arası dakika çizgileri. Üstte 0, 50, 100, 150, 200, 250 ve 300. saniyelerde lamba yanışları. 0 ve 300'deki yanışlar yeşil ve dakika çizgisiyle çakışıyor.](gorsel/tyt-matematik/05-11-zaman-cizelgesi.svg "Mavi yanışlar dakika çizgilerine denk gelmiyor; yalnızca yeşil olanlar, yani 5 dakikada bir olanlar denk geliyor.")

Dakika başındaki yanışlar 13.00, 13.05, 13.10, 13.15, 13.20, 13.25, 13.30: **7 kez**.

b) 1. yanış 13.00.00'da. 30. yanışa kadar $30 - 1 = 29$ aralık vardır: $29 \cdot 50 = 1450$ saniye. $1450 = 24 \cdot 60 + 10$, yani 24 dakika 10 saniye. Cevap **13.24.10**.

**Kural.**

- İlk birkaç durumu listele; tekrar eden adımı bul.
- İki farklı tekrarın çakışması EKOK kadar sürede bir olur.
- $n$. olaya kadar $n - 1$ aralık vardır (çit direği kuralı). Birinci olay "sıfırıncı saniyede" olur.

**Şekil örüntüsü.** Aynı fikir şekillerde de çalışır. Kibritlerle yan yana kareler yapılıyor:

![Kibritten yan yana kareler. 1. adımda 1 kare 4 kibrit, 2. adımda 2 kare 7 kibrit, 3. adımda 3 kare 10 kibrit. Her adımda eklenen 3 kibrit kırmızı.](gorsel/tyt-matematik/05-11-kibrit-kare.svg "Yeni kare soldaki kareyle bir kenarı paylaşır, bu yüzden 4 değil 3 kibrit ekler.")

İlk kare 4 kibrit, sonraki her kare 3 kibrit ekler: $n$ kare için $4 + 3(n - 1) = 3n + 1$ kibrit. 20 kare için $3 \cdot 20 + 1 = 61$ kibrit. 100 kibritle en çok kaç kare yapılır? $3n + 1 \le 100$, $n \le 33$: **33 kare** (bir kibrit artar).

## Strateji 3: Geriye doğru çalış

**Örnek.** Bir öğrenci harçlığının yarısıyla kitap aldı, sonra 20 TL'lik yemek yedi, sonra kalan paranın yarısını kardeşine verdi. Elinde 15 TL kaldı. Harçlığı kaç TL idi?

Sonuç belli, başlangıç bilinmiyor. Sondan başla ve her işlemi **tersiyle** geri al:

| Adım | İleri işlem | Geri işlem | Para |
|---|---|---|---|
| Son durum | | | 15 |
| Kardeşine yarısı | $\div 2$ | $\cdot 2$ | 30 |
| Yemek | $- 20$ | $+ 20$ | 50 |
| Kitap (yarısı) | $\div 2$ | $\cdot 2$ | **100** |

Harçlık **100 TL**. Kontrol: $100 \to 50 \to 30 \to 15$.

**Kural.** Sonucu verilen bir işlem zincirinde sondan başla; işlemlerin **sırasını** ve **yönünü** ters çevir: çıkarmanın tersi toplama, yarıya bölmenin tersi 2 ile çarpma.

## ÖSYM tuzakları

> **Sıfırı unutmak ya da yanlışlıkla saymak:** "Her türden en az bir" denince $0$ olmaz; denmiyorsa $0$ da bir çözüm olabilir. Soruyu bu gözle bir daha oku.

> **Kesirli çözümü kabul etmek:** Paket, kişi, masa sayısı tam sayıdır. $3x + 5y = 47$ için $y = 9$ alınca $x = \frac{2}{3}$ çıkar; bu satır çözüm değildir.

> **Çit direği hatası:** 30. olaya kadar 30 değil 29 aralık vardır. "13.00 ile 13.30 arası, iki uç dahil" denirse ilk anı da say.

> **"En az" sorusunda aşağı yuvarlamak:** İlki 4, sonraki her biri 2 koltuk ekleyen sıralarla 25 kişi oturtmak için $2n + 2 \ge 25$ gerekir. $n = 11{,}5$ çıkar; $n = 11$ yalnızca 24 kişi oturtur, cevap 12'dir.

> **Geriye giderken sırayı korumak:** Son yapılan işlem ilk geri alınır. Önce $-20$'yi geri alıp sonra $\cdot 2$ yaparsan yanlış sonuç bulursun.

## Kendini dene

### Soru 1
Bir mağazada tişörtler 40 TL'ye, gömlekler 70 TL'ye satılıyor. Bu mağazadan her birinden en az bir tane alıp toplam 600 TL ödeyen biri en çok kaç parça ürün almıştır?

A) 9
B) 10
C) 12
D) 14
E) 15

**Cevap:** C
**Çözüm:** Tişört $a$, gömlek $b$ tane: $40a + 70b = 600$, yani $4a + 7b = 60$. $60 - 7b$ sayısının 4'e bölünmesi için $b$ 4'ün katı olmalı. $b = 4$ için $a = 8$ (12 parça), $b = 8$ için $a = 1$ (9 parça). En çok 12. 15, $b = 0$ alıp "en az bir" koşulunu bozmaktır; 9 en az parça sayısıdır.

### Soru 2
Kibritlerle yan yana üçgenler yapılıyor. İlk üçgen 3 kibritle yapılıyor; her yeni üçgen bir öncekiyle bir kenarı ortak kullandığı için 2 kibrit ekliyor.

Buna göre 20 üçgen için kaç kibrit gerekir?

A) 40
B) 41
C) 42
D) 60
E) 63

**Cevap:** B
**Çözüm:** İlk üçgen 3, sonraki 19 üçgenin her biri 2 kibrit: $3 + 2 \cdot 19 = 41$. Genel kural $2n + 1$. 60, ortak kenarları iki kez saymaktır ($3 \cdot 20$); 40 ilk üçgenin fazladan kibritini unutmaktır.

### Soru 3
Bir sayı önce 3 ile çarpılıyor, sonra sonuçtan 5 çıkarılıyor, en son da bulunan sayı 2'ye bölünüyor. Sonuç 14 olduğuna göre başlangıçtaki sayı kaçtır?

A) 3
B) 7
C) 11
D) 23
E) 33

**Cevap:** C
**Çözüm:** Son işlemden başla ve tersini uygula: $\div 2$'nin tersi $14 \cdot 2 = 28$; $-5$'in tersi $28 + 5 = 33$; $\cdot 3$'ün tersi $33 \div 3 = 11$. Kontrol: $11 \cdot 3 = 33$, $33 - 5 = 28$, $28 \div 2 = 14$. 33 son geri adımı unutmaktır; 3, işlemleri ters çevirmeden $(14 - 5) \div 3$ yapmaktır.

## Özet kartı

- Önce verileni ve isteneni yaz; formül arama, strateji seç.
- Tam sayı + en çok/en az: denklemi kur, bir bilinmeyeni sırayla dene, tabloya yaz.
- Tekrar eden durum: ilk birkaç adımı listele; çakışma EKOK'ta, $n$. olaya $n - 1$ aralık.
- Şekil örüntüsü: ilk şekil + (adım sayısı $- 1$) $\cdot$ eklenen miktar.
- Sonuç verilmişse geriye doğru çalış: sırayı ve işlemi ters çevir.
- Bulduğun cevabı soruya koyup kontrol et.

## Sonraki adım

Alıştırmaya geç (aşağıdaki düğme). Sonraki konu **Önermeler**; orada bu dersteki "akıl yürütme" adımlarını mantık diliyle yazmayı öğreneceksin.
