---
baslik: Kümelerde Temel Kavramlar
ders: tyt-matematik
sure: 20 dk
kaynak: MEBİ Konu Özeti 84a5cc28c9
guncelleme: 2026-11-17
---
# Kümelerde Temel Kavramlar

**Bu dersin sonunda:** bir topluluğun küme olup olmadığına karar verebilecek, bir kümeyi liste, Venn şeması ve ortak özellik yöntemiyle yazabilecek, eleman sayısını tekrarlara ve boş kümeye düşmeden bulabileceksin.

> **TYT'de yeri:** Bu konu tek başına az soru olur; ama bütün küme sorularının dilidir. "Ortak özelliği verilen kümenin eleman sayısı", "hangisi boş kümedir?", "$\{\emptyset\}$ kaç elemanlıdır?" ve yeni tanımlanan bir kümeyi (rakam kümesi, harf kümesi gibi) yorumlama kalıpları gelir.

## Önce hatırla

<details><summary>Tanım, aksiyom, teorem dersinden: Nokta, doğru ve düzlem neden tanımlanmaz, ne tür terimlerdir?</summary>
Bunlar <b>tanımsız terimlerdir</b>: başka bir terime ihtiyaç duymadan anlaşılırlar. Diğer kavramlar (doğru parçası, açı, üçgen) bu tanımsız terimler kullanılarak tanımlanır.
</details>

<details><summary>Tanım, aksiyom, teorem dersinden: "Bir dörtgen kare ise köşegenleri eşit uzunluktadır." teoreminin hipotezi ve hükmü nedir?</summary>
Teorem $p \Rightarrow q$ biçimindedir. <b>Hipotez</b> $p$: "Dörtgen karedir." <b>Hüküm</b> $q$: "Köşegenleri eşit uzunluktadır." İspatta hipotezden yola çıkıp hükmün doğru olduğu gösterilir.
</details>

## Küme nedir?

**Örnek.** Hangileri bir küme belirtir?

- "Türkiye'ye komşu olan ülkeler": Bir ülkenin bu topluluğa girip girmediği herkes için aynıdır. **Küme.**
- "10'dan küçük asal sayılar": $2, 3, 5, 7$. **Küme.**
- "Sınıfın uzun boylu öğrencileri": "Uzun" kişiden kişiye değişir; 1,75 m olan biri girer mi, belli değil. **Küme değil.**

Bir nesnenin topluluğa ait olup olmadığı kesin olarak söylenebiliyorsa topluluk **iyi tanımlanmıştır**. İyi tanımlanmış ve **birbirinden farklı** nesnelerin topluluğuna **küme**, bu nesnelerin her birine kümenin **elemanı** denir. Kümeler genellikle büyük harfle ($A$, $B$, $K$) adlandırılır.

**Örnek.** MATEMATİK kelimesinin harflerinden oluşan küme kaç elemanlıdır?

Kelimede 9 harf var ama M, A ve T ikişer kez geçiyor. Kümede her eleman **bir kez** yazılır: $\{M, A, T, E, \text{İ}, K\}$. Eleman sayısı **6**.

**Kural.** Kümede eleman tekrar yazılmaz ve sıranın önemi yoktur: $\{1, 2, 3\}$ ile $\{3, 1, 2, 1\}$ aynı kümedir.

> **Tuzak:** "Güzel", "zor", "büyük", "ünlü" gibi kişiye göre değişen sözcükler topluluğu iyi tanımlamaz. "En büyük beş il (nüfusa göre)" gibi ölçütü belli ifadeler ise küme belirtir.

## Eleman olmak ve eleman sayısı

**Örnek.** $A = \{3, \{3\}, \{4, 5\}\}$ olsun.

| İfade | Doğru mu? | Neden |
|---|---|---|
| $3 \in A$ | Doğru | $3$ listede tek başına yazılı. |
| $\{3\} \in A$ | Doğru | $\{3\}$ de listede bir eleman. |
| $4 \in A$ | Yanlış, $4 \notin A$ | $4$, $\{4, 5\}$ elemanının **içinde**; $A$'nın kendi elemanı değil. |
| $\{4, 5\} \in A$ | Doğru | Listede bir eleman. |
| $s(A) = 3$ | Doğru | Virgülle ayrılmış üç eleman var. |

$a \in A$ "$a$ elemanıdır $A$", $a \notin A$ "$a$ elemanı değildir $A$" diye okunur. $A$'nın eleman sayısı $s(A)$ ile gösterilir.

**Kural.** Eleman saymak için en dıştaki süslü parantezin içinde **virgülle ayrılmış parçaları** say. İçinde ne kadar eleman olursa olsun $\{4, 5\}$ gibi bir küme, bulunduğu kümede **tek eleman** sayılır.

## Kümelerin gösterimi

Aynı kümeyi üç yolla yazabiliriz. Örnek: $1$'den $10$'a kadar olan doğal sayılar içindeki asal sayılar.

**1. Liste yöntemi.** Elemanlar süslü parantez içinde, aralarına virgül konarak yazılır: $A = \{2, 3, 5, 7\}$.

**2. Venn şeması.** Elemanlar kapalı bir eğrinin içine, önlerine nokta konarak yazılır.

![Dikdörtgen içinde bir elips. Dikdörtgenin köşesinde E, elipsin üstünde A yazıyor. Elipsin içinde noktalarla 2, 3, 5, 7; dışında 1, 4, 6, 8, 9, 10 var.](gorsel/tyt-matematik/07-01-venn-asal.svg "Elips A kümesi, dikdörtgen evrensel küme E. Her elemanın önünde bir nokta var; 1, 4, 6, 8, 9, 10 E'de ama A'da değil.")

**3. Ortak özellik yöntemi.** Bütün elemanların paylaştığı özellik yazılır:

$$A = \{x \mid x \text{ asal sayı},\ 1 \le x \le 10\}$$

"$\mid$" işareti "öyle ki" diye okunur ve değişkenin hemen ardından gelir; yerine "$:$" da yazılabilir. Eleman sayısı çok olan ya da sonsuz olan kümelerde en kullanışlı yöntem budur.

## Ortak özellikten listeye

ÖSYM soruları en çok burada gelir. Her seferinde aynı adımları uygula:

![Yukarıdan aşağı beş adım: Değişken hangi kümede? Koşulu sağlayanları sırala. Kurala yerleştir. Tekrarları bir kez yaz. Elemanları say.](gorsel/tyt-matematik/07-01-ortak-ozellik.svg "Hataların çoğu ilk adımda (doğal sayı mı, tam sayı mı?) ve dördüncü adımda (tekrar eden değer) yapılır.")

**Örnek 1.** $A = \{x \mid x \in \mathbb{N},\ x < 4\}$

$x$ doğal sayı ve doğal sayılar $0$'dan başlar: $A = \{0, 1, 2, 3\}$, $s(A) = 4$.

**Örnek 2.** $B = \{2n + 1 \mid n \in \mathbb{N},\ n \le 3\}$

Burada koşul $n$ için verilmiş; $n = 0, 1, 2, 3$. Kurala yerleştir: $2 \cdot 0 + 1 = 1$, $3$, $5$, $7$. Yani $B = \{1, 3, 5, 7\}$. Elemanlar $n$ değil, $2n + 1$ değerleridir.

**Örnek 3.** $C = \{x^2 \mid x \in \mathbb{Z},\ -2 \le x \le 2\}$

$x = -2, -1, 0, 1, 2$. Kareleri: $4, 1, 0, 1, 4$. Tekrarlar bir kez yazılır: $C = \{0, 1, 4\}$, $s(C) = 3$; **5 değil**.

**Ters yön.** $D = \{3, 6, 9, \dots, 30\}$ kümesi $3$'ün katlarıdır: $D = \{3k \mid k \in \mathbb{N}^+,\ k \le 10\}$, $s(D) = 10$.

**Kural.** Önce değişkenin hangi sayı kümesinde olduğuna bak ($\mathbb{N}$, $\mathbb{N}^+$, $\mathbb{Z}$, $\mathbb{R}$), sonra koşulu sağlayan değerleri sırala, kurala yerleştir ve tekrar edenleri at.

## Sonlu, sonsuz ve evrensel küme

**Örnek.** Rakamlar kümesi $\{0, 1, 2, \dots, 9\}$ 10 elemanlıdır; eleman sayısı bir doğal sayı ile söylenebilir. Doğal sayılar kümesi $\mathbb{N}$'nin ise son elemanı yoktur.

- **Sonlu küme:** Eleman sayısı bir doğal sayı ile gösterilebilen küme. Örnek: rakamlar, Türkiye'nin illeri.
- **Sonsuz küme:** Sonlu olmayan küme. Örnek: $\mathbb{N}$, $\mathbb{Z}$, "$1$ ile $2$ arasındaki gerçek sayılar".
- **Evrensel küme ($E$):** Üzerinde çalışılan bütün kümeleri içine alacak biçimde seçilen küme. Venn şemasında dikdörtgenle çizilir. Yukarıdaki şemada $E = \{1, 2, \dots, 10\}$ idi.

> **Tuzak:** "$1$ ile $2$ arasındaki **gerçek** sayılar" sonsuzdur; "$1$ ile $2$ arasındaki **tam** sayılar" ise hiç eleman içermez. Tek kelime cevabı değiştirir.

## Boş küme

**Örnek.** $K = \{x \mid x \in \mathbb{N},\ x + 4 = 1\}$

$x + 4 = 1$ ise $x = -3$; ama $-3$ doğal sayı değil. Koşulu sağlayan hiçbir eleman yok: $K$ **boş kümedir**.

Elemanı olmayan kümeye **boş küme** denir; $\emptyset$ ya da $\{\ \}$ ile gösterilir ve $s(\emptyset) = 0$'dır. Boş küme sonlu bir kümedir.

Başka örnekler: $\{x \mid x \in \mathbb{Z},\ 3x = 5\}$ ($x = \frac{5}{3}$ tam sayı değil) ve $\{x \mid x \in \mathbb{R},\ x^2 = -4\}$ (karesi negatif gerçek sayı yok).

Kümeyi bir kutu gibi düşün. $\emptyset$ boş kutudur. $\{\emptyset\}$ ise **içinde boş bir kutu olan** kutudur; boş değildir.

![Üç kutu yan yana. İlki boş, üstünde boş küme işareti, altında 0 eleman. İkincinin içinde küçük boş bir kutu var, üstünde süslü parantez içinde boş küme, altında 1 eleman. Üçüncünün içinde 0 yazıyor, altında 1 eleman.](gorsel/tyt-matematik/07-01-bos-kume.svg "Kutunun içinde bir şey varsa, o şey boş bir kutu ya da 0 sayısı olsa bile, küme boş değildir.")

**Kural.** $\emptyset = \{\ \}$ boştur. $\{\emptyset\}$, $\{\{\ \}\}$ ve $\{0\}$ birer elemanlıdır, boş küme değildir.

## ÖSYM tuzakları

> **Tekrar edeni iki kez saymak:** $\{x^2 \mid x \in \mathbb{Z},\ -2 \le x \le 2\}$ kümesinde $x$ beş değer alır ama küme $\{0, 1, 4\}$, yani 3 elemanlıdır.

> **Sıfırı unutmak:** $\mathbb{N}$ sıfırla başlar. $\{x \mid x \in \mathbb{N},\ x < 4\}$ 4 elemanlıdır, 3 değil. Ayrıca $0$ her sayıya bölünür: "4'e bölünen doğal sayılar" listesine $0$ da girer.

> **İç içe kümeyi açmak:** $A = \{1, \{2, 3\}\}$ ise $2 \notin A$ ve $s(A) = 2$'dir. İçteki küme bütün olarak tek elemandır.

> **$\{\emptyset\}$'yi boş sanmak:** $\{\emptyset\}$ ve $\{\{\ \}\}$ bir elemanlıdır. Bir kümede hem $\emptyset$ hem $\{\ \}$ yazılıysa ikisi aynı elemandır, bir kez sayılır.

## Kendini dene

### Soru 1
$A = \{x \mid x \in \mathbb{N},\ x \le 3\}$ kümesinin liste yöntemiyle gösterimi aşağıdakilerden hangisidir?

A) $\{1, 2, 3\}$
B) $\{0, 1, 2, 3\}$
C) $\{0, 1, 2\}$
D) $\{1, 2\}$
E) $\{0, 1, 2, 3, 4\}$

**Cevap:** B
**Çözüm:** Doğal sayılar $0$'dan başlar ve $x \le 3$ olduğu için $3$ de dahildir: $\{0, 1, 2, 3\}$. A seçeneği $0$'ı unutmaktan, C seçeneği $3$'ü dışarıda bırakmaktan gelir.

### Soru 2
Aşağıdakilerden hangisi sonsuz bir kümedir?

A) 100'den küçük doğal sayılar
B) Karesi 50'den küçük tam sayılar
C) Türkiye'deki iller
D) Rakamlar
E) 0 ile 1 arasındaki rasyonel sayılar

**Cevap:** E
**Çözüm:** $0$ ile $1$ arasında $\frac{1}{2}, \frac{1}{3}, \frac{1}{4}, \dots$ gibi sonu gelmeyen rasyonel sayılar vardır. A 100, B 15 ($-7$'den $7$'ye), C 81, D 10 elemanlıdır; hepsi sonludur.

### Soru 3
$B = \{2k - 1 \mid k \in \mathbb{Z},\ -2 < k \le 3\}$ kümesinin elemanlarının toplamı kaçtır?

A) 0
B) 4
C) 5
D) 8
E) 9

**Cevap:** C
**Çözüm:** $k$ tam sayı ve $-2 < k \le 3$: $k = -1, 0, 1, 2, 3$. Kurala yerleştir: $-3, -1, 1, 3, 5$. Toplam $-3 - 1 + 1 + 3 + 5 = 5$. $k = -2$'yi de alan ($-5$ eklenir) 0, $k$'yi doğal sayı sanıp $-3$'ü atan 8 bulur.

## Özet kartı

- Küme: iyi tanımlanmış, birbirinden farklı nesneler. Eleman tekrar yazılmaz, sıra önemsizdir.
- $a \in A$: $a$, $A$'nın elemanı. $s(A)$: eleman sayısı. İç küme tek eleman sayılır.
- Gösterimler: liste $\{\ \}$, Venn şeması (nokta ile), ortak özellik $\{x \mid \dots\}$.
- Ortak özellikte: değişkenin kümesi, koşul, kurala yerleştir, tekrarı at, say.
- Sonlu, sonsuz; evrensel küme $E$ (Venn'de dikdörtgen).
- $\emptyset = \{\ \}$ boştur; $\{\emptyset\}$ ve $\{0\}$ bir elemanlıdır.

## Sonraki adım

Alıştırmaya geç (aşağıdaki düğme). Sonraki ders **Alt Küme**; bir kümenin bütün elemanlarının başka bir kümede bulunmasını ve alt küme sayısını göreceksin.
