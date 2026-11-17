---
baslik: Üçgen Eşitsizliği
ders: tyt-matematik
sure: 20 dk
kaynak: MEBİ Konu Özeti 075c58448d
guncelleme: 2026-11-17
---
# Üçgen Eşitsizliği

**Bu dersin sonunda:** iki kenarı bilinen bir üçgende üçüncü kenarın aralığını yazabilecek, ortak kenarlı iki üçgende aralıkları kesiştirebilecek ve açının dar ya da geniş olmasına göre aralığı daraltarak "kaç farklı tam sayı değeri alır?" sorusunu çözebileceksin.

> **TYT'de yeri:** Geometri bölümünde sık gelen kalıp: "$x$'in alabileceği tam sayı değerleri kaç tanedir / toplamı kaçtır / en büyük değeri kaçtır?". Soru ya tek bir üçgende, ya bir köşegenle ikiye bölünmüş dörtgende, ya da bir açının geniş (dar) olduğu söylenerek gelir. Günlük hayat sorularında çubuk, yol ya da robot kolu olarak karşına çıkar.

## Önce hatırla

<details><summary>Geçen dersten: ABC üçgeninde m(A) = 65° ve m(C) = 45° ise en uzun kenar hangisidir?</summary>
$m(\widehat{B}) = 180^\circ - 65^\circ - 45^\circ = 70^\circ$. En büyük açı $\widehat{B}$; karşısındaki $b = |AC|$ en uzun kenardır. Bugün bu bilgiyi bir kenarın <b>alt sınırı</b> olarak kullanacaksın.
</details>

<details><summary>Geçen dersten: Kenarları 6, 7 ve 10 olan üçgen dar açılı mı, dik üçgen mi, geniş açılı mı?</summary>
En uzun kenara bak: $10^2 = 100$, $6^2 + 7^2 = 36 + 49 = 85$. $100 > 85$ olduğu için 10'un karşısındaki açı <b>geniş</b>: üçgen geniş açılıdır. Bugün bu karşılaştırmayı üçgen eşitsizliğiyle birleştireceksin.
</details>

Gösterim geçen dersteki gibi: $a = |BC|$, $b = |AC|$, $c = |AB|$.

## 1. Üçüncü kenar iki sınır arasındadır

**Örnek 1.** Uzunlukları 2 cm, 3 cm ve 6 cm olan üç çubukla üçgen kurulabilir mi?

**Çözüm.** 6 cm'lik çubuğu yere koy, 2 ve 3 cm'liklerin birer ucunu onun iki ucuna bağla. Kısa çubuklar ne kadar çevrilirse çevrilsin uçları buluşmaz: yan yana yatırsan bile $2 + 3 = 5$ cm eder, 6 cm'yi kapatmaz. Üçgen **kurulamaz**. Çubukları 4 ve 3 cm alırsan $4 + 3 = 7 > 6$ olur ve uçlar $A$ noktasında buluşur.

![Üstte: 6 birimlik BC tabanının uçlarında 2 ve 3 birimlik kırmızı çubuklar; çubukların döndüğü kesikli yaylar birbirine değmiyor, aralarında 1 birim boşluk var. Altta: aynı tabanda 4 ve 3 birimlik yeşil çubuklar; yaylar A noktasında kesişiyor ve ABC üçgeni oluşuyor.](gorsel/tyt-matematik/18-06-kapanmayan.svg "Kesikli yaylar, çubuğun ucunun gidebileceği yerlerdir. Yaylar kesişmiyorsa üçgen kurulamaz. Kesişmeleri için iki kısa kenarın toplamı tabandan büyük olmalı.")

**Örnek 2.** Bir üçgenin iki kenarı 4 ve 7 birimdir. Üçüncü kenar $x$ bir tam sayı ise $x$ kaç farklı değer alabilir?

**Çözüm.** 4 ve 7 birimlik kenarları $B$ köşesinde menteşe gibi bağlı düşün. Aradaki açı küçüldükçe $x$ kısalır, büyüdükçe uzar.

![7 birimlik BC ve 4 birimlik BA kenarları sabit; B'deki açı yukarıdan aşağı 20, 90 ve 160 derece. Üçüncü kenar x sırasıyla yaklaşık 3,5; 8,1 ve 10,8 birim.](gorsel/tyt-matematik/18-06-mentese.svg "Açı kapandıkça x, 7 − 4 = 3'e yaklaşır; açıldıkça 7 + 4 = 11'e yaklaşır. Ama açı 0° ya da 180° olamaz, bu yüzden x hiçbir zaman 3 ya da 11 olmaz.")

1. Açı neredeyse $0^\circ$ olunca kenarlar üst üste biner: $x$, $7 - 4 = 3$'e yaklaşır.
2. Açı neredeyse $180^\circ$ olunca kenarlar düz bir çizgi olur: $x$, $7 + 4 = 11$'e yaklaşır.
3. Uç durumlarda üçgen yassılaşıp bir doğru parçası olur, yani $3$ ve $11$ dahil değildir: $3 < x < 11$.
4. Tam sayılar: $4, 5, 6, 7, 8, 9, 10$. Toplam **7** değer ($11 - 3 - 1 = 7$).

**Kural (üçgen eşitsizliği):** Bir üçgende her kenar, öbür iki kenarın **farkından büyük, toplamından küçüktür.**

$$|b - c| < a < b + c \qquad |a - c| < b < a + c \qquad |a - b| < c < a + b$$

**Üç sayı verildiyse kısa kontrol:** En uzun kenar, öbür ikisinin toplamından küçükse üçgen kurulur; yalnızca bunu denemek yeter. Örneğin $5, 7, 13$: $5 + 7 = 12 < 13$, kurulmaz. $5, 7, 11$: $12 > 11$, kurulur.

> **Tuzak:** Eşitsizlikler **kesin**dir. $x = 3$ ya da $x = 11$ alırsan üç nokta aynı doğru üzerine düşer, üçgen olmaz. "Kaç tam sayı?" sorusunda uçları sayan seçenek ($9$) hazır bekler.

## 2. Ortak kenarlı iki üçgen: aralıkları kesiştir

**Örnek 3.** Şekildeki $ABCD$ dörtgeninde $|AB| = 5$, $|AD| = 8$, $|BC| = 6$, $|CD| = 12$ ve $|BD| = x$'tir. $x$ bir tam sayı ise kaç farklı değer alabilir?

![ABCD dörtgeni, kırmızı kesikli BD köşegeni x ile iki üçgene ayrılmış. Üstteki mavi ABD üçgeninde AB 5, AD 8; alttaki sarı BCD üçgeninde BC 6, CD 12.](gorsel/tyt-matematik/18-06-ortak-kenar.svg "x iki üçgenin ortak kenarıdır. Mavi üçgen bir aralık, sarı üçgen başka bir aralık verir; x ikisini birden sağlamalı.")

**Çözüm.**

1. $ABD$ üçgeni: $8 - 5 < x < 8 + 5 \Rightarrow 3 < x < 13$.
2. $BCD$ üçgeni: $12 - 6 < x < 12 + 6 \Rightarrow 6 < x < 18$.
3. İkisi birden: büyük alt sınırı ve küçük üst sınırı al: $6 < x < 13$.
4. Tam sayılar: $7, 8, 9, 10, 11, 12$. **6** değer.

**Kural:** Bir kenar iki üçgende ortaksa her üçgenden ayrı aralık yaz, sonra **kesişimini** al: alt sınırların büyüğü, üst sınırların küçüğü.

> **Tuzak:** Yalnızca bir üçgene bakıp durmak. $ABD$'den çıkan $3 < x < 13$ aralığında 9 tam sayı var; seçeneklerde 9 da bulunur. Kesişimi almadan cevap verme.

## 3. Açı dar mı geniş mi? Aralığı daralt

Geçen dersten: $\widehat{B}$ dik açıysa $b^2 = a^2 + c^2$, dar açıysa $b^2 < a^2 + c^2$, geniş açıysa $b^2 > a^2 + c^2$. Bunu üçgen eşitsizliğiyle birleştirince aralık ikiye bölünür.

**Örnek 4.** $ABC$ üçgeninde $a = |BC| = 6$, $c = |AB| = 8$'dir. $b = |AC|$ bir tam sayıdır.
a) $\widehat{B}$ geniş açı ise $b$ kaç farklı değer alır?
b) $\widehat{B}$ dar açı ise $b$ kaç farklı değer alır?

**Çözüm.**

1. Üçgen eşitsizliği: $8 - 6 < b < 8 + 6 \Rightarrow 2 < b < 14$.
2. Dik açı sınırı: $\widehat{B} = 90^\circ$ olsaydı $b^2 = 6^2 + 8^2 = 100$, yani $b = 10$ olurdu.
3. a) Geniş: $b^2 > 100 \Rightarrow b > 10$. Birlikte $10 < b < 14$: $11, 12, 13$. **3** değer.
4. b) Dar: $b^2 < 100 \Rightarrow b < 10$. Birlikte $2 < b < 10$: $3, 4, \dots, 9$. **7** değer.

![2 ile 14 arasında sayı doğrusu; uçlar boş nokta. 2 ile 10 arası mavi ve B dar açı yazıyor, 10 ile 14 arası kırmızı ve B geniş açı yazıyor; 10'da yeşil dolu nokta ve B dik açı, b eşittir 10 notu.](gorsel/tyt-matematik/18-06-dar-genis.svg "Üçgen eşitsizliği b için 2 ile 14 arasını verir. Dik açı değeri 10, bu aralığı ikiye böler: solu dar, sağı geniş.")

**Kural:** $\widehat{B}$, $a$ ile $c$ kenarlarının arasındaki açı ise

$$\widehat{B} \text{ dar} \Rightarrow |a - c| < b < \sqrt{a^2 + c^2} \qquad \widehat{B} \text{ geniş} \Rightarrow \sqrt{a^2 + c^2} < b < a + c$$

> **Tuzak:** $b = 10$ hiçbir tarafa girmez; o değerde açı tam $90^\circ$'dir. Ayrıca kök tam çıkmayabilir: $a = 5$, $c = 7$ için $\sqrt{74} \approx 8{,}6$; geniş açıda $b$ en az $9$ olur.

## Açı-kenar bağıntısıyla birlikte

Geçen dersin kuralı (büyük açının karşısında büyük kenar) da bir sınır verir.

**Örnek 5.** $ABC$ üçgeninde $m(\widehat{A}) > m(\widehat{B})$, $b = |AC| = 8$ ve $c = |AB| = 5$'tir. $a = |BC|$ tam sayı ise kaç değer alır?

**Çözüm.** Üçgen eşitsizliği: $8 - 5 < a < 8 + 5 \Rightarrow 3 < a < 13$. Açı-kenar: $m(\widehat{A}) > m(\widehat{B}) \Rightarrow a > b = 8$. Birlikte $8 < a < 13$: $9, 10, 11, 12$. **4** değer.

![ABC üçgeninde AB 5, AC 8. A köşesindeki kırmızı yay büyük açı, B köşesindeki mavi yay küçük açı olarak işaretli. A'nın karşısındaki BC kenarı kırmızı ve altında a büyüktür 8 yazıyor.](gorsel/tyt-matematik/18-06-aci-kenar.svg "A'daki açı B'dekinden büyük, öyleyse A'nın karşısındaki a da B'nin karşısındaki 8'den uzun. Çizimde a = 10.")

**Kural:** Açılar arasında bir sıra verilmişse onu kenarlar arasındaki sıraya çevir ve üçgen eşitsizliğinden çıkan aralığa ek sınır olarak yaz.

## ÖSYM tuzakları

> **Uçları saymak.** $3 < x < 11$ aralığında $3$ ve $11$ yoktur. $(3, 11)$ açık aralığında $11 - 3 - 1 = 7$ tam sayı vardır, $9$ değil.

> **Yalnızca toplamı kontrol etmek.** Üçüncü kenar için alt sınır da var: kenarları 4 ve 7 olan üçgende $x = 2$ olamaz, çünkü $2 + 4 < 7$.

> **İkizkenar üçgende yanlış kenarı çift almak.** İki kenarı 4 ve 9 olan ikizkenar üçgenin kenarları $4, 4, 9$ olamaz ($4 + 4 < 9$). Kenarlar $4, 9, 9$'dur; çevre $22$.

> **Kesişim yerine birleşim.** Ortak kenarlı iki üçgende $x$ iki koşulu **birlikte** sağlar. Alt sınırların büyüğünü, üst sınırların küçüğünü al.

> **Dik açı değerini aralığa katmak.** "Geniş açı" ya da "dar açı" denmişse $b^2 = a^2 + c^2$ veren değer dışarıda kalır.

## Kendini dene

### Soru 1
Bir üçgenin iki kenarının uzunlukları 3 cm ve 8 cm'dir. Üçüncü kenarın uzunluğu santimetre cinsinden bir tam sayı ise kaç farklı değer alabilir?

A) 4
B) 5
C) 6
D) 7
E) 10

**Cevap:** B
**Çözüm:** $8 - 3 < x < 8 + 3 \Rightarrow 5 < x < 11$. Tam sayılar: $6, 7, 8, 9, 10$; **5** değer. $7$, iki ucu da saymaktır ($5$ ile $11$ dahil); $10$ ise en büyük değerdir, sayı değil.

### Soru 2
$ABC$ üçgeninde $a = |BC| = 9$, $b = |AC| = 4$ ve $m(\widehat{C}) > m(\widehat{A})$'dır. $c = |AB|$'nin alabileceği tam sayı değerlerinin toplamı kaçtır?

A) 12
B) 21
C) 33
D) 46
E) 63

**Cevap:** C
**Çözüm:** Üçgen eşitsizliği: $9 - 4 < c < 9 + 4 \Rightarrow 5 < c < 13$. Açı-kenar: $m(\widehat{C}) > m(\widehat{A}) \Rightarrow c > a = 9$. Birlikte $9 < c < 13$: $10, 11, 12$; toplam $33$. $63$, açı koşulunu unutup $6$'dan $12$'ye kadar toplamaktır; $46$ ise $13$'ü de katmaktır.

### Soru 3
$ABC$ üçgeninde $|AB| = 7$, $|AC| = 5$ ve $\widehat{A}$ geniş açıdır. $|BC|$ bir tam sayı ise kaç farklı değer alabilir?

A) 2
B) 3
C) 6
D) 9
E) 11

**Cevap:** B
**Çözüm:** Üçgen eşitsizliği: $2 < |BC| < 12$. $\widehat{A}$ geniş: $|BC|^2 > 7^2 + 5^2 = 74$; $8^2 = 64 < 74$, $9^2 = 81 > 74$, yani $|BC| \ge 9$. Değerler $9, 10, 11$; **3** tane. $6$, dar açı durumunun sayısıdır ($3$'ten $8$'e); $9$ ise yalnızca üçgen eşitsizliğinden gelir.

## Özet kartı

- Her kenar, öbür iki kenarın farkından büyük, toplamından küçüktür: $|b - c| < a < b + c$.
- Üç sayı verildiyse: en uzun kenar < öbür ikisinin toplamı ise üçgen kurulur.
- Eşitsizlikler kesindir; $(m, n)$ açık aralığında $n - m - 1$ tam sayı vardır.
- Ortak kenar: iki aralık yaz, kesişimini al.
- Arada geniş açı varsa $b > \sqrt{a^2 + c^2}$, dar açı varsa $b < \sqrt{a^2 + c^2}$.
- Büyük açının karşısında büyük kenar da ayrı bir sınır verir.

## Sonraki adım

Alıştırmaya geç (aşağıdaki düğme). Bu dersle **Üçgenlerde Temel Kavramlar** konusu bitiyor. Sıradaki konu **Üçgenlerde Eşlik ve Benzerlik**; orada iki üçgenin kenarlarını birbiriyle karşılaştıracaksın.
