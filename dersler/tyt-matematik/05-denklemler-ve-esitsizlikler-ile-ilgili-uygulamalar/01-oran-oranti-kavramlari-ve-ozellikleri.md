---
baslik: Oran-Orantı Kavramları ve Özellikleri
ders: tyt-matematik
sure: 20 dk
kaynak: MEBİ Konu Özeti db2747c6b2
guncelleme: 2026-11-17
---
# Oran-Orantı Kavramları ve Özellikleri

**Bu dersin sonunda:** bir orantıda bilinmeyeni içler-dışlar çarpımıyla ve orantı sabitiyle bulabilecek, orantının özelliklerini kullanarak kesirli ifadeleri hesaplamadan değerlendirebilecek ve iki çokluğun doğru mu ters mi orantılı olduğunu ayırt edip problem çözebileceksin.

> **TYT'de yeri:** Oran-orantıdan her yıl doğrudan 1–2 soru gelir; ayrıca yaş, işçi, karışım ve hız problemlerinin çoğu orantıyla kurulur. Kalıplar: "$\frac{a}{3} = \frac{b}{5}$ ve $a + b = 24$ ise…", "$a$ ile $b$ doğru, $c$ ile ters orantılı…", "tarifteki oran bozulmadan en çok kaç…" ve grafikten oran okuma.

## Önce hatırla

<details><summary>Köklü denklemlerden: $\sqrt{x + 6} - 2 = 3$ olduğuna göre $x$ kaçtır?</summary>
Önce kökü yalnız bırak: $\sqrt{x + 6} = 5$. Sonra kare al: $x + 6 = 25$, yani <b>$x = 19$</b>. Sağlama: $\sqrt{25} - 2 = 3$.
</details>

<details><summary>Köklü eşitsizliklerden: $\sqrt{x - 2} < 4$ eşitsizliğini sağlayan kaç $x$ tam sayısı vardır?</summary>
Tanım koşulu: $x - 2 \ge 0$, yani $x \ge 2$. İki taraf negatif değil, kare al: $x - 2 < 16$, yani $x < 18$. Birlikte $2 \le x < 18$: $2, 3, \dots, 17$, toplam <b>16 tam sayı</b>.
</details>

## Oran: iki çokluğu bölerek karşılaştırmak

**Örnek.** Bir sınıfta 12 kız, 18 erkek öğrenci var.

- Kızların erkeklere oranı: $\frac{12}{18} = \frac{2}{3}$. Her 2 kıza karşılık 3 erkek var.
- Kızların sınıf mevcuduna oranı: $\frac{12}{30} = \frac{2}{5}$.

İki cevap farklı. Soruda "neyin neye oranı" dendiğine bak: birincisi **parça : parça**, ikincisi **parça : bütün**.

**Örnek (birim).** 40 cm'lik bir ipin 2 m'lik bir ipe oranı nedir? $\frac{40}{2} = 20$ yanlıştır. Önce aynı birime çevir: $2 \text{ m} = 200 \text{ cm}$, oran $\frac{40}{200} = \frac{1}{5}$.

**Kural.** Aynı türden iki çokluğun bölme yoluyla karşılaştırılmasına **oran** denir; $\frac{a}{b}$ ya da $a : b$ diye yazılır ($b \ne 0$). Oran yazmadan önce birimleri eşitle; oranın birimi yoktur.

## Orantı ve içler-dışlar çarpımı

İki oranın eşitliğine **orantı** denir: $\frac{a}{b} = \frac{c}{d}$ ya da $a : b = c : d$. Bu yazımda $b$ ve $c$ **içler**, $a$ ve $d$ **dışlar** adını alır.

![4 : 6 = 10 : 15 orantısı. Ortadaki 6 ve 10 mavi bir yayla birleştirilmiş, içler; çarpımları 60. Uçtaki 4 ve 15 kırmızı bir yayla birleştirilmiş, dışlar; çarpımları da 60.](gorsel/tyt-matematik/05-01-icler-dislar.svg "Ortadaki iki sayı içler, uçtaki iki sayı dışlar. Orantı doğruysa iki çarpım hep eşit çıkar.")

**Örnek.** $\frac{x}{6} = \frac{10}{15}$ ise $x$ kaçtır?

İçler-dışlar çarpımı: $15x = 6 \cdot 10 = 60$, yani $x = 4$.

**Örnek.** $\frac{x + 1}{x - 2} = \frac{5}{2}$ ise $x$ kaçtır?

Çapraz çarp: $2(x + 1) = 5(x - 2)$. Düzenle: $2x + 2 = 5x - 10$, $3x = 12$, $x = 4$. Kontrol: $\frac{5}{2}$.

**Kural.** $\frac{a}{b} = \frac{c}{d}$ ise $a \cdot d = b \cdot c$ (dışlar çarpımı = içler çarpımı). Ayrıca içler kendi arasında, dışlar kendi arasında yer değiştirebilir:

$$\frac{a}{b} = \frac{c}{d} \;\Rightarrow\; \frac{a}{c} = \frac{b}{d} \quad \text{ve} \quad \frac{d}{b} = \frac{c}{a}$$

## Orantı sabiti $k$: her şeyi $k$ cinsinden yaz

**Örnek.** $\frac{a}{3} = \frac{b}{5} = \frac{c}{7}$ ve $a + b + c = 45$ ise $a$, $b$, $c$ kaçtır?

Oranların ortak değerine $k$ de: $a = 3k$, $b = 5k$, $c = 7k$. Toplam $15k = 45$, yani $k = 3$. Buradan $a = 9$, $b = 15$, $c = 21$.

![Üç satır kutu: a için 3 mavi kutu, b için 5 yeşil kutu, c için 7 sarı kutu. Her kutunun içinde 3 yazıyor; satır sonlarında 9, 15 ve 21. Altta: 15 kutu 45 ise 1 kutu 3.](gorsel/tyt-matematik/05-01-birim-kutular.svg "Her sayıyı kutu sayısı kadar parça gibi düşün. Bir kutunun değeri orantı sabiti k'dir; toplamı kutu sayısına bölünce bulunur.")

**Kural.** $\frac{a}{b} = \frac{c}{d} = k$ eşitliğindeki $k$'ye **orantı sabiti** denir. $\frac{a}{x} = \frac{b}{y} = \frac{c}{z} = k$ ise $a = xk$, $b = yk$, $c = zk$ yaz ve verilen koşula yerleştir. Bu yazım $a : b : c = x : y : z$ ile aynı anlamdadır.

Fark verilirse de aynı yol: $\frac{a}{3} = \frac{b}{5}$ ve $b - a = 8$ ise $5k - 3k = 2k = 8$, $k = 4$.

## Orantının özellikleri

**Örnek.** $\frac{a}{b} = \frac{c}{d} = \frac{3}{4}$ olsun. Sayıları bilmeden şu ifadeleri bul.

- $\frac{a + c}{b + d}$: payları ve paydaları topladın, sabit değişmez: $\frac{3}{4}$.
- $\frac{2a + 3c}{2b + 3d}$: birinci oranı 2, ikinciyi 3 ile genişletip topladın: yine $\frac{3}{4}$.
- $\frac{a \cdot c}{b \cdot d}$: oranları çarptın: $\frac{3}{4} \cdot \frac{3}{4} = \frac{9}{16}$.

Neden? $a = 3t$, $b = 4t$, $c = 3s$, $d = 4s$ yaz: $\frac{2a + 3c}{2b + 3d} = \frac{6t + 9s}{8t + 12s} = \frac{3(2t + 3s)}{4(2t + 3s)} = \frac{3}{4}$.

**Kural.** $\frac{a}{b} = \frac{c}{d} = k$ ise ($m$, $n$ sıfırdan farklı, paydalar sıfır değil):

| İşlem | Sonuç |
|---|---|
| Payları ve paydaları topla | $\frac{a + c}{b + d} = k$ |
| Aynı katsayılarla genişletip topla | $\frac{m a + n c}{m b + n d} = k$ |
| Oranları çarp | $\frac{a \cdot c}{b \cdot d} = k^2$ |

Payda ve paydada **aynı katsayılar** kullanılmalıdır. $\frac{a + 2c}{b + 3d}$ ifadesi genelde $k$ değildir. Örneğin $a = 3$, $b = 4$, $c = 6$, $d = 8$ için $\frac{3 + 12}{4 + 24} = \frac{15}{28} \ne \frac{3}{4}$.

**Örnek (çarpım).** $\frac{a}{b} = \frac{c}{d}$, pozitif sayılarla $a \cdot c = 48$ ve $b \cdot d = 12$ ise orantı sabiti nedir? $k^2 = \frac{48}{12} = 4$, $k > 0$ olduğundan $k = 2$.

## Doğru orantı

**Örnek.** 3 kg elma 45 TL ise 7 kg elma kaç TL'dir?

Kilogram fiyatı sabittir: $\frac{45}{3} = 15$. 7 kg: $7 \cdot 15 = 105$ TL. Orantıyla: $\frac{45}{3} = \frac{y}{7}$, $y = 105$.

![Yatay eksende elma kilogramı, dikey eksende fiyat. Orijinden geçen mavi doğru üzerinde 3 kg için 45 TL ve 7 kg için 105 TL noktaları işaretli; ikisinde de bölüm 15.](gorsel/tyt-matematik/05-01-dogru-oranti.svg "Doğru orantının grafiği orijinden geçen bir doğrudur. Doğru üzerindeki her noktada y bölü x aynı sayıdır.")

**Kural.** İki çokluktan biri kaç katına çıkınca öbürü de aynı katına çıkıyorsa (ya da ikisi aynı oranda azalıyorsa) bu çokluklar **doğru orantılıdır**:

$$\frac{y}{x} = k \quad \text{yani} \quad y = k \cdot x$$

## Ters orantı

**Örnek.** Aynı hızda çalışan 6 işçi bir işi 10 günde bitiriyor. 4 işçi aynı işi kaç günde bitirir?

İşçi azalınca gün artar. İşin büyüklüğü sabittir: $6 \cdot 10 = 60$ işçi-gün. 4 işçi: $\frac{60}{4} = 15$ gün.

![Yatay eksende işçi sayısı, dikey eksende gün. Kırmızı eğri x çarpı y eşittir 60. Eğri üzerindeki 4 işçi 15 gün ve 6 işçi 10 gün noktalarından eksenlere dikdörtgenler çizilmiş; ikisinin de alanı 60.](gorsel/tyt-matematik/05-01-ters-oranti.svg "Ters orantıda çarpım sabittir. Eğri üzerindeki hangi noktayı seçersen seç, eksenlerle oluşan dikdörtgenin alanı 60 çıkar.")

**Kural.** Biri kaç katına çıkınca öbürü aynı sayıya bölünüyorsa çokluklar **ters orantılıdır**:

$$x \cdot y = k \quad \text{yani} \quad y = \frac{k}{x}$$

### Birden fazla çokluk

**Örnek.** $a$, $b$ ile doğru, $c$ ile ters orantılıdır. $b = 4$, $c = 2$ iken $a = 6$. $b = 9$, $c = 3$ iken $a$ kaçtır?

Doğru orantılı olan paya, ters orantılı olan paydaya yazılır: $a = k \cdot \frac{b}{c}$. Önce $k$: $6 = k \cdot \frac{4}{2}$, $k = 3$. Sonra $a = 3 \cdot \frac{9}{3} = 9$.

**Kural.** "$a$, $b$ ile doğru, $c$ ile ters orantılı" ise $\frac{a \cdot c}{b} = k$. Önce verilen değerlerle $k$'yi bul, sonra yeni değerleri yerleştir.

## ÖSYM tuzakları

> **Parça ile bütünü karıştırmak:** "Kızların sınıfa oranı" ile "kızların erkeklere oranı" farklıdır. 12 kız 18 erkekte biri $\frac{2}{5}$, öbürü $\frac{2}{3}$'tür.

> **Birlikte artan her şeyi doğru orantılı sanmak:** $y = x + 3$ olsun; $x$ artınca $y$ de artar ama $\frac{y}{x}$ sabit değildir ($x = 1$ için 4, $x = 2$ için $\frac{5}{2}$). Doğru orantıda **bölüm** sabittir, fark değil.

> **Katsayıları eşleştirmeden toplamak:** $\frac{a}{b} = \frac{c}{d} = k$ ise $\frac{2a + 3c}{2b + 3d} = k$ olur, ama $\frac{a + 2c}{b + 3d}$ genelde $k$ değildir.

> **Oranları çarpınca $k$ demek:** $\frac{a \cdot c}{b \cdot d}$ sorulursa cevap $k^2$'dir; üç oran çarpılırsa $k^3$.

> **Ters orantıyı doğru orantı gibi kurmak:** 6 işçi 10 günde bitiren işi 4 işçi $\frac{4 \cdot 10}{6}$ günde değil, $\frac{6 \cdot 10}{4} = 15$ günde bitirir. Önce "biri artınca öbürü artar mı, azalır mı?" diye sor.

## Kendini dene

### Soru 1
$\frac{a}{5} = \frac{b}{2}$ ve $a + b = 28$ olduğuna göre $a$ kaçtır?

A) 8
B) 10
C) 14
D) 20
E) 24

**Cevap:** D
**Çözüm:** $a = 5k$, $b = 2k$ yaz. $5k + 2k = 7k = 28$, $k = 4$. $a = 5 \cdot 4 = 20$ ($b = 8$). A seçeneği $b$'yi, C seçeneği toplamın yarısını alır.

### Soru 2
$a, b, c, d$ pozitif sayılar olmak üzere $\frac{a}{b} = \frac{c}{d} = \frac{2}{5}$ ve $a \cdot c = 24$ olduğuna göre $b \cdot d$ çarpımı kaçtır?

A) 60
B) 96
C) 120
D) 150
E) 240

**Cevap:** D
**Çözüm:** Oranları çarp: $\frac{a \cdot c}{b \cdot d} = \left(\frac{2}{5}\right)^2 = \frac{4}{25}$. Buradan $b \cdot d = 24 \cdot \frac{25}{4} = 150$. Kareyi unutup $\frac{a \cdot c}{b \cdot d} = \frac{2}{5}$ alan $24 \cdot \frac{5}{2} = 60$ bulur.

### Soru 3
Bir duvarın örülme süresi, işçi sayısıyla ters, duvarın uzunluğuyla doğru orantılıdır. 6 işçi 120 m duvarı 10 günde örüyor. Aynı hızda çalışan 8 işçi 192 m duvarı kaç günde örer?

A) 9
B) 10
C) 12
D) 16
E) 20

**Cevap:** C
**Çözüm:** Süre $t = k \cdot \frac{\text{uzunluk}}{\text{işçi}}$. $10 = k \cdot \frac{120}{6}$, $k = \frac{1}{2}$. Yeni süre $t = \frac{1}{2} \cdot \frac{192}{8} = 12$ gün. İşçi sayısını hesaba katmayan $10 \cdot \frac{192}{120} = 16$ bulur.

## Özet kartı

- Oran = aynı türden iki çokluğun bölümü; önce birimleri eşitle, "neyin neye" oranı sorulduğuna bak.
- $\frac{a}{b} = \frac{c}{d}$ ise $a \cdot d = b \cdot c$ (içler çarpımı = dışlar çarpımı).
- $\frac{a}{x} = \frac{b}{y} = \frac{c}{z} = k$ ise $a = xk$, $b = yk$, $c = zk$ yaz ve koşulu kullan.
- $\frac{m a + n c}{m b + n d} = k$ (aynı katsayılar); $\frac{a \cdot c}{b \cdot d} = k^2$.
- Doğru orantı: $\frac{y}{x} = k$, grafik orijinden geçen doğru. Ters orantı: $x \cdot y = k$.
- Doğru orantılı olan paya, ters orantılı olan paydaya: $a = k \cdot \frac{b}{c}$.

## Sonraki adım

Alıştırmaya geç (aşağıdaki düğme). Gerçek çıkmış soruları görmek için MEBİ'deki bu konunun "Çıkmış Sorular" testini ve ÖSYM'nin yayımladığı TYT kitapçıklarını kullan. Bu dersteki $k$ yöntemini sayı, kesir, yaş ve işçi problemlerinde sürekli kullanacaksın.
