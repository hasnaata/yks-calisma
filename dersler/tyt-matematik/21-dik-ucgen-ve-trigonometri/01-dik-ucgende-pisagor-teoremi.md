---
baslik: Dik Üçgende Pisagor Teoremi
ders: tyt-matematik
sure: 25 dk
kaynak: MEBİ Konu Özeti e9eb52be47
guncelleme: 2026-11-18
---
# Dik Üçgende Pisagor Teoremi

**Bu dersin sonunda:** bir dik üçgende iki kenar verildiğinde üçüncüsünü Pisagor teoremiyle ya da özel dik üçgenleri tanıyarak hesaplayabileceksin.

> **TYT'de yeri:** Pisagor teoremi geometri sorularının çoğunda bir ara adımdır: dikdörtgenin köşegeni, merdiven, iki direk arası ip, karenin köşegeni. $3$–$4$–$5$, $5$–$12$–$13$ ya da $30^\circ$–$60^\circ$–$90^\circ$ üçgenini hemen tanımak sana sınavda dakikalar kazandırır.

## Önce hatırla

<details><summary>Geçen dersten: ABC dik üçgeninde m(B) = 90° ve |AC| = 14 birimdir. Kenar orta dikmelerin kesiştiği K noktasının B köşesine uzaklığı kaç birimdir?</summary>
Dik üçgende kenar orta dikmeler <b>hipotenüsün orta noktasında</b> kesişir. K noktası üç köşeye eşit uzaklıktadır: |KA| = |KB| = |KC| = 14 / 2 = <b>7</b>. Bugün hipotenüsü kenarlardan nasıl hesaplayacağını göreceksin.
</details>

<details><summary>Geçen dersten: P noktası [BC] kenarının orta dikmesi üzerindedir ve |PB| = 9 birimdir. |PC| kaç birimdir?</summary>
Kenar orta dikme üzerindeki her nokta kenarın iki ucuna eşit uzaklıktadır: |PC| = <b>9</b>. Bu eşitliği kanıtlarken iki dik üçgen kullanılır; bugünkü teorem de dik üçgenin kenarları arasındaki bağıntıdır.
</details>

## Dik üçgende adlar

Bir açısı $90^\circ$ olan üçgene **dik üçgen** denir. Dik açının karşısındaki kenar **hipotenüs**tür; dik açıyı oluşturan iki kenar **dik kenar**dır. Hipotenüs, dik üçgenin her zaman **en uzun** kenarıdır.

## 1. Pisagor teoremi

**Örnek 1.** $ABC$ üçgeninde $m(\widehat{B}) = 90^\circ$, $|AB| = 6$ ve $|BC| = 8$ birimdir. $|AC|$ kaçtır?

**Çözüm.** $[AC]$ dik açının karşısında, yani hipotenüs.

$$|AC|^2 = 6^2 + 8^2 = 36 + 64 = 100 \Rightarrow |AC| = 10$$

**Örnek 2.** Bir dik üçgenin hipotenüsü $9$, bir dik kenarı $6$ birimdir. Öbür dik kenar kaçtır?

**Çözüm.** Bu kez bilinmeyen bir dik kenar. Hipotenüsün karesinden çıkar:

$$x^2 = 9^2 - 6^2 = 81 - 36 = 45 \Rightarrow x = \sqrt{45} = 3\sqrt{5}$$

![Dik kenarları 3 ve 4, hipotenüsü 5 olan ABC dik üçgeni. Her kenarın dışına bir kare çizilmiş: AB üstündeki yeşil karede 3 kare eşittir 9, BC altındaki mavi karede 4 kare eşittir 16, hipotenüs üstündeki kırmızı karede 5 kare eşittir 25 yazıyor.](gorsel/tyt-matematik/21-01-pisagor-kareler.svg "Dik kenarlar üzerindeki iki karenin alanları toplamı (9 + 16), hipotenüs üzerindeki karenin alanına (25) eşittir.")

**Kural:** Dik kenarlar $a$ ve $b$, hipotenüs $c$ ise

$$a^2 + b^2 = c^2$$

- Hipotenüs isteniyorsa kareleri **topla**, dik kenar isteniyorsa hipotenüsün karesinden **çıkar**.
- Kökten çıkan sayıyı sadeleştir: $\sqrt{45} = \sqrt{9 \cdot 5} = 3\sqrt{5}$.
- Tersi de doğrudur: kenarları $a^2 + b^2 = c^2$ eşitliğini sağlayan üçgen diktir; dik açı en uzun kenarın karşısındadır.

> **Tuzak:** "Dik üçgenin iki kenarı $6$ ve $10$" denip hangisinin hipotenüs olduğu söylenmiyorsa iki durum vardır. $10$ hipotenüsse üçüncü kenar $8$, ikisi de dik kenarsa üçüncü kenar $\sqrt{136} = 2\sqrt{34}$ olur. Uzun kenarı hemen hipotenüs sanma.

## 2. Kenarları tam sayı olan özel dik üçgenler

**Örnek 3.** Bir dik üçgenin dik kenarları $15$ ve $20$ birimdir. Hipotenüs kaçtır?

**Çözüm (uzun yol).** $15^2 + 20^2 = 225 + 400 = 625 \Rightarrow c = 25$.

**Çözüm (kısa yol).** $15 = 3 \cdot 5$, $20 = 4 \cdot 5$. Bu bir $3$–$4$–$5$ üçgenidir ($k = 5$): hipotenüs $5 \cdot 5 = 25$.

**Örnek 4.** Hipotenüsü $26$, bir dik kenarı $10$ olan dik üçgenin öbür dik kenarı kaçtır?

**Çözüm.** $10 = 5 \cdot 2$, $26 = 13 \cdot 2$. Bu bir $5$–$12$–$13$ üçgenidir ($a = 2$): öbür dik kenar $12 \cdot 2 = 24$. Kontrol: $26^2 - 10^2 = 676 - 100 = 576 = 24^2$.

![Dört dik üçgen: kenarları 3k, 4k, 5k olan mavi üçgen; 8x, 15x, 17x olan yeşil üçgen; 5a, 12a, 13a olan sarı üçgen; 7b, 24b, 25b olan kırmızı üçgen. Her birinde dik açı sol alt köşede.](gorsel/tyt-matematik/21-01-ozel-tam.svg "Her üçgende en büyük sayı hipotenüstür. Kenarlar aynı sayıyla çarpılınca üçgen yine dik kalır.")

**Kural:** Şu üçlüleri ve katlarını ezbere tanı:

| Dik kenarlar | Hipotenüs | Katları (örnek) |
|---|---|---|
| $3k$, $4k$ | $5k$ | $6$–$8$–$10$, $9$–$12$–$15$, $12$–$16$–$20$ |
| $5a$, $12a$ | $13a$ | $10$–$24$–$26$ |
| $8x$, $15x$ | $17x$ | $16$–$30$–$34$ |
| $7b$, $24b$ | $25b$ | $14$–$48$–$50$ |

> **Tuzak:** Üçlüyü tanırken sayıların **yerine** bak. Kenarları $12$ ve $13$ olan dik üçgende $13$ hipotenüsse öbür dik kenar $5$'tir. Ama $12$ ve $13$ ikisi de dik kenarsa hipotenüs $\sqrt{313}$ olur. Hangi kenarın dik açının karşısında olduğunu soru ya da şekil söyler.

## 3. Açılarına göre özel dik üçgenler

**Örnek 5 (30°–60°–90°).** $ABC$ üçgeninde $m(\widehat{B}) = 90^\circ$, $m(\widehat{A}) = 30^\circ$ ve $|AC| = 12$ birimdir. $|BC|$ ve $|AB|$ kaçtır?

**Çözüm.** $30^\circ$'nin karşısındaki kenar hipotenüsün yarısıdır: $|BC| = 6$. $60^\circ$'nin karşısındaki kenar bunun $\sqrt{3}$ katıdır: $|AB| = 6\sqrt{3}$. Kontrol: $6^2 + (6\sqrt{3})^2 = 36 + 108 = 144 = 12^2$.

**Örnek 6 (45°–45°–90°).** Bir karenin köşegeni $8$ birimdir. Karenin bir kenarı kaçtır?

**Çözüm.** Köşegen kareyi iki ikizkenar dik üçgene böler. Hipotenüs $= \text{kenar} \cdot \sqrt{2}$:

$$a\sqrt{2} = 8 \Rightarrow a = \frac{8}{\sqrt{2}} = \frac{8\sqrt{2}}{2} = 4\sqrt{2}$$

**Örnek 7 (15°–75°–90°).** Dar açıları $15^\circ$ ve $75^\circ$ olan dik üçgenin hipotenüsü $20$ birimdir. Hipotenüse ait yükseklik kaçtır?

**Çözüm.** Bu üçgende hipotenüse ait yükseklik hipotenüsün dörtte biridir: $20 : 4 = 5$.

![Üç dik üçgen. Mavi 30-60-90 üçgeni: 30 derecenin karşısı a, 60 derecenin karşısı a kök 3, hipotenüs 2a. Yeşil 45-45-90 üçgeni: dik kenarlar a, hipotenüs a kök 2. Kırmızı 15-75-90 üçgeni: hipotenüs LM 4a, K köşesinden inen KH yüksekliği a.](gorsel/tyt-matematik/21-01-ozel-aci.svg "Açılar kenarları belirler: 30° karşısı a, 60° karşısı a√3, 45° karşısı a, 15°–75° üçgeninde yükseklik hipotenüsün dörtte biri.")

**Kural:**

| Üçgen | Kenarlar |
|---|---|
| $30^\circ$–$60^\circ$–$90^\circ$ | $30^\circ$ karşısı $a$, $60^\circ$ karşısı $a\sqrt{3}$, hipotenüs $2a$ |
| $45^\circ$–$45^\circ$–$90^\circ$ | dik kenarlar $a$ ve $a$, hipotenüs $a\sqrt{2}$ |
| $15^\circ$–$75^\circ$–$90^\circ$ | hipotenüs $4a$ ise hipotenüse ait yükseklik $a$ |

> **Tuzak:** Hipotenüsün yarısı **$30^\circ$'nin karşısındaki** kenardır, $60^\circ$'ninki değil. Seçeneklerde iki kenar da hazır bekler. Ayrıca $\sqrt{3}$ ile $\sqrt{2}$'yi karıştırma: $\sqrt{2}$ yalnızca $45^\circ$'li üçgende çıkar.

## 4. Pisagor'dan çıkan iki eşitlik

Bu iki kural yeni bir şey değil, Pisagor'un iki kez kullanılmasıdır. Ama soruyu tek satırda bitirir.

**Örnek 8 (köşegenleri dik dörtgen).** $ABCD$ dörtgeninde $[AC] \perp [BD]$, $|AB| = 10$, $|BC| = 5$, $|CD| = 11$ birimdir. $|DA| = x$ kaçtır?

![ABCD dörtgeni. Kesikli AC ve BD köşegenleri O noktasında dik kesişiyor. AB kenarı 10, BC kenarı 5, CD kenarı 11, DA kenarı x olarak işaretli.](gorsel/tyt-matematik/21-01-dik-kosegen.svg "Karşılıklı kenarlar aynı renkte: kırmızı kenarların kareleri toplamı, yeşil kenarların kareleri toplamına eşittir.")

**Çözüm.** $O$ çevresindeki dört dik üçgende Pisagor yaz: $|AB|^2 = |OA|^2 + |OB|^2$, $|CD|^2 = |OC|^2 + |OD|^2$, $|BC|^2 = |OB|^2 + |OC|^2$, $|DA|^2 = |OD|^2 + |OA|^2$. İlk ikisinin toplamı ile son ikisinin toplamı aynı dört kareden oluşur:

$$|AB|^2 + |CD|^2 = |BC|^2 + |DA|^2 \Rightarrow 100 + 121 = 25 + x^2 \Rightarrow x^2 = 196 \Rightarrow x = 14$$

**Örnek 9 (yükseklik üzerinde nokta).** $ABC$ üçgeninde $[AH] \perp [BC]$ ve $D$ noktası $[AH]$ üzerindedir. $|AB| = 11$, $|AC| = 9$, $|DB| = 7$ birimdir. $|DC| = x$ kaçtır?

![ABC üçgeni ve A'dan BC'ye inen AH yüksekliği, H'de dik açı. AH üzerindeki D noktası B ve C'ye bağlanmış. AB 11, AC 9, DB 7, DC x olarak işaretli.](gorsel/tyt-matematik/21-01-yukseklik-nokta.svg "Çapraz duran kenarları eşleştir: AB ile DC, AC ile DB. Her eşleşmede bir kırmızı ve bir yeşil kenar vardır; iki eşleşmenin kareleri toplamı eşittir.")

**Çözüm.** $|AB|^2 - |AC|^2 = |HB|^2 - |HC|^2$ ve $|DB|^2 - |DC|^2 = |HB|^2 - |HC|^2$ (iki durumda da $|AH|^2$ ya da $|DH|^2$ sadeleşir). Öyleyse:

$$|AB|^2 + |DC|^2 = |AC|^2 + |DB|^2 \Rightarrow 121 + x^2 = 81 + 49 \Rightarrow x^2 = 9 \Rightarrow x = 3$$

**Kural:**

$$[AC] \perp [BD] \Rightarrow |AB|^2 + |CD|^2 = |BC|^2 + |DA|^2 \quad \text{(karşılıklı kenarlar)}$$

$$[AH] \perp [BC],\ D \in [AH] \Rightarrow |AB|^2 + |DC|^2 = |AC|^2 + |DB|^2 \quad \text{(çapraz kenarlar)}$$

> **Tuzak:** Dörtgende **komşu** kenarları eşleştirmek ($|AB|^2 + |BC|^2$) yanlış sonuç verir. Eşleşen kenarların ortak köşesi yoktur.

## ÖSYM tuzakları

> **Hipotenüsü yanlış seçmek.** Hipotenüs her zaman dik açının karşısındaki kenardır. Şekilde dik açı işaretine bak; kenar uzunluklarının sırasına göre karar verme.

> **Kök almayı unutmak.** $x^2 = 64$ bulup $64$'ü işaretlemek. Seçeneklerde karesi de bulunur.

> **Kenarları doğrudan toplamak.** $3$ ve $4$ dik kenarsa hipotenüs $7$ değil, $5$'tir. Pisagor uzunlukları değil, **kareleri** toplar.

> **Özel üçgende kenarı yanlış yere koymak.** $30^\circ$–$60^\circ$–$90^\circ$ üçgeninde $a$, $a\sqrt{3}$, $2a$ sırası açılar sırasıdır: küçük açının karşısında kısa kenar.

> **Ara uzunlukta durmak.** Çok adımlı sorularda önce bir yardımcı kenar bulunur ($|AB|$ gibi); soru genelde başka bir kenarı ister.

## Kendini dene

### Soru 1
Kenarları $8$ cm ve $15$ cm olan bir dikdörtgenin köşegeni kaç cm'dir?

A) 7
B) $\sqrt{161}$
C) 17
D) 23
E) 289

**Cevap:** C
**Çözüm:** Köşegen, dik kenarları $8$ ve $15$ olan dik üçgenin hipotenüsüdür: $8^2 + 15^2 = 64 + 225 = 289 \Rightarrow 17$. Bu bir $8$–$15$–$17$ üçgenidir. $289$ kök almayı unutmak, $23$ kenarları toplamak, $\sqrt{161}$ ise kareleri çıkarmaktır.

### Soru 2
$ABC$ üçgeninde $m(\widehat{B}) = 90^\circ$, $m(\widehat{A}) = 30^\circ$ ve $|AC| = 16$ birimdir. $|AB|$ kaç birimdir?

A) 8
B) $8\sqrt{2}$
C) $8\sqrt{3}$
D) $16\sqrt{3}$
E) 32

**Cevap:** C
**Çözüm:** $m(\widehat{C}) = 60^\circ$. $[BC]$, $30^\circ$'nin karşısındadır: $|BC| = 16 : 2 = 8$. $[AB]$, $60^\circ$'nin karşısındadır: $|AB| = 8\sqrt{3}$. Kontrol: $64 + 192 = 256 = 16^2$. $8$ ise $|BC|$'dir.

### Soru 3
Bir dik üçgenin iki kenarının uzunlukları $6$ cm ve $10$ cm'dir. Üçüncü kenarın uzunluğu aşağıdakilerden hangisi olabilir?

A) 4
B) 6
C) $2\sqrt{17}$
D) $2\sqrt{34}$
E) 16

**Cevap:** D
**Çözüm:** $10$ hipotenüsse üçüncü kenar $\sqrt{100 - 36} = 8$; bu seçeneklerde yok. İkisi de dik kenarsa hipotenüs $\sqrt{36 + 100} = \sqrt{136} = 2\sqrt{34}$. $4$ ve $16$, uzunlukların farkı ve toplamıdır.

## Özet kartı

- $a^2 + b^2 = c^2$: hipotenüs dik açının karşısındaki, en uzun kenardır.
- Hipotenüs için kareleri topla, dik kenar için çıkar; kökü sadeleştir.
- Tam sayı üçlüleri: $3$–$4$–$5$, $5$–$12$–$13$, $8$–$15$–$17$, $7$–$24$–$25$ ve katları.
- $30^\circ$–$60^\circ$–$90^\circ$: $a$, $a\sqrt{3}$, $2a$. $45^\circ$–$45^\circ$–$90^\circ$: $a$, $a$, $a\sqrt{2}$.
- $15^\circ$–$75^\circ$–$90^\circ$: hipotenüse ait yükseklik hipotenüsün $\dfrac{1}{4}$'ü.
- Köşegenleri dik dörtgende karşılıklı, yükseklik üzerindeki noktada çapraz kenarların kareleri toplamı eşittir.

## Sonraki adım

Alıştırmaya geç (aşağıdaki düğme). Sonraki ders: **Dik Üçgende Öklid Teoremi**. Orada hipotenüse dik inen yüksekliğin ayırdığı parçalarla kenarlar arasındaki bağıntıları göreceksin; çoğunu Pisagor ile kontrol edebilirsin.
