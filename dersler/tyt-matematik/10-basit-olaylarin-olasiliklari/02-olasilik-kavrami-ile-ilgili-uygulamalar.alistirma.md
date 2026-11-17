---
baslik: Olasılık Kavramı İle İlgili Uygulamalar · Alıştırma
ders: tyt-matematik
soru: 12
guncelleme: 2026-11-17
---
# Alıştırma: Olasılık Kavramı İle İlgili Uygulamalar

Sorular özgündür ve ÖSYM soru tarzında yazılmıştır. Derse bakmadan çöz.

## Isınma

### Soru 1 · Kolay
Bir torbada 4 kırmızı, 5 mavi ve 3 yeşil bilye vardır. Torbadan rastgele bir bilye çekiliyor.

Çekilen bilyenin mavi **olmama** olasılığı kaçtır?

A) $\dfrac{1}{4}$
B) $\dfrac{5}{12}$
C) $\dfrac{1}{2}$
D) $\dfrac{7}{12}$
E) $\dfrac{3}{4}$

**Cevap:** D
**Çözüm:** Toplam $4 + 5 + 3 = 12$ bilye. Mavi olmayan: $4 + 3 = 7$. $P = \dfrac{7}{12}$. Tümleyenle de bulunur: $1 - \dfrac{5}{12} = \dfrac{7}{12}$. $\dfrac{5}{12}$ mavi olma olasılığıdır; $\dfrac{1}{4} = \dfrac{3}{12}$ yalnızca yeşili, $\dfrac{3}{4} = \dfrac{9}{12}$ kırmızı ile maviyi saymaktır.

### Soru 2 · Kolay
Bir madenî para 3 kez atılıyor.

İki kez yazı, bir kez tura gelme olasılığı kaçtır?

A) $\dfrac{1}{8}$
B) $\dfrac{1}{4}$
C) $\dfrac{3}{8}$
D) $\dfrac{1}{2}$
E) $\dfrac{2}{3}$

**Cevap:** C
**Çözüm:** $s(E) = 2^3 = 8$. İki yazı bir tura: $YYT, YTY, TYY$, yani 3 çıktı. $P = \dfrac{3}{8}$. Yalnızca $YYT$ sırasını sayan $\dfrac{1}{8}$ bulur. Yazı sayısı 0, 1, 2, 3 olabilir diye $\dfrac{1}{4}$ demek, bu dört sonucu eş olası saymaktır; öyle değildir. $\dfrac{1}{2}$ "en az iki yazı" olasılığıdır.

### Soru 3 · Kolay
Bir A olayı için $P(A') = 3 \cdot P(A)$ olduğu biliniyor.

Buna göre $P(A)$ kaçtır?

A) $\dfrac{1}{6}$
B) $\dfrac{1}{4}$
C) $\dfrac{1}{3}$
D) $\dfrac{3}{4}$
E) $1$

**Cevap:** B
**Çözüm:** $P(A) + P(A') = 1$ olduğundan $P(A) + 3P(A) = 1$, $\;4P(A) = 1$, $\;P(A) = \dfrac{1}{4}$. $\dfrac{3}{4}$, $P(A')$'nün değeridir. $\dfrac{1}{3}$, "3 katı" bilgisini doğrudan oran sanmaktan gelir.

## Orta

### Soru 4 · Orta
İki zar birlikte atılıyor.

Üst yüzlerdeki sayıların çarpımının çift sayı olma olasılığı kaçtır?

A) $\dfrac{1}{4}$
B) $\dfrac{1}{3}$
C) $\dfrac{1}{2}$
D) $\dfrac{2}{3}$
E) $\dfrac{3}{4}$

**Cevap:** E
**Çözüm:** Çarpım ancak iki sayı da tekse tek olur. Tümleyen: iki zar da tek, $3 \cdot 3 = 9$ çıktı, olasılığı $\dfrac{9}{36} = \dfrac{1}{4}$. İstenen: $1 - \dfrac{1}{4} = \dfrac{3}{4}$. $\dfrac{1}{4}$ çarpımın tek olma olasılığıdır. "Tek ya da çift, yarı yarıya" diyen $\dfrac{1}{2}$ bulur; $\dfrac{1}{2}$ aynı zamanda yalnızca bir zarın çift gelme olasılığıdır ($\dfrac{18}{36}$), iki zarın da çift geldiği durumlar unutulmuştur.

### Soru 5 · Orta
1'den 50'ye kadar numaralanmış 50 karttan biri rastgele çekiliyor.

Çekilen kartın numarasının 3'e veya 4'e bölünme olasılığı kaçtır?

A) $\dfrac{8}{25}$
B) $\dfrac{2}{5}$
C) $\dfrac{11}{25}$
D) $\dfrac{12}{25}$
E) $\dfrac{14}{25}$

**Cevap:** D
**Çözüm:** 3'e bölünen: 3, 6, …, 48, yani 16 kart. 4'e bölünen: 4, 8, …, 48, yani 12 kart. İkisine birden, yani 12'ye bölünen: 12, 24, 36, 48, yani 4 kart. $s(A \cup B) = 16 + 12 - 4 = 24$; $P = \dfrac{24}{50} = \dfrac{12}{25}$. Ortak kartları çıkarmayan $\dfrac{28}{50} = \dfrac{14}{25}$, iki kez çıkaran $\dfrac{20}{50} = \dfrac{2}{5}$, yalnızca 3'e bölünenleri sayan $\dfrac{16}{50} = \dfrac{8}{25}$ bulur.

### Soru 6 · Orta
Bir torbada yalnızca kırmızı ve beyaz bilyeler vardır. Torbadan rastgele çekilen bir bilyenin kırmızı olma olasılığı $\dfrac{2}{5}$'tir. Torbaya 6 beyaz bilye eklendiğinde kırmızı bilye çekme olasılığı $\dfrac{1}{4}$ oluyor.

Buna göre torbada kaç kırmızı bilye vardır?

A) 4
B) 6
C) 8
D) 10
E) 16

**Cevap:** A
**Çözüm:** Başlangıçta toplam $5k$ olsun; kırmızı $2k$. Ekleme sonrası $\dfrac{2k}{5k + 6} = \dfrac{1}{4}$, $\;8k = 5k + 6$, $\;k = 2$. Kırmızı $2 \cdot 2 = 4$, başlangıç toplamı 10, yeni toplam 16. Kontrol: $\dfrac{4}{16} = \dfrac{1}{4}$. 10 ve 16 toplamlardır; 6 eklenen beyaz sayısıdır.

### Soru 7 · Orta
A ve B aynı örnek uzayda tanımlı **ayrık** iki olaydır. $P(A) = \dfrac{1}{3}$ ve $P(B') = \dfrac{3}{4}$'tür.

Buna göre $P(A \cup B)$ kaçtır?

A) $\dfrac{1}{12}$
B) $\dfrac{1}{4}$
C) $\dfrac{5}{12}$
D) $\dfrac{7}{12}$
E) $\dfrac{11}{12}$

**Cevap:** D
**Çözüm:** $P(B) = 1 - \dfrac{3}{4} = \dfrac{1}{4}$. Ayrık olaylarda $P(A \cup B) = P(A) + P(B) = \dfrac{1}{3} + \dfrac{1}{4} = \dfrac{7}{12}$. $\dfrac{1}{12}$, olasılıkları çarpmaktır; $\dfrac{5}{12} = \dfrac{3}{4} - \dfrac{1}{3}$ ise $P(B')$'yü $P(B)$ sanıp çıkarmaktır. $P(B')$'yü doğrudan eklemek 1'den büyük sonuç verir, bu da hatayı gösterir.

## ÖSYM tarzı

### Soru 8 · ÖSYM tarzı
Bir okulda öğrencilere hangi takımlarda oynadıkları sorulmuştur. Öğrencilerin %60'ı basketbol, %45'i voleybol takımında oynamaktadır; %20'si ise bu iki takımın **hiçbirinde** oynamamaktadır.

Bu okuldan rastgele seçilen bir öğrencinin her iki takımda da oynuyor olma olasılığı kaçtır?

A) $\dfrac{1}{20}$
B) $\dfrac{1}{5}$
C) $\dfrac{1}{4}$
D) $\dfrac{2}{5}$
E) $\dfrac{9}{20}$

**Cevap:** C
**Çözüm:** En az bir takımda oynayanlar: $1 - 0{,}20 = 0{,}80$. Birleşim kuralı: $0{,}80 = 0{,}60 + 0{,}45 - P(A \cap B)$, buradan $P(A \cap B) = 0{,}25 = \dfrac{1}{4}$. "Hiçbiri" bilgisini kullanmadan $0{,}60 + 0{,}45 - 1 = 0{,}05$ hesaplayan $\dfrac{1}{20}$ bulur; $\dfrac{1}{5}$ hiçbirinde oynamayanların oranıdır.

### Soru 9 · ÖSYM tarzı
Aşağıdaki çark 12 eş dilime ayrılmıştır. Dilimler 1'den 12'ye kadar numaralanmış ve kırmızı, mavi ya da sarıya boyanmıştır. Çark çevrildiğinde ok, dilimlerden birini eşit şansla gösterir.

![12 eş dilimli çark. Kırmızı dilimler 1, 4, 6, 9, 11; mavi dilimler 2, 5, 7, 12; sarı dilimler 3, 8, 10. Tepede aşağıyı gösteren bir ok var.](gorsel/tyt-matematik/10-02-soru9-cark.svg "Her dilimin hem rengine hem numarasına bak.")

Çark bir kez çevrildiğinde okun gösterdiği dilimin **ne kırmızı ne de çift numaralı** olma olasılığı kaçtır?

A) $\dfrac{1}{4}$
B) $\dfrac{1}{3}$
C) $\dfrac{5}{12}$
D) $\dfrac{1}{2}$
E) $\dfrac{7}{12}$

**Cevap:** A
**Çözüm:** Önce "kırmızı veya çift" olanları say. Kırmızı: 1, 4, 6, 9, 11 (5 dilim). Çift: 2, 4, 6, 8, 10, 12 (6 dilim). İkisi birden: 4, 6 (2 dilim). Kırmızı veya çift: $5 + 6 - 2 = 9$ dilim. İstenen bunun tümleyenidir: $12 - 9 = 3$ dilim (3, 5, 7). $P = \dfrac{3}{12} = \dfrac{1}{4}$. Kesişimi iki kez çıkaran $12 - 7 = 5$ dilimle $\dfrac{5}{12}$ bulur; $\dfrac{1}{2}$ yalnızca tek numaralı dilimlerin olasılığıdır, $\dfrac{1}{3}$ ise mavi dilimlerin olasılığıdır.

### Soru 10 · ÖSYM tarzı
Bir kilit, 1, 2, 3 ve 4 rakamlarının her birinin bir kez kullanıldığı dört basamaklı bir şifreyle açılmaktadır. Şifreyi unutan Ece, bu koşula uyan şifrelerden birini rastgele deniyor.

Ece'nin denediği şifrenin 4'e tam bölünen bir sayı olma olasılığı kaçtır?

A) $\dfrac{1}{6}$
B) $\dfrac{1}{4}$
C) $\dfrac{1}{3}$
D) $\dfrac{3}{8}$
E) $\dfrac{1}{2}$

**Cevap:** B
**Çözüm:** Bütün şifreler: $4! = 24$. Bir sayı, son iki basamağının oluşturduğu sayı 4'e bölünüyorsa 4'e bölünür. Bu rakamlarla son iki basamak 12, 24 ya da 32 olabilir. Her birinde kalan iki rakam ilk iki basamağa $2! = 2$ biçimde yerleşir: $3 \cdot 2 = 6$ şifre. $P = \dfrac{6}{24} = \dfrac{1}{4}$. $\dfrac{1}{2}$, çift sayı olma olasılığıdır (son basamak 2 ya da 4); 4'e bölünme için yalnızca son basamağa bakmak yetmez.

### Soru 11 · ÖSYM tarzı
Bir kutuda kırmızı, mavi ve yeşil kalemler vardır. Kutudan rastgele çekilen bir kalemin

- kırmızı olma olasılığı $\dfrac{1}{3}$,
- mavi olma olasılığı, yeşil olma olasılığının 2 katıdır.

Kutudaki yeşil kalem sayısı 4'ten büyük ve 10'dan küçük olduğuna göre kutuda **en az** kaç kalem vardır?

A) 9
B) 18
C) 27
D) 36
E) 45

**Cevap:** C
**Çözüm:** Toplam $n$ olsun. Kırmızı $\dfrac{n}{3}$, mavi ve yeşil birlikte $\dfrac{2n}{3}$. Mavi $= 2 \cdot$ yeşil olduğundan yeşil $= \dfrac{1}{3} \cdot \dfrac{2n}{3} = \dfrac{2n}{9}$. Bu yüzden $n$, 9'un katıdır. $n = 9$: yeşil 2; $n = 18$: yeşil 4 (4'ten büyük değil); $n = 27$: yeşil 6, koşul sağlanır. Kontrol: kırmızı 9, mavi 12, yeşil 6, toplam 27. "4'ten büyük" koşulunu "en az 4" okuyan 18 bulur; 36 da koşulu sağlar ama en küçük değildir.

### Soru 12 · ÖSYM tarzı
Bir öğrenci, her sorusunda "Doğru" ya da "Yanlış" seçeneklerinden birinin işaretlendiği 4 soruluk bir testi soruları okumadan, her soruda iki seçenekten birini rastgele işaretleyerek dolduruyor. Her sorunun tek bir doğru cevabı vardır.

Öğrencinin en az bir soruyu yanlış cevaplamış olma olasılığı kaçtır?

A) $\dfrac{1}{16}$
B) $\dfrac{1}{4}$
C) $\dfrac{1}{2}$
D) $\dfrac{3}{4}$
E) $\dfrac{15}{16}$

**Cevap:** E
**Çözüm:** Her soru için 2 seçenek: $s(E) = 2^4 = 16$ eş olası cevap dizisi. "En az bir yanlış"ın tümleyeni "hiç yanlış yok", yani hepsinin doğru olmasıdır; bu tek bir dizidir: $\dfrac{1}{16}$. İstenen: $1 - \dfrac{1}{16} = \dfrac{15}{16}$. $\dfrac{1}{16}$ tümleyenin kendisidir; $\dfrac{1}{2}$ ise tek bir sorunun yanlış olma olasılığıdır.
