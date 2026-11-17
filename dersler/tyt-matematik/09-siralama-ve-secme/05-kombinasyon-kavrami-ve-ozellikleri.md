---
baslik: Kombinasyon Kavramı ve Özellikleri
ders: tyt-matematik
sure: 25 dk
kaynak: MEBİ Konu Özeti 6a9890787e
guncelleme: 2026-11-17
---
# Kombinasyon Kavramı ve Özellikleri

**Bu dersin sonunda:** sıranın önemsiz olduğu seçimleri $C(n, r)$ ile sayabilecek, $C(n, r) = C(n, n - r)$ ve $C(n, r) + C(n, r + 1) = C(n + 1, r + 1)$ özelliklerini denklemde kullanabilecek ve "belirli eleman bulunsun / bulunmasın" seçimlerini sayabileceksin.

> **TYT'de yeri:** Kombinasyon çoğu zaman "kaç farklı ekip / grup / komisyon seçilebilir?" diye sorulur. Ayrıca $C(n, 2) = 28$ gibi kısa bir denklem, $C(n, a) = C(n, b)$ eşitliği ya da "şu kişi mutlaka bulunsun, bu kişi bulunmasın" koşullu bir seçim sorusu gelir.

## Önce hatırla

<details><summary>Tekrarlı permütasyondan: KAYAK kelimesinin harfleri yer değiştirilerek anlamlı ya da anlamsız kaç farklı 5 harfli kelime yazılabilir?</summary>
5 harf var; K iki kez, A iki kez, Y bir kez. $\dfrac{5!}{2! \cdot 2! \cdot 1!} = \dfrac{120}{4} = 30$.
</details>

<details><summary>Tekrarlı permütasyondan: 3 özdeş kırmızı ve 2 özdeş mavi top bir sıraya kaç farklı biçimde dizilir?</summary>
$\dfrac{5!}{3! \cdot 2!} = \dfrac{120}{12} = 10$. Bu 10 sayısını aklında tut: dersin sonunda başka bir yoldan da karşına çıkacak.
</details>

## Kombinasyon nedir?

**Örnek.** $\{a, b, c, d\}$ kümesinden 2 eleman seçilecek. Kaç farklı seçim vardır?

Hepsini yaz: $\{a, b\}, \{a, c\}, \{a, d\}, \{b, c\}, \{b, d\}, \{c, d\}$. Toplam **6** seçim.

$\{a, b\}$ ile $\{b, a\}$ **aynı** kümedir: burada sıra önemli değil. Önceki derslerde 2 elemanı **sıralasaydık** $P(4, 2) = 4 \cdot 3 = 12$ bulurduk; çünkü her seçim kendi içinde $2! = 2$ biçimde sıralanır.

![Solda 6 alt küme kutusu: a b, a c, a d, b c, b d, c d. Her birinden çıkan okla sağda iki sıralı diziliş, örneğin ab ve ba. Altta C(4, 2) eşittir 6, P(4, 2) eşittir 12 ve 12 eşittir 6 çarpı 2 faktöriyel.](gorsel/tyt-matematik/09-05-sirali-sirasiz.svg "Her seçim 2 sıralı dizilişe karşılık gelir. Sıralı sayıyı sıralama sayısına bölersen sırasız sayıyı bulursun.")

**Tanım.** $n$ elemanlı bir $A$ kümesinin $r$ elemanlı alt kümelerinin her birine $A$'nın **$r$'li kombinasyonu** denir. Bunların sayısı $C(n, r)$ ya da $\dbinom{n}{r}$ ile gösterilir. Yukarıdaki örnekte $C(4, 2) = 6$.

| | Permütasyon | Kombinasyon |
|---|---|---|
| Ne sayar? | sıralı dizilişler | sırasız seçimler (alt kümeler) |
| Sözcük ipucu | sırala, diz, 1.-2.-3. seç, görev dağıt | seç, ekip, grup, komisyon |
| $\{a, b\}$ ve $\{b, a\}$ | farklı | aynı |

## $C(n, r)$ formülü

**Örnek.** 8 kişilik bir sınıftan 3 kişilik bir temizlik ekibi kaç farklı biçimde seçilir?

Önce sıralıymış gibi say: $P(8, 3) = 8 \cdot 7 \cdot 6 = 336$. Ama ekipte görev farkı yok; aynı 3 kişi kendi içinde $3! = 6$ biçimde sıralanıp hep aynı ekibi verir. Her ekip 6 kez sayıldı:

$$C(8, 3) = \frac{P(8, 3)}{3!} = \frac{8 \cdot 7 \cdot 6}{3 \cdot 2 \cdot 1} = \frac{336}{6} = 56.$$

**Kural.**
$$C(n, r) = \binom{n}{r} = \frac{n!}{r! \cdot (n - r)!} \qquad\text{ve}\qquad P(n, r) = C(n, r) \cdot r!$$

Pratikte: pay kısmında $n$'den başlayıp **$r$ tane** azalan sayının çarpımı, paydada $r!$ bulunur. Örneğin $C(7, 2) = \dfrac{7 \cdot 6}{2 \cdot 1} = 21$, $C(9, 3) = \dfrac{9 \cdot 8 \cdot 7}{3 \cdot 2 \cdot 1} = 84$.

**Denklem örneği.** $C(n, 2) = 28$ ise $n$ kaçtır?

$C(n, 2) = \dfrac{n(n - 1)}{2} = 28$, yani $n(n - 1) = 56 = 8 \cdot 7$. Buradan $n = 8$.

> **Tuzak:** $C(n, 2) = 28$ görünce $n(n-1) = 28$ yazıp 2'ye bölmeyi unutma. Önce paydayı karşıya at: $n(n-1) = 56$.

## Kolay değerler

| İfade | Değer | Anlamı |
|---|---|---|
| $C(n, 0)$ | $1$ | hiç eleman seçmemenin tek yolu: boş küme |
| $C(n, 1)$ | $n$ | tek eleman seçmenin $n$ yolu |
| $C(n, n)$ | $1$ | hepsini seçmenin tek yolu: kümenin kendisi |
| $C(n, 2)$ | $\frac{n(n-1)}{2}$ | ikili seçimler (tokalaşma, maç sayısı) |

$C(n, 0) = 1$ çünkü $\dfrac{n!}{0! \cdot n!} = 1$ ve $0! = 1$.

## Simetri: $C(n, r) = C(n, n - r)$

**Örnek.** 6 kişilik bir gruptan 2 kişi geziye gidecek, 4 kişi kalacak. Gidenleri seçmek kaç yolla olur? Kalanları seçmek kaç yolla olur?

Gidecek 2 kişiyi seçtiğin anda kalacak 4 kişi de belli olur. Yani her "giden ikili" tam bir "kalan dörtlü"ye karşılık gelir:

$$C(6, 2) = \frac{6 \cdot 5}{2 \cdot 1} = 15, \qquad C(6, 4) = \frac{6 \cdot 5 \cdot 4 \cdot 3}{4 \cdot 3 \cdot 2 \cdot 1} = 15.$$

![6 numaralı daire: 1 ve 2 yeşil çerçevede gidenler, 3, 4, 5, 6 mavi çerçevede kalanlar. Altta C(6, 2) eşittir C(6, 4) eşittir 15.](gorsel/tyt-matematik/09-05-simetri.svg "Seçilenleri belirlemek, seçilmeyenleri belirlemekle aynı şeydir. Bu yüzden 2'li ve 4'lü seçimlerin sayısı eşittir.")

**Kural.** $C(n, r) = C(n, n - r)$. Hesapta işine yarar: $C(10, 8) = C(10, 2) = \dfrac{10 \cdot 9}{2} = 45$. Sekiz çarpan yerine iki çarpan yazarsın.

**Denklem örneği.** $C(n, 3) = C(n, 5)$ ise $n$ kaçtır?

$C(n, a) = C(n, b)$ ise ya $a = b$ ya da $a + b = n$. Burada $3 \ne 5$, o hâlde $n = 3 + 5 = 8$.

> **Tuzak:** $C(n, 3) = C(n, 5)$ görünce "$3 = 5$ olamaz, çözüm yok" deme. Simetri sayesinde $n = 8$ çözümdür.

## Belirli eleman bulunsun ya da bulunmasın

**Örnek.** $A = \{a, b, c, d, e, f, x, y\}$ kümesi veriliyor (8 eleman).

a) 3 elemanlı alt kümelerin kaçında $x$ **bulunur**?
b) 3 elemanlı alt kümelerin kaçında $y$ **bulunmaz**?
c) 3 elemanlı alt kümelerin kaçında $x$ bulunur ama $y$ bulunmaz?

a) $x$'i baştan kümeye koy. Geriye 2 eleman seçilecek, aday $x$ dışındaki 7 eleman: $C(7, 2) = 21$.

b) $y$'yi adaylardan çıkar. 7 elemandan 3'ü seçilir: $C(7, 3) = \dfrac{7 \cdot 6 \cdot 5}{6} = 35$.

c) $x$'i koy, $y$'yi çıkar. Adaylar $a, b, c, d, e, f$ (6 eleman), seçilecek 2 eleman: $C(6, 2) = 15$.

**Kural.** $x$ bulunsun: $x$'i al, kalan $n - 1$ elemandan $r - 1$ tane seç, $C(n - 1, r - 1)$. $x$ bulunmasın: $x$'i at, $C(n - 1, r)$.

![Akış şeması: Seçilenler sıralanıyor mu? Evet ise permütasyon. Hayır ise kombinasyon; x bulunsun ise x'i al, n eksi 1'den r eksi 1 seç; x bulunmasın ise x'i at, n eksi 1'den r seç.](gorsel/tyt-matematik/09-05-yontem.svg "Önce sıranın önemli olup olmadığına karar ver. Sonra koşullu elemanı ya baştan al ya da adaylardan çıkar.")

## Toplama özelliği: $C(n, r) + C(n, r + 1) = C(n + 1, r + 1)$

Yukarıdaki örneğe tekrar bak. 8 elemanlı kümenin bütün 3'lü alt kümeleri ikiye ayrılır: $x$'i içerenler ve içermeyenler. Bir alt küme ya birinci gruptadır ya ikinci grupta, ikisinde birden olamaz.

![Üstte 3 elemanlı alt kümeler, C(8, 3) eşittir 56. Altta iki kutu: x var, C(7, 2) eşittir 21; x yok, C(7, 3) eşittir 35. En altta 21 artı 35 eşittir 56.](gorsel/tyt-matematik/09-05-x-var-yok.svg "Bütün seçimler, x'in bulunduğu ve bulunmadığı seçimlere ayrılır. İki grubun toplamı hepsini verir.")

$$C(7, 2) + C(7, 3) = 21 + 35 = 56 = C(8, 3).$$

**Kural.** $C(n, r) + C(n, r + 1) = C(n + 1, r + 1)$. Alt satırları (üst sayı aynı, alt sayılar ardışık) topla: üst sayı 1 artar, alt sayı büyük olanı alır.

**Örnek.** $C(9, 4) + C(9, 5)$ kaçtır? Kural: $C(10, 5) = \dfrac{10 \cdot 9 \cdot 8 \cdot 7 \cdot 6}{120} = 252$. Kontrol: $126 + 126 = 252$.

## Bütün alt kümeler: $C(n, 0) + C(n, 1) + \dots + C(n, n) = 2^n$

**Örnek.** $\{a, b, c, d\}$ kümesinin kaç alt kümesi vardır?

Eleman sayısına göre say: 0 elemanlı 1, 1 elemanlı 4, 2 elemanlı 6, 3 elemanlı 4, 4 elemanlı 1.

$$1 + 4 + 6 + 4 + 1 = 16 = 2^4.$$

Başka bir yoldan: her eleman için iki karar var, "alınır" ya da "alınmaz". 4 eleman, $2 \cdot 2 \cdot 2 \cdot 2 = 16$.

**Kural.** $n$ elemanlı kümenin alt küme sayısı $2^n$'dir. "En az 1 elemanlı" denirse boş kümeyi çıkar: $2^n - 1$.

**Önce hatırla bağlantısı.** 3 kırmızı ve 2 mavi topu dizmek, 5 yerden mavilerin gideceği 2 yeri **seçmek** demektir: $C(5, 2) = 10$. Tekrarlı permütasyonla bulduğun sayının aynısı.

## ÖSYM tuzakları

> **Sıra önemli mi?** "3 kişilik ekip" kombinasyondur: $C(8, 3) = 56$. "Başkan, yardımcı, sekreter" seçilecekse görevler farklıdır, permütasyondur: $P(8, 3) = 336$. Soruyu okurken görev farkı var mı diye bak.

> **Paydayı yanlış yazmak:** $C(n, r) = \dfrac{n!}{r!}$ değildir. Paydada $r! \cdot (n - r)!$ var. Kısa yol: üstte $r$ tane azalan çarpan, altta $r!$.

> **$C(n, 0)$'ı 0 sanmak:** $C(n, 0) = C(n, n) = 1$'dir. "Hiç seçmemek" de bir seçimdir (boş küme).

> **"Bulunsun" sorusunda $r$'yi azaltmamak:** $x$ mutlaka bulunacaksa $x$ zaten bir yer kaplar. $C(7, 3)$ değil $C(7, 2)$ seçersin.

> **Simetride tek çözüm bulmak:** $C(7, k) = 35$ ise $k = 3$ ya da $k = 4$ olabilir. İki değeri de düşün.

## Kendini dene

### Soru 1
$C(9, 7)$ işleminin sonucu kaçtır?

A) 9
B) 36
C) 72
D) 84
E) 504

**Cevap:** B
**Çözüm:** Simetri: $C(9, 7) = C(9, 2) = \dfrac{9 \cdot 8}{2} = 36$. 72, 2'ye bölmeyi unutmaktır ($P(9, 2)$); 84, $C(9, 3)$'tür; 504 ise $P(9, 3)$'tür.

### Soru 2
$C(n, 2) + C(n, 3) = C(9, 3)$ olduğuna göre $n$ kaçtır?

A) 6
B) 7
C) 8
D) 9
E) 10

**Cevap:** C
**Çözüm:** Toplama özelliği: $C(n, 2) + C(n, 3) = C(n + 1, 3)$. O hâlde $C(n + 1, 3) = C(9, 3)$, $n + 1 = 9$, $n = 8$. Kontrol: $C(8, 2) + C(8, 3) = 28 + 56 = 84 = C(9, 3)$. 9, üst sayının 1 arttığını unutmaktır; 10 ise $n - 1 = 9$ yazmaktır.

### Soru 3
Bir manavda birbirinden farklı 7 meyve vardır. Bunlardan 3'ü ile meyve salatası yapılacaktır. Salatada elma **mutlaka bulunacak**, muz ise **bulunmayacaktır**. Kaç farklı salata yapılabilir?

A) 10
B) 15
C) 20
D) 21
E) 35

**Cevap:** A
**Çözüm:** Elmayı salataya koy, muzu adaylardan çıkar. Geriye 5 meyveden 2 tane seçilir: $C(5, 2) = 10$. 15 ($C(6, 2)$), muzu çıkarmayı unutmaktır; 20 ($C(6, 3)$), elmanın bir yer kapladığını unutmaktır; 21 ($C(7, 2)$), elmayı adaylardan çıkarmamak ve muzu unutmaktır; 35 ise koşulsuz seçimdir ($C(7, 3)$).

## Özet kartı

- Kombinasyon = sırasız seçim = alt küme. $C(n, r) = \dfrac{n!}{r! \cdot (n - r)!}$, $P(n, r) = C(n, r) \cdot r!$.
- $C(n, 0) = C(n, n) = 1$, $C(n, 1) = n$, $C(n, 2) = \dfrac{n(n-1)}{2}$.
- $C(n, r) = C(n, n - r)$; $C(n, a) = C(n, b)$ ise $a = b$ ya da $a + b = n$.
- $C(n, r) + C(n, r + 1) = C(n + 1, r + 1)$.
- Alt küme sayısı $2^n$; boş olmayanlar $2^n - 1$.
- $x$ bulunsun: $C(n - 1, r - 1)$; $x$ bulunmasın: $C(n - 1, r)$.

## Sonraki adım

Alıştırmaya geç (aşağıdaki düğme). Sonraki ders **Kombinasyon Problemleri**; "en az bir kız", "iki gruptan ayrı ayrı seçim" gibi birden çok koşulu olan seçimleri sayacaksın.
