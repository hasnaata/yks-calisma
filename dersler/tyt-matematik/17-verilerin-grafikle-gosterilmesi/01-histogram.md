---
baslik: Histogram
ders: tyt-matematik
sure: 20 dk
kaynak: MEBİ Konu Özeti 0e38692b7d
guncelleme: 2026-11-17
---
# Histogram

**Bu dersin sonunda:** ham verilerden grup genişliğini bulup gruplama tablosunu yapabilecek, histogram çizebilecek ve verilen bir histogramdan "kaç kişi, yüzde kaç, kesin mi?" sorularını cevaplayabileceksin.

> **TYT'de yeri:** Histogram çoğunlukla hazır çizilmiş verilir: "Şu aralıkta kaç kişi var?", "Yüzde kaçı?", "Aşağıdakilerden hangisi kesinlikle doğrudur?" Bazen de ham veri ya da açıklık verilip grup genişliği sorulur. Hesap kısadır; tuzak grup sınırlarındadır.

## Önce hatırla

<details><summary>Merkezi yayılım ölçülerinden: 17, 4, 25, 9, 12 veri grubunun açıklığı kaçtır?</summary>
En büyük değer 25, en küçük değer 4. Açıklık $25 - 4 = $ <b>21</b>. Listede ilk ve son yazılan sayılara değil, en büyük ve en küçük değere bakılır.
</details>

<details><summary>Merkezi yayılım ölçülerinden: Bir veri grubunun standart sapması 3'tür. Her veri 2 ile çarpılıp üzerine 5 eklenirse yeni standart sapma kaç olur?</summary>
2 ile çarpmak standart sapmayı 2 katına çıkarır: $2 \cdot 3 = 6$. 5 eklemek yayılımı değiştirmez. Yeni standart sapma <b>6</b>.
</details>

## Histogram nedir?

Bir önceki konuda tek tek değerleri **sütun grafiğiyle** gösterdin: "1 kardeşi olan 8 öğrenci" gibi. Ama veriler çok çeşitliyse (yaşlar, süreler, puanlar) her değere ayrı sütun çizmek işe yaramaz. Bunun yerine veriler **gruplara** ayrılır ve her gruptaki veri sayısı bir sütunla gösterilir.

Gruplandırılmış verilerin tekrar sayılarını **bitişik dikdörtgen sütunlarla** gösteren grafiğe **histogram** denir.

| | Sütun grafiği | Histogram |
|---|---|---|
| Yatay eksende | Tek tek değerler ya da kategoriler | Gruplar (21–27, 28–34, …) |
| Sütunlar | Aralıklı | Bitişik |
| Sütun yüksekliği | O değerin kaç kez tekrar ettiği | O gruptaki veri sayısı |

## Histogram çizmek

**Örnek.** Bir sınıftaki 12 öğrencinin bir günde kitap okuduğu süreler (dakika):

$$33,\ 21,\ 44,\ 29,\ 36,\ 25,\ 41,\ 30,\ 47,\ 24,\ 38,\ 32$$

Bu verileri 4 grupla histogramda gösterelim.

**1. Sırala:** $21, 24, 25, 29, 30, 32, 33, 36, 38, 41, 44, 47$

**2. Açıklık:** $47 - 21 = 26$

**3. Grup sayısı:** 4 (soruda verildi)

**4. Grup genişliği:** $\frac{26}{4} = 6{,}5$. Bundan **büyük** en küçük doğal sayı $7$'dir. Genişlik 7.

**5. Gruplama tablosu:** İlk grup **en küçük veriden** başlar ve 7 sayı içerir: $21, 22, \dots, 27$. Sonraki grup 28'den başlar.

| Grup | Veriler | Öğrenci sayısı |
|---|---|---|
| 21–27 | 21, 24, 25 | 3 |
| 28–34 | 29, 30, 32, 33 | 4 |
| 35–41 | 36, 38, 41 | 3 |
| 42–48 | 44, 47 | 2 |
| | **Toplam** | **12** |

Kontrol: tablodaki sayıların toplamı veri sayısına (12) eşit olmalı.

**6. Histogram:** Gruplar yatay eksene, öğrenci sayıları dikey eksene yazılır.

![Histogram: yatay eksende 21–27, 28–34, 35–41, 42–48 grupları; sütun yükseklikleri sırasıyla 3, 4, 3, 2. Yatay eksenin başında, sıfır ile ilk grup arasında zikzak var.](gorsel/tyt-matematik/17-01-okuma-suresi.svg "Sütunlar arasında boşluk yok. Eksenin başındaki zikzak, 0 ile 21 arasında veri olmadığını ve o kısmın kısaltıldığını gösterir.")

**Kural.** Histogram şu altı adımla çizilir:

![Altı kutulu akış şeması: verileri sırala, açıklığı bul, grup sayısını seç, grup genişliğini bul, gruplama tablosunu yap, histogramı çiz. Dördüncü kutu sarı renkle vurgulanmış.](gorsel/tyt-matematik/17-01-yontem.svg "Hataların çoğu sarı kutuda, grup genişliğinde yapılır.")

- $\text{Grup genişliği} = \dfrac{\text{açıklık}}{\text{grup sayısı}}$ değerinden **büyük** olan en küçük doğal sayı.
- İlk grup **en küçük veriyle** başlar. Genişlik $w$ ise her grupta $w$ tane tam sayı vardır: ilk grup $a$ ile $a + w - 1$ arasıdır.
- Gruplar yatay, veri sayıları dikey eksene yazılır; ölçek eşit aralıklı olur.
- Sıfırdan ilk gruba kadar veri olmayan bölge eksende **zikzakla** gösterilir.

## Bölme tam çıkarsa

**Örnek.** Bir sınavda en düşük puan 10, en yüksek puan 30. Veriler 4 gruba ayrılacak. Grup genişliği kaçtır?

Açıklık $30 - 10 = 20$, $\frac{20}{4} = 5$. Bölüm tam çıktı. "5'ten **büyük** en küçük doğal sayı" $6$'dır.

Neden 5 olmaz? Genişlik 5 alınırsa gruplar $10–14$, $15–19$, $20–24$, $25–29$ olur ve **30 hiçbir gruba girmez**.

![İki sayı doğrusu. Üstte genişlik 5 ile dört grup: 10–14, 15–19, 20–24, 25–29; en büyük veri olan 30 grupların dışında kırmızı nokta. Altta genişlik 6 ile dört grup: 10–15, 16–21, 22–27, 28–33; 30 son grubun içinde.](gorsel/tyt-matematik/17-01-tam-bolunme.svg "Genişlik 5 iken gruplar 29'da biter, 30 dışarıda kalır. Genişlik 6 ile bütün veriler gruplara girer.")

**Kural.** Bölüm tam sayı çıkarsa grup genişliği **bölüm + 1** olur. Bölüm tam çıkmazsa bir üst doğal sayıya yuvarlanır: $6{,}5 \to 7$, $5 \to 6$.

Bu kuralı tersinden de okuyabilirsin: $k$ grup ve genişlik $w$ ise $\frac{\text{açıklık}}{k}$ değeri $w - 1$ ile $w$ arasındadır ($w - 1$ olabilir, $w$ olamaz).

## Histogram okumak

**Örnek.** Bir spor salonundaki 40 üyenin yaşları aşağıdaki histogramda verilmiştir.

![Histogram: yaş grupları 16–22, 23–29, 30–36, 37–43, 44–50; üye sayıları sırasıyla 6, 14, 10, 7, 3.](gorsel/tyt-matematik/17-01-spor-salonu.svg "Her sütunun yüksekliğini dikey eksendeki noktalı çizgiyle oku. Toplam 6 + 14 + 10 + 7 + 3 = 40.")

**a) 30 yaş ve üzeri üyeler yüzde kaçtır?** 30 yaş, 30–36 grubunun ilk değeridir. $10 + 7 + 3 = 20$ üye. $\frac{20}{40} = \%50$.

**b) Kaç üyenin 30 yaşından büyük olduğu kesindir?** 30–36 grubundaki 10 kişinin hepsi 30 yaşında olabilir. Kesin olanlar yalnızca 37–43 ve 44–50 grupları: $7 + 3 = 10$ üye. En çok ise $20$ üye 30'dan büyük olabilir.

**c) En genç üye kaç yaşındadır?** İlk grup en küçük veriyle başladığı için en genç üye **16** yaşındadır. Ama en yaşlı üyenin yaşı kesin değildir; yalnızca 44–50 arasında olduğu bilinir.

**Kural.** Histogram bir grubun **içindeki** verileri tek tek göstermez. Bir grubun hepsi o grubun en küçük değeri de olabilir, en büyük değeri de. "Kesinlikle" sorularında her grubu iki uç durumla düşün.

## ÖSYM tuzakları

> **Bölme tam çıkınca bölümü almak:** Açıklık 20, grup sayısı 4 ise genişlik 5 değil **6**'dır. 5 alınırsa en büyük veri dışarıda kalır.

> **Grubun son değerini yanlış yazmak:** Genişlik 7 ve ilk veri 21 ise ilk grup 21–28 değil **21–27**'dir. Grupta 7 sayı olmalı: son değer $21 + 7 - 1$.

> **"Büyük" ile "büyük ya da eşit" farkı:** "30 yaş ve üzeri" denince 30–36 grubu sayılır. "30'dan büyük olduğu kesin" denince sayılmaz, çünkü o gruptakilerin hepsi 30 olabilir.

> **Toplamı kontrol etmemek:** Gruplama tablosundaki sayıların toplamı veri sayısına eşit değilse bir veri ya iki gruba yazılmış ya da hiç yazılmamıştır.

## Kendini dene

### Soru 1
Bir veri grubunun açıklığı 30'dur. Veriler 5 gruba ayrılarak histogram çizilecektir. Grup genişliği kaç olmalıdır?

A) 5
B) 6
C) 7
D) 8
E) 9

**Cevap:** C
**Çözüm:** $\frac{30}{5} = 6$, bölüm tam çıktı. 6'dan büyük en küçük doğal sayı **7**'dir. 6 alınırsa gruplar en küçük veriden itibaren yalnızca 30 sayı kapsar, açıklık 30 olduğu için 31 farklı değer gerekir ve en büyük veri dışarıda kalır.

### Soru 2
12 öğrencinin bir haftada çözdüğü test sayıları şöyledir:

$$14,\ 9,\ 22,\ 17,\ 11,\ 25,\ 30,\ 19,\ 12,\ 27,\ 8,\ 21$$

Bu veriler 3 grupla histogramda gösterilirse ikinci grubun sütun yüksekliği kaç olur?

A) 3
B) 4
C) 5
D) 6
E) 7

**Cevap:** B
**Çözüm:** Sıralı: $8, 9, 11, 12, 14, 17, 19, 21, 22, 25, 27, 30$. Açıklık $30 - 8 = 22$; $\frac{22}{3} \approx 7{,}33$, genişlik 8. Gruplar: 8–15, 16–23, 24–31. İkinci grupta $17, 19, 21, 22$: **4** öğrenci. Genişliği 7 alan 8–14, 15–21, 22–28 gruplarını kurar, ikinci grupta 3 bulur ve 30'u dışarıda bırakır.

### Soru 3
Bir sınıftaki 30 öğrencinin boyları aşağıdaki histogramda verilmiştir.

![Histogram: boy grupları 150–157, 158–165, 166–173, 174–181 cm; öğrenci sayıları sırasıyla 4, 9, 11, 6.](gorsel/tyt-matematik/17-01-kd-boy.svg "Sütun yüksekliklerini dikey eksenden oku. 166 cm hangi grubun ilk değeri?")

Boyu en az 166 cm olan öğrenciler sınıfın kaçta kaçıdır?

A) $\frac{1}{5}$
B) $\frac{11}{30}$
C) $\frac{13}{30}$
D) $\frac{17}{30}$
E) $\frac{13}{15}$

**Cevap:** D
**Çözüm:** 166, 166–173 grubunun ilk değeri. "En az 166" bu grubu ve sonrakini kapsar: $11 + 6 = 17$ öğrenci. Oran $\frac{17}{30}$. $\frac{1}{5}$ yalnızca son grubu, $\frac{11}{30}$ yalnızca 166–173 grubunu almaktır; $\frac{13}{30}$ ise 166'dan kısa olanların oranıdır.

## Özet kartı

- Histogram: gruplandırılmış verilerin bitişik sütunlarla gösterimi; gruplar yatay, veri sayıları dikey eksende.
- Adımlar: sırala → açıklık → grup sayısı → genişlik → tablo → grafik.
- Grup genişliği, $\frac{\text{açıklık}}{\text{grup sayısı}}$ değerinden **büyük** en küçük doğal sayıdır; bölüm tam çıkarsa 1 eklenir.
- İlk grup en küçük veriyle başlar; genişlik $w$ ise grup $a$ ile $a + w - 1$ arasıdır.
- Tablodaki sayıların toplamı veri sayısına eşit olmalı.
- Grubun içindeki değerler bilinmez: "kesin" sorularında grubun iki ucunu da düşün.

## Sonraki adım

Alıştırmaya geç (aşağıdaki düğme). Sonraki ders **Çizgi, Sütun ve Daire Grafikleri**; aynı verinin farklı grafiklerle nasıl gösterildiğini ve grafikler arasında geçiş yapmayı göreceksin.
