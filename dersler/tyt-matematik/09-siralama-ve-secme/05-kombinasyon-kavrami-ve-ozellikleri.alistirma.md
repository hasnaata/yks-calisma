---
baslik: Kombinasyon Kavramı ve Özellikleri · Alıştırma
ders: tyt-matematik
soru: 12
guncelleme: 2026-11-17
---
# Alıştırma: Kombinasyon Kavramı ve Özellikleri

Sorular özgündür ve ÖSYM soru tarzında yazılmıştır. Derse bakmadan çöz.

## Isınma

### Soru 1 · Kolay
$C(8, 2) + C(8, 8)$ işleminin sonucu kaçtır?

A) 29
B) 36
C) 56
D) 57
E) 64

**Cevap:** A
**Çözüm:** $C(8, 2) = \dfrac{8 \cdot 7}{2} = 28$. $C(8, 8) = 1$. Toplam $28 + 1 = 29$. 36, $C(8, 8)$'i 8 sanmaktır; 56, 2'ye bölmeyi unutup ($P(8, 2)$) $C(8, 8)$'i 0 almaktır; 57, $P(8, 2) + 1$; 64 ise $P(8, 2) + 8$'dir.

### Soru 2 · Kolay
9 kişilik bir sınıftan 4 kişilik bir temizlik ekibi seçilecektir. Kaç farklı ekip seçilebilir?

A) 24
B) 84
C) 126
D) 3024
E) 15120

**Cevap:** C
**Çözüm:** Ekipte görev farkı yok, sıra önemsiz: $C(9, 4) = \dfrac{9 \cdot 8 \cdot 7 \cdot 6}{4 \cdot 3 \cdot 2 \cdot 1} = \dfrac{3024}{24} = 126$. 3024, $4!$'e bölmeyi unutmaktır ($P(9, 4)$); 84, 3 kişilik ekip saymaktır ($C(9, 3)$); 15120, $\dfrac{9!}{4!}$ yazmaktır; 24 ise yalnızca $4!$'tür.

### Soru 3 · Kolay
$C(n, 2) = 21$ olduğuna göre $n$ kaçtır?

A) 6
B) 7
C) 8
D) 21
E) 42

**Cevap:** B
**Çözüm:** $\dfrac{n(n - 1)}{2} = 21$, yani $n(n - 1) = 42 = 7 \cdot 6$. Büyük çarpan $n$: $n = 7$. Kontrol: $C(7, 2) = \dfrac{7 \cdot 6}{2} = 21$. 6, çarpımı $n(n + 1)$ sanmaktır; 42 ise $n(n-1) = 42$ ara sonucunu cevap sanmaktır.

## Orta

### Soru 4 · Orta
$C(n, 4) = C(n, 6)$ olduğuna göre $C(n, 8)$ kaçtır?

A) 45
B) 90
C) 120
D) 210
E) 252

**Cevap:** A
**Çözüm:** $4 \ne 6$ olduğundan simetriyle $n = 4 + 6 = 10$. $C(10, 8) = C(10, 2) = \dfrac{10 \cdot 9}{2} = 45$. 90, 2'ye bölmeyi unutmaktır; 120, $C(10, 3)$'tür; 210, $C(10, 4)$'tür; 252 ise $C(10, 5)$'tir.

### Soru 5 · Orta
$C(6, 2) + C(6, 3) = C(7, k)$ eşitliğini sağlayan $k$ değerlerinin toplamı kaçtır?

A) 3
B) 4
C) 5
D) 6
E) 7

**Cevap:** E
**Çözüm:** Toplama özelliği: $C(6, 2) + C(6, 3) = C(7, 3)$. Kontrol: $15 + 20 = 35 = C(7, 3)$. Simetriden $C(7, 3) = C(7, 4)$ olduğundan $k = 3$ ya da $k = 4$. Toplam $3 + 4 = 7$. 3, yalnızca bir değer bulmaktır; 5 ise alt sayıları toplamaktır ($2 + 3$).

### Soru 6 · Orta
Aralarında Aslı ile Burak'ın da bulunduğu 10 kişilik bir gruptan 4 kişilik bir ekip seçilecektir. Aslı'nın ekipte **bulunduğu**, Burak'ın ise **bulunmadığı** kaç farklı ekip seçilebilir?

A) 28
B) 56
C) 70
D) 84
E) 210

**Cevap:** B
**Çözüm:** Aslı'yı ekibe koy, Burak'ı adaylardan çıkar. Kalan adaylar $10 - 2 = 8$ kişi, seçilecek $4 - 1 = 3$ kişi: $C(8, 3) = \dfrac{8 \cdot 7 \cdot 6}{6} = 56$. 84 ($C(9, 3)$), Burak'ı çıkarmayı unutmaktır; 70 ($C(8, 4)$), Aslı'nın bir yer kapladığını unutmaktır; 28 ($C(8, 2)$), ikisini de ekibe koymaktır; 210 ise koşulsuz seçimdir.

### Soru 7 · Orta
$A = \{1, 2, 3, 4, 5, 6, 7\}$ kümesinin **en az 2 elemanlı** alt kümelerinin sayısı kaçtır?

A) 21
B) 35
C) 120
D) 121
E) 127

**Cevap:** C
**Çözüm:** Bütün alt kümeler $2^7 = 128$. Bunlardan 0 elemanlı ($C(7, 0) = 1$) ve 1 elemanlı ($C(7, 1) = 7$) olanları çıkar: $128 - 1 - 7 = 120$. 121, boş kümeyi çıkarmayı unutmaktır; 127 yalnızca boş kümeyi çıkarmaktır; 21 ise yalnızca 2 elemanlı alt kümelerin sayısıdır.

## ÖSYM tarzı

### Soru 8 · ÖSYM tarzı
Bir dondurmacıda birbirinden farklı 6 çeşit sos vardır. Müşteri dondurmasına **en çok 2** çeşit sos ekletebilir; hiç sos istemeyebilir de. Sosların ekleniş sırası önemsizdir.

Buna göre bir müşteri sos seçimini kaç farklı biçimde yapabilir?

A) 6
B) 7
C) 15
D) 21
E) 22

**Cevap:** E
**Çözüm:** Hiç sos: $C(6, 0) = 1$. Bir sos: $C(6, 1) = 6$. İki sos: $C(6, 2) = 15$. Toplam $1 + 6 + 15 = 22$. 21, "hiç sos istemeyebilir" durumunu unutmaktır; 15 yalnızca iki sosluları, 7 ise yalnızca sıfır ve bir sosluları saymaktır.

### Soru 9 · ÖSYM tarzı
Bir futbol liginde her takım diğer her takımla yalnızca bir kez maç yapmış ve toplam 66 maç oynanmıştır. Gelecek sezon lige 2 yeni takım katılacak ve aynı kuralla maçlar oynanacaktır.

Buna göre gelecek sezon oynanacak maç sayısı bu sezona göre kaç artar?

A) 12
B) 24
C) 25
D) 48
E) 91

**Cevap:** C
**Çözüm:** Her maç 2 takımın seçimidir: $C(n, 2) = 66$, $n(n - 1) = 132 = 12 \cdot 11$, $n = 12$. Gelecek sezon 14 takım: $C(14, 2) = \dfrac{14 \cdot 13}{2} = 91$. Artış $91 - 66 = 25$. Kontrol: iki yeni takımın her biri 12 eski takımla oynar ($2 \cdot 12 = 24$), bir de kendi aralarında 1 maç: $25$. 24, iki yeni takımın kendi aralarındaki maçı unutmaktır; 12, yalnızca bir takım eklemektir; 91 ise artış yerine toplam maç sayısıdır.

### Soru 10 · ÖSYM tarzı
Bir kümenin 3 elemanlı alt kümelerinin sayısı, 2 elemanlı alt kümelerinin sayısının 2 katıdır.

Buna göre bu kümenin 4 elemanlı alt kümelerinin sayısı kaçtır?

A) 8
B) 28
C) 56
D) 70
E) 1680

**Cevap:** D
**Çözüm:** $C(n, 3) = 2 \cdot C(n, 2)$. Açık yaz: $\dfrac{n(n-1)(n-2)}{6} = 2 \cdot \dfrac{n(n-1)}{2}$. $n(n - 1)$ sadeleşir: $\dfrac{n - 2}{6} = 1$, $n = 8$. Kontrol: $C(8, 3) = 56 = 2 \cdot 28$. İstenen $C(8, 4) = \dfrac{8 \cdot 7 \cdot 6 \cdot 5}{24} = 70$. 8, eleman sayısını cevap sanmaktır; 28 ve 56 sırasıyla $C(8, 2)$ ve $C(8, 3)$'tür; 1680 ise $4!$'e bölmeyi unutmaktır ($P(8, 4)$).

### Soru 11 · ÖSYM tarzı
Bir öğrenci okuma listesindeki birbirinden farklı 9 kitaptan 4'ünü seçecektir. Listedeki kitaplardan 2'si aynı yazara aittir ve öğrenci bu iki kitaptan **en çok birini** seçmek istemektedir.

Buna göre öğrenci seçimini kaç farklı biçimde yapabilir?

A) 21
B) 35
C) 70
D) 105
E) 126

**Cevap:** D
**Çözüm:** Bütün seçimler $C(9, 4) = 126$. İstenmeyen durum iki kitabın ikisinin birden seçilmesi: o ikisini al, kalan 7 kitaptan 2 tane seç, $C(7, 2) = 21$. İstenen $126 - 21 = 105$. Doğrudan: hiçbiri yok $C(7, 4) = 35$, tam biri var $2 \cdot C(7, 3) = 70$; $35 + 70 = 105$. 35 ve 70 durumlardan yalnızca birini saymaktır; 21 istenmeyen durumdur; 126 ise koşulsuz seçimdir.

### Soru 12 · ÖSYM tarzı
Bir öğretmen 10 öğrencilik kulübünden bir yarışmaya öğrenci gönderecektir. Yarışma kuralına göre gönderilen öğrenci sayısı 3 ya da 7 olmalıdır.

Buna göre öğretmen gönderilecek öğrencileri kaç farklı biçimde belirleyebilir?

A) 120
B) 240
C) 720
D) 1024
E) 1440

**Cevap:** B
**Çözüm:** 3 öğrenci gönderme: $C(10, 3) = \dfrac{10 \cdot 9 \cdot 8}{6} = 120$. 7 öğrenci gönderme: $C(10, 7) = C(10, 3) = 120$. Bu iki durum farklıdır (3 kişilik takım ile 7 kişilik takım aynı değildir), toplanır: $120 + 120 = 240$. 120, simetri yüzünden iki durumu tek sanmaktır; 720 ($P(10, 3)$), sırayı önemli saymaktır; 1440 bunun iki katıdır; 1024 ($2^{10}$) ise bütün alt kümelerin sayısıdır.
