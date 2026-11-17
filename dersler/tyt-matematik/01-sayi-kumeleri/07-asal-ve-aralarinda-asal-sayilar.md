---
baslik: Asal ve Aralarında Asal Sayılar
ders: tyt-matematik
sure: 20 dk
kaynak: MEBİ Konu Özeti 55a84c2edf
guncelleme: 2026-11-17
---
# Asal ve Aralarında Asal Sayılar

**Bu dersin sonunda:** bir sayının asal olup olmadığını hızlıca test edebilecek, asal sayı içeren denklemlerde "biri 2 olmalı" çıkarımını yapabilecek ve aralarında asal sayılarla kurulan eşitliklerden bilinmeyenleri bulabileceksin.

> **TYT'de yeri:** Asal sayılar genellikle başka bir sorunun içinde gelir: "$a$ ve $b$ asal sayılar, $a + 3b = 29$ ise…" kalıbında tek-çift akıl yürütmesi, "aralarında asal $x$ ve $y$ için $18x = 42y$" kalıbında sadeleştirme istenir. Yeni nesil sorularda dikdörtgen biçiminde dizilemeyen nesneler ya da yaşları asal olan kişiler çıkar.

## Önce hatırla

<details><summary>Sayı basamaklarından: İki basamaklı $\overline{AB}$ ve $\overline{BA}$ sayılarının toplamı 121 ise $A + B$ kaçtır?</summary>
Çözümle: $\overline{AB} + \overline{BA} = (10A + B) + (10B + A) = 11(A + B)$. $11(A + B) = 121$, yani $A + B = $ <b>11</b>. Bu derste $\overline{AB}$ biçimindeki sayıların asal olup olmadığını da soracağız.
</details>

<details><summary>Sayı basamaklarından: İki basamaklı $\overline{AB}$ sayısının rakamları yer değiştirince sayı 27 azalıyor. $A - B$ kaçtır?</summary>
$\overline{AB} - \overline{BA} = (10A + B) - (10B + A) = 9(A - B)$. $9(A - B) = 27$, yani $A - B = $ <b>3</b>.
</details>

## Asal sayı nedir?

**Örnek.** Elinde 12 kare fayans var ve hepsini kullanarak dikdörtgen bir zemin döşemek istiyorsun. $2 \times 6$, $3 \times 4$ gibi farklı dizilişler mümkün. 13 fayansla ise tek seçenek $1 \times 13$ olan tek sıradır, çünkü 13'ün 1 ve 13'ten başka pozitif böleni yoktur. 13 bir **asal sayıdır**, 12 değildir.

**1'den büyük** olup 1 ve kendisinden başka pozitif böleni olmayan tam sayılara **asal sayı** denir. Asal olmayan, 1'den büyük sayılara **bileşik sayı** da denir.

![1'den 50'ye kadar sayılar 5 satır 10 sütunluk tabloda. Asal olanlar mavi kutuda kalın yazılmış: 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47. 1 gri kutuda.](gorsel/tyt-matematik/01-07-asal-elek.svg "50'ye kadar 15 asal sayı var. 2 dışındaki bütün asallar tektir; ama 9, 15, 21, 27 gibi tek sayıların hepsi asal değildir.")

| Bilgi | Neden |
|---|---|
| 1 asal **değildir** | Tanım 1'den büyük olmayı ister; 1'in tek böleni vardır. |
| En küçük asal $2$'dir | 2'nin bölenleri yalnızca 1 ve 2. |
| Tek çift asal $2$'dir | Her çift sayı 2'ye bölünür; 2'den büyükse 2 fazladan bir bölen olur. |
| Negatif asal yoktur | Asal sayılar pozitif tam sayılar arasından seçilir. |
| Ardışık iki asal tam sayı yalnızca $2$ ve $3$'tür | Ardışık iki sayıdan biri çifttir; asal olan tek çift sayı 2'dir. |

1 ile 100 arasında 25 asal sayı vardır. İlk 10 asalı ezbere bil: $2, 3, 5, 7, 11, 13, 17, 19, 23, 29$.

**Kural.** Asal sayının tam olarak **iki** pozitif böleni vardır: 1 ve kendisi.

## Bir sayı asal mı?

**Örnek.** 91 ve 97 asal mı?

- $91$: $2$'ye bölünmez (tek), $3$'e bölünmez (rakam toplamı 10), $5$'e bölünmez (son rakam 1). $7$'ye dene: $91 = 7 \cdot 13$. **Asal değil.**
- $97$: $10^2 = 100 > 97$ olduğu için yalnızca karesi 97'yi geçmeyen asalları denemek yeter: $2, 3, 5, 7$. $97$ tek, rakam toplamı $16$ (3'e bölünmez), son rakamı 7 (5'e bölünmez), $97 = 7 \cdot 13 + 6$ (7'ye bölünmez). **Asaldır.**

Neden yeter? $97$ iki sayının çarpımı olsaydı, çarpanlardan biri $\sqrt{97} \approx 9{,}8$'den küçük olmak zorundaydı. O küçük çarpanın da bir asal böleni olurdu; onu zaten denedin.

![Akış şeması: Sayı n verildi. n en az 2 mi? Hayırsa asal değil. Evetse karesi n'yi aşmayan asalları yaz; n bunlardan birine tam bölünüyor mu? Evetse asal değil, hayırsa asaldır.](gorsel/tyt-matematik/01-07-asal-mi.svg "Asallık testi: yalnızca karesi n'yi aşmayan asallara bölmeyi denersin. 97 için 2, 3, 5 ve 7 yeter.")

**Kural.** $n$'nin asal olup olmadığını anlamak için karesi $n$'yi geçmeyen asallara böl. Hiçbirine bölünmüyorsa $n$ asaldır.

## Asal sayılarla denklem: biri 2 olmalı

**Örnek.** $a$ ve $b$ asal sayılar olmak üzere $7a + 3b = 41$ ise $a + b$ kaçtır?

Önce tek-çift durumuna bak (Tek ve Çift Sayılar dersi). 41 tektir. $a$ ve $b$ ikisi de tek asal olsaydı $7a$ ve $3b$ tek olur, toplamları **çift** çıkardı. Bu imkânsız; demek ki biri çift asaldır, yani **2**'dir.

- $a = 2$ ise $3b = 27$, $b = 9$. Ama 9 asal değil.
- $b = 2$ ise $7a = 35$, $a = 5$. 5 asal. ✓

$a + b = 5 + 2 = $ **7**.

**Fark 1 ise.** $a$ ve $b$ asal ve $b - a = 1$ ise ardışık iki asal sayıdır: $a = 2$, $b = 3$. Başka seçenek yoktur.

**Kural.** Asal sayılarla kurulan bir toplamda sonuç beklenen teklik ya da çiftlikle uyuşmuyorsa, asallardan biri **2**'dir. Bulduğun diğer sayının da asal olduğunu mutlaka kontrol et.

## Aralarında asal sayılar

**Örnek.** 8 ve 15 asal değil. Peki ortak bölenleri ne?

![İki Venn şeması. Solda 8'in bölenleri 2, 4, 8 ve 15'in bölenleri 3, 5, 15; kesişimde yalnızca 1. Sağda 12'nin bölenleri 4, 12 ve 18'in bölenleri 9, 18; kesişimde 1, 2, 3, 6.](gorsel/tyt-matematik/01-07-bolen-venn.svg "Kesişime bak: 8 ile 15'in ortak böleni yalnız 1, bu yüzden aralarında asaldır. 12 ile 18'in 1'den başka ortak bölenleri de var.")

8 ile 15'in 1'den başka ortak pozitif böleni yoktur. Bu iki sayı **aralarında asaldır**; kendileri asal olmasa da.

1'den başka pozitif ortak böleni olmayan pozitif tam sayılara **aralarında asal sayılar** denir. Bu bir sayının değil, **iki sayının birlikte** özelliğidir.

| Durum | Aralarında asal mı? | Örnek |
|---|---|---|
| 1 ve herhangi bir pozitif tam sayı | Evet | $1$ ve $50$ |
| İki farklı asal sayı | Evet | $7$ ve $11$ |
| Ardışık iki pozitif tam sayı | Evet | $35$ ve $36$ |
| Ardışık iki tek sayı | Evet | $21$ ve $23$ |
| Ardışık iki çift sayı | **Hayır** (2 ortak bölen) | $14$ ve $16$ |

Neden? İki sayıyı bölen her sayı **farklarını** da böler. Ardışık sayıların farkı 1'dir; 1'i yalnızca 1 böler. Ardışık tek sayıların farkı 2'dir; ortak bölen 1 ya da 2 olabilir, ama tek sayılar 2'ye bölünmez.

**Kural.** İki sayı aralarında asalsa $\frac{a}{b}$ kesri sadeleşmez. Aralarında asal olmak için sayıların asal olması gerekmez.

## Aralarında asal sayılarla eşitlik

**Örnek.** $x$ ve $y$ aralarında asal pozitif tam sayılar ve $\frac{x}{y} = \frac{24}{36}$ ise $x + y$ kaçtır?

$\frac{24}{36}$ kesrini sonuna kadar sadeleştir: $\frac{24}{36} = \frac{2}{3}$. $x$ ile $y$ aralarında asal olduğu için $\frac{x}{y}$ de sadeleşmez; sadeleşmeyen iki eşit kesrin payları ve paydaları eşittir: $x = 2$, $y = 3$. $x + y = $ **5**.

$x = 24$, $y = 36$ cevabı yanlıştır: 24 ile 36'nın ortak böleni 12'dir.

**Örnek.** $a$ ve $b$ pozitif tam sayılar, $a + b$ ile $a - b$ aralarında asal ve

$$15(a - b) = 9(a + b)$$

ise $a$ kaçtır?

Önce iki taraftaki sayıları sadeleştir: $5(a - b) = 3(a + b)$, yani $\frac{a - b}{a + b} = \frac{3}{5}$. Kesir sadeleşmez, bu yüzden

$$a - b = 3, \qquad a + b = 5.$$

Taraf tarafa topla: $2a = 8$, $a = $ **4** ve $b = 1$. Kontrol: $15 \cdot 3 = 45 = 9 \cdot 5$. ✓

**Kural.** $m \cdot X = n \cdot Y$ eşitliğinde $X$ ile $Y$ aralarında asalsa önce $m$ ile $n$'yi sadeleştir. Sonra $X = n$ ve $Y = m$ olur: her ifade karşı taraftaki sayıya eşittir (çapraz eşleşme).

## ÖSYM tuzakları

> **1'i asal saymak:** 1'in tek pozitif böleni vardır. "20'den küçük asal sayıların toplamı" sorusunda 1'i eklersen cevap 1 fazla çıkar.

> **Her tek sayıyı asal sanmak:** $9, 15, 21, 27, 33, 39, 49, 51, 57, 91$ tektir ama asal değildir. Özellikle $51 = 3 \cdot 17$ ve $91 = 7 \cdot 13$ sık kullanılır.

> **"Biri 2" seçeneğini kontrol etmemek:** $a + 3b = 29$ için $a = 2$ denersen $b = 9$ çıkar; 9 asal değil. Doğrusu $b = 2$, $a = 23$. İki durumu da dene.

> **Aralarında asalı asal sanmak:** 8 ile 15 aralarında asaldır ama ikisi de asal değildir. Tersine, 14 ve 16 gibi ardışık çift sayılar aralarında asal değildir.

> **Sadeleştirmeden eşitlemek:** $18x = 42y$ ve $x$, $y$ aralarında asalsa $x = 42$, $y = 18$ değildir. Önce $3x = 7y$ yap: $x = 7$, $y = 3$.

## Kendini dene

### Soru 1
Aşağıdaki sayılardan hangisi asaldır?

A) 51
B) 57
C) 87
D) 91
E) 97

**Cevap:** E
**Çözüm:** Karesi 97'yi geçmeyen asallar 2, 3, 5, 7; 97 bunların hiçbirine bölünmez, asaldır. Diğerleri: $51 = 3 \cdot 17$, $57 = 3 \cdot 19$, $87 = 3 \cdot 29$ (rakam toplamları 3'e bölünür) ve $91 = 7 \cdot 13$.

### Soru 2
$a$ ve $b$ asal sayılar olmak üzere $a + 3b = 29$ olduğuna göre $a \cdot b$ çarpımı kaçtır?

A) 21
B) 25
C) 27
D) 46
E) 69

**Cevap:** D
**Çözüm:** İkisi de tek olsaydı $a + 3b$ çift olurdu; 29 tek olduğu için biri 2'dir. $a = 2$ ise $3b = 27$, $b = 9$ asal değil. $b = 2$ ise $a = 23$, asal. $a \cdot b = 23 \cdot 2 = 46$. 25 toplamı ($a + b$), 21 farkı ($a - b$) verir.

### Soru 3
Aşağıdaki sayı ikililerinden hangisi aralarında asaldır?

A) 9 ve 15
B) 16 ve 24
C) 21 ve 28
D) 26 ve 39
E) 28 ve 45

**Cevap:** E
**Çözüm:** $28 = 2^2 \cdot 7$ ve $45 = 3^2 \cdot 5$; ortak asal çarpanları yok, ortak bölenleri yalnız 1. Diğerlerinde ortak bölen var: 9 ve 15'te 3; 16 ve 24'te 8; 21 ve 28'de 7; 26 ve 39'da 13. İkisi de asal olmadığı hâlde 28 ile 45 aralarında asaldır.

## Özet kartı

- Asal sayı: 1'den büyük, yalnızca 1'e ve kendisine bölünen tam sayı. 1 asal değil, negatif asal yok.
- 2 tek çift asaldır; ardışık iki asal yalnızca 2 ve 3'tür.
- Asallık testi: karesi $n$'yi geçmeyen asallara böl.
- Asallı denklemde teklik-çiftlik tutmuyorsa biri 2'dir; diğerinin de asal olduğunu kontrol et.
- Aralarında asal: ortak böleni yalnız 1. Ardışık tam sayılar ve ardışık tek sayılar aralarında asaldır, ardışık çift sayılar değildir.
- $mX = nY$ ve $X$, $Y$ aralarında asalsa: $m$ ile $n$'yi sadeleştir, sonra çapraz eşle.

## Sonraki adım

Alıştırmaya geç (aşağıdaki düğme). Sonraki ders **Ondalık ve Devirli Ondalık Sayılar**; ondalık sayıları kesre çevirirken kesri sadeleşmeyen hâle, yani payı ile paydası aralarında asal olana kadar sadeleştireceksin. Bölünebilme kuralları ünitesinde de bu dersteki asallık testini kullanacaksın.
