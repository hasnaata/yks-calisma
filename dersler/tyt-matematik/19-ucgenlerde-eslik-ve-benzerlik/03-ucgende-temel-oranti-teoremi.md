---
baslik: Üçgende Temel Orantı Teoremi
ders: tyt-matematik
sure: 20 dk
kaynak: MEBİ Konu Özeti bba21e0006
guncelleme: 2026-11-18
---
# Üçgende Temel Orantı Teoremi

<div class="giris" dir="rtl" lang="ar">

**الدرس ده عن إيه؟** عن نظرية التناسب في المثلث (temel orantı teoremi): لما تشد خط موازي لضلع في المثلث، إزاي يقسم الضلعين التانيين بنفس النسبة.

- هتعرف تكتب التناسب صح وتطلع الطول المجهول على طول، وإمتى تقسم على الضلع كله مش على الجزء بس.
- هتتعلم القطعة المتوسطة (orta taban): القطعة اللي بتوصّل منتصفي ضلعين بتبقى موازية للضلع التالت وطولها نصه بالظبط.
- هتفهم نظرية طاليس (Thales teoremi): المستقيمات المتوازية بتقسم أي قاطعين بنفس النسبة.

**ليه مهم؟** في TYT الصعوبة مش في الحسبة، الصعوبة إنك تختار الأجزاء الصح للتناسب، والاختيارات دايمًا فيها نتيجة التناسب الغلط عشان توقعك.

الدرس ٢٠ دقيقة بس وكله رسومات واضحة، خليك مركز وهتلاقيه أسهل مما تتخيل.

</div>

**Bu dersin sonunda:** bir kenara paralel çizilen doğrunun ya da paralel doğruların oluşturduğu parçalardan doğru orantıyı kurup bilinmeyen uzunluğu tek adımda bulabileceksin.

> **TYT'de yeri:** Bir üçgenin içinde tabana paralel bir doğru parçası, kenar orta noktalarını birleştiren yollar ya da paralel caddeleri kesen iki yol: hepsi bu dersin kalıbıdır. Soruların çoğunda zorluk hesapta değil, orantının **hangi parçalarla** kurulacağındadır. Seçeneklerde yanlış parçalarla kurulmuş orantının sonucu mutlaka bulunur.

## Önce hatırla

<details><summary>Geçen dersten: ABC ve ADE üçgenlerinde A açısı ortak ve m(ADE) = m(ABC). Bu üçgenler benzer midir? Hangi kuralla?</summary>
Evet, <b>A.A.</b> ile benzerdir: iki açı karşılıklı eşit. Bugünkü bütün kurallar bu benzerlikten çıkar; paralel bir doğru, eşit açıları kendiliğinden verir.
</details>

<details><summary>Geçen dersten: △ABC ~ △DEF, |AB| = 6, |DE| = 9 ve ABC üçgeninin çevresi 20'dir. DEF üçgeninin çevresi kaçtır?</summary>
Benzerlik oranı k = 9/6 = 3/2. Çevreler de bu oranda değişir: 20 · 3/2 = <b>30</b>. Bugün de aynı kuralı kullanacaksın: küçük ve büyük üçgende karşılıklı uzunlukların oranı hep aynıdır.
</details>

## 1. Temel orantı teoremi

**Örnek.** $ABC$ üçgeninde $D \in [AB]$, $E \in [AC]$ ve $[DE] \parallel [BC]$'dir. $|AD| = 4$, $|DB| = 6$, $|AE| = 6$ ve $|BC| = 15$ ise $|EC| = x$ ve $|DE|$ kaçtır?

![ABC üçgeni; D noktası AB üzerinde, E noktası AC üzerinde, DE mavi çizgiyle tabana paralel çizilmiş. AD 4, DB 6, AE 6, EC x, BC 15, DE soru işareti. D ile B'deki açılar kırmızı, E ile C'deki açılar yeşil yayla işaretli.](gorsel/tyt-matematik/19-03-temel.svg "Paralellik yüzünden aynı renkli açılar eşittir (yöndeş açılar). Bu yüzden küçük ADE üçgeni, büyük ABC üçgeninin küçültülmüşüdür.")

**Çözüm.**

1. $[DE] \parallel [BC]$ olduğu için $m(\widehat{ADE}) = m(\widehat{ABC})$ ve $m(\widehat{AED}) = m(\widehat{ACB})$ (yöndeş açılar). $\widehat{A}$ da ortak. **A.A.** ile $\triangle ADE \sim \triangle ABC$.
2. Benzerlik oranı: $k = \dfrac{|AD|}{|AB|} = \dfrac{4}{4 + 6} = \dfrac{4}{10} = \dfrac{2}{5}$.
3. Kenar parçaları için kısa yol: $\dfrac{|AD|}{|DB|} = \dfrac{|AE|}{|EC|} \Rightarrow \dfrac{4}{6} = \dfrac{6}{x} \Rightarrow x = 9$.
4. Paralel parça için **bütün kenarı** kullan: $\dfrac{|DE|}{|BC|} = \dfrac{|AD|}{|AB|} \Rightarrow \dfrac{|DE|}{15} = \dfrac{4}{10} \Rightarrow |DE| = 6$.

**Kural:** $[DE] \parallel [BC]$ ise

$$\frac{|AD|}{|DB|} = \frac{|AE|}{|EC|}$$

$$\frac{|AD|}{|AB|} = \frac{|AE|}{|AC|} = \frac{|DE|}{|BC|} = k$$

- Teoremin tersi de doğrudur: $\dfrac{|AD|}{|DB|} = \dfrac{|AE|}{|EC|}$ ise $[DE] \parallel [BC]$'dir.
- $ADE$ ile $ABC$ benzer olduğu için $A$'dan inen yükseklikler ve çevreler de $k$ oranındadır.

> **Tuzak:** $|DE|$'yi bulurken $\dfrac{|DE|}{|BC|} = \dfrac{|AD|}{|DB|}$ yazmak. Bu, $|DE| = 15 \cdot \dfrac{4}{6} = 10$ verir; yanlıştır. $[DE]$ küçük üçgenin kenarıdır, $[DB]$ ise hiçbir üçgenin kenarı değildir. Paralel parçayı her zaman **tepeden başlayan bütün kenarla** ($|AB|$, $|AC|$) oranla.

## 2. Orta taban

**Örnek.** $ABC$ üçgeninde $|AB| = 10$, $|AC| = 12$, $|BC| = 14$'tür. $D$, $[AB]$'nin; $E$, $[AC]$'nin orta noktasıdır. $|DE|$ ve $ADE$ üçgeninin çevresi kaçtır?

![ABC üçgeni; D, AB'nin orta noktası, E, AC'nin orta noktası, DE mavi çizgiyle birleştirilmiş. AD ve DB 5'er, tek çentikli; AE ve EC 6'şar, çift çentikli; DE 7, BC 14.](gorsel/tyt-matematik/19-03-orta-taban.svg "Aynı sayıda çentikli parçalar eşittir. Orta noktaları birleştiren DE, tabana paraleldir ve tabanın tam yarısıdır: 7 ile 14.")

**Çözüm.**

1. $\dfrac{|AD|}{|DB|} = \dfrac{5}{5} = 1$ ve $\dfrac{|AE|}{|EC|} = \dfrac{6}{6} = 1$. Oranlar eşit, temel orantının tersinden $[DE] \parallel [BC]$.
2. $k = \dfrac{|AD|}{|AB|} = \dfrac{1}{2}$, yani $|DE| = \dfrac{14}{2} = 7$.
3. $ADE$'nin çevresi: $5 + 6 + 7 = 18$. Bu, $ABC$'nin çevresinin ($36$) yarısıdır.

**Kural:** İki kenarın orta noktalarını birleştiren doğru parçasına **orta taban** denir. Üçüncü kenara paraleldir ve onun yarısıdır.

$$D, E \text{ orta nokta} \Rightarrow [DE] \parallel [BC], \qquad |DE| = \frac{|BC|}{2}$$

- Tersi: Bir kenarın orta noktasından öbür kenara paralel çizilen doğru, üçüncü kenarı da **orta noktasından** keser.
- Üç kenarın orta noktaları birleştirilirse üçgen, birbirine eş **dört** küçük üçgene ayrılır; her birinin çevresi büyük üçgenin çevresinin yarısıdır.

> **Tuzak:** "Yarısıdır" kuralı yalnızca **iki nokta da orta nokta** ise geçerlidir. $|AD| = \dfrac{|AB|}{3}$ ise $|DE| = \dfrac{|BC|}{3}$ olur. Orta taban, temel orantının $k = \dfrac{1}{2}$ olan özel hâlidir.

## 3. Thales teoremi

**Örnek.** $d_1 \parallel d_2 \parallel d_3$ doğruları iki keseni $A, B, C$ ve $D, E, F$ noktalarında kesiyor. $|AB| = 4$, $|BC| = 6$ ve $|DE| = 5$ ise $|EF| = x$ kaçtır?

![Üç yatay paralel doğru d1, d2, d3. Soldaki kesen bunları A, B, C noktalarında, sağdaki kesen D, E, F noktalarında kesiyor. AB 4, BC 6, DE 5, EF x.](gorsel/tyt-matematik/19-03-thales.svg "Kesenler paralel değildir, eğimleri farklıdır; yine de parçaların oranı iki kesende aynıdır: 4'e 6 ile 5'e x.")

**Çözüm.**

1. Aynı iki paralelin arasında kalan parçalar karşılıklıdır: $[AB] \leftrightarrow [DE]$ ($d_1$ ile $d_2$ arası), $[BC] \leftrightarrow [EF]$ ($d_2$ ile $d_3$ arası).
2. Orantı: $\dfrac{|AB|}{|BC|} = \dfrac{|DE|}{|EF|} \Rightarrow \dfrac{4}{6} = \dfrac{5}{x} \Rightarrow x = \dfrac{30}{4} = 7{,}5$.

**Neden?** Sağdaki keseni $A$'dan geçecek biçimde kendine paralel kaydır. Ortaya $d_3$'ü taban kabul eden bir üçgen ve $d_2$'nin içinden geçtiği bir paralel çıkar; bu, 1. bölümdeki temel orantı teoremidir.

**Kural:** En az üç paralel doğru, iki kesen üzerinde orantılı parçalar ayırır.

$$d_1 \parallel d_2 \parallel d_3 \Rightarrow \frac{|AB|}{|BC|} = \frac{|DE|}{|EF|} \qquad \text{ve} \qquad \frac{|AB|}{|AC|} = \frac{|DE|}{|DF|}$$

> **Tuzak:** Parçaları iki kesende **aynı sırayla** yaz. $\dfrac{|AB|}{|BC|} = \dfrac{|EF|}{|DE|}$ yazarsan $x = \dfrac{10}{3}$ bulursun; yanlıştır. Kontrol: soldaki kesende alt parça üstten uzunsa ($6 > 4$), sağdakinde de uzun olmalı ($7{,}5 > 5$).

## ÖSYM tuzakları

> **Paralel parçayı kenar parçasıyla oranlamak.** $\dfrac{|DE|}{|BC|} = \dfrac{|AD|}{|DB|}$ yanlıştır; doğrusu $\dfrac{|DE|}{|BC|} = \dfrac{|AD|}{|AB|}$. Bu yanlışın sonucu seçeneklerde hep vardır.

> **Fark ile oranı karıştırmak.** "$|AE|$, $|AD|$'den $2$ fazla, öyleyse $|EC|$ de $|DB|$'den $2$ fazla" yanlış. Orantıda parçalar **aynı sayıyla çarpılır**.

> **Orta taban kuralını her yerde kullanmak.** $|DE| = \dfrac{|BC|}{2}$ yalnızca $D$ ve $E$ orta nokta ise doğrudur. Bir kenarın orta noktası verilmiş, diğeri verilmemişse paralellikten öbürünün de orta nokta olduğunu göster.

> **Thales'te çapraz eşleme.** $d_1$–$d_2$ arasındaki parça yine $d_1$–$d_2$ arasındaki parçayla eşlenir. Yolların uzunluğu değil, iki kesendeki **oran** aynıdır.

> **Yükseklikte yanlış parça.** Tabana paralel bir parça yerden $h$ yükseklikteyse oran $\dfrac{h}{H}$ değil, tepeden ölçülen $\dfrac{H - h}{H}$'dir; küçük üçgen tepededir.

## Kendini dene

### Soru 1
$ABC$ üçgeninde $D \in [AB]$, $E \in [AC]$ ve $[DE] \parallel [BC]$'dir. $|AD| = 5$, $|DB| = 10$ ve $|AE| = 4$ ise $|EC|$ kaçtır?

A) 2
B) 8
C) 9
D) 10
E) 12

**Cevap:** B
**Çözüm:** $\dfrac{|AD|}{|DB|} = \dfrac{|AE|}{|EC|} \Rightarrow \dfrac{5}{10} = \dfrac{4}{|EC|} \Rightarrow |EC| = 8$. $2$ oranı ters kurmaktır ($4 \cdot \frac{5}{10}$); $9$ farkı eklemektir ($4 + 5$); $12$ ise $|AC|$'dir.

### Soru 2
$ABC$ üçgeninde $|AB| = 10$ ve $|AC| = 14$'tür. $D$, $[AB]$'nin; $E$, $[AC]$'nin orta noktasıdır ve $|DE| = 9$'dur. $DBCE$ dörtgeninin çevresi kaçtır?

A) 21
B) 30
C) 39
D) 42
E) 48

**Cevap:** C
**Çözüm:** $[DE]$ orta tabandır: $|BC| = 2 \cdot 9 = 18$. $|DB| = 5$, $|EC| = 7$. Dörtgenin çevresi $|DB| + |BC| + |CE| + |ED| = 5 + 18 + 7 + 9 = 39$. $42$, $ABC$ üçgeninin çevresidir ($10 + 14 + 18$); $21$, $ADE$ üçgeninin çevresidir; $30$ ise $|BC|$'yi $9$ almaktır.

### Soru 3
$d_1 \parallel d_2 \parallel d_3$ doğruları bir keseni sırasıyla $A$, $B$, $C$; başka bir keseni sırasıyla $D$, $E$, $F$ noktalarında kesiyor. $|AB| = 5$, $|AC| = 12$ ve $|DE| = 10$ ise $|DF|$ kaçtır?

A) 12
B) 14
C) 17
D) 22
E) 24

**Cevap:** E
**Çözüm:** $\dfrac{|AB|}{|AC|} = \dfrac{|DE|}{|DF|} \Rightarrow \dfrac{5}{12} = \dfrac{10}{|DF|} \Rightarrow |DF| = 24$. Ya da $|BC| = 7$, $|EF| = 10 \cdot \dfrac{7}{5} = 14$, $|DF| = 10 + 14 = 24$. $14$, $|EF|$'de durmaktır; $17$ ise $|EF|$'yi $|BC|$ ile aynı sanmaktır ($10 + 7$).

## Özet kartı

- $[DE] \parallel [BC]$ ise $\triangle ADE \sim \triangle ABC$ (yöndeş açılar, A.A.).
- Kenar parçaları: $\dfrac{|AD|}{|DB|} = \dfrac{|AE|}{|EC|}$. Tersi de doğru: bu oran tutuyorsa $[DE] \parallel [BC]$.
- Paralel parça: $\dfrac{|DE|}{|BC|} = \dfrac{|AD|}{|AB|}$; payda **bütün kenar**.
- Orta taban: iki orta noktayı birleştiren parça tabana paraleldir ve tabanın yarısıdır.
- Thales: paraleller iki keseni aynı oranda böler; parçaları aynı sırayla eşle.
- Orantıda parçalar aynı sayıyla çarpılır, aynı sayı eklenmez.

## Sonraki adım

Alıştırmaya geç (aşağıdaki düğme). Sonraki ders: **Üçgenlerin Benzerliği ile İlgili Uygulamalar**. Orada bugünkü orantıları gölge, ayna ve harita gibi gerçek ölçüm sorularına uygulayacaksın.
