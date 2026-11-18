---
baslik: Deltoid
ders: tyt-matematik
sure: 20 dk
kaynak: MEBİ Konu Özeti 600e5c8c35
guncelleme: 2026-11-18
---
# Deltoid

<div class="giris" dir="rtl" lang="ar">

**الدرس ده عن إيه؟** عن الطيارة الورق! الشكل ده اسمه الدلتويد (deltoid): شكل رباعي فيه زوجين من الأضلاع المتجاورة، وكل زوج ضلعينه متساويين.

- هتعرف إن القطر الرئيسي (ana köşegen) هو محور التماثل (simetri ekseni)، وإن الزاويتين اللي على الجنبين متساويتين.
- هتتعلم إن القطرين متعامدين (dik)، وإن القطر الرئيسي بيقسم القطر التاني نصين، بس هو نفسه مش متقسم نصين.
- هتحسب المساحة (alan) من القطرين في خطوة واحدة، وهتشوف الحالة اللي فيها زاويتين قايمتين (dik açı).

**ليه مهم؟** الدلتويد بييجي في TYT لوحده أو مستخبي جوه شبه منحرف (yamuk) أو مربع، والحل دايمًا بيبدأ من التماثل والقطرين المتعامدين.

الدرس ٢٠ دقيقة، وكل قاعدة معاها رسمة ومثال محلول. هات ورقة وقلم ويلا بينا.

</div>

**Bu dersin sonunda:** bir deltoidde simetri eksenini görüp eş açıları yazabilecek, köşegenlerin dikliğinden Pisagor kurarak uzunluk bulabilecek ve alanı köşegenlerden $\dfrac{|AC| \cdot |BD|}{2}$ ile hesaplayabileceksin.

> **TYT'de yeri:** Deltoid soruları ya doğrudan gelir (köşegen, kenar, açı ya da alan istenir) ya da bir yamuğun veya karenin içine gizlenir. Çözüm hemen her zaman iki bilgiyle başlar: köşegenler diktir ve ana köşegen simetri eksenidir. Uçurtma gibi günlük hayat sorularında alan $\dfrac{e \cdot f}{2}$ ile bir adımda bulunur.

## Önce hatırla

<details><summary>Geçen dersten: Çevresi 14 cm, köşegeni 5 cm olan bir dikdörtgenin alanı kaç cm²'dir?</summary>
$a + b = 7$, $a^2 + b^2 = 25$. $(a + b)^2 = a^2 + b^2 + 2ab \Rightarrow 49 = 25 + 2ab \Rightarrow ab =$ <b>12 cm²</b> (kenarlar 3 ve 4). Bugün alanı yine köşegenlerden bulacaksın, ama bu kez çok daha kısa bir yoldan.
</details>

<details><summary>Geçen dersten: Dikdörtgenin alanı neden köşegen karesinin yarısı (e²/2) ile hesaplanamaz?</summary>
Çünkü $\dfrac{e \cdot f}{2}$ türü formüller yalnızca köşegenleri <b>dik</b> olan dörtgenlerde çalışır; dikdörtgenin köşegenleri eşittir ama dik değildir. Deltoidin köşegenleri ise diktir; bu yüzden bugün alan $\dfrac{|AC| \cdot |BD|}{2}$ olacak.
</details>

## Deltoid nedir?

Komşu kenarları ikişer ikişer eşit olan dörtgene **deltoid** denir. Bu derste hep aynı adlandırmayı kullanacağız: $|AB| = |AD|$ (alttaki iki kenar) ve $|CB| = |CD|$ (üstteki iki kenar).

- Eşit kenarların buluştuğu köşeler $A$ ve $C$'dir. Onları birleştiren $[AC]$'ye **ana köşegen** diyeceğiz; öbür köşegen $[BD]$'dir.
- Dört kenarı da eşit olan deltoid **eşkenar dörtgendir**; kare de bir deltoiddir. Yani eşkenar dörtgen ve karede öğrendiğin köşegen kuralları deltoidin özel hâlleridir.
- Deltoid genelde paralelkenar **değildir**: karşılıklı kenarları eşit ya da paralel olmak zorunda değildir.

## 1. Simetri ekseni ve eş açılar

**Örnek 1.** $ABCD$ deltoidinde $|AB| = |AD|$, $|CB| = |CD|$, $m(\widehat{DAB}) = 50^\circ$ ve $m(\widehat{DCB}) = 110^\circ$'dir. $m(\widehat{ABC})$ kaç derecedir?

![ABCD deltoidi: A altta, C üstte, D solda, B sağda. AB ve AD tek çentikle, CB ve CD çift çentikle eşit işaretli. A'da 50 derece, C'de 110 derece; B ve D'deki açılar x ile işaretli. AC kesikli mavi çizgi, simetri ekseni yazıyor.](gorsel/tyt-matematik/25-10-tanim.svg "AC boyunca katlarsan B, D'nin üstüne düşer. Bu yüzden B ile D'deki x açıları eşittir; A ile C'deki açılar eşit değildir.")

**Çözüm.**

1. $ABC$ ve $ADC$ üçgenlerinde $|AB| = |AD|$, $|CB| = |CD|$ ve $[AC]$ ortak kenardır. Üç kenarı eşit olduğu için bu iki üçgen eştir (K.K.K.).
2. Eş üçgenlerde karşılık gelen açılar eşittir: $m(\widehat{ABC}) = m(\widehat{ADC}) = x$.
3. Dörtgenin iç açıları toplamı $360^\circ$: $50^\circ + 110^\circ + 2x = 360^\circ \Rightarrow 2x = 200^\circ \Rightarrow x = 100^\circ$.

**Kural:** $|AB| = |AD|$ ve $|CB| = |CD|$ ise $[AC]$ deltoidin **simetri eksenidir**:

$$m(\widehat{ABC}) = m(\widehat{ADC}), \qquad [AC] \text{ hem } \widehat{A}\text{'nın hem } \widehat{C}\text{'nin açıortayıdır.}$$

> **Tuzak:** Eşit olan açılar, **farklı** uzunluktaki kenarların buluştuğu $B$ ve $D$ köşelerindedir. Eşit kenarların buluştuğu $A$ ile $C$'deki açılar genelde farklıdır ($50^\circ$ ve $110^\circ$). "Karşılıklı açılar eşittir" diye $A$ ile $C$'yi eşitlemek en sık yapılan hatadır.

## 2. Köşegenler: dik, ama yalnızca biri ortalanır

**Örnek 2.** $ABCD$ deltoidinde $|AB| = |AD| = 13$ cm, $|CB| = |CD| = 15$ cm ve $|BD| = 24$ cm'dir. Köşegenler $K$ noktasında kesişiyor. $|AC|$ kaç cm'dir?

![ABCD deltoidi: AB ve AD 13, CB ve CD 15. BD köşegeni yatay, K noktasında AC köşegenine dik; DK = KB = 12. AC mavi: AK = 5, KC = 9. K'de dik açı işareti.](gorsel/tyt-matematik/25-10-kosegenler.svg "K, BD'nin orta noktasıdır (12 ve 12), ama AC'nin orta noktası değildir (5 ve 9). Dört küçük üçgenin hepsi K'de dik açılıdır.")

**Çözüm.**

1. Köşegenler diktir ve $[AC]$, $[BD]$'yi ortalar: $|DK| = |KB| = \dfrac{24}{2} = 12$.
2. $AKB$ dik üçgeni: $|AK|^2 = 13^2 - 12^2 = 25 \Rightarrow |AK| = 5$.
3. $CKB$ dik üçgeni: $|CK|^2 = 15^2 - 12^2 = 81 \Rightarrow |CK| = 9$.
4. $|AC| = 5 + 9 = 14$ cm.

**Kural:** Deltoidde köşegenler $K$'de kesişirse

$$[AC] \perp [BD], \qquad |DK| = |KB| = \frac{|BD|}{2}$$

Neden? $ABD$ üçgeni ikizkenardır ($|AB| = |AD|$) ve $[AK]$ tepe açısının açıortayıdır. İkizkenar üçgende tepe açısının açıortayı tabana diktir ve tabanı ortalar. Köşegenler deltoidi **dört dik üçgene** böler; uzunluk sorularının hepsi bu dik üçgenlerde Pisagor ile çözülür.

> **Tuzak:** $K$'yi $[AC]$'nin de orta noktası sanmak. Ortalanan yalnızca $[BD]$'dir. $|AK| = |KC|$ olsaydı dört kenar eşit olur, şekil eşkenar dörtgen olurdu. Örnekte $|AC| = 2 \cdot 5 = 10$ ya da $2 \cdot 9 = 18$ yazmak yanlıştır.

## 3. Alan: köşegenlerin çarpımının yarısı

**Örnek 3.** Örnek 2'deki deltoidin ($|AC| = 14$ cm, $|BD| = 24$ cm) alanı kaç cm²'dir?

![Kenarları 24 ve 14 olan kesikli sarı bir dikdörtgenin içine köşeleri kenarlara değen ABCD deltoidi çizilmiş. Deltoidin içinde 168 yazıyor. K, B, C üçgeni koyu mavi ve içinde 54; dışında B, köşe, C üçgeni koyu sarı ve içinde 54.](gorsel/tyt-matematik/25-10-alan.svg "Deltoidin içindeki her dik üçgenin dışarıda bir eşi var (mavi 54 ile sarı 54). Bu yüzden deltoid, köşegenlerin kurduğu dikdörtgenin tam yarısıdır.")

**Çözüm.**

1. Köşegenler deltoidi dört dik üçgene böler. $[AC]$ ortak taban gibi düşünülürse deltoid, $ABC$ ve $ADC$ üçgenlerinin birleşimidir.
2. $A(ABC) = \dfrac{|AC| \cdot |KB|}{2} = \dfrac{14 \cdot 12}{2} = 84$, $A(ADC) = \dfrac{14 \cdot 12}{2} = 84$.
3. $A(ABCD) = 84 + 84 = 168$ cm².
4. Kısa yol: $\dfrac{|AC| \cdot |BD|}{2} = \dfrac{14 \cdot 24}{2} = 168$.

**Kural:**

$$A(ABCD) = \frac{|AC| \cdot |BD|}{2}$$

Bu formül köşegenleri **dik** olan her dörtgende çalışır: deltoid, eşkenar dörtgen ($\frac{e \cdot f}{2}$) ve kare ($\frac{e^2}{2}$) bunun özel hâlleridir. Dikdörtgende ve genel paralelkenarda çalışmaz.

> **Tuzak:** İkiye bölmeyi unutmak ($14 \cdot 24 = 336$, köşegenlerin kurduğu dikdörtgenin alanıdır) ya da kenarları çarpmak ($13 \cdot 15 = 195$). Deltoidde kenarlar arasındaki açı genelde dik değildir; kenarların çarpımı alanı vermez.

## 4. İki dik açılı deltoid

$B$ ve $D$'deki eş açılar $90^\circ$ ise deltoid, hipotenüsü ortak iki eş dik üçgenden oluşur.

**Örnek 4.** $ABCD$ deltoidinde $|AB| = |AD| = 8$ cm, $|CB| = |CD| = 6$ cm ve $m(\widehat{ABC}) = m(\widehat{ADC}) = 90^\circ$'dir. Deltoidin alanını ve $|BD|$'yi bulunuz.

![ABCD deltoidi: AB ve AD 8, CB ve CD 6; B ve D'de dik açı işareti. ABC üçgeni mavi, ADC üçgeni yeşil boyalı. Kesikli AC köşegeni 10, noktalı BD köşegeni yatay.](gorsel/tyt-matematik/25-10-dik.svg "Mavi ve yeşil, hipotenüsü AC olan iki eş dik üçgendir. Her birinin alanı 8 · 6 / 2 = 24; ikisi birlikte 48.")

**Çözüm.**

1. $ABC$ dik üçgeni: $|AC|^2 = 8^2 + 6^2 = 100 \Rightarrow |AC| = 10$ cm.
2. Alan: iki eş dik üçgen, $2 \cdot \dfrac{8 \cdot 6}{2} = 8 \cdot 6 = 48$ cm².
3. $|BD|$'yi alan formülünden bul: $\dfrac{|AC| \cdot |BD|}{2} = 48 \Rightarrow \dfrac{10 \cdot |BD|}{2} = 48 \Rightarrow |BD| = 9{,}6$ cm.
4. Kontrol: $[BK]$, $ABC$ dik üçgeninde hipotenüse ait yüksekliktir: $|BK| = \dfrac{8 \cdot 6}{10} = 4{,}8$, $|BD| = 2 \cdot 4{,}8 = 9{,}6$.

**Kural:** $m(\widehat{B}) = m(\widehat{D}) = 90^\circ$ ise

$$A(ABCD) = |AB| \cdot |BC|, \qquad |AC|^2 = |AB|^2 + |BC|^2, \qquad |BD| = \frac{2 \cdot |AB| \cdot |BC|}{|AC|}$$

> **Tuzak:** Alanı $\dfrac{|AB| \cdot |BC|}{2} = 24$ yazmak. Bu yalnızca bir dik üçgendir; deltoidde iki tane vardır. $|BD|$ için de $|BK| = 4{,}8$'de durma; $K$, $[BD]$'nin orta noktasıdır, $|BD| = 9{,}6$.

## 5. Yamuk içindeki deltoid: açıortay ile paralel

Ana köşegen bir açıortaydır. Bu açıortay bir de paralel doğrularla kesişirse ikizkenar üçgen doğar.

**Örnek 5.** Şekilde $ABCD$ bir yamuk, $[AB] \parallel [DC]$ ve $E \in [AD]$'dir. $DEBC$ bir deltoiddir: $|DE| = |DC| = 5$ cm ve $|BE| = |BC|$. $|AE| = 7$ cm ise $|AB| = x$ kaç cm'dir?

![ABCD yamuğu: DC üst taban 5, AB alt taban x. E noktası AD kenarı üzerinde; DE = 5, AE = 7. DEBC deltoidi mavi boyalı, EB çizilmiş. Kırmızı DB köşegeni; D'de EDB ve BDC açıları, B'de ABD açısı α ile işaretli.](gorsel/tyt-matematik/25-10-yamuk.svg "Üç α eşittir: ikisi deltoidin açıortayından, biri DC ile AB'nin paralelliğinden (iç ters açı). Bu yüzden ADB üçgeni ikizkenardır.")

**Çözüm.**

1. $DEBC$ deltoidinde eşit kenarlar $D$'de ($|DE| = |DC|$) ve $B$'de ($|BE| = |BC|$) buluşur; ana köşegen $[DB]$'dir. $[DB]$, $\widehat{EDC}$'nin açıortayıdır: $m(\widehat{EDB}) = m(\widehat{BDC}) = \alpha$.
2. $[DC] \parallel [AB]$ ve $[DB]$ kesen olduğundan $\widehat{BDC}$ ile $\widehat{ABD}$ iç ters açıdır: $m(\widehat{ABD}) = \alpha$.
3. $ADB$ üçgeninde $D$ ve $B$'deki açıların ikisi de $\alpha$: üçgen ikizkenardır, $|AB| = |AD|$.
4. $|AD| = |AE| + |ED| = 7 + 5 = 12 \Rightarrow x = 12$ cm.

**Kural:** Bir açıortay, açının bir koluna paralel bir doğruyu keserse ikizkenar üçgen oluşur. Deltoidin ana köşegeni bir açıortay olduğu için, şekilde paralel kenarlar varsa önce bu ikizkenar üçgeni ara.

> **Tuzak:** $|AB|$'yi $|AE|$ ya da $|DE|$ ile eşitlemek. Eşit olan, $|AB|$ ile $[AD]$'nin **tamamıdır**: $|AD| = |AE| + |ED|$. Bir de ana köşegeni yanlış seçmek: $DEBC$'de eşit kenarlar $D$ ve $B$'de buluşur; açıortay olan $[DB]$'dir, $[EC]$ değil.

## Hangi kural ne zaman?

| Soruda verilen | Kullanacağın kural |
|---|---|
| Açılar | $B$ ve $D$'deki açılar eşit; toplam $360^\circ$ |
| Kenarlar ve bir köşegen | Köşegenler dik, $[BD]$ ortalanır: dik üçgende Pisagor |
| İki köşegen | Alan $= \dfrac{\lvert AC \rvert \cdot \lvert BD \rvert}{2}$ |
| $B$ ve $D$ dik açı | Alan $= \lvert AB \rvert \cdot \lvert BC \rvert$; $\lvert BD \rvert$ alandan |
| Deltoid + paralel kenar | Ana köşegen açıortay: ikizkenar üçgen ara |

## ÖSYM tuzakları

> **Yanlış açıları eşitlemek.** Deltoidde eşit olan açılar, farklı kenarların buluştuğu iki köşededir ($B$ ve $D$). $A$ ile $C$'deki açılar eşit değildir.

> **İki köşegeni de ortalamak.** Yalnızca $[BD]$ ortalanır. $|AK| = |KC|$ demek, deltoidi eşkenar dörtgene çevirmektir.

> **Köşegenin yarısını unutmak.** $|BD| = 24$ verilince dik üçgende $24$ değil $12$ kullanılır. Tersine, $|KB|$ bulunca soru $|BD|$'yi istiyorsa ikiyle çarp.

> **Alanda ikiye bölmeyi unutmak.** $|AC| \cdot |BD|$ köşegenlerin kurduğu dikdörtgenin alanıdır; deltoid bunun yarısıdır.

> **Dik açılı deltoidde yalnızca bir üçgen almak.** $|AB| \cdot |BC|$ iki dik üçgenin toplamıdır; $\dfrac{|AB| \cdot |BC|}{2}$ yalnızca yarısıdır.

## Kendini dene

### Soru 1
$ABCD$ deltoidinde $|AB| = |AD|$ ve $|CB| = |CD|$'dir. $m(\widehat{BCD}) = 80^\circ$ ve $m(\widehat{ABC}) = 120^\circ$ ise $m(\widehat{DAB})$ kaç derecedir?

A) 40
B) 60
C) 80
D) 120
E) 160

**Cevap:** A
**Çözüm:** $B$ ve $D$'deki açılar eşittir: $m(\widehat{ADC}) = 120^\circ$. $m(\widehat{DAB}) = 360^\circ - 80^\circ - 120^\circ - 120^\circ = 40^\circ$. $160^\circ$, $D$'deki açıyı unutmaktır ($360^\circ - 80^\circ - 120^\circ$); $80^\circ$, $A$ ile $C$'yi eşit sanmaktır; $120^\circ$, $B$'nin kendisidir; $60^\circ$ ise $120^\circ$'nin bütünleridir.

### Soru 2
![ABCD deltoidi: AB ve AD 10, CB ve CD 17. BD köşegeni yatay, uzunluğu 16. AC mavi köşegen soru işaretiyle gösterilmiş; köşegenler K'de kesişiyor.](gorsel/tyt-matematik/25-10-kd2.svg "Şekil ölçeklidir.")

Şekildeki $ABCD$ deltoidinde $|AB| = |AD| = 10$ birim, $|CB| = |CD| = 17$ birim ve $|BD| = 16$ birimdir. Buna göre $|AC|$ kaç birimdir?

A) 6
B) 9
C) 15
D) 21
E) 27

**Cevap:** D
**Çözüm:** $|KB| = 8$. $AKB$ dik üçgeni: $|AK| = \sqrt{100 - 64} = 6$. $CKB$ dik üçgeni: $|CK| = \sqrt{289 - 64} = 15$. $|AC| = 6 + 15 = 21$. $6$ ve $15$ yalnızca birer parçadır; $9$, iki parçanın farkıdır; $27$, iki kenarın toplamıdır ($10 + 17$).

### Soru 3
![ABCD deltoidi: AB ve AD 12, CB ve CD 5; B ve D'de dik açı işareti. Kesikli AC köşegeni, mavi BD köşegeni soru işaretiyle gösterilmiş.](gorsel/tyt-matematik/25-10-kd3.svg "Şekil ölçeklidir.")

Şekildeki $ABCD$ deltoidinde $|AB| = |AD| = 12$ cm, $|CB| = |CD| = 5$ cm ve $m(\widehat{ABC}) = m(\widehat{ADC}) = 90^\circ$'dir. Buna göre $|BD|$ kaç cm'dir?

A) $\dfrac{60}{13}$
B) 5
C) $\dfrac{120}{13}$
D) 12
E) 13

**Cevap:** C
**Çözüm:** $|AC| = \sqrt{144 + 25} = 13$. Alan $= 12 \cdot 5 = 60$. $\dfrac{13 \cdot |BD|}{2} = 60 \Rightarrow |BD| = \dfrac{120}{13}$. $\dfrac{60}{13}$, $|BK|$'de durmaktır (yarısı); $13$ ise $|AC|$'dir.

## Özet kartı

- Deltoid: $|AB| = |AD|$ ve $|CB| = |CD|$. Eşkenar dörtgen ve kare özel deltoiddir.
- $[AC]$ simetri eksenidir: $m(\widehat{B}) = m(\widehat{D})$; $[AC]$, $\widehat{A}$ ile $\widehat{C}$'nin açıortayıdır.
- $[AC] \perp [BD]$ ve $|DK| = |KB|$; $[AC]$ ise ortalanmaz.
- Alan $= \dfrac{|AC| \cdot |BD|}{2}$.
- $B$ ve $D$ dik ise alan $= |AB| \cdot |BC|$ ve $|BD| = \dfrac{2 \cdot |AB| \cdot |BC|}{|AC|}$.
- Deltoid + paralel kenar: ana köşegen açıortaydır, ikizkenar üçgen ara.

## Sonraki adım

Alıştırmaya geç (aşağıdaki düğme). Bu ders **Özel Dörtgenler** konusunun son dersidir. Sonraki konu **Katı Cisimler**: orada dikdörtgen, kare ve yamuğun alanlarını prizmaların taban ve yüzeylerinde yeniden kullanacaksın.
