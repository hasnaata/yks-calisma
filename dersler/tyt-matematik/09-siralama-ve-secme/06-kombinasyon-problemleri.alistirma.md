---
baslik: Kombinasyon Problemleri · Alıştırma
ders: tyt-matematik
soru: 12
guncelleme: 2026-11-17
---
# Alıştırma: Kombinasyon Problemleri

Sorular özgündür ve ÖSYM soru tarzında yazılmıştır. Derse bakmadan çöz.

## Isınma

### Soru 1 · Kolay
8 kişilik bir sınıftan bir proje için 3 kişilik bir çalışma grubu kaç farklı şekilde seçilebilir?

A) 11
B) 24
C) 28
D) 56
E) 336

**Cevap:** D
**Çözüm:** Grupta görev yok; üyelerin yeri değişince yeni grup oluşmaz. Sıra önemsiz: $\binom{8}{3} = \frac{8 \cdot 7 \cdot 6}{3 \cdot 2 \cdot 1} = 56$. $336 = P(8, 3)$ sırayı önemli saymaktır; $28 = \binom{8}{2}$ yanlış sayıda kişi seçmektir; $11$ ve $24$ sayıları toplamak ya da çarpmaktır.

### Soru 2 · Kolay
6 kız ve 5 erkek öğrenci arasından 2 kız ve 2 erkekten oluşan 4 kişilik bir ekip kaç farklı şekilde seçilebilir?

A) 15
B) 25
C) 150
D) 330
E) 600

**Cevap:** C
**Çözüm:** 2 kız $\binom{6}{2} = 15$, 2 erkek $\binom{5}{2} = 10$ şekilde seçilir. Kızlar **ve** erkekler seçildiği için çarpılır: $15 \cdot 10 = 150$. $25$ toplamak, $330 = \binom{11}{4}$ kız-erkek koşulunu yok saymak, $600 = P(6, 2) \cdot P(5, 2)$ sırayı önemli saymaktır.

### Soru 3 · Kolay
Bir toplantıya katılan 12 kişinin her biri diğerlerinin her biriyle birer kez tokalaşmıştır.

Toplam kaç tokalaşma olmuştur?

A) 24
B) 66
C) 78
D) 132
E) 144

**Cevap:** B
**Çözüm:** Her tokalaşma 2 kişiyle belirlenir ve Ali-Can ile Can-Ali tokalaşması aynıdır: $\binom{12}{2} = \frac{12 \cdot 11}{2} = 66$. $132 = 12 \cdot 11$ her tokalaşmayı iki kez saymaktır; $144 = 12^2$ kişinin kendisiyle tokalaşmasını da saymaktır.

## Orta

### Soru 4 · Orta
Aralarında Ayşe'nin de bulunduğu 6 kız ve 5 erkek arasından 2 kız ve 2 erkekten oluşan 4 kişilik bir ekip seçilecektir.

Ayşe'nin kesinlikle bulunduğu kaç farklı ekip seçilebilir?

A) 50
B) 100
C) 120
D) 150
E) 210

**Cevap:** A
**Çözüm:** Ayşe ekibe konur. Geriye 1 kız daha (kalan 5 kızdan) ve 2 erkek seçilir: $\binom{5}{1} \cdot \binom{5}{2} = 5 \cdot 10 = 50$. $150$ Ayşe koşulunu yok saymak, $120 = \binom{10}{3}$ kız-erkek koşulunu unutmak, $100$ erkekleri sıralamaktır ($5 \cdot P(5, 2)$).

### Soru 5 · Orta
4 öğretmen ve 6 öğrenci arasından 3 kişilik bir komisyon seçilecektir.

Komisyonda en az 1 öğretmen bulunacağına göre kaç farklı komisyon seçilebilir?

A) 20
B) 60
C) 96
D) 100
E) 144

**Cevap:** D
**Çözüm:** Tüm komisyonlar $\binom{10}{3} = 120$. Hiç öğretmen olmayanlar $\binom{6}{3} = 20$. $120 - 20 = 100$. Kontrol: 1 öğretmenli $4 \cdot 15 = 60$, 2 öğretmenli $6 \cdot 6 = 36$, 3 öğretmenli $4$; $60 + 36 + 4 = 100$. $96$ son durumu unutmak, $144 = 4 \cdot \binom{9}{2}$ "önce 1 öğretmen koy" diyerek aynı komisyonları birden çok kez saymaktır.

### Soru 6 · Orta
Aralarında Deniz ve Emre'nin de bulunduğu 9 kişiden 4 kişilik bir takım seçilecektir.

Deniz ile Emre aynı takımda **bulunmayacaksa** kaç farklı takım seçilebilir?

A) 21
B) 35
C) 70
D) 84
E) 105

**Cevap:** E
**Çözüm:** Tüm takımlar $\binom{9}{4} = 126$. İkisi birlikteyse kalan 2 kişi diğer 7 kişiden seçilir: $\binom{7}{2} = 21$. $126 - 21 = 105$. Kontrol: ikisi de yok $\binom{7}{4} = 35$, yalnızca biri var $2 \cdot \binom{7}{3} = 70$; $35 + 70 = 105$. $21$ istenmeyen durumun kendisi, $35$ ve $70$ istenen durumların yalnızca biridir.

### Soru 7 · Orta
4 kız ve 3 erkek arasından 2 kız ve 1 erkek seçilip bu 3 kişi bir fotoğraf için yan yana dizilecektir.

Kaç farklı fotoğraf karesi oluşturulabilir?

A) 18
B) 35
C) 36
D) 108
E) 210

**Cevap:** D
**Çözüm:** Önce seç: $\binom{4}{2} \cdot \binom{3}{1} = 6 \cdot 3 = 18$. Sonra diz: seçilen 3 kişi $3! = 6$ şekilde sıralanır. $18 \cdot 6 = 108$. $18$ dizmeyi unutmak, $35 = \binom{7}{3}$ kız-erkek koşulunu ve dizmeyi unutmak, $210 = P(7, 3)$ kız-erkek koşulunu unutmaktır.

## ÖSYM tarzı

### Soru 8 · ÖSYM tarzı
Bir lokantadaki öğle menüsünde 4 çeşit çorba, 6 çeşit ana yemek ve 3 çeşit tatlı vardır. Menüyü seçen bir müşteri

- 1 çorba,
- birbirinden farklı 2 ana yemek,
- en fazla 1 tatlı

seçmektedir.

Buna göre bir müşteri kaç farklı öğle menüsü seçebilir?

A) 23
B) 180
C) 240
D) 360
E) 480

**Cevap:** C
**Çözüm:** Çorba $4$, ana yemekler $\binom{6}{2} = 15$ şekilde seçilir. "En fazla 1 tatlı": tatlı yok (1 yol) ya da 3 tatlıdan biri (3 yol), toplam $1 + 3 = 4$. Hepsi birlikte seçildiği için çarp: $4 \cdot 15 \cdot 4 = 240$. $180$ tatsız menüyü unutmak, $480$ ana yemekleri sıralamak ($P(6, 2) = 30$), $23$ çarpacağına toplamaktır.

### Soru 9 · ÖSYM tarzı
Selin'in 5 farklı romanı ve 3 farklı şiir kitabı vardır. Selin bunlardan 2 roman ve 2 şiir kitabı seçip rafına yan yana dizecektir.

Buna göre raftaki diziliş kaç farklı şekilde olabilir?

A) 30
B) 70
C) 180
D) 240
E) 720

**Cevap:** E
**Çözüm:** Önce seç: $\binom{5}{2} \cdot \binom{3}{2} = 10 \cdot 3 = 30$. Sonra diz: 4 farklı kitap $4! = 24$ şekilde dizilir. $30 \cdot 24 = 720$. $30$ dizmeyi unutmak, $70 = \binom{8}{4}$ kitap türünü önemsememek, $240$ şiirleri seçmeyi unutmak ($10 \cdot 24$), $180$ kitapları özdeş sanıp $\frac{4!}{2! \cdot 2!}$ ile dizmektir.

### Soru 10 · ÖSYM tarzı
Bir pizzacıda 3 farklı boy ve 8 farklı malzeme vardır. Müşteri bir boy seçer ve pizzasına en az 2, en çok 3 farklı malzeme ekletir.

Buna göre kaç farklı pizza siparişi verilebilir?

A) 84
B) 168
C) 252
D) 276
E) 4704

**Cevap:** C
**Çözüm:** Malzeme: 2 tane $\binom{8}{2} = 28$ ya da 3 tane $\binom{8}{3} = 56$; "ya da" olduğu için topla: $28 + 56 = 84$. Boy ile çarp: $3 \cdot 84 = 252$. $84$ boyu unutmak, $168$ yalnızca 3 malzemeli siparişleri saymak, $276$ "en az 2" koşulunu unutup 1 malzemeyi de saymak ($3 \cdot (8 + 28 + 56)$), $4704$ iki durumu toplayacağına çarpmaktır.

### Soru 11 · ÖSYM tarzı
5 kız ve 4 erkekten oluşan bir kulüpten 4 kişilik bir takım seçilecektir. Takımdaki kızların sayısı erkeklerin sayısından fazla olacaktır.

Buna göre kaç farklı takım seçilebilir?

A) 40
B) 45
C) 60
D) 105
E) 126

**Cevap:** B
**Çözüm:** 4 kişilik takımda kızlar erkeklerden fazlaysa 3 kız 1 erkek ya da 4 kız olur. 3 kız 1 erkek: $\binom{5}{3} \cdot \binom{4}{1} = 10 \cdot 4 = 40$. 4 kız: $\binom{5}{4} = 5$. Toplam $45$. $105$ eşit sayıyı da (2 kız 2 erkek, $60$) kabul etmek, $40$ yalnızca bir durumu saymak, $126$ koşulu yok saymaktır.

### Soru 12 · ÖSYM tarzı
Bir futbol turnuvasında her takım diğer her takımla yalnızca bir kez maç yapmaktadır. Turnuvaya son anda 2 takım daha katılınca oynanacak toplam maç sayısı 25 artmıştır.

Buna göre turnuvada başlangıçta kaç takım vardı?

A) 12
B) 13
C) 14
D) 24
E) 25

**Cevap:** A
**Çözüm:** Başlangıçta $n$ takım varsa maç sayısı $\binom{n}{2}$. Yeni maçlar: iki yeni takımın her biri eski $n$ takımla oynar ($2n$) ve kendi aralarında 1 maç yapar: $2n + 1 = 25$, $n = 12$. Kontrol: $\binom{14}{2} - \binom{12}{2} = 91 - 66 = 25$. $14$ yeni takım sayısıdır; iki yeni takımın kendi arasındaki maçı unutan $2n = 25$ ile tam sayı bulamaz.
