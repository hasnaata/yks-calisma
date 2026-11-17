---
baslik: Birinci Dereceden Bir Bilinmeyenli Denklemler
ders: tyt-matematik
sure: 20 dk
kaynak: MEBİ Konu Özeti 18df908184
guncelleme: 2026-11-18
---
# Birinci Dereceden Bir Bilinmeyenli Denklemler

<div class="giris" dir="rtl" lang="ar">

**الدرس ده عن إيه؟** عن المعادلة من الدرجة الأولى في مجهول واحد (birinci dereceden bir bilinmeyenli denklem): إزاي تحلها خطوة بخطوة من غير ما تتلخبط في الإشارات.

- هتحل معادلات فيها أقواس وكسور، وتتأكد من الحل بالتعويض.
- هتعرف من المعاملات (katsayılar) إمتى المعادلة ليها جذر (kök) واحد، وإمتى مجموعة الحل (çözüm kümesi) تبقى كل الأعداد الحقيقية أو مجموعة خالية (boş küme).
- هتتعلم تطلّع المعامل المجهول لما يدّوك جذر المعادلة.

**ليه مهم؟** السؤال المباشر عليه قليل في TYT، بس تقريبًا كل مسألة كلامية في الامتحان بتتحول في الآخر لمعادلة زي دي، فلو أتقنتها هتوفّر وقت كتير.

٢٠ دقيقة بس، ومعاك ميزان ورسومات بتوضّح الفكرة. ابدأ دلوقتي وهتلاقيه أسهل ما انت متخيّل.

</div>

**Bu dersin sonunda:** parantezli ve kesirli bir denklemi hatasız çözebilecek, çözüm kümesinin tek kök, $\mathbb{R}$ ya da $\varnothing$ olduğunu katsayılardan anlayabilecek ve kökü verilen bir denklemde bilinmeyen katsayıyı bulabileceksin.

> **TYT'de yeri:** Bu konu doğrudan az sorulur ama TYT matematiğin neredeyse her problem sorusu sonunda bir denkleme dönüşür. Doğrudan gelen kalıplar: "denklem birinci dereceden olduğuna göre kökü kaçtır?", "çözüm kümesi boş küme / gerçek sayılar ise $a + b$ kaçtır?", "kökü 3 olduğuna göre $m$ kaçtır?" ve tanımlanan bir işlemle kurulan denklemler.

## Önce hatırla

<details><summary>Aralık kavramından: $(-4, 3]$ aralığında kaç tam sayı vardır?</summary>
$-4$ dahil değil, $3$ dahil. Tam sayılar $-3, -2, -1, 0, 1, 2, 3$; toplam <b>7</b>. Uçlar tam sayı ve aralık yarı açık olduğu için kısa yol: $3 - (-4) = 7$.
</details>

<details><summary>Aralık kavramından: $A = [0, 6)$ olduğuna göre $\mathbb{R} \setminus A$ kümesi nedir?</summary>
Tümleyende uçların durumu ters döner: $0$ dahildi, artık değil; $6$ dahil değildi, artık dahil. $\mathbb{R} \setminus A = (-\infty, 0) \cup [6, \infty)$.
</details>

## Denklem ve derecesi

**Örnek.** $(m - 2)x^2 + (m + 1)x - 6 = 0$ denklemi birinci dereceden bir bilinmeyenli bir denklem olduğuna göre kökü kaçtır?

Birinci dereceden olması için $x^2$ terimi yok olmalı: $m - 2 = 0$, yani $m = 2$. Yerine yaz: $(2 + 1)x - 6 = 0$, yani $3x - 6 = 0$. Buradan $3x = 6$, $x = 2$.

İçinde bilinmeyen bulunan bir **eşitliğe** denklem denir. $2x + 8$ bir denklem değildir (eşittir yok, yalnızca ifade); $2x + 8 = 0$ bir denklemdir. Denklemin derecesi, bilinmeyenin en büyük kuvvetidir.

**Kural.** $a, b \in \mathbb{R}$ ve $a \ne 0$ olmak üzere $ax + b = 0$ biçimine getirilebilen denkleme **birinci dereceden bir bilinmeyenli denklem** denir. $a$ ve $b$ katsayılar, $x$ bilinmeyendir (değişken). Denklemi sağlayan $x$ değerine **kök**, köklerin kümesine **çözüm kümesi** (ÇK) denir.

Bilinmeyen her zaman $x$ olmak zorunda değildir. $5t - 15 = 0$ denkleminde bilinmeyen $t$'dir, kökü $3$'tür.

## Eşitliği koruyarak çözmek

**Örnek.** $3x + 2 = x + 8$ denklemini bir terazi gibi düşün: her $x$ bir kutu, sayılar kilogram cinsinden ağırlık.

![İki terazi alt alta. Üstteki dengede: sol kefede üç x kutusu ve 2 kg, sağ kefede bir x kutusu ve 8 kg. Alttaki de dengede: solda iki x kutusu, sağda 6 kg.](gorsel/tyt-matematik/03-02-terazi.svg "İki kefeden aynı şeyi çıkarınca denge bozulmaz. Sonunda iki kutu 6 kg ise bir kutu 3 kg olur.")

İki kefeden de bir kutu ve 2 kg çıkarırsan denge bozulmaz: $2x = 6$. İki tarafı 2'ye böl: $x = 3$.

**Sağlama:** $3 \cdot 3 + 2 = 11$ ve $3 + 8 = 11$. Eşit, kök doğru.

**Kural.** Eşitliğin iki tarafına aynı sayı eklenebilir ya da çıkarılabilir; iki taraf **sıfırdan farklı** aynı sayıyla çarpılabilir ya da bölünebilir. "Karşıya atınca işaret değişir" kısa yolu da bundan gelir. Bulduğun kökü ilk denklemde yerine yazarak sağlama yap.

**Parantezli örnek.** $4(x - 3) + 5 = 2x + 9$

$$4x - 12 + 5 = 2x + 9 \;\Rightarrow\; 4x - 7 = 2x + 9 \;\Rightarrow\; 2x = 16 \;\Rightarrow\; x = 8$$

Sıra hep aynı: parantezleri aç, iki tarafı ayrı ayrı sadeleştir, $x$'li terimleri bir tarafa, sayıları öbür tarafa topla, katsayıya böl.

## Kesirli denklemler

**Örnek.** $\dfrac{x + 1}{2} - \dfrac{x - 2}{3} = 2$

Paydaların EKOK'u 6. Her terimi, sağ taraf da dahil, 6 ile çarp:

$$3(x + 1) - 2(x - 2) = 12$$
$$3x + 3 - 2x + 4 = 12$$
$$x + 7 = 12 \;\Rightarrow\; x = 5$$

Sağlama: $\frac{6}{2} - \frac{3}{3} = 3 - 1 = 2$. Doğru.

**Kural.** Paydaları EKOK ile çarparak yok et. Kesir çizgisi bir parantez gibidir: kesrin önündeki eksi, payın **bütün** terimlerine dağılır. $-2(x - 2) = -2x + 4$ olur, $-2x - 4$ değil. Bu hatayı yapan $x = 13$ bulur.

## Çözüm kümesinin üç durumu

**Örnek 1.** $2(x + 3) - x = x + 6$. Sol taraf $x + 6$ olur, denklem $x + 6 = x + 6$. Her $x$ için doğrudur. $x$'leri topladığında $0 \cdot x = 0$ kalır: **ÇK $= \mathbb{R}$**.

**Örnek 2.** $3x - 1 = 3(x + 1)$. Sağ taraf $3x + 3$. $x$'leri topla: $0 \cdot x = 4$. Hiçbir sayıyı sıfırla çarpınca 4 çıkmaz: **ÇK $= \varnothing$**.

Denklemin iki tarafını ayrı ayrı çizersen farkı görürsün:

![Üç grafik alt alta. Birincide sol taraf ve sağ taraf doğruları x eşittir 2'de kesişiyor. İkincide iki doğru paralel, hiç kesişmiyor. Üçüncüde iki doğru üst üste çakışıyor.](gorsel/tyt-matematik/03-02-uc-durum.svg "Kök, iki tarafın eşit olduğu x değeridir. Paralel doğrular hiç eşit olmaz, çakışık doğrular her yerde eşittir.")

Bütün durumları tek bir karar akışında topla:

![Akış şeması: denklemi ax eşittir b biçimine getir. a sıfır değilse tek kök x eşittir b bölü a. a sıfırsa b'ye bak: b sıfırsa çözüm kümesi gerçek sayılar, değilse boş küme.](gorsel/tyt-matematik/03-02-durumlar.svg "Önce a'ya, sonra b'ye bak. b'ye yalnızca a sıfırsa bakılır.")

| $ax = b$ biçiminde | Çözüm kümesi |
|---|---|
| $a \ne 0$ | Tek kök: $\left\{\frac{b}{a}\right\}$ |
| $a = 0$ ve $b = 0$ | $\mathbb{R}$ (her gerçek sayı) |
| $a = 0$ ve $b \ne 0$ | $\varnothing$ (boş küme) |

Kaynakta denklem $ax + b = 0$ biçiminde yazılır; o zaman tek kök $x = -\frac{b}{a}$ olur. İkisi aynı şeydir, işaretine dikkat et.

**Parametreli örnek.** $(a - 2)x + 6 = 3x + b$ denkleminin çözüm kümesi $\mathbb{R}$ ise $a$ ve $b$ kaçtır?

$x$'leri sola, sayıları sağa topla: $(a - 2 - 3)x = b - 6$, yani $(a - 5)x = b - 6$. ÇK $= \mathbb{R}$ için iki katsayı da sıfır olmalı: $a = 5$, $b = 6$.

**Kural.** Önce denklemi mutlaka $ax = b$ biçimine getir, sonra tabloya bak. Katsayıları ilk hâlinden okumak yanlış sonuç verir.

## Harfli denklemler ve kökü verilen denklemler

**Örnek 1.** $2x + m = 5x - 7$ denkleminin kökü $3$ ise $m$ kaçtır?

Kök, denklemi sağlayan sayıdır; $x = 3$ yaz: $6 + m = 15 - 7 = 8$, yani $m = 2$.

**Örnek 2.** $mx - 4 = 2x + m$ denklemini $x$'e göre çöz.

$m$ bir sabit sayı gibi davranır. $x$'li terimleri sola, ötekileri sağa topla: $(m - 2)x = m + 4$. $m \ne 2$ ise

$$x = \frac{m + 4}{m - 2}$$

$m = 2$ olursa $0 \cdot x = 6$ kalır ve kök yoktur.

**Kural.** Kök verilirse yerine yaz. Harfle bölmeden önce o harfin sıfır olup olamayacağını sor.

## ÖSYM tuzakları

> **Kesrin önündeki eksi:** $-\frac{x - 2}{3}$ ifadesi 3 ile çarpılınca $-x + 2$ olur. Eksiyi yalnızca ilk terime dağıtan yanlış kökü bulur ve o kök seçeneklerde mutlaka vardır.

> **Sağ tarafı çarpmayı unutmak:** $\frac{x + 1}{2} - \frac{x - 2}{3} = 2$ denkleminde 6 ile çarparken sağdaki $2$ de $12$ olur. Yalnızca kesirleri çarpan $x + 7 = 2$ yazar.

> **Sıfır olabilecek şeye bölmek:** $3x = 5x$ denkleminde iki tarafı $x$'e bölüp "$3 = 5$, çözüm yok" demek yanlıştır. Doğrusu $2x = 0$, yani $x = 0$; ÇK $= \{0\}$.

> **$a = 0$ bulup durmak:** $(a^2 - 9)x = a - 3$ denkleminde ÇK $= \varnothing$ istenirse $a^2 = 9$ yetmez. $a = 3$ için sağ taraf $0$ olur, ÇK $= \mathbb{R}$. Yalnızca $a = -3$ boş küme verir. Her adayı $b$'de dene.

> **"Birinci dereceden" koşulu:** $x^2$'nin katsayısı sıfır olmalı, ama $x$'in katsayısı sıfır **olmamalı**. Bulduğun değeri yerine yazıp kalan denklemi kontrol et.

## Kendini dene

### Soru 1
$5(x - 1) - 2 = 3x + 7$ denkleminin kökü kaçtır?

A) $-7$
B) $0$
C) $5$
D) $6$
E) $7$

**Cevap:** E
**Çözüm:** Parantezi aç: $5x - 5 - 2 = 3x + 7$, yani $5x - 7 = 3x + 7$. $x$'leri sola, sayıları sağa topla: $2x = 14$, $x = 7$. Sağlama: $5 \cdot 6 - 2 = 28$ ve $21 + 7 = 28$. Parantezi açarken $5$'i yalnızca $x$ ile çarpan $5x - 1 - 2 = 3x + 7$ yazar ve $5$ bulur.

### Soru 2
$(m + 3)x^2 - (m - 1)x + 8 = 0$ denklemi birinci dereceden bir bilinmeyenli bir denklem olduğuna göre bu denklemin kökü kaçtır?

A) $-4$
B) $-2$
C) $-1$
D) $1$
E) $2$

**Cevap:** B
**Çözüm:** $x^2$ terimi yok olmalı: $m + 3 = 0$, $m = -3$. Yerine yaz: $-(-3 - 1)x + 8 = 0$, yani $4x + 8 = 0$, $x = -2$. Eksiyi parantezin içine yanlış dağıtan $2x + 8 = 0$ yazar ve $-4$ bulur; işareti karşıya geçirirken unutan $2$ bulur.

### Soru 3
$3(x - 1) + ax = 7x + b$ denkleminin çözüm kümesi gerçek sayılar kümesi olduğuna göre $a + b$ toplamı kaçtır?

A) $-7$
B) $-1$
C) $1$
D) $4$
E) $7$

**Cevap:** C
**Çözüm:** Sol taraf $(3 + a)x - 3$. Denklem $(3 + a)x - 3 = 7x + b$, yani $(a - 4)x = b + 3$. ÇK $= \mathbb{R}$ için iki taraf da sıfır olmalı: $a = 4$, $b = -3$. Toplam $4 + (-3) = 1$. $b$'nin işaretini yanlış alan $a + b = 7$ bulur.

## Özet kartı

- Denklemi çözmek: parantezi aç, sadeleştir, $x$'leri bir tarafa topla, katsayıya böl, sağlama yap.
- Kesirli denklemde her terimi (sağ taraf dahil) paydaların EKOK'u ile çarp; kesrin önündeki eksi bütün paya dağılır.
- $ax = b$: $a \ne 0$ ise tek kök $\frac{b}{a}$; $a = 0, b = 0$ ise ÇK $= \mathbb{R}$; $a = 0, b \ne 0$ ise ÇK $= \varnothing$.
- "Birinci dereceden" ise $x^2$'nin katsayısı $0$, $x$'in katsayısı $0$ değil.
- Kök verildiyse yerine yaz; harfle bölmeden önce o harf sıfır olabilir mi diye bak.

## Sonraki adım

Alıştırmaya geç (aşağıdaki düğme). Sonraki ders **Basit Eşitsizlikler**: çözüm yöntemi neredeyse aynıdır, tek fark negatif sayıyla çarpınca yön değiştiren eşitsizlik işaretidir. Cevabı da önceki dersteki aralık gösterimiyle yazacaksın.
