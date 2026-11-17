---
baslik: Saymanın Temel İlkesi
ders: tyt-matematik
sure: 25 dk
kaynak: MEBİ Konu Özeti 4748fa90fd
guncelleme: 2026-11-18
---
# Saymanın Temel İlkesi

<div class="giris" dir="rtl" lang="ar">

**الدرس ده عن إيه؟** عن مبدأ العدّ الأساسي (saymanın temel ilkesi): إزاي تعرف اختيار معيّن ممكن يتعمل بكام طريقة من غير ما تعدّهم واحد واحد.

- هتفهم إمتى تجمع الحالات اللي بينها "أو" (ya da)، وإمتى تضرب الخطوات اللي بينها "و" (ve).
- هتتعلم طريقة الخانات (kutu yöntemi): تفتح خانة لكل حد بيختار، وتعرف الفرق لما التكرار مسموح أو ممنوع.
- هتحل مسائل الأرقام (rakam problemleri) وتبدأ بالخانة اللي عليها شرط، وتعدّ "واحد على الأقل" (en az bir) عن طريق العكس.

**ليه مهم؟** كل سنة في TYT بييجي سؤال تباديل (permütasyon) أو توافيق (kombinasyon) أو احتمالات (olasılık)، وكلهم مبنيين على الدرس ده، زي "كام عدد أرقامه مختلفة؟" و"كام شفرة ممكنة؟".

الدرس ٢٥ دقيقة بس، ولو مسكت أساسه كويس الباب ده كله هيبقى أسهل عليك.

</div>

**Bu dersin sonunda:** bir seçimin kaç farklı biçimde yapılabileceğini, "ya da" durumlarını toplayarak ve "ve" adımlarını çarparak, rakam ve dağıtım sorularında kısıtlı yerden başlayarak hesaplayabileceksin.

> **TYT'de yeri:** Her yıl permütasyon, kombinasyon ya da olasılık sorusu gelir ve hepsi bu derse dayanır. Tek başına en sık çıkan kalıplar: "rakamları farklı kaç sayı yazılabilir?", "kaç farklı şifre / kombin oluşturulabilir?", "kaç farklı yoldan gidilebilir?" ve "en az biri ... olan kaç tane var?".

## Önce hatırla

<details><summary>Sıralı ikililer ve kartezyen çarpımdan: $A = \{1, 2, 3\}$ ve $B = \{a, b\}$ ise $A \times B$ kümesi kaç elemanlıdır? $B \times A$ ile aynı küme midir?</summary>
$s(A \times B) = s(A) \cdot s(B) = 3 \cdot 2 = 6$. $B \times A$ da 6 elemanlıdır ama <b>aynı küme değildir</b>: $(1, a) \in A \times B$ iken $(a, 1) \in B \times A$ olur ve sıralı ikililerde sıra önemlidir.
</details>

<details><summary>Sıralı ikililer ve kartezyen çarpımdan: $(x + 1, 5) = (4, y - 2)$ ise $x + y$ kaçtır?</summary>
Sıralı ikililer eşitse karşılıklı bileşenler eşittir: $x + 1 = 4 \Rightarrow x = 3$; $5 = y - 2 \Rightarrow y = 7$. $x + y = 10$.
</details>

## Saymak, eşlemektir

**Örnek.** Bir kitabın 15. sayfasından 42. sayfasına kadar (ikisi de dahil) okursan kaç sayfa okumuş olursun?

Sayfaları sırayla $1, 2, 3, \dots$ ile eşle: 15. sayfa 1'e, 16. sayfa 2'ye, … 42. sayfa $42 - 14 = 28$'e eşlenir. Cevap **28** sayfa; $42 - 15 = 27$ değil.

Bir kümenin elemanlarını pozitif tam sayılarla sırayla birebir eşleyerek saymaya **birebir eşleme yoluyla sayma** denir. Kısa yol: $a$'dan $b$'ye kadar ardışık tam sayıların sayısı $b - a + 1$'dir.

## Toplama yoluyla sayma: "ya da"

**Örnek.** Kantinde 4 çeşit tost ve 3 çeşit sandviç var. Yalnızca **bir** yiyecek alacaksın. Kaç farklı seçim yapabilirsin?

Ya tost alırsın (4 yol) ya da sandviç alırsın (3 yol). İkisi aynı anda olmaz, yani durumlar **ayrık**tır: $4 + 3 = 7$.

**Kural.** Birbirini dışlayan (aynı anda olamayan) durumlar **toplanır**. $A$ ve $B$ sonlu, ayrık kümelerse
$$s(A \cup B) = s(A) + s(B).$$

## Çarpma yoluyla sayma: "ve"

**Örnek.** 3 tişörtün (kırmızı K, mavi M, yeşil Y) ve 2 pantolonun (siyah S, gri G) var. Bir tişört **ve** bir pantolon giyeceksin. Kaç farklı kombin yapabilirsin?

Her tişört seçiminden sonra 2 pantolon seçeneği açılır. Ağaç çizince dallar $3 \cdot 2 = 6$ uca ulaşır.

![Ağaç şeması: soldaki başlangıç noktasından K, M, Y adlı üç tişörte dal çıkıyor; her tişörtten S ve G adlı iki pantolona dal çıkıyor; sağda (K, S)'den (Y, G)'ye kadar altı kombin yazılı.](gorsel/tyt-matematik/09-01-agac.svg "Her tişörtten aynı sayıda (2) dal çıkıyor. Bu yüzden uçları tek tek saymak yerine 3 ile 2 çarpılır.")

Kombinlerin her biri bir sıralı ikilidir: $(K, S)$, $(K, G)$, … Yani bu sayma, önceki dersteki $A \times B$ kümesinin eleman sayısıdır: $s(A \times B) = 3 \cdot 2$.

**Kural.** Art arda yapılan ("ve" ile bağlanan) seçimlerde seçenek sayıları **çarpılır**. $s(A) = m$, $s(B) = n$ ise $s(A \times B) = m \cdot n$.

## Saymanın temel ilkesi

**Örnek.** Bir okul dolabının şifresi önce bir harf (A, B ya da C), sonra iki rakamdan (0–9) oluşuyor. Rakamlar aynı olabilir (B07, A55 gibi). Kaç farklı şifre vardır?

Şifreyi üç kutu gibi düşün ve her kutuya kaç seçenek olduğunu yaz:

$$\underbrace{3}_{\text{harf}} \cdot \underbrace{10}_{\text{1. rakam}} \cdot \underbrace{10}_{\text{2. rakam}} = 300.$$

**Kural (saymanın temel ilkesi).** Bir iş $k$ adımda yapılıyorsa ve 1. adım $n_1$, 2. adım $n_2$, …, $k$'ninci adım $n_k$ farklı biçimde yapılabiliyorsa iş toplam
$$n_1 \cdot n_2 \cdot n_3 \cdots n_k$$
farklı biçimde yapılır. Önemli olan, bir adımın **seçenek sayısının** önceki adımda ne seçildiğine bağlı olmamasıdır.

## Tekrarlı mı, tekrarsız mı?

**Örnek.** 3 öğrenci, okuldaki 5 kulüpten birine yazılacak.

a) Birden fazla öğrenci aynı kulübe yazılabiliyorsa kaç farklı durum olur?
b) Her kulübe en çok bir öğrenci yazılabiliyorsa kaç farklı durum olur?

Burada **seçimi yapan öğrencidir**; her öğrenci için bir kutu aç.

a) Her öğrencinin önünde 5 kulüp var: $5 \cdot 5 \cdot 5 = 5^3 = 125$.
b) 1. öğrenci 5 kulüpten birini, 2. öğrenci kalan 4 kulüpten birini, 3. öğrenci kalan 3 kulüpten birini seçer: $5 \cdot 4 \cdot 3 = 60$.

![Kutu yöntemi, iki satır. Üst satır: 5, 5, 5 yazılı üç kutu, sonuç 125. Alt satır: 5, 4, 3 yazılı üç kutu, sonuç 60. Kutuların altında 1., 2., 3. öğrenci yazıyor.](gorsel/tyt-matematik/09-01-kutular.svg "Kutu sayısı seçim yapan öğrenci sayısı kadar. Tekrar yasaksa her kutuda seçenek bir azalır.")

**Kural.** Kutu sayısı = seçim yapanların sayısı. Tekrar serbestse her kutuya aynı sayı yazılır: $n$ seçeneği olan $k$ kişi için $n^k$. Tekrar yasaksa sayılar birer azalır: $n \cdot (n - 1) \cdot (n - 2) \cdots$

## Rakam problemleri

**Örnek.** $\{0, 1, 2, 3, 4, 5\}$ kümesinin rakamlarıyla, rakamları **farklı** üç basamaklı kaç **çift** sayı yazılabilir?

İki kısıt var: yüzler basamağı $0$ olamaz, birler basamağı çift olmalı ($0$, $2$ ya da $4$). Birler basamağına $0$ gelirse yüzler basamağının seçenek sayısı değişir. Bu yüzden iki **ayrık durum**a ayırırız:

- **Birler 0:** önce birlere $0$ (1 yol). Yüzlere kalan 5 rakamdan biri (5 yol), onlara kalan 4 rakamdan biri: $5 \cdot 4 \cdot 1 = 20$.
- **Birler 2 ya da 4:** birlere 2 yol. Yüzlere $0$ ve birlerdeki rakam dışında 4 yol, onlara kalan 4 rakam ($0$ artık kullanılabilir): $4 \cdot 4 \cdot 2 = 32$.

Durumlar "ya da" ile bağlı, toplanır: $20 + 32 = 52$.

![Kutu yöntemi, iki durum. Birinci durum, birler 0: yüzler 5, onlar 4, birler 1, sonuç 20. İkinci durum, birler 2 ya da 4: yüzler 4, onlar 4, birler 2, sonuç 32. Altta toplam 20 artı 32 eşittir 52.](gorsel/tyt-matematik/09-01-rakam.svg "Her durumun içinde çarpılır, durumlar kendi aralarında toplanır. 0 birlerde mi değil mi sorusu yüzler basamağının seçenek sayısını değiştiriyor.")

**Kural.** Önce **kısıtlı** basamağı doldur (yüzler 0 olamaz, birler çift olmalı gibi). Bir kısıt diğerinin seçenek sayısını değiştiriyorsa soruyu durumlara ayır, her durumu çarp, sonuçları topla.

![Yöntem akışı: doldurulacak yerleri belirle, kısıtlı yerden başla, her yere seçenek yaz. Tek kalıp yeter mi? Evet ise kutuları çarp; hayır ise durumlara ayır, çarp, sonra durumları topla.](gorsel/tyt-matematik/09-01-yontem.svg "Saymanın temel ilkesi sorularında izlenecek sıra. Takıldığın yer genellikle kısıtlı yeri sona bırakmaktır.")

## Tümleyenle sayma: "en az bir"

**Örnek.** Üç basamaklı doğal sayıların kaçında **en az bir** rakam 5'tir?

"En az bir 5" içinde bir tane, iki tane, üç tane 5 olan durumlar var; tek tek saymak uzun sürer. Tersini say:

- Bütün üç basamaklı sayılar: $9 \cdot 10 \cdot 10 = 900$.
- **Hiç** 5 içermeyenler: yüzlere $0$ ve $5$ dışında 8 rakam, onlara ve birlere 5 dışında 9'ar rakam: $8 \cdot 9 \cdot 9 = 648$.
- En az bir 5 olanlar: $900 - 648 = 252$.

**Kural.** En az bir = tümü − hiç olmayan.

## ÖSYM tuzakları

> **"Ya da" ile "ve"yi karıştırmak:** 4 tost ve 3 sandviçten **bir** yiyecek seçmek $4 + 3 = 7$; bir tost **ve** bir sandviç seçmek $4 \cdot 3 = 12$ yoldur. Soru kökündeki bağlacı bul.

> **Üssü ters yazmak:** 3 öğrenci 5 kulüpten birini seçiyorsa cevap $5^3 = 125$'tir, $3^5 = 243$ değil. Kutuyu **seçim yapana** aç; her kutuya onun seçenek sayısını yaz.

> **Sıfırı unutmak:** $\{0, 1, 2, 3, 4\}$ ile rakamları farklı üç basamaklı sayı sayısı $5 \cdot 4 \cdot 3 = 60$ değil, $4 \cdot 4 \cdot 3 = 48$'dir. Yüzler basamağına $0$ gelemez ama onlar basamağına gelebilir.

> **Kısıtlı yeri sona bırakmak:** "Rakamları farklı çift sayı" sorusunda yüzlerden başlayıp birlere gelince "kaç çift rakam kaldı?" sorusunun cevabı belli olmaz. Önce birleri doldur; gerekirse durumlara ayır.

> **"En az bir"i doğrudan saymak:** "En az bir 5" için $1 \cdot 9 \cdot 9$ gibi tek bir çarpım yazmak 5'in başka basamakta olduğu sayıları atlar; "5'i bir basamağa koy, kalanları serbest bırak" demek ise birden çok 5 içeren sayıları birden çok kez sayar. Tümleyeni kullan.

## Kendini dene

### Soru 1
Bir restoranın menüsünde 4 çeşit çorba, 5 çeşit ana yemek ve 3 çeşit tatlı vardır. Bir çorba, bir ana yemek ve bir tatlıdan oluşan kaç farklı menü seçilebilir?

A) 12
B) 20
C) 32
D) 60
E) 120

**Cevap:** D
**Çözüm:** Üç seçim art arda ("ve") yapılır, çarpılır: $4 \cdot 5 \cdot 3 = 60$. 12, sayıları toplamaktır (bu "yalnızca bir yemek" sorusunun cevabı olurdu); 20 tatlıyı unutmaktır; 120 ise 60'ı gereksiz yere 2 ile çarpmaktır.

### Soru 2
Bir otelde 6 boş oda vardır. Gelen 3 misafirin her biri ayrı bir odaya yerleştirilecektir. Bu yerleştirme kaç farklı biçimde yapılabilir?

A) 18
B) 20
C) 120
D) 216
E) 729

**Cevap:** C
**Çözüm:** Kutuları misafirlere aç. 1. misafir 6 odadan birine, 2. misafir kalan 5 odadan birine, 3. misafir kalan 4 odadan birine: $6 \cdot 5 \cdot 4 = 120$. 216, aynı odaya birden fazla misafir koymaktır ($6^3$); 729 üssü ters yazmaktır ($3^6$); 18 ise $6 \cdot 3$'tür.

### Soru 3
$\{0, 1, 2, 3, 4\}$ kümesinin rakamları kullanılarak rakamları birbirinden farklı üç basamaklı kaç doğal sayı yazılabilir?

A) 36
B) 48
C) 60
D) 64
E) 100

**Cevap:** B
**Çözüm:** Kısıtlı basamaktan başla: yüzlere $0$ gelemez, 4 seçenek. Onlara kalan 4 rakam ($0$ dahil), birlere kalan 3 rakam: $4 \cdot 4 \cdot 3 = 48$. 60, $0$'ın yüzlere gelemeyeceğini unutmaktır ($5 \cdot 4 \cdot 3$); 100, rakamların tekrar edebileceğini sanmaktır ($4 \cdot 5 \cdot 5$).

## Özet kartı

- "Ya da" ile ayrılan, aynı anda olamayan durumlar **toplanır**; "ve" ile art arda yapılan seçimler **çarpılır**.
- Saymanın temel ilkesi: adımların seçenek sayıları $n_1 \cdot n_2 \cdots n_k$ biçiminde çarpılır.
- Kutuyu seçim yapana aç. Tekrar serbestse $n^k$, yasaksa $n \cdot (n-1) \cdot (n-2) \cdots$
- Rakam sorularında yüzler (en soldaki) basamak $0$ olamaz. Kısıtlı basamağı önce doldur.
- Bir kısıt diğerinin seçenek sayısını değiştiriyorsa durumlara ayır, her durumu çarp, sonuçları topla.
- En az bir = tümü − hiç olmayan.

## Sonraki adım

Alıştırmaya geç (aşağıdaki düğme). Sonraki ders **Faktöriyel Kavramı**; bu derste yazdığın $5 \cdot 4 \cdot 3 \cdot 2 \cdot 1$ gibi azalan çarpımların kısa yazılışını öğreneceksin.
