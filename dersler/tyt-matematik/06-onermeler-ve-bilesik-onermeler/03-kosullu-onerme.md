---
baslik: Koşullu Önerme
ders: tyt-matematik
sure: 20 dk
kaynak: MEBİ Konu Özeti 946d4f187e
guncelleme: 2026-11-17
---
# Koşullu Önerme

**Bu dersin sonunda:** $p \Rightarrow q$ önermesinin değerini bulabilecek, onu $p' \vee q$ biçimine çevirerek sadeleştirebilecek ve bir koşullu önermenin karşıtını, tersini, karşıt tersini birbirinden ayırabileceksin.

> **TYT'de yeri:** Mantık sorularının çoğunda "ise" bağlacı vardır. Üç kalıp sık gelir: "Bileşik önerme yanlış olduğuna göre $p$, $q$, $r$ nedir?", "Hangisi $p \Rightarrow q$ önermesine denktir?" ve günlük hayattan bir kuralın hangi durumda çiğnendiği. Hepsinin anahtarı tek bir satırdır: **$p \Rightarrow q$ yalnızca $1 \Rightarrow 0$ durumunda yanlıştır.**

## Önce hatırla

<details><summary>Bileşik önermelerden: p ≡ 1, q ≡ 0 ve r ≡ 0 ise (p ∨ q) ∧ r′ önermesinin doğruluk değeri nedir?</summary>
Önce parantez: $p \vee q \equiv 1 \vee 0 \equiv 1$ ("veya" için biri doğru yeter). Sonra $r' \equiv 1$. "Ve" için ikisi de doğru olmalı: $1 \wedge 1 \equiv 1$. Sonuç <b>1</b>.
</details>

<details><summary>Bileşik önermelerden: De Morgan kuralıyla (p ∧ q′)′ önermesinin denkini yaz.</summary>
De Morgan: "ve" ifadesinin değilinde her parça değillenir ve bağlaç "veya" olur. $(p \wedge q')' \equiv p' \vee (q')' \equiv p' \vee q$. Bu sonucu aklında tut: bu dersin en önemli denkliği bu.
</details>

## "İse" bağlacı: koşullu önerme

**Örnek.** Bir veli çocuğuna söz veriyor: "Sınavdan 90 alırsan sana bisiklet alırım."

- $p$: "Sınavdan 90 alırsın."
- $q$: "Sana bisiklet alırım."

Söz, $p$ ile $q$'nun "ise" ile bağlanmasıdır: $p \Rightarrow q$. Dört durum var. Hangisinde veli sözünü **bozmuş** olur?

![Dört satırlık tablo. p ve q birer, söz tutuldu, değer 1. p bir q sıfır, söz bozuldu, değer 0. p sıfır q bir, söz bozulmadı, değer 1. p sıfır q sıfır, söz bozulmadı, değer 1.](gorsel/tyt-matematik/06-03-soz-tablosu.svg "Kırmızı satır tek bozuk durumdur: koşul gerçekleşmiş, söz yerine gelmemiş. 90 alınmadıysa veli ne yaparsa yapsın sözünü bozmuş sayılmaz.")

Çocuk 90 almadıysa veli bisiklet alsa da almasa da söz çiğnenmiş olmaz; söz yalnızca "90 alırsan" durumu için verilmişti. Tek bozuk durum: 90 alındı, bisiklet alınmadı.

**Kural.** $p$ ile $q$'nun "ise" bağlacıyla bağlanmasıyla kurulan önermeye **koşullu önerme** denir ve $p \Rightarrow q$ ile gösterilir ("$p$ ise $q$" diye okunur).

| $p$ | $q$ | $p \Rightarrow q$ |
|---|---|---|
| 1 | 1 | 1 |
| 1 | 0 | **0** |
| 0 | 1 | 1 |
| 0 | 0 | 1 |

$p \Rightarrow q$ yalnızca **$p \equiv 1$, $q \equiv 0$** iken yanlıştır; diğer üç durumda doğrudur. Özellikle $p \equiv 0$ ise $q$ ne olursa olsun $p \Rightarrow q \equiv 1$ olur.

"İse" bağlacında sıra önemlidir: $p \equiv 1$, $q \equiv 0$ için $p \Rightarrow q \equiv 0$ ama $q \Rightarrow p \equiv 0 \Rightarrow 1 \equiv 1$. Yani genel olarak $p \Rightarrow q \not\equiv q \Rightarrow p$; "ise" bağlacının değişme özelliği yoktur.

## Önemli denklik: $p \Rightarrow q \equiv p' \vee q$

**Örnek.** $p \Rightarrow q$ ile $p' \vee q$ önermelerinin doğruluk tablosunu yan yana kuralım.

| $p$ | $q$ | $p'$ | $p' \vee q$ | $p \Rightarrow q$ |
|---|---|---|---|---|
| 1 | 1 | 0 | 1 | 1 |
| 1 | 0 | 0 | **0** | **0** |
| 0 | 1 | 1 | 1 | 1 |
| 0 | 0 | 1 | 1 | 1 |

Son iki sütun satır satır aynıdır. İkisi de yalnızca "$p$ doğru, $q$ yanlış" satırında 0 olur.

![Dikdörtgen içinde kesişen p ve q daireleri. Yalnızca p dairesinin q ile kesişmeyen kısmı kırmızı ve 0 yazılı; kesişim, yalnız q bölgesi ve iki dairenin dışı yeşil ve 1 yazılı.](gorsel/tyt-matematik/06-03-venn.svg "p ⇒ q yalnızca p olup q olmayan bölgede yanlıştır. Yeşil bölgelerin tamamı, p dışı ile q birleşimidir: p′ ∨ q.")

**Kural.** $$p \Rightarrow q \equiv p' \vee q$$

Bu denklik, "ise" içeren her ifadeyi "veya" ve "değil" ile yazmana, sonra Bileşik Önermeler dersindeki kurallarla sadeleştirmene izin verir. Değilini almak için De Morgan uygula:

$$(p \Rightarrow q)' \equiv (p' \vee q)' \equiv p \wedge q'$$

**Örnek (sadeleştirme).** $(p \wedge q) \Rightarrow p$ önermesinin denki nedir?

$$(p \wedge q) \Rightarrow p \equiv (p \wedge q)' \vee p \equiv p' \vee q' \vee p \equiv (p \vee p') \vee q' \equiv 1 \vee q' \equiv 1$$

Her durumda doğru olan bu tür önermeye **totoloji** denir.

### İse bağlacının özellikleri

Aşağıdakilerin hepsi $p \Rightarrow q \equiv p' \vee q$ denkliğinden bir satırda çıkar. Ezberleme, çıkar.

| Özellik | Neden? |
|---|---|
| $p \Rightarrow p \equiv 1$ | $p' \vee p \equiv 1$ |
| $p \Rightarrow 1 \equiv 1$ | $p' \vee 1 \equiv 1$ |
| $0 \Rightarrow p \equiv 1$ | $1 \vee p \equiv 1$ |
| $1 \Rightarrow p \equiv p$ | $0 \vee p \equiv p$ |
| $p \Rightarrow 0 \equiv p'$ | $p' \vee 0 \equiv p'$ |
| $p \Rightarrow p' \equiv p'$ | $p' \vee p' \equiv p'$ |

Kısaca: hüküm 1 ise ya da hipotez 0 ise sonuç kesin 1'dir.

## Değeri verilen önermeden $p$, $q$, $r$ bulmak

**Örnek.** $(p \Rightarrow q') \vee r \equiv 0$ olduğuna göre $p$, $q$, $r$ nedir?

1. "Veya" yanlışsa iki parça da yanlıştır: $p \Rightarrow q' \equiv 0$ ve $r \equiv 0$.
2. "İse" yanlışsa hipotez 1, hüküm 0'dır: $p \equiv 1$ ve $q' \equiv 0$, yani $q \equiv 1$.

Sonuç: $p \equiv 1$, $q \equiv 1$, $r \equiv 0$. Tek bir durum çıktı.

**Kural.** Bir koşullu önerme **yanlış** verilirse işin kolaydır: $p \Rightarrow q \equiv 0$ ise kesinlikle $p \equiv 1$, $q \equiv 0$. Önerme **doğru** verilirse üç durum vardır ($11$, $01$, $00$); başka bir bilgi gerekmeden $p$ ile $q$'yu bulamazsın.

## Karşıt, ters, karşıt ters

**Örnek.** Tam sayılar için şu önerme doğrudur: "Bir sayı 6'ya bölünüyorsa 3'e bölünür." ($p$: 6'ya bölünür, $q$: 3'e bölünür.)

| Ad | Simge | Cümle | Doğru mu? |
|---|---|---|---|
| Koşullu | $p \Rightarrow q$ | 6'ya bölünüyorsa 3'e bölünür. | Evet |
| Karşıtı | $q \Rightarrow p$ | 3'e bölünüyorsa 6'ya bölünür. | Hayır: 9 |
| Tersi | $p' \Rightarrow q'$ | 6'ya bölünmüyorsa 3'e bölünmez. | Hayır: 9 |
| Karşıt tersi | $q' \Rightarrow p'$ | 3'e bölünmüyorsa 6'ya bölünmez. | Evet |

9 sayısı karşıtı ve tersi aynı anda çürütür. Karşıt ters ise asıl önerme ile birlikte doğrudur: 3'e bölünmeyen bir sayı 6'ya hiç bölünemez.

![Dört kutu. Sol üstte koşullu p ise q, sağ üstte karşıtı q ise p, sol altta tersi p üssü ise q üssü, sağ altta karşıt tersi q üssü ise p üssü. Koşullu ile karşıt tersi yeşil, karşıtı ile tersi sarı; yeşil kutular arasında denk işareti.](gorsel/tyt-matematik/06-03-dort-bicim.svg "Yatay ok yerleri değiştirir, dikey ok ikisini de değiller. Çapraz karşıdaki kutular aynı renktedir ve birbirine denktir.")

**Kural.** $p \Rightarrow q$ önermesi için:

- **Karşıtı:** $q \Rightarrow p$ (yer değiştir).
- **Tersi:** $p' \Rightarrow q'$ (ikisini de değille).
- **Karşıt tersi:** $q' \Rightarrow p'$ (yer değiştir ve ikisini de değille).
- $p \Rightarrow q \equiv q' \Rightarrow p'$. Kontrol: $q' \Rightarrow p' \equiv (q')' \vee p' \equiv q \vee p' \equiv p' \vee q$.
- Aynı şekilde karşıt ile ters birbirine denktir: $q \Rightarrow p \equiv p' \Rightarrow q'$.

**Tersi ile değili aynı şey değildir.** $p \Rightarrow q$ önermesinin değili $(p \Rightarrow q)' \equiv p \wedge q'$'dür; bir "ise" önermesi değil, "ve" önermesidir. Tersi $p' \Rightarrow q'$ ise yine bir "ise" önermesidir. Örneğin $p \equiv 0$, $q \equiv 0$ için tersi $1 \Rightarrow 1 \equiv 1$, değili $0 \wedge 1 \equiv 0$ olur.

## Gerektirme

**Örnek.** $x$ bir gerçek sayı olsun. "$x = 3$ ise $x^2 = 9$" önermesinde $x = 3$ olduğu her durumda $x^2 = 9$ de olur; hipotez doğruyken hüküm yanlış olamaz. Bu önerme doğrudur.

Karşıtına bak: "$x^2 = 9$ ise $x = 3$". $x = -3$ için hipotez doğru, hüküm yanlış; önerme yanlıştır.

**Kural.** $p \Rightarrow q$ önermesinde $p$'ye **hipotez** (koşul), $q$'ya **hüküm** (sonuç) denir. Doğruluk değeri 1 olan koşullu önermeye **gerektirme** denir: "$p$, $q$'yu gerektirir." Yukarıdaki örnekte "$x = 3$", "$x^2 = 9$" ifadesini gerektirir; tersi doğru değildir.

## ÖSYM tuzakları

> **Hipotez yanlışken önermeyi yanlış saymak:** $0 \Rightarrow 0$ ve $0 \Rightarrow 1$ ifadelerinin ikisi de 1'dir. Koşul gerçekleşmediyse söz bozulmuş olmaz.

> **Yeri değiştirmek:** $p \Rightarrow q$ ile $q \Rightarrow p$ denk değildir. $1 \Rightarrow 0 \equiv 0$ ama $0 \Rightarrow 1 \equiv 1$.

> **Tersi ile karşıt tersini karıştırmak:** Asıl önermeye denk olan **karşıt tersi** $q' \Rightarrow p'$'dür. Tersi $p' \Rightarrow q'$ ise karşıtına denktir, asıl önermeye değil.

> **Değili "ise" ile yazmak:** $(p \Rightarrow q)' \equiv p \wedge q'$. "$p' \Rightarrow q'$" ya da "$p \Rightarrow q'$" yazmak yanlıştır.

> **Doğru verilen koşullu önermeden kesin sonuç çıkarmak:** $p \Rightarrow q \equiv 1$ bilgisi $p$ ile $q$'yu belirlemez. Yalnızca "yanlış" bilgisi tek durum verir.

## Kendini dene

### Soru 1
$p \equiv 0$ ve $q \equiv 1$ olduğuna göre aşağıdaki önermelerden hangisinin doğruluk değeri 0'dır?

A) $p \Rightarrow q$
B) $p' \Rightarrow q$
C) $q \Rightarrow p$
D) $p \Rightarrow q'$
E) $q' \Rightarrow p$

**Cevap:** C
**Çözüm:** Hipotezi 1, hükmü 0 olanı ara. C) $q \Rightarrow p \equiv 1 \Rightarrow 0 \equiv 0$. Diğerleri: A) $0 \Rightarrow 1 \equiv 1$; B) $1 \Rightarrow 1 \equiv 1$; D) $0 \Rightarrow 0 \equiv 1$; E) $0 \Rightarrow 0 \equiv 1$. A, D ve E'de hipotez 0 olduğu için sonuç kesin 1'dir.

### Soru 2
$p \Rightarrow q'$ önermesi aşağıdakilerden hangisine denktir?

A) $q' \Rightarrow p$
B) $p' \Rightarrow q$
C) $p \wedge q'$
D) $q \Rightarrow p'$
E) $p' \Rightarrow q'$

**Cevap:** D
**Çözüm:** Karşıt tersini al: yer değiştir ve ikisini de değille. $p \Rightarrow q'$ için hüküm $q'$, değili $q$; hipotez $p$, değili $p'$. Karşıt tersi $q \Rightarrow p'$ olur. Kontrol: $p \Rightarrow q' \equiv p' \vee q'$ ve $q \Rightarrow p' \equiv q' \vee p'$; aynı. A ve B ifadeleri $p \vee q$'ya denktir. C) $p \wedge q'$, $p \Rightarrow q$ önermesinin değilidir; denk değildir. E ise tersidir.

### Soru 3
$(p \Rightarrow q) \Rightarrow r \equiv 0$ ve $q \equiv 0$ olduğuna göre $p$ ile $r$'nin doğruluk değerleri sırasıyla nedir?

A) $1, 0$
B) $0, 0$
C) $0, 1$
D) $1, 1$
E) $p$ belirlenemez, $0$

**Cevap:** B
**Çözüm:** Dış "ise" yanlış: hipotez $p \Rightarrow q \equiv 1$, hüküm $r \equiv 0$. Şimdi $p \Rightarrow 0 \equiv 1$ olmalı. $p \Rightarrow 0 \equiv p'$ olduğundan $p' \equiv 1$, yani $p \equiv 0$. Sonuç $p \equiv 0$, $r \equiv 0$. $q$ bilinmeseydi $p$ belirlenemezdi (E); burada $q \equiv 0$ verildiği için tek çözüm vardır. $p \equiv 1$ alan, $1 \Rightarrow 0 \equiv 0$ olduğunu gözden kaçırır.

## Özet kartı

- $p \Rightarrow q$ yalnızca $1 \Rightarrow 0$ durumunda yanlıştır; hipotez 0 ise sonuç kesin 1'dir.
- $p \Rightarrow q \equiv p' \vee q$ ve değili $(p \Rightarrow q)' \equiv p \wedge q'$.
- $p \Rightarrow 0 \equiv p'$, $1 \Rightarrow p \equiv p$, $p \Rightarrow p' \equiv p'$; $p \Rightarrow 1$, $0 \Rightarrow p$, $p \Rightarrow p$ her zaman 1.
- Karşıt $q \Rightarrow p$, ters $p' \Rightarrow q'$, karşıt ters $q' \Rightarrow p'$.
- Asıl önerme ≡ karşıt tersi; karşıtı ≡ tersi. "İse" bağlacında yer değiştirilemez.
- Doğru olan koşullu önermeye gerektirme denir; $p$ hipotez, $q$ hükümdür.

## Sonraki adım

Alıştırmaya geç (aşağıdaki düğme). Sonraki ders **İki Yönlü Koşullu Önerme**; "ancak ve ancak" bağlacının $p \Rightarrow q$ ile $q \Rightarrow p$ önermelerinin birlikte doğru olması demek olduğunu göreceksin.
