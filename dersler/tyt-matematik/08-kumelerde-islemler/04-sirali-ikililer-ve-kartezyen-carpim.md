---
baslik: Sıralı İkililer ve Kartezyen Çarpım
ders: tyt-matematik
sure: 20 dk
kaynak: MEBİ Konu Özeti 82824aa912
guncelleme: 2026-11-18
---
# Sıralı İkililer ve Kartezyen Çarpım

<div class="giris" dir="rtl" lang="ar">

**الدرس ده عن إيه؟** عن الزوج المرتب (sıralı ikili) وحاصل الضرب الديكارتي (kartezyen çarpım): لما الترتيب يفرق، زي رقم الصف ورقم الكرسي في تذكرة السينما.

- هتعرف إزاي تساوي زوجين مرتبين وتطلّع المجاهيل: الأول مع الأول والتاني مع التاني.
- هتكتب حاصل الضرب الديكارتي لمجموعتين وتحسب عدد عناصره (eleman sayısı) بضرب عدد عناصر المجموعتين في بعض.
- هترسمه نقط على المستوى الإحداثي وتقرا الرسم بالعكس، وتعرف العناصر المشتركة بين A في B و B في A.

**ليه مهم؟** الموضوع قصير بس أسئلته في TYT ليها قوالب ثابتة، والفكرة دي نفسها هي أساس مبدأ العد (saymanın temel ilkesi) في الدرس الجاي.

٢٠ دقيقة بس، ولو مسكت فكرة الترتيب صح، الباقي هيمشي معاك بسهولة.

</div>

**Bu dersin sonunda:** iki sıralı ikilinin eşitliğinden bilinmeyenleri bulabilecek, iki kümenin kartezyen çarpımını yazıp eleman sayısını hesaplayabilecek ve kartezyen çarpımın grafiğini çizip okuyabileceksin.

> **TYT'de yeri:** Konu kısa ama soru kalıpları belli: "$(a, b) = (c, d)$ ise $x + y$ kaçtır?", "$s(A \times B)$ ve $s(B \times B)$ verilmiş, $s(A)$ kaçtır?", grafiği verilen $A \times B$'den $A$ ve $B$'yi bulma, $A \times B$ ile $B \times A$'nın ortak elemanları ve koşulu sağlayan sıralı ikilileri sayma. Bu sayma fikri bir sonraki konu olan saymanın temel ilkesinin de çıkış noktasıdır.

## Önce hatırla

<details><summary>Küme problemlerinden: 32 kişilik bir grupta 20 kişi A, 15 kişi B etkinliğine katılıyor; 4 kişi hiçbirine katılmıyor. İki etkinliğe de katılan kaç kişidir?</summary>
En az birine katılan $32 - 4 = 28$ kişi. $20 + 15 = 35$ toplamında ortak bölge iki kez sayıldı: $35 - 28 = $ <b>7</b>.
</details>

<details><summary>Küme problemlerinden: 30 kişilik bir sınıfta 8 öğrenci iki kursa da gidiyor. Bu kurslardan en çok birine giden kaç öğrenci vardır?</summary>
En çok biri = toplam − ikisi de: $30 - 8 = $ <b>22</b>. Hiçbirine gitmeyenler de bu sayının içindedir.
</details>

## Sıralı ikili

**Örnek.** Sinemada bilet "(sıra, koltuk)" diye yazılır. $(5, 8)$ beşinci sıranın sekizinci koltuğudur; $(8, 5)$ ise sekizinci sıranın beşinci koltuğu. İki sayı aynı ama yer farklı. İşte **sıralı ikili** budur: yazılış sırası önemlidir.

$(a, b)$ sıralı ikilisinde $a$'ya **birinci bileşen**, $b$'ye **ikinci bileşen** denir. $a \ne b$ ise $(a, b) \ne (b, a)$ olur. Küme gösteriminde ise sıra önemsizdir: $\{5, 8\} = \{8, 5\}$.

**Örnek.** $(x + 2,\ 7) = (5,\ y - 1)$ olduğuna göre $x$ ve $y$ kaçtır?

İki sıralı ikili eşitse **birinci bileşenler kendi arasında, ikinci bileşenler kendi arasında** eşittir:

- $x + 2 = 5 \Rightarrow x = 3$
- $7 = y - 1 \Rightarrow y = 8$

**Örnek.** $(2a - b,\ 4) = (5,\ a + b)$ ise $a$ ve $b$ kaçtır?

$2a - b = 5$ ve $a + b = 4$. Taraf tarafa topla: $3a = 9$, $a = 3$. Sonra $b = 4 - 3 = 1$.

**Kural.** $(a, b) = (c, d) \iff a = c$ ve $b = d$. Çapraz eşitleme ($a = d$ gibi) yapılmaz.

## Kartezyen çarpım

**Örnek.** $A = \{1, 2, 3\}$ ve $B = \{4, 5\}$ olsun. Birinci bileşeni $A$'dan, ikinci bileşeni $B$'den gelen bütün sıralı ikilileri yaz.

$A$'nın her elemanını $B$'nin her elemanıyla eşle. Bir tablo kurarsan hiçbirini atlamazsın:

![Üç satır iki sütunlu tablo. Satır başlarında A'nın elemanları 1, 2, 3; sütun başlarında B'nin elemanları 4 ve 5. Hücrelerde (1, 4), (1, 5), (2, 4), (2, 5), (3, 4), (3, 5).](gorsel/tyt-matematik/08-04-tablo.svg "Satırlar birinci bileşeni (A), sütunlar ikinci bileşeni (B) verir. 3 satır ve 2 sütun, 3 · 2 = 6 hücre demektir.")

$$A \times B = \{(1, 4), (1, 5), (2, 4), (2, 5), (3, 4), (3, 5)\}$$

Bu kümeye **A kartezyen çarpım B** denir ve $A \times B$ diye yazılır:

$$A \times B = \{(a, b) \mid a \in A \text{ ve } b \in B\}$$

Aynı kümelerle $B \times A = \{(4, 1), (4, 2), (4, 3), (5, 1), (5, 2), (5, 3)\}$ olur. $(1, 4) \in A \times B$ ama $(1, 4) \notin B \times A$. Yani $A \times B \ne B \times A$; yine de ikisi de 6 elemanlıdır.

**Kural.**

| Özellik | Açıklama |
|---|---|
| $s(A \times B) = s(A) \cdot s(B)$ | Tablodaki satır sayısı çarpı sütun sayısı |
| $A \ne B$ (ikisi de boş değil) ise $A \times B \ne B \times A$ | Ama $s(A \times B) = s(B \times A)$ |
| $A \times \varnothing = \varnothing \times A = \varnothing$ | Boş kümeden bileşen seçilemez |
| $A \times A$ (kısaca $A^2$) | $s(A \times A) = s(A)^2$ |

**Örnek.** $s(A \times B) = 20$ ve $s(A \times A) = 16$ ise $s(B)$ kaçtır?

$s(A)^2 = 16$ olduğundan $s(A) = 4$ (eleman sayısı negatif olamaz). $4 \cdot s(B) = 20$, yani $s(B) = 5$.

$A \times B$ de bir kümedir; alt küme sayısı bildiğin kuralla bulunur: $s(A) = 2$, $s(B) = 2$ ise $A \times B$ 4 elemanlıdır ve $2^4 = 16$ alt kümesi vardır.

## Kartezyen çarpımın grafiği

**Örnek.** $A = \{1, 2, 4\}$ ve $B = \{1, 3\}$ için $A \times B$'yi koordinat düzleminde göster.

Birinci bileşenleri $x$ ekseninde, ikinci bileşenleri $y$ ekseninde işaretle. $A$'nın elemanlarından dikey, $B$'nin elemanlarından yatay kesikli çizgiler çiz. Kesişme noktaları $A \times B$'nin elemanlarıdır.

![Koordinat düzlemi. x ekseninde 1, 2 ve 4'ten dikey, y ekseninde 1 ve 3'ten yatay kesikli çizgiler. Kesişimlerde altı kırmızı nokta: (1, 1), (2, 1), (4, 1), (1, 3), (2, 3), (4, 3).](gorsel/tyt-matematik/08-04-grafik.svg "3 dikey çizgi ile 2 yatay çizgi 3 · 2 = 6 noktada kesişir. x = 3'te nokta yok, çünkü 3 A'nın elemanı değil.")

Grafik tersten de okunur: noktaların **x değerleri** $A$'yı, **y değerleri** $B$'yi verir. Aynı x değeri kaç kez görünürse görünsün $A$'ya bir kez yazılır.

**Kural.** $A \times B$'nin grafiği $s(A) \cdot s(B)$ noktadan oluşur ve noktalar dikdörtgen bir ızgara gibi dizilir: her dikey çizgide aynı sayıda nokta vardır. Izgarada boşluk olan bir nokta kümesi tek başına bir kartezyen çarpım değildir.

## $A \times B$ ile $B \times A$ birlikte

**Örnek.** $A = \{1, 2, 3\}$ ve $B = \{2, 3, 4\}$ olsun. $(A \times B) \cap (B \times A)$ kaç elemanlıdır?

Bir $(x, y)$ ikilisi iki kümede de olmalı: $A \times B$'de olması için $x \in A$, $y \in B$; $B \times A$'da olması için $x \in B$, $y \in A$. Yani hem $x$ hem $y$, $A \cap B = \{2, 3\}$ kümesinden gelir:

$$(A \times B) \cap (B \times A) = \{2, 3\} \times \{2, 3\} = \{(2, 2), (2, 3), (3, 2), (3, 3)\}$$

![Koordinat düzleminde yalnız A×B'de olan 5 nokta mavi daire, yalnız B×A'da olan 5 nokta kırmızı kare. y = x doğrusu kesikli. Ortadaki yeşil karede iki kümede de bulunan (2, 2), (2, 3), (3, 2), (3, 3) noktaları yeşil daire.](gorsel/tyt-matematik/08-04-simetri.svg "B×A, A×B'nin y = x doğrusuna göre yansımasıdır. Ortak noktalar yeşil karede: x ve y'nin ikisi de A∩B'den gelir.")

Birleşim için kesişimi bir kez çıkar: $9 + 9 - 4 = 14$.

**Kural.**

- $(A \times B) \cap (B \times A) = (A \cap B) \times (A \cap B)$, eleman sayısı $s(A \cap B)^2$.
- Kartezyen çarpım birleşim, kesişim ve fark üzerine dağılır:
  $A \times (B \cup C) = (A \times B) \cup (A \times C)$,
  $A \times (B \cap C) = (A \times B) \cap (A \times C)$,
  $A \times (B \setminus C) = (A \times B) \setminus (A \times C)$.

Örneğin $s(A) = 3$ ve $s(B \cap C) = 2$ ise $s\big((A \times B) \cap (A \times C)\big) = s\big(A \times (B \cap C)\big) = 3 \cdot 2 = 6$.

## ÖSYM tuzakları

> **Bileşenleri çapraz eşitlemek:** $(x, 3) = (5, y)$ ise $x = 5$, $y = 3$'tür. $x = y$ ya da $x = 3$ yazmak yanlıştır; birinci birinciyle, ikinci ikinciyle eşitlenir.

> **$A \times B$ ile $B \times A$'yı aynı sanmak:** Eleman sayıları eşittir ama kümeler farklıdır. "$B \times A$'nın elemanı hangisidir?" sorusunda birinci bileşen $B$'den gelmelidir.

> **Eleman sayılarını toplamak:** $s(A) = 4$, $s(B) = 3$ ise $s(A \times B) = 12$'dir, $7$ değil.

> **Grafikte nokta saymak:** Grafiği verilen $A \times B$'de 6 nokta varsa $s(A) + s(B) = 6$ değildir. $A$'yı x değerlerinden, $B$'yi y değerlerinden ayrı ayrı oku.

> **$(A \times B) \cup (B \times A)$'da ortakları iki kez saymak:** $s(A \times B) + s(B \times A)$ toplamından $s(A \cap B)^2$ çıkarılır.

## Kendini dene

### Soru 1
$(a + 3,\ 2b) = (7,\ b + 5)$ olduğuna göre $a \cdot b$ çarpımı kaçtır?

A) 9
B) 12
C) 16
D) 20
E) 35

**Cevap:** D
**Çözüm:** Birinci bileşenler: $a + 3 = 7$, $a = 4$. İkinci bileşenler: $2b = b + 5$, $b = 5$. Çarpım $4 \cdot 5 = 20$. 9, $a + b$ toplamıdır; 35, $a$ yerine $7$ alınmasından gelir.

### Soru 2
$A = \{1, 2, 3\}$ ve $B = \{2, 3, 4, 5\}$ olduğuna göre $(A \times B) \cap (B \times A)$ kümesi kaç elemanlıdır?

A) 2
B) 4
C) 9
D) 12
E) 16

**Cevap:** B
**Çözüm:** Ortak elemanların iki bileşeni de $A \cap B = \{2, 3\}$ kümesinden gelir: $\{2, 3\} \times \{2, 3\}$, yani $2 \cdot 2 = 4$ eleman: $(2, 2), (2, 3), (3, 2), (3, 3)$. 2, yalnızca $s(A \cap B)$'dir; 12, $s(A \times B)$'dir.

### Soru 3
$A \times B = \{(2, 1), (2, 4), (5, 1), (5, 4), (7, 1), (7, 4)\}$ olduğuna göre $A$ kümesinin elemanları toplamı kaçtır?

A) 5
B) 9
C) 14
D) 19
E) 28

**Cevap:** C
**Çözüm:** $A$, birinci bileşenlerin kümesidir: $A = \{2, 5, 7\}$. Toplam $2 + 5 + 7 = 14$. Birinci bileşenleri tekrarlarıyla toplayan $28$ bulur; bir kümede aynı eleman bir kez yazılır. 19, iki kümenin bütün elemanlarını toplamaktır; 5, $B = \{1, 4\}$ kümesinin toplamıdır.

## Özet kartı

- $(a, b)$ sıralı ikilisinde sıra önemlidir; $(a, b) = (c, d) \iff a = c$ ve $b = d$.
- $A \times B = \{(a, b) \mid a \in A,\ b \in B\}$; birinci bileşen hep ilk yazılan kümeden.
- $s(A \times B) = s(A) \cdot s(B)$; $A \times \varnothing = \varnothing$; $s(A \times A) = s(A)^2$.
- $A \ne B$ ise $A \times B \ne B \times A$, ama eleman sayıları eşittir.
- Grafikte x değerleri $A$'yı, y değerleri $B$'yi verir; noktalar ızgara oluşturur.
- $(A \times B) \cap (B \times A) = (A \cap B)^2$; çarpım $\cup$, $\cap$ ve fark üzerine dağılır.

## Sonraki adım

Alıştırmaya geç (aşağıdaki düğme). Bu dersle **Kümelerde İşlemler** konusu biter. Sonraki konu **Saymanın Temel İlkesi**: $s(A \times B) = s(A) \cdot s(B)$ kuralı orada "çarpma yoluyla sayma"nın ta kendisi olarak karşına çıkacak.
