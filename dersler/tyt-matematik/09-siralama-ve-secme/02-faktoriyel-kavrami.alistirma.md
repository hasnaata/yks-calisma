---
baslik: Faktöriyel Kavramı · Alıştırma
ders: tyt-matematik
soru: 12
guncelleme: 2026-11-17
---
# Alıştırma: Faktöriyel Kavramı

Sorular özgündür ve ÖSYM soru tarzında yazılmıştır. Derse bakmadan çöz.

## Isınma

### Soru 1 · Kolay
$0! + 1! + 2! + 3!$ toplamı kaçtır?

A) 6
B) 8
C) 9
D) 10
E) 12

**Cevap:** D
**Çözüm:** $0! = 1$, $1! = 1$, $2! = 2$, $3! = 6$. Toplam $1 + 1 + 2 + 6 = 10$. $0!$'i $0$ alan $9$ bulur.

### Soru 2 · Kolay
$\dfrac{9!}{7! \cdot 2!}$ işleminin sonucu kaçtır?

A) 9
B) 18
C) 36
D) 72
E) 81

**Cevap:** C
**Çözüm:** $9! = 9 \cdot 8 \cdot 7!$ olduğundan $\frac{9 \cdot 8 \cdot 7!}{7! \cdot 2} = \frac{72}{2} = 36$. $72$, paydadaki $2!$'i unutmaktır.

### Soru 3 · Kolay
Birbirinden farklı 5 kitap bir rafa yan yana kaç farklı şekilde dizilebilir?

A) 5
B) 15
C) 25
D) 60
E) 120

**Cevap:** E
**Çözüm:** 1. yere 5, 2. yere 4, 3. yere 3, 4. yere 2, 5. yere 1 seçenek: $5 \cdot 4 \cdot 3 \cdot 2 \cdot 1 = 5! = 120$. $15$ çarpmak yerine toplamaktan ($5 + 4 + 3 + 2 + 1$), $60$ son iki yeri unutmaktan ($5 \cdot 4 \cdot 3$) gelir.

## Orta

### Soru 4 · Orta
$n$ pozitif tam sayı olmak üzere

$$\frac{(n+1)!}{(n-1)!} = 56$$

olduğuna göre $n$ kaçtır?

A) 6
B) 7
C) 8
D) 9
E) 10

**Cevap:** B
**Çözüm:** $(n+1)! = (n+1) \cdot n \cdot (n-1)!$ olduğundan sol taraf $(n+1) \cdot n$ olur. $56 = 8 \cdot 7$, ardışık iki sayının çarpımı; küçüğü $n = 7$. $8$, $n + 1$ değerini cevap sanmaktır.

### Soru 5 · Orta
$\dfrac{6! + 7! + 8!}{6! + 7!}$ işleminin sonucu kaçtır?

A) 8
B) 9
C) 36
D) 56
E) 64

**Cevap:** A
**Çözüm:** En küçük faktöriyel $6!$. $7! = 7 \cdot 6!$, $8! = 8 \cdot 7 \cdot 6! = 56 \cdot 6!$.
Pay: $6!\,(1 + 7 + 56) = 64 \cdot 6!$. Payda: $6!\,(1 + 7) = 8 \cdot 6!$. Sonuç $\frac{64}{8} = 8$. Parantezlerdeki 1'leri unutan $\frac{63}{7} = 9$; paydayı unutan $64$ bulur.

### Soru 6 · Orta
$3! + 4! + 5! + \ldots + 40!$ toplamının birler basamağındaki rakam kaçtır?

A) 0
B) 3
C) 4
D) 6
E) 9

**Cevap:** A
**Çözüm:** $5!$ ve sonrası 0 ile biter. Geriye $3! + 4! = 6 + 24 = 30$ kalır; birler basamağı $0$. Toplamın $1!$'den başladığını sanan $1 + 2 + 6 + 24 = 33$ ile $3$ bulur.

### Soru 7 · Orta
$k$ ve $A$ doğal sayılar olmak üzere $60! = 3^k \cdot A$ olduğuna göre $k$ en çok kaçtır?

A) 20
B) 22
C) 26
D) 27
E) 28

**Cevap:** E
**Çözüm:** $60$'ı art arda 3'e böl: $60 : 3 = 20$, $20 : 3 = 6$ (kalan 2 atılır), $6 : 3 = 2$, $2 < 3$ dur. Bölümler toplamı $20 + 6 + 2 = 28$. Yalnızca ilk bölümü alan $20$, son bölümü unutan $26$ bulur.

## ÖSYM tarzı

### Soru 8 · ÖSYM tarzı
Her $n$ doğal sayısı için $f(n) = \dfrac{(n+2)!}{n!}$ olarak tanımlanıyor.

$f(a) = 42$ olduğuna göre $f(a+1)$ kaçtır?

A) 48
B) 56
C) 63
D) 72
E) 90

**Cevap:** B
**Çözüm:** $f(n) = (n+2)(n+1)$. $f(a) = (a+2)(a+1) = 42 = 7 \cdot 6$, yani $a = 5$. $f(6) = 8 \cdot 7 = 56$. $72 = 9 \cdot 8$, $a$ yerine $a + 1 = 6$'yı $a$ sanıp $f(7)$ hesaplamaktır; $48 = 8 \cdot 6$ ise bir çarpanı yanlış artırmaktır.

### Soru 9 · ÖSYM tarzı
Bir ışık gösterisinde birbirinden farklı renkteki lambalar her gösterimde farklı bir sırayla yakılıyor. Her sıralama 1 saniye sürüyor ve lambaların bütün sıralamaları tam bir kez gösterildiğinde gösteri 720 saniyede bitiyor.

Gösteriye farklı renkte bir lamba daha eklenirse aynı kuralla yapılan gösteri kaç dakika sürer?

A) 12
B) 72
C) 84
D) 96
E) 120

**Cevap:** C
**Çözüm:** Bütün sıralamaların sayısı $n! = 720$, yani $n = 6$ lamba var. Bir lamba eklenince $7! = 7 \cdot 6! = 5040$ sıralama, $5040$ saniye olur. $5040 : 60 = 84$ dakika. $12$ dakika eski süredir; $72$, süreyi 6 ile, $96$, 8 ile çarpmaktan gelir. Doğru çarpan $n + 1 = 7$'dir.

### Soru 10 · ÖSYM tarzı
$k$ bir doğal sayı olmak üzere $20!$ sayısı $12^k$ sayısına tam bölünmektedir.

Buna göre $k$ en çok kaçtır?

A) 6
B) 8
C) 9
D) 10
E) 18

**Cevap:** B
**Çözüm:** $12^k = 2^{2k} \cdot 3^k$. $20!$ içindeki 2'ler: $10 + 5 + 2 + 1 = 18$, bu da $2k \le 18$, $k \le 9$ verir. 3'ler: $20 : 3 = 6$, $6 : 3 = 2$, toplam $8$, yani $k \le 8$. İki koşul birlikte: $k$ en çok $8$. Yalnızca 2'lere bakan $9$, $2^2$'yi tek 2 sanan $18$ bulur.

### Soru 11 · ÖSYM tarzı
$a$ ve $b$ pozitif tam sayılar olmak üzere

$$a! = 6 \cdot b!$$

eşitliği sağlanıyor. Buna göre $a + b$ toplamının alabileceği değerlerin toplamı kaçtır?

A) 4
B) 11
C) 14
D) 15
E) 18

**Cevap:** D
**Çözüm:** $\frac{a!}{b!} = 6 > 1$, yani $a > b$ ve bu oran $b$'den sonraki ardışık sayıların çarpımıdır.
- Tek çarpan: $a = b + 1$ ve $a = 6$, $b = 5$; $a + b = 11$.
- İki çarpan: $(b+1)(b+2) = 6 = 2 \cdot 3$, $b = 1$, $a = 3$; $a + b = 4$.
- Üç çarpan: $(b+1)(b+2)(b+3) = 6 = 1 \cdot 2 \cdot 3$ için $b = 0$ gerekir, ama $b$ pozitif. Daha fazla çarpan 6'yı aşar.

Değerlerin toplamı $11 + 4 = 15$. Yalnızca $a = 6$, $b = 5$ çözümünü bulan $11$; $b = 0$ durumunu da sayan $18$ bulur.

### Soru 12 · ÖSYM tarzı
Ece, hesap makinesinde $1 \cdot 2 \cdot 3 \cdot \ldots \cdot n$ çarpımını hesaplıyor ve sonucun sonunda **tam olarak** 6 tane sıfır bulunduğunu görüyor.

Buna göre $n$ en az kaçtır?

A) 20
B) 24
C) 25
D) 29
E) 30

**Cevap:** C
**Çözüm:** Sıfır sayısı 5 çarpanı sayısıdır. $24!$ içinde $24 : 5 = 4$ tane 5 var, 4 sıfır. $25 = 5 \cdot 5$ iki tane 5 getirir: $25!$ içinde $5 + 1 = 6$ tane 5, yani tam 6 sıfır. En küçük $n = 25$. "Her 5 bir sıfır" diye $6 \cdot 5 = 30$ bulan yanılır: $30!$ sonunda $6 + 1 = 7$ sıfır vardır. $29$, 6 sıfırlı en büyük değerdir.
