---
baslik: Pozitif ve Negatif Sayılar
ders: tyt-matematik
sure: 20 dk
kaynak: MEBİ Konu Özeti ec41536b86
guncelleme: 2026-11-17
---
# Pozitif ve Negatif Sayılar

**Bu dersin sonunda:** toplam, çarpım ve kuvvetlerin işaretini verilen bilgiden bulabilecek, "$a \cdot b < 0$, $a + b > 0$" gibi koşullardan sayıların işaretini çıkarabileceksin.

> **TYT'de yeri:** Doğrudan gelen kalıp "verilen eşitsizliklere göre aşağıdakilerden hangisi kesinlikle pozitiftir / negatiftir?" sorusudur. Sayı doğrusunda yeri gösterilen $a$, $b$, $c$ ile ifadelerin işaretini sormak ve $-2^4$ ile $(-2)^4$ farkını yoklayan işlem soruları da sık gelir.

## Önce hatırla

<details><summary>Tek ve çift sayılardan: $a$ tek, $b$ çift tam sayı ise $a \cdot b + a + b$ tek midir, çift midir?</summary>
Çarpanlardan biri çift olduğu için $a \cdot b$ <b>çift</b>. Sonra çift + tek + çift: iki çift toplamı değiştirmez, tek sayı bir kez eklendiği için sonuç <b>tek</b>.
</details>

<details><summary>Tek ve çift sayılardan: $a$ tek tam sayı ve $n$ pozitif tam sayı ise $a^n + 4$ tek midir, çift midir?</summary>
Tek sayının bütün pozitif tam kuvvetleri tektir: $a^n$ tek. Tek + çift = <b>tek</b>. Bu derste aynı fikri işaret için kullanacaksın: kuvvetin sonucunu tabana ve üsse bakarak bulmak.
</details>

## Pozitif, negatif ve sıfır

**Örnek.** $-6,\ 0,\ \frac{1}{3},\ -(-2),\ -\sqrt{3},\ +5$ sayılarını pozitif ve negatif diye ayır, sonra küçükten büyüğe sırala.

- $-(-2) = 2$ olduğu için bu sayı **pozitiftir**. Pozitifler: $\frac{1}{3}$, $2$, $5$.
- Negatifler: $-6$ ve $-\sqrt{3} \approx -1{,}73$.
- $0$ hiçbir gruba girmez.
- Sıra: $-6 < -\sqrt{3} < 0 < \frac{1}{3} < 2 < 5$.

Sıfırdan büyük sayılar **pozitif**, sıfırdan küçük sayılar **negatif** sayılardır. Sayının önündeki $+$ ya da $-$ onun **işaretidir**; işaret yazılmamışsa sayı pozitiftir. $-0 = +0 = 0$ olduğu için sıfır **ne pozitif ne negatiftir**.

![Sayı doğrusu: sıfırın solu kırmızı ve Negatif sayılar diye, sağı yeşil ve Pozitif sayılar diye işaretli; sıfırda boş bir halka var. Altta sağa gittikçe büyür yazan bir ok.](gorsel/tyt-matematik/01-04-sayi-dogrusu.svg "Sağdaki sayı her zaman büyüktür. Bu yüzden −5, −1'den küçüktür: sıfırdan uzak olan negatif sayı daha küçüktür.")

Sözlü ifadeleri karıştırma:

| İfade | Anlamı | Sıfır dahil mi? |
|---|---|---|
| $a$ pozitif | $a > 0$ | Hayır |
| $a$ negatif | $a < 0$ | Hayır |
| $a$ pozitif değil | $a \le 0$ | Evet |
| $a$ negatif değil | $a \ge 0$ | Evet |

Pozitif gerçek sayılar $\mathbb{R}^+$, negatif gerçek sayılar $\mathbb{R}^-$ ile gösterilir ve $\mathbb{R}^- \cup \{0\} \cup \mathbb{R}^+ = \mathbb{R}$ olur. Tam sayılarda da aynısı geçerlidir: $\mathbb{Z}^- \cup \{0\} \cup \mathbb{Z}^+ = \mathbb{Z}$.

**Kural.** Sıfır ne pozitif ne negatiftir. $a < 0$ ise $-a > 0$ olur: önünde eksi olan bir harf negatif demek değildir.

## Toplamın işareti

**Örnek.** $a = -2$, $b = 5$ ise $a + b = 3$; $a = -5$, $b = 2$ ise $a + b = -3$; $a = -4$, $b = 4$ ise $a + b = 0$. Üç durumda da sayılar ters işaretli, ama toplamın işareti değişiyor.

![Üç sayı doğrusu. Birincide eksi 2 ile 5 toplanıp 3 bulunuyor, ikincide eksi 5 ile 2 toplanıp eksi 3, üçüncüde eksi 4 ile 4 toplanıp 0. Toplam baklava biçimli noktayla gösterilmiş.](gorsel/tyt-matematik/01-04-toplam-isareti.svg "Kırmızı ve yeşil çubukları karşılaştır: hangisi uzunsa, yani hangi sayı sıfıra daha uzaksa, toplam o tarafa düşer.")

| $a$ ve $b$ | $a + b$ |
|---|---|
| ikisi de pozitif | pozitif |
| ikisi de negatif | negatif |
| ters işaretli | mutlak değerce büyük olanın işareti |

**Ters yönden düşün.** Sorular çoğu zaman toplamı verir, sayıları sorar:

- $a + b > 0$ ise: ya ikisi de pozitiftir ya da ters işaretlidirler ve **pozitif olan mutlak değerce büyüktür**.
- $a + b < 0$ ise: ya ikisi de negatiftir ya da ters işaretlidirler ve **negatif olan mutlak değerce büyüktür**.
- $a + b = 0$ ise: ya ikisi de sıfırdır ya da $b = -a$ olur.

**Kural.** Toplamın işareti tek başına sayıların işaretini belirlemez. $a + b > 0$ verildiğinde "ikisi de pozitif" diyemezsin; $-2 + 5 > 0$ da olur.

## Çarpım ve bölümün işareti

**Örnek.** $a \cdot b < 0$, $\frac{b}{c} > 0$ ve $c < 0$ olduğuna göre $a$ ve $b$'nin işaretleri nedir?

- $\frac{b}{c} > 0$: bölüm pozitif, yani $b$ ile $c$ aynı işaretli. $c < 0$ olduğu için $b < 0$.
- $a \cdot b < 0$: çarpım negatif, yani $a$ ile $b$ ters işaretli. $b < 0$ olduğu için $a > 0$.

Bilinen işaretle başla, her adımda bir bilinmeyeni çöz.

| $a$ | $b$ | $a \cdot b$ ve $\frac{a}{b}$ |
|---|---|---|
| $+$ | $+$ | $+$ |
| $+$ | $-$ | $-$ |
| $-$ | $+$ | $-$ |
| $-$ | $-$ | $+$ |

Çok çarpanlı bir işlemde **negatif çarpanları say**: sayı çiftse sonuç pozitif, tekse negatiftir. $(-1) \cdot (-2) \cdot (-3) \cdot 4$ işleminde 3 negatif var, sonuç $-24$.

**Kural.** $a \cdot b > 0$ (ya da $\frac{a}{b} > 0$) ise $a$ ve $b$ aynı işaretli; $a \cdot b < 0$ ise ters işaretlidir. Çarpım ve bölüm aynı işareti verir.

## Kuvvetlerin işareti

**Örnek.** $(-2)^1,\ (-2)^2,\ (-2)^3,\ (-2)^4$ ile $-2^4$ ve $(-2)^0$ değerlerini bul.

- $(-2)^1 = -2$, $(-2)^2 = 4$, $(-2)^3 = -8$, $(-2)^4 = 16$.
- $-2^4$ yazımında üs yalnızca $2$'ye aittir, eksi dışarıda kalır: $-2^4 = -(2^4) = -16$.
- $(-2)^0 = 1$: sıfırıncı kuvvet pozitiftir (çünkü $0$ çift sayıdır).
- Negatif üste de aynı kural geçerli: $(-2)^{-3} = \frac{1}{(-2)^3} = -\frac{1}{8}$, üs tek olduğu için negatif.

![Sayı doğrusunda eksi 2'nin kuvvetleri: birinci kuvvet eksi 2'de, ikinci kuvvet 4'te, üçüncü kuvvet eksi 8'de, dördüncü kuvvet 16'da. Tek üsler solda kırmızı, çift üsler sağda yeşil.](gorsel/tyt-matematik/01-04-kuvvet-zipla.svg "Üs bir arttıkça sonuç sıfırın bir sağına bir soluna geçer. Tek üsler negatif tarafta, çift üsler pozitif tarafta kalır.")

| Taban | Üs | Sonuç |
|---|---|---|
| pozitif | her tam sayı | pozitif |
| negatif | çift | pozitif |
| negatif | tek | negatif |

Buradan iki sonuç çıkar: sıfırdan farklı her $a$ için $a^2 > 0$ ve $a^4 > 0$ gibi **çift kuvvetler hep pozitiftir**; tek kuvvet ise tabanın işaretini taşır, $a^3$ ile $a$ aynı işaretlidir.

**Kural.** Pozitif sayının her kuvveti pozitiftir. Negatif sayının çift kuvveti pozitif, tek kuvveti negatiftir. Parantez yoksa üs yalnızca sayıya aittir: $-3^2 = -9$, $(-3)^2 = 9$.

## Üslü eşitsizliklerden işaret bulma

**Örnek.** $a$ ve $b$ sıfırdan farklı gerçek sayılardır. $a^6 \cdot b^3 > 0$ ve $a^3 \cdot b^2 < 0$ olduğuna göre $a \cdot b$ ve $a - b$ ifadelerinin işaretleri nedir?

- $a^6 \cdot b^3 > 0$: $a^6$ çift kuvvet, pozitif; işareti etkilemez. Geriye $b^3 > 0$ kalır, $b^3$ ile $b$ aynı işaretli: $b > 0$.
- $a^3 \cdot b^2 < 0$: $b^2$ pozitif, atılır. $a^3 < 0$, yani $a < 0$.
- $a < 0 < b$: $a \cdot b < 0$ (ters işaretli) ve $a - b < 0$ (küçükten büyük çıkıyor).

![Dört adımlı yöntem: verilen eşitsizlikten başla; çift üslü çarpanları at; tek üsleri sil; işaret kuralını uygula; bulduğun işareti sonraki eşitsizlikte kullan.](gorsel/tyt-matematik/01-04-isaret-yontemi.svg "Çift üslü çarpan pozitif olduğu için işareti değiştirmez, atılır. Tek üslü çarpan tabanıyla aynı işaretli olduğu için üssü silinebilir.")

**Kural.** Sıfırdan farklı sayılarda çift üslü çarpanları at, tek üsleri sil; geriye kalan sade eşitsizliği çarpma kuralıyla çöz.

Son bir kalıp: $a < b < 0 < c$ gibi bir sıralama verilirse her ifadeyi tek tek kontrol et. Örneğin $a \cdot b > 0$, $a \cdot b \cdot c > 0$, $b - a > 0$ kesindir; ama $b + c$ hakkında $|b|$ ile $|c|$ bilinmeden bir şey söylenemez.

## ÖSYM tuzakları

> **Parantezsiz üs:** $-2^4 = -16$, $(-2)^4 = 16$. Eksi işareti parantezin içinde değilse üs onu kapsamaz.

> **Sıfırı pozitif saymak:** "Pozitif olmayan" sayı $a \le 0$ demektir, sıfır da dahildir. "Pozitif sayılar" içinde ise sıfır yoktur.

> **"$-a$ negatiftir" sanmak:** $a < 0$ ise $-a > 0$. Örneğin $a = -3$ için $-a = 3$. Harfin önündeki eksi, sayının işaretini söylemez.

> **Toplamdan hızlı sonuç:** $a + b > 0$ diye "ikisi de pozitif" denmez. $a \cdot b < 0$ ile birlikte verilirse sayılar ters işaretlidir ve pozitif olan mutlak değerce büyüktür.

> **"Kesinlikle" sözcüğü:** Bazı değerlerde pozitif, bazılarında negatif olan ifade "kesinlikle pozitif" değildir. Şüphelendiğin seçeneği bir karşı örnekle dene: $a = -1$, $b = -5$ gibi.

## Kendini dene

### Soru 1
$-2^4 + (-2)^3$ işleminin sonucu kaçtır?

A) $-24$
B) $-8$
C) $0$
D) $8$
E) $24$

**Cevap:** A
**Çözüm:** $-2^4 = -(2^4) = -16$; $(-2)^3 = -8$ (negatif taban, tek üs). Toplam $-16 + (-8) = -24$. $-2^4$ değerini $16$ alan $16 - 8 = 8$ bulur; iki terimi de pozitif alan $24$ bulur.

### Soru 2
$a \cdot b > 0$ ve $a + b < 0$ olduğuna göre aşağıdakilerden hangisi **kesinlikle** doğrudur?

A) $a > 0$
B) $b > 0$
C) $a - b < 0$
D) $a \cdot b^2 < 0$
E) $a + b^2 > 0$

**Cevap:** D
**Çözüm:** $a \cdot b > 0$: aynı işaretliler. Toplamları negatif olduğu için ikisi de negatiftir: $a < 0$, $b < 0$. $b^2 > 0$ olduğundan $a \cdot b^2$ negatif ile pozitifin çarpımıdır, negatiftir. A ve B yanlış. C için $a = -1$, $b = -5$ alırsan $a - b = 4 > 0$ olur; E için $a = -10$, $b = -1$ alırsan $a + b^2 = -9 < 0$ olur. Bu ikisi kesin değildir.

### Soru 3
$x$ ve $y$ sıfırdan farklı gerçek sayılardır. $x^2 \cdot y < 0$ ve $x \cdot y^3 > 0$ olduğuna göre $x$ ve $y$'nin işaretleri aşağıdakilerden hangisidir?

A) $x > 0,\ y > 0$
B) $x > 0,\ y < 0$
C) $x < 0,\ y < 0$
D) $x < 0,\ y > 0$
E) Belirlenemez

**Cevap:** C
**Çözüm:** $x^2 > 0$ atılır: $y < 0$. $y^3$ tek kuvvet, $y$ ile aynı işaretli, negatif. $x \cdot y^3 > 0$ için $x$ de negatif olmalı: $x < 0$. İkinci eşitsizlikte $y^3$'ü pozitif sanan B'yi seçer.

## Özet kartı

- Sıfır ne pozitif ne negatiftir; "pozitif değil" $\le 0$, "negatif değil" $\ge 0$ demektir.
- Ters işaretli iki sayının toplamı, mutlak değerce büyük olanın işaretini alır.
- $a \cdot b$ ya da $\frac{a}{b}$ pozitifse aynı işaretli, negatifse ters işaretli.
- Negatif tabanda çift üs pozitif, tek üs negatif; $-2^4 = -16$, $(-2)^4 = 16$.
- Üslü eşitsizlikte çift üslüleri at, tek üsleri sil, sonra çarpma kuralını uygula.
- "Kesinlikle" sorularında şüpheli seçeneği bir karşı örnekle dene.

## Sonraki adım

Alıştırmaya geç (aşağıdaki düğme). Sonraki ders **Ardışık Sayılar**; ardışık tam sayıların toplam ve çarpımlarında burada öğrendiğin işaret kurallarını kullanacaksın.
