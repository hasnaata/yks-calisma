---
baslik: Önermeler
ders: tyt-matematik
sure: 20 dk
kaynak: MEBİ Konu Özeti 417f2eca34
guncelleme: 2026-11-18
---
# Önermeler

<div class="giris" dir="rtl" lang="ar">

**الدرس ده عن إيه؟** عن أول خطوة في المنطق: القضية المنطقية (önerme)، يعني الجملة اللي تقدر تقول عليها صح أو غلط بشكل أكيد.

- هتعرف تفرّق القضية عن غيرها: السؤال والأمر والتمنّي والرأي الشخصي مش قضايا، لكن الجملة الغلط بتفضل قضية برضه.
- هتكتب قيمة الصواب (doğruluk değeri) لكل قضية، 1 أو 0، وتعرف إمتى قضيتين يبقوا متكافئين (denk).
- هتبني جدول الصواب (doğruluk tablosu) وتعرف عدد صفوفه، وتكتب نفي القضية (değil) صح.

**ليه مهم؟** أسئلة المنطق في TYT كلها قايمة على الأساسيات دي، وأشهر غلطة إن نفي "أكبر من" يتكتب "أصغر من" بدل "أصغر من أو يساوي".

هما ٢٠ دقيقة بس، وده أساس بسيط هتبني عليه الدرس الجاي على طول.

</div>

**Bu dersin sonunda:** bir ifadenin önerme olup olmadığına karar verebilecek, önermelerin doğruluk değerini ve denkliğini yazabilecek, $n$ önermenin doğruluk tablosunu kurabilecek ve bir önermenin değilini doğru söyleyebileceksin.

> **TYT'de yeri:** Mantık soruları genellikle bileşik önermeler üzerinden gelir; ama hepsi bu dersteki üç temele dayanır: "Hangisi önermedir?", "$p \equiv 0$ ise $p'$ nedir?" ve "doğruluk tablosu kaç satırdır?". En çok yapılan hata, "büyüktür" ifadesinin değilini "küçüktür" sanmaktır.

## Önce hatırla

<details><summary>Rutin olmayan problemlerden: x ve y pozitif tam sayılar ve 2x + 3y = 31 olduğuna göre x + y en çok kaçtır?</summary>
Toplamın büyük olması için katsayısı büyük olan $y$ küçük seçilmeli. $2x = 31 - 3y$ çift olmalı, yani $y$ tek olmalı. En küçük değer $y = 1$: $2x = 28$, $x = 14$. Sonuç $x + y = 15$. Sistematik deneme: en uç değerden başla, koşulu kontrol et.
</details>

<details><summary>Rutin olmayan problemlerden: Bir cihaz saat 10.00.00'dan başlayarak 40 saniyede bir sinyal veriyor. 10.00 ile 10.10 arasında (ikisi de dahil) kaç sinyal tam dakika başında verilir?</summary>
Sinyaller 0, 40, 80, 120… saniyede gelir. Dakika başı, 60'ın katı demektir. 40 ile 60'ın ortak katı $\text{EKOK}(40, 60) = 120$ saniye, yani 2 dakikada bir. Liste: 10.00, 10.02, 10.04, 10.06, 10.08, 10.10. Toplam <b>6</b>.
</details>

## Önerme nedir?

**Örnek.** Aşağıdaki ifadelere bak:

| İfade | Önerme mi? | Neden? |
|---|---|---|
| "Ankara, Türkiye'nin başkentidir." | Evet | Kesin hüküm, doğru. |
| "$13 + 5 = 16$" | Evet | Kesin hüküm, **yanlış**. Yanlış olması önerme olmasını engellemez. |
| "Yarın sinemaya gelir misin?" | Hayır | Soru; hüküm bildirmiyor. |
| "Pencereyi kapat." | Hayır | Emir. |
| "Keşke tatil uzun olsa." | Hayır | Dilek. |
| "En güzel renk mavidir." | Hayır | Doğruluğu kişiden kişiye değişir. |

Doğru ya da yanlış olduğu **kesin** olarak söylenebilen hüküm cümlesine **önerme** denir. Önermeler $p, q, r, s$ gibi küçük harflerle adlandırılır: $p$: "Ankara, Türkiye'nin başkentidir."

![Akış şeması: bir ifade için önce hüküm bildirip bildirmediğine bakılır; soru, emir ve dilek önerme değildir. Hüküm bildiriyorsa doğruluğunun kişiye göre değişip değişmediğine bakılır; değişiyorsa önerme değildir, değişmiyorsa önermedir.](gorsel/tyt-matematik/06-01-onerme-mi.svg "İki soru sor: Hüküm var mı? Herkes için aynı cevap mı? İkisinden de geçen ifade önermedir.")

**Kural.** Önerme olmak için iki koşul yeter: hüküm bildirmek ve doğru mu yanlış mı olduğu kişiye göre değişmemek. Önermenin doğru olması **gerekmez**.

Not: "$x + 3 = 7$" gibi bir ifadenin doğruluğu $x$'e bağlıdır; $x$ bilinmeden doğru ya da yanlış denemez. Bunlara **açık önerme** denir, Niceleyiciler dersinde göreceksin.

## Doğruluk değeri ve denklik

**Örnek.** $p$: "$2^4 = 16$", $q$: "7 bir asal sayıdır", $r$: "$-3^2 = 9$".

- $p$ doğrudur: $p \equiv 1$.
- $q$ doğrudur: $q \equiv 1$.
- $r$ yanlıştır, çünkü üs yalnızca 3'e etki eder: $-3^2 = -9$. Yani $r \equiv 0$.

$p$ ile $q$ bambaşka konulardan söz eder, ama ikisinin de doğruluk değeri 1'dir. Bu yüzden $p \equiv q$ yazılır. $p$ ile $r$'nin değerleri farklıdır: $p \not\equiv r$.

**Kural.**

- Bir önerme doğruysa doğruluk değeri **1** (D), yanlışsa **0** (Y) olur: $p \equiv 1$ ya da $p \equiv 0$.
- Doğruluk değerleri aynı olan iki önerme **denktir**: $p \equiv q$. Değerleri farklıysa $p \not\equiv q$.
- Denklik anlamla ilgili değildir; yalnızca 1 ve 0'a bakılır. İki yanlış önerme de birbirine denktir.

## Doğruluk tablosu

**Örnek.** $p$, $q$ ve $r$ önermelerinin her biri 1 ya da 0 olabilir. Kaç farklı durum vardır?

$p$ için 2 seçenek var. Her biri için $q$'nun 2 seçeneği, her biri için de $r$'nin 2 seçeneği var. Ağaçla saydığında:

![Ağaç şeması: bir noktadan p için 1 ve 0 dalları, her dal q için ikiye, her biri r için yine ikiye ayrılıyor. Sağda 8 satır: 111, 110, 101, 100, 011, 010, 001, 000.](gorsel/tyt-matematik/06-01-dogruluk-agaci.svg "Her yeni önerme satır sayısını ikiye katlar. Sağdaki sütunlara bak: r birer, q ikişer, p dörder değişiyor.")

$2 \cdot 2 \cdot 2 = 8$ durum vardır. Bu durumların listelendiği tabloya **doğruluk tablosu** denir.

| Önerme sayısı | 1 | 2 | 3 | 4 | 5 | $n$ |
|---|---|---|---|---|---|---|
| Satır sayısı | 2 | 4 | 8 | 16 | 32 | $2^n$ |

**Kural.** Birbirinden bağımsız $n$ önermenin doğruluk tablosunda $2^n$ satır vardır. Tabloyu düzenli kurmak için son sütun 1, 0, 1, 0…; bir öncekinde ikişer; ondan öncekinde dörder 1 ve 0 yazılır. İlk sütunda üst yarı 1, alt yarı 0'dır.

Önermeler bağımsız değilse satır sayısı azalır. Örneğin $q \equiv p$ olduğu biliniyorsa $q$ yeni bir seçenek getirmez: $p$, $q$, $r$ için yalnızca $2 \cdot 1 \cdot 2 = 4$ durum kalır.

## Bir önermenin değili

**Örnek 1.** $p$: "15 bir tek sayıdır." Bu önerme doğrudur: $p \equiv 1$.

Hükmü olumsuz yaparsak: $p'$: "15 bir tek sayı değildir." Bu önerme yanlıştır: $p' \equiv 0$.

**Örnek 2.** Bir $a$ gerçek sayısı için $p$: "$a > 3$" olsun. $p$ yanlışsa $a$ nerede olabilir?

![İki sayı doğrusu. Üstte p: a büyüktür 3, 3'te boş nokta ve sağa doğru boyalı. Altta p üssü: a küçük eşittir 3, 3'te dolu nokta ve sola doğru boyalı.](gorsel/tyt-matematik/06-01-degil-sayi-dogrusu.svg "İki önerme sayı doğrusunu tam olarak ikiye böler. 3 sayısı p'de yok, bu yüzden p üssünde var.")

$a > 3$ olmayan her sayı, $3$'ün kendisi dahil, $3$'ün solundadır. Değil: $p'$: "$a \le 3$". "$a < 3$" yazarsan $a = 3$ durumunu kaybedersin.

**Kural.**

- Bir önermenin hükmü olumsuz yapılarak elde edilen önermeye onun **değili** (olumsuzu) denir; $p'$ ya da $\sim p$ ile gösterilir.
- $p \equiv 1$ ise $p' \equiv 0$; $p \equiv 0$ ise $p' \equiv 1$. Bir önerme ile değili hiçbir zaman denk değildir.
- Değilin değili önermenin kendisidir: $(p')' \equiv p$.

| $p$ | $p'$ | $(p')'$ |
|---|---|---|
| 1 | 0 | 1 |
| 0 | 1 | 0 |

| Önerme | Değili |
|---|---|
| $a > b$ | $a \le b$ |
| $a < b$ | $a \ge b$ |
| $a = b$ | $a \ne b$ |
| "$n$ tektir" | "$n$ tek değildir" ($n$ tam sayıysa: "$n$ çifttir") |

Çok sayıda değil işareti görürsen say: **çift** sayıda üs varsa sonuç $p$, **tek** sayıda varsa $p'$ olur. Örneğin $(((p')')')' \equiv p$ (4 üs), $((p')')' \equiv p'$ (3 üs).

## ÖSYM tuzakları

> **Yanlış önermeyi "önerme değil" saymak:** "$13 + 5 = 16$" yanlıştır ama önermedir. Önerme olmak için doğru olmak gerekmez, kesin hüküm bildirmek yeter.

> **Kişisel görüşü önerme sanmak:** "Matematik en zevkli derstir." bir hüküm cümlesidir ama doğruluğu kişiye göre değişir; önerme değildir.

> **Büyüğün değilini küçük yazmak:** "$a > 3$" önermesinin değili "$a < 3$" değil, "$a \le 3$" olur. Eşitlik durumu değile geçer.

> **Denkliği anlamda aramak:** "$2^4 = 16$" ile "7 asaldır" önermelerinin konuları farklıdır, ama ikisi de 1 olduğu için denktir.

> **Üs sayımını karıştırmak:** $((p')')'$ ifadesinde 3 üs vardır, sonuç $p'$'dür. Üsleri tek tek say.

## Kendini dene

### Soru 1
Aşağıdakilerden hangisi bir önerme **değildir**?

A) 5 bir tek sayıdır.
B) Ankara, Türkiye'nin başkentidir.
C) Bu film çok sıkıcıdır.
D) 4 sayısı 9'dan büyüktür.
E) Bir yılda 12 ay vardır.

**Cevap:** C
**Çözüm:** A, B ve E doğru; D yanlış, ama dördü de kesin hüküm bildirir, yani önermedir. "Bu film çok sıkıcıdır." ifadesinin doğruluğu izleyene göre değişir; önerme değildir.

### Soru 2
Birbirinden bağımsız 5 önermenin doğruluk tablosunda kaç satır vardır?

A) 10
B) 16
C) 25
D) 32
E) 64

**Cevap:** D
**Çözüm:** Her önerme 1 ya da 0 olabilir: $2 \cdot 2 \cdot 2 \cdot 2 \cdot 2 = 2^5 = 32$. $2 \cdot 5 = 10$ ya da $5^2 = 25$ işlemleri yanlıştır; 16 dört, 64 altı önermenin satır sayısıdır.

### Soru 3
$p$: "$3 \cdot 4 - 5 > 8$" önermesi için aşağıdakilerden hangisi doğrudur?

A) $p \equiv 1$
B) $((p')')' \equiv 1$
C) $(p')' \equiv 1$
D) $p' \equiv 0$
E) $p \equiv p'$

**Cevap:** B
**Çözüm:** $3 \cdot 4 - 5 = 7$ ve $7 > 8$ yanlıştır: $p \equiv 0$. Buradan $p' \equiv 1$, $(p')' \equiv p \equiv 0$ ve $((p')')' \equiv p' \equiv 1$ olur. A, C ve D bu değerlerle çelişir; bir önerme değiline hiçbir zaman denk olmadığı için E de yanlıştır.

## Özet kartı

- Önerme: doğru ya da yanlış olduğu kesin olan hüküm. Soru, emir, dilek ve kişisel görüş önerme değildir.
- Doğru önerme $\equiv 1$, yanlış önerme $\equiv 0$. Değerleri aynı olan önermeler denktir.
- $n$ bağımsız önermenin doğruluk tablosunda $2^n$ satır vardır.
- $p \equiv 1 \Rightarrow p' \equiv 0$ ve tersi; $(p')' \equiv p$.
- "$>$" önermesinin değili "$\le$", "$<$" önermesinin değili "$\ge$" olur.
- Üs sayısı çiftse $p$, tekse $p'$.

## Sonraki adım

Alıştırmaya geç (aşağıdaki düğme). Sonraki ders **Bileşik Önermeler**; "ve", "veya" bağlaçlarıyla kurulan önermelerin değerini bu dersteki doğruluk tablosuyla bulacaksın.
