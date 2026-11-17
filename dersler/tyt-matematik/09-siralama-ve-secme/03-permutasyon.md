---
baslik: Permütasyon
ders: tyt-matematik
sure: 25 dk
kaynak: MEBİ Konu Özeti 90c5f9f8a3
guncelleme: 2026-11-17
---
# Permütasyon

**Bu dersin sonunda:** $n$ farklı nesneden $r$ tanesinin kaç farklı biçimde sıralanabileceğini $P(n, r)$ ile hesaplayabilecek, $P(n, r)$ içeren denklemleri çözebilecek ve "belirli yerde", "yan yana", "yan yana olmasın", "mutlaka bulunsun" kısıtlı sıralamaları sayabileceksin.

> **TYT'de yeri:** Permütasyon çoğu zaman adı geçmeden sorulur: "kaç farklı biçimde sıralanabilir?", "ilk üç derece kaç farklı biçimde oluşabilir?", "X ile Y yan yana olmak koşuluyla kaç farklı sıralama vardır?" gibi. Ayrıca $P(n, r)$ içeren kısa bir denklem sorusu da gelebilir.

## Önce hatırla

<details><summary>Faktöriyel kavramından: $\dfrac{7! + 8!}{6!}$ işleminin sonucu kaçtır?</summary>
Küçük faktöriyele göre düzenle: $8! = 8 \cdot 7!$. Pay $7! + 8 \cdot 7! = 7! \cdot (1 + 8) = 9 \cdot 7!$. $7! = 7 \cdot 6!$ olduğundan $\dfrac{9 \cdot 7 \cdot 6!}{6!} = 63$.
</details>

<details><summary>Faktöriyel kavramından: $15! = 3^k \cdot A$ ($A$ ve $k$ doğal sayı) ise $k$ en çok kaçtır?</summary>
15'i kalan 3'ten küçük olana kadar 3'e böl ve bölümleri topla: $15 : 3 = 5$, $5 : 3 = 1$ (kalan 2). $k = 5 + 1 = 6$.
</details>

## Permütasyon nedir?

**Örnek.** $\{1, 2, 3\}$ kümesinin rakamlarıyla, rakamları farklı iki basamaklı kaç sayı yazılabilir?

Hepsini yaz: $12, 21, 13, 31, 23, 32$. Toplam **6** sayı. $12$ ile $21$ aynı iki rakamdan oluşur ama **farklı** sayılardır: burada sıra önemlidir.

| Seçilen rakamlar | Sıralamalar |
|---|---|
| 1 ve 2 | 12, 21 |
| 1 ve 3 | 13, 31 |
| 2 ve 3 | 23, 32 |

**Tanım.** $r \le n$ olmak üzere $n$ elemanlı bir kümenin birbirinden farklı $r$ elemanından oluşan her **sıralı diziliş**e $n$'nin $r$'li bir **permütasyonu** denir. Bunların sayısı $P(n, r)$ ile gösterilir. Yukarıdaki örnekte $P(3, 2) = 6$.

## $P(n, r)$ formülü

**Örnek.** Bir koşuya 7 atlet katılıyor. Birinci, ikinci ve üçüncü kaç farklı biçimde belirlenebilir? (Beraberlik yok.)

Saymanın temel ilkesiyle üç kutu aç. Birinciliğe 7 atletten biri, ikinciliğe kalan 6 atletten biri, üçüncülüğe kalan 5 atletten biri gelir:

$$7 \cdot 6 \cdot 5 = 210.$$

![Kutu yöntemi: 1., 2. ve 3. derece için üç kutu; içlerinde 7, 6 ve 5 yazıyor, sonuç 210. Altta P(7, 3) eşittir 7 faktöriyel bölü 4 faktöriyel eşittir 7 çarpı 6 çarpı 5.](gorsel/tyt-matematik/09-03-kutular.svg "Kutu sayısı r kadar, ilk kutuda n yazar ve sayılar birer azalır. Faktöriyelli yazım aynı çarpımın kısa hâlidir.")

Bu çarpımı faktöriyelle yazabilirsin: $7 \cdot 6 \cdot 5 = \dfrac{7 \cdot 6 \cdot 5 \cdot 4!}{4!} = \dfrac{7!}{4!}$.

**Kural.**
$$P(n, r) = \frac{n!}{(n - r)!} = \underbrace{n \cdot (n-1) \cdot (n-2) \cdots}_{r \text{ tane çarpan}}$$

Pratikte faktöriyel yazmana gerek yok: $n$'den başlayıp **$r$ tane** azalan sayı çarp. Örneğin $P(9, 2) = 9 \cdot 8 = 72$, $P(6, 4) = 6 \cdot 5 \cdot 4 \cdot 3 = 360$.

| İfade | Değer | Neden? |
|---|---|---|
| $P(n, 0)$ | $1$ | $\frac{n!}{n!}$; hiç seçmemenin tek yolu var |
| $P(n, 1)$ | $n$ | tek kutu, $n$ seçenek |
| $P(n, n)$ | $n!$ | $\frac{n!}{0!}$ ve $0! = 1$ |
| $P(n, n-1)$ | $n!$ | son kutuya tek seçenek kalır |

$P(n, n) = n!$ şu demektir: $n$ farklı nesne yan yana $n!$ biçimde sıralanır. 5 kişi bir sırada $5! = 120$ biçimde oturur.

## $P(n, r)$ içeren denklemler

**Örnek 1.** $P(n, 2) = 42$ ise $n$ kaçtır?

$P(n, 2) = n \cdot (n - 1)$. Ardışık iki sayının çarpımı 42: $7 \cdot 6 = 42$. Yani $n = 7$.

**Örnek 2.** $P(n, 3) = 10 \cdot P(n, 2)$ ise $n$ kaçtır?

Açık yaz: $n(n-1)(n-2) = 10 \cdot n(n-1)$. İki tarafta da $n(n-1)$ var, sadeleştir: $n - 2 = 10$, $n = 12$.

**Kural.** $P(n, r)$'yi $n(n-1)\cdots$ biçiminde açık yaz, ortak çarpanları sadeleştir. Sonuçta $n \ge r$ olmalı.

## Belirli bir eleman bulunsun ya da bulunmasın

**Örnek.** Birbirinden farklı 7 kitaptan 3'ü bir rafa yan yana dizilecek. Kitaplardan biri sözlük.

a) Sözlüğün **bulunmadığı** kaç diziliş vardır?
b) Sözlüğün **bulunduğu** kaç diziliş vardır?

a) Sözlüğü kenara koy, 6 kitap kalır: $P(6, 3) = 6 \cdot 5 \cdot 4 = 120$.

b) Bütün dizilişler $P(7, 3) = 210$. Sözlüğün bulunduğu dizilişler: $210 - 120 = 90$.

Doğrudan da sayabilirsin: sözlük 3 yerden birine konur (3 yol), kalan 2 yere 6 kitaptan sıralı seçim yapılır, $P(6, 2) = 30$. Toplam $3 \cdot 30 = 90$.

**Kural.** Eleman bulunmasın: o elemanı kümeden çıkar, $P(n-1, r)$. Eleman bulunsun: $P(n, r) - P(n-1, r)$.

## Belirli yer kısıtı

**Örnek.** Ali, Banu ve 3 arkadaşı tek sırada oturacak (5 kişi).

a) Ali en başta olmak üzere kaç sıralama vardır?
b) Ali ve Banu uçlarda olmak üzere kaç sıralama vardır?

a) Ali'nin yeri sabit (1 yol). Kalan 4 kişi kalan 4 yere: $4! = 24$.

b) Uçlara Ali ile Banu: Ali solda Banu sağda ya da tersi, $2! = 2$ yol. Ortadaki 3 yere 3 kişi: $3! = 6$. Toplam $2 \cdot 6 = 12$.

**Kural.** Kısıtlı yeri **önce** doldur, sonra kalanları serbestçe sırala. "Uçlarda" denince iki kişinin yer değiştirmesini ($2!$) unutma.

## Yan yana olsun, yan yana olmasın

**Örnek.** A, B, C, D, E adlı 5 kişi tek sırada duracak.

a) A ile B **yan yana** olmak üzere kaç sıralama vardır?
b) A ile B **yan yana olmamak** üzere kaç sıralama vardır?

a) A ile B'yi bir pakete koy ve tek kişi gibi düşün. Paket + C + D + E = 4 nesne: $4! = 24$. Paketin içinde AB ya da BA: $2! = 2$. Toplam $24 \cdot 2 = 48$.

![Blok yöntemi: A ve B kesikli bir çerçeve içinde tek blok, yanında C, D, E kutuları. Blok ve 3 kişi 4 nesne, 4 faktöriyel eşittir 24; blok içi 2 faktöriyel eşittir 2; sonuç 24 çarpı 2 eşittir 48.](gorsel/tyt-matematik/09-03-blok.svg "Blok tek nesne gibi sayılır, sonra bloğun içi ayrıca sıralanır. İçteki 2 faktöriyeli unutmak en sık yapılan hatadır.")

b) Tümü $5! = 120$. Yan yana olanlar 48. Yan yana olmayanlar: $120 - 48 = 72$.

**Kural.** $k$ kişi yan yana olacaksa: onları tek blok say, $(n - k + 1)!$; bloğun içini sırala, $k!$. Sonuç $(n - k + 1)! \cdot k!$. "Yan yana olmasın" = tümü − yan yana.

![Yöntem şeması: Kısıtı bul. Belirli yer ise önce o yeri doldur. Yan yana olsun ise blok yap, içini sırala. Yan yana olmasın ise tümü eksi yan yana. Eleman bulunsun ise tümü eksi bulunmayan.](gorsel/tyt-matematik/09-03-yontem.svg "Sıralama sorusunda önce kısıtın türünü belirle; her türün kendi kısa yolu var.")

## ÖSYM tuzakları

> **$P(n, r)$'yi $\frac{n!}{r!}$ sanmak:** $P(7, 3) = \frac{7!}{4!} = 210$'dur; $\frac{7!}{3!} = 840$ değil. Paydada $(n - r)!$ var. Kısa yol: $n$'den başlayıp $r$ tane çarpan.

> **Blok içini unutmak:** A ile B yan yana olan 5 kişilik sıralama $4! = 24$ değil, $4! \cdot 2! = 48$'dir. AB ile BA farklı sıralamalardır.

> **"Uçlarda" sorusunda yer değiştirmeyi unutmak:** Ali ve Banu uçlardaysa $3! = 6$ değil, $2! \cdot 3! = 12$ sıralama vardır.

> **"Bulunsun" sorusunda yeri unutmak:** Sözlük mutlaka bulunacaksa sözlüğü yalnızca başa koyup $P(6, 2) = 30$ demek eksiktir; sözlük 3 yerden birinde olabilir: $3 \cdot 30 = 90$. Emin değilsen tümleyeni kullan: $P(7,3) - P(6,3)$.

> **$P(n, n-1)$ ile $P(n, n)$:** İkisi de $n!$'e eşittir. $P(5, 4) = 5 \cdot 4 \cdot 3 \cdot 2 = 120 = 5!$. Seçeneklerde ikisini farklı sanma.

## Kendini dene

### Soru 1
$P(6, 2) + P(5, 5)$ işleminin sonucu kaçtır?

A) 31
B) 135
C) 150
D) 390
E) 480

**Cevap:** C
**Çözüm:** $P(6, 2) = 6 \cdot 5 = 30$. $P(5, 5) = 5! = 120$. Toplam $30 + 120 = 150$. 31, $P(5, 5)$'i 1 sanmaktır; 135, $P(6, 2)$ yerine sırasız seçim sayısı 15'i almaktır; 480, $P(6, 2)$'yi $\frac{6!}{2!} = 360$ sanmaktır.

### Soru 2
$P(n, 2) = 72$ olduğuna göre $n$ kaçtır?

A) 8
B) 9
C) 12
D) 36
E) 72

**Cevap:** B
**Çözüm:** $P(n, 2) = n(n - 1) = 72$. Ardışık iki sayının çarpımı 72: $9 \cdot 8$. Büyük olan $n$: $n = 9$. 8, çarpımı $n(n + 1)$ sanmaktır; 36 ise 72'yi 2'ye bölmektir.

### Soru 3
Aralarında Deniz ile Efe'nin de bulunduğu 6 kişi tek sırada fotoğraf çektirecektir. Deniz ile Efe **yan yana olmamak** koşuluyla kaç farklı sıralama yapılabilir?

A) 120
B) 240
C) 360
D) 480
E) 720

**Cevap:** D
**Çözüm:** Tümü $6! = 720$. Yan yana olanlar: Deniz–Efe bloğu + 4 kişi = 5 nesne, $5! = 120$; blok içi $2! = 2$; toplam $240$. Yan yana olmayanlar $720 - 240 = 480$. 240 yan yana olanların sayısıdır; 720 kısıtsız sıralama sayısıdır; 120 ise blok içini unutup yalnızca $5!$ yazmaktır.

## Özet kartı

- Permütasyon = sıralı diziliş; sıra değişince yeni bir diziliş olur.
- $P(n, r) = \frac{n!}{(n-r)!}$ = $n$'den başlayan $r$ tane azalan sayının çarpımı.
- $P(n, 0) = 1$, $P(n, 1) = n$, $P(n, n) = P(n, n-1) = n!$.
- Eleman bulunsun = $P(n, r) - P(n - 1, r)$.
- Yan yana: blok tek nesne, sonra bloğun içi ($k!$). Yan yana olmasın = tümü − yan yana.
- Belirli yer kısıtında önce o yeri doldur.

## Sonraki adım

Alıştırmaya geç (aşağıdaki düğme). Sonraki ders **Tekrarlı Permütasyon**; KALEM gibi farklı harfleri değil, ANKARA gibi tekrar eden harfleri sıralamayı öğreneceksin.
