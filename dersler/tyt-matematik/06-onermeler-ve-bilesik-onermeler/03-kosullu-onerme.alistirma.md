---
baslik: Koşullu Önerme · Alıştırma
ders: tyt-matematik
soru: 12
guncelleme: 2026-11-17
---
# Alıştırma: Koşullu Önerme

Sorular özgündür ve ÖSYM soru tarzında yazılmıştır. Derse bakmadan çöz.

## Isınma

### Soru 1 · Kolay
$p \equiv 1$ ve $q \equiv 0$ olduğuna göre aşağıdaki önermelerden hangisinin doğruluk değeri 0'dır?

A) $q \Rightarrow p$
B) $p' \Rightarrow q$
C) $p \Rightarrow q$
D) $q' \Rightarrow p$
E) $q \Rightarrow q'$

**Cevap:** C
**Çözüm:** Koşullu önerme yalnızca $1 \Rightarrow 0$ durumunda yanlıştır. C) $p \Rightarrow q \equiv 1 \Rightarrow 0 \equiv 0$. Diğerleri: A) $0 \Rightarrow 1 \equiv 1$; B) $0 \Rightarrow 0 \equiv 1$; D) $1 \Rightarrow 1 \equiv 1$; E) $0 \Rightarrow 1 \equiv 1$. A seçeneğini işaretleyen, yer değiştirmenin sonucu değiştirdiğini unutmuştur.

### Soru 2 · Kolay
$p \Rightarrow q$ önermesinin karşıt tersi aşağıdakilerden hangisidir?

A) $q \Rightarrow p$
B) $p' \Rightarrow q'$
C) $p \wedge q'$
D) $q' \Rightarrow p'$
E) $q \Rightarrow p'$

**Cevap:** D
**Çözüm:** Karşıt ters için önermelerin yeri değiştirilir ve ikisi de değillenir: $q' \Rightarrow p'$. A karşıtı (yalnızca yer değişti), B tersidir (yalnızca değillendi). C, $p \Rightarrow q$ önermesinin değilidir. E'de yalnız $p$ değillenmiştir.

### Soru 3 · Kolay
$(p \Rightarrow q)'$ önermesi aşağıdakilerden hangisine denktir?

A) $p \wedge q'$
B) $p' \wedge q$
C) $p' \vee q$
D) $p' \Rightarrow q'$
E) $q \Rightarrow p$

**Cevap:** A
**Çözüm:** $p \Rightarrow q \equiv p' \vee q$. De Morgan ile değilini al: $(p' \vee q)' \equiv (p')' \wedge q' \equiv p \wedge q'$. C, değil alınmadan önceki önermedir. D tersidir; tersi ile değili aynı değildir. B'de değil işareti yanlış önermeye konmuştur.

## Orta

### Soru 4 · Orta
$(p \Rightarrow q) \wedge p$ önermesi aşağıdakilerden hangisine denktir?

A) $p$
B) $p \wedge q$
C) $q$
D) $p \vee q$
E) $p \wedge q'$

**Cevap:** B
**Çözüm:** "İse" bağlacını çevir: $(p' \vee q) \wedge p$. "Ve" bağlacını dağıt: $(p' \wedge p) \vee (q \wedge p) \equiv 0 \vee (p \wedge q) \equiv p \wedge q$. Kontrol: $p \equiv 1$, $q \equiv 0$ için verilen önerme $0 \wedge 1 \equiv 0$ olur; A ($p$) bu durumda 1 verdiği için denk olamaz.

### Soru 5 · Orta
$(p \wedge q) \Rightarrow r' \equiv 0$ olduğuna göre aşağıdaki önermelerden hangisinin doğruluk değeri 1'dir?

A) $p \Rightarrow r'$
B) $(q \Rightarrow r)'$
C) $(p \vee q) \Rightarrow r'$
D) $r \Rightarrow (p \wedge q')$
E) $(p \Rightarrow r') \vee (q' \Rightarrow r)$

**Cevap:** E
**Çözüm:** "İse" yanlışsa hipotez 1, hüküm 0'dır: $p \wedge q \equiv 1$, yani $p \equiv 1$, $q \equiv 1$; $r' \equiv 0$, yani $r \equiv 1$. Seçenekler: A) $1 \Rightarrow 0 \equiv 0$. B) $q \Rightarrow r \equiv 1$, değili 0. C) $1 \Rightarrow 0 \equiv 0$. D) $p \wedge q' \equiv 0$, $1 \Rightarrow 0 \equiv 0$. E) $p \Rightarrow r' \equiv 0$ ama $q' \Rightarrow r \equiv 0 \Rightarrow 1 \equiv 1$; "veya" için biri yeter: $0 \vee 1 \equiv 1$.

### Soru 6 · Orta
"Bir üçgen eşkenar ise ikizkenardır." önermesinin karşıt tersi aşağıdakilerden hangisidir?

A) Bir üçgen ikizkenar ise eşkenardır.
B) Bir üçgen eşkenar değilse ikizkenar değildir.
C) Bir üçgen eşkenar ise ikizkenar değildir.
D) Bir üçgen eşkenar değilse ikizkenardır.
E) Bir üçgen ikizkenar değilse eşkenar değildir.

**Cevap:** E
**Çözüm:** $p$: "eşkenardır", $q$: "ikizkenardır". Karşıt ters $q' \Rightarrow p'$: "İkizkenar değilse eşkenar değildir." Bu önerme asıl önerme gibi doğrudur. A karşıtıdır ($q \Rightarrow p$) ve yanlıştır: kenarları 5, 5, 3 olan üçgen ikizkenardır ama eşkenar değildir. B tersidir ($p' \Rightarrow q'$) ve aynı örnekle yanlıştır.

### Soru 7 · Orta
Aşağıdaki önermelerden hangisi $p$ ve $q$'nun bütün doğruluk değerleri için doğrudur?

A) $p \Rightarrow (p \vee q)$
B) $(p \vee q) \Rightarrow p$
C) $p \Rightarrow (p \wedge q)$
D) $(p \Rightarrow q) \Rightarrow q$
E) $q' \Rightarrow (p \Rightarrow q)$

**Cevap:** A
**Çözüm:** A) $p \Rightarrow (p \vee q) \equiv p' \vee p \vee q \equiv 1 \vee q \equiv 1$. Diğerleri için 0 yapan bir durum bul: B) $p \equiv 0$, $q \equiv 1$: $1 \Rightarrow 0 \equiv 0$. C) $p \equiv 1$, $q \equiv 0$: $1 \Rightarrow 0 \equiv 0$. D) $p \equiv 0$, $q \equiv 0$: $p \Rightarrow q \equiv 1$, $1 \Rightarrow 0 \equiv 0$. E) $p \equiv 1$, $q \equiv 0$: $q' \equiv 1$, $p \Rightarrow q \equiv 0$, $1 \Rightarrow 0 \equiv 0$.

## ÖSYM tarzı

### Soru 8 · ÖSYM tarzı
Bir internet mağazası şu kuralı ilan ediyor:

"Alışverişin 200 TL'nin üzerindeyse kargo ücretsizdir."

Altı müşterinin alışveriş tutarı ve kargo için ödeme yapıp yapmadığı tabloda verilmiştir.

| Müşteri | Alışveriş | Kargo |
|---|---|---|
| Ece | 240 TL | Ücret ödedi |
| Can | 180 TL | Ücret ödedi |
| Deniz | 320 TL | Ücretsiz |
| Mert | 150 TL | Ücretsiz |
| Selin | 210 TL | Ücret ödedi |
| Arda | 200 TL | Ücret ödedi |

Buna göre kaç müşterinin durumu mağazanın kuralına aykırıdır?

A) 1
B) 2
C) 3
D) 4
E) 5

**Cevap:** B
**Çözüm:** $p$: "Alışveriş 200 TL'nin üzerinde", $q$: "Kargo ücretsiz". Kural $p \Rightarrow q$ yalnızca $p \equiv 1$, $q \equiv 0$ iken çiğnenir: 200 TL'yi geçip kargo ücreti ödeyenler. Ece (240) ve Selin (210): **2** müşteri. Mert'in kargosu ücretsizdir ama koşul gerçekleşmediği için kural çiğnenmez ($0 \Rightarrow 1 \equiv 1$). Arda'nın tutarı 200 TL'nin üzerinde değildir. Mert'i ya da Arda'yı sayan 3, ikisini de sayan 4 bulur.

### Soru 9 · ÖSYM tarzı
Her kartın bir yüzünde bir harf, öbür yüzünde bir sayı vardır. Masadaki dört kartın üstte kalan yüzleri şöyledir:

**U**  **M**  **6**  **9**

"Bir kartın bir yüzünde sesli harf varsa öbür yüzünde çift sayı vardır." kuralının çiğnenip çiğnenmediğini anlamak için **yalnızca gerekli** kartlar çevrilecektir.

Buna göre hangi kartlar çevrilmelidir?

A) Yalnız U
B) U ve 6
C) M ve 9
D) U ve 9
E) U, 6 ve 9

**Cevap:** D
**Çözüm:** $p$: "sesli harf", $q$: "çift sayı". Kural yalnızca "sesli harf ve tek sayı" ($1 \Rightarrow 0$) olan bir kartla çiğnenir. U sesli harftir; arkası tek sayıysa kural bozulur, çevrilmeli. 9 tek sayıdır; arkası sesli harfse kural bozulur, çevrilmeli. M sessizdir: $p \equiv 0$, arkası ne olursa olsun kural bozulmaz. 6 çifttir: $q \equiv 1$, arkası ne olursa olsun kural bozulmaz. 6'yı çevirmek isteyen kuralın karşıtını ($q \Rightarrow p$) sınamaya çalışıyordur.

### Soru 10 · ÖSYM tarzı
$p$ ve $q$ önermeleri için $\Delta$ bağlacı şöyle tanımlanıyor:

$$p \,\Delta\, q \equiv (p \Rightarrow q) \wedge (q \Rightarrow p')$$

Buna göre $p \,\Delta\, q$ önermesi aşağıdakilerden hangisine denktir?

A) $p$
B) $p'$
C) $q$
D) $q'$
E) $1$

**Cevap:** B
**Çözüm:** İki parçayı "veya" ile yaz: $p \Rightarrow q \equiv p' \vee q$ ve $q \Rightarrow p' \equiv q' \vee p'$. İkisinde de $p'$ ortak: $(p' \vee q) \wedge (p' \vee q') \equiv p' \vee (q \wedge q') \equiv p' \vee 0 \equiv p'$. Kontrol: $p \equiv 1$ ise ilk parça $q$, ikinci parça $q'$ olur; $q \wedge q' \equiv 0 \equiv p'$. $p \equiv 0$ ise $0 \Rightarrow q \equiv 1$ ve $q \Rightarrow 1 \equiv 1$; sonuç $1 \equiv p'$.

### Soru 11 · ÖSYM tarzı
Bir öğretmen, Ayşe hakkında söylenen "Ayşe ödevini teslim ettiyse ek puan almıştır." önermesinin **yanlış** olduğunu belirtiyor.

Buna göre Ayşe hakkında söylenen aşağıdaki önermelerden hangileri doğrudur?

- I. Ayşe ödevini teslim etmediyse ek puan almıştır.
- II. Ayşe ek puan aldıysa ödevini teslim etmemiştir.
- III. Ayşe ek puan almadıysa ödevini teslim etmemiştir.

A) Yalnız I
B) Yalnız III
C) I ve II
D) II ve III
E) I, II ve III

**Cevap:** C
**Çözüm:** $p$: "Ayşe ödevini teslim etti", $q$: "Ayşe ek puan aldı". $p \Rightarrow q \equiv 0$ ise $p \equiv 1$, $q \equiv 0$. I) $p' \Rightarrow q \equiv 0 \Rightarrow 0 \equiv 1$, doğru. II) $q \Rightarrow p' \equiv 0 \Rightarrow 0 \equiv 1$, doğru. III) $q' \Rightarrow p' \equiv 1 \Rightarrow 0 \equiv 0$, yanlış. III, verilen önermenin karşıt tersidir; ona denk olduğu için o da yanlıştır.

### Soru 12 · ÖSYM tarzı
$x$ bir pozitif tam sayı olmak üzere

- $p$: "$x$ tek sayıdır."
- $q$: "$x$ asal sayıdır."

veriliyor. $x$ yerine 1'den 10'a kadar (1 ve 10 dahil) tam sayılar tek tek yazılıyor.

Buna göre bu sayılardan kaç tanesi için $p \Rightarrow q$ önermesi doğru olur?

A) 2
B) 3
C) 7
D) 8
E) 9

**Cevap:** D
**Çözüm:** $p \Rightarrow q$ yalnızca "$x$ tek ama asal değil" iken yanlıştır. 1–10 arasındaki tek sayılar 1, 3, 5, 7, 9; bunlardan asal olmayanlar 1 ve 9. Yanlış yapan 2 sayı var, doğru yapan $10 - 2 = 8$. Çift sayılarda $p \equiv 0$ olduğu için önerme kesin doğrudur. Yalnızca hem tek hem asal olanları (3, 5, 7) sayan 3 bulur. 1'i asal sanan 9 bulur. Yanlış yapanları sayan 2'yi işaretler.
