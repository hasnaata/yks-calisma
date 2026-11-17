---
baslik: 30°, 45° ve 60°'nin Trigonometrik Oranları
ders: tyt-matematik
sure: 20 dk
kaynak: MEBİ Konu Özeti 08d4da8df9
guncelleme: 2026-11-18
---
# 30°, 45° ve 60°'nin Trigonometrik Oranları

<div class="giris" dir="rtl" lang="ar">

**الدرس ده عن إيه؟** عن النسب المثلثية للزوايا الخاصة (özel açılar): 30 و 45 و 60 درجة، اللي هتقابلها في مسائل كتير جدًا.

- هتطلّع قيم الجيب وجيب التمام والظل وظل التمام (sinüs, kosinüs, tanjant, kotanjant) من مثلث متساوي الأضلاع (eşkenar üçgen) ومن المربع (kare)، من غير حفظ أعمى.
- هتعرف طريقة سهلة تفتكر بيها الجدول كله، وتفرّق بين 30 و 60 من غير لخبطة.
- هتتعلم تنزّل عمود (dikme) في مثلث مش قائم عشان تقسمه لمثلثين خاصين وتحسب الضلع الناقص.

**ليه مهم؟** الزوايا دي هي الأكتر استخدامًا في TYT، سواء في سؤال حسابي مباشر أو في موقف من الحياة زي سلم أو ضل أو منحدر، وأكتر غلطة إن الطالب يحط قيمة 30 مكان 60.

الدرس ٢٠ دقيقة بس، وبعده الزوايا دي هتبقى في جيبك. يلا بينا.

</div>

**Bu dersin sonunda:** $30^\circ$, $45^\circ$ ve $60^\circ$'nin sinüs, kosinüs, tanjant ve kotanjant değerlerini eşkenar üçgenden ve kareden birkaç saniyede çıkarıp bir dik üçgende eksik kenarı ya da bir ifadenin değerini bulabileceksin.

> **TYT'de yeri:** Bu üç açı TYT'de en sık kullanılan açılardır. Soru ya doğrudan "$\sin 30^\circ + \tan 60^\circ \cdot \cos 30^\circ$ kaçtır?" diye gelir ya da merdiven, kule, gölge, rampa gibi bir günlük hayat durumunda bir açı $30^\circ$, $45^\circ$ veya $60^\circ$ verilir ve bir uzunluk istenir. Değerleri yanlış yere koymak (sin 30° ile sin 60°'yi karıştırmak) en sık puan kaybıdır.

## Önce hatırla

<details><summary>Geçen dersten: Bir dik üçgende α dar açısının karşısındaki dik kenar 8, hipotenüs 17 birimdir. cos α ve tan α kaçtır?</summary>
Komşu dik kenar: √(17² − 8²) = √225 = 15. Buradan <b>cos α = 15/17</b> ve <b>tan α = 8/15</b>. Bugün aynı tanımları, kenarlarını bildiğin özel üçgenlere uygulayacaksın.
</details>

<details><summary>Geçen dersten: cos 40° − sin 50° farkı kaçtır?</summary>
40° + 50° = 90°, yani bu iki açı tümlerdir ve cos 40° = sin 50°. Fark <b>0</b>. Bugün aynı kuralı sin 30° = cos 60° ve tan 30° = cot 60° eşitliklerinde göreceksin.
</details>

## 1. 30° ve 60°: eşkenar üçgeni ikiye böl

**Örnek 1.** Kenarı $2$ birim olan $ABC$ eşkenar üçgeninde $A$'dan $[BC]$'ye $[AH]$ yüksekliği iniyor. $ABH$ üçgenini kullanarak $30^\circ$ ve $60^\circ$'nin oranlarını bul.

![Kenarları 2 olan ABC eşkenar üçgeni. A'dan BC'ye AH yüksekliği iniyor; H'de dik açı. Sol yarıdaki ABH üçgeni mavi boyalı: AB = 2, BH = 1, AH = kök 3. B'de 60 derece, A'da AB ile AH arasında 30 derece.](gorsel/tyt-matematik/21-04-eskenar.svg "Yükseklik eşkenar üçgeni iki eş dik üçgene ayırır. Mavi üçgende 30° karşısı 1, 60° karşısı √3, hipotenüs 2.")

**Çözüm.**

1. Eşkenar üçgenin her açısı $60^\circ$'dir. Yükseklik hem tabanı hem tepe açısını ikiye böler: $|BH| = 1$ ve $m(\widehat{BAH}) = 30^\circ$.
2. Pisagor: $|AH| = \sqrt{2^2 - 1^2} = \sqrt{3}$.
3. $30^\circ$ $A$ köşesinde: karşısı $|BH| = 1$, komşusu $|AH| = \sqrt{3}$, hipotenüs $2$.

$$\sin 30^\circ = \frac{1}{2} \qquad \cos 30^\circ = \frac{\sqrt{3}}{2} \qquad \tan 30^\circ = \frac{1}{\sqrt{3}} = \frac{\sqrt{3}}{3} \qquad \cot 30^\circ = \sqrt{3}$$

4. $60^\circ$ $B$ köşesinde: karşısı $|AH| = \sqrt{3}$, komşusu $|BH| = 1$.

$$\sin 60^\circ = \frac{\sqrt{3}}{2} \qquad \cos 60^\circ = \frac{1}{2} \qquad \tan 60^\circ = \sqrt{3} \qquad \cot 60^\circ = \frac{\sqrt{3}}{3}$$

**Kural:** $30^\circ$–$60^\circ$–$90^\circ$ üçgeninin kenarları $1 : \sqrt{3} : 2$'dir. $30^\circ$'nin karşısı en kısa kenar ($1$), $60^\circ$'nin karşısı $\sqrt{3}$, hipotenüs $2$. $30^\circ + 60^\circ = 90^\circ$ olduğu için oranlar çapraz eşittir:

$$\sin 30^\circ = \cos 60^\circ \qquad \sin 60^\circ = \cos 30^\circ \qquad \tan 30^\circ = \cot 60^\circ \qquad \tan 60^\circ = \cot 30^\circ$$

> **Tuzak:** $\sin 60^\circ$, $\sin 30^\circ$'nin iki katı **değildir**: $2 \cdot \frac{1}{2} = 1$ ama $\sin 60^\circ = \frac{\sqrt{3}}{2}$. Açı iki katına çıkınca oran iki katına çıkmaz.

## 2. 45°: kareyi köşegenle böl

**Örnek 2.** Kenarı $1$ birim olan $ABCD$ karesinde $[AC]$ köşegeni çiziliyor. $ABC$ üçgeninden $45^\circ$'nin oranlarını bul.

![Kenarı 1 olan ABCD karesi. AC köşegeni çizilmiş; ABC üçgeni yeşil boyalı. AB = 1, BC = 1, AC = kök 2. B'de dik açı, A'da ve C'de 45 derece.](gorsel/tyt-matematik/21-04-kare.svg "Köşegen kareyi iki eş ikizkenar dik üçgene böler. Dik kenarlar eşit (1 ve 1), hipotenüs √2.")

**Çözüm.**

1. Köşegen karenin dik açılarını ikiye böler: $m(\widehat{BAC}) = m(\widehat{BCA}) = 45^\circ$.
2. Pisagor: $|AC| = \sqrt{1^2 + 1^2} = \sqrt{2}$.
3. $45^\circ$ $A$ köşesinde: karşısı $|BC| = 1$, komşusu $|AB| = 1$, hipotenüs $\sqrt{2}$.

$$\sin 45^\circ = \cos 45^\circ = \frac{1}{\sqrt{2}} = \frac{\sqrt{2}}{2} \qquad \tan 45^\circ = \cot 45^\circ = \frac{1}{1} = 1$$

**Kural:** $45^\circ$–$45^\circ$–$90^\circ$ üçgeninin kenarları $1 : 1 : \sqrt{2}$'dir. $45^\circ$'nin tümleri yine $45^\circ$ olduğu için sinüs ile kosinüs, tanjant ile kotanjant eşittir.

> **Tuzak:** $\frac{1}{\sqrt{2}}$ ile $\frac{\sqrt{2}}{2}$ aynı sayıdır (pay ve paydayı $\sqrt{2}$ ile genişlet). Seçeneklerde paydası köklü sayı genelde yazılmaz; $\frac{\sqrt{2}}{2}$ ve $\frac{\sqrt{3}}{3}$ biçimini tanı.

## 3. Tablo ve kolay hatırlama yolu

Üç üçgeni **hipotenüs $2$ olacak** biçimde yan yana koy. Açı büyüdükçe karşı kenar $1$, $\sqrt{2}$, $\sqrt{3}$ diye büyür; komşu kenar aynı sayılarla küçülür.

![Hipotenüsü 2 olan üç dik üçgen yan yana. Mavi 30 derecelik üçgende karşı kenar 1, komşu kenar kök 3. Yeşil 45 derecelik üçgende karşı ve komşu kenar kök 2. Kırmızı 60 derecelik üçgende karşı kenar kök 3, komşu kenar 1. Altlarında sin 30 = 1/2, sin 45 = kök 2 bölü 2, sin 60 = kök 3 bölü 2 yazıyor.](gorsel/tyt-matematik/21-04-ayni-hipotenus.svg "Hipotenüs hep 2. Dikey kenar 1, √2, √3 diye uzar (sinüs artar); yatay kenar √3, √2, 1 diye kısalır (kosinüs azalır).")

**Örnek 3.** $\dfrac{\sin 60^\circ \cdot \tan 30^\circ + \cos 60^\circ}{\tan 45^\circ}$ işleminin sonucu kaçtır?

**Çözüm.**

1. $\sin 60^\circ \cdot \tan 30^\circ = \dfrac{\sqrt{3}}{2} \cdot \dfrac{\sqrt{3}}{3} = \dfrac{3}{6} = \dfrac{1}{2}$.
2. Pay: $\dfrac{1}{2} + \cos 60^\circ = \dfrac{1}{2} + \dfrac{1}{2} = 1$.
3. Payda: $\tan 45^\circ = 1$. Sonuç $\dfrac{1}{1} = 1$.

**Kural (tablo):**

| Açı | $\sin$ | $\cos$ | $\tan$ | $\cot$ |
|---|---|---|---|---|
| $30^\circ$ | $\frac{1}{2}$ | $\frac{\sqrt{3}}{2}$ | $\frac{\sqrt{3}}{3}$ | $\sqrt{3}$ |
| $45^\circ$ | $\frac{\sqrt{2}}{2}$ | $\frac{\sqrt{2}}{2}$ | $1$ | $1$ |
| $60^\circ$ | $\frac{\sqrt{3}}{2}$ | $\frac{1}{2}$ | $\sqrt{3}$ | $\frac{\sqrt{3}}{3}$ |

- **Sinüs satırı:** $\dfrac{\sqrt{1}}{2}$, $\dfrac{\sqrt{2}}{2}$, $\dfrac{\sqrt{3}}{2}$. **Kosinüs** aynı sayıları tersten sıralar.
- **Tanjant** $= \dfrac{\sin}{\cos}$: $30^\circ$'de küçük ($\frac{\sqrt{3}}{3}$), $45^\circ$'de $1$, $60^\circ$'de büyük ($\sqrt{3}$). **Kotanjant** bunların tersidir.
- Unutursan tabloyu ezberden değil, eşkenar üçgenden ve kareden yeniden kur: 20 saniye sürer.

> **Tuzak:** $\tan 30^\circ$ ile $\tan 60^\circ$'yi karıştırmak. Küçük açının tanjantı küçüktür: $\tan 30^\circ = \frac{\sqrt{3}}{3} \approx 0{,}58$, $\tan 60^\circ = \sqrt{3} \approx 1{,}73$.

## 4. Üçgende kullanmak: dikme indir, özel üçgen oluştur

**Örnek 4.** $ABC$ üçgeninde $m(\widehat{B}) = 45^\circ$, $m(\widehat{C}) = 30^\circ$ ve $|AC| = 8$ birimdir. $|BC|$ kaç birimdir?

![ABC üçgeni: B'de 45, C'de 30 derece, AC = 8. A'dan BC'ye kırmızı kesikli AH dikmesi iniyor, H'de dik açı. AH = 4, BH = 4, HC = 4 kök 3.](gorsel/tyt-matematik/21-04-dikme.svg "Dikme üçgeni iki özel dik üçgene ayırır: solda 45°–45°–90°, sağda 30°–60°–90°. Ortak kenar AH = 4 iki üçgeni bağlar.")

**Çözüm.** $ABC$ dik üçgen değil; $A$'dan $[BC]$'ye $[AH]$ dikmesini indir.

1. $AHC$ dik üçgeninde $30^\circ$ $C$'de, hipotenüs $|AC| = 8$:
   $|AH| = 8 \cdot \sin 30^\circ = 8 \cdot \frac{1}{2} = 4$ ve $|HC| = 8 \cdot \cos 30^\circ = 8 \cdot \frac{\sqrt{3}}{2} = 4\sqrt{3}$.
2. $ABH$ dik üçgeninde $45^\circ$ $B$'de: $\tan 45^\circ = \dfrac{|AH|}{|BH|} = 1$, yani $|BH| = |AH| = 4$.
3. $|BC| = |BH| + |HC| = 4 + 4\sqrt{3}$.

**Kural:** Bir kenar ve özel bir açı biliniyorsa:

$$\text{karşı} = \text{hipotenüs} \cdot \sin \alpha \qquad \text{komşu} = \text{hipotenüs} \cdot \cos \alpha \qquad \text{karşı} = \text{komşu} \cdot \tan \alpha$$

Özel açı bir dik üçgende değilse, iki parçaya bölen dikmeyi sen indir. Dikme, iki üçgende **ortak** kenar olur.

> **Tuzak:** $|BC|$'yi $8 \cdot \cos 30^\circ$ diye tek adımda bulmak. $[BC]$ hipotenüsü $[AC]$ olan bir dik üçgenin kenarı değildir; önce dikmeyle iki dik üçgene ayırmak gerekir.

## ÖSYM tuzakları

> **30° ile 60°'yi karıştırmak.** Hipotenüsün yarısı $30^\circ$'nin **karşısındaki** kenardır. $\sin 30^\circ = \frac{1}{2}$, $\cos 30^\circ = \frac{\sqrt{3}}{2}$. Seçeneklerde iki değer de hazır bekler.

> **Açıyı ikiyle çarpınca oranı da ikiyle çarpmak.** $\sin 60^\circ \neq 2 \sin 30^\circ$, $\tan 60^\circ \neq 2 \tan 30^\circ$. Önce açıyı bul, sonra tablodan oku.

> **İşlem önceliğini atlamak.** $2\sin 30^\circ + \tan 45^\circ \cdot \cos 60^\circ$ ifadesinde önce çarpmalar yapılır: $1 + \frac{1}{2} = \frac{3}{2}$. Soldan sağa giderek $(1 + 1) \cdot \frac{1}{2} = 1$ yazmak yanlıştır.

> **Karesini almayı unutmak.** $\sin^2 45^\circ = \left(\frac{\sqrt{2}}{2}\right)^2 = \frac{2}{4} = \frac{1}{2}$; $\frac{\sqrt{2}}{4}$ değil.

> **Dik açısız üçgende oran yazmak.** Oranlar yalnızca dik üçgende kenar oranıdır. Açı ve kenar farklı üçgenlerdeyse önce dikme indir.

## Kendini dene

### Soru 1
$\dfrac{\tan 60^\circ \cdot \cos 30^\circ}{\sin 30^\circ}$ işleminin sonucu kaçtır?

A) $\frac{3}{4}$
B) $\frac{3}{2}$
C) $\sqrt{3}$
D) $3$
E) $2\sqrt{3}$

**Cevap:** D
**Çözüm:** Pay: $\sqrt{3} \cdot \dfrac{\sqrt{3}}{2} = \dfrac{3}{2}$. Payda: $\sin 30^\circ = \dfrac{1}{2}$. Sonuç $\dfrac{3}{2} : \dfrac{1}{2} = 3$. B, paydayı unutmaktır; A, $\frac{1}{2}$ ile bölmek yerine çarpmaktır.

### Soru 2
$ABC$ üçgeninde $m(\widehat{B}) = 90^\circ$, $m(\widehat{C}) = 60^\circ$ ve $|BC| = 5$ birimdir. $|AB|$ kaç birimdir?

A) $\frac{5\sqrt{3}}{3}$
B) $5$
C) $5\sqrt{3}$
D) $10$
E) $10\sqrt{3}$

**Cevap:** C
**Çözüm:** $60^\circ$ $C$ köşesinde: karşısı $[AB]$, komşusu $[BC] = 5$. $\tan 60^\circ = \dfrac{|AB|}{5} = \sqrt{3}$, yani $|AB| = 5\sqrt{3}$. Kontrol: $[BC]$, $30^\circ$'nin ($A$'nın) karşısında, en kısa kenar; hipotenüs $10$, $25 + 75 = 100$. A, $\tan 30^\circ$ kullanmaktır; D hipotenüs $|AC|$'dir.

### Soru 3
Bir dik üçgende dar açılardan birinin kosinüsü $\dfrac{\sqrt{3}}{2}$'dir. Hipotenüs $12$ birim ise bu açının karşısındaki dik kenar kaç birimdir?

A) $4$
B) $6$
C) $4\sqrt{3}$
D) $6\sqrt{2}$
E) $6\sqrt{3}$

**Cevap:** B
**Çözüm:** $\cos \alpha = \dfrac{\sqrt{3}}{2}$ ise $\alpha = 30^\circ$. Karşı kenar $= 12 \cdot \sin 30^\circ = 12 \cdot \dfrac{1}{2} = 6$. E, açının **komşu** kenarıdır ($12 \cdot \frac{\sqrt{3}}{2}$); D ise $45^\circ$ sanmaktır.

## Özet kartı

- $30^\circ$–$60^\circ$–$90^\circ$: kenarlar $1 : \sqrt{3} : 2$ (eşkenar üçgenin yarısı). $45^\circ$–$45^\circ$–$90^\circ$: $1 : 1 : \sqrt{2}$ (karenin yarısı).
- $\sin$: $\frac{1}{2}$, $\frac{\sqrt{2}}{2}$, $\frac{\sqrt{3}}{2}$ ($30^\circ$, $45^\circ$, $60^\circ$); $\cos$ aynı sayıları tersten sıralar.
- $\tan$: $\frac{\sqrt{3}}{3}$, $1$, $\sqrt{3}$; $\cot$ bunların tersi.
- Tümler açılar: $\sin 30^\circ = \cos 60^\circ$, $\tan 30^\circ = \cot 60^\circ$; $45^\circ$'de $\sin = \cos$, $\tan = \cot = 1$.
- Karşı $=$ hipotenüs $\cdot \sin$, komşu $=$ hipotenüs $\cdot \cos$, karşı $=$ komşu $\cdot \tan$.
- Dik üçgen yoksa dikme indir; dikme iki özel üçgenin ortak kenarı olur.

## Sonraki adım

Alıştırmaya geç (aşağıdaki düğme). Sonraki ders: **Birim Çember**. Orada bugünkü değerleri yarıçapı $1$ olan bir çember üzerinde noktaların koordinatları olarak göreceksin.
