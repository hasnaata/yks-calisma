---
baslik: Tekrarlı Permütasyon · Alıştırma
ders: tyt-matematik
soru: 12
guncelleme: 2026-11-17
---
# Alıştırma: Tekrarlı Permütasyon

Sorular özgündür ve ÖSYM soru tarzında yazılmıştır. Derse bakmadan çöz.

## Isınma

### Soru 1 · Kolay
SAAT kelimesinin harflerinin tamamı kullanılarak anlamlı ya da anlamsız 4 harfli kaç farklı kelime yazılabilir?

A) 4
B) 6
C) 12
D) 24
E) 48

**Cevap:** C
**Çözüm:** 4 harf; A 2 tane, S ve T birer tane. $\frac{4!}{2!} = \frac{24}{2} = 12$. $24$, A'ların özdeş olduğunu unutmaktır; $48$, $2!$'e bölmek yerine çarpmaktır; $6$, S ve T'yi de tekrarlı sayıp $\frac{4!}{2! \cdot 2!}$ almaktır.

### Soru 2 · Kolay
Özdeş 3 kırmızı ve özdeş 2 beyaz bilye bir sıraya yan yana kaç farklı şekilde dizilebilir?

A) 5
B) 10
C) 20
D) 60
E) 120

**Cevap:** B
**Çözüm:** 5 bilye; kırmızılar 3, beyazlar 2 tane: $\frac{5!}{3! \cdot 2!} = \frac{120}{12} = 10$. Yalnızca $3!$'e bölen $20$, yalnızca $2!$'e bölen $60$, hiç bölmeyen $120$ bulur.

### Soru 3 · Kolay
1, 1, 2, 2, 3 rakamlarının tamamı kullanılarak beş basamaklı kaç farklı sayı yazılabilir?

A) 30
B) 40
C) 60
D) 80
E) 120

**Cevap:** A
**Çözüm:** 0 olmadığı için başa gelme sorunu yok. 5 rakam; 1 iki tane, 2 iki tane: $\frac{5!}{2! \cdot 2!} = \frac{120}{4} = 30$. Yalnızca bir $2!$'e bölen $60$, hiç bölmeyen $120$ bulur.

## Orta

### Soru 4 · Orta
KELEBEK kelimesinin harflerinin tamamı kullanılarak yazılan anlamlı ya da anlamsız 7 harfli kelimelerden kaç tanesi K ile başlar ve K ile biter?

A) 5
B) 10
C) 20
D) 60
E) 120

**Cevap:** C
**Çözüm:** KELEBEK: K 2, E 3, L 1, B 1 tane. İki K başa ve sona sabitlenir. Ortadaki 5 yere E, L, E, B, E dizilir; E 3 tane: $\frac{5!}{3!} = \frac{120}{6} = 20$. $120$, E'lerin özdeş olduğunu unutmaktır; $60$, $3!$ yerine $2!$'e bölmektir.

### Soru 5 · Orta
0, 0, 3, 3, 3, 7 rakamlarının tamamı kullanılarak altı basamaklı kaç farklı sayı yazılabilir?

A) 20
B) 24
C) 30
D) 40
E) 60

**Cevap:** D
**Çözüm:** Önce 0 başa gelebilir gibi say: 6 rakam, 0 iki tane, 3 üç tane: $\frac{6!}{2! \cdot 3!} = \frac{720}{12} = 60$.
0 ile başlayanlar: başa 0 konur, kalan 0, 3, 3, 3, 7 rakamları $\frac{5!}{3!} = 20$ şekilde dizilir.
Altı basamaklı sayılar: $60 - 20 = 40$. $60$, 0 ile başlayanları çıkarmayı unutmaktır; $20$, çıkarılacak kısmı cevap sanmaktır.

### Soru 6 · Orta
Aşağıdaki şekil, kare biçimli bloklardan oluşan bir yol ağını göstermektedir.

![5 sütun 3 satırlık kare ızgara; sol alt köşe A, sağ üst köşe B. C noktası A'nın 2 birim sağında ve 1 birim yukarısında bir kavşak.](gorsel/tyt-matematik/09-04-soru6.svg "C noktasının A'ya ve B'ye göre kaç birim sağda, kaç birim yukarıda olduğunu say.")

Yalnızca sağa ve yukarı doğru ilerleyen biri, A noktasından B noktasına C noktasından geçmek koşuluyla kaç farklı yoldan gidebilir?

A) 13
B) 30
C) 35
D) 56
E) 60

**Cevap:** B
**Çözüm:** A'dan C'ye: 2 sağ, 1 yukarı: $\frac{3!}{2! \cdot 1!} = 3$.
C'den B'ye: 3 sağ, 2 yukarı: $\frac{5!}{3! \cdot 2!} = 10$.
İki aşama art arda yapıldığı için çarpılır: $3 \cdot 10 = 30$. $13$, iki aşamayı toplamaktır; $56$, C koşulunu yok sayıp A'dan B'ye tüm yolları ($\frac{8!}{5! \cdot 3!}$) saymaktır.

### Soru 7 · Orta
MANAV kelimesinin harflerinin tamamı kullanılarak yazılan anlamlı ya da anlamsız 5 harfli kelimelerden kaç tanesinde A harfleri yan yana **değildir**?

A) 12
B) 24
C) 36
D) 48
E) 60

**Cevap:** C
**Çözüm:** Tümü: 5 harf, A 2 tane: $\frac{5!}{2!} = 60$.
A'lar yan yana: [AA] bloğu, M, N, V; dört farklı nesne: $4! = 24$. Blok içindeki A'lar özdeş olduğu için $2!$ ile çarpılmaz.
Yan yana olmayanlar: $60 - 24 = 36$. $24$, yan yana olanları cevap sanmaktır; $48$, bloğu $2!$ ile çarpmaktır ($4! \cdot 2!$); $60$, koşulu yok saymaktır.

## ÖSYM tarzı

### Soru 8 · ÖSYM tarzı
Bir okul kulübü, birbirinden farklı 7 etkinliği art arda 7 güne, her güne bir etkinlik gelecek şekilde yerleştirecektir. Tanışma, atölye ve kapanış etkinlikleri bu sırayla yapılacaktır; bu üç etkinliğin arasında başka etkinlikler olabilir.

Buna göre etkinlikler kaç farklı şekilde yerleştirilebilir?

A) 35
B) 120
C) 210
D) 840
E) 5040

**Cevap:** D
**Çözüm:** Üç etkinliğin kendi arasındaki sırası sabit; hangi üç güne düşerlerse düşsünler bu günlere tek şekilde yerleşirler. Üçü özdeş gibi sayılır: $\frac{7!}{3!} = \frac{5040}{6} = 840$. $5040$, koşulu yok saymaktır; $120$, üç etkinliği yan yana bir blok sanmaktır ($5!$).

### Soru 9 · ÖSYM tarzı
Bir dolap kilidinin şifresi, yalnızca 1, 2 ve 3 rakamları kullanılarak oluşturulan 4 basamaklı bir sayıdır. Rakamlar tekrar edebilir ve hepsinin kullanılması gerekmez. Şifrenin rakamları toplamı 7'dir.

Buna göre bu koşullara uyan kaç farklı şifre vardır?

A) 4
B) 6
C) 12
D) 15
E) 16

**Cevap:** E
**Çözüm:** Önce toplamı 7 olan 4 rakamı bul (1, 2, 3'ten). En küçük toplam $1+1+1+1 = 4$; 3 fazlalık dağıtılır:
- $\{1, 1, 2, 3\}$: 1 iki tane, $\frac{4!}{2!} = 12$ şifre.
- $\{1, 2, 2, 2\}$: 2 üç tane, $\frac{4!}{3!} = 4$ şifre.

İki 3 kullanılamaz ($3 + 3 + 1 + 1 = 8$). Toplam $12 + 4 = 16$. Yalnızca bir durumu bulan $12$ ya da $4$ bulur.

### Soru 10 · ÖSYM tarzı
Bir kelime oyununda KAVAK kelimesinin harflerinden 3 tanesi seçilip yan yana dizilerek anlamlı ya da anlamsız 3 harfli kelimeler oluşturuluyor.

Buna göre en çok kaç farklı kelime oluşturulabilir?

A) 6
B) 9
C) 12
D) 15
E) 18

**Cevap:** E
**Çözüm:** Harfler K, K, A, A, V. Durumlara ayır:
- Üç harf de farklı (K, A, V): $3! = 6$.
- İki K ve A ya da V: 2 seçim, her biri $\frac{3!}{2!} = 3$ şekilde: $2 \cdot 3 = 6$.
- İki A ve K ya da V: aynı şekilde $6$.

Toplam $6 + 6 + 6 = 18$. Yalnızca farklı harfleri kullanan $6$, tekrarlı durumlardan birini unutan $12$ bulur.

### Soru 11 · ÖSYM tarzı
Bir kurye, sokakları şekildeki gibi kare biçimli olan bir mahallede A noktasından B noktasına yalnızca doğuya (sağa) ve kuzeye (yukarı) giderek ulaşacaktır. D kavşağı yol çalışması nedeniyle kapalıdır.

![4 sütun 3 satırlık kare ızgara; sol alt köşe A, sağ üst köşe B. A'nın 2 birim sağında ve 1 birim yukarısındaki D kavşağı kırmızı çarpıyla işaretli.](gorsel/tyt-matematik/09-04-soru11.svg "D kavşağından geçen yolların hepsi kapalıdır.")

Buna göre kurye kaç farklı yoldan gidebilir?

A) 17
B) 18
C) 20
D) 30
E) 35

**Cevap:** A
**Çözüm:** Tüm yollar: 4 sağ, 3 yukarı: $\frac{7!}{4! \cdot 3!} = 35$.
D'den geçenler: A'dan D'ye (2 sağ, 1 yukarı) $\frac{3!}{2!} = 3$; D'den B'ye (2 sağ, 2 yukarı) $\frac{4!}{2! \cdot 2!} = 6$; $3 \cdot 6 = 18$.
D'den geçmeyenler: $35 - 18 = 17$. $18$, D'den geçenleri cevap sanmaktır; $35$, kapalı kavşağı yok saymaktır.

### Soru 12 · ÖSYM tarzı
Bir gemide birbirinin aynısı 3 kırmızı, birbirinin aynısı 2 mavi ve 1 sarı bayrak, bir direğe alt alta asılarak işaret veriliyor. Her işarette 6 bayrağın tamamı kullanılıyor. Sarı bayrağın en üstte ya da en altta olduğu dizilişler kullanılmıyor.

Buna göre kaç farklı işaret verilebilir?

A) 10
B) 20
C) 30
D) 40
E) 50

**Cevap:** D
**Çözüm:** Tüm dizilişler: $\frac{6!}{3! \cdot 2! \cdot 1!} = \frac{720}{12} = 60$.
Sarı en üstte: kalan 3 kırmızı, 2 mavi $\frac{5!}{3! \cdot 2!} = 10$. Sarı en altta: aynı şekilde $10$.
Kullanılabilir işaretler: $60 - 10 - 10 = 40$. $50$, yalnızca bir ucu çıkarmaktır; $20$, çıkarılacak kısmı cevap sanmaktır.
