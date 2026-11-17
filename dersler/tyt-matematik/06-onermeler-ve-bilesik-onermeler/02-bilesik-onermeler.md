---
baslik: Bileşik Önermeler
ders: tyt-matematik
sure: 25 dk
kaynak: MEBİ Konu Özeti f11d72b5cb
guncelleme: 2026-11-17
---
# Bileşik Önermeler

**Bu dersin sonunda:** "ve", "veya", "ya da" bağlaçlarıyla kurulan bir bileşik önermenin doğruluk değerini bulabilecek, sonucu bilinen bir önermeden bileşenlerin değerini geri çıkarabilecek ve De Morgan kurallarıyla bir bileşik önermenin değilini yazabileceksin.

> **TYT'de yeri:** Mantık sorularının çoğu bu derstendir. Üç kalıp sık gelir: "$p \equiv 1$, $q \equiv 0$ ise hangisi doğrudur?", "$(p \vee q') \wedge r \equiv 1$ ise $p$, $q$, $r$ nedir?" ve "hangi önermenin değili / hangisine denktir?". Yeni nesil sorularda bağlaç bir devre, bir alarm kuralı ya da yeni tanımlanan bir işlemle verilir.

## Önce hatırla

<details><summary>Önermelerden: p: "(−2)³ = −8" ve q: "−2² = 4" önermelerinin doğruluk değerleri nedir? p ≡ q yazılabilir mi?</summary>
$(-2)^3 = -8$ doğrudur: $p \equiv 1$. Üs yalnızca 2'ye etki eder, $-2^2 = -4$ olur; $q \equiv 0$. Değerler farklı olduğu için $p \not\equiv q$. Buradan $q' \equiv 1$ olduğunu da bil: bu derste değilleri sürekli kullanacaksın.
</details>

<details><summary>Önermelerden: Bir x gerçek sayısı için p: "x ≥ 5" önermesinin değili nedir?</summary>
$p'$: "$x < 5$". Eşitlik $p$'nin içinde olduğu için değile geçmez. "Büyük eşit"in değili "küçük", "büyük"ün değili "küçük eşit" olur.
</details>

## Bileşik önerme nedir?

"12 bir çift sayıdır **ve** 12 bir asal sayıdır." cümlesi iki önermeden kurulmuştur: $p$: "12 bir çift sayıdır", $q$: "12 bir asal sayıdır". İki ya da daha çok önermenin bir **bağlaçla** birleştirilmesiyle oluşan yeni önermeye **bileşik önerme** denir.

| Bağlaç | Simge | Okunuşu | Ne zaman 1? |
|---|---|---|---|
| ve | $p \wedge q$ | "p ve q" | İkisi de 1 ise |
| veya | $p \vee q$ | "p veya q" | En az biri 1 ise |
| ya da | $p \veebar q$ | "p ya da q" | Yalnız biri 1 ise |
| ise | $p \Rightarrow q$ | "p ise q" | Sonraki ders |
| ancak ve ancak | $p \Leftrightarrow q$ | "p ancak ve ancak q" | Sonraki dersler |

Bileşik önermenin değeri, bileşenlerin anlamına değil yalnızca **1 ve 0'larına** bağlıdır.

## "ve" bağlacı: $p \wedge q$

**Örnek.** $p$: "$2^5 = 32$", $q$: "15 bir asal sayıdır".

$p \equiv 1$, $q \equiv 0$ ($15 = 3 \cdot 5$). "$2^5 = 32$ **ve** 15 asaldır." cümlesi iki hükmü birden iddia eder; ikincisi yanlış olduğu için bütün cümle yanlıştır: $p \wedge q \equiv 1 \wedge 0 \equiv 0$.

![Üstte seri bağlı devre: pil, p ve q anahtarları aynı tel üzerinde arka arkaya, sonra lamba. Altta paralel bağlı devre: p ve q anahtarları iki ayrı kolda, kollar birleşip lambaya gidiyor.](gorsel/tyt-matematik/06-02-devre.svg "Kapalı anahtar 1, açık anahtar 0 demektir. Seri devrede tek bir açık anahtar lambayı söndürür; paralel devrede tek bir kapalı anahtar lambayı yakar.")

| $p$ | $q$ | $p \wedge q$ |
|---|---|---|
| 1 | 1 | **1** |
| 1 | 0 | 0 |
| 0 | 1 | 0 |
| 0 | 0 | 0 |

**Kural.** $p \wedge q$ yalnızca $p$ ile $q$'nun **ikisi de 1** iken 1'dir. Bir tane 0 bütün "ve" zincirini 0 yapar.

- $p \wedge p \equiv p$ (tek kuvvet), $\;p \wedge q \equiv q \wedge p$ (değişme), $\;(p \wedge q) \wedge r \equiv p \wedge (q \wedge r)$ (birleşme)
- $p \wedge 1 \equiv p$, $\;p \wedge 0 \equiv 0$, $\;p \wedge p' \equiv 0$

## "veya" bağlacı: $p \vee q$

**Örnek.** $p$: "7 bir tek sayıdır", $q$: "7 bir asal sayıdır".

İkisi de doğrudur. "7 tektir **veya** asaldır." cümlesi en az birinin doğru olduğunu iddia eder; ikisi de doğru olduğu için iddia yine doğrudur: $p \vee q \equiv 1 \vee 1 \equiv 1$. Yukarıdaki paralel devrede iki anahtar birden kapalıyken de lamba yanar.

| $p$ | $q$ | $p \vee q$ |
|---|---|---|
| 1 | 1 | 1 |
| 1 | 0 | 1 |
| 0 | 1 | 1 |
| 0 | 0 | **0** |

**Kural.** $p \vee q$ yalnızca **ikisi de 0** iken 0'dır. Bir tane 1 bütün "veya" zincirini 1 yapar.

- $p \vee p \equiv p$, $\;p \vee q \equiv q \vee p$, $\;(p \vee q) \vee r \equiv p \vee (q \vee r)$
- $p \vee 0 \equiv p$, $\;p \vee 1 \equiv 1$, $\;p \vee p' \equiv 1$

## Bileşik önermenin değerini bulmak

**Örnek 1 (ileri).** $p \equiv 1$, $q \equiv 0$, $r \equiv 0$ ise $(p \wedge q') \wedge (q \vee r)$ kaçtır?

1. Önce değiller: $q' \equiv 1$.
2. Parantezler: $p \wedge q' \equiv 1 \wedge 1 \equiv 1$ ve $q \vee r \equiv 0 \vee 0 \equiv 0$.
3. Dıştaki bağlaç: $1 \wedge 0 \equiv 0$.

**Örnek 2 (geri).** $(p \vee q') \vee r' \equiv 0$ ise $p$, $q$, $r$ nedir?

Sonuç 0 olan bir "veya", ancak **bütün** parçaları 0 iken mümkündür: $p \equiv 0$, $q' \equiv 0$, $r' \equiv 0$. Buradan $p \equiv 0$, $q \equiv 1$, $r \equiv 1$.

**Kural.** Sırayla: değil → parantez içi → dıştaki bağlaç. Geriye doğru giderken iki durum tek cevap verir:

- "ve" $\equiv 1$ ise **bütün** parçalar 1'dir.
- "veya" $\equiv 0$ ise **bütün** parçalar 0'dır.

"ve" $\equiv 0$ ya da "veya" $\equiv 1$ bilgisi tek başına parçaları belirlemez; ikinci bir bilgi gerekir.

## Dağılma özelliği

**Örnek.** $(p \wedge q) \vee (p \wedge q')$ önermesini sadeleştir.

İki parantezde de $p \wedge$ ortak. Ortak parçayı dışarı al: $p \wedge (q \vee q')$. $q \vee q' \equiv 1$ olduğundan sonuç $p \wedge 1 \equiv p$.

**Kural.** Sayılardaki $a(b + c) = ab + ac$ gibi:

$$p \wedge (q \vee r) \equiv (p \wedge q) \vee (p \wedge r) \qquad p \vee (q \wedge r) \equiv (p \vee q) \wedge (p \vee r)$$

Sayılardan farkı: burada **iki yön de** geçerlidir; "veya" da "ve" üzerine dağılır.

## De Morgan kuralları

**Örnek.** $p$: "Bugün yağmur yağıyor", $q$: "Hava soğuk". $p \wedge q$: "Bugün yağmur yağıyor ve hava soğuk."

Bu cümle ne zaman yanlıştır? Yağmur yağmıyorsa da, hava soğuk değilse de yanlıştır; yani **en az biri** bozulunca. Değili: "Bugün yağmur yağmıyor **veya** hava soğuk değil." Kısaca $(p \wedge q)' \equiv p' \vee q'$.

Sayılarla: "$-1 < x$ ve $x \le 4$" önermesinin değili "$x \le -1$ **veya** $x > 4$" olur. $x$ aralığın dışına sol taraftan da sağ taraftan da çıkabilir.

![İki Venn şeması. Solda dikdörtgenin iki daire dışında kalan kısmı boyalı: p veya q önermesinin değili, p üssü ve q üssüne denk. Sağda yalnızca iki dairenin ortak bölgesi boş, geri kalan her yer boyalı: p ve q önermesinin değili, p üssü veya q üssüne denk.](gorsel/tyt-matematik/06-02-de-morgan.svg "Daire içi o önermenin doğru olduğu durumlardır. Soldaki boyalı bölge iki dairenin de dışı, yani p üssü ve q üssü; sağdaki ortak bölge dışındaki her yer.")

**Kural.**

$$(p \vee q)' \equiv p' \wedge q' \qquad (p \wedge q)' \equiv p' \vee q'$$

Değil paranteze girerken iki iş yapar: her önermeye üs koyar **ve** bağlacı çevirir ($\wedge \leftrightarrow \vee$).

## "ya da" bağlacı: $p \veebar q$

**Örnek.** Bir $x$ tam sayısı için $p$: "$x$ çifttir", $q$: "$x > 5$". $x = 8$ olsun.

$p \equiv 1$, $q \equiv 1$. "veya" ile: $p \vee q \equiv 1$. "ya da" ile: iki önerme birden doğru olduğu için $p \veebar q \equiv 0$. $x = 3$ için ise $p \equiv 0$, $q \equiv 0$: ikisi de 0'dır. $x = 4$ için yalnız $p$ doğrudur: $p \veebar q \equiv 1$.

![Üç Venn şeması yan yana. p ve q daireleri kesişiyor. Birincide yalnız ortak bölge boyalı: p ve q. İkincide iki dairenin tamamı boyalı: p veya q. Üçüncüde iki daire boyalı ama ortak bölge boş: p ya da q.](gorsel/tyt-matematik/06-02-venn.svg "Boyalı bölge bileşik önermenin 1 olduğu durumlardır. Üç bağlacı ortak bölgeye bakarak ayır: ve yalnız orada, veya orada da, ya da orada asla.")

| $p$ | $q$ | $p \veebar q$ |
|---|---|---|
| 1 | 1 | **0** |
| 1 | 0 | 1 |
| 0 | 1 | 1 |
| 0 | 0 | 0 |

**Kural.** $p \veebar q$, $p$ ile $q$'dan **yalnız biri** 1 iken 1'dir. Kısaca: değerler farklıysa 1, aynıysa 0.

- Değişme ve birleşme geçerlidir: $p \veebar q \equiv q \veebar p$, $\;(p \veebar q) \veebar r \equiv p \veebar (q \veebar r)$
- Tablodan çıkanlar: $p \veebar p \equiv 0$, $\;p \veebar p' \equiv 1$, $\;p \veebar 0 \equiv p$, $\;p \veebar 1 \equiv p'$

Günlük dilde "ya da" bazen "veya" anlamında kullanılır; mantık sorularında $\veebar$ her zaman "yalnız biri" demektir.

## ÖSYM tuzakları

> **"veya"yı "yalnız biri" sanmak:** $1 \vee 1 \equiv 1$'dir. İki önerme birden doğruyken 0 olan bağlaç $\veebar$'dir, $\vee$ değil.

> **De Morgan'da bağlacı çevirmeyi unutmak:** $(p \wedge q')'$ ifadesi $p' \wedge q$ değil, $p' \vee q$ olur. Üsleri dağıtırken $\wedge$ da $\vee$'ye döner; $(q')' \equiv q$.

> **Eşitsizliğin değilinde iki hata birden:** "$3 \le x$ ve $x < 8$" önermesinin değili "$x < 3$ **veya** $x \ge 8$" olur. "ve" kalırsa hiçbir sayı sağlamaz; eşitlik yanlış uca konursa bir sayı kaybolur.

> **Tek bilgiden fazlasını çıkarmak:** $p \wedge q \equiv 0$ ise "$p \equiv 0$" denemez; yalnızca "ikisi birden 1 değil" denebilir. Kesin sonuç yalnızca "ve $\equiv 1$" ya da "veya $\equiv 0$" bilgisinden çıkar.

> **İşlem sırasını karıştırmak:** $(p \vee q)'$ ile $p' \vee q$ farklıdır. Üs parantezin dışındaysa bütün parantezin değilidir.

## Kendini dene

### Soru 1
$p \equiv 0$, $q \equiv 1$ ve $r \equiv 1$ olduğuna göre aşağıdaki önermelerden hangisinin doğruluk değeri 0'dır?

A) $p \vee q$
B) $q \wedge r$
C) $(p \wedge q) \vee r$
D) $p' \wedge q$
E) $q \veebar r$

**Cevap:** E
**Çözüm:** A) $0 \vee 1 \equiv 1$. B) $1 \wedge 1 \equiv 1$. C) $p \wedge q \equiv 0$, $0 \vee 1 \equiv 1$. D) $p' \equiv 1$, $1 \wedge 1 \equiv 1$. E) $q$ ile $r$ ikisi de 1; "ya da" yalnız biri 1 iken 1 olur, burada $q \veebar r \equiv 0$.

### Soru 2
Bir $x$ gerçek sayısı için "$3 \le x$ ve $x < 8$" önermesinin değili aşağıdakilerden hangisidir?

A) $x < 3$ ve $x \ge 8$
B) $x < 3$ veya $x \ge 8$
C) $x \le 3$ veya $x > 8$
D) $x > 3$ veya $x \le 8$
E) $x < 3$ veya $x > 8$

**Cevap:** B
**Çözüm:** De Morgan: $(p \wedge q)' \equiv p' \vee q'$. "$3 \le x$" önermesinin değili "$x < 3$", "$x < 8$" önermesinin değili "$x \ge 8$". Bağlaç "veya" olur: B. A'da bağlaç çevrilmemiş (hiçbir sayı sağlamaz). C ve E'de eşitlikler yanlış uçta; örneğin $x = 8$ asıl önermeyi sağlamaz, öyleyse değile girmelidir. D asıl önermenin bağlaç değiştirilmiş hâlidir.

### Soru 3
$p' \wedge (p \vee q)$ önermesi aşağıdakilerden hangisine denktir?

A) $0$
B) $p'$
C) $q$
D) $p' \wedge q$
E) $p \wedge q$

**Cevap:** D
**Çözüm:** Dağıt: $(p' \wedge p) \vee (p' \wedge q)$. $p' \wedge p \equiv 0$ ve $0 \vee x \equiv x$ olduğundan sonuç $p' \wedge q$. Kontrol: $p \equiv 0$, $q \equiv 0$ için önerme $1 \wedge 0 \equiv 0$ olur; B seçeneği ise 1 verir, bu yüzden B olamaz.

## Özet kartı

- $p \wedge q$: ikisi de 1 ise 1. Bir tane 0 yeter, sonuç 0.
- $p \vee q$: ikisi de 0 ise 0. Bir tane 1 yeter, sonuç 1.
- $p \veebar q$: değerler farklıysa 1, aynıysa 0.
- $p \wedge p' \equiv 0$, $\;p \vee p' \equiv 1$, $\;p \wedge 0 \equiv 0$, $\;p \vee 1 \equiv 1$.
- De Morgan: $(p \vee q)' \equiv p' \wedge q'$ ve $(p \wedge q)' \equiv p' \vee q'$.
- Geri çözerken: "ve $\equiv 1$" ise hepsi 1, "veya $\equiv 0$" ise hepsi 0.

## Sonraki adım

Alıştırmaya geç (aşağıdaki düğme). Sonraki ders **Koşullu Önerme**: "$p$ ise $q$" bağlacının yalnızca tek bir durumda 0 olduğunu göreceksin ve onu bugünkü "veya" ile yazmayı öğreneceksin.
