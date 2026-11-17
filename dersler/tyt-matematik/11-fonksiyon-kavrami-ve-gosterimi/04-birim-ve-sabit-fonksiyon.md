---
baslik: Birim ve Sabit Fonksiyon
ders: tyt-matematik
sure: 20 dk
kaynak: MEBİ Konu Özeti d612185080
guncelleme: 2026-11-17
---
# Birim ve Sabit Fonksiyon

**Bu dersin sonunda:** bir kuralın birim ya da sabit fonksiyon olması için katsayıların ne olması gerektiğini bulabilecek, kesirli bir kuralın sabit olup olmadığına $\frac{a}{c} = \frac{b}{d}$ ile karar verebilecek ve bu iki fonksiyonu ok şemasında ve grafikte tanıyabileceksin.

> **TYT'de yeri:** Sorular çoğunlukla "$f$ birim fonksiyon olduğuna göre $a + b$ kaçtır?", "$f$ sabit fonksiyon olduğuna göre $f(2027)$ kaçtır?" kalıbında gelir. Kesirli bir kuralın sabit olması ve grafikte $y = x$ ile $y = c$ doğruları da sık kullanılır.

## Önce hatırla

<details><summary>İçine, örten, bire bir dersinden: $f\colon \{1, 2, 3\} \to \{a, b, c, d\}$, $f = \{(1, a),\ (2, c),\ (3, a)\}$. $f$ içine mi örten mi? Bire bir mi?</summary>
Görüntü kümesi $\{a, c\}$; $b$ ve $d$ boşta kalıyor, yani $f$ <b>içine</b>dir. $a$'ya iki ok geliyor ($f(1) = f(3)$), yani <b>bire bir değildir</b>.
</details>

<details><summary>İçine, örten, bire bir dersinden: $s(A) = 3$, $s(B) = 4$ ise $A$'dan $B$'ye kaç bire bir fonksiyon yazılır?</summary>
Sırayla 4, 3 ve 2 seçenek: $4 \cdot 3 \cdot 2 = 24$. Seçilen görüntü bir sonraki eleman için kullanılamaz.
</details>

## Birim fonksiyon

**Örnek.** $f\colon \mathbb{R} \to \mathbb{R}$, $f(x) = (a - 4)x + b + 1$ birim fonksiyon olduğuna göre $a$, $b$ ve $f(7)$ kaçtır?

Birim fonksiyon her sayıyı kendisine götürür: $f(x) = x$, yani $f(x) = 1 \cdot x + 0$. Katsayıları eşleştir:

- $x$'in katsayısı $1$ olmalı: $a - 4 = 1$, $a = 5$.
- Sabit terim $0$ olmalı: $b + 1 = 0$, $b = -1$.

Buradan $f(x) = x$ ve $f(7) = 7$. Hesap yapmaya gerek yok: birim fonksiyonda görüntü, elemanın kendisidir.

**Kural.** $A \ne \varnothing$ olmak üzere $f\colon A \to A$ fonksiyonu için her $x \in A$'da $f(x) = x$ ise $f$'ye **birim (özdeşlik) fonksiyon** denir ve $I$ ile gösterilir: $I(x) = x$.

- Tanım kümesi ile değer kümesi **aynı** kümedir.
- Her eleman kendisiyle eşlenir; bu yüzden birim fonksiyon hem **bire bir** hem **örtendir**.
- Grafiği $(x, x)$ noktalarından oluşur: $\mathbb{R}$'de bu, orijinden geçen $y = x$ doğrusudur.

![İki ok şeması. Solda A'dan A'ya: 1, 2, 3, 4 her biri karşıdaki kendisine gidiyor. Sağda A kümesi −1, 0, 2, 5 elemanlarının hepsi B'deki 7'ye gidiyor; B'deki 3 ve 9 kırmızı daire içinde boşta.](gorsel/tyt-matematik/11-04-ok-semalari.svg "Birimde oklar düz karşıya gider. Sabitte bütün oklar tek bir elemanda toplanır, geri kalanlar boşta kalır.")

**Bileşik ifadelerde.** $f$ birim fonksiyonsa parantezin içi ne olursa olsun aynen çıkar: $f(2x + 1) = 2x + 1$, $f(a^2) = a^2$.

## Sabit fonksiyon

**Örnek.** $f\colon \mathbb{R} \to \mathbb{R}$, $f(x) = (a - 3)x + b - 2$ sabit fonksiyondur ve $f(5) = 4$'tür. $a$ ve $b$ kaçtır?

Sabit fonksiyonun kuralında $x$ bulunmaz. Bu yüzden $x$'in katsayısı sıfır olmalı: $a - 3 = 0$, $a = 3$. Geriye $f(x) = b - 2$ kalır. Her $x$ için değer aynı olduğundan $f(5) = b - 2 = 4$, $b = 6$. Sonuç: $f(x) = 4$; $f(-10)$, $f(0)$, $f(2027)$ hepsi $4$'tür.

**Kural.** $f\colon A \to B$ fonksiyonunda tanım kümesinin **bütün** elemanları değer kümesindeki **tek bir** elemana gidiyorsa $f$ **sabit fonksiyondur**: $c \in B$ olmak üzere $f(x) = c$.

- Kuralda değişken ($x$) yoktur. Polinom kuralda $x$'li bütün terimlerin katsayıları $0$ olmalıdır.
- Grafiği $x$ eksenine paralel $y = c$ doğrusudur. $c = 0$ ise grafik $x$ ekseninin kendisidir.
- Bir değeri bilmek hepsini bilmektir: $f(3) = 7$ ise her $x$ için $f(x) = 7$.

![İki grafik. Solda y = x doğrusu orijinden geçiyor, üzerinde (2, 2) ve (−3, −3) noktaları işaretli. Sağda y = 3 yatay doğrusu, üzerinde (−3, 3) ve (2, 3) noktaları işaretli.](gorsel/tyt-matematik/11-04-grafikler.svg "Birimde noktanın iki koordinatı eşittir. Sabitte x ne olursa olsun y hep 3'tür.")

**Önceki dersle bağlantı.** Bütün oklar aynı elemana gittiği için:

| Durum | Sonuç |
|---|---|
| $s(A) \ge 2$ | Sabit fonksiyon bire bir **değildir** |
| $s(B) \ge 2$ | Sabit fonksiyon **içinedir** (boşta eleman kalır) |
| $s(B) = 1$ | Sabit fonksiyon örtendir |
| $A$'dan $B$'ye sabit fonksiyon sayısı | $s(B)$ (oklar hangi elemana gidecek?) |

Örneğin $\mathbb{R} \to \mathbb{R}$, $f(x) = 4$ hem içine hem bire bir olmayan bir fonksiyondur.

## Kesirli kural ne zaman sabittir?

**Örnek.** $f(x) = \dfrac{6x + m}{2x + 5}$ sabit fonksiyon olduğuna göre $m$ ve $f(x)$ nedir?

Kesir, pay paydanın sabit bir katıysa sadeleşip sayıya döner. Payın $x$'li terimi $6x$, paydanınki $2x$; oran $3$. Pay paydanın 3 katı olmalı: $6x + m = 3(2x + 5) = 6x + 15$, yani $m = 15$.

$$f(x) = \frac{6x + 15}{2x + 5} = \frac{3(2x + 5)}{2x + 5} = 3$$

Aynı sonuca katsayıları oranlayarak da varırsın: $\frac{6}{2} = \frac{m}{5}$, $m = 15$.

**Kural.** Tanımlı olduğu aralıkta

$$f(x) = \frac{ax + b}{cx + d} \text{ sabit fonksiyon} \iff \frac{a}{c} = \frac{b}{d}$$

ve bu durumda $f(x) = \dfrac{a}{c}$ olur. Oranı her zaman **$x$'li terimler kendi arasında, sabit terimler kendi arasında** kur. İşaretleri katsayıyla birlikte al: $\frac{4x + m}{2x - 3}$ için $\frac{4}{2} = \frac{m}{-3}$.

![Akış şeması: f sabit fonksiyon, kural nasıl? Polinom kuralı ise x'li katsayılar sıfıra eşitlenir ve f(x) sabit terime eşit olur. Kesirli kural ise a bölü c eşittir b bölü d yazılır ve f(x) a bölü c olur.](gorsel/tyt-matematik/11-04-sabit-mi.svg "Önce kuralın türüne bak. Kesirli kuralda sabitin değeri a bölü c'dir; a ya da c tek başına değil.")

## ÖSYM tuzakları

> **Birim fonksiyonda sabit terimi unutmak:** $f(x) = (a - 4)x + b + 1$ birim ise yalnızca $a - 4 = 1$ yetmez; $b + 1 = 0$ da olmalı. $f(x) = x + 2$ birim fonksiyon değildir.

> **Birim ile sabiti karıştırmak:** Birimde $x$'in katsayısı $1$, sabitte $0$'dır. $(a - 3)x$ terimi birimde $a = 4$, sabitte $a = 3$ verir.

> **Tanım ve değer kümesini kontrol etmemek:** $f\colon \{1, 2\} \to \{1, 2, 3\}$, $f(x) = x$ birim fonksiyon değildir; değer kümesi tanım kümesinden farklıdır ve $3$ boşta kalır (içine).

> **Kesirli kuralda değeri yanlış okumak:** $\frac{6x + 15}{2x + 5}$ sabitse değeri $6$ ya da $2$ değil, $\frac{6}{2} = 3$'tür. Oranı kurarken eksi işaretini de taşı.

> **Sabit fonksiyonda $x$'i yerine koymaya çalışmak:** $f$ sabit ve $f(1) = 5$ ise $f(100) = 5$'tir; $500$ ya da $104$ değil.

## Kendini dene

### Soru 1
$f\colon \mathbb{R} \to \mathbb{R}$, $f(x) = (2a - 5)x + a + b - 1$ birim fonksiyon olduğuna göre $a - b$ farkı kaçtır?

A) 1
B) 3
C) 5
D) 7
E) 9

**Cevap:** C
**Çözüm:** Birimde $x$'in katsayısı $1$: $2a - 5 = 1$, $a = 3$. Sabit terim $0$: $3 + b - 1 = 0$, $b = -2$. $a - b = 3 - (-2) = 5$. $a + b$'yi hesaplayan 1 bulur.

### Soru 2
$f(x) = \dfrac{3x - 6}{x + m}$ fonksiyonu tanımlı olduğu aralıkta sabit fonksiyon olduğuna göre $m$ kaçtır?

A) $-3$
B) $-2$
C) $2$
D) $3$
E) $6$

**Cevap:** B
**Çözüm:** $\frac{3}{1} = \frac{-6}{m}$, buradan $3m = -6$, $m = -2$. Kontrol: $\frac{3x - 6}{x - 2} = \frac{3(x - 2)}{x - 2} = 3$. Eksi işaretini kaybeden $2$ bulur; $3$ ise fonksiyonun değeridir, $m$ değil.

### Soru 3
$f\colon \mathbb{R} \to \mathbb{R}$ sabit fonksiyon ve $f(1) + f(2) + \dots + f(10) = 50$ olduğuna göre $f(100)$ kaçtır?

A) 5
B) 10
C) 50
D) 100
E) 500

**Cevap:** A
**Çözüm:** Sabit fonksiyonda on terimin hepsi aynıdır: $10 \cdot f(x) = 50$, $f(x) = 5$. Her $x$ için değer $5$ olduğundan $f(100) = 5$. $500$, $f(100)$'ü $100 \cdot 5$ sanmaktan gelir.

## Özet kartı

- Birim fonksiyon: $f\colon A \to A$, $I(x) = x$; bire bir ve örten, grafiği $y = x$.
- $f(x) = mx + n$ birim $\iff m = 1$ ve $n = 0$.
- Sabit fonksiyon: $f(x) = c$; kuralda $x$ yok, grafiği yatay $y = c$ doğrusu.
- Polinom kural sabitse $x$'li bütün katsayılar $0$; değer sabit terimdir.
- $\frac{ax + b}{cx + d}$ sabit $\iff \frac{a}{c} = \frac{b}{d}$; değeri $\frac{a}{c}$.
- Sabit fonksiyon $s(A) \ge 2$ ise bire bir değil, $s(B) \ge 2$ ise içinedir; $A$'dan $B$'ye $s(B)$ tane sabit fonksiyon vardır.

## Sonraki adım

Alıştırmaya geç (aşağıdaki düğme). Sonraki ders **Doğrusal ve Parçalı Fonksiyonlar**; $f(x) = ax + b$ kuralında $a = 1$, $b = 0$ olursa birim, $a = 0$ olursa sabit fonksiyon elde ettiğini orada yeniden göreceksin.
