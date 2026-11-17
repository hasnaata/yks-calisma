---
baslik: Birinci Dereceden İki Bilinmeyenli Eşitsizlikler
ders: tyt-matematik
sure: 20 dk
kaynak: MEBİ Konu Özeti 01d11ac5c1
guncelleme: 2026-11-17
---
# Birinci Dereceden İki Bilinmeyenli Eşitsizlikler

**Bu dersin sonunda:** $ax + by \le c$ gibi bir eşitsizliğin çözüm bölgesini analitik düzlemde çizebilecek, verilen taralı bölgenin hangi eşitsizliği gösterdiğini bulabilecek ve bölgedeki tam sayı noktalarını sayabileceksin.

> **TYT'de yeri:** Bu konu genellikle grafikle gelir: "Taralı bölge hangi eşitsizliğin grafiğidir?", "Hangi nokta çözüm kümesinde değildir?", "Eşitsizliği sağlayan kaç pozitif tam sayı ikilisi vardır?" ve "Bütçesi en çok 100 TL olan biri…" gibi günlük hayat soruları. Doğrunun düz mü kesikli mi olduğu ve hangi tarafın boyandığı en sık yapılan hatadır.

## Önce hatırla

<details><summary>İki bilinmeyenli denklemlerden: $x + y = 7$ ve $x - y = 3$ sisteminin çözümü nedir?</summary>
Yok etme yöntemi: iki denklemi taraf tarafa topla, $y$ gider: $2x = 10$, yani $x = 5$. Birinci denklemden $y = 7 - 5 = 2$. Çözüm <b>$(5, 2)$</b>. Sağlama: $5 - 2 = 3$.
</details>

<details><summary>İki bilinmeyenli denklemlerden: $ax + 3y = 6$ ve $4x + 6y = 9$ sisteminin çözüm kümesi boş küme ise $a$ kaçtır?</summary>
Çözüm yoksa doğrular paraleldir: $\frac{a}{4} = \frac{3}{6} \ne \frac{6}{9}$. Buradan $a = 2$. Sabitlerin oranı $\frac{6}{9} = \frac{2}{3}$, katsayıların oranı $\frac{1}{2}$; eşit değil, doğrular çakışık değil paraleldir: <b>$a = 2$</b>.
</details>

## Çözüm kümesi bir bölgedir

Önceki derste $ax + by = c$ denkleminin grafiğinin bir **doğru** olduğunu gördün. Eşittir yerine $<$, $\le$, $>$, $\ge$ koyarsan **birinci dereceden iki bilinmeyenli eşitsizlik** elde edersin ($a \ne 0$, $b \ne 0$):

$$ax + by < c, \quad ax + by \le c, \quad ax + by > c, \quad ax + by \ge c$$

**Örnek.** $2x + y \le 4$ eşitsizliğini hangi noktalar sağlar?

- $(0, 0)$: $0 \le 4$ doğru, sağlar.
- $(1, 2)$: $2 + 2 = 4 \le 4$ doğru, sağlar. Bu nokta $2x + y = 4$ doğrusunun **üzerinde**.
- $(2, 1)$: $4 + 1 = 5 \le 4$ yanlış, sağlamaz.

Çözüm kümesinin elemanları yine $(x, y)$ sıralı ikilileridir; ama bu kez sonsuz tane ve bir doğruyla değil, **bir doğrunun bir tarafındaki bölgeyle** gösterilir. Bu doğruya **sınır doğrusu** denir.

## Bölgeyi çizmek: üç adım

**Örnek.** $2x + y \le 4$ eşitsizliğinin grafiğini çiz.

1. **Eşitlik yap, doğruyu çiz.** $2x + y = 4$ için $x = 0 \Rightarrow y = 4$, $y = 0 \Rightarrow x = 2$. Doğru $(0, 4)$ ve $(2, 0)$ noktalarından geçer.
2. **Çizgiyi seç.** Eşitsizlikte $\le$ var; doğrunun üzerindeki noktalar da çözüm, doğru **düz çizgi** ile çizilir.
3. **Deneme noktası koy.** $(0, 0)$ için $0 \le 4$ doğru. Orijinin bulunduğu taraf boyanır.

![Koordinat düzleminde (0, 4) ve (2, 0) noktalarından geçen düz mavi doğru. Doğrunun sol altı, orijini de içeren taraf mavi boyalı. Orijinde yeşil deneme noktası.](gorsel/tyt-matematik/03-05-ornek-kapali.svg "Deneme noktası (0, 0) eşitsizliği sağladığı için onun bulunduğu taraf boyandı. Düz çizgi doğrunun da çözüme dahil olduğunu gösterir.")

**Kural.** $\le$ ya da $\ge$ varsa sınır doğrusu **düz**, $<$ ya da $>$ varsa **kesikli** çizilir. Hangi tarafın boyanacağını bir deneme noktasıyla bul: nokta eşitsizliği sağlıyorsa onun tarafı, sağlamıyorsa karşı taraf boyanır.

![Yöntem şeması: Eşitsizliği eşitlik yap, iki noktayla doğruyu çiz. Eşitlik varsa düz, yoksa kesikli çizgi. Sonra (0, 0) noktasını dene; eşitsizlik doğruysa o tarafı, değilse karşı tarafı boya.](gorsel/tyt-matematik/03-05-yontem.svg "Her soruda bu sırayı izle. Doğru orijinden geçiyorsa (0, 0) yerine (1, 0) gibi başka bir nokta dene.")

## Üst bölge mi, alt bölge mi?

Deneme noktası yerine $y$'yi yalnız bırakıp $y = mx + n$ biçimine getirerek de karar verebilirsin:

| Eşitsizlik | Bölge | Sınır doğrusu |
|---|---|---|
| $y > mx + n$ | doğrunun **üstü** | kesikli |
| $y \ge mx + n$ | doğrunun **üstü** | düz |
| $y < mx + n$ | doğrunun **altı** | kesikli |
| $y \le mx + n$ | doğrunun **altı** | düz |

**Örnek.** $x - 2y < 4$ eşitsizliğinin bölgesi doğrunun üstünde mi, altında mı?

$y$'yi yalnız bırak: $-2y < 4 - x$. Şimdi iki tarafı $-2$'ye böl. **Negatif sayıya bölünce yön değişir:**

$$y > \frac{x}{2} - 2$$

Bölge doğrunun **üstü**, sınır kesikli. Kontrol: $(0, 0)$ için $0 < 4$ doğru; orijin de doğrunun üstünde ($x = 0$ iken doğru $y = -2$'de).

![Koordinat düzleminde (4, 0) ve (0, −2) noktalarından geçen kesikli kırmızı doğru. Doğrunun üstü mavi boyalı. Doğru üzerindeki iki nokta içi boş.](gorsel/tyt-matematik/03-05-ornek-kesikli.svg "Kesikli çizgi: doğrunun üzerindeki noktalar çözüme dahil değil. Boyalı bölge doğrunun üstü, çünkü y > x/2 − 2.")

**Kural.** $y > \dots$ üst, $y < \dots$ alt bölgedir. Ama bu kuralı kullanmadan önce $y$'nin katsayısı negatifse yönü çevirmeyi unutma.

**Özel durumlar.** Bir değişken yoksa sınır doğrusu eksene paraleldir:

| Eşitsizlik | Sınır doğrusu | Boyalı bölge |
|---|---|---|
| $x > 2$ | $x = 2$ dikey, kesikli | doğrunun sağı |
| $x \le -1$ | $x = -1$ dikey, düz | doğrunun solu |
| $y \ge 3$ | $y = 3$ yatay, düz | doğrunun üstü |
| $y < 0$ | $x$ ekseni, kesikli | eksenin altı |

## Grafikten eşitsizliği bulmak

**Örnek.** Aşağıdaki taralı bölge hangi eşitsizliğin grafiğidir?

![Koordinat düzleminde x eksenini −3'te, y eksenini 2'de kesen düz mavi doğru. Doğrunun sol üstü boyalı; orijin boyalı bölgenin dışında.](gorsel/tyt-matematik/03-05-grafik-oku.svg "Orijin taralı bölgede değil. Eşitsizliğin yönünü orijinin sağlamadığı tarafa göre seç.")

1. **Doğrunun denklemi.** Eksenleri $(-3, 0)$ ve $(0, 2)$'de kesen doğru: $\frac{x}{-3} + \frac{y}{2} = 1$. İki tarafı $6$ ile çarp: $-2x + 3y = 6$, yani $2x - 3y = -6$.
2. **Çizgi.** Doğru düz çizilmiş; eşitsizlik $\le$ ya da $\ge$.
3. **Yön.** Orijin için $2 \cdot 0 - 3 \cdot 0 = 0$ ve $0 \ge -6$. Orijin boyalı bölgede **değil**, o hâlde boyalı taraf bunun tersidir:

$$2x - 3y \le -6$$

Kontrol: boyalı bölgedeki $(-3, 3)$ için $-6 - 9 = -15 \le -6$ doğru.

**Kural.** Eksenleri $(a, 0)$ ve $(0, b)$'de kesen doğrunun denklemi $\frac{x}{a} + \frac{y}{b} = 1$'dir. Denklemi bulduktan sonra yönü her zaman bir deneme noktasıyla seç.

## Tam sayı çözümlerini saymak

**Örnek.** $x$ ve $y$ pozitif tam sayılar olmak üzere $x + 2y \le 6$ eşitsizliğini sağlayan kaç $(x, y)$ ikilisi vardır?

Katsayısı büyük olan $y$'yi sabitle, $x$'i say:

- $y = 1$: $x \le 4$, yani $x = 1, 2, 3, 4$: **4** ikili.
- $y = 2$: $x \le 2$, yani $x = 1, 2$: **2** ikili.
- $y = 3$: $x \le 0$; pozitif $x$ yok.

Toplam $4 + 2 = 6$ ikili.

![x + 2y = 6 doğrusu ve altında kalan boyalı bölge. Birinci bölgede (1,1), (2,1), (3,1), (4,1), (1,2), (2,2) noktaları yeşil.](gorsel/tyt-matematik/03-05-tam-sayi.svg "Yeşil noktalar pozitif tam sayı çözümleri. (2, 2) doğrunun üzerinde ama ≤ olduğu için sayılır.")

**Kural.** Bir değişkeni sırayla $1, 2, 3, \dots$ yap, diğerinin kaç değer alabileceğini say, topla. Doğrunun üzerindeki noktaları yalnızca $\le$ ve $\ge$ durumunda say.

## ÖSYM tuzakları

> **Negatife bölüp yönü çevirmemek:** $x - 2y < 4$ eşitsizliğinden $y < \frac{x}{2} - 2$ yazıp alt bölgeyi boyamak yanlıştır. $-2$'ye bölünce yön değişir: $y > \frac{x}{2} - 2$, bölge üsttedir.

> **Düz ile kesikliyi karıştırmak:** Seçeneklerde aynı doğru için hem $\le$ hem $<$ bulunur. Grafikte doğru kesikliyse eşitlik yoktur.

> **Orijin bölgede değilken yönü ters seçmek:** Orijin taralı bölgedeyse yön, $0$'ı doğru yapan yöndür; değilse tersi. Denemeyi yapmadan seçenek işaretleme.

> **Doğru orijinden geçerken $(0, 0)$ denemek:** $x - 3y < 0$ gibi $c = 0$ olan eşitsizlikte orijin doğrunun üzerindedir ve karar vermez. $(1, 0)$ gibi başka bir nokta dene.

> **"Pozitif" ile "doğal sayı"yı karıştırmak:** Pozitif tam sayılarda $0$ yoktur. $x = 0$ ya da $y = 0$ olan ikilileri saymak cevabı büyütür.

## Kendini dene

### Soru 1
Aşağıdaki noktalardan hangisi $x + 3y \le 6$ eşitsizliğinin çözüm kümesinde **değildir**?

A) $(0, 0)$
B) $(1, 2)$
C) $(-2, 2)$
D) $(3, 1)$
E) $(6, 0)$

**Cevap:** B
**Çözüm:** Her noktayı yerine koy. $(0, 0)$: $0 \le 6$. $(1, 2)$: $1 + 6 = 7 \le 6$ **yanlış**. $(-2, 2)$: $-2 + 6 = 4 \le 6$. $(3, 1)$: $3 + 3 = 6 \le 6$ (doğru üzerinde, dahil). $(6, 0)$: $6 \le 6$ (dahil). Sağlamayan tek nokta $(1, 2)$.

### Soru 2
$x$ ve $y$ pozitif tam sayılar olmak üzere $2x + y \le 7$ eşitsizliğini sağlayan kaç $(x, y)$ ikilisi vardır?

A) 6
B) 8
C) 9
D) 12
E) 20

**Cevap:** C
**Çözüm:** $x = 1$: $y \le 5$, 5 ikili. $x = 2$: $y \le 3$, 3 ikili. $x = 3$: $y \le 1$, 1 ikili. $x = 4$: $y \le -1$, yok. Toplam $5 + 3 + 1 = 9$. $\le$ yerine $<$ alan 6 bulur; $y = 0$'ı da sayan 12 bulur.

### Soru 3
$x$ eksenini $-2$'de, $y$ eksenini $4$'te kesen **kesikli** doğrunun altında kalan bölge hangi eşitsizliğin grafiğidir?

A) $y > 2x + 4$
B) $y \le 2x + 4$
C) $y < -2x + 4$
D) $y < 2x + 4$
E) $y < 2x - 4$

**Cevap:** D
**Çözüm:** Doğru $(0, 4)$ ve $(-2, 0)$'dan geçer; eğimi $\frac{4 - 0}{0 - (-2)} = 2$, denklemi $y = 2x + 4$. Kesikli olduğu için eşitlik yok; alt bölge $y < 2x + 4$. B seçeneği doğruyu dahil eder, C ise eğimin işaretini yanlış alır.

## Özet kartı

- Çözüm kümesi, sınır doğrusunun bir tarafındaki bölgedir.
- $\le$, $\ge$: düz çizgi (doğru dahil); $<$, $>$: kesikli çizgi (doğru dahil değil).
- Tarafı seçmek için deneme noktası koy; doğru orijinden geçiyorsa başka nokta seç.
- $y > mx + n$ üst, $y < mx + n$ alt bölge; $y$'nin katsayısı negatifse bölerken yönü çevir.
- Eksenleri $(a, 0)$ ve $(0, b)$'de kesen doğru: $\frac{x}{a} + \frac{y}{b} = 1$.
- Tam sayı çözümlerini bir değişkeni sabitleyerek say.

## Sonraki adım

Alıştırmaya geç (aşağıdaki düğme). Sonraki ders **Birinci Dereceden İki Bilinmeyenli Eşitsizlik Sistemleri**; orada birden çok eşitsizliğin bölgelerini aynı düzlemde kesiştireceksin.
