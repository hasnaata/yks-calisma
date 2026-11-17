---
baslik: Diskriminant Kavramı ve Diskriminantın Kullanılması · Alıştırma
ders: tyt-matematik
soru: 12
guncelleme: 2026-11-17
---
# Alıştırma: Diskriminant Kavramı ve Diskriminantın Kullanılması

Sorular özgündür ve ÖSYM soru tarzında yazılmıştır. Derse bakmadan çöz.

## Isınma

### Soru 1 · Kolay
$3x^2 - 4x - 5 = 0$ denkleminin diskriminantı kaçtır?

A) $-44$
B) $31$
C) $36$
D) $44$
E) $76$

**Cevap:** E
**Çözüm:** $a = 3$, $b = -4$, $c = -5$. $\Delta = (-4)^2 - 4 \cdot 3 \cdot (-5) = 16 + 60 = 76$. $c$'nin eksisini kaybeden $16 - 60 = -44$, $a$'yı unutan $16 + 20 = 36$, $4$ çarpanını unutan $16 + 15 = 31$ bulur.

### Soru 2 · Kolay
Aşağıdaki denklemlerden hangisinin birbirinden farklı iki gerçek kökü vardır?

A) $x^2 + 4 = 0$
B) $x^2 - 2x + 1 = 0$
C) $x^2 + x + 1 = 0$
D) $2x^2 - x - 3 = 0$
E) $x^2 + 2x + 3 = 0$

**Cevap:** D
**Çözüm:** D'de $a = 2$ ile $c = -3$ ters işaretli; hesap yapmadan iki farklı kök vardır ($\Delta = 1 + 24 = 25$, kökler $-1$ ve $\frac{3}{2}$). A'da $\Delta = 0 - 16 = -16$, C'de $\Delta = 1 - 4 = -3$, E'de $\Delta = 4 - 12 = -8$: gerçek kök yok. B'de $\Delta = 4 - 4 = 0$: tek (çakışık) kök, $x = 1$.

### Soru 3 · Kolay
$x^2 - 2x - 1 = 0$ denkleminin büyük kökü kaçtır?

A) $-1 + \sqrt{2}$
B) $1$
C) $1 + \sqrt{2}$
D) $2 + \sqrt{2}$
E) $2 + 2\sqrt{2}$

**Cevap:** C
**Çözüm:** $a = 1$, $b = -2$, $c = -1$. $\Delta = 4 + 4 = 8$, $\sqrt{8} = 2\sqrt{2}$. $x = \dfrac{2 \pm 2\sqrt{2}}{2} = 1 \pm \sqrt{2}$. Büyük kök $1 + \sqrt{2}$. $2a$'ya bölmeyi unutan $2 + 2\sqrt{2}$, $-b$ yerine $b$ yazan $-1 + \sqrt{2}$ bulur.

## Orta

### Soru 4 · Orta
$x^2 + (m - 1)x + 4 = 0$ denkleminin eşit iki kökü olduğuna göre $m$'nin alabileceği değerlerin toplamı kaçtır?

A) $2$
B) $3$
C) $5$
D) $8$
E) $15$

**Cevap:** A
**Çözüm:** $\Delta = (m - 1)^2 - 4 \cdot 1 \cdot 4 = 0$, yani $(m - 1)^2 = 16$. Buradan $m - 1 = 4$ ya da $m - 1 = -4$; $m = 5$ ya da $m = -3$. Toplam $5 + (-3) = 2$. Yalnızca pozitif karekökü alan $5$, $-3$'ün işaretini kaybeden $8$ bulur.

### Soru 5 · Orta
$x^2 - 4x + 2k - 6 = 0$ denkleminin gerçek kökü olmadığına göre $k$'nin alabileceği en küçük tam sayı değeri kaçtır?

A) $3$
B) $4$
C) $5$
D) $6$
E) $7$

**Cevap:** D
**Çözüm:** $\Delta = 16 - 4(2k - 6) = 16 - 8k + 24 = 40 - 8k$. Gerçek kök yoksa $40 - 8k < 0$, $k > 5$. En küçük tam sayı $6$. $k = 5$ için $\Delta = 0$ olur ve denklemin çakışık kökü vardır; $5$ cevap olamaz. $\Delta > 0$ kurup en büyük değeri arayan $4$ bulur.

### Soru 6 · Orta
$(m - 3)x^2 + 4x + 1 = 0$ denkleminin birbirinden farklı iki gerçek kökü olduğuna göre $m$ kaç farklı pozitif tam sayı değeri alabilir?

A) $4$
B) $5$
C) $6$
D) $7$
E) $8$

**Cevap:** B
**Çözüm:** $\Delta = 16 - 4(m - 3) \cdot 1 = 28 - 4m > 0$, $m < 7$. Ayrıca denklem ikinci dereceden olmalı: $m - 3 \ne 0$, $m \ne 3$ ($m = 3$ için $4x + 1 = 0$ olur, tek kök). Pozitif tam sayılar: $1, 2, 4, 5, 6$; toplam $5$. $m \ne 3$ koşulunu unutan $6$, ayrıca $m = 7$'yi de sayan $7$ bulur.

### Soru 7 · Orta
$a$, $b$, $c$ gerçek sayılar, $a > 0$ ve $c < 0$ olmak üzere

$$ax^2 + bx + c = 0$$

denklemi için aşağıdakilerden hangisi kesinlikle doğrudur?

A) Birbirinden farklı iki gerçek kökü vardır.
B) Eşit iki gerçek kökü vardır.
C) Gerçek kökü yoktur.
D) Köklerinden biri $0$'dır.
E) Gerçek kökünün olup olmadığı $b$'ye bağlıdır.

**Cevap:** A
**Çözüm:** $a > 0$ ve $c < 0$ ise $a \cdot c < 0$, yani $-4ac > 0$. $b^2 \ge 0$ olduğundan $\Delta = b^2 - 4ac > 0$; $b$ ne olursa olsun iki farklı gerçek kök vardır. Bu yüzden B, C ve E yanlıştır. $c \ne 0$ olduğu için $x = 0$ denklemi sağlamaz; D de yanlıştır.

## ÖSYM tarzı

### Soru 8 · ÖSYM tarzı
Yerden yukarı doğru atılan bir topun $t$ saniye sonraki yerden yüksekliği

$$h = 20t - 5t^2$$

metredir. Top, en yüksek noktası dışındaki her yüksekliğe biri çıkarken biri inerken olmak üzere iki farklı anda ulaşır; en yüksek noktaya ise yalnızca bir anda ulaşır.

Buna göre topun çıkabildiği en yüksek nokta yerden kaç metredir?

A) $15$
B) $20$
C) $25$
D) $40$
E) $80$

**Cevap:** B
**Çözüm:** Top $H$ yüksekliğine $20t - 5t^2 = H$ olan anlarda ulaşır: $5t^2 - 20t + H = 0$. En yüksek noktaya tek bir anda ulaşıldığına göre bu denklemin çakışık kökü vardır: $\Delta = 400 - 4 \cdot 5 \cdot H = 400 - 20H = 0$, $H = 20$. Kontrol: $5t^2 - 20t + 20 = 5(t - 2)^2$, top 2. saniyede 20 metrededir. $15$, $t = 1$ anındaki yüksekliktir. $\Delta$'yı $400 - 10H$ diye kuran $40$ bulur.

### Soru 9 · ÖSYM tarzı
Bir oyunda zar atılır ve gelen sayı $b$ olmak üzere

$$x^2 - bx + 2b - 3 = 0$$

denklemi yazılır. Bu denklemin çözüm kümesi tek elemanlı olursa oyuncu puan kazanır.

Buna göre oyuncuya puan kazandıran zar sayılarının toplamı kaçtır?

A) $1$
B) $2$
C) $6$
D) $8$
E) $12$

**Cevap:** D
**Çözüm:** Çözüm kümesi tek elemanlıysa $\Delta = 0$ olmalıdır. $\Delta = b^2 - 4(2b - 3) = b^2 - 8b + 12 = (b - 2)(b - 6)$. $\Delta = 0$ için $b = 2$ ya da $b = 6$; ikisi de zarda gelebilir. Toplam $8$. Kontrol: $b = 2$ için $(x - 1)^2 = 0$, $b = 6$ için $(x - 3)^2 = 0$. $b = 1$ için $\Delta = 5$ (iki kök), $b = 3, 4, 5$ için $\Delta < 0$ (kök yok); $3 + 4 + 5 = 12$ kök olmayan durumların toplamıdır.

### Soru 10 · ÖSYM tarzı
Çevresi 20 metre olan dikdörtgen biçiminde bir bahçe yapılacaktır. Bahçenin bir kenarı $x$ metre olduğuna göre alanı $x(10 - x)$ metrekaredir.

Buna göre bahçenin alanı aşağıdakilerden hangisi **olamaz**?

A) $9$
B) $16$
C) $21$
D) $24$
E) $26$

**Cevap:** E
**Çözüm:** Alan $S$ olsun: $x(10 - x) = S$, yani $x^2 - 10x + S = 0$. Böyle bir $x$ ancak $\Delta = 100 - 4S \ge 0$ ise vardır: $S \le 25$. $26 > 25$ olduğundan bu alan olamaz ($\Delta = -4$). Diğerleri olabilir: $9$ için kenarlar $1$ ve $9$, $16$ için $2$ ve $8$, $21$ için $3$ ve $7$, $24$ için $4$ ve $6$.

### Soru 11 · ÖSYM tarzı
$m$ bir tam sayı olmak üzere

- $x^2 - 2x + m = 0$ denkleminin gerçek kökü yoktur,
- $x^2 + 4x + m - 1 = 0$ denkleminin birbirinden farklı iki gerçek kökü vardır.

Buna göre $m$ kaç farklı değer alabilir?

A) $1$
B) $2$
C) $3$
D) $4$
E) $5$

**Cevap:** C
**Çözüm:** Birinci denklem: $\Delta = 4 - 4m < 0$, $m > 1$. İkinci denklem: $\Delta = 16 - 4(m - 1) = 20 - 4m > 0$, $m < 5$. İki koşul birlikte: $1 < m < 5$, tam sayılar $2, 3, 4$; toplam $3$. Uçları da dahil eden ($1 \le m \le 5$) $5$, yalnız bir ucu dahil eden $4$ bulur.

### Soru 12 · ÖSYM tarzı
$a$, $b$, $c$ sıfırdan farklı gerçek sayılar olmak üzere $ax^2 + bx + c = 0$ denkleminin gerçek kökü yoktur.

Buna göre

I. $cx^2 + bx + a = 0$ denkleminin gerçek kökü yoktur.
II. $a$ ile $c$ aynı işaretlidir.
III. $ax^2 + bx - c = 0$ denkleminin birbirinden farklı iki gerçek kökü vardır.

ifadelerinden hangileri doğrudur?

A) Yalnız I
B) Yalnız II
C) I ve II
D) II ve III
E) I, II ve III

**Cevap:** E
**Çözüm:** Verilen: $\Delta = b^2 - 4ac < 0$. I: $a$ ile $c$'nin yeri değişince diskriminant $b^2 - 4ca$ olur, yani aynıdır; gerçek kök yoktur, doğru. II: $4ac > b^2 \ge 0$ olduğundan $ac > 0$; $a$ ile $c$ aynı işaretlidir, doğru. III: Bu denklemde $\Delta = b^2 - 4a(-c) = b^2 + 4ac$; $ac > 0$ olduğu için pozitiftir, doğru. Üçü de doğrudur.
