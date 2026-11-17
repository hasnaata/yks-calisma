---
baslik: İkinci Dereceden Bir Bilinmeyenli Denklemler
ders: tyt-matematik
sure: 20 dk
kaynak: MEBİ Konu Özeti 33f3fe2a0a
guncelleme: 2026-11-17
---
# İkinci Dereceden Bir Bilinmeyenli Denklemler

**Bu dersin sonunda:** bir denklemin ikinci dereceden olup olmadığını düzenleyerek anlayabilecek, katsayılarını okuyabilecek, verilen bir sayının kök olup olmadığını deneyebilecek ve bir kökü verilen denklemde bilinmeyen katsayıyı bulabileceksin.

> **TYT'de yeri:** Bu ders konunun alfabesidir. Doğrudan "hangisi ikinci dereceden denklemdir?", "denklem ikinci dereceden ise $m$ kaçtır?" ve "bir kökü 2 ise $k$ kaçtır?" kalıpları gelir. Problemlerde kurduğun denklem çoğu zaman ikinci derecedendir; çözmeden önce onu $ax^2 + bx + c = 0$ biçimine getirmen gerekir.

## Önce hatırla

<details><summary>Geçen dersten: $\dfrac{x^2 - 9}{x^2 + x - 6}$ ifadesini sadeleştir.</summary>
Pay iki kare farkı: $x^2 - 9 = (x - 3)(x + 3)$. Payda üç terimli: çarpımı $-6$, toplamı $1$ olan sayılar $3$ ve $-2$, yani $(x + 3)(x - 2)$. Ortak çarpan $x + 3$ sadeleşir: $\dfrac{x - 3}{x - 2}$. Payda, $x = 2$ ve $x = -3$ için sıfır olduğundan bu değerlerde ifade tanımsızdır.
</details>

<details><summary>Geçen dersten: $\dfrac{x + 1}{x - 2} - \dfrac{3}{x - 2}$ işleminin sonucu nedir?</summary>
Paydalar zaten eşit, payları çıkar: $\dfrac{x + 1 - 3}{x - 2} = \dfrac{x - 2}{x - 2} = 1$ (burada $x \ne 2$). Bu derste kullanacağın fikir aynı: önce her şeyi tek tarafa topla, sonra sadeleştir.
</details>

## Tanım: hangi denklem ikinci derecedendir?

**Örnek.** Aşağıdakilerden hangileri ikinci dereceden bir bilinmeyenli denklemdir?

| Denklem | Düzenlenmiş hâli | Sonuç |
|---|---|---|
| $x^2 - 7 = 0$ | $x^2 - 7 = 0$ | İkinci dereceden ($x$'li terim yok, sorun değil) |
| $x(x + 5) = 2$ | $x^2 + 5x - 2 = 0$ | İkinci dereceden |
| $(x - 1)^2 = x^2 + 3$ | $x^2 - 2x + 1 - x^2 - 3 = 0$, yani $-2x - 2 = 0$ | $x^2$'ler sadeleşti: **birinci** dereceden |
| $x^3 - x^2 = x^3 + 2$ | $-x^2 - 2 = 0$ | $x^3$'ler sadeleşti: **ikinci** dereceden |
| $x^2 + \frac{4}{x} = 1$ | paydada $x$ var | Değil |
| $\sqrt{x} + x^2 = 6$ | kök içinde $x$ var | Değil |

**Kural.** $a, b, c$ gerçek sayılar ve $a \ne 0$ olmak üzere

$$ax^2 + bx + c = 0$$

biçimine getirilebilen denkleme **ikinci dereceden bir bilinmeyenli denklem** denir. Karar vermeden önce bütün terimleri bir tarafa topla ve sadeleştir. Paydada ya da kök içinde $x$ olan terim varsa bu denklem bu sınıfa girmez.

![Karar akışı: x paydada veya kökte ise ikinci dereceden değil. Değilse bütün terimleri sola topla, sadeleştir, en büyük üs 2 ise ikinci dereceden denklem, değilse değil.](gorsel/tyt-matematik/15-01-karar.svg "Görünüşe değil, düzenlenmiş hâle bak. Üç adım: tek tarafa topla, sadeleştir, en büyük üssü oku.")

Bu sınıftaki bir denklemin **en fazla iki kökü** vardır. Bunu aşağıda grafikte de göreceksin.

## Katsayıları okumak

**Örnek.** $3x - 5 = x^2$ denkleminin katsayılarını bul.

Bütün terimleri $x^2$'nin olduğu tarafa topla: $0 = x^2 - 3x + 5$. Terimleri üslere göre sırala ve her terimin **işaretiyle birlikte** katsayısını oku:

![x kare eksi 3x artı 5 eşittir 0 denkleminde x kare kutusunun altında a eşittir 1, eksi 3x kutusunun altında b eşittir eksi 3, artı 5 kutusunun altında c eşittir 5 yazıyor.](gorsel/tyt-matematik/15-01-katsayilar.svg "Katsayı, terimin önündeki işaretle birlikte okunur: b = 3 değil, b = −3.")

| Denklem | $a$ | $b$ | $c$ |
|---|---|---|---|
| $x^2 - 3x + 5 = 0$ | $1$ | $-3$ | $5$ |
| $x^2 = 9$, yani $x^2 - 9 = 0$ | $1$ | $0$ | $-9$ |
| $2x^2 + 7x = 0$ | $2$ | $7$ | $0$ |

**Kural.** Önce $ax^2 + bx + c = 0$ sırasına getir, sonra oku. Eksik terimin katsayısı $0$'dır. Denklemi $-1$ ile çarparsan ($-x^2 + 3x - 5 = 0$) aynı denklemi elde edersin ama katsayıların hepsinin işareti değişir. Bu yüzden sorular genellikle "$a = 1$ olacak biçimde" ya da "$a > 0$ olmak üzere" der; bu ifadeyi atlama.

## Denklem ikinci dereceden ise: parametre bulmak

**Örnek.** $(m + 2)x^3 + (m - 1)x^n + 5x - 4 = 0$ denklemi ikinci dereceden bir bilinmeyenli denklem olduğuna göre $m$ ve $n$ kaçtır?

1. $x^3$'lü terim kalırsa denklem üçüncü dereceden olur. Bu terim yok olmalı: $m + 2 = 0$, $m = -2$.
2. Kalan denklem $-3x^n + 5x - 4 = 0$. İçinde $x^2$ olması gerekir ve bu terim ancak $x^n$ olabilir: $n = 2$.
3. Kontrol: $-3x^2 + 5x - 4 = 0$. $a = -3 \ne 0$, denklem gerçekten ikinci dereceden.

**Kural.** Derecesi 2'den büyük terimlerin **katsayısı 0** olmalı; $x^2$'li terimin **katsayısı 0 olmamalı**. Üste parametre varsa o üs 2'ye eşitlenir.

Tersi de sorulur: $(k - 3)x^2 + 2x + 1 = 0$ denklemi $k \ne 3$ için ikinci derecedendir. $k = 3$ olursa $x^2$'li terim silinir, $2x + 1 = 0$ kalır; denklem birinci dereceden olur ve tek kökü $-\frac{1}{2}$'dir.

## Kök ve çözüm kümesi

**Örnek.** $3$ ve $-2$ sayıları $x^2 - 5x + 6 = 0$ denkleminin kökü müdür?

- $x = 3$: $9 - 15 + 6 = 0$. Eşitlik sağlandı, $3$ **köktür**.
- $x = -2$: $4 + 10 + 6 = 20 \ne 0$. $-2$ kök **değildir**.

Denklemi sağlayan $x$ sayılarına **kök**, köklerin oluşturduğu kümeye **çözüm kümesi** (Ç) denir.

**Örnek.** $x^2 + kx - 10 = 0$ denkleminin bir kökü $2$ olduğuna göre $k$ kaçtır? Diğer kök nedir?

1. Kök denklemi sağlar; $x$ yerine $2$ yaz: $4 + 2k - 10 = 0$, $2k = 6$, $k = 3$.
2. Denklem: $x^2 + 3x - 10 = 0$. Geçen konudaki gibi çarpanlara ayır: çarpımı $-10$, toplamı $3$ olan sayılar $5$ ve $-2$. $(x + 5)(x - 2) = 0$.
3. Çarpım sıfırsa çarpanlardan biri sıfırdır: $x = -5$ ya da $x = 2$. Ç $= \{-5, 2\}$.

![y eşittir x kare artı 3x eksi 10 parabolü, x eksenini eksi 5 ve 2 noktalarında kesiyor.](gorsel/tyt-matematik/15-01-kok-grafik.svg "Kökler, ifadenin değerinin 0 olduğu yerlerdir: grafikte x eksenini kestiği iki nokta.")

**Kural.** "$r$ bir köktür" cümlesi "$x = r$ yazınca eşitlik sağlanır" demektir. Bilinmeyen katsayı bu eşitlikten bulunur.

Bir ikinci dereceden denklemin gerçek sayılarda **iki**, **bir** ya da **hiç** kökü olabilir; üçüncü bir kök asla olmaz. Hangisinin olduğunu ilerideki diskriminant dersinde hesapla bulacaksın.

![Üç grafik yan yana: x kare eksi 4 eksen ile iki noktada kesişiyor, çözüm kümesi eksi 2 ve 2. x kare eksene tek noktada değiyor, çözüm kümesi 0. x kare artı 1 ekseni hiç kesmiyor, çözüm kümesi boş küme.](gorsel/tyt-matematik/15-01-kok-sayisi.svg "Grafik x eksenini en çok iki yerde keser; bu yüzden en çok iki kök vardır. x² + 1 hiçbir gerçek sayı için 0 olmaz.")

## ÖSYM tuzakları

> **Görünüşe göre karar vermek:** $(x - 1)^2 = x^2 + 3$ denkleminde $x^2$ görünüyor ama iki taraftaki $x^2$'ler sadeleşir; denklem birinci derecedendir. Tersine $x^3 - x^2 = x^3 + 2$ ikinci derecedendir. Önce düzenle, sonra karar ver.

> **İşaretsiz katsayı okumak:** $x^2 - 3x + 5 = 0$ için $b = 3$ değil $b = -3$'tür. Terimi diğer tarafa atarken işaretini değiştirmeyi de unutma.

> **$x^2$'nin katsayısını unutmak:** "$(m - 4)x^2 + \dots$ denklemi ikinci derecedendir" deniyorsa $m \ne 4$ koşulu sorunun parçasıdır. Bulduğun $m$ değeri $x^2$'yi siliyorsa o değer cevap olamaz.

> **İki tarafı $x$'e bölmek:** $x^2 = 4x$ denklemini $x$'e bölüp $x = 4$ bulan bir kök kaybeder; $x = 0$ da denklemi sağlar. Doğrusu: $x^2 - 4x = 0$, $x(x - 4) = 0$, Ç $= \{0, 4\}$.

> **$(-3)^2$ ile $-3^2$'yi karıştırmak:** Negatif kökü yerine koyarken parantez kullan: $(-3)^2 = 9$, ama $-3^2 = -9$.

## Kendini dene

### Soru 1
Aşağıdakilerden hangisi ikinci dereceden bir bilinmeyenli denklemdir?

A) $x^2 + \sqrt{x} = 4$
B) $(x + 3)^2 = x^2 - 1$
C) $x(x - 4) = 0$
D) $x^4 - x^2 = 0$
E) $2x - y^2 = 0$

**Cevap:** C
**Çözüm:** C'de çarpımı aç: $x^2 - 4x = 0$; $a = 1$, $b = -4$, $c = 0$. A'da kök içinde $x$ var. B'de $x^2$'ler sadeleşir: $6x + 10 = 0$, birinci derecedendir. D dördüncü derecedendir. E'de iki bilinmeyen var.

### Soru 2
$4x - 3 = x^2$ denklemi $ax^2 + bx + c = 0$ biçiminde $a = 1$ olacak şekilde yazılırsa $c$ kaçtır?

A) $-4$
B) $-3$
C) $1$
D) $3$
E) $4$

**Cevap:** D
**Çözüm:** Terimleri $x^2$'nin tarafına topla: $0 = x^2 - 4x + 3$. Buradan $a = 1$, $b = -4$, $c = 3$. $-3$ cevabı, $-3$'ü diğer tarafa atarken işaretini değiştirmemekten gelir; $-4$ ise $b$'dir.

### Soru 3
$x^2 - 2x + m = 0$ denkleminin bir kökü $-3$ olduğuna göre $m$ kaçtır?

A) $-15$
B) $-3$
C) $3$
D) $9$
E) $15$

**Cevap:** A
**Çözüm:** $x = -3$ yaz: $(-3)^2 - 2 \cdot (-3) + m = 0$, yani $9 + 6 + m = 0$, $m = -15$. $-2 \cdot (-3)$ çarpımını $-6$ alan $m = -3$, $(-3)^2$'yi $-9$ alan $m = 3$ bulur.

## Özet kartı

- $ax^2 + bx + c = 0$ ve $a \ne 0$: ikinci dereceden bir bilinmeyenli denklem.
- Karar vermeden önce tek tarafa topla ve sadeleştir; paydada ya da kök içinde $x$ olmamalı.
- Katsayılar işaretiyle okunur; eksik terimin katsayısı $0$'dır.
- Parametre sorusu: yüksek dereceli terimlerin katsayısı $0$, $x^2$'nin katsayısı $0$ değil.
- Kök denklemi sağlar: $x$ yerine kökü yaz, bilinmeyen katsayıyı bul.
- En fazla iki kök vardır; iki tarafı $x$'e bölüp kök kaybetme.

## Sonraki adım

Alıştırmaya geç (aşağıdaki düğme). Sonraki ders **İkinci Dereceden Bir Bilinmeyenli Denklemlerin Çözüm Kümesi**; burada çarpanlara ayırarak yaptığın çözümü sistemli hâle getirecek ve çarpanlara ayrılmayan denklemler için yeni yollar öğreneceksin.
