---
baslik: Kare
ders: tyt-matematik
sure: 20 dk
kaynak: MEBİ Konu Özeti 635a4a0706
guncelleme: 2026-11-18
---
# Kare

<div class="giris" dir="rtl" lang="ar">

**الدرس ده عن إيه؟** عن المربع (kare): مستطيل أضلاعه الأربعة متساوية، فهو في نفس الوقت متوازي أضلاع ومستطيل ومعيّن (eşkenar dörtgen).

- هتعرف تجيب المحيط (çevre) والقطر (köşegen) من طول الضلع بفيثاغورس (Pisagor)، والعكس.
- هتشوف إن القطرين متساويين وبيقطعوا بعض بزاوية قائمة، وكل قطر بيقسم زاوية الركن نصين بالظبط (açıortay).
- هتحسب المساحة (alan) من الضلع أو من القطر، وهتتعلم حيلة المثلثين المتطابقين (eş üçgenler) لما خط يعدّي من ركن المربع.

**ليه مهم؟** المربع بييجي كتير في TYT، لوحده أو جوه أسئلة البلاط وطي الورق (katlama)، وأغلب أسئلته بتتحل بالقواعد الأربعة دي.

الدرس ٢٠ دقيقة، وكل قاعدة معاها رسمة ومثال محلول. امسك ورقة وقلم وامشي معانا خطوة بخطوة.

</div>

**Bu dersin sonunda:** karede kenardan köşegeni ve alanı (ya da tersini) bulabilecek, köşegenin $45^\circ$ ve diklik özelliklerinden açı hesaplayabilecek, bir köşeden geçen doğruya inen dikmelerde eş üçgenleri kullanabileceksin.

> **TYT'de yeri:** Kare soruları çoğunlukla bir köşegen ya da karenin bir köşesinden geçen bir doğru çizer. Açı sorularında anahtar köşegenin yaptığı $45^\circ$'dir; uzunluk ve alan sorularında Pisagor ile eş üçgenler. Fayans, tablo, kâğıt katlama gibi günlük hayat soruları da sıkça kare üzerine kurulur.

## Önce hatırla

<details><summary>Geçen dersten: ABCD dikdörtgeninde köşegenler O'da kesişiyor ve m(OAB) = 35°. m(AOB) kaç derecedir?</summary>
|OA| = |OB| olduğu için AOB ikizkenardır: m(OBA) = 35° ve m(AOB) = 180° − 70° = <b>110°</b>. Dikdörtgende köşegenler arasındaki açı köşegenin kenarla yaptığı açıya bağlıydı. Bugün göreceksin: karede bu açı her zaman 90°'dir.
</details>

<details><summary>Geçen dersten: ABCD dikdörtgeninde |AB| = 12, |AD| = 7. A'nın açıortayı [DC]'yi K'de kesiyor. |KC| kaçtır?</summary>
Açıortay 45° yapar, ADK ikizkenar dik üçgendir: |DK| = |AD| = 7. |KC| = 12 − 7 = <b>5</b>. Kenarlar eşit olsaydı K, C'ye düşerdi: karede köşenin açıortayı köşegenin ta kendisidir.
</details>

## Kare nedir?

Dört kenarı eşit olan dikdörtgene **kare** denir. Kare aynı zamanda bir paralelkenar, bir dikdörtgen ve bir eşkenar dörtgendir; bu yüzden üçünün de bütün özellikleri karede geçerlidir.

| Özellik | Paralelkenar | Dikdörtgen | Eşkenar dörtgen | Kare |
|---|:-:|:-:|:-:|:-:|
| Karşılıklı kenarlar paralel ve eşit | ✓ | ✓ | ✓ | ✓ |
| Dört kenar eşit | | | ✓ | ✓ |
| Dört açı $90^\circ$ | | ✓ | | ✓ |
| Köşegenler birbirini ortalar | ✓ | ✓ | ✓ | ✓ |
| Köşegenler eşit | | ✓ | | ✓ |
| Köşegenler dik ve köşe açılarını ikiye böler | | | ✓ | ✓ |

Tersinden de okunur: köşegenleri **eşit**, **birbirini ortalayan** ve **dik** olan dörtgen karedir (ortalıyorsa paralelkenar, eşitse dikdörtgen, dikse eşkenar dörtgen).

### 1. Kenar, çevre ve köşegen

**Örnek 1.** Çevresi $36$ cm olan $ABCD$ karesinin köşegeni kaç cm'dir?

![ABCD karesi; dört kenarda 9 yazıyor, dört köşede dik açı işareti. Mavi AC köşegeni 9√2; ABC üçgeni açık maviye boyalı. A'da köşegenin iki yanındaki açılar 45 ve 45 derece.](gorsel/tyt-matematik/25-08-kosegen.svg "Köşegen, mavi ABC ikizkenar dik üçgeninin hipotenüsüdür. A'daki dik açıyı iki tane 45°'ye böler.")

**Çözüm.**

1. Dört kenar eşittir: $4a = 36 \Rightarrow a = 9$ cm.
2. $ABC$ üçgeni $B$'de diktir ve $|AB| = |BC| = 9$. Pisagor: $|AC|^2 = 9^2 + 9^2 = 162 \Rightarrow |AC| = \sqrt{162} = 9\sqrt{2}$ cm.

**Kural:** Kenarı $a$ olan karede

$$\text{Ç}(ABCD) = 4a, \qquad |AC| = |BD| = a\sqrt{2}$$

Köşegen verilirse kenar $a = \dfrac{|AC|}{\sqrt{2}} = \dfrac{|AC|\sqrt{2}}{2}$ olur. Örneğin köşegen $10$ ise kenar $5\sqrt{2}$'dir.

> **Tuzak:** Köşegeni kenarın iki katı sanmak. $9$ kenarlı karenin köşegeni $18$ değil, $9\sqrt{2} \approx 12{,}7$'dir. Köşegen kenardan uzun, kenarın iki katından kısadır.

### 2. Köşegenler: eşit, dik, açıortay

**Örnek 2.** $ABCD$ karesinde $E$ noktası $[BD]$ köşegeni üzerindedir ve $m(\widehat{AEB}) = 100^\circ$'dir. $m(\widehat{BAE})$, $m(\widehat{BCE})$ ve $m(\widehat{ECD})$ kaç derecedir?

![ABCD karesi; BD köşegeni düz, AC köşegeni kesikli; ikisi O'da dik kesişiyor. E noktası BD üzerinde, O ile B arasında. Mavi AE ve CE doğru parçaları eşitlik çentikli. A'da BAE açısı 35, C'de BCE açısı 35, B'de iki tane 45, E'de AEB açısı 100 derece. ABE ve CBE üçgenleri açık mavi.](gorsel/tyt-matematik/25-08-kosegen-nokta.svg "Köşegen bir simetri doğrusudur: mavi ABE ve CBE üçgenleri eştir. Bu yüzden |AE| = |CE| ve A ile C'deki kırmızı açılar eşittir.")

**Çözüm.**

1. Köşegen köşe açısını ikiye böler: $m(\widehat{ABE}) = m(\widehat{EBC}) = 45^\circ$.
2. $ABE$ üçgeninde $m(\widehat{BAE}) = 180^\circ - 100^\circ - 45^\circ = 35^\circ$.
3. $ABE$ ile $CBE$ eştir: $|BA| = |BC|$, $m(\widehat{ABE}) = m(\widehat{CBE}) = 45^\circ$, $[BE]$ ortak (KAK). Bu yüzden $m(\widehat{BCE}) = m(\widehat{BAE}) = 35^\circ$ ve $|AE| = |CE|$.
4. $m(\widehat{ECD}) = 90^\circ - 35^\circ = 55^\circ$.

**Kural:** Kenarı $a$ olan $ABCD$ karesinde köşegenler $O$'da kesişirse

$$|AC| = |BD|, \qquad [AC] \perp [BD], \qquad |OA| = |OB| = |OC| = |OD| = \frac{a\sqrt{2}}{2}$$

- Köşegen ile kenar arasındaki açı her zaman $45^\circ$'dir. Köşegenler karenin içini dört eş ikizkenar dik üçgene böler.
- Bir köşegen üzerindeki her nokta, öbür iki köşeye eşit uzaklıktadır: $E \in [BD]$ ise $|AE| = |CE|$.

> **Tuzak:** $E$, $[BD]$ üzerindeyse eşit olanlar $|AE|$ ile $|CE|$'dir; $|AE|$ ile $|BE|$ değil. Simetri, köşegenin **dışında kalan** iki köşe arasındadır.

### 3. Alan

**Örnek 3.** Köşegeninin uzunluğu $12$ cm olan karenin alanı kaç cm²'dir?

![ABCD karesi; AC ve BD köşegenleri O'da dik kesişiyor. Dört yarım köşegende 6 yazıyor. AOB ve COD üçgenleri mavi, BOC ve DOA üçgenleri yeşil.](gorsel/tyt-matematik/25-08-alan.svg "Köşegenler kareyi dört eş ikizkenar dik üçgene böler. Her birinin dik kenarları 6 ve 6, alanı 18. Dördü birlikte 72.")

**Çözüm (kenardan).** $a = \dfrac{12}{\sqrt{2}} = 6\sqrt{2}$, alan $a^2 = (6\sqrt{2})^2 = 36 \cdot 2 = 72$ cm².

**Çözüm (köşegenden).** Köşegenler kareyi dört eş dik üçgene böler, her birinin dik kenarları $6$ ve $6$'dır: $4 \cdot \dfrac{6 \cdot 6}{2} = 72$ cm². Kısaca $\dfrac{12^2}{2} = 72$.

**Kural:** Kenarı $a$, köşegeni $e$ olan karede

$$A(ABCD) = a^2 = \frac{e^2}{2}$$

Kare bir eşkenar dörtgen olduğu için "köşegenler çarpımının yarısı" formülü de aynı sonucu verir: $\dfrac{e \cdot e}{2}$.

> **Tuzak:** Köşegenin karesini alanla karıştırmak. Köşegeni $12$ olan karenin alanı $144$ değil, $72$'dir. $144$, kenarı $12$ olan karenin alanıdır.

### 4. Bir köşeden geçen doğruya dikmeler

**Örnek 4.** $ABCD$ karesinin $D$ köşesinden geçen bir $d$ doğrusu karenin dışında kalıyor. $[AF] \perp d$ ve $[CE] \perp d$'dir ($F$ ve $E$, $d$ üzerinde). $|AF| = 3$ ve $|CE| = 4$ birim ise $|FE|$ ve $A(ABCD)$ kaçtır?

![ABCD karesi eğik duruyor; D köşesi yatay d doğrusunun üzerinde. A'dan d'ye kırmızı AF dikmesi 3, C'den d'ye kırmızı CE dikmesi 4. d üzerinde FD = 4 ve DE = 3 yeşil yazılmış. AFD ve DEC üçgenleri açık mavi; A'da ve D'de alfa açıları işaretli.](gorsel/tyt-matematik/25-08-dis-dikme.svg "Mavi AFD ve DEC üçgenleri eştir: A'daki ve D'deki α açıları eşit, hipotenüsler karenin kenarı. Bu yüzden |FD| = |CE| = 4 ve |DE| = |AF| = 3.")

**Çözüm.**

1. $F$, $D$, $E$ aynı doğru üzerinde ve $m(\widehat{ADC}) = 90^\circ$: $m(\widehat{FDA}) + m(\widehat{EDC}) = 90^\circ$.
2. $AFD$ dik üçgeninde $m(\widehat{FAD}) + m(\widehat{FDA}) = 90^\circ$. Öyleyse $m(\widehat{FAD}) = m(\widehat{EDC}) = \alpha$.
3. $AFD$ ve $DEC$ üçgenlerinde hipotenüsler eşit ($|AD| = |DC|$), dik açılar ve $\alpha$ açıları eşit: üçgenler eştir.
4. Eş açıların karşısındaki kenarlar eşittir: $|DE| = |AF| = 3$ ve $|FD| = |CE| = 4$.
5. $|FE| = |FD| + |DE| = 4 + 3 = 7$. Alan: $|AD|^2 = |AF|^2 + |FD|^2 = 3^2 + 4^2 = 25$.

**Doğru karenin içinden geçerse.** Bu kez doğru $D$'den karenin içine girer; dikmeler $C$ ve $A$'dan iner.

![ABCD karesi; D'den karenin içine inen DF doğru parçası. C'den bu doğruya kırmızı CE dikmesi 12, A'dan kırmızı AF dikmesi 5; E ve F'de dik açı işareti. Doğru üzerinde DE = 5 ve EF = 7 yeşil yazılmış. DEC üçgeni mavi, AFD üçgeni yeşil.](gorsel/tyt-matematik/25-08-ic-dikme.svg "Mavi DEC ve yeşil AFD üçgenleri yine eştir: |DE| = |AF| = 5, |DF| = |CE| = 12. Aradaki parça 12 − 5 = 7.")

**Örnek 5.** Şekilde $|AF| = 5$, $|CE| = 12$ ise $|EF|$ kaçtır? Aynı eşlikten $|DE| = |AF| = 5$ ve $|DF| = |CE| = 12$. Bu kez parçalar üst üste biner: $|EF| = |DF| - |DE| = 12 - 5 = 7$. Karenin kenarı $\sqrt{5^2 + 12^2} = 13$'tür.

**Kural:** Karenin bir köşesinden geçen doğruya komşu iki köşeden dikmeler inince iki eş dik üçgen oluşur. Dikmeler $|AF|$ ve $|CE|$ ise

$$\text{dışarıda: } |FE| = |AF| + |CE|, \qquad \text{içeride: } |EF| = |CE| - |AF|, \qquad a^2 = |AF|^2 + |CE|^2$$

> **Tuzak:** Eşit parçaları yanlış eşlemek. $D$'nin yanındaki parça, **öbür** üçgenin dikmesine eşittir: $|FD| = |CE|$, $|DE| = |AF|$. Ayrıca doğru karenin içinden geçiyorsa dikmeler toplanmaz, **çıkarılır**.

## Hangi kural ne zaman?

| Soruda verilen | Kullanacağın kural |
|---|---|
| Çevre, kenar ya da köşegen | $\text{Ç} = 4a$, köşegen $a\sqrt{2}$ |
| Köşegen ve bir açı | Köşegen kenarla $45^\circ$ yapar; köşegenler diktir |
| Köşegen üzerinde bir nokta | Simetri: $\lvert AE \rvert = \lvert CE \rvert$, eş açılar |
| Alan | $a^2$ ya da $\dfrac{e^2}{2}$ |
| Bir köşeden geçen doğru ve iki dikme | Eş dik üçgenler, sonra Pisagor |

## ÖSYM tuzakları

> **Köşegeni $2a$ sanmak.** Köşegen $a\sqrt{2}$'dir. Seçeneklerde $2a$ ve $2a\sqrt{2}$ hazır bekler.

> **Alanı köşegenin karesi sanmak.** Alan $\dfrac{e^2}{2}$'dir; $e^2$ seçeneği yarıya bölmeyi unutmaktır.

> **Köşegen açısını unutmak.** Karede köşegen ile kenar arasındaki $45^\circ$ şekilde yazılı değildir; sen yazmazsan açı sorusu çözülmez.

> **Simetriyi yanlış köşelere kurmak.** $E \in [BD]$ ise $A$ ve $C$ simetriktir; $B$ ve $D$ köşegenin üzerindedir, onlar için eşitlik yoktur.

> **Dikme sorusunda toplamak ya da çıkarmak.** Doğru karenin dışında kalıyorsa $|FE| = |AF| + |CE|$; içinden geçiyorsa $|EF| = |CE| - |AF|$. Önce şekle bak.

## Kendini dene

### Soru 1
Çevresi $28$ cm olan bir karenin köşegeni kaç cm'dir?

A) $7$
B) $7\sqrt{2}$
C) $14$
D) $14\sqrt{2}$
E) $49$

**Cevap:** B
**Çözüm:** $4a = 28 \Rightarrow a = 7$. Köşegen $a\sqrt{2} = 7\sqrt{2} \approx 9{,}9$ cm. $7$ kenarın kendisi, $14$ köşegeni $2a$ sanmak, $14\sqrt{2}$ çevrenin yarısını kenar almak, $49$ ise alandır.

### Soru 2
Köşegeninin uzunluğu $6$ cm olan bir karenin alanı kaç cm²'dir?

A) $6$
B) $9$
C) $12$
D) $18$
E) $36$

**Cevap:** D
**Çözüm:** $A = \dfrac{e^2}{2} = \dfrac{36}{2} = 18$ cm². Kontrol: kenar $\dfrac{6}{\sqrt{2}} = 3\sqrt{2}$, $(3\sqrt{2})^2 = 18$. $36$, köşegenin karesidir (ikiye bölmeyi unutmak); $9$ ise köşegenin yarısının karesidir.

### Soru 3
![ABCD karesi eğik duruyor; D köşesi yatay d doğrusunun üzerinde. A'dan d'ye kırmızı AF dikmesi 3, C'den d'ye kırmızı CE dikmesi; F ile E arası 10.](gorsel/tyt-matematik/25-08-kd3.svg "F ve E, d doğrusu üzerindedir.")

Şekildeki $ABCD$ karesinin $D$ köşesi $d$ doğrusu üzerindedir. $[AF] \perp d$, $[CE] \perp d$, $|AF| = 3$ birim ve $|FE| = 10$ birimdir. Buna göre $A(ABCD)$ kaç birimkaredir?

A) $30$
B) $49$
C) $58$
D) $100$
E) $109$

**Cevap:** C
**Çözüm:** $AFD$ ve $DEC$ eş üçgenlerdir: $|DE| = |AF| = 3$, öyleyse $|FD| = 10 - 3 = 7$. $AFD$ dik üçgeninde $|AD|^2 = 3^2 + 7^2 = 9 + 49 = 58$. Alan $|AD|^2 = 58$. $49$, yalnızca $|FD|^2$'dir; $109$, $3^2 + 10^2$ işleminden gelir; $100$ ise $|FE|$'yi kenar sanmaktır.

## Özet kartı

- Kare: dört kenarı eşit dikdörtgen; paralelkenar, dikdörtgen ve eşkenar dörtgenin bütün özellikleri geçerli.
- Çevre $4a$, köşegen $a\sqrt{2}$, alan $a^2 = \dfrac{e^2}{2}$.
- Köşegenler eşit, dik, birbirini ortalar ve köşe açısını $45^\circ + 45^\circ$ böler.
- Köşegen üzerindeki nokta öbür iki köşeye eşit uzaklıktadır.
- Köşeden geçen doğruya dikmeler: eş dik üçgenler, $a^2 = |AF|^2 + |CE|^2$; dışarıda topla, içeride çıkar.

## Sonraki adım

Alıştırmaya geç (aşağıdaki düğme). Sonraki ders: **Dikdörtgenin Alanı**. Orada bugünkü alan bilgisini dikdörtgene ve dikdörtgenin içine çizilen üçgenlere genişleteceksin.
