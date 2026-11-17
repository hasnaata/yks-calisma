---
baslik: Pascal Üçgeni ve Binom Açılımı
ders: tyt-matematik
sure: 20 dk
kaynak: MEBİ Konu Özeti 53bfd274bb
guncelleme: 2026-11-18
---
# Pascal Üçgeni ve Binom Açılımı

**Bu dersin sonunda:** $(x + y)^n$ ifadesini Pascal üçgeniyle açabilecek; terim sayısını, katsayılar toplamını, sabit terimi ve istenen bir terimi genel terim formülüyle bulabileceksin.

> **TYT'de yeri:** Soru genelde açılımın tamamını istemez. "$x^3$'lü terimin katsayısı kaçtır?", "katsayılar toplamı kaçtır?", "sabit terim kaçtır?", "ortadaki terim nedir?" kalıpları gelir. Yeni nesil sorularda Pascal üçgeni bir yol sayma ya da sayı örüntüsü olarak gizlenir.

## Önce hatırla

<details><summary>Geçen dersten: Düzlemde herhangi üçü doğrusal olmayan 8 nokta var. Bu noktaların en az ikisinden geçen kaç farklı doğru çizilir?</summary>
Her doğru 2 noktayla belirlenir, sıra önemsiz: $C(8, 2) = \dfrac{8 \cdot 7}{2} = 28$. Bugün $C(n, r)$ sayılarını Pascal üçgeninde dizili olarak göreceksin.
</details>

<details><summary>Geçen dersten: Aynı düzlemdeki 4 farklı çember en çok kaç noktada kesişir?</summary>
Çember çiftlerinin sayısı $C(4, 2) = 6$; her çift en çok 2 noktada kesişir: $2 \cdot 6 = 12$.
</details>

## 1. Pascal üçgeni

**Örnek.** $(x + y)^2$ ve $(x + y)^3$ ifadelerini çarparak aç.

$(x + y)^2 = x^2 + 2xy + y^2$. Katsayılar: $1, 2, 1$.

$(x + y)^3 = (x + y)(x^2 + 2xy + y^2) = x^3 + 3x^2y + 3xy^2 + y^3$. Katsayılar: $1, 3, 3, 1$.

Bir sonraki satırı çarpmadan da bulabilirsin: başa ve sona 1 yaz, aradaki her sayı üstteki iki komşunun toplamı. $1, 3, 3, 1$ satırından $1,\ 1+3,\ 3+3,\ 3+1,\ 1$ yani $1, 4, 6, 4, 1$ gelir. Bunlar $(x + y)^4$'ün katsayılarıdır.

![Pascal üçgeninin n eşittir 0'dan 6'ya kadar satırları. Her satır 1 ile başlayıp 1 ile bitiyor. n eşittir 4 satırındaki 4 ve 6 mavi, altlarındaki 10 yeşil. Sağda satır toplamları: 1, 2, 4, 8, 16, 32, 64.](gorsel/tyt-matematik/09-08-pascal.svg "Her sayı üstündeki iki komşunun toplamı: 4 + 6 = 10. Satırlar simetrik ve n. satırın toplamı 2 üzeri n.")

**Kural.**

- Üçgenin tepesinde tek bir 1 vardır ($n = 0$ satırı). Her satırda bir öncekinden **bir fazla** sayı bulunur.
- Her satır 1 ile başlar, 1 ile biter; aradaki sayılar üstteki iki komşunun toplamıdır.
- $n$. satırdaki sayılar sırasıyla $C(n, 0), C(n, 1), \dots, C(n, n)$'dir ve $(x + y)^n$'in katsayılarını verir.
- Satırlar simetriktir ($C(n, r) = C(n, n - r)$) ve $n$. satırın toplamı $2^n$'dir.

> **Tuzak:** Satır numarası 0'dan başlar. $1, 4, 6, 4, 1$ satırı 5 sayı içerir ama $n = 4$ satırıdır; $(x + y)^5$'in değil $(x + y)^4$'ün katsayılarıdır.

## 2. Binom açılımı

**Örnek.** $(2x - 1)^3$ ifadesini aç.

$n = 3$ satırı: $1, 3, 3, 1$. Birinci terim $2x$, ikinci terim $-1$. Birincinin üssü 3'ten 0'a iner, ikincinin üssü 0'dan 3'e çıkar:

$$(2x - 1)^3 = 1 \cdot (2x)^3 + 3 \cdot (2x)^2 (-1) + 3 \cdot (2x)(-1)^2 + 1 \cdot (-1)^3$$

$$= 8x^3 - 12x^2 + 6x - 1$$

İşaretler $+, -, +, -$ diye sırayla değişti: $(-1)$'in tek kuvvetleri eksi, çift kuvvetleri artıdır.

![(x + y) üzeri 4 açılımının beş terimi kartlar hâlinde: katsayılar 1, 4, 6, 4, 1; terimler x üzeri 4, x küp y, x kare y kare, x y küp, y üzeri 4. Her kartın altında r = 0'dan 4'e ve üslerin toplamı 4.](gorsel/tyt-matematik/09-08-terimler.svg "x'in üssü her adımda 1 azalır, y'nin üssü 1 artar; her terimde üsler toplamı n = 4. Terimin sırası r + 1'dir.")

**Kural.** $n$ bir doğal sayı olmak üzere

$$(x + y)^n = C(n, 0)\,x^n + C(n, 1)\,x^{n-1}y + C(n, 2)\,x^{n-2}y^2 + \dots + C(n, n)\,y^n$$

- Açılımda **$n + 1$ terim** vardır.
- Her terimde $x$ ve $y$'nin üsleri toplamı $n$'dir.
- $C(n, r)$ yerine $\binom{n}{r}$ de yazılır; ikisi aynı sayıdır.

> **Tuzak:** $(2x)^3$ yerine $2x^3$ yazmak. Katsayılı terimin kuvveti alınırken katsayı da kuvvete girer: $(2x)^3 = 8x^3$.

## 3. Genel terim: istenen terimi doğrudan bul

**Örnek.** $(x + 2)^6$ açılımında $x^4$'lü terimin katsayısı kaçtır?

Bütün açılımı yazmana gerek yok. Baştan $(r + 1)$. terim $C(6, r)\,x^{6 - r}\,2^r$'dir.

1. $x$'in üssünü eşitle: $6 - r = 4 \Rightarrow r = 2$ (bu, baştan 3. terim).
2. Katsayı: $C(6, 2) \cdot 2^2 = 15 \cdot 4 = 60$.

**Kural.** $(x + y)^n$ açılımı $x$'in azalan kuvvetlerine göre yazılırsa

$$\text{Baştan } (r + 1).\ \text{terim} = C(n, r)\, x^{n - r}\, y^r$$

Baştan $(r + 1)$. terim aynı zamanda sondan $(n - r + 1)$. terimdir. Sondan $(r + 1)$. terim $C(n, r)\, x^r\, y^{n - r}$'dir.

**Ortadaki terim.** $n$ çiftse terim sayısı $n + 1$ tektir ve tek bir ortadaki terim vardır: $r = \dfrac{n}{2}$. $(x - 2)^6$ açılımında $r = 3$:

$$C(6, 3)\, x^3 (-2)^3 = 20 \cdot (-8)\, x^3 = -160x^3$$

$n$ tekse terim sayısı çifttir; tek bir ortadaki terim yoktur.

**Paydada $x$ varsa.** $\left(x + \dfrac{2}{x}\right)^6$ açılımında sabit terim kaçtır?

Genel terim $C(6, r)\, x^{6 - r} \left(\dfrac{2}{x}\right)^r = C(6, r)\, 2^r\, x^{6 - 2r}$. Sabit terimde $x$'in üssü 0'dır: $6 - 2r = 0 \Rightarrow r = 3$. Sabit terim $C(6, 3) \cdot 2^3 = 20 \cdot 8 = 160$.

> **Tuzak:** "Baştan 3. terim" demek $r = 3$ değil $r = 2$ demektir. Terimin sırası her zaman $r + 1$'dir.

## 4. Katsayılar toplamı ve sabit terim

**Örnek.** $(3x - 2)^5$ açılımında katsayılar toplamı ve sabit terim kaçtır?

- Katsayılar toplamı: değişkenlere 1 yaz. $(3 \cdot 1 - 2)^5 = 1^5 = 1$.
- Sabit terim: değişkenlere 0 yaz. $(3 \cdot 0 - 2)^5 = (-2)^5 = -32$.

Neden? $x = 1$ yazınca her terim yalnızca katsayısına eşit olur, toplam katsayılar toplamıdır. $x = 0$ yazınca $x$'li bütün terimler sıfırlanır, geriye sabit terim kalır.

Aynı yol çok terimli ifadelerde de çalışır: $(x^2 - 2x + 3)^4$ için katsayılar toplamı $(1 - 2 + 3)^4 = 16$, sabit terim $3^4 = 81$.

![Akış şeması: Ne soruluyor? Katsayılar toplamı ise değişkenlere 1 yaz. Sabit terim ise x paydada var mı diye bak; yoksa değişkenlere 0 yaz, varsa genel terimden r'yi bul. Belirli ya da ortadaki terim ise genel terimden r'yi bul.](gorsel/tyt-matematik/09-08-yontem.svg "Önce sorulanı belirle. x paydadaysa x = 0 yazılamaz; o zaman genel terimde x'in üssünü 0'a eşitle.")

**Kural.** Katsayılar toplamı için bütün değişkenlere **1**, sabit terim için bütün değişkenlere **0** yazılır. Paydada değişken varsa sabit terim genel terimle bulunur.

> **Tuzak:** Katsayılar toplamını her zaman $2^n$ sanmak. $2^n$ yalnızca $(x + y)^n$ için doğrudur; $(3x - 2)^5$'te toplam $1$'dir.

## ÖSYM tuzakları

> **Terim sayısı $n$ değil $n + 1$.** $(x + y)^9$ açılımında 10 terim vardır.

> **Sıra ile $r$'yi karıştırmak.** Baştan 4. terim $r = 3$ ile bulunur. Ortadaki terim için $r = \frac{n}{2}$.

> **Eksi işaretini kaybetmek.** $(x - 2)^5$'te $y = -2$'dir; $(-2)^r$ tek $r$ için eksidir. İşareti kuvvetin içinde taşı.

> **Katsayıyı kuvvete sokmamak.** $(3x)^2 = 9x^2$; $3x^2$ değil.

> **Paydada $x$ varken $x = 0$ yazmak.** $\left(x + \frac{2}{x}\right)^6$'da $x = 0$ yazılamaz; üssü 0'a eşitle.

## Kendini dene

### Soru 1
$(x + 1)^7$ açılımında $x^5$'li terimin katsayısı kaçtır?

A) 7
B) 21
C) 35
D) 42
E) 128

**Cevap:** B
**Çözüm:** Genel terim $C(7, r)\, x^{7 - r} \cdot 1^r$. $7 - r = 5 \Rightarrow r = 2$. Katsayı $C(7, 2) = \dfrac{7 \cdot 6}{2} = 21$. 35, $C(7, 3)$'tür (r'yi 3 almak); 42, ikiye bölmeyi unutan $7 \cdot 6$'dır; 128 ise katsayılar toplamı $2^7$'dir.

### Soru 2
$(2x - 3)^5$ açılımında katsayılar toplamı kaçtır?

A) $-1$
B) 0
C) 1
D) 32
E) 3125

**Cevap:** A
**Çözüm:** $x = 1$ yaz: $(2 - 3)^5 = (-1)^5 = -1$. 1, tek kuvvette eksiyi kaybetmektir; 32, $2^5$ kuralını yanlış yere uygulamaktır; 3125 ise işareti görmeyip $(2 + 3)^5$ hesaplamaktır.

### Soru 3
$\left(x^2 + \dfrac{1}{x}\right)^6$ açılımında sabit terim kaçtır?

A) 1
B) 6
C) 15
D) 20
E) 30

**Cevap:** C
**Çözüm:** Genel terim $C(6, r)\,(x^2)^{6 - r} \left(\dfrac{1}{x}\right)^r = C(6, r)\, x^{12 - 3r}$. $12 - 3r = 0 \Rightarrow r = 4$. Sabit terim $C(6, 4) = 15$. 20, ortadaki terimin ($r = 3$) katsayısıdır; o terim $20x^3$'tür, sabit değildir. 1, ilk terimin ($x^{12}$) katsayısıdır; sabit terim değildir.

## Özet kartı

- Pascal üçgeni: kenarlar 1, içteki her sayı üstteki iki komşunun toplamı; $n$. satır $C(n, 0), \dots, C(n, n)$, toplamı $2^n$.
- $(x + y)^n$ açılımında $n + 1$ terim var; her terimde üsler toplamı $n$.
- Baştan $(r + 1)$. terim: $C(n, r)\, x^{n - r}\, y^r$. İstenen üssü eşitleyip $r$'yi bul.
- $n$ çiftse ortadaki terim $r = \frac{n}{2}$; $n$ tekse tek bir ortadaki terim yok.
- Katsayılar toplamı: değişkenlere 1; sabit terim: değişkenlere 0 (paydada $x$ yoksa).
- Eksi işaretini ve katsayıyı kuvvetin içine al: $(-2)^r$, $(3x)^r$.

## Sonraki adım

Alıştırmaya geç (aşağıdaki düğme). Bu ders Sıralama ve Seçme konusunu bitirir. Sonraki ders: **Basit Olayların Olasılıkları**; bu konuda öğrendiğin sayma yolları orada olasılığın payını ve paydasını bulmak için kullanılacak.
