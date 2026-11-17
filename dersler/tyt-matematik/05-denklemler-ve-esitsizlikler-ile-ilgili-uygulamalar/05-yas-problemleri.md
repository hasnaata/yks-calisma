---
baslik: Yaş Problemleri
ders: tyt-matematik
sure: 20 dk
kaynak: MEBİ Konu Özeti d5211d5a59
guncelleme: 2026-11-18
---
# Yaş Problemleri

<div class="giris" dir="rtl" lang="ar">

**الدرس ده عن إيه؟** عن مسائل الأعمار (yaş problemleri): إزاي تحوّل كلام المسألة عن "زمان" و"دلوقتي" و"بعدين" لمعادلة (denklem) بسيطة وتحلها.

- هتتعلم تعمل جدول "قبل، دلوقتي، بعد" وتزوّد نفس عدد السنين على كل الناس.
- هتعرف إن فرق السن (yaş farkı) عمره ما بيتغير، وإن مجموع الأعمار بيزيد كل سنة بعدد الأشخاص.
- هتفهم أسئلة "لما كنت في سنك" و"لو كان اتولد بدري أو متأخر كام سنة"، وإزاي تاخد بالك من حد لسه ما اتولدش.

**ليه مهم؟** النوع ده بييجي كتير في جزء المسائل في TYT، والحساب فيه سهل؛ الدرجة بتروح للي ياخد باله من الفخ.

الدرس ٢٠ دقيقة بس، ومعاك أمثلة محلولة خطوة بخطوة، يلا بينا.

</div>

**Bu dersin sonunda:** yaş sorusunu "önce–şimdi–sonra" tablosuna döküp denkleme çevirebilecek, yaş farkının sabit kaldığını ve toplam yaşın kişi sayısı kadar arttığını kullanarak çoğu soruyu iki adımda çözebileceksin.

> **TYT'de yeri:** Problemler bölümünde sık gelen bir kalıptır: "şimdi 4 katı, 5 yıl sonra 3 katı", "ben senin yaşındayken…", "ailenin yaşları toplamı 6 yıl önce…". Hesap küçüktür; puanı, herkesin aynı yıl yaşlandığını ve henüz doğmamış kişiyi gözden kaçırmayan alır.

## Önce hatırla

<details><summary>Kesir problemlerinden: Bir öğrenci parasının 1/4'ünü harcıyor, kalanın 1/3'ünü de harcayınca geriye 120 TL kalıyor. Başlangıçtaki parası kaç TL'dir?</summary>
Kalan oranlar çarpılır: $\frac{3}{4} \cdot \frac{2}{3} = \frac{1}{2}$. Paranın yarısı $120$ TL ise para <b>240 TL</b>. Kesirleri bütünden çıkarıp $1 - \frac{1}{4} - \frac{1}{3} = \frac{5}{12}$ yazmak yanlıştır.
</details>

<details><summary>Kesir problemlerinden: Bir sayının 1/3'ü ile 1/4'ünün toplamı 42'dir. Sayı kaçtır?</summary>
Paydaların EKOK'u 12; sayıya $12x$ de: $4x + 3x = 7x = 42$, $x = 6$. Sayı $12x = $ <b>72</b>. Bugün de bilinmeyeni akıllıca seçip sonunda istenen çokluğu yazacaksın.
</details>

## 1. Önce–şimdi–sonra tablosu

**Örnek.** Bir annenin yaşı kızının yaşının 4 katıdır. 5 yıl sonra annenin yaşı kızının yaşının 3 katı olacaktır. Anne şimdi kaç yaşındadır?

Şimdiki yaşlara harf ver, sonra zamanı satır olarak ekle. 5 yıl sonra **herkes** 5 yaş büyür:

| | Kız | Anne |
|---|---|---|
| şimdi | $k$ | $4k$ |
| 5 yıl sonra | $k + 5$ | $4k + 5$ |

Cümle ikinci satırda geçiyor: $4k + 5 = 3(k + 5)$. Buradan $4k + 5 = 3k + 15$, $k = 10$. Anne $4k = 40$ yaşında.

Kontrol: 5 yıl sonra anne 45, kız 15; $45 = 3 \cdot 15$.

**Kural.** $a$ yıl önce herkesin yaşı $a$ azalır, $b$ yıl sonra herkesin yaşı $b$ artar. Bilinmeyeni **şimdiki** yaşa ver, cümleyi hangi zamandan söz ediyorsa o satırdan kur. Kat ifadesinde parantezi unutma: "3 katı" $3(k + 5)$ demektir, $3k + 5$ değil.

![Akış şeması: şimdiki yaşlara harf ver, herkese aynı yılı ekle, cümleyi denkleme çevir; doğmamış kişi varsa onu ayrı hesapla; sonunda istenen çokluğu yaz.](gorsel/tyt-matematik/05-05-yontem.svg "Her yaş sorusunda bu sırayı izle. Sarı karardaki soruyu atlamak, toplam yaş sorularında en sık yapılan hatadır.")

## 2. Yaş farkı hiç değişmez

**Örnek.** Bir babanın yaşı oğlunun yaşının 5 katıdır ve aralarında 28 yaş fark vardır. Kaç yıl sonra babanın yaşı oğlunun yaşının 3 katı olur?

Oğul $k$ ise baba $5k$; fark $5k - k = 4k = 28$, yani oğul 7, baba 35.

Fark hep 28 kalır. Baba oğlunun 3 katı olduğunda fark, oğlun yaşının 2 katıdır: $2 \cdot (\text{oğul}) = 28$, oğul 14. Oğul 7'den 14'e **7 yıl sonra** gelir. Kontrol: $42 = 3 \cdot 14$.

![Yaş–zaman grafiği: baba ve oğul için iki paralel doğru. 0, 7 ve 21 yıl sonra iki doğru arasındaki dikey uzaklık hep 28. Baba 35 iken oğul 7 (5 kat), 42 iken 14 (3 kat), 56 iken 28 (2 kat).](gorsel/tyt-matematik/05-05-yas-farki.svg "İki doğru paraleldir: kırmızı fark her zaman 28. Değişen yalnızca oran; zaman geçtikçe kat sayısı küçülür.")

**Kural.** İki kişi arasındaki yaş farkı her zaman aynıdır. Büyük, küçüğün $n$ katı ise fark küçüğün $(n - 1)$ katıdır:

$$\text{fark} = (n - 1) \cdot \text{küçüğün yaşı}$$

Bu yüzden zaman ilerledikçe oran küçülür, geriye gidildikçe büyür.

## 3. Toplam yaş: her yıl kişi sayısı kadar

**Örnek.** Bir anne 38 yaşında, üç çocuğunun yaşları 4, 7 ve 11'dir. Kaç yıl sonra çocukların yaşları toplamı annenin yaşına eşit olur?

Çocukların toplamı şimdi $22$. $t$ yıl sonra anne $38 + t$, üç çocuğun toplamı $22 + 3t$ olur (her çocuk $t$ yaş büyür):

$$22 + 3t = 38 + t \quad\Rightarrow\quad 2t = 16 \quad\Rightarrow\quad t = 8$$

Kontrol: 8 yıl sonra anne 46; çocuklar $12 + 15 + 19 = 46$.

**Kural.** $n$ kişinin yaşları toplamı $b$ yıl sonra $n \cdot b$ artar, $a$ yıl önce $n \cdot a$ azalır. İki grubun toplamı karşılaştırılıyorsa aradaki fark her yıl kişi sayılarının farkı kadar kapanır.

**Örnek (tuzak).** Anne, baba ve iki çocuktan oluşan bir ailenin yaşları toplamı 80'dir. Büyük çocuk 8 yaşındadır. 5 yıl önce ailenin yaşları toplamı 62 idi. Küçük çocuk kaç yaşındadır?

4 kişi 5 yıl önce de var olsaydı toplam $80 - 4 \cdot 5 = 60$ olurdu. Oysa 62; demek ki biri 5 yıl önce henüz doğmamıştı. Bu kişi küçük çocuktur (anne, baba ve 8 yaşındaki çocuk 5 yıl önce vardı). Küçük çocuğun yaşı $c$ ise toplamdan yalnızca $c$ düşer:

$$80 - 3 \cdot 5 - c = 62 \quad\Rightarrow\quad c = 3$$

**Kural.** Toplam yaş beklenenden az değişmişse o tarihte doğmamış biri vardır. O kişi için "geçmişteki yaşı" yazılmaz; toplamdan yalnızca şimdiki yaşı kadar düşülür.

## 4. "Ben senin yaşındayken…"

**Örnek.** Biri kardeşine şöyle diyor: "Ben senin yaşındayken sen 6 yaşındaydın. Sen benim yaşıma geldiğinde ben 33 yaşında olacağım." İkisi şimdi kaç yaşındadır?

Yaş farkına $d$ de. "Ben senin yaşındayken" demek, $d$ yıl önce demektir; "sen benim yaşıma geldiğinde" demek $d$ yıl sonra demektir. Dört sayı eşit adımlarla dizilir:

$$6,\quad 6 + d,\quad 6 + 2d,\quad 6 + 3d = 33 \quad\Rightarrow\quad d = 9$$

Kardeş şimdi $15$, konuşan $24$ yaşındadır.

![Sayı doğrusunda eşit aralıklı dört nokta: 6 (sen o zaman), 15 (sen şimdi, ben o zaman), 24 (ben şimdi, sen sonra), 33 (ben sonra). Aralarında üç tane artı 9 oku var.](gorsel/tyt-matematik/05-05-esit-adim.svg "Uçtaki iki sayı arasında üç eşit adım var: 33 − 6 = 27, bir adım 9. Ortadaki iki nokta şimdiki yaşlardır.")

**Kural.** Şimdiki yaşlar $x > y$ ise:

| | Büyük | Küçük |
|---|---|---|
| büyük, küçüğün yaşındayken | $y$ | $2y - x$ |
| şimdi | $x$ | $y$ |
| küçük, büyüğün yaşına geldiğinde | $2x - y$ | $x$ |

Ezberleme; aradaki sürenin yaş farkı kadar olduğunu bil, yeter.

## 5. "… yıl önce doğsaydı"

**Örnek.** Ece 4 yıl önce doğmuş olsaydı şimdi 21 yaşında olurdu. Ece 3 yıl sonra doğmuş olsaydı şimdi kaç yaşında olurdu?

Daha önce doğmak yaşı büyütür: gerçek yaş $21 - 4 = 17$. Daha sonra doğmak yaşı küçültür: $17 - 3 = 14$.

**Kural.** Şimdiki yaşı $x$ olan kişi $a$ yıl önce doğsaydı şimdi $x + a$, $b$ yıl sonra doğsaydı şimdi $x - b$ yaşında olurdu. Bu bir varsayımdır, zaman geçmez: yalnızca o kişinin yaşı değişir, öbür kişilerin yaşı aynı kalır. Önce gerçek yaşı bul, sonra soruya devam et.

## ÖSYM tuzakları

> **Kat ifadesinde parantezi unutmak:** "5 yıl sonra kızının 3 katı" ifadesini $4k + 5 = 3k + 5$ yazan $k = 0$ bulur. Doğrusu $4k + 5 = 3(k + 5)$; zaman herkese eklenir, katsayı sonra uygulanır.

> **Toplam yaşa zamanı bir kez eklemek:** 3 kardeşin yaşları toplamı 4 yıl sonra $4$ değil $3 \cdot 4 = 12$ artar. Her kişi ayrı ayrı yaşlanır.

> **Doğmamış kişiyi unutmak:** "5 yıl önce toplam" sorusunda herkesten 5 çıkaran, toplamın tutmadığını görünce hesap hatası yaptığını sanar. Tutmuyorsa biri o tarihte henüz doğmamıştır.

> **$x$'i cevap sanmak:** Annenin yaşını soran soruda $k = 10$ bulup "10" işaretlemek. Seçeneklerde kızın yaşı, 5 yıl sonraki yaşlar ve yaş farkı da bulunur; istenen kişiyi ve zamanı yeniden oku.

## Kendini dene

### Soru 1
İki kardeşin yaşları toplamı 30, yaşları farkı 6'dır.

Buna göre büyük kardeş 5 yıl sonra kaç yaşında olur?

A) 13
B) 17
C) 18
D) 20
E) 23

**Cevap:** E
**Çözüm:** Büyük kardeş $\frac{30 + 6}{2} = 18$, küçük $12$ yaşındadır. 5 yıl sonra büyük kardeş $18 + 5 = 23$ yaşında olur. 18 bugünkü yaştır, 17 küçük kardeşin 5 yıl sonraki yaşıdır, 13 büyüğün 5 yıl önceki yaşıdır. 20 ise 5 yıl sonraki toplamı ($30 + 2 \cdot 5 = 40$) farkı unutup ikiye bölmekten gelir.

### Soru 2
Selin doğduğunda ağabeyi 6 yaşındaydı. Selin, ağabeyinin bugünkü yaşına geldiğinde iki kardeşin yaşları toplamı 40 olacaktır.

Buna göre ağabey bugün kaç yaşındadır?

A) 11
B) 17
C) 20
D) 23
E) 34

**Cevap:** B
**Çözüm:** Yaş farkı 6'dır ve hiç değişmez. Ağabeyin bugünkü yaşı $a$ olsun. Selin $a$ yaşına geldiğinde ağabey $a + 6$ olur: $a + (a + 6) = 40$, $a = 17$. 23 o günkü ağabey yaşıdır, 11 Selin'in bugünkü yaşıdır, 20 ise toplamı ikiye bölüp farkı unutmaktan gelir.

### Soru 3
Bir genç kız kardeşine şöyle diyor: "Ben senin yaşındayken sen 4 yaşındaydın. Sen benim yaşıma geldiğinde ben 37 yaşında olacağım."

Buna göre iki kardeşin bugünkü yaşları toplamı kaçtır?

A) 15
B) 26
C) 37
D) 41
E) 52

**Cevap:** D
**Çözüm:** Fark $d$ ise $4$, $4 + d$, $4 + 2d$, $4 + 3d = 37$ eşit adımlıdır: $33 = 3d$, $d = 11$. Kardeş $4 + 11 = 15$, konuşan $15 + 11 = 26$ yaşında; toplam $41$. 15 ve 26 tek tek yaşlardır; 37 konuşanın ileride olacağı yaştır.

## Özet kartı

- Bilinmeyeni şimdiki yaşa ver; önce–şimdi–sonra tablosu kur, herkese aynı yılı ekle ya da çıkar.
- "3 katı olacak" ifadesinde parantez: $3(k + t)$.
- Yaş farkı sabittir; büyük küçüğün $n$ katıysa fark küçüğün $(n - 1)$ katıdır.
- $n$ kişinin toplam yaşı $t$ yılda $n \cdot t$ değişir; tutmuyorsa o tarihte doğmamış biri vardır.
- "Ben senin yaşındayken / sen benim yaşıma geldiğinde": dört yaş, adımı yaş farkı olan eşit aralıklı dizidir.
- $a$ yıl önce doğsaydı $x + a$, $b$ yıl sonra doğsaydı $x - b$.

## Sonraki adım

Alıştırmaya geç (aşağıdaki düğme). Sonraki ders **İşçi Problemleri**: orada da "herkese aynı süre eklenir" düşüncesi işe yarar; bu kez yaş yerine birim zamanda yapılan iş toplanır.
