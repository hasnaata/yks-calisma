---
baslik: Üçgende Açıortay ve Özellikleri
ders: tyt-matematik
sure: 20 dk
kaynak: MEBİ Konu Özeti 06dbfb93a8
guncelleme: 2026-11-18
---
# Üçgende Açıortay ve Özellikleri

<div class="giris" dir="rtl" lang="ar">

**الدرس ده عن إيه؟** عن منصّف الزاوية (açıortay) في المثلث: الشعاع اللي بيقسم الزاوية نصّين متساويين، وإزاي تستخدمه في الحل.

- هتعرف إن أي نقطة على منصّف الزاوية بتبعد نفس المسافة عن ضلعي الزاوية، بشرط إن المسافة تكون عمودية.
- هتشوف إن منصّفات الزوايا الداخلة التلاتة بتتقابل في نقطة واحدة، وهي مركز الدائرة الداخلة (iç teğet çemberin merkezi).
- هتحسب الزاوية عند نقطة تقابل منصّفين في التلات حالات: داخلي مع داخلي (iç–iç)، خارجي مع خارجي (dış–dış)، وداخلي مع خارجي (iç–dış).

**ليه مهم؟** سؤال "منصّفين بيتقابلوا في نقطة، الزاوية دي كام؟" بييجي كتير في هندسة TYT، والشطارة إنك تعرف أنهي حالة قدامك وتختار القاعدة الصح.

هو ٢٠ دقيقة بس، وفيه جدول صغير بيلمّ القواعد كلها. هات ورقة وقلم ويلا بينا.

</div>

**Bu dersin sonunda:** açıortay üzerindeki bir noktanın kollara uzaklığını bulabilecek, iki açıortayın kesiştiği noktadaki açıyı (iç–iç, dış–dış, iç–dış) tek satırda hesaplayabileceksin.

> **TYT'de yeri:** Geometri sorularında "iki açıortay $D$'de kesişiyor, $x$ kaçtır?" kalıbı çok sık gelir. Şekilde eş açılar aynı çentikle işaretlenir; senden beklenen, hangi açıortayların (iç mi, dış mı) kesiştiğini görüp doğru kuralı seçmektir. Açıortayın kollara eşit uzaklık özelliği ise alan ve uzunluk sorularında gizli anahtar olarak kullanılır.

## Önce hatırla

<details><summary>Geçen dersten: 4,5 m yüksekliğindeki bir sokak lambasının dibinden 4 m uzakta 1,5 m boyunda bir kişi duruyor. Kişinin gölgesi kaç metredir?</summary>
Gölge s ise 1,5 / 4,5 = s / (s + 4). İçler dışlar: 4,5s = 1,5s + 6, yani 3s = 6 ve <b>s = 2 m</b>. Büyük üçgenin tabanı gölgenin ucundan direğin dibine kadardır (s + 4). Bugün de iki dik üçgeni karşılaştıracaksın; ama bu kez benzer değil, eş olacaklar.
</details>

<details><summary>Geçen dersten: Aralarında 10 m bulunan 4 m ve 12 m yüksekliğindeki iki direğin her birinin tepesinden öbürünün dibine birer ip geriliyor. İplerin kesiştiği nokta yerden kaç metre yüksektedir?</summary>
h = (4 · 12) / (4 + 12) = 48 / 16 = <b>3 m</b>. Direkler arası uzaklık sonucu değiştirmez ve h kısa direkten de kısadır. Bugünkü sorularda da her veri gerekmeyecek: iki açıortayın kesiştiği açı yalnızca üçüncü köşedeki açıya bağlıdır.
</details>

## Açıortay nedir?

Bir açıyı iki eş açıya bölen ışına **açıortay** denir. $[OB$, $\widehat{AOC}$'nin açıortayı ise $m(\widehat{AOB}) = m(\widehat{BOC})$. Şekillerde eş açılar aynı sayıda çentikle ya da aynı harfle ($\alpha$) gösterilir.

## 1. Açıortay üzerindeki nokta kollara eşit uzaklıktadır

**Örnek.** $[OB$, $\widehat{AOC}$'nin açıortayıdır. $B$'den kollara dikmeler $[BA] \perp [OA$ ve $[BC] \perp [OC$ çiziliyor. $|OB| = 5$ ve $|BA| = 3$ ise $|BC|$ ve $|OC|$ kaçtır?

![O köşeli bir açı; O'dan çıkan mavi açıortay ışını üzerinde B noktası. B'den alttaki kola dik BA, üstteki kola dik BC çizilmiş, ikisi de 3. OB 5, OA ve OC 4. O'daki iki açı alfa ile işaretli.](gorsel/tyt-matematik/20-01-uzaklik.svg "OAB ve OCB dik üçgenleri hipotenüsü (OB) ve bir açıyı (α) paylaşır, bu yüzden eştir. Kırmızı dikmeler eşit (3), kollardaki parçalar da eşit (4).")

**Çözüm.**

1. $OAB$ ve $OCB$ üçgenlerinde $[OB]$ ortak, $O$'daki açılar eşit ($\alpha$), $A$ ve $C$'deki açılar dik. Üçüncü açılar da eşit olur ($90^\circ - \alpha$). A.K.A. ile $\triangle OAB \cong \triangle OCB$.
2. Eş üçgenlerin karşılıklı kenarları eşittir: $|BC| = |BA| = 3$.
3. Pisagor: $|OA| = \sqrt{5^2 - 3^2} = 4$, ve $|OC| = |OA| = 4$.

**Kural:** Açıortay üzerindeki bir noktadan kollara indirilen **dikmeler** eşittir; dikme ayaklarının köşeye uzaklıkları da eşittir.

$$|BA| = |BC| \qquad |OA| = |OC|$$

Tersi de doğrudur: bir açının içinde, iki kola eşit uzaklıkta olan nokta o açının açıortayı üzerindedir.

> **Tuzak:** "Uzaklık" her zaman **dik** uzaklıktır. Açıortay üzerindeki $B$'den kollara eğik çizilen iki doğru parçası eşit olmak zorunda değildir. Şekilde dik açı işareti yoksa bu kuralı kullanamazsın.

## 2. İç açıortaylar ve kesişme noktaları

Bir üçgenin iç açısını iki eş parçaya bölen ışına **iç açıortay** denir. Üç iç açıortay **tek bir noktada** kesişir. Bu yüzden iki iç açıortayın kesiştiği nokta verilirse, üçüncü köşeden o noktaya çizilen doğru parçası da açıortaydır.

**Örnek.** $ABC$ üçgeninde $m(\widehat{A}) = 70^\circ$. $B$ ve $C$'deki iç açıortaylar $D$'de kesişiyor. $m(\widehat{BDC})$ kaçtır?

![ABC üçgeni, A'da 70 derece. B ve C'den çıkan mavi iç açıortaylar D'de buluşuyor; D'deki açı 125 derece. A'dan D'den geçen yeşil kesikli açıortay iniyor. D merkezli kesikli bir çember üç kenara da değiyor. B'deki iki eş açı tek çentikli, C'deki iki eş açı çift çentikli.](gorsel/tyt-matematik/20-01-ic-aciortay.svg "B ve C'nin ayrı ayrı ölçüsü gerekmez, yalnızca toplamlarının yarısı (55°) gerekir. Yeşil kesikli çizgi: A'nın açıortayı da D'den geçer. Kesikli çember: D üç kenara eşit uzaklıktadır.")

**Çözüm.**

1. $m(\widehat{B}) + m(\widehat{C}) = 180^\circ - 70^\circ = 110^\circ$.
2. $BDC$ üçgeninde $D$'ye komşu açılar bunların yarısıdır: $\dfrac{m(\widehat{B})}{2} + \dfrac{m(\widehat{C})}{2} = 55^\circ$.
3. $m(\widehat{BDC}) = 180^\circ - 55^\circ = 125^\circ$.

Genel hâli: $180^\circ - \dfrac{180^\circ - m(\widehat{A})}{2} = 90^\circ + \dfrac{m(\widehat{A})}{2}$.

**Kural:** $[BD]$ ve $[CD]$ iç açıortay ise

$$m(\widehat{BDC}) = 90^\circ + \frac{m(\widehat{A})}{2}$$

- Sonuç her zaman $90^\circ$'den **büyüktür** (geniş açı).
- $D$, açıortay üzerinde olduğu için üç kenara da **eşit uzaklıktadır**. $D$ merkezli ve bu uzaklık yarıçaplı çember üç kenara da değer; bu yüzden $D$'ye **iç teğet çemberin merkezi** denir.

> **Tuzak:** Formüldeki açı, kesişme noktasının **karşısındaki** köşenin açısıdır. $\widehat{BDC}$ soruluyorsa $\widehat{A}$ kullanılır; $\widehat{ADB}$ soruluyorsa $\widehat{C}$ kullanılır.

## 3. Dış açıortaylar

Bir üçgenin **dış** açısını iki eş parçaya bölen ışına **dış açıortay** denir. İki dış açıortayın kesiştiği noktadan üçüncü köşeye çizilen doğru, o köşenin **iç** açıortayıdır.

**Örnek.** $ABC$ üçgeninde $m(\widehat{A}) = 50^\circ$, $m(\widehat{B}) = 70^\circ$. $B$ ve $C$'deki dış açıortaylar $D$'de kesişiyor. $m(\widehat{BDC})$ kaçtır?

![ABC üçgeni, A'da 50 derece. AB ve AC kenarları B ve C'nin ötesine kesikli çizgiyle uzatılmış. B ve C'deki dış açıları ikiye bölen mavi ışınlar BC'nin altında D'de buluşuyor; D'deki açı 65 derece. A'dan D'ye yeşil noktalı çizgi.](gorsel/tyt-matematik/20-01-dis-aciortay.svg "Dış açıortaylar üçgenin dışında, A'nın karşı tarafında kesişir. Yeşil noktalı çizgi A'nın iç açıortayıdır ve D'den geçer.")

**Çözüm.**

1. $m(\widehat{C}) = 180^\circ - 50^\circ - 70^\circ = 60^\circ$.
2. $B$'deki dış açı $180^\circ - 70^\circ = 110^\circ$, yarısı $m(\widehat{DBC}) = 55^\circ$. $C$'deki dış açı $120^\circ$, yarısı $m(\widehat{DCB}) = 60^\circ$.
3. $BDC$ üçgeninde $m(\widehat{BDC}) = 180^\circ - 55^\circ - 60^\circ = 65^\circ$.

**Kısa yol:** $90^\circ - \dfrac{50^\circ}{2} = 65^\circ$. $m(\widehat{B})$ verilmese de sonuç aynıdır.

**Kural:** $[BD]$ ve $[CD]$ dış açıortay ise

$$m(\widehat{BDC}) = 90^\circ - \frac{m(\widehat{A})}{2}$$

Sonuç her zaman $90^\circ$'den **küçüktür** (dar açı).

> **Tuzak:** İç–iç ile dış–dış formüllerini karıştırmak. Hatırlama yolu: iç açıortaylar üçgenin **içinde**, $A$'ya yakın kesişir ve geniş bir açı oluşturur ($+$). Dış açıortaylar **uzakta** kesişir ve dar bir açı oluşturur ($-$).

## 4. Bir iç, bir dış açıortay

**Örnek.** $ABC$ üçgeninde $m(\widehat{A}) = 64^\circ$, $m(\widehat{B}) = 56^\circ$. $[BE$, $B$'deki iç açıortaydır ($E \in [AC]$). $[BC]$, $C$'nin ötesine $P$'ye kadar uzatılıyor ve $[CD$, $\widehat{ACP}$ dış açısının açıortayıdır. $[BE$ ile $[CD$, $D$'de kesişiyor. $m(\widehat{BDC})$ kaçtır?

![ABC üçgeni, A'da 64 derece. B'den çıkan mavi iç açıortay AC'yi E'de kesip üçgenin dışına uzanıyor. BC kenarı C'nin ötesine P'ye kadar kesikli uzatılmış; C'den çıkan kırmızı ışın ACP dış açısını iki eş parçaya bölüyor. İki ışın D'de buluşuyor; D'deki açı 32 derece.](gorsel/tyt-matematik/20-01-ic-dis.svg "D'deki açı A'daki açının tam yarısıdır: 64° ve 32°. Tek çentikli açılar B'nin, çift çentikli açılar C'deki dış açının yarılarıdır.")

**Çözüm.**

1. $C$'deki dış açı, komşu olmayan iki iç açının toplamıdır: $m(\widehat{ACP}) = 64^\circ + 56^\circ = 120^\circ$. Yarısı $m(\widehat{DCP}) = 60^\circ$.
2. $BDC$ üçgeninde $\widehat{DCP}$ dış açıdır: $m(\widehat{DCP}) = m(\widehat{DBC}) + m(\widehat{BDC})$.
3. $60^\circ = 28^\circ + m(\widehat{BDC}) \Rightarrow m(\widehat{BDC}) = 32^\circ$.

Genel hâli: $\dfrac{m(\widehat{A}) + m(\widehat{B})}{2} = \dfrac{m(\widehat{B})}{2} + x \Rightarrow x = \dfrac{m(\widehat{A})}{2}$.

**Kural:** $[BD$ iç açıortay, $[CD$ dış açıortay ise

$$m(\widehat{BDC}) = \frac{m(\widehat{A})}{2}$$

> **Tuzak:** Burada $90^\circ$ **yoktur**. "$90^\circ$ artı ya da eksi" alışkanlığıyla $90^\circ - 32^\circ$ gibi sonuçlar seçeneklerde hazır bekler.

## Hangi kural?

| Kesişen açıortaylar | $m(\widehat{BDC})$ | Açı türü |
|---|---|---|
| $B$'de iç, $C$'de iç | $90^\circ + \dfrac{m(\widehat{A})}{2}$ | geniş |
| $B$'de dış, $C$'de dış | $90^\circ - \dfrac{m(\widehat{A})}{2}$ | dar |
| $B$'de iç, $C$'de dış | $\dfrac{m(\widehat{A})}{2}$ | dar |

Üçünde de sonucu belirleyen, kesişme noktasının **karşısındaki** köşenin açısıdır. Formülü unutursan $BDC$ üçgeninde açıları tek tek yaz; iki dakikada yeniden bulursun.

## ÖSYM tuzakları

> **Dik olmayan uzaklık.** Kollara eşit uzaklık kuralı yalnızca dikmeler için geçerlidir. Şekilde dik açı işaretini ara.

> **Yanlış köşenin açısı.** $\widehat{ADB}$ soruluyorsa formüle $\widehat{C}$ girer, $\widehat{A}$ değil. Kesişme noktasını oluşturan iki köşeye değil, karşıdaki üçüncü köşeye bak.

> **İşareti karıştırmak.** İç–iç $90^\circ + \frac{A}{2}$ (geniş), dış–dış $90^\circ - \frac{A}{2}$ (dar). Bulduğun açının geniş mi dar mı olması gerektiğini şekilden kontrol et.

> **Üçüncü açıortayı görmemek.** İki açıortay $D$'de kesişiyorsa üçüncü köşeden $D$'ye çizilen doğru da açıortaydır (iç–iç durumunda iç, dış–dış durumunda üçüncü köşenin iç açıortayı). Soru bunu söylemez; senin görmen beklenir.

> **Ters soruda yarıyı unutmak.** $m(\widehat{BDC}) = 118^\circ$ verilip $m(\widehat{A})$ sorulursa $118^\circ - 90^\circ = 28^\circ$ bulunur ama cevap bunun **iki katı**, $56^\circ$'dir.

## Kendini dene

### Soru 1
$ABC$ üçgeninde $m(\widehat{A}) = 64^\circ$'dir. $B$ ve $C$ köşelerindeki iç açıortaylar $D$ noktasında kesişiyor. $m(\widehat{BDC})$ kaç derecedir?

A) 32
B) 58
C) 116
D) 122
E) 154

**Cevap:** D
**Çözüm:** İç–iç: $90^\circ + \dfrac{64^\circ}{2} = 122^\circ$. Kontrol: $\dfrac{m(\widehat{B}) + m(\widehat{C})}{2} = \dfrac{116^\circ}{2} = 58^\circ$, $180^\circ - 58^\circ = 122^\circ$. $58^\circ$ dış–dış formülünün sonucu, $154^\circ$ ise $\widehat{A}$'yı ikiye bölmeyi unutmaktır.

### Soru 2
$ABC$ üçgeninde $B$ ve $C$ köşelerindeki dış açıortaylar $D$ noktasında kesişiyor. $m(\widehat{BDC}) = 52^\circ$ ise $m(\widehat{A})$ kaç derecedir?

A) 26
B) 38
C) 76
D) 104
E) 142

**Cevap:** C
**Çözüm:** $90^\circ - \dfrac{m(\widehat{A})}{2} = 52^\circ \Rightarrow \dfrac{m(\widehat{A})}{2} = 38^\circ \Rightarrow m(\widehat{A}) = 76^\circ$. $38^\circ$ yarıda durmaktır; $104^\circ$ ise $52^\circ$'yi doğrudan ikiyle çarpmaktır.

### Soru 3
$ABC$ üçgeninde $m(\widehat{B}) = 70^\circ$ ve $m(\widehat{C}) = 50^\circ$'dir. $B$'deki iç açıortay ile $C$'deki dış açıortay $D$ noktasında kesişiyor. $m(\widehat{BDC})$ kaç derecedir?

A) 25
B) 30
C) 35
D) 60
E) 120

**Cevap:** B
**Çözüm:** $m(\widehat{A}) = 180^\circ - 70^\circ - 50^\circ = 60^\circ$. İç–dış: $\dfrac{60^\circ}{2} = 30^\circ$. Adım adım: $C$'deki dış açı $130^\circ$, yarısı $65^\circ$; $65^\circ = 35^\circ + m(\widehat{BDC})$, yani $30^\circ$. $120^\circ$, iç–iç formülünü kullanmaktır.

## Özet kartı

- Açıortay üzerindeki nokta, kollara (dik uzaklıkla) eşit uzaklıktadır.
- Üç iç açıortay tek noktada kesişir: iç teğet çemberin merkezi, üç kenara eşit uzaklıkta.
- İki açıortay $D$'de kesişiyorsa üçüncü köşeden $D$'ye çizilen doğru da açıortaydır.
- İç–iç: $90^\circ + \dfrac{A}{2}$ · Dış–dış: $90^\circ - \dfrac{A}{2}$ · İç–dış: $\dfrac{A}{2}$
- Formüldeki $A$, kesişme noktasının karşısındaki köşenin açısıdır.

## Sonraki adım

Alıştırmaya geç (aşağıdaki düğme). Sonraki ders: **Üçgende Açıortay Teoremleri**. Orada açıortayın karşı kenarı, komşu kenarların oranında nasıl böldüğünü göreceksin.
