---
baslik: Olasılık Kavramı İle İlgili Uygulamalar
ders: tyt-matematik
sure: 25 dk
kaynak: MEBİ Konu Özeti 44b292d4db
guncelleme: 2026-11-18
---
# Olasılık Kavramı İle İlgili Uygulamalar

<div class="giris" dir="rtl" lang="ar">

**الدرس ده عن إيه؟** هنا هتبدأ تحسب الاحتمال (olasılık) بجد: عدد النتايج اللي عايزها على عدد كل النتايج، في الزهر والعملة والكروت والكيس اللي فيه بلي.

- هتعرف إن الاحتمال دايمًا بين 0 و 1، وإن الحدث المستحيل (imkânsız olay) احتماله 0 والحدث المؤكد (kesin olay) احتماله 1.
- هتستخدم الحدث المكمّل (tümleyen) في أسئلة "على الأقل واحد"، وتعرف إمتى تطرح الجزء المشترك في أسئلة "أو" لما الحدثين مش متنافيين (ayrık değil).
- هتعرف تلاقي عدد البلي المجهول في الكيس لو الاحتمال معروف، حتى بعد ما نزوّد بلي جديد.

**ليه مهم؟** في TYT بييجي سؤال احتمال كل سنة تقريبًا، والحساب فيه سهل؛ الشطارة إنك تعدّ فضاء العينة (örnek uzay) والحدث صح من غير ما تعدّ حاجة مرتين.

خد ٢٥ دقيقة على رواقة، وهتلاقي الاحتمال بقى أسهل بكتير مما كنت فاكر.

</div>

**Bu dersin sonunda:** eş olası çıktılarda bir olayın olasılığını $\dfrac{s(A)}{s(E)}$ ile hesaplayabilecek, "en az bir" sorularında tümleyeni, "veya" sorularında birleşim kuralını kullanabilecek ve olasılığı verilen bir torbadaki bilinmeyen sayıyı bulabileceksin.

> **TYT'de yeri:** Her yıl 1 soru gelir. Kalıplar: zar, para, kart ya da torbadan çekilişte "olasılığı kaçtır?"; "en az bir" içeren sorular; iki koşuldan biri istenen "veya" soruları; olasılığı verilip torbadaki bilye sayısının sorulduğu yeni nesil sorular. İşlem yükü azdır; asıl iş örnek uzayı ve olayı doğru saymaktır.

## Önce hatırla

<details><summary>Geçen dersten: İki zar atılıyor. Üst yüzlerdeki sayıların toplamının 7 olması olayı kaç elemanlıdır?</summary>
Çıktılar sıralı ikililerdir: $(1,6), (2,5), (3,4), (4,3), (5,2), (6,1)$. Olay <b>6 elemanlıdır</b>. $(1,6)$ ile $(6,1)$'i tek sayan 3 bulur ve yanılır.
</details>

<details><summary>Geçen dersten: Üç madenî para atılıyor. "En az bir tura" olayının tümleyeni nedir, kaç elemanlıdır?</summary>
Tümleyen "hiç tura gelmemesi"dir: $\{YYY\}$, 1 eleman. Bu yüzden "en az bir tura" $8 - 1 = 7$ elemanlıdır. Bugün bu iki sayıyı oranlayacaksın: olasılık $\dfrac{7}{8}$.
</details>

## Olasılık: istenen bölü tümü

**Örnek 1.** Bir zar atılıyor. Asal sayı gelme olasılığı kaçtır?

- Örnek uzay: $E = \{1, 2, 3, 4, 5, 6\}$, $s(E) = 6$. Her yüzün gelme şansı eşittir.
- Olay: $A = \{2, 3, 5\}$, $s(A) = 3$.
- $P(A) = \dfrac{3}{6} = \dfrac{1}{2}$.

**Örnek 2.** İki zar atılıyor. Toplamın 8 olma olasılığı kaçtır?

- $s(E) = 6 \cdot 6 = 36$.
- Toplamı 8 olanlar: $(2,6), (3,5), (4,4), (5,3), (6,2)$, yani $s(A) = 5$.
- $P(A) = \dfrac{5}{36}$.

**Kural.** Çıktıları **eş olası** olan bir örnek uzayda

$$P(A) = \frac{s(A)}{s(E)} = \frac{\text{istenen çıktı sayısı}}{\text{bütün çıktıların sayısı}}$$

Bu kural yalnızca her çıktının şansı eşitse çalışır. İki zarda 36 sıralı ikili eş olasıdır; ama 2'den 12'ye kadar 11 farklı **toplam** eş olası değildir:

![Çubuk grafik: yatay eksende iki zarın toplamı 2'den 12'ye, çubukların yüksekliği 1, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1. En yüksek çubuk 7, yeşil.](gorsel/tyt-matematik/10-02-toplam-dagilimi.svg "Toplam 7'yi 6 çıktı verir, toplam 2'yi yalnızca 1. Bu yüzden toplamların olasılığı 1/11 değildir; 36 çıktı üzerinden sayılır.")

> **Tuzak:** "Toplam 8'in olasılığı $\dfrac{1}{11}$" demek, 11 toplamı eş olası saymaktır. Örnek uzayı her zaman eş olası çıktılardan kur: iki zarda 36 sıralı ikili.

## Olasılık 0 ile 1 arasındadır

**Örnek 3.** Bir zar atılıyor.

- "7 gelmesi" hiçbir çıktıda olmaz: $P = \dfrac{0}{6} = 0$. **İmkânsız olay**.
- "7'den küçük gelmesi" her çıktıda olur: $P = \dfrac{6}{6} = 1$. **Kesin olay**.

![0'dan 1'e uzanan olasılık ölçeği. 0'da zarda 7 (imkânsız), 1/6'da zarda 6, 1/2'de parada yazı, 5/6'da zarda 6 gelmemesi, 1'de zarda 7'den küçük (kesin).](gorsel/tyt-matematik/10-02-olasilik-olcegi.svg "Her olasılık bu ölçeğin üzerindedir. 1/6 ile 5/6'ya bak: bir olay ile tümleyeninin olasılıkları toplamı 1'dir.")

**Kural.** Her A olayı için $0 \le P(A) \le 1$. İmkânsız olayın olasılığı 0, kesin olayınki 1'dir. Hesabın 1'den büyük ya da negatif çıktıysa bir yerde hata var.

## Tümleyen: "en az bir" sorularının kısa yolu

**Örnek 4.** İki zar atılıyor. En az birinin 6 gelme olasılığı kaçtır?

- Tümleyen: hiçbirinin 6 gelmemesi. Her zar için 5 seçenek: $5 \cdot 5 = 25$ çıktı.
- $P(\text{hiç 6 yok}) = \dfrac{25}{36}$.
- $P(\text{en az bir 6}) = 1 - \dfrac{25}{36} = \dfrac{11}{36}$.

**Örnek 5.** Bir A olayı için $P(A) = 2 \cdot P(A')$ ise $P(A)$ kaçtır?

$P(A) + P(A') = 1$ olduğundan $2P(A') + P(A') = 1$, $P(A') = \dfrac{1}{3}$ ve $P(A) = \dfrac{2}{3}$.

**Kural.** $P(A) + P(A') = 1$, yani $P(A) = 1 - P(A')$. "En az bir" görünce tümleyeni ("hiç") hesapla, 1'den çıkar.

> **Tuzak:** İki zarda "en az bir 6" için $\dfrac{1}{6} + \dfrac{1}{6} = \dfrac{12}{36}$ demek $(6,6)$'yı iki kez saymaktır. Doğrusu $\dfrac{11}{36}$.

## "Veya": ayrık ve ayrık olmayan olaylar

**Örnek 6 (ayrık).** Bir zar atılıyor. 2'den küçük **veya** 5'ten büyük gelme olasılığı kaçtır?

$A = \{1\}$, $B = \{6\}$; ortak çıktı yok. $P(A \cup B) = \dfrac{1}{6} + \dfrac{1}{6} = \dfrac{1}{3}$.

**Örnek 7 (ayrık değil).** 1'den 30'a kadar numaralanmış 30 karttan biri rastgele çekiliyor. Kartın 2'ye **veya** 3'e bölünme olasılığı kaçtır?

- 2'ye bölünen: 15 kart, 3'e bölünen: 10 kart.
- İkisine birden (yani 6'ya) bölünen: 6, 12, 18, 24, 30, yani 5 kart. Bunlar iki grupta da sayıldı.
- $P = \dfrac{15}{30} + \dfrac{10}{30} - \dfrac{5}{30} = \dfrac{20}{30} = \dfrac{2}{3}$.

![Venn şeması: E içinde 30 kart. A (2'ye bölünen) dairesinin yalnız kısmında 10, kesişimde 5, B (3'e bölünen) dairesinin yalnız kısmında 5, dışarıda 10 kart.](gorsel/tyt-matematik/10-02-venn-2-3.svg "Kesişimdeki 5 kart hem 15'in hem 10'un içinde. Toplamdan bir kez çıkarılmazsa iki kez sayılmış olur.")

**Kural.**

| Olaylar | $P(A \text{ veya } B) = P(A \cup B)$ |
|---|---|
| Ayrık ($A \cap B = \varnothing$) | $P(A) + P(B)$ |
| Ayrık değil | $P(A) + P(B) - P(A \cap B)$ |

İlk satır ikincinin özel hâlidir: ayrık olaylarda $P(A \cap B) = 0$.

> **Tuzak:** 2'ye veya 3'e bölünenler için $\dfrac{15 + 10}{30} = \dfrac{5}{6}$ bulmak, 6'nın katlarını iki kez saymaktır. Toplamadan önce sor: "İkisine birden uyan var mı?"

## Olasılıktan sayıya: torba soruları

**Örnek 8.** Bir torbada 6 kırmızı ve bir miktar mavi bilye var. Rastgele çekilen bir bilyenin kırmızı olma olasılığı $\dfrac{2}{5}$'tir.

a) Torbada kaç mavi bilye vardır?

Mavi bilye sayısı $m$ olsun: $\dfrac{6}{6 + m} = \dfrac{2}{5}$, $\;30 = 12 + 2m$, $\;m = 9$. Toplam 15 bilye.

b) Torbaya kaç mavi bilye eklenirse kırmızı çekme olasılığı $\dfrac{1}{4}$ olur?

Kırmızı sayısı değişmez, toplam büyür: $\dfrac{6}{15 + x} = \dfrac{1}{4}$, $\;15 + x = 24$, $\;x = 9$.

**Kural.** Olasılık bir orandır: $\dfrac{2}{5}$, "her 5 bilyenin 2'si" demektir; gerçek sayı $\dfrac{4}{10}$, $\dfrac{6}{15}$ gibi bir genişletme olabilir. Bilinmeyene harf ver, oranı eşitle. Torbaya bilye eklenince **paydaki toplam da** değişir.

Soru "en az kaç" diye soruyor ve ek koşul veriyorsa genişletmeleri sırayla dene: $\dfrac{2}{5}, \dfrac{4}{10}, \dfrac{6}{15}, \dots$ Koşulu sağlayan ilk değer cevaptır.

## Bir olasılık sorusunu çözme sırası

![Akış şeması: Çıktılar eş olası mı? sonra s(E): bütün çıktılar, sonra Soruda ne var? Üç dal: En az bir: 1 eksi P(hiç); Veya: ortak kısmı çıkar; Diğer: s(A) say. Üç dal da P = s(A) / s(E) kutusunda birleşir.](gorsel/tyt-matematik/10-02-yontem.svg "Önce örnek uzayı eş olası çıktılarla kur; sonra sorudaki anahtar kelimeye göre olayı say.")

## ÖSYM tuzakları

> **Eş olası olmayanı eş olası saymak:** İki zarın toplamları, üç paradaki tura sayıları (0, 1, 2, 3) eş olası değildir. Üç parada "iki tura" olasılığı $\dfrac{1}{4}$ değil, $\dfrac{3}{8}$'dir.

> **Kesişimi unutmak:** "A veya B" sorusunda olaylar ayrık değilse ortak çıktıları bir kez çıkar.

> **Tümleyende yanlış olay:** "En az bir"in tümleyeni "hiç"tir, "en çok bir" değildir.

> **Eklemeden sonra eski toplamla bölmek:** Torbaya bilye eklenince yeni olasılığın paydası yeni toplamdır.

## Kendini dene

### Soru 1
İki zar birlikte atılıyor. Üst yüzlerdeki sayıların toplamının 10 olma olasılığı kaçtır?

A) $\dfrac{1}{18}$
B) $\dfrac{1}{12}$
C) $\dfrac{1}{11}$
D) $\dfrac{1}{9}$
E) $\dfrac{1}{6}$

**Cevap:** B
**Çözüm:** $s(E) = 36$. Toplamı 10 olanlar: $(4,6), (5,5), (6,4)$, yani 3 çıktı. $P = \dfrac{3}{36} = \dfrac{1}{12}$. $(4,6)$ ile $(6,4)$'ü tek sayan $\dfrac{2}{36} = \dfrac{1}{18}$, $(5,5)$'i iki kez sayan $\dfrac{4}{36} = \dfrac{1}{9}$, 11 toplamı eş olası sayan $\dfrac{1}{11}$ bulur.

### Soru 2
1'den 20'ye kadar numaralanmış 20 karttan biri rastgele çekiliyor. Çekilen kartın numarasının 4'e veya 5'e bölünme olasılığı kaçtır?

A) $\dfrac{1}{4}$
B) $\dfrac{7}{20}$
C) $\dfrac{2}{5}$
D) $\dfrac{9}{20}$
E) $\dfrac{1}{2}$

**Cevap:** C
**Çözüm:** 4'e bölünen: 4, 8, 12, 16, 20 (5 kart). 5'e bölünen: 5, 10, 15, 20 (4 kart). İkisine birden bölünen: 20 (1 kart). $P = \dfrac{5 + 4 - 1}{20} = \dfrac{8}{20} = \dfrac{2}{5}$. Ortak kartı çıkarmayan $\dfrac{9}{20}$, iki kez çıkaran $\dfrac{7}{20}$ bulur.

### Soru 3
Bir torbada yalnızca mavi ve beyaz bilyeler vardır. Torbadan rastgele çekilen bir bilyenin mavi olma olasılığı $\dfrac{3}{8}$'dir. Torbaya 4 mavi bilye eklenirse mavi bilye çekme olasılığı $\dfrac{1}{2}$ oluyor.

Buna göre torbada kaç beyaz bilye vardır?

A) 4
B) 6
C) 8
D) 10
E) 16

**Cevap:** D
**Çözüm:** Toplam $8k$ olsun; mavi $3k$, beyaz $5k$. Ekleme sonrası $\dfrac{3k + 4}{8k + 4} = \dfrac{1}{2}$, $\;6k + 8 = 8k + 4$, $\;k = 2$. Mavi 6, beyaz 10, toplam 16. Kontrol: $\dfrac{10}{20} = \dfrac{1}{2}$. 6 mavi sayısı, 16 başlangıçtaki toplamdır.

## Özet kartı

- Eş olası çıktılarda $P(A) = \dfrac{s(A)}{s(E)}$. İki zarda 36 sıralı ikili eş olasıdır, 11 toplam değildir.
- $0 \le P(A) \le 1$; imkânsız olay 0, kesin olay 1.
- $P(A) + P(A') = 1$. "En az bir" → $1 - P(\text{hiç})$.
- Ayrık olaylar: $P(A \cup B) = P(A) + P(B)$.
- Ayrık değilse: $P(A \cup B) = P(A) + P(B) - P(A \cap B)$.
- Olasılık bir orandır; torba sorularında bilinmeyene harf ver, eklemeden sonra paydayı da güncelle.

## Sonraki adım

Alıştırmaya geç (aşağıdaki düğme). Gerçek sınav sorularını görmek için MEBİ'deki "Çıkmış Sorular" testini ve ÖSYM'nin yayımladığı TYT kitapçıklarını kullan.
