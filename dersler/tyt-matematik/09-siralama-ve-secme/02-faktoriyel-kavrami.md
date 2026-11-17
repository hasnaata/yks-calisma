---
baslik: Faktöriyel Kavramı
ders: tyt-matematik
sure: 20 dk
kaynak: MEBİ Konu Özeti aa423e9603
guncelleme: 2026-11-17
---
# Faktöriyel Kavramı

**Bu dersin sonunda:** faktöriyelli bölme, toplama ve çıkarma işlemlerini açmadan sadeleştirebilecek, $n!$ içinde bir asal çarpanın kaç kez bulunduğunu ve $n!$ sayısının sonunda kaç sıfır olduğunu bulabileceksin.

> **TYT'de yeri:** Faktöriyel permütasyon ve kombinasyonun dilidir; her sayma sorusunda karşına çıkar. Tek başına sorulduğunda kalıplar bellidir: "$\frac{12!}{10!}$ kaçtır?", "$\frac{9! - 8!}{7!}$ işleminin sonucu", "$n!$ sayısının sonunda kaç sıfır var?", "$k$ en çok kaçtır?" ve birler basamağı soruları.

## Önce hatırla

<details><summary>Saymanın temel ilkesinden: A kentinden B kentine 3 farklı yol, B'den C'ye 4 farklı yol var. A'dan B'ye uğrayarak C'ye kaç farklı şekilde gidilir?</summary>
İki aşama art arda yapılıyor; seçenekler çarpılır: $3 \cdot 4 = 12$.
</details>

<details><summary>Saymanın temel ilkesinden: 5 kişinin katıldığı bir yarışmada birinci, ikinci ve üçüncü kaç farklı şekilde belirlenebilir?</summary>
Birinci 5 kişiden biri, ikinci kalan 4 kişiden biri, üçüncü kalan 3 kişiden biri: $5 \cdot 4 \cdot 3 = 60$.
</details>

## Faktöriyel nedir?

**Örnek.** 4 farklı kitabı rafa yan yana kaç farklı şekilde dizebilirsin?

Saymanın temel ilkesiyle yerleri tek tek doldur. 1. yere 4 kitaptan biri, 2. yere kalan 3 kitaptan biri, 3. yere kalan 2 kitaptan biri, son yere kalan 1 kitap gelir:

$$4 \cdot 3 \cdot 2 \cdot 1 = 24$$

![Yan yana dört kutu: içlerinde 4, 3, 2, 1 yazıyor, aralarında çarpma noktası var ve sonunda eşittir 4 faktöriyel eşittir 24 yazıyor.](gorsel/tyt-matematik/09-02-kutu-yontemi.svg "Her yere bir kitap konunca seçenek bir azalır. 1'e kadar inen bu çarpımın kısa adı 4! (4 faktöriyel).")

1'den $n$'ye kadar olan doğal sayıların çarpımına **$n$ faktöriyel** (çarpansal) denir ve $n!$ ile gösterilir:

$$n! = 1 \cdot 2 \cdot 3 \cdot \ldots \cdot (n-1) \cdot n$$

**Kural.** Birbirinden farklı $n$ nesne yan yana $n!$ farklı şekilde sıralanır. Ayrıca $0! = 1$ ve $1! = 1$ kabul edilir.

| $n$ | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 |
|---|---|---|---|---|---|---|---|---|---|
| $n!$ | 1 | 1 | 2 | 6 | 24 | 120 | 720 | 5040 | 40 320 |

Bu tabloyu ezberle; $7!$'e kadar olan değerler sorularda hesap yaptırmadan kullanılır. İki gözlem:

- $n \ge 2$ ise $n!$ **çift** sayıdır (içinde 2 çarpanı var).
- $n \ge 5$ ise $n!$ içinde hem 2 hem 5 bulunur, yani $n!$ **10'a bölünür** ve birler basamağı $0$'dır.

## Bölme: büyüğü küçüğe kadar aç

**Örnek.** $\dfrac{10!}{8!}$ kaçtır?

$10!$'i tamamen hesaplamana gerek yok. $10! = 10 \cdot 9 \cdot 8!$ diye yaz, $8!$ sadeleşir:

$$\frac{10!}{8!} = \frac{10 \cdot 9 \cdot 8!}{8!} = 10 \cdot 9 = 90$$

**Kural.** $n! = n \cdot (n-1)!$. Büyük faktöriyeli, küçük olana ulaşana kadar aç; ortak faktöriyel sadeleşir.

**Örnek.** $\dfrac{n!}{(n-2)!} = 30$ ise $n$ kaçtır?

$n! = n \cdot (n-1) \cdot (n-2)!$ olduğundan sol taraf $n(n-1)$ olur. Ardışık iki sayının çarpımı $30$: $6 \cdot 5 = 30$, yani $n = 6$.

Bu tür denklemlerde ikinci dereceden denklem çözme; çarpımı **ardışık sayılara** ayır.

## Toplama ve çıkarma: en küçüğü paranteze al

**Örnek.** $\dfrac{9! - 8!}{7!}$ kaçtır?

Paydaki en küçük faktöriyel $8!$. Her terimi $8!$ cinsinden yaz: $9! = 9 \cdot 8!$.

$$9! - 8! = 9 \cdot 8! - 1 \cdot 8! = 8!\,(9 - 1) = 8 \cdot 8!$$

Şimdi bölme kuralı: $8! = 8 \cdot 7!$.

$$\frac{8 \cdot 8!}{7!} = \frac{8 \cdot 8 \cdot 7!}{7!} = 64$$

**Kural.** Faktöriyellerin toplamında ya da farkında **en küçük faktöriyeli** ortak paranteze al. Parantezin içinde küçük sayılar kalır.

Aynı yolla: $4! + 5! + 6! = 4!\,(1 + 5 + 5 \cdot 6) = 4! \cdot 36$.

![Yöntem şeması: faktöriyelli ifade üç dala ayrılıyor. Bölme ya da çarpmada büyüğü küçüğe kadar aç; toplama ya da çıkarmada en küçüğü paranteze al; asal çarpan sayısında art arda böl, topla.](gorsel/tyt-matematik/09-02-yontem.svg "Önce ifadenin türüne bak, sonra yöntemi seç. Hiçbir yolda büyük faktöriyeli sonuna kadar hesaplamazsın.")

## $n!$ içinde bir asal çarpan kaç tane?

**Örnek.** $40! = 2^k \cdot A$ ($k$ ve $A$ doğal sayı) eşitliğinde $k$ en çok kaçtır?

$1 \cdot 2 \cdot \ldots \cdot 40$ çarpımında kaç tane 2 çarpanı olduğunu sayıyoruz.

- 2'nin katları (2, 4, 6, …, 40): $40 : 2 = 20$ tane, her biri en az bir 2 verir.
- 4'ün katları ikinci bir 2 verir: $20 : 2 = 10$ tane.
- 8'in katları üçüncü bir 2 verir: $10 : 2 = 5$ tane.
- 16'nın katları: $5 : 2 = 2$ (kalan atılır); 32'nin katları: $2 : 2 = 1$.

Toplam: $20 + 10 + 5 + 2 + 1 = 38$. Yani $k$ en çok $38$'dir.

![Ardışık bölme merdiveni: 40, 2'ye bölünüyor ve bölümler 20, 10, 5, 2, 1 olarak alt alta iniyor; altta 20 artı 10 artı 5 artı 2 artı 1 eşittir 38 yazıyor.](gorsel/tyt-matematik/09-02-bolme-merdiveni.svg "Kalanlar önemsiz, yalnızca halkalı bölümleri topla. Bölüm, bölen asaldan küçük olunca dur.")

**Kural.** $p$ asal olmak üzere $n!$ içindeki $p$ çarpanı sayısını bulmak için $n$'yi, bölüm $p$'den küçük olana kadar art arda $p$'ye böl ve **bölümleri topla**.

Bu yalnızca **asal** sayı için çalışır. $12^k$ gibi bir sayı sorulursa önce asal çarpanlarına ayır ($12 = 2^2 \cdot 3$), her asalı ayrı say, sonra hangisinin önce bittiğine bak.

## $n!$ sayısının sonundaki sıfırlar

Her sondaki sıfır bir $10 = 2 \cdot 5$ çarpanından gelir. $n!$ içinde 2'ler her zaman 5'lerden fazladır, bu yüzden **sıfır sayısı = 5 çarpanı sayısı**.

**Örnek.** $100!$ sayısının sonunda kaç sıfır vardır?

$100 : 5 = 20$, $20 : 5 = 4$, $4 < 5$ dur. Toplam $20 + 4 = 24$ sıfır.

![Basamaklı grafik: yatay eksende n 0'dan 30'a, dikey eksende n faktöriyelin sonundaki sıfır sayısı. Her 5'te bir artıyor; 25'te 4'ten 6'ya iki birden sıçrıyor.](gorsel/tyt-matematik/09-02-sifir-basamaklari.svg "Sıfır sayısı her 5'in katında artar. 25'te iki tane 5 geldiği için 5 sıfırlı bir faktöriyel hiç yoktur.")

**Kural.** $n!$ sonundaki sıfır sayısı, $n$'yi art arda 5'e bölüp bölümleri toplayarak bulunur.

## Birler basamağı

**Örnek.** $1! + 2! + 3! + \ldots + 20!$ toplamının birler basamağı kaçtır?

$5!$ ve sonrası 0 ile biter, birler basamağına etki etmez. Yalnızca ilk dört terime bak: $1 + 2 + 6 + 24 = 33$. Birler basamağı **3**.

**Kural.** Faktöriyel toplamının birler basamağında yalnızca $4!$'e kadar olan terimler sayılır.

## ÖSYM tuzakları

> **$0! = 0$ sanmak:** $0! = 1$'dir. $0! + 1! = 2$ olur, $1$ değil.

> **Faktöriyelleri sayı gibi çıkarmak:** $9! - 8! \ne 1!$ ve $\frac{10!}{5!} \ne 2!$. Faktöriyelde toplama, çıkarma ve bölme içeri girmez; en küçüğü paranteze al ya da büyüğü aç.

> **Yalnızca ilk bölümü almak:** $100!$ sonundaki sıfır $100 : 5 = 20$ değil, $20 + 4 = 24$'tür. $25$, $50$, $75$, $100$ ikişer tane 5 getirir.

> **Asal olmayan sayıya bölmek:** $40!$ içindeki 4 çarpanı sayılırken $40$'ı 4'e bölmek yanlıştır. Önce 2'leri say ($38$), sonra $4 = 2^2$ olduğu için $38 : 2 = 19$ tane 4 vardır.

> **25'teki sıçramayı unutmak:** $24!$ sonunda 4, $25!$ sonunda 6 sıfır vardır. "Sonunda tam 5 sıfır olan $n!$" yoktur.

## Kendini dene

### Soru 1
$\dfrac{12!}{10!}$ işleminin sonucu kaçtır?

A) 2
B) 22
C) 110
D) 132
E) 156

**Cevap:** D
**Çözüm:** $12! = 12 \cdot 11 \cdot 10!$ olduğundan $\frac{12!}{10!} = 12 \cdot 11 = 132$. $2$, faktöriyelleri sayı gibi çıkarmaktan ($12 - 10$); $110$, $11 \cdot 10$ almaktan; $156$, $13 \cdot 12$ almaktan gelir.

### Soru 2
$\dfrac{7! - 6!}{5!}$ işleminin sonucu kaçtır?

A) 6
B) 36
C) 42
D) 120
E) 210

**Cevap:** B
**Çözüm:** En küçüğü paranteze al: $7! - 6! = 6!\,(7 - 1) = 6 \cdot 6!$. Sonra $6! = 6 \cdot 5!$: $\frac{6 \cdot 6 \cdot 5!}{5!} = 36$. Kontrol: $\frac{5040 - 720}{120} = \frac{4320}{120} = 36$. $42$, yalnızca $\frac{7!}{5!}$ hesaplamaktır; $6$, yalnızca $\frac{6!}{5!}$.

### Soru 3
$40!$ sayısının sonunda kaç tane sıfır vardır?

A) 4
B) 8
C) 9
D) 10
E) 16

**Cevap:** C
**Çözüm:** Sıfır sayısı 5 çarpanı sayısıdır: $40 : 5 = 8$, $8 : 5 = 1$ (kalan atılır), $1 < 5$ dur. $8 + 1 = 9$. $8$, ikinci bölümü (25'in getirdiği fazladan 5'i) unutmaktır; $4$, $40$'ı 10'a bölmektir.

## Özet kartı

- $n! = 1 \cdot 2 \cdot \ldots \cdot n$; $0! = 1! = 1$. Farklı $n$ nesne $n!$ şekilde sıralanır.
- $n! = n \cdot (n-1)!$: bölmede büyüğü küçüğe kadar aç.
- Toplama ve çıkarmada en küçük faktöriyeli ortak paranteze al.
- $n!$ içindeki $p$ asal çarpanı: $n$'yi art arda $p$'ye böl, bölümleri topla.
- Sondaki sıfır sayısı = 5 çarpanı sayısı. $n \ge 5$ ise $n!$ 0 ile biter.
- Faktöriyel toplamının birler basamağında yalnızca $1!$–$4!$ önemlidir.

## Sonraki adım

Alıştırmaya geç (aşağıdaki düğme). Sonraki ders **Permütasyon**; $n$ nesneden $r$ tanesini sıralamayı $\frac{n!}{(n-r)!}$ ile yazacak ve bu dersteki sadeleştirmeyi her soruda kullanacaksın.
