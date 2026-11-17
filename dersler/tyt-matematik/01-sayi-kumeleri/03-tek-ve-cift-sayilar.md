---
baslik: Tek ve Çift Sayılar
ders: tyt-matematik
sure: 20 dk
kaynak: MEBİ Konu Özeti 11e883cea3
guncelleme: 2026-11-17
---
# Tek ve Çift Sayılar

**Bu dersin sonunda:** bir toplamın, farkın, çarpımın ya da kuvvetin tek mi çift mi olduğunu sayıları hesaplamadan bulabilecek ve "hangisi kesinlikle doğrudur?" sorularında bilinmeyenin tek ya da çift olduğunu çıkarabileceksin.

> **TYT'de yeri:** Genellikle şu kalıpta gelir: "$a$ ve $b$ tam sayılar, $3a + 4b$ tek sayı olduğuna göre aşağıdakilerden hangisi kesinlikle doğrudur?" Yeni nesil sorularda ise bir oyunun, lambanın ya da tablonun sonucu "tek mi çift mi" akıl yürütmesiyle bulunur. Çoğu zaman hesap gerekmez, kural gerekir.

## Önce hatırla

<details><summary>Temel işlemlerden: $(-1)^{2027} - (-1)^{2026}$ işleminin sonucu kaçtır?</summary>
Negatif sayının tek kuvveti negatif, çift kuvveti pozitiftir: $(-1)^{2027} = -1$, $(-1)^{2026} = 1$. Sonuç $-1 - 1 = -2$, yani <b>−2</b>. Üssün tek ya da çift olması bu derste de karşına çıkacak.
</details>

<details><summary>Temel işlemlerden: $6 \cdot 47 + 6 \cdot 53$ işlemini kısa yoldan yap.</summary>
Ortak çarpanı dışarı al (dağılma özelliği): $6 \cdot (47 + 53) = 6 \cdot 100 = 600$. Bu derste aynı fikri kullanacaksın: $2k + 2m = 2(k + m)$ olduğu için iki çift sayının toplamı çifttir.
</details>

## Tek sayı, çift sayı

**Örnek.** $-6,\ -3,\ 0,\ 7,\ 14$ sayılarından hangileri çifttir?

Bir tam sayı 2'ye kalansız bölünüyorsa **çift**tir: $-6 = 2 \cdot (-3)$, $0 = 2 \cdot 0$, $14 = 2 \cdot 7$. Çift olanlar $-6$, $0$ ve $14$. 2'ye bölününce 1 kalanını verenler **tek**tir: $-3 = 2 \cdot (-2) + 1$, $7 = 2 \cdot 3 + 1$.

![Eksi 5'ten 6'ya kadar sayı doğrusu. Çift sayılar mavi nokta ve Ç harfiyle, tek sayılar kırmızı nokta ve T harfiyle gösterilmiş; renkler sırayla değişiyor.](gorsel/tyt-matematik/01-03-sayi-dogrusu.svg "Tam sayılar sırayla bir tek, bir çift gelir. 0 da negatif sayılar da bu sıraya dahildir: 0 çift, −1 tektir.")

**Kural.** $k$ bir tam sayı olmak üzere:

| | Genel biçim | Küme |
|---|---|---|
| Çift sayı | $2k$ | $\{\dots, -4, -2, 0, 2, 4, \dots\}$ |
| Tek sayı | $2k + 1$ ya da $2k - 1$ | $\{\dots, -3, -1, 1, 3, \dots\}$ |

Teklik ve çiftlik yalnızca **tam sayılar** için konuşulur. $2{,}5$ ya da $\frac{1}{2}$ ne tektir ne çift.

## Toplama ve çıkarma

**Örnek.** İki tek sayının toplamı neden çifttir?

Tek sayılar $2k + 1$ ve $2m + 1$ olsun. Toplamları $2k + 2m + 2 = 2(k + m + 1)$; yani 2'nin katı, çift. Daha görsel düşün: çift sayı, noktaların ikişerli eşleşebilmesidir. Tek sayıda bir nokta eşsiz kalır. İki tek sayı toplanınca eşsiz kalan iki nokta birbiriyle eşleşir.

![Noktalarla üç toplama: 6 artı 4'te bütün noktalar ikişerli eşleşiyor ve sonuç 10 çift; 5 artı 7'de iki grubun eşsiz kalan kırmızı noktaları birbiriyle eşleşiyor, sonuç 12 çift; 5 artı 4'te bir kırmızı nokta eşsiz kalıyor, sonuç 9 tek.](gorsel/tyt-matematik/01-03-eslesme.svg "Kırmızı noktalar eşsiz kalanlardır. İki tek sayıda iki eşsiz nokta birleşip bir çift oluşturur.")

| $+$ ya da $-$ | T | Ç |
|---|---|---|
| **T** | Ç | T |
| **Ç** | T | Ç |

**Kural.** Toplanan iki sayı **aynı türdense** (ikisi de tek ya da ikisi de çift) sonuç çift, **farklı türdense** sonuç tektir. Çıkarmada da tablo aynıdır: $9 - 4 = 5$ tek, $9 - 3 = 6$ çift.

**Çok terimli toplam.** $13 + 8 + 21 + 5 + 10$ tek mi çift mi? Çiftler sonucu değiştirmez; yalnızca tekleri say: $13, 21, 5$, yani **3 tek** sayı. İki tanesi eşleşir, biri kalır: toplam tektir (gerçekten $57$). Kural: bir toplamda **tek terimlerin sayısı tekse** sonuç tek, çiftse sonuç çifttir.

## Çarpma

**Örnek.** $7 \cdot 9 \cdot 11$ ve $7 \cdot 9 \cdot 12$ çarpımları tek mi çift mi?

İlkinde bütün çarpanlar tek: $693$, tek. İkincisinde bir çarpan ($12$) çift. $12 = 2 \cdot 6$ olduğundan çarpımın içinde bir $2$ çarpanı vardır: $7 \cdot 9 \cdot 12 = 2 \cdot (7 \cdot 9 \cdot 6) = 756$, çift.

| $\cdot$ | T | Ç |
|---|---|---|
| **T** | T | Ç |
| **Ç** | Ç | Ç |

**Kural.** Çarpım **yalnızca bütün çarpanlar tek ise** tektir. Tek bir çift çarpan bile çarpımı çift yapar.

Bundan çıkan iki önemli sonuç:

- $a \cdot b$ tek ise $a$ da $b$ de tektir (kesin bilgi).
- $a \cdot b$ çift ise yalnızca "**en az biri** çift" diyebilirsin. Hangisinin çift olduğu bilinmez: $2 \cdot 3$, $3 \cdot 2$ ve $2 \cdot 4$ hepsi çifttir.

**Katsayının etkisi.** $4b$, $6b$, $10b$ gibi çift katsayılı terimler $b$ ne olursa olsun **her zaman çifttir**. $3a$, $7a$ gibi tek katsayılı terimler ise $a$ ile aynı türdedir.

## Kuvvetler

**Örnek.** $3^4$ ve $6^3$ tek mi çift mi?

$3^4 = 3 \cdot 3 \cdot 3 \cdot 3$: hep tek çarpanlar, sonuç tek ($81$). $6^3 = 6 \cdot 6 \cdot 6$: çift çarpan var, sonuç çift ($216$).

**Kural.** $n$ pozitif tam sayı olmak üzere

$$\text{T}^n = \text{T} \qquad \text{Ç}^n = \text{Ç}$$

Yani bir sayının pozitif kuvveti, sayının kendisiyle aynı türdedir. Bu yüzden $a^2$, $a^3$, $a^{10}$ hepsi $a$ gibi davranır.

İki önemli uyarı:

- **Sıfırıncı kuvvet hep 1'dir, yani tektir:** $8^0 = 1$. "Çift sayının kuvveti çifttir" kuralı yalnızca **pozitif** üs için geçerlidir.
- **Ardışık iki tam sayının çarpımı hep çifttir:** $n^2 + n = n(n + 1)$ ve $n$ ile $n + 1$'den biri mutlaka çifttir. Benzer şekilde $n^2 - n = (n - 1)n$ de hep çifttir.

## "Kesinlikle doğru" soruları

**Örnek.** $a$ ve $b$ tam sayılar ve $7a + 4b + 2$ çift sayı olduğuna göre $a$ ve $b$ için ne söylenebilir?

1. $4b$ ve $2$ çift katsayılı; hangi $a$, $b$ için olursa olsun çifttir. Onları sil.
2. Geriye $7a$ kalır. Çift + çift + $7a$ = çift olması için $7a$ çift olmalı.
3. $7$ tek olduğu için $7a$ ile $a$ aynı türdedir: **$a$ çifttir.**
4. $b$ hakkında hiçbir bilgi yoktur: $a = 0$, $b = 1$ de $a = 0$, $b = 2$ de koşulu sağlar.

![Yukarıdan aşağı dört adım: çift katsayılı terimleri sil, kalanların tek ya da çift olduğunu yaz, bilinmeyenin durumunu çıkar, emin değilsen sayı ver.](gorsel/tyt-matematik/01-03-yontem.svg "Bu dört adım tek ve çift sorularının çoğunu çözer. Son adımda koşulu sağlayan küçük sayılar (0, 1, 2) seçip seçenekleri dene.")

**Kural.** Çift katsayılı terimler sonucu değiştirmez. Kalan terimlerden bilinmeyenin türünü çıkar. Bir seçeneğin "kesinlikle" doğru olmadığını göstermek için koşulu sağlayan **tek bir karşı örnek** yeter.

## ÖSYM tuzakları

> **0'ı unutmak:** $0 = 2 \cdot 0$ olduğundan $0$ çift sayıdır. Negatif sayılar da tek ya da çifttir: $-8$ çift, $-5$ tek.

> **Sıfırıncı kuvvet:** $4^0 = 1$ tektir. $\text{Ç}^n = \text{Ç}$ kuralı $n = 0$ için geçerli değildir.

> **"Çarpım çift" bilgisinden fazlasını çıkarmak:** $a \cdot b$ çift ise "$a$ çifttir" diyemezsin; yalnızca "en az biri çift" bilinir. Ama $a \cdot b$ tek ise ikisi de kesin tektir.

> **Bölmeyi tabloya katmak:** Bölmenin tablosu yoktur. $12 : 4 = 3$ (çift : çift = tek), $8 : 4 = 2$ (çift : çift = çift), $10 : 4$ ise tam sayı bile değildir.

> **Katsayıya bakmamak:** $5x + 2y$ tek ise $y$ hakkında bilgi yoktur; $2y$ her zaman çifttir. Bilgi yalnızca tek katsayılı terimden ($x$ tektir) gelir.

## Kendini dene

### Soru 1
Aşağıdaki işlemlerden hangisinin sonucu tek sayıdır?

A) $13 + 27$
B) $9 \cdot 14$
C) $5^3 \cdot 3$
D) $11^2 - 1$
E) $8^5 - 2$

**Cevap:** C
**Çözüm:** $5^3$ tek (tek sayının kuvveti), $3$ tek; tek $\cdot$ tek = tek. Ötekiler: A tek + tek = çift ($40$); B'de çift çarpan ($14$) var; D tek − tek = çift ($120$); E çift − çift = çift.

### Soru 2
$a$ ve $b$ tam sayılar ve $a \cdot b$ tek sayı olduğuna göre aşağıdakilerden hangisi **çift** sayıdır?

A) $a + b$
B) $a \cdot b + 2$
C) $a^2$
D) $a + 2b$
E) $b^3$

**Cevap:** A
**Çözüm:** Çarpım tek ise iki çarpan da tektir: $a$ ve $b$ tek. Tek + tek = çift, yani $a + b$ çift. B tek + çift = tek; C ve E tek sayının kuvveti, tek; D'de $2b$ çift, tek + çift = tek.

### Soru 3
$a$ tek, $b$ çift pozitif tam sayılar olduğuna göre aşağıdakilerden hangisi **tek** sayıdır?

A) $a^2 \cdot b$
B) $(a + b)^2 + 1$
C) $a^3 - a$
D) $b^a + a + 1$
E) $a^b + b^a$

**Cevap:** E
**Çözüm:** $a^b$ tek (tek sayının kuvveti), $b^a$ çift ($a$ pozitif, çift sayının pozitif kuvveti). Tek + çift = tek. A'da çift çarpan $b$ var; B'de $a + b$ tek, karesi tek, $+1$ ile çift; C tek − tek = çift; D çift + tek + tek = çift.

## Özet kartı

- Çift: $2k$; tek: $2k + 1$ ($k$ tam sayı). $0$ çifttir; negatifler de tek ya da çifttir.
- Toplama ve çıkarmada aynı türler çift, farklı türler tek verir; çok terimlide tek terimleri say.
- Çarpım yalnızca bütün çarpanlar tekse tektir; bir çift çarpan yeter.
- $n$ pozitifse $\text{T}^n = \text{T}$, $\text{Ç}^n = \text{Ç}$; ama $a^0 = 1$ tektir.
- $n(n + 1) = n^2 + n$ her zaman çifttir.
- Çift katsayılı terimleri sil, kalandan bilinmeyenin türünü çıkar; şüphede küçük sayılarla dene.

## Sonraki adım

Alıştırmaya geç (aşağıdaki düğme). Sonraki ders **Pozitif ve Negatif Sayılar**; orada "tek mi çift mi" yerine "pozitif mi negatif mi" sorusunu aynı mantıkla, sayıları bilmeden cevaplayacaksın.
