---
baslik: Bölünebilme Kuralları 1
ders: tyt-matematik
sure: 20 dk
kaynak: MEBİ Konu Özeti f7b60732c9
guncelleme: 2026-11-17
---
# Bölünebilme Kuralları 1

**Bu dersin sonunda:** bir sayıyı bölmeden 2, 3, 4, 5, 8, 9, 10 ve 11 ile bölümünden kalanı bulabilecek ve $\overline{4a7b}$ gibi sayılarda bilinmeyen rakamları bölünebilme koşulundan çözebileceksin.

> **TYT'de yeri:** Neredeyse her sınavda 1 soru gelir. Kalıplar: "bu sayının 9 ile bölümünden kalan kaçtır?", "$\overline{5a26}$ sayısı 11 ile tam bölündüğüne göre $a$ kaçtır?", "iki koşulu birlikte sağlayan $a$ değerlerinin toplamı kaçtır?". Ayrıca şifre, kod, paketleme gibi günlük hayat durumlarında da karşına çıkar.

## Önce hatırla

<details><summary>Kalanlı bölmeden: Bir doğal sayı 7'ye bölündüğünde bölüm 12, kalan 5 oluyor. Bu sayı kaçtır?</summary>
Bölünen = Bölen · Bölüm + Kalan: $7 \cdot 12 + 5 = 89$.
</details>

<details><summary>Kalanlı bölmeden: A'nın 9 ile bölümünden kalan 4, B'nin 9 ile bölümünden kalan 7'dir. A · B sayısının 9 ile bölümünden kalan kaçtır?</summary>
Sayıların yerine kalanları koyarsın: $4 \cdot 7 = 28$ ve $28 = 9 \cdot 3 + 1$. Kalan <b>1</b>. Bu derste de hep "sayının tamamı yerine kalanını veren küçük bir parçaya bakma" fikrini kullanacaksın.
</details>

## Neden bölmeden bulabiliriz?

$4738 = 473 \cdot 10 + 8$ yazabilirsin. $473 \cdot 10$ kısmı 2'ye ve 5'e tam bölünür, çünkü 10 bunlara bölünür. Kalanı yalnızca son rakam olan $8$ belirler. Aynı fikir $100 = 4 \cdot 25$ ve $1000 = 8 \cdot 125$ için de geçerlidir. 3, 9 ve 11'de ise bütün rakamlar işe karışır.

![Altı kutuda 5, 7, 3, 9, 2, 8 rakamları. Üstteki yeşil parantez bütün rakamları kapsıyor: rakam toplamı 3 ve 9 için, işaretli toplam 11 için. Alttaki parantezler sağdan: son 1 basamak 2, 5, 10 için; son 2 basamak 4 için; son 3 basamak 8 için.](gorsel/tyt-matematik/02-02-basamak-haritasi.svg "Bu dersin haritası: her bölen için sayının hangi parçasına bakacağını ezberle. Son basamak kuralları sağdan, toplam kuralları bütün rakamlardan çalışır.")

## 2, 5 ve 10 ile bölünebilme: son rakam

**Örnek.** $4738$ sayısının 2, 5 ve 10 ile bölümünden kalanları bul.

- 2 ile: son rakam 8 çift, sayı 2 ile tam bölünür. Kalan **0**.
- 5 ile: son rakam 8; $8 = 5 \cdot 1 + 3$. Kalan **3**.
- 10 ile: kalan doğrudan son rakamdır. Kalan **8**.

**Kural.** Sadece birler basamağına bak.

| Bölen | Tam bölünür, eğer son rakam… | Kalan |
|---|---|---|
| 2 | çiftse (0, 2, 4, 6, 8) | çiftse 0, tekse 1 |
| 5 | 0 ya da 5 ise | son rakamın 5 ile bölümünden kalan |
| 10 | 0 ise | son rakamın kendisi |

**Bilinmeyen rakam.** $\overline{73a}$ sayısı 5 ile tam bölünüyorsa $a \in \{0, 5\}$ olur.

## 4 ve 8 ile bölünebilme: son iki, son üç basamak

**Örnek.** $72538$ sayısının 4 ile bölümünden kalanı bul.

Son iki basamak $38$: $38 = 4 \cdot 9 + 2$. Kalan **2**.

**Örnek.** $13576$ sayısı 8 ile tam bölünür mü?

Son üç basamak $576 = 8 \cdot 72$. Evet, tam bölünür (kalan 0).

**Kural.** 4 için son iki basamağın oluşturduğu sayıya, 8 için son üç basamağın oluşturduğu sayıya bak. Sayının kalanı, o parçanın kalanına eşittir.

> **Tuzak:** $2534$ sayısının son rakamı 4 diye 4'e bölünür sanma: $34 = 4 \cdot 8 + 2$, kalan 2. Benzer şekilde $2316$ sayısının son iki basamağı $16$ 8'in katıdır ama 8 için son **üç** basamak gerekir: $316 = 8 \cdot 39 + 4$, kalan 4.

## 3 ve 9 ile bölünebilme: rakam toplamı

**Örnek.** $57482$ sayısının 3 ve 9 ile bölümünden kalanları bul.

Rakam toplamı: $5 + 7 + 4 + 8 + 2 = 26$.

- 3 ile: $26 = 3 \cdot 8 + 2$. Kalan **2**.
- 9 ile: $26 = 9 \cdot 2 + 8$. Kalan **8**.

**Kural.** Rakamları topla; sayının 3 (ya da 9) ile bölümünden kalan, bu toplamın 3 (ya da 9) ile bölümünden kalana eşittir. Rakam toplamı 9'un katı olan sayı 3'e de bölünür, ama tersi her zaman doğru değildir ($12$ sayısı 3'e bölünür, 9'a bölünmez).

**Bilinmeyen rakam.** $\overline{6a51}$ sayısı 9 ile tam bölünüyorsa $a$ kaçtır?

Rakam toplamı $12 + a$. $a$ bir rakam olduğu için $12 \le 12 + a \le 21$; bu aralıktaki tek 9 katı 18'dir. $12 + a = 18$, yani $a = 6$.

Aynı sayı yalnızca 3 ile tam bölünseydi: $12 + a \in \{12, 15, 18, 21\}$, yani $a \in \{0, 3, 6, 9\}$.

> **Tuzak:** Rakam toplamı **kalanın kendisi değildir**. $57482$ için "9 ile kalan 26" yazılamaz; 26'yı da 9'a bölmen gerekir.

## 11 ile bölünebilme: işaretli toplam

**Örnek.** $7352$ sayısının 11 ile bölümünden kalanı bul.

Rakamları **sağdan başlayarak** $+, -, +, -$ ile işaretle ve topla.

![7, 3, 5, 2 rakamları kutularda; sağdan başlayarak 2 artı, 5 eksi, 3 artı, 7 eksi işaretli. Altta işlem: 2 artı 3, eksi 5 artı 7, eşittir eksi 7; eksi 7 artı 11 eşittir 4, kalan 4.](gorsel/tyt-matematik/02-02-onbir-isaret.svg "İşaretleme birler basamağından başlar ve birler basamağı her zaman artıdır. Sonuç negatifse 11 ekleyerek kalanı bulursun.")

$$(2 + 3) - (5 + 7) = -7 \quad\Rightarrow\quad -7 + 11 = 4$$

Kalan **4**.

**Örnek.** $82918$ sayısı 11 ile tam bölünür mü?

Sağdan: $8 - 1 + 9 - 2 + 8 = 22$. $22 = 11 \cdot 2$, kalan 0. Evet, tam bölünür.

**Kural.** Sağdan başlayıp $+, -, +, -, \dots$ işaretiyle toplanır. Sonuç 11'in katıysa sayı 11'e tam bölünür; değilse sonucun 11 ile bölümünden kalan, sayının kalanıdır. Sonuç negatifse **11'in katlarını ekleyerek** $0$ ile $10$ arasına getir.

> **Tuzak:** Soldan başlamak. $7352$ için soldan $7 - 3 + 5 - 2 = 7$ bulunur ve kalan 7 sanılır; doğrusu 4'tür. Basamak sayısı çiftse soldan başlamak sonucun işaretini ters çevirir. Tam bölünme sorusunda sonuç değişmez ama **kalan** sorusunda değişir. Hep sağdan başla.

## Birden fazla kural birlikte

Bir sayı $k$ ile tam bölünüyorsa $k$'nin bütün bölenlerine de tam bölünür: 8'e bölünen sayı 4'e ve 2'ye, 9'a bölünen sayı 3'e de bölünür.

**Örnek.** Dört basamaklı $\overline{4a7b}$ sayısı hem 5 hem 9 ile tam bölünüyor. $a$'nın alabileceği değerler nelerdir?

1. Önce son basamak kuralı (5): $b \in \{0, 5\}$. Seçenekleri azaltan kural budur, onunla başla.
2. Sonra rakam toplamı (9): toplam $4 + a + 7 + b = 11 + a + b$.
   - $b = 0$: $11 + a$ 9'un katı olmalı, $11 + a = 18$, $a = 7$.
   - $b = 5$: $16 + a$ 9'un katı olmalı, $16 + a = 18$, $a = 2$ ($16 + a = 27$ için $a = 11$ olur, rakam değil).

$a \in \{2, 7\}$. Sayılar $4275$ ve $4770$; ikisini de kontrol et: $4275 = 9 \cdot 475$, $4770 = 9 \cdot 530$.

![Yukarıdan aşağı beş kutu: son basamak (2, 5, 10), son 2-3 basamak (4, 8), rakam toplamı (3, 9), işaretli toplam (11), adayları birlikte dene.](gorsel/tyt-matematik/02-02-yontem.svg "Birden fazla koşul varsa bu sırayla ilerle: önce adayları en çok azaltan son basamak kuralları, en son bütün rakamları kullanan kurallar.")

**Kural.** Önce son basamağa, sonra son iki ve son üç basamağa, en son bütün rakamlara bakan kuralı uygula. Her durum için ayrı satır aç; rakamın 0 ile 9 arasında olduğunu, ilk rakamın 0 olamayacağını unutma.

## ÖSYM tuzakları

> **Yanlış parçaya bakmak:** 4 için son iki, 8 için son üç basamak gerekir. Son rakama ya da son iki basamağa bakıp 8 kuralını uygulamak en sık hatadır.

> **Rakam toplamını kalan sanmak:** Rakam toplamını da 3'e ya da 9'a bölmeyi unutma.

> **11'de soldan başlamak ve negatif sonuç:** İşaretleme sağdan başlar. $-7$ gibi bir sonuçta kalan 7 değil, $-7 + 11 = 4$'tür.

> **Bir durumu atlamak:** $\overline{4a7b}$ örneğinde $b = 0$ durumunu unutan $a = 7$ değerini kaçırır. Ortadaki ve sondaki rakam 0 olabilir; yalnızca ilk rakam 0 olamaz. "Kaç değer?" sorularında 0'ı da dene.

## Kendini dene

### Soru 1
$6\,253\,714$ sayısının 8 ile bölümünden kalan kaçtır?

A) 1
B) 2
C) 4
D) 6
E) 7

**Cevap:** B
**Çözüm:** 8 için son üç basamağa bakılır: $714 = 8 \cdot 89 + 2$. Kalan 2. Yalnızca son iki basamağa ($14$) bakan $14 = 8 + 6$ ile 6, son rakamı kalan sanan 4 bulur.

### Soru 2
Dört basamaklı $\overline{7a43}$ sayısı 3 ile tam bölünmektedir. Buna göre $a$'nın alabileceği değerlerin toplamı kaçtır?

A) 4
B) 7
C) 11
D) 12
E) 15

**Cevap:** D
**Çözüm:** Rakam toplamı $7 + a + 4 + 3 = 14 + a$, 3'ün katı olmalı. $14 + a \in \{15, 18, 21\}$, yani $a \in \{1, 4, 7\}$. Toplam $1 + 4 + 7 = 12$. 9 kuralını uygulayan yalnızca $a = 4$ bulur.

### Soru 3
Dört basamaklı $\overline{6a74}$ sayısı 11 ile tam bölünmektedir. Buna göre $a$ kaçtır?

A) 2
B) 4
C) 5
D) 7
E) 9

**Cevap:** E
**Çözüm:** Sağdan işaretle: $4 - 7 + a - 6 = a - 9$. Bu 11'in katı olmalı; $a$ rakam olduğundan $a - 9 = 0$, $a = 9$. Kontrol: $6974 = 11 \cdot 634$. Rakamların hepsini toplayan ($17 + a = 22$) 5 bulur.

## Özet kartı

- 2, 5, 10: son rakam. 4: son iki basamak. 8: son üç basamak.
- 3 ve 9: rakam toplamı; toplamı da 3'e ya da 9'a bölüp kalanı bul.
- 11: sağdan $+, -, +, -$; sonuç negatifse 11 ekle.
- Sayının kalanı, bakılan parçanın kalanına eşittir.
- $k$'ya bölünen sayı $k$'nin bütün bölenlerine de bölünür.
- Birden fazla koşulda önce son basamak kuralı, sonra toplam kuralları; her durumu ayrı yaz.

## Sonraki adım

Alıştırmaya geç (aşağıdaki düğme). Gerçek çıkmış sorular için MEBİ'deki "Çıkmış Sorular" testine ve ÖSYM'nin resmî kitapçıklarına bak. Sonraki ders **Bölünebilme Kuralları 2**; orada 6, 12, 15, 18 gibi sayılara bölünebilmeyi, bu dersteki kuralları aralarında asal çarpanlarla birleştirerek bulacaksın.
