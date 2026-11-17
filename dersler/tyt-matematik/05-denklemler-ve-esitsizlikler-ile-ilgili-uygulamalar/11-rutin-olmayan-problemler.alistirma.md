---
baslik: Rutin Olmayan Problemler · Alıştırma
ders: tyt-matematik
soru: 12
guncelleme: 2026-11-17
---
# Alıştırma: Rutin Olmayan Problemler

Sorular özgündür ve ÖSYM soru tarzında yazılmıştır. Derse bakmadan çöz.

## Isınma

### Soru 1 · Kolay
Bir fırında poğaçalar yalnızca 4'lü ve 6'lı kutularla satılıyor. Tam 38 poğaça alan biri en az kaç kutu almıştır?

A) 6
B) 7
C) 8
D) 9
E) 10

**Cevap:** B
**Çözüm:** 4'lü kutu $a$, 6'lı kutu $b$ tane: $4a + 6b = 38$, yani $2a + 3b = 19$. Kutu sayısını azaltmak için $b$ büyük olmalı. $b = 6$ için $2a = 1$ (olmaz), $b = 5$ için $2a = 4$, $a = 2$. Toplam $2 + 5 = 7$ kutu. Kontrol: $8 + 30 = 38$. 9 en çok kutu sayısıdır ($a = 8$, $b = 1$); 6, $38 \div 6$'yı yuvarlayıp tam sayı koşulunu atlamaktır.

### Soru 2 · Kolay
300 metrelik düz bir koşu yolunun bir kenarına, başlangıç ve bitiş noktaları dahil, 15 metre arayla bayrak dikiliyor.

Kaç bayrak dikilir?

A) 19
B) 20
C) 21
D) 22
E) 30

**Cevap:** C
**Çözüm:** Aralık sayısı $300 \div 15 = 20$. Uçların ikisinde de bayrak olduğu için bayrak sayısı aralık sayısından 1 fazladır: $20 + 1 = 21$. 20, ilk bayrağı unutmak (çit direği hatası); 19 iki ucu da dışarıda bırakmaktır.

### Soru 3 · Kolay
Bir öğrenci bir kitabın ilk gün yarısını, ikinci gün kalan sayfaların $\frac{1}{3}$'ünü okuyor. Geriye 40 sayfa kalıyor.

Kitap kaç sayfadır?

A) 60
B) 80
C) 100
D) 120
E) 240

**Cevap:** D
**Çözüm:** Geriye doğru çalış. İkinci gün kalanın $\frac{1}{3}$'ü okununca $\frac{2}{3}$'ü kalır: $\frac{2}{3} \cdot K = 40$, $K = 60$ (birinci günden sonra kalan). Bu, kitabın yarısıdır: $60 \cdot 2 = 120$. Kontrol: $120 \to 60 \to 60 - 20 = 40$. 60'ta durmak birinci günü unutmaktır; 240, $40 \cdot 3 \cdot 2$ yapıp $\frac{1}{3}$'ü kalan sanmaktır.

## Orta

### Soru 4 · Orta
Bir sinyal lambası saat 08.00.00'da ilk kez yanıyor ve sonra her 40 saniyede bir yanıyor.

08.00 ile 09.00 arasında (iki an da dahil) lamba kaç kez tam dakika başında yanar?

A) 15
B) 16
C) 29
D) 30
E) 31

**Cevap:** E
**Çözüm:** Yanışlar 0, 40, 80, 120, … saniyede. Tam dakika başı 60'ın katıdır. İkisinin ortak katları $\text{EKOK}(40, 60) = 120$ saniyede, yani 2 dakikada bir gelir: 08.00, 08.02, …, 09.00. Sayı: $60 \div 2 + 1 = 31$. 30, 08.00'daki ilk yanışı saymamaktır.

### Soru 5 · Orta
Kibritlerle aşağıdaki gibi yan yana evler yapılıyor.

![Kibritten evler. 1. şekilde bir kare ve üstünde üçgen çatı, 2. şekilde yan yana iki ev ortak duvarlı, 3. şekilde yan yana üç ev.](gorsel/tyt-matematik/05-11-soru5.svg "Yan yana gelen evler aradaki duvarı ortak kullanıyor.")

Bu örüntüyle yan yana 12 ev yapmak için kaç kibrit gerekir?

A) 56
B) 60
C) 61
D) 66
E) 72

**Cevap:** C
**Çözüm:** İlk ev: 4 kenar + 2 çatı = 6 kibrit. Her yeni ev sol duvarı ortak kullandığı için 1 taban, 1 tavan, 1 sağ duvar ve 2 çatı ekler: 5 kibrit. $6 + 5 \cdot 11 = 61$. Genel kural $5n + 1$. 72, her evi 6 kibritle ayrı saymaktır; 60, ilk evin fazladan duvarını unutmaktır.

### Soru 6 · Orta
Bir kişinin cüzdanında yeterince 1 TL'lik, 5 TL'lik ve 10 TL'lik para vardır.

Bu kişi 20 TL'lik bir ödemeyi kaç farklı şekilde yapabilir? (Yalnızca her türden kaç tane kullanıldığı önemlidir.)

A) 5
B) 6
C) 8
D) 9
E) 10

**Cevap:** D
**Çözüm:** Sistematik say: önce 10 TL'liklerin sayısını sabitle.
- İki tane 10 TL: kalan 0, 1 yol.
- Bir tane 10 TL: kalan 10 TL, 5 TL'lik sayısı 0, 1 ya da 2 (gerisi 1 TL): 3 yol.
- Hiç 10 TL yok: 5 TL'lik sayısı 0, 1, 2, 3 ya da 4: 5 yol.

Toplam $1 + 3 + 5 = 9$. 8, "hiç 5 TL kullanmama" gibi bir durumu atlamaktır; düzenli tablo kurmazsan bir satır kolayca kaybolur.

### Soru 7 · Orta
Bir otoparkta yalnızca otomobiller (4 tekerlekli) ve motosikletler (2 tekerlekli) vardır. Otoparkta her türden en az bir araç bulunuyor ve toplam tekerlek sayısı 50'dir.

Otoparktaki toplam araç sayısı kaç farklı değer alabilir?

A) 11
B) 12
C) 13
D) 24
E) 25

**Cevap:** B
**Çözüm:** Otomobil $a$, motosiklet $b$: $4a + 2b = 50$, yani $b = 25 - 2a$. Araç sayısı $a + b = 25 - a$. $a \ge 1$ ve $b \ge 1$ için $a = 1, 2, \dots, 12$ olur ($a = 12$ iken $b = 1$). Her $a$ farklı bir araç sayısı verir (24'ten 13'e): 12 değer. 13, $a = 0$ durumunu da saymaktır; 24 ise en çok araç sayısıdır, sorulan değil.

## ÖSYM tarzı

### Soru 8 · ÖSYM tarzı
Bir binanın asansöründe yalnızca iki düğme vardır: biri asansörü 3 kat yukarı, diğeri 5 kat aşağı götürür. Bina zemin kat (0) ile 10. kat arasındadır ve asansör bu katların dışına çıkamaz.

Zemin kattan binen biri 2. kata en az kaç düğmeye basarak ulaşır?

A) 3
B) 4
C) 5
D) 6
E) 7

**Cevap:** D
**Çözüm:** $x$ kez yukarı, $y$ kez aşağı: $3x - 5y = 2$. $y = 0$ için $3x = 2$, $y = 1$ için $3x = 7$ olmaz; $y = 2$ için $3x = 12$, $x = 4$. En az $4 + 2 = 6$ basış. Bu sıra binada uygulanabilir: $0 \to 3 \to 6 \to 9 \to 4 \to 7 \to 2$. Daha az basışla $3x - 5y = 2$ sağlanmaz.

### Soru 9 · ÖSYM tarzı
Bir hasta, doktorunun önerisiyle ilacını 8 saatte bir içiyor. İlk dozu pazartesi saat 07.00'de içti.

Bu hasta 22. dozu hangi gün ve saatte içer?

A) Pazar 23.00
B) Pazartesi 07.00
C) Pazartesi 15.00
D) Pazartesi 23.00
E) Salı 07.00

**Cevap:** B
**Çözüm:** 1. dozdan 22. doza $22 - 1 = 21$ aralık vardır: $21 \cdot 8 = 168$ saat $= 7$ gün. Tam bir hafta sonra: pazartesi 07.00. $22 \cdot 8 = 176$ saat alan C'yi, 20 aralık sayan A'yı bulur.

### Soru 10 · ÖSYM tarzı
Ali, Burak, Cem, Deniz ve Emre bir koşu yarışını farklı sıralarda bitiriyor. Yarışla ilgili şunlar biliniyor:

- Cem, Ali'den hemen sonra geldi.
- Burak, Emre'den önce geldi.
- Emre, Ali'den önce geldi.
- Deniz ne birinci ne de sonuncu oldu.

Buna göre aşağıdakilerden hangisi kesinlikle doğrudur?

A) Ali dördüncü olmuştur.
B) Burak ikinci olmuştur.
C) Deniz ikinci olmuştur.
D) Emre üçüncü olmuştur.
E) Cem dördüncü olmuştur.

**Cevap:** A
**Çözüm:** Burak, Emre'den; Emre, Ali'den önce; Cem, Ali'nin hemen arkasında: Burak … Emre … Ali, Cem. Deniz sonuncu olamadığı için Cem beşinci, Ali dördüncüdür. Deniz birinci olamadığı için Burak birincidir. Geriye 2. ve 3. sıralar kalır; Deniz ile Emre bunları iki şekilde paylaşabilir (B, D, E, A, C ya da B, E, D, A, C). Bu yüzden C ve D kesin değildir; B ve E yanlıştır.

### Soru 11 · ÖSYM tarzı
Bir restoranda kare masalar şekildeki gibi yan yana birleştirilerek uzun bir masa oluşturuluyor. Her masanın açıkta kalan her kenarına bir kişi oturuyor.

![Kare masalar ve sandalyeler. 1 masada 4 sandalye, yan yana 2 masada 6 sandalye, yan yana 3 masada 8 sandalye var.](gorsel/tyt-matematik/05-11-soru11.svg "Masalar birleşince aradaki kenarlarda kimse oturamıyor.")

33 kişilik bir grubun tamamı bu şekilde tek bir uzun masaya oturacağına göre en az kaç masa birleştirilmelidir?

A) 8
B) 9
C) 14
D) 15
E) 16

**Cevap:** E
**Çözüm:** 1 masa 4, 2 masa 6, 3 masa 8 kişi: her yeni masa 2 kişi ekler, $n$ masa $2n + 2$ kişi alır. $2n + 2 \ge 33$, $n \ge 15{,}5$, en az 16 masa. 15 masa yalnızca 32 kişi alır; D aşağı yuvarlama hatasıdır. 9, her masaya ayrı ayrı 4 kişi oturtmaktır ($33 \div 4$).

### Soru 12 · ÖSYM tarzı
Bir bilgisayar oyununda her turun sonunda oyuncunun puanı önce 2 katına çıkıyor, sonra bu puandan 10 düşülüyor. Bir oyuncu 3 tur sonunda 50 puana ulaşıyor.

Bu oyuncunun başlangıç puanı kaçtır?

A) 15
B) 20
C) 25
D) 35
E) 40

**Cevap:** A
**Çözüm:** Geriye doğru: her turda önce $+10$, sonra $\div 2$ yapılır (ileri işlemlerin tersi, ters sırada). 3. tur: $(50 + 10) \div 2 = 30$. 2. tur: $(30 + 10) \div 2 = 20$. 1. tur: $(20 + 10) \div 2 = 15$. Kontrol: $15 \to 20 \to 30 \to 50$. 20'de durmak bir turu eksik saymaktır; 25, sırayı ters çevirmeden $50 \div 2$ yapmaktır.
