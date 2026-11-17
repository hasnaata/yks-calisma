---
baslik: Kalıtımla İlgili Kavramlar, Olasılık İlkeleri ve Gamet Çeşitlerinin Bulunması
ders: tyt-biyoloji
sure: 25 dk
kaynak: MEBİ Konu Özeti a8cdc267b5
guncelleme: 2026-11-16
---
# Kalıtımla İlgili Kavramlar, Olasılık İlkeleri ve Gamet Çeşitlerinin Bulunması

**Bu dersin sonunda:** genotipi verilen bir bireyin kaç çeşit gamet oluşturacağını ve belirli bir gameti hangi olasılıkla oluşturacağını hesaplayabilecek, alel, lokus, homozigot, heterozigot, genotip ve fenotip kavramlarını karıştırmadan kullanabileceksin.

> **TYT'de yeri:** Kalıtım sorularının hepsi bu dersteki dile dayanır. Doğrudan gelen kalıplar: "Bu birey kaç çeşit gamet oluşturur?", "Şu gametin oluşma olasılığı kaçtır?" ve kavram tanımı soruları. Çaprazlama sorularının ilk adımı da her zaman gametleri yazmaktır.

## Önce hatırla

<details><summary>Eşeyli üremenin temelini oluşturan iki olay hangileridir? Gametler kaç kromozom takımı taşır?</summary>
Mayoz ve döllenme. Mayoz, diploit ($2n$) hücreden haploit ($n$) gametleri oluşturur; döllenme iki gameti birleştirip yeniden $2n$ zigotu verir. Bu derste mayozun sonucuna bakacaksın: bir gamete her gen çiftinden <b>yalnızca bir alel</b> gider.
</details>

## Temel kavramlar

| Kavram | Anlamı | Örnek |
|---|---|---|
| **Gen** | Bir karakterin oluşumunda etkili DNA parçası | Tohum şekli geni |
| **Lokus** | Genin kromozom üzerindeki özgül yeri | |
| **Homolog kromozom** | Biri anneden, biri babadan gelen; aynı karakterlerin genlerini taşıyan kromozom çifti | |
| **Alel** | Homolog kromozomların karşılıklı lokuslarında bulunan, aynı karaktere etki eden genin farklı biçimleri | D ve d |
| **Karakter** | Dölden döle aktarılan nitelik | Göz rengi, tohum şekli |
| **Özellik** | Bir karakterin her bir farklı tipi | Mavi göz, buruşuk tohum |

![Yeşil zemin üzerinde dağınık duran, sarı renkli, çubuk ve X biçimli onlarca insan kromozomunun mikroskop görüntüsü](gorsel/tyt-biyoloji/12-01-karyotip.jpg "Mikroskop altında insan kromozomları. Genler bu kromozomların üzerinde, lokus denen belirli yerlerde bulunur. Görsel: Josef Reischig, CC BY-SA 3.0.")

Bir genin alelleri aynı harfin büyüğü ve küçüğüyle gösterilir.

- **Baskın (dominant) alel:** heterozigot durumda fenotipte etkisini gösteren aleldir; büyük harfle yazılır (A).
- **Çekinik (resesif) alel:** heterozigot durumda fenotipte etkisini gösteremeyen aleldir; küçük harfle yazılır (a).

## Genotip ve fenotip

- **Genotip:** bireyin sahip olduğu genlerin tamamı (harflerle yazdığın şey).
- **Fenotip:** gözlenebilen ya da ölçülebilen dış görünüş.

| Genotip | Adı | Fenotip | Gamet |
|---|---|---|---|
| AA | Homozigot (arı döl) baskın | Baskın | Tek çeşit: A |
| Aa | Heterozigot (melez) | Baskın | İki çeşit: A ve a |
| aa | Homozigot (arı döl) çekinik | Çekinik | Tek çeşit: a |

![Şema: AA ve Aa genotiplerinden çıkan oklar baskın fenotipte birleşir, aa genotipinden çıkan ok çekinik fenotipe gider](gorsel/tyt-biyoloji/12-01-genotip-fenotip.svg "İki farklı genotip (AA ve Aa) aynı baskın fenotipi verir; çekinik fenotipe ise yalnızca aa ulaşır.")

Bu tablodan iki sonuç çıkar ve ikisi de sık sorulur:

1. **Çekinik fenotipli** bireyin genotipi kesin bellidir: aa.
2. **Baskın fenotipli** bireyin genotipi kesin değildir: AA ya da Aa olabilir.

Diploit ($2n$) canlıda her karakter için iki alel yazılır (Aa). Haploit ($n$) canlıda ya da gamette her karakter için tek alel bulunur (A ya da a).

**Çevrenin etkisi:** Kan grubu, renk körlüğü gibi bazı özellikler yalnızca genlerle belirlenir. Boy uzunluğu, zekâ, derinin bronzlaşması gibi özelliklerde ise genlerle birlikte çevre de etkilidir. Çevre (sıcaklık, ışık, nem, besin) genin **işleyişini** değiştirir, genin **yapısını** değiştirmez. Bu olaya **modifikasyon** denir ve kalıtsal değildir.

## Olasılık ilkeleri

Kalıtım hesaplarının tamamı üç kurala dayanır.

| Kural | Ne zaman | Örnek |
|---|---|---|
| **Bağımsızlık** | Şansa bağlı bir olayın sonucu, sonraki denemeleri etkilemez. | Üç kız çocuğu olan ailenin dördüncü çocuğunun kız olma olasılığı yine $\frac{1}{2}$'dir. |
| **Çarpım ("ve")** | İki bağımsız olayın birlikte gerçekleşmesi isteniyorsa olasılıklar çarpılır. | İki paranın ikisinin de tura gelmesi: $\frac{1}{2} \cdot \frac{1}{2} = \frac{1}{4}$ |
| **Toplam ("ya da")** | Bir olay birden fazla yolla gerçekleşebiliyorsa yolların olasılıkları toplanır. | İki paradan birinin yazı, diğerinin tura gelmesi: $\frac{1}{4} + \frac{1}{4} = \frac{1}{2}$ |

Son örneğe dikkat et: "biri yazı, diğeri tura" iki ayrı yolla olur (yazı–tura ve tura–yazı). Sıra belirtilmemişse iki yolu da saymalısın.

## Gamet çeşidi sayısı

Gamet, mayozla oluşan $n$ kromozomlu üreme hücresidir ve **her karakter için bir alel** taşır.

- Aleller **farklı kromozomlarda** ise genler **bağımsız**dır.
- Aleller **aynı kromozomda** ise genler **bağlı**dır.

Soruda aksi söylenmedikçe genleri bağımsız kabul et.

### Bağımsız genlerde

$$\text{Gamet çeşidi sayısı} = 2^n \qquad (n = \text{heterozigot karakter sayısı})$$

Homozigot karakterler gamet çeşidini değiştirmez; yalnızca heterozigot olanları say.

| Genotip | Heterozigot karakter | Gamet çeşidi | Gametler |
|---|---|---|---|
| BBdd | 0 | $2^0 = 1$ | Bd |
| Bbdd | 1 | $2^1 = 2$ | Bd, bd |
| AaDd | 2 | $2^2 = 4$ | AD, Ad, aD, ad |
| AaDDBb | 2 | $2^2 = 4$ | ADB, ADb, aDB, aDb |

![Dallanma şeması: AaDd bireyinden yarım olasılıkla A ya da a seçilir, her birinden yine yarım olasılıkla D ya da d eklenerek AD, Ad, aD, ad gametleri elde edilir](gorsel/tyt-biyoloji/12-01-gamet-agaci.svg "AaDd için dallanma: her heterozigot karakter dalları ikiye katlar. Dört gametin her biri 1/2 · 1/2 = 1/4 olasılıkla oluşur.")

### Belirli bir gametin olasılığı

Her karaktere ayrı bak, sonra çarp (çarpım kuralı):

- Heterozigot karakterde (Aa) istenen alelin gamete gitme olasılığı $\frac{1}{2}$.
- Homozigot karakterde (AA ya da aa) o alelin gitme olasılığı $1$.
- Bireyde **olmayan** bir alel isteniyorsa olasılık $0$.

**Çözümlü örnek 1.** TTNnkkSsrr genotipli bireyde genler bağımsızdır.

a) Kaç çeşit gamet oluşturur? Heterozigot karakterler Nn ve Ss, yani $n = 2$. Gamet çeşidi $2^2 = 4$.

b) TNksr gametini oluşturma olasılığı kaçtır?

$$\underbrace{1}_{T} \cdot \underbrace{\tfrac{1}{2}}_{N} \cdot \underbrace{1}_{k} \cdot \underbrace{\tfrac{1}{2}}_{s} \cdot \underbrace{1}_{r} = \frac{1}{4}$$

**Çözümlü örnek 2.** AaBbDd genotipli bireyin gametlerinde A, B, D alellerinden **en az birinin** bulunma olasılığı kaçtır? Tersini hesapla: hiçbir baskın alel taşımayan tek gamet abd'dir ve olasılığı $\frac{1}{2} \cdot \frac{1}{2} \cdot \frac{1}{2} = \frac{1}{8}$. İstenen olasılık $1 - \frac{1}{8} = \frac{7}{8}$.

### Bağlı genlerde

Bağlı genler aynı kromozomda oldukları için mayozda **birlikte** hareket eder.

AaBb genotipli bir bireyde A ile B aynı kromozomda, a ile b homoloğunda olsun:

| Durum | Oluşan gametler | Çeşit sayısı |
|---|---|---|
| Krossing over **yok** | AB, ab | 2 |
| Krossing over **var** | AB, ab, Ab, aB | 4 |

![Şema: A ile B bağlı AaBb bireyi krossing over yoksa AB ve ab olmak üzere 2 çeşit, krossing over varsa AB, ab, Ab, aB olmak üzere 4 çeşit gamet oluşturur](gorsel/tyt-biyoloji/12-01-bagli-genler.svg "Bağlı genlerde önce krossing over var mı diye bak: yoksa 2, varsa 4 çeşit gamet.")

- Krossing over yoksa bağlı genler tek bir karakter gibi davranır: birlikte giden gen grubunu tek bir heterozigot çift say.
- Krossing over varsa çeşit sayısı bağımsız genlerdeki gibi $2^n$ ile bulunur.
- Krossing over yeni gen kombinasyonları oluşturur, gamet çeşitliliğini artırır.
- İki gen kromozom üzerinde birbirinden ne kadar **uzaksa** krossing over ile ayrılma olasılığı o kadar **yüksektir**.

![Mavi ve pembe iki homolog kromozomun yan yana gelip üst üste binmesini, parça değiştirmesini ve sonunda uçlarında karşı rengin parçasını taşıyan kromozomlara dönüşmesini gösteren dört aşamalı 3B çizim](gorsel/tyt-biyoloji/12-01-krossing-over.png "Krossing over: homolog kromozomlar parça değiştirir. Son aşamada uçların renk değiştirdiğine bak; yeni gen kombinasyonları böyle oluşur. Görsel: Christinelmiller, CC BY-SA 4.0.")

**Çözümlü örnek 3.** AaBbDd genotipli bireyde A ve B bağlı (A ile B aynı kromozomda), D geni başka bir kromozomdadır. Krossing over yoksa: AB/ab grubu 2 çeşit, Dd 2 çeşit verir; toplam $2 \cdot 2 = 4$ çeşit gamet (ABD, ABd, abD, abd). Krossing over varsa $2^3 = 8$ çeşit.

## ÖSYM tuzakları

> **Formüldeki $n$ toplam karakter sayısı değildir.** $n$ yalnızca **heterozigot** karakterlerin sayısıdır. AaBBddEe için $n = 2$, gamet çeşidi 4'tür; 16 değil.

> **"Kaç çeşit gamet" ile "kaç gamet" aynı soru değildir.** $2^n$ çeşit sayısını verir. Homozigot bir birey milyonlarca gamet üretir ama hepsi tek çeşittir.

> **Baskın fenotipli bireye "kesinlikle homozigottur" denemez.** Genotipi AA ya da Aa olabilir. Kesin genotip yalnızca çekinik fenotipte bilinir.

> **Modifikasyon kalıtsal değildir.** Çevre genin işleyişini etkiler, yapısını değiştirmez; bu yüzden sonraki kuşağa aktarılmaz.

## Kendini dene

### Soru 1
Genleri bağımsız olan AaBbDD genotipli bir birey kaç çeşit gamet oluşturabilir?

A) 1
B) 2
C) 4
D) 6
E) 8

**Cevap:** C
**Çözüm:** Heterozigot karakterler Aa ve Bb'dir, DD homozigottur. $n = 2$ olduğundan $2^2 = 4$ çeşit gamet oluşur: ABD, AbD, aBD, abD.

### Soru 2
Bir karakter bakımından çekinik fenotipe sahip diploit bir bireyin genotipi aşağıdakilerden hangisidir?

A) AA
B) aa
C) Aa
D) A
E) a

**Cevap:** B
**Çözüm:** Çekinik alel etkisini yalnızca homozigot durumda gösterir. Diploit canlıda iki alel yazılır; bu yüzden cevap aa'dır. Tek harfli gösterimler haploit hücreler içindir.

### Soru 3
Genleri bağımsız olan AaBb genotipli bir bireyin ab genotipli gamet oluşturma olasılığı kaçtır?

A) $\frac{1}{16}$
B) $\frac{1}{8}$
C) $\frac{1}{2}$
D) $\frac{3}{4}$
E) $\frac{1}{4}$

**Cevap:** E
**Çözüm:** a alelinin gamete gitme olasılığı $\frac{1}{2}$, b alelinin gitme olasılığı $\frac{1}{2}$'dir. İkisinin birlikte gitmesi: $\frac{1}{2} \cdot \frac{1}{2} = \frac{1}{4}$.

## Özet kartı

- Alel: aynı genin farklı biçimleri; lokus: genin kromozomdaki yeri.
- AA ve aa homozigot (tek çeşit gamet), Aa heterozigot (iki çeşit gamet).
- Çekinik fenotip = kesin aa; baskın fenotip = AA ya da Aa.
- "Ve" için çarp, "ya da" için topla; her olay bir öncekinden bağımsızdır.
- Gamet çeşidi $= 2^n$, $n$ = heterozigot karakter sayısı.
- Bağlı genler krossing over yoksa birlikte gider; krossing over çeşitliliği artırır.

## Sonraki adım

Alıştırmaya geç (aşağıdaki düğme).
