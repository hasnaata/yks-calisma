---
baslik: Küp
ders: tyt-matematik
sure: 20 dk
kaynak: MEBİ Konu Özeti dba71cdf63
guncelleme: 2026-11-18
---
# Küp

<div class="giris" dir="rtl" lang="ar">

**الدرس ده عن إيه؟** عن المكعب (küp): منشور (prizma) كل أحرفه (ayrıt) متساوية، وكل أوجهه مربعات زي بعض.

- هتعرف تحسب الحجم (hacim) والمساحة الكلية (yüzey alanı) من طول حرف واحد بس.
- هتتعلم قطر الوجه (yüzey köşegeni) والقطر اللي بيعدّي جوه المكعب (cisim köşegeni)، وإزاي تطلّعهم بفيثاغورس (Pisagor).
- هتعرف تقرا شبكة المكعب (açınım) وتحدد الأوجه المتقابلة (karşılıklı yüzler)، وتحسب المساحة لما مكعبين يتلزقوا في بعض.

**ليه مهم؟** المكعب بييجي كتير في TYT، ساعات لوحده وساعات جوه سؤال عن مية في حوض أو مكعبات صغيرة متلزقة.

هو 20 دقيقة بس، وكل قاعدة معاها رسمة ومثال محلول، فامشي معاه خطوة خطوة.

</div>

**Bu dersin sonunda:** bir küpün ayrıtından ya da köşegeninden yola çıkarak hacmini, yüzey alanını ve köşegenlerini bulabilecek, bir açınımda hangi yüzlerin karşılıklı olduğunu söyleyebileceksin.

> **TYT'de yeri:** Küp, katı cisim sorularının en sık gelenidir. Soru genelde bir uzunluk verir (ayrıtlar toplamı, köşegen, hacim) ve başka birini ister. "Yeni nesil" sorularda ise küpler yapıştırılır, köşesinden parça kesilir, suya batırılır ya da zar açınımı katlanır.

## Önce hatırla

<details><summary>Geçen dersten: Ayrıtları 3, 4 ve 12 cm olan dikdörtgenler prizmasının cisim köşegeni kaç cm'dir?</summary>
$\sqrt{3^2 + 4^2 + 12^2} = \sqrt{9 + 16 + 144} = \sqrt{169} = 13$ cm. Bugün aynı formülü üç ayrıtı da eşit olan prizmada kullanacaksın.
</details>

<details><summary>Geçen dersten: Ayrıtları 2, 3 ve 4 cm olan dikdörtgenler prizmasının yüzey alanı ve hacmi kaçtır?</summary>
Yüzey alanı $2(2 \cdot 3 + 2 \cdot 4 + 3 \cdot 4) = 2 \cdot 26 = 52$ cm², hacim $2 \cdot 3 \cdot 4 = 24$ cm³. Küpte bu formüller çok kısalır.
</details>

## Küp nedir?

**Bütün ayrıtları eşit uzunlukta olan dikdörtgenler prizmasına küp** denir. Yani küp, ayrıtları $a$, $a$, $a$ olan bir dikdörtgenler prizmasıdır; geçen dersteki her formül küpte de geçerlidir, sadece kısalır.

| Eleman | Sayı | Not |
|---|---|---|
| Yüz | 6 | Hepsi kenarı $a$ olan eş kare |
| Ayrıt | 12 | Hepsinin uzunluğu $a$ |
| Köşe | 8 | Her köşede 3 ayrıt ve 3 yüz birleşir |

## 1. Hacim ve yüzey alanı

**Örnek 1.** Ayrıtı $4$ cm olan küpün hacmi, yüzey alanı ve bütün ayrıtlarının uzunlukları toplamı kaçtır?

**Çözüm.**

1. Hacim: taban alanı $\cdot$ yükseklik $= 4^2 \cdot 4 = 4^3 = 64$ cm³. Şekilde her katta $4 \cdot 4 = 16$ birim küp var, 4 kat: $64$.
2. Yüzey alanı: 6 eş kare yüz, her biri $4^2 = 16$ cm². Toplam $6 \cdot 16 = 96$ cm².
3. Ayrıtlar toplamı: 12 ayrıt, her biri 4 cm. Toplam $12 \cdot 4 = 48$ cm.

![ABCDEFGH küpü, ayrıtları 4. Ön, sağ ve üst yüzler 4'e 4 birim karelere bölünmüş.](gorsel/tyt-matematik/26-02-hacim.svg "Her yüzde 16 birim kare var, 6 yüz: 96. Her katta 16 birim küp var, 4 kat: 64.")

**Kural:** Ayrıtı $a$ olan küpte

$$V = a^3 \qquad A = 6a^2 \qquad \text{ayrıtlar toplamı} = 12a$$

Ayrıt 2 katına çıkarsa yüzey alanı $2^2 = 4$ katına, hacim $2^3 = 8$ katına çıkar. Genel olarak ayrıt $k$ katına çıkarsa alan $k^2$, hacim $k^3$ katına çıkar.

> **Tuzak:** Yan yüzler (yanal alan) 4 tanedir: $4a^2$. Soru "yüzey alanı" diyorsa 6 yüzü de say; "üstü açık kutu" diyorsa 5 yüzü say. Ayrıt sayısını 8 sanmak da sık görülür: küpün 8 **köşesi**, 12 **ayrıtı** vardır.

## 2. Yüzey köşegeni ve cisim köşegeni

**Örnek 2.** Ayrıtı $5$ cm olan küpte $|AC|$ yüzey köşegenini ve $|AG|$ cisim köşegenini bul.

**Çözüm.**

1. $ABC$ üçgeni $B$'de diktir (kare yüzün köşesi). Pisagor: $|AC|^2 = 5^2 + 5^2 = 50 \Rightarrow |AC| = 5\sqrt{2}$.
2. $[CG]$ ayrıtı taban düzlemine diktir, bu yüzden $ACG$ üçgeni $C$'de diktir. Pisagor: $|AG|^2 = |AC|^2 + |CG|^2 = 50 + 25 = 75 \Rightarrow |AG| = 5\sqrt{3}$.
3. Kontrol: geçen dersin formülüyle $\sqrt{5^2 + 5^2 + 5^2} = \sqrt{75} = 5\sqrt{3}$.

![Ayrıtı 5 olan küp. Tabandaki AC yüzey köşegeni yeşil kesikli, CG ayrıtı yeşil, AG cisim köşegeni kırmızı. C köşesinde dik açı işareti var.](gorsel/tyt-matematik/26-02-kosegen.svg "Kırmızı cisim köşegeni, yeşil iki kenarlı dik üçgenin hipotenüsüdür: önce tabanda yüzey köşegeni, sonra yukarı bir ayrıt.")

**Kural:**

$$\text{yüzey köşegeni} = a\sqrt{2} \qquad \text{cisim köşegeni} = a\sqrt{3}$$

Köşegen verilip ayrıt sorulursa tersten git: cisim köşegeni $6\sqrt{3}$ ise $a = 6$, hacim $216$ olur. Cisim köşegeni $6$ ise $a = \dfrac{6}{\sqrt{3}} = 2\sqrt{3}$ olur.

> **Tuzak:** Yüzey köşegeni ile cisim köşegenini karıştırmak. Yüzey köşegeni bir **yüzün** üstünde durur ($\sqrt{2}$), cisim köşegeni küpün **içinden** geçer ($\sqrt{3}$). Bir küpte 12 yüzey köşegeni (her yüzde 2), 4 cisim köşegeni vardır.

## 3. Küpün açınımı

Küpü ayrıtlarından kesip düzleme açarsan 6 kareden oluşan bir **açınım** elde edersin. Farklı 11 açınım vardır; her 6 karelik şekil açınım değildir.

**Örnek 3.** Aşağıdaki dört şekilden hangileri katlanınca küp olur?

**Çözüm.**

1. İlk üç şekilde hiçbir kare üst üste gelmez; katlayınca 6 yüz de dolar. Üçü de açınımdır.
2. Dördüncüde kırmızı çerçeveli $2 \times 2$'lik blok var. Bu dört kare bir köşede buluşur; küpün bir köşesinde ise yalnız 3 yüz birleşir. Katlayınca iki kare üst üste biner, bir yüz boş kalır. Açınım değildir.

![Dört 6 karelik şekil. Mavi artı biçimli, yeşil ve sarı basamaklı şekillerin altında olur yazısı var. Pembe şekilde kırmızı çerçeveli 2'ye 2 kare blok var ve altında olmaz yazısı var.](gorsel/tyt-matematik/26-02-acinim.svg "2'ye 2 blok olan şekil katlanınca iki kare çakışır. Bir sırada 4'ten fazla kare olan şekil de açınım olamaz.")

**Kural:** Açınımda 6 kare bulunur, $2 \times 2$'lik blok bulunmaz, bir sırada en çok 4 kare yan yana durur.

> **Tuzak:** Bu üç koşul, şeklin açınım olmadığını hızlıca gösterir ama her zaman yeterli değildir. Emin değilsen bir kareyi taban seç, komşularını kafanda yukarı katla ve iki karenin aynı yere gelip gelmediğine bak.

## 4. Karşılıklı yüzler

**Örnek 4.** Şekildeki açınım katlanınca hangi yüzler karşılıklı olur?

**Çözüm.**

1. $2, 3, 4, 5$ yan yana bir sıradır; katlanınca küpün etrafını bir kuşak gibi sarar. Bu sırada **aralarında bir kare olan** yüzler karşılıklıdır: $2$ ile $4$, $3$ ile $5$.
2. Geriye kalan $1$ ve $6$ kuşağın alt ve üst kapağı olur: $1$ ile $6$ karşılıklıdır.

![Açınım: alt sırada 2, 3, 4, 5 yan yana; 1 numaralı kare 2'nin altında, 6 numaralı kare 5'in üstünde. Karşılıklı yüzler aynı renkte: 1 ve 6 sarı, 2 ve 4 mavi, 3 ve 5 yeşil.](gorsel/tyt-matematik/26-02-karsilikli.svg "Aynı renkli kareler katlanınca karşı karşıya gelir. Karşılıklı iki yüz açınımda hiçbir zaman yan yana olmaz.")

**Kural:**

- Düz bir sırada aralarında tam bir kare olan iki yüz karşılıklıdır.
- Dört karelik "Z" biçiminin iki ucu karşılıklıdır (merdiven biçimli açınımlarda işe yarar).
- Kenarı ortak olan iki yüz asla karşılıklı olamaz. Üç çift bulunur; son çifti eleyerek bul.

> **Tuzak:** Bir köşeden birleşen (çapraz duran) iki kareyi karşılıklı sanmak. Katlanınca bunlar komşu yüz olur. Zar sorularında karşılıklı yüzlerin toplamı 7'dir; açınımda sayıları bu kurala göre yerleştir.

## 5. Küpleri yapıştırma

**Örnek 5.** Ayrıtı $3$ cm olan iki küp bir yüzleri tam çakışacak biçimde yapıştırılıyor. Oluşan cismin yüzey alanı kaç cm²'dir?

**Çözüm.**

1. İki küpün yüzey alanları toplamı: $2 \cdot 6 \cdot 3^2 = 108$.
2. Yapışan yüzler dışarıda kalmaz. Her küpten bir yüz, yani $2$ yüz kaybolur: $2 \cdot 9 = 18$.
3. Yüzey alanı $108 - 18 = 90$ cm². Kontrol: cisim $6 \times 3 \times 3$ prizmadır, $2(18 + 18 + 9) = 90$.

![Ayrıtı 3 olan iki küp yan yana yapıştırılmış; 6'ya 3'e 3 dikdörtgenler prizması oluşmuş. Aradaki yapışma yüzü çizgiyle gösterilmiş.](gorsel/tyt-matematik/26-02-birlesim.svg "Ortadaki ortak yüz iki küpün de birer yüzüdür; ikisi de içeride kalır. Görünen yüz sayısı 12 değil 10'dur.")

**Kural:** Her yapışma yüzeyi dışarıdan **2 kare** yüz eksiltir. $n$ küp bir sıra hâlinde yapıştırılırsa $n - 1$ yapışma olur: yüzey alanı $(6n - 2(n - 1)) \cdot a^2$. Hacim ise sadece toplanır: $n \cdot a^3$.

> **Tuzak:** Yalnızca bir yüz çıkarmak ($108 - 9 = 99$). Yapışan yüzey iki küpe de aittir, iki kez çıkarılır.

## ÖSYM tuzakları

> **Alan ile hacmi karıştırmak.** Ayrıtı 6 olan küpte $6a^2 = 216$ ve $a^3 = 216$ çıkar. Sayı aynıdır ama birimler farklıdır (cm² ve cm³); başka ayrıtlarda bu eşitlik bozulur.

> **Ayrıtlar toplamını 6'ya ya da 8'e bölmek.** Ayrıtlar toplamı $48$ ise $a = 48 : 12 = 4$. Küpün 6 yüzü, 8 köşesi, 12 ayrıtı vardır.

> **Kat soruları.** Yüzey alanı 9 katına çıkıyorsa ayrıt 3 katına, hacim 27 katına çıkar. Alan ile hacim aynı oranda büyümez.

> **Köşeden küp kesmek.** Büyük bir küpün köşesinden küçük bir küp kesilirse 3 kare yüz gider ama yerine eş 3 kare yüz açılır: yüzey alanı **değişmez**, hacim azalır.

> **Yüzeyde en kısa yol.** Küpün yüzeyi üzerinde $A$'dan $G$'ye giden en kısa yol cisim köşegeni değildir (o, içinden geçer). İki yüzü açınım gibi düzleme açıp düz çizgi çizersin: kenarları $2a$ ve $a$ olan dikdörtgenin köşegeni, $a\sqrt{5}$.

## Kendini dene

### Soru 1
Cisim köşegeninin uzunluğu $6$ cm olan küpün hacmi kaç cm³'tür?

A) 8
B) $24\sqrt{3}$
C) 72
D) $54\sqrt{2}$
E) 216

**Cevap:** B
**Çözüm:** $a\sqrt{3} = 6 \Rightarrow a = \dfrac{6}{\sqrt{3}} = 2\sqrt{3}$. $V = (2\sqrt{3})^3 = 8 \cdot 3\sqrt{3} = 24\sqrt{3}$. $8$, $6$'yı $3$'e bölüp $a = 2$ almaktır; $54\sqrt{2}$, 6'yı yüzey köşegeni sanmaktır ($a = 3\sqrt{2}$); $72$ yüzey alanıdır ($6 \cdot 12$); $216$ ise $a = 6$ almaktır.

### Soru 2
![Açınım: alt sırada 1, 2, 3 yan yana; üst sırada 4, 5, 6 yan yana. 4 numaralı kare 3'ün tam üstünde.](gorsel/tyt-matematik/26-02-kd2.svg "Basamaklı açınım.")

Şekildeki açınım katlanarak bir küp elde ediliyor. Buna göre 2 numaralı yüzün karşısındaki yüzde hangi sayı yazılıdır?

A) 1
B) 3
C) 4
D) 5
E) 6

**Cevap:** D
**Çözüm:** $2, 3, 4, 5$ kareleri "Z" biçimindedir; Z'nin uçları karşılıklıdır: $2$ ile $5$. (Kontrol: $1, 2, 3$ düz sırasında $1$ ile $3$; $4, 5, 6$ düz sırasında $4$ ile $6$ karşılıklıdır. Üç çift tamam.) $1$ ve $3$, $2$ ile kenar paylaşır, karşılıklı olamaz; $4$ ise $1$ ile değil $6$ ile eşleşir.

### Soru 3
![Ayrıtı 2 cm olan iki küp yan yana yapıştırılmış.](gorsel/tyt-matematik/26-02-kd3.svg "İki küp bir yüzleri tam çakışacak biçimde yapışık.")

Ayrıtı $2$ cm olan iki küp, şekildeki gibi bir yüzleri tam çakışacak biçimde yapıştırılıyor. Oluşan cismin yüzey alanı kaç cm²'dir?

A) 16
B) 32
C) 40
D) 44
E) 48

**Cevap:** C
**Çözüm:** İki küpün yüzey alanları toplamı $2 \cdot 6 \cdot 4 = 48$. Yapışan iki yüz ($2 \cdot 4 = 8$) çıkar: $48 - 8 = 40$. Kontrol: $4 \times 2 \times 2$ prizma, $2(8 + 8 + 4) = 40$. $44$ yalnız bir yüzü çıkarmaktır; $48$ hiç çıkarmamaktır; $16$ hacimdir.

## Özet kartı

- Küp: bütün ayrıtları eşit dikdörtgenler prizması; 6 yüz, 12 ayrıt, 8 köşe.
- $V = a^3$, $A = 6a^2$, ayrıtlar toplamı $12a$.
- Yüzey köşegeni $a\sqrt{2}$, cisim köşegeni $a\sqrt{3}$.
- Ayrıt $k$ katı olursa alan $k^2$, hacim $k^3$ katı olur.
- Açınım: 6 kare, $2 \times 2$ blok yok; aralarında bir kare olanlar ve Z'nin uçları karşılıklıdır.
- Yapıştırma: her yapışma 2 yüz eksiltir; köşeden küp kesmek yüzey alanını değiştirmez.

## Sonraki adım

Alıştırmaya geç (aşağıdaki düğme). Sonraki ders: **Dik Piramitler**. Orada yan yüzler tek bir tepe noktasında buluşacak; bugünkü Pisagor adımları (yüzey köşegeni, sonra dik bir ayrıt) piramidin yüksekliğini bulurken de işine yarayacak.
