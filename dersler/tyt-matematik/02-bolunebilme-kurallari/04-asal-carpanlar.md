---
baslik: Asal Çarpanlar
ders: tyt-matematik
sure: 20 dk
kaynak: MEBİ Konu Özeti aa74283ccd
guncelleme: 2026-11-18
---
# Asal Çarpanlar

<div class="giris" dir="rtl" lang="ar">

**الدرس ده عن إيه؟** عن تحليل العدد لعوامله الأولية (asal çarpanlarına ayırma): إزاي تكتب أي عدد كحاصل ضرب أعداد أولية (asal sayılar) بالأُسس.

- هتتعلم طريقة القسمة المتتالية (bölme merdiveni) وتبدأ دايمًا بأصغر عدد أولي، يعني 2.
- هتعرف تحسب عدد القواسم الموجبة (pozitif bölen sayısı) من الأُسس بس: تزوّد كل أُس واحد وتضربهم في بعض.
- هتفرّق بين القواسم الموجبة والسالبة والصحيحة (tam sayı bölenleri)، وتعرف مجموع اللي مش أولية منها.

**ليه مهم؟** سؤال "العدد ده له كام قاسم؟" بييجي كتير في TYT، والتحليل ده هو أول خطوة في القاسم المشترك الأكبر والمضاعف المشترك الأصغر (EBOB - EKOK) والجذور والاختصار.

الدرس ٢٠ دقيقة بس، ولو مسكت الفكرة دي هتلاقي حاجات كتير بعدها بقت أسهل.

</div>

**Bu dersin sonunda:** bir sayıyı asal çarpanlarına ayırıp üslü biçimde yazabilecek, bu yazımdan sayının pozitif, negatif ve tam sayı bölenlerinin sayısını ve asal olmayan bölenlerinin toplamını bulabileceksin.

> **TYT'de yeri:** "Kaç pozitif böleni vardır?", "tam sayı bölenlerinin sayısı kaçtır?", "bölen sayısı verilen sayıda üs kaçtır?" kalıpları sık gelir. Asal çarpanlara ayırma ayrıca EBOB-EKOK, köklü sayılar ve sadeleştirme sorularının ilk adımıdır.

## Önce hatırla

<details><summary>Bölünebilme Kuralları 2'den: Bir sayı hem 4'e hem 6'ya tam bölünüyor. Bu sayı 24'e de kesinlikle tam bölünür mü?</summary>
Hayır. "İkisine bölünen çarpımlarına da bölünür" kuralı yalnızca <b>aralarında asal</b> sayılar için geçerlidir; 4 ile 6'nın ortak böleni 2'dir. Örneğin 12 hem 4'e hem 6'ya bölünür ama 24'e bölünmez. 24'e bölünmeyi aralarında asal olan 3 ve 8 ile kontrol ederiz.
</details>

<details><summary>Bölünebilme Kuralları 2'den: Bir x doğal sayısının 15 ile bölümünden kalan 13'tür. x'in 3 ile ve 5 ile bölümünden kalanlar kaçtır?</summary>
$15 = 3 \cdot 5$ ve kalan 13, hem 3'ten hem 5'ten büyük. Kalanı bölenlere böleriz: $13 = 3 \cdot 4 + 1$, $13 = 5 \cdot 2 + 3$. Kalanlar <b>1</b> ve <b>3</b>.
</details>

## Asal çarpanlarına ayırma

**Örnek.** 540'ı asal sayıların çarpımı olarak yaz.

Sayıyı **en küçük asal olan 2'den** başlayarak bölmeye devam et. 2'ye bölünmeyince 3'e, 3'e bölünmeyince 5'e geç. Bölüm 1 olunca dur. Bu dikey düzene **bölme merdiveni** denir.

![Bölme merdiveni: solda alt alta 540, 270, 135, 45, 15, 5, 1; sağda bölenler 2, 2, 3, 3, 3, 5. İki tane 2, üç tane 3 ve bir tane 5 gruplanmış; altta 540 eşittir 2 üssü 2 çarpı 3 üssü 3 çarpı 5 yazıyor.](gorsel/tyt-matematik/02-04-bolme-merdiveni.svg "Sağ sütundaki asalları say: kaç kez yazıldıysa o asalın üssü odur.")

2 iki kez, 3 üç kez, 5 bir kez kullanıldı:

$$540 = 2^2 \cdot 3^3 \cdot 5$$

**Kural.** $x, y, z$ birbirinden **farklı asal sayılar** olmak üzere bir sayıyı $A = x^a \cdot y^b \cdot z^c$ biçiminde yazmaya **asal çarpanlarına ayırma** denir. Üs, o asalın merdivende kaç kez kullanıldığını gösterir. $\{x, y, z\}$ kümesi $A$'nın **asal bölenleridir**; 540'ın asal bölenleri 2, 3 ve 5'tir.

**Kısa yol: sondaki sıfırlar.** $10 = 2 \cdot 5$ olduğundan $10^n = 2^n \cdot 5^n$ olur.

$$72000 = 72 \cdot 10^3 = (2^3 \cdot 3^2) \cdot (2^3 \cdot 5^3) = 2^6 \cdot 3^2 \cdot 5^3$$

Aynı tabandaki üsleri **topla**: $2^3 \cdot 2^3 = 2^6$. Sonuçta her asal yalnızca bir kez yazılmalı.

**Negatif sayılar.** $-540 = -1 \cdot 2^2 \cdot 3^3 \cdot 5$. İşaret bir $-1$ çarpanı olarak öne çıkar; asal bölenler yine 2, 3 ve 5'tir.

## Pozitif bölen sayısı

**Örnek.** $72 = 2^3 \cdot 3^2$ sayısının kaç pozitif böleni vardır?

72'nin her böleni $2^m \cdot 3^n$ biçimindedir. $2$'nin üssü $m$ için $0, 1, 2, 3$ (4 seçenek), $3$'ün üssü $n$ için $0, 1, 2$ (3 seçenek) vardır. Bunları bir tabloya dizersen her kutu bir bölen olur.

![4 satır 3 sütunluk tablo. Satır başlarında 1, 2, 4, 8; sütun başlarında çarpı 1, çarpı 3, çarpı 9. Kutularda 1, 3, 9; 2, 6, 18; 4, 12, 36; 8, 24, 72. İlk satır sarı ve tek bölenler olarak işaretli, diğer satırlar çift bölenler.](gorsel/tyt-matematik/02-04-bolen-tablosu.svg "Satır sayısı 3 + 1, sütun sayısı 2 + 1. Üsse 1 eklenmesinin nedeni üssün 0 da olabilmesidir.")

$4 \cdot 3 = 12$ pozitif bölen var.

**Kural.** $A = x^a \cdot y^b \cdot z^c$ ise

$$\text{pozitif bölen sayısı} = (a+1)(b+1)(c+1)$$

Her üsse 1 ekle, sonra çarp. Çarpanın kendisi (2, 3, 5) değil, yalnızca **üsler** kullanılır.

**Tek ve çift bölenler.** Tablonun ilk satırında 2'nin üssü 0'dır; bu satırdaki bölenler **tektir**: $1, 3, 9$. Tek bölen sayısını bulmak için 2'li çarpanı yok say: $2 + 1 = 3$. Çift bölen sayısı da $12 - 3 = 9$ olur.

**Tersinden soru.** $2^n \cdot 3^2$ sayısının 15 pozitif böleni varsa: $(n+1) \cdot (2+1) = 15$, yani $n + 1 = 5$ ve $n = 4$.

## Tam sayı bölenleri

**Örnek.** 12'nin bütün tam sayı bölenlerini yaz ve topla.

Pozitif bölenler: $1, 2, 3, 4, 6, 12$. Her birinin negatifi de 12'yi böler: $-1, -2, -3, -4, -6, -12$. Toplam 12 tam sayı bölen var.

![Sayı doğrusu: mavi noktalar 1, 2, 3, 4, 6, 12; kırmızı noktalar eksi 1, eksi 2, eksi 3, eksi 4, eksi 6, eksi 12. Her pozitif bölen, kendi negatifiyle bir yayla bağlanmış.](gorsel/tyt-matematik/02-04-tam-bolenler.svg "Her yay bir çift: 6 ile −6 gibi. Çiftlerin toplamı 0 olduğu için bütün tam sayı bölenlerin toplamı da 0'dır.")

Bölenler çiftler hâlinde birbirini götürür: toplam **0**.

**Kural.** $A = x^a \cdot y^b \cdot z^c$ için:

| Ne soruluyor? | Sonuç |
|---|---|
| Asal bölenler | $\{x, y, z\}$ |
| Pozitif bölen sayısı | $(a+1)(b+1)(c+1)$ |
| Negatif bölen sayısı | $(a+1)(b+1)(c+1)$ |
| Tam sayı bölen sayısı | $2 \cdot (a+1)(b+1)(c+1)$ |
| Tam sayı bölenlerin toplamı | $0$ |
| Asal olmayan tam sayı bölenlerin toplamı | $-(x + y + z)$ |

Son satırın nedeni: bütün tam sayı bölenlerin toplamı 0'dır. Bunların içinden asal olanları ($x, y, z$) çıkarırsan geriye $0 - (x + y + z)$ kalır. 12 için asal bölenler 2 ve 3 olduğundan asal olmayan tam sayı bölenlerin toplamı $-(2 + 3) = -5$'tir.

**Asal olmayan bölen sayısı.** 12'nin 6 pozitif böleninden 2'si asaldır; asal olmayan pozitif bölen sayısı $6 - 2 = 4$ olur: $1, 4, 6, 12$. 1 asal değildir, bu sayıya dahildir.

## ÖSYM tuzakları

> **Asal olmayan çarpanla yazmak:** $540 = 4 \cdot 27 \cdot 5$ doğru bir çarpımdır ama asal çarpanlara ayırma değildir. Bu yazımla bölen sayısını $2 \cdot 2 \cdot 2 = 8$ bulursun; doğrusu $(2+1)(3+1)(1+1) = 24$.

> **Üsse 1 eklemeyi unutmak:** $72 = 2^3 \cdot 3^2$ için $3 \cdot 2 = 6$ değil, $(3+1)(2+1) = 12$ bölen vardır. 1 eklenmesi, üssün 0 olabildiği durumu sayar.

> **Parçaların bölen sayılarını çarpmak:** $72000 = 72 \cdot 1000$ için "72'nin 12, 1000'in 16 böleni var, $12 \cdot 16 = 192$" yanlıştır; iki sayıda da 2 çarpanı var. Önce $2^6 \cdot 3^2 \cdot 5^3$ biçiminde birleştir: $7 \cdot 3 \cdot 4 = 84$.

> **Pozitif ile tam sayıyı karıştırmak:** "Tam sayı bölenleri" denince negatifler de sayılır, sonuç 2 katına çıkar. Soru kökünde "pozitif", "negatif", "tam sayı", "asal olmayan" kelimelerinin altını çiz.

> **1'i unutmak:** "Asal olmayan bölenler" sayılırken 1 de dahildir; 1 asal değildir.

## Kendini dene

### Soru 1
$504 = 2^a \cdot 3^b \cdot c$ eşitliğinde $c$ bir asal sayıdır.

Buna göre $a + b + c$ toplamı kaçtır?

A) 7
B) 10
C) 12
D) 14
E) 19

**Cevap:** C
**Çözüm:** Bölme merdiveni: $504 \to 252 \to 126 \to 63$ (üç kez 2'ye bölündü), $63 \to 21 \to 7$ (iki kez 3'e bölündü), $7 \to 1$. Yani $504 = 2^3 \cdot 3^2 \cdot 7$; $a = 3$, $b = 2$, $c = 7$. Toplam $3 + 2 + 7 = 12$. E seçeneği (19) bütün asal çarpanları tek tek toplamaktan gelir: $2 + 2 + 2 + 3 + 3 + 7$.

### Soru 2
504 sayısının kaç tane pozitif böleni vardır?

A) 6
B) 12
C) 18
D) 24
E) 48

**Cevap:** D
**Çözüm:** $504 = 2^3 \cdot 3^2 \cdot 7^1$. Pozitif bölen sayısı $(3+1)(2+1)(1+1) = 4 \cdot 3 \cdot 2 = 24$. Üslere 1 eklemeden çarpan 6, tam sayı bölenlerini sayan 48 bulur.

### Soru 3
180 sayısının asal olmayan tam sayı bölenlerinin toplamı kaçtır?

A) $-10$
B) $-5$
C) $0$
D) $5$
E) $10$

**Cevap:** A
**Çözüm:** $180 = 2^2 \cdot 3^2 \cdot 5$; asal bölenler 2, 3, 5. Bütün tam sayı bölenlerin toplamı 0'dır. Asal olanları çıkarınca $0 - (2 + 3 + 5) = -10$ kalır. 0 cevabı asal bölenleri çıkarmayı unutmaktan, 10 ise işareti kaçırmaktan gelir.

## Özet kartı

- Asal çarpanlara ayırma: en küçük asaldan başlayarak böl, bölüm 1 olunca dur; $A = x^a \cdot y^b \cdot z^c$.
- $10^n = 2^n \cdot 5^n$; aynı tabanın üslerini topla, her asalı bir kez yaz.
- Pozitif bölen sayısı $(a+1)(b+1)(c+1)$; negatif bölen sayısı da aynı, tam sayı bölen sayısı bunun 2 katı.
- Tek bölen sayısı: 2'li çarpanı yok sayarak hesapla; çift bölen = toplam − tek.
- Tam sayı bölenlerin toplamı 0; asal olmayan tam sayı bölenlerin toplamı $-(x + y + z)$.

## Sonraki adım

Alıştırmaya geç (aşağıdaki düğme). Gerçek çıkmış sorular için MEBİ'deki "Çıkmış Sorular" testine ve ÖSYM'nin resmî kitapçıklarına bak. Sonraki ders **EBOB-EKOK Kavramı ve Özellikleri**; orada iki sayının asal çarpanlarını yan yana yazıp ortak ve ortak olmayan çarpanlardan EBOB ile EKOK'u bulacaksın.
