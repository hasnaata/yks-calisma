---
baslik: Temel İşlemler
ders: tyt-matematik
sure: 20 dk
kaynak: MEBİ Konu Özeti d864386300
guncelleme: 2026-11-17
---
# Temel İşlemler

**Bu dersin sonunda:** işaretli sayılarla dört işlemi doğru işaretle yapabilecek, uzun bir ifadeyi işlem önceliğine göre hatasız sadeleştirebilecek ve dağılma özelliğiyle hesabı kısaltabileceksin.

> **TYT'de yeri:** Bu konu çoğu zaman ayrı bir soru olmaz; ama her sorunun içindedir. Doğrudan gelen kalıplar: "işlemin sonucu kaçtır?" (öncelik ve işaret tuzağıyla), "$47 \cdot 98$ gibi bir çarpımı kısa yoldan bul", "hangi eşitlik her zaman doğrudur?" ve tuşlara ya da kartlara sayı yerleştirilen yeni nesil sorular.

## Önce hatırla

<details><summary>Sayı kümelerinden: $-4,\ 0,\ \frac{7}{2},\ \sqrt{16},\ \sqrt{5},\ \pi$ sayılarından kaç tanesi tam sayıdır, kaç tanesi irrasyoneldir?</summary>
$\sqrt{16} = 4$ olduğu için tam sayılar $-4$, $0$ ve $\sqrt{16}$: <b>3 tane</b>. $\frac{7}{2}$ rasyoneldir ama tam sayı değildir. İki tam sayının oranı olarak yazılamayanlar $\sqrt{5}$ ve $\pi$: <b>2 tane</b> irrasyonel.
</details>

<details><summary>Sayı kümelerinden: Her doğal sayı bir rasyonel sayı mıdır? $\sqrt{-9}$ hangi sayı kümesindedir?</summary>
Evet: $\mathbb{N} \subset \mathbb{Z} \subset \mathbb{Q} \subset \mathbb{R}$ ve her $n$ doğal sayısı $\frac{n}{1}$ biçiminde yazılır. $\sqrt{-9}$ ise <b>gerçek sayı değildir</b>, bu kümelerin hiçbirinde yoktur.
</details>

## İşaretli sayılarla toplama

**Örnek.** $-7 + 4$ kaçtır?

Sayı doğrusunda $-7$'den başla. $+4$ demek **4 birim sağa** git demektir. Vardığın yer $-3$. Benzer şekilde $3 + (-8)$ işleminde $3$'ten **8 birim sola** gidersin ve $-5$'e varırsın.

![İki sayı doğrusu. Üstte eksi 7'den 4 birim sağa giden mavi ok eksi 3'te biter. Altta 3'ten 8 birim sola giden kırmızı ok eksi 5'te biter.](gorsel/tyt-matematik/01-02-sayi-dogrusu-toplama.svg "Pozitif sayı eklemek sağa, negatif sayı eklemek sola gitmektir. Sonuç, uzun okun yönündeki tarafta kalır.")

Kısa yol: işaretler farklıysa büyük mutlak değerden küçüğü çıkar, sonuca **mutlak değerce büyük olanın işaretini** ver.

- $-7 + 4$: $7 - 4 = 3$, büyük olan $-7$ negatif, sonuç $-3$.
- $3 + (-8)$: $8 - 3 = 5$, büyük olan $-8$ negatif, sonuç $-5$.
- İşaretler aynıysa mutlak değerler toplanır, işaret korunur: $-5 + (-6) = -11$.

Çıkarma, tersini eklemektir: $4 - (-9) = 4 + 9 = 13$.

**Kural.** Farklı işaretli iki sayının toplamının işareti, mutlak değerce büyük olanın işaretidir. $a - b = a + (-b)$.

## İşaretli sayılarla çarpma ve bölme

**Örnek.** $(-2) \cdot (-3) \cdot (-1) \cdot 5$ kaçtır?

Önce işarete bak: 3 tane negatif çarpan var. İkisi birbirini pozitife çevirir, biri kalır; sonuç negatif. Sonra sayılar: $2 \cdot 3 \cdot 1 \cdot 5 = 30$. Sonuç $-30$.

| İşlem | Sonucun işareti |
|---|---|
| $(+) \cdot (+)$ ve $(-) \cdot (-)$ | $+$ |
| $(+) \cdot (-)$ ve $(-) \cdot (+)$ | $-$ |
| $(+) : (+)$ ve $(-) : (-)$ | $+$ |
| $(+) : (-)$ ve $(-) : (+)$ | $-$ |

**Kural.** Aynı işaretliler çarpılır ya da bölünürse sonuç pozitif, farklı işaretlilerde negatiftir. Çok çarpanlı işlemde negatif çarpan sayısı **çiftse** sonuç pozitif, **tekse** negatiftir.

## İşlem önceliği

**Örnek.** $4 + (3 - 7)^2 : 2 \cdot 3 - 5$ işleminin sonucu kaçtır?

1. Parantez içi: $3 - 7 = -4$. İfade: $4 + (-4)^2 : 2 \cdot 3 - 5$.
2. Üs: $(-4)^2 = 16$. İfade: $4 + 16 : 2 \cdot 3 - 5$.
3. Çarpma ve bölme, **soldan sağa**: $16 : 2 = 8$, sonra $8 \cdot 3 = 24$. İfade: $4 + 24 - 5$.
4. Toplama ve çıkarma, soldan sağa: $4 + 24 - 5 = 23$.

![Yukarıdan aşağı dört kutu: parantez içi, üslü ifadeler, soldan sağa çarpma ve bölme, soldan sağa toplama ve çıkarma.](gorsel/tyt-matematik/01-02-islem-onceligi.svg "Her adımda bir alt kutuya inersin. Parantezin içinde de aynı sıra geçerlidir.")

**Kural.** Önce parantez içi (içinde de aynı sıra), sonra üs, sonra çarpma ve bölme, en son toplama ve çıkarma. Çarpma ile bölme **aynı öncelikte**dir; art arda geldiklerinde soldan sağa yapılır. Toplama ile çıkarma için de böyledir.

Üç sık hata:

- $30 : 5 \cdot 2 = 6 \cdot 2 = 12$. Önce çarpıp $30 : 10 = 3$ bulmak yanlıştır.
- $10 - 4 + 2 = 6 + 2 = 8$. Önce toplayıp $10 - 6 = 4$ bulmak yanlıştır. (Çıkarmayı negatif sayı eklemek olarak düşünürsen sıra serbesttir: $10 + (-4) + 2 = 8$.)
- $-3^2 = -9$ ama $(-3)^2 = 9$. Parantez yoksa üs yalnızca $3$'e uygulanır, eksi işareti dışarıda kalır.

## Toplama ve çarpmanın özellikleri

**Örnek.** $25 \cdot 17 \cdot 4$ işlemini kolay yoldan yap.

Çarpanların yerini değiştir ve uygun olanları grupla: $25 \cdot 4 \cdot 17 = 100 \cdot 17 = 1700$. Bunu yapabilmemizin nedeni çarpmanın **değişme** ve **birleşme** özelliğidir.

| Özellik | Toplama | Çarpma |
|---|---|---|
| Kapalılık | $a + b \in \mathbb{R}$ | $a \cdot b \in \mathbb{R}$ |
| Değişme | $a + b = b + a$ | $a \cdot b = b \cdot a$ |
| Birleşme | $(a + b) + c = a + (b + c)$ | $(a \cdot b) \cdot c = a \cdot (b \cdot c)$ |
| Birim (etkisiz) eleman | $0$: $a + 0 = a$ | $1$: $a \cdot 1 = a$ |
| Ters eleman | $-a$: $a + (-a) = 0$ | $\frac{1}{a}$ ($a \neq 0$): $a \cdot \frac{1}{a} = 1$ |
| Yutan eleman | yok | $0$: $a \cdot 0 = 0$ |

Bu tablodan çıkan dört not:

- **$0$'ın çarpma işlemine göre tersi yoktur**, çünkü $0 \cdot x = 1$ olan bir $x$ bulunamaz.
- Ters elemanlar karıştırılmasın: $-\frac{2}{5}$ sayısının toplamaya göre tersi $\frac{2}{5}$, çarpmaya göre tersi $-\frac{5}{2}$'dir. İşaret çarpmaya göre terste **değişmez**.
- Kapalılık kümeye bağlıdır: $\mathbb{R}$ toplama ve çarpmaya göre kapalıdır. Ama $3 - 5 = -2 \notin \mathbb{N}$ olduğu için $\mathbb{N}$ çıkarmaya göre, $3 : 4 \notin \mathbb{Z}$ olduğu için $\mathbb{Z}$ bölmeye göre kapalı değildir.
- **Çıkarma ve bölmede** değişme ve birleşme yoktur: $8 - 3 \neq 3 - 8$; $(12 : 6) : 2 = 1$ ama $12 : (6 : 2) = 4$.

## Dağılma özelliği

**Örnek.** $7 \cdot 13$ işlemini $13 = 10 + 3$ yazarak yap.

$7 \cdot (10 + 3) = 7 \cdot 10 + 7 \cdot 3 = 70 + 21 = 91$. Kenarları $7$ ve $13$ olan dikdörtgeni iki parçaya ayırınca alanlar toplanır.

![Bir kenarı 7, öbür kenarı 10 artı 3 olan dikdörtgen; 7'ye 10'luk mavi parçanın alanı 70, 7'ye 3'lük yeşil parçanın alanı 21.](gorsel/tyt-matematik/01-02-dagilma-alan.svg "Büyük dikdörtgenin alanı iki parçanın alanları toplamıdır: 7 · 13 = 70 + 21 = 91.")

**Kural.** Çarpma, toplama ve çıkarma üzerine dağılır:
$$a \cdot (b + c) = a \cdot b + a \cdot c \qquad a \cdot (b - c) = a \cdot b - a \cdot c$$

Soruda bu eşitlik çoğu zaman **tersinden** kullanılır, yani ortak çarpan dışarı alınır:

- $25 \cdot 38 + 25 \cdot 62 = 25 \cdot (38 + 62) = 25 \cdot 100 = 2500$
- $46 \cdot 99 = 46 \cdot (100 - 1) = 4600 - 46 = 4554$

Bölmede dikkat: $(20 + 8) : 4 = 20 : 4 + 8 : 4 = 7$ doğrudur. Ama bölen toplam olunca dağılma **olmaz**: $12 : (4 + 2) = 2$, oysa $12 : 4 + 12 : 2 = 9$.

## ÖSYM tuzakları

> **Çarpmayı bölmeden önce yapmak:** $30 : 5 \cdot 2$ işleminin sonucu $12$'dir, $3$ değil. Çarpma ile bölme eşit önceliklidir; soldan sağa git.

> **Üssü eksiye uygulamak:** $-2^4 = -16$, $(-2)^4 = 16$. Parantez yoksa eksi işareti üssün dışında kalır.

> **Çıkarmada parantezi açmayı unutmak:** $a - (b - c) = a - b + c$'dir. Parantezin önündeki eksi, içindeki **her** terimin işaretini değiştirir.

> **Bölmeyi paydadaki toplama dağıtmak:** $\frac{12}{4 + 2} \neq \frac{12}{4} + \frac{12}{2}$. Pay dağılır, payda dağılmaz.

> **$0$'ın tersini sormak:** $0$'ın toplamaya göre tersi $0$'dır; çarpmaya göre tersi yoktur.

## Kendini dene

### Soru 1
$20 - 8 : 4 \cdot 2$ işleminin sonucu kaçtır?

A) 4
B) 6
C) 16
D) 18
E) 19

**Cevap:** C
**Çözüm:** Önce çarpma ve bölme, soldan sağa: $8 : 4 = 2$, $2 \cdot 2 = 4$. Sonra $20 - 4 = 16$. Önce çarpıp $8 : 8 = 1$ alan 19, işlemi soldan sağa öncelik gözetmeden yapan $(20 - 8) : 4 \cdot 2 = 6$ bulur.

### Soru 2
$-3^2 - (-3)^2$ işleminin sonucu kaçtır?

A) $-18$
B) $-9$
C) $0$
D) $9$
E) $18$

**Cevap:** A
**Çözüm:** $-3^2 = -9$ (üs yalnızca 3'e uygulanır), $(-3)^2 = 9$. Sonuç $-9 - 9 = -18$. $-3^2$'yi $9$ sanan $9 - 9 = 0$ bulur.

### Soru 3
$73 \cdot 18 + 27 \cdot 18 - 18$ işleminin sonucu kaçtır?

A) 1764
B) 1782
C) 1800
D) 1818
E) 1836

**Cevap:** B
**Çözüm:** Üç terimde de $18$ çarpanı var; sondaki $18 = 1 \cdot 18$. Ortak çarpanı dışarı al: $18 \cdot (73 + 27 - 1) = 18 \cdot 99 = 1800 - 18 = 1782$. Son terimi unutan 1800 bulur.

## Özet kartı

- Farklı işaretlilerin toplamında büyük mutlak değerin işareti kalır; $a - b = a + (-b)$.
- Çarpma ve bölmede negatif sayısı çiftse sonuç pozitif, tekse negatif.
- Sıra: parantez, üs, çarpma ve bölme (soldan sağa), toplama ve çıkarma (soldan sağa).
- $-a^2 \neq (-a)^2$: parantez yoksa üs eksiye uygulanmaz.
- Birim elemanlar $0$ ve $1$; yutan eleman $0$; $0$'ın çarpmaya göre tersi yok.
- $a \cdot (b \pm c) = a \cdot b \pm a \cdot c$; ortak çarpanı dışarı almak hesabı kısaltır.

## Sonraki adım

Alıştırmaya geç (aşağıdaki düğme). Sonraki ders **Tek ve Çift Sayılar**; orada toplamanın ve çarpmanın sonucunu sayıları bilmeden, yalnızca tek ya da çift olmalarına bakarak bulacaksın.
