---
baslik: Dik Piramitler
ders: tyt-matematik
sure: 25 dk
kaynak: MEBİ Konu Özeti 4033d4531e
guncelleme: 2026-11-18
---
# Dik Piramitler

<div class="giris" dir="rtl" lang="ar">

**الدرس ده عن إيه؟** عن الهرم القائم (dik piramit): قاعدة (taban) على شكل مضلع، وكل رؤوسها متوصلة بنقطة واحدة فوق اسمها الرأس (tepe noktası).

- هتعرف أجزاءه وتعدّ رؤوسه (köşe) وأحرفه (ayrıt) وأوجهه (yüz) من عدد أضلاع القاعدة.
- هتتعلم تلاقي الارتفاع (yükseklik) وارتفاع الوجه الجانبي (yan yüz yüksekliği) والحرف الجانبي (yanal ayrıt) بفيثاغورس.
- هتحسب المساحة الجانبية (yanal alan) والمساحة الكلية (yüzey alanı) والحجم (hacim).

**ليه مهم؟** الهرم بييجي في TYT في صورة سقف، خيمة، أو هرم جوه مكعب، والحل دايمًا مثلث قائم صغير مستخبي جواه.

الدرس 25 دقيقة، وكل قاعدة معاها رسمة ومثال محلول. ارسم المثلث القائم بإيدك وهتلاقي كل حاجة بتتحل لوحدها.

</div>

**Bu dersin sonunda:** bir dik piramidin köşe, ayrıt ve yüz sayısını, yüksekliğini, yan yüz yüksekliğini, yanal ayrıtını, yanal alanını, yüzey alanını ve hacmini içindeki dik üçgenleri kullanarak bulabileceksin.

> **TYT'de yeri:** Piramit soruları katı cisimlerin içinde gelir ve çoğu yeni nesildir: kare tabanlı çatı, çadır, küpün içine yerleştirilmiş piramit, piramidin açınımı. Soru genelde iki uzunluk verir, üçüncüsünü piramidin içindeki dik üçgenden bulmanı ister; sonra alan ya da hacim gelir.

## Önce hatırla

<details><summary>Geçen dersten: Cisim köşegeni $6\sqrt{3}$ cm olan bir küpün hacmi kaç cm³'tür?</summary>
Küpte cisim köşegeni $a\sqrt{3}$: $a\sqrt{3} = 6\sqrt{3}$, $a = 6$. Hacim $a^3 = 216$ cm³. Bugün piramidin hacmini, aynı tabanlı ve aynı yükseklikli prizmanın hacmiyle karşılaştıracaksın.
</details>

<details><summary>Geçen dersten: Yüzey alanı 150 cm² olan bir küpün bir yüzünün köşegeni kaç cm'dir?</summary>
$6a^2 = 150$, $a^2 = 25$, $a = 5$. Yüz köşegeni $a\sqrt{2} = 5\sqrt{2}$ cm. Bugün kare tabanın köşegeninin yarısını, yanal ayrıtı bulurken kullanacaksın.
</details>

## Piramit ve parçaları

Bir çokgen ile bu çokgenin düzleminin dışında bir $T$ noktası al. $T$'yi çokgenin bütün noktalarına birleştirince oluşan kapalı cisme **piramit** denir. $T$ **tepe noktasıdır**, çokgen **tabandır**. Piramit, köşeleri sırayla yazılarak gösterilir: $(T, ABCD)$.

![T tepeli, ABCD kare tabanlı dik piramit. TAB yüzü sarı, TBC yüzü mavi. Kırmızı TB yanal ayrıt, yeşil AB taban ayrıtı, mavi kesikli TG yükseklik; G tabanın merkezi, G'de dik açı işareti. Arkadaki ayrıtlar kesikli.](gorsel/tyt-matematik/26-03-parcalar.svg "Yükseklik TG, tepeden tabanın tam ortasına (G) dik iner. Kesikli çizgiler arkada kalan ayrıtlardır.")

| Parça | Ne |
|---|---|
| taban ayrıtı | tabandaki çokgenin kenarı ($[AB]$) |
| yanal ayrıt | tepeyi tabanın bir köşesine birleştiren ayrıt ($[TB]$) |
| yanal yüz | tepe ile bir taban ayrıtının oluşturduğu **üçgen** ($TAB$) |
| yükseklik ($h$) | tepeden taban düzlemine inen dikme ($[TG]$) |

Tepeden inen dikme tabanın **ağırlık merkezine** ($G$) düşüyorsa piramit **dik piramittir**. Tabanı düzgün çokgen (bütün kenarları ve açıları eşit) olan dik piramide **düzgün dik piramit** denir. Düzgün dik piramitte yanal yüzler eş ikizkenar üçgenlerdir, bütün yanal ayrıtlar eşittir. Piramit tabanına göre adlandırılır: üçgen piramit, kare piramit, altıgen piramit.

## 1. Köşe, ayrıt ve yüz sayısı

**Örnek 1.** Tabanı altıgen olan bir piramidin kaç köşesi, kaç ayrıtı ve kaç yüzü vardır?

**Çözüm.**

1. Köşeler: tabanda 6, bir de tepe. Toplam $6 + 1 = 7$.
2. Ayrıtlar: tabanda 6 taban ayrıtı, tepeden her taban köşesine bir yanal ayrıt, yani 6. Toplam $2 \cdot 6 = 12$.
3. Yüzler: her taban ayrıtının üstünde bir yanal yüz (6 üçgen), bir de taban. Toplam $6 + 1 = 7$.
4. Kontrol: $K + Y - A = 7 + 7 - 12 = 2$. (Prizmada olduğu gibi piramitte de bu fark 2'dir.)

![Üç piramit yan yana. Üçgen piramit: 4 köşe, 6 ayrıt, 4 yüz. Kare piramit: 5 köşe, 8 ayrıt, 5 yüz. Altıgen piramit: 7 köşe, 12 ayrıt, 7 yüz.](gorsel/tyt-matematik/26-03-turler.svg "Tabandaki kenar sayısı 3, 4, 6. Köşe ve yüz sayısı bunun 1 fazlası, ayrıt sayısı 2 katı.")

**Kural:** Tabanı $n$ kenarlı çokgen olan piramitte

$$\text{köşe} = n + 1 \qquad \text{ayrıt} = 2n \qquad \text{yüz} = n + 1$$

> **Tuzak:** Prizma formüllerini kullanmak ($2n$, $3n$, $n + 2$). Piramidin tek tabanı ve tek tepesi vardır. Soru tersten de gelir: "Ayrıt sayısı 16 ise yüz sayısı?" Önce $2n = 16$, $n = 8$; sonra yüz $= 9$.

## 2. İçerideki dik üçgenler

**Örnek 2.** Taban ayrıtı 6 birim, yüksekliği 4 birim olan kare dik piramitte yan yüz yüksekliği ve yanal ayrıt kaç birimdir?

**Çözüm.**

1. $G$ karenin merkezidir. $[BC]$'nin orta noktası $M$ olsun: $|GM| = \dfrac{6}{2} = 3$ (taban ayrıtının yarısı).
2. $[TG]$ tabana dik, bu yüzden $TGM$ üçgeni $G$'de diktir. $[TM]$, yan yüzün ($TBC$) yüksekliğidir: $|TM|^2 = 4^2 + 3^2 = 25$, $h_Y = |TM| = 5$.
3. Yanal ayrıt için $TGB$ üçgenini kullan. $|GB|$ köşegenin yarısıdır: $\dfrac{6\sqrt{2}}{2} = 3\sqrt{2}$.
4. $|TB|^2 = 4^2 + (3\sqrt{2})^2 = 16 + 18 = 34$, $|TB| = \sqrt{34}$.
5. Kontrol: yan yüzde $TMB$ üçgeni $M$'de diktir; $|TB|^2 = 5^2 + 3^2 = 34$. Tutuyor.

![Aynı kare dik piramit iki kez. Üstte TGM dik üçgeni: TG = 4 mavi, GM = 3 yeşil, TM = 5 kırmızı yan yüz yüksekliği; G'de ve M'de dik açı. Altta TGB dik üçgeni: TG = 4, GB = 3 kök 2 yeşil, TB = kök 34 kırmızı yanal ayrıt.](gorsel/tyt-matematik/26-03-dik-ucgenler.svg "İki dik üçgenin de bir dik kenarı yükseklik (4). Üstte öbür dik kenar taban ayrıtının yarısı, altta köşegenin yarısı.")

**Kural:** Kare dik piramitte (taban ayrıtı $a$, yükseklik $h$, yan yüz yüksekliği $h_Y$, yanal ayrıt $l$)

$$h_Y^2 = h^2 + \left(\frac{a}{2}\right)^2 \qquad l^2 = h^2 + \left(\frac{a\sqrt{2}}{2}\right)^2 \qquad l^2 = h_Y^2 + \left(\frac{a}{2}\right)^2$$

Üç formül aynı fikirdir: aradığın uzunluğu hipotenüs yapan dik üçgeni bul.

> **Tuzak:** Yükseklik ($h$) ile yan yüz yüksekliğini ($h_Y$) karıştırmak. $h$ piramidin içinden dik iner; $h_Y$ yan yüzün üzerindedir ve her zaman $h$'den uzundur. Bir de $|GM|$ yerine bütün taban ayrıtını almak: $4^2 + 6^2$ yanlıştır.

## 3. Yanal alan ve yüzey alanı

**Örnek 3.** Örnek 2'deki piramidin (taban ayrıtı 6, $h_Y = 5$) yanal alanı ve yüzey alanı kaç birimkaredir?

**Çözüm.**

1. Piramidi yanal ayrıtlarından kesip açarsan ortada kare taban, çevresinde dört eş üçgen kalır.
2. Bir yan yüz: tabanı 6, yüksekliği $h_Y = 5$ olan üçgen. Alanı $\dfrac{6 \cdot 5}{2} = 15$.
3. Yanal alan: $4 \cdot 15 = 60$. (Kısa yol: taban çevresi $24$, $\dfrac{24 \cdot 5}{2} = 60$.)
4. Taban alanı: $6^2 = 36$. Yüzey alanı: $60 + 36 = 96$.

![Kare dik piramidin açınımı: ortada kenarı 6 olan mavi kare taban, her kenarına yapışık sarı birer ikizkenar üçgen yan yüz. Alttaki üçgende kırmızı kesikli yükseklik h_Y = 5.](gorsel/tyt-matematik/26-03-acinim.svg "Dört sarı üçgen yanal alandır, mavi kare tabandır. Üçgenin yüksekliği piramidin yüksekliği değil, yan yüz yüksekliğidir.")

**Kural:** Düzgün dik piramitte taban çevresi $Ç_T$, taban alanı $A_T$ olmak üzere

$$A_Y = \frac{Ç_T \cdot h_Y}{2} \qquad A = A_T + A_Y$$

> **Tuzak:** Yan yüzün alanında $h_Y$ yerine $h$ kullanmak: $\dfrac{24 \cdot 4}{2} = 48$ yanlıştır. Bir de $2$'ye bölmeyi unutmak ($120$) ya da prizmadaki gibi tabanı iki kez eklemek ($132$). Piramidin **tek** tabanı vardır.

## 4. Hacim

**Örnek 4.** Örnek 2'deki piramidin (taban ayrıtı 6, yükseklik 4) hacmi kaç birimküptür?

**Çözüm.**

1. Aynı tabanlı ve aynı yükseklikli prizmayı düşün: $V_{\text{prizma}} = 36 \cdot 4 = 144$.
2. Piramit bu prizmanın tam olarak üçte birini doldurur.
3. $V = \dfrac{36 \cdot 4}{3} = 48$.

![Tabanı 6 · 6, yüksekliği 4 olan kare prizma ince gri çizgilerle; içinde aynı tabanlı, tepesi üst yüzün merkezinde olan sarı piramit. Yanda prizma 36 · 4 = 144, piramit 144 : 3 = 48 yazıyor.](gorsel/tyt-matematik/26-03-hacim.svg "Piramit, kendisiyle aynı tabanlı ve aynı yükseklikli prizmanın üçte biri kadardır. Üç tane böyle piramidin suyu prizmayı doldurur.")

**Kural:** Her piramitte (tabanı ne olursa olsun)

$$V = \frac{A_T \cdot h}{3}$$

> **Tuzak:** $3$'e bölmeyi unutmak ($144$, prizmanın hacmi). Bir de yükseklik yerine yan yüz yüksekliğini ya da yanal ayrıtı koymak: $\dfrac{36 \cdot 5}{3} = 60$ yanlıştır. Hacimde **yalnızca** $h$ kullanılır; $h$ verilmemişse önce 2. kuraldaki dik üçgenden bul.

## ÖSYM tuzakları

> **Üç yükseklik.** $h$ (piramidin içinden), $h_Y$ (yan yüz üzerinde), yanal ayrıt $l$ (köşeye giden). Hacimde $h$, yanal alanda $h_Y$ kullanılır. Sıralama her zaman $h < h_Y < l$.

> **Yarım mı, köşegenin yarısı mı?** $h_Y$ için $G$'den kenarın ortasına ($\frac{a}{2}$), yanal ayrıt için $G$'den köşeye ($\frac{a\sqrt{2}}{2}$) gidilir.

> **Çatı ve çadır.** "Çatı kaplanacak", "çadır bezi" yanal alan ister; taban (zemin) eklenmez. "İçindeki hava", "dolduran kum" hacim ister.

> **Küpün içindeki piramit.** Tepe üst yüzün merkezinde, taban alt yüz ise piramidin yüksekliği küpün ayrıtına eşittir ve hacmi küpün $\frac{1}{3}$'üdür. Dışarıda kalan kısım $\frac{2}{3}$'tür.

> **Açınımın çevresi.** Kare piramidin yıldız biçimli açınımının kenarlarının hepsi yanal ayrıttır: çevre $8l$. Taban ayrıtları içeride kalır.

## Kendini dene

### Soru 1
Ayrıt sayısı 16 olan bir piramidin yüz sayısı kaçtır?

A) 8
B) 9
C) 10
D) 16
E) 24

**Cevap:** B
**Çözüm:** Taban $n$ kenarlı ise ayrıt sayısı $2n$: $2n = 16$, $n = 8$. Yüz sayısı $n + 1 = 9$ (8 yan yüz ve taban). $8$, tabanı unutmaktır; $10$ prizma formülüdür ($n + 2$); $24$ ise prizmanın ayrıt sayısıdır ($3n$).

### Soru 2
![Kare dik piramit: taban ayrıtı AB = 10, mavi kesikli yükseklik TG = 12. BC'nin orta noktası M; kırmızı TM yan yüz yüksekliği soru işaretiyle gösterilmiş.](gorsel/tyt-matematik/26-03-kd2.svg "TG tabana, TM de BC kenarına diktir.")

Şekildeki kare dik piramidin taban ayrıtı 10 birim, yüksekliği 12 birimdir. Bu piramidin yanal alanı kaç birimkaredir?

A) 130
B) 240
C) 260
D) 360
E) 520

**Cevap:** C
**Çözüm:** $|GM| = 5$, $h_Y^2 = 12^2 + 5^2 = 169$, $h_Y = 13$. Yanal alan $\dfrac{40 \cdot 13}{2} = 260$. $240$, $h_Y$ yerine $h$ kullanmaktır; $360$ tabanı da eklemektir (yüzey alanı); $520$, $2$'ye bölmeyi unutmaktır; $130$ ise $2$'ye iki kez bölmektir.

### Soru 3
![Kare dik piramit: taban ayrıtı AB = 8, BC'nin orta noktası M, kırmızı TM = 5 yan yüz yüksekliği.](gorsel/tyt-matematik/26-03-kd3.svg "Verilen 5, yan yüzün yüksekliğidir; piramidin yüksekliği değildir.")

Şekildeki kare dik piramidin taban ayrıtı 8 birim, yan yüz yüksekliği 5 birimdir. Bu piramidin hacmi kaç birimküptür?

A) 64
B) 80
C) 320/3
D) 192
E) 320

**Cevap:** A
**Çözüm:** $|GM| = 4$, $h^2 = 5^2 - 4^2 = 9$, $h = 3$. $V = \dfrac{64 \cdot 3}{3} = 64$. $320/3$, $h$ yerine $h_Y = 5$ koymaktır; $192$, $3$'e bölmeyi unutmaktır; $320$ ikisini birden yapmaktır; $80$ ise yanal alandır ($\frac{32 \cdot 5}{2}$).

## Özet kartı

- $n$ kenarlı tabanda: köşe $n + 1$, ayrıt $2n$, yüz $n + 1$.
- Dik piramit: yükseklik tabanın merkezine ($G$) iner; düzgün dik piramitte yanal ayrıtlar eşit.
- Kare piramitte: $h_Y^2 = h^2 + \left(\frac{a}{2}\right)^2$, $l^2 = h^2 + \left(\frac{a\sqrt{2}}{2}\right)^2$.
- Yanal alan $A_Y = \dfrac{Ç_T \cdot h_Y}{2}$; yüzey alanı $A = A_T + A_Y$ (tek taban).
- Hacim $V = \dfrac{A_T \cdot h}{3}$: aynı tabanlı, aynı yükseklikli prizmanın üçte biri.
- Hacimde $h$, yanal alanda $h_Y$.

## Sonraki adım

Alıştırmaya geç (aşağıdaki düğme). Sonraki ders: **Düzgün Dört Yüzlü**. O, bütün ayrıtları eşit olan üçgen piramittir; bugünkü dik üçgen yöntemini eşkenar üçgen tabana uygulayacaksın.
