---
baslik: Fonksiyon Grafikleri ile İlgili Uygulamalar · Alıştırma
ders: tyt-matematik
soru: 12
guncelleme: 2026-11-17
---
# Alıştırma: Fonksiyon Grafikleri ile İlgili Uygulamalar

Sorular özgündür ve ÖSYM soru tarzında yazılmıştır. Derse bakmadan çöz.

## Isınma

### Soru 1 · Kolay
Aşağıda $f\colon [-2, 4] \to [-3, 5]$ fonksiyonunun grafiği verilmiştir.

![Koordinat düzleminde azalan kırık çizgi: (−2, 5) noktasından (0, 3)'e, oradan (4, −3)'e iniyor. Grafik x eksenini 2'de kesiyor. Uçlar dolu nokta.](gorsel/tyt-matematik/12-03-soru1.svg "Grafiğin y eksenini ve x eksenini kestiği noktalara bak.")

Buna göre $f^{-1}(0) - f(0)$ farkı kaçtır?

A) $-1$
B) $0$
C) $1$
D) $2$
E) $5$

**Cevap:** A
**Çözüm:** $f(0)$: $x = 0$'da grafiğin yüksekliği, yani y eksenini kestiği yer: $f(0) = 3$. $f^{-1}(0)$: $f$'nin $0$'a götürdüğü sayı, yani grafiğin x eksenini kestiği yer: $f^{-1}(0) = 2$. Fark $2 - 3 = -1$. Sırayı ters çeviren $1$, iki değeri toplayan $5$ bulur. $f^{-1}(0)$ yerine de $f(0)$ okuyan $3 - 3 = 0$ bulur.

### Soru 2 · Kolay
Doğrusal $f$ fonksiyonunun grafiği $A(1, 5)$ ve $B(3, 9)$ noktalarından geçmektedir. Buna göre $f(-1)$ kaçtır?

A) $1$
B) $3$
C) $4$
D) $5$
E) $7$

**Cevap:** A
**Çözüm:** Eğim $m = \frac{9 - 5}{3 - 1} = 2$. $f(1) = 5$ ise $2 + n = 5$, $n = 3$: $f(x) = 2x + 3$. $f(-1) = -2 + 3 = 1$. Kısa yol: $x$, $1$'den $-1$'e $2$ birim azalınca $f(x)$, $2 \cdot 2 = 4$ azalır: $5 - 4 = 1$. Yalnızca bir adım geri giden $3$, eğimi ters alıp ($\frac{1}{2}$) $f(x) = \frac{x}{2} + \frac{9}{2}$ yazan $4$ bulur.

### Soru 3 · Kolay
Aşağıda $[-4, 5]$ aralığında tanımlı $f$ fonksiyonunun grafiği verilmiştir.

![Koordinat düzleminde zikzak kırık çizgi: (−4, 2) noktasından (−1, −1)'e iner, orijinden geçerek (2, 2)'ye çıkar, (5, −1)'e iner. Grafik x eksenini −2, 0 ve 4'te kesiyor. Uçlar dolu nokta.](gorsel/tyt-matematik/12-03-soru3.svg "Grafiğin x ekseninin altında kaldığı aralıkları bul; uç noktaları unutma.")

Buna göre $f(x) < 0$ eşitsizliğini sağlayan kaç farklı $x$ tam sayısı vardır?

A) $1$
B) $2$
C) $3$
D) $4$
E) $5$

**Cevap:** B
**Çözüm:** Grafik x ekseninin altında: $(-2, 0)$ ve $(4, 5]$ aralıkları. $x = 5$ dolu nokta ve $f(5) = -1 < 0$, dahil. Tam sayılar: $-1$ ve $5$; toplam $2$. Kesim noktalarını ($-2$, $0$, $4$) da sayan $5$ bulur, ama orada $f(x) = 0$'dır. Sağ uçtaki $5$'i unutan $1$ bulur.

## Orta

### Soru 4 · Orta
Aşağıda bire bir ve örten $f\colon [-3, 3] \to [-2, 4]$ fonksiyonunun grafiği verilmiştir.

![Koordinat düzleminde artan kırık çizgi: (−3, −2) noktasından x eksenindeki (−2, 0)'a, oradan y eksenindeki (0, 3)'e, oradan (3, 4)'e çıkıyor. Uçlar dolu nokta.](gorsel/tyt-matematik/12-03-soru4.svg "Her adımda kendine sor: bu sayı girdi mi (x ekseni), görüntü mü (y ekseni)?")

Buna göre $(f \circ f)(-2) + (f^{-1} \circ f^{-1})(3)$ toplamı kaçtır?

A) $-2$
B) $0$
C) $1$
D) $3$
E) $5$

**Cevap:** C
**Çözüm:** $(f \circ f)(-2)$: $f(-2) = 0$ (grafik x eksenini $-2$'de kesiyor), $f(0) = 3$. Sonuç $3$. $(f^{-1} \circ f^{-1})(3)$: $3$ y ekseninde; $y = 3$ olan nokta $(0, 3)$, $f^{-1}(3) = 0$. Sonra $f^{-1}(0)$: $y = 0$ olan nokta $(-2, 0)$, $f^{-1}(0) = -2$. Toplam $3 + (-2) = 1$. İkinci bileşkede tek adım yapan $3 + 0 = 3$, birinci bileşkede tek adım yapan $0 + (-2) = -2$ bulur.

### Soru 5 · Orta
Aşağıda doğrusal $f$ fonksiyonunun grafiği verilmiştir.

![Koordinat düzleminde yükselen bir doğru. x eksenini 4'te, y eksenini −2'de kesiyor.](gorsel/tyt-matematik/12-03-soru5.svg "İki kesim noktasından eğimi ve n'yi bul.")

Buna göre $f^{-1}(3)$ kaçtır?

A) $-10$
B) $-\frac{1}{2}$
C) $\frac{5}{2}$
D) $6$
E) $10$

**Cevap:** E
**Çözüm:** Noktalar $(4, 0)$ ve $(0, -2)$. $m = \frac{0 - (-2)}{4 - 0} = \frac{1}{2}$, $n = -2$: $f(x) = \frac{x}{2} - 2$. $f^{-1}(3)$ için $\frac{x}{2} - 2 = 3$, $x = 10$. Kontrol: $f(10) = 5 - 2 = 3$. $-\frac{1}{2}$, $f(3)$ değeridir. Eğimi $2$ alan $\frac{5}{2}$, eğimin işaretini yanlış alan $-10$, $n$'yi unutan $6$ bulur.

### Soru 6 · Orta
Aşağıda bire bir ve örten $f\colon [-3, 4] \to [-4, 5]$ fonksiyonunun grafiği verilmiştir.

![Koordinat düzleminde artan kırık çizgi: (−3, −4) noktasından y eksenindeki (0, −1)'e, oradan (2, 3)'e, oradan (4, 5)'e çıkıyor. Uçlar dolu nokta.](gorsel/tyt-matematik/12-03-soru6.svg "f⁻¹(x) > 0 koşulunda x, f'nin bir görüntüsüdür; cevabı y ekseninde ara.")

Buna göre $f^{-1}(x) > 0$ eşitsizliğini sağlayan kaç farklı $x$ tam sayısı vardır?

A) $3$
B) $4$
C) $5$
D) $6$
E) $7$

**Cevap:** D
**Çözüm:** $f^{-1}(x) = t$ dersen $f(t) = x$ ve istenen $t > 0$. Grafiğin $t \in (0, 4]$ olan parçasının y değerleri: $f(0) = -1$ dahil değil, $f(4) = 5$ dahil; $f$ artan olduğu için $x \in (-1, 5]$. Tam sayılar $0, 1, 2, 3, 4, 5$; toplam $6$. $f(x) > 0$ sorusunu çözen $1, 2, 3, 4$ ile $4$ bulur. $-1$'i de dahil eden $7$ bulur.

### Soru 7 · Orta
Bir fidanın boyu her hafta aynı miktarda uzamaktadır. Fidan dikildikten 3 hafta sonra boyu $17$ cm, 7 hafta sonra $29$ cm olarak ölçülüyor.

Bu fidanın boyu dikildikten kaç hafta sonra $50$ cm olur?

A) $7$
B) $11$
C) $12$
D) $14$
E) $17$

**Cevap:** D
**Çözüm:** 4 haftada $29 - 17 = 12$ cm uzamış: hız haftada $3$ cm. Dikim anındaki boy: $17 - 3 \cdot 3 = 8$ cm. Kural $h(t) = 3t + 8$. $3t + 8 = 50$, $t = 14$. Kontrol: $h(14) = 42 + 8 = 50$. $(50 - 17) \div 3 = 11$ ve $(50 - 29) \div 3 = 7$, ölçümden sonra geçen hafta sayısıdır; 3 ve 7 hafta eklenmezse yanlış olur. $17$, cevaba bir kez daha 3 eklemektir.

## ÖSYM tarzı

### Soru 8 · ÖSYM tarzı
İki aracın depolarındaki yakıt miktarının gidilen yola göre değişimi aşağıdaki grafikte gösterilmiştir. Araçlar aynı noktadan aynı anda yola çıkıyor ve yakıt, gidilen yolla doğrusal olarak azalıyor.

![Koordinat düzleminde iki azalan doğru. Yatay eksen yol (km), dikey eksen yakıt (L). Mavi A doğrusu (0, 48)'den (600, 0)'a, yeşil B doğrusu (0, 36)'dan (900, 0)'a iniyor.](gorsel/tyt-matematik/12-03-soru8.svg "Her aracın başlangıç yakıtını ve deposunun kaç km'de bittiğini oku.")

İki aracın depolarındaki yakıt miktarı eşit olduğu anda, her bir depoda kaç litre yakıt vardır?

A) $12$
B) $24$
C) $30$
D) $36$
E) $42$

**Cevap:** B
**Çözüm:** A aracı $600$ km'de $48$ L harcıyor: km başına $\frac{48}{600} = 0{,}08$ L. B aracı $900$ km'de $36$ L: km başına $0{,}04$ L. $x$ km sonra $A = 48 - 0{,}08x$, $B = 36 - 0{,}04x$. Eşitle: $12 = 0{,}04x$, $x = 300$ km. Yakıt: $48 - 24 = 24$ L, kontrol $36 - 12 = 24$ L. $42$, başlangıç değerlerinin ortalamasıdır. $12$, A'nın deposu bittiğinde ($600$ km) B'de kalan yakıttır.

### Soru 9 · ÖSYM tarzı
Bir kafenin günlük kârı, o gün satılan kahve sayısına bağlı doğrusal bir fonksiyondur. Hiç kahve satılmayan bir günde kafe $600$ TL zarar ediyor, $40$ kahve satılan bir günde ise $200$ TL kâr ediyor.

Kafenin bir günde kâr edebilmesi için en az kaç kahve satması gerekir?

A) $10$
B) $15$
C) $20$
D) $30$
E) $31$

**Cevap:** E
**Çözüm:** Kâr fonksiyonu $K(x) = mx + n$. Zarar negatif kârdır: $K(0) = -600$, yani $n = -600$. $K(40) = 200$: $40m - 600 = 200$, $m = 20$. $K(x) = 20x - 600 > 0$ ise $x > 30$. En az $31$ kahve. $30$ kahvede $K(30) = 0$: ne kâr ne zarar. $10$, $15$ ve $20$ kahvede kâr negatiftir: örneğin $K(20) = -200$, kafe hâlâ zarardadır. $15 = 600 \div 40$, zararı $40$ kahveye bölmekten gelir.

### Soru 10 · ÖSYM tarzı
Bir şehirde taksi ücreti, gidilen yolun doğrusal bir fonksiyonudur. $4$ km'lik bir yolculuk için $110$ TL, $10$ km'lik bir yolculuk için $230$ TL ödeniyor.

Aynı tarifeyle $300$ TL ödenen bir yolculuk kaç km'dir?

A) $9{,}5$
B) $12$
C) $13{,}5$
D) $15$
E) $16{,}5$

**Cevap:** C
**Çözüm:** $6$ km fazladan gitmek $120$ TL fazla tutuyor: km başına $20$ TL. Açılış ücreti ($0$ km'deki değer): $110 - 4 \cdot 20 = 30$ TL. Ücret $U(x) = 20x + 30$. $20x + 30 = 300$, $x = 13{,}5$ km. $300 \div 20 = 15$, açılış ücretini unutmaktır. $(300 - 110) \div 20 = 9{,}5$, ilk $4$ km'yi eklemeyi unutmaktır. $16{,}5$, açılış ücretini çıkarmak yerine eklemekten gelir.

### Soru 11 · ÖSYM tarzı
Bir spor salonunun iki üyelik paketinde aylık ücretin, ay içinde salona gidilen gün sayısına göre değişimi aşağıdaki grafikte gösterilmiştir. İki paketin ücreti de gün sayısıyla doğrusal olarak artmaktadır.

![Koordinat düzleminde iki artan doğru. Yatay eksen gün, dikey eksen ücret (TL). Mavi A doğrusu (0, 300)'den (10, 500)'e, yeşil B doğrusu (0, 0)'dan (10, 450)'ye çıkıyor.](gorsel/tyt-matematik/12-03-soru11.svg "Grafik 10. günde bitiyor ama doğrular aynı hızla devam eder. Her paketin başlangıç ücretini ve günlük artışını bul.")

Bir ayda en fazla kaç gün salona giden bir kişi için B paketi, A paketinden daha ucuzdur?

A) $10$
B) $11$
C) $12$
D) $13$
E) $15$

**Cevap:** B
**Çözüm:** A: sabit $300$ TL, 10 günde $200$ TL artıyor; günlük $20$ TL, $A(x) = 20x + 300$. B: sabit ücret yok, 10 günde $450$ TL; günlük $45$ TL, $B(x) = 45x$. B daha ucuz: $45x < 20x + 300$, $25x < 300$, $x < 12$. En fazla $11$ gün. $12$. günde ikisi de $540$ TL; eşitlik "daha ucuz" sayılmaz. Grafikte görünen son değeri seçen $10$ bulur.

### Soru 12 · ÖSYM tarzı
Bir hava istasyonunun ekranı sıcaklığı kendi ölçeğinde "birim" olarak gösteriyor. Birim değeri, santigrat derece cinsinden sıcaklığın doğrusal bir fonksiyonudur: $10\,°\text{C}$ için ekranda $45$ birim, $30\,°\text{C}$ için $105$ birim görünüyor.

Ekranda $90$ birim görünüyorsa hava sıcaklığı kaç $°\text{C}$'tır?

A) $15$
B) $20$
C) $25$
D) $30$
E) $285$

**Cevap:** C
**Çözüm:** $f(x)$, $x\,°\text{C}$ için ekrandaki birim olsun. $20\,°\text{C}$ artış $60$ birim artış: $m = 3$. $f(10) = 45$ ise $30 + n = 45$, $n = 15$; $f(x) = 3x + 15$. İstenen $f^{-1}(90)$: $3x + 15 = 90$, $x = 25$. Kontrol: $f(25) = 75 + 15 = 90$. $285 = f(90)$, yönü ters çevirmektir. $90 \div 3 = 30$, $n$'yi unutmaktır. $(90 - 45) \div 3 = 15$, $10\,°\text{C}$'yi eklemeyi unutmaktır. $20$, birimin sıcaklıkla doğru orantılı ($45 \div 10 = 4{,}5$ kat) olduğunu sanmaktan gelir.
