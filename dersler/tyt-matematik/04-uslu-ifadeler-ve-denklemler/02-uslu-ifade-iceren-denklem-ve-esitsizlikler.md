---
baslik: Üslü İfade İçeren Denklem ve Eşitsizlikler
ders: tyt-matematik
sure: 20 dk
kaynak: MEBİ Konu Özeti 1b30d425e4
guncelleme: 2026-11-17
---
# Üslü İfade İçeren Denklem ve Eşitsizlikler

**Bu dersin sonunda:** bilinmeyeni üste olan bir denklemi tabanları eşitleyerek çözebilecek, $x^n = y^n$ ve $a^b = 1$ denklemlerindeki bütün durumları yakalayabilecek ve üslü bir eşitsizliği tabanın 1'den büyük ya da küçük olmasına göre doğru yönde çözebileceksin.

> **TYT'de yeri:** Her yıl üslü ifadelerden 1–2 soru gelir. Kalıplar: "$x$ kaçtır?" (tabanları eşitle), "$x$'in alabileceği değerlerin toplamı" ($a^b = 1$ ya da çift kuvvet), "eşitsizliği sağlayan kaç tam sayı var?" ve büyüme ya da katlanma gibi günlük hayat durumları.

## Önce hatırla

<details><summary>Üslü ifadeler ve özelliklerinden: $\dfrac{8^3 \cdot 4^{-2}}{2^5}$ işleminin sonucu kaçtır?</summary>
Hepsini 2 tabanına çevir: $8^3 = 2^9$, $4^{-2} = 2^{-4}$. Pay $2^{9 + (-4)} = 2^5$. Sonuç $\dfrac{2^5}{2^5} = 2^0 = $ <b>1</b>.
</details>

<details><summary>Üslü ifadeler ve özelliklerinden: $a = 2^{30}$, $b = 3^{20}$, $c = 5^{10}$ sayılarını sırala.</summary>
Üsleri eşitle: $a = (2^3)^{10} = 8^{10}$, $b = (3^2)^{10} = 9^{10}$, $c = 5^{10}$. Üsler eşit ve tabanlar pozitif olduğundan tabanı büyük olan büyüktür: <b>$c < a < b$</b>.
</details>

## Tabanları eşitle, üsleri eşitle

**Örnek.** $4^{x+1} = 8^{x-1}$ denklemini çöz.

İki taban da 2'nin kuvveti: $4 = 2^2$, $8 = 2^3$.

$$\left(2^2\right)^{x+1} = \left(2^3\right)^{x-1} \;\Rightarrow\; 2^{2x+2} = 2^{3x-3}$$

Tabanlar aynı, öyleyse üsler de aynı: $2x + 2 = 3x - 3$, yani $x = 5$.
Kontrol: $4^6 = 2^{12}$ ve $8^4 = 2^{12}$.

**Örnek.** $\left(\frac{1}{9}\right)^{x} = 27^{x-5}$ denklemini çöz.

Kesirli tabanı negatif üsle yaz: $\frac{1}{9} = 3^{-2}$ ve $27 = 3^3$.

$$3^{-2x} = 3^{3x-15} \;\Rightarrow\; -2x = 3x - 15 \;\Rightarrow\; x = 3$$

**Kural.** $a \notin \{-1, 0, 1\}$ olmak üzere $a^m = a^n$ ise $m = n$ olur. Yöntem hep aynıdır: iki tarafı **aynı tabana** çevir, sonra üsleri eşitle. Ondalık ve kesirli sayıları da önce bu tabana çevir ($0{,}25 = 2^{-2}$, $\frac{1}{125} = 5^{-3}$).

**Neden $-1$, $0$, $1$ hariç?** $1^{2} = 1^{7}$ doğrudur ama $2 = 7$ değildir. $1$'in her kuvveti $1$, $0$'ın her pozitif kuvveti $0$'dır; $(-1)^2 = (-1)^4$ olur. Bu tabanlarda üsleri eşitleyemezsin.

### Toplam varsa önce ortak paranteze al

**Örnek.** $3^{x+2} + 3^{x} = 90$ denklemini çöz.

$3^{x+2} = 3^x \cdot 9$ olduğundan $3^x$ ortak çarpandır:

$$3^x \,(9 + 1) = 90 \;\Rightarrow\; 3^x = 9 \;\Rightarrow\; x = 2$$

Toplanan terimlerin üslerini **toplayamazsın**: $3^{x+2} + 3^x \ne 3^{2x+2}$. Önce en küçük kuvveti ortak paranteze al.

## Üsler eşitse: tek mi çift mi?

**Örnek (tek kuvvet).** $(2a - 1)^5 = (a + 3)^5$ ise $a$ kaçtır?

Tek kuvvet işareti korur, her sayının tek bir beşinci kuvveti vardır. Öyleyse tabanlar eşittir: $2a - 1 = a + 3$, $a = 4$.

**Örnek (çift kuvvet).** $(x - 1)^6 = 64$ denkleminin köklerini bul.

$64 = 2^6$. Ama $(-2)^6$ de $64$'tür. İki durum var:

- $x - 1 = 2 \Rightarrow x = 3$
- $x - 1 = -2 \Rightarrow x = -1$

Çözüm kümesi $\{-1, 3\}$.

![İki grafik yan yana. Solda y eşittir x küp eğrisi ile y eşittir 8 doğrusu yalnızca x eşittir 2'de kesişiyor. Sağda y eşittir x üzeri 4 eğrisi ile y eşittir 16 doğrusu x eşittir eksi 2 ve 2'de, iki noktada kesişiyor.](gorsel/tyt-matematik/04-02-tek-cift-kuvvet.svg "Tek kuvvette yatay doğru eğriyi bir kez keser, tek kök vardır. Çift kuvvette eğri iki yana simetrik açılır, birbirinin ters işaretlisi iki kök çıkar.")

**Kural.** $n$ pozitif tam sayı olmak üzere $x^n = y^n$ ise

| $n$ | Sonuç | Örnek |
|---|---|---|
| Tek | $x = y$ | $x^3 = (-2)^3 \Rightarrow x = -2$ |
| Çift | $\lvert x \rvert = \lvert y \rvert$, yani $x = y$ ya da $x = -y$ | $x^4 = 3^4 \Rightarrow x = 3$ ya da $x = -3$ |

**Örnek.** $(2x - 3)^4 = (x + 3)^4$ denkleminin kökleri: $2x - 3 = x + 3$ ise $x = 6$; $2x - 3 = -(x + 3)$ ise $3x = 0$, $x = 0$. Çözüm kümesi $\{0, 6\}$.

## $a^b = 1$ denklemi: üç durum

**Örnek.** $(x - 3)^{x+2} = 1$ denklemini sağlayan $x$ değerlerini bul.

Bir üslü ifade üç yoldan $1$ olabilir. Hepsini sırayla dene:

1. **Üs sıfır:** $x + 2 = 0 \Rightarrow x = -2$. Taban $-5$, sıfır değil. $(-5)^0 = 1$. Geçerli.
2. **Taban bir:** $x - 3 = 1 \Rightarrow x = 4$. $1^6 = 1$. Geçerli.
3. **Taban eksi bir:** $x - 3 = -1 \Rightarrow x = 2$. Üs $4$, çift. $(-1)^4 = 1$. Geçerli.

Çözüm kümesi $\{-2, 2, 4\}$, elemanların toplamı $4$.

![Akış şeması: a üzeri b eşittir 1 denklemi üç dala ayrılıyor. Taban 1 ise kök geçerli. Üs 0 ise tabanın sıfır olup olmadığına bakılıyor; sıfırsa kök atılır. Taban eksi 1 ise üssün çift olup olmadığına bakılıyor; çift değilse kök atılır.](gorsel/tyt-matematik/04-02-bir-esitligi.svg "Üç dalın üçünü de dene. Üs sıfır dalında tabanı, taban eksi bir dalında üssü kontrol etmeden kökü yazma.")

**Kural.** $a^b = 1$ ise:

| Durum | Ek koşul | Neden |
|---|---|---|
| $b = 0$ | $a \ne 0$ | $0^0$ tanımsızdır |
| $a = 1$ | yok | $1$'in her kuvveti $1$ |
| $a = -1$ | $b$ çift tam sayı | $(-1)^{\text{tek}} = -1$ |

**Örnek (ek koşul işe yarıyor).** $(x - 2)^{x-2} = 1$.
Üs sıfır: $x = 2$, ama taban da $0$ olur: $0^0$ tanımsız, **atılır**. Taban bir: $x = 3$, geçerli. Taban eksi bir: $x = 1$, üs $-1$ tek: $(-1)^{-1} = -1$, **atılır**. Tek kök $x = 3$.

## Üslü eşitsizlikler: taban yönü belirler

**Örnek (taban 1'den büyük).** $3^{2x-1} > 27$.

$27 = 3^3$: $3^{2x-1} > 3^3$. Taban $3 > 1$ olduğundan büyük olanın üssü de büyüktür: $2x - 1 > 3$, $x > 2$. Çözüm kümesi $(2, \infty)$.

**Örnek (taban 0 ile 1 arasında).** $\left(\frac{1}{2}\right)^{x+1} \ge \frac{1}{8}$.

$\frac{1}{8} = \left(\frac{1}{2}\right)^3$: $\left(\frac{1}{2}\right)^{x+1} \ge \left(\frac{1}{2}\right)^3$. Taban 1'den küçük; bu tabanda **üs büyüdükçe değer küçülür**. Bu yüzden yön döner: $x + 1 \le 3$, $x \le 2$. Çözüm kümesi $(-\infty, 2]$.

Kontrol: $x = 0$ için $\left(\frac{1}{2}\right)^1 = \frac{1}{2} \ge \frac{1}{8}$, doğru. $x = 5$ için $\left(\frac{1}{2}\right)^6 = \frac{1}{64} < \frac{1}{8}$, sağlamaz.

![İki grafik yan yana. Solda y eşittir 2 üzeri x artan eğri; x eşittir 1'de 2, x eşittir 3'te 8. Sağda y eşittir yarım üzeri x azalan eğri; x eşittir eksi 3'te 8, x eşittir eksi 1'de 2.](gorsel/tyt-matematik/04-02-artan-azalan.svg "Solda üs 1'den 3'e çıkınca değer 2'den 8'e çıkıyor. Sağda üs −3'ten −1'e çıkınca değer 8'den 2'ye iniyor. Taban 1'den küçükse üsler arasındaki eşitsizliğin yönü ters döner.")

**Kural.** $a^m < a^n$ eşitsizliğinde

| Taban | Üsler için |
|---|---|
| $a > 1$ | $m < n$ (yön aynı) |
| $0 < a < 1$ | $m > n$ (yön döner) |

**Kısa yol:** Tabanı 1'den büyük yap, yön derdi kalmasın. $\left(\frac{1}{5}\right)^{x} \le 25^{x-3}$ eşitsizliğinde $\frac{1}{5} = 5^{-1}$, $25 = 5^2$ yaz: $5^{-x} \le 5^{2x-6}$. Taban $5 > 1$, yön aynı kalır: $-x \le 2x - 6$, $x \ge 2$.

## ÖSYM tuzakları

> **Tabanı 1 ya da −1 iken üsleri eşitlemek:** $1^{x+4} = 1^{2x}$ eşitliği her $x$ için doğrudur; "$x + 4 = 2x$, $x = 4$" demek yanlıştır. Üsleri eşitlemeden önce tabanın $-1$, $0$, $1$ olmadığına bak.

> **Çift kuvvette negatif kökü unutmak:** $(x - 1)^6 = 64$ için yalnızca $x = 3$ yazarsan $x = -1$ kaybolur; "değerler toplamı" sorusunda cevap $2$ yerine $3$ çıkar.

> **$a^b = 1$'de bir durumu atlamak ya da kontrolsüz almak:** $a = -1$ durumunu unutmak kök kaçırır; $b = 0$ durumunda tabanı, $a = -1$ durumunda üssün çiftliğini kontrol etmemek fazla kök ekler ($0^0$ tanımsızdır).

> **Taban 1'den küçükken yönü çevirmemek:** $\left(\frac{1}{3}\right)^x > \frac{1}{9}$ için cevap $x > 2$ değil, $x < 2$'dir. Şüphedeysen bir sayı koyup dene.

> **Toplamda üsleri toplamak:** $2^x + 2^x = 2^{x+1}$'dir, $2^{2x}$ değil. $4^x + 4^x + 4^x + 4^x = 4 \cdot 4^x = 4^{x+1}$.

## Kendini dene

### Soru 1
$9^{x-1} = 27^{x-3}$ olduğuna göre $x$ kaçtır?

A) 1
B) 2
C) 4
D) 7
E) 9

**Cevap:** D
**Çözüm:** $9 = 3^2$, $27 = 3^3$: $3^{2(x-1)} = 3^{3(x-3)}$, yani $2x - 2 = 3x - 9$, $x = 7$. Kontrol: $9^6 = 3^{12}$ ve $27^4 = 3^{12}$. Üsleri parantezle çarpmayı unutup $2x - 1 = 3x - 3$ yazan $2$ bulur.

### Soru 2
$(x + 1)^{x-4} = 1$ denklemini sağlayan $x$ değerlerinin toplamı kaçtır?

A) −2
B) 0
C) 2
D) 4
E) 6

**Cevap:** C
**Çözüm:** Üs sıfır: $x = 4$, taban $5 \ne 0$, geçerli. Taban bir: $x + 1 = 1$, $x = 0$, geçerli. Taban eksi bir: $x = -2$, üs $-6$ çift, $(-1)^{-6} = 1$, geçerli. Toplam $4 + 0 + (-2) = 2$. $-1$ durumunu unutan $4 + 0 = 4$ bulur.

### Soru 3
$\left(\frac{1}{3}\right)^{x-2} > 9^{x-5}$ eşitsizliğini sağlayan en büyük $x$ tam sayısı kaçtır?

A) 2
B) 3
C) 4
D) 5
E) 6

**Cevap:** B
**Çözüm:** 3 tabanına çevir: $3^{-(x-2)} > 3^{2(x-5)}$, yani $3^{-x+2} > 3^{2x-10}$. Taban $3 > 1$, yön aynı: $-x + 2 > 2x - 10$, $12 > 3x$, $x < 4$. En büyük tam sayı $3$. $x = 4$ eşitliği verir, eşitsizliği sağlamaz.

## Özet kartı

- Bilinmeyen üsteyse iki tarafı aynı tabana çevir, üsleri eşitle (taban $-1$, $0$, $1$ olmasın).
- Toplam varsa önce en küçük kuvveti ortak paranteze al.
- $x^n = y^n$: $n$ tekse $x = y$; $n$ çiftse $x = y$ ya da $x = -y$.
- $a^b = 1$: $b = 0$ ($a \ne 0$), $a = 1$, $a = -1$ ($b$ çift). Üçünü de dene.
- Eşitsizlikte taban $> 1$ ise yön aynı, $0 <$ taban $< 1$ ise yön döner.

## Sonraki adım

Alıştırmaya geç (aşağıdaki düğme). Gerçek çıkmış soruları görmek için MEBİ'deki bu konunun "Çıkmış Sorular" testini ve ÖSYM'nin yayımladığı TYT kitapçıklarını kullan. Sonraki ders **Köklü İfadeler ve Özellikleri**; köklü sayıları kesirli üs olarak yazınca bu dersteki tabanı eşitleme yöntemini orada da kullanacaksın.
