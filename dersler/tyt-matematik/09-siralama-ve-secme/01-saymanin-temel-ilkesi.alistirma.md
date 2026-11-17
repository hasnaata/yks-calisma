---
baslik: Saymanın Temel İlkesi · Alıştırma
ders: tyt-matematik
soru: 12
guncelleme: 2026-11-17
---
# Alıştırma: Saymanın Temel İlkesi

Sorular özgündür ve ÖSYM soru tarzında yazılmıştır. Derse bakmadan çöz.

## Isınma

### Soru 1 · Kolay
Bir okul yemekhanesinde 3 çeşit çorba, 4 çeşit ana yemek ve 2 çeşit tatlı vardır. Bir öğrenci bunlardan **yalnızca bir** tabak alacaktır. Öğrenci kaç farklı seçim yapabilir?

A) 9
B) 12
C) 14
D) 20
E) 24

**Cevap:** A
**Çözüm:** Öğrenci ya çorba (3 yol) ya ana yemek (4 yol) ya da tatlı (2 yol) alır. Durumlar aynı anda olmaz, toplanır: $3 + 4 + 2 = 9$. 24, her birinden birer tane alındığını sanıp çarpmaktır ($3 \cdot 4 \cdot 2$); 14 ise $3 \cdot 4 + 2$ işleminden gelir.

### Soru 2 · Kolay
A kentinden B kentine 3 farklı yol, B kentinden C kentine 4 farklı yol vardır. A kentinden B'ye uğrayarak C kentine kaç farklı biçimde gidilebilir?

A) 7
B) 12
C) 24
D) 64
E) 81

**Cevap:** B
**Çözüm:** Önce A'dan B'ye (3 yol) **ve** sonra B'den C'ye (4 yol) gidilir; art arda iki adım çarpılır: $3 \cdot 4 = 12$. 7, toplamaktır. 64 ($4^3$) ve 81 ($3^4$) üslü yazım karışıklığından gelir.

### Soru 3 · Kolay
8 kişilik bir kulüpten bir başkan ve bir başkan yardımcısı seçilecektir. Bir kişi iki göreve birden seçilemez. Bu seçim kaç farklı biçimde yapılabilir?

A) 15
B) 16
C) 28
D) 49
E) 56

**Cevap:** E
**Çözüm:** Başkan 8 kişiden biri (8 yol). Başkan yardımcısı kalan 7 kişiden biri (7 yol): $8 \cdot 7 = 56$. Görevler farklı olduğu için "Ayşe başkan, Mert yardımcı" ile "Mert başkan, Ayşe yardımcı" farklı seçimlerdir; 28, bu ikisini aynı saymaktır. 15 ise $8 + 7$'dir.

## Orta

### Soru 4 · Orta
Birbirinden farklı 4 oyuncak, 3 çocuğa dağıtılacaktır. Her oyuncak bir çocuğa verilecek; bir çocuk birden fazla oyuncak alabilir, hiç oyuncak almayan çocuk da olabilir. Bu dağıtım kaç farklı biçimde yapılabilir?

A) 12
B) 24
C) 64
D) 81
E) 256

**Cevap:** D
**Çözüm:** Seçim her **oyuncak** için yapılır: "bu oyuncak hangi çocuğa gidecek?" Her oyuncağın 3 seçeneği var ve 4 oyuncak var: $3 \cdot 3 \cdot 3 \cdot 3 = 3^4 = 81$. 64 ($4^3$), kutuları çocuklara açıp üssü ters yazmaktır. 12 ise $4 \cdot 3$'tür.

### Soru 5 · Orta
$\{0, 1, 2, 3, 4, 5, 6\}$ kümesinin rakamları kullanılarak rakamları birbirinden farklı dört basamaklı kaç doğal sayı yazılabilir?

A) 360
B) 720
C) 840
D) 2058
E) 2401

**Cevap:** B
**Çözüm:** Kümede 7 rakam var. Binler basamağı $0$ olamaz: 6 yol. Yüzler: kalan 6 rakam ($0$ artık olabilir). Onlar: 5, birler: 4. Toplam $6 \cdot 6 \cdot 5 \cdot 4 = 720$. 840, $0$ kısıtını unutmaktır ($7 \cdot 6 \cdot 5 \cdot 4$); 360, $0$'ı hiç kullanmamaktır ($6 \cdot 5 \cdot 4 \cdot 3$); 2058 ise rakamların tekrar edebileceğini sanmaktır ($6 \cdot 7^3$).

### Soru 6 · Orta
Üç yatay şeritten oluşan bir bayrak, 4 farklı renk kullanılarak boyanacaktır. Her şerit tek renge boyanır ve **bitişik** iki şerit aynı renkte olamaz. Bitişik olmayan şeritler aynı renkte olabilir. Kaç farklı bayrak elde edilebilir?

A) 24
B) 36
C) 48
D) 64
E) 81

**Cevap:** B
**Çözüm:** Üst şerit 4 renkten biri (4 yol). Orta şerit üsttekinden farklı: 3 yol. Alt şerit yalnızca ortadakinden farklı olmalı, üsttekiyle aynı olabilir: 3 yol. $4 \cdot 3 \cdot 3 = 36$. 24, üç şeridin de farklı olması gerektiğini sanmaktır ($4 \cdot 3 \cdot 2$); 64 ise kısıtı hiç kullanmamaktır ($4^3$).

### Soru 7 · Orta
Aşağıdaki şekilde A, B ve C kentleri arasındaki yollar gösterilmiştir: A ile B arasında 3, B ile C arasında 2 yol vardır; ayrıca A'dan C'ye B'ye uğramadan giden 4 yol vardır.

![A, B, C kentleri yan yana. A ile B arasında mavi 3 yol, B ile C arasında yeşil 2 yol, A ile C arasında alttan dolaşan sarı 4 yol.](gorsel/tyt-matematik/09-01-soru7.svg "Mavi: A ile B arası 3 yol. Yeşil: B ile C arası 2 yol. Sarı: A ile C arası doğrudan 4 yol.")

Bir yolcu A kentinden C kentine kaç farklı biçimde gidebilir? (Yolcu bir kente en çok bir kez uğrar.)

A) 6
B) 9
C) 10
D) 14
E) 24

**Cevap:** C
**Çözüm:** İki ayrık durum var. B'ye uğrayarak: A→B **ve** B→C, $3 \cdot 2 = 6$. B'ye uğramadan: doğrudan 4 yol. Durumlar "ya da" ile bağlı, toplanır: $6 + 4 = 10$. 9 her şeyi toplamaktır ($3 + 2 + 4$); 24 her şeyi çarpmaktır ($3 \cdot 2 \cdot 4$); 6 doğrudan yolları unutmaktır.

## ÖSYM tarzı

### Soru 8 · ÖSYM tarzı
Bir mobil uygulamada kullanıcı adı, A, B, C, D harflerinden **birbirinden farklı** iki harf ve ardından iki rakam (0–9) yazılarak oluşturuluyor. Rakamlar aynı olabilir. Örneğin AB37, DC00 ve CA55 birer kullanıcı adıdır; AA12 ise değildir.

Buna göre en fazla kaç farklı kullanıcı adı oluşturulabilir?

A) 27
B) 112
C) 1080
D) 1200
E) 1600

**Cevap:** D
**Çözüm:** Dört kutu: 1. harf 4 yol, 2. harf (ilkinden farklı) 3 yol, 1. rakam 10 yol, 2. rakam 10 yol. $4 \cdot 3 \cdot 10 \cdot 10 = 1200$. 1600, harflerin aynı olabileceğini sanmaktır ($4 \cdot 4 \cdot 100$); 1080, rakamların da farklı olması gerektiğini sanmaktır ($12 \cdot 10 \cdot 9$); 112, harf ve rakam kısımlarını çarpmak yerine toplamaktır ($12 + 100$).

### Soru 9 · ÖSYM tarzı
Bir yarışmada kartların üzerinde 0, 1, 2, 3, 4 ve 5 rakamları yazılıdır; her rakamdan bir kart vardır. Bir yarışmacı bu kartlardan üçünü yan yana koyarak üç basamaklı bir sayı oluşturuyor. Oluşan sayı 5 ile tam bölünebiliyorsa yarışmacı puan kazanıyor.

Buna göre yarışmacının puan kazandığı kaç farklı sayı oluşturulabilir?

A) 20
B) 32
C) 36
D) 40
E) 50

**Cevap:** C
**Çözüm:** Her rakamdan bir kart olduğu için rakamlar farklıdır. 5 ile bölünen sayının birler basamağı 0 ya da 5'tir; iki durum ayrıdır.
Birler 0: yüzlere kalan 5 rakam, onlara kalan 4 rakam: $5 \cdot 4 = 20$.
Birler 5: yüzlere $0$ ve $5$ dışında 4 rakam, onlara kalan 4 rakam ($0$ dahil): $4 \cdot 4 = 16$.
Toplam $20 + 16 = 36$. 40, ikinci durumda da yüzlere 5 rakam yazıp $0$'ı unutmaktır ($20 + 20$); 20, yalnızca birler 0 durumunu saymaktır.

### Soru 10 · ÖSYM tarzı
Ece, Can ve Deniz; yan yana dizili 5 sandalyeden üçüne oturacaktır. Her sandalyeye en çok bir kişi oturur. Ece, sıranın **uçlarındaki** iki sandalyeden birine oturmak istemektedir.

Buna göre bu üç kişi kaç farklı biçimde oturabilir?

A) 6
B) 12
C) 24
D) 48
E) 60

**Cevap:** C
**Çözüm:** Kısıtlı kişiden başla. Ece iki uçtan birine: 2 yol. Can kalan 4 sandalyeden birine: 4 yol. Deniz kalan 3 sandalyeden birine: 3 yol. $2 \cdot 4 \cdot 3 = 24$. 12, yalnızca bir ucu saymaktır; 60, koşulu hiç kullanmamaktır ($5 \cdot 4 \cdot 3$).

### Soru 11 · ÖSYM tarzı
Bir elektronik kilit, 1'den 9'a kadar numaralı tuşlardan sırayla **üç** basışla açılmaktadır. Kilidin kuralına göre art arda yapılan iki basış aynı tuşa olamaz; ancak birinci ve üçüncü basış aynı tuşa olabilir. Örneğin 4-7-4 geçerli bir koddur, 4-4-7 ise değildir.

Buna göre bu kilit için kaç farklı kod belirlenebilir?

A) 24
B) 72
C) 504
D) 512
E) 576

**Cevap:** E
**Çözüm:** 1. basış 9 tuştan biri: 9 yol. 2. basış 1.'den farklı: 8 yol. 3. basış yalnızca 2.'den farklı olmalı: 8 yol. $9 \cdot 8 \cdot 8 = 576$. 504, üç basışın da birbirinden farklı olması gerektiğini sanmaktır ($9 \cdot 8 \cdot 7$); 72 ise üçüncü basışı unutmaktır.

### Soru 12 · ÖSYM tarzı
Bir bankanın kart şifreleri 0–9 rakamlarından oluşan dört haneli dizilerdir; şifre 0 ile başlayabilir ve rakamlar tekrar edebilir (0070, 1234 gibi). Banka, içinde **en az bir** tane 7 rakamı bulunan şifreleri "şanslı şifre" olarak adlandırıyor.

Buna göre kaç farklı şanslı şifre vardır?

A) 3439
B) 4000
C) 6561
D) 9000
E) 10000

**Cevap:** A
**Çözüm:** Tümleyenle say. Bütün şifreler: $10^4 = 10000$. Hiç 7 içermeyenler: her hanede 7 dışında 9 rakam, $9^4 = 6561$. Şanslı şifreler: $10000 - 6561 = 3439$. 6561 hiç 7 olmayanlardır; 4000, "7'yi bir haneye koy, kalan üç haneyi serbest bırak" diye $4 \cdot 10^3$ hesaplamaktır, bu yöntem birden fazla 7 içeren şifreleri birden çok kez sayar. 9000, ilk hanenin 0 olamayacağını sanmaktır.
