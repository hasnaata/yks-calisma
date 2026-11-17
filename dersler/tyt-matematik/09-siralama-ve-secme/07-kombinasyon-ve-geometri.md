---
baslik: Kombinasyon ve Geometri
ders: tyt-matematik
sure: 20 dk
kaynak: MEBİ Konu Özeti 9e9d4f39f8
guncelleme: 2026-11-17
---
# Kombinasyon ve Geometri

**Bu dersin sonunda:** verilen noktalardan kaç doğru, üçgen ya da dörtgen çizilebileceğini ve doğru, çember, çokgen gibi şekillerin en çok kaç noktada kesişebileceğini $C(n, r)$ ile hesaplayabileceksin.

> **TYT'de yeri:** Sıralama–seçme sorularının bir kısmı geometri kılığında gelir: "Bu noktalardan kaç üçgen çizilir?", "Bu doğrular ve çemberler en çok kaç noktada kesişir?". Genelde bir kısmı doğrusal noktalar ya da iki paralel doğru üzerindeki noktalarla zorlaştırılır.

## Önce hatırla

<details><summary>Geçen dersten: 5 kız ve 4 erkek öğrenci arasından 2 kız ve 2 erkekten oluşan 4 kişilik bir ekip kaç farklı biçimde seçilir?</summary>
Kızlar ve erkekler ayrı seçilir, sonuçlar çarpılır: $C(5, 2) \cdot C(4, 2) = 10 \cdot 6 = 60$. Bugün iki paralel doğrudan nokta seçerken aynı çarpmayı yapacaksın.
</details>

<details><summary>Geçen dersten: 4 kız ve 3 erkek arasından en az 1 erkeğin bulunduğu 3 kişilik ekip kaç farklı biçimde seçilir?</summary>
Tümünden istenmeyeni çıkar: $C(7, 3) - C(4, 3) = 35 - 4 = 31$. Bugün doğrusal noktalardan üçgen sayarken de "hepsini say, olmayanları çıkar" yolunu kullanacaksın.
</details>

## Temel fikir

Bir doğru **2** noktayla, bir üçgen **3** noktayla, bir dörtgen **4** noktayla belirlenir. Noktaların hangi sırayla seçildiği önemli değildir: $A$, $B$, $C$ noktalarını hangi sırayla seçersen seç aynı üçgeni çizersin. Bu yüzden şekil saymak **kombinasyondur**.

## 1. Noktalardan geçen doğrular

**Örnek.** Düzlemde herhangi üçü doğrusal olmayan 6 nokta var. Bu noktaların en az ikisinden geçen kaç farklı doğru çizilir?

**Çözüm.** Her doğru 2 noktayla belirlenir ve hiçbir üçü aynı doğru üzerinde olmadığı için her nokta çifti **farklı** bir doğru verir: $C(6, 2) = \dfrac{6 \cdot 5}{2} = 15$.

**Doğrusal nokta varsa.** Şimdi 6 noktadan 4'ü aynı $d$ doğrusu üzerinde olsun, başka hiçbir üçü doğrusal olmasın.

1. Hepsini say: $C(6, 2) = 15$.
2. $d$ üzerindeki 4 noktadan seçilen her çift aynı doğruyu ($d$'yi) verir. Bu çiftlerin sayısı $C(4, 2) = 6$; onları çıkar: $15 - 6 = 9$.
3. $d$ doğrusunu bir kez geri ekle: $9 + 1 = 10$.

![Solda beşgen köşelerinde 5 nokta ve her iki noktadan geçen 10 mavi doğru. Sağda kırmızı d doğrusu üzerinde 4 nokta, dışarıda 2 nokta; dış noktaların her birinden d üzerindeki 4 noktaya 4'er doğru ve iki dış noktadan geçen 1 doğru.](gorsel/tyt-matematik/09-07-dogrular.svg "Sağda say: dış noktalardan 4 + 4 = 8 doğru, iki dış noktadan 1 doğru, bir de d: toplam 10. Formül de aynısını verir: 15 − 6 + 1.")

**Kural.** Herhangi üçü doğrusal olmayan $n$ noktadan $C(n, 2)$ doğru geçer. $k$ tanesi aynı doğru üzerindeyse:

$$C(n, 2) - C(k, 2) + 1$$

**Çokgenin köşegenleri.** Bir $n$-genin köşelerinden seçilen her çift ya bir kenar ya da bir köşegen verir. Kenarları çıkar: köşegen sayısı $C(n, 2) - n$. Sekizgende $C(8, 2) - 8 = 28 - 8 = 20$.

> **Tuzak:** Doğrusal noktaların çiftlerini çıkarıp $+1$'i unutmak. O noktaların üzerindeki $d$ doğrusu da bir doğrudur; bir kez sayılmalı.

## 2. Üçgen ve dörtgen sayısı

**Örnek.** Bir çember üzerinde 7 nokta var. Köşeleri bu noktalardan seçilen kaç üçgen ve kaç dörtgen çizilir?

**Çözüm.** Çember üzerindeki hiçbir üç nokta doğrusal değildir. Üçgen: $C(7, 3) = \dfrac{7 \cdot 6 \cdot 5}{6} = 35$. Dörtgen: $C(7, 4) = C(7, 3) = 35$.

**Doğrusal nokta varsa.** Yukarıdaki 6 noktaya dön (4'ü $d$ üzerinde). Aynı doğrudaki 3 nokta üçgen oluşturmaz.

1. Hepsini say: $C(6, 3) = 20$.
2. $d$ üzerindeki 4 noktadan seçilen üçlüler üçgen değildir: $C(4, 3) = 4$.
3. $20 - 4 = 16$ üçgen.

Burada $+1$ **yok**: doğrusal üçlüler hiçbir şekil vermez, geri eklenecek bir şey yoktur.

**Kural.** Herhangi üçü doğrusal olmayan $n$ noktadan $C(n, 3)$ üçgen, $C(n, 4)$ dörtgen; genel olarak $C(n, r)$ tane $r$-gen çizilir. $k$ nokta doğrusalsa üçgen sayısı:

$$C(n, 3) - C(k, 3)$$

## 3. İki paralel doğru üzerindeki noktalar

**Örnek.** $d_1 \parallel d_2$. $d_1$ üzerinde 3, $d_2$ üzerinde 4 nokta var. Köşeleri bu noktalardan seçilen kaç üçgen ve kaç dörtgen vardır?

![İki yatay paralel doğru: üstte d1 üzerinde 3, altta d2 üzerinde 4 nokta. Solda üstten 1, alttan 2 nokta seçilerek çizilmiş yeşil üçgen; sağda üstten 2, alttan 2 nokta seçilerek çizilmiş mavi dörtgen.](gorsel/tyt-matematik/09-07-paralel.svg "Aynı doğrudan 3 nokta seçilemez. Üçgen için ya 1 üstten 2 alttan ya da 2 üstten 1 alttan; dörtgen için mutlaka 2 üstten 2 alttan.")

**Çözüm (üçgen).** Üç köşenin üçü de aynı doğrudan gelemez. İki durum var:

- 2 nokta $d_1$'den, 1 nokta $d_2$'den: $C(3, 2) \cdot C(4, 1) = 3 \cdot 4 = 12$
- 1 nokta $d_1$'den, 2 nokta $d_2$'den: $C(3, 1) \cdot C(4, 2) = 3 \cdot 6 = 18$

Toplam $12 + 18 = 30$. Kontrol (tümünden çıkarma): $C(7, 3) - C(3, 3) - C(4, 3) = 35 - 1 - 4 = 30$.

**Çözüm (dörtgen).** Bir doğrudan 3 nokta alınırsa dörtgen olmaz. Tek yol: her doğrudan 2 nokta. $C(3, 2) \cdot C(4, 2) = 3 \cdot 6 = 18$.

**Kural.** $d_1$'de $m$, $d_2$'de $n$ nokta varsa:

| Şekil | Sayı |
|---|---|
| Üçgen | $C(m, 2) \cdot n + m \cdot C(n, 2)$ |
| Dörtgen | $C(m, 2) \cdot C(n, 2)$ |
| Doğru | $m \cdot n + 2$ (çaprazlar ve $d_1$, $d_2$) |

> **Tuzak:** Dörtgende "2 + 2" yerine $C(m + n, 4)$ yazmak. Bir doğrudan 3 ya da 4 nokta seçilirse dörtgen oluşmaz.

## 4. En çok kaç noktada kesişir?

**Örnek.** Aynı düzlemde 6 farklı doğru en çok kaç noktada kesişir?

**Çözüm.** Paralel ya da çakışık olmayan iki doğru **tek** noktada kesişir. Doğrular ikişer ikişer eşleşir ve her eşleşme en çok 1 nokta verir. Kesişim noktalarının en çok olması için hiçbir iki doğru paralel olmamalı, hiçbir üç doğru da aynı noktadan geçmemeli: $C(6, 2) \cdot 1 = 15$.

Bu doğrulardan 3'ü birbirine paralel olsaydı, bu 3 doğrunun çiftleri ($C(3, 2) = 3$) kesişmezdi: $15 - 3 = 12$.

Aynı düşünce her şekilde geçerlidir: **çift sayısı × iki şeklin en çok kesişim sayısı.**

![Solda üç çember; her iki çember 2 noktada kesişiyor, toplam 6 kırmızı nokta. Sağda biri yukarı biri aşağı bakan iki üçgen altı köşeli yıldız oluşturuyor, 6 kırmızı kesişim noktası.](gorsel/tyt-matematik/09-07-kesisim.svg "Üç çemberde 3 çift var, her çift 2 nokta: 6. İki üçgen en çok 6 noktada kesişir; bir üçgenin her kenarı öbür üçgeni en çok 2 noktada keser.")

| İki şekil | En çok kesişim | $n$ tane şekil |
|---|---|---|
| doğru – doğru | 1 | $C(n, 2)$ |
| çember – çember | 2 | $2 \cdot C(n, 2)$ |
| üçgen – üçgen | 6 | $6 \cdot C(n, 2)$ |
| $r$-gen – $r$-gen | $2r$ | $2r \cdot C(n, 2)$ |
| doğru – çember | 2 | — |

Örnekler: 5 çember en çok $2 \cdot C(5, 2) = 20$ noktada, 4 üçgen $6 \cdot C(4, 2) = 36$ noktada, 3 kare $2 \cdot 4 \cdot C(3, 2) = 24$ noktada kesişir.

**Karışık örnek.** 4 doğru ve 3 çember en çok kaç noktada kesişir?

Üç tür eşleşme vardır; her birini ayrı say, topla:

1. doğru–doğru: $C(4, 2) \cdot 1 = 6$
2. çember–çember: $C(3, 2) \cdot 2 = 6$
3. doğru–çember: $4 \cdot 3 \cdot 2 = 24$ (her doğru her çemberi en çok 2 noktada keser)

Toplam $6 + 6 + 24 = 36$.

> **Tuzak:** Karışık sorularda doğru–çember eşleşmesini unutmak ya da onu 1 noktayla saymak. Bir doğru bir çemberi **2** noktada kesebilir.

## ÖSYM tuzakları

> **Doğruda $+1$, üçgende $+1$ yok.** Doğru sayarken doğrusal noktaların doğrusu bir kez eklenir: $C(n, 2) - C(k, 2) + 1$. Üçgen sayarken eklenmez: $C(n, 3) - C(k, 3)$.

> **Permütasyon yazmak.** $ABC$ ile $BCA$ aynı üçgendir. $P(7, 3) = 210$ değil, $C(7, 3) = 35$.

> **Çemberde iki kat.** $n$ çember $C(n, 2)$ değil $2 \cdot C(n, 2)$ noktada kesişir. Çokgende de kenar sayısının 2 katı unutulmaz: iki beşgen en çok 10 noktada kesişir.

> **"En çok" sözcüğü.** Formüller en çok kesişim sayısını verir. Soru paralel doğrular ya da aynı noktadan geçen doğrular verirse o kesişimleri çıkar.

> **Köşegen ile doğru farkı.** $n$-genin köşelerinden $C(n, 2)$ doğru geçer; bunların $n$ tanesi kenardır. Köşegen sayısı $C(n, 2) - n$'dir.

## Kendini dene

### Soru 1
Bir çember üzerinde birbirinden farklı 9 nokta vardır. Köşeleri bu noktalardan seçilen kaç farklı üçgen çizilebilir?

A) 36
B) 72
C) 84
D) 126
E) 504

**Cevap:** C
**Çözüm:** Çember üzerindeki hiçbir üç nokta doğrusal değildir; her üçlü bir üçgen verir: $C(9, 3) = \dfrac{9 \cdot 8 \cdot 7}{6} = 84$. 36, $C(9, 2)$ (doğru sayısı); 126, $C(9, 4)$ (dörtgen sayısı); 504 ise sırayı önemli sayan $P(9, 3)$'tür.

### Soru 2
Düzlemdeki 10 noktadan 4'ü aynı doğru üzerindedir; bunun dışında hiçbir üçü doğrusal değildir. Bu noktaların en az ikisinden geçen kaç farklı doğru çizilebilir?

A) 39
B) 40
C) 42
D) 45
E) 51

**Cevap:** B
**Çözüm:** $C(10, 2) - C(4, 2) + 1 = 45 - 6 + 1 = 40$. 39, doğrusal noktaların doğrusunu geri eklemeyi unutmaktır; 45, doğrusal noktaları hiç dikkate almamaktır; 42 ise çiftler yerine üçlüleri çıkarmaktır ($45 - 4 + 1$).

### Soru 3
Aynı düzlemde çizilen 3 farklı çember ve 2 farklı doğru en çok kaç noktada kesişir?

A) 7
B) 13
C) 18
D) 19
E) 20

**Cevap:** D
**Çözüm:** Çember–çember $2 \cdot C(3, 2) = 6$, doğru–doğru $C(2, 2) = 1$, doğru–çember $2 \cdot 3 \cdot 2 = 12$. Toplam $6 + 1 + 12 = 19$. 7, doğru–çember kesişimlerini unutmaktır; 13, doğru–çemberi 1 noktayla saymaktır; 18, iki doğrunun kesişimini unutmaktır.

## Özet kartı

- Doğru 2, üçgen 3, dörtgen 4 noktayla belirlenir; sıra önemsiz: $C(n, 2)$, $C(n, 3)$, $C(n, 4)$.
- $k$ nokta doğrusal: doğru $C(n, 2) - C(k, 2) + 1$; üçgen $C(n, 3) - C(k, 3)$.
- İki paralel doğru ($m$ ve $n$ nokta): üçgen $C(m, 2) \cdot n + m \cdot C(n, 2)$; dörtgen $C(m, 2) \cdot C(n, 2)$.
- $n$-genin köşegen sayısı $C(n, 2) - n$.
- En çok kesişim = çift sayısı × iki şeklin kesişimi: doğru 1, çember 2, üçgen 6, $r$-gen $2r$, doğru–çember 2.
- Karışık sorularda her eşleşme türünü ayrı say, topla.

## Sonraki adım

Alıştırmaya geç (aşağıdaki düğme). Sonraki ders: **Pascal Üçgeni ve Binom Açılımı**. $C(n, r)$ sayıları orada bir toplamın kuvvetindeki katsayılar olarak karşına çıkacak.
