---
baslik: İki Yönlü Koşullu Önerme
ders: tyt-matematik
sure: 20 dk
kaynak: MEBİ Konu Özeti 01686bd48b
guncelleme: 2026-11-18
---
# İki Yönlü Koşullu Önerme

<div class="giris" dir="rtl" lang="ar">

**الدرس ده عن إيه؟** عن القضية الشرطية الثنائية (iki yönlü koşullu önerme)، اللي بنقراها "إذا وفقط إذا" (ancak ve ancak): إمتى بتبقى صح وإمتى بتبقى غلط.

- هتعرف إن قيمة الصدق (doğruluk değeri) بتاعتها بتطلع 1 لما الطرفين يبقوا زي بعض، و0 لما يختلفوا.
- هتتعلم خواصها، وإزاي تحرّك علامات النفي (değil) صح وتبسّط العبارات اللي فيها الرابط ده.
- هتعرف تطلّع قيم p و q و r من قيمة قضية مركبة معروفة، وتفهم يعني إيه الاستلزام المزدوج (çift gerektirme).

**ليه مهم؟** في TYT الرابط ده نادرًا ما بييجي لوحده؛ بييجي جوه قضية مركبة (bileşik önerme)، وأشهر غلطة إنك تحل السؤال في اتجاه واحد وتنسى الحالة التانية.

الدرس ٢٠ دقيقة بس، وسؤال واحد "الطرفين زي بعض ولا لأ؟" هيحلّ لك أغلب المسائل. يلا بينا.

</div>

**Bu dersin sonunda:** $p \Leftrightarrow q$ önermesinin değerini "iki taraf aynı mı?" sorusuyla hemen bulabilecek, değil işaretlerini doğru taşıyarak $p \Leftrightarrow q$ içeren ifadeleri sadeleştirebileceksin.

> **TYT'de yeri:** "Ancak ve ancak" bağlacı genelde tek başına değil, bir bileşik önermenin içinde gelir: "Önerme yanlış olduğuna göre $p$, $q$, $r$ nedir?", "Hangisi $(p \Leftrightarrow q)'$ önermesine denktir?" ya da iki yönlü işleyen bir kuralın (kart, bariyer, lamba) hangi durumlarda bozulduğu. Anahtar cümle: **$p \Leftrightarrow q$, iki taraf aynı değerdeyse 1, farklıysa 0'dır.**

## Önce hatırla

<details><summary>Koşullu önermeden: p ≡ 1 ve q ≡ 0 ise p ⇒ q ile q ⇒ p önermelerinin doğruluk değerleri nedir?</summary>
$p \Rightarrow q \equiv 1 \Rightarrow 0 \equiv 0$ (tek yanlış durum budur). $q \Rightarrow p \equiv 0 \Rightarrow 1 \equiv 1$ (hipotez 0 ise sonuç kesin 1). Yer değiştirince değer değişti: "ise" bağlacında yön önemlidir. Bu derste iki yönü birden isteyeceğiz.
</details>

<details><summary>Koşullu önermeden: p ⇒ q önermesinin karşıtı nedir? Asıl önermeye denk midir?</summary>
Karşıtı $q \Rightarrow p$'dir (yer değiştir). Denk değildir; asıl önermeye denk olan karşıt tersi $q' \Rightarrow p'$'dür. Karşıt, terse ($p' \Rightarrow q'$) denktir.
</details>

## "Ancak ve ancak" bağlacı

**Örnek.** Bir binanın girişindeki kural: "Kapı **ancak ve ancak** kart okutulursa açılır."

- $p$: "Kart okutuldu."
- $q$: "Kapı açıldı."

Bu kural iki şey söyler: kart okutulursa kapı açılır ($p \Rightarrow q$) **ve** kapı açıldıysa kart okutulmuştur ($q \Rightarrow p$). Dört durumdan hangileri kuralı bozar?

![Dört satırlık tablo. p bir q bir, kural işledi, değer 1. p bir q sıfır, arıza, değer 0. p sıfır q bir, arıza, değer 0. p sıfır q sıfır, kural işledi, değer 1.](gorsel/tyt-matematik/06-04-kapi-tablosu.svg "İki kırmızı satır da arızadır: kart okutulup kapının açılmaması da, kart olmadan kapının açılması da kuralı bozar. Değerler aynı olan satırlar 1, farklı olanlar 0.")

Kart okutulup kapı açılmazsa $p \Rightarrow q$ bozulur. Kart yokken kapı açılırsa $q \Rightarrow p$ bozulur. Kural ancak iki taraf "birlikte var" ya da "birlikte yok" iken işler.

**Kural.** $p \Rightarrow q$ ile $q \Rightarrow p$ önermelerinin "ve" ile bağlanmasıyla kurulan önermeye **iki yönlü koşullu önerme** denir. $p \Leftrightarrow q$ ile gösterilir ve "$p$ ancak ve ancak $q$" diye okunur.

$$p \Leftrightarrow q \equiv (p \Rightarrow q) \wedge (q \Rightarrow p)$$

| $p$ | $q$ | $p \Rightarrow q$ | $q \Rightarrow p$ | $(p \Rightarrow q) \wedge (q \Rightarrow p)$ | $p \Leftrightarrow q$ |
|---|---|---|---|---|---|
| 1 | 1 | 1 | 1 | 1 | 1 |
| 1 | 0 | 0 | 1 | **0** | **0** |
| 0 | 1 | 1 | 0 | **0** | **0** |
| 0 | 0 | 1 | 1 | 1 | 1 |

$p \Leftrightarrow q$, $p$ ile $q$ **aynı** değerdeyse 1, **farklı** değerdeyse 0'dır. "Ancak ve ancak" işaretini bir "aynı mı?" sorusu gibi oku.

$p \Rightarrow q$ yalnızca bir satırda (1, 0) yanlıştı; $p \Leftrightarrow q$ iki satırda yanlıştır: (1, 0) ve (0, 1).

![Dikdörtgen içinde kesişen p ve q daireleri. Yalnız p bölgesi ve yalnız q bölgesi kırmızı ve 0 yazılı; kesişim ve iki dairenin dışı yeşil ve 1 yazılı.](gorsel/tyt-matematik/06-04-venn.svg "Yeşil bölgeler ikisinin de doğru olduğu kesişim ile ikisinin de yanlış olduğu dış bölgedir. Kırmızı bölgelerde p ve q farklıdır.")

Şemadaki iki yeşil bölge şu denkliği verir: ya ikisi de doğru ya ikisi de yanlış.

$$p \Leftrightarrow q \equiv (p \wedge q) \vee (p' \wedge q')$$

## Ancak ve ancak bağlacının özellikleri

**Örnek.** $p \Leftrightarrow 1$ önermesinin denkini bul.

"Aynı mı?" diye sor. $p \equiv 1$ ise $1 \Leftrightarrow 1 \equiv 1$; $p \equiv 0$ ise $0 \Leftrightarrow 1 \equiv 0$. Sonuç her durumda $p$'nin kendi değeri: $p \Leftrightarrow 1 \equiv p$.

Aynı yolla $p \Leftrightarrow 0$: $p \equiv 1$ ise $0$, $p \equiv 0$ ise $1$. Sonuç $p$'nin tersi: $p \Leftrightarrow 0 \equiv p'$.

**Kural.**

| Özellik | Neden? |
|---|---|
| $p \Leftrightarrow q \equiv q \Leftrightarrow p$ | "Aynı mı?" sorusunda sıra önemli değildir (değişme özelliği). |
| $p \Leftrightarrow 1 \equiv p$ | $p$, 1 ile aynıysa 1 çıkar. |
| $p \Leftrightarrow 0 \equiv p'$ | $p$, 0 ile aynıysa 1 çıkar; yani $p \equiv 0$ iken. |
| $p \Leftrightarrow p \equiv 1$ | Bir önerme kendisiyle hep aynıdır. |
| $p \Leftrightarrow p' \equiv 0$ | Bir önerme değiliyle hiç aynı olmaz. |

"İse" bağlacının değişme özelliği yoktu ($p \Rightarrow q \not\equiv q \Rightarrow p$); "ancak ve ancak" bağlacının vardır.

## Değil işaretlerini taşımak

**Örnek.** $p \equiv 1$, $q \equiv 0$ için dört önermeyi hesaplayalım.

| Önerme | Hesap | Değer |
|---|---|---|
| $p \Leftrightarrow q$ | $1 \Leftrightarrow 0$ | 0 |
| $p' \Leftrightarrow q'$ | $0 \Leftrightarrow 1$ | 0 |
| $p' \Leftrightarrow q$ | $0 \Leftrightarrow 0$ | 1 |
| $p \Leftrightarrow q'$ | $1 \Leftrightarrow 1$ | 1 |

İkisini birden değillersen ikisi birlikte değişir, "aynı mı?" sorusunun cevabı değişmez. Yalnız birini değillersen cevap tersine döner.

**Kural.**

$$p \Leftrightarrow q \equiv p' \Leftrightarrow q' \qquad (p \Leftrightarrow q)' \equiv p' \Leftrightarrow q \equiv p \Leftrightarrow q'$$

![Üst satırda yeşil iki kutu: p ancak ve ancak q, denktir p üssü ancak ve ancak q üssü. Alt satırda kırmızı üç kutu: p üssü ancak ve ancak q, p ancak ve ancak q üssü ve p ancak ve ancak q önermesinin değili; aralarında denk işareti.](gorsel/tyt-matematik/06-04-degil-sayisi.svg "Değil işaretlerini say. Sayı çiftse ifade p ⇔ q ile denktir, tekse onun değiline denktir.")

Kısa yol: bir $\Leftrightarrow$ ifadesindeki değil işaretlerini (dıştaki dahil) say. Çift sayıda ise $p \Leftrightarrow q$, tek sayıda ise $(p \Leftrightarrow q)'$ elde edersin. Örneğin $(p' \Leftrightarrow q')'$ ifadesinde 3 değil var: $(p' \Leftrightarrow q')' \equiv (p \Leftrightarrow q)' \equiv p \Leftrightarrow q'$.

**Örnek (sadeleştirme).** $(p \Leftrightarrow q) \wedge q$ önermesinin denki nedir?

$q \equiv 0$ ise "ve" bağlacı yüzünden sonuç 0. $q \equiv 1$ ise $p \Leftrightarrow 1 \equiv p$, sonuç $p \wedge 1 \equiv p$. Sonuç: $q \equiv 1$ iken $p$, $q \equiv 0$ iken 0. Bu, $p \wedge q$ önermesinin ta kendisidir: $(p \Leftrightarrow q) \wedge q \equiv p \wedge q$.

## Değeri verilen önermeden $p$, $q$, $r$ bulmak

**Örnek.** $(p \vee q) \Leftrightarrow r' \equiv 0$ ve $r \equiv 0$ olduğuna göre $p$ ile $q$'nun değerleri nedir?

1. $r \equiv 0$ ise sağ taraf $r' \equiv 1$.
2. "Ancak ve ancak" yanlışsa iki taraf farklıdır: $p \vee q \equiv 0$.
3. "Veya" yanlışsa ikisi de yanlıştır: $p \equiv 0$, $q \equiv 0$.

**Kural.** $p \Leftrightarrow q$ önermesinin değeri ve taraflardan birinin değeri biliniyorsa öbür taraf kesin bulunur. Yalnızca $p \Leftrightarrow q \equiv 0$ bilgisi ise tek durum vermez: (1, 0) ya da (0, 1) olabilir. Bu, $p \Rightarrow q \equiv 0$ bilgisinden farklıdır; orada tek durum vardı.

## Çift gerektirme

**Örnek.** $x$ bir tam sayı olsun.

- "$x$ çift sayıdır $\Leftrightarrow$ $x^2$ çift sayıdır." Çift sayının karesi çifttir; tek sayının karesi tektir. İki yön de her tam sayı için doğrudur. Bu önerme **doğrudur**.
- "$x = 3 \Leftrightarrow x^2 = 9$." Soldan sağa doğru, ama $x = -3$ için $x^2 = 9$ doğru, $x = 3$ yanlış; iki taraf farklı değer alır. Bu önerme **yanlıştır**.

**Kural.** Doğruluk değeri 1 olan $p \Leftrightarrow q$ önermesine **çift gerektirme** denir: $p$, $q$'yu gerektirir ve $q$, $p$'yi gerektirir. Bir yönün çürümesi için tek bir karşı örnek yeter.

## ÖSYM tuzakları

> **"Ancak ve ancak" sorusunu tek yönlü çözmek:** Bir kural iki yönlü verildiyse bozulduğu durum iki tanedir: (1, 0) ve (0, 1). Yalnız $p \Rightarrow q$'yu sınayan, ikinci arızayı kaçırır.

> **Değili yanlış yere koymak:** $(p \Leftrightarrow q)' \not\equiv p' \Leftrightarrow q'$. İkisini birden değillemek hiçbir şeyi değiştirmez; değil için yalnızca **bir** tarafı değille: $(p \Leftrightarrow q)' \equiv p \Leftrightarrow q'$.

> **$p \Leftrightarrow q \equiv 0$ bilgisinden tek durum çıkarmak:** "İse" yanlışsa $p \equiv 1$, $q \equiv 0$ kesindi. "Ancak ve ancak" yanlışsa yalnızca "farklılar" bilgisi vardır; hangisinin 1 olduğu başka bir bilgiyle belirlenir.

> **$p \Leftrightarrow 0$ ile $p \Leftrightarrow 1$ özelliklerini karıştırmak:** $p \Leftrightarrow 1 \equiv p$, $p \Leftrightarrow 0 \equiv p'$. Emin değilsen $p$ yerine 1 ve 0 koyup "aynı mı?" diye sor.

## Kendini dene

### Soru 1
$p \equiv 1$, $q \equiv 0$ ve $r \equiv 0$ olduğuna göre aşağıdaki önermelerden hangisinin doğruluk değeri 1'dir?

A) $p \Leftrightarrow q$
B) $q \Leftrightarrow r$
C) $p \Leftrightarrow r$
D) $p' \Leftrightarrow r'$
E) $(p \Leftrightarrow q) \Leftrightarrow p$

**Cevap:** B
**Çözüm:** Aynı değerdeki çifti ara. B) $q \Leftrightarrow r \equiv 0 \Leftrightarrow 0 \equiv 1$. Diğerleri: A) $1 \Leftrightarrow 0 \equiv 0$; C) $1 \Leftrightarrow 0 \equiv 0$; D) $0 \Leftrightarrow 1 \equiv 0$; E) önce $p \Leftrightarrow q \equiv 0$, sonra $0 \Leftrightarrow 1 \equiv 0$. B'yi "ikisi de 0, sonuç 0" diye eleyen, $\Leftrightarrow$ bağlacını "ve" gibi okumuştur.

### Soru 2
$(p \Leftrightarrow q)'$ önermesi aşağıdakilerden hangisine denktir?

A) $p' \Leftrightarrow q'$
B) $p' \wedge q'$
C) $p \Rightarrow q'$
D) $q \Leftrightarrow p$
E) $p \Leftrightarrow q'$

**Cevap:** E
**Çözüm:** Değil için tek bir tarafı değillemek yeter: $(p \Leftrightarrow q)' \equiv p \Leftrightarrow q'$. A'da iki değil var; çift sayıda değil sonucu değiştirmez, A $p \Leftrightarrow q$'ya denktir. D de değişme özelliğiyle $p \Leftrightarrow q$'nun kendisidir. B ve C'yi $p \equiv 0$, $q \equiv 1$ ile sına: $(p \Leftrightarrow q)' \equiv 1$ ama $p' \wedge q' \equiv 0$; C için $p \equiv 0$, $q \equiv 0$ al: $(p \Leftrightarrow q)' \equiv 0$ ama $p \Rightarrow q' \equiv 0 \Rightarrow 1 \equiv 1$.

### Soru 3
$(p \Leftrightarrow q) \vee r \equiv 0$ ve $p \vee r \equiv 1$ olduğuna göre $p$, $q$, $r$ önermelerinin doğruluk değerleri sırasıyla nedir?

A) $1, 0, 0$
B) $1, 1, 0$
C) $0, 1, 0$
D) $0, 0, 0$
E) $1, 0, 1$

**Cevap:** A
**Çözüm:** "Veya" yanlışsa iki parça da yanlıştır: $r \equiv 0$ ve $p \Leftrightarrow q \equiv 0$ ($p$ ile $q$ farklı). İkinci bilgi: $p \vee r \equiv p \vee 0 \equiv p \equiv 1$. O hâlde $q \equiv 0$. Sonuç $1, 0, 0$. C, ikinci bilgiyi kullanmadan $p \Leftrightarrow q \equiv 0$ durumlarından diğerini seçer. B ve D'de $p$ ile $q$ aynıdır, $p \Leftrightarrow q \equiv 1$ olur. E'de $r \equiv 1$ olduğu için "veya" doğru olur.

## Özet kartı

- $p \Leftrightarrow q \equiv (p \Rightarrow q) \wedge (q \Rightarrow p)$: iki taraf aynıysa 1, farklıysa 0.
- $p \Leftrightarrow q \equiv (p \wedge q) \vee (p' \wedge q')$; yanlış olduğu iki durum vardır: (1, 0) ve (0, 1).
- $p \Leftrightarrow 1 \equiv p$, $p \Leftrightarrow 0 \equiv p'$, $p \Leftrightarrow p \equiv 1$, $p \Leftrightarrow p' \equiv 0$, $p \Leftrightarrow q \equiv q \Leftrightarrow p$.
- Değilleri say: çiftse $p \Leftrightarrow q$, tekse $(p \Leftrightarrow q)' \equiv p' \Leftrightarrow q \equiv p \Leftrightarrow q'$.
- Değeri ve bir tarafı bilinen $\Leftrightarrow$ önermesi öbür tarafı kesin belirler.
- Doğruluk değeri 1 olan $p \Leftrightarrow q$ önermesine çift gerektirme denir.

## Sonraki adım

Alıştırmaya geç (aşağıdaki düğme). Sonraki ders **Niceleyiciler**; "her" ve "bazı" sözcükleriyle kurulan önermeleri ve bunların değillerini göreceksin.
