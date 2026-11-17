---
baslik: Ardışık Sayılar
ders: tyt-matematik
sure: 20 dk
kaynak: MEBİ Konu Özeti 6b6a0b7f99
guncelleme: 2026-11-18
---
# Ardışık Sayılar

<div class="giris" dir="rtl" lang="ar">

**الدرس ده عن إيه؟** عن الأعداد المتتالية (ardışık sayılar): أعداد جاية ورا بعض والفرق بين كل عدد واللي بعده ثابت، وده اسمه الفرق الثابت (ortak fark)، زي الأعداد الزوجية أو الفردية المتتالية.

- هتعرف تحسب عدد الحدود (terim sayısı) من أول حد لآخر حد، من غير ما تنسى تزوّد واحد في الآخر.
- هتتعلم تجمع الحدود بسرعة لما تكتبها مرة من الأول ومرة من الآخر، وهتحفظ تلات مجاميع جاهزة.
- هتعرف تطلّع الأعداد نفسها لو معاك مجموعها بس، عن طريق الحد الأوسط (ortanca terim).

**ليه مهم؟** في TYT بييجي سؤال زي "مجموع خمس أعداد فردية متتالية كذا، أصغرهم كام؟"، أو مسألة من الحياة فيها كراسي أو صفحات بتزيد بانتظام، ولو جبت عدد الحدود صح تبقى خلّصت نص الحل.

الدرس ٢٠ دقيقة بس وكل قاعدة فيه قبلها مثال محلول خطوة بخطوة، هات ورقة وقلم ويلّا بينا.

</div>

**Bu dersin sonunda:** düzenli artan bir sayı dizisinin kaç terimden oluştuğunu ve terimlerinin toplamını hızlıca bulabilecek, "ardışık üç çift sayının toplamı 78" gibi bir bilgiden sayıların kendisini çıkarabileceksin.

> **TYT'de yeri:** İki kalıp sık gelir: "ardışık $k$ sayının toplamı verilmiş, en büyüğü kaçtır?" ve "$7 + 11 + 15 + \dots + 83$ toplamı kaçtır?". Yeni nesil sorularda dizi bir günlük duruma gizlenir: her sırada 2 fazla koltuk, her gün 3 fazla sayfa, katları büyüyen bir kule. Terim sayısını doğru bulmak işin yarısıdır.

## Önce hatırla

<details><summary>Pozitif ve negatif sayılardan: $(-5) \cdot (-4) \cdot (-3) \cdot (-2) \cdot (-1)$ çarpımı kaçtır?</summary>
Negatif çarpanları say: 5 tane, yani tek sayıda. Sonuç negatiftir: $5 \cdot 4 \cdot 3 \cdot 2 \cdot 1 = 120$ olduğu için cevap <b>−120</b>. Bu derste ardışık tam sayıları negatif taraftan başlatınca aynı işaret kurallarını kullanacaksın.
</details>

<details><summary>Pozitif ve negatif sayılardan: $a < 0 < b$ ve $|a| < |b|$ ise $a + b$ pozitif midir, negatif midir?</summary>
Ters işaretli iki sayının toplamı, mutlak değerce büyük olanın işaretini alır. $|b|$ büyük ve $b$ pozitif, toplam <b>pozitif</b>. Bu derste $-5$ ile $8$ arasındaki tam sayıları toplarken negatiflerin pozitiflerle nasıl götürüldüğünü göreceksin.
</details>

## Ardışık sayı ve ortak fark

**Örnek.** Ardışık üç çift sayının toplamı 78'dir. En büyüğü kaçtır?

Ardışık çift sayılar 2'şer artar. Ortadakine $x$ dersen sayılar $x - 2$, $x$, $x + 2$ olur. Toplam $3x = 78$, yani $x = 26$. Sayılar $24, 26, 28$; en büyüğü **28**.

Ortadakini $x$ seçmek işi kısaltır: $-2$ ile $+2$ birbirini götürür.

Belli bir kurala göre art arda gelen ve **ardışık iki terimi arasındaki farkı hep aynı** olan sayılara **ardışık sayılar**, bu sabit farka **ortak fark** denir.

![Üç sayı doğrusu alt alta. Birincide eksi 2'den 4'e kadar tam sayılar artı 1'lik oklarla, ikincide eksi 2'den 6'ya çift sayılar artı 2'lik oklarla, üçüncüde eksi 3'ten 5'e tek sayılar artı 2'lik oklarla bağlanmış.](gorsel/tyt-matematik/01-05-ortak-fark.svg "Ardışık tam sayılarda adım 1, ardışık çift ve ardışık tek sayılarda adım 2'dir. Tek sayılar da 2'şer artar.")

| Dizi | Ortak fark | Genel yazım ($n \in \mathbb{Z}$) | Örnek |
|---|---|---|---|
| Ardışık tam sayılar | 1 | $n,\ n + 1,\ n + 2,\ \dots$ | $-2, -1, 0, 1$ |
| Ardışık çift sayılar | 2 | $2n,\ 2n + 2,\ 2n + 4,\ \dots$ | $14, 16, 18$ |
| Ardışık tek sayılar | 2 | $2n + 1,\ 2n + 3,\ 2n + 5,\ \dots$ | $-7, -5, -3$ |
| 5'in ardışık katları | 5 | $5n,\ 5n + 5,\ 5n + 10,\ \dots$ | $10, 15, 20$ |

**Kural.** Ardışık çift ya da ardışık tek sayılar $x,\ x + 2,\ x + 4$ diye yazılır. Tek sayıda terim varsa ortadakine $x$ de; toplam, terim sayısı çarpı ortanca terimdir.

## Terim sayısı

**Örnek.** $7, 11, 15, \dots, 83$ dizisinde kaç terim vardır?

Ortak fark $4$. İlk terimden son terime $83 - 7 = 76$ birim yol var; bu yol $76 : 4 = 19$ adımda gidilir. 19 adım atan biri ilk sayıyı da sayarsa **20** terime basar.

![Beş çit direği: üstlerinde 7, 11, 15, 19, 23 yazıyor, aralarındaki her boşlukta artı 4. Altta 5 direk, 4 boşluk yazıyor.](gorsel/tyt-matematik/01-05-cit-direkleri.svg "Boşluklar ortak farktır, direkler terimdir. Direk sayısı her zaman boşluk sayısından 1 fazladır.")

$$\text{Terim sayısı} = \frac{\text{Son terim} - \text{İlk terim}}{\text{Ortak fark}} + 1$$

**Örnek.** 3'ün katı olan iki basamaklı kaç doğal sayı vardır?

İlk terim $10$ değil, 3'ün katı olan ilk iki basamaklı sayı $12$; son terim $99$. Terim sayısı $\frac{99 - 12}{3} + 1 = 29 + 1 = 30$.

**Kural.** Önce ilk ve son terimi dizinin kuralına uyacak biçimde bul, sonra formülü uygula. Sondaki $+1$'i unutma.

## Terimlerin toplamı

**Örnek.** $7 + 11 + 15 + 19 + 23$ toplamını kısa yoldan bul.

Toplama $S$ de. Aynı toplamı bir de tersten yaz ve alt alta topla: her sütunda $7 + 23 = 30$ çıkar. 5 sütun var, yani $2S = 5 \cdot 30$ ve $S = 75$.

![İki satır kutu: üstte 7, 11, 15, 19, 23; altta aynı sayılar tersten. Her sütunun altında 30 yazıyor ve yanda 2S eşittir 5 çarpı 30.](gorsel/tyt-matematik/01-05-gauss-esleme.svg "Dizi tersten yazılınca alt alta gelen her çift aynı toplamı verir: ilk terim artı son terim.")

$$\text{Toplam} = \frac{\text{İlk terim} + \text{Son terim}}{2} \cdot \text{Terim sayısı}$$

Baştaki dizi için: $7 + 11 + \dots + 83 = \frac{7 + 83}{2} \cdot 20 = 45 \cdot 20 = 900$.

**Negatif terimler.** $-5 + (-4) + \dots + 7 + 8$ toplamında $-5$ ile $5$, $-4$ ile $4$… birbirini götürür; geriye $6 + 7 + 8 = 21$ kalır. Formül de aynı sonucu verir: 14 terim, $\frac{-5 + 8}{2} \cdot 14 = 21$.

**Kural.** Toplamı bulmak için iki şey gerekir: terim sayısı ve ilk ile son terimin ortalaması. Önce terim sayısını bul.

## Akılda tutulacak üç toplam

**Örnek.** $1 + 3 + 5 + \dots + 29$ toplamı kaçtır?

Bu dizide terim sayısı $\frac{29 - 1}{2} + 1 = 15$. Toplam $\frac{1 + 29}{2} \cdot 15 = 225 = 15^2$. Bu bir rastlantı değil: 1'den başlayan ardışık tek sayıların toplamı her zaman **terim sayısının karesidir**.

![4'e 4 kare: sol üstte 1 kare, onu saran 3 karelik L, onu saran 5 karelik L ve en dışta 7 karelik L; her L ayrı renkte. Yanında 1 artı 3 artı 5 artı 7 eşittir 16 eşittir 4 çarpı 4.](gorsel/tyt-matematik/01-05-tek-kare.svg "Her tek sayı kareyi bir sıra büyüten bir L parçasıdır. 4 tek sayı toplanınca 4 × 4 kare oluşur.")

| Toplam | Sonuç | Örnek |
|---|---|---|
| $1 + 2 + 3 + \dots + n$ | $\dfrac{n(n + 1)}{2}$ | $1 + \dots + 20 = 210$ |
| $2 + 4 + 6 + \dots + 2n$ | $n(n + 1)$ | $2 + \dots + 40 = 20 \cdot 21 = 420$ |
| $1 + 3 + 5 + \dots + (2n - 1)$ | $n^2$ | $1 + \dots + 29 = 15^2 = 225$ |

Bu formüllerde $n$ **son terim değil, terim sayısıdır**. $2 + 4 + \dots + 40$ için $n = 20$, $1 + 3 + \dots + 29$ için $n = 15$ (çünkü $2n - 1 = 29$).

Ortadan başlayan toplamda iki toplamın farkını al: $11 + 12 + \dots + 30 = (1 + \dots + 30) - (1 + \dots + 10) = 465 - 55 = 410$. Çıkardığın toplam 10'da biter, 11'de değil.

**Kural.** 1'den başlayan dizilerde hazır formülü kullan; önce $n$'yi (terim sayısını) bul.

## Ortanca terim

**Örnek.** Ardışık beş tek sayının toplamı 115'tir. En küçüğü kaçtır?

Terim sayısı tek, bu yüzden tam ortada bir terim var ve bu terim sayıların ortalamasıdır: $115 : 5 = 23$. Ortanın iki yanında ikişer terim, 2'şer adımla: $19, 21, 23, 25, 27$. En küçüğü **19**.

**Çift sayıda terim.** Ardışık dört tam sayının toplamı 74 ise ortalama $74 : 4 = 18{,}5$. Bu bir terim değil, ortadaki iki terimin tam arasıdır: $18$ ve $19$. Sayılar $17, 18, 19, 20$.

**Kural.** Ardışık sayılarda ortalama, $\frac{\text{İlk terim} + \text{Son terim}}{2}$ değerine eşittir. Terim sayısı tekse bu değer ortanca terimdir; çiftse ortadaki iki terimin arasına düşer.

## ÖSYM tuzakları

> **Ardışık tek sayıyı $n, n + 1, n + 2$ yazmak:** Ardışık tek (ya da çift) sayılar 2'şer artar: $x, x + 2, x + 4$. Toplamı 135 olan ardışık beş tek sayıda en küçüğü $25$ değil $23$'tür.

> **Terim sayısında $+1$'i unutmak:** $7$'den $83$'e 4'er giden dizide $\frac{76}{4} = 19$ boşluk, **20** terim vardır.

> **Formüldeki $n$'yi son terim sanmak:** $1 + 3 + \dots + 29 \ne 29^2$. Terim sayısı $n = 15$, toplam $225$.

> **Sınırları yanlış almak:** "İki basamaklı 3'ün katları" $12$ ile başlar, $99$ ile biter. $10$ ya da $9$ ile başlarsan terim sayısı da toplam da değişir.

> **Ortadan başlayan toplamda fazla çıkarmak:** $11 + \dots + 30$ için $1 + \dots + 30$ toplamından $1 + \dots + 10$ çıkarılır, $1 + \dots + 11$ değil.

## Kendini dene

### Soru 1
$4, 7, 10, \dots, 61$ dizisinde kaç terim vardır?

A) 18
B) 19
C) 20
D) 21
E) 22

**Cevap:** C
**Çözüm:** Ortak fark $3$. Terim sayısı $\frac{61 - 4}{3} + 1 = 19 + 1 = 20$. $+1$'i unutan 19 bulur.

### Soru 2
$2 + 4 + 6 + \dots + 40$ toplamı kaçtır?

A) 210
B) 380
C) 400
D) 420
E) 441

**Cevap:** D
**Çözüm:** Ardışık çift sayılar, $2n = 40$ olduğundan $n = 20$ terim. Toplam $n(n + 1) = 20 \cdot 21 = 420$. Kontrol: $\frac{2 + 40}{2} \cdot 20 = 420$. Tek sayı formülünü ($n^2$) kullanan 400, $\frac{n(n + 1)}{2}$ kullanan 210 bulur.

### Soru 3
Ardışık beş tek sayının toplamı 135'tir. Bu sayıların en küçüğü kaçtır?

A) 21
B) 23
C) 25
D) 27
E) 29

**Cevap:** B
**Çözüm:** Ortanca terim $135 : 5 = 27$. Tek sayılar 2'şer artar: $23, 25, 27, 29, 31$. En küçüğü 23. Sayıları 1'er artıran $25, 26, 27, 28, 29$ yazar ve 25 bulur; 27 ise ortanca terimdir.

## Özet kartı

- Ardışık tam sayılarda ortak fark 1; ardışık çift ve tek sayılarda 2.
- Terim sayısı $= \frac{\text{son} - \text{ilk}}{\text{ortak fark}} + 1$.
- Toplam $= \frac{\text{ilk} + \text{son}}{2} \cdot \text{terim sayısı}$.
- $1 + \dots + n = \frac{n(n + 1)}{2}$, $\ 2 + 4 + \dots + 2n = n(n + 1)$, $\ 1 + 3 + \dots + (2n - 1) = n^2$; $n$ terim sayısıdır.
- Toplamı verilen ardışık sayılarda toplamı terim sayısına böl: ortanca terimi (ya da ortadaki iki terimin arasını) bulursun.
- Negatiften başlayan ardışık tam sayılarda karşılıklı terimler birbirini götürür.

## Sonraki adım

Alıştırmaya geç (aşağıdaki düğme). Sonraki ders **Sayı Basamakları**; orada $\overline{ab}$ gibi sayıları basamaklarına ayıracak, ardışık rakamlarla kurulan sayıları da göreceksin.
