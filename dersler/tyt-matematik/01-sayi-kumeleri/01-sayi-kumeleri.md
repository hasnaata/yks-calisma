---
baslik: Sayı Kümeleri
ders: tyt-matematik
sure: 20 dk
kaynak: MEBİ Konu Özeti fb85b97e86
guncelleme: 2026-11-18
---
# Sayı Kümeleri

<div class="giris" dir="rtl" lang="ar">

**الدرس ده عن إيه؟** عن مجموعات الأعداد (sayı kümeleri): إزاي تعرف أي عدد تبع أنهي مجموعة، من الأعداد الطبيعية لحد الأعداد الحقيقية (gerçek sayılar).

- هتفرّق بين الأعداد الطبيعية (doğal sayılar) والأعداد الصحيحة (tam sayılar) والأعداد النسبية (rasyonel sayılar) والأعداد غير النسبية (irrasyonel sayılar).
- هتتعلم تبسّط الجذر التربيعي (karekök) الأول قبل ما تحكم على العدد، وتحدد مكانه تقريبًا على خط الأعداد (sayı doğrusu).
- هتعرف إمتى جمع أو ضرب عددين غير نسبيين ممكن يطلع عدد نسبي، وإزاي تدوّر على مثال مضاد (karşı örnek).

**ليه مهم؟** أسئلة المجموعات دي لوحدها قليلة في TYT، بس كلمة زي "tam sayı" أو "doğal sayı" في نص السؤال ممكن تقلب الإجابة خالص.

الدرس ٢٠ دقيقة بس، وهو أساس كل اللي جاي في الرياضيات، فابدأ بيه وإنت مركّز.

</div>

**Bu dersin sonunda:** verilen bir sayının doğal, tam, rasyonel ya da irrasyonel olduğunu kökü sadeleştirerek karar verebilecek, irrasyonel bir sayının sayı doğrusundaki yerini tahmin edebilecek ve rasyonel–irrasyonel sayılarla yapılan işlemlerin sonucunu yorumlayabileceksin.

> **TYT'de yeri:** Sayı kümeleri tek başına az soru olur ama her sorunun kökünde vardır: "$x$ bir tam sayı", "$a$ ve $b$ birer rakam", "$\sqrt{n}$ rasyonel" gibi ifadeler cevabı belirler. Sık kalıplar: "hangisi irrasyoneldir?", "kaç farklı doğal sayı değeri alır?", "hangileri kesinlikle rasyoneldir?" ve sayı doğrusunda yer bulma.

## Önce hatırla

Bu konunun ön bilgisi ortaokuldan: tam kare sayılar ve ondalık gösterim.

<details><summary>8. sınıftan: $\sqrt{50}$ hangi iki ardışık tam sayı arasındadır?</summary>
50'ye en yakın tam kareler $49 = 7^2$ ve $64 = 8^2$. $49 < 50 < 64$ olduğundan $7 < \sqrt{50} < 8$. Üstelik 50, 49'a çok yakın; $\sqrt{50} \approx 7{,}07$.
</details>

<details><summary>7. sınıftan: $0{,}25$ sayısını sadeleşmiş kesir olarak yaz.</summary>
$0{,}25 = \frac{25}{100} = \frac{1}{4}$. Sonlu her ondalık sayı böyle bir kesre çevrilebilir; bu dersin "rasyonel sayı" tanımı tam olarak buna dayanır.
</details>

## Rakam, doğal sayı, tam sayı

**Örnek.** $-3 < x \le 4$ koşulunu sağlayan $x$ sayıları için:

- $x$ **tam sayı** ise: $-2, -1, 0, 1, 2, 3, 4$ (7 tane).
- $x$ **doğal sayı** ise: $0, 1, 2, 3, 4$ (5 tane). Negatifler düşer, $0$ kalır.
- $x$ **pozitif tam sayı** ise: $1, 2, 3, 4$ (4 tane). $0$ da düşer.

Aynı eşitsizlik, kümeye göre farklı cevap verir. Bu yüzden soruda önce "$x$ hangi kümede?" diye bak.

| Küme | Simge | Elemanlar |
|---|---|---|
| Rakamlar | | $\{0, 1, 2, \dots, 9\}$ (10 tane) |
| Doğal sayılar | $\mathbb{N}$ | $\{0, 1, 2, 3, \dots\}$ |
| Sayma sayıları (pozitif tam sayılar) | $\mathbb{N}^+$ ya da $\mathbb{Z}^+$ | $\{1, 2, 3, \dots\}$ |
| Tam sayılar | $\mathbb{Z}$ | $\{\dots, -2, -1, 0, 1, 2, \dots\}$ |

**Kural.** Rakam, sayıyı yazmaya yarayan **simgedir**; 10 tane vardır. $\mathbb{N}$'ye negatifleri ekleyince $\mathbb{Z}$ olur. $0$ bir doğal sayıdır ve bir tam sayıdır, ama **ne pozitif ne negatiftir**.

## Rasyonel sayılar

**Örnek.** Şu sayıların her biri iki tam sayının oranı olarak yazılabilir:

$$-4 = \frac{-4}{1}, \qquad 0{,}75 = \frac{3}{4}, \qquad 1{,}333\dots = \frac{4}{3}, \qquad \sqrt{\frac{9}{16}} = \frac{3}{4}$$

Hepsi **rasyonel** sayıdır. Karekök görünce hemen "irrasyonel" deme; önce sadeleştir.

**Kural.** $a$ ve $b$ tam sayı, $b \ne 0$ olmak üzere $\frac{a}{b}$ biçiminde yazılabilen sayılar rasyonel sayılardır; kümesi $\mathbb{Q}$. Her tam sayı rasyoneldir ($7 = \frac{7}{1}$). Sonlu ondalık sayılar ve devirli ondalık sayılar da rasyoneldir. $\frac{0}{5} = 0$ rasyoneldir; $\frac{5}{0}$ ise **tanımsızdır**, hiçbir kümede değildir.

## İrrasyonel sayılar

**Örnek.** Hangileri irrasyonel?

| Sayı | Sadeleştir | Sonuç |
|---|---|---|
| $\sqrt{49}$ | $7$ | rasyonel (doğal sayı) |
| $\sqrt{0{,}36}$ | $0{,}6 = \frac{3}{5}$ | rasyonel |
| $\sqrt{\frac{2}{8}}$ | $\sqrt{\frac{1}{4}} = \frac{1}{2}$ | rasyonel |
| $\sqrt{12}$ | $2\sqrt{3}$ | **irrasyonel** |
| $\pi$ | $3{,}14159\dots$ (devretmez, bitmez) | **irrasyonel** |
| $\frac{22}{7}$ | iki tam sayının oranı | rasyonel ($\pi$'nin yaklaşık değeri) |

**Kural.** İki tam sayının oranı olarak **yazılamayan** sayılar irrasyoneldir; kümesi $\mathbb{Q}'$. Tam kare olmayan bir sayının karekökü ($\sqrt{2}$, $\sqrt{5}$, $\sqrt{12}$), $\pi$ ve $e \approx 2{,}718$ irrasyoneldir. Ondalık açılımları ne biter ne de devreder.

Dikkat: $\sqrt{-4}$ gibi kök içi negatif olan kareköklü ifadeler **gerçek sayı değildir**; ne rasyoneldir ne irrasyonel.

## Gerçek sayılar: kümeler arası ilişki

Rasyonel ve irrasyonel sayılar birlikte **gerçek (reel) sayılar** kümesini oluşturur: $\mathbb{Q} \cup \mathbb{Q}' = \mathbb{R}$. Bir sayı ya rasyoneldir ya irrasyonel; ikisi birden olamaz: $\mathbb{Q} \cap \mathbb{Q}' = \varnothing$.

![İç içe dikdörtgenler: en dışta R. Onun içinde solda Q, sağda Q üssü. Q'nun içinde Z, Z'nin içinde N. N'de 0, 7 ve kök 9; Z'de eksi 4 ve eksi kök 16; Q'da 2 bölü 3, 0,75 ve eksi 1,5; Q üssünde kök 2, pi ve eksi kök 7.](gorsel/tyt-matematik/01-01-kume-semasi.svg "Her küme bir öncekini içine alır: N, Z'nin; Z, Q'nun içindedir. Q üssü ise Q'nun dışında, yan yanadır. Kök 9 ve eksi kök 16'nın nereye düştüğüne bak.")

$$\mathbb{N} \subset \mathbb{Z} \subset \mathbb{Q} \subset \mathbb{R}, \qquad \mathbb{Q}' \subset \mathbb{R}$$

Bir sayının **en küçük** kümesini bulmak için şemada en içten dışarı doğru sor: doğal sayı mı? Değilse tam sayı mı? Değilse rasyonel mi? Hiçbiri değilse irrasyoneldir.

## Rasyonel ve irrasyonel sayılarla işlem

**Örnek.** $a = \sqrt{5} + 2$ ve $b = \sqrt{5} - 2$ olsun. İkisi de irrasyonel.

- $a + b = 2\sqrt{5}$: irrasyonel.
- $a - b = 4$: **rasyonel**.
- $a \cdot b = (\sqrt{5})^2 - 2^2 = 5 - 4 = 1$: **rasyonel**.

İki irrasyonelin toplamı, farkı ya da çarpımı rasyonel **çıkabilir**.

| İşlem | Sonuç |
|---|---|
| rasyonel $\pm$ rasyonel, rasyonel $\cdot$ rasyonel | her zaman rasyonel |
| rasyonel $\pm$ irrasyonel | her zaman irrasyonel |
| **sıfırdan farklı** rasyonel $\cdot$ irrasyonel | her zaman irrasyonel |
| irrasyonel ile irrasyonel | belli değil: $\sqrt{2} \cdot \sqrt{8} = 4$ ama $\sqrt{2} \cdot \sqrt{3} = \sqrt{6}$ |

**Kural.** "Kesinlikle" ya da "her zaman" soruluyorsa bir **karşı örnek** ara: $\sqrt{2}$ ile $-\sqrt{2}$, $\sqrt{2}$ ile $\sqrt{8}$ ya da $0$ çoğu yanlış seçeneği eler. $0 \cdot \sqrt{2} = 0$ olduğu için çarpımda "sıfırdan farklı" şartı önemlidir.

## Sayı doğrusunda yer bulma

**Örnek.** $\sqrt{5}$, $\frac{7}{3}$ ve $2{,}2$ sayılarını küçükten büyüğe sırala.

Üçü de pozitif; karelerini karşılaştırmak yeter (pozitif sayılarda büyük olanın karesi de büyüktür):

$$(2{,}2)^2 = 4{,}84 \qquad (\sqrt{5})^2 = 5 \qquad \left(\tfrac{7}{3}\right)^2 = \tfrac{49}{9} \approx 5{,}44$$

Sıralama: $2{,}2 < \sqrt{5} < \frac{7}{3}$.

![Eksi 3'ten 4'e sayı doğrusu. Eksi 7 bölü 3, eksi kök 2, 0,75, kök 5, e ve pi işaretli. Rasyoneller mavi, irrasyoneller kırmızı.](gorsel/tyt-matematik/01-01-sayi-dogrusu.svg "Rasyonel (mavi) ve irrasyonel (kırmızı) sayılar doğruda karışık dizilir. Kök 5, e ve pi'nin hepsi 2 ile 4 arasında; sıralarına dikkat et.")

Her gerçek sayıya sayı doğrusunda bir nokta karşılık gelir; irrasyonel sayılar da doğrunun üzerindedir. $\sqrt{5}$'in yeri cetvelle değil, **pergelle** tam olarak bulunabilir: kenarları 2 ve 1 birim olan dikdörtgenin köşegeni Pisagor'dan $\sqrt{2^2 + 1^2} = \sqrt{5}$'tir. Pergeli $0$'a koyup köşegeni doğruya indirirsin.

![Sayı doğrusunda 0'dan başlayan, 2 birim eninde 1 birim boyunda dikdörtgen. 0'dan karşı köşeye çizilen köşegen kök 5. Kesikli yay köşegeni doğruya indiriyor; yaklaşık 2,24'te kırmızı nokta.](gorsel/tyt-matematik/01-01-kok-bes.svg "Yay, köşegen uzunluğunu doğruya taşır. Nokta 2 ile 3 arasında ama 2'ye daha yakın, çünkü 5, 4'e 9'dan daha yakındır.")

**Kural.** $\sqrt{n}$'nin yerini bulmak için $n$'nin iki yanındaki tam kareleri bul: $k^2 < n < (k+1)^2$ ise $k < \sqrt{n} < k + 1$. Orta noktayı geçip geçmediğini anlamak için $(k + 0{,}5)^2$ ile karşılaştır.

## ÖSYM tuzakları

> **Kökü görünce irrasyonel demek:** $\sqrt{0{,}49} = 0{,}7$, $\sqrt{\frac{18}{2}} = 3$, $-\sqrt{16} = -4$. Önce sadeleştir, sonra karar ver.

> **$\frac{22}{7}$ ya da $3{,}14$'ü irrasyonel sanmak:** İkisi de $\pi$'nin yaklaşık değeridir ve rasyoneldir. İrrasyonel olan yalnızca $\pi$'nin kendisidir.

> **$0$'ı unutmak:** $0$ doğal sayıdır, tam sayıdır, rasyoneldir; ama pozitif değildir. "Kaç doğal sayı?" sorusunda $0$'ı say, "kaç sayma sayısı?" sorusunda sayma. $\sqrt{0} = 0$ da rasyoneldir.

> **"İki irrasyonelin çarpımı irrasyoneldir" demek:** $\sqrt{2} \cdot \sqrt{2} = 2$. "Kesinlikle" soruluyorsa karşı örnek dene.

> **Negatifin karekökünü bir kümeye koymak:** $\sqrt{-9}$ gerçek sayı belirtmez; "irrasyonel" seçeneği de yanlıştır.

## Kendini dene

### Soru 1
Aşağıdakilerden hangisi tam sayı olup doğal sayı **değildir**?

A) $-\sqrt{9}$
B) $-1{,}5$
C) $-\frac{1}{3}$
D) $0$
E) $\sqrt{4}$

**Cevap:** A
**Çözüm:** $-\sqrt{9} = -3$: tam sayıdır, negatif olduğu için doğal sayı değildir. $-1{,}5$ ve $-\frac{1}{3}$ tam sayı değildir. $0$ ve $\sqrt{4} = 2$ hem tam sayı hem doğal sayıdır.

### Soru 2
$\sqrt{30}$ sayısı hangi iki ardışık tam sayı arasındadır?

A) 4 ile 5
B) 5 ile 6
C) 6 ile 7
D) 14 ile 15
E) 15 ile 16

**Cevap:** B
**Çözüm:** $5^2 = 25 < 30 < 36 = 6^2$ olduğundan $5 < \sqrt{30} < 6$ (yaklaşık $5{,}48$). 15 ile 16, 30'u ikiye bölmekten gelir; karekök yarıya bölmek değildir.

### Soru 3
$a = \sqrt{3} + 1$ ve $b = \sqrt{3} - 1$ olduğuna göre

I. $a + b$
II. $a - b$
III. $a \cdot b$

ifadelerinden hangileri rasyonel sayıdır?

A) Yalnız I
B) Yalnız II
C) I ve II
D) II ve III
E) I, II ve III

**Cevap:** D
**Çözüm:** $a + b = 2\sqrt{3}$ irrasyonel. $a - b = (\sqrt{3} + 1) - (\sqrt{3} - 1) = 2$ rasyonel. $a \cdot b = 3 - 1 = 2$ rasyonel. Toplamda kökler birbirini götürmez; $a + b$'yi de rasyonel sanan E'yi, çarpımı hesaplamayan B'yi seçer.

## Özet kartı

- $\mathbb{N} \subset \mathbb{Z} \subset \mathbb{Q} \subset \mathbb{R}$; $\mathbb{Q} \cup \mathbb{Q}' = \mathbb{R}$, $\mathbb{Q} \cap \mathbb{Q}' = \varnothing$.
- $0$: doğal, tam, rasyonel; pozitif değil. Rakamlar 10 tanedir: $0$–$9$.
- Rasyonel: $\frac{a}{b}$ ($a, b \in \mathbb{Z}$, $b \ne 0$); sonlu ve devirli ondalıklar da rasyonel.
- Kökü önce sadeleştir: tam kare çıkarsa rasyonel, çıkmazsa irrasyonel. $\sqrt{\text{negatif}} \notin \mathbb{R}$.
- Rasyonel $\pm$ irrasyonel $=$ irrasyonel; irrasyonel ile irrasyonelin sonucu belli değildir.
- $k^2 < n < (k+1)^2$ ise $k < \sqrt{n} < k + 1$.

## Sonraki adım

Alıştırmaya geç (aşağıdaki düğme). Sonraki ders **Temel İşlemler**; işlem önceliği ve parantezle çalışırken buradaki küme adlarını soru kökünde sürekli göreceksin.
