---
baslik: Periyodik Problemler
ders: tyt-matematik
sure: 20 dk
kaynak: MEBİ Konu Özeti 3e385c2ca5
guncelleme: 2026-11-18
---
# Periyodik Problemler

<div class="giris" dir="rtl" lang="ar">

**الدرس ده عن إيه؟** عن المسائل الدورية (periyodik problemler): حاجات بتتكرر كل فترة ثابتة زي أيام الأسبوع وساعات اليوم، وإزاي تحلها بالقسمة على الدورة (periyot) وتبص على الباقي (kalan) بس.

- هتعرف تجيب "بعد كام يوم هيبقى يوم إيه؟" وكمان "من كام يوم كان يوم إيه؟".
- هتفهم ليه المرة رقم 10 بتيجي بعد 9 فترات مش 10، وإزاي تستخدم المضاعف المشترك الأصغر (EKOK) لما حاجتين يتكرروا ويحصلوا مع بعض.
- هتتعلم تجيب العنصر رقم كذا في سلسلة بتتكرر، زي ألوان اللمبات، وإيه معنى إن الباقي يطلع صفر.

**ليه مهم؟** في TYT تقريبًا كل امتحان فيه سؤال قايم على فكرة الدورة دي، والفخ المشهور إنك تعد المرات غلط بفرق واحد.

هي 20 دقيقة بس، والفكرة واحدة بتتكرر في كل الأسئلة، أول ما تمسكها هتحلهم بسهولة.

</div>

**Bu dersin sonunda:** "kaç gün sonra hangi gün?", "kaçıncı kez hangi gün?", "iki olay kaçıncı kez birlikte?" ve "tekrar eden dizinin kaçıncı elemanı?" sorularını periyoda bölüp kalana bakarak çözebileceksin.

> **TYT'de yeri:** Neredeyse her sınavda bir soru periyot mantığına dayanır. Sık kalıplar: "Bugün salıysa 100 gün sonra hangi gündür?", "4 günde bir nöbet tutan biri 12. nöbetini hangi gün tutar?", "iki kişi 5. kez birlikte hangi gün karşılaşır?" ve tekrar eden bir ışık ya da harf dizisinin kaçıncı elemanı.

## Önce hatırla

<details><summary>EBOB-EKOK Problemleri'nden: 84 m ile 60 m boyutlarındaki dikdörtgen bir tarla, eşit büyüklükte ve olabildiğince büyük kare parsellere ayrılacak. Kaç parsel elde edilir?</summary>
Bütünü en büyük eş parçalara bölmek EBOB ister: $\text{EBOB}(84, 60) = 12$. Kenarlar $84 \div 12 = 7$ ve $60 \div 12 = 5$ parçaya ayrılır: $7 \cdot 5 =$ <b>35 parsel</b>.
</details>

<details><summary>EBOB-EKOK Problemleri'nden: Bir duraktan iki otobüs hattı 12 dakikada bir ve 18 dakikada bir kalkıyor. İkisi 08.00'de birlikte kalktıysa bir sonraki birlikte kalkış saat kaçtadır?</summary>
Tekrarlanan iki olayın yeniden çakışması EKOK ister: $\text{EKOK}(12, 18) = 36$ dakika. Saat <b>08.36</b>. Bu derste aynı fikri "kaçıncı kez, hangi gün" sorularına taşıyacaksın.
</details>

## Periyot ve kalan

Belli aralıklarla aynen tekrar eden olaya **periyodik olay**, tekrar aralığına **periyot** denir. Haftanın günleri 7 günde bir, saat 24 saatte bir tekrar eder.

**Örnek.** Bugün çarşamba. 90 gün sonra hangi gün olur?

Her 7 günde bir yine çarşambaya döneriz; bu tam turlar sonucu değiştirmez. O yüzden 90'ı 7'ye böl, yalnızca kalana bak:

$$90 = 7 \cdot 12 + 6$$

12 tam hafta sonra yine çarşamba; sonra 6 gün daha ileri: perşembe, cuma, cumartesi, pazar, pazartesi, **salı**.

![Haftanın yedi günü bir çemberin üstünde, çarşamba en üstte. Çarşambadan saat yönünde altı adım giden mavi ok salıda bitiyor. Ortada 90 eşittir 7 çarpı 12 artı 6 yazıyor.](gorsel/tyt-matematik/02-07-hafta-cemberi.svg "Günler bir çember gibi döner. 12 tam tur seni çarşambaya geri getirir, sonucu yalnızca kalan 6 adım belirler.")

**Geriye gitmek.** Aynı soru "90 gün önce" diye sorulursa 6 gün **geri** gidersin: çarşambadan 6 gün önce **perşembe**. Kısa yol: 6 gün geri gitmek, $7 - 6 = 1$ gün ileri gitmekle aynıdır.

**Kural.** Periyot $p$ olan bir olayda $n$ adım sonrası için $n$'yi $p$'ye böl. Kalan $k$ ise başlangıçtan $k$ adım ileri git. **Kalan 0 ise başlangıçtaki yerdesin.**

| Olay | Periyot |
|---|---|
| Haftanın günleri | 7 gün |
| Günün saatleri | 24 saat |
| Saat kadranı (akrep) | 12 saat |
| Yılın ayları | 12 ay |
| Bir yıl | 365 gün ($= 7 \cdot 52 + 1$) |

**Saatle örnek.** Saat 15.00. 100 saat sonra saat kaç olur? $100 = 24 \cdot 4 + 4$; 4 gün sonra yine 15.00, sonra 4 saat daha: **19.00**.

## Kaçıncı kez?

**Örnek.** Bir öğrenci 3 günde bir kursa gidiyor. İlk kez cuma günü gitti. 10. kez hangi gün gider?

İlk gidiş zaten cuma; ondan sonra 9 gidiş daha var. 10 gidiş arasında **9 aralık** vardır, bir çitin 10 direği arasında 9 boşluk olduğu gibi:

![Sayı doğrusunda 0'dan 27'ye kadar 3'er gün arayla 10 nokta. Noktaların üstünde 1. ile 10. arası sıra numaraları, altlarında 9 yay ve 9 aralık çarpı 3 gün eşittir 27 gün yazısı.](gorsel/tyt-matematik/02-07-kacinci-kez.svg "10 nokta arasında 9 yay var. 1. gidiş 0. günde olduğu için 10. gidiş 27. gündedir, 30. günde değil.")

Geçen süre $9 \cdot 3 = 27$ gün. $27 = 7 \cdot 3 + 6$; cumadan 6 gün sonra: **perşembe**.

**Kural.** $d$ günde bir tekrarlanan olayın $n$. kez gerçekleşmesi, ilkinden $(n - 1) \cdot d$ gün sonradır.

Tuzak: $10 \cdot 3 = 30$ alırsan $30 = 7 \cdot 4 + 2$ ve cevabı pazar bulursun. ÖSYM'nin çeldiricisi tam olarak budur.

## İki olay birlikte

**Örnek.** Bir hemşire 6 günde bir, diğeri 10 günde bir nöbet tutuyor. İkisi ilk kez pazar günü birlikte nöbet tuttu. 4. kez birlikte hangi gün nöbet tutarlar?

Birlikte nöbet günleri hem 6'nın hem 10'un katı olan günlerdir. Bunların en küçüğü $\text{EKOK}(6, 10) = 30$. Yani ortak nöbet 30 günde bir tekrar eder; yeni periyot 30'dur.

![İki satır nokta: üstte 6 günde bir, altta 10 günde bir. 0, 30, 60 ve 90. günlerde iki satırdaki noktalar üst üste geliyor ve sarı kutuyla 1., 2., 3., 4. kez diye işaretli.](gorsel/tyt-matematik/02-07-ortak-gunler.svg "İki satırın aynı anda dolu olduğu günler 30'un katları. 4. ortak nöbet 90. gündedir, çünkü 1. ortak nöbet 0. gündür.")

4. kez için 3 aralık: $3 \cdot 30 = 90$ gün. $90 = 7 \cdot 12 + 6$; pazardan 6 gün sonra: **cumartesi**.

**Kural.** İki ya da daha fazla periyodik olayın birlikte tekrarı **EKOK** günde birdir. Sonra "kaçıncı kez" kuralı aynen uygulanır: $(n - 1) \cdot \text{EKOK}$.

Bir ilginç durum: Periyotlardan biri 7'nin katıysa (örneğin 5 ve 7) EKOK da 7'nin katı olur. O zaman ortak günler **hep haftanın aynı günü** gelir.

![Akış şeması: periyodu bul; iki olay birlikteyse periyot EKOK olur; atılan adımı bul; adımı periyoda böl; kalan 0 değilse kalan kadar ilerle, kalan 0 ise başlangıçla aynı yerdesin.](gorsel/tyt-matematik/02-07-yontem.svg "Gün ve saat sorularının hepsi bu dört adımdır. En çok hata atılan adımda yapılır: n. kez için adım sayısı n eksi 1'dir.")

## Tekrar eden diziler

**Örnek.** Bir ışık zincirinde ampuller sırayla kırmızı, sarı, yeşil, mavi diye diziliyor ve bu dörtlü baştan tekrar ediyor. 50. ampul hangi renktir? 48. ampul hangi renktir?

Periyot 4'tür. Sıra numarasını 4'e böl:

- $50 = 4 \cdot 12 + 2$. 12 tam dörtlüden sonra 2. ampul: **sarı**.
- $48 = 4 \cdot 12 + 0$. Kalan 0, yani 48. ampul 12. dörtlünün **son** ampulü: **mavi**.

**Kural.** Periyodu $p$ olan bir dizide $n$. eleman için $n$'yi $p$'ye böl. Kalan $k$ ise periyodun $k$. elemanı; **kalan 0 ise periyodun son elemanı**.

Gün sorularından farkına dikkat et: orada başlangıçtan atılan **adımı** böldün, kalan 0 başlangıçtaki güne döndürdü. Burada **sıra numarasını** bölüyorsun; kalan 0 periyodun sonunu verir. İkisi de doğru, yeter ki neyi böldüğünü bil.

"İlk 50 ampulden kaçı sarı?" gibi sayma sorularında: 12 tam dörtlüde 12 sarı, kalan 2 ampulde (kırmızı, sarı) 1 sarı daha; toplam **13**.

## ÖSYM tuzakları

> **n. kez için n adım saymak:** "4 günde bir giden biri 12. kez ne zaman gider?" sorusunda geçen süre $12 \cdot 4$ değil $11 \cdot 4$ gündür. İlk gidiş sayılır, aralık sayısı bir eksiktir.

> **Kalan 0'ı yanlış okumak:** Gün sorusunda kalan 0 ise cevap başlangıç günüdür, "bir önceki gün" ya da "0. gün" diye bir şey yoktur. Dizi sorusunda kalan 0 ise cevap periyodun son elemanıdır, ilk elemanı değil.

> **Geri sayarken ileri gitmek:** "60 gün önce" sorusunda kalan kadar geri git. İleri gidersen ÖSYM'nin hazır çeldiricisini işaretlersin.

> **Ayları 30 gün saymak:** Tarih sorularında her ayın gün sayısını tek tek kullan (mart 31, nisan 30, şubat 28 ya da 29). Bir yıl 365 gün, yani $52$ hafta $+ 1$ gün: aynı tarih ertesi yıl haftanın bir sonraki gününe kayar.

> **24 saat yerine 12 almak:** "Saat kaç olur?" sorusu 24 saatlik gösterimle soruluyorsa periyot 24'tür. $70$ saat sonrası için $70 = 24 \cdot 2 + 22$ yazılır; $70 = 12 \cdot 5 + 10$ yanlış saati verir.

## Kendini dene

### Soru 1
Bugün perşembe. 150 gün sonra hangi gün olur?

A) Cuma
B) Cumartesi
C) Pazar
D) Pazartesi
E) Salı

**Cevap:** C
**Çözüm:** $150 = 7 \cdot 21 + 3$. 21 tam haftadan sonra yine perşembe; 3 gün ileri: cuma, cumartesi, pazar. Cevap pazar.

### Soru 2
Bir bitki 5 günde bir sulanıyor. İlk kez salı günü sulandığına göre 8. kez hangi gün sulanır?

A) Pazartesi
B) Salı
C) Perşembe
D) Cuma
E) Pazar

**Cevap:** B
**Çözüm:** 8 sulama arasında 7 aralık var: $7 \cdot 5 = 35$ gün. $35 = 7 \cdot 5 + 0$; kalan 0, yani yine salı. $8 \cdot 5 = 40$ alan, $40 = 7 \cdot 5 + 5$ bulur ve salıdan 5 gün sonrasını, pazarı işaretler.

### Soru 3
Bir kolyede boncuklar kırmızı, mavi, mavi, sarı, yeşil sırasıyla dizilmiş ve bu beşli baştan tekrar ediyor. İlk 63 boncuktan kaç tanesi mavidir?

A) 22
B) 24
C) 25
D) 26
E) 27

**Cevap:** D
**Çözüm:** Periyot 5, her beşlide 2 mavi. $63 = 5 \cdot 12 + 3$. 12 tam beşlide $12 \cdot 2 = 24$ mavi. Kalan 3 boncuk kırmızı, mavi, mavi: 2 mavi daha. Toplam $24 + 2 = 26$. Kalanı unutan 24, oranla $63 \cdot \frac{2}{5} = 25{,}2$ hesaplayıp yuvarlayan 25 bulur.

## Özet kartı

- Periyodik olayda tam turlar sonucu değiştirmez: periyoda böl, **kalana** bak.
- Gün sorusu: kalan kadar ileri (önce sorulursa geri) git; kalan 0 ise aynı gün.
- $n$. kez $= (n - 1)$ aralık sonrası.
- Birlikte tekrar EKOK'ta bir; $n$. kez birlikte $= (n - 1) \cdot \text{EKOK}$.
- Dizide $n$. eleman: kalan $k$ ise $k$. eleman, kalan 0 ise periyodun son elemanı.
- Tarih sorusunda ayların gerçek gün sayısını kullan; 1 yıl $= 52$ hafta $+ 1$ gün.

## Sonraki adım

Alıştırmaya geç (aşağıdaki düğme). Bu ders Bölünebilme Kuralları konusunu kapatıyor. Sonraki ders **Aralık Kavramı**; eşitsizlik ve denklem konusuna geçeceksin ve "Önce hatırla" sorularında periyodik problemlere geri döneceksin.
