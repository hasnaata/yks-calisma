---
baslik: Üçgenlerde Benzerlik
ders: tyt-matematik
sure: 20 dk
kaynak: MEBİ Konu Özeti 1928b82e41
guncelleme: 2026-11-17
---
# Üçgenlerde Benzerlik

**Bu dersin sonunda:** iki üçgenin benzer olduğunu A.A., K.A.K. ya da K.K.K. ile gösterip benzerlik oranından bilinmeyen kenarı, yüksekliği ya da çevreyi bulabileceksin.

> **TYT'de yeri:** Geometri bölümünde hemen her yıl en az bir soru benzerliğe dayanır: iç içe geçmiş iki üçgende bir kenar, gölge ya da ayna ile yükseklik ölçme, bir haritada ya da büyütülmüş çizimde uzunluk. Çoğunda iş, doğru köşeleri eşleyip tek bir orantı kurmaktır.

## Önce hatırla

<details><summary>Geçen dersten: ABC ve DEF üçgenlerinde |AB| = |DE|, |AC| = |DF| ve m(A) = m(D). Bu üçgenler eş midir? Hangi kuralla?</summary>
Evet, <b>K.A.K.</b> ile eştir: iki kenar ve bu kenarların <b>arasındaki</b> açı eşit. Bugün aynı kuralın benzerlik hâlini göreceksin: kenarlar eşit değil, <b>orantılı</b> olacak.
</details>

<details><summary>Geçen dersten: Üç açısı da karşılıklı eşit olan iki üçgen eş olmak zorunda mıdır?</summary>
<b>Hayır.</b> Eşlik için en az bir kenarın da eşit olması gerekir; açılar eşit olup biri ötekinin büyütülmüşü olabilir. İşte bu durum bugünün konusu: açıları eşit üçgenler <b>benzerdir</b>.
</details>

## 1. Benzerlik ve benzerlik oranı

İki üçgenin köşeleri bire bir eşlendiğinde **karşılıklı açılar eşit** ve **karşılıklı kenarlar orantılı** ise bu üçgenler **benzerdir**. $\triangle ABC \sim \triangle DEF$ diye yazılır. Kenarların oranına **benzerlik oranı** denir ve $k$ ile gösterilir. Biri ötekinin büyütülmüş ya da küçültülmüş hâlidir; aynı ayakkabı modelinin farklı numaraları gibi.

**Örnek.** $\triangle ABC \sim \triangle DEF$, $|AB| = 4$, $|BC| = 6$, $|AC| = 5$ ve $|DE| = 6$ ise $|EF|$ ve $|DF|$ kaçtır?

**Çözüm.**

1. Yazılıştaki sıra eşlemeyi verir: $A \leftrightarrow D$, $B \leftrightarrow E$, $C \leftrightarrow F$. Yani $[AB] \leftrightarrow [DE]$, $[BC] \leftrightarrow [EF]$, $[AC] \leftrightarrow [DF]$.
2. Uzunlukları bilinen eş kenarlardan oranı bul: $k = \dfrac{|DE|}{|AB|} = \dfrac{6}{4} = \dfrac{3}{2}$.
3. Öbür kenarları $k$ ile çarp: $|EF| = 6 \cdot \dfrac{3}{2} = 9$, $|DF| = 5 \cdot \dfrac{3}{2} = 7{,}5$.

![Solda kenarları 4, 6, 5 olan ABC üçgeni, sağda kenarları 6, 9, 7,5 olan daha büyük DEF üçgeni. A ile D, B ile E, C ile F köşelerindeki açılar aynı renkte işaretli.](gorsel/tyt-matematik/19-02-tanim.svg "Aynı renkli açılar eşittir. Her kenar 1,5 katına çıkmış: 4 → 6, 6 → 9, 5 → 7,5.")

**Kural:** $\triangle ABC \sim \triangle DEF$ ise

$$m(\widehat{A}) = m(\widehat{D}),\quad m(\widehat{B}) = m(\widehat{E}),\quad m(\widehat{C}) = m(\widehat{F})$$

$$\frac{|DE|}{|AB|} = \frac{|EF|}{|BC|} = \frac{|DF|}{|AC|} = k$$

> **Tuzak:** Eşlemeyi şekildeki konumdan değil, **yazılıştaki harf sırasından** oku. $\triangle ABC \sim \triangle DFE$ yazıyorsa $B \leftrightarrow F$ ve $[AB] \leftrightarrow [DF]$'dir. Eşleme verilmemişse eşit açıları bul; **eşit açıların karşısındaki kenarlar** karşılıklıdır.

İki üçgenin benzer olduğunu göstermek için bütün açılara ve kenarlara bakmana gerek yok. Aşağıdaki üç kuraldan biri yeter.

## 2. Açı–Açı (A.A.) benzerliği

**Örnek.** Şekilde $D \in [AB]$, $E \in [AC]$ ve $m(\widehat{ADE}) = m(\widehat{ACB})$'dir. $|AD| = 4$, $|AE| = 3$, $|EC| = 5$ ise $|DB| = x$ kaçtır?

![ABC üçgeni; D noktası AB üzerinde, E noktası AC üzerinde, DE mavi çizgiyle birleştirilmiş. AD 4, DB x, AE 3, EC 5. D'deki ADE açısı ile C'deki ACB açısı kırmızı yayla işaretli.](gorsel/tyt-matematik/19-02-aa.svg "İki kırmızı açı eşittir, A açısı iki üçgende ortaktır. Küçük ADE üçgeni, büyük ACB üçgeninin ters çevrilmiş küçüğüdür.")

**Çözüm.**

1. $ADE$ ve $ACB$ üçgenlerinde $\widehat{A}$ ortak, $m(\widehat{ADE}) = m(\widehat{ACB})$. İki açı eşit: **A.A.** ile benzerler.
2. Eşlemeyi açılardan yaz: $A \leftrightarrow A$, $D \leftrightarrow C$, $E \leftrightarrow B$. Yani $\triangle ADE \sim \triangle ACB$.
3. Orantı: $\dfrac{|AD|}{|AC|} = \dfrac{|AE|}{|AB|} \Rightarrow \dfrac{4}{8} = \dfrac{3}{|AB|} \Rightarrow |AB| = 6$.
4. $x = |AB| - |AD| = 6 - 4 = 2$.

**Kural:** İki üçgenin ikişer açısı karşılıklı eşitse üçgenler benzerdir. (Üçüncü açılar da kendiliğinden eşit olur; toplam $180^\circ$.)

> **Tuzak:** Bu şekilde $[DE]$, $[BC]$'ye paralel **değildir**; küçük üçgen "ters dönmüştür". $\dfrac{|AD|}{|AB|} = \dfrac{|AE|}{|AC|}$ yazarsan $|AB| = \dfrac{32}{3}$ bulursun; yanlıştır. Orantıyı her zaman **eşit açıların karşısındaki** kenarlarla kur: $D$'deki açının karşısı $[AE]$, $C$'deki açının karşısı $[AB]$.

## 3. Kenar–Açı–Kenar (K.A.K.) benzerliği

**Örnek.** $|AB| = 6$, $|AC| = 9$, $|DE| = 4$, $|DF| = 6$ ve $m(\widehat{A}) = m(\widehat{D})$'dir. $|BC| = 7{,}5$ ise $|EF|$ kaçtır?

![Solda ABC üçgeni: AB 6, AC 9, BC 7,5; A'daki açı alfa. Sağda DEF üçgeni: DE 4, DF 6, EF soru işareti; D'deki açı alfa.](gorsel/tyt-matematik/19-02-kak.svg "Kırmızı kenarlar orantılı (4/6 = 6/9), aradaki α açıları eşit. Sorulan EF, α'nın karşısındaki kenardır.")

**Çözüm.**

1. Açıyı oluşturan kenarların oranları: $\dfrac{|DE|}{|AB|} = \dfrac{4}{6} = \dfrac{2}{3}$ ve $\dfrac{|DF|}{|AC|} = \dfrac{6}{9} = \dfrac{2}{3}$. Eşit.
2. Bu kenarların arasındaki açılar eşit. **K.A.K.** ile $\triangle ABC \sim \triangle DEF$, $k = \dfrac{2}{3}$.
3. $|EF| = 7{,}5 \cdot \dfrac{2}{3} = 5$.

**Kural:** İki kenar orantılı ve bu iki kenarın **arasındaki** açılar eşitse üçgenler benzerdir.

> **Tuzak:** Eşit açı, orantılı kenarların **arasında** olmalıdır. İki kenar orantılı ama eşit açı bu kenarlardan birinin karşısındaysa K.A.K. kullanılamaz.

## 4. Kenar–Kenar–Kenar (K.K.K.) benzerliği

**Örnek.** Kenarları $4$, $6$, $7$ olan $ABC$ üçgeni ile kenarları $12$, $8$, $14$ olan $KLM$ üçgeni benzer midir? Kenarları $8$, $12$, $15$ olan bir üçgen için ne dersin?

![Solda ABC üçgeni: AB 4, AC 6, BC 7. Sağda KLM üçgeni: KL 8, KM 12, LM 14. Aynı renkli kenarlar karşılıklıdır; en uzun kenarların karşısındaki A ve K açıları kırmızı yayla işaretli.](gorsel/tyt-matematik/19-02-kkk.svg "Kısa ile kısa, orta ile orta, uzun ile uzun eşlenir: 8/4 = 12/6 = 14/7 = 2. En büyük açılar (A ve K) en uzun kenarların karşısındadır.")

**Çözüm.**

1. İki üçgenin kenarlarını küçükten büyüğe sırala: $4, 6, 7$ ve $8, 12, 14$.
2. Sırayla oranla: $\dfrac{8}{4} = \dfrac{12}{6} = \dfrac{14}{7} = 2$. Üç oran eşit: **K.K.K.** ile benzerler, $k = 2$.
3. $8, 12, 15$ için: $\dfrac{8}{4} = 2$, $\dfrac{12}{6} = 2$ ama $\dfrac{15}{7} \neq 2$. Benzer **değildir**.

**Kural:** Üç kenar karşılıklı orantılıysa üçgenler benzerdir. Büyük kenarın karşısında büyük açı olduğu için en uzun kenarların karşısındaki açılar eşleşir.

> **Tuzak:** Kenarları sıralamadan, verildiği sırayla bölme. Ayrıca her kenara aynı sayıyı **eklemek** benzer üçgen vermez: $4, 6, 7$'nin her kenarına $2$ eklenirse $6, 8, 9$ olur ve oranlar eşit değildir. Benzerlikte işlem **çarpmadır**.

## 5. Yükseklik, kenarortay, açıortay ve çevre

**Örnek.** $\triangle ABC \sim \triangle DEF$, $|BC| = 8$, $|EF| = 12$. $A$'dan $[BC]$'ye inen yükseklik $3$, $ABC$'nin çevresi $18$'dir. $D$'den $[EF]$'ye inen yüksekliği ve $DEF$'nin çevresini bul.

![Solda ABC üçgeni, taban BC 8, A'dan tabana inen kesikli mavi yükseklik 3. Sağda daha büyük DEF üçgeni, taban EF 12, D'den inen yükseklik soru işareti.](gorsel/tyt-matematik/19-02-yukseklik.svg "Kenar 1,5 katına çıkınca yükseklik de 1,5 katına çıkar: 3 → 4,5. Çevre de öyle: 18 → 27.")

**Çözüm.**

1. $k = \dfrac{|EF|}{|BC|} = \dfrac{12}{8} = \dfrac{3}{2}$.
2. Yükseklik: $3 \cdot \dfrac{3}{2} = 4{,}5$.
3. Çevre: $18 \cdot \dfrac{3}{2} = 27$. (Kontrol: her kenar $\dfrac{3}{2}$ katına çıktıysa toplamları da $\dfrac{3}{2}$ katına çıkar.)

**Kural:** Benzer üçgenlerde karşılıklı **yüksekliklerin**, **kenarortayların**, **açıortayların** ve **çevrelerin** oranı da $k$'dır.

$$\frac{h_D}{h_A} = \frac{V_D}{V_A} = \frac{n_D}{n_A} = \frac{\text{Ç}(DEF)}{\text{Ç}(ABC)} = k$$

> **Tuzak:** Bu liste uzunluklar içindir. **Alan** bir uzunluk değildir: alan, taban ile yüksekliğin çarpımından geldiği için $k$ ile değil $k^2$ ile değişir. Örnekte alanlar $12$ ve $27$'dir; oran $\dfrac{27}{12} = \dfrac{9}{4} = \left(\dfrac{3}{2}\right)^2$.

## ÖSYM tuzakları

> **Eşlemeyi şekle bakarak yapmak.** Üçgenler döndürülmüş ya da ters çevrilmiş çizilir. Eşleme ya yazılıştaki harf sırasından ya da eşit açılardan okunur. "Eşit açıların karşısındaki kenarlar orantılıdır" cümlesi her zaman işe yarar.

> **Oranı ters kurmak.** $k = \dfrac{\text{büyük}}{\text{küçük}}$ alıp küçük üçgendeki bir kenarı bulmak için çarpmak. Sonucu kontrol et: küçük üçgenin kenarı büyük üçgeninkinden küçük çıkmalı. Ters oran seçeneklerde hep vardır.

> **Fark ile oranı karıştırmak.** "$|DE|$, $|AB|$'den $2$ fazla, öyleyse $|EF|$ de $|BC|$'den $2$ fazla" yanlış. Benzerlikte kenarlar **aynı sayıyla çarpılır**, aynı sayı eklenmez.

> **Açısı eşit diye K.A.K. demek.** Eşit açı orantılı iki kenarın arasında değilse K.A.K. yoktur. A.A. ya da K.K.K. için başka bilgi gerekir.

> **Alana $k$ uygulamak.** Çevre $k$ katına çıkar, alan $k^2$ katına çıkar.

## Kendini dene

### Soru 1
$\triangle ABC \sim \triangle DEF$, $|AB| = 4$, $|AC| = 6$ ve $|DE| = 10$'dur. $|DF|$ kaçtır?

A) 2,4
B) 12
C) 15
D) 16
E) 24

**Cevap:** C
**Çözüm:** $[AB] \leftrightarrow [DE]$ olduğundan $k = \dfrac{10}{4} = \dfrac{5}{2}$. $[AC] \leftrightarrow [DF]$: $|DF| = 6 \cdot \dfrac{5}{2} = 15$. $2{,}4$ oranı ters kurmaktır ($6 \cdot \frac{4}{10}$); $12$ ise farkı eklemektir ($6 + 6$).

### Soru 2
Kenar uzunlukları $6$, $8$ ve $9$ olan bir üçgen veriliyor. Kenar uzunlukları aşağıdakilerden hangisi olan üçgen, bu üçgenle benzerdir?

A) 3, 4, 5
B) 8, 10, 11
C) 12, 16, 20
D) 9, 12, 13,5
E) 18, 24, 30

**Cevap:** D
**Çözüm:** Sıralı kenarları oranla: $\dfrac{9}{6} = \dfrac{12}{8} = \dfrac{13{,}5}{9} = 1{,}5$. Üç oran eşit: K.K.K. B her kenara $2$ eklemektir; C ve E'de ilk iki oran tutar ($2$ ve $3$) ama üçüncü tutmaz ($\frac{20}{9}$, $\frac{30}{9}$). A'da $\frac{3}{6} = \frac{4}{8} = \frac{1}{2}$ ama $\frac{5}{9} \neq \frac{1}{2}$.

### Soru 3
$\triangle ABC \sim \triangle DEF$'dir. $A$ köşesinden çizilen kenarortayın uzunluğu $9$, $D$ köşesinden çizilen kenarortayın uzunluğu $6$'dır. $ABC$ üçgeninin çevresi $42$ ise $DEF$ üçgeninin çevresi kaçtır?

A) 21
B) 28
C) 36
D) 39
E) 63

**Cevap:** B
**Çözüm:** Karşılıklı kenarortayların oranı benzerlik oranıdır: $k = \dfrac{6}{9} = \dfrac{2}{3}$. Çevrelerin oranı da $k$: $42 \cdot \dfrac{2}{3} = 28$. $63$ oranı ters kurmak, $39$ ise farkı ($9 - 6 = 3$) çıkarmaktır.

## Özet kartı

- Benzer üçgenlerde karşılıklı açılar eşit, karşılıklı kenarlar orantılıdır; oran $k$.
- Eşleme harf sırasından ya da eşit açılardan okunur; eşit açıların karşısındaki kenarlar karşılıklıdır.
- A.A.: iki açı eşit. K.A.K.: iki kenar orantılı, aradaki açı eşit. K.K.K.: üç kenar orantılı.
- K.K.K.'de kenarları sırala; kısa–kısa, orta–orta, uzun–uzun oranla.
- Yükseklik, kenarortay, açıortay ve çevre oranı $k$; alan oranı $k^2$.
- Benzerlikte kenarlar aynı sayıyla çarpılır, aynı sayı eklenmez.

## Sonraki adım

Alıştırmaya geç (aşağıdaki düğme). Sonraki ders: **Üçgende Temel Orantı Teoremi**. Orada bugünkü A.A. benzerliğini, bir kenara paralel çizilen doğrunun oluşturduğu üçgenlere uygulayacaksın.
