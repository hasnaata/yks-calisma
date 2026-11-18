---
baslik: Eşkenar Dörtgen
ders: tyt-matematik
sure: 20 dk
kaynak: MEBİ Konu Özeti d9988fb2c3
guncelleme: 2026-11-18
---
# Eşkenar Dörtgen

<div class="giris" dir="rtl" lang="ar">

**الدرس ده عن إيه؟** عن المعيّن (eşkenar dörtgen): متوازي أضلاع (paralelkenar) أضلاعه الأربعة متساوية، وده بيديله خواص زيادة.

- هتعرف إن القطرين (köşegenler) بيقطعوا بعض بزاوية قايمة، وكل واحد بيقسم التاني نصين، وكل قطر بيقسم الزاوية نصين (açıortay).
- هتتعلم تجيب طول الضلع من القطرين بفيثاغورس (Pisagor)، وتعرف إن المعيّن اللي زاويته 60 درجة قطره الصغير بيساوي ضلعه.
- هتحسب المساحة (alan) من القطرين، والارتفاع (yükseklik) من المساحة.

**ليه مهم؟** المعيّن بييجي في TYT كتير، ومعظم أسئلته بتتحل بالمثلث القايم اللي بيطلع لما ترسم القطرين.

الدرس ٢٠ دقيقة، وكل قاعدة معاها رسمة ومثال محلول. امسك ورقة وقلم وامشي معانا خطوة بخطوة.

</div>

**Bu dersin sonunda:** eşkenar dörtgende köşegenlerin dik kesişmesini, birbirini ortalamasını ve açıortay olmasını kullanarak kenar, köşegen, açı, alan ya da yükseklikten istenen birini bulabileceksin.

> **TYT'de yeri:** Eşkenar dörtgen sorularında genelde köşegenler ya da bir açı verilir; kenar, çevre, alan veya bir açı istenir. Hemen hepsinin anahtarı aynıdır: köşegenler eşkenar dörtgeni dört eş dik üçgene böler. $60^\circ$'lik açılı eşkenar dörtgen ("kısa köşegen kenara eşit") da sık gelir.

## Önce hatırla

<details><summary>Geçen dersten: ABCD paralelkenarında köşegenler E noktasında kesişiyor. |AE| = 9 ve |BE| = 5 ise |AC| ve |BD| kaçtır?</summary>
Paralelkenarda köşegenler birbirini ortalar: |AC| = 2 · 9 = <b>18</b>, |BD| = 2 · 5 = <b>10</b>. Köşegenler eşit değildir. Bugün eşkenar dörtgende bu yarım parçaların bir dik üçgenin dik kenarları olduğunu göreceksin.
</details>

<details><summary>Geçen dersten: ABCD paralelkenarında |AB| = 10 ve |AD| = 6. A açısının açıortayı [DC]'yi K noktasında kesiyor. |DK| kaçtır?</summary>
Açıortay paralel kenarla ikizkenar üçgen oluşturur: |DK| = |AD| = <b>6</b>. Bugün şunu soracağız: |AD| ile |DC| eşit olsaydı K nereye düşerdi?
</details>

## Eşkenar dörtgen nedir?

Dört kenarı eşit olan paralelkenara **eşkenar dörtgen** denir. Eşkenar dörtgen bir paralelkenar olduğu için geçen dersteki bütün kurallar burada da geçerlidir. Kenarların eşit olması bunlara üç yeni özellik ekler.

### 1. Kenarlar ve açılar

**Örnek 1.** $ABCD$ eşkenar dörtgeninin çevresi $36$ cm ve $m(\widehat{A}) = 70^\circ$'dir. Kenar uzunluğunu ve öbür açıları bul.

![ABCD eşkenar dörtgeni: dört kenarın her birinde 9 yazıyor ve birer eşitlik çentiği var. A ve C'de mavi 70 derece, B ve D'de kırmızı 110 derece işaretli.](gorsel/tyt-matematik/25-05-tanim.svg "Dört kenar eşit (9 cm). Karşılıklı açılar eşit (mavi 70°, kırmızı 110°); bir mavi ile bir kırmızı açının toplamı 180°.")

**Çözüm.**

1. Dört kenar eşittir: $a = \dfrac{36}{4} = 9$ cm.
2. Ardışık açılar bütünlerdir: $m(\widehat{B}) = 180^\circ - 70^\circ = 110^\circ$.
3. Karşılıklı açılar eşittir: $m(\widehat{C}) = 70^\circ$, $m(\widehat{D}) = 110^\circ$.

**Kural:**

$$|AB| = |BC| = |CD| = |DA| = a, \qquad \text{Çevre} = 4a$$

$$m(\widehat{A}) = m(\widehat{C}), \qquad m(\widehat{B}) = m(\widehat{D}), \qquad m(\widehat{A}) + m(\widehat{B}) = 180^\circ$$

> **Tuzak:** Kenarlar eşit diye açıları da eşit sanmak. Dört açısı da $90^\circ$ olan eşkenar dörtgen **karedir**. Genel eşkenar dörtgende yalnızca karşılıklı açılar eşittir.

### 2. Köşegenler: dik keser, ortalar, açıortaydır

**Örnek 2.** Aynı $ABCD$ eşkenar dörtgeninde ($m(\widehat{A}) = 70^\circ$) köşegenler $E$ noktasında kesişiyor. $m(\widehat{CAB})$, $m(\widehat{ABD})$ ve $m(\widehat{AEB})$ kaçtır?

![ABCD eşkenar dörtgeni: mavi AC ve yeşil BD köşegenleri E'de dik kesişiyor. A'daki açı iki tane 35 derecelik parçaya, B'deki açı iki tane 55 derecelik parçaya bölünmüş. Mavi yarılarda tek çentik, yeşil yarılarda çift çentik.](gorsel/tyt-matematik/25-05-kosegen-aci.svg "Köşegenler E'de dik kesişir ve birbirini ortalar. Her köşegen, geçtiği iki köşedeki açıyı ikiye böler: A'da 35° + 35°, B'de 55° + 55°.")

**Çözüm.**

1. $[AC]$ köşegeni $\widehat{A}$'nın açıortayıdır: $m(\widehat{CAB}) = \dfrac{70^\circ}{2} = 35^\circ$.
2. $[BD]$ köşegeni $\widehat{B}$'nin açıortayıdır: $m(\widehat{B}) = 110^\circ$, $m(\widehat{ABD}) = 55^\circ$.
3. $ABE$ üçgeninde $m(\widehat{AEB}) = 180^\circ - 35^\circ - 55^\circ = 90^\circ$. Köşegenler diktir.

**Neden?**

- **Açıortay:** Geçen dersteki kurala göre $\widehat{A}$'nın açıortayı $[DC]$'yi $K$'de keserse $|DK| = |AD|$ olur. Eşkenar dörtgende $|AD| = |DC|$ olduğu için $K$, $C$'nin ta kendisidir. Yani açıortay $[AC]$ köşegenidir.
- **Diklik:** $ABD$ üçgeninde $|AB| = |AD|$, yani üçgen ikizkenardır. $E$, $[BD]$'nin orta noktasıdır (köşegenler birbirini ortalar). İkizkenar üçgende tepeden tabanın ortasına çizilen doğru tabana diktir: $[AE] \perp [BD]$.

**Kural:**

$$[AC] \perp [BD], \qquad |AE| = |EC|, \qquad |BE| = |ED|$$

$$m(\widehat{CAB}) = \frac{m(\widehat{A})}{2}, \qquad m(\widehat{ABD}) = \frac{m(\widehat{B})}{2}$$

Köşegenler eşkenar dörtgeni **dört eş dik üçgene** böler. Her birinin dar açıları $\dfrac{m(\widehat{A})}{2}$ ve $\dfrac{m(\widehat{B})}{2}$'dir; toplamları $90^\circ$.

> **Tuzak:** Köşegen ile kenar arasındaki açıyı köşe açısı sanmak: $m(\widehat{CAB}) = 35^\circ$'dir, $70^\circ$ değil. Ayrıca köşegenler dik keser ama **eşit değildir**; eşit olmaları yalnızca karede olur.

### 3. Köşegenlerden kenara: Pisagor

**Örnek 3.** $ABCD$ eşkenar dörtgeninde $|AC| = 24$ cm ve $|BD| = 10$ cm'dir. Kenar uzunluğu ve çevre kaçtır?

![Yatay duran ABCD eşkenar dörtgeni: mavi AC köşegeni yatay, yeşil BD köşegeni dikey, E'de kesişiyorlar. AE ve EC üzerinde 12, EB ve ED üzerinde 5 yazıyor. AEB dik üçgeni pembe boyalı, AB kenarında kırmızı 13 yazıyor.](gorsel/tyt-matematik/25-05-kosegen-uzunluk.svg "Pembe AEB üçgeni dik üçgendir: dik kenarları köşegenlerin yarıları (12 ve 5), hipotenüsü eşkenar dörtgenin kenarıdır (13).")

**Çözüm.**

1. Köşegenler birbirini ortalar: $|AE| = 12$, $|BE| = 5$.
2. Köşegenler diktir: $AEB$ bir dik üçgendir, hipotenüsü $[AB]$.
3. $|AB|^2 = 12^2 + 5^2 = 169 \Rightarrow |AB| = 13$ cm. Çevre $= 4 \cdot 13 = 52$ cm.

**Kural:** Köşegenler $e$ ve $f$, kenar $a$ ise

$$a^2 = \left(\frac{e}{2}\right)^2 + \left(\frac{f}{2}\right)^2$$

> **Tuzak:** Pisagor'u köşegenlerin **tamamıyla** yapmak: $\sqrt{24^2 + 10^2} = 26$, kenarın iki katıdır. Önce ikiye böl. Sık çıkan dik üçgenler: 3-4-5, 5-12-13, 8-15-17, 7-24-25 ve bunların katları.

### 4. 60°'lik eşkenar dörtgen: kısa köşegen kenara eşit

**Örnek 4.** $ABCD$ eşkenar dörtgeninde kenar $8$ cm ve $m(\widehat{A}) = 60^\circ$'dir. $|BD|$ ve $|AC|$ kaçtır?

![ABCD eşkenar dörtgeni, kenarları 8. A'da 60 derece. ABD üçgeni mavi boyalı; köşeleri A, B ve D'de 60 derece işaretli, BD köşegeni mavi ve üzerinde 8 yazıyor. Gri kesikli AC köşegeni üzerinde 8 kök 3 yazıyor.](gorsel/tyt-matematik/25-05-altmis.svg "Mavi ABD üçgeninin üç açısı da 60°: eşkenar üçgendir, bu yüzden kısa köşegen BD kenara eşittir (8). Uzun köşegen AC, 8√3'tür.")

**Çözüm.**

1. $ABD$ üçgeninde $|AB| = |AD| = 8$ ve aradaki açı $60^\circ$. Taban açıları $\dfrac{180^\circ - 60^\circ}{2} = 60^\circ$: üçgen **eşkenardır**. $|BD| = 8$ cm.
2. $|BE| = 4$. $AEB$ dik üçgeninde $|AE|^2 = 8^2 - 4^2 = 48 \Rightarrow |AE| = 4\sqrt{3}$.
3. $|AC| = 2 \cdot 4\sqrt{3} = 8\sqrt{3}$ cm.

**Kural:** Açılardan biri $60^\circ$ (öbürü $120^\circ$) ise eşkenar dörtgen iki eşkenar üçgenden oluşur:

$$\text{kısa köşegen} = a, \qquad \text{uzun köşegen} = a\sqrt{3}$$

Tersi de doğrudur: kısa köşegen kenara eşitse dar açı $60^\circ$'dir.

> **Tuzak:** Kısa köşegen $120^\circ$'lik köşeleri birleştirir (burada $B$ ile $D$). Soru "$m(\widehat{B}) = 120^\circ$" derse $60^\circ$ yine $A$'dadır ve kenara eşit olan yine $[BD]$'dir. Uzun köşegeni kenara eşitleme.

### 5. Alan ve yükseklik

**Örnek 5.** $ABCD$ eşkenar dörtgeninin köşegenleri $16$ cm ve $12$ cm'dir. Alanı, kenarı ve yüksekliği kaçtır?

![ABCD eşkenar dörtgeni: gri kesikli köşegenler üzerinde 16 ve 12, AB kenarında 10 yazıyor. D'den AB'ye kırmızı DH dikmesi, D'den BC'ye kırmızı DK dikmesi; ikisinin üzerinde de h yazıyor, H ve K'de dik açı işareti var.](gorsel/tyt-matematik/25-05-alan.svg "İki kırmızı yükseklik eşittir (h = 9,6). Alan iki yoldan aynı çıkar: köşegenlerle 16 · 12 / 2, kenar ve yükseklikle 10 · h.")

**Çözüm.**

1. Köşegenler dört eş dik üçgen oluşturur; dik kenarları $8$ ve $6$, her birinin alanı $\dfrac{8 \cdot 6}{2} = 24$. Toplam alan $4 \cdot 24 = 96$ cm². Kısa yol: $\dfrac{16 \cdot 12}{2} = 96$.
2. Kenar: $a^2 = 8^2 + 6^2 = 100 \Rightarrow a = 10$ cm.
3. Eşkenar dörtgen bir paralelkenardır, alanı taban · yüksekliktir: $10 \cdot h = 96 \Rightarrow h = 9{,}6$ cm.
4. $|DH|$ ($[AB]$'ye inen) ile $|DK|$ ($[BC]$'ye inen) eşittir: tabanlar eşit ($10$), alan aynı, yani yükseklikler de aynı.

**Kural:** Köşegenler $e$ ve $f$, kenar $a$, yükseklik $h$ ise

$$A(ABCD) = \frac{e \cdot f}{2} = a \cdot h$$

Eşkenar dörtgenin bütün yükseklikleri eşittir.

> **Tuzak:** İkiye bölmeyi unutmak ($16 \cdot 12 = 192$). Yüksekliği köşegenin yarısıyla ($6$ ya da $8$) karıştırmak da sık yapılır: yükseklik **kenara** diktir, köşegene değil.

## Hangi kural ne zaman?

| Soruda verilen | Kullanacağın kural |
|---|---|
| Çevre ya da bir kenar | Dört kenar eşit: $a = \dfrac{\text{Çevre}}{4}$ |
| Bir açı | Karşılıklılar eşit, ardışıklar $180^\circ$; köşegen açıyı ikiye böler |
| İki köşegen | Yarıları dik üçgenin dik kenarları: Pisagor ile kenar |
| Kenar ve bir köşegen | Pisagor ile öbür köşegenin yarısı |
| $60^\circ$ ya da $120^\circ$ | Kısa köşegen $= a$, uzun köşegen $= a\sqrt{3}$ |
| Alan veya yükseklik | $\dfrac{e \cdot f}{2} = a \cdot h$ |

## ÖSYM tuzakları

> **Pisagor'u tam köşegenlerle yapmak.** Kenar, köşegenlerin **yarılarıyla** kurulan dik üçgenin hipotenüsüdür. Tam köşegenlerle bulunan sayı kenarın iki katıdır ve seçeneklerde hazır bekler.

> **Köşegenleri eşit sanmak.** Eşkenar dörtgenin köşegenleri dik kesişir ve birbirini ortalar, ama eşit değildir. Eşit köşegen karede olur.

> **Alanda ikiye bölmeyi unutmak.** $\dfrac{e \cdot f}{2}$; $e \cdot f$ seçeneklerde iki katı olarak durur.

> **Köşegen–kenar açısını köşe açısıyla karıştırmak.** Köşegen köşedeki açıyı ikiye böler. $m(\widehat{A}) = 70^\circ$ ise $m(\widehat{CAB}) = 35^\circ$'dir.

> **$60^\circ$'de yanlış köşegen.** Kenara eşit olan **kısa** köşegendir ($120^\circ$'lik köşeleri birleştirir). Uzun köşegen $a\sqrt{3}$'tür.

## Kendini dene

### Soru 1
$ABCD$ eşkenar dörtgeninde $m(\widehat{A}) = (2x + 20)^\circ$ ve $m(\widehat{B}) = (3x + 10)^\circ$'dir. Buna göre $m(\widehat{ABD})$ kaç derecedir?

A) 30
B) 40
C) 50
D) 80
E) 100

**Cevap:** C
**Çözüm:** $\widehat{A}$ ile $\widehat{B}$ ardışıktır: $(2x + 20) + (3x + 10) = 180 \Rightarrow 5x = 150 \Rightarrow x = 30$. $m(\widehat{A}) = 80^\circ$, $m(\widehat{B}) = 100^\circ$. $[BD]$ köşegeni $\widehat{B}$'nin açıortayıdır: $m(\widehat{ABD}) = 50^\circ$. $30$, $x$'in kendisidir; $40$, $\widehat{A}$'nın yarısıdır; $80$ ve $100$ açıların tamamıdır (ikiye bölmeyi unutmak).

### Soru 2
Bir eşkenar dörtgenin bir kenarı $25$ cm, köşegenlerinden biri $14$ cm'dir. Bu eşkenar dörtgenin alanı kaç cm²'dir?

A) 168
B) 336
C) 350
D) 600
E) 672

**Cevap:** B
**Çözüm:** Verilen köşegenin yarısı $7$. Öbür köşegenin yarısı: $25^2 - 7^2 = 625 - 49 = 576 \Rightarrow 24$. Öbür köşegen $48$. Alan $= \dfrac{14 \cdot 48}{2} = 336$. $672$, ikiye bölmeyi unutmaktır; $168$ yarım köşegenlerin çarpımıdır ($7 \cdot 24$); $350$ ($25 \cdot 14$) ve $600$ ($25 \cdot 24$), kenarı bir köşegenle ya da yarısıyla çarpmaktır.

### Soru 3
$ABCD$ eşkenar dörtgeninde kenar $6$ cm ve $m(\widehat{B}) = 120^\circ$'dir. Bu eşkenar dörtgenin uzun köşegeni kaç cm'dir?

A) $3\sqrt{3}$
B) $6$
C) $6\sqrt{2}$
D) $6\sqrt{3}$
E) $12$

**Cevap:** D
**Çözüm:** $m(\widehat{B}) = 120^\circ$ ise $m(\widehat{A}) = 60^\circ$. $ABD$ üçgeni eşkenardır: kısa köşegen $|BD| = 6$. $|BE| = 3$, $|AE|^2 = 6^2 - 3^2 = 27 \Rightarrow |AE| = 3\sqrt{3}$. Uzun köşegen $|AC| = 6\sqrt{3}$. $6$ kısa köşegendir; $3\sqrt{3}$ uzun köşegenin yarısıdır; $6\sqrt{2}$, karenin köşegenidir.

## Özet kartı

- Dört kenar eşit: çevre $4a$. Karşılıklı açılar eşit, ardışık açılar $180^\circ$.
- Köşegenler dik keser ve birbirini ortalar; ama eşit değildir.
- Her köşegen geçtiği köşelerdeki açıları ikiye böler (açıortaydır).
- Kenar: $a^2 = \left(\dfrac{e}{2}\right)^2 + \left(\dfrac{f}{2}\right)^2$.
- $60^\circ$ açıda kısa köşegen $= a$, uzun köşegen $= a\sqrt{3}$.
- Alan $= \dfrac{e \cdot f}{2} = a \cdot h$; bütün yükseklikler eşit.

## Sonraki adım

Alıştırmaya geç (aşağıdaki düğme). Sonraki ders: **Paralelkenarın Alanı**. Bugün kullandığın "alan = taban · yükseklik" fikri orada her paralelkenar için genişletilecek.
