---
baslik: Üslü İfadeler ve Özellikleri
ders: tyt-matematik
sure: 25 dk
kaynak: MEBİ Konu Özeti c503fcd74e
guncelleme: 2026-11-18
---
# Üslü İfadeler ve Özellikleri

<div class="giris" dir="rtl" lang="ar">

**الدرس ده عن إيه؟** عن الأسس (üslü ifadeler): لما تضرب نفس العدد في نفسه كذا مرة، وإزاي تحسب وتختصر القوى دي من غير ما تتلخبط.

- هتعرف إشارة الناتج لما الأساس (taban) يكون سالب، والفرق بين وجود القوس وعدمه.
- هتفهم الأس صفر والأس السالب (negatif kuvvet) من غير حفظ، وقواعد الجمع والطرح والضرب والقسمة في الأسس.
- هتتعلم ترتّب الأعداد الأسية من الأصغر للأكبر، وتعرف عدد أرقام (basamak sayısı) ناتج زي حاصل ضرب قوى ٢ في قوى ٥.

**ليه مهم؟** في كل امتحان TYT بييجي سؤال أو اتنين على الأسس مباشرة، وكمان هتحتاجها بعدين في الجذور والمعادلات الأسية والمسائل.

٢٥ دقيقة، وكل قاعدة معاها مثال محلول خطوة بخطوة. ابدأ وهتلاقيه أسهل ما انت فاكر.

</div>

**Bu dersin sonunda:** üslü bir ifadenin işaretini ve değerini bulabilecek, sıfır ve negatif kuvvetleri yazabilecek, üslü sayılarla dört işlemi kurallara göre sadeleştirebilecek ve üslü sayıları büyükten küçüğe sıralayabileceksin.

> **TYT'de yeri:** Her sınavda 1–2 soru doğrudan üslü ifadeden gelir; köklü ifadeler, üslü denklemler ve problemlerde de araç olarak kullanılır. Sık kalıplar: "ifadenin değeri kaçtır?", "$2^{x+3} - 2^{x+1}$ gibi bir ifadeyi ortak paranteze alma", "sayı kaç basamaklıdır?", "$a$, $b$, $c$ sıralaması". Yeni nesil sorularda ikiye katlanan nüfus, bellek birimleri (KB, MB, GB) ya da tanımlanan bir tuş işlemi verilir.

## Önce hatırla

<details><summary>Mutlak değerli denklemlerden: $|2x + 1| = 9$ denkleminin köklerinin toplamı kaçtır?</summary>
İçerisi ya $9$ ya $-9$'dur: $2x + 1 = 9 \Rightarrow x = 4$; $2x + 1 = -9 \Rightarrow x = -5$. Toplam $4 + (-5) = $ <b>−1</b>.
</details>

<details><summary>Mutlak değerli eşitsizliklerden: $|x - 4| \le 3$ eşitsizliğini sağlayan kaç tam sayı vardır?</summary>
$x$'in $4$'e uzaklığı en çok $3$: $-3 \le x - 4 \le 3 \Rightarrow 1 \le x \le 7$. Tam sayılar $1, 2, \dots, 7$; toplam <b>7</b> tane.
</details>

## Üslü ifade ve işaret

**Örnek.** $(-3)^2$, $-3^2$ ve $(-2)^3$ değerlerini bul.

- $(-3)^2 = (-3) \cdot (-3) = 9$. Parantez var; eksi işareti de kuvvete girer.
- $-3^2 = -(3 \cdot 3) = -9$. Parantez yok; kuvvet yalnızca $3$'e uygulanır, eksi sonra gelir.
- $(-2)^3 = (-2) \cdot (-2) \cdot (-2) = -8$. Üç eksi çarpılınca sonuç eksi kalır.

$n$ pozitif bir tam sayı olmak üzere $a^n$, $n$ tane $a$'nın çarpımıdır:

$$a^n = \underbrace{a \cdot a \cdot \ldots \cdot a}_{n \text{ tane}}$$

Burada $a$ **taban**, $n$ **üs** (kuvvet) adını alır. $a^n$ ifadesine **üslü ifade** denir.

![Çubuk grafik: eksi 2'nin 1'den 6'ya kadar kuvvetleri. Tek kuvvetler (−2, −8, −32) kırmızı ve aşağıda, çift kuvvetler (4, 16, 64) yeşil ve yukarıda.](gorsel/tyt-matematik/04-01-isaret.svg "Negatif tabanda işaret üssün tek ya da çift olmasına bağlıdır: çift kuvvet pozitif, tek kuvvet negatif.")

**Kural.**

| Taban | Çift kuvvet | Tek kuvvet |
|---|---|---|
| Pozitif ($3$) | $3^4 = 81$, pozitif | $3^3 = 27$, pozitif |
| Negatif ($-2$) | $(-2)^4 = 16$, pozitif | $(-2)^3 = -8$, negatif |
| Sıfır | $0^4 = 0$ | $0^3 = 0$ |

Ayrıca her $n$ için $1^n = 1$, $a^1 = a$ ve $(-1)^{\text{çift}} = 1$, $(-1)^{\text{tek}} = -1$ olur.

## Sıfırıncı ve negatif kuvvet

**Örnek.** $2^0$ ve $2^{-1}$ neye eşittir?

$2^3 = 8$, $2^2 = 4$, $2^1 = 2$: üs $1$ azalınca değer **yarıya** iniyor. Bu düzeni sürdür: $2^0 = 2 \div 2 = 1$, $2^{-1} = 1 \div 2 = \frac{1}{2}$, $2^{-2} = \frac{1}{4}$.

![Altı kutu yan yana: 2 üssü 3 eşittir 8, 2 üssü 2 eşittir 4, 2 üssü 1 eşittir 2, 2 üssü 0 eşittir 1, 2 üssü eksi 1 eşittir bir bölü 2, 2 üssü eksi 2 eşittir bir bölü 4. Kutular arasında bölü 2 okları.](gorsel/tyt-matematik/04-01-yarilama.svg "Her adımda üs 1 azalır, değer 2'ye bölünür. Sarı kutular bu düzenin devamıdır; kural ezber değil, düzenin sonucudur.")

**Kural.** $x \ne 0$ ve $n$ pozitif tam sayı olmak üzere:

$$x^0 = 1 \qquad x^{-n} = \frac{1}{x^n} \qquad \left(\frac{a}{b}\right)^{-n} = \left(\frac{b}{a}\right)^{n}$$

Örnekler: $\left(\frac{2}{5}\right)^{-2} = \left(\frac{5}{2}\right)^{2} = \frac{25}{4}$; $(-3)^{-3} = \frac{1}{(-3)^3} = -\frac{1}{27}$.

- Negatif üs sayıyı **negatif yapmaz**, sayıyı **ters çevirir**: $2^{-3} = \frac{1}{8}$, $-8$ değil.
- $0^{-1}$ tanımsızdır, çünkü $0$'ın çarpmaya göre tersi yoktur. $0^0$ belirsizdir.
- $-7^0 = -(7^0) = -1$, ama $(-7)^0 = 1$.

## Toplama ve çıkarma: ortak paranteze al

**Örnek.** $2^5 + 2^5$ ve $\dfrac{3^{10} + 3^{8}}{3^{8}}$ değerlerini bul.

- $2^5 + 2^5 = 2 \cdot 2^5 = 2^6$. Aynı şeyden iki tane var; üsler toplanmaz.
- Payda en küçük kuvvet olan $3^8$'i ortak paranteze al: $3^{10} + 3^8 = 3^8 (3^2 + 1) = 3^8 \cdot 10$. Bölünce $10$ kalır.

**Kural.** Yalnızca **tabanı ve üssü aynı** olan terimler toplanıp çıkarılır, katsayılar toplanır:

$$a \cdot x^n + b \cdot x^n - c \cdot x^n = (a + b - c) \cdot x^n$$

Örnek: $5 \cdot 3^7 - 2 \cdot 3^7 = 3 \cdot 3^7 = 3^8$. Üsleri farklıysa (örneğin $2^{x+3} - 2^{x+1}$) küçük kuvveti ortak paranteze al: $2^{x+1}(2^2 - 1) = 3 \cdot 2^{x+1}$.

## Çarpma ve bölme

**Örnek.** $2^3 \cdot 2^2$ kaçtır?

![Beş kutuda 2 yazıyor; ilk üçünün üstünde 2 üssü 3, son ikisinin üstünde 2 üssü 2. Altta: 5 tane 2 çarpılıyor, 2 üssü 3 çarpı 2 üssü 2 eşittir 2 üssü 5.](gorsel/tyt-matematik/04-01-carpma.svg "Çarpımda 2'ler yan yana dizilir; kaç tane 2 olduğunu saymak üsleri toplamaktır.")

$2^3 \cdot 2^2 = 2^{3+2} = 2^5 = 32$. Bölmede ortak çarpanlar sadeleşir: $\dfrac{5^9}{5^6} = 5^{9-6} = 5^3 = 125$.

**Üsler aynıysa** tabanlar birleşir: $4^5 \cdot 25^5 = (4 \cdot 25)^5 = 100^5 = 10^{10}$ ve $\dfrac{18^4}{6^4} = \left(\dfrac{18}{6}\right)^4 = 3^4 = 81$.

**Kural.**

| İşlem | Koşul | Sonuç |
|---|---|---|
| $x^a \cdot x^b$ | taban aynı | $x^{a+b}$ |
| $\dfrac{x^a}{x^b}$ | taban aynı, $x \ne 0$ | $x^{a-b}$ |
| $x^a \cdot y^a$ | üs aynı | $(x \cdot y)^a$ |
| $\dfrac{x^a}{y^a}$ | üs aynı, $y \ne 0$ | $\left(\dfrac{x}{y}\right)^a$ |
| $(x^a)^b$ | üssün üssü | $x^{a \cdot b}$ |

Taban da üs de farklıysa önce **tabanları aynı asala** çevir: $8^3 \cdot 4^{-2} = (2^3)^3 \cdot (2^2)^{-2} = 2^9 \cdot 2^{-4} = 2^5 = 32$.

**Basamak sayısı.** $2^{10} \cdot 5^{8} = 2^2 \cdot (2^8 \cdot 5^8) = 4 \cdot 10^8 = 400\,000\,000$; yani 9 basamaklı. $2$ ile $5$'i eşleştirip $10$ yap, artanı başa yaz.

## Üslü sayıları sıralama

**Örnek 1 (tabanları eşitle).** $a = 9^7$, $b = 27^4$, $c = 243^3$ sırala.

$a = (3^2)^7 = 3^{14}$, $b = (3^3)^4 = 3^{12}$, $c = (3^5)^3 = 3^{15}$. Taban $1$'den büyükse üssü büyük olan büyüktür: $b < a < c$.

**Örnek 2 (üsleri eşitle).** $a = 2^{30}$, $b = 3^{20}$, $c = 5^{10}$ sırala.

Üslerin ortak böleni $10$: $a = (2^3)^{10} = 8^{10}$, $b = (3^2)^{10} = 9^{10}$, $c = 5^{10}$. Üsler aynı ve tabanlar pozitif; tabanı büyük olan büyüktür: $c < a < b$.

**Örnek 3 (aralığa yerleştir).** $2^x = 50$, $3^y = 50$, $7^z = 50$ ise $x$, $y$, $z$ sırala.

Hiçbir şey eşitlenemiyor. $50$'yi her tabanın ardışık iki kuvveti arasına koy:

| Denklem | Yerleştirme | Sonuç |
|---|---|---|
| $2^x = 50$ | $2^5 = 32 < 50 < 64 = 2^6$ | $5 < x < 6$ |
| $3^y = 50$ | $3^3 = 27 < 50 < 81 = 3^4$ | $3 < y < 4$ |
| $7^z = 50$ | $7^2 = 49 < 50 < 343 = 7^3$ | $2 < z < 3$ |

![Sayı doğrusu 0'dan 7'ye. Üstünde üç aralık: z için 2 ile 3 arası, y için 3 ile 4 arası, x için 5 ile 6 arası; uçlar boş nokta.](gorsel/tyt-matematik/04-01-aralik.svg "Üç bilinmeyen ayrı aralıklara düştüğü için tam değerlerini bilmeden sıralanır: z < y < x.")

Sonuç: $z < y < x$.

![Karar şeması: üslü sayıları sırala. Tabanlar eşitlenebiliyorsa büyük üs büyüktür. Değilse üsler eşitlenebiliyorsa büyük taban büyüktür. O da olmazsa ardışık kuvvetler arasına yerleştir.](gorsel/tyt-matematik/04-01-siralama.svg "Sıralama sorusunda bu sırayla dene. İlk yol taban 1'den büyükken, ikinci yol tabanlar pozitifken geçerlidir.")

## ÖSYM tuzakları

> **Parantezsiz eksi:** $-2^4 = -16$, ama $(-2)^4 = 16$. Kuvvet yalnızca hemen solundaki sayıya ya da paranteze uygulanır.

> **Negatif üssü negatif sayı sanmak:** $3^{-2} = \frac{1}{9}$'dur; $-9$ ya da $-6$ değil. Negatif üs ters çevirir.

> **Toplamada üsleri toplamak:** $2^3 + 2^4 \ne 2^7$. Toplamada kural yoktur; ortak paranteze al: $2^3(1 + 2) = 24$. Aynı biçimde $4^5 + 4^5 + 4^5 + 4^5 = 4 \cdot 4^5 = 4^6$'dır, $4^{20}$ ya da $16^5$ değil.

> **Üssün üssünü karıştırmak:** $(2^3)^2 = 2^6$, ama $2^{3^2} = 2^9$. Parantez yoksa önce üstteki kuvvet hesaplanır.

> **1'den küçük tabanda sıra döner:** $\left(\frac{1}{2}\right)^3 = \frac{1}{8} < \frac{1}{4} = \left(\frac{1}{2}\right)^2$. Taban $0$ ile $1$ arasındaysa üssü büyük olan **küçüktür**. "Büyük üs büyük" kuralını yalnızca taban $1$'den büyükken kullan.

## Kendini dene

### Soru 1
$-3^2 + (-3)^2 + (-2)^3$ işleminin sonucu kaçtır?

A) $-26$
B) $-8$
C) $8$
D) $10$
E) $26$

**Cevap:** B
**Çözüm:** $-3^2 = -9$ (parantez yok), $(-3)^2 = 9$, $(-2)^3 = -8$ (tek kuvvet). Toplam $-9 + 9 - 8 = -8$. $-3^2$'yi $9$ alan $10$; $(-2)^3$'ü $8$ alan $8$ bulur.

### Soru 2
$\dfrac{9^{4} \cdot 3^{-4}}{27}$ işleminin sonucu kaçtır?

A) $\frac{1}{3}$
B) $1$
C) $3$
D) $9$
E) $3^{9}$

**Cevap:** C
**Çözüm:** Hepsini $3$ tabanına çevir: $9^4 = (3^2)^4 = 3^8$, $27 = 3^3$. İfade $3^{8 + (-4) - 3} = 3^1 = 3$. $9^4$'ü $3^6$ yazan (üsleri toplayan) $\frac{1}{3}$; $-4$'ün işaretini kaçıran $3^9$ bulur.

### Soru 3
$a = 4^{11}$, $b = 8^{7}$, $c = 16^{5}$ olduğuna göre aşağıdaki sıralamalardan hangisi doğrudur?

A) $a < b < c$
B) $a < c < b$
C) $b < c < a$
D) $c < b < a$
E) $c < a < b$

**Cevap:** D
**Çözüm:** Tabanları $2$ yap: $a = 2^{22}$, $b = 2^{21}$, $c = 2^{20}$. Taban $1$'den büyük olduğundan üssü büyük olan büyüktür: $c < b < a$. Tabanı büyük olanı büyük sanan A'yı seçer.

## Özet kartı

- $a^n$: $n$ tane $a$'nın çarpımı. Negatif taban: çift kuvvet $+$, tek kuvvet $-$. $-a^n$ ile $(-a)^n$ farklıdır.
- $x^0 = 1$ ($x \ne 0$), $x^{-n} = \frac{1}{x^n}$, $\left(\frac{a}{b}\right)^{-n} = \left(\frac{b}{a}\right)^n$.
- Toplama, çıkarma: yalnızca aynı taban ve aynı üs; değilse ortak paranteze al.
- Aynı tabanda çarpma üsleri toplar, bölme çıkarır; aynı üste tabanlar çarpılır, bölünür; $(x^a)^b = x^{ab}$.
- Basamak sayısı: $2$ ile $5$'leri eşleştir, $10$'un kuvvetini ayır.
- Sıralama: tabanları eşitle, olmazsa üsleri eşitle, o da olmazsa aralığa yerleştir.

## Sonraki adım

Alıştırmaya geç (aşağıdaki düğme). Sonraki ders **Üslü İfade İçeren Denklem ve Eşitsizlikler**; orada $2^{x+1} = 32$ gibi denklemleri, bu dersteki "tabanları eşitle" fikriyle çözeceksin.
