---
baslik: Olasılıkta Temel Kavramlar
ders: tyt-matematik
sure: 20 dk
kaynak: MEBİ Konu Özeti 2b4cdac8ac
guncelleme: 2026-11-18
---
# Olasılıkta Temel Kavramlar

<div class="giris" dir="rtl" lang="ar">

**الدرس ده عن إيه؟** ده أول درس في الاحتمالات: هنتعلم نعدّ كل النتايج الممكنة لتجربة زي رمي عملة أو زهر، ونعدّ النتايج اللي إحنا عايزينها.

- هتكتب فضاء العينة (örnek uzay) وتعرف عدد عناصره، زي إن عملتين ليهم 4 نتايج وزهرين ليهم 36.
- هتفرّق بين الحدث المستحيل (imkânsız olay) والحدث الأكيد (kesin olay)، وتعرف إمتى حدثين يبقوا متنافيين (ayrık olaylar).
- هتستخدم الحدث المكمّل (tümleyen) عشان تحل أسئلة "على الأقل واحد" بسرعة.

**ليه مهم؟** أي سؤال احتمالات في TYT بيقوم على رقمين: عدد عناصر فضاء العينة وعدد عناصر الحدث المطلوب، والدرس ده بيعلّمك تطلعهم صح من غير ما تقع في فخ العدّ.

عشرين دقيقة بس، وبعدها هتبدأ أسئلة الاحتمالات وإنت فاهم أساسها.

</div>

**Bu dersin sonunda:** bir deneyin örnek uzayını yazıp eleman sayısını bulabilecek, istenen olayın kaç elemanlı olduğunu sayabilecek ve ayrık olay, tümleyen, imkânsız olay ve kesin olay kavramlarını ayırt edebileceksin.

> **TYT'de yeri:** Her olasılık sorusu iki sayıya dayanır: örnek uzayın eleman sayısı ve istenen olayın eleman sayısı. Bu ders o iki sayıyı doğru bulmayı öğretir. Doğrudan gelen kalıplar: "örnek uzay kaç elemanlıdır?", "bu olay kaç elemanlıdır?", "hangileri ayrık olaylardır?", "hangisi kesin olaydır?". "En az bir" geçen sorularda tümleyenle saymak işi kısaltır.

## Önce hatırla

<details><summary>Geçen dersten: Pascal üçgeninde 1 3 3 1 satırından sonra gelen satır nedir ve bu satırdaki sayıların toplamı kaçtır?</summary>
Her sayı üstündeki iki komşunun toplamıdır: 1, $1+3=4$, $3+3=6$, $3+1=4$, 1. Satır <b>1 4 6 4 1</b>, toplamı $16 = 2^4$. Bugün 4 madenî para atıldığında örnek uzayın da 16 elemanlı olduğunu göreceksin.
</details>

<details><summary>Geçen dersten: $(x + y)^5$ açılımında kaç terim vardır ve katsayılar toplamı kaçtır?</summary>
$(x + y)^n$ açılımında $n + 1$ terim vardır: <b>6 terim</b>. Katsayılar toplamı için $x = y = 1$ yazılır: $(1 + 1)^5 = 2^5 = 32$.
</details>

## Deney, çıktı, örnek uzay

**Örnek.** Bir madenî parayı havaya at. Sonuç ya yazı (Y) ya tura (T) olur; aynı atışı tekrarlarsan farklı sonuç da gelebilir.

- Bu atış bir **deneydir**: tekrarlanabilen ve her tekrarda farklı sonuç verebilen bir süreç.
- Y ve T bu deneyin **çıktılarıdır**.
- Bütün çıktıların kümesi **örnek uzaydır**: $E = \{Y, T\}$, $s(E) = 2$.

İki para atınca $E = \{YY, YT, TY, TT\}$ ve $s(E) = 4$ olur. $YT$ ile $TY$ farklı çıktılardır: birincide 1. para yazı, ikincide 1. para tura gelmiştir. Üç parada her yeni para her dalı ikiye ayırır:

![Üç madenî para için ağaç şeması: her basamakta Y ve T olmak üzere iki dal açılıyor, sonunda YYY'den TTT'ye kadar 8 çıktı yazılı.](gorsel/tyt-matematik/10-01-agac.svg "Her para dal sayısını ikiye katlar: 2 · 2 · 2 = 8. Sağdaki her satır ayrı bir çıktıdır.")

Çarpma kuralı burada da geçerlidir: $s(E) = 2 \cdot 2 \cdot 2 = 2^3 = 8$. Bir zarın 6 yüzü olduğundan iki zarda $6 \cdot 6 = 36$ çıktı vardır.

| Deney | $s(E)$ |
|---|---|
| $n$ madenî para birlikte atılıyor (ya da 1 para $n$ kez) | $2^n$ |
| $n$ zar birlikte atılıyor (ya da 1 zar $n$ kez) | $6^n$ |
| 1 para ve 1 zar birlikte atılıyor | $2 \cdot 6 = 12$ |

**Kural.** Bir deney art arda yapılan adımlardan oluşuyorsa $s(E)$, her adımdaki çıktı sayılarının çarpımıdır. $n$ parayı birlikte atmak ile bir parayı $n$ kez atmak **aynı** örnek uzayı verir.

Pascal bağlantısı: üç parada tura sayısı 0, 1, 2, 3 olan çıktıların sayıları $1, 3, 3, 1$'dir; toplamları $2^3 = 8$. Geçen dersteki satır toplamının $2^n$ çıkmasının sebebi budur.

### Seçme ile örnek uzay

**Örnek.** Bir torbada 3 kırmızı ve 2 mavi bilye var. Torbadan **aynı anda** 2 bilye çekiliyor. Bilyeleri ayırt edilebilir say (K1, K2, K3, M1, M2).

Aynı anda çekildiği için sıra önemsizdir: $s(E) = C(5, 2) = 10$. "İkisi de kırmızı" çıktıları $C(3, 2) = 3$ tanedir.

**Kural.** Seçim sırasız ise örnek uzay kombinasyonla, sıralı ise (art arda çekip sırayla not almak gibi) permütasyonla sayılır.

## Olay

**Örnek.** Bir zar atılıyor: $E = \{1, 2, 3, 4, 5, 6\}$. "Asal sayı gelmesi" olayı $A = \{2, 3, 5\}$, yani $s(A) = 3$.

**Kural.** Örnek uzayın her alt kümesi bir **olaydır**. $s(E) = n$ ise $2^n$ farklı olay tanımlanabilir; bir zar için $2^6 = 64$. Boş küme ve $E$'nin kendisi de bu sayının içindedir.

İki zarda olay saymak için 36 çıktıyı tablo olarak düşün:

![6'ya 6 tablo: satırlar 1. zar, sütunlar 2. zar; her kutuda bir sıralı ikili var. Toplamı 7 olan 6 kutu yeşil boyalı ve sağ üstten sol alta bir köşegen oluşturuyor.](gorsel/tyt-matematik/10-01-iki-zar.svg "Toplamı 7 olan 6 çıktı bir köşegen üzerindedir. 1,6 ile 6,1 ayrı kutulardır.")

"Toplamın 7 olması" olayı $\{(1,6), (2,5), (3,4), (4,3), (5,2), (6,1)\}$, yani 6 elemanlıdır. $(1,6)$ ile $(6,1)$'i tek çıktı sayan 3 bulur ve yanılır.

## İmkânsız olay ve kesin olay

**Örnek.** Bir zar atılıyor.

- "7 gelmesi" hiçbir çıktıda gerçekleşmez. Bu olay $\varnothing$ (boş küme): **imkânsız olay**.
- "7'den küçük sayı gelmesi" her çıktıda gerçekleşir. Bu olay $E$'nin kendisi: **kesin olay**.

**Kural.** İmkânsız olay $\varnothing$, kesin olay $E$'dir. "Gerçekleşmesi zor" bir olay imkânsız değildir; tek bir çıktıda bile gerçekleşebiliyorsa imkânsız sayılmaz.

## Ayrık ve ayrık olmayan olaylar

**Örnek.** Bir zar atılıyor.

- $A$: 3'ten küçük gelmesi $= \{1, 2\}$, $B$: 4'ten büyük gelmesi $= \{5, 6\}$. Ortak çıktı yok: $A \cap B = \varnothing$. A ile B **ayrık** olaylardır.
- $A$: çift gelmesi $= \{2, 4, 6\}$, $C$: asal gelmesi $= \{2, 3, 5\}$. 2 hem çift hem asal: $A \cap C = \{2\}$. A ile C **ayrık değildir**.

![İki Venn şeması yan yana. Solda A içinde 1 ve 2, B içinde 5 ve 6 var, daireler kesişmiyor; 3 ve 4 dışarıda. Sağda A ile C kesişiyor, kesişimde 2 var; A'da 4 ve 6, C'de 3 ve 5, dışarıda 1.](gorsel/tyt-matematik/10-01-ayrik.svg "Ayrık olaylarda daireler kesişmez. Soldaki 3 ve 4'e bak: ayrık olaylar örnek uzayın tamamını kaplamak zorunda değildir.")

**Kural.** $A \cap B = \varnothing$ ise A ve B ayrıktır: ikisi aynı anda gerçekleşemez. Tek bir ortak çıktı bile varsa ayrık değildir. İki olayın ayrık olup olmadığını anlamak için ortak bir çıktı ara.

## Bir olayın tümleyeni

**Örnek.** Üç madenî para atılıyor. $A$: en az bir tura gelmesi. A'yı tek tek yazmak yerine A'da **olmayanlara** bak: hiç tura gelmemesi, yani yalnızca $YYY$.

![Venn şeması: dikdörtgen E'nin içinde A dairesi; dairede en az bir tura içeren 7 çıktı yazılı. Dairenin dışında yalnızca YYY var, A′ olarak işaretli.](gorsel/tyt-matematik/10-01-tumleyen.svg "A ile A′ birlikte örnek uzayın tamamını kaplar ve ortak elemanları yoktur. En az bir turanın tümleyeni hiç tura gelmemesidir.")

$s(A) = 8 - 1 = 7$.

**Kural.** A olayının tümleyeni $A'$, örnek uzayda A'ya ait olmayan bütün çıktılardır:

$$s(A') = s(E) - s(A), \qquad A \cap A' = \varnothing, \qquad A \cup A' = E$$

Kesin olayın tümleyeni imkânsız olaydır: $E' = \varnothing$.

**Örnek.** İki zar atılıyor. "En az bir zarın 6 gelmesi" kaç elemanlıdır? Tümleyeni: hiçbir zarın 6 gelmemesi, $5 \cdot 5 = 25$ çıktı. İstenen: $36 - 25 = 11$. Tabloda 6. satır ile 6. sütunu say: $6 + 6 - 1 = 11$; $(6,6)$ iki kez sayılmamalı.

## ÖSYM tuzakları

> **Sıralı çıktıyı tek saymak:** İki zar ya da iki para atıldığında $(2,5)$ ile $(5,2)$, $YT$ ile $TY$ farklı çıktılardır. "Toplam 7" olayı 3 değil 6 elemanlıdır.

> **"En az bir"in tümleyenini yanlış kurmak:** "En az bir tura"nın tümleyeni "en çok bir tura" değil, **hiç tura gelmemesidir**.

> **Ayrık ile tümleyeni karıştırmak:** Tümleyen olaylar her zaman ayrıktır, ama ayrık olaylar tümleyen olmak zorunda değildir. $\{1, 2\}$ ile $\{5, 6\}$ ayrıktır; birbirinin tümleyeni değildir.

> **Kesin olay ile imkânsız olayı karıştırmak:** "Zarın 7'den küçük gelmesi" imkânsız değil, kesin olaydır. Seçenekte ikisi birlikte varsa olayın kümesini yaz: boş küme mi, E mi?

## Kendini dene

### Soru 1
İki madenî para ve bir zar birlikte atılıyor.

Bu deneyin örnek uzayı kaç elemanlıdır?

A) 8
B) 12
C) 24
D) 36
E) 48

**Cevap:** C
**Çözüm:** Her paranın 2, zarın 6 çıktısı var. Çarpma kuralı: $2 \cdot 2 \cdot 6 = 24$. Tek para sayan $2 \cdot 6 = 12$, zarı da para gibi 2 çıktılı sayan $2^3 = 8$, üç para sayan $2^3 \cdot 6 = 48$ bulur.

### Soru 2
Üç madenî para atılıyor. A, en az bir yazı gelmesi olayıdır.

Buna göre $A'$ olayı aşağıdakilerden hangisidir?

A) $\{YYY\}$
B) $\{YTT, TYT, TTY\}$
C) $\{YTT, TYT, TTY, TTT\}$
D) $\{TTT\}$
E) $\varnothing$

**Cevap:** D
**Çözüm:** "En az bir yazı"nın tümleyeni "hiç yazı gelmemesi"dir. Yazı hiç yoksa üç para da tura: $A' = \{TTT\}$. C seçeneği "en çok bir yazı" olayıdır; tümleyen değildir.

### Soru 3
5 kişilik bir gruptan 2 kişilik bir temsilci ekibi seçilecektir. Gruptaki Ayşe'nin ekipte **olmadığı** çıktılardan oluşan olay kaç elemanlıdır?

A) 4
B) 6
C) 8
D) 10
E) 20

**Cevap:** B
**Çözüm:** Ekip sırasız seçilir: $s(E) = C(5, 2) = 10$. Ayşe'nin olduğu ekipler: Ayşe ve kalan 4 kişiden biri, $C(4, 1) = 4$. Tümleyen: $10 - 4 = 6$. Doğrudan da sayılır: Ayşe'yi dışarıda bırak, 4 kişiden 2 seç: $C(4, 2) = 6$. Sıralı sayan 20 bulur.

## Özet kartı

- Deney → çıktılar → örnek uzay $E$. Örnek uzayın her alt kümesi bir olaydır.
- $n$ para: $2^n$ çıktı; $n$ zar: $6^n$ çıktı. Birlikte atmak ile art arda atmak aynı örnek uzayı verir.
- İki zar ya da para atılınca çıktılar sıralıdır: $(1,6) \neq (6,1)$.
- İmkânsız olay $\varnothing$, kesin olay $E$.
- Ayrık olay: $A \cap B = \varnothing$. Tek ortak çıktı varsa ayrık değildir.
- Tümleyen: $s(A') = s(E) - s(A)$. "En az bir"in tümleyeni "hiç"tir.

## Sonraki adım

Alıştırmaya geç (aşağıdaki düğme). Sonraki ders **Olasılık Kavramı İle İlgili Uygulamalar**; orada bu derste saydığın iki sayıyı oranlayacaksın: olasılık $= \dfrac{s(A)}{s(E)}$.
