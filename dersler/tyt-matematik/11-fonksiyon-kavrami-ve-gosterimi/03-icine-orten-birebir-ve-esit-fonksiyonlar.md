---
baslik: İçine, Örten, Birebir ve Eşit Fonksiyonlar
ders: tyt-matematik
sure: 20 dk
kaynak: MEBİ Konu Özeti aad486ecb6
guncelleme: 2026-11-18
---
# İçine, Örten, Birebir ve Eşit Fonksiyonlar

**Bu dersin sonunda:** bir fonksiyonun içine mi örten mi, bire bir olup olmadığını ok şemasından, kuralından ve grafiğinden söyleyebilecek; bire bir fonksiyonları sayabilecek ve iki fonksiyonun eşit olup olmadığına karar verebileceksin.

> **TYT'de yeri:** Bu kavramlar çoğu zaman tek başına değil, bir fonksiyon sorusunun içinde gelir: "aşağıdakilerden hangisi bire birdir?", "$f$ örten olduğuna göre değer kümesi nedir?", "kaç tane bire bir fonksiyon yazılabilir?" ve "$f = g$ olduğuna göre $a$ kaçtır?" en sık kalıplardır. Bire bir fonksiyon, ileride ters fonksiyonun da ön koşuludur.

## Önce hatırla

<details><summary>Fonksiyon sorularından: $f(2x - 1) = 6x + 5$ olduğuna göre $f(3)$ kaçtır?</summary>
Parantezin içini 3 yapan $x$'i bul: $2x - 1 = 3$, $x = 2$. Bunu sağ tarafa yaz: $f(3) = 6 \cdot 2 + 5 = 17$.
</details>

<details><summary>Fonksiyon sorularından: $f\colon (1, 4] \to \mathbb{R}$, $f(x) = 3x - 2$ fonksiyonunun görüntü kümesi nedir?</summary>
Sınırların görüntülerine bak: $f(1) = 1$, $f(4) = 10$. $1$ tanım kümesinde olmadığı için görüntüsü de kümeye girmez: görüntü kümesi $(1, 10]$.
</details>

## İçine ve örten fonksiyon

**Örnek.** $f(x) = x^2$ kuralı $A = \{-1, 0, 1, 2\}$ kümesinde tanımlı olsun. Görüntüler $f(-1) = 1$, $f(0) = 0$, $f(1) = 1$, $f(2) = 4$; yani $f(A) = \{0, 1, 4\}$.

- Değer kümesi $B = \{0, 1, 2, 4\}$ seçilirse $2$'ye hiç ok gelmez. $f(A) \ne B$.
- Değer kümesi $B = \{0, 1, 4\}$ seçilirse $B$'nin her elemanına en az bir ok gelir. $f(A) = B$.

![İki ok şeması yan yana. A kümesi −1, 0, 1, 2. Solda B kümesi 0, 1, 2, 4 ve 2 kırmızı daire içinde boşta. Sağda B kümesi 0, 1, 4 ve boşta eleman yok.](gorsel/tyt-matematik/11-03-icine-orten.svg "Kural aynı, yalnızca değer kümesi değişti. İçine ya da örten olmak değer kümesine bağlıdır.")

**Kural.** $f\colon A \to B$ bir fonksiyon olsun.

| Ad | Koşul | Ok şemasında |
|---|---|---|
| **İçine** | $f(A) \ne B$ | Değer kümesinde boşta eleman var |
| **Örten** | $f(A) = B$ | Değer kümesinde boşta eleman yok |

Her fonksiyon ya içinedir ya örtendir; ikisi birden olamaz. Örten olup olmadığını anlamak için görüntü kümesini bul ve değer kümesiyle karşılaştır.

**Gerçek sayılarda.** $f\colon \mathbb{R} \to \mathbb{R}$, $f(x) = x^2$ örten değildir: hiçbir sayının karesi $-2$ olmaz, yani negatif sayılar boşta kalır. Aynı kural $f\colon \mathbb{R} \to [0, \infty)$ olarak yazılırsa örtendir.

## Bire bir fonksiyon

**Örnek.** $A = \{-1, 0, 1, 2\}$ kümesinde iki kural deneyelim.

- $f(x) = x^2$: $f(-1) = 1$ ve $f(1) = 1$. Farklı iki eleman **aynı** görüntüye gidiyor.
- $g(x) = 2x + 1$: görüntüler $-1, 1, 3, 5$. Hepsi farklı.

$g$ bire birdir, $f$ değildir.

**Kural.** Tanım kümesinin farklı elemanlarının görüntüleri de farklıysa fonksiyon **bire birdir**:

$$x_1 \ne x_2 \implies f(x_1) \ne f(x_2)$$

Aynı şeyi şöyle de söyleyebilirsin: $f(a) = f(b)$ ise $a = b$ olmalı. Ok şemasında değer kümesinin hiçbir elemanına **iki ok gelmez**. Bire bir olmadığını göstermek için tek bir örnek yeter: $f(-1) = f(1)$.

**Grafikte yatay doğru testi.** $f\colon \mathbb{R} \to \mathbb{R}$ fonksiyonunun grafiğini $x$ eksenine paralel doğrularla kes.

![İki grafik. Solda f(x) = 2x − 1 doğrusu ve y = 3 yatay doğrusu, tek noktada (2, 3) kesişiyor. Sağda g(x) = x kare parabolü; y = 4 doğrusu onu −2 ve 2'de iki noktada kesiyor, y = −2 doğrusu hiç kesmiyor.](gorsel/tyt-matematik/11-03-yatay-dogru.svg "Yatay doğru grafiği iki kez keserse bire bir değil; hiç kesmezse örten değil. Sağdaki parabol iki testten de kalıyor.")

| Her yatay doğru grafiği | Sonuç |
|---|---|
| En çok bir noktada keser | Bire bir |
| En az bir noktada keser | Örten |
| Tam bir noktada keser | Bire bir ve örten |

Doğrusal fonksiyon $f(x) = ax + b$, $a \ne 0$ ise $\mathbb{R}$'den $\mathbb{R}$'ye hem bire bir hem örtendir. $x^2$ ve $|x|$ gibi "$-x$ ile $x$'e aynı değeri veren" kurallar $\mathbb{R}$ üzerinde bire bir değildir.

## Eleman sayıları ve sayma

İki özelliği birlikte düşününce dört durum çıkar:

![Dört ok şeması. İçine ve bire bir: 1 ve 2, a ve b'ye gidiyor, c boşta. İçine ve bire bir değil: 1 ve 2 a'ya, 3 b'ye, c boşta. Örten ve bire bir değil: 1 a'ya, 2 ve 3 b'ye. Bire bir ve örten: 1 b'ye, 2 c'ye, 3 a'ya.](gorsel/tyt-matematik/11-03-dort-durum.svg "Kırmızı daire boşta kalan eleman, sarı daire iki ok alan elemandır. Bire bir ve örten olanda ikisi de yok.")

Sonlu kümelerde $s(A)$ ile $s(B)$'yi karşılaştırmak çoğu soruyu tek adımda çözer:

| Durum | Sonuç |
|---|---|
| $f$ bire bir | $s(A) \le s(B)$ olmalı |
| $f$ örten | $s(A) \ge s(B)$ olmalı |
| $f$ bire bir ve örten | $s(A) = s(B)$ olmalı |
| $s(A) = s(B)$ | Bire bir $\iff$ örten |

Örneğin $s(A) = 5$, $s(B) = 4$ ise 5 elemana 4 farklı görüntü yetmez; iki eleman aynı yere gider, $f$ bire bir **olamaz**.

**Örnek.** $A = \{a, b, c\}$ ve $B = \{1, 2, 3, 4, 5\}$ ise $A$'dan $B$'ye kaç bire bir fonksiyon yazılır?

$f(a)$ için 5 seçenek var. $f(b)$, $f(a)$'dan farklı olmalı: 4 seçenek. $f(c)$ ilk ikisinden farklı: 3 seçenek. Toplam $5 \cdot 4 \cdot 3 = 60$.

**Kural.** $s(A) = m$, $s(B) = n$ ve $m \le n$ ise:

- Bire bir fonksiyon sayısı: $n \cdot (n - 1) \cdots (n - m + 1) = \dfrac{n!}{(n - m)!}$ (tam $m$ çarpan).
- $m = n$ ise bire bir ve örten fonksiyon sayısı: $n!$.
- $m = n$ ise içine fonksiyon sayısı: bütün fonksiyonlardan bire bir örtenleri çıkar, $n^n - n!$.
- $m < n$ ise hiçbir fonksiyon örten olamaz; $n^m$ fonksiyonun hepsi içinedir.

## Eşit fonksiyonlar

**Örnek.** $A = \{1, 2\}$ olmak üzere $f, g\colon A \to \mathbb{R}$, $f(x) = x^2$ ve $g(x) = 3x - 2$ olsun.

| $x$ | $f(x) = x^2$ | $g(x) = 3x - 2$ |
|---|---|---|
| $1$ | $1$ | $1$ |
| $2$ | $4$ | $4$ |

Kurallar farklı görünse de $A$'nın her elemanında aynı değeri veriyorlar: $f = g$.

**Kural.** $f\colon A \to B$ ve $g\colon A \to B$ olsun. Her $x \in A$ için $f(x) = g(x)$ ise $f$ ile $g$ **eşit fonksiyonlardır**, $f = g$ yazılır. Tanım ve değer kümeleri aynı olmalı; kuralların aynı yazılması gerekmez.

Hangi küme üzerinde eşit olduklarını bulmak için denklemi çöz: $x^2 = 3x - 2 \implies x^2 - 3x + 2 = 0 \implies x = 1$ ya da $x = 2$. Bu iki fonksiyon, $\{1, 2\}$ kümesinin boş olmayan her alt kümesinde eşittir; $\mathbb{R}$ üzerinde eşit değildir ($f(0) = 0$, $g(0) = -2$).

## ÖSYM tuzakları

> **Değer kümesine bakmadan "örten" demek:** $f(x) = x^2$ kuralı tek başına örten ya da içine değildir. $\mathbb{R} \to \mathbb{R}$ ise içine, $\mathbb{R} \to [0, \infty)$ ise örtendir. Önce değer kümesini oku.

> **Bire bir için ters yöne bakmak:** Soldaki her elemandan tek ok çıkması fonksiyon olmanın şartıdır. Bire bir için **sağdaki** hiçbir elemana iki ok gelmemeli.

> **Eleman sayısını unutmak:** $s(A) > s(B)$ ise bire bir fonksiyon yoktur; $s(A) < s(B)$ ise örten fonksiyon yoktur. Uzun sayma yapmadan önce bu karşılaştırmayı yap.

> **Bire bir saymada üs kullanmak:** $s(A) = 3$, $s(B) = 5$ için bire bir fonksiyon sayısı $5^3 = 125$ değil, $5 \cdot 4 \cdot 3 = 60$'tır. Seçilen görüntü bir sonraki eleman için kullanılamaz.

> **Eşitliği tek noktada denemek:** $f = g$ için tanım kümesinin **her** elemanında $f(x) = g(x)$ olmalı. Bir elemanda tutması yetmez.

## Kendini dene

### Soru 1
$f\colon \{1, 2, 3\} \to \{4, 5, 6\}$ fonksiyonu $f = \{(1, 6),\ (2, 4),\ (3, 5)\}$ biçimindedir. Buna göre $f$ için aşağıdakilerden hangisi doğrudur?

A) İçine ve bire birdir.
B) İçinedir, bire bir değildir.
C) Örtendir, bire bir değildir.
D) Bire bir ve örtendir.
E) Fonksiyon değildir.

**Cevap:** D
**Çözüm:** Görüntüler $6, 4, 5$; hepsi farklı, yani bire bir. Görüntü kümesi $\{4, 5, 6\}$ değer kümesine eşit, yani örten. Her elemandan tek ok çıktığı için fonksiyondur.

### Soru 2
$s(A) = 4$ ve $s(B) = 6$ olduğuna göre $A$'dan $B$'ye kaç tane bire bir fonksiyon tanımlanabilir?

A) 24
B) 360
C) 720
D) 1296
E) 4096

**Cevap:** B
**Çözüm:** Sırayla 6, 5, 4 ve 3 seçenek: $6 \cdot 5 \cdot 4 \cdot 3 = 360$. $6^4 = 1296$ bütün fonksiyonların sayısıdır; $4^6 = 4096$ üssü ters koymaktır; $6! = 720$ ve $4! = 24$ çarpan sayısını yanlış almaktır.

### Soru 3
$A = \{0, 2\}$ olmak üzere $f, g\colon A \to \mathbb{R}$, $f(x) = x^2$ ve $g(x) = ax$ fonksiyonları eşittir. Buna göre $a$ kaçtır?

A) 0
B) 1
C) 2
D) 3
E) 4

**Cevap:** C
**Çözüm:** $x = 0$ için $f(0) = 0 = g(0)$, her $a$ için doğru. $x = 2$ için $f(2) = 4$ ve $g(2) = 2a$; $2a = 4$, $a = 2$. $4$, $f(2)$'nin kendisidir; $a$ değildir.

## Özet kartı

- İçine: $f(A) \ne B$ (boşta eleman var). Örten: $f(A) = B$ (boşta eleman yok).
- Bire bir: farklı elemanların görüntüleri farklı; sağdaki hiçbir elemana iki ok gelmez.
- Grafikte yatay doğru en çok bir kez keserse bire bir, en az bir kez keserse örten.
- Bire bir için $s(A) \le s(B)$, örten için $s(A) \ge s(B)$; $s(A) = s(B)$ ise bire bir $\iff$ örten.
- Bire bir fonksiyon sayısı $n(n - 1)\cdots$ ($m$ çarpan); $s(A) = s(B) = n$ ise bire bir örten sayısı $n!$.
- $f = g$: aynı tanım ve değer kümesi, her $x$ için $f(x) = g(x)$.

## Sonraki adım

Alıştırmaya geç (aşağıdaki düğme). Sonraki ders **Birim ve Sabit Fonksiyon**; birim fonksiyonun bire bir ve örten, sabit fonksiyonun ise (çoğu zaman) içine olduğunu orada göreceksin.
