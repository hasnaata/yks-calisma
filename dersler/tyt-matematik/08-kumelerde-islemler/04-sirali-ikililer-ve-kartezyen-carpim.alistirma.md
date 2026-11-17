---
baslik: Sıralı İkililer ve Kartezyen Çarpım · Alıştırma
ders: tyt-matematik
soru: 12
guncelleme: 2026-11-17
---
# Alıştırma: Sıralı İkililer ve Kartezyen Çarpım

Sorular özgündür ve ÖSYM soru tarzında yazılmıştır. Derse bakmadan çöz.

## Isınma

### Soru 1 · Kolay
$(2x - 1,\ y + 4) = (7,\ 1)$ olduğuna göre $x + y$ toplamı kaçtır?

A) 1
B) 4
C) 5
D) 7
E) 9

**Cevap:** A
**Çözüm:** Birinci bileşenler eşit: $2x - 1 = 7$, $2x = 8$, $x = 4$. İkinci bileşenler eşit: $y + 4 = 1$, $y = -3$. Toplam $4 + (-3) = 1$. 4 yalnızca $x$'tir; 7, $x - y$ farkıdır; 9, $y$'yi işaret hatasıyla $5$ bulmaktan gelir.

### Soru 2 · Kolay
$s(A) = 4$ ve $s(B) = 3$ olduğuna göre $s(A \times B) + s(B \times B)$ toplamı kaçtır?

A) 7
B) 12
C) 16
D) 21
E) 25

**Cevap:** D
**Çözüm:** $s(A \times B) = 4 \cdot 3 = 12$, $s(B \times B) = 3 \cdot 3 = 9$. Toplam $12 + 9 = 21$. 7, eleman sayılarını çarpmak yerine toplamaktan; 25, $B \times B$ yerine $A \times A$ (16) almaktan gelir.

### Soru 3 · Kolay
$A = \{1, 2\}$ ve $B = \{3, 4, 5\}$ olduğuna göre aşağıdakilerden hangisi $B \times A$ kümesinin elemanı **değildir**?

A) $(3, 1)$
B) $(3, 2)$
C) $(4, 1)$
D) $(5, 2)$
E) $(2, 4)$

**Cevap:** E
**Çözüm:** $B \times A$'da birinci bileşen $B = \{3, 4, 5\}$'ten, ikinci bileşen $A = \{1, 2\}$'den gelir. $(2, 4)$ ikilisinde birinci bileşen $2 \notin B$; bu ikili $A \times B$'nin elemanıdır, $B \times A$'nın değil. Diğer dört ikili kurala uyar.

## Orta

### Soru 4 · Orta
$A$ ve $B$ boş olmayan iki kümedir. $s(A \times B) = 24$ ve $s(B \times B) = 16$ olduğuna göre $s(A \times A)$ kaçtır?

A) 16
B) 24
C) 36
D) 48
E) 64

**Cevap:** C
**Çözüm:** $s(B)^2 = 16$ ise $s(B) = 4$. $s(A) \cdot 4 = 24$ ise $s(A) = 6$. $s(A \times A) = 6^2 = 36$. 16, $B \times B$'nin kendisidir; 24, $A \times B$'nin eleman sayısıdır; 48 ve 64 gibi değerler $s(A)$'yı yanlış bulmaktan gelir.

### Soru 5 · Orta
Aşağıdaki grafikte $A \times B$ kümesinin bütün elemanları gösterilmiştir.

![Koordinat düzleminde altı kırmızı nokta: (1, 2), (3, 2), (4, 2), (1, 3), (3, 3), (4, 3).](gorsel/tyt-matematik/08-04-soru5.svg "Noktaların x değerleri A'yı, y değerleri B'yi verir.")

Buna göre $A \cup B$ kümesi kaç elemanlıdır?

A) 2
B) 3
C) 4
D) 5
E) 6

**Cevap:** C
**Çözüm:** x değerleri: $A = \{1, 3, 4\}$. y değerleri: $B = \{2, 3\}$. $A \cup B = \{1, 2, 3, 4\}$, 4 eleman. 5, $3 + 2$ toplamından gelir; ortak eleman $3$ iki kez sayılmıştır. 6, grafikteki nokta sayısıdır.

### Soru 6 · Orta
$A = \{1, 2, 3\}$, $B = \{2, 3, 4, 5\}$ ve $C = \{3, 5, 6\}$ olduğuna göre $(A \times B) \cap (A \times C)$ kümesi kaç elemanlıdır?

A) 2
B) 6
C) 9
D) 12
E) 15

**Cevap:** B
**Çözüm:** Kartezyen çarpım kesişim üzerine dağılır: $(A \times B) \cap (A \times C) = A \times (B \cap C)$. $B \cap C = \{3, 5\}$, eleman sayısı $2$. Sonuç $3 \cdot 2 = 6$. 2, yalnız $s(B \cap C)$'dir; 12 ve 9, $A \times B$ ile $A \times C$'nin eleman sayılarıdır; 15, birleşimin eleman sayısıdır.

### Soru 7 · Orta
$s(A) = n$ ve $s(B) = n + 2$ olmak üzere $s(A \times B) - s(A \times A) = 10$ olduğuna göre $s(B \times B)$ kaçtır?

A) 25
B) 35
C) 36
D) 49
E) 64

**Cevap:** D
**Çözüm:** $n(n + 2) - n^2 = 2n = 10$, buradan $n = 5$. $s(B) = 5 + 2 = 7$ ve $s(B \times B) = 7^2 = 49$. 25, $s(A \times A)$; 35, $s(A \times B)$ değeridir.

## ÖSYM tarzı

### Soru 8 · ÖSYM tarzı
Bir kafede menü, bir içecek ve bir tatlıdan oluşur ve (içecek, tatlı) sıralı ikilisiyle gösterilir. Kafede başlangıçta 20 farklı menü vardır. Menüye yeni bir içecek eklenince farklı menü sayısı 24 olur. Ardından yeni bir tatlı da eklenirse farklı menü sayısı kaç olur?

A) 30
B) 32
C) 35
D) 36
E) 40

**Cevap:** A
**Çözüm:** İçecek sayısı $n$, tatlı sayısı $t$ olsun: $n \cdot t = 20$ ve $(n + 1) \cdot t = 24$. Farkı al: $t = 4$, buradan $n = 5$. Yeni içecekle 6 içecek var; yeni tatlıyla 5 tatlı olur: $6 \cdot 5 = 30$. Kısa yol: yeni tatlı her içecekle bir menü kurar, $24 + 6 = 30$. 35, iki ekleme de içeceğe yapılmış gibi $7 \cdot 5$; 36, tatlı sayısını da 6 sanmaktan gelir.

### Soru 9 · ÖSYM tarzı
Bir oyunda Ali $A = \{1, 2, 3, 4, 5\}$ kümesinden, Berk $B = \{2, 4, 6\}$ kümesinden birer sayı seçer ve seçim (Ali'nin sayısı, Berk'in sayısı) sıralı ikilisiyle yazılır. Berk'in sayısı Ali'nin sayısından **büyükse** Berk kazanır.

Buna göre Berk'in kazandığı kaç farklı sıralı ikili vardır?

A) 4
B) 6
C) 7
D) 9
E) 11

**Cevap:** D
**Çözüm:** Toplam $5 \cdot 3 = 15$ ikili var. Berk'in sayısına göre say: Berk 2 seçerse Ali yalnız 1 olabilir (1 ikili); 4 seçerse Ali 1, 2, 3 (3 ikili); 6 seçerse Ali 1–5'in hepsi (5 ikili). Toplam $1 + 3 + 5 = 9$. Eşit sayıları da ($(2, 2)$ ve $(4, 4)$) katan 11 bulur; 4, Ali'nin büyük olduğu durumların sayısıdır.

### Soru 10 · ÖSYM tarzı
Aşağıdaki grafikte bir $A \times B$ kümesinin elemanlarından yalnızca dördü gösterilmiştir.

![Koordinat düzleminde dört kırmızı nokta: (1, 1), (2, 3), (4, 3), (4, 5).](gorsel/tyt-matematik/08-04-soru10.svg "Bu dört nokta A×B'nin içinde. A ve B en az hangi elemanları içermek zorunda?")

Buna göre $A \times B$ kümesi **en az** kaç elemanlıdır?

A) 4
B) 5
C) 6
D) 8
E) 9

**Cevap:** E
**Çözüm:** Her noktanın x değeri $A$'da, y değeri $B$'de olmalıdır. Öyleyse $\{1, 2, 4\} \subseteq A$ ve $\{1, 3, 5\} \subseteq B$. En küçük durumda $s(A) = 3$, $s(B) = 3$ ve $s(A \times B) = 3 \cdot 3 = 9$. 4 yalnız gösterilen noktalardır; 5, eksik nokta sayısıdır ($9 - 4$). Grafik ızgara oluşturmadığı için dört nokta tek başına bir kartezyen çarpım olamaz.

### Soru 11 · ÖSYM tarzı
$A = \{1, 2, 3, 4\}$ ve $B = \{3, 4, 5\}$ olduğuna göre $(A \times B) \cup (B \times A)$ kümesi kaç elemanlıdır?

A) 4
B) 20
C) 24
D) 25
E) 49

**Cevap:** B
**Çözüm:** $s(A \times B) = s(B \times A) = 4 \cdot 3 = 12$. Ortak elemanlar $(A \cap B) \times (A \cap B) = \{3, 4\} \times \{3, 4\}$, yani $4$ tane. Birleşim $12 + 12 - 4 = 20$. 24, ortakları iki kez saymaktır; 25, $(A \cup B) \times (A \cup B)$ kümesinin eleman sayısıdır ($5^2$); bu küme $(3, 1)$ gibi hiçbir çarpımda olmayan ikilileri de içerir.

### Soru 12 · ÖSYM tarzı
Bir ligde her takım diğer her takımla bir kez kendi sahasında, bir kez rakibin sahasında oynar. Her maç (ev sahibi, konuk) sıralı ikilisiyle gösterilir; bir takım kendisiyle oynamaz. Bu sezon ligde 30 maç oynanmıştır. Gelecek sezon lige bir takım daha katılırsa kaç maç oynanır?

A) 32
B) 36
C) 42
D) 49
E) 56

**Cevap:** C
**Çözüm:** Takım kümesi $T$ ve $s(T) = n$ olsun. Maçlar $T \times T$'nin $(a, a)$ biçiminde olmayan elemanlarıdır: $n^2 - n = n(n - 1) = 30$, buradan $n = 6$. Gelecek sezon $7$ takımla $7 \cdot 6 = 42$ maç oynanır. 49, takımın kendisiyle oynadığı $(a, a)$ ikililerini de saymaktan; 36, eski $6 \cdot 6$ hesabından; 56, $8 \cdot 7$ almaktan gelir.
