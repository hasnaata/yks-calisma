---
baslik: Diskriminant Kavramı ve Diskriminantın Kullanılması
ders: tyt-matematik
sure: 20 dk
kaynak: MEBİ Konu Özeti 7902b07f4b
guncelleme: 2026-11-18
---
# Diskriminant Kavramı ve Diskriminantın Kullanılması

<div class="giris" dir="rtl" lang="ar">

**الدرس ده عن إيه؟** عن المميز (diskriminant): رقم واحد بتحسبه من معاملات معادلة الدرجة التانية (ikinci dereceden denklem)، وبيقولك على طول المعادلة ليها كام جذر.

- هتحل أي معادلة من الدرجة التانية بالقانون العام (kök formülü)، حتى لو مش بتتحلل لعوامل.
- هتعرف من إشارة المميز بس إذا كان فيه جذرين مختلفين، ولا جذرين متساويين (çakışık kök)، ولا مفيش جذور حقيقية (gerçek kök) خالص.
- هتطلع قيمة المعامل المجهول (parametre) اللي تخلي المعادلة ليها العدد المطلوب من الجذور.

**ليه مهم؟** في TYT بييجي كتير سؤال زي "المعادلة ليها جذرين متساويين، يبقى m بكام؟"، وأغلب الغلط بيكون في إشارة سالب صغيرة اتنسيت.

٢٠ دقيقة بس، وفيه أمثلة محلولة خطوة بخطوة ورسومات بتوضح كل حالة. هات ورقة وقلم ويلا بينا.

</div>

**Bu dersin sonunda:** her ikinci dereceden denklemi kök formülüyle çözebilecek, denklemi çözmeden yalnızca $\Delta = b^2 - 4ac$ işaretine bakarak kaç gerçek kökü olduğunu söyleyebilecek ve "çakışık kök", "gerçek kök yok" gibi koşullardan bilinmeyen katsayıyı bulabileceksin.

> **TYT'de yeri:** Doğrudan "denklemin çakışık iki kökü olduğuna göre $m$ kaçtır?", "gerçek kökü olmadığına göre $k$'nin alabileceği en küçük tam sayı değeri kaçtır?" ve "hangi denklemin iki farklı gerçek kökü vardır?" kalıpları gelir. Problem sorularında da "bu alan, bu yükseklik mümkün mü?" sorusunun cevabı diskriminanttır.

## Önce hatırla

<details><summary>Geçen dersten: $2x^2 - 5x - 3 = 0$ denkleminin çözüm kümesini çarpanlara ayırarak bul.</summary>
$2x^2$'yi $2x \cdot x$, $-3$'ü $1 \cdot (-3)$ diye böl. Çapraz çarpımların toplamı: $2x \cdot (-3) + x \cdot 1 = -5x$, tuttu. $(2x + 1)(x - 3) = 0$. Her çarpanı sıfıra eşitle: $x = -\frac{1}{2}$ ya da $x = 3$. Ç $= \left\{-\frac{1}{2}, 3\right\}$.
</details>

<details><summary>Geçen dersten: $x^2 - 6x + 4 = 0$ denklemi tam sayılarla çarpanlarına ayrılmıyor. Tam kareye tamamlayarak çöz.</summary>
$x^2 - 6x$ ifadesini $(x - 3)^2 = x^2 - 6x + 9$ yapmak için $9$ gerekir: $x^2 - 6x + 9 - 9 + 4 = 0$, yani $(x - 3)^2 = 5$. Buradan $x - 3 = \pm\sqrt{5}$, Ç $= \{3 - \sqrt{5},\ 3 + \sqrt{5}\}$. Bu derste aynı işi her denklem için bir kerede yapan formülü kullanacaksın.
</details>

## Kök formülü ve diskriminant

**Örnek.** $x^2 - 4x + 1 = 0$ denklemini çöz.

Çarpımı $1$, toplamı $-4$ olan tam sayı yok; çarpanlara ayırma tıkanır. Formülü kullan:

1. Katsayıları işaretiyle oku: $a = 1$, $b = -4$, $c = 1$.
2. Diskriminantı hesapla: $\Delta = b^2 - 4ac = (-4)^2 - 4 \cdot 1 \cdot 1 = 16 - 4 = 12$.
3. Kökler: $x = \dfrac{-b \pm \sqrt{\Delta}}{2a} = \dfrac{4 \pm \sqrt{12}}{2} = \dfrac{4 \pm 2\sqrt{3}}{2} = 2 \pm \sqrt{3}$.

Ç $= \{2 - \sqrt{3},\ 2 + \sqrt{3}\}$.

**Örnek.** $2x^2 + x - 6 = 0$ denklemini formülle çöz.

$a = 2$, $b = 1$, $c = -6$. $\Delta = 1^2 - 4 \cdot 2 \cdot (-6) = 1 + 48 = 49$, $\sqrt{49} = 7$.

$$x_1 = \frac{-1 + 7}{2 \cdot 2} = \frac{6}{4} = \frac{3}{2}, \qquad x_2 = \frac{-1 - 7}{2 \cdot 2} = \frac{-8}{4} = -2$$

Ç $= \left\{-2, \frac{3}{2}\right\}$. Çarpanlara ayırarak da aynı sonuca ulaşırsın: $(2x - 3)(x + 2) = 0$. $\Delta$ tam kare çıktıysa denklem tam sayılarla çarpanlarına ayrılır.

**Kural.** $a \ne 0$ olmak üzere $ax^2 + bx + c = 0$ denkleminde

$$\Delta = b^2 - 4ac \qquad x_{1,2} = \frac{-b \pm \sqrt{\Delta}}{2a}$$

$\Delta$ (delta) ifadesine denklemin **diskriminantı** denir. Formül, geçen dersteki tam kareye tamamlamanın genel hâlidir; bu yüzden her ikinci dereceden denklemde çalışır.

## Δ'nın işareti kök sayısını söyler

**Örnek.** Yalnızca sabit terimi farklı olan üç denklemi karşılaştır.

| Denklem | $\Delta = b^2 - 4ac$ | Kökler |
|---|---|---|
| $x^2 - 2x - 3 = 0$ | $4 + 12 = 16$ | $\frac{2 \pm 4}{2}$: $x = 3$ ya da $x = -1$ |
| $x^2 - 2x + 1 = 0$ | $4 - 4 = 0$ | $\frac{2 \pm 0}{2}$: yalnızca $x = 1$ |
| $x^2 - 2x + 5 = 0$ | $4 - 20 = -16$ | $\sqrt{-16}$ gerçek sayı değil: kök yok |

![Üç parabol yan yana. x kare eksi 2x eksi 3 grafiği x eksenini eksi 1 ve 3'te keser, delta 16. x kare eksi 2x artı 1 grafiği eksene 1'de değer, delta 0. x kare eksi 2x artı 5 grafiği ekseni hiç kesmez, delta eksi 16.](gorsel/tyt-matematik/15-03-uc-durum.svg "c büyüdükçe grafik yukarı kayar. Δ pozitifken eksen iki yerde kesilir, Δ sıfırken grafik eksene değer, Δ negatifken eksenle hiç buluşmaz.")

Formülde $\sqrt{\Delta}$ hem eklenir hem çıkarılır. $\Delta > 0$ ise iki farklı sonuç çıkar; $\Delta = 0$ ise iki sonuç aynıdır; $\Delta < 0$ ise negatif sayının karekökü gerçek sayılarda yoktur.

**Kural.**

| $\Delta$ | Gerçek kökler | Çözüm kümesi |
|---|---|---|
| $\Delta > 0$ | Birbirinden farklı iki gerçek kök | İki elemanlı |
| $\Delta = 0$ | Eşit (çakışık) iki kök: $x_1 = x_2 = -\dfrac{b}{2a}$ | Bir elemanlı |
| $\Delta < 0$ | Gerçek kök yok | Ç $= \varnothing$ |

$\Delta = 0$ olduğunda sol taraf bir **tam karedir**: $x^2 - 2x + 1 = (x - 1)^2$. "Gerçek kökü vardır" ifadesi ilk iki satırı birlikte kapsar, yani $\Delta \ge 0$ demektir.

![Akış: standart biçime getir, katsayıları işaretiyle oku, delta eşittir b kare eksi 4ac hesapla. Delta pozitifse iki farklı kök, sıfırsa çakışık kök, negatifse gerçek kök yok.](gorsel/tyt-matematik/15-03-yontem.svg "Kök sayısı sorulduğunda denklemi çözme; üç adımda Δ'yı bul ve işaretine bak.")

**Kısa yol.** $3x^2 + 5x - 7 = 0$ denkleminin kaç gerçek kökü var? $a = 3$ ile $c = -7$ ters işaretli, yani $a \cdot c < 0$. O zaman $-4ac$ pozitiftir ve $b^2 \ge 0$ olduğundan $\Delta$ kesinlikle pozitif çıkar ($\Delta = 25 + 84 = 109$). **$a$ ile $c$ ters işaretliyse denklemin her zaman iki farklı gerçek kökü vardır.** Tersi doğru değildir: $a$ ile $c$ aynı işaretliyse $\Delta$'yı hesaplaman gerekir.

## Parametreli sorular

**Örnek.** $x^2 - 4x + m = 0$ denklemi için $m$'nin hangi değerlerinde iki farklı kök, çakışık kök ya da hiç gerçek kök olmaz?

1. $\Delta = (-4)^2 - 4 \cdot 1 \cdot m = 16 - 4m$.
2. Çakışık kök: $16 - 4m = 0$, $m = 4$. Denklem $(x - 2)^2 = 0$, kök $x = 2$.
3. İki farklı kök: $16 - 4m > 0$, $m < 4$.
4. Gerçek kök yok: $16 - 4m < 0$, $m > 4$. Bu durumda $m$'nin alabileceği en küçük tam sayı $5$'tir.

![m sayı doğrusu: 4'ün solu yeşil, delta pozitif, iki farklı kök. 4 noktası sarı, delta sıfır, çakışık kök. 4'ün sağı kırmızı, delta negatif, gerçek kök yok.](gorsel/tyt-matematik/15-03-parametre.svg "Sınır değeri Δ = 0 denkleminden bulunur; sonra sağına ve soluna bakılır. m = 4 yeşil bölgeye de kırmızı bölgeye de ait değildir.")

**Örnek.** $(m - 2)x^2 - 4x + 2 = 0$ denkleminin eşit iki kökü olduğuna göre $m$ kaçtır?

1. $a = m - 2$, $b = -4$, $c = 2$. $\Delta = 16 - 4(m - 2) \cdot 2 = 16 - 8(m - 2)$.
2. $\Delta = 0$: $8(m - 2) = 16$, $m - 2 = 2$, $m = 4$.
3. Kontrol: $a = m - 2 = 2 \ne 0$. Denklem $2x^2 - 4x + 2 = 0$, yani $2(x - 1)^2 = 0$; çakışık kök $x = 1$.

**Kural.** Önce $\Delta$'yı parametreye bağlı yaz, sonra soruya göre $\Delta > 0$, $\Delta = 0$, $\Delta < 0$ ya da $\Delta \ge 0$ kur. $x^2$'nin katsayısında parametre varsa bulduğun değer **$a \ne 0$** koşulunu bozmamalı.

## ÖSYM tuzakları

> **Negatif $b$'nin karesi:** $b = -4$ ise $b^2 = (-4)^2 = 16$'dır, $-16$ değil. Formüldeki $-b$ de $-(-4) = 4$ olur.

> **$c$'nin işaretini kaybetmek:** $c = -6$ iken $-4ac = -4 \cdot 2 \cdot (-6) = +48$'dir. $\Delta$'yı $1 - 48$ diye hesaplayan, iki kökü olan bir denkleme "kök yok" der.

> **$a$'yı unutmak:** $-4ac$ çarpımında da paydadaki $2a$'da da $a$ vardır. $a = 1$ olmayan denklemlerde $\Delta = b^2 - 4c$ ya da bölümü yalnızca $2$ almak en sık hatadır.

> **"Gerçek kökü var" ile "iki farklı gerçek kökü var" farkı:** İlki $\Delta \ge 0$, ikincisi $\Delta > 0$ demektir. Sınır değer ($\Delta = 0$ yapan değer) yalnızca ilkine dahildir; tam sayı sayarken bu tek fark cevabı değiştirir.

> **$a \ne 0$ koşulunu atlamak:** $(m - 3)x^2 + 4x + 1 = 0$ denkleminde $m = 3$ olursa denklem $4x + 1 = 0$ olur; artık ikinci dereceden değildir ve tek kökü vardır. "İki farklı kök" sorusunda $m = 3$ elenir.

## Kendini dene

### Soru 1
$2x^2 - 3x - 2 = 0$ denkleminin diskriminantı kaçtır?

A) $-7$
B) $1$
C) $7$
D) $17$
E) $25$

**Cevap:** E
**Çözüm:** $a = 2$, $b = -3$, $c = -2$. $\Delta = (-3)^2 - 4 \cdot 2 \cdot (-2) = 9 + 16 = 25$. $c$'nin eksisini kaybeden $9 - 16 = -7$, $a$'yı unutan $9 + 8 = 17$ bulur.

### Soru 2
Aşağıdaki denklemlerden hangisinin gerçek kökü **yoktur**?

A) $x^2 - 4x + 4 = 0$
B) $x^2 + 3x - 1 = 0$
C) $2x^2 + x + 1 = 0$
D) $x^2 - 5x = 0$
E) $3x^2 - 2x - 1 = 0$

**Cevap:** C
**Çözüm:** C'de $\Delta = 1^2 - 4 \cdot 2 \cdot 1 = 1 - 8 = -7 < 0$, gerçek kök yok. A'da $\Delta = 16 - 16 = 0$ (çakışık kök $2$). B ve E'de $a$ ile $c$ ters işaretli, iki kök kesin var ($\Delta = 13$ ve $\Delta = 16$). D'de $\Delta = 25$; kökler $0$ ve $5$.

### Soru 3
$x^2 + 6x + k - 1 = 0$ denkleminin çakışık iki kökü olduğuna göre $k$ kaçtır?

A) $8$
B) $9$
C) $10$
D) $35$
E) $37$

**Cevap:** C
**Çözüm:** $c = k - 1$. $\Delta = 36 - 4(k - 1) = 0$, $k - 1 = 9$, $k = 10$. Kontrol: $x^2 + 6x + 9 = (x + 3)^2$, kök $-3$. $c$'yi $k$ sanan $9$, $4$'ü unutan $k - 1 = 36$ ile $37$ bulur.

## Özet kartı

- $\Delta = b^2 - 4ac$; kökler $x_{1,2} = \dfrac{-b \pm \sqrt{\Delta}}{2a}$.
- $\Delta > 0$: iki farklı gerçek kök; $\Delta = 0$: çakışık kök $-\frac{b}{2a}$, ifade tam kare; $\Delta < 0$: Ç $= \varnothing$.
- "Gerçek kökü var" $\Delta \ge 0$, "iki farklı gerçek kökü var" $\Delta > 0$ demektir.
- $a$ ile $c$ ters işaretliyse hesap yapmadan: iki farklı gerçek kök.
- Katsayılar işaretiyle okunur: $(-4)^2 = 16$; $a > 0$ ve $c < 0$ ise $-4ac$ pozitiftir.
- Parametre $x^2$'nin katsayısındaysa $a \ne 0$ koşulunu kontrol et.

## Sonraki adım

Alıştırmaya geç (aşağıdaki düğme). Sonraki ders **İkinci Dereceden Denklemlerde Kök-Katsayı İlişkisi**; kökleri hiç bulmadan toplamlarını ve çarpımlarını katsayılardan okuyacaksın. Orada da önce $\Delta$ ile köklerin var olup olmadığına bakman gerekecek.
