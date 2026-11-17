---
baslik: Basit Eşitsizlikler
ders: tyt-matematik
sure: 25 dk
kaynak: MEBİ Konu Özeti dc6e58d0e7
guncelleme: 2026-11-18
---
# Basit Eşitsizlikler

<div class="giris" dir="rtl" lang="ar">

**الدرس ده عن إيه؟** عن المتباينات البسيطة (basit eşitsizlikler): بتحلّها زي المعادلة بالظبط، بس فيه خطوات معيّنة بتقلب اتجاه العلامة.

- هتعرف إمتى اتجاه المتباينة بيتقلب، زي لما تضرب أو تقسم على عدد سالب (negatif sayı).
- هتحل المتباينة المزدوجة (çift taraflı eşitsizlik) وتعدّ الأعداد الصحيحة (tam sayılar) اللي بتحققها.
- هتتعلم لو عارف فترة (aralık) كل عدد، إزاي تطلع فترة المجموع والفرق وحاصل الضرب، وكمان فترة مقلوب العدد ومربعه.

**ليه مهم؟** في كل امتحان تجريبي لـ TYT بييجي سؤال واحد على الأقل من المتباينات، والفخ المشهور إنك تنسى تقلب العلامة.

٢٥ دقيقة، ومعاك رسومات على خط الأعداد وعلى الرسم البياني بتوضّح القواعد. خد وقتك وهتلاقيه أسهل ما إنت متخيّل.

</div>

**Bu dersin sonunda:** birinci dereceden bir eşitsizliği yönünü doğru koruyarak çözebilecek, verilen aralıklardan $a + b$, $a - b$, $a \cdot b$, $\frac{1}{x}$ ve $x^2$ ifadelerinin aralığını bulabileceksin.

> **TYT'de yeri:** Her denemede en az bir soru eşitsizlikten gelir. Kalıplar: "eşitsizliği sağlayan kaç tam sayı var?", "$a$ ve $b$ şu aralıklarda ise $2a - b$ hangi aralıktadır?", "$a < b < 0$ ise hangisi kesinlikle doğrudur?" ve "en az kaç km yol giderse ikinci firma daha ucuz olur?" gibi günlük hayat problemleri.

## Önce hatırla

<details><summary>Denklemlerden: $3(x - 2) + 5 = 2x + 7$ denkleminin kökü kaçtır?</summary>
Parantezi aç: $3x - 6 + 5 = 2x + 7$, yani $3x - 1 = 2x + 7$. Bilinmeyenleri bir tarafa topla: $x = 8$. Sağlama: $3 \cdot 6 + 5 = 23$ ve $2 \cdot 8 + 7 = 23$.
</details>

<details><summary>Denklemlerden: $(a - 3)x = a + 1$ denkleminin çözüm kümesi boş küme ise $a$ kaçtır?</summary>
$ax + b = 0$ biçiminde katsayı $0$, sabit $0$'dan farklı olursa çözüm yoktur. $a - 3 = 0$ için $a = 3$ ve sağ taraf $3 + 1 = 4 \ne 0$. Denklem $0 \cdot x = 4$ olur, çözüm kümesi $\varnothing$: <b>$a = 3$</b>.
</details>

## Eşitsizlik nedir?

$<$, $\le$, $>$, $\ge$ sembolleriyle kurulan ifadelere **eşitsizlik** denir. $a$ ve $b$ gerçek sayıyken $a < b$, $a \le b$, $a > b$, $a \ge b$ ifadeleri **basit eşitsizliktir**.

$a \ne 0$ olmak üzere $ax + b < 0$, $ax + b > 0$, $ax + b \le 0$, $ax + b \ge 0$ biçimindekiler **birinci dereceden bir bilinmeyenli eşitsizliklerdir**. Denklemin tek bir kökü vardı; eşitsizliğin çözümü ise bir **aralıktır**.

Eşitsizliği denklem gibi çözersin. Tek fark: **bazı işlemler yönü çevirir.** Hangileri olduğunu tek tek görelim.

## Toplama, çıkarma ve pozitifle çarpma

**Örnek.** $3x - 4 > 11$ eşitsizliğini çöz.

- İki tarafa $4$ ekle: $3x > 15$.
- İki tarafı $3$'e böl: $x > 5$.

Çözüm kümesi $(5, \infty)$. Kontrol: $x = 6$ için $14 > 11$ doğru; $x = 5$ için $11 > 11$ yanlış, yani $5$ dahil değil.

**Kural.** İki tarafa aynı sayıyı eklemek ya da çıkarmak yönü değiştirmez. İki tarafı **pozitif** bir sayıyla çarpmak ya da bölmek de yönü değiştirmez.

## Negatif sayıyla çarpma: yön döner

**Örnek.** $-3x + 4 \le 13$ eşitsizliğini çöz.

- İki taraftan $4$ çıkar: $-3x \le 9$.
- İki tarafı $-3$'e böl ve **yönü çevir**: $x \ge -3$.

Çözüm kümesi $[-3, \infty)$. Kontrol: $x = 0$ için $4 \le 13$ doğru. Yönü çevirmeseydin $x \le -3$ bulurdun; ama $x = -10$ için $34 \le 13$ yanlış.

Neden döner? $2 < 5$ doğrudur. İki tarafı $-1$ ile çarpınca sayılar sıfıra göre aynalanır: $-2$, $-5$'in **sağında** kalır.

![Sayı doğrusu: 2 ve 5 mavi noktalar, oklarla 0'a göre aynalanarak −2 ve −5 kırmızı noktalarına gidiyor. Altında 2 < 5 ve −2 > −5 yazıyor.](gorsel/tyt-matematik/03-03-yon-degisir.svg "−1 ile çarpmak sayıları 0'a göre aynalar. Büyük olan 5, aynada daha solda kalır; sıra tersine döner.")

**Kural.** İki tarafı **negatif** bir sayıyla çarpar ya da bölersen eşitsizliğin yönü değişir: $a < b$ ve $c < 0$ ise $a \cdot c > b \cdot c$.

**Paydalı örnek.** $\dfrac{x + 1}{3} - \dfrac{x - 2}{4} < 1$ eşitsizliğini çöz.

Paydaları eşitlemek için iki tarafı pozitif $12$ ile çarp (yön değişmez): $4(x + 1) - 3(x - 2) < 12$. Parantezleri aç: $4x + 4 - 3x + 6 < 12$, yani $x + 10 < 12$ ve $x < 2$.

## Çift taraflı eşitsizlik

**Örnek.** $-3 < 2x + 1 \le 9$ eşitsizliğini sağlayan kaç tam sayı vardır?

Üç tarafa da aynı işlemi uygula:

- $1$ çıkar: $-4 < 2x \le 8$.
- $2$'ye böl: $-2 < x \le 4$.

Tam sayılar $-1, 0, 1, 2, 3, 4$: **6 tane**.

![Sayı doğrusu: −2'de boş nokta, 4'te dolu nokta, arası boyalı. −1, 0, 1, 2, 3 ve 4 yeşil noktalarla işaretli.](gorsel/tyt-matematik/03-03-cift-esitsizlik.svg "−2 boş nokta olduğu için sayılmaz, 4 dolu nokta olduğu için sayılır.")

Negatif katsayı varsa yine üç tarafı da çevirirsin. $-1 \le 5 - 2x < 7$ için $5$ çıkar: $-6 \le -2x < 2$. $-2$'ye böl, iki işaret de döner: $3 \ge x > -1$. Küçük sayıyı sola alarak yaz: $-1 < x \le 3$.

**Kural.** Çift taraflı eşitsizlikte her işlem **üç tarafa birden** yapılır; negatif sayıya bölünce **iki işaret de** döner.

## İki eşitsizliği birleştirmek: $a + b$ ve $a - b$

**Örnek.** $2 < a < 5$ ve $-3 < b < 1$ ise $a + b$ ve $a - b$ hangi aralıktadır?

- **Toplam:** Yönleri aynı eşitsizlikler taraf tarafa toplanır: $2 + (-3) < a + b < 5 + 1$, yani $-1 < a + b < 6$.
- **Fark:** Taraf tarafa **çıkarma yapılmaz**. Önce $b$'yi $-1$ ile çarp (yön döner): $-1 < -b < 3$. Sonra topla: $2 + (-1) < a - b < 5 + 3$, yani $1 < a - b < 8$.

Taraf tarafa çıkarsaydın $2 - (-3) = 5$ ve $5 - 1 = 4$ bulurdun: "$5 < a - b < 4$" anlamsızdır.

**Çarpım.** $-2 < a < 3$ ve $1 < b < 4$ ise $a \cdot b$ için uçların dört çarpımını hesapla: $(-2) \cdot 1 = -2$, $(-2) \cdot 4 = -8$, $3 \cdot 1 = 3$, $3 \cdot 4 = 12$. En küçüğü ve en büyüğü alınır: $-8 < a \cdot b < 12$.

**Kural.** Toplamda uçlar toplanır. Farkta önce çıkarılanı $-1$ ile çarp, sonra topla. Çarpımda dört uç çarpımının en küçüğü ve en büyüğü sınırlardır.

## Ters alma: $\frac{1}{x}$

**Örnek.** $2 < x < 5$ ise $\frac{1}{x}$ hangi aralıktadır?

Payda büyüdükçe kesir küçülür: $x = 2$ iken $\frac{1}{2}$, $x = 5$ iken $\frac{1}{5}$. Yani $\frac{1}{5} < \frac{1}{x} < \frac{1}{2}$.

**Kural.**
- Aynı işaretli sayılarda ($0 < a < b$ ya da $a < b < 0$) ters alınca **yön döner**: $\frac{1}{a} > \frac{1}{b}$.
- Zıt işaretli sayılarda ($a < 0 < b$) **yön dönmez**: $\frac{1}{a} < 0 < \frac{1}{b}$, yani $\frac{1}{a} < \frac{1}{b}$.

## Kuvvet alma: $x^2$ ve $x^3$

**Örnek.** $-3 < -2$ eşitsizliğinde kare ve küp al.

- Kare: $(-3)^2 = 9$, $(-2)^2 = 4$ ve $9 > 4$. Yön **döndü**.
- Küp: $(-3)^3 = -27$, $(-2)^3 = -8$ ve $-27 < -8$. Yön **dönmedi**.

| Durum | Tek kuvvet ($x^3$) | Çift kuvvet ($x^2$) |
|---|---|---|
| $0 < a < b$ | $a^3 < b^3$ | $a^2 < b^2$ |
| $a < b < 0$ | $a^3 < b^3$ | $a^2 > b^2$ |

**Aralık sıfırı içeriyorsa.** $-3 < x < 2$ ise $x^2$ hangi aralıktadır? Uçların karesi $9$ ve $4$; ama $x = 0$ da aralıkta ve $0^2 = 0$. Kare hiç negatif olmaz, en küçük değer $0$'dır. En büyük değere en uzak uç ($-3$) yaklaştırır: $0 \le x^2 < 9$.

![y eşittir x kare grafiğinin x eksi 3 ile 2 arasındaki parçası. Uçlarda (−3, 9) ve (2, 4) boş noktalar, tepe (0, 0) yeşil. y ekseninde 0'dan 9'a kırmızı boyalı aralık.](gorsel/tyt-matematik/03-03-kare-araligi.svg "x, −3 ile 2 arasında gezerken x² değeri 0'dan başlar, 9'a yaklaşır ama ulaşmaz. 4 sınır değildir.")

**Kural.** $0 < a < b$ ise $a^n < b^n$. $a < b < 0$ ise tek kuvvette yön korunur, çift kuvvette döner. Aralık $0$'ı içeriyorsa çift kuvvetin en küçük değeri $0$'dır.

## ÖSYM tuzakları

> **Negatife bölüp yönü unutmak:** $-2x > 6$ ise $x < -3$'tür, $x > -3$ değil. Böldüğün sayının işaretine her seferinde bak.

> **Taraf tarafa çıkarmak:** $2 < a < 5$ ve $-3 < b < 1$ için $a - b$ aralığını uçları çıkararak bulamazsın. Önce $-b$ aralığını yaz, sonra topla: $1 < a - b < 8$.

> **Sıfırı atlamak:** $-3 < x < 2$ için "$4 < x^2 < 9$" yanlıştır; $x = 0$ alınabildiği için $0 \le x^2 < 9$ olur. Aynı şekilde $-2 < x < 3$ için $\frac{1}{x}$, $-\frac{1}{2}$ ile $\frac{1}{3}$ arasında **değildir**: $x$ sıfıra yaklaştıkça $\frac{1}{x}$ sınırsız büyür ya da küçülür.

> **Paydalıda işareti dağıtmamak:** $-\dfrac{x - 2}{4}$ terimi paydadan kurtulunca $-3(x - 2) = -3x + 6$ olur, $-3x - 6$ değil.

## Kendini dene

### Soru 1
$-2x + 7 \ge 1$ eşitsizliğinin çözüm kümesi aşağıdakilerden hangisidir?

A) $(-\infty, -3]$
B) $[-3, \infty)$
C) $(-\infty, 3]$
D) $[3, \infty)$
E) $(3, \infty)$

**Cevap:** C
**Çözüm:** İki taraftan $7$ çıkar: $-2x \ge -6$. $-2$'ye böl ve yönü çevir: $x \le 3$. $3$ dahil (eşitlik var): $(-\infty, 3]$. Yönü çevirmeyen D'yi, işareti karıştıran A'yı bulur.

### Soru 2
$1 < x < 4$ olduğuna göre $2x - 5$ ifadesinin alabileceği kaç farklı tam sayı değeri vardır?

A) 2
B) 3
C) 4
D) 5
E) 6

**Cevap:** D
**Çözüm:** $2$ ile çarp: $2 < 2x < 8$. $5$ çıkar: $-3 < 2x - 5 < 3$. Tam sayı değerleri $-2, -1, 0, 1, 2$: 5 tane. Burada $x$ gerçek sayıdır; sayılan, $x$'in değil $2x - 5$'in tam sayı değerleridir.

### Soru 3
$2 < a < 6$ ve $-1 < b < 3$ olduğuna göre $a - b$ hangi aralıktadır?

A) $(-1, 3)$
B) $(-1, 7)$
C) $(1, 5)$
D) $(1, 9)$
E) $(3, 7)$

**Cevap:** B
**Çözüm:** $b$'yi $-1$ ile çarp, yön döner: $-3 < -b < 1$. Taraf tarafa topla: $2 + (-3) < a - b < 6 + 1$, yani $-1 < a - b < 7$. Uçları doğrudan çıkaran $2 - (-1) = 3$ ve $6 - 3 = 3$ bulur ve takılır.

## Özet kartı

- Toplama, çıkarma, pozitifle çarpma ve bölme yönü değiştirmez; **negatifle çarpma ve bölme yönü çevirir**.
- Çift taraflı eşitsizlikte işlem üç tarafa birden yapılır.
- Aynı yönlü eşitsizlikler toplanır; fark için önce $-b$ aralığını yaz, sonra topla.
- Çarpımda dört uç çarpımına bak; en küçüğü ve en büyüğü sınırlardır.
- Aynı işaretlilerde ters alınca yön döner; zıt işaretlilerde dönmez.
- Aralık $0$'ı içeriyorsa $x^2$'nin en küçük değeri $0$'dır.

## Sonraki adım

Alıştırmaya geç (aşağıdaki düğme). Sonraki ders **Birinci Dereceden İki Bilinmeyenli Denklemler**. Eşitsizlik cevaplarını hep aralık gösterimiyle yaz; mutlak değer ve problem konularında bu adımları sürekli kullanacaksın.
