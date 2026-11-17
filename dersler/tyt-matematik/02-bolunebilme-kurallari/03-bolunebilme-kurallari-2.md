---
baslik: Bölünebilme Kuralları 2
ders: tyt-matematik
sure: 20 dk
kaynak: MEBİ Konu Özeti afccf19128
guncelleme: 2026-11-18
---
# Bölünebilme Kuralları 2

<div class="giris" dir="rtl" lang="ar">

**الدرس ده عن إيه؟** بنكمّل قواعد قابلية القسمة (bölünebilme kuralları)، والمرة دي على أعداد زي 6 و12 و15 و24 و45.

- هتعرف تفكّ المقسوم عليه لعاملين أوليين فيما بينهما (aralarında asal) وتختبر كل قاعدة لوحدها.
- هتتعلم قاعدة القسمة على 25 من آخر رقمين، وإزاي تلاقي الأرقام المجهولة وتبدأ دايمًا من آخر رقم.
- هتعرف تجيب باقي القسمة (kalan) على 12 مثلًا من الباقي على 3 والباقي على 4.

**ليه مهم؟** تقريبًا في كل امتحان TYT بييجي سؤال من النوع ده، وفيه فخ مشهور: العدد اللي بيقبل القسمة على 4 و6 مش شرط يقبل القسمة على 24.

هي عشرين دقيقة بس، وبعدها هتحل الأسئلة دي وانت واثق من نفسك.

</div>

**Bu dersin sonunda:** 6, 12, 15, 18, 24, 30, 44, 45 gibi bir sayıya bölünebilmeyi aralarında asal iki çarpanın kurallarıyla sınayabilecek, 25 ile bölünebilmeyi son iki basamaktan okuyabilecek ve böyle bir sayıya bölümden kalanı küçük kalanlardan bulabileceksin.

> **TYT'de yeri:** Neredeyse her sınavda bir soru gelir. En sık kalıp: "Dört basamaklı $3a5b$ sayısı 12 ile tam bölünüyor, $a + b$ en çok kaçtır?" Bir de "3 ile bölümünden kalan 1, 4 ile bölümünden kalan 3 olan sayının 12 ile bölümünden kalan kaçtır?" kalıbı ve "4'e ve 6'ya bölünen sayı 24'e bölünür mü?" tuzağı sık görülür.

## Önce hatırla

<details><summary>Bölünebilme Kuralları 1'den: 52 836 sayısının 11 ile bölümünden kalan kaçtır?</summary>
Rakamları sağdan sola $+, -, +, -, +$ diye işaretle: $6 - 3 + 8 - 2 + 5 = 14$. $14$'ün 11 ile bölümünden kalan <b>3</b>.
</details>

<details><summary>Bölünebilme Kuralları 1'den: Dört basamaklı $2a51$ sayısı 3 ile tam bölünüyor ve $a$ çift rakam ise $a$ kaçtır?</summary>
Rakamlar toplamı $2 + a + 5 + 1 = 8 + a$ olmalı ve 3'ün katı olmalı: $a \in \{1, 4, 7\}$. Bunlardan çift olan <b>4</b>.
</details>

## Aralarında asal çarpanlar: 6 ile bölünebilme

**Örnek.** $5\,742$ sayısı 6 ile tam bölünür mü? $7\,435$ sayısı?

$6 = 2 \cdot 3$ ve 2 ile 3'ün 1'den başka ortak böleni yok. Bu yüzden iki kuralı ayrı ayrı sınarsın:

- $5\,742$: son rakam 2, çift; 2 ile bölünür. Rakamlar toplamı $5 + 7 + 4 + 2 = 18$; 3 ile bölünür. İkisi birden sağlandı: **6 ile tam bölünür** ($5\,742 = 6 \cdot 957$).
- $7\,435$: son rakam 5, tek; 2 ile bölünmez. 3'e bakmaya gerek yok: **6 ile bölünmez.**

**Kural.** $a$ ile $b$ **aralarında asal** ise (1'den başka ortak bölenleri yoksa), hem $a$'ya hem $b$'ye tam bölünen bir sayı $a \cdot b$'ye de tam bölünür. Bileşik bir sayıya bölünebilmeyi böyle iki koşula ayırırsın:

| Bölen | Ayırma | Sınanacak iki kural |
|---|---|---|
| 6 | $2 \cdot 3$ | son rakam çift, rakamlar toplamı 3'ün katı |
| 12 | $3 \cdot 4$ | son iki basamak 4'ün katı, rakamlar toplamı 3'ün katı |
| 15 | $3 \cdot 5$ | son rakam 0 ya da 5, rakamlar toplamı 3'ün katı |
| 18 | $2 \cdot 9$ | son rakam çift, rakamlar toplamı 9'un katı |
| 24 | $3 \cdot 8$ | son üç basamak 8'in katı, rakamlar toplamı 3'ün katı |
| 30 | $3 \cdot 10$ | son rakam 0, rakamlar toplamı 3'ün katı |
| 44 | $4 \cdot 11$ | son iki basamak 4'ün katı, 11 kuralı |
| 45 | $5 \cdot 9$ | son rakam 0 ya da 5, rakamlar toplamı 9'un katı |

Aynı yolla $20 = 4 \cdot 5$, $22 = 2 \cdot 11$, $33 = 3 \cdot 11$, $36 = 4 \cdot 9$, $72 = 8 \cdot 9$ için de kural kurarsın.

## Tuzak: çarpanlar aralarında asal olmalı

**Örnek.** Bir sayı hem 4'e hem 6'ya bölünüyor. 24'e bölünür mü?

$12$'yi dene: $12 = 4 \cdot 3 = 6 \cdot 2$, yani hem 4'e hem 6'ya bölünür; ama 24'e bölünmez. Demek ki **bölünmeyebilir**. Sebep: 4 ve 6'nın ortak böleni 2 var; $4 \cdot 6 = 24$ çarpımında bu 2 iki kez sayılmış olur.

![Sayı doğrusu 0'dan 48'e: üstte 4'ün katları mavi noktalarla, altta 6'nın katları sarı karelerle. 12, 24, 36 ve 48'de iki işaret üst üste geliyor ve yeşil çerçeveye alınmış; yalnızca 24 ve 48'in üstünde 24'ün katı yazıyor.](gorsel/tyt-matematik/02-03-ortak-katlar.svg "Yeşil çerçeveler iki koşulu birlikte sağlayan sayılardır: 12'nin katları. Bunların yalnızca yarısı 24'ün katıdır.")

Şekilde görüldüğü gibi 4'e ve 6'ya birlikte bölünen sayılar **12'nin katlarıdır** (12, 24, 36, 48, …). Bu yüzden 12 için $2 \cdot 6$ ayırması değil, $3 \cdot 4$ ayırması kullanılır; 24 için de $4 \cdot 6$ değil, $3 \cdot 8$.

![Akış şeması: böleni iki çarpana ayır; çarpanlar aralarında asal değilse başka iki çarpan seç; asalsa önce son basamak kuralına, sonra tüm basamaklar kuralına bak ve iki koşulu birlikte sağla.](gorsel/tyt-matematik/02-03-yontem.svg "Bilinmeyen rakam sorularında sıra önemlidir: önce son basamak kuralı bilinmeyeni birkaç değere indirir, sonra rakamlar toplamı ya da 11 kuralı uygulanır.")

## Bilinmeyen rakamlar: önce son basamak

**Örnek.** Dört basamaklı $2a7b$ sayısı 12 ile tam bölünüyor. $a + b$ en çok kaçtır?

1. $12 = 3 \cdot 4$. Önce son iki basamağa bak: $\overline{7b}$ sayısı 4'ün katı olmalı. $72$ ve $76$ uyar; $b \in \{2, 6\}$.
2. Sonra 3 kuralı: $2 + a + 7 + b = 9 + a + b$ toplamı 3'ün katı, yani $a + b$ 3'ün katı olmalı.
3. $b = 6$ ise $a \in \{0, 3, 6, 9\}$, en büyük toplam $9 + 6 = 15$. $b = 2$ ise $a \in \{1, 4, 7\}$, en büyük toplam $7 + 2 = 9$.

Cevap **15** ($2\,976 = 12 \cdot 248$).

**Örnek.** Dört basamaklı $3a52$ sayısı 44 ile tam bölünüyorsa $a$ kaçtır?

1. $44 = 4 \cdot 11$. Son iki basamak $52 = 4 \cdot 13$; 4 koşulu zaten sağlanıyor.
2. 11 kuralı, sağdan sola $+, -, +, -$: $2 - 5 + a - 3 = a - 6$. Bu 11'in katı olmalı; $a$ bir rakam olduğundan $a - 6 = 0$, **$a = 6$** ($3\,652 = 44 \cdot 83$).

**Kural.** Önce birler basamağına, sonra son iki ya da son üç basamağa bakan kuralı uygula; rakamlar toplamı ve 11 kuralını en sona bırak. Son basamak kuralı bilinmeyeni birkaç değere indirir, işin kalanı kısa olur.

## 25 ile bölünebilme

**Örnek.** Dört basamaklı $4ab5$ sayısı 75 ile tam bölünüyor. Bu koşula uyan kaç sayı vardır?

$100$, 25'in katı olduğu için bir sayının 25'e bölünmesi yalnızca **son iki basamağına** bağlıdır. Son iki basamak $00$, $25$, $50$ ya da $75$ olmalı.

1. $75 = 3 \cdot 25$. Son iki basamak $\overline{b5}$; 5 ile biten seçenekler $25$ ve $75$. $b \in \{2, 7\}$.
2. Rakamlar toplamı $4 + a + b + 5 = 9 + a + b$; $a + b$ 3'ün katı olmalı.
3. $b = 2$ ise $a \in \{1, 4, 7\}$; $b = 7$ ise $a \in \{2, 5, 8\}$.

Toplam **6** sayı: $4\,125$, $4\,425$, $4\,725$, $4\,275$, $4\,575$, $4\,875$.

**Kural.** Bir sayının son iki basamağı $00$, $25$, $50$ ya da $75$ ise sayı 25 ile tam bölünür. 25 ile bölümden kalan, son iki basamağın oluşturduğu sayının 25 ile bölümünden kalana eşittir (örneğin $8\,437$ için $37 - 25 = 12$).

## Kalanı küçük kalanlardan bulmak

**Örnek.** $43\,762$ sayısının 12 ile bölümünden kalan kaçtır?

$12 = 3 \cdot 4$, kalanı iki parçadan kurarsın:

- 4'e kalan: son iki basamak $62$; $62 = 4 \cdot 15 + 2$, kalan **2**.
- 3'e kalan: $4 + 3 + 7 + 6 + 2 = 22$; $22 = 3 \cdot 7 + 1$, kalan **1**.

12'ye kalan $r$, $0$ ile $11$ arasındadır. Aşağıdaki tabloda 3'e kalanı 1, 4'e kalanı 2 olan tek sütunu bul:

![Tablo: üst satırda 12'ye kalan 0'dan 11'e, altında her biri için 3'e kalan ve 4'e kalan. 10 sütunu kırmızı çerçeveli; 3'e kalan 1, 4'e kalan 2.](gorsel/tyt-matematik/02-03-kalan-tablosu.svg "Her sütunda 3'e ve 4'e kalan ikilisi farklıdır. Bu yüzden iki küçük kalan, 12'ye kalanı tek türlü belirler.")

Tabloyu ezberlemen gerekmez. Kısa yol: 4'e kalanı 2 olan adaylar $2, 6, 10$; bunlardan 3'e kalanı 1 olan **10**. Kontrol: $43\,762 = 12 \cdot 3\,646 + 10$.

Ters yön de aynı tablodan okunur: bir sayının 12 ile bölümünden kalan 10 ise, 10 hem 3'ten hem 4'ten büyük olduğu için 10'u bölersin: 3'e kalan $1$, 4'e kalan $2$.

**Kural.** $a$ ile $b$ aralarında asal ve $C = a \cdot b$ olsun.

- $x$'in $a$'ya ve $b$'ye kalanları biliniyorsa: büyük bölenin kalanına o bölenin katlarını ekleyerek $0$ ile $C - 1$ arası adayları yaz, öbür koşulu sağlayanı seç.
- $x$'in $C$'ye kalanı $r$ ise: $x$'in $a$'ya kalanı, $r$'nin $a$'ya kalanıdır; $b$ için de öyle.

## ÖSYM tuzakları

> **Aralarında asal olmayan çarpanlar:** "4'e ve 6'ya bölünüyor, o hâlde 24'e bölünür" yanlıştır; 12 bir karşı örnektir. Kesin olan yalnızca 12'ye bölünmesidir.

> **Kuralları yanlış sırada uygulamak:** $2a7b$ gibi sorularda önce rakamlar toplamına bakarsan iki bilinmeyenle uğraşırsın. Önce son basamak kuralıyla $b$'yi sınırla.

> **Yalnızca bir koşula bakmak:** 12 ile bölünebilmede son rakamın çift olması yetmez; son iki basamak 4'ün katı olmalı. $\overline{58}$ çifttir ama 4'ün katı değildir.

> **Kalanları toplamak ya da çarpmak:** 3'e kalanı 2, 5'e kalanı 4 olan sayının 15'e kalanı $2 + 4 = 6$ ya da $2 \cdot 4 = 8$ değildir. Adayları yaz: $4, 9, 14$; 3'e kalanı 2 olan **14**.

## Kendini dene

### Soru 1
Aşağıdaki sayılardan hangisi 15 ile tam bölünür?

A) 2 435
B) 3 573
C) 4 155
D) 5 225
E) 6 351

**Cevap:** C
**Çözüm:** 15 için hem 5 hem 3 koşulu gerekir. 5 koşulu: son rakam 0 ya da 5; B ve E elenir. 3 koşulu: $2 + 4 + 3 + 5 = 14$, $4 + 1 + 5 + 5 = 15$, $5 + 2 + 2 + 5 = 14$. Yalnızca $4\,155$'in toplamı 3'ün katı ($4\,155 = 15 \cdot 277$). B seçeneği 3'e bölünür ama 5'e bölünmez.

### Soru 2
Dört basamaklı $4a8b$ sayısı 30 ile tam bölünüyor. $a$ kaç farklı değer alabilir?

A) 3
B) 4
C) 5
D) 7
E) 10

**Cevap:** B
**Çözüm:** $30 = 3 \cdot 10$. 10 koşulu: $b = 0$. 3 koşulu: $4 + a + 8 + 0 = 12 + a$ toplamı 3'ün katı, yani $a$ 3'ün katı: $a \in \{0, 3, 6, 9\}$. 4 farklı değer. $a = 0$'ı unutan 3, bütün rakamları sayan 10 bulur.

### Soru 3
Bir $x$ doğal sayısının 3 ile bölümünden kalan 1, 4 ile bölümünden kalan 3'tür. $x$'in 12 ile bölümünden kalan kaçtır?

A) 3
B) 4
C) 5
D) 7
E) 11

**Cevap:** D
**Çözüm:** 12'ye kalan $0$ ile $11$ arasıdır. 4'e kalanı 3 olan adaylar: $3, 7, 11$. 3'e kalanları sırayla $0, 1, 2$. Koşulu sağlayan **7**. Kalanları toplayan $1 + 3 = 4$ bulur.

## Özet kartı

- Aralarında asal $a$ ve $b$'ye bölünen sayı $a \cdot b$'ye de bölünür: $6 = 2 \cdot 3$, $12 = 3 \cdot 4$, $15 = 3 \cdot 5$, $18 = 2 \cdot 9$, $24 = 3 \cdot 8$, $44 = 4 \cdot 11$.
- Çarpanlar ortak bölenli olursa kural çalışmaz: 4 ve 6'ya bölünen sayı 24'e değil, 12'ye bölünür.
- Bilinmeyen rakamda sıra: önce son basamak kuralı, sonra rakamlar toplamı ya da 11 kuralı.
- 25 ile bölünebilme: son iki basamak $00$, $25$, $50$ ya da $75$.
- Küçük kalanlardan büyük kalan: büyük bölenin kalanından aday listesi yaz, öbür kalanı tutanı seç.

## Sonraki adım

Alıştırmaya geç (aşağıdaki düğme). Sonraki ders **Asal Çarpanlar**; bir sayıyı asal çarpanlarına ayırarak hangi sayılara bölündüğünü tek bakışta görmeyi öğreneceksin.
