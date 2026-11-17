---
baslik: Üçgende Açı-Kenar Bağıntıları
ders: tyt-matematik
sure: 20 dk
kaynak: MEBİ Konu Özeti 36aa445876
guncelleme: 2026-11-18
---
# Üçgende Açı-Kenar Bağıntıları

<div class="giris" dir="rtl" lang="ar">

**الدرس ده عن إيه؟** عن العلاقة بين زوايا المثلث وأضلاعه: الزاوية الكبيرة دايمًا قصادها الضلع الأكبر.

- هتعرف ترتّب أضلاع المثلث من زواياه (kenar sıralaması)، وترتّب الزوايا من الأضلاع.
- هتتعلم لما يكون فيه أكتر من مثلث في الشكل إزاي توصل لأطول ضلع عن طريق الضلع المشترك.
- هتقدر تقول المثلث حاد الزوايا (dar açılı) ولا قائم (dik) ولا منفرج (geniş açılı) بمقارنة مربع أطول ضلع بمجموع مربعي الضلعين التانيين.

**ليه مهم؟** في TYT السؤال غالبًا بيكون "أطول ضلع أنهي واحد؟" أو "أصغر قيمة صحيحة للضلع لو الزاوية منفرجة"، ومحتاج ترتيب ومقارنة مش حسابات طويلة.

الدرس ٢٠ دقيقة بس، وفكرته واحدة لو فهمتها هتحل بيها أسئلة كتير.

</div>

**Bu dersin sonunda:** bir üçgenin açılarından kenarlarını, kenarlarından açılarını sıralayabilecek ve kenar uzunluklarına bakarak üçgenin dar, dik ya da geniş açılı olduğunu söyleyebileceksin.

> **TYT'de yeri:** Soru genelde iki kalıpta gelir: "Şekildeki en uzun (ya da en kısa) kenar hangisidir?" ve "Bu açı geniş açı ise $x$'in alabileceği en küçük tam sayı değeri kaçtır?". İkisi de hesap değil, sıralama ve karşılaştırma ister.

## Önce hatırla

<details><summary>Geçen dersten: ABC üçgeninde |AB| = |AC| ve m(A) = 40° ise m(B) kaç derecedir?</summary>
Eş kenarların karşısındaki açılar eşittir: $m(\widehat{B}) = m(\widehat{C}) = \dfrac{180^\circ - 40^\circ}{2} = 70^\circ$. Bugün bu kuralı genişleteceksin: kenarlar eşit <b>değilse</b> hangi açı büyük olur?
</details>

<details><summary>Geçen dersten: Bir ikizkenar üçgenin tepe açısı 100° olabilir mi? Taban açısı 100° olabilir mi?</summary>
Tepe açısı olabilir: taban açıları $40^\circ$ ve $40^\circ$ olur. Taban açısı olamaz: iki taban açısı eşit olduğundan toplamları $200^\circ$ olurdu, bu da $180^\circ$'yi geçer. Yani <b>taban açıları her zaman dar açıdır</b>; bugün bunu kullanacaksın.
</details>

## Gösterim

$ABC$ üçgeninde bir kenar, **karşısındaki köşenin küçük harfiyle** adlandırılır:

- $a = |BC|$ ($A$ köşesinin karşısı),
- $b = |AC|$ ($B$ köşesinin karşısı),
- $c = |AB|$ ($C$ köşesinin karşısı).

Bu derste her kural "bir açı ve onun **karşısındaki** kenar" eşleşmesine dayanır. Önce eşleşmeyi doğru kur.

## 1. Büyük açının karşısında büyük kenar

**Örnek.** $ABC$ üçgeninde $m(\widehat{A}) = 75^\circ$ ve $m(\widehat{B}) = 45^\circ$'dir. $a$, $b$, $c$ kenarlarını sırala.

**Çözüm.**

1. Üçüncü açıyı bul: $m(\widehat{C}) = 180^\circ - 75^\circ - 45^\circ = 60^\circ$.
2. Açıları sırala: $m(\widehat{A}) > m(\widehat{C}) > m(\widehat{B})$, yani $75^\circ > 60^\circ > 45^\circ$.
3. Her açının yerine karşısındaki kenarı yaz: $a > c > b$.

![ABC üçgeni: A'da 75, B'de 45, C'de 60 derece. 75 derecenin karşısındaki BC kenarı kırmızı ve en uzun, 60 derecenin karşısındaki AB kenarı sarı, 45 derecenin karşısındaki AC kenarı yeşil ve en kısa.](gorsel/tyt-matematik/18-05-buyuk-aci.svg "Aynı renkli açı ile kenar birbirinin karşısındadır. Kırmızı 75° en büyük açı, karşısındaki kırmızı a en uzun kenar.")

**Kural:** Aynı üçgende açılar hangi sıradaysa karşılarındaki kenarlar da o sıradadır. Kural iki yönlü çalışır:

$$m(\widehat{A}) > m(\widehat{B}) > m(\widehat{C}) \iff a > b > c$$

**Tersten örnek.** $|AB| = 7$, $|BC| = 5$, $|AC| = 8$ ise en büyük açı en uzun kenarın ($[AC]$) karşısındaki $\widehat{B}$, en küçük açı en kısa kenarın ($[BC]$) karşısındaki $\widehat{A}$'dır: $m(\widehat{A}) < m(\widehat{C}) < m(\widehat{B})$.

> **Tuzak:** Kenarı açının **yanındaki** değil, **karşısındaki** kenarla eşleştir. $\widehat{A}$'nın kolları $[AB]$ ve $[AC]$'dir; $\widehat{A}$'nın karşısındaki kenar ise $[BC]$'dir.

## 2. Eşit açıların karşısında eşit kenar

**Örnek.** $ABC$ üçgeninde $m(\widehat{B}) = m(\widehat{C}) = 65^\circ$'dir. Kenarları karşılaştır.

**Çözüm.** $m(\widehat{A}) = 180^\circ - 2 \cdot 65^\circ = 50^\circ$. Eşit açıların ($\widehat{B}$ ve $\widehat{C}$) karşısındaki kenarlar eşittir: $b = c$, yani $|AC| = |AB|$. $\widehat{A}$ en küçük açı olduğu için karşısındaki $a = |BC|$ en kısa kenardır: $a < b = c$.

![İkizkenar ABC üçgeni: B ve C köşelerinde 65'er derece, A'da 50 derece. AB ve AC kenarlarında birer eşlik çentiği var.](gorsel/tyt-matematik/18-05-ikizkenar.svg "Eşit iki açının (65°) karşısındaki kenarlar çentikle gösterilmiştir, eşittir. 50°'nin karşısındaki BC en kısa kenardır.")

**Kural:**

- Bir üçgende eşit açıların karşısındaki kenarlar eşittir (ve tersi).
- İkizkenar üçgende taban açıları $\alpha$ ise $2\alpha < 180^\circ$, yani $\alpha < 90^\circ$: **taban açıları daima dar açıdır.**
- Bu yüzden ikizkenar üçgende tepe açısı $60^\circ$'den büyükse taban en uzun kenar, $60^\circ$'den küçükse taban en kısa kenardır.

> **Tuzak:** Kural yalnızca **aynı üçgen** içinde geçerlidir. Açıları aynı olan iki farklı üçgenden biri büyük, biri küçük olabilir; birinin $65^\circ$'lik açısının karşısındaki kenar diğerininkine eşit olmak zorunda değildir.

## 3. Birden çok üçgen: en uzun kenarı bulmak

**Örnek.** Şekildeki $ABCD$ dörtgeninde $[BD]$ köşegeni çizilmiştir. $m(\widehat{ABD}) = 40^\circ$, $m(\widehat{ADB}) = 60^\circ$, $m(\widehat{DBC}) = 70^\circ$, $m(\widehat{BDC}) = 50^\circ$'dir. En uzun doğru parçası hangisidir?

![ABCD dörtgeni ve BD köşegeni. Üstteki ABD üçgeninde B'de 40, D'de 60, A'da 80 derece; alttaki BCD üçgeninde B'de 70, D'de 50, C'de 60 derece.](gorsel/tyt-matematik/18-05-dortgen.svg "Ortak kenar BD iki üçgeni bağlar. Önce her üçgeni ayrı sırala, sonra iki sırayı BD üzerinden birleştir.")

**Çözüm.**

1. $ABD$ üçgeni: $m(\widehat{A}) = 180^\circ - 40^\circ - 60^\circ = 80^\circ$. Açılar $40^\circ < 60^\circ < 80^\circ$; karşılarındaki kenarlar $|AD| < |AB| < |BD|$.
2. $BCD$ üçgeni: $m(\widehat{C}) = 180^\circ - 70^\circ - 50^\circ = 60^\circ$. Açılar $50^\circ < 60^\circ < 70^\circ$; karşılarındaki kenarlar $|BC| < |BD| < |CD|$.
3. İki sıra $[BD]$'de buluşur: $|AD| < |AB| < |BD| < |CD|$ ve $|BC| < |BD|$. En uzun: $[CD]$.

**Yöntem:** Her üçgeni ayrı ayrı sırala, sonra ortak kenar üzerinden zincir kur. Ortak kenar bir üçgende en uzunsa öbür üçgende ondan da uzun bir kenar var mı, ona bak.

> **Tuzak:** Farklı üçgenlerdeki açıları doğrudan karşılaştırma. $ABD$'deki $80^\circ$, $BCD$'deki $70^\circ$'den büyük diye $[BD]$ en uzun olmaz; karşılaştırma ancak ortak kenar üzerinden yapılır. Bu örnekte $|AB|$ ile $|BC|$ karşılaştırılamaz bile: aralarında zincir yoktur.

## 4. Kenarlardan açının türü: $a^2$ ile $b^2 + c^2$

**Örnek.** Kenar uzunlukları $5$, $6$ ve $8$ olan üçgen dar açılı mı, dik üçgen mi, geniş açılı mı?

**Çözüm.** Yalnızca en uzun kenara bak; en büyük açı onun karşısındadır.

$$8^2 = 64, \qquad 5^2 + 6^2 = 25 + 36 = 61$$

$64 > 61$ olduğu için $8$'in karşısındaki açı **geniş** açıdır: üçgen geniş açılıdır.

Neden böyle? $b = 4$ ve $c = 5$ kenarlarını sabit tutup aralarındaki $\alpha$ açısını büyüttüğünü düşün. Açı büyüdükçe karşıdaki $a$ kenarı uzar. Dik açıda Pisagor bağıntısı geçerlidir: $a^2 = 4^2 + 5^2 = 41$. Açı daha küçükse $a^2$ bundan küçük, daha büyükse bundan büyük olur.

![b=4 ve c=5 kenarları sabit, aralarındaki alfa açısı 60, 90 ve 120 derece olan üç üçgen. Karşıdaki a kenarının karesi sırasıyla 21, 41 ve 61.](gorsel/tyt-matematik/18-05-uc-ucgen.svg "İki kenar sabit (4 ve 5, kareleri toplamı 41). Açı dar iken a² 41'den küçük, dik iken eşit, geniş iken büyük.")

**Kural:** $\alpha = m(\widehat{A})$ ve karşısındaki kenar $a$ ise

| Açı | Bağıntı |
|---|---|
| $\alpha < 90^\circ$ (dar) | $a^2 < b^2 + c^2$ |
| $\alpha = 90^\circ$ (dik) | $a^2 = b^2 + c^2$ |
| $\alpha > 90^\circ$ (geniş) | $a^2 > b^2 + c^2$ |

**Tam sayı örneği.** $ABC$ üçgeninde $|AB| = 5$, $|AC| = 4$ ve $\widehat{A}$ geniş açıdır. $|BC|$'nin alabileceği en küçük tam sayı değeri kaçtır?

**Çözüm.** $\widehat{A}$ geniş olduğundan $|BC|^2 > 4^2 + 5^2 = 41$. $6^2 = 36 < 41$, $7^2 = 49 > 41$. En küçük tam sayı değeri $7$'dir.

> **Tuzak:** Bir üçgenin **dar açılı** olduğunu söylemek için yalnızca en uzun kenarı denemek yeterlidir; ama kısa bir kenarı denersen her zaman "dar" çıkar ve bir şey öğrenmezsin. Kenarlardan biri bilinmiyorsa ($x$) en uzun kenarın hangisi olduğu belli değildir: iki durumu da ayrı ayrı incele.

## ÖSYM tuzakları

> **Yanlış eşleştirme.** $a$, $\widehat{A}$'nın kollarından biri değildir; $\widehat{A}$'nın karşısındaki $[BC]$'dir. Seçeneklerde sıralamanın tam tersi ya da bir harfi kaymış hâli hazır bekler.

> **Üçüncü açıyı bulmadan sıralamak.** İki açı verildiğinde üçüncüsü çoğu zaman en büyük ya da en küçük çıkar. Önce $180^\circ$'den çıkar, sonra sırala.

> **Farklı üçgenleri karıştırmak.** Bir şekilde birden çok üçgen varsa her birini ayrı sırala; zinciri yalnızca ortak kenar üzerinden kur.

> **Dik açı sınırını kaçırmak.** "Geniş açı" için $a^2 > b^2 + c^2$ **kesin** eşitsizliktir. Eşitlik dik açı verir; $a^2 = 41$ olan değer geniş açı değildir.

> **Taban açısını geniş sanmak.** İkizkenar üçgenin geniş açısı, varsa, ancak tepe açısıdır.

## Kendini dene

### Soru 1
$ABC$ üçgeninde $m(\widehat{A}) = 50^\circ$ ve $m(\widehat{B}) = 70^\circ$'dir. Kenarların doğru sıralaması hangisidir?

A) $a < b < c$
B) $a < c < b$
C) $b < a < c$
D) $b < c < a$
E) $c < a < b$

**Cevap:** B
**Çözüm:** $m(\widehat{C}) = 180^\circ - 50^\circ - 70^\circ = 60^\circ$. Açılar $\widehat{A} < \widehat{C} < \widehat{B}$, yani $50^\circ < 60^\circ < 70^\circ$. Karşılarındaki kenarlar aynı sırada: $a < c < b$. A seçeneği üçüncü açıyı bulmadan harf sırasıyla yazmaktır.

### Soru 2
$ABC$ üçgeninde $|AB| = 7$, $|BC| = 9$ ve $|AC| = 5$'tir. Bu üçgen için aşağıdakilerden hangisi doğrudur?

A) $m(\widehat{A}) = 90^\circ$
B) $m(\widehat{B}) > 90^\circ$
C) $m(\widehat{C}) > 90^\circ$
D) $m(\widehat{A}) > 90^\circ$
E) Bütün açıları dar açıdır.

**Cevap:** D
**Çözüm:** En uzun kenar $|BC| = 9$; karşısındaki açı $\widehat{A}$. $9^2 = 81$, $7^2 + 5^2 = 49 + 25 = 74$. $81 > 74$ olduğu için $\widehat{A}$ geniş açıdır. B seçeneği, en uzun kenarın bir ucundaki köşeyi seçmektir; açı kenarın karşısındadır.

### Soru 3
$ABC$ üçgeninde $|AB| = |AC|$ ve $m(\widehat{B}) = 50^\circ$'dir. Kenarların doğru sıralaması hangisidir?

A) $|BC| < |AB| = |AC|$
B) $|AB| < |AC| < |BC|$
C) $|AB| = |BC| < |AC|$
D) $|AB| = |AC| = |BC|$
E) $|AB| = |AC| < |BC|$

**Cevap:** E
**Çözüm:** $|AB| = |AC|$ olduğundan $m(\widehat{C}) = m(\widehat{B}) = 50^\circ$ ve $m(\widehat{A}) = 180^\circ - 100^\circ = 80^\circ$. En büyük açı $\widehat{A}$; karşısındaki $[BC]$ en uzun kenardır: $|AB| = |AC| < |BC|$. A seçeneği, $50^\circ$'yi tepe açısı sanmaktan gelir.

## Özet kartı

- $a = |BC|$, $b = |AC|$, $c = |AB|$: kenar, karşısındaki köşenin adını alır.
- Büyük açının karşısında büyük kenar, küçük açının karşısında küçük kenar (iki yönlü).
- Eşit açıların karşısındaki kenarlar eşittir; ikizkenar üçgenin taban açıları daima dardır.
- Birden çok üçgende: her üçgeni ayrı sırala, ortak kenar üzerinden birleştir.
- En uzun kenar $a$ ise: $a^2 < b^2 + c^2$ dar, $a^2 = b^2 + c^2$ dik, $a^2 > b^2 + c^2$ geniş açılı üçgen.

## Sonraki adım

Alıştırmaya geç (aşağıdaki düğme). Sonraki ders: **Üçgen Eşitsizliği**. Orada bir kenarın alabileceği değerlerin üst sınırını da bulacaksın; bugünkü $a^2 > b^2 + c^2$ koşulu ile birleşince "kaç farklı tam sayı değeri alır?" soruları çözülür.
