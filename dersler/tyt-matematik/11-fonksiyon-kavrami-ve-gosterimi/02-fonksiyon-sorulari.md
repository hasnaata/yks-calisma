---
baslik: Fonksiyon Soruları
ders: tyt-matematik
sure: 25 dk
kaynak: MEBİ Konu Özeti 02dbcbc400
guncelleme: 2026-11-18
---
# Fonksiyon Soruları

<div class="giris" dir="rtl" lang="ar">

**الدرس ده عن إيه؟** عن أشهر أنواع مسائل الدوال (fonksiyon): إزاي تطلّع القيمة المطلوبة من القاعدة اللي في السؤال، حتى لو جوه القوس تعبير مش رقم.

- هتعرف إمتى تساوي اللي جوه القوس بالرقم على طول، وإمتى تسمّيه حرف جديد عشان تجيب قاعدة الدالة كلها.
- هتتعلم تحسب المعاملات المجهولة من نقط على الرسم، وتجيب المدى (görüntü kümesi) من المجال (tanım kümesi).
- هتحل المساويات اللي فيها قيمتين للدالة مع بعض، بإنك تعوّض بأرقام مناسبة وتعمل معادلتين.

**ليه مهم؟** سؤال الدالة في TYT غالبًا حساب قيمة، والغلط بيبقى في تفصيلة صغيرة زي قوس الرقم السالب أو طرف الفترة، وكل ده متوضّح هنا.

٢٥ دقيقة وهتلاقي المسائل دي بقت سهلة عليك، يلا بينا.

</div>

**Bu dersin sonunda:** $f(2x + 3)$ gibi verilen bir kuraldan istenen değeri ya da $f(x)$'i bulabilecek, bilinmeyen katsayıyı hesaplayabilecek, bir aralığın görüntüsünü yazabilecek ve iki değeri birbirine bağlayan eşitliklerden denklem sistemi kurabileceksin.

> **TYT'de yeri:** TYT'de fonksiyon sorusu çoğunlukla değer hesabıdır: "$f(3x - 1) = \dots$ ise $f(5)$ kaçtır?", "$f(2) = 7$ ise $a$ kaçtır?", "tanım kümesi bu aralık ise görüntü kümesi nedir?". Yeni nesil sorularda fonksiyon bir ücret, sıcaklık ya da su miktarı olarak gelir; işlem azdır, doğru yere doğru sayıyı yazmak gerekir.

## Önce hatırla

<details><summary>Fonksiyon kavramından: s(A) = 3 ve s(B) = 2 ise A'dan B'ye kaç fonksiyon tanımlanabilir?</summary>
$A$'nın her elemanı için 2 seçenek vardır: $2^3 = 8$. Üs tanım kümesinin eleman sayısıdır; $3^2 = 9$ yanlıştır.
</details>

<details><summary>Fonksiyon kavramından: A = {1, 2, 3} olmak üzere f = {(1, a + 2), (2, 5), (3, 4), (1, 7)} kümesi A'dan bir fonksiyondur. a kaçtır?</summary>
$1$ iki ikilide birinci bileşen. Fonksiyonda $1$'in tek görüntüsü olmalı: $a + 2 = 7$, $a = 5$.
</details>

## Kuraldan değer bulmak

**Örnek.** $f(x) = 2x^2 - x + 1$ ise $f(-2)$ kaçtır?

$x$ gördüğün her yere $(-2)$ yaz, **parantezle**:

$$f(-2) = 2 \cdot (-2)^2 - (-2) + 1 = 8 + 2 + 1 = 11$$

**Örnek.** $f(x) = 3x - 2$ ise $f(x + 1)$ ve $f(2a)$ nedir?

$x$ yerine bu kez bir ifade yazılır: $f(x + 1) = 3(x + 1) - 2 = 3x + 1$ ve $f(2a) = 3 \cdot 2a - 2 = 6a - 2$. Buradan $f(x + 1) - f(x) = (3x + 1) - (3x - 2) = 3$ bulunur.

**Kural.** $f(\square)$ istendiğinde kuraldaki **her** $x$'in yerine $\square$ yazılır, parantez içinde. Kutunun içinde sayı da olabilir, $x + 1$ gibi bir ifade de.

## Parantez içi ifade olunca: $f(2x + 3)$

**Örnek.** $f(2x + 3) = x^2 - x + 4$ ise $f(7)$ kaçtır?

$f(7)$ için parantezin içi $7$ olmalı: $2x + 3 = 7$, $x = 2$. Şimdi sağ tarafta $x = 2$ yaz:

$$f(7) = 2^2 - 2 + 4 = 6$$

**Örnek.** $f(2x + 3) = 4x + 1$ ise $f(x)$ nedir?

Parantezin içine yeni bir ad ver: $2x + 3 = t$. Buradan $x = \frac{t - 3}{2}$. Sağ tarafta $x$'i $t$ cinsinden yaz:

$$f(t) = 4 \cdot \frac{t - 3}{2} + 1 = 2t - 5 \quad\Rightarrow\quad f(x) = 2x - 5$$

Kontrol: $f(2x + 3) = 2(2x + 3) - 5 = 4x + 1$. Doğru.

![Akış şeması: f(2x + 3) verildi; ne isteniyor? Tek değer f(7) isteniyorsa 2x + 3 = 7 çöz, x = 2'yi yerine yaz. Kural f(x) isteniyorsa 2x + 3 = t de, x'i t cinsinden yaz.](gorsel/tyt-matematik/11-02-yontem.svg "Önce ne istendiğine bak. Tek değer için t'ye gerek yok; parantezi o sayıya eşitlemen yeter.")

Bazen sağ taraf parantezdeki ifadeyle yazılabilir; bu daha hızlıdır. $f(2x - 1) = 4x^2 - 4x + 6$ verilsin. $(2x - 1)^2 = 4x^2 - 4x + 1$ olduğundan sağ taraf $(2x - 1)^2 + 5$ olur. Kutu $2x - 1$ olduğuna göre $f(x) = x^2 + 5$.

**Kural.** $f(ax + b)$ verildiğinde:

- **Tek değer** $f(c)$ isteniyorsa $ax + b = c$ denkleminden $x$'i bul, sağ tarafa yaz.
- **Kural** $f(x)$ isteniyorsa $ax + b = t$ de, $x$'i $t$ cinsinden yazıp yerine koy; sonunda $t$ yerine $x$ yaz.

## Bilinmeyen katsayı

**Örnek.** $f(x) = ax + b$ fonksiyonunun grafiği aşağıda verilmiştir. $f(5)$ kaçtır?

![Koordinat düzleminde artan bir doğru. Doğru (0, −2) ve (3, 4) noktalarından geçiyor; bu iki nokta kırmızı ile işaretli.](gorsel/tyt-matematik/11-02-katsayi-grafik.svg "Grafik üzerindeki her nokta bir (x, f(x)) ikilisidir. İşaretli iki noktadan iki denklem çıkar.")

Grafikteki her nokta bir $(x, f(x))$ ikilisidir:

- $(0, -2)$: $f(0) = b = -2$.
- $(3, 4)$: $f(3) = 3a - 2 = 4$, yani $a = 2$.

$f(x) = 2x - 2$, $f(5) = 10 - 2 = 8$.

**Kural.** Kuralda bilinmeyen kaç katsayı varsa o kadar bilgi gerekir. Her $(x, f(x))$ ikilisi (verilen bir değer ya da grafikteki bir nokta) bir denklem verir. $x = 0$ noktası çoğunlukla sabit terimi doğrudan verir.

## Tanım kümesinden görüntü kümesine

**Örnek.** $f(x) = 2x + 1$ ve tanım kümesi $(-1, 3]$ ise görüntü kümesi nedir?

Uçların görüntülerini bul: $f(-1) = -1$, $f(3) = 7$. $-1$ tanım kümesinde **yok**, bu yüzden görüntüsü de yok. $3$ var, görüntüsü $7$ de var. Görüntü kümesi $(-1, 7]$.

![İki sayı doğrusu. Üstte x için −1 boş, 3 dolu nokta. Altta f(x) için −1 boş, 7 dolu nokta. Oklar −1'i −1'e, 3'ü 7'ye götürüyor.](gorsel/tyt-matematik/11-02-goruntu-araligi.svg "Uç noktanın dolu ya da boş olması görüntüsüne aynen geçer.")

Fonksiyon azalan olursa uçlar yer değiştirir. $f(x) = 5 - x$ ve tanım kümesi $[0, 2)$ ise $f(0) = 5$ (dahil), $f(2) = 3$ (dahil değil). Küçük sayı solda yazılır: görüntü kümesi $(3, 5]$.

**Örnek.** $f(x) = x^2$ ve tanım kümesi $[-2, 3]$ ise görüntü kümesi nedir?

Yalnız uçlara bakarsan $f(-2) = 4$ ve $f(3) = 9$ bulursun. Ama aralığın içinde $0$ var ve $f(0) = 0$. $x^2$ hiçbir zaman negatif olmaz, en küçük değeri $0$'dır. Görüntü kümesi $[0, 9]$, $[4, 9]$ değil.

![y = x kare eğrisinin −2 ile 3 arasındaki parçası mavi. f(−2) = 4, f(0) = 0, f(3) = 9 noktaları işaretli; y ekseninde 0'dan 9'a yeşil bir şerit görüntü kümesini gösteriyor.](gorsel/tyt-matematik/11-02-parabol.svg "En küçük değer uçta değil, aralığın içinde, x = 0'da. Yeşil şerit 0'dan başlar.")

**Kural.** $ax + b$ gibi birinci dereceden fonksiyonlarda uçların görüntüsü yeter; dahil olma durumu korunur, küçük sayı sola yazılır. $x^2$ gibi çift dereceli terim varsa ya da fonksiyon parçalı verilmişse **kritik noktalara** (örneğin $x = 0$'a ya da parçaların birleştiği yere) ayrıca bak.

## İki değeri bağlayan eşitlikler

**Örnek.** Her $x$ gerçek sayısı için $f(x) + 2 \cdot f(2 - x) = 4x - 1$ ise $f(0)$ kaçtır?

Eşitlikte $f(x)$ ve $f(2 - x)$ var. $x = 0$ ve $x = 2$ yazınca aynı iki bilinmeyen çıkar:

- $x = 0$: $f(0) + 2 f(2) = -1$
- $x = 2$: $f(2) + 2 f(0) = 7$

İkinci denklemden $f(2) = 7 - 2f(0)$. Birinciye yaz: $f(0) + 14 - 4f(0) = -1$, $f(0) = 5$. Buradan $f(2) = -3$. Kontrol: $5 + 2(-3) = -1$.

**Örnek.** $f(x + 1) = f(x) + 2$ ve $f(1) = 3$ ise $f(6)$ kaçtır?

$x$ bir artınca değer 2 artıyor. $1$'den $6$'ya $6 - 1 = 5$ adım var: $f(6) = 3 + 5 \cdot 2 = 13$.

**Kural.** Eşitlikte iki farklı $f(\dots)$ varsa, $x$ yerine bu iki değeri birbirine çeviren sayıları yaz ve oluşan iki denklemi yerine koyma ya da yok etme ile çöz. $f(x + 1) = f(x) + k$ biçiminde her adımda $k$ eklenir; adım sayısı iki girdinin farkıdır.

## ÖSYM tuzakları

> **Sayıyı doğrudan yazmak:** $f(2x + 3) = x^2 - x + 4$ ise $f(7)$ için $x = 7$ yazılmaz. Önce $2x + 3 = 7$ denkleminden $x = 2$ bulunur; $x = 7$ yazan $46$ bulur.

> **Negatif sayıyı parantezsiz yazmak:** $f(x) = 2x^2 - x + 1$ için $-2^2 = -4$ değil, $(-2)^2 = 4$ yazılır; $-x$ terimi de $-(-2) = +2$ olur.

> **Azalan fonksiyonda uçları karıştırmak:** $f(x) = 5 - x$, $x \in [0, 2)$ için görüntü $[5, 3)$ diye yazılmaz. Dahil olan $5$'tir: $(3, 5]$.

> **Kritik noktayı atlamak:** $f(x) = x^2$, $x \in [-2, 3]$ için görüntü kümesi $[4, 9]$ değil, $[0, 9]$'dur.

> **Adım sayısını yanlış saymak:** $f(x + 1) = f(x) + 2$ ve $f(1) = 3$ ise $f(6)$ için 6 değil, 5 adım vardır.

## Kendini dene

### Soru 1
$f(x) = x^2 - 2x + 3$ olduğuna göre $f(-1) + f(2)$ toplamı kaçtır?

A) 5
B) 6
C) 7
D) 9
E) 11

**Cevap:** D
**Çözüm:** $f(-1) = (-1)^2 - 2(-1) + 3 = 1 + 2 + 3 = 6$. $f(2) = 4 - 4 + 3 = 3$. Toplam $6 + 3 = 9$. $-2x$ terimini $-2$ alan $f(-1) = 2$ bulur ve toplamı 5 yapar.

### Soru 2
$f(3x + 1) = 6x - 5$ olduğuna göre $f(x)$ aşağıdakilerden hangisidir?

A) $2x - 3$
B) $2x - 7$
C) $2x - 5$
D) $6x - 5$
E) $18x + 1$

**Cevap:** B
**Çözüm:** $3x + 1 = t$ dersen $x = \frac{t - 1}{3}$. $f(t) = 6 \cdot \frac{t - 1}{3} - 5 = 2t - 2 - 5 = 2t - 7$. Yani $f(x) = 2x - 7$. Kontrol: $2(3x + 1) - 7 = 6x - 5$. $18x + 1$, sağ taraftaki $x$ yerine $3x + 1$ yazmaktan gelir; ters yöndür.

### Soru 3
$f(x) = 4 - x$ fonksiyonunun tanım kümesi $(-2, 3]$ olduğuna göre görüntü kümesi aşağıdakilerden hangisidir?

A) $(1, 6]$
B) $[1, 6]$
C) $(1, 6)$
D) $(-2, 3]$
E) $[1, 6)$

**Cevap:** E
**Çözüm:** $f(-2) = 6$; $-2$ dahil değil, $6$ da dahil değil. $f(3) = 1$; $3$ dahil, $1$ de dahil. Küçük sayı solda: $[1, 6)$. Parantezleri olduğu gibi taşıyan A seçeneğine gider; fonksiyon azalan olduğu için uçlar yer değiştirir.

## Özet kartı

- $f(\square)$: kuraldaki her $x$ yerine $\square$, parantez içinde.
- $f(ax + b)$ verildi, $f(c)$ isteniyor: $ax + b = c$ çöz, bulduğun $x$'i yaz.
- $f(ax + b)$ verildi, $f(x)$ isteniyor: $ax + b = t$ de, $x$'i $t$ cinsinden yaz.
- Her $(x, f(x))$ ikilisi bir denklem verir; bilinmeyen kadar ikili gerekir.
- Görüntü kümesi: uçların görüntüsü, dahil olma durumu korunur; çift dereceli ya da parçalı fonksiyonda kritik noktaya bak.
- İki farklı $f(\dots)$ içeren eşitlikte uygun iki $x$ değeri yaz, sistem kur.

## Sonraki adım

Alıştırmaya geç (aşağıdaki düğme). Sonraki ders **İçine, Örten, Birebir ve Eşit Fonksiyonlar**; bir fonksiyonun örten olup olmadığına karar verirken bu derste bulduğun görüntü kümesini değer kümesiyle karşılaştıracaksın.
