---
baslik: Birinci Dereceden İki Bilinmeyenli Eşitsizlik Sistemleri
ders: tyt-matematik
sure: 20 dk
kaynak: MEBİ Konu Özeti a0a558963f
guncelleme: 2026-11-18
---
# Birinci Dereceden İki Bilinmeyenli Eşitsizlik Sistemleri

<div class="giris" dir="rtl" lang="ar">

**الدرس ده عن إيه؟** عن أنظمة المتباينات (eşitsizlik sistemi): لما يبقى عندك متباينتين أو أكتر في x و y مع بعض، والحل هو المنطقة المشتركة بينهم على المستوى الإحداثي.

- هتعرف ترسم كل متباينة لوحدها، الخط متصل ولا متقطع، وتلوّن الجهة الصح وبعدين تاخد الجزء المشترك (kesişim).
- هتفهم إمتى الخطين يبقوا متوازيين، والحل يطلع شريط بينهم أو مجموعة خالية (boş küme).
- هتتعلم تعدّ النقط اللي إحداثياتها أعداد صحيحة (tam sayı) جوه المنطقة، وتقرا من الرسمة النظام اللي المنطقة بتمثّله.

**ليه مهم؟** في TYT السؤال بييجي كده: المنطقة المتلوّنة دي حل أنهي نظام؟ أو فيه كام نقطة صحيحة جواها؟ وغلط كتير بيحصل في نقطة الركن (köşe) اللي على خط متقطع.

الدرس ٢٠ دقيقة بس، خد ورقة وقلم وارسم معانا، هتلاقيه أسهل ما انت متخيّل.

</div>

**Bu dersin sonunda:** iki ya da daha fazla eşitsizliğin ortak çözüm bölgesini analitik düzlemde çizebilecek, boyalı bir bölgenin hangi sistemi gösterdiğini okuyabilecek ve bölgedeki tam sayı noktalarını sayabileceksin.

> **TYT'de yeri:** Sorular üç kalıpta gelir: "Grafikte boyalı bölge hangi sistemin çözüm kümesidir?", "Hangi nokta sistemi sağlar?" ve "Bölgede kaç tane $(x, y)$ tam sayı ikilisi vardır?". Günlük hayat sorularında bütçe ve adet koşulları bir sisteme dönüşür.

## Önce hatırla

<details><summary>Önceki dersten: $3x - 2y > 4$ eşitsizliğinin grafiğinde sınır doğrusu düz mü, kesikli mi çizilir? $(2, 1)$ noktası çözüm kümesinde midir?</summary>
Eşitlik yok ($>$), bu yüzden doğru <b>kesikli</b> çizilir. $(2, 1)$ için $3 \cdot 2 - 2 \cdot 1 = 4$ ve $4 > 4$ yanlıştır: nokta çözümde <b>değildir</b>. Bu nokta tam kesikli doğrunun üzerindedir.
</details>

<details><summary>Önceki dersten: $2x + y \le 6$ eşitsizliğinde doğrunun hangi tarafı boyanır?</summary>
Orijini dene: $2 \cdot 0 + 0 \le 6$ doğru. Orijinin bulunduğu taraf, yani doğrunun <b>alt</b> tarafı boyanır ($y \le -2x + 6$). Doğru da çözüme dahildir, düz çizilir.
</details>

## Sistem nedir?

**Örnek.** Sistem: $x + y \le 5$ ve $x - y > 1$. Aşağıdaki noktalardan hangileri sistemin çözümüdür?

| Nokta | $x + y \le 5$ | $x - y > 1$ | Sistemin çözümü mü? |
|---|---|---|---|
| $(4, 1)$ | $5 \le 5$ ✓ | $3 > 1$ ✓ | Evet |
| $(2, 1)$ | $3 \le 5$ ✓ | $1 > 1$ ✗ | Hayır |
| $(5, -1)$ | $4 \le 5$ ✓ | $6 > 1$ ✓ | Evet |
| $(3, 3)$ | $6 \le 5$ ✗ | $0 > 1$ ✗ | Hayır |

$(2, 1)$ birinci eşitsizliği sağlıyor ama yetmez; nokta **her** eşitsizliği sağlamalı.

**Kural.** En az iki tane birinci dereceden iki bilinmeyenli eşitsizlik birlikte yazılınca **eşitsizlik sistemi** olur. Sistemin çözüm kümesi, eşitsizliklerin çözüm kümelerinin **kesişimidir**. Düzlemde bu, boyalı bölgelerin **ortak** kısmıdır.

## Ortak bölgeyi çizmek

**Örnek.** $2x + y \le 6$ ve $x - y < 3$ sisteminin çözüm bölgesini çiz.

1. **Birinci eşitsizlik.** $2x + y = 6$ doğrusu: $x = 0$ ise $y = 6$, $y = 0$ ise $x = 3$. Doğru $(0, 6)$ ve $(3, 0)$ noktalarından geçer; $\le$ olduğu için **düz**. Orijin: $0 \le 6$ doğru, orijinin tarafı boyanır (mavi).
2. **İkinci eşitsizlik.** $x - y = 3$ doğrusu: $(0, -3)$ ve $(3, 0)$ noktalarından geçer; $<$ olduğu için **kesikli**. Orijin: $0 < 3$ doğru, orijinin tarafı boyanır (sarı).
3. **Ortak kısım.** İki boyanın üst üste geldiği bölge sistemin çözümüdür (yeşil).

![Koordinat düzleminde iki doğru: (0, 6) ve (3, 0) noktalarından geçen düz mavi doğru ile (0, −3) ve (3, 0) noktalarından geçen kesikli sarı doğru. Mavi doğrunun solu açık mavi, sarı doğrunun üstü açık sarı; ikisinin üst üste geldiği sol bölge yeşil. İki doğrunun kesiştiği (3, 0) noktası içi boş.](gorsel/tyt-matematik/03-06-kesisim.svg "Yeşil bölge iki koşulu birden sağlar. (3, 0) köşesi kesikli doğrunun üzerinde olduğu için çözüme dahil değildir.")

İki doğru $(3, 0)$ noktasında kesişir. Bu köşe $2x + y \le 6$ koşulunu sağlar ($6 \le 6$) ama $x - y < 3$ koşulunu sağlamaz ($3 < 3$ yanlış). Köşe, **kesikli** doğruya ait olduğu için dahil değildir.

**Kural.** Her eşitsizliği ayrı ayrı çiz: sınır doğrusu (düz ya da kesikli) + doğru tarafı (orijinle dene). Sonra yalnızca ortak kısmı bırak. Köşe noktası, ancak iki doğru da düzse dahildir.

> Doğru orijinden geçiyorsa orijinle deneme yapılamaz. O zaman $(1, 0)$ ya da $(0, 1)$ gibi doğrunun üzerinde olmayan bir nokta dene.

## Paralel doğrular: şerit ya da boş küme

**Örnek.** $2x - y \ge -2$ ve $2x - y < 4$ sisteminin çözüm bölgesini çiz.

İki eşitsizliğin sol tarafı aynı: $2x - y$. Demek ki sınır doğruları **paraleldir**. Sistem aslında tek satırda yazılabilir:

$$-2 \le 2x - y < 4$$

- $2x - y = -2$: $(-1, 0)$ ve $(0, 2)$ noktalarından geçer, **düz**.
- $2x - y = 4$: $(2, 0)$ ve $(0, -4)$ noktalarından geçer, **kesikli**.
- Orijin: $-2 \le 0 < 4$ doğru. Çözüm, iki doğrunun **arasındaki şerittir**.

![Koordinat düzleminde iki paralel doğru: (−1, 0) ve (0, 2) noktalarından geçen düz doğru ile (2, 0) ve (0, −4) noktalarından geçen kesikli doğru. Aralarındaki şerit mavi boyalı.](gorsel/tyt-matematik/03-06-serit.svg "Paralel iki doğru arasındaki şerit. Düz kenardaki noktalar çözüme dahil, kesikli kenardakiler dahil değil.")

Aynı doğrularla durum değişebilir:

| Sistem | Çözüm kümesi |
|---|---|
| $2x - y \ge -2$ ve $2x - y < 4$ | İki doğru arasındaki şerit |
| $2x - y < -2$ ve $2x - y > 4$ | **Boş küme** ($2x - y$ hem $-2$'den küçük hem $4$'ten büyük olamaz) |
| $2x - y > 4$ ve $2x - y > -2$ | Yalnızca $2x - y > 4$ bölgesi (biri diğerini kapsar) |
| $2x - y \le 4$ ve $2x - y \ge 4$ | Yalnızca $2x - y = 4$ doğrusu |

**Kural.** $x$ ve $y$ katsayıları orantılıysa (örneğin $x + 2y$ ile $2x + 4y$) doğrular paraleldir. Önce katsayıları eşitle, sonra $a \le \text{ifade} < b$ biçiminde yaz: aralık doluysa şerit, boşsa çözüm kümesi boş kümedir.

## Kapalı bölge ve tam sayı noktaları

**Örnek.** $x > 0$, $y > 0$ ve $2x + 3y < 12$ sistemini sağlayan kaç tane $(x, y)$ tam sayı ikilisi vardır?

$x > 0$ ve $y > 0$ birinci bölgeyi verir. $2x + 3y = 12$ doğrusu $(6, 0)$ ve $(0, 4)$ noktalarından geçer. Üç koşul bir **üçgen** bölge oluşturur; üç kenar da kesiklidir.

Tam sayıları $x$'e göre sırayla say:

| $x$ | Koşul | $y$ değerleri | Sayı |
|---|---|---|---|
| 1 | $3y < 10$ | 1, 2, 3 | 3 |
| 2 | $3y < 8$ | 1, 2 | 2 |
| 3 | $3y < 6$ | 1 | 1 |
| 4 | $3y < 4$ | 1 | 1 |
| 5 | $3y < 2$ | yok | 0 |

Toplam **7** ikili.

![Birinci bölgede (6, 0) ve (0, 4) noktaları arasında kesikli doğru; eksenlerle oluşan üçgen boyalı, kenarları kesikli. İçinde 7 yeşil nokta var; doğrunun üzerindeki (3, 2) noktası içi boş ve kırmızı.](gorsel/tyt-matematik/03-06-ucgen.svg "Yeşil noktalar sayılır. (3, 2) tam kesikli doğrunun üzerinde olduğu için sayılmaz.")

Koşul $2x + 3y \le 12$ olsaydı doğru üzerindeki $(3, 2)$ noktası da sayılırdı ($6 + 6 = 12$) ve cevap 8 olurdu. Eksenler de kesikli olduğu için $(0, 4)$ ve $(6, 0)$ hiç sayılmaz.

**Kural.** Kapalı bir bölgedeki tam sayı noktalarını bulmak için bir değişkeni sabitle ($x = 1, 2, \dots$), diğerinin alabileceği değerleri say. Sınırda kalan noktaları tek tek kontrol et: düz kenardakiler sayılır, kesikli kenardakiler sayılmaz.

## Grafikten sistemi okumak

**Örnek.** Bir grafikte $(0, 6)$ ve $(3, 0)$ noktalarından geçen **düz** bir doğru var ve boyalı bölge orijin tarafında. Bu bölgenin eşitsizliği nedir?

1. **Doğrunun denklemi.** Eksenleri $(a, 0)$ ve $(0, b)$ noktalarında kesen doğru $\frac{x}{a} + \frac{y}{b} = 1$ biçimindedir: $\frac{x}{3} + \frac{y}{6} = 1$, yani $2x + y = 6$.
2. **Eşitlik var mı?** Doğru düz: $\le$ ya da $\ge$.
3. **Yön.** Orijin boyalı bölgede ve $2 \cdot 0 + 0 = 0 < 6$. O hâlde $2x + y \le 6$.

**Kural.** Grafikteki her doğru için üç soru sor: denklemi ne, düz mü kesikli mi, boyalı tarafta hangi nokta var? O noktayı ifadede yerine koy ve işareti seç.

## ÖSYM tuzakları

> **Bir koşula bakıp karar vermek:** Bir nokta, sistemdeki eşitsizliklerden yalnızca birini sağlıyorsa çözüm değildir. Seçenekleri **bütün** eşitsizliklerde dene.

> **Köşeyi otomatik dahil etmek:** İki doğrunun kesiştiği köşe, doğrulardan biri bile kesikliyse çözüme dahil değildir. Tam sayı sayarken en çok bu noktalar yanlış sayılır.

> **Paralel doğruları fark etmemek:** $x + 2y < 1$ ve $2x + 4y > 6$ farklı görünür. İkincisini 2'ye bölünce $x + 2y > 3$ olur: bir sayı hem $1$'den küçük hem $3$'ten büyük olamaz, çözüm kümesi **boş kümedir**.

> **Kesikli ile düzü karıştırmak:** Grafikte doğru kesikliyse işaret $<$ ya da $>$, düzse $\le$ ya da $\ge$ olur. Seçenekler çoğu zaman yalnızca bu farkla ayrılır.

## Kendini dene

### Soru 1
Aşağıdaki noktalardan hangisi

$$x + 2y \le 8, \quad 3x - y > 2$$

sisteminin çözüm kümesindedir?

A) $(0, 0)$
B) $(1, 1)$
C) $(2, 3)$
D) $(4, 3)$
E) $(1, 4)$

**Cevap:** C
**Çözüm:** $(2, 3)$: $2 + 6 = 8 \le 8$ ✓ ve $6 - 3 = 3 > 2$ ✓. Diğerleri: $(0, 0)$ için $0 > 2$ yanlış; $(1, 1)$ için $3 - 1 = 2 > 2$ yanlış (nokta kesikli doğru üzerinde); $(4, 3)$ için $4 + 6 = 10 \le 8$ yanlış; $(1, 4)$ için $1 + 8 = 9 \le 8$ yanlış.

### Soru 2
$x \ge 0$, $y \ge 0$ ve $x + y < 3$ sistemini sağlayan kaç tane $(x, y)$ tam sayı ikilisi vardır?

A) 1
B) 3
C) 6
D) 9
E) 10

**Cevap:** C
**Çözüm:** $x + y < 3$ demek, tam sayılarda $x + y \le 2$ demektir. $x = 0$ için $y = 0, 1, 2$ (3 tane); $x = 1$ için $y = 0, 1$ (2 tane); $x = 2$ için $y = 0$ (1 tane). Toplam 6. Doğru üzerindeki noktaları da sayan ($x + y \le 3$) 10 bulur; eksenleri dışarıda bırakan ($x > 0$, $y > 0$) 1 bulur.

### Soru 3
Aşağıdaki grafikte boyalı bölge hangi sistemin çözüm kümesidir?

![Koordinat düzleminde iki paralel doğru: x eksenini −1'de, y eksenini 1'de kesen kesikli doğru ve x eksenini 2'de, y eksenini −2'de kesen düz doğru. Aradaki şerit mavi boyalı.](gorsel/tyt-matematik/03-06-kd3.svg "Hangi doğrunun kesikli, hangisinin düz olduğuna ve şeridin iki doğrunun arasında kaldığına bak.")

A) $y > x + 1$ ve $y \ge x - 2$
B) $y < x + 1$ ve $y \ge x - 2$
C) $y \le x + 1$ ve $y > x - 2$
D) $y < x + 1$ ve $y \le x - 2$
E) $y \le x + 1$ ve $y \ge x - 2$

**Cevap:** B
**Çözüm:** Üstteki doğru $(-1, 0)$ ve $(0, 1)$ noktalarından geçer: $y = x + 1$. Kesikli olduğu için eşitlik yok; bölge doğrunun altında: $y < x + 1$. Alttaki doğru $(2, 0)$ ve $(0, -2)$ noktalarından geçer: $y = x - 2$. Düz; bölge doğrunun üstünde: $y \ge x - 2$. Kontrol: orijin için $0 < 1$ ve $0 \ge -2$, ikisi de doğru. C ve E düz ile kesikliyi karıştırır.

## Özet kartı

- Sistemin çözümü = eşitsizliklerin çözüm bölgelerinin kesişimi (ortak boyalı bölge).
- Her eşitsizlik için: sınır doğrusu, düz ($\le$, $\ge$) ya da kesikli ($<$, $>$), orijinle taraf seçimi.
- Köşe noktası yalnızca iki doğru da düzse dahildir.
- Katsayılar orantılıysa doğrular paraleldir: çözüm şerit, tek doğru, tek yarı düzlem ya da boş küme olur.
- Tam sayı noktaları: bir değişkeni sabitle, diğerini say; sınırdaki noktaları ayrıca kontrol et.
- Grafikten sistem: denklem, düz mü kesikli mi, boyalı taraftaki bir noktayla işaret.

## Sonraki adım

Alıştırmaya geç (aşağıdaki düğme). Sonraki ders **Mutlak Değer Kavramı ve Özellikleri**; orada $|x| < 3$ gibi ifadelerin aslında $-3 < x < 3$ sistemi olduğunu göreceksin.
