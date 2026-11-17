---
baslik: Olasılıkta Temel Kavramlar · Alıştırma
ders: tyt-matematik
soru: 12
guncelleme: 2026-11-17
---
# Alıştırma: Olasılıkta Temel Kavramlar

Sorular özgündür ve ÖSYM soru tarzında yazılmıştır. Derse bakmadan çöz.

## Isınma

### Soru 1 · Kolay
Üç madenî para birlikte havaya atılıyor.

Bu deneyin örnek uzayı kaç elemanlıdır?

A) 2
B) 3
C) 4
D) 6
E) 8

**Cevap:** E
**Çözüm:** Her paranın 2 çıktısı (Y, T) var. Çarpma kuralı: $2 \cdot 2 \cdot 2 = 2^3 = 8$. Para sayısını yazan 3, $2 \cdot 3$ hesaplayan 6 bulur.

### Soru 2 · Kolay
Bir zar atılıyor.

Aşağıdaki olaylardan hangisi **imkânsız** olaydır?

A) Tek sayı gelmesi
B) 6'dan küçük sayı gelmesi
C) İki basamaklı sayı gelmesi
D) Asal sayı gelmesi
E) 7'den küçük sayı gelmesi

**Cevap:** C
**Çözüm:** Zarın yüzleri 1, 2, 3, 4, 5, 6'dır; hiçbiri iki basamaklı değildir. Bu olay $\varnothing$, yani imkânsızdır. E seçeneği her çıktıda gerçekleşir: imkânsız değil, kesin olaydır. A, B ve D en az bir çıktıda gerçekleşir.

### Soru 3 · Kolay
1'den 10'a kadar numaralanmış 10 karttan biri rastgele çekiliyor. A, çekilen kartın numarasının asal sayı olması olayıdır.

Buna göre $A'$ olayı kaç elemanlıdır?

A) 3
B) 4
C) 5
D) 6
E) 7

**Cevap:** D
**Çözüm:** $s(E) = 10$. 10'a kadar asal sayılar $2, 3, 5, 7$: $s(A) = 4$. $s(A') = 10 - 4 = 6$. 1'i asal sayan $10 - 5 = 5$, 2'yi unutan $10 - 3 = 7$ bulur; 4 ise A'nın kendisidir.

## Orta

### Soru 4 · Orta
İki zar birlikte atılıyor.

Üst yüze gelen sayıların toplamının 8 olması olayı kaç elemanlıdır?

A) 3
B) 4
C) 5
D) 6
E) 8

**Cevap:** C
**Çözüm:** Toplamı 8 olan sıralı ikililer: $(2,6), (6,2), (3,5), (5,3), (4,4)$. Toplam 5 çıktı. $(2,6)$ ile $(6,2)$'yi tek sayan $\{2,6\}, \{3,5\}, \{4,4\}$ ile 3, $(4,4)$'ü iki kez sayan 6, $(4,4)$'ü unutan 4 bulur.

### Soru 5 · Orta
Bir zar atılıyor.

Aşağıdaki olay çiftlerinden hangisi **ayrık** olaylardır?

A) Asal gelmesi ile 4'ün katı gelmesi
B) Çift gelmesi ile asal gelmesi
C) Tek gelmesi ile 3'ün katı gelmesi
D) 4'ten büyük gelmesi ile asal gelmesi
E) Çift gelmesi ile 5'ten büyük gelmesi

**Cevap:** A
**Çözüm:** Kümeleri yaz. A: $\{2, 3, 5\} \cap \{4\} = \varnothing$, ayrık. B: $\{2, 4, 6\} \cap \{2, 3, 5\} = \{2\}$. C: $\{1, 3, 5\} \cap \{3, 6\} = \{3\}$. D: $\{5, 6\} \cap \{2, 3, 5\} = \{5\}$. E: $\{2, 4, 6\} \cap \{6\} = \{6\}$. Yalnızca A'da ortak çıktı yoktur.

### Soru 6 · Orta
Bir torbada 4 kırmızı ve 3 beyaz bilye vardır. Torbadan aynı anda 2 bilye çekiliyor.

Çekilen iki bilyenin aynı renkte olması olayının tümleyeni kaç elemanlıdır?

A) 9
B) 12
C) 15
D) 21
E) 24

**Cevap:** B
**Çözüm:** Aynı anda çekildiği için sıra önemsiz: $s(E) = C(7, 2) = 21$. Aynı renk: $C(4, 2) + C(3, 2) = 6 + 3 = 9$. Tümleyen (farklı renk): $21 - 9 = 12$. Kontrol: bir kırmızı ve bir beyaz, $4 \cdot 3 = 12$. Olayın kendisini veren 9, yalnız kırmızı çiftleri çıkaran $21 - 6 = 15$, sıralı sayan $4 \cdot 3 \cdot 2 = 24$ bulur.

### Soru 7 · Orta
Bir madenî para ve bir zar birlikte atılıyor. A, paranın tura **ve** zarın asal sayı gelmesi olayıdır.

Buna göre $A'$ olayı kaç elemanlıdır?

A) 3
B) 5
C) 6
D) 9
E) 12

**Cevap:** D
**Çözüm:** $s(E) = 2 \cdot 6 = 12$. $A = \{(T,2), (T,3), (T,5)\}$, $s(A) = 3$. $s(A') = 12 - 3 = 9$. Örnek uzayı $2 + 6 = 8$ sanan $8 - 3 = 5$ bulur; yalnızca paraya ya da yalnızca zara bakan 6 bulur; 3 ise A'nın kendisidir.

## ÖSYM tarzı

### Soru 8 · ÖSYM tarzı
Aşağıdaki çark 8 eş dilime ayrılmıştır. Her dilimde bir numara ve bir renk vardır. Çark çevrildiğinde ok bir dilimde durur.

![8 eş dilimli çark. Kırmızı dilimler 1, 3 ve 6; mavi dilimler 2, 5 ve 8; sarı dilimler 4 ve 7. Çarkın tepesinde aşağıyı gösteren bir ok var.](gorsel/tyt-matematik/10-01-soru8.svg "Her dilimin hem numarasına hem rengine bak. Kırmızı 1, 3, 6; mavi 2, 5, 8; sarı 4, 7.")

Bu deneyle ilgili aşağıdaki ifadelerden hangileri doğrudur?

I. Okun kırmızı dilimde durması ile çift numaralı dilimde durması ayrık olaylardır.
II. Okun sarı dilimde durması olayının tümleyeni 6 elemanlıdır.
III. Okun mavi dilimde durması ile 3'ün katı olan bir numarada durması ayrık olaylardır.

A) Yalnız I
B) Yalnız II
C) I ve III
D) II ve III
E) I, II ve III

**Cevap:** D
**Çözüm:** $E = \{1, 2, \dots, 8\}$. I: kırmızı $\{1, 3, 6\}$, çift $\{2, 4, 6, 8\}$; ortak çıktı 6, ayrık **değil**. Yanlış. II: sarı $\{4, 7\}$, tümleyeni $8 - 2 = 6$ elemanlı. Doğru. III: mavi $\{2, 5, 8\}$, 3'ün katı $\{3, 6\}$; ortak çıktı yok, ayrık. Doğru.

### Soru 9 · ÖSYM tarzı
Eren bir madenî parayı yazı gelene kadar atıyor; ancak parayı en fazla 4 kez atabiliyor. Yazı gelirse ya da 4 atış biterse durur.

Örneğin ilk iki atışta tura, üçüncüde yazı gelirse çıktı $TTY$ olur.

Buna göre bu deneyin örnek uzayı kaç elemanlıdır?

A) 4
B) 5
C) 8
D) 15
E) 16

**Cevap:** B
**Çözüm:** Yazı gelince deney biter, bu yüzden yazıdan sonra atış yoktur. Çıktılar: $Y$, $TY$, $TTY$, $TTTY$ ve 4 atışın hepsi tura $TTTT$. Toplam 5. Her zaman 4 atış yapıldığını sanan $2^4 = 16$, $TTTT$'yi unutan 4 bulur.

### Soru 10 · ÖSYM tarzı
1'den 9'a kadar numaralanmış 9 karttan aynı anda 2 kart çekiliyor.

Çekilen kartlardaki numaraların toplamının çift sayı olması olayı kaç elemanlıdır?

A) 6
B) 10
C) 16
D) 20
E) 36

**Cevap:** C
**Çözüm:** İki sayının toplamı çiftse ikisi de tek ya da ikisi de çifttir. Tek numaralar $1, 3, 5, 7, 9$ (5 tane), çift numaralar $2, 4, 6, 8$ (4 tane). İkisi tek: $C(5, 2) = 10$; ikisi çift: $C(4, 2) = 6$. Toplam $10 + 6 = 16$. Yalnız tekleri sayan 10, yalnız çiftleri sayan 6, tümleyeni (biri tek biri çift, $5 \cdot 4 = 20$) bulan 20, örnek uzayın tamamını ($C(9, 2) = 36$) yazan 36 bulur.

### Soru 11 · ÖSYM tarzı
Bir masa oyununda iki zar birlikte atılıyor. Üst yüzlerdeki sayıların çarpımı çift ise oyuncu bir hamle daha yapıyor.

Buna göre oyuncunun bir hamle daha yapmasını sağlayan çıktılardan oluşan olay kaç elemanlıdır?

A) 9
B) 12
C) 18
D) 24
E) 27

**Cevap:** E
**Çözüm:** Tümleyenle say. Çarpım tek olması için iki zarın da tek gelmesi gerekir: $3 \cdot 3 = 9$ çıktı. Çarpım çift: $36 - 9 = 27$. Tümleyeni cevap sanan 9, "yarısı çift" diye düşünen 18 bulur.

### Soru 12 · ÖSYM tarzı
Bir torbada 3 kırmızı ve 2 mavi bilye vardır. Torbadan aynı anda 3 bilye çekiliyor.

Buna göre aşağıdakilerden hangisi **kesin** olaydır?

A) En az bir kırmızı bilye çekilmesi
B) En az bir mavi bilye çekilmesi
C) En çok bir kırmızı bilye çekilmesi
D) Üç bilyenin de aynı renkte olması
E) En az iki mavi bilye çekilmesi

**Cevap:** A
**Çözüm:** Torbada yalnızca 2 mavi var; 3 bilye çekilince en az biri kırmızı olmak zorunda. A her çıktıda gerçekleşir, kesin olaydır. B: üçü de kırmızı ($KKK$) çekilebilir, kesin değil. C ve E: $KKM$ çekilebilir, ikisi de gerçekleşmez. D: $KKM$ çıktısında renkler farklıdır.
