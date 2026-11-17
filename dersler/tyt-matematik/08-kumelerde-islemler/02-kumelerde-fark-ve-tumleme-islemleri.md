---
baslik: Kümelerde Fark ve Tümleme İşlemleri
ders: tyt-matematik
sure: 20 dk
kaynak: MEBİ Konu Özeti b82a06dffe
guncelleme: 2026-11-18
---
# Kümelerde Fark ve Tümleme İşlemleri

**Bu dersin sonunda:** $A \setminus B$ ve $A'$ kümelerini yazabilecek, $s(A \setminus B) = s(A) - s(A \cap B)$ ve $s(A') = s(E) - s(A)$ bağıntılarıyla "yalnız birinde" ve "hiçbirinde" sorularını çözebileceksin.

> **TYT'de yeri:** Fark ve tümleme, küme problemlerinin "yalnız A'yı seçen", "hiçbirini seçmeyen" kısımlarıdır. Sık gelen kalıplar: Venn şemasında taralı bölgeyi işlemle yazmak, $A' \setminus B'$ gibi ifadeleri sadeleştirmek ve "sınıftaki öğrencilerden kaçı iki kursa da gitmiyor?" türü günlük hayat problemleri.

## Önce hatırla

<details><summary>Kesişim ve birleşimden: $s(A) = 10$, $s(B) = 7$ ve $s(A \cup B) = 13$ ise $s(A \cap B)$ kaçtır?</summary>
$s(A \cup B) = s(A) + s(B) - s(A \cap B)$ bağıntısından $13 = 10 + 7 - s(A \cap B)$, yani $s(A \cap B) = 17 - 13 = $ <b>4</b>.
</details>

<details><summary>Kesişim ve birleşimden: $A \subseteq B$ ise $A \cap B$ ve $A \cup B$ hangi kümelere eşittir?</summary>
$A$'nın her elemanı zaten $B$'dedir. Ortak elemanlar $A$'nın kendisidir, birleşime yeni eleman gelmez: <b>$A \cap B = A$, $A \cup B = B$</b>.
</details>

## Fark: birinde olup ötekinde olmayanlar

**Örnek.** Önceki dersteki kümeleri al: $A$, 12'nin pozitif bölenleri; $B$, 18'in pozitif bölenleri.

$$A = \{1, 2, 3, 4, 6, 12\} \qquad B = \{1, 2, 3, 6, 9, 18\}$$

$A$'nın elemanlarını tek tek gez, $B$'de **olmayanları** seç: $1, 2, 3, 6$ $B$'de var, atılır; $4$ ve $12$ yok, kalır.

$$A \setminus B = \{4, 12\} \qquad B \setminus A = \{9, 18\}$$

İki sonuç farklı. Fark işleminde sıra önemlidir.

![Yan yana iki Venn şeması. Solda A dairesinin B ile çakışmayan kısmı boyalı, içinde 4 ve 12; başlık A fark B. Sağda B'nin A ile çakışmayan kısmı boyalı, içinde 9 ve 18; başlık B fark A. Ortak bölgede 1, 2, 3, 6 iki şemada da boyasız.](gorsel/tyt-matematik/08-02-fark.svg "A fark B, A'nın ortak bölge dışında kalan parçasıdır. Ortak bölge hiçbir farka girmez.")

**Kural.** $A$'da olup $B$'de olmayan elemanların kümesine **$A$ fark $B$** denir; $A \setminus B$ ya da $A - B$ yazılır.

$$A \setminus B = \{x \mid x \in A \text{ ve } x \notin B\}, \qquad s(A \setminus B) = s(A) - s(A \cap B)$$

Örnekte $s(A \setminus B) = 6 - 4 = 2$. Önceki dersteki "yalnız $A$" bölgesinin adı artık $A \setminus B$'dir.

## Farkın özellikleri

**Örnek.** $A = \{a, b, c\}$ olsun.

- $A \setminus A$: $A$'dan $A$'nın bütün elemanlarını atarsan geriye bir şey kalmaz, $\emptyset$.
- $A \setminus \emptyset$: atılacak eleman yok, sonuç $A$.
- $A \setminus \{a, b, c, d\}$: $A$'nın her elemanı ikinci kümede var, hepsi atılır, $\emptyset$.
- $A \setminus \{x, y\}$: ortak eleman yok, hiçbir şey atılmaz, sonuç $A$.

**Kural.**

| Durum | Sonuç |
|---|---|
| Kümenin kendisinden farkı | $A \setminus A = \emptyset$ |
| Boş kümeden farkı | $A \setminus \emptyset = A$ |
| $A \subseteq B$ ise | $A \setminus B = \emptyset$ (özel olarak $A \setminus E = \emptyset$) |
| $A$ ve $B$ ayrık ise ($A \cap B = \emptyset$) | $A \setminus B = A$, $B \setminus A = B$ |
| $A = B$ ise | $A \setminus B = B \setminus A = \emptyset$ |
| $A \ne B$ ise | $A \setminus B \ne B \setminus A$ (değişme özelliği yok) |

## Tümleme: evrensel kümede kalanlar

**Örnek.** Evrensel küme $E = \{1, 2, 3, \ldots, 10\}$, $A$ ise $E$'deki asal sayılar olsun: $A = \{2, 3, 5, 7\}$.

$E$'nin $A$'da **olmayan** elemanlarını yaz:

$$A' = \{1, 4, 6, 8, 9, 10\}, \qquad s(A') = 10 - 4 = 6$$

1 asal değildir; $A'$'ya girer.

![Dikdörtgen biçiminde E kümesi, içinde bir A dairesi. Dairenin içinde 2, 3, 5, 7. Dairenin dışındaki boyalı alanda 1, 4, 6, 8, 9, 10 ve A üssü işareti var.](gorsel/tyt-matematik/08-02-tumleyen.svg "A' dikdörtgenin A dışında kalan boyalı kısmıdır. E'yi bilmeden A' yazılamaz.")

**Kural.** $E$'de olup $A$'da olmayan elemanların kümesine **$A$'nın tümleyeni** denir, $A'$ yazılır.

$$A' = \{x \mid x \in E \text{ ve } x \notin A\} = E \setminus A, \qquad s(A') = s(E) - s(A)$$

Tümleme aslında evrensel kümeden fark almaktır. Bunu fark işlemine de uygula: $B$'de olmamak, $B'$'de olmak demektir. Bu yüzden

$$A \setminus B = A \cap B'$$

Örnek: $B$ çift sayılar $\{2, 4, 6, 8, 10\}$ ise $B' = \{1, 3, 5, 7, 9\}$ ve $A \cap B' = \{3, 5, 7\} = A \setminus B$.

## Tümlemenin özellikleri ve De Morgan

**Örnek.** Aynı $E$, $A = \{2, 3, 5, 7\}$ ve $B = \{2, 4, 6, 8, 10\}$ için iki yoldan hesapla:

- $A \cup B = \{2, 3, 4, 5, 6, 7, 8, 10\}$, buradan $(A \cup B)' = \{1, 9\}$.
- $A' = \{1, 4, 6, 8, 9, 10\}$, $B' = \{1, 3, 5, 7, 9\}$, buradan $A' \cap B' = \{1, 9\}$.

Sonuçlar aynı: "ikisinden birinde de olmayanlar", "$A$'da olmayan **ve** $B$'de olmayan" elemanlardır.

**Kural.**

| Özellik | Anlamı |
|---|---|
| $(A')' = A$ | İki kez tümleyen kümenin kendisini verir. |
| $A \cap A' = \emptyset$, $A \cup A' = E$ | Bir eleman ya $A$'dadır ya $A'$'da; ikisinde birden olamaz. |
| $E' = \emptyset$, $\emptyset' = E$ | Evrensel kümenin dışında eleman yoktur. |
| $E \setminus A = A'$, $A \setminus A' = A$ | $A$ ile $A'$ ayrıktır. |
| $(A \cup B)' = A' \cap B'$ | De Morgan: tümleme birleşimi kesişime çevirir. |
| $(A \cap B)' = A' \cup B'$ | De Morgan: kesişimi birleşime çevirir. |

## Dört bölge: "hiçbiri" soruları

**Örnek.** 40 kişilik bir sınıfta 22 öğrenci İngilizce, 15 öğrenci Almanca kursuna gidiyor; 8 öğrenci iki kursa da gidiyor. İki kursa da gitmeyen kaç öğrenci vardır?

Sınıf evrensel kümedir: $s(E) = 40$. İngilizce kümesi $\text{İ}$, Almanca kümesi $A$ olsun.

1. Ortak bölge: $s(\text{İ} \cap A) = 8$.
2. Yalnız İngilizce: $s(\text{İ} \setminus A) = 22 - 8 = 14$. Yalnız Almanca: $s(A \setminus \text{İ}) = 15 - 8 = 7$.
3. En az bir kursa gidenler: $14 + 8 + 7 = 29$.
4. Hiçbirine gitmeyenler: $s\big((\text{İ} \cup A)'\big) = 40 - 29 = 11$.

![Dikdörtgen E içinde kesişen iki elips, İ ve A. Yalnız İ bölgesinde 14, ortak bölgede 8, yalnız A bölgesinde 7, elipslerin dışında 11 yazıyor. Her sayının altında ya da yanında bölgenin adı var.](gorsel/tyt-matematik/08-02-dort-bolge.svg "Dört bölgenin toplamı 14 + 8 + 7 + 11 = 40, yani sınıfın tamamı.")

**Kural.** İki küme evrensel kümeyi dört parçaya ayırır: $A \setminus B$, $A \cap B$, $B \setminus A$, $(A \cup B)'$. Dördünün toplamı $s(E)$'dir.

$$s\big((A \cup B)'\big) = s(E) - s(A \cup B)$$

## ÖSYM tuzakları

> **Farkta sırayı karıştırmak:** $A \setminus B$ ile $B \setminus A$ farklı kümelerdir. "$A$'da olup $B$'de olmayan" ifadesinde ilk yazılan küme, elemanların alındığı kümedir.

> **$s(A \setminus B) = s(A) - s(B)$ yazmak:** Yanlış. Çıkarılan, $B$'nin tamamı değil, ortak kısımdır: $s(A) - s(A \cap B)$.

> **"Hiçbiri" sorusunda ortak bölgeyi unutmak:** Örnekte $40 - 22 - 15 = 3$ bulunur; ortak 8 kişi iki kez çıkarılmıştır. Önce $s(A \cup B)$'yi bul, sonra $s(E)$'den çıkar.

> **De Morgan'da işareti çevirmemek:** $(A \cup B)' = A' \cup B'$ değildir. Tümleme parantezin içine girerken $\cup$ ile $\cap$ yer değiştirir.

## Kendini dene

### Soru 1
$E = \{1, 2, 3, \ldots, 10\}$, $A = \{2, 3, 5, 7\}$ ve $B = \{1, 2, 3, 4\}$ olduğuna göre $(A \setminus B)'$ kümesinin eleman sayısı kaçtır?

A) 2
B) 4
C) 6
D) 8
E) 10

**Cevap:** D
**Çözüm:** Önce parantez: $A \setminus B = \{5, 7\}$ ($2$ ve $3$ $B$'de olduğu için atılır). Tümleyen, $E$'nin bu iki eleman dışındaki elemanlarıdır: $s\big((A \setminus B)'\big) = 10 - 2 = 8$. 2, tümleyeni almayı unutmaktır; 6 ise $s(A')$'dır.

### Soru 2
$s(E) = 40$, $s(A) = 18$, $s(B) = 15$ ve $s(A \cap B) = 6$ olduğuna göre $s(A' \cap B')$ kaçtır?

A) 7
B) 13
C) 19
D) 22
E) 27

**Cevap:** B
**Çözüm:** De Morgan: $A' \cap B' = (A \cup B)'$. $s(A \cup B) = 18 + 15 - 6 = 27$, buradan $s\big((A \cup B)'\big) = 40 - 27 = 13$. 7, ortak elemanları çıkarmadan $40 - 33$ yapmaktır; 27 ise birleşimin kendisidir.

### Soru 3
$A$ ve $B$ herhangi iki küme olmak üzere $A \setminus (A \setminus B)$ kümesi aşağıdakilerden hangisine eşittir?

A) $\emptyset$
B) $A$
C) $B$
D) $A \setminus B$
E) $A \cap B$

**Cevap:** E
**Çözüm:** $A \setminus B$, $A$'nın ortak bölge dışında kalan parçasıdır. Bunu $A$'dan atınca $A$'nın yalnızca ortak bölgesi kalır: $A \cap B$. Örnekle kontrol: $A = \{1, 2, 3\}$, $B = \{2, 3, 4\}$ için $A \setminus B = \{1\}$, $A \setminus \{1\} = \{2, 3\} = A \cap B$. C seçeneği ($B$) bu örnekte $\{2, 3, 4\}$ olur, yanlıştır.

## Özet kartı

- $A \setminus B$: $A$'da olup $B$'de olmayanlar. $s(A \setminus B) = s(A) - s(A \cap B)$. Sıra önemlidir.
- $A'$: $E$'de olup $A$'da olmayanlar. $s(A') = s(E) - s(A)$.
- $A \setminus B = A \cap B'$; $A \subseteq B$ ise $A \setminus B = \emptyset$, ayrık kümelerde $A \setminus B = A$.
- $(A')' = A$, $A \cap A' = \emptyset$, $A \cup A' = E$, $E' = \emptyset$, $\emptyset' = E$.
- De Morgan: $(A \cup B)' = A' \cap B'$, $(A \cap B)' = A' \cup B'$.
- İki küme $E$'yi dört bölgeye ayırır; "hiçbiri" $= s(E) - s(A \cup B)$.

## Sonraki adım

Alıştırmaya geç (aşağıdaki düğme). Sonraki ders **Küme Problemleri**; orada bu dört bölgeyi üç kümeli ve oranlı sözel problemlerde kullanacaksın.
