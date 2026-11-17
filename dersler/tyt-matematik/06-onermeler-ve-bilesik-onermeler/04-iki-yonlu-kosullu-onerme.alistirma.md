---
baslik: İki Yönlü Koşullu Önerme · Alıştırma
ders: tyt-matematik
soru: 12
guncelleme: 2026-11-17
---
# Alıştırma: İki Yönlü Koşullu Önerme

Sorular özgündür ve ÖSYM soru tarzında yazılmıştır. Derse bakmadan çöz.

## Isınma

### Soru 1 · Kolay
$p \equiv 1$ ve $q \equiv 0$ olduğuna göre aşağıdaki önermelerden hangisinin doğruluk değeri 1'dir?

A) $p \Leftrightarrow q$
B) $p' \Leftrightarrow q'$
C) $p \Leftrightarrow q'$
D) $q \Leftrightarrow p$
E) $(p \Leftrightarrow q') \Leftrightarrow q$

**Cevap:** C
**Çözüm:** İki tarafı aynı olanı ara. C) $p \Leftrightarrow q' \equiv 1 \Leftrightarrow 1 \equiv 1$. Diğerleri: A) $1 \Leftrightarrow 0 \equiv 0$; B) $0 \Leftrightarrow 1 \equiv 0$; D) $0 \Leftrightarrow 1 \equiv 0$; E) önce $p \Leftrightarrow q' \equiv 1$, sonra $1 \Leftrightarrow 0 \equiv 0$. B'yi seçen, iki tarafı birden değillemenin sonucu değiştirdiğini sanmıştır.

### Soru 2 · Kolay
- $p$: "Üçgen eşkenardır."
- $q$: "Üçgenin üç açısı eşittir."

önermeleri veriliyor. Buna göre $p \Leftrightarrow q$ önermesi aşağıdakilerden hangisidir?

A) Üçgen eşkenardır ancak ve ancak üç açısı eşittir.
B) Üçgen eşkenarsa üç açısı eşittir.
C) Üçgenin üç açısı eşitse üçgen eşkenardır.
D) Üçgen eşkenardır ve üç açısı eşittir.
E) Üçgen eşkenardır ancak ve ancak üç açısı eşit değildir.

**Cevap:** A
**Çözüm:** $\Leftrightarrow$ işareti "ancak ve ancak" diye okunur: A. B yalnızca $p \Rightarrow q$, C yalnızca $q \Rightarrow p$ yönüdür; $p \Leftrightarrow q$ bu ikisinin birlikte doğru olmasıdır. D, $p \wedge q$ önermesidir. E'de $q$ değillenmiştir: $p \Leftrightarrow q'$.

### Soru 3 · Kolay
$(p \Leftrightarrow p') \Leftrightarrow q$ önermesi aşağıdakilerden hangisine denktir?

A) $0$
B) $1$
C) $q$
D) $q'$
E) $p$

**Cevap:** D
**Çözüm:** Bir önerme değiliyle hiç aynı olmaz: $p \Leftrightarrow p' \equiv 0$. Geriye $0 \Leftrightarrow q$ kalır. $q \equiv 0$ ise $0 \Leftrightarrow 0 \equiv 1$, $q \equiv 1$ ise $0 \Leftrightarrow 1 \equiv 0$; sonuç $q'$. C'yi seçen $0 \Leftrightarrow q$'yu $1 \Leftrightarrow q \equiv q$ ile karıştırmıştır. A'yı seçen, ilk parçanın 0 olmasının bütün önermeyi 0 yaptığını sanmıştır; bu yalnızca "ve" bağlacında olur.

## Orta

### Soru 4 · Orta
$(p \Leftrightarrow q) \vee p$ önermesi aşağıdakilerden hangisine denktir?

A) $p \Rightarrow q$
B) $q \Rightarrow p$
C) $p \vee q$
D) $p' \vee q$
E) $1$

**Cevap:** B
**Çözüm:** $p$'ye göre iki durum incele. $p \equiv 1$ ise "veya" kesin 1. $p \equiv 0$ ise $(0 \Leftrightarrow q) \vee 0 \equiv q'$. Sonuç: $p \equiv 1$ iken 1, $p \equiv 0$ iken $q'$; bu $p \vee q'$ demektir. $p \vee q' \equiv q' \vee p \equiv q \Rightarrow p$. A ve D birbirine denktir ($p \Rightarrow q \equiv p' \vee q$); yön ters alınmıştır. C'de $q$'nun değili unutulmuştur. E, $p \equiv 0$, $q \equiv 1$ durumunda sonucun 0 olduğunu gözden kaçırır.

### Soru 5 · Orta
$(p \Leftrightarrow q') \Rightarrow (r \Leftrightarrow q)$ önermesinin doğruluk değeri 0'dır.

Buna göre aşağıdakilerden hangisi **kesinlikle** doğrudur?

A) $p \equiv 1$
B) $q \equiv 0$
C) $r \equiv 1$
D) $p \Leftrightarrow q \equiv 1$
E) $p \Leftrightarrow r \equiv 1$

**Cevap:** E
**Çözüm:** "İse" yanlışsa hipotez 1, hüküm 0'dır.
1. $p \Leftrightarrow q' \equiv 1$: $p$ ile $q'$ aynı, yani $p$ ile $q$ farklı.
2. $r \Leftrightarrow q \equiv 0$: $r$ ile $q$ farklı.

İki çözüm vardır: $q \equiv 0$ ise $p \equiv 1$, $r \equiv 1$; $q \equiv 1$ ise $p \equiv 0$, $r \equiv 0$. A, B, C yalnızca birinci çözümde doğrudur, kesin değildir. İkisi de $q$'dan farklı olduğu için $p$ ile $r$ her durumda aynıdır: $p \Leftrightarrow r \equiv 1$. D ise her iki çözümde de 0'dır.

### Soru 6 · Orta
$x$ bir tam sayı olmak üzere aşağıdaki önermeler veriliyor.

- I. $x = 2 \Leftrightarrow x + 3 = 5$
- II. $x^2 = 16 \Leftrightarrow x = 4$
- III. "$x$ çift sayıdır" $\Leftrightarrow$ "$x + 1$ tek sayıdır"
- IV. $x > 3 \Leftrightarrow x > 5$

Bu önermelerden hangileri her $x$ tam sayısı için doğrudur (çift gerektirmedir)?

A) I ve III
B) I ve II
C) II ve IV
D) I, II ve III
E) I, III ve IV

**Cevap:** A
**Çözüm:** Her önermede iki yönü ayrı sına; tek karşı örnek önermeyi bozar.
- I: $x + 3 = 5$ yalnızca $x = 2$ iken doğrudur; iki taraf hep aynı değerdedir. Doğru.
- II: $x = -4$ için $x^2 = 16$ doğru, $x = 4$ yanlış. Yanlış.
- III: $x$ çiftse $x + 1$ tektir; $x + 1$ tekse $x$ çifttir. Doğru.
- IV: $x = 4$ için $x > 3$ doğru, $x > 5$ yanlış. Yanlış.

II'yi seçen yalnızca $x = 4 \Rightarrow x^2 = 16$ yönüne bakmıştır. IV'ü seçen yalnızca $x > 5 \Rightarrow x > 3$ yönüne bakmıştır.

### Soru 7 · Orta
$(p \Rightarrow q) \wedge (p' \Rightarrow q')$ önermesi aşağıdakilerden hangisine denktir?

A) $p \Rightarrow q$
B) $q \Rightarrow p$
C) $p \wedge q$
D) $p \Leftrightarrow q$
E) $p \Leftrightarrow q'$

**Cevap:** D
**Çözüm:** $p' \Rightarrow q'$ önermesi $p \Rightarrow q$'nun tersidir ve karşıtına denktir: $p' \Rightarrow q' \equiv q \Rightarrow p$ (kontrol: $p' \Rightarrow q' \equiv p \vee q' \equiv q' \vee p \equiv q \Rightarrow p$). Böylece önerme $(p \Rightarrow q) \wedge (q \Rightarrow p) \equiv p \Leftrightarrow q$ olur. A ya da B'yi seçen yalnızca bir parçayı görmüştür. C, $p \equiv 0$, $q \equiv 0$ durumunu kaçırır; orada önerme $1 \wedge 1 \equiv 1$'dir. E bunun değilidir.

## ÖSYM tarzı

### Soru 8 · ÖSYM tarzı
Bir sitenin otopark bariyeri şu kurala göre çalışacak biçimde ayarlanmıştır:

"Bariyer **ancak ve ancak** aracın plakası sistemde kayıtlıysa açılır."

Bir sabah bariyere gelen altı aracın durumu tabloda verilmiştir.

| Araç | Plaka kayıtlı mı? | Bariyer |
|---|---|---|
| 1. araç | Evet | Açıldı |
| 2. araç | Evet | Açılmadı |
| 3. araç | Hayır | Açıldı |
| 4. araç | Hayır | Açılmadı |
| 5. araç | Evet | Açılmadı |
| 6. araç | Evet | Açıldı |

Buna göre bariyer kaç araçta kurala aykırı çalışmıştır?

A) 1
B) 2
C) 3
D) 4
E) 5

**Cevap:** C
**Çözüm:** $p$: "Plaka kayıtlı", $q$: "Bariyer açıldı". Kural $p \Leftrightarrow q$; iki tarafın farklı olduğu her araçta kural bozulur.
- Kayıtlı ama açılmadı ($1, 0$): 2. ve 5. araç.
- Kayıtsız ama açıldı ($0, 1$): 3. araç.

Toplam **3** araç. Yalnızca "kayıtlıysa açılır" yönünü sınayan 2, yalnızca "açıldıysa kayıtlıdır" yönünü sınayan 1 bulur. 4. araçta ikisi de 0'dır; $0 \Leftrightarrow 0 \equiv 1$, kural işlemiştir.

### Soru 9 · ÖSYM tarzı
Bir merdivenin altında ve üstünde birer anahtar bulunan bir lamba vardır.

- $p$: "Alttaki anahtar yukarı konumdadır."
- $q$: "Üstteki anahtar yukarı konumdadır."

Lamba, **ancak ve ancak** iki anahtar aynı konumdayken yanmaktadır.

Buna göre lambanın **sönük** olduğu durumları ifade eden önerme aşağıdakilerden hangisidir?

A) $p \Leftrightarrow q'$
B) $p' \Leftrightarrow q'$
C) $p \wedge q'$
D) $p' \wedge q$
E) $p \Rightarrow q'$

**Cevap:** A
**Çözüm:** Lamba yanıyor: $p \Leftrightarrow q$. Sönük: $(p \Leftrightarrow q)'$. Tek bir tarafı değille: $(p \Leftrightarrow q)' \equiv p \Leftrightarrow q'$. Kontrol: anahtarlar farklı ($1, 0$ ya da $0, 1$) iken $p$ ile $q'$ aynıdır, sonuç 1. B'de iki değil vardır; $p \Leftrightarrow q$'ya, yani lambanın yandığı durumlara denktir. C yalnızca "alt yukarı, üst aşağı", D yalnızca "alt aşağı, üst yukarı" durumunu kapsar; ikisi de sönük durumların yarısıdır. E, iki anahtar da aşağıdayken ($0, 0$) 1 olur ama lamba o anda yanıyordur.

### Soru 10 · ÖSYM tarzı
$p$, $q$ ve $r$ önermeleri için

$$(p \vee q) \Leftrightarrow (q \wedge r)$$

önermesinin doğruluk değeri 0'dır.

Buna göre $(p, q, r)$ doğruluk değerleri üçlüsü kaç farklı biçimde olabilir?

A) 3
B) 4
C) 5
D) 6
E) 7

**Cevap:** B
**Çözüm:** İki taraf farklı olmalı. $q \wedge r \equiv 1$ ise $q \equiv 1$, o zaman $p \vee q \equiv 1$ olur ve iki taraf aynı çıkar. Bu yüzden tek olasılık $p \vee q \equiv 1$, $q \wedge r \equiv 0$.
- $p \vee q \equiv 1$ olan $(p, q)$ çiftleri: $(1, 1)$, $(1, 0)$, $(0, 1)$. Her biri için $r$ iki değer alabilir: $3 \cdot 2 = 6$ üçlü.
- Bunlardan $q \wedge r \equiv 1$ olanlar ($q \equiv 1$, $r \equiv 1$): $(1, 1, 1)$ ve $(0, 1, 1)$. Çıkar: $6 - 2 = 4$.

Üçlüler: $(1, 1, 0)$, $(1, 0, 1)$, $(1, 0, 0)$, $(0, 1, 0)$. $q \wedge r \equiv 1$ olanları çıkarmayı unutan 6 bulur. Yalnızca $(p, q)$ çiftlerini sayıp $r$'yi unutan 3 bulur.

### Soru 11 · ÖSYM tarzı
$p$ ve $q$ önermeleri için $\oplus$ bağlacı

$$p \oplus q \equiv (p \wedge q') \vee (p' \wedge q)$$

biçiminde tanımlanıyor. ("Ya $p$ ya $q$, ama ikisi birden değil.")

Buna göre $p \oplus q$ önermesi aşağıdakilerden hangisine denktir?

A) $p \Leftrightarrow q$
B) $p \Rightarrow q'$
C) $p' \Leftrightarrow q'$
D) $p \vee q$
E) $p \Leftrightarrow q'$

**Cevap:** E
**Çözüm:** $p \wedge q'$ yalnızca $(1, 0)$, $p' \wedge q$ yalnızca $(0, 1)$ durumunda doğrudur. Yani $p \oplus q$, $p$ ile $q$ farklıyken 1, aynıyken 0'dır: $(p \Leftrightarrow q)' \equiv p \Leftrightarrow q'$. A ve C bunun tam tersidir (C'deki iki değil birbirini götürür). D, $(1, 1)$ durumunda 1 olur; $\oplus$ ise 0'dır. B, $(0, 0)$ durumunda $0 \Rightarrow 1 \equiv 1$ olur; $\oplus$ ise 0'dır.

### Soru 12 · ÖSYM tarzı
Bir mağazanın alarm sistemi için şu kural geçerlidir:

"Alarm **ancak ve ancak** kapı açık ve sistem kurulu ise çalar."

- $a$: "Alarm çalıyor."
- $k$: "Kapı açık."
- $s$: "Sistem kurulu."

Kural doğru işlemektedir. Bir gece kapı açık olduğu hâlde alarmın çalmadığı görülüyor.

Buna göre aşağıdakilerden hangileri doğrudur?

- I. Sistem kurulu değildir.
- II. $k \Rightarrow s$ önermesi yanlıştır.
- III. $s \Leftrightarrow a$ önermesi doğrudur.

A) Yalnız I
B) Yalnız III
C) I ve II
D) I ve III
E) I, II ve III

**Cevap:** E
**Çözüm:** Kural: $a \Leftrightarrow (k \wedge s) \equiv 1$. Verilenler $a \equiv 0$, $k \equiv 1$. İki taraf aynı olmalı: $k \wedge s \equiv 0$, yani $1 \wedge s \equiv s \equiv 0$.
- I: $s \equiv 0$, doğru.
- II: $k \Rightarrow s \equiv 1 \Rightarrow 0 \equiv 0$; önerme yanlıştır, ifade doğru.
- III: $s \Leftrightarrow a \equiv 0 \Leftrightarrow 0 \equiv 1$, doğru.

Üçü de doğrudur. III'ü eleyen, iki tarafı da 0 olan "ancak ve ancak" önermesini yanlış sanmıştır. II'yi eleyen, "yanlıştır" diyen bir ifadenin kendisinin doğru olabileceğini gözden kaçırmıştır.
