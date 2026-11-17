---
baslik: Kümelerde Kesişim ve Birleşim İşlemleri
ders: tyt-matematik
sure: 20 dk
kaynak: MEBİ Konu Özeti b96c4ae392
guncelleme: 2026-11-18
---
# Kümelerde Kesişim ve Birleşim İşlemleri

<div class="giris" dir="rtl" lang="ar">

**الدرس ده عن إيه؟** عن أهم عمليتين في المجموعات (kümeler): التقاطع (kesişim) يعني العناصر اللي في المجموعتين مع بعض، والاتحاد (birleşim) يعني العناصر اللي في واحدة منهم على الأقل.

- هتعرف تكتب تقاطع واتحاد مجموعتين، وتعرف إن العنصر المشترك بيتكتب مرة واحدة بس.
- هتتعلم تقسّم شكل فن (Venn şeması) لمناطق وتلاقي عدد العناصر (eleman sayısı) الناقص.
- هتشوف الحالات الخاصة زي المجموعة الجزئية (alt küme) والمجموعات المنفصلة (ayrık kümeler)، وتعرف النتيجة من غير حسابات.

**ليه مهم؟** في TYT كل أسئلة المجموعات مبنية على الدرس ده، وخصوصًا مسائل زي "كام واحد مشترك في الناديين؟" اللي بتيجي كتير.

هما ٢٠ دقيقة بس، وبعدها أسئلة المجموعات هتبقى أسهل بكتير.

</div>

**Bu dersin sonunda:** iki kümenin kesişimini ve birleşimini yazabilecek, $s(A \cup B) = s(A) + s(B) - s(A \cap B)$ bağıntısıyla eksik eleman sayısını bulabilecek ve alt küme, ayrık küme gibi özel durumlarda sonucu işlem yapmadan görebileceksin.

> **TYT'de yeri:** Kesişim ve birleşim, küme sorularının tamamının temelidir. En sık gelen kalıplar: "iki kümenin eleman sayıları verilmiş, ortak eleman sayısı kaç?", Venn şemasında bölgelere yazılmış ifadelerle denklem kurmak ve "iki kulübe/iki listeye birden kaç kişi?" gibi günlük hayat problemleri.

## Önce hatırla

<details><summary>Alt kümeden: $A = \{a, b, c, d\}$ kümesinin kaç alt kümesi, kaç öz alt kümesi vardır?</summary>
$s(A) = 4$ olduğundan alt küme sayısı $2^4 = 16$. Öz alt kümeler, kümenin kendisi dışındaki alt kümelerdir: $16 - 1 = $ <b>15</b>.
</details>

<details><summary>Alt kümeden: $A \subseteq B$ ve $B \subseteq A$ ise $A$ ile $B$ hakkında ne söylenir?</summary>
$A$'nın her elemanı $B$'de, $B$'nin her elemanı $A$'da. İki kümenin elemanları aynıdır: <b>$A = B$</b>.
</details>

## Kesişim: ikisinde de olanlar

**Örnek.** $A$, 12'nin pozitif bölenleri; $B$, 18'in pozitif bölenleri olsun.

$$A = \{1, 2, 3, 4, 6, 12\} \qquad B = \{1, 2, 3, 6, 9, 18\}$$

İki kümede de bulunan elemanları tek tek seç: $1, 2, 3, 6$. Bunlar $A$ ile $B$'nin **kesişimi**dir:

$$A \cap B = \{1, 2, 3, 6\}, \qquad s(A \cap B) = 4$$

![Kesişen iki elips. Yalnız A bölgesinde 4 ve 12, ortak bölgede 1, 2, 3, 6, yalnız B bölgesinde 9 ve 18 yazıyor.](gorsel/tyt-matematik/08-01-bolenler.svg "Ortak bölgedeki 1, 2, 3, 6 hem A'da hem B'de; her biri şemada yalnız bir kez yazılır.")

**Kural.** İki kümenin ortak elemanlarının kümesine **kesişim kümesi** denir:

$$A \cap B = \{x \mid x \in A \text{ ve } x \in B\}$$

Kesişimin anahtar kelimesi **ve**dir: eleman iki koşulu birlikte sağlamalı. Dikkat et: $A \cap B$ kümesi hem $A$'nın hem $B$'nin alt kümesidir.

## Birleşim: en az birinde olanlar

**Örnek.** Aynı $A$ ve $B$ için bütün elemanları bir araya topla. Ortak olanları **bir kez** yaz:

$$A \cup B = \{1, 2, 3, 4, 6, 9, 12, 18\}, \qquad s(A \cup B) = 8$$

$s(A) + s(B) = 6 + 6 = 12$ eder; ama cevap 8. Fark, ortak 4 elemandan gelir: $1, 2, 3, 6$ hem $A$'yı sayarken hem $B$'yi sayarken sayıldı. Fazladan sayılanı bir kez çıkar: $12 - 4 = 8$.

![Yan yana iki Venn şeması. Solda yalnızca iki dairenin ortak bölgesi boyalı, başlık A kesişim B. Sağda iki dairenin tamamı boyalı, başlık A birleşim B.](gorsel/tyt-matematik/08-01-kesisim-birlesim.svg "Kesişimde yalnız ortak bölge, birleşimde iki dairenin tamamı boyanır.")

**Kural.** İki kümenin bütün elemanlarından oluşan kümeye **birleşim kümesi** denir:

$$A \cup B = \{x \mid x \in A \text{ veya } x \in B\}$$

"Veya" burada **en az biri** demektir; iki kümede birden bulunan eleman da birleşimdedir. Eleman sayısı için:

$$s(A \cup B) = s(A) + s(B) - s(A \cap B)$$

## Eleman sayısı soruları: bölgelerle düşün

**Örnek.** $s(A) = 15$, $s(B) = 11$ ve $s(A \cup B) = 20$ ise $s(A \cap B)$ kaçtır? Yalnız $A$'da ve yalnız $B$'de kaç eleman vardır?

Bağıntıya koy: $20 = 15 + 11 - s(A \cap B)$, buradan $s(A \cap B) = 26 - 20 = 6$.

Şimdi şemayı bölgelere ayır. Ortak bölgeye 6 yaz; $A$'nın geri kalanı $15 - 6 = 9$, $B$'nin geri kalanı $11 - 6 = 5$.

![İki daireli Venn şeması. Yalnız A bölgesinde 9, ortak bölgede 6, yalnız B bölgesinde 5 yazıyor. Altında 9 artı 6 eşittir 15, 6 artı 5 eşittir 11, 9 artı 6 artı 5 eşittir 20.](gorsel/tyt-matematik/08-01-bolge-sayilari.svg "Her bölgeye bir sayı yaz; s(A) iki bölgenin, s(A ∪ B) üç bölgenin toplamıdır.")

**Kural.** Önce ortak bölgeyi bul, sonra "yalnız" bölgeleri çıkararak doldur:

| İstenen | Bölgeler |
|---|---|
| $s(A)$ | yalnız $A$ + ortak |
| $s(A \cap B)$ | ortak |
| $s(A \cup B)$ | yalnız $A$ + ortak + yalnız $B$ |
| Yalnız birinde olanlar | yalnız $A$ + yalnız $B$ |

**En az, en çok.** $s(A) = 15$, $s(B) = 11$ biliniyor, başka bilgi yoksa: ortak eleman en çok 11 olabilir ($B \subseteq A$ ise), en az 0 olabilir (ortak eleman yoksa). Bu yüzden $s(A \cup B)$ en az $15$, en çok $26$ olur.

## Özel durumlar: alt küme ve ayrık kümeler

**Örnek.** $A = \{2, 4\}$ ve $B = \{1, 2, 3, 4, 5\}$ olsun. $A \subset B$. $A$'nın her elemanı zaten $B$'de olduğu için ortak elemanlar $A$'nın kendisidir; bir araya toplayınca da $B$'ye yeni eleman eklenmez:

$$A \cap B = \{2, 4\} = A, \qquad A \cup B = \{1, 2, 3, 4, 5\} = B$$

**Örnek.** $C = \{1, 3\}$ ve $D = \{2, 4, 6\}$ olsun. Ortak eleman yok: $C \cap D = \emptyset$. Kesişimi boş küme olan kümelere **ayrık kümeler** denir. Fazladan sayılan eleman olmadığı için $s(C \cup D) = 2 + 3 = 5$.

![Solda büyük bir B elipsinin içinde küçük bir A elipsi, altında A alt kümesi B, A kesişim B eşittir A, A birleşim B eşittir B. Sağda birbirine değmeyen iki daire, altında ayrık kümeler, kesişim boş küme ve eleman sayılarının doğrudan toplandığı yazıyor.](gorsel/tyt-matematik/08-01-ozel-durumlar.svg "A, B'nin içindeyse kesişim küçük küme, birleşim büyük kümedir. Ayrık kümelerde eleman sayıları doğrudan toplanır.")

**Kural.** $A \subseteq B$ ise $A \cap B = A$ ve $A \cup B = B$. Ters yönü de doğrudur: soruda $A \cap B = A$ ya da $A \cup B = B$ verilirse $A \subseteq B$ demektir.

## İşlemlerin özellikleri

**Örnek (dağılma).** $A = \{1, 2, 3\}$, $B = \{2, 4\}$, $C = \{3, 4, 5\}$ için iki yoldan hesapla:

- $A \cap (B \cup C) = \{1, 2, 3\} \cap \{2, 3, 4, 5\} = \{2, 3\}$
- $(A \cap B) \cup (A \cap C) = \{2\} \cup \{3\} = \{2, 3\}$

Sonuçlar aynı. Kesişim, birleşimin üzerine **dağılır**; aynısı birleşim için de geçerlidir.

| Özellik | Kesişim | Birleşim |
|---|---|---|
| Tek kuvvet | $A \cap A = A$ | $A \cup A = A$ |
| Değişme | $A \cap B = B \cap A$ | $A \cup B = B \cup A$ |
| Birleşme | $A \cap (B \cap C) = (A \cap B) \cap C$ | $A \cup (B \cup C) = (A \cup B) \cup C$ |
| Boş küme | $A \cap \emptyset = \emptyset$ | $A \cup \emptyset = A$ |
| Dağılma | $A \cap (B \cup C) = (A \cap B) \cup (A \cap C)$ | $A \cup (B \cap C) = (A \cup B) \cap (A \cup C)$ |

**Kural.** Değişme ve birleşme sayesinde yalnız kesişimlerden ya da yalnız birleşimlerden oluşan ifadede parantez ve sıra önemsizdir. Ama $\cap$ ile $\cup$ **karışık** ise parantezin yeri sonucu değiştirir: yukarıdaki kümelerde $(A \cap B) \cup C = \{2, 3, 4, 5\}$, oysa $A \cap (B \cup C) = \{2, 3\}$.

## ÖSYM tuzakları

> **Ortak elemanları iki kez saymak:** $s(A) = 15$, $s(B) = 11$ ise $s(A \cup B) = 26$ değildir; ortak eleman sayısını çıkarmadan birleşim bulunmaz. 26 yalnızca kümeler ayrıksa doğrudur.

> **"Yalnız A" ile "A"yı karıştırmak:** $s(A)$ ortak bölgeyi de içerir. "Yalnız $A$'da olan" sorulursa $s(A) - s(A \cap B)$ hesaplanır.

> **Tekrarlanan elemanı yazmak:** Birleşim kümesini listelerken ortak elemanlar bir kez yazılır; $\{1, 2\} \cup \{2, 3\} = \{1, 2, 3\}$, $s = 3$.

> **Parantezi yok saymak:** $A \cap (B \cup C)$ ile $(A \cap B) \cup C$ genelde farklı kümelerdir. İşlemi önce parantezin içinden yap.

## Kendini dene

### Soru 1
$A = \{2, 4, 6, 8\}$ ve $B = \{1, 2, 3, 4\}$ olduğuna göre $s(A \cup B) - s(A \cap B)$ farkı kaçtır?

A) 2
B) 4
C) 6
D) 8
E) 10

**Cevap:** B
**Çözüm:** $A \cap B = \{2, 4\}$, $s(A \cap B) = 2$. $A \cup B = \{1, 2, 3, 4, 6, 8\}$, $s(A \cup B) = 6$. Fark $6 - 2 = 4$. Ortak elemanları iki kez yazan $s(A \cup B) = 8$ alır ve 6 bulur.

### Soru 2
$s(A) = 8$, $s(B) = 13$ ve $s(A \cup B) = 17$ olduğuna göre $s(A \cap B)$ kaçtır?

A) 4
B) 5
C) 9
D) 13
E) 21

**Cevap:** A
**Çözüm:** $s(A \cup B) = s(A) + s(B) - s(A \cap B)$ bağıntısından $17 = 8 + 13 - s(A \cap B)$, yani $s(A \cap B) = 21 - 17 = 4$. 9, $17 - 8$ farkıdır ve yalnız $B$'deki eleman sayısını verir; 21 ise ortak elemanı çıkarmadan yapılan toplamdır.

### Soru 3
$A \subset B$, $s(B) = 10$ ve $s(A \cap B) = 6$ olduğuna göre $s(A \cup B)$ kaçtır?

A) 4
B) 6
C) 10
D) 16
E) 22

**Cevap:** C
**Çözüm:** $A \subset B$ olduğundan $A \cap B = A$, yani $s(A) = 6$; ve $A \cup B = B$, yani $s(A \cup B) = s(B) = 10$. Bağıntıyla kontrol: $6 + 10 - 6 = 10$. 16, ortak elemanları çıkarmadan toplamaktır.

## Özet kartı

- $A \cap B$: iki kümede de olanlar (**ve**). $A \cup B$: en az birinde olanlar (**veya**).
- $s(A \cup B) = s(A) + s(B) - s(A \cap B)$.
- Venn şemasında önce ortak bölgeyi yaz, sonra "yalnız" bölgeleri çıkararak doldur.
- $A \subseteq B$ ise $A \cap B = A$, $A \cup B = B$. Ayrık kümelerde $A \cap B = \emptyset$.
- $A \cap \emptyset = \emptyset$, $A \cup \emptyset = A$; iki işlem de değişme, birleşme ve dağılma özelliğine sahiptir.

## Sonraki adım

Alıştırmaya geç (aşağıdaki düğme). Sonraki ders **Kümelerde Fark ve Tümleme İşlemleri**; "yalnız $A$'da olanlar" bölgesine orada bir ad vereceksin: $A \setminus B$.
