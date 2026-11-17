---
baslik: Dik Üçgende Öklid Teoremi
ders: tyt-matematik
sure: 20 dk
kaynak: MEBİ Konu Özeti 3f6ca2625c
guncelleme: 2026-11-18
---
# Dik Üçgende Öklid Teoremi

<div class="giris" dir="rtl" lang="ar">

**الدرس ده عن إيه؟** عن نظرية إقليدس (Öklid teoremi) في المثلث القائم (dik üçgen): لما ننزّل عمود من الزاوية القائمة على الوتر (hipotenüs)، بيطلع علاقات حلوة بين الأطوال.

- هتعرف إن مربع الارتفاع (yükseklik) بيساوي حاصل ضرب الجزأين اللي اتقسم لهم الوتر.
- هتتعلم إن مربع كل ضلع قائم (dik kenar) بيساوي الجزء اللي في ناحيته مضروب في الوتر كله.
- هتحسب الارتفاع من المساحة بطريقتين، وتعرف تختار العلاقة الصح حسب المعطيات وتتأكد بفيثاغورس (Pisagor).

**ليه مهم؟** شكل العمود النازل على الوتر بييجي كتير في أسئلة الهندسة في TYT، والعلاقات دي بتختصر الحل جامد.

الدرس ٢٠ دقيقة بس، خد ورقة وقلم وارسم الشكل معانا وهتلاقيه سهل.

</div>

**Bu dersin sonunda:** dik açıdan hipotenüse dikme inen bir üçgende $h^2 = p \cdot k$, $c^2 = p \cdot a$ ve $h = \dfrac{b \cdot c}{a}$ bağıntılarından doğru olanı seçip eksik uzunluğu bulabileceksin.

> **TYT'de yeri:** Geometri bölümünde "dik üçgende dikme" şekli çok sık çıkar. Soru genelde hipotenüs üzerindeki iki parçayı ya da bir dik kenarı verir, yüksekliği, başka bir kenarı veya alanı ister. Öklid bağıntıları bu soruları Pisagor'dan daha kısa çözer; çoğu zaman ikisi birlikte kullanılır.

## Önce hatırla

<details><summary>Geçen dersten: Dik kenarları 9 cm ve 12 cm olan dik üçgenin hipotenüsü kaç cm'dir?</summary>
$9^2 + 12^2 = 81 + 144 = 225$, hipotenüs <b>15 cm</b>. Kısa yol: 9-12-15 üçgeni, 3-4-5 üçgeninin 3 katıdır. Bugün Pisagor'u her sorunun sonunda kontrol için kullanacaksın.
</details>

<details><summary>Geçen dersten: Bir dik üçgende hipotenüs 26, dik kenarlardan biri 10'dur. Öbür dik kenar kaçtır?</summary>
$26^2 - 10^2 = 676 - 100 = 576$, öbür dik kenar <b>24</b>. Kısa yol: 5-12-13 üçgeninin 2 katı (10-24-26).
</details>

## Şekli tanı: harfler

Öklid teoremi tek bir şekil için yazılır: $ABC$ üçgeninde **A köşesi diktir** ve $A$'dan hipotenüs $[BC]$'ye bir dikme ($[AH]$) iner.

![A'da dik açılı ABC üçgeni. A'dan BC'ye kırmızı AH dikmesi iniyor. AB kenarı c, AC kenarı b, AH yüksekliği h, BH parçası p, HC parçası k, BC hipotenüsü a ile gösterilmiş. AB ve BH mavi, AC ve HC yeşil.](gorsel/tyt-matematik/21-02-adlar.svg "Renklere bak: c kenarı ile p parçası aynı taraftadır (mavi), b kenarı ile k parçası aynı taraftadır (yeşil). Bu eşleşme ikinci kuralın anahtarıdır.")

| Harf | Uzunluk | Ne |
|---|---|---|
| $a$ | $\lvert BC \rvert$ | hipotenüs, $a = p + k$ |
| $b$, $c$ | $\lvert AC \rvert$, $\lvert AB \rvert$ | dik kenarlar |
| $h$ | $\lvert AH \rvert$ | hipotenüse ait yükseklik |
| $p$, $k$ | $\lvert BH \rvert$, $\lvert HC \rvert$ | hipotenüs üzerindeki parçalar |

$p$ parçası, $[AB]$ kenarının $[BC]$ üzerindeki **dik izdüşümüdür**; $k$ de $[AC]$'nin izdüşümü. Sorular bazen "izdüşüm" kelimesini kullanır.

## 1. Yükseklik bağıntısı: $h^2 = p \cdot k$

**Örnek 1.** $A$'sı dik $ABC$ üçgeninde $[AH] \perp [BC]$, $|BH| = 4$ ve $|HC| = 9$. $|AH|$ kaçtır?

**Çözüm.**

1. Yükseklik, iki parçanın ortasında durur: $h^2 = p \cdot k = 4 \cdot 9 = 36$.
2. $h = 6$.
3. Kontrol: $ABH$ üçgeninde $|AB|^2 = 4^2 + 6^2 = 52$; $AHC$ üçgeninde $|AC|^2 = 9^2 + 6^2 = 117$. Büyük üçgende $52 + 117 = 169 = 13^2$ ve $|BC| = 4 + 9 = 13$. Tutuyor.

![A'da dik açılı ABC üçgeni; AH = 6 kırmızı dikme. Soldaki ABH üçgeni yeşil, sağdaki AHC üçgeni sarı boyalı. BH = 4, HC = 9.](gorsel/tyt-matematik/21-02-yukseklik.svg "Yeşil ve sarı üçgenin açıları aynıdır, biri öbürünün büyütülmüşüdür. Yeşilde kısa kenar 4, uzun 6; sarıda kısa kenar 6, uzun 9. Oran aynı: 4/6 = 6/9.")

**Neden?** $m(\widehat{B}) = \beta$ olsun. $ABH$ üçgeninde $m(\widehat{BAH}) = 90^\circ - \beta$, bu yüzden $m(\widehat{HAC}) = \beta$. İki küçük üçgenin açıları aynıdır ($\beta$, $90^\circ - \beta$, $90^\circ$), yani biri öbürünün büyütülmüşüdür. Kenarlar aynı oranda büyür:

$$\frac{|BH|}{|AH|} = \frac{|AH|}{|HC|} \;\Rightarrow\; |AH|^2 = |BH| \cdot |HC|$$

**Kural:**

$$h^2 = p \cdot k$$

> **Tuzak:** $h = p \cdot k$ değil, $h^{\mathbf{2}} = p \cdot k$. Örnekte $36$ seçeneklerde hazır bekler. $h$ ne $\frac{p + k}{2}$'dir ne de $k - p$.

## 2. Dik kenar bağıntısı: $c^2 = p \cdot a$, $b^2 = k \cdot a$

**Örnek 2.** $A$'sı dik $ABC$ üçgeninde $[AH] \perp [BC]$, $|BH| = 9$ ve $|BC| = 25$. $|AB|$ ve $|AC|$ kaçtır?

**Çözüm.**

1. $[AB]$ kenarı $B$ tarafındadır; aynı taraftaki parça $|BH| = 9$. Bütün hipotenüs $25$.
2. $|AB|^2 = |BH| \cdot |BC| = 9 \cdot 25 = 225 \Rightarrow |AB| = 15$.
3. Öbür parça $|HC| = 25 - 9 = 16$. $|AC|^2 = |HC| \cdot |BC| = 16 \cdot 25 = 400 \Rightarrow |AC| = 20$.
4. Kontrol: $15^2 + 20^2 = 225 + 400 = 625 = 25^2$. (Bu, 3-4-5 üçgeninin 5 katıdır.)

![A'da dik açılı ABC üçgeni. AB = 15 ve BH = 9 mavi, AC ve HC yeşil, BC = 25 alttaki ölçü çizgisiyle gösterilmiş.](gorsel/tyt-matematik/21-02-dik-kenar.svg "Mavi kenar (AB = 15) ile mavi parça (BH = 9) aynı köşeden, B'den çıkar. Formül: 15² = 9 · 25.")

**Kural:** Bir dik kenarın karesi, **kendi tarafındaki** parça ile bütün hipotenüsün çarpımıdır.

$$c^2 = p \cdot a \qquad b^2 = k \cdot a$$

İki eşitliği taraf tarafa bölersen kullanışlı bir sonuç çıkar: $\dfrac{c^2}{b^2} = \dfrac{p}{k}$. Örnekte $\dfrac{15^2}{20^2} = \dfrac{9}{16}$. Dik kenarların oranı $3 : 4$ ise parçaların oranı $9 : 16$'dır.

> **Tuzak:** İki yanlış çok sık yapılır. (1) Karşı taraftaki parçayı almak: $|AB|^2 = 16 \cdot 25$ değil. (2) Bütün hipotenüs yerine öbür parçayı almak: $|AB|^2 = 9 \cdot 16$ yazarsan $h^2$'yi bulursun, $|AB|^2$'yi değil.

## 3. Alan bağıntısı: $h = \dfrac{b \cdot c}{a}$

**Örnek 3.** Dik kenarları $|AB| = 6$ ve $|AC| = 8$ olan $ABC$ üçgeninde $[AH] \perp [BC]$. $|AH|$ kaçtır?

**Çözüm.**

1. Pisagor: $|BC|^2 = 6^2 + 8^2 = 100 \Rightarrow |BC| = 10$.
2. Alanı iki yoldan yaz. Dik kenarlarla: $\dfrac{6 \cdot 8}{2} = 24$. Hipotenüs ve yükseklikle: $\dfrac{10 \cdot h}{2}$.
3. $\dfrac{10 \cdot h}{2} = 24 \Rightarrow h = \dfrac{48}{10} = 4{,}8$.
4. İstersen parçaları da bul: $p = \dfrac{6^2}{10} = 3{,}6$, $k = \dfrac{8^2}{10} = 6{,}4$. Kontrol: $3{,}6 \cdot 6{,}4 = 23{,}04 = 4{,}8^2$.

![A'da dik açılı ABC üçgeni: AB = 6, AC = 8, BC = 10, AH = 4,8 kırmızı dikme.](gorsel/tyt-matematik/21-02-alan.svg "Aynı üçgenin alanı iki yoldan: dik kenarlarla 6 · 8 / 2 ve hipotenüsle 10 · 4,8 / 2. İkisi de 24.")

**Kural:**

$$b \cdot c = a \cdot h \qquad\Rightarrow\qquad h = \frac{b \cdot c}{a}$$

> **Tuzak:** $h$ bulunurken alanı ikiye bölmek iki tarafta da yapılır, birbirini götürür. Ama soru **alanı** soruyorsa $\dfrac{b \cdot c}{2}$ yazmayı unutma; $48$ değil $24$.

## Hangi bağıntıyı ne zaman?

![Karar şeması: dik açıdan hipotenüse dikme varsa soruda h, p, k geçiyorsa h kare eşittir p çarpı k; dik kenar ve parça geçiyorsa c kare eşittir p çarpı a; iki dik kenar verilmişse önce Pisagor ile a, sonra h eşittir b çarpı c bölü a. Hepsinin sonunda Pisagorla kontrol.](gorsel/tyt-matematik/21-02-hangi-baginti.svg "Soruda verilen üç uzunluğa bak, onları birbirine bağlayan bağıntıyı seç. Sonuçta Pisagor her zaman tutmalıdır.")

Öklid bağıntıları Pisagor'u kısaltır, onun yerini almaz. Bilinen iki uzunluk aynı küçük üçgendeyse ($ABH$ ya da $AHC$) Pisagor da tek adımda sonuç verir.

> **Öklid kimdir?** MÖ 300 dolaylarında yaşamış bir matematikçidir. Kendinden önce bilinen geometriyi *Elemanlar* (Ögeler) adlı kitapta toplamış, her şeyi beş temel kabulden (aksiyomdan) türetmiştir. Örneğin "İki noktadan bir ve yalnız bir doğru geçer." ve "Bütün dik açılar eşittir." bu kabullerdendir.

## ÖSYM tuzakları

> **Kareyi unutmak.** $|BH| = 4$, $|HC| = 9$ için $|AH| = 36$ yazmak. Doğrusu $|AH|^2 = 36$, $|AH| = 6$.

> **Parçayı yanlış kenarla eşlemek.** $c$ kenarı $B$'den, $p$ parçası da $B$'den çıkar. $|AB|^2 = |HC| \cdot |BC|$ yanlıştır.

> **Hipotenüs yerine parça.** $c^2 = p \cdot a$ formülünde $a$ **bütün** hipotenüstür ($p + k$), öbür parça değildir.

> **Oranı karesiz kullanmak.** Dik kenarlar $2 : 3$ ise parçalar $2 : 3$ değil, $4 : 9$ oranındadır. Tersten de geçerli: parçalar $1 : 4$ ise dik kenarlar $1 : 2$'dir.

> **Hangi parça küçük?** Kısa dik kenarın tarafındaki parça da kısadır. Soru "$|BH| < |HC|$" diyorsa denklemin iki kökünden doğrusunu buna göre seç.

## Kendini dene

### Soru 1
![A'da dik açılı ABC üçgeni. AH dikmesi soru işaretiyle gösterilmiş; BH = 5, HC = 20.](gorsel/tyt-matematik/21-02-kd1.svg "Şekil ölçeklidir.")

Şekilde $[AB] \perp [AC]$, $[AH] \perp [BC]$, $|BH| = 5$ ve $|HC| = 20$ birimdir. Buna göre $|AH|$ kaç birimdir?

A) 10
B) 25/2
C) 15
D) 25
E) 100

**Cevap:** A
**Çözüm:** $|AH|^2 = |BH| \cdot |HC| = 5 \cdot 20 = 100 \Rightarrow |AH| = 10$. $100$, karekök almayı unutmaktır; $25/2$ iki parçanın ortalaması, $15$ farkı, $25$ toplamıdır.

### Soru 2
![A'da dik açılı ABC üçgeni. AB = 12, BC = 16; BH parçası soru işaretiyle gösterilmiş.](gorsel/tyt-matematik/21-02-kd2.svg "Şekil ölçeklidir.")

Şekilde $[AB] \perp [AC]$, $[AH] \perp [BC]$, $|AB| = 12$ ve $|BC| = 16$ birimdir. Buna göre $|BH|$ kaç birimdir?

A) 7
B) 9
C) $4\sqrt{7}$
D) 12
E) 16

**Cevap:** B
**Çözüm:** $[AB]$ kenarı ile $[BH]$ parçası aynı taraftadır: $|AB|^2 = |BH| \cdot |BC| \Rightarrow 144 = |BH| \cdot 16 \Rightarrow |BH| = 9$. $7$, öbür parça $|HC|$'dir; $4\sqrt{7}$ ise $|AC|$'dir ($|AC|^2 = 7 \cdot 16 = 112$). Kontrol: $12^2 + 112 = 256 = 16^2$.

### Soru 3
Dik kenarlarının uzunlukları $9$ cm ve $12$ cm olan bir dik üçgende, hipotenüse ait yükseklik kaç cm'dir?

A) 27/5
B) 6
C) 36/5
D) 15/2
E) 54

**Cevap:** C
**Çözüm:** Hipotenüs: $\sqrt{9^2 + 12^2} = 15$. $h = \dfrac{9 \cdot 12}{15} = \dfrac{108}{15} = \dfrac{36}{5} = 7{,}2$. $54$ üçgenin alanıdır; $15/2$ hipotenüsün yarısıdır; $27/5$ ise kısa kenarın tarafındaki parçadır ($81/15$).

## Özet kartı

- Şekil: $A$ dik, $[AH] \perp [BC]$; $p = |BH|$, $k = |HC|$, $a = p + k$.
- Yükseklik: $h^2 = p \cdot k$.
- Dik kenar: $c^2 = p \cdot a$, $b^2 = k \cdot a$ (kenar ve parça aynı taraftan).
- Alan: $b \cdot c = a \cdot h$, yani $h = \dfrac{b \cdot c}{a}$.
- Oran: $\dfrac{c^2}{b^2} = \dfrac{p}{k}$; dik kenar oranının karesi parça oranını verir.
- Her sonucu Pisagor ile kontrol et.

## Sonraki adım

Alıştırmaya geç (aşağıdaki düğme). Sonraki ders: **Trigonometrik Oranlar**. Orada dik üçgendeki kenar oranlarına sinüs, kosinüs ve tanjant adları verilecek; bugünkü iki küçük üçgenin "aynı açılı" olması orada da işine yarayacak.
