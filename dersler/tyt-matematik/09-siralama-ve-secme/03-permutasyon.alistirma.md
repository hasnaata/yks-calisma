---
baslik: Permütasyon · Alıştırma
ders: tyt-matematik
soru: 12
guncelleme: 2026-11-17
---
# Alıştırma: Permütasyon

Sorular özgündür ve ÖSYM soru tarzında yazılmıştır. Derse bakmadan çöz.

## Isınma

### Soru 1 · Kolay
$P(7, 2) + P(4, 4)$ işleminin sonucu kaçtır?

A) 25
B) 43
C) 45
D) 66
E) 2544

**Cevap:** D
**Çözüm:** $P(7, 2) = 7 \cdot 6 = 42$. $P(4, 4) = 4! = 24$. Toplam $42 + 24 = 66$. 43, $P(4, 4)$'ü 1 sanmaktır; 45, $P(7, 2)$ yerine sırasız seçim sayısı 21'i almaktır; 2544 ise $P(7, 2)$'yi $\frac{7!}{2!} = 2520$ sanmaktır.

### Soru 2 · Kolay
Bir yarışmaya 8 kişi katılmaktadır. Altın, gümüş ve bronz madalyalar birer kişiye verilecektir. Bir kişi en çok bir madalya alabildiğine göre madalyalar kaç farklı biçimde dağıtılabilir?

A) 24
B) 56
C) 336
D) 512
E) 6720

**Cevap:** C
**Çözüm:** Madalyalar farklı olduğu için sıra önemlidir: $P(8, 3) = 8 \cdot 7 \cdot 6 = 336$. 56, madalyaları aynı sanmaktır (sırasız seçim); 512 ($8^3$), bir kişinin birden fazla madalya alabileceğini sanmaktır; 6720 ise $\frac{8!}{3!}$ yazmaktır.

### Soru 3 · Kolay
$A = \{a, b, c, d, e\}$ kümesinin ikili permütasyonlarının sayısı kaçtır?

A) 10
B) 20
C) 25
D) 60
E) 120

**Cevap:** B
**Çözüm:** $P(5, 2) = 5 \cdot 4 = 20$. $(a, b)$ ile $(b, a)$ farklı sayılır. 10, bu ikisini aynı saymaktır; 25 ($5^2$), $(a, a)$ gibi tekrarlı ikilileri de saymaktır; 60, $\frac{5!}{2!}$ yazmaktır.

## Orta

### Soru 4 · Orta
$P(n, 3) = 8 \cdot P(n, 2)$ olduğuna göre $n$ kaçtır?

A) 6
B) 7
C) 8
D) 9
E) 10

**Cevap:** E
**Çözüm:** Açık yaz: $n(n-1)(n-2) = 8 \cdot n(n-1)$. Her iki taraftaki $n(n-1)$ sadeleşir: $n - 2 = 8$, $n = 10$. Kontrol: $P(10, 3) = 720$, $8 \cdot P(10, 2) = 8 \cdot 90 = 720$. 8, son çarpanı $n - 2$ yerine $n$ sanmaktır; 9, $n - 1 = 8$ yazmaktır; 6 ise $n + 2 = 8$ hatasıdır.

### Soru 5 · Orta
Biri sözlük olan birbirinden farklı 7 kitaptan 4'ü bir rafa yan yana dizilecektir. Sözlüğün **mutlaka** dizilen kitaplar arasında bulunduğu kaç farklı diziliş vardır?

A) 120
B) 360
C) 480
D) 720
E) 840

**Cevap:** C
**Çözüm:** Bütün dizilişler $P(7, 4) = 7 \cdot 6 \cdot 5 \cdot 4 = 840$. Sözlüğün bulunmadığı dizilişler $P(6, 4) = 6 \cdot 5 \cdot 4 \cdot 3 = 360$. Sözlüğün bulunduğu dizilişler $840 - 360 = 480$. Doğrudan: sözlük 4 yerden birine (4 yol), kalan 3 yere $P(6, 3) = 120$; $4 \cdot 120 = 480$. 120, sözlüğü yalnızca bir yere sabitlemektir; 360 bulunmayanların, 840 ise bütün dizilişlerin sayısıdır.

### Soru 6 · Orta
Aralarında Ece ile Can'ın da bulunduğu 6 kişi tek sırada oturacaktır. Ece ile Can sıranın iki ucunda oturmak koşuluyla kaç farklı oturma düzeni vardır?

A) 24
B) 48
C) 120
D) 240
E) 720

**Cevap:** B
**Çözüm:** Önce uçları doldur: Ece solda Can sağda ya da tersi, $2! = 2$ yol. Ortadaki 4 yere kalan 4 kişi: $4! = 24$. Toplam $2 \cdot 24 = 48$. 24, Ece ile Can'ın yer değiştirebileceğini unutmaktır; 240, "uçlarda" yerine "yan yana" hesabı yapmaktır ($5! \cdot 2!$).

### Soru 7 · Orta
3 kız ve 4 erkek öğrenci tek sıra hâlinde dizilecektir. Kızların üçü de yan yana olmak koşuluyla kaç farklı sıralama yapılabilir?

A) 120
B) 144
C) 576
D) 720
E) 4320

**Cevap:** D
**Çözüm:** 3 kızı bir blok yap. Blok + 4 erkek = 5 nesne: $5! = 120$. Blok içinde kızlar $3! = 6$ biçimde sıralanır. Toplam $120 \cdot 6 = 720$. 120, blok içini unutmaktır; 144 ($3! \cdot 4!$), bloğun erkekler arasında yer değiştirebileceğini unutmaktır; 576 ($4! \cdot 4!$), erkekleri blok yapmaktır; 4320 ise $7! - 720$, yani kızların yan yana olmadığı durumların sayısıdır.

## ÖSYM tarzı

### Soru 8 · ÖSYM tarzı
Bir otoparkta yan yana dizilmiş 5 boş park yeri vardır. Birbirinden farklı 3 araç bu yerlere, her araç bir yere olmak üzere park edecektir. Araçlar arasında **hiç boş yer kalmayacak** biçimde kaç farklı park düzeni oluşturulabilir?

A) 18
B) 24
C) 36
D) 60
E) 120

**Cevap:** A
**Çözüm:** Araçlar bitişik 3 yeri kaplar. Bitişik 3 yer şunlar olabilir: 1-2-3, 2-3-4, 3-4-5; yani 3 yol. Seçilen yerlere 3 araç $3! = 6$ biçimde dizilir. Toplam $3 \cdot 6 = 18$. 60 ($P(5, 3)$), bitişiklik koşulunu unutmaktır; 24, bitişik yer grubu sayısını 4 sanmaktır; 120 ise 5 yeri de dolu sanmaktır.

### Soru 9 · ÖSYM tarzı
10 kişinin katıldığı bir bilgi yarışmasında yalnızca ilk üç sıradaki kişiler açıklanacaktır. Beraberlik olmayan bu yarışmada Selin'in ilk üç arasında olduğu bilinmektedir.

Buna göre açıklanacak ilk üç sıralaması kaç farklı biçimde olabilir?

A) 72
B) 216
C) 504
D) 720
E) 1000

**Cevap:** B
**Çözüm:** Selin 1., 2. ya da 3. olabilir: 3 yol. Kalan iki sıraya diğer 9 kişiden sıralı seçim: $P(9, 2) = 9 \cdot 8 = 72$. Toplam $3 \cdot 72 = 216$. Tümleyenle: $P(10, 3) - P(9, 3) = 720 - 504 = 216$. 72, Selin'i yalnızca birinci saymaktır; 504 Selin'in bulunmadığı, 720 ise bütün sıralamaların sayısıdır.

### Soru 10 · ÖSYM tarzı
KALEM kelimesindeki harflerin her biri bir kez kullanılarak anlamlı ya da anlamsız 5 harfli kelimeler yazılıyor. Bu kelimelerden K harfiyle başlayıp M harfiyle **bitmeyen** kaç tane vardır?

A) 6
B) 12
C) 18
D) 24
E) 96

**Cevap:** C
**Çözüm:** K ile başlayanlar: K sabit, kalan 4 harf 4 yere, $4! = 24$. Bunlardan K ile başlayıp M ile bitenler: K ve M sabit, ortadaki 3 harf $3! = 6$. İstenen $24 - 6 = 18$. Doğrudan: son harf için A, L, E'den biri (3 yol), ortadaki 3 yer $3! = 6$; $3 \cdot 6 = 18$. 24, "M ile bitmeyen" koşulunu unutmaktır; 6, istenmeyen durumdur; 96 ise K ile başlamayanların sayısıdır ($120 - 24$).

### Soru 11 · ÖSYM tarzı
Bir pastanede birbirinden farklı 4 pasta ve birbirinden farklı 3 kurabiye vitrine tek sıra hâlinde dizilecektir. Pastaların hepsi yan yana, kurabiyelerin hepsi de yan yana olacaktır.

Buna göre vitrin kaç farklı biçimde düzenlenebilir?

A) 288
B) 576
C) 720
D) 1440
E) 5040

**Cevap:** A
**Çözüm:** Pastalar bir blok, kurabiyeler bir blok: 2 blok $2! = 2$ biçimde sıralanır (önce pastalar ya da önce kurabiyeler). Pasta bloğunun içi $4! = 24$, kurabiye bloğunun içi $3! = 6$. Toplam $2 \cdot 24 \cdot 6 = 288$. 576 ($4! \cdot 4!$), yalnızca pastaların yan yana olmasını hesaplamaktır; 720 ($5! \cdot 3!$), yalnızca kurabiyelerin yan yana olmasını hesaplamaktır; 5040 ($7!$) ise koşulsuz sıralamadır.

### Soru 12 · ÖSYM tarzı
Üzerinde 1'den 7'ye kadar rakamlar yazılı 7 kart vardır. Bu kartlardan 4 tanesi yan yana dizilerek dört basamaklı bir sayı oluşturuluyor.

Oluşturulabilecek sayıların kaçında 1 ve 2 rakamlarından **en az biri** bulunur?

A) 120
B) 360
C) 480
D) 600
E) 720

**Cevap:** E
**Çözüm:** Bütün sayılar $P(7, 4) = 7 \cdot 6 \cdot 5 \cdot 4 = 840$. 1 de 2 de bulunmayan sayılar, kalan 5 karttan: $P(5, 4) = 5 \cdot 4 \cdot 3 \cdot 2 = 120$. En az biri bulunanlar $840 - 120 = 720$. 120, hiçbirinin bulunmadığı sayıların sayısıdır; 360 ($P(6, 4)$), 1'in bulunmadığı sayılardır; 480 ($840 - 360$) yalnızca 1'in bulunduğu sayıları sayıp 2'yi unutmaktır.
