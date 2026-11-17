---
baslik: Tanım, Aksiyom, Teorem ve İspat Kavramları
ders: tyt-matematik
sure: 20 dk
kaynak: MEBİ Konu Özeti f65ea46531
guncelleme: 2026-11-18
---
# Tanım, Aksiyom, Teorem ve İspat Kavramları

<div class="giris" dir="rtl" lang="ar">

**الدرس ده عن إيه؟** عن الأساس اللي الرياضيات كلها مبنية عليه: التعريف (tanım)، والمسلّمة (aksiyom)، والنظرية (teorem)، والبرهان (ispat).

- هتفرّق بين الحاجات اللي بنقبلها من غير تعريف، زي النقطة والمستقيم والمستوى، والحاجات اللي بنعرّفها بيها.
- هتكتب أي نظرية على شكل "لو كذا يبقى كذا"، وتطلّع منها الفرض (hipotez) والمطلوب (hüküm).
- هتفهم إن كام مثال مش برهان، وإن مثال مضاد (karşı örnek) واحد كفاية يوقّع أي ادعاء.

**ليه مهم؟** الموضوع ده نادر ييجي لوحده في TYT، بس فكرته مستخبية في أسئلة كتير من النوع الجديد، زي إنك تدوّر على الرقم اللي بيكسر ادعاء معيّن.

٢٠ دقيقة بس، وبيهم تقفل موضوع القضايا (önermeler) كله. يلا بينا.

</div>

**Bu dersin sonunda:** bir cümlenin tanım mı, aksiyom mu, teorem mi olduğunu ayırt edebilecek, bir teoremi $p \Rightarrow q$ biçiminde yazıp hipotezini ve hükmünü bulabilecek, bir iddiayı ispatla doğrulamanın ya da tek bir karşı örnekle çürütmenin yolunu gösterebileceksin.

> **TYT'de yeri:** Bu konu tek başına seyrek gelir; gelirse kavram sorusudur: "Hangisi tanımsız terimdir?", "Teoremin hipotezi hangisidir?", "Aksiyomlarda hangi özellik aranmaz?" Ama yeni nesil soruların çoğunda gizlice vardır: bir iddianın karşıtının doğru olup olmadığı ya da bir iddiayı çürüten sayının hangisi olduğu sorulur.

## Önce hatırla

<details><summary>Niceleyicilerden: ∀x ∈ ℕ, x ≥ 1 önermesi doğru mu? Bunu göstermek için kaç sayı yeter?</summary>
Yanlış. $0 \in \mathbb{N}$ ve $0 \ge 1$ yanlıştır. "Her" ile kurulan bir önermeyi çürütmek için <b>tek bir karşı örnek</b> yeter. Bu derste aynı fikir teoremlerde karşına çıkacak.
</details>

<details><summary>Niceleyicilerden: ∀x ∈ ℤ, x² > 0 önermesinin değilini yaz. Hangisi doğrudur?</summary>
Değili: $\exists x \in \mathbb{Z},\ x^2 \le 0$. Niceleyici ve koşul birlikte değişir, küme aynı kalır. $x = 0$ için $0 \le 0$ doğru olduğundan değili <b>doğru</b>, asıl önerme yanlıştır.
</details>

## Matematik nasıl kurulur?

Matematikte her şey bir zincir gibi birbirine dayanır. Zincirin en altında tanımlanmayan terimler ve ispatlanmayan kabuller vardır; üst halkalar bunların üzerine ispatla eklenir.

![Akış şeması. Tanımsız terimler kullanılarak tanımlar yapılır. Tanımlar, ispatsız kabul edilen aksiyomlar ve doğru kabul edilen hipotez ispata girer. İspattan teorem çıkar; teorem sonraki ispatlarda yeniden kullanılır.](gorsel/tyt-matematik/06-06-yapi.svg "İspatın dört kaynağı vardır: tanımlar, aksiyomlar, hipotez ve daha önce ispatlanmış teoremler. Teorem bir kez ispatlanınca yeni ispatlarda kullanılır.")

Bu dersteki dört kavram şu sorulara cevap verir:

| Kavram | Hangi soruya cevap verir? | Örnek |
|---|---|---|
| Tanım | Bu kavram nedir? | Kare, dört kenarı eşit ve bir açısı dik olan dörtgendir. |
| Aksiyom | Neyi ispatsız doğru kabul ediyoruz? | İki farklı noktadan bir ve yalnız bir doğru geçer. |
| Teorem | Neyi ispatladık? | İki tek sayının toplamı çifttir. |
| İspat | Teoremin doğru olduğunu nasıl gösterdik? | Aşağıdaki adım adım akıl yürütme. |

## Tanımsız ve tanımlı terimler

**Örnek.** "Doğru parçası" nedir? Bir doğru üzerindeki iki nokta ile bu noktaların arasındaki noktalardan oluşan kümedir. Peki "nokta" nedir? "Boyutu olmayan yer" desen, "yer" ve "boyut" kelimelerini de tanımlaman gerekir. Her yeni tanım yeni kelimeler ister; bir yerde durmak zorundasın.

Bu yüzden matematik bazı terimleri **tanımlamadan** kabul eder: **nokta, doğru, düzlem**. Herkes ne olduklarını sezgiyle bilir. Doğru parçası, ışın, açı, üçgen ise bunlar kullanılarak tanımlanır.

**Kural.**

- **Tanımsız terim:** Başka bir terime dayanmadan anlaşılan, tanımı yapılmayan terimdir. Nokta, doğru ve düzlem tanımsız terimlerdir.
- **Tanımlı terim:** Tanımsız terimler ve daha önce tanımlanmış terimler kullanılarak tanımlanan terimdir. Doğru parçası, ışın, açı, üçgen, kare tanımlı terimlerdir.

## İyi bir tanım nasıl olur?

**Örnek.** Bir öğrenci kareyi üç farklı biçimde tanımlıyor:

1. "Kare, dört kenarı eşit olan dörtgendir."
2. "Kare, kare biçimindeki dörtgendir."
3. "Kare, dört kenarı eşit ve bir açısı dik olan dörtgendir."

Birincisi **fazla geniştir**: eşkenar dörtgen de dört kenarı eşit bir dörtgendir ama kare değildir. İkincisi **kendini kullanır**: "kare"yi bilmeyen biri bu cümleden bir şey öğrenemez. Üçüncüsü doğru tanımdır: her kare bu iki özelliği taşır ve bu iki özelliği taşıyan her dörtgen karedir.

![Dörtgenler kümesi içinde iki kesişen daire. Mavi daire dört kenarı eşit olanlar, içinde eşkenar dörtgen. Sarı daire dört açısı dik olanlar, içinde dikdörtgen. Kesişimde kare var. Dışarıda bir yamuk.](gorsel/tyt-matematik/06-06-kare-tanimi.svg "Yalnız dört kenarı eşit demek mavi dairenin tamamını alır. Bir açının dik olduğunu eklemek yalnızca yeşil kesişimi, yani kareleri bırakır.")

**Kural.** Bir tanım:

- anlamı bilinen sözcüklerle, tanımsız terimlerle ya da önceden tanımlanmış terimlerle yapılır; tanımlanan kelimenin kendisini kullanmaz,
- tutarlı, açık ve anlaşılır olur,
- tanımlanan kavramın **tamamını** kapsar ve **başka hiçbir şeyi** içine almaz (kesin olur).

## Aksiyom

**Örnek.** "İki farklı noktadan bir ve yalnız bir doğru geçer." Bunu ispatlamaya çalış: dayanacağın şey nokta ve doğrudur, ikisi de tanımsızdır. Daha temel bir bilgi yoktur. Bu cümleyi ispatsız **doğru kabul ederiz**; böyle cümlelere aksiyom denir.

Başka örnekler: "Bir doğru dışındaki bir noktadan bu doğruya yalnız bir paralel çizilebilir." ve sayılarda "$a + b = b + a$" (toplamanın değişme özelliği).

**Kural.** İspata gerek duyulmadan doğruluğu kabul edilen önermeye **aksiyom** denir. Bir aksiyom sistemi:

- **Çelişkisiz** olmalıdır: iki aksiyom birbirinin tersini söylememelidir.
- **Bağımsız** olmalıdır: bir aksiyom, diğer aksiyomlardan çıkarılabiliyorsa o aksiyom değil teoremdir; listeden atılır.
- **Olabildiğince az** sayıda olmalıdır.

Bağımsızlığa bir örnek: "Her takımda en az iki oyuncu vardır." kuralı varken "Her takımda en az bir oyuncu vardır." ayrıca aksiyom olarak yazılmaz, çünkü ilkinden çıkar.

## Teorem: hipotez ve hüküm

**Örnek.** Teorem: "Bir üçgenin iki kenarı eşitse bu kenarların karşısındaki açılar eşittir."

Bunu "ise" ile yaz. $p$: "ABC üçgeninde $|AB| = |AC|$", $q$: "$m(\widehat{B}) = m(\widehat{C})$". Teorem $p \Rightarrow q$ biçimindedir.

![İkizkenar ABC üçgeni. AB ve AC kenarlarında mavi eşitlik çizikleri var. B ve C köşelerinde yeşil açı yayları ve soru işaretleri var. Yanda mavi kutuda hipotez: AB eşittir AC, yeşil kutuda hüküm: B açısı eşittir C açısı.](gorsel/tyt-matematik/06-06-hipotez-hukum.svg "Mavi çizikler bize verilendir: hipotez. Yeşil soru işaretli açılar gösterilmesi gerekendir: hüküm.")

- $p$, teoremde **verilen** kısımdır: **hipotez**.
- $q$, teoremde **gösterilmesi istenen** kısımdır: **hüküm**.

Cümlede "ise" geçmese de teorem bu biçime sokulur:

| Teorem | Hipotez ($p$) | Hüküm ($q$) |
|---|---|---|
| Dikdörtgenin köşegenleri eşittir. | ABCD bir dikdörtgendir. | $\lvert AC \rvert = \lvert BD \rvert$ |
| İki tek sayının toplamı çifttir. | $a$ ve $b$ tek tam sayılardır. | $a + b$ çifttir. |
| Bir sayının karesi, sayı çiftse çifttir. | $n$ çifttir. | $n^2$ çifttir. |

Son satıra dikkat: cümlenin başında olan hüküm, sonunda olan hipotezdir. Sırayı cümlenin düzeni değil, **"neyin verildiği"** belirler.

**Kural.** Doğruluğu ispatla gösterilen önermeye **teorem** denir. Teorem $p \Rightarrow q$ biçiminde yazılır; $p$ **hipotez**, $q$ **hüküm**dür.

Bir teoremin **karşıtı** ($q \Rightarrow p$) teorem olmak zorunda değildir. "Bir dörtgen kare ise köşegenleri eşittir." doğrudur; karşıtı "Köşegenleri eşit olan dörtgen karedir." yanlıştır: köşegenleri eşit olan ama kare olmayan dikdörtgen karşı örnektir. Hem $p \Rightarrow q$ hem $q \Rightarrow p$ teoremse $p \Leftrightarrow q$ yazılır.

## İspat

**Örnek.** Teorem: "$a$ ve $b$ tek tam sayılar ise $a + b$ çifttir."

Önce örneklere bak: $5 + 7 = 12$. Her tek sayı ikişerli gruplar ve bir artık noktadan oluşur. İki tek sayı toplanınca iki artık nokta yeni bir çift olur.

![Üstte 5 nokta: iki çift mavi ve bir kırmızı artık; 7 nokta: üç çift sarı ve bir kırmızı artık. Altta toplam 12 nokta altı çift olarak dizilmiş; iki kırmızı artık kesikli çerçevede yan yana bir çift oluşturuyor.](gorsel/tyt-matematik/06-06-tek-tek.svg "Tek sayının tanımı: ikişerli gruplar artı bir. İki artık birleşince toplamda artık kalmaz, bu yüzden toplam çifttir.")

Şekil bir fikir verir ama yalnızca 5 ile 7 içindir. **İspat** her tek sayı çifti için geçerli olmalıdır:

| Adım | Gerekçe |
|---|---|
| $a = 2m + 1$ ve $b = 2n + 1$ ($m, n \in \mathbb{Z}$) | Hipotez ve tek sayının tanımı |
| $a + b = 2m + 2n + 2$ | Toplama |
| $a + b = 2(m + n + 1)$ | Dağılma özelliği (aksiyom) |
| $m + n + 1$ bir tam sayıdır, öyleyse $a + b$ çifttir. | Tam sayılarda toplama, çift sayının tanımı |

Her adımın bir gerekçesi var: hipotez, bir tanım, bir aksiyom ya da daha önce ispatlanmış bir teorem.

**Kural.** Bir teoremin doğru olduğunu göstermeye **ispat** denir. $p \Rightarrow q$ teoreminde $p$ doğru kabul edilir ve $q$'nun doğru olduğu gösterilir. İspatta yalnızca şunlar kullanılır: **hipotez, tanımlar, aksiyomlar ve önceden ispatlanmış teoremler.**

### Örnek ispat değildir; karşı örnek çürütür

"Her asal sayı tektir." Denersen $3, 5, 7, 11, 13$ tektir. Ama $2$ hem asal hem çifttir. Tek bir karşı örnek iddiayı **yanlış** yapar. Tersine yüz örnek bile bir "her" iddiasını ispatlamaz.

$p \Rightarrow q$ biçimindeki bir iddiayı çürütmek için $p$'nin doğru, $q$'nun yanlış olduğu bir durum bulmak yeter (Koşullu Önerme dersindeki $1 \Rightarrow 0$ satırı).

### Karşıt tersle ispat

Teorem: "$n^2$ tek ise $n$ tektir." Doğrudan ispatı zordur. Ama $p \Rightarrow q \equiv q' \Rightarrow p'$ olduğundan karşıt tersini ispatlamak yeter: "$n$ çift ise $n^2$ çifttir." $n = 2k$ ise $n^2 = 4k^2 = 2(2k^2)$, yani çifttir. Karşıt ters doğru olduğuna göre asıl teorem de doğrudur.

## ÖSYM tuzakları

> **Örnekle ispat yapmak:** "$1 + 3$, $5 + 7$, $9 + 11$ çift; öyleyse iki tek sayının toplamı çifttir, ispatlandı." Yanlış. Bu bir ispat değil, yalnızca denemedir. İspat her sayı için geçerli harflerle ($2m + 1$ gibi) yapılır.

> **Hipotez ile hükmü cümle sırasına göre seçmek:** "Bir sayının karesi, sayı çiftse çifttir." cümlesinde hipotez "sayı çifttir"dir; cümlenin sonunda olsa da verilen odur.

> **Teoremin karşıtını da doğru saymak:** "Kare ise köşegenleri eşittir." doğru, "Köşegenleri eşitse karedir." yanlıştır. Asıl teoreme denk olan karşıt tersidir: "Köşegenleri eşit değilse kare değildir."

> **Aksiyomu "henüz ispatlanmamış teorem" sanmak:** Aksiyom ispatlanmaz, kabul edilir. Teorem ise ispatlanmadan kabul edilmez.

> **Açıyı, ışını, üçgeni tanımsız saymak:** Tanımsız terimler yalnızca **nokta, doğru, düzlem**dir. Doğru parçası, ışın, açı, üçgen tanımlıdır.

## Kendini dene

### Soru 1
Aşağıdakilerden hangisi tanımsız bir terimdir?

A) Açı
B) Işın
C) Düzlem
D) Üçgen
E) Doğru parçası

**Cevap:** C
**Çözüm:** Tanımsız terimler nokta, doğru ve düzlemdir. Açı iki ışınla, ışın bir doğru ve bir noktayla, üçgen doğru parçalarıyla, doğru parçası da iki nokta ile tanımlanır; hepsi tanımlı terimdir.

### Soru 2
"Bir tam sayı 4'e bölünüyorsa çifttir." teoremi veriliyor.

Bu teoremin hükmü ve teoremin karşıtının doğruluk değeri sırasıyla aşağıdakilerden hangisidir?

A) Sayı 4'e bölünür; 1
B) Sayı 4'e bölünür; 0
C) Sayı çifttir; 1
D) Sayı çifttir; 0
E) Sayı tam sayıdır; 1

**Cevap:** D
**Çözüm:** Verilen "4'e bölünür" olduğundan hipotez odur; gösterilen "çifttir" hükümdür. Karşıtı: "Bir tam sayı çiftse 4'e bölünür." $2$ çifttir ama 4'e bölünmez; karşı örnek var, karşıtın değeri 0. A ve B hipotez ile hükmü karıştırır; C karşıtı da doğru sayar.

### Soru 3
"$n$ tek tam sayı ise $n^2$ tektir." teoremi şöyle ispatlanıyor:

$n = 2k + 1$ ($k \in \mathbb{Z}$) olsun. $n^2 = 4k^2 + 4k + 1 = 2 \cdot (\ \ \ \ ) + 1$. Parantez içi bir tam sayı olduğundan $n^2$ tektir.

Boş bırakılan yere aşağıdakilerden hangisi yazılmalıdır?

A) $k^2 + k$
B) $2k^2 + k$
C) $2k^2 + 2k$
D) $2k^2 + 2k + 1$
E) $4k^2 + 4k$

**Cevap:** C
**Çözüm:** $(2k + 1)^2 = 4k^2 + 4k + 1$. İlk iki terimden 2 parantezine al: $4k^2 + 4k = 2(2k^2 + 2k)$. Böylece $n^2 = 2(2k^2 + 2k) + 1$. A, 4'ü ortak çarpan alıp 2 yazmanın sonucudur; D, 1'i de parantezin içine katar; E ise 2'yi hiç dışarı almaz.

## Özet kartı

- Tanımsız terimler: nokta, doğru, düzlem. Diğer terimler bunlarla tanımlanır.
- İyi tanım bilinen terimlerle yapılır, kendini kullanmaz, kavramın tamamını alır ve başka hiçbir şeyi almaz.
- Aksiyom ispatsız kabul edilir; aksiyomlar çelişkisiz, bağımsız ve olabildiğince az olur.
- Teorem ispatlanan önermedir: $p \Rightarrow q$; $p$ hipotez (verilen), $q$ hüküm (gösterilecek).
- İspatta hipotez, tanım, aksiyom ve önceki teoremler kullanılır; örnekler ispat değildir, tek karşı örnek ise çürütür.
- Teoremin karşıtı teorem olmayabilir; karşıt tersi ise her zaman asıl teoreme denktir.

## Sonraki adım

Alıştırmaya geç (aşağıdaki düğme). Bununla **Önermeler ve Bileşik Önermeler** konusu bitiyor. Sonraki ders **Kümelerde Temel Kavramlar**; burada gördüğün "ve", "veya", "değil" bağlaçlarının kesişim, birleşim ve tümleyen olarak geri döndüğünü göreceksin.
