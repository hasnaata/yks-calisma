---
baslik: Merkezi Yayılım Ölçüleri
ders: tyt-matematik
sure: 20 dk
kaynak: MEBİ Konu Özeti 85718ea3a8
guncelleme: 2026-11-18
---
# Merkezi Yayılım Ölçüleri

<div class="giris" dir="rtl" lang="ar">

**الدرس ده عن إيه؟** المتوسط لوحده مش بيقولك كل حاجة؛ الدرس ده بيوريك إزاي تقيس البيانات متفرّقة قد إيه، وده اسمه مقاييس التشتت (merkezi yayılım ölçüleri).

- هتحسب المدى (açıklık): أكبر قيمة ناقص أصغر قيمة، وتعرف ليه الحكم بيه سطحي.
- هتتعلم الانحراف المعياري (standart sapma) في خمس خطوات ثابتة، وإن القسمة بتبقى على عدد البيانات ناقص 1.
- هتعرف إيه اللي بيحصل لما تزوّد رقم ثابت على كل البيانات أو تضربها كلها في رقم.

**ليه مهم؟** في TYT بييجي غالبًا جدول أو رسم لمجموعتين ويسألك: مين أكتر استقرارًا (tutarlı)؟ الحساب قصير، والمهم إنك تفهم الانحراف المعياري الصغير معناه إيه.

٢٠ دقيقة بس، وبعدها هتقارن أي مجموعتين وإنت واثق من نفسك.

</div>

**Bu dersin sonunda:** bir veri grubunun açıklığını ve standart sapmasını hesaplayabilecek, iki grubu standart sapmalarına bakarak "hangisi daha tutarlı?" diye karşılaştırabileceksin.

> **TYT'de yeri:** Genellikle tablo ya da grafikle verilen iki veri grubu sorulur: "Açıklık kaçtır?", "Hangi grubun puanları daha istikrarlıdır?", "Her veriye sabit eklenirse standart sapma ne olur?" Hesap kısa tutulur, yorum önemlidir.

## Önce hatırla

<details><summary>Merkezi eğilim ölçülerinden: 5, 8, 3, 8, 6 veri grubunun aritmetik ortalaması, ortancası ve tepe değeri nedir?</summary>
Ortalama: $\frac{5 + 8 + 3 + 8 + 6}{5} = \frac{30}{5} = 6$. Sıralı hâli $3, 5, 6, 8, 8$; 5 veri var, ortanca 3. terim: <b>6</b>. En çok tekrar eden 8, tepe değer: <b>8</b>.
</details>

<details><summary>Merkezi eğilim ölçülerinden: 4 sayının ortalaması 7'dir. Bu gruba bir sayı eklenince ortalama 8 oluyor. Eklenen sayı kaçtır?</summary>
Önce toplamlar: $4 \cdot 7 = 28$, sonra $5 \cdot 8 = 40$. Eklenen sayı $40 - 28 = $ <b>12</b>.
</details>

## Ortalama neden yetmez?

**Örnek.** İki basketbolcunun son 5 maçtaki sayıları:

| Oyuncu | Sayılar | Ortalama | Ortanca |
|---|---|---|---|
| Kaan | 14, 15, 16, 17, 18 | 16 | 16 |
| Mert | 4, 10, 16, 22, 28 | 16 | 16 |

Ortalama da ortanca da aynı. Ama Kaan her maç 16 civarında atıyor; Mert bir maç 4, bir maç 28 atıyor. Merkezi eğilim ölçüleri bu farkı göstermez. Verilerin **ne kadar dağıldığını** gösteren ölçülere **merkezi yayılım ölçüleri** denir. TYT'de ikisi kullanılır: **açıklık** ve **standart sapma**.

![İki yatay sayı doğrusu. Kaan'ın beş noktası 14 ile 18 arasında sıkışık, Mert'in beş noktası 4 ile 28 arasına yayılmış. İkisinde de 16'da kesikli ortalama çizgisi var.](gorsel/tyt-matematik/16-02-iki-oyuncu.svg "Ortalama çizgisi iki oyuncuda da aynı yerde. Farkı noktaların ortalamaya uzaklığı yaratıyor.")

## Açıklık

**Örnek.** Bir haftanın en düşük sıcaklıkları (°C): $12, -3, 7, 15, 4, -1, 9$. Açıklık kaçtır?

En büyük değer $15$, en küçük değer $-3$. Açıklık $= 15 - (-3) = 18$.

**Kural.** $\text{Açıklık} = \text{en büyük değer} - \text{en küçük değer}$

- Açıklık büyükse veriler **heterojen** (uç değerler birbirinden uzak), küçükse **homojen** (veriler birbirine yakın) denir.
- Açıklık yalnızca iki uç değere bakar. Aradaki veriler ne olursa olsun değişmez. Bu yüzden açıklığa dayalı yorum **yüzeyseldir**: tek bir uç değer açıklığı büyütür. Yukarıdaki örnekte 15 yerine 30 olsaydı açıklık 33 olurdu, diğer altı gün aynı kalsa bile.

Yukarıdaki iki oyuncuda: Kaan'ın açıklığı $18 - 14 = 4$, Mert'in açıklığı $28 - 4 = 24$.

## Standart sapma

Standart sapma, verilerin **ortalamadan ortalama ne kadar uzak** olduğunu ölçer ve $S$ ile gösterilir. Açıklıktan farkı: **bütün verileri** hesaba katar.

**Örnek.** $3, 5, 9, 10, 13$ veri grubunun standart sapmasını bul.

**1. Ortalama:** $\bar{x} = \frac{3 + 5 + 9 + 10 + 13}{5} = \frac{40}{5} = 8$

**2. Her verinin ortalamadan farkı:**

![Sayı doğrusunda 3, 5, 9, 10 ve 13 noktaları; 8'de kesikli ortalama çizgisi. Ortalamadan her noktaya ok: eksi 5, eksi 3, artı 1, artı 2, artı 5.](gorsel/tyt-matematik/16-02-sapmalar.svg "Soldaki oklar eksi, sağdakiler artı. Eksiler ile artılar toplamda birbirini götürür: −5 − 3 + 1 + 2 + 5 = 0.")

**3. Farkların kareleri ve toplamı:**

| $x$ | $x - \bar{x}$ | $(x - \bar{x})^2$ |
|---|---|---|
| 3 | $-5$ | 25 |
| 5 | $-3$ | 9 |
| 9 | $1$ | 1 |
| 10 | $2$ | 4 |
| 13 | $5$ | 25 |
| | **Toplam: 0** | **Toplam: 64** |

**4. Veri sayısının 1 eksiğine böl:** $n = 5$, $\frac{64}{5 - 1} = \frac{64}{4} = 16$

**5. Karekök al:** $S = \sqrt{16} = 4$

![Beş kutulu akış şeması: ortalamayı bul, her veriden ortalamayı çıkar, farkların karelerini topla, toplamı n eksi 1'e böl, karekökünü al.](gorsel/tyt-matematik/16-02-yontem.svg "Beş adım hep bu sırayla yapılır. En çok unutulan adımlar 4 ve 5.")

**Kural.** $n$ veriden oluşan bir grupta

$$S = \sqrt{\frac{(x_1 - \bar{x})^2 + (x_2 - \bar{x})^2 + \dots + (x_n - \bar{x})^2}{n - 1}}$$

- Farkların toplamı **her zaman 0'dır**. Bu yüzden farklar doğrudan toplanmaz, önce kareleri alınır.
- MEB ders kitabındaki tanımda bölen $n$ değil **$n - 1$**'dir. Bu derste hep $n - 1$'e bölüyoruz.
- $S \ge 0$'dır. $S = 0$ ise bütün veriler birbirine eşittir (açıklık da 0'dır).

## Standart sapmayı yorumlamak

**Örnek.** Kaan ile Mert'i standart sapmayla karşılaştır.

Kaan: farklar $-2, -1, 0, 1, 2$; kareler toplamı $10$; $S = \sqrt{\frac{10}{4}} \approx 1{,}6$.
Mert: farklar $-12, -6, 0, 6, 12$; kareler toplamı $360$; $S = \sqrt{\frac{360}{4}} = \sqrt{90} \approx 9{,}5$.

Mert'in farkları Kaan'ınkilerin tam 6 katı, standart sapması da 6 katı. Kaan daha **istikrarlı** bir oyuncudur.

| Standart sapma küçükse | Standart sapma büyükse |
|---|---|
| Veriler ortalamaya ve birbirine yakın | Veriler ortalamadan ve birbirinden uzak |
| Düzenli, tutarlı, istikrarlı, güvenilir | Düzensiz, tutarsız, istikrarsız |
| Grup homojen | Grup heterojen |

**Kural.** İki grubu karşılaştırırken standart sapması **küçük** olan grup daha tutarlıdır. Ortalamalar eşit olmak zorunda değildir; soru "tutarlılık" soruyorsa ortalamaya değil standart sapmaya bakılır.

## Bütün veriler değişince

**Örnek.** $3, 5, 9, 10, 13$ grubunda ($\bar{x} = 8$, açıklık 10, $S = 4$):

- Her veriye 2 eklenirse: $5, 7, 11, 12, 15$. Ortalama $10$ olur; farklar yine $-5, -3, 1, 2, 5$. Açıklık 10, $S = 4$: **değişmez**.
- Her veri 2 ile çarpılırsa: $6, 10, 18, 20, 26$. Ortalama $16$; farklar $-10, -6, 2, 4, 10$, yani 2 katı. Açıklık $20$, $S = 8$: **2 katına çıkar**.

![Üç nokta dizisi alt alta: asıl veri, her veriye 2 eklenmiş hâli ve her verinin 2 ile çarpılmış hâli. İlk ikisinde noktaların arası aynı, sağda S eşittir 4; üçüncüde aralar iki kat, S eşittir 8.](gorsel/tyt-matematik/16-02-kaydirma.svg "Sabit eklemek grubu olduğu gibi kaydırır, noktaların arası değişmez. Çarpmak ise araları açar.")

**Kural.** Her veri $k$ ile çarpılıp ($k > 0$) üzerine $c$ eklenirse:

| | Ortalama | Açıklık | Standart sapma |
|---|---|---|---|
| Her veriye $c$ ekle | $\bar{x} + c$ | aynı | aynı |
| Her veriyi $k$ ile çarp | $k \cdot \bar{x}$ | $k$ katı | $k$ katı |

## ÖSYM tuzakları

> **$n$'ye bölmek:** Standart sapmada kareler toplamı $n - 1$'e bölünür. $3, 5, 9, 10, 13$ için $\frac{64}{5}$ yazan yanlış sonuca gider.

> **Karekökü unutmak:** $\frac{64}{4} = 16$ standart sapma değildir; $S = \sqrt{16} = 4$. Seçeneklerde 16 da bulunur.

> **Açıklıkta sırayı unutmak:** Açıklık "son veri eksi ilk veri" değildir. Önce en büyük ve en küçük değeri bul. Negatif veri varsa $15 - (-3) = 18$ olur, 12 değil.

> **Sabit eklemenin yayılımı değiştirdiğini sanmak:** Herkese 5 puan eklenirse ortalama 5 artar ama açıklık ve standart sapma **aynı kalır**. Çarpma ise ikisini de aynı oranda değiştirir.

> **Açıklığı eşit olan gruplar aynı dağılır sanmak:** $2, 6, 10, 14, 18$ ile $2, 9, 10, 11, 18$ gruplarının ortalaması da açıklığı da aynıdır; ama ikinci grupta ortadaki veriler ortalamaya daha yakın olduğu için standart sapması daha küçüktür.

## Kendini dene

### Soru 1
$17, 9, 24, 11, 6, 20$ veri grubunun açıklığı kaçtır?

A) 3
B) 14
C) 15
D) 18
E) 30

**Cevap:** D
**Çözüm:** En büyük değer 24, en küçük değer 6: açıklık $24 - 6 = 18$. 3, "son veri eksi ilk veri" ($20 - 17$); 14, ortanca ($\frac{11 + 17}{2}$); 15, en küçük yerine 9'u almak; 30 ise uçları toplamaktır.

### Soru 2
$6, 8, 10, 12, 14$ veri grubunun standart sapması kaçtır?

A) $\sqrt{8}$
B) $\sqrt{10}$
C) 8
D) 10
E) 40

**Cevap:** B
**Çözüm:** Ortalama $\frac{50}{5} = 10$. Farklar $-4, -2, 0, 2, 4$; kareleri $16, 4, 0, 4, 16$, toplam $40$. $n - 1 = 4$'e böl: $\frac{40}{4} = 10$. Karekök: $S = \sqrt{10}$. $\sqrt{8}$, 5'e bölmekten; 8 açıklıktan; 10 karekökü unutmaktan; 40 hiç bölmemekten gelir.

### Soru 3
Bir sınavda iki sınıfın sonuçları şöyledir:

| Sınıf | Ortalama | Standart sapma |
|---|---|---|
| A | 65 | 4 |
| B | 65 | 12 |

Buna göre aşağıdakilerden hangisi **kesinlikle** doğrudur?

A) B sınıfındaki en yüksek not, A sınıfındakinden büyüktür.
B) İki sınıfın notlarının açıklıkları eşittir.
C) A sınıfındaki öğrenci sayısı B sınıfındakinden azdır.
D) B sınıfındaki notların ortancası 65'tir.
E) A sınıfının notları ortalama çevresinde daha az dağılmıştır.

**Cevap:** E
**Çözüm:** Standart sapma, verilerin ortalamadan ne kadar uzak olduğunu ölçer; A'nınki küçük olduğu için notlar 65 çevresinde daha toplu, yani daha az dağılmıştır. Diğerleri kesin değildir: en yüksek not ve açıklık yalnız uç değerlere bağlıdır, öğrenci sayısı verilmemiştir, ortalama 65 olsa da ortanca farklı olabilir.

## Özet kartı

- Açıklık = en büyük değer − en küçük değer. Yalnızca uçlara bakar, yorumu yüzeyseldir.
- Standart sapma: ortalama → farklar → kareler toplamı → $n - 1$'e böl → karekök.
- Ortalamadan farkların toplamı her zaman 0'dır.
- Küçük $S$: tutarlı, istikrarlı, homojen. Büyük $S$: dağınık, istikrarsız, heterojen.
- Her veriye sabit eklemek açıklığı ve $S$'yi değiştirmez; $k$ ile çarpmak ikisini de $k$ katına çıkarır.
- $S = 0$ ancak bütün veriler eşitse olur.

## Sonraki adım

Alıştırmaya geç (aşağıdaki düğme). Bu dersle **Merkezi Eğilim ve Yayılım Ölçüleri** konusu biter. Sonraki ders **Histogram**; verileri grafikle göstermeyi öğrenirken açıklığı yeniden kullanacaksın.
