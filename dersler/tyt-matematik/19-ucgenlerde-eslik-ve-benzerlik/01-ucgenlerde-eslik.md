---
baslik: Üçgenlerde Eşlik
ders: tyt-matematik
sure: 20 dk
kaynak: MEBİ Konu Özeti cde084b5ab
guncelleme: 2026-11-18
---
# Üçgenlerde Eşlik

**Bu dersin sonunda:** iki üçgenin eş olduğunu K.A.K., A.K.A. ya da K.K.K. kuralıyla gösterebilecek, köşeleri doğru eşleyip bilinmeyen kenarı ya da açıyı eş üçgenden okuyabileceksin.

> **TYT'de yeri:** Eşlik nadiren tek başına sorulur; çoğu geometri sorusunun **ilk adımıdır**. Kare içinde, iki dik üçgenin "merdiven" gibi dizildiği şekillerde, kesişen iki doğru parçasında ya da kâğıt katlama sorularında önce "bu iki üçgen eş" dersin, sonra uzunluğu ya da açıyı öbür üçgene taşırsın. Günlük hayat sorularında göl genişliği ölçme, merdiven ya da özdeş karton olarak gelir.

## Önce hatırla

<details><summary>Geçen dersten: Bir üçgenin iki kenarı 5 ve 9 birimdir. Üçüncü kenar bir tam sayı ise kaç farklı değer alabilir?</summary>
$9 - 5 < x < 9 + 5 \Rightarrow 4 < x < 14$. Tam sayılar $5, 6, \dots, 13$: <b>9</b> değer. Üç kenar bir üçgeni kurmaya yetiyor; bugün üç kenarın üçgeni <b>tek biçimde</b> belirlediğini (K.K.K.) göreceksin.
</details>

<details><summary>Geçen dersten: Uzunlukları 3, 4 ve 8 cm olan üç çubukla üçgen kurulabilir mi?</summary>
Kurulamaz: en uzun kenar $8$, öbür ikisinin toplamı $3 + 4 = 7 < 8$. Bugünkü kurallar yalnızca gerçekten kurulabilen üçgenler için geçerlidir.
</details>

## Eş üçgen ne demek?

Biri öbürünün üstüne konunca (gerekirse çevrilip ters yüz edilerek) tam örtüşen iki üçgene **eş üçgenler** denir. $ABC$ ile $DEF$ eşse $\triangle ABC \cong \triangle DEF$ yazılır.

**Örnek 1.** $\triangle ABC \cong \triangle DEF$, $|AB| = 5$, $|BC| = 7$, $|AC| = 6$'dır. $DEF$ üçgeninin kenarlarını bul.

![Solda ABC üçgeni: AB 5, BC 7, AC 6. Sağda aynı üçgenin aynadaki görüntüsü DEF: E sağ altta, F sol altta. Eş kenarlar aynı sayıda çentikle, eş açılar aynı renkli yayla işaretli.](gorsel/tyt-matematik/19-01-esleme.svg "DEF ters yüz edilmiş: E sağda, F solda. Konuma göre değil, harf sırasına göre eşle. Aynı çentik sayısı eş kenarları, aynı renk eş açıları gösterir.")

**Çözüm.** Harf sırası eşlemeyi verir: $A \leftrightarrow D$, $B \leftrightarrow E$, $C \leftrightarrow F$.

| $ABC$'de | $DEF$'de | Uzunluk |
|---|---|---|
| $[AB]$ | $[DE]$ | $5$ |
| $[BC]$ | $[EF]$ | $7$ |
| $[AC]$ | $[DF]$ | $6$ |

Açılar da aynı sırayla eşleşir: $m(\widehat{A}) = m(\widehat{D})$, $m(\widehat{B}) = m(\widehat{E})$, $m(\widehat{C}) = m(\widehat{F})$.

**Kural:** $\triangle ABC \cong \triangle DEF$ ise aynı sırada yazılan köşeler, kenarlar ve açılar birbirine eşittir. Eşliği göstermek için altı eşitliğin hepsi gerekmez: **en az biri kenar olan üç uygun eleman** yeter. Hangi üç elemanın yettiğini aşağıdaki üç kural söyler.

> **Tuzak:** Şekildeki konuma bakıp eşlemek. Sağdaki üçgende sol alt köşe $F$'dir; $B$'nin karşılığı ise $E$'dir. Eşlemeyi her zaman $\cong$ işaretinin iki yanındaki **harf sırasından** oku.

## 1. Kenar – Açı – Kenar (K.A.K.)

**Örnek 2.** Bir gölün iki ucundaki $A$ ve $B$ ağaçları arasını doğrudan ölçemiyorsun. Göl dışında bir $O$ noktası seçiyorsun. $A$'dan $O$'ya 40 m yürüyüp aynı doğrultuda 40 m daha giderek $C$'yi, $B$'den $O$'ya 25 m yürüyüp aynı doğrultuda 25 m daha giderek $D$'yi işaretliyorsun. $|CD| = 52$ m ölçülüyor. $|AB|$ kaç metredir?

![A ile B arasında mavi bir göl. AC ve BD doğru parçaları O'da kesişiyor; AO ile OC 40 m, BO ile OD 25 m. CD yeşil, 52 m. O'daki iki ters açı kırmızı yayla işaretli. AB kesikli, uzunluğu soru işareti.](gorsel/tyt-matematik/19-01-kak.svg "AOB ve COD üçgenlerinde iki kenar eşit (40 ve 25), aradaki açılar ters açı olduğu için eşit. Bu yüzden |AB| = |CD| = 52 m.")

**Çözüm.**

1. $|AO| = |OC| = 40$ m (kenar).
2. $m(\widehat{AOB}) = m(\widehat{COD})$, çünkü ters açılardır (açı).
3. $|BO| = |OD| = 25$ m (kenar).
4. Açı, iki kenarın **arasında**: K.A.K. ile $\triangle AOB \cong \triangle COD$. Eşlemede $A \leftrightarrow C$, $B \leftrightarrow D$, o halde $|AB| = |CD| = 52$ m.

Bonus: $m(\widehat{OAB}) = m(\widehat{OCD})$ çıkar. Bunlar iç ters açılar olduğu için $[AB] \parallel [CD]$'dir.

**Kural:** İki kenarı ve bu iki kenarın **arasındaki** açısı eşit olan üçgenler eştir.

> **Tuzak:** Açı iki kenarın arasında değilse (K.K.A.) eşlik kesin değildir. Örnek: $|AB| = 8$, $|AC| = 5$, $m(\widehat{B}) = 30^\circ$ olan iki farklı üçgen çizilebilir; birinde $|BC| \approx 3{,}9$, öbüründe $|BC| \approx 9{,}9$ olur. "K.K.A." diye bir eşlik kuralı **yoktur**.

## 2. Açı – Kenar – Açı (A.K.A.)

**Örnek 3.** $A$, $B$, $C$ doğrusal; $[DA] \perp [AC]$ ve $[EC] \perp [AC]$. $|DB| = |BE|$ ve $m(\widehat{DBE}) = 90^\circ$'dir. $|AD| = 4$ ve $|CE| = 9$ ise $|AC|$ kaçtır?

![A, B, C yatay bir doğru üzerinde. A'da yukarı dik AD = 4, C'de yukarı dik CE = 9. DB ve BE eşit uzunlukta (çentikli) ve B'de dik açı yapıyor. D'deki ve B'nin sağındaki açı alfa, B'nin solundaki ve E'deki açı beta olarak işaretli.](gorsel/tyt-matematik/19-01-aka.svg "Mavi ve yeşil üçgen eştir: hipotenüsler eşit, uçlarındaki açılar α ve β. Bu yüzden |AB| = |CE| = 9 ve |BC| = |AD| = 4.")

**Çözüm.**

1. $DAB$ dik üçgeninde $m(\widehat{ADB}) = \alpha$ dersen $m(\widehat{ABD}) = 90^\circ - \alpha$.
2. $B$'de doğru açı: $(90^\circ - \alpha) + 90^\circ + m(\widehat{CBE}) = 180^\circ \Rightarrow m(\widehat{CBE}) = \alpha$.
3. $BCE$ dik üçgeninde $m(\widehat{CEB}) = 90^\circ - \alpha$.
4. İki üçgende hipotenüsler eşit ($|DB| = |BE|$) ve hipotenüsün iki ucundaki açılar eşit ($\alpha$ ve $90^\circ - \alpha$): A.K.A. ile $\triangle DAB \cong \triangle BCE$ ($D \leftrightarrow B$, $A \leftrightarrow C$, $B \leftrightarrow E$).
5. $|AB| = |CE| = 9$, $|BC| = |AD| = 4$. Sonuç: $|AC| = 9 + 4 = 13$.

**Kural:** İki açısı ve bu açıların **arasındaki** kenarı eşit olan üçgenler eştir.

İki açı eşitse üçüncü açılar da eşittir ($180^\circ$'den kalan). Bu yüzden iki açı ve **herhangi bir** karşılıklı kenar eşitse de üçgenler eştir; buna A.A.K. de denir.

> **Tuzak:** Üç açının eşit olması (A.A.A.) eşlik **değildir**. Açıları $60^\circ$, $60^\circ$, $60^\circ$ olan kenarı 2 cm ve kenarı 5 cm iki üçgen aynı biçimde ama farklı boydadır. Buna **benzerlik** denir; sonraki dersin konusudur. Kural için en az bir kenar şart.

## 3. Kenar – Kenar – Kenar (K.K.K.)

**Örnek 4.** $ABCD$ dörtgeninde $|AB| = |AD|$ ve $|CB| = |CD|$'dir. $m(\widehat{BAD}) = 70^\circ$ ve $m(\widehat{BCD}) = 50^\circ$ ise $m(\widehat{ABC}) = x$ kaç derecedir?

![Uçurtma biçimli ABCD dörtgeni: AB ve AD tek çentikle, CB ve CD çift çentikle eş işaretli. A'daki açı 70, C'deki açı 50 derece. Kesikli AC köşegeni çizili. B'deki açı x, D'deki açı aynı renkte işaretli.](gorsel/tyt-matematik/19-01-kkk.svg "AC köşegeni iki üçgende ortak. Üç kenar eşit olduğu için ABC ve ADC üçgenleri eş; B ve D'deki açılar da eşit.")

**Çözüm.**

1. $[AC]$ köşegenini çiz. $ABC$ ve $ADC$ üçgenlerinde $|AB| = |AD|$, $|CB| = |CD|$ ve $[AC]$ ortak.
2. K.K.K. ile $\triangle ABC \cong \triangle ADC$. Bu yüzden $m(\widehat{ABC}) = m(\widehat{ADC}) = x$.
3. Dörtgenin iç açıları toplamı $360^\circ$: $70^\circ + 50^\circ + 2x = 360^\circ \Rightarrow x = 120^\circ$.

Ayrıca $[AC]$, hem $\widehat{A}$'yı hem $\widehat{C}$'yi ikiye böler: $m(\widehat{BAC}) = 35^\circ$, $m(\widehat{BCA}) = 25^\circ$. Kontrol: $35^\circ + 120^\circ + 25^\circ = 180^\circ$.

**Kural:** Üç kenarı karşılıklı olarak eşit olan üçgenler eştir. **Ortak kenar** en sık kullanılan "bedava" eşitliktir.

> **Tuzak:** Ortak kenarı fark etmemek. Şekilde iki üçgen bir kenarı paylaşıyorsa o kenar zaten iki üçgende de aynıdır; soruda ayrıca yazılmaz.

## 4. Eş üçgenlerin öbür elemanları

**Örnek 5.** $\triangle ABC \cong \triangle DEF$, $|BC| = 10$ ve $A$'dan $[BC]$'ye inen yükseklik $6$'dır. $D$'den $[EF]$'ye inen yükseklik kaçtır? $DEF$ üçgeninin alanı kaçtır?

![Solda ABC üçgeni: BC 10, A'dan inen mavi yükseklik 6, yeşil kesikli kenarortay. Sağda aynı üçgen 180 derece döndürülmüş DEF: D altta, EF üstte; D'den EF'ye inen mavi yükseklik soru işaretli.](gorsel/tyt-matematik/19-01-yardimci.svg "DEF, ABC'nin döndürülmüş hâli. [BC] ile [EF] eşleşir; bu kenarlara inen yükseklikler (mavi) ve kenarortaylar (yeşil) da eşittir.")

**Çözüm.** $B \leftrightarrow E$, $C \leftrightarrow F$ olduğu için $[BC]$'nin karşılığı $[EF]$'dir: $|EF| = 10$. $A$'nın karşılığı $D$; $A$'dan $[BC]$'ye inen yüksekliğin karşılığı $D$'den $[EF]$'ye inen yüksekliktir: $6$. Alan $\dfrac{10 \cdot 6}{2} = 30$.

**Kural:** Eş iki üçgende karşılıklı **yükseklikler**, **kenarortaylar** ve **açıortaylar** eşittir. Çevreleri ve alanları da eşittir.

> **Tuzak:** Yüksekliği yanlış kenarla eşlemek. $A$'dan inen yüksekliğin karşılığı $D$'den inen yüksekliktir, $E$ ya da $F$'den inen değil.

## ÖSYM tuzakları

> **Konuma göre eşlemek.** Şekilde ters dönmüş üçgende "soldaki köşe soldakine" eşlenmez. $\triangle ABC \cong \triangle KLM$ ise $[BC]$'nin karşılığı $[LM]$'dir; harf sırasını izle.

> **Arada olmayan açı (K.K.A.).** İki kenar ve bunlardan birinin karşısındaki açı eşitse eşlik kesin değildir. Seçeneklerde bu durum, eşliği gösteren bir bilgi gibi karşına çıkar.

> **Üç açı (A.A.A.).** Açıların hepsi eşit ama boyutlar farklı olabilir. Bu benzerliktir, eşlik değil.

> **Gizli eşitlikleri görmemek.** Ters açılar, ortak kenar, karenin eş kenarları ve dik açıları, katlanan kâğıdın iki yarısı: soruda yazmayan bu eşitlikler genelde eşliğin anahtarıdır.

> **Eşliği bulunca durmak.** Soru eşliği değil, eşlikten çıkan bir uzunluğu ya da açıyı ister. "Merdiven" şeklinde $|AC| = |AD| + |CE|$ toplamı sorulur; bir parçayı cevap sanma.

## Kendini dene

### Soru 1
$\triangle ABC \cong \triangle PRS$ ve $|AB| = 7$, $|BC| = 9$, $|CA| = 8$'dir. $|RS|$ kaçtır?

A) 7
B) 8
C) 9
D) 16
E) 24

**Cevap:** C
**Çözüm:** Eşleme harf sırasından: $A \leftrightarrow P$, $B \leftrightarrow R$, $C \leftrightarrow S$. $[RS]$'nin karşılığı $[BC]$'dir: $|RS| = 9$. $7$, $[PR]$'nin karşılığıdır; $24$ ise çevredir.

### Soru 2
$ABC$ ve $DEF$ üçgenleri için aşağıdaki bilgilerden hangisi, iki üçgenin eş olduğunu **kesin olarak göstermez**?

A) $|AB| = |DE|$, $|BC| = |EF|$, $|AC| = |DF|$
B) $|AB| = |DE|$, $m(\widehat{B}) = m(\widehat{E})$, $|BC| = |EF|$
C) $m(\widehat{A}) = m(\widehat{D})$, $|AB| = |DE|$, $m(\widehat{B}) = m(\widehat{E})$
D) $m(\widehat{A}) = m(\widehat{D})$, $m(\widehat{B}) = m(\widehat{E})$, $|BC| = |EF|$
E) $|AB| = |DE|$, $|AC| = |DF|$, $m(\widehat{B}) = m(\widehat{E})$

**Cevap:** E
**Çözüm:** A) K.K.K. B) K.A.K.: $\widehat{B}$, $[AB]$ ile $[BC]$'nin arasında. C) A.K.A.: $[AB]$, $\widehat{A}$ ile $\widehat{B}$'nin arasında. D) İki açı eşitse üçüncü açılar da eşit; $[BC]$, $\widehat{B}$ ile $\widehat{C}$'nin arasında, yani A.K.A. E) $\widehat{B}$, $[AB]$ ile $[AC]$'nin arasında değil (K.K.A.); iki farklı üçgen çizilebilir.

### Soru 3
$ABCD$ dörtgeninde $|AB| = |AD|$ ve $|CB| = |CD|$'dir. $m(\widehat{BAD}) = 84^\circ$ ve $m(\widehat{ABC}) = 110^\circ$ ise $m(\widehat{BCD})$ kaç derecedir?

A) 28
B) 56
C) 70
D) 84
E) 166

**Cevap:** B
**Çözüm:** $[AC]$ ortak olduğu için K.K.K. ile $\triangle ABC \cong \triangle ADC$; $m(\widehat{ADC}) = m(\widehat{ABC}) = 110^\circ$. Dörtgende $84^\circ + 110^\circ + 110^\circ + m(\widehat{BCD}) = 360^\circ \Rightarrow m(\widehat{BCD}) = 56^\circ$. $166^\circ$, $\widehat{D}$'yi hesaba katmamaktır; $28^\circ$ ise $m(\widehat{BCA})$'dır.

## Özet kartı

- $\triangle ABC \cong \triangle DEF$: eşleme harf sırasından okunur, şekildeki konumdan değil.
- K.A.K.: iki kenar ve **aralarındaki** açı.
- A.K.A.: iki açı ve **aralarındaki** kenar (iki açı + herhangi bir karşılıklı kenar da yeter).
- K.K.K.: üç kenar; ortak kenar bedava eşitliktir.
- K.K.A. ve A.A.A. eşlik kuralı **değildir**.
- Eş üçgenlerde karşılıklı yükseklik, kenarortay, açıortay, çevre ve alan eşittir.

## Sonraki adım

Alıştırmaya geç (aşağıdaki düğme). Sonraki ders: **Üçgenlerde Benzerlik**. Orada A.A.A. durumuna geri döneceksin: açıları eşit üçgenlerin kenarları eşit değil, **orantılıdır**.
