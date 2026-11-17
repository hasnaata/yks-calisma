---
baslik: Çizgi, Sütun ve Daire Grafikleri
ders: tyt-matematik
sure: 20 dk
kaynak: MEBİ Konu Özeti cafaa7832b
guncelleme: 2026-11-17
---
# Çizgi, Sütun ve Daire Grafikleri

**Bu dersin sonunda:** çizgi, sütun ve daire grafiğinden doğru değeri okuyabilecek, daire grafiğinde merkez açı ile kişi (adet) sayısı arasında iki yönde geçiş yapabilecek ve grafiklerin yanıltıcı görünüşüne düşmeyeceksin.

> **TYT'de yeri:** Grafik soruları her yıl gelir ve genelde iki üç soruluk bir grubun parçasıdır. Kalıplar: "grafiğe göre en çok artış hangi dönemde?", "daire grafiğinde bu dilim kaç kişi?", "sütun grafiğindeki veriler daire grafiğinde gösterilirse dilimin açısı kaç derece?", "iki grafikten hangisi doğru sonuç verir?". İşlem azdır; asıl iş grafiği doğru okumaktır.

## Önce hatırla

<details><summary>Histogramdan: En küçük verisi 12, en büyük verisi 40 olan bir veri grubu için 4 gruplu histogram çizilecek. Grup genişliği kaç olur?</summary>
Açıklık $40 - 12 = 28$. $28 : 4 = 7$. Grup genişliği, bu bölümden <b>büyük</b> en küçük doğal sayıdır: <b>8</b>. Gruplar 12–19, 20–27, 28–35, 36–43 olur. Genişlik 7 alınsaydı son grup 33–39 olur ve 40 dışarıda kalırdı.
</details>

<details><summary>Histogramdan: Histogramın sütunları bitişiktir, bu dersteki sütun grafiğinin sütunları arasında boşluk vardır. Neden?</summary>
Histogram <b>gruplandırılmış</b> veriyi gösterir: bir grubun bittiği yerde sonraki başlar, bu yüzden sütunlar bitişiktir. Sütun grafiğinde her sütun ayrı bir kategoriyi ya da değeri gösterir (Ekim, Kasım, elma, muz…); sütunlar birbirinden ayrı çizilir.
</details>

## Hangi grafik ne için?

Üç grafik türü üç farklı soruya cevap verir. Önce grafiğin hangi soruya cevap verdiğini anla:

| Grafik | Ne gösterir? | Ne zaman kullanılır? |
|---|---|---|
| Çizgi grafiği | Bir değerin **zamanla değişimi** | Sıcaklık, boy, nüfus, aylık satış (sürekli veri) |
| Sütun grafiği | Grupların **karşılaştırılması** | Sınıflara, ürünlere, aylara göre sayılar (kesikli veri) |
| Daire grafiği | Her parçanın **bütüne oranı** | Bütçenin, sınıfın, satışın paylara dağılımı |

## Çizgi grafiği

**Örnek.** Bir fidanın boyu her hafta sonunda ölçülüp grafiğe işleniyor.

![Çizgi grafiği: yatay eksende hafta 0'dan 5'e, dikey eksende boy. Noktalar 4, 7, 9, 9, 14, 16 santimetre. 2 ile 3. hafta arası yatay, 3 ile 4. hafta arası en dik çizgi.](gorsel/tyt-matematik/17-02-cizgi.svg "Değişimi iki ardışık noktanın farkı verir. En dik parça (3 ile 4. hafta arası) en hızlı büyüme, yatay parça hiç değişmeme demektir.")

Her hafta için artışı hesapla: sonraki değer − önceki değer.

| Hafta aralığı | 0–1 | 1–2 | 2–3 | 3–4 | 4–5 |
|---|---|---|---|---|---|
| Artış (cm) | $7 - 4 = 3$ | $9 - 7 = 2$ | $9 - 9 = 0$ | $14 - 9 = 5$ | $16 - 14 = 2$ |

- En hızlı büyüme 3. ile 4. hafta arasında: $5$ cm. Bu, grafiğin **en dik** parçasıdır.
- 2. ile 3. hafta arasında boy değişmemiş: çizgi **yatay**.
- 5 haftada toplam artış $16 - 4 = 12$ cm; haftalık ortalama artış $12 : 5 = 2{,}4$ cm.

**Kural.** Çizgi grafiğinde noktalar ölçülen değerlerdir, çizgiler noktaları birleştirir. İki nokta arasındaki değişim = sonraki değer − önceki değer. Yatay eksen eşit aralıklıysa çizgi ne kadar dikse değişim o kadar hızlıdır; yükselen çizgi artış, alçalan çizgi azalış, yatay çizgi değişmeme demektir.

Dikkat: "En yüksek değer" ile "en çok artış" farklı sorulardır. Bu örnekte en yüksek değer 5. haftada (16 cm), en çok artış ise 3–4. hafta arasındadır.

## Sütun grafiği

**Örnek.** Bir kütüphaneden dört ayda ödünç alınan roman ve bilim kitabı sayıları aynı grafikte, yan yana sütunlarla gösterilmiş.

![Çift sütun grafiği: Ekim, Kasım, Aralık, Ocak aylarında koyu mavi roman ve açık yeşil bilim sütunları. Roman 40, 35, 50, 45; bilim 20, 30, 25, 35.](gorsel/tyt-matematik/17-02-sutun.svg "Önce açıklamaya (lejant) bak: hangi renk hangi veri? Sonra her sütunun tepesini yatay çizgiyle dikey eksene taşı.")

Sütunları okuyup tabloya geçir:

| Ay | Ekim | Kasım | Aralık | Ocak |
|---|---|---|---|---|
| Roman | 40 | 35 | 50 | 45 |
| Bilim | 20 | 30 | 25 | 35 |
| Toplam | 60 | 65 | 75 | 80 |

- Toplam en çok **Ocak**'ta (80). Tek başına en uzun sütun Aralık'taki roman sütunu olsa da toplam Ocak'ta büyüktür.
- Roman sayısının bilim kitabı sayısının 2 katı olduğu aylar: Ekim ($40 = 2 \cdot 20$) ve Aralık ($50 = 2 \cdot 25$).
- Dört ayda $40 + 35 + 50 + 45 = 170$ roman, $20 + 30 + 25 + 35 = 110$ bilim kitabı alınmış.

**Kural.** Sütun grafiğinde her sütunun **yüksekliği** değeri verir. Değeri okurken sütunun tepesini dikey eksene taşı; ölçeği (bir çizgi kaç birim?) kontrol et. Çift sütunlu grafikte her soruda hangi renge baktığını açıklamadan doğrula.

### Yanıltıcı eksen

Aynı üç veri (A: 52, B: 48, C: 56) iki farklı biçimde çizilmiş:

![Yan yana iki sütun grafiği, aynı veri: A 52, B 48, C 56. Soldakinde dikey eksen 0'dan başlıyor, sütunlar birbirine yakın boyda. Sağdakinde eksen 45'ten başlıyor, C sütunu B'nin yaklaşık dört katı uzun görünüyor.](gorsel/tyt-matematik/17-02-kesik-eksen.svg "Sağdaki grafik farkı büyütüyor. Oranı sütun boyundan değil, eksendeki değerlerden hesapla.")

Sağdaki grafikte C sütunu B'nin neredeyse 4 katı uzun görünür. Gerçek oran ise $\frac{56}{48} = \frac{7}{6}$, yani C, B'den yalnızca yaklaşık %17 fazladır.

**Kural.** Dikey eksen 0'dan başlamıyorsa sütun boylarının oranı, değerlerin oranı **değildir**. Önce değerleri eksenden oku, sonra karşılaştır.

## Daire grafiği

Daire grafiğinde bütün, $360^\circ$'lik dairedir. Her dilimin **merkez açısı**, o parçanın bütüne oranıyla orantılıdır.

$$\text{Merkez açı} = \frac{\text{parça}}{\text{bütün}} \cdot 360^\circ$$

**Örnek 1 (sayıdan açıya).** 120 öğrenciye okula nasıl geldiği sorulmuş: otobüs 45, yürüyerek 30, servis 25, özel araç 20.

Bir öğrenciye düşen açı: $360^\circ : 120 = 3^\circ$. Her sayıyı 3 ile çarp:

| Ulaşım | Öğrenci | Merkez açı |
|---|---|---|
| Otobüs | 45 | $45 \cdot 3^\circ = 135^\circ$ |
| Yürüyerek | 30 | $30 \cdot 3^\circ = 90^\circ$ |
| Servis | 25 | $25 \cdot 3^\circ = 75^\circ$ |
| Özel araç | 20 | $20 \cdot 3^\circ = 60^\circ$ |
| Toplam | 120 | $360^\circ$ |

![Daire grafiği: otobüs 135 derece, yürüyerek 90 derece, servis 75 derece, özel araç 60 derece.](gorsel/tyt-matematik/17-02-daire.svg "Yürüyerek dilimi tam çeyrek dairedir (90°): öğrencilerin dörtte biri, yani 30 kişi. Açıların toplamı 360° olmalı.")

Kontrol: $135 + 90 + 75 + 60 = 360$. Toplam 360 çıkmıyorsa bir yerde hata var.

**Örnek 2 (açıdan sayıya).** Başka bir okulun daire grafiğinde yürüyerek gelenlerin dilimi $72^\circ$ ve bu dilim 48 öğrenciyi gösteriyor. Okulda kaç öğrenci var?

$72^\circ$ dairenin $\frac{72}{360} = \frac{1}{5}$'idir. 48 öğrenci bütünün beşte biriyse bütün $48 \cdot 5 = 240$ öğrencidir.

**Kural.** Önce "bir derece kaç kişi?" ya da "bir kişi kaç derece?" sorusunu cevapla, sonra çarp. Yüzde verilirse: $\%100 = 360^\circ$, yani $\%1 = 3{,}6^\circ$ ve $\%25 = 90^\circ$.

İki dilimin **farkı** verildiğinde de aynı yol işler: açı farkı $40^\circ$ ve kişi farkı 20 ise $1^\circ$ = $0{,}5$ kişi; bütün $360 \cdot 0{,}5 = 180$ kişi.

## ÖSYM tuzakları

> **İki daire grafiğini açıyla karşılaştırmak:** 200 öğrencili okulda $90^\circ$'lik dilim 50 kişi, 600 öğrencili okulda $60^\circ$'lik dilim 100 kişidir. Büyük açı, büyük sayı demek değildir; daire grafiği yalnızca **oranı** gösterir. Karşılaştırmadan önce her grafiği kendi toplamıyla sayıya çevir.

> **En yüksek değer ile en çok artışı karıştırmak:** Çizgi grafiğinde "en çok arttığı dönem" sorulursa ardışık farklara bak, en yüksek noktaya değil.

> **Eksenin başladığı yeri görmemek:** Dikey eksen 0'dan başlamıyorsa sütun boyları yanıltır. "Kaç katı?" sorusunda değerleri eksenden oku ve böl.

> **Yüzdeyi açı sanmak:** $\%30$'luk dilimin açısı $30^\circ$ değil, $30 \cdot 3{,}6^\circ = 108^\circ$'dir.

> **Lejantı okumamak:** Çift sütunlu ya da çift çizgili grafikte renkleri karıştırmak, bütün işlemi doğru yapsan da yanlış cevap verir.

## Kendini dene

### Soru 1
72 kişilik bir grubun spor tercihleri daire grafiğinde gösterilmiştir. Yüzmeyi seçenlerin dilimi $50^\circ$'dir.

Buna göre yüzmeyi seçen kaç kişi vardır?

A) 5
B) 10
C) 14
D) 20
E) 50

**Cevap:** B
**Çözüm:** Bir derece $\frac{72}{360} = 0{,}2$ kişidir. $50 \cdot 0{,}2 = 10$ kişi. Kontrol: $\frac{10}{72} \cdot 360^\circ = 50^\circ$. 5, bir kişinin açısıdır ($360 : 72$); 14, $\frac{50}{360}$ oranını yüzde sanmaktan ($\approx \%14$); 20, daireyi $180^\circ$ almaktan gelir.

### Soru 2
Bir sınıftaki 36 öğrencinin göz renkleri şöyledir: kahverengi 18, yeşil 6, mavi 9, ela 3.

Bu veriler daire grafiğiyle gösterilirse kahverengi, yeşil, mavi ve ela dilimlerinin merkez açıları sırasıyla aşağıdakilerden hangisi olur?

A) $18^\circ, 6^\circ, 9^\circ, 3^\circ$
B) $90^\circ, 30^\circ, 45^\circ, 15^\circ$
C) $180^\circ, 60^\circ, 90^\circ, 30^\circ$
D) $180^\circ, 30^\circ, 90^\circ, 60^\circ$
E) $216^\circ, 72^\circ, 108^\circ, 36^\circ$

**Cevap:** C
**Çözüm:** Bir öğrenci $360^\circ : 36 = 10^\circ$'dir. Açılar $180^\circ$, $60^\circ$, $90^\circ$, $30^\circ$; toplam $360^\circ$. A sayıları açı sanmak, B daireyi $180^\circ$ almak, D yeşil ile elayı karıştırmak, E öğrencileri 30 kişi sayıp 12 ile çarpmaktır (toplamı $432^\circ$ olur).

### Soru 3
Bir okulun A sınıfında 30, B sınıfında 20 öğrenci vardır. Her sınıfta gözlük takan öğrenciler ayrı birer daire grafiğinde gösterilmiştir. Gözlüklülerin dilimi A sınıfının grafiğinde $72^\circ$, B sınıfının grafiğinde $108^\circ$'dir.

Buna göre gözlük takan öğrenci sayıları için aşağıdakilerden hangisi doğrudur?

A) A sınıfında 2 kişi fazladır.
B) B sınıfında 2 kişi fazladır.
C) B sınıfında 36 kişi fazladır.
D) İki sınıfta eşittir.
E) B sınıfında 1 kişi fazladır.

**Cevap:** D
**Çözüm:** A sınıfı: $\frac{72}{360} \cdot 30 = \frac{1}{5} \cdot 30 = 6$. B sınıfı: $\frac{108}{360} \cdot 20 = \frac{3}{10} \cdot 20 = 6$. İkisi de 6, eşit. B'nin açısı büyük diye B'de daha fazla gözlüklü olduğunu düşünmek tipik hatadır; $36$, açı farkını kişi sanmaktır.

## Özet kartı

- Çizgi grafiği zamanla değişimi, sütun grafiği karşılaştırmayı, daire grafiği bütüne oranı gösterir.
- Çizgi grafiğinde değişim = sonraki değer − önceki değer; en dik parça en hızlı değişimdir.
- Sütun grafiğinde değeri eksenden oku; eksen 0'dan başlamıyorsa boylar oranı vermez.
- Merkez açı $= \dfrac{\text{parça}}{\text{bütün}} \cdot 360^\circ$; açıların toplamı $360^\circ$.
- $\%1 = 3{,}6^\circ$, $\%25 = 90^\circ$, $\%50 = 180^\circ$.
- Farklı toplamlı iki daire grafiğini açıyla karşılaştırma; önce sayıya çevir.

## Sonraki adım

Alıştırmaya geç (aşağıdaki düğme). Grafik sorularında merkezi eğilim ölçüleri (ortalama, ortanca, tepe değer) de sık karşına çıkar; grafikten okuduğun değerlerle bu hesapları yapmaya hazır ol. Gerçek çıkmış sorular için MEBİ'deki "Çıkmış Sorular" testine bak.
