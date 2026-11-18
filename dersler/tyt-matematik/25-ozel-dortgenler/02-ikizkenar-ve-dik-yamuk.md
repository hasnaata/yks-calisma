---
baslik: İkizkenar ve Dik Yamuk
ders: tyt-matematik
sure: 25 dk
kaynak: MEBİ Konu Özeti 06c2283cdd
guncelleme: 2026-11-18
---
# İkizkenar ve Dik Yamuk

<div class="giris" dir="rtl" lang="ar">

**الدرس ده عن إيه؟** عن نوعين مخصوصين من شبه المنحرف (yamuk): شبه المنحرف المتساوي الساقين (ikizkenar yamuk) وشبه المنحرف القائم (dik yamuk).

- هتعرف إن في ikizkenar yamuk زاويتين القاعدة الواحدة متساويين، والقطرين (köşegenler) طولهم واحد.
- هتتعلم تنزّل الارتفاع (yükseklik) من فوق، فالشكل يتقسم لمستطيل ومثلث قائم أو اتنين، وتكمّل بفيثاغورس (Pisagor).
- هتعرف قانونين لما القطرين يقطعوا بعض بزاوية قائمة (dik kesişen): واحدة للـ ikizkenar yamuk وواحدة للـ dik yamuk.

**ليه مهم؟** أسئلة شبه المنحرف بتيجي كتير في هندسة TYT، وأغلبها بيتحل لما تنزّل ارتفاع وتبص على المثلث القائم اللي طلع.

الدرس ٢٥ دقيقة، ارسم كل شكل بإيدك وإنت ماشي معانا.

</div>

**Bu dersin sonunda:** ikizkenar ve dik yamukta yükseklik indirerek eksik kenarı, açıyı ya da köşegeni bulabilecek; köşegenler dik kesiştiğinde hangi kuralın geçerli olduğunu ayırt edebileceksin.

> **TYT'de yeri:** Geometri bölümünde yamuk sorularının çoğu ikizkenar ya da dik yamuktur. Soru genelde tabanları ve bir yan kenarı verir, yüksekliği, köşegeni ya da bir açıyı ister. Çözümün ilk adımı hemen her zaman aynıdır: üst köşelerden alt tabana dikme indirmek.

## Önce hatırla

<details><summary>Geçen dersten: ABCD yamuğunda [AB] ∥ [DC] ve m(DAB) = 65°. m(ADC) kaç derecedir?</summary>
Aynı yan kenar üzerindeki iki açı paralellerin arasında kalır, toplamları 180°'dir: m(ADC) = 180° − 65° = <b>115°</b>. Bugün ikizkenar yamukta bu açıların nasıl eşleştiğini göreceksin.
</details>

<details><summary>Geçen dersten: Tabanları 14 cm ve 6 cm olan bir yamuğun orta tabanı kaç cm'dir?</summary>
Orta taban, tabanların ortalamasıdır: (14 + 6) / 2 = <b>10 cm</b>. Bu sayı bugün ikizkenar yamukta iki yerde karşına çıkacak: dikme ayağından karşı köşeye uzaklıkta ve köşegenler dik olduğunda yükseklikte.
</details>

## İkizkenar yamuk

$ABCD$ yamuğunda $[AB] \parallel [DC]$ ve yan kenarlar eşitse ($|AD| = |BC|$) bu yamuğa **ikizkenar yamuk** denir. Bu derste hep $|AB| = a$ (alt taban, uzun), $|DC| = c$ (üst taban, kısa) ve yükseklik $h$ yazacağız.

### 1. Açılar: aynı tabandaki açılar eşittir

**Örnek 1.** $ABCD$ ikizkenar yamuğunda $[AB] \parallel [DC]$, $|AD| = |BC|$, $m(\widehat{DAB}) = (2x + 10)^\circ$ ve $m(\widehat{BCD}) = (3x + 20)^\circ$'dir. $x$ kaçtır?

![ABCD ikizkenar yamuğu. AD ve BC yan kenarlarında eşitlik çentikleri, AB ve DC üzerinde paralellik okları. A'daki açı 2x + 10 derece ve B'deki açı alfa mavi; C'deki açı 3x + 20 derece ve D'deki açı beta yeşil.](gorsel/tyt-matematik/25-02-acilar.svg "Mavi açılar (alt tabandakiler) birbirine, yeşil açılar (üst tabandakiler) birbirine eşittir. Bir mavi ile bir yeşilin toplamı 180°'dir.")

**Çözüm.**

1. İkizkenar yamukta alt tabandaki iki açı eşittir: $m(\widehat{B}) = m(\widehat{A}) = 2x + 10$.
2. $[AB] \parallel [DC]$ olduğu için $\widehat{B}$ ile $\widehat{C}$ aynı yan kenarın iki ucundadır, toplamları $180^\circ$'dir.
3. $(2x + 10) + (3x + 20) = 180 \Rightarrow 5x = 150 \Rightarrow x = 30$.
4. Açılar: $m(\widehat{A}) = m(\widehat{B}) = 70^\circ$, $m(\widehat{C}) = m(\widehat{D}) = 110^\circ$. Kontrol: dört açının toplamı $2 \cdot 70 + 2 \cdot 110 = 360$.

**Kural:**

$$m(\widehat{A}) = m(\widehat{B}) = \alpha, \qquad m(\widehat{C}) = m(\widehat{D}) = \beta, \qquad \alpha + \beta = 180^\circ$$

Sonuç olarak ikizkenar yamukta **karşılıklı** açılar da bütünlerdir: $m(\widehat{A}) + m(\widehat{C}) = 180^\circ$.

> **Tuzak:** Paralelkenarda karşılıklı açılar eşittir, ikizkenar yamukta değil. $2x + 10 = 3x + 20$ yazarsan $x = -10$ çıkar; negatif açı, yanlış kuralı kullandığını söyler.

### 2. Yükseklik indir: dikdörtgen ve iki eş dik üçgen

**Örnek 2.** $ABCD$ ikizkenar yamuğunda $|AB| = 16$, $|DC| = 6$ ve $|AD| = |BC| = 13$ birimdir. Yamuğun yüksekliği kaç birimdir?

![ABCD ikizkenar yamuğu: AB = 16, DC = 6, yan kenarlar 13. D ve C'den AB'ye kırmızı kesik çizgili DH ve CK dikmeleri iniyor. AH ve KB mavi, 5'er birim; HK = 6; h = 12.](gorsel/tyt-matematik/25-02-dikmeler.svg "İki dikme yamuğu ortada bir dikdörtgene (HK = DC = 6) ve iki yanda eş dik üçgenlere ayırır. Fazlalık 16 − 6 = 10 iki yana eşit bölünür: 5 ve 5.")

**Çözüm.**

1. $D$ ve $C$'den $[AB]$'ye $[DH]$ ve $[CK]$ dikmelerini indir. $DHKC$ dikdörtgendir: $|HK| = |DC| = 6$.
2. $ADH$ ve $BCK$ dik üçgenleri eştir (hipotenüsler $13$, dik kenarlar $h$). Bu yüzden $|AH| = |KB| = \dfrac{16 - 6}{2} = 5$.
3. $ADH$ üçgeninde Pisagor: $h^2 = 13^2 - 5^2 = 169 - 25 = 144 \Rightarrow h = 12$.
4. Bir şey daha: $|HB| = 6 + 5 = 11 = \dfrac{16 + 6}{2}$. Dikme ayağından karşı köşeye olan uzaklık orta tabana eşittir.

**Kural:**

$$|AH| = |KB| = \frac{a - c}{2}, \qquad |HB| = |AK| = \frac{a + c}{2}$$

> **Tuzak:** Tabanların farkı **iki yana** bölünür. $|AH| = 16 - 6 = 10$ alırsan $h^2 = 169 - 100 = 69$ bulursun; şıklarda $\sqrt{69}$ seni bekler.

### 3. Köşegenler eşittir

**Örnek 3.** $ABCD$ ikizkenar yamuğunda $[AC]$ ve $[BD]$ köşegenleri $E$ noktasında kesişiyor. $|ED| = 4$ ve $|EB| = 10$ birimdir. $|AC|$ kaç birimdir?

![ABCD ikizkenar yamuğu, köşegenler E'de kesişiyor. EA ve EB mavi, ED ve EC yeşil. ED = 4, EB = 10; EA ve EC soru işaretiyle gösterilmiş.](gorsel/tyt-matematik/25-02-kosegenler.svg "Mavi parçalar (alt tabana giden) eşittir, yeşil parçalar (üst tabana giden) eşittir. E köşegenlerin orta noktası değildir.")

**Çözüm.**

1. $ABD$ ve $BAC$ üçgenlerine bak: $|AD| = |BC|$, $[AB]$ ortak, aradaki açılar $m(\widehat{A}) = m(\widehat{B})$. Üçgenler eştir (KAK), bu yüzden $|BD| = |AC|$.
2. Eşlikten $m(\widehat{ABD}) = m(\widehat{BAC})$ da çıkar, yani $EAB$ üçgeni ikizkenardır: $|EA| = |EB| = 10$.
3. Köşegenler eşit olduğuna göre geriye kalan parçalar da eşittir: $|EC| = |ED| = 4$.
4. $|AC| = |EA| + |EC| = 10 + 4 = 14$. ($|BD| = 10 + 4 = 14$, tutuyor.)

**Kural:**

$$|AC| = |BD|, \qquad |EA| = |EB|, \qquad |EC| = |ED|$$

> **Tuzak:** Paralelkenarda köşegenler birbirini ortalar, ikizkenar yamukta ortalamaz. $|EA| = |EC|$ yazıp $|AC| = 2 \cdot 4 = 8$ ya da $2 \cdot 10 = 20$ bulmak yanlıştır.

### 4. Köşegenler dik kesişirse: $h = \dfrac{a + c}{2}$

**Örnek 4.** $ABCD$ ikizkenar yamuğunda köşegenler $E$ noktasında dik kesişiyor. $|AB| = 14$ ve $|DC| = 6$ birimdir. Yamuğun yüksekliği ve alanı kaçtır?

![Köşegenleri E'de dik kesişen ABCD ikizkenar yamuğu; köşegenler kırmızı. Alttaki EAB üçgeni mavi, üstteki EDC üçgeni yeşil boyalı. E'den AB'ye mavi kesik dikme 7, DC'ye yeşil kesik dikme 3. AB = 14, DC = 6.](gorsel/tyt-matematik/25-02-dik-kosegen.svg "Mavi ve yeşil üçgenler ikizkenar dik üçgendir. Dik köşeden inen yükseklik tabanın yarısıdır: 14 / 2 = 7 ve 6 / 2 = 3. Yükseklik 7 + 3 = 10.")

**Çözüm.**

1. Kural 3'ten $|EA| = |EB|$. Üstelik $E$'deki açı $90^\circ$. Demek ki $EAB$ **ikizkenar dik üçgendir**, taban açıları $45^\circ$.
2. $E$'den $[AB]$'ye inen dikme hem yükseklik hem kenarortaydır; $45^\circ$'lik üçgende bu dikme tabanın yarısına eşittir: $\dfrac{14}{2} = 7$.
3. Aynı şey $EDC$ üçgeninde: $E$'den $[DC]$'ye uzaklık $\dfrac{6}{2} = 3$.
4. Yükseklik $h = 7 + 3 = 10 = \dfrac{14 + 6}{2}$, yani orta tabana eşit.
5. Yamuğun alanı orta taban ile yüksekliğin çarpımıdır (ayrıntısı sonraki derste): $10 \cdot 10 = 100$ birimkare.

**Kural:** İkizkenar yamukta köşegenler dik kesişiyorsa

$$h = \frac{a + c}{2}, \qquad A(ABCD) = h^2$$

> **Tuzak:** Burada $h$ tabanların **toplamının** yarısıdır, farkının değil. $\dfrac{14 - 6}{2} = 4$, Kural 2'deki $|AH|$ parçasıdır, yükseklik değil.

## Dik yamuk

Bir açısı $90^\circ$ olan yamuğa **dik yamuk** denir. $[AB] \parallel [DC]$ ve $m(\widehat{A}) = 90^\circ$ ise $m(\widehat{D}) = 90^\circ$ olur (yan açılar bütünler). Dik olan $[AD]$ kenarı aynı zamanda yamuğun **yüksekliğidir**.

### 5. Dik yamukta yükseklik indir: tek dik üçgen

**Örnek 5.** $ABCD$ dik yamuğunda $[AB] \parallel [DC]$, $[AD] \perp [AB]$, $|AB| = 11$, $|DC| = 5$ ve $|AD| = 8$ birimdir. $|BC|$ kaç birimdir?

![ABCD dik yamuğu: A ve D'de dik açı. AD = 8, DC = 5, AB = 11. C'den AB'ye kırmızı kesik dikme CH = 8; AH = 5, HB = 6 mavi. BC soru işaretiyle gösterilmiş.](gorsel/tyt-matematik/25-02-dik-yamuk.svg "Tek bir dikme yeter: soldaki AHCD dikdörtgendir, sağda kalan CHB dik üçgeninin yatay kenarı tabanların farkıdır, 11 − 5 = 6.")

**Çözüm.**

1. $C$'den $[AB]$'ye $[CH]$ dikmesini indir. $AHCD$ dikdörtgendir: $|AH| = |DC| = 5$ ve $|CH| = |AD| = 8$.
2. $|HB| = 11 - 5 = 6$. Bu kez fark ikiye bölünmez, çünkü öbür yanda üçgen yok.
3. $CHB$ dik üçgeninde Pisagor: $|BC|^2 = 6^2 + 8^2 = 100 \Rightarrow |BC| = 10$.

**Kural:** Dik yamukta $|AD| = h$ ve eğik kenar için

$$|BC|^2 = h^2 + (a - c)^2$$

> **Tuzak:** İkizkenar yamuk alışkanlığıyla $|HB| = \dfrac{11 - 5}{2} = 3$ almak. Dik yamukta tabanların farkının tamamı tek üçgene gider.

### 6. Dik yamukta köşegenler dik kesişirse: $h^2 = a \cdot c$

**Örnek 6.** $ABCD$ dik yamuğunda $[AD] \perp [AB]$, köşegenler $O$ noktasında dik kesişiyor. $|AB| = 9$ ve $|DC| = 4$ birimdir. $|AD|$ kaç birimdir?

![ABCD dik yamuğu: A ve D'de dik açı, AB = 9, DC = 4, AD = h. Köşegenler AC ve BD kırmızı, O'da dik kesişiyor. A'da DAC açısı ve B'de ABD açısı aynı mavi yay ve noktayla işaretli.](gorsel/tyt-matematik/25-02-dik-yamuk-kosegen.svg "Noktalı mavi açılar eşittir. Bu yüzden ADC ve BAD dik üçgenleri benzerdir; kısa kenarın uzun kenara oranı ikisinde de aynıdır: 4/h = h/9.")

**Çözüm.**

1. $AOB$ üçgeninde $O$ dik olduğu için $m(\widehat{OAB}) + m(\widehat{OBA}) = 90^\circ$. Öte yandan $m(\widehat{DAC}) + m(\widehat{CAB}) = 90^\circ$. Demek ki $m(\widehat{DAC}) = m(\widehat{ABD})$.
2. $ADC$ üçgeni ($D$'de dik) ile $BAD$ üçgeni ($A$'da dik) iki açısı eş olduğu için benzerdir: $\dfrac{|DC|}{|AD|} = \dfrac{|AD|}{|AB|}$.
3. $|AD|^2 = |AB| \cdot |DC| = 9 \cdot 4 = 36 \Rightarrow |AD| = 6$.
4. Kontrol: $A(0, 0)$ alırsan $\overrightarrow{AC} = (4, 6)$, $\overrightarrow{DB} = (9, -6)$; $4 \cdot 9 + 6 \cdot (-6) = 0$, köşegenler gerçekten dik.

**Kural:** Dik yamukta köşegenler dik kesişiyorsa

$$h^2 = a \cdot c$$

> **Tuzak:** Kareyi unutmak ($h = 36$) ya da ikizkenar yamuğun kuralını kullanmak ($h = \dfrac{9 + 4}{2} = 6{,}5$). İki kural yalnızca şekil türüyle ayrılır.

## Hangi kural ne zaman?

| Şekil | İlk adım | Köşegenler dik ise |
|---|---|---|
| İkizkenar yamuk | İki dikme; yanlarda $\dfrac{a - c}{2}$ | $h = \dfrac{a + c}{2}$, alan $h^2$ |
| Dik yamuk | Tek dikme; yanda $a - c$ | $h^2 = a \cdot c$ |

İki kuralın ortak noktası yok gibi görünse de ikisi de aynı fikirden gelir: dik kesişen köşegenler şekilde benzer ya da ikizkenar dik üçgenler oluşturur.

## ÖSYM tuzakları

> **Paralelkenar kuralını taşımak.** İkizkenar yamukta karşılıklı açılar eşit değil, bütünlerdir; köşegenler eşittir ama birbirini ortalamaz.

> **Farkı ikiye bölmeyi unutmak.** İkizkenar yamukta yanlardaki parça $\dfrac{a - c}{2}$'dir. Dik yamukta ise ikiye bölünmez: $a - c$.

> **Yan kenarı yükseklik sanmak.** İkizkenar yamukta yan kenar yükseklikten uzundur. Dik yamukta yükseklik yalnızca dik olan kenardır, eğik kenar değil.

> **İki "dik köşegen" kuralını karıştırmak.** İkizkenar yamuk: $h = \dfrac{a + c}{2}$. Dik yamuk: $h^2 = a \cdot c$.

> **Alanı yarıya bölmek.** Köşegenleri dik ikizkenar yamukta alan $h^2$'dir, $\dfrac{h^2}{2}$ değil.

## Kendini dene

### Soru 1
![ABCD ikizkenar yamuğu, AB ve DC paralel, yan kenarlar eşit. B'deki açı 2x + 15 derece mavi, D'deki açı 4x − 15 derece yeşil.](gorsel/tyt-matematik/25-02-kd1.svg "Şekil ölçeklidir.")

Şekildeki $ABCD$ ikizkenar yamuğunda $[AB] \parallel [DC]$, $|AD| = |BC|$, $m(\widehat{ABC}) = (2x + 15)^\circ$ ve $m(\widehat{ADC}) = (4x - 15)^\circ$'dir. Buna göre $m(\widehat{ADC})$ kaç derecedir?

A) 30
B) 45
C) 75
D) 105
E) 120

**Cevap:** D
**Çözüm:** $m(\widehat{A}) = m(\widehat{B}) = 2x + 15$ ve $\widehat{A}$ ile $\widehat{D}$ aynı yan kenarda olduğu için $(2x + 15) + (4x - 15) = 180 \Rightarrow 6x = 180 \Rightarrow x = 30$. $m(\widehat{ADC}) = 4 \cdot 30 - 15 = 105$. $30$, $x$'in kendisidir; $75$, $\widehat{B}$'dir. $45$, $\widehat{B}$ ile $\widehat{D}$'yi eşit sanmaktan gelir ($2x + 15 = 4x - 15 \Rightarrow x = 15$).

### Soru 2
![ABCD ikizkenar yamuğu: AB = 21, DC = 9, yan kenarlar 10. AC köşegeni kırmızı kesik çizgi ve soru işaretiyle gösterilmiş.](gorsel/tyt-matematik/25-02-kd2.svg "Şekil ölçeklidir.")

Şekildeki $ABCD$ ikizkenar yamuğunda $[AB] \parallel [DC]$, $|AB| = 21$, $|DC| = 9$ ve $|AD| = |BC| = 10$ birimdir. Buna göre $|AC|$ kaç birimdir?

A) 8
B) 15
C) 17
D) 21
E) $\sqrt{505}$

**Cevap:** C
**Çözüm:** $C$'den $[AB]$'ye $[CK]$ dikmesi: $|KB| = \dfrac{21 - 9}{2} = 6$, $h^2 = 10^2 - 6^2 = 64 \Rightarrow h = 8$. $|AK| = 21 - 6 = 15$ (orta taban). $ACK$ dik üçgeninde $|AC|^2 = 15^2 + 8^2 = 289 \Rightarrow |AC| = 17$. $8$ yükseklik, $15$ ise $|AK|$'dir; $\sqrt{505}$, yatay kenar olarak bütün $|AB| = 21$'i almaktır.

### Soru 3
![ABCD dik yamuğu: A ve D'de dik açı, AB = 16, DC = 4. Köşegenler kırmızı, dik kesişiyor. AD soru işaretiyle gösterilmiş.](gorsel/tyt-matematik/25-02-kd3.svg "Şekil ölçeklidir.")

Şekildeki $ABCD$ dik yamuğunda $[AD] \perp [AB]$, $[AB] \parallel [DC]$, köşegenler dik kesişiyor, $|AB| = 16$ ve $|DC| = 4$ birimdir. Buna göre $|AD|$ kaç birimdir?

A) 6
B) 8
C) 10
D) 12
E) 64

**Cevap:** B
**Çözüm:** Dik yamukta köşegenler dikse $|AD|^2 = |AB| \cdot |DC| = 16 \cdot 4 = 64 \Rightarrow |AD| = 8$. $64$ karekök almayı unutmaktır; $10$, ikizkenar yamuğun kuralıdır ($\frac{16 + 4}{2}$); $6$ ve $12$ ise tabanların farkından gelir.

## Özet kartı

- İkizkenar yamuk: $|AD| = |BC|$; aynı tabandaki açılar eşit, yan açılar ve karşılıklı açılar bütünler.
- İki dikme indir: yanlarda $\dfrac{a - c}{2}$, ortada $c$; dikme ayağından karşı köşeye $\dfrac{a + c}{2}$.
- Köşegenler eşit: $|AC| = |BD|$; kesişim noktasında $|EA| = |EB|$ ve $|EC| = |ED|$.
- Köşegenleri dik ikizkenar yamuk: $h = \dfrac{a + c}{2}$, alan $h^2$.
- Dik yamuk: dik kenar yüksekliktir; eğik kenar için $|BC|^2 = h^2 + (a - c)^2$.
- Köşegenleri dik dik yamuk: $h^2 = a \cdot c$.

## Sonraki adım

Alıştırmaya geç (aşağıdaki düğme). Sonraki ders: **Yamuğun Alanı**. Örnek 4'te kullandığın "alan = orta taban × yükseklik" bağıntısının nereden geldiğini ve yamuğu köşegenlerle bölünce oluşan üçgenlerin alanlarını orada göreceksin.
