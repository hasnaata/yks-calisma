---
baslik: Yamuğun Alanı
ders: tyt-matematik
sure: 25 dk
kaynak: MEBİ Konu Özeti 1d1534aae3
guncelleme: 2026-11-18
---
# Yamuğun Alanı

<div class="giris" dir="rtl" lang="ar">

**الدرس ده عن إيه؟** عن مساحة شبه المنحرف (yamuğun alanı): إزاي تحسبها من القاعدتين (taban) والارتفاع (yükseklik)، وإزاي تقسمها لمثلثات وتلعب بيها.

- هتعرف القانون الأساسي: نص مجموع القاعدتين في الارتفاع، وإزاي تطلع الارتفاع بفيثاغورس (Pisagor) لو مش مكتوب.
- هتتعلم إن المثلث اللي رأسه في نص الضلع الجانبي (yan kenar) مساحته نص مساحة شبه المنحرف بالظبط.
- هتشوف إزاي الأقطار (köşegen) بتقسم الشكل لأربع مثلثات: اللي على الجنبين مساحتهم واحدة، وتقدر تجيب أي واحد من التانيين.

**ليه مهم؟** مساحة شبه المنحرف بتيجي كتير في TYT، ساعات على شكل أرض أو جنينة أو لوحة، وأغلب الأسئلة بتتحل بقاعدة واحدة من غير حسابات طويلة.

الدرس 25 دقيقة، وكل قاعدة معاها رسمة ومثال محلول. امسك ورقة وقلم وحل معانا خطوة بخطوة.

</div>

**Bu dersin sonunda:** bir yamuğun alanını tabanlardan ve yükseklikten hesaplayabilecek; yan kenarın orta noktası, tabandaki bir nokta ya da köşegenlerle oluşan üçgenlerin alanlarını birbirinden tek adımda bulabileceksin.

> **TYT'de yeri:** Yamuk alanı soruları iki kalıpta gelir: "alan kaç birimkaredir?" (tabanlar ve yükseklik, gerekirse Pisagor) ve "boyalı bölgenin alanı kaçtır?" (yamuğun içindeki üçgenler). Yeni nesil sorularda yamuk bir bahçe, bir tarla ya da bir levhadır; yine bu kurallarla çözülür.

## Önce hatırla

<details><summary>Geçen dersten: ABCD ikizkenar yamuğunda [AB] ∥ [DC], |AB| = 16, |DC| = 6 ve köşegenler birbirini dik kesiyor. Yamuğun yüksekliği kaçtır?</summary>
Köşegenleri dik olan ikizkenar yamukta yükseklik, tabanların toplamının yarısıdır: h = (16 + 6) / 2 = <b>11</b>. Alan da h² = 121 olur. Bugünkü temel formül aynı sonucu verecek: (16 + 6) / 2 · 11 = 121.
</details>

<details><summary>Geçen dersten: ABCD dik yamuğunda [AB] ∥ [DC], [AD] ⊥ [AB], köşegenler birbirine dik, |AB| = 9 ve |DC| = 4. |AD| kaçtır?</summary>
Dik yamukta köşegenler dikse h² = a · c: |AD|² = 9 · 4 = 36, |AD| = <b>6</b>. Dik yamukta dik kenar aynı zamanda yüksekliktir; bugün alanı (9 + 4) / 2 · 6 = 39 diye bulacaksın.
</details>

## Harfler

Bu derste hep $[AB] \parallel [DC]$ alınır: $|AB| = a$ alt taban, $|DC| = c$ üst taban, $h$ iki taban arasındaki **dik uzaklık** (yükseklik). $A(ABCD)$, $ABCD$'nin alanı demektir.

## 1. Temel formül

**Örnek 1.** $ABCD$ yamuğunda $[AB] \parallel [DC]$, $|AB| = 12$, $|DC| = 6$ ve yükseklik $|DH| = 4$'tür. $A(ABCD)$ kaçtır?

![ABCD yamuğu, AB = 12, DC = 6. D'den AB'ye kırmızı kesikli DH dikmesi, h = 4. Kesikli BD köşegeni yamuğu mavi ABD ve yeşil BCD üçgenlerine ayırıyor; alanları 24 ve 12.](gorsel/tyt-matematik/25-03-temel.svg "İki üçgenin yüksekliği de 4'tür. Mavi üçgenin tabanı 12, yeşilinki 6. Alanlar 24 ve 12; toplam 36.")

**Çözüm.**

1. $[BD]$ köşegenini çiz. Yamuk iki üçgene ayrılır; ikisinin de yüksekliği $h = 4$'tür (tabanlar paralel olduğu için aradaki uzaklık her yerde aynıdır).
2. $A(ABD) = \dfrac{12 \cdot 4}{2} = 24$, $\quad A(BCD) = \dfrac{6 \cdot 4}{2} = 12$.
3. $A(ABCD) = 24 + 12 = 36$. Tek adımda: $\dfrac{12 + 6}{2} \cdot 4 = 9 \cdot 4 = 36$.

**Kural:**

$$A(ABCD) = \frac{a + c}{2} \cdot h$$

$\dfrac{a + c}{2}$ geçen dersteki **orta tabandır**. Yani alan = orta taban $\cdot$ yükseklik. Soru orta tabanı verirse doğrudan $h$ ile çarp.

> **Tuzak:** $(a + c) \cdot h$ yazıp ikiye bölmeyi unutmak sonucu iki katına çıkarır (72). Formül tersine de çalışır: alan ve tabanlar verilirse $h$'yi bulursun.

## 2. Yükseklik verilmemişse: Pisagor

**Örnek 2.** $ABCD$ ikizkenar yamuğunda $[AB] \parallel [DC]$, $|AB| = 14$, $|DC| = 6$ ve $|AD| = |BC| = 5$'tir. $A(ABCD)$ kaçtır?

![İkizkenar ABCD yamuğu, AB = 14, DC = 6, yan kenarlar 5. D'den ve C'den AB'ye kırmızı kesikli dikmeler, ayakları H ve K. AH = 4, HK = 6, KB = 4; iki uçtaki sarı dik üçgenlerde yükseklik 3.](gorsel/tyt-matematik/25-03-pisagor.svg "Sarı dik üçgenler 3-4-5 üçgenidir. Ortadaki parça üst tabana eşittir (6); iki uçta (14 − 6) / 2 = 4 kalır.")

**Çözüm.**

1. $D$ ve $C$'den alt tabana dikmeler indir; ayakları $H$ ve $K$ olsun. $DCKH$ bir dikdörtgendir, $|HK| = 6$.
2. İkizkenar yamukta iki uçta kalan parçalar eşittir: $|AH| = |KB| = \dfrac{14 - 6}{2} = 4$.
3. $AHD$ dik üçgeninde Pisagor: $h^2 = 5^2 - 4^2 = 9 \Rightarrow h = 3$.
4. $A(ABCD) = \dfrac{14 + 6}{2} \cdot 3 = 10 \cdot 3 = 30$.

**Kural:** Yükseklik yoksa üst tabanın uçlarından dikme indir. Uçta oluşan dik üçgende yan kenar hipotenüstür; $h$'yi Pisagor verir. İkizkenar yamukta uçtaki parça $\dfrac{a - c}{2}$'dir.

> **Tuzak:** Yan kenar yükseklik **değildir** (eğiktir, yükseklikten uzundur). $5$'i yükseklik alırsan $10 \cdot 5 = 50$ bulursun. Yan kenar ancak tabana dikse (dik yamuk) yüksekliğe eşittir.

## 3. Yan kenarın orta noktası: alanın yarısı

**Örnek 3.** $ABCD$ yamuğunda $[AB] \parallel [DC]$, $|AB| = 10$, $|DC| = 6$, yükseklik $4$'tür. $E$, $[AD]$'nin orta noktasıdır. $A(EBC)$ kaçtır?

![ABCD yamuğu, AB = 10, DC = 6. E, AD'nin orta noktası, iki eş parça çentikle işaretli. E'den B'ye ve C'ye mavi çizgiler. Mavi EBC üçgeninin alanı 16; sarı ABE üçgeni 10, sarı DEC üçgeni 6.](gorsel/tyt-matematik/25-03-orta-nokta.svg "İki sarı üçgenin toplamı (10 + 6) mavi üçgene eşittir. Mavi üçgen yamuğun tam yarısıdır.")

**Çözüm.**

1. $E$ orta nokta olduğu için iki tabana da uzaklığı $\dfrac{h}{2} = 2$'dir.
2. $A(ABE) = \dfrac{10 \cdot 2}{2} = 10$, $\quad A(DEC) = \dfrac{6 \cdot 2}{2} = 6$.
3. $A(ABCD) = \dfrac{10 + 6}{2} \cdot 4 = 32$.
4. $A(EBC) = 32 - 10 - 6 = 16$. Bu, $32$'nin tam yarısıdır.

**Neden hep yarısı?** Sarı üçgenlerin toplamı $\dfrac{a \cdot \frac{h}{2}}{2} + \dfrac{c \cdot \frac{h}{2}}{2} = \dfrac{(a + c) \cdot h}{4}$, yani yamuğun yarısı. Geriye kalan mavi üçgen de öbür yarıdır.

**Kural:** $E$, bir yan kenarın orta noktası ise

$$A(ABCD) = 2 \cdot A(EBC)$$

> **Tuzak:** Üçgenin köşeleri $E$ ve **öbür yan kenarın** iki ucudur ($B$ ve $C$). $E$ bir tabanın orta noktası olsaydı bu kural geçerli olmazdı. Kural iki sarı üçgenin **toplamı** için de geçerlidir: toplamları da yamuğun yarısıdır.

## 4. Köşegenlerin ayırdığı dört üçgen

$[AC]$ ve $[BD]$ köşegenleri $O$'da kesişsin. Dört üçgene ad ver: $S_1 = A(DOC)$ (üst), $S_2 = A(COB)$ (sağ), $S_3 = A(BOA)$ (alt), $S_4 = A(AOD)$ (sol).

**Örnek 4.** $ABCD$ yamuğunda $[AB] \parallel [DC]$, $S_1 = 4$ ve $S_3 = 9$'dur. $S_2$, $S_4$ ve $A(ABCD)$ kaçtır?

![ABCD yamuğu, köşegenler O'da kesişiyor. Üstteki yeşil DOC üçgeni S1 = 4, alttaki sarı AOB üçgeni S3 = 9, yanlardaki pembe üçgenler S2 = 6 ve S4 = 6.](gorsel/tyt-matematik/25-03-kosegen.svg "Yandaki iki pembe üçgen eşittir. Çapraz çarpım: 4 · 9 = 6 · 6. Bu yamukta |DC| = 4, |AB| = 6, yükseklik 5'tir.")

**Çözüm.**

1. **Yanlar eşit.** $ABD$ ile $ABC$ üçgenlerinin tabanı aynı ($[AB]$), yüksekliği aynı ($h$); alanları eşittir. İkisinden de $S_3$'ü çıkarınca $S_4 = S_2$ kalır.
2. **Çapraz çarpım.** $S_1$ ile $S_4$'ün $D$'den $[AC]$'ye inen yüksekliği ortaktır; tabanları $[OC]$ ve $[OA]$: $\dfrac{S_1}{S_4} = \dfrac{|OC|}{|OA|}$. $S_2$ ile $S_3$'ün de $B$'den $[AC]$'ye inen yüksekliği ortaktır: $\dfrac{S_2}{S_3} = \dfrac{|OC|}{|OA|}$. İki oran eşit: $\dfrac{S_1}{S_4} = \dfrac{S_2}{S_3}$, yani $S_1 \cdot S_3 = S_2 \cdot S_4$.
3. $S_2 = S_4$ olduğu için $S_2^2 = 4 \cdot 9 = 36 \Rightarrow S_2 = S_4 = 6$.
4. $A(ABCD) = 4 + 6 + 9 + 6 = 25$.

**Kural:**

$$S_2 = S_4 \qquad S_2 \cdot S_4 = S_1 \cdot S_3 \qquad A(ABCD) = \left(\sqrt{S_1} + \sqrt{S_3}\right)^2$$

Tabanlarla bağlantı: $DOC$ ile $BOA$ benzer üçgenlerdir, benzerlik oranı $\dfrac{c}{a}$. Bu yüzden $\dfrac{S_1}{S_3} = \dfrac{c^2}{a^2}$ ve $\dfrac{S_1}{S_2} = \dfrac{c}{a}$. Örnekte $c : a = 2 : 3$, $S_1 : S_3 = 4 : 9$, $S_1 : S_2 = 4 : 6$.

> **Tuzak:** Eşit olan **yandaki** iki üçgendir; üst ve alt üçgen eşit değildir. Yan üçgen, $S_1$ ile $S_3$'ün aritmetik ortalaması ($6{,}5$) değil, çarpımının kareköküdür ($6$). Taban oranı $1 : 3$ ise $S_1 : S_3 = 1 : 9$'dur, $1 : 3$ değil.

## 5. Tabandaki bir noktadan çizilen üçgenler

**Örnek 5.** $ABCD$ yamuğunda $[AB] \parallel [DC]$, $|DC| = 5$, yükseklik $4$; $E$ noktası $[AB]$ üzerinde, $|AE| = 4$ ve $|EB| = 7$'dir. $A(AED)$, $A(EBC)$ ve $A(DEC)$ kaçtır?

![ABCD yamuğu, DC = 5, yükseklik 4 kırmızı kesikli. E noktası AB üzerinde, AE = 4, EB = 7. Sarı AED üçgeni 8, mavi DEC üçgeni 10, yeşil EBC üçgeni 14.](gorsel/tyt-matematik/25-03-taban-nokta.svg "Üç üçgenin de yüksekliği 4'tür; alanları tabanlarıyla orantılıdır: 4, 5 ve 7 tabanlara 8, 10 ve 14 alan.")

**Çözüm.** Üç üçgenin de bir köşesi bir tabanda, karşısındaki kenarı öbür tabandadır; yükseklikleri ortaktır ve $h = 4$'tür.

1. $A(AED) = \dfrac{4 \cdot 4}{2} = 8$, $\quad A(EBC) = \dfrac{7 \cdot 4}{2} = 14$, $\quad A(DEC) = \dfrac{5 \cdot 4}{2} = 10$.
2. Kontrol: $8 + 14 + 10 = 32$ ve $\dfrac{11 + 5}{2} \cdot 4 = 32$.

**Kural:** Yükseklikleri ortak olan üçgenlerin alanları tabanlarıyla orantılıdır.

$$A(DEC) = \frac{c \cdot h}{2} \qquad A(AED) + A(EBC) = \frac{a \cdot h}{2}$$

$E$, $[AB]$ üzerinde nereye kayarsa kaysın $A(DEC)$ değişmez. Aynı şekilde $[DC]$ üzerindeki bir $P$ noktası için $A(APB) = \dfrac{a \cdot h}{2}$'dir.

> **Tuzak:** $E$ yer değiştirince $A(AED)$ ile $A(EBC)$ değişir ama toplamları ve $A(DEC)$ sabit kalır. Soru $E$'nin yerini vermiyorsa büyük ihtimalle bunu soruyordur.

## ÖSYM tuzakları

> **Yan kenarı yükseklik almak.** Eğik kenar yükseklikten uzundur. Önce dikme indir, Pisagor ile $h$'yi bul.

> **İkiye bölmeyi unutmak.** $(a + c) \cdot h$ değil, $\dfrac{a + c}{2} \cdot h$. Alan verilip $h$ sorulduğunda da aynı hata yapılır.

> **Orta nokta kuralını yanlış üçgene uygulamak.** Yarı alan, yan kenarın orta noktasını öbür yan kenarın uçlarına bağlayan üçgenindir.

> **Köşegen üçgenlerinde üst = alt sanmak.** Eşit olanlar yanlardır ($S_2 = S_4$). Üst ve alt üçgenden yan üçgen, çarpımın karekökü ile bulunur.

> **Oranı karesiz kullanmak.** $|DC| : |AB| = 1 : 3$ ise $S_1 : S_3 = 1 : 9$, ama $S_1 : S_2 = 1 : 3$.

## Kendini dene

### Soru 1
$ABCD$ ikizkenar yamuğunda $[AB] \parallel [DC]$, $|AB| = 16$ cm, $|DC| = 4$ cm ve $|AD| = |BC| = 10$ cm'dir. Bu yamuğun alanı kaç cm²'dir?

A) 60
B) 80
C) 100
D) 128
E) 160

**Cevap:** B
**Çözüm:** Uçta kalan parça $\dfrac{16 - 4}{2} = 6$. Dik üçgende $h^2 = 10^2 - 6^2 = 64$, $h = 8$. Alan $\dfrac{16 + 4}{2} \cdot 8 = 10 \cdot 8 = 80$. $100$, yan kenarı yükseklik almaktır; $60$, uçtaki $6$'yı yükseklik almaktır; $128$ alt taban ile yüksekliğin çarpımı, $160$ ikiye bölmeyi unutmaktır.

### Soru 2
![ABCD yamuğu, köşegenler O'da kesişiyor. Üstteki yeşil DOC üçgeninin alanı 9, alttaki sarı AOB üçgeninin alanı 25; yan üçgenler boş.](gorsel/tyt-matematik/25-03-kd2.svg "Şekil ölçeklidir.")

Şekildeki $ABCD$ yamuğunda $[AB] \parallel [DC]$ ve köşegenler $O$ noktasında kesişmektedir. $A(DOC) = 9$ birimkare ve $A(AOB) = 25$ birimkare olduğuna göre $A(ABCD)$ kaç birimkaredir?

A) 30
B) 34
C) 49
D) 64
E) 102

**Cevap:** D
**Çözüm:** Yan üçgenler eşittir ve $S_2 \cdot S_4 = 9 \cdot 25 = 225$, yani $S_2 = S_4 = 15$. Toplam $9 + 25 + 15 + 15 = 64$. Kısa yol: $(\sqrt{9} + \sqrt{25})^2 = 8^2 = 64$. $34$ yalnız verilen iki üçgen, $49$ bir yan üçgeni unutmak, $30$ yalnız yan üçgenlerdir; $102$ ise yan üçgenleri $9 + 25 = 34$ sanmaktır.

### Soru 3
![ABCD yamuğu, AB = 12, DC = 8. E, AD'nin orta noktası; mavi EBC üçgeninin alanı 20. C'den AB'ye inen kırmızı kesikli dikme h = ? ile gösterilmiş.](gorsel/tyt-matematik/25-03-kd3.svg "Şekil ölçeklidir.")

Şekildeki $ABCD$ yamuğunda $[AB] \parallel [DC]$, $|AB| = 12$ cm, $|DC| = 8$ cm ve $E$, $[AD]$ kenarının orta noktasıdır. $A(EBC) = 20$ cm² olduğuna göre yamuğun yüksekliği kaç cm'dir?

A) 2
B) 10/3
C) 4
D) 5
E) 8

**Cevap:** C
**Çözüm:** $E$ yan kenarın orta noktası: $A(ABCD) = 2 \cdot 20 = 40$. $\dfrac{12 + 8}{2} \cdot h = 40 \Rightarrow 10h = 40 \Rightarrow h = 4$. $2$, $A(ABCD) = 20$ sanmaktır; $10/3$ ve $5$, orta taban yerine yalnız bir tabanı kullanmaktır ($12h = 40$, $8h = 40$).

## Özet kartı

- $A(ABCD) = \dfrac{a + c}{2} \cdot h$ = orta taban $\cdot$ yükseklik.
- Yükseklik yoksa dikme indir, Pisagor uygula; ikizkenar yamukta uçtaki parça $\dfrac{a - c}{2}$.
- $E$ yan kenarın orta noktası: $A(EBC) = \dfrac{A(ABCD)}{2}$.
- Köşegenler: $S_2 = S_4$, $S_2 \cdot S_4 = S_1 \cdot S_3$, toplam $(\sqrt{S_1} + \sqrt{S_3})^2$.
- $S_1 : S_3 = c^2 : a^2$, $S_1 : S_2 = c : a$.
- $E \in [AB]$ ise $A(DEC) = \dfrac{c \cdot h}{2}$, $E$'nin yerinden bağımsız.

## Sonraki adım

Alıştırmaya geç (aşağıdaki düğme). Sonraki ders: **Paralelkenarda Açı ve Uzunluk**. Paralelkenar, iki çift kenarı paralel olan bir yamuktur; bugünkü alan fikirleri orada da işine yarayacak.
