---
baslik: Doğrusal ve Parçalı Fonksiyonlar · Alıştırma
ders: tyt-matematik
soru: 12
guncelleme: 2026-11-17
---
# Alıştırma: Doğrusal ve Parçalı Fonksiyonlar

Sorular özgündür ve ÖSYM soru tarzında yazılmıştır. Derse bakmadan çöz.

## Isınma

### Soru 1 · Kolay
$f\colon \mathbb{R} \to \mathbb{R}$, $f(x) = (a - 3)x^2 + 2x + a$ doğrusal bir fonksiyon olduğuna göre $f(4)$ kaçtır?

A) 3
B) 5
C) 8
D) 9
E) 11

**Cevap:** E
**Çözüm:** Doğrusal olması için $x^2$ terimi olmamalı: $a - 3 = 0$, $a = 3$. $f(x) = 2x + 3$, $f(4) = 8 + 3 = 11$. $8$, sabit terimi unutmaktır; $5$, $a = -3$ alan işaret hatasından gelir; $9$ ise $f(3)$ değeridir.

### Soru 2 · Kolay
$$f(x) = \begin{cases} 2x + 3, & x < 1 \\ 4, & 1 \le x \le 3 \\ x^2 - 6, & x > 3 \end{cases}$$

olduğuna göre $f(-1) + f(3) + f(4)$ toplamı kaçtır?

A) 9
B) 14
C) 15
D) 19
E) 20

**Cevap:** C
**Çözüm:** $-1 < 1$: $f(-1) = -2 + 3 = 1$. $3$, $1 \le x \le 3$ aralığında: $f(3) = 4$. $4 > 3$: $f(4) = 16 - 6 = 10$. Toplam $1 + 4 + 10 = 15$. $f(3)$'ü son satırdan ($3$) hesaplayan $14$'ü, $f(3)$'ü ilk satırdan ($9$) hesaplayan $20$'yi bulur.

### Soru 3 · Kolay
![Koordinat düzleminde yükselen bir doğru. Doğru y eksenini −2'de, x eksenini 4'te kesiyor.](gorsel/tyt-matematik/11-05-soru3.svg "Doğrunun eksenleri kestiği iki noktaya bak.")

Grafiği şekilde verilen doğrusal $f$ fonksiyonu için $f(10)$ kaçtır?

A) 3
B) 5
C) 7
D) 8
E) 18

**Cevap:** A
**Çözüm:** $y$ eksenini $-2$'de kestiği için $n = -2$. $x$, $0$'dan $4$'e 4 artınca $y$, $-2$'den $0$'a 2 artıyor: $m = \frac{2}{4} = \frac{1}{2}$. $f(x) = \frac{x}{2} - 2$, $f(10) = 5 - 2 = 3$. $5$, $n$'yi unutmak; $7$, $n$'yi $+2$ almak; $18$ ise eğimi ters çevirip $m = 2$ almaktır.

## Orta

### Soru 4 · Orta
$f$ doğrusal bir fonksiyondur. $f(3) = 10$ ve $f(7) = 22$ olduğuna göre $f(a) = 40$ eşitliğini sağlayan $a$ kaçtır?

A) 10
B) 11
C) 12
D) 13
E) 121

**Cevap:** D
**Çözüm:** $m = \frac{22 - 10}{7 - 3} = 3$; $f(3) = 9 + n = 10$, $n = 1$. $f(x) = 3x + 1$. $3a + 1 = 40$, $a = 13$. $12$, "$f(3) = 10$ ise $f(x)$, $x$ ile orantılı" sanıp $\frac{40 \cdot 3}{10}$ yapmaktır; $121$ ise $a$ yerine $f(40)$ hesaplamaktır.

### Soru 5 · Orta
$$f(x) = \begin{cases} x^2 - 1, & x < 2 \\ 3x - 4, & x \ge 2 \end{cases}$$

olduğuna göre $f(f(-2))$ kaçtır?

A) 3
B) 5
C) 8
D) 24
E) 99

**Cevap:** B
**Çözüm:** $-2 < 2$: $f(-2) = (-2)^2 - 1 = 3$. $3 \ge 2$: $f(3) = 9 - 4 = 5$. $3$, ikinci adımı unutmaktır; $8$, $f(3)$'ü üst satırdan ($9 - 1$) hesaplamaktır; $24$, $(-2)^2$ yerine $-2^2 = -4$ yazıp $f(-5)$ bulmaktır.

### Soru 6 · Orta
$$f(x) = \begin{cases} 2x + 6, & x < -1 \\ x^2, & -1 \le x \le 3 \\ 15 - x, & x > 3 \end{cases}$$

olduğuna göre $f(x) = 4$ eşitliğini sağlayan $x$ değerlerinin toplamı kaçtır?

A) 9
B) 10
C) 11
D) 12
E) 13

**Cevap:** E
**Çözüm:** Her satırı çöz, aralığı kontrol et.
- $2x + 6 = 4 \Rightarrow x = -1$; ama bu satır $x < -1$ için: **atılır**.
- $x^2 = 4 \Rightarrow x = 2$ ya da $x = -2$; aralık $[-1, 3]$: $2$ kalır, $-2$ **atılır**.
- $15 - x = 4 \Rightarrow x = 11 > 3$: geçerli.

Çözümler $2$ ve $11$, toplam $13$. Aralık kontrolü yapmayan $-1 - 2 + 2 + 11 = 10$ bulur; yalnızca $-2$'yi tutan $11$'i, yalnızca $-1$'i tutan $12$'yi bulur.

### Soru 7 · Orta
![Koordinat düzleminde parçalı bir grafik. x = 2'nin solunda (−2, 0) ve (0, 1) noktalarından geçen yükselen bir doğru, (2, 2) noktasında içi boş daireyle bitiyor. x = 2'den başlayarak y = 4 yüksekliğinde yatay bir doğru var; (2, 4) noktası dolu daire.](gorsel/tyt-matematik/11-05-soru7.svg "Izgaranın her karesi 1 birimdir. x = 2'deki iki daireye dikkat et.")

Grafiği şekilde verilen $f$ fonksiyonu için $f(-4) + f(0) + f(2)$ toplamı kaçtır?

A) 2
B) 4
C) 5
D) 6
E) 7

**Cevap:** B
**Çözüm:** Grafikten: $f(-4) = -1$, $f(0) = 1$. $x = 2$'de boş daire $(2, 2)$ grafiğe ait değil, dolu daire $(2, 4)$ ait: $f(2) = 4$. Toplam $-1 + 1 + 4 = 4$. Boş daireyi okuyan $-1 + 1 + 2 = 2$'yi, iki daireyi de sayan $6$'yı bulur.

## ÖSYM tarzı

### Soru 8 · ÖSYM tarzı
Bir şehirde taksi ücreti, sabit bir açılış ücreti ile gidilen her kilometre için sabit bir ücretin toplamıdır. Bu taksiyle 4 km'lik bir yolculuk 160 TL, 10 km'lik bir yolculuk 310 TL tutmaktadır.

Buna göre açılış ücreti kaç TL'dir?

A) 25
B) 31
C) 40
D) 60
E) 85

**Cevap:** D
**Çözüm:** Ücret $f(x) = mx + n$. Fazladan 6 km için $310 - 160 = 150$ TL: $m = 25$ TL/km. $160 = 25 \cdot 4 + n$, $n = 60$ TL. Kontrol: $25 \cdot 10 + 60 = 310$. $40$, açılış ücreti yokmuş gibi $160 \div 4$ yapmaktır; $25$ km başına ücrettir; $85$ ise 1 km'lik yolculuğun tutarıdır.

### Soru 9 · ÖSYM tarzı
Bir ilçede su faturası şöyle hesaplanıyor: aylık ilk 10 m³ için m³ başına 8 TL, 10 m³'ü aşan her m³ için 16 TL.

Bir ayda 8 m³ su kullanan bir hanenin faturasının 3 katı kadar fatura ödeyen başka bir hane, o ay kaç m³ su kullanmıştır?

A) 7
B) 12
C) 17
D) 20
E) 24

**Cevap:** C
**Çözüm:** Birinci hane: $8 \cdot 8 = 64$ TL. İkinci hane: $3 \cdot 64 = 192$ TL. $192 > 80$ olduğundan 10 m³ aşılmış: $80 + 16(x - 10) = 192 \Rightarrow x - 10 = 7 \Rightarrow x = 17$. $24$, faturayı kullanımla orantılı sanıp $3 \cdot 8$ yapmaktır; $7$, ilk 10 m³'ü eklemeyi unutmaktır; $12$ ise bütün suya 16 TL uygulamaktır ($192 \div 16$).

### Soru 10 · ÖSYM tarzı
Bir telefon şirketinin iki aylık tarifesi vardır:

- **A tarifesi:** 100 TL sabit ücret ve konuşulan her dakika için 2 TL.
- **B tarifesi:** İlk 200 dakika dahil 300 TL; 200 dakikayı aşan her dakika için 3 TL.

Bir ayda konuşulan süre için B tarifesinin A tarifesinden **pahalı olmadığı** en uzun süre kaç dakikadır?

A) 100
B) 200
C) 300
D) 400
E) 700

**Cevap:** D
**Çözüm:** $A(x) = 100 + 2x$. 200 dakikaya kadar $B = 300$; eşitlik $100 + 2x = 300$, $x = 100$. 200 dakikadan sonra $B(x) = 300 + 3(x - 200) = 3x - 300$. $3x - 300 \le 100 + 2x \Rightarrow x \le 400$. Kontrol: $x = 400$'de ikisi de $900$ TL; $x = 401$'de $B = 903 > A = 902$. B, $100 \le x \le 400$ için pahalı değildir; en uzun süre $400$. $100$, ilk eşitliği cevap sanmaktır; $700$ ise B'deki 300 TL'yi unutup $100 + 2x = 3(x - 200)$ yazmaktır.

### Soru 11 · ÖSYM tarzı
Pozitif tam sayılarda tanımlı bir $f$ fonksiyonu, çift sayıyı yarısına, tek sayıyı ise 3 katının 1 fazlasına götürüyor:

$$f(x) = \begin{cases} \dfrac{x}{2}, & x \text{ çift} \\ 3x + 1, & x \text{ tek} \end{cases}$$

Buna göre $f(f(x)) = 4$ eşitliğini sağlayan $x$ pozitif tam sayılarının toplamı kaçtır?

A) 9
B) 16
C) 18
D) 25
E) 27

**Cevap:** C
**Çözüm:** Önce $f(y) = 4$: $y$ çiftse $\frac{y}{2} = 4$, $y = 8$; $y$ tekse $3y + 1 = 4$, $y = 1$. İki değer de koşuluna uyuyor.
- $f(x) = 8$: çift $x$ için $x = 16$; tek $x$ için $3x + 1 = 8$, $x = \frac{7}{3}$ tam sayı değil.
- $f(x) = 1$: çift $x$ için $x = 2$; tek $x$ için $3x + 1 = 1$, $x = 0$ pozitif ve tek değil.

Çözümler $2$ ve $16$, toplam $18$. Kontrol: $f(16) = 8$, $f(8) = 4$; $f(2) = 1$, $f(1) = 4$. $9$, ara değerleri ($1 + 8$) toplamaktır; $27$ ise ara değerleri de cevaba katmaktır.

### Soru 12 · ÖSYM tarzı
Yanan bir mumun boyu zamanla doğrusal olarak azalmaktadır. Mum yakıldıktan 2 saat sonra boyu 21 cm, 5 saat sonra 12 cm olarak ölçülüyor.

Buna göre mum, yakıldıktan kaç saat sonra boyu ilk boyunun $\frac{2}{3}$'üne iner?

A) 3
B) 6
C) 9
D) 12
E) 18

**Cevap:** A
**Çözüm:** 3 saatte $21 - 12 = 9$ cm kısalıyor: saatte 3 cm. İlk boy $21 + 2 \cdot 3 = 27$ cm, yani boy $h(t) = 27 - 3t$. İlk boyun $\frac{2}{3}$'ü $18$ cm: $27 - 3t = 18$, $t = 3$. $6$, boyun $\frac{1}{3}$'e indiği an ($9$ cm); $9$, mumun bittiği an; $18$ ise saat yerine santimetre değeridir.
