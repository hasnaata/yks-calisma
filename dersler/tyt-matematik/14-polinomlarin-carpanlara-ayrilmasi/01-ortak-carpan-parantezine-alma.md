---
baslik: Ortak Çarpan Parantezine Alma
ders: tyt-matematik
sure: 20 dk
kaynak: MEBİ Konu Özeti e421f9a3d1
guncelleme: 2026-11-18
---
# Ortak Çarpan Parantezine Alma

<div class="giris" dir="rtl" lang="ar">

**الدرس ده عن إيه؟** عن أول وأسهل طريقة في تحليل كثيرة الحدود (çarpanlara ayırma): إخراج العامل المشترك (ortak çarpan parantezine alma)، وبعدها التحليل بالتجميع (gruplandırma).

- هتعرف تطلّع العامل المشترك صح: القاسم المشترك الأكبر (EBOB) للمعاملات مع أصغر أُس للمتغير، ومن غير ما تضيّع ولا حد جوه القوس.
- هتتعلم تلعب بالإشارة لما القوسين يبقوا عكس بعض، وتجمّع الحدود اتنين اتنين لحد ما يطلع نفس القوس.
- هتشوف إزاي التحليل ده بيختصر حسابات كبيرة وأسئلة زي "مجموع العددين وحاصل ضربهم معلومين".

**ليه مهم؟** في TYT بييجي سؤال "أنهي واحد من دول عامل من عوامل كثيرة الحدود؟" وأسئلة الأُسس والكسور الكبيرة، وكل طرق التحليل اللي جاية بتبدأ بالخطوة دي.

هو ٢٠ دقيقة بس، وبعده التحليل هيبقى أسهل عليك بكتير. يلا بينا!

</div>

**Bu dersin sonunda:** bir polinomu ortak çarpan parantezine alarak ve gruplandırarak çarpanlarına ayırabilecek, bunu sayısal işlemleri ve "$a + b$, $ab$ verilmiş" sorularını kısaltmak için kullanabileceksin.

> **TYT'de yeri:** "Aşağıdakilerden hangisi bu polinomun bir çarpanıdır?", "$a - b = 4$ ve $ab = 5$ ise ... kaçtır?", üslü ya da büyük sayılarla verilen kesirli işlemler ve tanımlanan işlem soruları bu dersin kalıplarıdır. Sonraki bütün çarpanlara ayırma yöntemleri de ilk adımda ortak çarpanı arar.

## Önce hatırla

<details><summary>Kalan bulmadan: P(x) = x³ − 2x² + x + 5 polinomunun x − 2 ile bölümünden kalan kaçtır?</summary>
$x - 2$ ile bölümden kalan $P(2)$'dir: $P(2) = 8 - 8 + 2 + 5 = $ <b>7</b>. Bölme yapmaya gerek yok.
</details>

<details><summary>Kalan bulmadan: x − 2, P(x) = x³ + ax − 6 polinomunun bir çarpanı ise a kaçtır?</summary>
$x - 2$ çarpan ise kalan $0$, yani $P(2) = 0$: $8 + 2a - 6 = 0$, <b>$a = -1$</b>. O zaman $P(x) = x^3 - x - 6 = (x - 2)(x^2 + 2x + 3)$. Bu derste polinomu böyle çarpımlara ayırmanın en temel yolunu öğreneceksin.
</details>

## Ortak çarpan nedir?

**Örnek.** $4x^2 + 6x$ ifadesini çarpım biçiminde yaz.

- Katsayılar $4$ ve $6$: ikisini de bölen en büyük sayı $\text{EBOB}(4, 6) = 2$.
- Harfler $x^2$ ve $x$: ikisinde de en az $x^1$ var.
- Ortak çarpan $2x$. Her terimi $2x$'e böl: $\dfrac{4x^2}{2x} = 2x$, $\dfrac{6x}{2x} = 3$.

$$4x^2 + 6x = 2x(2x + 3)$$

Kontrol: $2x(2x + 3) = 4x^2 + 6x$. Doğru.

![Bir dikdörtgen iki parçaya ayrılmış: yüksekliği 2x. Soldaki mavi parçanın genişliği 2x, alanı 4x kare; sağdaki yeşil parçanın genişliği 3, alanı 6x. Üstte toplam genişlik 2x artı 3.](gorsel/tyt-matematik/14-01-alan-modeli.svg "İki parçanın ortak kenarı 2x, ortak çarpandır. Alanların toplamı yükseklik çarpı toplam genişlik olarak da yazılabilir.")

Bu, dağılma özelliğinin tersidir: $k \cdot a + k \cdot b = k(a + b)$. Çarpımı açmak yerine toplamı çarpıma çeviriyoruz.

**Kural.** Ortak çarpan = katsayıların EBOB'u $\times$ her terimde bulunan harflerin **en küçük** kuvveti. Paranteze, her terimin ortak çarpana bölümü yazılır.

## Kuvvetlerde en küçük üs

**Örnek.** $12x^5 - 8x^3 + 4x^2$ ifadesini çarpanlarına ayır.

- $\text{EBOB}(12, 8, 4) = 4$.
- $x^5$, $x^3$, $x^2$ içinde en küçük kuvvet $x^2$.
- Ortak çarpan $4x^2$: $\dfrac{12x^5}{4x^2} = 3x^3$, $\dfrac{-8x^3}{4x^2} = -2x$, $\dfrac{4x^2}{4x^2} = 1$.

$$12x^5 - 8x^3 + 4x^2 = 4x^2(3x^3 - 2x + 1)$$

Dışarıda üç terim vardı, parantezin içinde de üç terim olmalı. Son terim tamamen dışarı çıktığı için yerinde $1$ kalır, $0$ değil.

**Kural.** Ortak çarpanı aldıktan sonra terim sayısını say: parantezin içindeki terim sayısı, başlangıçtaki terim sayısına eşittir.

## Ortak çarpan bir ifade olabilir

**Örnek.** $3(x - 2)^2 + 5(x - 2)$ ifadesini çarpanlarına ayır.

$(x - 2)$'yi tek bir harf gibi düşün, $t = x - 2$ de: $3t^2 + 5t = t(3t + 5)$. Geri yaz:

$$3(x - 2)^2 + 5(x - 2) = (x - 2)\big(3(x - 2) + 5\big) = (x - 2)(3x - 1)$$

Parantezin içini mutlaka sadeleştir: $3x - 6 + 5 = 3x - 1$.

**Kural.** $a \cdot (\text{ifade}) + b \cdot (\text{ifade}) = (\text{ifade})(a + b)$. Ortak ifadenin kuvvetleri farklıysa yine en küçük kuvvet dışarı alınır.

## İşaret çevirme

**Örnek.** $x(a - 3) + y(3 - a)$ ifadesini çarpanlarına ayır.

$a - 3$ ile $3 - a$ aynı değil, birbirinin **ters işaretlisi**: $3 - a = -(a - 3)$. Buna göre

$$x(a - 3) + y(3 - a) = x(a - 3) - y(a - 3) = (a - 3)(x - y)$$

Kuvvet varsa işaret, üssün tek ya da çift olmasına bağlıdır:

| İfade | Eşiti | Neden |
|---|---|---|
| $(3 - x)^2$ | $(x - 3)^2$ | Çift kuvvet: eksi işareti kaybolur |
| $(3 - x)^3$ | $-(x - 3)^3$ | Tek kuvvet: eksi işareti dışarı çıkar |

**Örnek.** $5(3 - x)^2 + 2(x - 3)$ ifadesini çarpanlarına ayır.

$(3 - x)^2 = (x - 3)^2$ olduğundan

$$5(x - 3)^2 + 2(x - 3) = (x - 3)\big(5(x - 3) + 2\big) = (x - 3)(5x - 13)$$

**Kural.** $b - a = -(a - b)$; $(b - a)^n$ ifadesi $n$ çiftse $(a - b)^n$, $n$ tekse $-(a - b)^n$ olur.

## Gruplandırma

Her terimde ortak bir çarpan yoksa terimleri ikişerli gruplara ayırırız.

**Örnek.** $xy + 2x + 3y + 6$ ifadesini çarpanlarına ayır.

Dört terimin hepsinde ortak çarpan yok. İlk iki terimde $x$, son iki terimde $3$ ortak:

$$xy + 2x + 3y + 6 = x(y + 2) + 3(y + 2) = (y + 2)(x + 3)$$

![Dört parçalı dikdörtgen: üst kenar x ve 3, sol kenar y ve 2. Parçaların alanları xy, 3y, 2x ve 6. Soldaki mavi sütun x çarpı y artı 2, sağdaki yeşil sütun 3 çarpı y artı 2.](gorsel/tyt-matematik/14-01-gruplama-alan.svg "Her sütunun yüksekliği aynı: y + 2. Bu yüzden iki grup aynı parantezi verir ve bütün dikdörtgen (x + 3)(y + 2) olur.")

**Örnek (eksi işaretli grup).** $x^3 + 4x^2 - x - 4$ ifadesini çarpanlarına ayır.

$$x^2(x + 4) - x - 4 = x^2(x + 4) - (x + 4) = (x + 4)(x^2 - 1)$$

İkinci gruptan $-1$ alınca içerideki işaretler değişir: $-x - 4 = -(x + 4)$. ($x^2 - 1$ de çarpanlarına ayrılır; bunu bir sonraki derste göreceksin.)

**Örnek (orta terimi bölmek).** $x^2 + 5x + 6$ ifadesinde $5x$ terimini $2x + 3x$ diye yaz:

$$x^2 + 2x + 3x + 6 = x(x + 2) + 3(x + 2) = (x + 2)(x + 3)$$

Burada $2 + 3 = 5$ ve $2 \cdot 3 = 6$ olduğu için parçalama işe yarar.

![Akış şeması: her terimde ortak çarpan varsa EBOB ile paranteze al. Yoksa terimleri ikişerli grupla, her gruptan ortak çarpanı al; parantezler aynıysa ortak parantezi dışarı al, değilse işaret çevir ya da yeniden grupla ve tekrar dene.](gorsel/tyt-matematik/14-01-yontem.svg "Gruplar aynı parantezi vermiyorsa yöntem yanlış değildir: işareti çevir ya da terimleri başka biçimde eşleştir.")

**Kural.** Gruplandırmada amaç, her gruptan **aynı parantezi** elde etmektir. Aynı çıkmazsa önce işaret çevirmeyi, sonra terimleri farklı eşleştirmeyi dene.

## Sayılarla kısa yol

Ortak çarpan almak, hesap makinesi gerektiren işlemleri kısaltır.

**Örnek 1.** $37 \cdot 64 + 37 \cdot 36 = 37(64 + 36) = 37 \cdot 100 = 3700$.

**Örnek 2.** $\dfrac{5^6 + 5^4}{5^5 + 5^3}$ kaçtır?

Pay: $5^4(5^2 + 1) = 5^4 \cdot 26$. Payda: $5^3(5^2 + 1) = 5^3 \cdot 26$. Sonuç $\dfrac{5^4}{5^3} = 5$.

**Örnek 3.** $a + b = 7$ ve $ab = 3$ ise $a^2b + ab^2$ kaçtır?

$a$ ve $b$'yi bulmaya çalışma: $a^2b + ab^2 = ab(a + b) = 3 \cdot 7 = 21$.

**Örnek 4.** $x$ ve $y$ pozitif tam sayılar ve $xy + x + y = 5$ ise $x + y$ kaçtır?

İki tarafa $1$ ekle, gruplandır: $xy + x + y + 1 = 6$, yani $x(y + 1) + (y + 1) = (x + 1)(y + 1) = 6$. Çarpanlar en az $2$ olduğu için $2 \cdot 3$ ya da $3 \cdot 2$: $(x, y) = (1, 2)$ veya $(2, 1)$. İkisinde de $x + y = 3$.

**Kural.** Verilen ifadeyi çarpanlarına ayır, sonra elindeki toplam ya da çarpımı yerine yaz. Tam sayı çözümü istenirse eksik sabiti ekleyerek ifadeyi iki çarpanın çarpımına çevir.

## ÖSYM tuzakları

> **Terim kaybetmek:** $12x^5 - 8x^3 + 4x^2 = 4x^2(3x^3 - 2x)$ yazmak yanlıştır. Tamamen dışarı çıkan terimin yerine $1$ kalır: $4x^2(3x^3 - 2x + 1)$.

> **En büyük kuvveti dışarı almak:** $x^5 + x^3$ ifadesinde ortak çarpan $x^5$ değil, en küçük kuvvet olan $x^3$'tür: $x^3(x^2 + 1)$.

> **Eksi grupta işareti unutmak:** $x^2(x + 4) - x - 4$ ifadesinde ikinci grup $-(x - 4)$ değil, $-(x + 4)$'tür. Eksiyi dışarı alınca parantezdeki her terimin işareti değişir.

> **Çift kuvvette işareti yanlış çevirmek:** $(2 - x)^2 = -(x - 2)^2$ yanlıştır; çift kuvvette eksi kaybolur: $(2 - x)^2 = (x - 2)^2$.

> **Kesri terim terim bölmek:** $\dfrac{5^6 + 5^4}{5^5 + 5^3} \ne \dfrac{5^6}{5^5} + \dfrac{5^4}{5^3}$. Toplamı bölmek için önce pay ve paydayı çarpanlarına ayır, sonra sadeleştir.

## Kendini dene

### Soru 1
$10x^4 - 15x^2$ ifadesinin çarpanlarına ayrılmış biçimi aşağıdakilerden hangisidir?

A) $5x^2(2x^2 - 15)$
B) $5x^2(2x^2 - 3x)$
C) $5x^2(2x^2 - 3)$
D) $5x^4(2 - 3x^2)$
E) $10x^2(x^2 - 3)$

**Cevap:** C
**Çözüm:** $\text{EBOB}(10, 15) = 5$, en küçük kuvvet $x^2$; ortak çarpan $5x^2$. $\frac{10x^4}{5x^2} = 2x^2$, $\frac{-15x^2}{5x^2} = -3$. Sonuç $5x^2(2x^2 - 3)$. A'da $15$ bölünmemiş, B'de $x$ fazla, D'de en büyük kuvvet dışarı alınmış, E'de EBOB yerine $10$ alınmış; açılınca $10x^4 - 30x^2$ olur.

### Soru 2
$xy + 3x - 2y - 6$ polinomunun çarpanlarından biri aşağıdakilerden hangisidir?

A) $x + 2$
B) $x - 2$
C) $y - 3$
D) $y + 2$
E) $x + 3$

**Cevap:** B
**Çözüm:** İlk iki terimden $x$, son iki terimden $-2$ al: $x(y + 3) - 2(y + 3) = (y + 3)(x - 2)$. Çarpanlar $x - 2$ ve $y + 3$; seçeneklerde yalnızca $x - 2$ var. Son grupta eksiyi dışarı alırken işareti çevirmeyen $x + 2$ ya da $y - 3$ bulur.

### Soru 3
$a + b = 6$ ve $ab = 4$ olduğuna göre $a^2b + ab^2$ ifadesinin değeri kaçtır?

A) 10
B) 16
C) 20
D) 24
E) 36

**Cevap:** D
**Çözüm:** $a^2b + ab^2 = ab(a + b) = 4 \cdot 6 = 24$. $a + b$ ile $ab$'yi toplayan 10, $(a + b)^2$ hesaplayan 36 bulur.

## Özet kartı

- Ortak çarpan = katsayıların EBOB'u $\times$ ortak harflerin en küçük kuvveti.
- Parantezin içindeki terim sayısı başlangıçtaki terim sayısına eşittir; tamamen çıkan terimin yerinde $1$ kalır.
- Ortak çarpan bir ifade de olabilir: $a(x - y) + b(x - y) = (x - y)(a + b)$.
- $b - a = -(a - b)$; çift kuvvette işaret kaybolur, tek kuvvette dışarı çıkar.
- Gruplandırma: her gruptan aynı parantezi elde et; olmazsa işaret çevir ya da yeniden grupla.
- $a + b$ ve $ab$ verilen sorularda önce ifadeyi çarpanlarına ayır, sonra yerine yaz.

## Sonraki adım

Alıştırmaya geç (aşağıdaki düğme). Sonraki ders **Tam Kare veya İki Kare Farkı Özdeşliklerinden Faydalanarak Çarpanlara Ayırma**; bu derste yarım kalan $x^2 - 1$ gibi ifadeleri orada sonuna kadar ayıracaksın.
