---
baslik: Üç Terimli İfadelerin Çarpanlarına Ayrılması
ders: tyt-matematik
sure: 20 dk
kaynak: MEBİ Konu Özeti b7d774edeb
guncelleme: 2026-11-18
---
# Üç Terimli İfadelerin Çarpanlarına Ayrılması

**Bu dersin sonunda:** $ax^2 + bx + c$ biçimindeki bir ifadeyi, baş katsayı 1 olsun ya da olmasın, iki birinci dereceden çarpana ayırabilecek ve $x^4 - 5x^2 + 4$ gibi ifadelerde değişken değiştirmeyi kullanabileceksin.

> **TYT'de yeri:** Üç terimli ifade TYT'de tek başına nadiren sorulur; ama rasyonel ifade sadeleştirme, "çarpanlarından biri hangisidir?", ikinci dereceden denklem ve "ifade asal sayı ise $n$ kaçtır?" sorularının hepsinde ilk adım budur. Hızlı ve hatasız ayırabilmek süre kazandırır.

## Önce hatırla

<details><summary>Geçen dersten: $x^3 - 27$ ifadesini çarpanlarına ayır.</summary>
$27 = 3^3$, iki küp farkı: $a^3 - b^3 = (a - b)(a^2 + ab + b^2)$. Sonuç $(x - 3)(x^2 + 3x + 9)$. İkinci çarpan $x^2 + 3x + 9$ bir üç terimlidir ama gerçek sayılarda ayrılmaz: çarpımı $9$, toplamı $3$ olan iki gerçek sayı yok. Bu derste hangi üç terimlilerin ayrıldığını göreceksin.
</details>

<details><summary>Geçen dersten: $8x^3 + 1$ ifadesini çarpanlarına ayır.</summary>
$8x^3 = (2x)^3$, $1 = 1^3$. İki küp toplamı: $(2x + 1)(4x^2 - 2x + 1)$. İkinci çarpandaki orta terimin işareti eksidir; ilk çarpandaki işaretin tersi.
</details>

## Çarpma işlemini tersten okumak

**Örnek.** $(x + 2)(x + 3)$ çarpımını yap:

$$(x + 2)(x + 3) = x^2 + 3x + 2x + 6 = x^2 + 5x + 6$$

Sabit terim $6 = 2 \cdot 3$, orta terimin katsayısı $5 = 2 + 3$. Çarpanlara ayırmak bu işlemi tersten yapmaktır: $x^2 + 5x + 6$ verilince **çarpımı 6, toplamı 5** olan iki sayıyı ararsın.

![Kenarları x artı 3 ve x artı 2 olan dikdörtgen dört parçaya bölünmüş: x kare, 3x, 2x ve 6.](gorsel/tyt-matematik/14-04-alan-modeli.svg "Dikdörtgenin alanı x² + 5x + 6. İki yeşil şerit orta terimi (2x + 3x = 5x), sarı kare sabit terimi (2 · 3 = 6) verir.")

## 1. Baş katsayı 1: $x^2 + bx + c$

**Örnek.** $x^2 + 7x + 12$ ifadesini çarpanlarına ayır.

1. Çarpımı $12$ olan pozitif tam sayı çiftleri: $1 \cdot 12$, $2 \cdot 6$, $3 \cdot 4$.
2. Toplamı $7$ olan çift: $3 + 4 = 7$.
3. Sonuç: $x^2 + 7x + 12 = (x + 3)(x + 4)$.

**Örnek.** $x^2 - 2x - 15$ ifadesini çarpanlarına ayır.

1. Çarpım $-15$ negatif: sayılardan biri pozitif, biri negatif.
2. Toplam $-2$: büyük olan (mutlak değerce) negatif olmalı. $-5 + 3 = -2$.
3. Sonuç: $x^2 - 2x - 15 = (x - 5)(x + 3)$.

**Kural.** $m \cdot n = c$ ve $m + n = b$ ise

$$x^2 + bx + c = (x + m)(x + n)$$

İşaretleri $c$ ve $b$ belirler:

| $c$ | $b$ | $m$ ve $n$ | Örnek |
|---|---|---|---|
| $+$ | $+$ | ikisi de $+$ | $x^2 + 7x + 12 = (x + 3)(x + 4)$ |
| $+$ | $-$ | ikisi de $-$ | $x^2 - 9x + 20 = (x - 4)(x - 5)$ |
| $-$ | $+$ | büyüğü $+$ | $x^2 + 2x - 15 = (x + 5)(x - 3)$ |
| $-$ | $-$ | büyüğü $-$ | $x^2 - 2x - 15 = (x - 5)(x + 3)$ |

> **Tuzak:** $x^2 - x - 12$ için $-3 \cdot 4 = -12$ çarpımı doğru, ama toplam $-3 + 4 = +1$ olur. Doğrusu $-4$ ve $3$: $(x - 4)(x + 3)$. Çarpımı bulunca toplamın **işaretini** de kontrol et.

## 2. Baş katsayı 1 değil: çapraz çarpım

**Örnek.** $3x^2 + 10x - 8$ ifadesini çarpanlarına ayır.

1. Baş terimi ayır: $3x^2 = 3x \cdot x$. Sol sütuna $3x$ ve $x$ yaz.
2. Sabit terimi ayır: $-8$ için bir çift dene, örneğin $-2$ ve $+4$. Sağ sütuna yaz.
3. Çaprazları çarp ve topla: $3x \cdot 4 + x \cdot (-2) = 12x - 2x = 10x$. Orta terim tuttu.
4. Satırları **yan yana** oku: $(3x - 2)(x + 4)$.

![Çapraz çarpım şeması: solda alt alta 3x ve x, sağda eksi 2 ve artı 4. Çapraz çizgiler 3x çarpı 4 eşittir 12x ve x çarpı eksi 2 eşittir eksi 2x sonuçlarını veriyor; toplam 10x.](gorsel/tyt-matematik/14-04-capraz.svg "Çarpanlar satırlardan okunur (3x − 2 ve x + 4); çaprazlar yalnızca orta terimi kontrol etmek içindir.")

Deneme tutmazsa çifti ya da sırayı değiştir. $-8$ için $(+2, -4)$ denersen $3x \cdot (-4) + x \cdot 2 = -10x$ çıkar: işaret ters. O zaman işaretleri değiştirmek yeter.

**Kural.** $ax^2 = px \cdot tx$ ve $c = m \cdot n$ olsun. Çaprazlar toplamı $pn + tm = b$ ise

$$ax^2 + bx + c = (px + m)(tx + n)$$

**İkinci yol (gruplandırma).** $a \cdot c$ çarpımına bak: $3 \cdot (-8) = -24$. Çarpımı $-24$, toplamı $10$ olan sayılar $12$ ve $-2$. Orta terimi böl:

$$3x^2 + 12x - 2x - 8 = 3x(x + 4) - 2(x + 4) = (3x - 2)(x + 4)$$

Deneme sayısı çok olan ifadelerde bu yol daha düzenlidir.

**Kontrol.** Çarpanlara ayırdıktan sonra iki tarafa $x = 1$ koy. $3 + 10 - 8 = 5$ ve $(3 - 2)(1 + 4) = 5$. Eşitse büyük ihtimalle doğrudur; eşit değilse kesin yanlıştır.

> **Tuzak:** $6x^2 - 11x + 4$ için $(6x - 1)(x - 4)$ denersen çaprazlar $-24x - x = -25x$ olur. Baş katsayının yalnızca $6x \cdot x$ ayrılışını değil, $2x \cdot 3x$ ayrılışını da dene: $(2x - 1)(3x - 4)$ çaprazları $-8x - 3x = -11x$ verir.

## 3. İki değişkenli üç terimli

**Örnek.** $x^2 - 5xy + 6y^2$ ifadesini çarpanlarına ayır.

$y$'yi katsayının parçası gibi düşün: çarpımı $6y^2$, toplamı $-5y$ olan terimler $-2y$ ve $-3y$.

$$x^2 - 5xy + 6y^2 = (x - 2y)(x - 3y)$$

Bu biçim "$x^2 - 5xy + 6y^2 = 0$ ise $\dfrac{x}{y}$ kaçtır?" sorularında çıkar: çarpanlardan biri sıfırdır, $x = 2y$ ya da $x = 3y$.

## 4. Değişken değiştirme

**Örnek.** $x^4 - 5x^2 + 4$ ifadesini çarpanlarına ayır.

1. $x^4 = (x^2)^2$. $t = x^2$ de: ifade $t^2 - 5t + 4$ olur.
2. $t^2 - 5t + 4 = (t - 1)(t - 4)$.
3. $t$ yerine $x^2$ yaz: $(x^2 - 1)(x^2 - 4)$.
4. İkisi de iki kare farkı: $(x - 1)(x + 1)(x - 2)(x + 2)$.

**Örnek.** $(x + 1)^2 - 3(x + 1) - 10$ ifadesini çarpanlarına ayır.

$t = x + 1$ dersen $t^2 - 3t - 10 = (t - 5)(t + 2)$. Geri yerine koy: $(x + 1 - 5)(x + 1 + 2) = (x - 4)(x + 3)$.

**Kural.** Bir ifadede aynı parça hem karesiyle hem kendisiyle geçiyorsa ona tek harf ver, ayır, sonra harfi geri değiştir.

> **Tuzak:** $(t - 5)(t + 2)$ yazıp durmak ya da $t$ yerine $x$ yazmak. Soru $x$ cinsinden cevap ister: $t = x + 1$'i mutlaka geri koy.

## Önce ortak çarpan, sonra işaret

**Örnek.** $2x^2 - 2x - 24 = 2(x^2 - x - 12) = 2(x - 4)(x + 3)$.

**Örnek.** $-x^2 + x + 6$ ifadesinde baş katsayı negatif. $-1$'i paranteze al: $-(x^2 - x - 6) = -(x - 3)(x + 2)$. Eksiyi ilk çarpana dağıtırsan $(3 - x)(x + 2)$ da aynı sonuçtur.

![Yöntem akışı: önce ortak çarpanı al; tekrar eden ifade varsa ona t de; baş katsayı 1 ise çarpımı c, toplamı b olan sayıları bul, değilse çapraz çarpımı dene; en sonda x eşittir 1 koyup kontrol et.](gorsel/tyt-matematik/14-04-yontem.svg "Her üç terimlide aynı sıra. En çok atlanan adım ilk kutu: ortak çarpan.")

## ÖSYM tuzakları

> **İşaret karışıklığı:** $x^2 - x - 12 \ne (x + 4)(x - 3)$; bu çarpım $x^2 + x - 12$ verir. Toplamın işareti büyük sayının işaretidir.

> **Satır yerine çapraz okumak:** Çapraz çarpım şemasında çarpanlar **satırlardan** okunur. $3x$ ile $+4$'ü aynı paranteze yazarsan $(3x + 4)(x - 2) = 3x^2 - 2x - 8$ bulursun.

> **Ortak çarpanı unutmak:** $2x^2 + 10x + 12$ için $(x + 2)(x + 3)$ yazmak yanlıştır; önde $2$ kalır: $2(x + 2)(x + 3)$.

> **İşi yarıda bırakmak:** $x^4 - 5x^2 + 4 = (x^2 - 1)(x^2 - 4)$ yazıp durma; iki parantez de yine ayrılır.

> **Her üç terimli ayrılmaz:** $x^2 + 3x + 9$ gibi ifadelerde uygun tam sayı çifti yoktur. Seçeneklerde böyle bir ifade çarpan olarak görünürse, uydurma çarpan arama.

## Kendini dene

### Soru 1
$x^2 - 4x - 21$ ifadesinin çarpanlarına ayrılmış biçimi aşağıdakilerden hangisidir?

A) $(x - 3)(x + 7)$
B) $(x - 7)(x + 3)$
C) $(x - 7)(x - 3)$
D) $(x + 7)(x + 3)$
E) $(x - 21)(x + 1)$

**Cevap:** B
**Çözüm:** Çarpımı $-21$, toplamı $-4$ olan sayılar $-7$ ve $3$. Sonuç $(x - 7)(x + 3)$. A seçeneği $x^2 + 4x - 21$ verir: işaretler ters. C ve D'de çarpım $+21$ olur.

### Soru 2
$3x^2 - 5x - 2$ ifadesinin çarpanlarından biri aşağıdakilerden hangisidir?

A) $x + 2$
B) $3x - 1$
C) $3x + 2$
D) $x - 1$
E) $3x + 1$

**Cevap:** E
**Çözüm:** $3x^2 = 3x \cdot x$, $-2 = 1 \cdot (-2)$. Satırlar $3x, +1$ ve $x, -2$: çaprazlar $3x \cdot (-2) + x \cdot 1 = -6x + x = -5x$. Tuttu. Sonuç $(3x + 1)(x - 2)$. B seçeneği işaretleri ters koymaktan gelir: $(3x - 1)(x + 2) = 3x^2 + 5x - 2$.

### Soru 3
Aşağıdakilerden hangisi $x^4 - 13x^2 + 36$ ifadesinin çarpanlarından biri **değildir**?

A) $x - 3$
B) $x - 2$
C) $x + 1$
D) $x + 2$
E) $x + 3$

**Cevap:** C
**Çözüm:** $t = x^2$ de: $t^2 - 13t + 36 = (t - 4)(t - 9)$. Geri koy: $(x^2 - 4)(x^2 - 9) = (x - 2)(x + 2)(x - 3)(x + 3)$. $x + 1$ bu çarpanlar arasında yoktur. Kontrol: $x = -1$ koyunca $1 - 13 + 36 = 24 \ne 0$.

## Özet kartı

- $x^2 + bx + c$: çarpımı $c$, toplamı $b$ olan $m$, $n$ bul; $(x + m)(x + n)$.
- $c > 0$ ise iki sayı aynı işaretli; $c < 0$ ise mutlak değerce büyüğün işareti $b$'nin işareti.
- $ax^2 + bx + c$: çapraz çarpım; çaprazların toplamı $bx$ olmalı, çarpanlar satırlardan okunur.
- İkinci yol: $a \cdot c$ çarpımıyla orta terimi böl, gruplandır.
- Tekrar eden parça varsa $t$ de, ayır, geri koy.
- Önce ortak çarpan; sonunda $x = 1$ koyup kontrol et.

## Sonraki adım

Alıştırmaya geç (aşağıdaki düğme). Sonraki ders **Rasyonel İfadelerin Sadeleştirilmesi**; bu konudaki bütün kalıpları birlikte kullanacaksın, pay ve paydayı ayırmak bu dersteki adımlarla başlar.
