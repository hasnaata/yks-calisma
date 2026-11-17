---
baslik: Ondalık ve Devirli Ondalık Sayılar
ders: tyt-matematik
sure: 25 dk
kaynak: MEBİ Konu Özeti a3f464f3e4
guncelleme: 2026-11-17
---
# Ondalık ve Devirli Ondalık Sayılar

**Bu dersin sonunda:** ondalık sayılarla dört işlemi virgül hatası yapmadan yapabilecek, bir kesrin sonlu mu devirli mi olduğunu söyleyebilecek, devirli bir sayıyı kesre çevirebilecek ve kesirleri ya da ondalık sayıları sıralayabileceksin.

> **TYT'de yeri:** Neredeyse her sınavda bir soru doğrudan $\frac{0{,}36}{0{,}012}$ ya da $0{,}\overline{3} + 1{,}2\overline{7}$ gibi bir işlemdir. Kesir ve ondalık sıralama ("$a < c < b$ hangisi?") da sık gelir. Yeni nesil sorularda fiyat, ölçüm ve hesap makinesi bağlamında virgülün yerini doğru bulman istenir.

## Önce hatırla

<details><summary>Asal sayılardan: $a$ ve $b$ asal sayılar, $a + b = 15$ ise $a \cdot b$ kaçtır?</summary>
İki sayının toplamı tek ise biri çift olmalı. Tek çift asal 2'dir: $a = 2$, $b = 13$ (13 asal). $a \cdot b = $ <b>26</b>.
</details>

<details><summary>Aralarında asal sayılardan: $x$ ve $y$ aralarında asal pozitif tam sayılar, $6x = 10y$ ise $x + y$ kaçtır?</summary>
Sadeleştir: $3x = 5y$, yani $\frac{x}{y} = \frac{5}{3}$. 5 ile 3 aralarında asal olduğundan $x = 5$, $y = 3$; $x + y = $ <b>8</b>. Bu derste bir devirli sayıyı kesre çevirince cevabı yine "pay ile payda aralarında asal" olacak şekilde, yani en sade hâlde yazacaksın.
</details>

## Ondalık sayı nedir?

**Örnek.** $\frac{7}{40}$ kesrini ondalık sayı olarak yaz.

Paydayı 10'un bir kuvvetine tamamla: $40 \cdot 25 = 1000$. Payı da 25 ile genişlet:

$$\frac{7}{40} = \frac{7 \cdot 25}{40 \cdot 25} = \frac{175}{1000} = 0{,}175$$

Paydası $10, 100, 1000, \dots$ olan kesirlere **ondalık kesir**, bunların virgüllü yazılışına **ondalık sayı** denir. $0{,}175$ sayısında virgülden sonraki basamaklar sırasıyla onda birler (1), yüzde birler (7), binde birler (5) basamağıdır.

**Kural.** Kesri ondalık sayıya çevirmenin iki yolu var: paydayı $10^n$ yapacak sayıyla genişlet ya da payı paydaya böl. Genişletme yalnızca payda $2$ ve $5$'ten oluşuyorsa işe yarar, çünkü $10 = 2 \cdot 5$.

## Ondalık sayılarla dört işlem

### Toplama ve çıkarma

**Örnek.** $3{,}25 + 12{,}7 - 4{,}068$ işlemini yap.

Virgülleri alt alta getir, eksik basamaklara 0 yaz: $3{,}250 + 12{,}700 = 15{,}950$; $15{,}950 - 4{,}068 = 11{,}882$.

**Kural.** Toplama ve çıkarmada virgüller alt alta yazılır; sonuçtaki virgül de aynı hizadadır.

### Çarpma

**Örnek.** $1{,}2 \cdot 0{,}35$ kaçtır?

Virgülleri yok say: $12 \cdot 35 = 420$. Çarpanlarda virgülden sonra toplam $1 + 2 = 3$ basamak var. Sağdan 3 basamak say: $0{,}420 = 0{,}42$.

**Kural.** Çarpmada virgül yokmuş gibi çarp; sonuçta, çarpanların virgülden sonraki basamak sayılarının **toplamı** kadar basamak ayır.

### 10, 100, 1000 ile çarpma ve bölme

**Örnek.** $34{,}56 \cdot 100 = 3456$ ve $34{,}56 : 100 = 0{,}3456$.

![İki satır rakam kutusu: üstte 3, 4, 5, 6 ve virgül iki basamak sağa atlıyor, sonuç 3456. Altta 0, 3, 4, 5, 6 ve virgül iki basamak sola atlıyor, sonuç 0,3456.](gorsel/tyt-matematik/01-08-virgul-kaydirma.svg "Rakamlar yerinde kalır, yalnızca virgül hareket eder. 100'de iki sıfır var, virgül iki basamak atlar.")

**Kural.** $10^n$ ile çarparken virgül $n$ basamak **sağa**, $10^n$'e bölerken $n$ basamak **sola** kayar. Basamak yetmezse 0 eklenir: $0{,}042 \cdot 1000 = 42$, $5{,}2 : 100 = 0{,}052$.

### Bölme

**Örnek.** $\frac{3{,}6}{0{,}12}$ kaçtır?

Böleni virgülden kurtar: $0{,}12$ için 100 ile çarpmak gerek. Kesrin değeri değişmesin diye payı da 100 ile çarp:

$$\frac{3{,}6}{0{,}12} = \frac{3{,}6 \cdot 100}{0{,}12 \cdot 100} = \frac{360}{12} = 30$$

**Kural.** Bölmede pay ve paydayı **aynı** $10^n$ ile çarp; en çok basamaklı olana göre seç. Payda tam sayı olunca normal böl.

## Sonlu mu, devirli mi?

**Örnek.** $\frac{5}{11}$ kesrini ondalık sayıya çevir.

11, 10'un hiçbir kuvvetini bölmez, o yüzden böl: $50 = 11 \cdot 4 + 6$, $60 = 11 \cdot 5 + 5$, sonra yine $50$… Kalanlar $6, 5, 6, 5, \dots$ diye döner, bölüm de $0{,}4545\dots$ diye sonsuza kadar sürer.

Virgülden sonra bir rakam grubu sürekli tekrar ediyorsa sayıya **devirli ondalık sayı** denir. Tekrar eden kısmın (devreden) üstüne çizgi çekilir:

$$0{,}4545\dots = 0{,}\overline{45} \qquad 0{,}333\dots = 0{,}\overline{3} \qquad 1{,}2777\dots = 1{,}2\overline{7}$$

Bir kesrin hangi türde çıkacağını bölmeden anlayabilirsin. Önceki dersteki asal çarpanlar burada işe yarar:

![Akış şeması: kesri en sade hâline getir, paydayı asal çarpanlarına ayır, yalnız 2 ve 5 varsa sonlu ondalık, başka asal varsa devirli ondalık.](gorsel/tyt-matematik/01-08-sonlu-mu-devirli.svg "İlk adımı atlama: önce sadeleştir, sonra paydaya bak.")

**Kural.** En sade kesrin paydasında yalnızca 2 ve 5 varsa ondalık açılım **sonludur**; başka bir asal çarpan varsa **devirlidir**. $\frac{7}{12}$ devirlidir ($12 = 2^2 \cdot 3$); $\frac{21}{35} = \frac{3}{5} = 0{,}6$ sonludur, paydadaki 7 sadeleşince gider.

## Devirli sayıyı kesre çevirmek

**Örnek.** $x = 0{,}1\overline{6}$ ise $x$ hangi kesirdir?

Virgülü önce devretmeyen kısmın sonuna, sonra bir devrin sonuna taşı:

$$10x = 1{,}666\dots \qquad 100x = 16{,}666\dots$$

Çıkar; sonsuz kuyruklar birbirini götürür: $100x - 10x = 16 - 1$, yani $90x = 15$ ve $x = \frac{15}{90} = \frac{1}{6}$.

Bunu her seferinde yapmamak için kısa yol:

![2,1 ve üstü çizgili 36 sayısı: 2 tam kısım, 1 devretmeyen, 36 devreden. Altta pay 2136 eksi 21, payda 990; iki 9 devreden iki basamaktan, bir 0 devretmeyen bir basamaktan gelir.](gorsel/tyt-matematik/01-08-devirli-kesir.svg "Paydadaki 9'lar devredenden, 0'lar virgülden sonraki devretmeyen basamaklardan gelir. Tam kısım paydayı etkilemez.")

$$2{,}1\overline{36} = \frac{2136 - 21}{990} = \frac{2115}{990} = \frac{47}{22}$$

**Kural.**

$$\text{Devirli sayı} = \frac{\text{sayının tamamı} - \text{devretmeyen kısım}}{\text{devreden kadar } 9,\ \text{ardından virgülden sonraki devretmeyen kadar } 0}$$

Sık kullanılanlar: $0{,}\overline{a} = \frac{a}{9}$, $0{,}\overline{ab} = \frac{ab}{99}$, $0{,}0\overline{a} = \frac{a}{90}$.

Bir de şaşırtıcı olanı: $0{,}\overline{9} = \frac{9 - 0}{9} = 1$. Yani $1{,}\overline{9} = 2$, $0{,}4\overline{9} = 0{,}5$. Devreden 9 olan sayı bir üst ondalık sayıya eşittir.

## Sıralama

**Örnek.** $0{,}3$; $0{,}33$; $0{,}\overline{3}$; $0{,}\overline{34}$; $0{,}3\overline{4}$ sayılarını sırala.

Hepsini aynı uzunlukta aç ve basamak basamak karşılaştır:

| Sayı | Açılım |
|---|---|
| $0{,}3$ | $0{,}30000\dots$ |
| $0{,}33$ | $0{,}33000\dots$ |
| $0{,}\overline{3}$ | $0{,}33333\dots$ |
| $0{,}\overline{34}$ | $0{,}34343\dots$ |
| $0{,}3\overline{4}$ | $0{,}34444\dots$ |

![0,30 ile 0,35 arası büyütülmüş sayı doğrusu: soldan sağa 0,3; 0,33; 0,3 devirli; 0,34 devirli; 0,3 ve 4 devirli.](gorsel/tyt-matematik/01-08-siralama.svg "Üstü çizgili sayılar kendi çizgisizlerinden biraz sağdadır. 0,34 devirli ile 0,3 ve 4 devirli birbirine çok yakın, yine de farklı.")

Sıra: $0{,}3 < 0{,}33 < 0{,}\overline{3} < 0{,}\overline{34} < 0{,}3\overline{4}$.

Kesirlerde açılım yapmadan kullanabileceğin kısa yollar (pozitif kesirler için):

| Durum | Hangisi büyük? | Örnek |
|---|---|---|
| Paydalar eşit | Payı büyük olan | $\frac{5}{9} < \frac{7}{9}$ |
| Paylar eşit | Paydası küçük olan | $\frac{12}{88} < \frac{12}{84}$ |
| Basit kesir, payda − pay farkı eşit | Payı büyük olan | $\frac{5}{8} < \frac{7}{10} < \frac{9}{12}$ |
| Bileşik kesir, pay − payda farkı eşit | Payı küçük olan | $\frac{12}{9} < \frac{10}{7} < \frac{8}{5}$ |

**Kural.** Negatif sayılarda önce işaretsiz sırala, sonra sırayı ters çevir: $0{,}33 < 0{,}\overline{3}$ olduğu için $-0{,}\overline{3} < -0{,}33$.

## ÖSYM tuzakları

> **Bölmede yalnız paydayı çarpmak:** $\frac{0{,}36}{0{,}012}$ için paydayı 1000 ile çarpıp payı unutursan $\frac{0{,}36}{12} = 0{,}03$ bulursun. Pay da 1000 ile çarpılır: $\frac{360}{12} = 30$.

> **Paydaya hep 9 yazmak:** $0{,}2\overline{7} = \frac{27 - 2}{90}$'dır, $\frac{27 - 2}{99}$ değil. Devretmeyen her basamak paydaya bir 0 ekler.

> **Sadeleştirmeden paydaya bakmak:** $\frac{21}{35}$ paydasında 7 var ama sonlu çıkar ($\frac{3}{5} = 0{,}6$). Sonlu/devirli kararını en sade kesirde ver.

> **$0{,}\overline{9}$'u 1'den küçük sanmak:** $1{,}\overline{3} + 0{,}\overline{6} = 1{,}\overline{9}$ ve bu tam olarak $2$'dir. Seçeneklerde $1{,}99$ görürsen tuzaktır.

> **Basamak sayısına bakarak sıralamak:** $0{,}3\overline{4}$ "daha kısa" görünür ama $0{,}\overline{34}$'ten büyüktür. Karşılaştırmadan önce açılımı birkaç basamak yaz.

## Kendini dene

### Soru 1
$\dfrac{0{,}36}{0{,}012}$ işleminin sonucu kaçtır?

A) 0,3
B) 3
C) 30
D) 300
E) 3000

**Cevap:** C
**Çözüm:** Böleni virgülden kurtarmak için pay ve paydayı 1000 ile çarp: $\frac{360}{12} = 30$. Payı 100, paydayı 1000 ile çarpan $\frac{36}{12} = 3$; yalnız paydayı 100 ile çarpan $\frac{0{,}36}{1{,}2} = 0{,}3$ bulur. Pay ile payda hep aynı sayıyla çarpılır.

### Soru 2
$0{,}2\overline{7}$ sayısının rasyonel sayı olarak en sade gösterimi aşağıdakilerden hangisidir?

A) $\frac{25}{99}$
B) $\frac{27}{100}$
C) $\frac{3}{11}$
D) $\frac{5}{18}$
E) $\frac{7}{25}$

**Cevap:** D
**Çözüm:** Sayının tamamı 27, devretmeyen kısım 2; devreden 1 basamak (bir 9), devretmeyen 1 basamak (bir 0): $\frac{27 - 2}{90} = \frac{25}{90} = \frac{5}{18}$. Paydaya 99 yazan $\frac{25}{99}$, devri görmezden gelen $\frac{27}{100}$ bulur; $\frac{3}{11} = 0{,}\overline{27}$ başka bir sayıdır.

### Soru 3
$a = 0{,}\overline{45}$, $b = 0{,}4\overline{5}$, $c = 0{,}45$ olduğuna göre aşağıdaki sıralamalardan hangisi doğrudur?

A) $a < b < c$
B) $a < c < b$
C) $b < c < a$
D) $c < b < a$
E) $c < a < b$

**Cevap:** E
**Çözüm:** Açılımları yaz: $a = 0{,}4545\dots$, $b = 0{,}4555\dots$, $c = 0{,}4500$. Üçüncü basamakta $c$'de 0, $a$'da 4, $b$'de 5 var. Sıra $c < a < b$.

## Özet kartı

- Çarpmada virgülden sonraki basamak sayıları toplanır; bölmede pay ve payda aynı $10^n$ ile çarpılır.
- $10^n$ ile çarpınca virgül $n$ basamak sağa, bölünce $n$ basamak sola kayar.
- En sade kesrin paydasında yalnız 2 ve 5 varsa sonlu, başka asal varsa devirli ondalık.
- Devirli → kesir: $\frac{\text{tamamı} - \text{devretmeyen}}{\text{devreden kadar 9, devretmeyen kadar 0}}$.
- $0{,}\overline{9} = 1$; $0{,}\overline{a} = \frac{a}{9}$, $0{,}\overline{ab} = \frac{ab}{99}$.
- Sıralarken açılımı birkaç basamak yaz; negatiflerde sıra ters döner.

## Sonraki adım

Alıştırmaya geç (aşağıdaki düğme). Gerçek çıkmış sorular için MEBİ'deki "Çıkmış Sorular" testine ve ÖSYM'nin resmî kitapçıklarına bak. Sonraki ders **Rasyonel Sayılarda İşlemler**; orada devirli sayıları kesre çevirip kesirlerle dört işlem yapacaksın.
