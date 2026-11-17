---
baslik: Üçgende Kenar Orta Dikme
ders: tyt-matematik
sure: 20 dk
kaynak: MEBİ Konu Özeti 22984e2f0a
guncelleme: 2026-11-18
---
# Üçgende Kenar Orta Dikme

<div class="giris" dir="rtl" lang="ar">

**الدرس ده عن إيه؟** عن محور الضلع (kenar orta dikme) في المثلث: الخط اللي بيعدّي من نص الضلع وبيبقى عمودي عليه.

- هتعرف إن أي نقطة على محور الضلع بتبعد نفس المسافة عن طرفين الضلع، وإزاي تستخدم ده في أسئلة المحيط (çevre) والزوايا.
- هتشوف إن المحاور التلاتة بيتقابلوا في نقطة واحدة K بعيدة بنفس المسافة عن الرؤوس التلاتة، وهي مركز الدايرة المارة برؤوس المثلث (çevrel çember).
- هتتعلم مكان K حسب نوع المثلث: جوّه في حاد الزوايا، في نص الوتر في القائم، وبره في منفرج الزاوية، وكمان حالة المثلث المتساوي الساقين والمتساوي الأضلاع.

**ليه مهم؟** أسئلة TYT في الحتة دي غالبًا بتعتمد على فكرة واحدة بس، والفخ المشهور إنك تخلط بين النقطة دي ونقطة تقاطع الارتفاعات أو منصّفات الزوايا.

الدرس ٢٠ دقيقة، فكرته بسيطة وهتلاقيها بتسهّل عليك أسئلة كتير. يلا بينا.

</div>

**Bu dersin sonunda:** kenar orta dikme üzerindeki bir noktanın kenarın iki ucuna eşit uzaklıkta olduğunu ve üç kenar orta dikmenin kesim noktası $K$'nin üç köşeye eşit uzaklıkta olduğunu kullanarak bir çevreyi, bir açıyı ya da $|KA|$ uzunluğunu bulabileceksin.

> **TYT'de yeri:** Kenar orta dikme soruları çoğu zaman tek bir bilgiye dayanır: dikme üzerindeki nokta kenarın iki ucuna eşit uzaklıktadır. Bu bilgi ya bir çevre sorusunda bir kenarın yerine öbürünü yazdırır ya da bir ikizkenar üçgen kurdurup açı buldurur. "Üç köşeye eşit uzaklıkta bir nokta" (depo, kule, lamba) diye başlayan günlük hayat soruları da bu konudandır.

## Önce hatırla

<details><summary>Geçen dersten: Bir dik üçgende üç yükseklik hangi noktada kesişir?</summary>
Dik açılı köşede. Dik kenarların ikisi de birer yüksekliktir; ikisi dik açının köşesinde buluşur, üçüncü yükseklik de oradan geçer. Bugün kenar orta dikmelerin dik üçgende başka bir yerde, <b>hipotenüsün orta noktasında</b> kesiştiğini göreceksin. İkisini karıştırma.
</details>

<details><summary>Geçen dersten: Bir kenarı 8 birim olan eşkenar üçgenin yüksekliği kaç birimdir?</summary>
Eşkenar üçgende yükseklik $\dfrac{a\sqrt{3}}{2}$'dir: $\dfrac{8\sqrt{3}}{2} = $ <b>$4\sqrt{3}$</b>. Bu yükseklik aynı zamanda kenarortay ve açıortaydır. Bugün aynı doğrunun kenar orta dikme de olduğunu göreceksin.
</details>

## Kenar orta dikme nedir?

Bir kenarın **orta noktasından** geçen ve o kenara **dik** olan doğruya o kenarın **kenar orta dikmesi** denir. İki koşul birden gerekir: ortadan geçecek, dik olacak.

Kenar orta dikme bir köşeden çıkmak zorunda değildir. Bu yönüyle kenarortaydan (köşeden orta noktaya) ve yükseklikten (köşeden dik iner) ayrılır.

## 1. Dikme üzerindeki nokta iki uca eşit uzaklıktadır

**Örnek.** $ABC$ üçgeninde $|AB| = 10$, $|AC| = 7$, $|BC| = 12$'dir. $[AB]$'nin kenar orta dikmesi $d$, $[BC]$'yi $D$ noktasında kesiyor. $ADC$ üçgeninin çevresi kaçtır?

![ABC üçgeni: AB 10, AC 7, BC 12. AB'nin orta noktası M'den AB'ye dik kırmızı kesikli d doğrusu BC'yi D'de kesiyor. AM ile MB tek çentikle, DA ile DB çift çentikle eş işaretli. ADC üçgeni mavi boyalı.](gorsel/tyt-matematik/20-05-esit-uzaklik.svg "Çift çentikler DA ile DB'nin eşit olduğunu gösterir. Mavi ADC üçgeninin çevresinde DA yerine DB yazınca DB + DC = BC olur.")

**Çözüm.**

1. $D$, $[AB]$'nin kenar orta dikmesi üzerindedir. $AMD$ ve $BMD$ üçgenlerinde $|AM| = |MB|$, $[MD]$ ortak ve $M$'deki açılar $90^\circ$; bu iki üçgen eştir. O halde $|DA| = |DB|$.
2. $\text{Ç}(ADC) = |DA| + |DC| + |AC| = |DB| + |DC| + |AC|$.
3. $|DB| + |DC| = |BC| = 12$. Çevre $= 12 + 7 = 19$.

$|DA|$'yı tek başına bulmana gerek yoktu (zaten $6{,}15$ civarında, tam olmayan bir sayıdır).

**Kural:** $d$, $[AB]$'nin kenar orta dikmesi ve $P$, $d$ üzerinde ise

$$|PA| = |PB|$$

Tersi de doğrudur: $A$ ve $B$'ye eşit uzaklıktaki her nokta $[AB]$'nin kenar orta dikmesi üzerindedir.

**Açıya etkisi:** $|DA| = |DB|$ olduğu için $DAB$ ikizkenardır: $m(\widehat{DAB}) = m(\widehat{B})$. Örneğin $m(\widehat{B}) = 30^\circ$ ise $m(\widehat{DAB}) = 30^\circ$ ve dış açı kuralıyla $m(\widehat{ADC}) = 60^\circ$ olur.

> **Tuzak:** Dikmenin kestiği nokta ($D$) genelde **orta nokta değildir**. $D$, $[BC]$'yi ortalamaz; ortalanan kenar, dikmenin ait olduğu $[AB]$'dir. Eşit olan parçalar $|AM| = |MB|$ ve $|DA| = |DB|$'dir.

## 2. Üç kenar orta dikme bir noktada kesişir

Bir üçgenin üç kenar orta dikmesi her zaman **tek bir noktada** kesişir. Bu noktaya $K$ diyelim. $K$, $[BC]$'nin dikmesi üzerinde olduğu için $|KB| = |KC|$; $[CA]$'nın dikmesi üzerinde olduğu için $|KC| = |KA|$. Demek ki

$$|KA| = |KB| = |KC|$$

$K$ üç köşeye eşit uzaklıktadır. Bu yüzden $K$ merkezli bir çember üç köşeden de geçer (üçgenin **çevrel çemberi**; çemberler konusunda yeniden göreceksin).

![Dar açılı ABC üçgeni. Üç kenarın orta noktalarından mavi, yeşil ve kırmızı kesikli dikmeler çıkıyor ve K'de kesişiyor. K'den köşelere sarı doğru parçaları çizilmiş; K merkezli kesikli çember A, B ve C'den geçiyor.](gorsel/tyt-matematik/20-05-kesisim.svg "Üç kesikli dikme aynı K noktasından geçer. Sarı KA, KB ve KC eşittir; çember üç köşeye de değer.")

**Örnek.** $ABC$ dar açılı bir üçgen, $K$ kenar orta dikmelerin kesim noktasıdır. $m(\widehat{KBC}) = 20^\circ$ ve $m(\widehat{KAC}) = 30^\circ$ ise $m(\widehat{KAB})$ ve $m(\widehat{BAC})$ kaçtır?

![ABC üçgeni ve içindeki K noktası; K'den köşelere sarı, birer çentikli eşit doğru parçaları. B'de KB ile BC arasında 20 derece, A'da KA ile AC arasında 30 derece, A'da AB ile AK arasında soru işareti.](gorsel/tyt-matematik/20-05-aci.svg "KA = KB = KC olduğu için KAB, KBC ve KCA üçgenleri ikizkenardır. Her birinin iki taban açısı eşittir.")

**Çözüm.**

1. $|KA| = |KB| = |KC|$ olduğu için $KBC$, $KCA$ ve $KAB$ üçgenlerinin üçü de ikizkenardır.
2. $KBC$'de taban açıları eşit: $m(\widehat{KCB}) = 20^\circ$. $KCA$'da: $m(\widehat{KCA}) = 30^\circ$. $KAB$'de: $m(\widehat{KAB}) = m(\widehat{KBA}) = z$.
3. Üçgenin iç açıları toplamı: her taban açısı iki kez sayılır, $2 \cdot 20^\circ + 2 \cdot 30^\circ + 2z = 180^\circ$. Buradan $z = 40^\circ$.
4. $m(\widehat{BAC}) = z + 30^\circ = 70^\circ$.

**Kural:** $K$'den köşelere çizilen doğru parçaları üçgeni üç ikizkenar üçgene böler. Taban açıları $x$, $y$, $z$ ise (dar açılı üçgende)

$$x + y + z = 90^\circ \qquad m(\widehat{BKC}) = 2\cdot m(\widehat{A})$$

Örnekte: $20^\circ + 30^\circ + 40^\circ = 90^\circ$ ve $m(\widehat{BKC}) = 180^\circ - 2 \cdot 20^\circ = 140^\circ = 2 \cdot 70^\circ$.

> **Tuzak:** $K$ köşelere eşit uzaklıktadır, **kenarlara değil**. Kenarlara eşit uzaklıktaki nokta, açıortayların kesim noktasıdır (iç teğet çemberin merkezi). İki noktayı karıştırma.

## 3. K'nin yeri üçgenin çeşidine bağlıdır

**Örnek.** $ABC$ üçgeninde $m(\widehat{B}) = 90^\circ$, $|AB| = 6$, $|BC| = 8$'dir. $K$, kenar orta dikmelerin kesim noktası ise $|KB|$ kaçtır?

**Çözüm.**

1. $[AB]$'nin dikmesi $[BC]$'ye paralel, $[BC]$'nin dikmesi $[AB]$'ye paraleldir; ikisi hipotenüsün orta noktasında buluşur. $K$, $[AC]$'nin orta noktasıdır.
2. Pisagor: $|AC| = \sqrt{6^2 + 8^2} = 10$.
3. $|KB| = |KA| = |KC| = \dfrac{10}{2} = 5$.

Bu, geçen derslerden bildiğin bilgidir: dik üçgende hipotenüse ait kenarortay hipotenüsün yarısıdır.

![Yan yana üç üçgen. Dar açılı üçgende kesikli dikmeler K'de, üçgenin içinde kesişiyor. B köşesi dik olan üçgende K, hipotenüs AC'nin orta noktasında. A açısı geniş olan üçgende K, BC kenarının altında, üçgenin dışında.](gorsel/tyt-matematik/20-05-konum.svg "K içeride, kenarın üstünde ya da dışarıda: hangisi olduğuna en büyük açı karar verir.")

**Kural:**

| Üçgen | $K$'nin yeri |
|---|---|
| Dar açılı | Üçgenin **içinde** |
| Dik | **Hipotenüsün orta noktasında**; $\lvert KA \rvert = \lvert KB \rvert = \lvert KC \rvert = \dfrac{\text{hipotenüs}}{2}$ |
| Geniş açılı | Üçgenin **dışında**, en uzun kenarın (geniş açının karşısı) öbür yanında |

Tersi de geçerlidir: $K$ bir kenarın üzerindeyse o kenarın karşısındaki açı $90^\circ$'dir; $K$ dışarıdaysa üçgen geniş açılıdır.

> **Tuzak:** Dik üçgende **yükseklikler** dik açılı köşede, **kenar orta dikmeler** hipotenüsün orta noktasında kesişir. "Dik üçgende $K$ köşededir" demek yükseklikle karıştırmaktır.

## 4. İkizkenar ve eşkenar üçgende

**İkizkenar üçgen.** $|AB| = |AC|$ ise $A$, $B$ ve $C$'ye eşit uzaklıktadır; yani $A$, $[BC]$'nin kenar orta dikmesi üzerindedir. Bu dikme $A$'dan inen yükseklik, kenarortay ve açıortay ile **aynı doğrudur**. $K$ de bu doğru üzerindedir.

**Eşkenar üçgen.** Her köşe için aynı şey geçerlidir: üç kenar orta dikme, üç yükseklik, üç kenarortay ve üç açıortay aynı üç doğrudur. Bu yüzden kenar orta dikmelerin kesim noktası $K$, ağırlık merkezi $G$, yüksekliklerin ve açıortayların kesim noktası **aynı noktadır**.

**Örnek.** Bir kenarı $6$ birim olan $ABC$ eşkenar üçgeninde $K$, kenar orta dikmelerin kesim noktasıdır. $|KA|$ ve $K$'nin $[BC]$'ye uzaklığı kaçtır?

![Solda AB ile AC'si eş ikizkenar üçgen; BC'nin orta noktası D'den çıkan kırmızı kesikli dikme A'dan geçiyor, K bu doğru üzerinde. Sağda kenarı 6 olan eşkenar üçgen; üç kırmızı kesikli doğru K'de kesişiyor, KA 2 kök 3, KD kök 3 olarak yazılmış.](gorsel/tyt-matematik/20-05-ikizkenar-eskenar.svg "İkizkenarda tabanın dikmesi tepe köşesinden geçer. Eşkenarda K aynı zamanda ağırlık merkezidir; yüksekliği 2'ye 1 böler.")

**Çözüm.**

1. Yükseklik: $|AD| = \dfrac{6\sqrt{3}}{2} = 3\sqrt{3}$.
2. $K = G$ olduğu için $K$, $[AD]$'yi köşeden itibaren $2 : 1$ böler.
3. $|KA| = \dfrac{2}{3} \cdot 3\sqrt{3} = 2\sqrt{3}$, $|KD| = \dfrac{1}{3} \cdot 3\sqrt{3} = \sqrt{3}$.

**Kural:** Kenarı $a$ olan eşkenar üçgende

$$|KA| = |KB| = |KC| = \frac{2}{3} \cdot \frac{a\sqrt{3}}{2} = \frac{a\sqrt{3}}{3} \qquad K\text{'nin kenarlara uzaklığı} = \frac{a\sqrt{3}}{6}$$

> **Tuzak:** $|KA|$ yüksekliğin tamamı ($3\sqrt{3}$) ya da yarısı değildir; $\dfrac{2}{3}$'üdür. Bu eşitlik yalnızca eşkenar üçgende geçerlidir: başka üçgende $K$ ile $G$ farklı noktalardır.

## ÖSYM tuzakları

> **Kesişme noktasını orta nokta sanmak.** $[AB]$'nin dikmesi $[BC]$'yi $D$'de keserse $|DB| = |DC|$ değil, $|DA| = |DB|$ olur. Eşitliği, dikmenin **ait olduğu kenarın uçlarıyla** kur.

> **Çevre sorusunda parçaları tek tek aramak.** Çevrede $|DA|$ yerine $|DB|$ yaz; iki parça birleşip bir kenarın tamamı olur. Seçeneklerde yanlış kenarların toplamı (örneğin $|AB| + |BC|$) hazır bekler.

> **$K$'yi kenarlara eşit uzaklıkta sanmak.** Kenar orta dikmelerin kesim noktası **köşelere** eşit uzaklıktadır. Kenarlara eşit uzaklık açıortaylara aittir.

> **Dik üçgende yanlış nokta.** Kenar orta dikmeler hipotenüsün orta noktasında, yükseklikler dik açılı köşede kesişir.

> **Eşkenar üçgende $\frac{1}{2}$ almak.** $|KA| = \dfrac{2}{3}h$'dir; $\dfrac{h}{2}$ ya da $h$ seçeneklerde bekler.

## Kendini dene

### Soru 1
$ABC$ üçgeninde $m(\widehat{A}) = 90^\circ$, $|AB| = 8$ ve $|AC| = 15$'tir. $K$, kenar orta dikmelerin kesim noktası ise $|KA|$ kaçtır?

A) 4
B) 7,5
C) 8,5
D) 15
E) 17

**Cevap:** C
**Çözüm:** Dik üçgende $K$, hipotenüsün orta noktasıdır. $|BC| = \sqrt{8^2 + 15^2} = \sqrt{289} = 17$; $|KA| = \dfrac{17}{2} = 8{,}5$. $4$ ve $7{,}5$ dik kenarların yarısıdır; $17$ ise hipotenüsün kendisidir.

### Soru 2
$ABC$ üçgeninde $|AB| = 10$, $|AC| = 6$ ve $|BC| = 12$'dir. $[BC]$'nin kenar orta dikmesi $[AB]$'yi $D$ noktasında kesiyor. $ADC$ üçgeninin çevresi kaçtır?

A) 16
B) 18
C) 22
D) 25
E) 28

**Cevap:** A
**Çözüm:** $D$, $[BC]$'nin dikmesi üzerinde: $|DC| = |DB|$. $\text{Ç}(ADC) = |AD| + |DC| + |AC| = |AD| + |DB| + |AC| = |AB| + |AC| = 10 + 6 = 16$. $18$ ($|AC| + |BC|$) ve $22$ ($|AB| + |BC|$) yanlış kenarları toplamaktır; $28$ ise $ABC$'nin çevresidir.

### Soru 3
$ABC$ dar açılı bir üçgen, $K$ kenar orta dikmelerin kesim noktasıdır. $m(\widehat{KAB}) = 20^\circ$ ve $m(\widehat{KBC}) = 30^\circ$ ise $m(\widehat{ACB})$ kaç derecedir?

A) 40
B) 50
C) 60
D) 70
E) 140

**Cevap:** D
**Çözüm:** $|KA| = |KB| = |KC|$: üç ikizkenar üçgen. Taban açıları toplamı $90^\circ$: $m(\widehat{KCA}) = 90^\circ - 20^\circ - 30^\circ = 40^\circ$. $m(\widehat{KCB}) = m(\widehat{KBC}) = 30^\circ$. $m(\widehat{ACB}) = 30^\circ + 40^\circ = 70^\circ$. $40^\circ$ yalnızca $\widehat{KCA}$'dır; $140^\circ$ ise $m(\widehat{AKB}) = 2 \cdot 70^\circ$'dir.

## Özet kartı

- Kenar orta dikme: kenarın orta noktasından geçer ve kenara diktir; köşeden çıkmak zorunda değildir.
- Dikme üzerindeki her nokta kenarın iki ucuna eşit uzaklıktadır: $|PA| = |PB|$. Çevrede bir parçanın yerine öbürünü yaz.
- Üç dikme $K$'de kesişir: $|KA| = |KB| = |KC|$ (çevrel çemberin merkezi). Taban açıları: $x + y + z = 90^\circ$.
- $K$: dar açılıda içeride, dikte hipotenüsün ortasında, geniş açılıda dışarıda.
- İkizkenarda tabanın dikmesi tepeden geçer; eşkenarda $K = G$ ve $|KA| = \dfrac{a\sqrt{3}}{3}$.

## Sonraki adım

Alıştırmaya geç (aşağıdaki düğme). Sonraki ders: **Dik Üçgende Pisagor Teoremi**. Bu derste hipotenüsü bulmak için kullandığın $a^2 + b^2 = c^2$ bağıntısını orada ayrıntılı göreceksin.
