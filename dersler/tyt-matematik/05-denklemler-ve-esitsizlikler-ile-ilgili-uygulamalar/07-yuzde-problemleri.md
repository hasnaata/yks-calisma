---
baslik: Yüzde Problemleri
ders: tyt-matematik
sure: 20 dk
kaynak: MEBİ Konu Özeti 94e996a2a3
guncelleme: 2026-11-18
---
# Yüzde Problemleri

<div class="giris" dir="rtl" lang="ar">

**الدرس ده عن إيه؟** عن مسائل النسبة المئوية (yüzde problemleri): إزاي تحسب نسبة من رقم، وإزاي تعرف الرقم كله لو عارف نسبة منه.

- هتعرف تحسب التغيّر بالنسبة المئوية (yüzde değişim)، وليه دايمًا بنقسم على القيمة القديمة.
- هتفهم ليه زيادة 20 في المية وبعدها تخفيض 20 في المية ما بيرجّعوش السعر زي ما كان.
- هتتعلم حيلة إنك تفرض المبلغ الأصلي 100x، وتحسب "نسبة من الباقي" (kalanın yüzdesi) صح.

**ليه مهم؟** تقريبًا في كل TYT فيه سؤال واحد على الأقل على النسبة المئوية، وهي الأساس لمسائل المكسب والخسارة (kâr-zarar) والخلطات.

الدرس 20 دقيقة بس، وهتلاقي الحسبة بقت أسهل بكتير مما كنت فاكر.

</div>

**Bu dersin sonunda:** bir sayının yüzdesini, yüzdesi verilen sayının tamamını ve yüzde değişimi bulabilecek; art arda yapılan artış ve azalışları çarpanla tek adımda hesaplayabileceksin.

> **TYT'de yeri:** Neredeyse her TYT'de en az bir yüzde sorusu vardır; kâr-zarar ve karışım sorularının da temelidir. Tipik kalıplar: "önce %20 zam, sonra %20 indirim yapılırsa…", "zamlı fiyatı 540 TL ise zamdan önce…", "kalanın %25'i…", "A, B'den %25 fazlaysa B, A'dan yüzde kaç az?". Bazen veriler bir daire grafiğinde ya da tabloda gelir.

## Önce hatırla

<details><summary>İşçi problemlerinden: A bir işi 12 günde, B aynı işi 4 günde bitiriyor. İkisi birlikte bu işi kaç günde bitirir?</summary>
İşe $\text{EKOK}(12, 4) = 12$ birim de. A günde 1, B günde 3 birim yapar; birlikte günde 4 birim. $12 \div 4 = 3$ gün. Bu derste de aynı hileyi kullanacaksın: bütüne kolay bir sayı (100) vereceksin.
</details>

<details><summary>İşçi problemlerinden: Bir işçi bir işi 20 günde bitiriyor. 5 günde işin yüzde kaçını yapar?</summary>
Günde $\frac{1}{20}$, 5 günde $\frac{5}{20} = \frac{1}{4}$'ünü yapar. $\frac{1}{4} = \frac{25}{100}$, yani işin <b>%25</b>'i. Yüzde, paydası 100 yapılmış bir kesirdir.
</details>

## Bir sayının yüzdesi

**Örnek.** Bir okulda 360 öğrenci var ve öğrencilerin %35'i okula servisle geliyor. Servisle gelen kaç öğrenci vardır?

%35, "100'de 35" demektir: $\%35 = \frac{35}{100}$.

$$360 \cdot \frac{35}{100} = \frac{12600}{100} = 126$$

*Zihinden:* %10'u $36$, %5'i bunun yarısı $18$. %35 = %10 + %10 + %10 + %5: $36 + 36 + 36 + 18 = 126$.

![Yüz küçük kareden oluşan 10'a 10'luk bir tablo. İlk 35 kare mavi boyalı. Altta: 360 öğrenci için bir kare 3,6 öğrenci, 35 kare 126 öğrenci.](gorsel/tyt-matematik/05-07-yuzlu-kare.svg "Bütünü 100 eşit parçaya böl; %35 bu parçaların 35 tanesidir.")

**Kural.** $A$ sayısının $\%x$'i:

$$A \cdot \frac{x}{100}$$

## Yüzdenin yüzdesi

**Örnek.** 600 kişiyle yapılan bir ankette katılımcıların %40'ı düzenli spor yaptığını, spor yapanların da %25'i yüzdüğünü söylüyor. Yüzen kaç kişi vardır? Bunlar katılımcıların yüzde kaçıdır?

Spor yapan: $600 \cdot \frac{40}{100} = 240$. Bunların %25'i: $240 \cdot \frac{25}{100} = 60$ kişi.

Tek adımda: $600 \cdot \frac{40}{100} \cdot \frac{25}{100} = 60$. Ayrıca $\frac{40}{100} \cdot \frac{25}{100} = \frac{10}{100}$, yani yüzenler bütünün **%10**'u.

**Kural.** $A$ sayısının $\%x$'inin $\%y$'si:

$$A \cdot \frac{x}{100} \cdot \frac{y}{100}$$

Yüzdenin yüzdesi **çarpılır**; toplanmaz, çıkarılmaz.

## Yüzdesi verilen sayıyı bulmak

**Örnek.** Bir sınıftaki öğrencilerin %30'u gözlük takıyor. Gözlüklü 12 öğrenci olduğuna göre sınıf kaç kişidir?

Sınıf $X$ kişi olsun: $X \cdot \frac{30}{100} = 12$, buradan $X = \frac{12 \cdot 100}{30} = 40$.

*Şeritle:* %30 = 12 ise %10 = 4, %100 = 40.

![On eşit parçalı şerit, her parça yüzde 10. İlk üç parça sarı ve toplamı yüzde 30 eşittir 12 kişi; her parçada 4 yazıyor. Altta: yüzde 100 eşittir 10 kere 4 eşittir 40 kişi.](gorsel/tyt-matematik/05-07-yuzde-seridi.svg "Önce %10'u bul (12 ÷ 3 = 4), sonra 10 ile çarp.")

**Kural.** $\%a$'sı $Y$ olan sayı $X$ ise

$$X \cdot \frac{a}{100} = Y \quad\Rightarrow\quad X = \frac{100 \cdot Y}{a}$$

## Bir sayı diğerinin yüzde kaçı? Yüzde değişim

**Örnek.** 45 soruluk bir denemede 36 soruyu doğru yapan öğrenci, soruların yüzde kaçını doğru yapmıştır?

$$\frac{36}{45} \cdot 100 = \frac{4}{5} \cdot 100 = 80 \quad\Rightarrow\quad \%80$$

**Örnek.** Bir ürünün fiyatı 250 TL'den 300 TL'ye çıkıyor. Fiyat yüzde kaç artmıştır? Sonra 300 TL'den yeniden 250 TL'ye inerse yüzde kaç azalmış olur?

Artış 50 TL. Değişim **eski** değere bölünür:

- Artış: $\frac{50}{250} \cdot 100 = \%20$.
- Azalış: $\frac{50}{300} \cdot 100 = \%16{,}6\ldots$ (yaklaşık %16,7).

Aynı 50 TL, farklı bütüne göre farklı yüzdedir.

**Kural.** $A$, $B$'nin $\frac{A}{B} \cdot 100$ yüzdesidir. Yüzde değişim:

$$\frac{\text{yeni} - \text{eski}}{\text{eski}} \cdot 100$$

## Artırma, azaltma ve art arda değişim

**Örnek.** 100 TL'lik bir ürüne önce %20 zam, sonra yeni fiyat üzerinden %20 indirim yapılıyor. Son fiyat kaç TL'dir?

- Zam: $100$'ün %20'si $20$, fiyat $120$ TL.
- İndirim: $120$'nin %20'si $24$, fiyat $96$ TL.

Fiyat başa dönmez; **%4 azalır**. Çünkü indirim daha büyük bir bütün (120) üzerinden yapıldı.

![Üç sütun. Başta 100. Yüzde 20 artış sonrası 120; üstte yeşil +20. Yüzde 20 azalış sonrası 96; üstte kırmızı −24. Kesikli çizgi 100 düzeyini gösteriyor.](gorsel/tyt-matematik/05-07-ardisik.svg "Artış 100 üzerinden (+20), azalış 120 üzerinden (−24) yapılır; son değer 100'ün altına iner.")

*Çarpanla:* %20 artış $\cdot 1{,}2$, %20 azalış $\cdot 0{,}8$ demektir:

$$100 \cdot 1{,}2 \cdot 0{,}8 = 100 \cdot 0{,}96 = 96$$

**Örnek (geriye gitmek).** %20 zamdan sonra fiyatı 540 TL olan ürünün zamdan önceki fiyatı kaç TL'dir?

Eski fiyat $P$ ise $P \cdot 1{,}2 = 540$, buradan $P = \frac{540}{1{,}2} = 450$ TL. Kontrol: $450$'nin %20'si $90$, $450 + 90 = 540$.

**Kural.**

- $\%x$ artış: $\cdot \left(1 + \frac{x}{100}\right)$; $\%x$ azalış: $\cdot \left(1 - \frac{x}{100}\right)$.
- Art arda değişimlerde çarpanlar **çarpılır**: $\%20$ artış ve $\%20$ azalış $\cdot 0{,}96$ eder.
- Değişmiş değerden eskiye dönmek için çarpana **bölünür**.

## Bilinmeyeni 100x seç

**Örnek.** Bir öğrenci cebindeki paranın %30'u ile kitap alıyor, kalan paranın %20'si ile yemek yiyor. Cebinde 112 TL kaldığına göre başlangıçta kaç TL'si vardı?

Para $100x$ olsun; yüzdeler kesirsiz çıkar:

- Kitap: $100x$'in %30'u $30x$; kalan $70x$.
- Yemek: **kalanın** %20'si, $70x \cdot \frac{20}{100} = 14x$; kalan $70x - 14x = 56x$.
- $56x = 112 \Rightarrow x = 2$; para $100x = 200$ TL.

![Üç şerit. Başta 100x. Kitaptan sonra 30x kırmızı, 70x mavi. Yemekten sonra 14x kırmızı, 56x yeşil. Altta: 56x eşittir 112, x eşittir 2, para 200 TL.](gorsel/tyt-matematik/05-07-yuz-x.svg "Kalanın yüzdesi, bütünün değil kalan parçanın (70x) yüzdesidir.")

**Kural.** Başlangıç değerini $100x$ seç. Her yüzde tam sayı katsayı verir; denklem sonda tek adımda çözülür. "Kalanın %…'i" gördüğünde yüzdeyi **kalan** üzerinden al.

## ÖSYM tuzakları

> **Art arda yüzdeleri toplamak:** %20 zam ve %20 indirimden sonra "fiyat değişmez" demek. Çarpanlar çarpılır: $1{,}2 \cdot 0{,}8 = 0{,}96$, fiyat %4 azalır.

> **Zamlı fiyattan aynı yüzdeyi düşmek:** %20 zamlı 540 TL'den $540 \cdot 0{,}8 = 432$ bulmak. Zam 450 üzerinden yapılmıştı; doğrusu $540 \div 1{,}2 = 450$.

> **Değişimi yeni değere bölmek:** 250'den 300'e çıkış için $\frac{50}{300}$ yazmak. Yüzde değişim her zaman **eski** değere göre hesaplanır.

> **"Kalanın" yüzdesini bütünden almak:** %30'u harcayıp kalanın %20'sini harcayan kişi parasının %50'sini değil, %30 + %14 = %44'ünü harcamış olur.

> **"%25 fazla" ile "%25 az"ı simetrik sanmak:** B, A'dan %25 fazlaysa $B = 1{,}25A$, yani $A = 0{,}8B$: A, B'den **%20** azdır.

## Kendini dene

### Soru 1
240 sayısının %15'i kaçtır?

A) 16
B) 24
C) 36
D) 160
E) 204

**Cevap:** C
**Çözüm:** $240 \cdot \frac{15}{100} = 36$. Zihinden: %10'u 24, %5'i 12, toplam 36. 24 yalnızca %10'dur; 204, 240'tan 36 çıkarılınca kalan miktardır; 16 ise $240 \div 15$ işleminin sonucudur.

### Soru 2
Fiyatı 400 TL olan bir ürüne önce %30 zam yapılıyor, sonra ürünün yeni fiyatı üzerinden %30 indirim yapılıyor.

Buna göre ürünün son fiyatı kaç TL'dir?

A) 280
B) 364
C) 388
D) 400
E) 520

**Cevap:** B
**Çözüm:** $400 \cdot 1{,}3 \cdot 0{,}7 = 400 \cdot 0{,}91 = 364$ TL. Zam ve indirimi birbirini götürür sanan 400'ü, yalnızca zammı uygulayan 520'yi, yalnızca indirimi uygulayan 280'i bulur.

### Soru 3
Bir sınıftaki öğrencilerin %45'i kızdır. Bu sınıfta erkek öğrenci sayısı kız öğrenci sayısından 6 fazladır.

Buna göre sınıf kaç kişidir?

A) 27
B) 33
C) 40
D) 60
E) 120

**Cevap:** D
**Çözüm:** Erkekler %55, kızlar %45; aradaki fark sınıfın %10'udur. %10 = 6 ise %100 = 60. Kontrol: 27 kız, 33 erkek, fark 6. 27 ve 33 sınıfın tamamı değil, kız ve erkek sayılarıdır; 120, farkı %5 sanınca bulunur.

## Özet kartı

- $A$'nın $\%x$'i $A \cdot \frac{x}{100}$; $\%x$'inin $\%y$'si $A \cdot \frac{x}{100} \cdot \frac{y}{100}$.
- $\%a$'sı $Y$ olan sayı $\frac{100 \cdot Y}{a}$; zihinden önce %10'u bul.
- $A$, $B$'nin $\frac{A}{B} \cdot 100$ yüzdesidir; yüzde değişim **eski** değere bölünür.
- $\%x$ artış $\cdot (1 + \frac{x}{100})$, azalış $\cdot (1 - \frac{x}{100})$; art arda değişimde çarpanlar çarpılır.
- Değişmiş değerden eskiye dönmek için çarpana böl.
- Başlangıç değerini $100x$ seç; "kalanın yüzdesi" kalan üzerinden alınır.

## Sonraki adım

Alıştırmaya geç (aşağıdaki düğme). Sonraki ders **Kâr-Zarar Problemleri**; orada maliyete göre kâr yüzdesi ve indirimli satış, bu dersteki artış ve azalış çarpanlarıyla çözülecek.
