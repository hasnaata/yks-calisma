---
baslik: Polinomlarda Bölme İşlemi Yapmadan Kalan Bulma
ders: tyt-matematik
sure: 20 dk
kaynak: MEBİ Konu Özeti 4e318d2bb9
guncelleme: 2026-11-17
---
# Polinomlarda Bölme İşlemi Yapmadan Kalan Bulma

**Bu dersin sonunda:** bir polinomun $(x - a)$ ya da $(ax + b)$ ile bölümünden kalanı bölme yapmadan bulabilecek, kalan bilgisinden bilinmeyen katsayıları hesaplayabilecek ve bir sayının polinomun kökü olup olmadığını söyleyebileceksin.

> **TYT'de yeri:** Polinom sorularının en sık gelen kalıbı budur. "$P(x)$ polinomunun $(x - 2)$ ile bölümünden kalan kaçtır?", "$(x + 1)$ ile tam bölünüyorsa $a$ kaçtır?", "$P(x + 1)$ verilmiş, $P(x)$'in $(x - 3)$ ile bölümünden kalan kaçtır?" soruları tek satırda çözülür; uzun bölme yapan zaman kaybeder.

## Önce hatırla

<details><summary>Polinomlarda Bölme İşlemi dersinden: 5. dereceden bir polinom, 2. dereceden bir polinoma bölünüyor. Bölümün derecesi kaçtır, kalanın derecesi en çok kaç olabilir?</summary>
Bölümün derecesi $5 - 2 = $ <b>3</b>. Kalanın derecesi bölenin derecesinden küçük olmalı, yani en çok <b>1</b>. Bugün bunun en önemli sonucunu kullanacaksın: bölen birinci dereceden ise kalanın derecesi 0'dır, yani kalan <b>bir sayıdır</b>.
</details>

<details><summary>Polinomlarda Bölme İşlemi dersinden: P(x) polinomu x² + 1 ile bölününce bölüm x − 2, kalan 3x + 1 oluyor. P(x) nedir?</summary>
Bölme eşitliği: bölünen $=$ bölen $\cdot$ bölüm $+$ kalan. $P(x) = (x^2 + 1)(x - 2) + 3x + 1 = x^3 - 2x^2 + x - 2 + 3x + 1 = $ <b>$x^3 - 2x^2 + 4x - 1$</b>. Bu derste bölme eşitliğine bir $x$ değeri yazarak kalanı bölme yapmadan bulacaksın.
</details>

## 1. Kalan, $P(a)$'dır

**Örnek.** $P(x) = x^3 - 4x^2 + 2x + 5$ polinomunun $(x - 3)$ ile bölümünden kalan kaçtır?

Bölme yapsaydın bölüm $x^2 - x - 1$, kalan $2$ çıkardı. Ama bölmeye gerek yok. Bölen birinci dereceden olduğu için kalan bir sayıdır; ona $K$ de. Bölme eşitliği:

$$P(x) = (x - 3) \cdot B(x) + K$$

Bu eşitlik her $x$ için doğrudur. $x = 3$ yaz: $(3 - 3) = 0$ olduğu için $B(3)$ ne olursa olsun çarpım sıfırlanır.

$$P(3) = 0 \cdot B(3) + K \quad\Rightarrow\quad K = P(3)$$

$$P(3) = 27 - 36 + 6 + 5 = 2$$

Kalan **2**. Uzun bölmeyle aynı sonuç.

![Üç satır: üstte P(x) eşittir (x − 3) çarpı B(x) artı K. Ok ile x = 3 yaz. Ortada P(3) eşittir (3 − 3) çarpı B(3) artı K; (3 − 3) kırmızı kutuda ve altında 0 olur yazıyor. Altta yeşil kutuda P(3) eşittir K.](gorsel/tyt-matematik/13-04-bolme-esitligi.svg "Böleni sıfır yapan değeri yazınca bölüm kısmı tamamen silinir, yalnızca kalan kalır. B(x)'i bilmene gerek yoktur.")

**Kural.** $P(x)$ polinomunun $(x - a)$ ile bölümünden kalan $P(a)$'dır. Bölen $(x + a)$ ise $x = -a$ yazılır: kalan $P(-a)$.

> **Tuzak:** $(x + 2)$ ile bölümden kalan $P(2)$ değil, $P(-2)$'dir. Her zaman böleni **sıfıra eşitle**: $x + 2 = 0$, $x = -2$.

## 2. Bölen $(ax + b)$ ise

**Örnek.** $P(x) = 8x^3 - 2x + 7$ polinomunun $(2x - 1)$ ile bölümünden kalan kaçtır?

Böleni sıfır yapan değer: $2x - 1 = 0$, $x = \frac{1}{2}$.

$$P\left(\tfrac{1}{2}\right) = 8 \cdot \tfrac{1}{8} - 2 \cdot \tfrac{1}{2} + 7 = 1 - 1 + 7 = 7$$

Kalan **7**.

**Kural.** Bölen ne olursa olsun (birinci dereceden olduğu sürece) yöntem aynıdır: böleni sıfıra eşitle, bulduğun $x$ değerini $P(x)$'te yaz.

| Bölen | Yazılacak değer | Kalan |
|---|---|---|
| $x - 3$ | $x = 3$ | $P(3)$ |
| $x + 2$ | $x = -2$ | $P(-2)$ |
| $2x - 1$ | $x = \frac{1}{2}$ | $P\left(\frac{1}{2}\right)$ |
| $3x + 6$ | $x = -2$ | $P(-2)$ |
| $x$ | $x = 0$ | $P(0)$ = sabit terim |
| $x - 1$ | $x = 1$ | $P(1)$ = katsayılar toplamı |

Son iki satır Polinom Kavramı dersinden tanıdık: sabit terim, $x$ ile bölümden kalandır; katsayılar toplamı, $(x - 1)$ ile bölümden kalandır.

> **Tuzak:** $(2x - 1)$ için $x = 1$ ya da $x = 2$ yazmak. Değer $\frac{1}{2}$'dir. $(3x + 6)$ ile $(x + 2)$ aynı değeri verir: ikisi için de $x = -2$.

## 3. Kalan sıfırsa: çarpan ve kök

**Örnek.** $P(x) = x^3 - 4x^2 + x + 6$ polinomunun $(x - 2)$ ile bölümünden kalan kaçtır?

$$P(2) = 8 - 16 + 2 + 6 = 0$$

Kalan $0$, yani bölme eşitliği $P(x) = (x - 2) \cdot B(x)$ biçimine iner. Buna göre:

- $P(x)$, $(x - 2)$ ile **tam (kalansız) bölünür**,
- $(x - 2)$, $P(x)$'in bir **çarpanıdır**,
- $x = 2$, $P(x)$'in bir **kökü** (sıfırı) dır.

Bu üç cümle aynı şeyi söyler. Aynı polinomda $P(-1) = -1 - 4 - 1 + 6 = 0$ ve $P(3) = 27 - 36 + 3 + 6 = 0$ da çıkar. Bu yüzden $P(x) = (x + 1)(x - 2)(x - 3)$ olarak yazılabilir.

Kök, grafikte de görülür: $y = P(x)$ grafiği x eksenini köklerde keser. Kök olmayan bir $a$ için kalan $P(a)$, grafiğin $x = a$'daki yüksekliğidir.

![y = x³ − 4x² + x + 6 grafiği. Eğri x eksenini −1, 2 ve 3'te kesiyor (yeşil noktalar). x = 1'de eğrinin yüksekliği 4 (kırmızı nokta, kesikli çizgi). y eksenini 6'da kesiyor.](gorsel/tyt-matematik/13-04-grafik.svg "Yeşil noktalar kökler: oralarda kalan 0. Kırmızı nokta: (x − 1) ile bölümden kalan 4, yani P(1) = 4. P(0) = 6 ise sabit terim.")

**Kural.** $P(a) = 0 \iff (x - a)$, $P(x)$'in çarpanıdır $\iff$ $x = a$, $P(x)$'in köküdür.

![Akış şeması: Böleni sıfıra eşitle, x değerini bul, bu değeri P'de yaz. Sonuç 0 mı? Evet ise kalan 0, tam bölünür; bölen çarpan, x kök. Hayır ise sonuç kalandır.](gorsel/tyt-matematik/13-04-yontem.svg "Bütün kalan sorularında aynı üç adım. Sonuç sıfır çıkarsa soru aslında çarpan ya da kök sorusudur.")

## 4. Kalandan bilinmeyen bulma

**Örnek 1 (bir bilinmeyen).** $P(x) = x^3 + ax^2 - 5x + 6$ polinomu $(x - 2)$ ile tam bölünüyor. $a$ kaçtır?

Tam bölünüyor, yani $P(2) = 0$:

$$8 + 4a - 10 + 6 = 0 \quad\Rightarrow\quad 4a + 4 = 0 \quad\Rightarrow\quad a = -1$$

**Örnek 2 (iki bilinmeyen).** $P(x) = x^3 + ax + b$ polinomunun $(x - 1)$ ile bölümünden kalan 3'tür ve $P(x)$, $(x + 2)$ ile tam bölünmektedir. $a \cdot b$ kaçtır?

Her bilgi bir denklem verir:

- $(x - 1)$ ile kalan 3: $P(1) = 1 + a + b = 3$, yani $a + b = 2$.
- $(x + 2)$ ile tam bölünme: $P(-2) = -8 - 2a + b = 0$, yani $-2a + b = 8$.

Birinciden ikinciyi çıkar: $3a = -6$, $a = -2$. Sonra $b = 4$. Çarpım $a \cdot b = -8$.

Kontrol: $P(x) = x^3 - 2x + 4$; $P(1) = 1 - 2 + 4 = 3$ ve $P(-2) = -8 + 4 + 4 = 0$. Doğru.

**Kural.** "Kalan $k$" bilgisi $P(a) = k$, "tam bölünür", "çarpanıdır" ya da "köküdür" bilgisi $P(a) = 0$ denklemini verir. Kaç bilinmeyen varsa o kadar bilgi gerekir.

> **Tuzak:** $P(-2)$ hesaplarken üslerin işaretini karıştırmak. $(-2)^3 = -8$ ama $(-2)^2 = 4$. Tek kuvvette işaret kalır, çift kuvvette gider.

## 5. $P(x + k)$ verilen sorular

**Örnek 1.** $P(x + 1) = x^2 + 3x - 2$ olduğuna göre $P(x)$ polinomunun $(x - 4)$ ile bölümünden kalan kaçtır?

İstenen $P(4)$. Verilen eşitlikte parantezin **içi** 4 olmalı: $x + 1 = 4$, $x = 3$.

$$P(4) = 3^2 + 3 \cdot 3 - 2 = 16$$

**Örnek 2.** $P(x)$ polinomunun $(x - 3)$ ile bölümünden kalan 7'dir. $P(2x - 1)$ polinomunun $(x - 2)$ ile bölümünden kalan kaçtır?

Bölünen polinom $P(2x - 1)$, bölen $(x - 2)$. Böleni sıfır yapan $x = 2$ değeri **bölünen polinomun tamamına** yazılır: $P(2 \cdot 2 - 1) = P(3)$. $P(3)$ de $P(x)$'in $(x - 3)$ ile bölümünden kalandır, yani 7. Kalan **7**.

**Kural.** Önce hangi polinomun hangi bölene bölündüğünü yaz. Böleni sıfır yapan değeri, bölünen ifadenin içindeki her $x$'e yaz.

> **Tuzak:** $P(x + 1) = x^2 + 3x - 2$ verilince $P(4)$ için sağ tarafa $x = 4$ yazmak. Bu $P(5)$'i verir. İçi 4 yapan $x$ değerini bul.

## ÖSYM tuzakları

> **Böleni sıfıra eşitlemeyi atlamak:** $(x + 3)$ ile bölümden kalan $P(-3)$'tür, $P(3)$ değil. $(3x - 2)$ ile bölümden kalan $P\left(\frac{2}{3}\right)$'tür.

> **Kalanın derecesini unutmak:** Birinci dereceden bir bölenle kalan her zaman **sabit bir sayıdır**. Seçeneklerde $x$ içeren bir kalan varsa o seçenek yanlıştır.

> **"Kök", "çarpan", "tam bölünür" ifadelerini farklı sanmak:** Üçü de $P(a) = 0$ demektir. "$x = -1$ köküdür" bilgisi $(x + 1)$ çarpanıdır, yani $P(-1) = 0$ demektir.

> **İç içe polinomda sağ tarafa doğrudan yazmak:** $P(x - 2)$ verilmişse $P(1)$ için $x = 1$ değil, $x - 2 = 1$ olan $x = 3$ yazılır.

## Kendini dene

### Soru 1
$P(x) = 2x^3 - x^2 + 4x - 3$ polinomunun $(x + 1)$ ile bölümünden kalan kaçtır?

A) $-10$
B) $-8$
C) $-4$
D) $0$
E) $2$

**Cevap:** A
**Çözüm:** $x + 1 = 0$, $x = -1$. $P(-1) = 2 \cdot (-1) - 1 + 4 \cdot (-1) - 3 = -2 - 1 - 4 - 3 = -10$. $x = 1$ yazan $P(1) = 2$ bulur. $(-1)^2$'nin işaretini eksi alan $-8$ bulur.

### Soru 2
$P(x) = x^3 - 2x^2 + mx + 6$ polinomunun bir çarpanı $(x - 3)$ olduğuna göre $m$ kaçtır?

A) $-13$
B) $-7$
C) $-5$
D) $5$
E) $13$

**Cevap:** C
**Çözüm:** $(x - 3)$ çarpan ise $P(3) = 0$: $27 - 18 + 3m + 6 = 0$, $3m = -15$, $m = -5$. $P(-3) = 0$ yazan $-27 - 18 - 3m + 6 = 0$ ile $-13$ bulur. Son adımda işareti kaçıran $5$ bulur.

### Soru 3
$P(x + 2) = x^3 - 3x + 5$ olduğuna göre $P(x)$ polinomunun $(x - 1)$ ile bölümünden kalan kaçtır?

A) $1$
B) $3$
C) $5$
D) $7$
E) $23$

**Cevap:** D
**Çözüm:** İstenen $P(1)$. İçi 1 yap: $x + 2 = 1$, $x = -1$. $P(1) = (-1)^3 - 3 \cdot (-1) + 5 = -1 + 3 + 5 = 7$. Sağ tarafa $x = 1$ yazan $3$ bulur (bu $P(3)$'tür). $-3 \cdot (-1)$ işlemini $-3$ alan $1$ bulur.

## Özet kartı

- $P(x)$'in $(x - a)$ ile bölümünden kalan $P(a)$'dır; bölen $(ax + b)$ ise $P\left(-\frac{b}{a}\right)$.
- Her zaman önce böleni sıfıra eşitle, bulduğun değeri bölünen polinoma yaz.
- Birinci dereceden bölenle kalan her zaman bir sayıdır.
- $P(a) = 0$: tam bölünür, $(x - a)$ çarpandır, $x = a$ köktür.
- Her kalan bilgisi bir denklem; iki bilinmeyen için iki bilgi gerekir.
- $P(x + k)$ verilmişse parantezin içini istenen sayıya eşitle.

## Sonraki adım

Alıştırmaya geç (aşağıdaki düğme). Sonraki konu **Polinomların Çarpanlara Ayrılması**; bir kök bulunca polinomu çarpanlarına ayırmak için bu derste öğrendiğin "$P(a) = 0$ ise $(x - a)$ çarpandır" kuralını kullanacaksın.
