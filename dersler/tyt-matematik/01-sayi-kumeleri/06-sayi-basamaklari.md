---
baslik: Sayı Basamakları
ders: tyt-matematik
sure: 20 dk
kaynak: MEBİ Konu Özeti 7850c6c58e
guncelleme: 2026-11-17
---
# Sayı Basamakları

**Bu dersin sonunda:** $ab$, $abc$ gibi bilinmeyen rakamlı sayıları çözümleyip denkleme çevirebilecek, rakamları yer değiştiren ya da yanına rakam eklenen sayıların nasıl değiştiğini hesaplayabileceksin.

> **TYT'de yeri:** Basamak çözümlemesi hem doğrudan sorularda hem de başka konuların içinde sık sık gerekir. Sık gelen kalıplar: "$ab$ iki basamaklı sayı, $ab = k \cdot (a + b)$ ise…", "$AB - BA = 36$ olan kaç sayı var?", "sayının sağına bir rakam yazılınca sayı 466 artıyor" ve "rakamları farklı en büyük / en küçük sayı". Rakamı yanlış okunan sayı, kart dizme, şifre gibi günlük hayat kalıplarıyla da sorulur.

## Önce hatırla

<details><summary>Ardışık sayılardan: 15'ten 87'ye kadar (ikisi de dahil) kaç tek sayı vardır?</summary>
Ortak fark 2: $\frac{87 - 15}{2} + 1 = 36 + 1 = $ <b>37</b>. Bu derste aynı formülle "kaç tane üç basamaklı sayı var?" sorusunu cevaplayacaksın: $\frac{999 - 100}{1} + 1 = 900$.
</details>

<details><summary>Ardışık sayılardan: $1 + 2 + 3 + \dots + 20$ toplamı kaçtır?</summary>
$\frac{n(n+1)}{2}$ formülüyle $\frac{20 \cdot 21}{2} = $ <b>210</b>.
</details>

## Rakam, basamak, sayı değeri, basamak değeri

**Örnek.** $36\,382$ sayısında iki tane 3 var. İkisi aynı mı?

- İki 3'ün de **sayı değeri** 3'tür. Sayı değeri rakamın kendisidir.
- Soldaki 3 on binler basamağında, değeri $3 \cdot 10\,000 = 30\,000$. Sağdaki 3 yüzler basamağında, değeri $3 \cdot 100 = 300$. Bunlar **basamak değeri**dir.
- Basamak değerleri farkı: $30\,000 - 300 = 29\,700$. Sayı değerleri farkı ise $0$.

![Beş sütunlu tablo: on binler, binler, yüzler, onlar, birler. Rakamlar 3, 6, 3, 8, 2; basamak değerleri 30 000, 6 000, 300, 80, 2. İki 3 mavi.](gorsel/tyt-matematik/01-06-basamak-tablosu.svg "Aynı rakam, farklı yer: iki 3'ün sayı değeri aynı, basamak değerleri çok farklı.")

**Kural.** $0, 1, 2, \dots, 9$ sayılarına **rakam** denir; rakamın sayı içindeki yerine **basamak**. Basamak değeri = rakam $\times$ basamağın değeri (1, 10, 100, …).

İki önemli sonuç:

- Basamak sayısı belli olan bir sayının **ilk rakamı 0 olamaz**. $ab$ iki basamaklı ise $a \in \{1, \dots, 9\}$, $b \in \{0, \dots, 9\}$.
- İki basamaklı sayılar 10'dan 99'a, yani $99 - 10 + 1 = 90$ tane; üç basamaklılar $999 - 100 + 1 = 900$ tane.

**Rakam değişince sayı ne kadar değişir?** $abc$ üç basamaklı sayısında $a$ 2 artırılır, $c$ 3 azaltılırsa sayı $2 \cdot 100 - 3 \cdot 1 = 197$ **artar**. Her değişikliği kendi basamak değeriyle çarp.

## Çözümleme

**Örnek.** $ab$ iki basamaklı bir sayı ve $ab = 4 \cdot (a + b)$ ise bu koşulu sağlayan kaç sayı vardır?

1. Çözümle: $ab = 10a + b$.
2. Denklemi kur: $10a + b = 4a + 4b \Rightarrow 6a = 3b \Rightarrow b = 2a$.
3. Rakam sınırına bak: $b \le 9$ olduğundan $a \in \{1, 2, 3, 4\}$.
4. Sayılar: $12, 24, 36, 48$. Toplam **4** tane.

**Kural.** Sayıyı basamak değerlerinin toplamı olarak yazmaya **çözümleme** denir:

$$ab = 10a + b \qquad abc = 100a + 10b + c \qquad abcd = 1000a + 100b + 10c + d$$

$ab$ yazımı çarpım değildir: $ab \ne a \cdot b$. Denklemi çözdükten sonra **her zaman** rakam sınırlarını (0–9, ilk rakam 0 değil) kontrol et.

## Rakamları yer değiştiren sayılar

**Örnek.** $72 + 27$ ve $72 - 27$ işlemlerine basamakla bak.

![72 için 7 onluk çubuk ve 2 birlik küp, 27 için 2 onluk çubuk ve 7 birlik küp. Altta toplam: 9 onluk ve 9 birlik, 9 çarpı 11 eşittir 99.](gorsel/tyt-matematik/01-06-onluk-birlik.svg "Rakamlar yer değiştirince her rakam bir kez onluk, bir kez birlik olur. Toplam bu yüzden hep 11'in katıdır.")

Toplamda her rakam bir kez onluk, bir kez birlik olarak sayılır: $72 + 27 = 9 \cdot 11 = 99$. Farkta ise $72 - 27 = 5 \cdot 9 = 45$ çıkar ($7 - 2 = 5$).

Genel hali çözümlemeyle çıkar:

$$AB + BA = (10A + B) + (10B + A) = 11(A + B)$$
$$AB - BA = (10A + B) - (10B + A) = 9(A - B)$$

**Örnek.** $AB$ ve $BA$ iki basamaklı sayılar, $AB - BA = 36$ ise kaç farklı $AB$ sayısı vardır?

$9(A - B) = 36 \Rightarrow A - B = 4$. $BA$ iki basamaklı olduğu için $B \ne 0$: $B = 1, 2, 3, 4, 5$ ve sayılar $51, 62, 73, 84, 95$. Toplam **5** tane. ($B = 0$ alınsaydı $40$ da sayılırdı, ama $04$ iki basamaklı değildir.)

Üç basamaklıda ortadaki rakam yerinde kalır ve sadeleşir: $abc - cba = 99(a - c)$.

## Sağa, sola ya da araya rakam yazmak

**Örnek.** İki basamaklı bir sayının sağına 7 yazılınca sayı 466 artıyor. Sayı kaçtır?

![51 sayısının rakamları onlar ve birler basamağında. Sağına 7 yazılınca 5 yüzler, 1 onlar basamağına kayıyor, birler basamağına 7 geliyor.](gorsel/tyt-matematik/01-06-saga-yazma.svg "Sağa yazılan rakam eski rakamları bir basamak sola iter: sayı 10 ile çarpılır, sonra yazılan rakam eklenir.")

Sayı $x$ olsun. Sağına 7 yazılınca yeni sayı $10x + 7$ olur. Artış: $10x + 7 - x = 9x + 7 = 466 \Rightarrow 9x = 459 \Rightarrow x = 51$. Kontrol: $517 - 51 = 466$.

**Kural.**

| İşlem | Yeni sayı ($x$ iki basamaklı) |
|---|---|
| Sağına 0 yazmak | $10x$ (sayı 10 katına çıkar) |
| Sağına $r$ rakamı yazmak | $10x + r$ |
| Soluna $r$ rakamı yazmak | $100r + x$ |
| $ab$ sayısının arasına 0 yazmak | $a0b = 100a + b$ |

**Parçalı çözümleme.** Bir grup rakamı tek parça gibi de çözümleyebilirsin:

$$ABCDE = 1000 \cdot AB + CDE = 100 \cdot ABC + DE = 10 \cdot ABCD + E$$

**Örnek.** Dört basamaklı $ABAB$ sayısı $AB$ sayısının kaç katıdır? $ABAB = 100 \cdot AB + AB = 101 \cdot AB$. Cevap **101**. (Örneğin $3737 = 101 \cdot 37$.)

## En büyük ve en küçük sayı

**Örnek.** Rakamları farklı üç basamaklı en büyük ve en küçük sayıyı bul.

- En büyük: soldan başla, her basamağa kalan en büyük rakamı yaz: $987$.
- En küçük: ilk basamağa **0 olmayan** en küçük rakamı (1), sonra kalanların en küçüğünü yaz: $102$.

**Kural.** Büyük sayı için büyük rakamlar sola, küçük sayı için küçük rakamlar sola gelir; ilk basamak hiçbir zaman 0 olmaz. Negatif sayılarda sıra tersine döner: rakamları farklı üç basamaklı **en küçük** tam sayı $-987$'dir.

## ÖSYM tuzakları

> **$ab$'yi çarpım sanmak:** $ab = 4(a + b)$ denkleminde $ab$, $a \cdot b$ değil $10a + b$'dir. Çözümlemeden denklem kurma.

> **İlk rakamı 0 almak:** "$AB$ ve $BA$ iki basamaklı" ise $B$ de 0 olamaz. $A - B = 4$ için $40$'ı saymak bir fazla cevap verir.

> **Sayı değeri ile basamak değerini karıştırmak:** Soruda "basamak değeri" geçiyorsa rakamı basamağıyla çarp; "sayı değeri" geçiyorsa rakamın kendisini al.

> **Sağa yazılan rakamın etkisini eksik hesaplamak:** $x$'in sağına 7 yazmak sayıyı $x + 7$ yapmaz, $10x + 7$ yapar. Artış $9x + 7$'dir.

> **Negatif en küçük sayı:** "Rakamları farklı üç basamaklı en küçük tam sayı" $102$ değil, $-987$'dir. "Doğal sayı" mı "tam sayı" mı dendiğine bak.

## Kendini dene

### Soru 1
$2\,806\,451$ sayısında 8 rakamının basamak değeri ile 5 rakamının basamak değeri arasındaki fark kaçtır?

A) $3$
B) $799\,500$
C) $799\,950$
D) $800\,050$
E) $800\,500$

**Cevap:** C
**Çözüm:** 8 yüz binler basamağında: $8 \cdot 100\,000 = 800\,000$. 5 onlar basamağında: $5 \cdot 10 = 50$. Fark $800\,000 - 50 = 799\,950$. Sayı değerlerinin farkını alan $3$, 5'i yüzler basamağında sanan $799\,500$ bulur.

### Soru 2
$AB$ ve $BA$ iki basamaklı sayılardır. $AB - BA = 63$ eşitliğini sağlayan kaç farklı $AB$ sayısı vardır?

A) 1
B) 2
C) 3
D) 4
E) 5

**Cevap:** B
**Çözüm:** $9(A - B) = 63 \Rightarrow A - B = 7$. Olası çiftler: $(7, 0), (8, 1), (9, 2)$. $BA$ iki basamaklı olduğu için $B \ne 0$; $70$ elenir. Kalan sayılar $81$ ve $92$: **2** tane. $70$'i de sayan 3 bulur.

### Soru 3
İki basamaklı bir sayının soluna 4 yazılınca elde edilen üç basamaklı sayı, ilk sayının 9 katına eşit oluyor. İlk sayı kaçtır?

A) 30
B) 40
C) 45
D) 50
E) 60

**Cevap:** D
**Çözüm:** Sayı $x$ olsun. Soluna 4 yazınca $400 + x$ olur: $400 + x = 9x \Rightarrow 8x = 400 \Rightarrow x = 50$. Kontrol: $450 = 9 \cdot 50$. Soluna yazmayı $40 + x$ sanan $x = 5$ bulur; bu iki basamaklı değildir.

## Özet kartı

- Sayı değeri rakamın kendisi; basamak değeri rakam $\times$ basamağın değeri.
- Çözümle: $ab = 10a + b$, $abc = 100a + 10b + c$. $ab$ çarpım değildir.
- $AB + BA = 11(A + B)$, $AB - BA = 9(A - B)$, $abc - cba = 99(a - c)$.
- Sağına $r$ yazmak: $10x + r$; soluna $r$ yazmak (iki basamaklıda): $100r + x$.
- İlk rakam 0 olamaz; denklemi çözünce rakam sınırlarını kontrol et.
- En büyük sayıda büyük rakamlar, en küçük sayıda küçük rakamlar sola.

## Sonraki adım

Alıştırmaya geç (aşağıdaki düğme). Sonraki ders **Asal ve Aralarında Asal Sayılar**; sayıları çarpanlarına ayırırken burada öğrendiğin $ABAB = 101 \cdot AB$ gibi yazımlar işini kolaylaştıracak.
