---
baslik: Açı Kavramı ve Çeşitleri
ders: tyt-matematik
sure: 20 dk
kaynak: MEBİ Konu Özeti 46407f0b2d
guncelleme: 2026-11-17
---
# Açı Kavramı ve Çeşitleri

**Bu dersin sonunda:** bir açıyı ölçüsüne göre adlandırabilecek; tümler, bütünler, ters açı ve açıortay bilgisini kullanarak bilinmeyen açıyı bir denklemle bulabileceksin.

> **TYT'de yeri:** Bu konu tek başına nadiren soru olur, ama geometri sorularının neredeyse hepsinde bir adım olarak karşına çıkar: "bir doğru üzerindeki açılar toplamı 180°", "ters açılar eşittir", "açıortay açıyı ikiye böler". Ayrıca "tümleri ile bütünlerinin toplamı…" kalıbında denklem kurma sorusu olarak gelir.

## Önce hatırla

<details><summary>Geçen dersten: Bir daire grafiğinde %25'lik dilimin merkez açısı kaç derecedir?</summary>
$\%1 = 3{,}6^\circ$ olduğundan $25 \cdot 3{,}6^\circ = $ <b>90°</b>; dairenin dörtte biri. Bu dersin adıyla bu bir <b>dik açı</b>dır.
</details>

<details><summary>Geçen dersten: 60 kişilik bir grubun daire grafiğinde 20 kişiyi gösteren dilimin merkez açısı kaç derecedir?</summary>
Bir kişi $360^\circ : 60 = 6^\circ$; $20 \cdot 6^\circ = $ <b>120°</b>. Bu açı 90° ile 180° arasında olduğu için bir <b>geniş açı</b>dır. Bugün tam çemberin neden $360^\circ$ sayıldığını da göreceksin.
</details>

## Açı nedir, nasıl ölçülür?

Başlangıç noktaları ortak olan iki ışının birleşimine **açı** denir. Ortak nokta açının **köşesi**, ışınlar açının **kollarıdır**.

- Kolları $[OA$ ve $[OB$ olan açı $\widehat{AOB}$ ya da $\widehat{BOA}$ diye yazılır. **Köşe her zaman ortadaki harftir.** Karışıklık yoksa yalnızca $\widehat{O}$ de yazılabilir.
- Açının ölçüsü $m(\widehat{AOB})$ ile gösterilir.
- **1 derece ($1^\circ$):** Tam çemberi 360 eş parçaya böldüğünde, bir parçayı gören merkez açının ölçüsüdür. Bu yüzden tam bir tur $360^\circ$'dir; daire grafiğindeki dilim açıları da bu birimle ölçülür.

## 1. Ölçüsüne göre açı türleri

**Örnek.** Saat tam 2'de, 3'te, 5'te ve 6'da akrep ile yelkovan arasındaki küçük açı hangi türdendir?

**Çözüm.** Saat kadranı 12 eş parçadır; iki komşu rakam arası $360^\circ : 12 = 30^\circ$.

| Saat | Açı | Tür |
|---|---|---|
| 2:00 | $2 \cdot 30^\circ = 60^\circ$ | dar |
| 3:00 | $3 \cdot 30^\circ = 90^\circ$ | dik |
| 5:00 | $5 \cdot 30^\circ = 150^\circ$ | geniş |
| 6:00 | $6 \cdot 30^\circ = 180^\circ$ | doğru |

![Altı küçük çizim. Birincisi O köşeli, OA ve OB kollu bir açı. Diğerleri: 40 derecelik dar açı, dik açı işaretli 90 derece, 130 derecelik geniş açı, iki kolu zıt yönde 180 derecelik doğru açı, iki kolu üst üste 360 derecelik tam açı.](gorsel/tyt-matematik/18-01-aci-cesitleri.svg "Açının türünü kolların uzunluğu değil, aralarındaki açıklık belirler. Tam açıda iki kol üst üste gelir ve bir tam tur atılmıştır.")

**Kural:**

| Tür | Ölçü |
|---|---|
| Dar açı | $0^\circ < m(\widehat{AOB}) < 90^\circ$ |
| Dik açı | $90^\circ$ (şekilde küçük kareyle gösterilir) |
| Geniş açı | $90^\circ < m(\widehat{AOB}) < 180^\circ$ |
| Doğru açı | $180^\circ$ (kollar bir doğru oluşturur) |
| Tam açı | $360^\circ$ |

> **Tuzak:** $90^\circ$ dar açı değildir, $180^\circ$ geniş açı değildir. Eşitlik durumları kendi adlarını alır: dik açı, doğru açı.

## 2. Tümler ve bütünler açılar

**Örnek.** Bir açının tümleri ile bütünlerinin ölçüleri toplamı $200^\circ$ ise bu açı kaç derecedir?

**Çözüm.**

1. Açıya $x$ de. Tümleri $90^\circ - x$, bütünleri $180^\circ - x$.
2. $(90 - x) + (180 - x) = 200 \Rightarrow 270 - 2x = 200 \Rightarrow x = 35^\circ$.
3. Kontrol: tümleri $55^\circ$, bütünleri $145^\circ$; toplam $200^\circ$.

![İki çizim. Solda OA ve OB arasında dik açı, araya OC ışını çizilmiş: AOC 35 derece, COB 55 derece. Sağda B, O, A bir doğru üzerinde, OC ışını: AOC 35 derece, COB 145 derece.](gorsel/tyt-matematik/18-01-tumler-butunler.svg "Aynı 35° iki farklı tamamlayıcıyla: soldakinde 90°'ye (tümler), sağdakinde 180°'ye (bütünler) tamamlanıyor. Ortak kolları olduğu için ikisi de komşu açıdır.")

**Kural:**

- Ölçüleri toplamı $90^\circ$ olan iki açı **tümler**, $180^\circ$ olan iki açı **bütünler** açılardır.
- $x$'in tümleri $90^\circ - x$, bütünleri $180^\circ - x$'tir. Her zaman: bütünleri $-$ tümleri $= 90^\circ$.
- Köşeleri ve birer kolları ortak, iç bölgeleri ayrı olan açılara **komşu açılar** denir. Şekildeki gibi hem komşu hem tümler olanlara **komşu tümler**, hem komşu hem bütünler olanlara **komşu bütünler** açılar denir.
- Bir doğru üzerinde bir noktada yan yana duran açıların toplamı $180^\circ$'dir.

> **Tuzak:** Yalnızca dar açının tümleri vardır ($90^\circ$'den büyük açının tümleri olmaz). Soru "tümleri" diyorsa açı dar açıdır. Ayrıca soruda istenen açının kendisi mi, tümleri mi, bütünleri mi, son satırda tekrar oku: üçü de seçeneklerde bulunur.

## 3. Ters açılar

**Örnek.** Kesişen iki doğrunun oluşturduğu iki ters açının ölçüleri $3x + 10^\circ$ ve $5x - 30^\circ$'dir. Oluşan dört açının ölçüleri nedir?

**Çözüm.**

1. Ters açılar eşittir: $3x + 10 = 5x - 30 \Rightarrow 2x = 40 \Rightarrow x = 20$.
2. Açı: $3 \cdot 20 + 10 = 70^\circ$ (kontrol: $5 \cdot 20 - 30 = 70^\circ$).
3. Bu açının iki yanındaki açılar onunla bir doğru üzerinde yan yanadır: $180^\circ - 70^\circ = 110^\circ$.
4. Dört açı: $70^\circ$, $110^\circ$, $70^\circ$, $110^\circ$. Toplam $360^\circ$.

![O noktasında kesişen d1 ve d2 doğruları. Karşılıklı iki mavi açı 70 derece, karşılıklı iki kırmızı açı 110 derece.](gorsel/tyt-matematik/18-01-ters-acilar.svg "Karşılıklı (aynı renkli) açılar ters açıdır ve eşittir. Yan yana duran mavi ile kırmızı açı ise bütünlerdir: 70 + 110 = 180.")

**Kural:** Kesişen iki doğrunun oluşturduğu açılardan komşu olmayanlara **ters açılar** denir.

$$\text{Ters açılar eşittir.} \qquad \text{Yan yana iki açının toplamı } 180^\circ.$$

> **Tuzak:** Ters açılar **eşittir**, toplamları $180^\circ$ değildir. Denklemi kurmadan önce iki açının karşılıklı mı (eşit) yoksa yan yana mı (toplam $180^\circ$) olduğuna bak. Son adımda $x$ yerine açının ölçüsünü yazmayı unutma.

## 4. Açıortay

**Örnek 1.** $m(\widehat{AOB}) = 84^\circ$ ve $[OC$, $\widehat{AOB}$'nin açıortayı ise $m(\widehat{AOC}) = m(\widehat{COB}) = 84^\circ : 2 = 42^\circ$.

**Örnek 2.** $A$, $O$, $B$ bir doğru üzerinde; $[OC$ ışını $m(\widehat{AOC}) = 70^\circ$ olacak biçimde çiziliyor. $[OD$, $\widehat{AOC}$'nin; $[OE$, $\widehat{COB}$'nin açıortayıdır. $m(\widehat{DOE})$ kaç derecedir?

**Çözüm.**

1. $m(\widehat{COB}) = 180^\circ - 70^\circ = 110^\circ$.
2. $m(\widehat{DOC}) = 70^\circ : 2 = 35^\circ$, $m(\widehat{COE}) = 110^\circ : 2 = 55^\circ$.
3. $m(\widehat{DOE}) = 35^\circ + 55^\circ = 90^\circ$.

![B, O, A bir doğru üzerinde. OC ışını AOC açısı 70 derece olacak biçimde çizilmiş. Mavi OD, AOC'yi 35 ve 35 dereceye; kırmızı OE, COB'yi 55 ve 55 dereceye bölüyor. OD ile OE arasında dik açı işareti var.](gorsel/tyt-matematik/18-01-aciortay.svg "Açıortay açıyı iki eş parçaya böler. Komşu bütünler iki açının açıortayları arasındaki açı her zaman 90 derecedir: iki yarının toplamı 180'in yarısıdır.")

**Kural:** Bir açıyı iki eş açıya bölen ışına **açıortay** denir.

- $[OC$ açıortay ise $m(\widehat{AOC}) = m(\widehat{COB}) = \dfrac{m(\widehat{AOB})}{2}$.
- Komşu iki açının açıortayları arasındaki açı, iki açının toplamının yarısıdır: $\dfrac{a + b}{2}$.
- Bu yüzden komşu bütünler açıların açıortayları arası $90^\circ$, komşu tümler açıların açıortayları arası $45^\circ$'dir. $C$'nin yeri değişse de sonuç değişmez.

> **Tuzak:** Açıortay sorularında bilinmeyeni genelde **yarım açı** olarak seçmek kolaylık sağlar: açıyı $2a$ dersen yarısı $a$ olur ve kesir çıkmaz. Sonunda sorulanın yarım açı mı yoksa bütün açı mı olduğunu kontrol et.

## ÖSYM tuzakları

> **Tümleri ile bütünlerini karıştırmak.** "Tümler" $90^\circ$'ye, "bütünler" $180^\circ$'ye tamamlar. Akılda tutma yolu: **bütün** daha büyük, $180^\circ$.

> **Ters açıları toplamı $180^\circ$ sanmak.** Karşılıklı açılar eşittir; yan yana olanlar $180^\circ$ eder. Şekilde hangi açının hangisiyle karşılıklı olduğunu parmağınla takip et.

> **$x$'te durmak.** $3x + 10^\circ$ gibi verilen açılarda soru çoğu zaman $x$'i değil açının ölçüsünü ister. $x$'in değeri seçeneklerde hazır bekler.

> **Doğru açıyı görmemek.** Bir doğru üzerinde bir noktadan çıkan bütün açılar toplanınca $180^\circ$, bir noktanın çevresindeki bütün açılar toplanınca $360^\circ$ olur. Şekilde doğrusal noktaları (örneğin $A$, $O$, $B$) önce bul.

> **Açıortayda ikiye bölmeyi unutmak ya da iki kez bölmek.** Açıortay sorusunda her adımda "bu açı bütün mü, yarım mı?" diye sor.

## Kendini dene

### Soru 1
Bütünlerinin ölçüsü, tümlerinin ölçüsünün $4$ katı olan açı kaç derecedir?

A) 30
B) 45
C) 60
D) 90
E) 120

**Cevap:** C
**Çözüm:** Açı $x$ olsun: $180 - x = 4(90 - x) \Rightarrow 180 - x = 360 - 4x \Rightarrow 3x = 180 \Rightarrow x = 60^\circ$. Kontrol: tümleri $30^\circ$, bütünleri $120^\circ = 4 \cdot 30^\circ$. $30$ tümler, $120$ bütünlerdir; sorulan açının kendisidir.

### Soru 2
İki doğru bir noktada kesişiyor. Oluşan açılardan yan yana duran ikisinin ölçüleri $2x + 30^\circ$ ve $4x$'tir.

Buna göre $4x$ ölçülü açının ters açısı kaç derecedir?

A) 25
B) 50
C) 80
D) 100
E) 130

**Cevap:** D
**Çözüm:** Yan yana iki açı bir doğru üzerindedir, toplamları $180^\circ$: $2x + 30 + 4x = 180 \Rightarrow 6x = 150 \Rightarrow x = 25$. $4x = 100^\circ$; ters açısı da $100^\circ$'dir. $25$, $x$'in kendisi; $80$, öbür açı ($2 \cdot 25 + 30$); $50$ ise $2x$'tir.

### Soru 3
![C, O, A bir doğru üzerinde. OB ışını ve mavi OD ışını var. AOD ve DOB açıları birer çentikle eş gösterilmiş. D'den C'ye uzanan kırmızı yay 130 derece.](gorsel/tyt-matematik/18-01-kd3.svg "Aynı çentikli yaylar eş açılardır.")

Şekilde $A$, $O$, $C$ noktaları doğrusaldır. $[OD$, $\widehat{AOB}$'nin açıortayıdır ve $m(\widehat{DOC}) = 130^\circ$'dir.

Buna göre $m(\widehat{AOB})$ kaç derecedir?

A) 40
B) 50
C) 65
D) 80
E) 100

**Cevap:** E
**Çözüm:** $m(\widehat{AOD}) = a$ olsun. $A$, $O$, $C$ doğrusal olduğu için $m(\widehat{AOD}) + m(\widehat{DOC}) = 180^\circ$: $a = 180^\circ - 130^\circ = 50^\circ$. $m(\widehat{AOB}) = 2a = 100^\circ$. Kontrol: $m(\widehat{BOC}) = 180^\circ - 100^\circ = 80^\circ$ ve $m(\widehat{DOC}) = 50^\circ + 80^\circ = 130^\circ$. $50$ yarım açıda durmak, $80$ ise $m(\widehat{BOC})$'dir.

## Özet kartı

- Açı = köşesi ortak iki ışın; $\widehat{AOB}$'de köşe ortadaki harf ($O$). Tam tur $360^\circ$.
- Dar $< 90^\circ$, dik $= 90^\circ$, $90^\circ <$ geniş $< 180^\circ$, doğru $= 180^\circ$, tam $= 360^\circ$.
- $x$'in tümleri $90^\circ - x$, bütünleri $180^\circ - x$; farkları hep $90^\circ$.
- Bir doğru üzerinde yan yana açılar toplamı $180^\circ$; bir noktanın çevresi $360^\circ$.
- Ters açılar eşittir.
- Açıortay açıyı ikiye böler; komşu bütünler açıların açıortayları arası $90^\circ$.

## Sonraki adım

Alıştırmaya geç (aşağıdaki düğme). Sonraki ders: **Paralel İki Doğrunun Bir Kesenle Yaptığı Açılar**. Orada bugünkü "ters açılar eşittir" ve "yan yana açılar $180^\circ$" bilgileri, paralel doğrularla birleşerek yeni eşit açılar verecek. Gerçek çıkmış sorular için MEBİ'deki "Çıkmış Sorular" testine bak.
