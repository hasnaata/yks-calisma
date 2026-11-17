---
baslik: Trigonometrik Oranlar
ders: tyt-matematik
sure: 20 dk
kaynak: MEBİ Konu Özeti b67d4b1d14
guncelleme: 2026-11-18
---
# Trigonometrik Oranlar

<div class="giris" dir="rtl" lang="ar">

**الدرس ده عن إيه؟** عن النسب المثلثية (trigonometrik oranlar) في المثلث القائم الزاوية (dik üçgen): إزاي تطلّع كل نسبة من أطوال الأضلاع.

- هتعرف الجيب (sinüs) وجيب التمام (kosinüs) والظل (tanjant) وظل التمام (kotanjant) لزاوية حادة، وتفرّق بين الضلع المقابل والضلع المجاور والوتر (hipotenüs).
- لو اتدّالك نسبة واحدة بس، هتبني المثلث بنفسك وتجيب باقي النسب بنظرية فيثاغورس (Pisagor).
- هتتعلم قاعدة الزاويتين المتتامتين (tümler açılar)، وإزاي تنزّل عمود (dikme) لما متلاقيش زاوية قائمة.

**ليه مهم؟** في TYT الأسئلة اللي على النسب دي لوحدها قليلة، بس بتدخل في أسئلة هندسة كتير، وفي مسائل من الحياة زي السلّم والمنحدر وخيط الطيارة الورق.

هي ٢٠ دقيقة بس، وبعدها هتبص لأي مثلث قائم وتعرف تقراه كويس. يلا بينا!

</div>

**Bu dersin sonunda:** bir dik üçgendeki dar açının sinüs, kosinüs, tanjant ve kotanjantını kenarlardan yazabilecek, tek bir oran verildiğinde üçgeni kurup diğer oranları bulabileceksin.

> **TYT'de yeri:** Trigonometri TYT'de kendi başına az soru getirir, ama geometri sorularında sık kullanılır: "$\tan \alpha$ kaçtır?", "$\sin \alpha = \frac{3}{5}$ ise $|AC|$ kaçtır?" gibi. Rampa, merdiven, uçurtma ipi gibi günlük hayat soruları da hep aynı dik üçgene dayanır.

## Önce hatırla

<details><summary>Geçen dersten: ABC dik üçgeninde m(A) = 90°, [AH] ⊥ [BC], |BH| = 4 ve |HC| = 9 birimdir. |AH| kaç birimdir?</summary>
Öklid teoremi: |AH|² = |BH| · |HC| = 4 · 9 = 36, yani |AH| = <b>6</b>. Bugün bu yüksekliğin oluşturduğu küçük dik üçgenlerde açıların oranlarını yazacaksın.
</details>

<details><summary>Geçen dersten: aynı tür bir üçgende |BH| = 4 ve |BC| = 16 ise |AB| kaçtır?</summary>
Dik kenarın karesi, kendi izdüşümü ile hipotenüsün çarpımıdır: |AB|² = |BH| · |BC| = 4 · 16 = 64, yani |AB| = <b>8</b>.
</details>

## Kenarların adı açıya göre değişir

Bir dik üçgende bir **dar açı** seç. Bu açıya göre:

- **Hipotenüs:** dik açının karşısındaki kenar (her zaman aynı, en uzun kenar).
- **Karşı dik kenar:** seçtiğin açının karşısındaki dik kenar.
- **Komşu dik kenar:** seçtiğin açıya değen dik kenar.

Açıyı değiştirirsen karşı ile komşu yer değiştirir; hipotenüs değişmez.

## 1. Dört oran

**Örnek 1.** $ABC$ üçgeninde $m(\widehat{A}) = 90^\circ$, $|AB| = 5$, $|AC| = 12$, $|BC| = 13$ ve $m(\widehat{ACB}) = \alpha$'dır. $\alpha$'nın dört trigonometrik oranını yaz.

![A köşesinde dik açı olan ABC üçgeni. AB kenarı kırmızı ve 5, AC kenarı yeşil ve 12, BC kenarı mavi ve 13. C köşesinde alfa açısı.](gorsel/tyt-matematik/21-03-oranlar.svg "α açısı C köşesinde. Karşısındaki kırmızı kenar 5, ona değen yeşil kenar 12, hipotenüs 13.")

**Çözüm.** $\alpha$, $C$ köşesinde. Karşısındaki dik kenar $[AB] = 5$, ona değen dik kenar $[AC] = 12$, hipotenüs $[BC] = 13$.

$$\sin \alpha = \frac{5}{13} \qquad \cos \alpha = \frac{12}{13} \qquad \tan \alpha = \frac{5}{12} \qquad \cot \alpha = \frac{12}{5}$$

**Kural:**

| Oran | Tanım |
|---|---|
| $\sin \alpha$ | $\dfrac{\text{karşı dik kenar}}{\text{hipotenüs}}$ |
| $\cos \alpha$ | $\dfrac{\text{komşu dik kenar}}{\text{hipotenüs}}$ |
| $\tan \alpha$ | $\dfrac{\text{karşı dik kenar}}{\text{komşu dik kenar}}$ |
| $\cot \alpha$ | $\dfrac{\text{komşu dik kenar}}{\text{karşı dik kenar}}$ |

- Hipotenüs en uzun kenar olduğu için dar açıda $0 < \sin \alpha < 1$ ve $0 < \cos \alpha < 1$'dir.
- $\tan$ ve $\cot$'ta hipotenüs **yoktur**; ikisi birbirinin tersidir: $\tan \alpha \cdot \cot \alpha = 1$.

> **Tuzak:** Aynı üçgende $B$ köşesindeki açı için karşı kenar $12$, komşu kenar $5$ olur: $\tan(\widehat{B}) = \frac{12}{5}$. Hangi açının sorulduğuna bakmadan "kısa kenar bölü uzun kenar" yazma.

## 2. Bir oran verilince üçgeni kur

**Örnek 2.** $\alpha$ dar açı ve $\tan \alpha = \dfrac{3}{4}$ ise $\sin \alpha$ ve $\cos \alpha$ kaçtır?

![B köşesinde dik açı olan ABC üçgeni. AB kırmızı 3k, BC yeşil 4k, AC mavi 5k. C köşesinde alfa açısı.](gorsel/tyt-matematik/21-03-ucgen-kur.svg "tan α = 3/4 olduğu için karşı kenar 3k, komşu kenar 4k alınır; Pisagor ile hipotenüs 5k çıkar.")

**Çözüm.**

1. Bir dik üçgen çiz, bir dar açısına $\alpha$ de. $\tan$ = karşı / komşu olduğu için karşı kenara $3k$, komşu kenara $4k$ yaz.
2. Pisagor: hipotenüs $= \sqrt{(3k)^2 + (4k)^2} = \sqrt{25k^2} = 5k$.
3. $\sin \alpha = \dfrac{3k}{5k} = \dfrac{3}{5}$, $\cos \alpha = \dfrac{4k}{5k} = \dfrac{4}{5}$. ($k$ her zaman sadeleşir.)

**Örnek 3.** $\alpha$ dar açı ve $\sin \alpha = \dfrac{2}{3}$ ise $\tan \alpha$ kaçtır?

**Çözüm.** Karşı kenar $2$, hipotenüs $3$. Komşu kenar $= \sqrt{3^2 - 2^2} = \sqrt{5}$. Buradan

$$\tan \alpha = \frac{2}{\sqrt{5}} = \frac{2\sqrt{5}}{5}$$

**Kural:** Tek oran verilirse iki kenarı yaz, üçüncüyü Pisagor ile bul, istenen oranı oku. Örnek 2'deki sayılarla iki bağıntıyı da kontrol edebilirsin:

$$\sin^2 \alpha + \cos^2 \alpha = 1 \qquad \left(\tfrac{9}{25} + \tfrac{16}{25} = 1\right) \qquad\quad \tan \alpha = \frac{\sin \alpha}{\cos \alpha} \qquad \left(\tfrac{3/5}{4/5} = \tfrac{3}{4}\right)$$

> **Tuzak:** $\tan \alpha = \frac{3}{4}$, kenarların $3$ ve $4$ **olduğunu** söylemez; yalnızca **oranlarının** $3:4$ olduğunu söyler. Soruda bir kenar uzunluğu verilirse önce $k$'yı bul. Örneğin hipotenüs $20$ ise $5k = 20$, $k = 4$; dik kenarlar $12$ ve $16$ olur.

## 3. Tümler açılar

Dik üçgende iki dar açının toplamı $90^\circ$'dir. Bu iki açıya **tümler açılar** denir.

![A köşesinde dik açı olan üçgen. B köşesinde mavi alfa, C köşesinde kırmızı beta. BC kenarı a, AC kenarı b, AB kenarı c.](gorsel/tyt-matematik/21-03-tumler.svg "b kenarı α'nın karşısında, β'ya ise komşu. Bu yüzden sin α ile cos β aynı oranı verir: b/a.")

**Örnek 4.** $\dfrac{\sin 20^\circ}{\cos 70^\circ} + \tan 35^\circ \cdot \tan 55^\circ$ işleminin sonucu kaçtır?

**Çözüm.** $20^\circ + 70^\circ = 90^\circ$, bu yüzden $\sin 20^\circ = \cos 70^\circ$ ve kesir $1$'dir. $35^\circ + 55^\circ = 90^\circ$, bu yüzden $\tan 55^\circ = \cot 35^\circ$ ve $\tan 35^\circ \cdot \cot 35^\circ = 1$'dir. Sonuç $1 + 1 = 2$. Hiçbir açının değerini bilmen gerekmedi.

**Kural:** $\alpha + \beta = 90^\circ$ ise

$$\sin \alpha = \cos \beta \qquad \cos \alpha = \sin \beta \qquad \tan \alpha = \cot \beta \qquad \cot \alpha = \tan \beta$$

Şekilde: $\sin \alpha = \frac{b}{a} = \cos \beta$ ve $\tan \alpha = \frac{b}{c} = \cot \beta$.

> **Tuzak:** Eşitlik **çapraz** gider: $\sin$ ile $\cos$, $\tan$ ile $\cot$ eşleşir. "$\sin 20^\circ = \sin 70^\circ$" yanlıştır. Toplamı $90^\circ$ olmayan açılarda (örneğin $20^\circ$ ve $60^\circ$) bu kural kullanılmaz.

## 4. Dik açı yoksa dikme indir

Trigonometrik oranlar yalnızca **dik üçgende** yazılır. Açı dik üçgende değilse, bir köşeden dikme indirip dik üçgeni sen oluştur.

**Örnek 5.** $ABC$ üçgeninde $|AB| = |AC| = 10$, $|BC| = 12$'dir. $D$ noktası $[BC]$ üzerinde ve $|BD| = 2$'dir. $m(\widehat{ADC}) = \alpha$ ise $\tan \alpha$ kaçtır?

![Tepesi A olan ikizkenar ABC üçgeni, AB ve AC 10. Taban BC üzerinde soldan B, D, H, C noktaları; BD 2, DH 4, HC 6. A'dan H'ye kırmızı kesikli dikme 8. AD mavi; D'deki alfa açısı ile ADH dik üçgeni sarı boyalı.](gorsel/tyt-matematik/21-03-dikme.svg "Sarı ADH dik üçgeninde α'nın karşısı |AH| = 8, komşusu |DH| = 4.")

**Çözüm.**

1. Üçgen ikizkenar: $A$'dan inen dikme tabanı ortalar. $H$ orta nokta, $|BH| = |HC| = 6$.
2. $AHC$ dik üçgeninde Pisagor: $|AH| = \sqrt{10^2 - 6^2} = 8$.
3. $|DH| = 6 - 2 = 4$. $ADH$ dik üçgeninde $\alpha$'nın karşısı $|AH| = 8$, komşusu $|DH| = 4$:

$$\tan \alpha = \frac{8}{4} = 2$$

**Kural:** Oranı istenen açıyı içine alan bir dik üçgen yoksa, açının bir kolu üzerine dikme indir. Dikme genellikle **ikizkenar üçgende tepeden**, ya da açısı bilinen köşenin karşısından indirilir.

> **Tuzak:** $\tan \alpha = \frac{8}{6}$ ya da $\frac{8}{10}$ yazmak. Kullanılacak dik üçgen $ADH$'dir; komşu kenar $|DC|$ ya da $|HC|$ değil, $|DH|$'dir.

## ÖSYM tuzakları

> **Karşı ile komşuyu karıştırmak.** Kenarlar açıya göre ad alır. Önce açıyı işaretle, sonra karşısındaki kenarı bul.

> **Hipotenüsü yanlış seçmek.** Hipotenüs dik açının karşısındaki kenardır, şekilde en uzun görünen kenar değil. Şekil ölçekli çizilmemiş olabilir.

> **Oranı uzunluk sanmak.** $\sin \alpha = \frac{3}{5}$ ve hipotenüs $20$ ise karşı kenar $3$ değil, $20 \cdot \frac{3}{5} = 12$'dir.

> **Dik olmayan üçgende oran yazmak.** $\tan$ ya da $\sin$ ancak dik üçgende kenar oranıdır. Dik açı yoksa önce dikme indir.

> **Tümler açıda aynı oranı eşitlemek.** $\alpha + \beta = 90^\circ$ ise $\sin \alpha = \cos \beta$; $\sin \alpha = \sin \beta$ değil.

## Kendini dene

### Soru 1
$ABC$ üçgeninde $m(\widehat{B}) = 90^\circ$, $|AB| = 7$ ve $|BC| = 24$ birimdir. $m(\widehat{ACB}) = \alpha$ olduğuna göre $\sin \alpha + \cos \alpha$ toplamı kaçtır?

A) $\frac{7}{25}$
B) $\frac{24}{25}$
C) $\frac{31}{25}$
D) $\frac{31}{24}$
E) $\frac{25}{7}$

**Cevap:** C
**Çözüm:** Hipotenüs $|AC| = \sqrt{7^2 + 24^2} = \sqrt{625} = 25$. $\alpha$, $C$ köşesinde: karşısı $|AB| = 7$, komşusu $|BC| = 24$. $\sin \alpha + \cos \alpha = \frac{7}{25} + \frac{24}{25} = \frac{31}{25}$. A ve B yalnızca bir oranı yazmaktır; D'de payda olarak hipotenüs ($25$) yerine komşu dik kenar ($24$) kullanılmıştır.

### Soru 2
$\alpha$ bir dar açı ve $\tan \alpha = 2{,}4$ olduğuna göre $\cos \alpha$ kaçtır?

A) $\frac{5}{13}$
B) $\frac{5}{12}$
C) $\frac{12}{13}$
D) $\frac{13}{12}$
E) $\frac{12}{5}$

**Cevap:** A
**Çözüm:** $2{,}4 = \frac{12}{5}$: karşı kenar $12k$, komşu kenar $5k$. Hipotenüs $\sqrt{144k^2 + 25k^2} = 13k$. $\cos \alpha = \frac{5k}{13k} = \frac{5}{13}$. C, $\sin \alpha$'dır; B ise $\cot \alpha$'dır.

### Soru 3
Bir dik üçgenin dar açıları $\alpha$ ve $\beta$'dır. $\sin \alpha = \frac{3}{5}$ olduğuna göre $\tan \beta$ kaçtır?

A) $\frac{3}{5}$
B) $\frac{3}{4}$
C) $\frac{4}{5}$
D) $\frac{4}{3}$
E) $\frac{5}{3}$

**Cevap:** D
**Çözüm:** $\alpha + \beta = 90^\circ$ olduğu için $\tan \beta = \cot \alpha$. $\sin \alpha = \frac{3}{5}$: karşı $3$, hipotenüs $5$, komşu $4$. $\cot \alpha = \frac{4}{3}$. B, $\tan \alpha$'dır; tümler açıda $\tan$'ı $\tan$'a eşitleme hatasından gelir.

## Özet kartı

- $\sin = \dfrac{\text{karşı}}{\text{hipotenüs}}$, $\cos = \dfrac{\text{komşu}}{\text{hipotenüs}}$, $\tan = \dfrac{\text{karşı}}{\text{komşu}}$, $\cot = \dfrac{\text{komşu}}{\text{karşı}}$.
- Karşı ve komşu açıya göre değişir; hipotenüs değişmez.
- Tek oran verilirse: iki kenarı $k$ ile yaz, üçüncüyü Pisagor ile bul.
- $\tan \alpha \cdot \cot \alpha = 1$, $\tan \alpha = \dfrac{\sin \alpha}{\cos \alpha}$, $\sin^2 \alpha + \cos^2 \alpha = 1$.
- $\alpha + \beta = 90^\circ$ ise $\sin \alpha = \cos \beta$ ve $\tan \alpha = \cot \beta$.
- Dik üçgen yoksa dikme indirip oluştur.

## Sonraki adım

Alıştırmaya geç (aşağıdaki düğme). Sonraki ders: **30°, 45° ve 60° Derecelerin Trigonometrik Oranları**. Pisagor dersindeki özel dik üçgenleri bugünkü tanımlarla birleştirip bu açıların oranlarını ezbere değil, üçgenden okuyacaksın.
