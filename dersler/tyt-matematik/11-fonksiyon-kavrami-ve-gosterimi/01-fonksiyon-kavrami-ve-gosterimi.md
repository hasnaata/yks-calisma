---
baslik: Fonksiyon Kavramı ve Gösterimi
ders: tyt-matematik
sure: 20 dk
kaynak: MEBİ Konu Özeti 7cc0376018
guncelleme: 2026-11-18
---
# Fonksiyon Kavramı ve Gösterimi

<div class="giris" dir="rtl" lang="ar">

**الدرس ده عن إيه؟** عن الدالة (fonksiyon): إمتى الربط بين مجموعتين يتسمّى دالة، وإزاي تكتبها وتقراها بأكتر من طريقة.

- هتعرف تحكم على أي ربط (eşleme) هل هو دالة ولا لأ: كل عنصر في المجموعة الأولى لازم يطلع منه سهم واحد بس.
- هتفرّق بين المجال (tanım kümesi) والمجال المقابل (değer kümesi) والمدى (görüntü kümesi).
- هتتعلم تحسب كام دالة ممكن تتعرّف من مجموعة لمجموعة، وتلاقي المجهول لما الدالة تكون مكتوبة كأزواج مرتبة (sıralı ikililer).

**ليه مهم؟** أغلب أسئلة الدوال في TYT مبنية على الكتابة والمصطلحات دي، وأسئلة زي «أنهي واحدة دالة؟» و«كام دالة ممكن تتعرّف؟» بتيجي من الدرس ده على طول.

هما ٢٠ دقيقة بس، ورسومات الأسهم هتخلّي الفكرة واضحة قدامك. يلا نبدأ.

</div>

**Bu dersin sonunda:** bir eşlemenin fonksiyon olup olmadığına karar verebilecek, tanım, değer ve görüntü kümesini ayırabilecek ve iki küme arasında kaç fonksiyon yazılabileceğini hesaplayabileceksin.

> **TYT'de yeri:** Fonksiyon sorularının neredeyse hepsi $f(x)$ gösterimini bilmeni ister. Bu dersten doğrudan gelen kalıplar: "hangisi bir fonksiyondur?", "görüntü kümesinin eleman sayısı kaçtır?", "sıralı ikililerden oluşan bu küme fonksiyon olduğuna göre $a$ kaçtır?" ve "A'dan B'ye kaç fonksiyon tanımlanabilir?".

## Önce hatırla

<details><summary>Olasılık uygulamalarından: Bir torbada 3 kırmızı ve 5 mavi bilye var. Rastgele çekilen bir bilyenin mavi olma olasılığı kaçtır?</summary>
Örnek uzayda $3 + 5 = 8$ bilye, istenen olayda 5 bilye var: $P = \frac{5}{8}$.
</details>

<details><summary>Olasılık uygulamalarından: Bir zar atılıyor. Gelen sayının asal ya da çift olma olasılığı kaçtır?</summary>
Asallar $\{2, 3, 5\}$, çiftler $\{2, 4, 6\}$. İki olay ayrık değil, ortak eleman 2: $P = \frac{3}{6} + \frac{3}{6} - \frac{1}{6} = \frac{5}{6}$. Kontrol: birleşim $\{2, 3, 4, 5, 6\}$, 5 eleman.
</details>

## Fonksiyon nedir?

**Örnek.** $A = \{1, 2, 3, 4\}$ ve $B = \{0, 1, 2\}$ olsun. $A$'daki her sayıyı, **3'e bölümünden kalana** eşleyelim: $1 \to 1$, $2 \to 2$, $3 \to 0$, $4 \to 1$.

$A$'nın her elemanından **bir ve yalnız bir** ok çıkıyor. Bu eşleme bir fonksiyondur. $B$'deki 1'e iki ok gelmesi sorun değildir.

Şimdi okları ters çevir ($B$'den $A$'ya): $1$'den hem $1$'e hem $4$'e ok çıkar. Bir eleman iki yere gidiyor; bu eşleme fonksiyon **değildir**.

![Üç ok şeması yan yana. Birincide A'dan B'ye her elemandan bir ok çıkıyor. İkincide B'den A'ya, 1'den iki ok çıkıyor. Üçüncüde A'dan B'ye, 4'ten ok çıkmıyor.](gorsel/tyt-matematik/11-01-eslesme.svg "Yalnızca soldaki kümeye bak: her elemandan tam bir ok çıkmalı. Sağdaki kümede boşta kalan ya da iki ok alan eleman olabilir.")

**Kural.** $A$ ve $B$ boş olmayan iki küme olsun. $A$'nın **her** elemanını $B$'nin **bir ve yalnız bir** elemanına eşleyen kurala $A$'dan $B$'ye **fonksiyon** denir. İki koşul var:

1. $A$'da boşta eleman kalmaz.
2. $A$'nın hiçbir elemanı iki farklı elemana gitmez.

![Karar şeması: A'dan B'ye bağıntı; her elemandan ok çıkıyor mu? Hayırsa fonksiyon değil. Evetse hepsinden yalnız bir ok mu? Evetse fonksiyondur, hayırsa fonksiyon değil.](gorsel/tyt-matematik/11-01-karar.svg "İki soru sor, ikisine de evet cevabı gelirse fonksiyondur.")

## Gösterim: $f\colon A \to B$ ve $y = f(x)$

**Örnek.** $A = \{-1, 0, 1, 2\}$ kümesinin her elemanını karesine eşleyen fonksiyona $f$ diyelim. Aynı fonksiyonu dört yolla yazabilirsin:

| Gösterim | Yazılışı |
|---|---|
| Kural | $f(x) = x^2$ |
| Sıralı ikililer | $f = \{(-1, 1),\ (0, 0),\ (1, 1),\ (2, 4)\}$ |
| Tablo | $x$: $-1, 0, 1, 2$ için $f(x)$: $1, 0, 1, 4$ |
| Ok şeması | aşağıdaki şekil |

Fonksiyonlar $f$, $g$, $h$ gibi küçük harflerle adlandırılır. $A$'dan $B$'ye tanımlı $f$ fonksiyonu $f\colon A \to B$ diye yazılır.

$(x, y) \in f$ ise $y = f(x)$ yazılır ve "$f$ fonksiyonu $x$'i $y$'ye götürür" diye okunur. Örnekte $(2, 4) \in f$, yani $f(2) = 4$.

- $x$: **bağımsız değişken** (seçtiğin eleman).
- $y = f(x)$: **bağımlı değişken** (seçtiğin $x$'e bağlı olarak belli olur). $f(x)$'e $x$'in **görüntüsü** denir.

Sıralı ikilide sıra önemlidir: $(2, 4)$ "2, 4'e gider" demektir; $(4, 2)$ başka bir eşlemedir.

## Tanım, değer ve görüntü kümesi

**Örnek.** Yukarıdaki fonksiyonu $f\colon A \to B$, $B = \{0, 1, 2, 3, 4\}$ olarak düşün.

![Ok şeması: A kümesinde −1, 0, 1, 2; B kümesinde 0, 1, 4 yeşil bir iç bölgede, 2 ve 3 dışarıda. Oklar: −1 ve 1'den 1'e, 0'dan 0'a, 2'den 4'e.](gorsel/tyt-matematik/11-01-kumeler.svg "Görüntü kümesi, ok gelen elemanlardan oluşur. 2 ve 3 değer kümesinde ama görüntü kümesinde değil.")

| Küme | Ne? | Örnekte |
|---|---|---|
| Tanım kümesi | Okların çıktığı küme, $A$ | $\{-1, 0, 1, 2\}$ |
| Değer kümesi | Okların gidebileceği küme, $B$ | $\{0, 1, 2, 3, 4\}$ |
| Görüntü kümesi | Gerçekten ok gelen elemanlar, $f(A)$ | $\{0, 1, 4\}$ |

**Kural.** Görüntü kümesi her zaman değer kümesinin alt kümesidir: $f(A) \subseteq B$. Görüntü kümesinde aynı eleman bir kez yazılır; $f(-1) = f(1) = 1$ olsa da $1$ bir kez sayılır. Bu yüzden $s(f(A)) \le s(A)$ olur.

## Sıralı ikililerden fonksiyon mu?

**Örnek.** $A = \{1, 2, 3\}$ olmak üzere $f = \{(1, 4),\ (2, a + 3),\ (3, 6),\ (2, 9)\}$ kümesi $A$'dan bir fonksiyondur. $a$ kaçtır?

$2$ iki ikilide birinci bileşen. Fonksiyonda $2$'nin tek görüntüsü olmalı, yani iki ikili aslında **aynı** ikilidir: $a + 3 = 9$, $a = 6$.

**Kural.** Sıralı ikililerle verilen bağıntıda:

- $A$'nın her elemanı en az bir ikilide **birinci bileşen** olmalı.
- Aynı birinci bileşen tekrar ediyorsa ikinci bileşenler **eşit** olmalı.

## A'dan B'ye kaç fonksiyon yazılır?

**Örnek.** $A = \{a, b\}$ ve $B = \{1, 2, 3\}$ ise $A$'dan $B$'ye kaç fonksiyon tanımlanabilir?

Her fonksiyon, $f(a)$ ve $f(b)$ değerlerinin seçimiyle belli olur. $f(a)$ için 3 seçenek, $f(b)$ için 3 seçenek: $3 \cdot 3 = 9$.

![Üç satır üç sütunluk tablo: satırlar f(a) = 1, 2, 3; sütunlar f(b) = 1, 2, 3. Her kutuda bir fonksiyon, toplam 9. İlk satır yeşil.](gorsel/tyt-matematik/11-01-sayma.svg "Her kutu bir fonksiyon. Yeşil satır f(a) = 1 koşulunu sağlayan 3 fonksiyondur.")

**Kural.** $s(A) = m$ ve $s(B) = n$ ise $A$'dan $B$'ye tanımlanabilecek fonksiyon sayısı

$$n^m$$

olur. Üs, **tanım kümesinin** eleman sayısıdır; çünkü seçim tanım kümesindeki her eleman için ayrı ayrı yapılır.

Koşul varsa yalnızca serbest elemanları say. Örnekte $f(a) = 1$ istenirse $a$'nın seçimi sabittir, yalnızca $b$ seçilir: $3^1 = 3$ fonksiyon (şekildeki yeşil satır).

## ÖSYM tuzakları

> **Üssü ters koymak:** $s(A) = 3$, $s(B) = 4$ ise $A$'dan $B$'ye $4^3 = 64$ fonksiyon vardır, $3^4 = 81$ değil. Taban değer kümesi, üs tanım kümesidir.

> **Değer kümesi ile görüntü kümesini karıştırmak:** "Görüntü kümesi" sorulduğunda yalnızca ok gelen elemanları yaz. $B$'nin tamamı değer kümesidir.

> **"Sağda iki ok gelirse fonksiyon olmaz" sanmak:** $f(1) = f(3)$ olabilir. Yasak olan, **soldaki** bir elemandan iki ok çıkmasıdır.

> **Görüntüleri tekrarlı saymak:** $f(-1) = 1$ ve $f(1) = 1$ ise görüntü kümesinde $1$ bir kez yazılır. Eleman sayısını sorarken tekrarları ayıkla.

> **Boşta kalan tanım elemanını görmemek:** $A = \{1, 2, 3\}$ iken $\{(1, 5), (2, 6)\}$ fonksiyon değildir; $3$'ün görüntüsü yok.

## Kendini dene

### Soru 1
$f\colon \{1, 2, 3\} \to \{4, 5, 6\}$ fonksiyonu $f = \{(1, 5),\ (2, 5),\ (3, 4)\}$ biçimindedir. $f$'nin görüntü kümesi aşağıdakilerden hangisidir?

A) $\{4\}$
B) $\{4, 5\}$
C) $\{5, 6\}$
D) $\{4, 5, 6\}$
E) $\{1, 2, 3\}$

**Cevap:** B
**Çözüm:** Görüntüler $f(1) = 5$, $f(2) = 5$, $f(3) = 4$. Ok gelen elemanlar $4$ ve $5$: $f(A) = \{4, 5\}$. $5$ bir kez yazılır. $\{4, 5, 6\}$ değer kümesi, $\{1, 2, 3\}$ tanım kümesidir.

### Soru 2
$s(A) = 2$ ve $s(B) = 5$ olduğuna göre $A$'dan $B$'ye kaç fonksiyon tanımlanabilir?

A) 7
B) 10
C) 25
D) 32
E) 120

**Cevap:** C
**Çözüm:** $A$'nın 2 elemanının her biri için 5 seçenek var: $5^2 = 25$. Üssü ters koyan $2^5 = 32$, toplayan $7$, çarpan $10$ bulur.

### Soru 3
$A = \{-2, 0, 1\}$ olmak üzere $f\colon A \to \mathbb{R}$, $f(x) = 2x + 3$ fonksiyonunun görüntü kümesindeki elemanların toplamı kaçtır?

A) $-1$
B) $1$
C) $5$
D) $7$
E) $9$

**Cevap:** D
**Çözüm:** $f(-2) = -4 + 3 = -1$, $f(0) = 3$, $f(1) = 5$. Görüntü kümesi $\{-1, 3, 5\}$, toplam $-1 + 3 + 5 = 7$. $-1$, tanım kümesinin elemanlarının toplamıdır ($-2 + 0 + 1$).

## Özet kartı

- Fonksiyon: tanım kümesinin **her** elemanından **tam bir** ok.
- $(x, y) \in f \iff y = f(x)$; $x$ bağımsız, $y$ bağımlı değişken.
- $f\colon A \to B$: $A$ tanım, $B$ değer, $f(A)$ görüntü kümesi; $f(A) \subseteq B$.
- Sıralı ikililerde aynı birinci bileşen tekrar ederse ikinci bileşenler eşit olmalı.
- $s(A) = m$, $s(B) = n$ ise $A$'dan $B$'ye $n^m$ fonksiyon.
- Koşullu saymada sabit elemanları çıkar, serbest elemanlar için seçenekleri çarp.

## Sonraki adım

Alıştırmaya geç (aşağıdaki düğme). Sonraki ders **Fonksiyon Soruları**; $f(x)$ kuralıyla değer bulma, $f(2x - 1)$ gibi ifadelerle çalışma burada öğrendiğin gösterime dayanır.
