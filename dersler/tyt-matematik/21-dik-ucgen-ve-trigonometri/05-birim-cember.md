---
baslik: Birim Çember
ders: tyt-matematik
sure: 20 dk
kaynak: MEBİ Konu Özeti b7900d490f
guncelleme: 2026-11-18
---
# Birim Çember

<div class="giris" dir="rtl" lang="ar">

**الدرس ده عن إيه؟** عن دايرة الوحدة (birim çember): دايرة مركزها نقطة الأصل (orijin) ونص قطرها واحد بس.

- هتعرف إن إحداثيات (koordinatlar) أي نقطة عليها بتحقق علاقة فيثاغورس، وإن إشارتها بتتحدد من الربع (bölge) اللي هي فيه.
- هتتعلم إن الإحداثي الأفقي هو جيب التمام (kosinüs) والرأسي هو الجيب (sinüs)، وتطلّع قيم زوايا أكبر من 90 درجة بالتماثل (simetri).
- هتشوف محور الظل (tanjant ekseni) ومحور ظل التمام (kotanjant ekseni) على نفس الرسمة.

**ليه مهم؟** في TYT بييجي سؤال عن نقطة على دايرة الوحدة أو موقف فيه حاجة بتلف، والحل كله إنك تقرا الإحداثيات والإشارات صح.

الدرس ٢٠ دقيقة، ارسم الدايرة معانا وهتلاقي النسب المثلثية بقت قدام عينك.

</div>

**Bu dersin sonunda:** birim çember üzerindeki bir noktanın eksik koordinatını $x^2 + y^2 = 1$ ve bölge işaretiyle bulabilecek, bir açının sinüs, kosinüs, tanjant ve kotanjantını o noktanın koordinatlarından okuyabileceksin.

> **TYT'de yeri:** Birim çember genelde bir trigonometri sorusunun içinde gelir. "Birim çember üzerindeki $K$ noktasının ordinatı ..." diye bir nokta verilir ve bir oran istenir; ya da dönme dolap, saat, döner kol gibi bir dönme hareketinde bir noktanın konumu sorulur. En çok puan kaybettiren yanlış işarettir: 2. bölgede kosinüsü pozitif almak.

## Önce hatırla

<details><summary>Geçen dersten: Hipotenüsü 1 birim olan 30°–60°–90° üçgeninin dik kenarları kaç birimdir?</summary>
Kenarlar 1 : √3 : 2 oranındadır. Hipotenüs 2 yerine 1 olunca hepsi yarıya iner: 30°'nin karşısı <b>1/2</b>, 60°'nin karşısı <b>√3/2</b>. Bugün bu iki sayı, birim çemberdeki 30° ve 60° noktalarının koordinatları olacak.
</details>

<details><summary>Geçen dersten: sin 45° ve tan 60° kaçtır?</summary>
<b>sin 45° = √2/2</b> (karenin yarısı: kenarlar 1 : 1 : √2) ve <b>tan 60° = √3</b> (karşı √3, komşu 1). Bugün tanjantı da çember üzerinde bir uzunluk olarak göreceksin.
</details>

## 1. Birim çember: $x^2 + y^2 = 1$

Merkezi orijin $O(0, 0)$, yarıçapı $1$ birim olan çembere **birim çember** denir. Eksenleri $A(1, 0)$, $B(0, 1)$, $C(-1, 0)$ ve $D(0, -1)$ noktalarında keser.

**Örnek 1.** $K\left(\frac{3}{5}, y\right)$ noktası birim çember üzerinde ve 1. bölgededir. $y$ kaçtır?

![O merkezli birim çember. Eksenleri A(1, 0), B(0, 1), C(−1, 0), D(0, −1) noktalarında kesiyor. Çember üzerindeki K(x, y) noktasından x eksenine KT dikmesi inmiş. OKT dik üçgeninde OT = x yeşil, KT = y kırmızı, OK = 1 mavi.](gorsel/tyt-matematik/21-05-birim-cember.svg "OKT dik üçgeninin hipotenüsü yarıçaptır, yani 1. Yeşil kenar noktanın apsisi, kırmızı kenar ordinatıdır.")

**Çözüm.**

1. $K$'dan $x$ eksenine $[KT]$ dikmesini indir. $OKT$ dik üçgeninde $|OT| = \frac{3}{5}$, $|KT| = y$ ve hipotenüs $|OK| = 1$ (yarıçap).
2. Pisagor: $\left(\frac{3}{5}\right)^2 + y^2 = 1 \Rightarrow y^2 = 1 - \frac{9}{25} = \frac{16}{25}$.
3. 1. bölgede $y$ pozitiftir: $y = \frac{4}{5}$. Nokta $K\left(\frac{3}{5}, \frac{4}{5}\right)$; 3-4-5 üçgeninin $5$'e bölünmüş hâli.

**Kural:** $K(x, y)$ birim çember üzerindeyse

$$x^2 + y^2 = 1 \qquad -1 \le x \le 1 \qquad -1 \le y \le 1$$

Bir noktanın çember üzerinde olup olmadığını da bu eşitlikle denetlersin: $(0{,}6;\ 0{,}7)$ için $0{,}36 + 0{,}49 = 0{,}85 \neq 1$, çember üzerinde değildir.

> **Tuzak:** Kareleri atlamak. $1 - \frac{3}{5} = \frac{2}{5}$ yazmak yanlıştır; eşitlik koordinatların **karelerini** toplar.

## 2. Bölgeler: koordinatların işareti

**Örnek 2.** $P\left(a, -\frac{2\sqrt{2}}{3}\right)$ noktası birim çember üzerinde ve 3. bölgededir. $a$ kaçtır?

**Çözüm.**

1. $a^2 + \left(\frac{2\sqrt{2}}{3}\right)^2 = 1 \Rightarrow a^2 + \frac{8}{9} = 1 \Rightarrow a^2 = \frac{1}{9}$.
2. Karekökten iki değer çıkar: $a = \frac{1}{3}$ ya da $a = -\frac{1}{3}$.
3. 3. bölgede apsis negatiftir: $a = -\frac{1}{3}$.

![Birim çember ve dört bölge. 1. bölgede x artı, y artı; 2. bölgede x eksi, y artı; 3. bölgede x eksi, y eksi; 4. bölgede x artı, y eksi. 3. bölgede kırmızı P noktası; P'den eksenlere kesikli çizgiler.](gorsel/tyt-matematik/21-05-bolgeler.svg "P noktası 3. bölgede: eksenlere inen kesikli çizgilerin ikisi de negatif yöne gider, iki koordinat da negatiftir.")

**Kural:**

| Bölge | $x$ (apsis) | $y$ (ordinat) |
|---|---|---|
| 1. bölge | $+$ | $+$ |
| 2. bölge | $-$ | $+$ |
| 3. bölge | $-$ | $-$ |
| 4. bölge | $+$ | $-$ |

Eksenler üzerindeki $A$, $B$, $C$, $D$ noktaları hiçbir bölgeye ait değildir.

> **Tuzak:** $x^2 + y^2 = 1$ eşitliği işareti söylemez; iki kökten doğrusunu bölge seçer. Seçeneklerde $\frac{1}{3}$ de hazır bekler.

## 3. Açı ve koordinat: $\cos\alpha = x$, $\sin\alpha = y$

**Örnek 3.** $K$ noktası birim çember üzerindedir ve $m(\widehat{AOK}) = 30^\circ$'dir. $K$'nın koordinatları nedir?

![Birim çember. K noktası 30 derecede; OK = 1 mavi, OT yeşil ve cos α ile, KT kırmızı ve sin α ile gösterilmiş. K'nın yanında K(cos α, sin α) yazıyor. x ekseni kosinüs ekseni, y ekseni sinüs ekseni olarak adlandırılmış.](gorsel/tyt-matematik/21-05-sin-cos.svg "Yarıçap 1 olduğu için dik üçgenin yatay kenarı cos α, dikey kenarı sin α olur. α = 30° için K(√3/2, 1/2).")

**Çözüm.**

1. $K$'dan $x$ eksenine dikme indir: $OKT$ dik üçgeninin hipotenüsü $|OK| = 1$, $O$'daki açı $30^\circ$.
2. Karşı kenar: $|KT| = 1 \cdot \sin 30^\circ = \frac{1}{2}$. Komşu kenar: $|OT| = 1 \cdot \cos 30^\circ = \frac{\sqrt{3}}{2}$.
3. $K\left(\frac{\sqrt{3}}{2}, \frac{1}{2}\right)$. Bu, geçen dersteki $1 : \sqrt{3} : 2$ üçgeninin yarıya küçültülmüşüdür.

**Kural:** $A$'dan başlayıp saat yönünün tersine $\alpha$ kadar dönünce gelinen nokta $K(\cos\alpha, \sin\alpha)$'dır. Bu yüzden $x$ eksenine **kosinüs ekseni**, $y$ eksenine **sinüs ekseni** denir.

$$\cos\alpha = x \qquad \sin\alpha = y \qquad \sin^2\alpha + \cos^2\alpha = 1$$

Eksen noktaları, en sık sorulan değerleri verir:

| Açı | Nokta | $\cos$ | $\sin$ |
|---|---|---|---|
| $0^\circ$ | $A(1, 0)$ | $1$ | $0$ |
| $90^\circ$ | $B(0, 1)$ | $0$ | $1$ |
| $180^\circ$ | $C(-1, 0)$ | $-1$ | $0$ |
| $270^\circ$ | $D(0, -1)$ | $0$ | $-1$ |

**Örnek 3b.** $\alpha$ dar açı ve $\sin\alpha = \frac{15}{17}$ ise $\cos\alpha$ kaçtır?

$\cos^2\alpha = 1 - \frac{225}{289} = \frac{64}{289}$. Dar açının noktası 1. bölgededir, kosinüs pozitif: $\cos\alpha = \frac{8}{17}$.

> **Tuzak:** Sinüs ile kosinüsü karıştırmak. Nokta $(\cos\alpha, \sin\alpha)$ diye yazılır: önce yatay (kosinüs), sonra dikey (sinüs). Bir de: $\sin\alpha$ ve $\cos\alpha$ hiçbir zaman $1$'den büyük olamaz; "$\sin\alpha = \frac{4}{3}$" diyen seçeneği hemen ele.

## 4. 90°'den büyük açılar: simetri

**Örnek 4.** $L$ noktası birim çember üzerindedir ve $m(\widehat{AOL}) = 150^\circ$'dir. $\sin 150^\circ$ ve $\cos 150^\circ$ kaçtır?

![Birim çember üzerinde dört nokta: K(√3/2, 1/2) 30 derecede, L(−√3/2, 1/2) 150 derecede, M(−√3/2, −1/2) ve N(√3/2, −1/2). Dört nokta kesikli bir dikdörtgenin köşeleri.](gorsel/tyt-matematik/21-05-simetri.svg "Dört nokta aynı dikdörtgenin köşeleridir: sayılar hep √3/2 ve 1/2, değişen yalnızca işarettir. L, K'nın y eksenine göre simetriğidir.")

**Çözüm.**

1. $150^\circ = 180^\circ - 30^\circ$. $L$ 2. bölgededir ve $x$ ekseninin negatif yönüyle $30^\circ$ yapar: $m(\widehat{COL}) = 30^\circ$.
2. Bu yüzden $L$, Örnek 3'teki $K\left(\frac{\sqrt{3}}{2}, \frac{1}{2}\right)$ noktasının $y$ eksenine göre simetriğidir: yüksekliği aynı, yatayda sol tarafta.
3. $L\left(-\frac{\sqrt{3}}{2}, \frac{1}{2}\right)$, yani $\cos 150^\circ = -\frac{\sqrt{3}}{2}$ ve $\sin 150^\circ = \frac{1}{2}$.

**Kural:** Simetri sayıyı değiştirmez, işareti değiştirir.

- $y$ eksenine göre: $(x, y) \to (-x, y)$. Buradan $\sin(180^\circ - \alpha) = \sin\alpha$ ve $\cos(180^\circ - \alpha) = -\cos\alpha$.
- $x$ eksenine göre: $(x, y) \to (x, -y)$. Şekilde $K$ ile $N$ ($330^\circ$).
- Orijine göre: $(x, y) \to (-x, -y)$. Şekilde $K$ ile $M$ ($210^\circ$).

Kısa yol: noktanın $x$ ekseniyle yaptığı dar açıyı bul ($150^\circ$ için $30^\circ$), sayıları o dar açıdan al, işareti bölgeden koy.

> **Tuzak:** $\cos 150^\circ = \frac{\sqrt{3}}{2}$ yazmak. 2. bölgede apsis negatiftir; sinüs aynı kalır, kosinüs eksi olur.

## 5. Tanjant ve kotanjant eksenleri

**Örnek 5.** $m(\widehat{AOK}) = 60^\circ$ olacak biçimde birim çember üzerinde bir $K$ noktası alınıyor. $[OK$ ışını $x = 1$ doğrusunu $N$ noktasında, $y = 1$ doğrusunu $R$ noktasında kesiyor. $N$ ve $R$'nin koordinatları nedir?

![Birim çember, x = 1 doğrusu (tanjant ekseni, mavi) ve y = 1 doğrusu (kotanjant ekseni, yeşil). O'dan 60 derecelik ışın çemberi K'de, y = 1 doğrusunu R'de, x = 1 doğrusunu N(1, √3)'te kesiyor. AN kırmızı ve tan α ile, BR kırmızı ve cot α ile gösterilmiş; A'da ve B'de dik açı.](gorsel/tyt-matematik/21-05-tanjant.svg "Kırmızı dikey parça AN tanjanttır, kırmızı yatay parça BR kotanjanttır. K'nın ordinatı (sinüs) ile N'nin ordinatı (tanjant) farklı uzunluklardır.")

**Çözüm.**

1. $K(\cos 60^\circ, \sin 60^\circ) = \left(\frac{1}{2}, \frac{\sqrt{3}}{2}\right)$.
2. $OAN$ dik üçgeni $A$'da diktir, $|OA| = 1$: $\tan 60^\circ = \frac{|AN|}{1} \Rightarrow |AN| = \sqrt{3}$. Yani $N(1, \sqrt{3})$.
3. $OBR$ dik üçgeni $B$'de diktir, $|OB| = 1$, $m(\widehat{BOR}) = 90^\circ - 60^\circ = 30^\circ$: $|BR| = \tan 30^\circ = \frac{\sqrt{3}}{3}$. Yani $R\left(\frac{\sqrt{3}}{3}, 1\right)$ ve bu sayı $\cot 60^\circ$'dir.
4. Kontrol: $\frac{y}{x} = \frac{\sqrt{3}/2}{1/2} = \sqrt{3} = \tan 60^\circ$. Tutuyor.

**Kural:**

$$\tan\alpha = \frac{\sin\alpha}{\cos\alpha} = \frac{y}{x} \qquad \cot\alpha = \frac{\cos\alpha}{\sin\alpha} = \frac{x}{y} \qquad \tan\alpha \cdot \cot\alpha = 1$$

$x = 1$ doğrusu **tanjant ekseni**dir: $[OK$ ışını onu $N(1, \tan\alpha)$'da keser. $y = 1$ doğrusu **kotanjant ekseni**dir: $[OK$ ışını onu $R(\cot\alpha, 1)$'de keser. $\alpha = 90^\circ$ olunca ışın $x = 1$'e paraleldir, kesişme yoktur: $\tan 90^\circ$ tanımsızdır.

> **Tuzak:** Tanjantı $K$'nın ordinatı sanmak. $K$'nın ordinatı $\sin 60^\circ = \frac{\sqrt{3}}{2}$; tanjant, ışının $x = 1$ doğrusundaki yüksekliğidir: $\sqrt{3}$.

## ÖSYM tuzakları

> **Kareyi atlamak.** $x^2 + y^2 = 1$ yerine $x + y = 1$ gibi düşünüp $1 - \frac{3}{5}$ hesaplamak. Önce kareler, sonra karekök.

> **İşareti bölgeye bakmadan koymak.** 2. bölgede kosinüs, 4. bölgede sinüs, 3. bölgede ikisi de negatiftir. Karekökten çıkan iki değerden doğrusunu bölge seçer.

> **Sinüs ile kosinüsü yer değiştirmek.** $K(\cos\alpha, \sin\alpha)$: apsis kosinüs, ordinat sinüs. Bir noktanın $y$ eksenine uzaklığı $|x|$, $x$ eksenine uzaklığı $|y|$'dir.

> **Açıyı yanlış yerden ölçmek.** Açı $A$'dan, saat yönünün tersine ölçülür. Şekilde açı $C$ tarafından verilmişse ($m(\widehat{COK}) = 60^\circ$ gibi), $m(\widehat{AOK}) = 180^\circ - 60^\circ = 120^\circ$'dir.

> **Tanjantı çember üzerinde aramak.** $\tan\alpha$, $x = 1$ doğrusundaki $|AN|$ uzunluğudur ve $1$'den büyük olabilir; $\sin\alpha$ ve $\cos\alpha$ olamaz.

## Kendini dene

### Soru 1
Birim çember üzerindeki $P\left(-\frac{\sqrt{5}}{3}, b\right)$ noktası 3. bölgededir. Buna göre $b$ kaçtır?

A) $-\frac{\sqrt{5}}{3}$
B) $-\frac{2}{3}$
C) $-\frac{4}{9}$
D) $\frac{4}{9}$
E) $\frac{2}{3}$

**Cevap:** B
**Çözüm:** $b^2 = 1 - \frac{5}{9} = \frac{4}{9}$, yani $b = \pm\frac{2}{3}$. 3. bölgede ordinat negatiftir: $b = -\frac{2}{3}$. C, karekök almayı unutmaktır; E işaret hatasıdır; A, apsisi kopyalamaktır.

### Soru 2
![O merkezli birim çember. K noktası 2. bölgede; A'dan K'ye 135 derecelik açı yayı.](gorsel/tyt-matematik/21-05-kd2.svg "Açı A'dan saat yönünün tersine ölçülmüştür.")

Şekilde $O$ merkezli birim çember üzerindeki $K$ noktası için $m(\widehat{AOK}) = 135^\circ$'dir. Buna göre $K$ noktasının koordinatları nedir?

A) $\left(-\frac{\sqrt{2}}{2}, \frac{\sqrt{2}}{2}\right)$
B) $\left(-\frac{\sqrt{2}}{2}, -\frac{\sqrt{2}}{2}\right)$
C) $\left(-\frac{\sqrt{3}}{2}, \frac{1}{2}\right)$
D) $\left(\frac{\sqrt{2}}{2}, -\frac{\sqrt{2}}{2}\right)$
E) $\left(\frac{\sqrt{2}}{2}, \frac{\sqrt{2}}{2}\right)$

**Cevap:** A
**Çözüm:** $135^\circ = 180^\circ - 45^\circ$. $45^\circ$ noktası $\left(\frac{\sqrt{2}}{2}, \frac{\sqrt{2}}{2}\right)$'dir; $y$ eksenine göre simetriği $\left(-\frac{\sqrt{2}}{2}, \frac{\sqrt{2}}{2}\right)$. E, $45^\circ$ noktasıdır (işaret unutulmuş); B orijine göre, D $x$ eksenine göre simetriktir; C ise $150^\circ$ noktasıdır.

### Soru 3
![O merkezli birim çember ve x = 1 doğrusu. O'dan çıkan ışın çemberi K'de, x = 1 doğrusunu N(1, 12/5)'te kesiyor; A'da dik açı, O'da α açısı.](gorsel/tyt-matematik/21-05-kd3.svg "x = 1 doğrusu tanjant eksenidir.")

Şekilde $O$ merkezli birim çember ve $x = 1$ doğrusu verilmiştir. $O$'dan çıkan ışın çemberi $K$ noktasında, $x = 1$ doğrusunu $N\left(1, \frac{12}{5}\right)$ noktasında kesiyor. $m(\widehat{AOK}) = \alpha$ olduğuna göre $\sin\alpha$ kaçtır?

A) $\frac{5}{13}$
B) $\frac{12}{17}$
C) $\frac{144}{169}$
D) $\frac{12}{13}$
E) $\frac{12}{5}$

**Cevap:** D
**Çözüm:** $N$ tanjant ekseninde: $\tan\alpha = \frac{12}{5}$. $OAN$ dik üçgeninde dik kenarlar $1$ ve $\frac{12}{5}$, hipotenüs $|ON| = \sqrt{1 + \frac{144}{25}} = \frac{13}{5}$ (5-12-13 üçgeninin $5$'e bölünmüşü). $\sin\alpha = \frac{12/5}{13/5} = \frac{12}{13}$, $K\left(\frac{5}{13}, \frac{12}{13}\right)$. Kontrol: $\frac{25}{169} + \frac{144}{169} = 1$. E, tanjantın kendisidir; A kosinüstür; C, karesidir.

## Özet kartı

- Birim çember: merkez $O(0, 0)$, yarıçap $1$; üzerindeki her nokta için $x^2 + y^2 = 1$.
- İşaretler: 1. bölge $(+, +)$, 2. $(-, +)$, 3. $(-, -)$, 4. $(+, -)$. İki kökten doğrusunu bölge seçer.
- $K(\cos\alpha, \sin\alpha)$: apsis kosinüs, ordinat sinüs; $\sin^2\alpha + \cos^2\alpha = 1$; ikisi de $-1$ ile $1$ arasındadır.
- Eksen noktaları: $0^\circ \to (1, 0)$, $90^\circ \to (0, 1)$, $180^\circ \to (-1, 0)$, $270^\circ \to (0, -1)$.
- Simetri işareti değiştirir: $\sin(180^\circ - \alpha) = \sin\alpha$, $\cos(180^\circ - \alpha) = -\cos\alpha$.
- $\tan\alpha = \frac{y}{x}$, ışın $x = 1$'i $N(1, \tan\alpha)$'da keser; $\cot\alpha = \frac{x}{y}$, $y = 1$'i $R(\cot\alpha, 1)$'de keser.

## Sonraki adım

Alıştırmaya geç (aşağıdaki düğme). Bu dersle **Dik Üçgen ve Trigonometri** konusu bitti. Sonraki konu: **Üçgenin Alanı**. Orada dar, dik ve geniş açılı üçgenlerin alanını taban ve yükseklikle bulacaksın; bu bölümde dikme indirme alışkanlığın orada da işine yarayacak.
