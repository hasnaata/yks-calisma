---
baslik: Dikdörtgende Açı ve Uzunluk
ders: tyt-matematik
sure: 20 dk
kaynak: MEBİ Konu Özeti af1f234c19
guncelleme: 2026-11-18
---
# Dikdörtgende Açı ve Uzunluk

<div class="giris" dir="rtl" lang="ar">

**الدرس ده عن إيه؟** عن المستطيل (dikdörtgen): متوازي أضلاع كل زواياه قائمة، وإزاي تحسب فيه الأطوال والزوايا.

- هتعرف إن القطرين (köşegenler) متساويين وبينصّفوا بعض، فبيطلع جوه المستطيل مثلثات متساوية الساقين (ikizkenar üçgen).
- هتتعلم تحسب القطر بفيثاغورس (Pisagor)، وتستخدم نظرية إقليدس (Öklid teoremi) لما ينزل عمود على القطر.
- هتشوف إن منصف الزاوية (açıortay) في المستطيل بيعمل زاوية 45 درجة ومثلث قائم متساوي الساقين.

**ليه مهم؟** المستطيل بييجي كتير في TYT في أسئلة طي الورق (katlama) وأسئلة من الحياة اليومية، وأغلبها بيتحل بالقواعد الأربعة دي.

الدرس ٢٠ دقيقة، وكل قاعدة معاها رسمة ومثال محلول. امسك ورقة وقلم وامشي معانا خطوة بخطوة.

</div>

**Bu dersin sonunda:** dikdörtgende köşegeni Pisagor ile bulabilecek, köşegenlerin oluşturduğu ikizkenar üçgenlerden açı hesaplayabilecek, köşegene inen dikmelerde Öklid bağıntısını ve köşe açıortayının $45^\circ$ özelliğini kullanabileceksin.

> **TYT'de yeri:** Dikdörtgen soruları genelde bir köşegen ya da köşegene inen bir dikme çizer ve bir uzunluk sorar; çözüm Pisagor ve Öklid'dir. Açı sorularında anahtar, köşegenlerin kesim noktasının dört köşeye eşit uzaklıkta olmasıdır. Kâğıt katlama ve bilardo masası gibi günlük hayat soruları da çoğunlukla dikdörtgen üzerine kurulur.

## Önce hatırla

<details><summary>Geçen dersten: Kenarları 8 cm ve 5 cm olan bir paralelkenarda bu iki kenar arasındaki açı 30°'dir. Paralelkenarın alanı kaç cm²'dir?</summary>
Alan = 8 · 5 · sin 30° = 40 · 1/2 = <b>20 cm²</b>. Açı 90° olsaydı sin 90° = 1 olur ve alan 8 · 5 = 40 cm² çıkardı. İşte o paralelkenar bugünün konusu: dikdörtgen.
</details>

<details><summary>Geçen dersten: ABCD paralelkenarının alanı 60 cm²'dir. E noktası [DC] kenarı üzerindedir. A(AEB) kaç cm²'dir?</summary>
E, [DC] üzerinde nerede olursa olsun AEB üçgeninin tabanı [AB], yüksekliği paralelkenarın yüksekliğidir. Bu yüzden A(AEB) paralelkenarın alanının yarısıdır: <b>30 cm²</b>.
</details>

## Dikdörtgen nedir?

Açılarından birinin ölçüsü $90^\circ$ olan paralelkenara **dikdörtgen** denir. Paralelkenarda karşılıklı açılar eşit, ardışık açılar bütünler olduğu için bir açı $90^\circ$ ise **dördü de** $90^\circ$'dir. Dikdörtgen bir paralelkenar olduğundan geçen dersteki bütün özellikler (karşılıklı kenarlar eşit ve paralel, köşegenler birbirini ortalar) burada da geçerlidir.

### 1. Kenarlar, çevre ve köşegen

**Örnek 1.** $ABCD$ dikdörtgeninin çevresi $34$ cm ve $|AB| = 12$ cm'dir. $|AD|$ ve $|AC|$ kaç cm'dir?

![ABCD dikdörtgeni; dört köşede dik açı işareti. AB ve DC kenarlarında 12, AD ve BC kenarlarında 5 yazıyor. Mavi AC köşegeni 13; ABC üçgeni açık maviye boyalı.](gorsel/tyt-matematik/25-07-tanim.svg "Köşegen, mavi ABC dik üçgeninin hipotenüsüdür: 5² + 12² = 13².")

**Çözüm.**

1. Karşılıklı kenarlar eşittir: $|AB| = |DC| = a$, $|AD| = |BC| = b$. Çevre $= 2(a + b)$.
2. $2(12 + b) = 34 \Rightarrow 12 + b = 17 \Rightarrow |AD| = b = 5$ cm.
3. $ABC$ üçgeni $B$'de diktir. Pisagor: $|AC|^2 = 12^2 + 5^2 = 144 + 25 = 169 \Rightarrow |AC| = 13$ cm.

**Kural:** Kenarları $a$ ve $b$ olan dikdörtgende

$$\text{Ç}(ABCD) = 2(a + b), \qquad |AC|^2 = a^2 + b^2$$

> **Tuzak:** Çevreden kenar bulurken ikiye bölmeyi unutmak: $|AD| = 34 - 12 = 22$ yanlıştır. Önce $a + b = 17$ yaz, sonra çıkar.

### 2. Köşegenler eşittir ve birbirini ortalar

**Örnek 2.** $ABCD$ dikdörtgeninde köşegenler $O$ noktasında kesişiyor. $m(\widehat{BAC}) = 28^\circ$ ise $m(\widehat{AOD})$ ve $m(\widehat{ADB})$ kaç derecedir?

![ABCD dikdörtgeni; AC ve BD köşegenleri O'da kesişiyor, dört yarım köşegende aynı çentik. AOB üçgeni mavi, AOD üçgeni yeşil boyalı. A'da BAC açısı 28 derece, B'de ABD açısı 28 derece, O'da AOD açısı 56 derece, D'de ADB açısı 62 derece.](gorsel/tyt-matematik/25-07-kosegenler.svg "Dört yarım köşegen eşit (çentikler). Bu yüzden mavi AOB ve yeşil AOD üçgenleri ikizkenardır: tabandaki açılar eşittir.")

**Çözüm.**

1. Köşegenler eşit ve birbirini ortalıyor, yani $|OA| = |OB|$. $AOB$ üçgeni ikizkenardır: $m(\widehat{OBA}) = m(\widehat{OAB}) = 28^\circ$.
2. $m(\widehat{AOB}) = 180^\circ - 2 \cdot 28^\circ = 124^\circ$. $\widehat{AOD}$ onun bütünleridir: $m(\widehat{AOD}) = 180^\circ - 124^\circ = 56^\circ$.
3. $|OA| = |OD|$ olduğu için $AOD$ de ikizkenardır: $m(\widehat{ODA}) = m(\widehat{OAD}) = \dfrac{180^\circ - 56^\circ}{2} = 62^\circ$. Yani $m(\widehat{ADB}) = 62^\circ$.
4. Kontrol: $A$'daki dik açı $28^\circ + 62^\circ = 90^\circ$.

**Neden eşit?** $ABC$ ve $BAD$ dik üçgenlerinde $[AB]$ ortak, $|BC| = |AD|$ ve aradaki açılar $90^\circ$'dir. Üçgenler eştir (KAK), bu yüzden hipotenüsleri de eşittir: $|AC| = |BD|$. Paralelkenar olduğu için köşegenler birbirini ortalar; eşit iki köşegenin yarıları da eşittir.

**Kural:**

$$|AC| = |BD|, \qquad |OA| = |OB| = |OC| = |OD| = \frac{|AC|}{2}$$

- Köşegen ile kenar arasındaki açı $\alpha$ ise köşegenler arasındaki açılar $2\alpha$ ve $180^\circ - 2\alpha$'dır. Örnekte $2 \cdot 28^\circ = 56^\circ$.
- $O$ dört köşeye eşit uzaklıktadır: dikdörtgenin dört köşesi, merkezi $O$ olan bir çemberin üzerindedir. $ABC$ dik üçgeninde $[BO]$, hipotenüse ait kenarortaydır ve hipotenüsün yarısına eşittir.

> **Tuzak:** Dikdörtgenin köşegenleri **dik kesişmez** (yalnızca karede diktir) ve köşe açısını **ikiye bölmez**. Örnekte $m(\widehat{BAC}) = 28^\circ$, $45^\circ$ değil.

### 3. Köşegene inen dikmeler

**Örnek 3.** $ABCD$ dikdörtgeninde $[BE] \perp [AC]$ ve $[DK] \perp [AC]$'dir ($E$ ve $K$, $[AC]$ üzerinde). $|AE| = 16$ ve $|EC| = 9$ birimdir. $|BE|$, $|AB|$ ve $|KE|$ kaç birimdir?

![ABCD dikdörtgeni ve AC köşegeni. B'den AC'ye kırmızı BE dikmesi, D'den AC'ye kırmızı DK dikmesi; E ve K'de dik açı işareti. ADK ve CBE üçgenleri mavi boyalı. Köşegen üzerinde AK = 9, KE = 7, EC = 9; dikmeler 12 ve 12; AB = 20, BC = 15.](gorsel/tyt-matematik/25-07-dikmeler.svg "Mavi üçgenler (ADK ve CBE) eştir: dikmeler eşit (12 ve 12), köşegenin iki ucundaki parçalar eşit (9 ve 9). Ortadaki parça 16 − 9 = 7.")

**Çözüm.**

1. $ABC$ üçgeni $B$'de diktir ve $[BE]$ hipotenüse inen yüksekliktir. Öklid: $|BE|^2 = |AE| \cdot |EC| = 16 \cdot 9 = 144 \Rightarrow |BE| = 12$.
2. $|AC| = 16 + 9 = 25$. Dik kenar bağıntısı: $|AB|^2 = |AE| \cdot |AC| = 16 \cdot 25 = 400 \Rightarrow |AB| = 20$. Benzer şekilde $|BC|^2 = 9 \cdot 25 = 225$, $|BC| = 15$. Kontrol: $20^2 + 15^2 = 625 = 25^2$.
3. $ADK$ ve $CBE$ üçgenleri eştir: hipotenüsler $|AD| = |CB|$, ve $[AD] \parallel [BC]$ olduğu için $m(\widehat{DAK}) = m(\widehat{BCE})$ (iç ters açılar). Bu yüzden $|DK| = |BE| = 12$ ve $|AK| = |EC| = 9$.
4. $|KE| = |AE| - |AK| = 16 - 9 = 7$.

$|DE|$ ya da $|BK|$ sorulursa son adım Pisagor'dur: $DKE$ dik üçgeninde $|DE|^2 = |DK|^2 + |KE|^2$.

**Kural:** $[BE] \perp [AC]$ ve $[DK] \perp [AC]$ ise

$$|BE|^2 = |AE| \cdot |EC|, \qquad |DK| = |BE|, \qquad |AK| = |EC|$$

> **Tuzak:** Eşit parçaları yanlış eşlemek. Eşit olanlar köşegenin **iki ucundaki** parçalardır: $|AK| = |EC|$. $|AK|$'yi $|AE|$'ye eşit sanma; ortadaki parça $|KE| = |AE| - |EC|$'dir.

### 4. Köşeden çizilen açıortay: $45^\circ$

**Örnek 4.** $ABCD$ dikdörtgeninde $|AB| = 10$ ve $|AD| = 6$ birimdir. $\widehat{A}$'nın açıortayı $[DC]$'yi $K$ noktasında kesiyor. $|KC|$, $|AK|$ ve $m(\widehat{AKC})$ nedir?

![ABCD dikdörtgeni: AB = 10, AD = 6. A'dan çıkan kırmızı açıortay DC'yi K'de kesiyor; A'daki iki yarım açı ve K'deki AKD açısı 45 derece. ADK üçgeni mavi boyalı; AD ve DK üzerinde eşitlik çentiği, ikisi de 6; KC = 4; AK = 6√2.](gorsel/tyt-matematik/25-07-aciortay.svg "Dik açının yarısı 45°'dir. Mavi ADK üçgeni ikizkenar dik üçgendir: |DK| = |AD| = 6 ve |AK| = 6√2.")

**Çözüm.**

1. $\widehat{A}$ dik açıdır, açıortay onu ikiye böler: $m(\widehat{DAK}) = 45^\circ$.
2. $ADK$ üçgeninde $m(\widehat{D}) = 90^\circ$, öyleyse $m(\widehat{AKD}) = 45^\circ$. Üçgen ikizkenar dik üçgendir: $|DK| = |AD| = 6$.
3. $|KC| = |DC| - |DK| = 10 - 6 = 4$.
4. $|AK| = 6\sqrt{2}$ (ikizkenar dik üçgende hipotenüs, dik kenarın $\sqrt{2}$ katı).
5. $m(\widehat{AKC}) = 180^\circ - 45^\circ = 135^\circ$.

**Kural:** Kısa kenar $|AD|$ ise $A$'nın açıortayı uzun kenarı keser ve

$$|DK| = |AD|, \qquad |AK| = |AD| \cdot \sqrt{2}, \qquad m(\widehat{AKD}) = 45^\circ$$

$|AB| < |AD|$ olsaydı açıortay $[BC]$'yi keserdi ve bu kez $|BK| = |AB|$ olurdu: eşit olan, açının **kısa** kolu ile kesilen kenarın köşeye komşu parçasıdır.

> **Tuzak:** Köşegeni açıortay sanmak. $[AC]$, $\widehat{A}$'yı ikiye bölmez (yalnızca karede böler). Açıortay köşegenle değil, $45^\circ$ ile çalışır.

## Hangi kural ne zaman?

| Soruda verilen | Kullanacağın kural |
|---|---|
| Çevre ya da iki kenar | $\text{Ç} = 2(a + b)$, köşegen için Pisagor |
| Köşegenler arasında ya da köşegenle kenar arasında açı | $\lvert OA \rvert = \lvert OB \rvert$: ikizkenar üçgen |
| Köşeden köşegene dikme | $ABC$ dik üçgeninde Öklid |
| İki köşeden köşegene dikme | Eş üçgenler: $\lvert DK \rvert = \lvert BE \rvert$, $\lvert AK \rvert = \lvert EC \rvert$ |
| Köşe açıortayı | $45^\circ$, ikizkenar dik üçgen: $\lvert DK \rvert = \lvert AD \rvert$ |

## ÖSYM tuzakları

> **Çevreyi yarım hesaplamak.** Çevre $2(a + b)$'dir. Seçeneklerde $a + b$ hazır bekler; çevreden kenar bulurken de önce ikiye böl.

> **Köşegenleri dik sanmak.** Köşegenler eşittir ve birbirini ortalar, ama aralarındaki açı genelde $90^\circ$ değildir. $90^\circ$ seçeneği karedeki özelliği dikdörtgene taşımaktır.

> **Köşegeni açıortay sanmak.** Köşegen ile kenar arasındaki açı $45^\circ$ değildir; kenarların oranına bağlıdır. $45^\circ$ yalnızca köşe açıortayında vardır.

> **Dikmelerde parçaları karıştırmak.** İki köşeden köşegene dikme inerse uçtaki parçalar eşittir ($|AK| = |EC|$); ortadaki parça ikisinin farkından bulunur.

> **Katlamada eşit kalanları görmemek.** Kâğıt bir doğru boyunca katlanınca katlanan parçanın kenarları ve açıları değişmez. Köşenin geldiği yeni noktaya olan uzunluk, eski uzunluğa eşittir; sonra bir dik üçgende Pisagor yazılır.

## Kendini dene

### Soru 1
Bir dikdörtgenin çevresi $46$ cm, köşegeninin uzunluğu $17$ cm'dir. Bu dikdörtgenin uzun kenarı kaç cm'dir?

A) 7
B) 8
C) 23/2
D) 15
E) 17

**Cevap:** D
**Çözüm:** $a + b = 23$ ve $a^2 + b^2 = 17^2 = 289$. $(a + b)^2 = a^2 + b^2 + 2ab \Rightarrow 529 = 289 + 2ab \Rightarrow ab = 120$. Toplamı $23$, çarpımı $120$ olan sayılar $8$ ve $15$'tir. Kontrol: $8^2 + 15^2 = 64 + 225 = 289$. Uzun kenar $15$. $8$ kısa kenar, $7$ kenarların farkı, $23/2$ ise kenarları eşit sanmaktır.

### Soru 2
![ABCD dikdörtgeni; köşegenler O'da kesişiyor. O'da BOC açısı 50 derece, A'da köşegen AC ile AB kenarı arasındaki açı x ile gösterilmiş.](gorsel/tyt-matematik/25-07-kd2.svg "Köşegenler O'da kesişiyor.")

Şekildeki $ABCD$ dikdörtgeninde köşegenler $O$ noktasında kesişiyor ve $m(\widehat{BOC}) = 50^\circ$'dir. Buna göre $m(\widehat{OAB}) = x$ kaç derecedir?

A) 25
B) 40
C) 50
D) 65
E) 130

**Cevap:** A
**Çözüm:** $|OB| = |OC|$ olduğundan $m(\widehat{OBC}) = m(\widehat{OCB}) = \dfrac{180^\circ - 50^\circ}{2} = 65^\circ$. $m(\widehat{OBA}) = 90^\circ - 65^\circ = 25^\circ$. $|OA| = |OB|$ olduğundan $x = m(\widehat{OBA}) = 25^\circ$. Kısa yol: köşegenler arası açı $2x$'tir, $2x = 50^\circ$. $65^\circ$, $m(\widehat{OBC})$'dir; $130^\circ$, $m(\widehat{AOB})$'dir; $40^\circ$ ise $90^\circ - 50^\circ$ işleminden gelir.

### Soru 3
![ABCD dikdörtgeni ve AC köşegeni. B'den AC'ye kırmızı BE dikmesi, D'den AC'ye kırmızı DK dikmesi; E ve K'de dik açı işareti. AK = 4, KE = 5; BE soru işaretiyle gösterilmiş.](gorsel/tyt-matematik/25-07-kd3.svg "K ve E, köşegen üzerindedir.")

Şekildeki $ABCD$ dikdörtgeninde $[BE] \perp [AC]$, $[DK] \perp [AC]$, $|AK| = 4$ ve $|KE| = 5$ birimdir. Buna göre $|BE|$ kaç birimdir?

A) $2\sqrt{5}$
B) 5
C) 6
D) $3\sqrt{5}$
E) 9

**Cevap:** C
**Çözüm:** $ADK$ ve $CBE$ eş üçgenlerdir, bu yüzden $|EC| = |AK| = 4$. $|AE| = 4 + 5 = 9$. $ABC$ dik üçgeninde Öklid: $|BE|^2 = |AE| \cdot |EC| = 9 \cdot 4 = 36 \Rightarrow |BE| = 6$. $2\sqrt{5}$, $|AK| \cdot |KE|$ çarpımının köküdür; $3\sqrt{5}$, $|KE| \cdot |AE|$ çarpımının köküdür; $9$ ise $|AE|$'dir.

## Özet kartı

- Dikdörtgen: bir açısı $90^\circ$ olan paralelkenar; dört açısı da diktir.
- Çevre $2(a + b)$; köşegen $\sqrt{a^2 + b^2}$.
- Köşegenler eşit ve birbirini ortalar: $|OA| = |OB| = |OC| = |OD|$; dört ikizkenar üçgen.
- Köşegen ile kenar arası $\alpha$ ise köşegenler arası $2\alpha$ ve $180^\circ - 2\alpha$.
- Köşegene dikme: $|BE|^2 = |AE| \cdot |EC|$; iki dikme varsa $|DK| = |BE|$, $|AK| = |EC|$.
- Köşe açıortayı $45^\circ$ yapar: $|DK| = |AD|$, $|AK| = |AD|\sqrt{2}$.

## Sonraki adım

Alıştırmaya geç (aşağıdaki düğme). Sonraki ders: **Kare**. Kare, dört kenarı eşit bir dikdörtgendir; bugünkü kurallar orada da geçerlidir, üstüne köşegenlerin dik kesişmesi ve köşe açılarını ikiye bölmesi eklenir.
