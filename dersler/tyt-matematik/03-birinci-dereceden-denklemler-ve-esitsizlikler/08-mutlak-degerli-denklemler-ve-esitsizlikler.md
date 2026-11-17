---
baslik: Mutlak Değerli Denklemler ve Eşitsizlikler
ders: tyt-matematik
sure: 25 dk
kaynak: MEBİ Konu Özeti d86a66b754
guncelleme: 2026-11-17
---
# Mutlak Değerli Denklemler ve Eşitsizlikler

**Bu dersin sonunda:** $|ax + b| = c$, $|ax + b| < c$ ve $|ax + b| > c$ biçimindeki denklem ve eşitsizlikleri "uzaklık" fikriyle çözebilecek, değişken mutlak değerin dışında da varsa bulduğun kökleri kontrol edebileceksin.

> **TYT'de yeri:** Her yıl en az bir soru mutlak değerden gelir ve çoğu bu dersin kalıplarıdır: "köklerin toplamı kaçtır?", "eşitsizliği sağlayan kaç tam sayı vardır?", "hangisinin çözüm kümesi boştur?". Yeni nesil sorularda "hedef değerden en fazla şu kadar sapma" gibi günlük durumlar mutlak değerli eşitsizliğe çevrilir.

## Önce hatırla

<details><summary>Mutlak değer kavramından: $x < 0$ olduğuna göre $|3x| + |-5x|$ ifadesinin eşiti nedir?</summary>
$x$ negatif olduğu için $3x$ negatiftir: $|3x| = -3x$. $-5x$ ise pozitiftir: $|-5x| = -5x$. Toplam: $-3x + (-5x) = -8x$, yani cevap <b>−8x</b>. (Sonuç pozitif bir sayıdır, çünkü $x < 0$.)
</details>

<details><summary>Mutlak değer kavramından: Sayı doğrusunda $-2$ ile $5$ arasındaki uzaklığı mutlak değerle yaz ve hesapla.</summary>
İki sayı arasındaki uzaklık farkın mutlak değeridir: $|-2 - 5| = |-7| = 7$. Uzaklık <b>7</b> birim. Bu dersin anahtarı bu fikir: $|x - a|$, $x$'in $a$'ya uzaklığıdır.
</details>

## |x − a| = c: uzaklığı belli olan noktalar

**Örnek.** $|x - 3| = 5$ denklemini çöz.

$|x - 3|$, $x$'in $3$'e uzaklığıdır. $3$'e uzaklığı $5$ olan iki sayı vardır: biri sağda, biri solda.

![Sayı doğrusu: 3'te merkez noktası; 3'ten sola 5 birim giden ok −2'de, sağa 5 birim giden ok 8'de biter. −2 ve 8 mavi dolu noktalar.](gorsel/tyt-matematik/03-08-uzaklik.svg "Merkez 3, uzaklık 5. Merkezin iki yanına eşit adım at: −2 ve 8.")

Cebirle: mutlak değerin içi ya $5$'tir ya $-5$:

$$x - 3 = 5 \Rightarrow x = 8 \qquad\text{veya}\qquad x - 3 = -5 \Rightarrow x = -2$$

Çözüm kümesi $\{-2, 8\}$. Köklerin toplamı $6 = 2 \cdot 3$: kökler merkeze göre simetriktir.

**Kural.** $c$ bir sabit olmak üzere $|A| = c$ denkleminde:

| $c$ | Çözüm |
|---|---|
| $c > 0$ | $A = c$ veya $A = -c$ (iki durum) |
| $c = 0$ | $A = 0$ (tek durum) |
| $c < 0$ | Çözüm yok: $\text{ÇK} = \varnothing$ |

Mutlak değer bir uzaklıktır, **negatif olamaz**. Bu yüzden $|2x + 1| = -3$ denkleminin hiç çözümü yoktur; içini hesaplamaya bile gerek yok.

**İçinde katsayı varsa** aynı iki durumu yaz: $|2x - 3| = 7$ için $2x - 3 = 7$ ya da $2x - 3 = -7$, yani $x = 5$ ya da $x = -2$.

## İki mutlak değer eşitse

**Örnek.** $|x - 1| = |2x + 4|$ denklemini çöz.

İki sayının mutlak değerleri eşitse sayılar ya **aynıdır** ya **birbirinin ters işaretlisidir**:

- $x - 1 = 2x + 4 \Rightarrow x = -5$
- $x - 1 = -(2x + 4) \Rightarrow x - 1 = -2x - 4 \Rightarrow 3x = -3 \Rightarrow x = -1$

Kontrol: $x = -5$ için $|-6| = |-6|$; $x = -1$ için $|-2| = |2|$. Çözüm kümesi $\{-5, -1\}$.

**Kural.** $|A| = |B| \iff A = B$ veya $A = -B$. İkinci durumda eksiyi **bütün** $B$'ye dağıt.

## Toplamları sıfır olan mutlak değerler

**Örnek.** $|x - 2| + |y + 3| = 0$ ise $x + y$ kaçtır?

Her mutlak değer en az $0$'dır. Negatif olmayan iki sayının toplamı $0$ ise ikisi de $0$'dır: $x - 2 = 0$ ve $y + 3 = 0$. Buradan $x = 2$, $y = -3$ ve $x + y = -1$.

**Kural.** $|A| + |B| = 0 \iff A = 0$ ve $B = 0$.

## Değişken dışarıda da varsa: kontrol şart

**Örnek.** $|x - 4| = 2x + 1$ denklemini çöz.

Sağ taraf artık sabit değil; yine iki durum yazılır:

- $x - 4 = 2x + 1 \Rightarrow x = -5$
- $x - 4 = -(2x + 1) \Rightarrow x - 4 = -2x - 1 \Rightarrow 3x = 3 \Rightarrow x = 1$

Şimdi **ilk denklemde** dene:

| Kök | Sol: $\lvert x - 4\rvert$ | Sağ: $2x + 1$ | Sonuç |
|---|---|---|---|
| $x = -5$ | $\lvert -9\rvert = 9$ | $-9$ | Sağlamaz |
| $x = 1$ | $\lvert -3\rvert = 3$ | $3$ | Sağlar |

$x = -5$ için sağ taraf negatif çıktı; bir mutlak değer $-9$'a eşit olamaz. Çözüm kümesi $\{1\}$.

**Kural.** $|A| = B$ denkleminde $B$ değişken içeriyorsa kökleri bul, sonra her kök için $B \ge 0$ olup olmadığına bak (ya da ilk denklemde yerine koy). Sağlamayanı at.

![Karar şeması: mutlak değer eşittir sağ taraf. Sağ taraf negatif sabitse çözüm kümesi boş. Değilse iki durum yaz. x dışarıda yoksa iki kök de geçerli; varsa her kökü yerine koy ve sağlamayanı at.](gorsel/tyt-matematik/03-08-yontem.svg "Mutlak değerli her denklemde aynı yol: önce sağ tarafın işaretine, sonra x'in dışarıda olup olmadığına bak.")

## |x − a| < c: merkeze yakın olanlar

**Örnek.** $|x - 3| < 5$ eşitsizliğini sağlayan kaç tam sayı vardır?

"$3$'e uzaklığı $5$'ten az" demek: $x$, $-2$ ile $8$ **arasında**dır.

$$-5 < x - 3 < 5 \Rightarrow -2 < x < 8$$

Tam sayılar $-1, 0, 1, \dots, 7$; toplam $8 - (-2) - 1 = 9$ tane.

**İçinde katsayı varsa:** $|2x + 1| \le 7 \Rightarrow -7 \le 2x + 1 \le 7 \Rightarrow -8 \le 2x \le 6 \Rightarrow -4 \le x \le 3$. Çift eşitsizlikte her işlemi **üç tarafa birden** yap.

**Kural.** $c > 0$ için $|A| < c \iff -c < A < c$ ve $|A| \le c \iff -c \le A \le c$. Çözüm **tek parça**, bir aralıktır.

## |x − a| > c: merkezden uzak olanlar

**Örnek.** $|x - 3| > 5$ eşitsizliğini çöz.

"$3$'e uzaklığı $5$'ten fazla" demek: $x$, $-2$'nin solunda ya da $8$'in sağındadır.

$$x - 3 < -5 \Rightarrow x < -2 \qquad\text{veya}\qquad x - 3 > 5 \Rightarrow x > 8$$

Çözüm kümesi $(-\infty, -2) \cup (8, \infty)$.

![İki sayı doğrusu alt alta, ikisinde de merkez 3, sınırlar −2 ve 8 boş nokta. Üstte |x − 3| küçüktür 5: −2 ile 8 arası yeşil boyalı. Altta |x − 3| büyüktür 5: −2'den sola ve 8'den sağa kırmızı oklar.](gorsel/tyt-matematik/03-08-ic-dis.svg "Aynı iki sınır, iki zıt cevap. Küçüktür içeriyi, büyüktür dışarıyı verir.")

**Kural.** $c > 0$ için $|A| > c \iff A < -c$ veya $A > c$. Çözüm **iki parça**dır; ortadaki bölge çözüm değildir.

Sağ taraf negatif ya da sıfırsa ezber yerine "uzaklık" diye düşün:

| Eşitsizlik | Çözüm kümesi | Neden? |
|---|---|---|
| $\lvert x\rvert < 0$ ya da $\lvert x\rvert < -2$ | $\varnothing$ | Uzaklık $0$'dan küçük olamaz |
| $\lvert x\rvert \le 0$ | $\{0\}$ | Yalnız $\lvert 0\rvert = 0$ |
| $\lvert x\rvert \ge 0$ ya da $\lvert x\rvert > -2$ | $\mathbb{R}$ | Her uzaklık bunu sağlar |
| $\lvert x\rvert > 0$ | $\mathbb{R} \setminus \{0\}$ | Yalnız $0$ sağlamaz |

## a ≤ |x − m| < b: iki parçalı bölge

**Örnek.** $2 \le |x - 1| < 5$ eşitsizliğini sağlayan kaç tam sayı vardır?

$x$'in $1$'e uzaklığı en az $2$, $5$'ten az. Merkezin iki yanında birer parça oluşur:

- Sağ parça: $2 \le x - 1 < 5 \Rightarrow 3 \le x < 6$
- Sol parça: $-5 < x - 1 \le -2 \Rightarrow -4 < x \le -1$

![Sayı doğrusu, merkez 1. Sol parça −4 boş noktadan −1 dolu noktaya, sağ parça 3 dolu noktadan 6 boş noktaya kadar mavi boyalı.](gorsel/tyt-matematik/03-08-halka.svg "Merkezin iki yanında simetrik iki parça. Uç noktaların durumu da simetrik: ≤ olan taraf dolu, < olan taraf boş.")

Tam sayılar: $3, 4, 5$ ve $-3, -2, -1$; toplam **6** tane.

**Kural.** $0 \le a < b$ için $a \le |A| \le b \iff a \le A \le b$ veya $-b \le A \le -a$. Sol parçada sınırların yeri değişir: $-b$ sola, $-a$ sağa yazılır.

## ÖSYM tuzakları

> **Negatif sağ tarafı görmemek:** $|3x - 2| + 5 = 1$ denkleminde önce $|3x - 2| = -4$ yaz. Mutlak değer negatif olamaz, çözüm kümesi boştur. İki durumu çözüp "kök" bulmak yanlıştır.

> **Kontrolü atlamak:** $|x - 4| = 2x + 1$ denkleminde iki durumdan $-5$ ve $1$ çıkar, ama $-5$ denklemi sağlamaz. Değişken mutlak değerin dışındaysa her kökü yerine koy.

> **Eksiyi yarım dağıtmak:** $|x - 1| = |2x + 4|$ için ikinci durum $x - 1 = -2x - 4$'tür; $x - 1 = -2x + 4$ yazan yanlış kök bulur.

> **Küçüktür ile büyüktürü karıştırmak:** $|x - 3| > 5$ için $-2 < x < 8$ yazmak en sık hatadır. Küçüktür içeriyi (tek parça), büyüktür dışarıyı (iki parça) verir.

> **Katsayıyı unutmak:** $|2x - 4| \le 6$ için merkez $4$ değil $2$'dir. Doğrusu: $-6 \le 2x - 4 \le 6 \Rightarrow -2 \le 2x \le 10 \Rightarrow -1 \le x \le 5$. İfadeyi $|x - 4| \le 6$ gibi okuyan $-2 \le x \le 10$ bulur.

## Kendini dene

### Soru 1
$|2x - 3| = 7$ denkleminin köklerinin toplamı kaçtır?

A) $-10$
B) $-2$
C) $0$
D) $3$
E) $5$

**Cevap:** D
**Çözüm:** $2x - 3 = 7 \Rightarrow x = 5$; $2x - 3 = -7 \Rightarrow x = -2$. Toplam $5 + (-2) = 3$. $-10$ köklerin çarpımıdır; $5$ ve $-2$ yalnızca birer köktür.

### Soru 2
$|x + 2| < 4$ eşitsizliğini sağlayan kaç tam sayı vardır?

A) 6
B) 7
C) 8
D) 9
E) 10

**Cevap:** B
**Çözüm:** $-4 < x + 2 < 4 \Rightarrow -6 < x < 2$. Tam sayılar $-5, -4, -3, -2, -1, 0, 1$; toplam 7. Uçları da sayan $-6$ ve $2$'yi ekleyip 9 bulur.

### Soru 3
$|x - 1| = 3x - 5$ denkleminin çözüm kümesi aşağıdakilerden hangisidir?

A) $\varnothing$
B) $\left\{\frac{3}{2}\right\}$
C) $\{2\}$
D) $\left\{\frac{3}{2}, 2\right\}$
E) $\{-2, 2\}$

**Cevap:** C
**Çözüm:** $x - 1 = 3x - 5 \Rightarrow x = 2$. $x - 1 = -(3x - 5) \Rightarrow 4x = 6 \Rightarrow x = \frac{3}{2}$. Kontrol: $x = 2$ için $|1| = 1$ ve $3 \cdot 2 - 5 = 1$, sağlar. $x = \frac{3}{2}$ için sağ taraf $\frac{9}{2} - 5 = -\frac{1}{2}$, negatif; sağlamaz. Çözüm kümesi $\{2\}$. D seçeneği kontrolü atlamanın sonucudur.

## Özet kartı

- $|x - a|$ = $x$'in $a$'ya uzaklığı. Denklem ve eşitsizlikleri önce bu gözle oku.
- $|A| = c$: $c > 0$ ise $A = \pm c$; $c = 0$ ise $A = 0$; $c < 0$ ise $\varnothing$.
- $|A| = |B| \iff A = \pm B$; $|A| + |B| = 0 \iff A = B = 0$.
- Değişken mutlak değerin dışında da varsa bulduğun her kökü ilk denklemde kontrol et.
- $|A| < c \iff -c < A < c$ (tek parça); $|A| > c \iff A < -c$ veya $A > c$ (iki parça).
- $a \le |A| \le b$: merkezin iki yanında simetrik iki parça.

## Sonraki adım

Alıştırmaya geç (aşağıdaki düğme). Bu ders "Birinci Dereceden Denklemler ve Eşitsizlikler" konusunun sonuncusu. Sonraki ders **Üslü İfadeler ve Özellikleri**; orada da $(-2)^2$ ile $-2^2$ farkı gibi işaret tuzakları seni bekliyor.
