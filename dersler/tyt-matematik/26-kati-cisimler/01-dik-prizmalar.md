---
baslik: Dik Prizmalar
ders: tyt-matematik
sure: 25 dk
kaynak: MEBİ Konu Özeti 2aa5a0f3d5
guncelleme: 2026-11-18
---
# Dik Prizmalar

<div class="giris" dir="rtl" lang="ar">

**الدرس ده عن إيه؟** عن المنشور القائم (dik prizma): جسم ليه قاعدتين (taban) زي بعض، واقفين فوق بعض بالظبط، وجوانبه كلها مستطيلات.

- هتعرف أجزاءه وتعدّ رؤوسه (köşe) وأحرفه (ayrıt) وأوجهه (yüz) من عدد أضلاع القاعدة بس.
- هتتعلم تفرده على الورق (açınım) وتحسب المساحة الجانبية (yanal alan) والمساحة الكلية (toplam alan).
- هتحسب الحجم (hacim) وطول القطر (cisim köşegeni) في متوازي المستطيلات (dikdörtgenler prizması).

**ليه مهم؟** المجسمات بتيجي في آخر أسئلة الهندسة في TYT، وغالبًا في شكل حكاية من الحياة: حوض سمك، كرتونة، علبة عصير.

الدرس 25 دقيقة، وكل قاعدة معاها رسمة ومثال محلول. ركّز في القاعدة وانت بتحسب، وهتلاقيها سهلة.

</div>

**Bu dersin sonunda:** bir dik prizmanın köşe, ayrıt ve yüz sayısını, yanal alanını, toplam alanını, hacmini ve (dikdörtgenler prizmasında) cisim köşegenini tek formülle bulabileceksin.

> **TYT'de yeri:** Katı cisim soruları geometri bölümünün sonunda gelir ve çoğu yeni nesildir: akvaryuma atılan taş, kartondan yapılan kutu, bir kaptan ötekine boşaltılan su. İşlem azdır; asıl iş, hacim mi alan mı istendiğini görmek ve doğru formülü seçmektir.

## Önce hatırla

<details><summary>Geçen dersten: Köşegen uzunlukları 10 cm ve 14 cm olan bir deltoidin alanı kaç cm²'dir?</summary>
Deltoidin köşegenleri birbirine diktir, alan $\dfrac{e \cdot f}{2} = \dfrac{10 \cdot 14}{2} = 70$ cm². Bugün prizmanın tabanı deltoid, kare ya da üçgen olabilir; hacmi bulmak için önce bu taban alanı gerekir.
</details>

<details><summary>Geçen dersten: ABCD deltoidinde |AB| = |AD| = 5 ve |BD| = 8'dir. Köşegenler K'de kesişiyorsa |AK| kaçtır?</summary>
$[AC]$ köşegeni $[BD]$'yi dik keser ve ortalar: $|BK| = 4$. $ABK$ dik üçgeninde $|AK|^2 = 5^2 - 4^2 = 9$, $|AK| = 3$. Bugün aynı Pisagor adımını prizmanın içindeki köşegeni bulurken iki kez kullanacaksın.
</details>

## Dik prizma ve parçaları

Bir çokgeni, düzlemine dik bir doğru boyunca yukarı kaydırdığını düşün. Çokgenin taradığı kapalı cisim **dik prizmadır**. Başlangıçtaki çokgen **alt taban**, vardığı yerdeki eş çokgen **üst tabandır**.

![ABCD A'B'C'D' dik prizması. Üstteki A'B'C'D' üst taban, alttaki ABCD alt taban, öndeki sarı dikdörtgen yanal yüz, kırmızı BB' ayrıtı yanal ayrıt, yeşil AB ayrıtı taban ayrıtı olarak gösterilmiş. Görünmeyen ayrıtlar kesikli.](gorsel/tyt-matematik/26-01-parcalar.svg "Kesikli çizgiler arkada kalan ayrıtlardır. Kırmızı yanal ayrıt aynı zamanda prizmanın yüksekliğidir.")

| Parça | Ne |
|---|---|
| taban ayrıtı | tabandaki çokgenin kenarı ($[AB]$) |
| yanal ayrıt | alt ve üst tabanın karşılıklı köşelerini birleştiren ayrıt ($[BB']$) |
| yanal yüz | iki yanal ayrıt arasındaki bölge; dik prizmada her zaman **dikdörtgendir** |
| yükseklik ($h$) | iki taban arasındaki uzaklık; dik prizmada yanal ayrıtın uzunluğuna eşittir |

Prizma, **tabanındaki çokgene göre** adlandırılır: üçgen dik prizma, dörtgen dik prizma, altıgen dik prizma. Tabanı düzgün çokgen olan (bütün kenarları ve açıları eşit) prizmaya **düzgün prizma** denir. Tabanı dikdörtgen olana **dikdörtgenler prizması**, bütün ayrıtları eşit olan kare prizmaya **küp** denir.

## 1. Köşe, ayrıt ve yüz sayısı

**Örnek 1.** Tabanı beşgen olan bir dik prizmanın kaç köşesi, kaç ayrıtı ve kaç yüzü vardır?

**Çözüm.**

1. Köşeler: alt tabanda 5, üst tabanda 5. Toplam $2 \cdot 5 = 10$.
2. Ayrıtlar: alt tabanda 5, üst tabanda 5, iki taban arasında her köşeden bir yanal ayrıt, yani 5. Toplam $3 \cdot 5 = 15$.
3. Yüzler: her taban kenarının üstünde bir yanal yüz (5 tane), bir de iki taban. Toplam $5 + 2 = 7$.
4. Kontrol: $K + Y - A = 10 + 7 - 15 = 2$. (Bütün prizmalarda bu fark 2'dir.)

![Üç dik prizma yan yana. Üçgen dik prizma: 6 köşe, 9 ayrıt, 5 yüz. Dörtgen dik prizma: 8 köşe, 12 ayrıt, 6 yüz. Altıgen dik prizma: 12 köşe, 18 ayrıt, 8 yüz.](gorsel/tyt-matematik/26-01-turler.svg "Tabandaki kenar sayısı 3, 4, 6. Köşe sayısı bunun 2 katı, ayrıt sayısı 3 katı, yüz sayısı 2 fazlası.")

**Kural:** Tabanı $n$ kenarlı çokgen olan dik prizmada

$$\text{köşe} = 2n \qquad \text{ayrıt} = 3n \qquad \text{yüz} = n + 2$$

> **Tuzak:** Yüz sayısında iki tabanı unutup $n$ demek; ayrıt sayısında yanal ayrıtları unutup $2n$ demek. Soru tersten de gelir: "Ayrıt sayısı 24 ise yüz sayısı?" Önce $3n = 24$, $n = 8$; sonra yüz $= 10$.

## 2. Açınım ve yanal alan

**Örnek 2.** Tabanı kenarları 3, 4 ve 5 cm olan dik üçgen, yüksekliği 10 cm olan dik prizmanın yanal alanı ve toplam alanı kaç cm²'dir?

**Çözüm.**

1. Prizmayı yanal ayrıtlarından birinden kesip açarsan üç yanal yüz yan yana dizilir ve **tek bir dikdörtgen** olur.
2. Bu dikdörtgenin eni, taban kenarlarının toplamıdır: $3 + 4 + 5 = 12$ (tabanın çevresi). Boyu yüksekliktir: $10$.
3. Yanal alan: $12 \cdot 10 = 120$ cm².
4. İki taban, dik kenarları 3 ve 4 olan dik üçgendir; birinin alanı $\dfrac{3 \cdot 4}{2} = 6$.
5. Toplam alan: $120 + 2 \cdot 6 = 132$ cm².

![Üçgen dik prizmanın açınımı: 3 · 10, 4 · 10 ve 5 · 10 boyutlarında üç dikdörtgen yan yana, eni 3 + 4 + 5 = 12 olan tek dikdörtgen oluşturuyor. 4 birimlik kenarın üstüne ve altına birer dik üçgen taban yapışık.](gorsel/tyt-matematik/26-01-acinim.svg "Yanal yüzler yan yana dizilince eni taban çevresi, boyu yükseklik olan bir dikdörtgen olur. Kırmızı üçgenler iki tabandır.")

**Kural:**

$$\text{Yanal alan} = \text{Taban çevresi} \cdot h \qquad \text{Toplam alan} = \text{Yanal alan} + 2 \cdot \text{Taban alanı}$$

> **Tuzak:** Toplam alanda tabanı **bir** kez eklemek ($126$). Kapağı olmayan kutu sorularında ise bilerek tek taban eklenir; soru "üstü açık" diyorsa dikkat et.

## 3. Dikdörtgenler prizmasının alanı

**Örnek 3.** Ayrıtları 6 cm, 4 cm ve 5 cm olan dikdörtgenler prizmasının toplam alanı kaç cm²'dir?

**Çözüm.**

1. Altı yüz, üç eş çift oluşturur: ön–arka $6 \cdot 5 = 30$, üst–alt $6 \cdot 4 = 24$, sağ–sol $4 \cdot 5 = 20$.
2. Her çiftten iki tane vardır: $2 \cdot (30 + 24 + 20) = 2 \cdot 74 = 148$ cm².
3. Kontrol (2. kural ile): taban çevresi $2 \cdot (6 + 4) = 20$, yanal alan $20 \cdot 5 = 100$, toplam $100 + 2 \cdot 24 = 148$. Tutuyor.

![Ayrıtları 6, 4 ve 5 olan dikdörtgenler prizması. Ön yüz mavi (6 · 5), üst yüz yeşil (6 · 4), sağ yüz sarı (4 · 5).](gorsel/tyt-matematik/26-01-dikdortgenler.svg "Gördüğün üç yüzün her birinin arkada eşi vardır. Üç farklı alanı topla, sonra 2 ile çarp.")

**Kural:** Ayrıtları $a$, $b$, $c$ olan dikdörtgenler prizmasında

$$\text{Toplam alan} = 2(ab + ac + bc)$$

> **Tuzak:** $2$ ile çarpmayı unutup yalnızca görünen üç yüzü toplamak ($74$). Bir de alanı hacimle karıştırmak: $6 \cdot 4 \cdot 5 = 120$ hacimdir, alan değil.

## 4. Hacim

**Örnek 4.** Örnek 2'deki prizmanın (taban 3-4-5 dik üçgeni, yükseklik 10 cm) hacmi kaç cm³'tür?

**Çözüm.**

1. Prizma, taban alanında ince dilimlerin üst üste konmasıyla oluşur. Her dilimin alanı taban alanına eşittir.
2. Taban alanı: $T = \dfrac{3 \cdot 4}{2} = 6$ cm².
3. Hacim: $V = T \cdot h = 6 \cdot 10 = 60$ cm³.

![Yan yatırılmış üçgen dik prizma. Öndeki kırmızı yüz dik kenarları 3 ve 4, hipotenüsü 5 olan dik üçgen taban, alanı T = 6. Mavi ayrıt h = 10, derinlik yönünde.](gorsel/tyt-matematik/26-01-hacim.svg "Prizma yan yatmış: taban öndeki kırmızı üçgendir, yükseklik iki üçgen taban arasındaki mavi ayrıttır. Yükseklik her zaman dikey durmaz.")

**Kural:**

$$V = \text{Taban alanı} \cdot h \qquad \text{Dikdörtgenler prizmasında } V = a \cdot b \cdot c$$

Birimler: $1 \text{ L} = 1 \text{ dm}^3 = 1000 \text{ cm}^3$.

> **Tuzak:** Üçgen tabanda alanı ikiye bölmeyi unutmak: $3 \cdot 4 \cdot 10 = 120$ yanlıştır. Bir de taban alanı yerine taban çevresiyle çarpmak: $12 \cdot 10 = 120$ yanal alandır, hacim değil.

## 5. Cisim köşegeni

**Örnek 5.** $ABCDEFGH$ dikdörtgenler prizmasında $|AB| = 6$, $|BC| = 2$ ve $|CG| = 3$ birimdir. $|AG|$ kaç birimdir?

**Çözüm.**

1. Önce tabanda kal: $ABC$ dik üçgeninde $|AC|^2 = 6^2 + 2^2 = 40$. Bu, **taban köşegenidir**.
2. $[CG]$ ayrıtı tabana diktir, yani $ACG$ üçgeni $C$'de diktir.
3. $|AG|^2 = |AC|^2 + |CG|^2 = 40 + 9 = 49$, $|AG| = 7$.

![ABCDEFGH dikdörtgenler prizması: AB = 6, BC = 2, CG = 3. Yeşil kesikli AC taban köşegeni (kök 40), yeşil CG ayrıtı ve kırmızı AG cisim köşegeni (7). C köşesinde dik açı işareti.](gorsel/tyt-matematik/26-01-kosegen.svg "Yeşil AC ile yeşil CG, C'de dik açı yapar. Kırmızı AG bu dik üçgenin hipotenüsüdür.")

**Kural:** Ayrıtları $a$, $b$, $c$ olan dikdörtgenler prizmasında cisim köşegeni

$$d = \sqrt{a^2 + b^2 + c^2}$$

İki adımlı Pisagor tek formüle sığar. Bir kutuya sığabilecek en uzun çubuk, cisim köşegeni kadardır.

> **Tuzak:** Taban köşegeninde durmak ($\sqrt{40}$). Ya da kareleri değil uzunlukları toplamak: $6 + 2 + 3 = 11$ yanlıştır.

## ÖSYM tuzakları

> **Alan mı hacim mi?** "Boya", "kaplama", "karton", "ambalaj" alan ister; "su", "doldurma", "sığdırma", "litre" hacim ister.

> **Birim.** Ayrıtlar cm ise hacim cm³'tür. Litreye çevirirken $1000$'e böl: $3000$ cm³ $= 3$ L.

> **Su yükselmesi.** Suya tamamen batan cisim, kendi hacmi kadar suyu yükseltir. Yükselme $=\dfrac{\text{cismin hacmi}}{\text{kabın taban alanı}}$. Cismin kendi yüksekliği eklenmez.

> **Yapıştırma.** İki prizma bir yüzden yapıştırılınca yapışan iki yüz dışarıda kalmaz: toplam alandan $2$ kez o yüzün alanı çıkar. Hacimler ise doğrudan toplanır.

> **Yükseklik hangisi?** Yükseklik iki **taban** arasındaki uzaklıktır. Yan yatmış prizmada tabanı bul, yüksekliği ona dik ayrıtta ara.

## Kendini dene

### Soru 1
Ayrıt sayısı 24 olan bir dik prizmanın yüz sayısı kaçtır?

A) 8
B) 10
C) 12
D) 16
E) 26

**Cevap:** B
**Çözüm:** Taban $n$ kenarlı ise ayrıt sayısı $3n$: $3n = 24$, $n = 8$. Yüz sayısı $n + 2 = 10$. $8$, iki tabanı unutmaktır; $16$ köşe sayısıdır; $12$ ise ayrıt sayısının yarısıdır.

### Soru 2
![Ayrıtları 3, 4 ve 12 olan dikdörtgenler prizması. Kırmızı cisim köşegeni soru işaretiyle gösterilmiş.](gorsel/tyt-matematik/26-01-kd2.svg "Kırmızı çizgi alt ön sol köşeden üst arka sağ köşeye gidiyor.")

Şekildeki dikdörtgenler prizmasının ayrıtları 3, 4 ve 12 birimdir. Kırmızı çizilen cisim köşegeninin uzunluğu kaç birimdir?

A) 5
B) 12
C) 13
D) 19
E) 169

**Cevap:** C
**Çözüm:** $d^2 = 3^2 + 4^2 + 12^2 = 9 + 16 + 144 = 169$, $d = 13$. $5$ taban köşegenidir ($\sqrt{9 + 16}$); $19$ uzunlukların toplamı; $169$ karekökü almamaktır.

### Soru 3
Taban ayrıtı 5 cm, yüksekliği 8 cm olan kare dik prizmanın toplam alanı kaç cm²'dir?

A) 160
B) 185
C) 200
D) 210
E) 320

**Cevap:** D
**Çözüm:** Taban çevresi $4 \cdot 5 = 20$, yanal alan $20 \cdot 8 = 160$. Taban alanı $25$, iki taban $50$. Toplam $160 + 50 = 210$ cm². $160$ yalnızca yanal alandır; $185$ tek taban eklemektir; $200$ hacimdir ($25 \cdot 8$); $320$, yanal alanı iki kez saymaktır.

## Özet kartı

- Dik prizma: iki eş taban, dikdörtgen yanal yüzler; yükseklik = yanal ayrıt.
- $n$ kenarlı tabanda: köşe $2n$, ayrıt $3n$, yüz $n + 2$.
- Yanal alan = taban çevresi $\cdot \, h$; toplam alan = yanal alan $+ \, 2 \cdot$ taban alanı.
- Dikdörtgenler prizması: alan $2(ab + ac + bc)$, hacim $abc$.
- Hacim = taban alanı $\cdot \, h$; $1$ L $= 1000$ cm³.
- Cisim köşegeni: $\sqrt{a^2 + b^2 + c^2}$.

## Sonraki adım

Alıştırmaya geç (aşağıdaki düğme). Sonraki ders: **Küp**. Küp, bütün ayrıtları eşit dikdörtgenler prizmasıdır; bugünkü formüllerde $a = b = c$ yazınca alan $6a^2$, hacim $a^3$, cisim köşegeni $a\sqrt{3}$ çıkar.
