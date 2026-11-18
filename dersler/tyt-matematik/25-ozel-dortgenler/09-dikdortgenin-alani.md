---
baslik: Dikdörtgenin Alanı
ders: tyt-matematik
sure: 25 dk
kaynak: MEBİ Konu Özeti 230957714a
guncelleme: 2026-11-18
---
# Dikdörtgenin Alanı

<div class="giris" dir="rtl" lang="ar">

**الدرس ده عن إيه؟** عن مساحة المستطيل (dikdörtgenin alanı): الطول في العرض، وإزاي الخطوط اللي جوّاه بتقسّمه لأجزاء مساحتها معروفة.

- هتعرف تحسب المساحة حتى لو معاك المحيط (çevre) والقطر (köşegen) بس، من غير ما تلاقي الأضلاع.
- هتتعلم إن نقطة على ضلع (kenar) بتعمل مثلث مساحته نص المستطيل، وإن القطرين بيقسموه أربع مثلثات مساحتهم واحدة.
- هتشوف شكل نقط المنتصف (orta nokta) وإزاي المساحة بتتغير لما الأضلاع تكبر أو تصغر بنسبة مئوية.

**ليه مهم؟** المستطيل أكتر شكل بييجي في أسئلة الحياة اليومية في TYT زي الأرض والسيراميك والشاشة، والحل غالبًا خطوة أو اتنين لو شفت النص والربع في الرسمة.

الدرس ٢٥ دقيقة، وكل قاعدة معاها رسمة ومثال محلول. امسك ورقة وقلم وامشي معانا.

</div>

**Bu dersin sonunda:** dikdörtgenin alanını kenarlardan ya da çevre ve köşegenden bulabilecek, köşegenlerin, bir kenar üzerindeki noktanın ve orta noktaların ayırdığı parçaların alanını bütünün yarısı ya da dörtte biri olarak yazabileceksin.

> **TYT'de yeri:** Dikdörtgen alanı TYT'de çoğu zaman günlük hayat sorusu olarak gelir: tarla, oda tabanı, fayans, ekran, kenarların yüzde değişimi. Geometri sorularında ise dikdörtgenin içine bir nokta, köşegen ya da orta noktalar çizilir ve bir parçanın alanı sorulur. Hesap azdır; asıl iş parçanın bütünün kaçta kaçı olduğunu görmektir.

## Önce hatırla

<details><summary>Geçen dersten: Köşegeni 6√2 cm olan bir karenin alanı kaç cm²'dir?</summary>
Karede köşegen $a\sqrt{2}$'dir: $a\sqrt{2} = 6\sqrt{2} \Rightarrow a = 6$, alan $6^2 =$ <b>36 cm²</b>. Kısa yol: kare bir eşkenar dörtgendir, alan $\dfrac{e^2}{2} = \dfrac{72}{2} = 36$. Bu kısa yol yalnızca karede çalışır; bugün dikdörtgende neden çalışmadığını göreceksin.
</details>

<details><summary>Geçen dersten: Karenin köşegenleri birbirini nasıl keser ve bir köşegen köşe açısını kaça böler?</summary>
Köşegenler eşittir, birbirine <b>diktir</b> ve birbirini <b>ortalar</b>; her köşegen köşe açısını iki $45^\circ$'ye böler. Kare bir dikdörtgendir, bu yüzden bugünkü bütün kurallar kare için de geçerlidir.
</details>

## Temel formül

### 1. Alan = uzun kenar · kısa kenar

**Örnek 1.** $ABCD$ dikdörtgeninde $|AB| = 8$ cm ve $|AC| = 10$ cm'dir. Dikdörtgenin alanı kaç cm²'dir?

![ABCD dikdörtgeni birim karelere bölünmüş: AB kenarı 8, BC kenarı 6 birim. Mavi AC köşegeni 10. Dört köşede dik açı işareti.](gorsel/tyt-matematik/25-09-temel.svg "Birim karelere bak: 8 sütun ve 6 sıra var, yani 48 kare. Alanı köşegen değil, iki kenar belirler.")

**Çözüm.**

1. $ABC$ dik üçgeninde Pisagor: $|BC|^2 = 10^2 - 8^2 = 36 \Rightarrow |BC| = 6$ cm. (6-8-10, yani 3-4-5'in iki katı.)
2. $A(ABCD) = |AB| \cdot |BC| = 8 \cdot 6 = 48$ cm².

**Kural:** Kenarları $a$ ve $b$ olan dikdörtgende

$$A(ABCD) = a \cdot b, \qquad \text{Çevre} = 2(a + b), \qquad |AC|^2 = a^2 + b^2$$

Dikdörtgen bir paralelkenardır; yüksekliği doğrudan öbür kenardır. Bu yüzden "taban · yükseklik" burada "kenar · kenar" olur.

**Örnek 2.** Çevresi $34$ cm, köşegeni $13$ cm olan dikdörtgenin alanı kaç cm²'dir?

**Çözüm.** Kenarları bulmak zorunda değilsin.

1. Çevreden: $2(a + b) = 34 \Rightarrow a + b = 17$.
2. Köşegenden: $a^2 + b^2 = 13^2 = 169$.
3. $(a + b)^2 = a^2 + b^2 + 2ab \Rightarrow 289 = 169 + 2ab \Rightarrow 2ab = 120 \Rightarrow ab = 60$ cm².
4. Kontrol: $5 + 12 = 17$ ve $5^2 + 12^2 = 169$; $5 \cdot 12 = 60$.

$$(a + b)^2 = |AC|^2 + 2 \cdot A(ABCD)$$

> **Tuzak:** Kareden kalan $\dfrac{e^2}{2}$ alışkanlığı. Bu, köşegenleri dik olan dörtgenler içindir; dikdörtgenin köşegenleri dik değildir. Örnekte $\dfrac{13^2}{2} = 84{,}5$ seçeneklerde bekler, doğrusu $60$. Bir de $2ab = 120$'de durmak: alan $ab$'dir.

## Alanı bölen çizgiler

### 2. Kenar üzerinde bir nokta: üçgen yarıyı alır

**Örnek 3.** $ABCD$ dikdörtgeninde $|AB| = 10$, $|BC| = 6$ birimdir. $E \in [DC]$ ve $|DE| = 4$ birimdir. $A(AEB)$, $A(ADE)$ ve $A(BEC)$ kaç birimkaredir?

![ABCD dikdörtgeni: AB = 10, BC = 6. E noktası DC üzerinde, DE = 4, EC = 6. AEB üçgeni mavi (30), ADE üçgeni sarı (12), BEC üçgeni sarı (18).](gorsel/tyt-matematik/25-09-kenarda-nokta.svg "Mavi üçgenin tabanı AB, yüksekliği dikdörtgenin kenarı kadardır. Mavi bütünün yarısı, iki sarı da öbür yarıyı paylaşır.")

**Çözüm.**

1. $A(ABCD) = 10 \cdot 6 = 60$.
2. $AEB$ üçgeninin tabanı $|AB| = 10$, yüksekliği $E$'nin $[AB]$'ye uzaklığı, yani $6$: $A(AEB) = \dfrac{10 \cdot 6}{2} = 30$.
3. $ADE$ dik üçgeni: $\dfrac{4 \cdot 6}{2} = 12$. $|EC| = 10 - 4 = 6$, $BEC$ dik üçgeni: $\dfrac{6 \cdot 6}{2} = 18$.
4. Kontrol: $12 + 18 = 30$, öbür yarı.

**Kural:** $E \in [DC]$ ise

$$A(AEB) = A(ADE) + A(BEC) = \frac{A(ABCD)}{2}$$

İki köşe üçgeni yarıyı $|DE| : |EC|$ oranında paylaşır.

> **Tuzak:** $E$ kayınca mavi üçgenin alanının değiştiğini sanmak. $E$, $[DC]$ üzerinde nerede olursa olsun $A(AEB)$ hep yarıdır. Köşe üçgenlerinde de $\frac{1}{2}$'yi unutma: $A(BEC) = 6 \cdot 6 = 36$ değil, $18$.

### 3. Köşegenler: dört eşit üçgen

**Örnek 4.** $ABCD$ dikdörtgeninde $|AB| = 12$, $|BC| = 8$ birimdir. Köşegenler $E$ noktasında kesişiyor. $A(AEB)$ ve $A(BEC)$ kaç birimkaredir?

![ABCD dikdörtgeni: AB = 12, BC = 8; AC ve BD köşegenleri E'de kesişiyor. Dört üçgenin her birinde 24 yazıyor; AEB ve CED mavi, BEC ve DEA yeşil. E'den AB'ye 4 birimlik, E'den BC'ye 6 birimlik kırmızı kesikli dikme.](gorsel/tyt-matematik/25-09-kosegenler.svg "Mavi üçgenin tabanı uzun (12), yüksekliği kısa (4); yeşilin tabanı kısa (8), yüksekliği uzun (6). Çarpım ikisinde de aynı.")

**Çözüm.**

1. $A(ABCD) = 12 \cdot 8 = 96$.
2. $E$, dikdörtgenin merkezidir: $[AB]$'ye uzaklığı $\dfrac{8}{2} = 4$, $[BC]$'ye uzaklığı $\dfrac{12}{2} = 6$.
3. $A(AEB) = \dfrac{12 \cdot 4}{2} = 24$, $A(BEC) = \dfrac{8 \cdot 6}{2} = 24$.
4. Dört üçgen de $24$, yani $\dfrac{96}{4}$.

**Kural:** Bir köşegen dikdörtgeni iki eş dik üçgene ayırır; iki köşegen alanları eşit dört üçgene ayırır.

$$A(ABC) = \frac{A(ABCD)}{2}, \qquad A(AEB) = A(BEC) = A(CED) = A(DEA) = \frac{A(ABCD)}{4}$$

> **Tuzak:** Kısa kenara dayanan üçgeni ($BEC$) daha küçük sanmak. Üçgenlerin biçimi farklıdır ama alanları eşittir: kısa tabana uzun yükseklik düşer.

### 4. Orta noktalar: köşelerde iki çeyrek, ortada yarı

**Örnek 5.** $ABCD$ dikdörtgeninde $|AB| = 12$, $|BC| = 8$ birimdir. $E$, $[AD]$'nin; $F$, $[BC]$'nin orta noktasıdır. $A(ABF)$, $A(EDC)$ ve $A(AFCE)$ kaç birimkaredir?

![ABCD dikdörtgeni: AB = 12, BF = FC = 4. E, AD'nin, F, BC'nin orta noktası. AF ve EC mavi çizgiler. Köşedeki ABF ve EDC üçgenleri sarı (24), ortadaki AFCE paralelkenarı mavi (48).](gorsel/tyt-matematik/25-09-orta-noktalar.svg "İki sarı üçgen birbirinin eşidir, her biri bütünün dörtte biri. Ortadaki mavi parça paralelkenardır ve bütünün yarısıdır.")

**Çözüm.**

1. $A(ABCD) = 12 \cdot 8 = 96$.
2. $ABF$ dik üçgeni: $\dfrac{|AB| \cdot |BF|}{2} = \dfrac{12 \cdot 4}{2} = 24$. $EDC$ dik üçgeni: $\dfrac{|DC| \cdot |DE|}{2} = \dfrac{12 \cdot 4}{2} = 24$.
3. $A(AFCE) = 96 - 24 - 24 = 48$.
4. İkinci yol: $[AE] \parallel [FC]$ ve $|AE| = |FC| = 4$ olduğundan $AFCE$ bir paralelkenardır. Tabanı $|AE| = 4$, yüksekliği $|AB| = 12$: $4 \cdot 12 = 48$.

**Kural:** $E$ ve $F$ karşılıklı iki kenarın ($[AD]$ ve $[BC]$) orta noktaları ise bütünü $4S$ al:

$$A(ABF) = A(EDC) = S, \qquad A(AFCE) = 2S = \frac{A(ABCD)}{2}$$

> **Tuzak:** $AFCE$'yi dikdörtgen sanıp $|AF| \cdot |AE|$ ile hesaplamak. $AFCE$ bir paralelkenardır, $[AF]$ ile $[AE]$ dik değildir: $|AF| \cdot |AE| = 4\sqrt{10} \cdot 4 \approx 50{,}6$ yanlış. Paralelkenarda taban ile ona **dik** yüksekliği çarp.

### 5. Kenarlar değişince alan

**Örnek 6.** Kenarları $10$ m ve $5$ m olan dikdörtgen bir bahçenin uzun kenarı $\%20$ uzatılıyor, kısa kenarı $\%20$ kısaltılıyor. Bahçenin alanı yüzde kaç değişir?

![Kesikli çizgiyle eski 10'a 5 dikdörtgen, düz çizgiyle yeni 12'ye 4 dikdörtgen. Ortak 10'a 4 parça mavi (40), üstte kaybedilen 10'a 1 şerit kırmızı (eksi 10), sağda kazanılan 2'ye 4 şerit yeşil (artı 8).](gorsel/tyt-matematik/25-09-kenar-degisimi.svg "Kaybedilen kırmızı şerit (10), kazanılan yeşil şeritten (8) büyük. Alan 2 birim azalır.")

**Çözüm.**

1. Eski alan: $10 \cdot 5 = 50$ m².
2. Yeni kenarlar: $10 \cdot 1{,}2 = 12$ ve $5 \cdot 0{,}8 = 4$. Yeni alan: $12 \cdot 4 = 48$ m².
3. Değişim: $\dfrac{48 - 50}{50} = -\dfrac{2}{50} = -\%4$. Alan $\%4$ azalır.
4. Kısa yol: alan $1{,}2 \cdot 0{,}8 = 0{,}96$ katına iner. Bu, kenarların uzunluğundan bağımsızdır.

**Kural:** Kenarlar $k$ ve $m$ katına çıkarsa alan $k \cdot m$ katına çıkar. İki kenar da $k$ katına çıkarsa alan $k^2$ katına çıkar.

$$A_{\text{yeni}} = (k \cdot a) \cdot (m \cdot b) = k \cdot m \cdot A$$

> **Tuzak:** Yüzdeleri toplamak: $+\%20 - \%20 = 0$ sanıp "değişmez" demek. Yüzdeler çarpılır: $1{,}2 \cdot 0{,}8 = 0{,}96$. Benzer biçimde iki kenar da iki katına çıkarsa alan iki değil **dört** katına çıkar.

## Hangi kural ne zaman?

| Soruda verilen | Kullanacağın kural |
|---|---|
| İki kenar ya da bir kenar ve köşegen | $A = a \cdot b$ (gerekirse önce Pisagor) |
| Çevre ve köşegen | $(a + b)^2 = \lvert AC \rvert^2 + 2A$ |
| Bir kenar üzerinde nokta | O noktadan karşı kenara çizilen üçgen yarıdır |
| İki köşegen | Dört üçgenin her biri dörtte birdir |
| Karşılıklı kenarların orta noktaları | Köşe üçgenleri $S$, ortadaki paralelkenar $2S$ |
| Kenarlarda yüzde ya da kat değişimi | Çarpanları çarp: $k \cdot m$ |

## ÖSYM tuzakları

> **Alanı köşegenle hesaplamak.** $|AB| \cdot |AC|$ alan değildir; alan iki **kenarın** çarpımıdır. Köşegen verilmişse önce Pisagor ile öbür kenarı bul.

> **Kare formülünü taşımak.** $\dfrac{e^2}{2}$ yalnızca karede (köşegenler dikken) çalışır. Dikdörtgende köşegen tek başına alanı belirlemez.

> **Üçgende $\frac{1}{2}$'yi unutmak.** Köşe üçgenleri ve köşegen üçgenleri birer üçgendir; dikdörtgenin kendisinde ise $\frac{1}{2}$ yoktur.

> **Yüzdeleri toplamak.** $\%25$ uzatıp $\%20$ kısaltınca alan $\%5$ artmaz, $1{,}25 \cdot 0{,}8 = 1$ olduğu için değişmez.

> **Birimleri karıştırmak.** Oda metre, fayans santimetre verilirse önce birimi eşitle: $40$ cm $= 0{,}4$ m, ve $0{,}4 \cdot 0{,}4 = 0{,}16$ m² (1,6 değil).

## Kendini dene

### Soru 1
![ABCD dikdörtgeni: AB = 9, BC = 6. E noktası DC üzerinde; AE ve EB mavi çizgiler. ADE üçgeni sarı, içinde 12; BEC üçgeni yeşil, içinde soru işareti.](gorsel/tyt-matematik/25-09-kd1.svg "Şekil ölçeklidir.")

Şekildeki $ABCD$ dikdörtgeninde $E \in [DC]$, $|AB| = 9$ cm, $|BC| = 6$ cm ve $A(ADE) = 12$ cm²'dir. Buna göre $A(BEC)$ kaç cm²'dir?

A) 12
B) 15
C) 27
D) 30
E) 42

**Cevap:** B
**Çözüm:** $A(ABCD) = 9 \cdot 6 = 54$, $A(AEB) = 27$. Köşe üçgenleri öbür yarıyı paylaşır: $A(ADE) + A(BEC) = 27 \Rightarrow A(BEC) = 27 - 12 = 15$. (Kontrol: $\dfrac{|DE| \cdot 6}{2} = 12 \Rightarrow |DE| = 4$, $|EC| = 5$, $\dfrac{5 \cdot 6}{2} = 15$.) $12$, iki köşe üçgenini eşit sanmaktır; $27$, yarının kendisidir; $30$, $\frac{1}{2}$'yi unutmaktır ($5 \cdot 6$); $42$ ise $54$'ten yalnızca $12$'yi çıkarmaktır.

### Soru 2
Çevresi $28$ cm, köşegeni $10$ cm olan bir dikdörtgenin alanı kaç cm²'dir?

A) 24
B) 48
C) 49
D) 50
E) 96

**Cevap:** B
**Çözüm:** $a + b = 14$, $a^2 + b^2 = 100$. $(a + b)^2 = 196 = 100 + 2ab \Rightarrow 2ab = 96 \Rightarrow ab = 48$. (Kenarlar $6$ ve $8$.) $96$, $2ab$'de durmaktır; $50$, kare formülü $\dfrac{10^2}{2}$'dir; $49$, dikdörtgeni kenarı $7$ olan kare sanmaktır; $24$, alanı yanlışlıkla ikiye bölmektir.

### Soru 3
![ABCD dikdörtgeni: AB = 10, BC = 8. E, AD'nin, F, BC'nin orta noktası; AF ve EC mavi çizgiler. Aradaki AFCE parçası mavi boyalı, içinde soru işareti.](gorsel/tyt-matematik/25-09-kd3.svg "Şekil ölçeklidir.")

Şekildeki $ABCD$ dikdörtgeninde $E$ ve $F$ sırasıyla $[AD]$ ve $[BC]$ kenarlarının orta noktalarıdır. $|AB| = 10$ birim ve $|BC| = 8$ birim olduğuna göre $A(AFCE)$ kaç birimkaredir?

A) 20
B) 32
C) 40
D) 60
E) 80

**Cevap:** C
**Çözüm:** $A(ABCD) = 80$. Köşe üçgenleri $A(ABF) = A(EDC) = \dfrac{10 \cdot 4}{2} = 20$; $A(AFCE) = 80 - 40 = 40$. Ya da paralelkenar olarak: taban $|AE| = 4$, yükseklik $|AB| = 10$, $4 \cdot 10 = 40$. $20$, ortadaki parçayı çeyrek sanmaktır; $32$, yükseklik yerine $|BC| = 8$ almaktır ($4 \cdot 8$); $60$, yalnızca bir köşe üçgenini çıkarmaktır; $80$ bütün dikdörtgendir.

## Özet kartı

- $A = a \cdot b$; köşegen verilirse önce Pisagor. Çevre ve köşegenden: $(a + b)^2 = |AC|^2 + 2A$.
- Dikdörtgende $\frac{e^2}{2}$ yok; o kare içindir.
- $E \in [DC]$: $A(AEB) = \frac{A}{2}$; köşe üçgenleri öbür yarıyı paylaşır.
- İki köşegen: alanı eşit dört üçgen, her biri $\frac{A}{4}$.
- $[AD]$ ve $[BC]$'nin orta noktaları: köşe üçgenleri $\frac{A}{4}$, ortadaki paralelkenar $\frac{A}{2}$.
- Kenarlar $k$ ve $m$ katına çıkarsa alan $k \cdot m$ katına çıkar; yüzdeler toplanmaz, çarpılır.

## Sonraki adım

Alıştırmaya geç (aşağıdaki düğme). Sonraki ders: **Deltoid**. Deltoidin köşegenleri, dikdörtgenin aksine birbirine diktir; bu yüzden orada alan yeniden köşegenlerden, $\dfrac{e \cdot f}{2}$ ile hesaplanır.
