---
baslik: Sayı Problemleri
ders: tyt-matematik
sure: 20 dk
kaynak: MEBİ Konu Özeti 364ee2b827
guncelleme: 2026-11-18
---
# Sayı Problemleri

<div class="giris" dir="rtl" lang="ar">

**الدرس ده عن إيه؟** عن المسائل الكلامية للأعداد (sayı problemleri): إزاي تحوّل كلام المسألة جملة جملة لمعادلة (denklem) أو متباينة (eşitsizlik) وتحلّها.

- هتتعلم تترجم عبارات زي "3 أضعاف العدد ناقص 5" صح، وتاخد بالك إن الترتيب بيفرق.
- هتحل مسائل مجموع وفرق عددين، ونوعين من الحاجات زي ترابيزات بـ4 كراسي وترابيزات بـ6، ومسائل التوزيع اللي فيها حاجة بتزيد أو بتنقص.
- هتشتغل على الأعداد المتتالية (ardışık sayılar) والمسائل اللي محتاجة متباينة زي "أكبر عدد صحيح".

**ليه مهم؟** دي من أول أسئلة جزء المسائل في TYT وبييجي منها كذا سؤال كل سنة، والدرجة بتضيع غالبًا لما تفتكر إن المجهول اللي طلعته هو المطلوب.

الدرس 20 دقيقة بس، وبعده هتقرا أي مسألة كلامية بثقة أكتر.

</div>

**Bu dersin sonunda:** bir problem metnini cümle cümle cebirsel ifadeye çevirip tek bilinmeyenli bir denklem ya da eşitsizlik kurabilecek ve sonunda sorunun gerçekten istediği sayıyı verebileceksin.

> **TYT'de yeri:** Problem bölümünün ilk sorularıdır ve her yıl birkaç tane gelir. Yeni nesil sorularda bilet, masa, terazi, puan gibi günlük bir durum verilir. Denklem kolaydır; puanı kaybettiren, metni yanlış çevirmek ya da bulunan $x$'i istenen sanmaktır.

## Önce hatırla

<details><summary>Oran-orantı problemlerinden: 10 işçi bir işi 12 günde bitiriyor. Aynı hızda çalışan 15 işçi bu işi kaç günde bitirir?</summary>
İşçi artınca süre azalır: ters orantı, çarpım sabit. $10 \cdot 12 = 120 = 15 \cdot x$, $x = 8$ gün.
</details>

<details><summary>Oran-orantı problemlerinden: 450 TL; 2, 3 ve 4 sayılarıyla doğru orantılı paylaştırılırsa en büyük pay kaç TL olur?</summary>
Paylar $2k$, $3k$, $4k$. $9k = 450$, $k = 50$. En büyük pay $4k = 200$ TL.
</details>

## Sözel ifadeyi cebire çevirmek

**Örnek.** Bir sayının 3 eksiğinin 4 katı, aynı sayının 2 katının 6 fazlasına eşittir. Bu sayı kaçtır?

Sayıya $x$ de ve cümleyi parça parça çevir:

- "3 eksiğinin 4 katı": önce 3 çıkar, sonra 4 ile çarp: $4(x - 3)$
- "2 katının 6 fazlası": önce 2 ile çarp, sonra 6 ekle: $2x + 6$

$$4(x - 3) = 2x + 6 \;\Rightarrow\; 4x - 12 = 2x + 6 \;\Rightarrow\; 2x = 18 \;\Rightarrow\; x = 9$$

Kontrol: $4 \cdot 6 = 24$ ve $2 \cdot 9 + 6 = 24$. Doğru.

**Kural.** Türkçede işlem sırası **soldan sağa** okunur: ilk söylenen işlem önce yapılır. Sık kullanılan çeviriler:

| Sözel ifade | Cebirsel karşılık |
|---|---|
| Bir sayının 7 fazlası | $x + 7$ |
| Bir sayının 7 eksiği | $x - 7$ |
| 3 katının 5 eksiği | $3x - 5$ |
| 5 eksiğinin 3 katı | $3(x - 5)$ |
| Yarısının 4 fazlası | $\frac{x}{2} + 4$ |
| Karesi ile kendisinin toplamı | $x^2 + x$ |
| Farkı 6 olan iki sayı | $x$ ve $x + 6$ |
| Toplamı 40 olan iki sayı | $x$ ve $40 - x$ |

> **Tuzak:** "3 katının 5 eksiği" ile "5 eksiğinin 3 katı" farklıdır: $3x - 5 \ne 3(x - 5)$. Paranteze dikkat.

## Problem çözme sırası

Her problemde aynı adımları izle. En çok atlanan adım sondakidir: bulduğun $x$ çoğu zaman sorunun cevabı değildir.

![Akış şeması: verileni ve isteneni yaz, bilinmeyene harf ver, denklemi kur ve çöz. Sonra x istenen mi diye sor: evetse soruda yerine koy, hayırsa önce isteneni hesapla sonra yerine koy.](gorsel/tyt-matematik/05-03-yontem.svg "Son karar kutusu puan kazandırır: x istenen değilse bir adım daha var.")

İpucu: Bilinmeyen olarak çoğu zaman **sorulan** çokluğu seç. Böylece son adım kendiliğinden kısalır.

## Toplamı ve farkı verilen iki sayı

**Örnek.** Toplamı 58, farkı 14 olan iki sayıdan büyüğü kaçtır?

Küçük sayı $x$ olsun; büyük sayı ondan 14 fazladır: $x + 14$.

$$x + (x + 14) = 58 \;\Rightarrow\; 2x = 44 \;\Rightarrow\; x = 22$$

Büyük sayı $22 + 14 = 36$. Kontrol: $22 + 36 = 58$, $36 - 22 = 14$.

![İki şerit. Üstteki büyük sayı şeridi x uzunluğunda mavi parça ile 14 yazan sarı parçadan oluşur. Alttaki küçük sayı şeridi yalnızca x parçasıdır. İkisinin toplamı 58. Altta 2x + 14 = 58, x = 22, büyük sayı 36 yazar.](gorsel/tyt-matematik/05-03-toplam-fark.svg "Fazlalık olan 14'ü toplamdan çıkarınca geriye iki eşit x kalır.")

**Kural.** Toplam $T$, fark $F$ ise

$$\text{büyük} = \frac{T + F}{2}, \qquad \text{küçük} = \frac{T - F}{2}$$

Bu kısayolu ezberlemek yerine şeridi düşün: farkı çıkarınca kalan iki eşit parçadır.

## İki türlü nesne: hepsini aynı türden say

**Örnek.** Bir düğün salonunda 25 masa var. Masaların bir kısmı 4 kişilik, diğerleri 6 kişiliktir. Salon tam dolduğunda 124 kişi oturuyor. Salonda kaç tane 4 kişilik masa vardır?

Denklemle: 6 kişilik masa sayısı $x$ ise 4 kişilik masa sayısı $25 - x$ olur.

$$6x + 4(25 - x) = 124 \;\Rightarrow\; 2x + 100 = 124 \;\Rightarrow\; x = 12$$

6 kişilik masa 12 tane, **4 kişilik masa $25 - 12 = 13$ tane**. Kontrol: $13 \cdot 4 + 12 \cdot 6 = 52 + 72 = 124$.

Akıldan: Bütün masaları 4 kişilik say: $25 \cdot 4 = 100$ kişi. Eksik $124 - 100 = 24$ kişi. Bir masayı 6 kişiliğe çevirmek 2 kişi ekler: $24 \div 2 = 12$ masa 6 kişiliktir.

**Kural.** İki tür nesnenin toplam sayısı ve toplam değeri verilirse birine $x$, diğerine "toplam $- x$" de. Aynı yol araba ve motosiklet tekerleği, tam ve öğrenci bileti, doğru ve yanlış cevap sorularında da çalışır.

> **Tuzak:** Denklemde $x$ 6 kişilik masaydı; soru 4 kişiliği soruyor. 12 seçeneği büyük olasılıkla şıklarda seni bekliyor.

## Dağıtma problemleri

**Örnek.** Bir grup öğrenciye kurabiye dağıtılıyor. Her öğrenciye 6 kurabiye verilirse 8 kurabiye artıyor, 8 kurabiye verilirse 10 kurabiye eksik kalıyor. Kaç kurabiye vardır?

Öğrenci sayısı $n$ olsun. Kurabiye sayısını iki yoldan yaz ve eşitle:

$$6n + 8 = 8n - 10 \;\Rightarrow\; 18 = 2n \;\Rightarrow\; n = 9$$

Kurabiye $6 \cdot 9 + 8 = 62$. Kontrol: $8 \cdot 9 - 10 = 62$.

![İki satır, her birinde 9 öğrenciyi gösteren 9 kutu. Üst satır 6'şar: her kutuda 6, yanında 8 artar yazan sarı kutu. Alt satır 8'er: her kutu 6 ve üstünde +2, yanında 10 eksik yazan kesik çizgili kırmızı kutu. Altta: kişi başı +2 için gereken 8 + 10 = 18, 18 bölü 2 = 9 kişi.](gorsel/tyt-matematik/05-03-dagitma.svg "Herkese 2 fazla vermek için önce artan 8 harcanır, sonra 10 daha gerekir.")

**Kural.** Kişi sayısı $=\dfrac{\text{artan} + \text{eksik}}{\text{kişi başı fark}}$. Her iki durumda da artıyorsa artanların farkını, her ikisinde de eksik kalıyorsa eksiklerin farkını böl. Emin değilsen denklemi kur: dağıtılan miktar iki durumda da aynıdır.

> **Tuzak:** "4 sıra boş kalıyor" ile "4 kişi eksik kalıyor" aynı şey değildir. 4 boş sıra, sıra başına düşen kişi sayısı kadar eksik demektir: $3(s - 4)$.

## Ardışık sayılar

**Örnek.** Ardışık üç tek sayının toplamı 81'dir. En büyüğü kaçtır?

Ortadakine $x$ de: sayılar $x - 2$, $x$, $x + 2$. Toplam $3x = 81$, $x = 27$. Sayılar 25, 27, 29; en büyüğü 29.

**Kural.** Ardışık tam sayılar 1'er, ardışık tek ya da çift sayılar **2'şer** artar. Tek sayıda ardışık sayı toplanıyorsa ortadakine $x$ demek işlemi kısaltır: ortadaki sayı $=$ toplam $\div$ adet.

## Eşitsizlik kuran problemler

**Örnek.** Bir sayının 3 katının 7 eksiği 20'den küçüktür. Bu koşulu sağlayan en büyük tam sayı kaçtır?

$$3x - 7 < 20 \;\Rightarrow\; 3x < 27 \;\Rightarrow\; x < 9$$

9 dahil değildir; en büyük tam sayı **8**.

**Kural.** "En az", "en çok", "-den küçük", "-yi geçmeyen" gibi ifadeler eşitsizlik ister. Sonucu tam sayıya çevirirken eşitliğin dahil olup olmadığına ve gerçek durumda (kişi, koli, otobüs) yukarı mı aşağı mı yuvarlanacağına bak.

## ÖSYM tuzakları

> **Sırayı ters çevirmek:** "5 eksiğinin 3 katı" $3(x - 5)$'tir, $3x - 5$ değil. İlk söylenen işlem önce yapılır.

> **Bulunan $x$'i cevap sanmak:** Masa, bilet, kurabiye sorularında denklem bir çokluğu verir, soru çoğu zaman diğerini ister. Cevabı işaretlemeden önce soru kökünü bir kez daha oku.

> **Ardışık çift ya da tek sayılarda 1'er artırmak:** Ardışık çift sayılar $x$, $x + 2$, $x + 4$ diye yazılır. $x$, $x + 1$, $x + 2$ yazan yanlış sonuç bulur.

> **Kesin eşitsizlikte sınırı almak:** $x < 9$ ise 9 cevap olamaz. Kapasite sorularında ($\le$) ise sınır dahildir ama sonuç kesirliyse **aşağı** yuvarlanır: 22,4 koli sığıyorsa cevap 22'dir.

## Kendini dene

### Soru 1
Bir sayının 4 katının 9 eksiği, aynı sayının 2 katının 15 fazlasına eşittir.

Buna göre bu sayı kaçtır?

A) 3
B) 6
C) 12
D) 18
E) 24

**Cevap:** C
**Çözüm:** $4x - 9 = 2x + 15$, $2x = 24$, $x = 12$. Kontrol: $48 - 9 = 39$ ve $24 + 15 = 39$. 24, $2x$'i bulup ikiye bölmeyi unutmaktan; 3, $4x + 9 = 2x + 15$ diye işareti yanlış yazmaktan gelir.

### Soru 2
Bir otoparkta otomobil ve motosikletlerden oluşan toplam 20 araç vardır. Otomobillerin 4, motosikletlerin 2 tekerleği olduğuna ve toplam tekerlek sayısı 64 olduğuna göre otoparkta kaç motosiklet vardır?

A) 6
B) 8
C) 10
D) 12
E) 14

**Cevap:** B
**Çözüm:** Hepsini motosiklet say: $20 \cdot 2 = 40$ tekerlek. Eksik $64 - 40 = 24$; bir motosikleti otomobile çevirmek 2 tekerlek ekler, $24 \div 2 = 12$ otomobil. Motosiklet $20 - 12 = 8$. Kontrol: $12 \cdot 4 + 8 \cdot 2 = 64$. 12, otomobil sayısıdır.

### Soru 3
Bir öğretmen kalemleri öğrencilerine dağıtıyor. Her öğrenciye 3 kalem verirse 10 kalem artıyor, 4 kalem verirse 5 kalem eksik kalıyor.

Buna göre öğretmenin kaç kalemi vardır?

A) 15
B) 45
C) 50
D) 55
E) 60

**Cevap:** D
**Çözüm:** Öğrenci sayısı $n$: $3n + 10 = 4n - 5$, $n = 15$. Kalem $3 \cdot 15 + 10 = 55$; kontrol $4 \cdot 15 - 5 = 55$. 15 öğrenci sayısıdır; 45 ve 60, artan ve eksik kalemi hesaba katmamaktan gelir.

## Özet kartı

- İlk söylenen işlem önce yapılır: "5 eksiğinin 3 katı" $= 3(x - 5)$.
- Bilinmeyen olarak sorulan çokluğu seç; seçmediysen sonda isteneni hesapla.
- Toplam $T$, fark $F$: büyük $= \frac{T + F}{2}$, küçük $= \frac{T - F}{2}$.
- İki türlü nesne: birine $x$, diğerine "toplam $- x$"; ya da hepsini aynı türden say.
- Dağıtma: kişi sayısı $=$ (artan $+$ eksik) $\div$ kişi başı fark.
- Ardışık tek/çift sayılar 2'şer artar; eşitsizlikte sınırın dahil olup olmadığına bak.

## Sonraki adım

Alıştırmaya geç (aşağıdaki düğme). Sonraki ders **Kesir Problemleri**: aynı çeviri adımlarını "üçte biri", "kalanın yarısı" gibi kesirli ifadelerle kuracaksın.
