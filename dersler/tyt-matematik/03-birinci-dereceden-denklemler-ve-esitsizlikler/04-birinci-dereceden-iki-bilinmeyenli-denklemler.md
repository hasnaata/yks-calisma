---
baslik: Birinci Dereceden İki Bilinmeyenli Denklemler
ders: tyt-matematik
sure: 20 dk
kaynak: MEBİ Konu Özeti add5518705
guncelleme: 2026-11-17
---
# Birinci Dereceden İki Bilinmeyenli Denklemler

**Bu dersin sonunda:** iki bilinmeyenli bir denklem sistemini yok etme ya da yerine koyma yöntemiyle çözebilecek, katsayılara bakarak sistemin tek çözümlü, çözümsüz ya da sonsuz çözümlü olduğunu söyleyebilecek ve bir problemi iki denkleme çevirebileceksin.

> **TYT'de yeri:** Doğrudan "sistemi çöz" sorusu azdır; ama "bilet, para, araç, yaş" problemlerinin çoğu iki bilinmeyenli bir sisteme döner. Doğrudan gelen kalıplar: "$x + y$ kaçtır?" (çözmeden toplama kısa yolu), "sistemin çözüm kümesi boş küme / sonsuz elemanlı ise $a + b$ kaçtır?" ve "$x$, $y$ doğal sayı ise kaç farklı $(x, y)$ ikilisi vardır?".

## Önce hatırla

<details><summary>Basit eşitsizliklerden: $-2x + 5 > 11$ eşitsizliğinin çözüm kümesi nedir?</summary>
İki taraftan $5$ çıkar: $-2x > 6$. Negatif sayıya bölünce yön döner: $x < -3$. Çözüm kümesi <b>$(-\infty, -3)$</b>.
</details>

<details><summary>Basit eşitsizliklerden: $1 < a < 4$ ve $-2 < b < 3$ ise $a - b$ hangi aralıktadır?</summary>
Taraf tarafa çıkarma yapılmaz. Önce $b$'yi $-1$ ile çarp: $-3 < -b < 2$. Sonra topla: $1 + (-3) < a - b < 4 + 2$, yani <b>$-2 < a - b < 6$</b>.
</details>

## İki bilinmeyenli denklem ve çözümleri

**Örnek.** $2x + y = 7$ denklemini sağlayan $x$, $y$ değerlerini bul.

$x$'e bir değer ver, $y$'yi hesapla:

| $x$ | $0$ | $1$ | $2$ | $3$ | $2{,}5$ | $4$ |
|---|---|---|---|---|---|---|
| $y = 7 - 2x$ | $7$ | $5$ | $3$ | $1$ | $2$ | $-1$ |

Her satır bir çözüm verir: $(0, 7)$, $(1, 5)$, $(2, 3)$… Bu denklemin **sonsuz sayıda** çözümü vardır. Hepsini koordinat düzleminde işaretlersen aynı doğru üzerinde dizilirler.

![Koordinat düzleminde 2x + y = 7 doğrusu. Üzerinde (0, 7), (1, 5), (2, 3), (3, 1) yeşil; (2,5; 2) ve (4, −1) kahverengi noktalar.](gorsel/tyt-matematik/03-04-dogru-cozumler.svg "Denklemi sağlayan her (x, y) ikilisi bu doğrunun bir noktasıdır. Yeşil olanlar x ve y'nin doğal sayı olduğu dört çözüm.")

**Kural.** $a \ne 0$, $b \ne 0$ ve $a, b, c \in \mathbb{R}$ olmak üzere $ax + by = c$ biçimindeki denkleme **birinci dereceden iki bilinmeyenli denklem** denir. Denklemi sağlayan her $(x, y)$ **sıralı ikilisi** çözüm kümesinin bir elemanıdır. Çözümlerin grafiği bir **doğrudur**.

**Doğal sayı çözümleri.** Soru "$x$ ve $y$ doğal sayı" derse çözüm sayısı sınırlıdır. $2x + y = 7$ için $y = 7 - 2x \ge 0$ olmalı: $x = 0, 1, 2, 3$. **4 çözüm** var. "Pozitif tam sayı" denseydi $x = 0$ gider ($x = 1, 2, 3$ kalır): **3 çözüm**.

## Denklem sistemi

Aynı iki bilinmeyeni içeren iki denklem birlikte verilirse buna **denklem sistemi** denir:

$$\begin{cases} a x + b y = m \\ c x + d y = n \end{cases}$$

Sistemin çözümü, **iki denklemi birden** sağlayan $(x, y)$ ikilisidir. Grafikte bu, iki doğrunun **kesim noktasıdır**. Çözmek için iki yol var: yok etme ve yerine koyma.

## Yok etme yöntemi

**Örnek 1.** $\begin{cases} 3x + 2y = 16 \\ 5x - 2y = 16 \end{cases}$

$y$'nin katsayıları $+2$ ve $-2$: zaten zıt. Taraf tarafa topla, $y$ yok olur:

$$8x = 32 \;\Rightarrow\; x = 4$$

Birinci denklemde yerine yaz: $12 + 2y = 16$, $y = 2$. Çözüm $(4, 2)$. **Sağlama:** $5 \cdot 4 - 2 \cdot 2 = 16$.

**Örnek 2.** $\begin{cases} 3x + 4y = 18 \\ 2x - 3y = -5 \end{cases}$

Katsayılar zıt değil. $y$'yi yok etmek için birinci denklemi $3$ ile, ikinciyi $4$ ile çarp:

$$\begin{cases} 9x + 12y = 54 \\ 8x - 12y = -20 \end{cases} \;\Rightarrow\; 17x = 34 \;\Rightarrow\; x = 2$$

$3 \cdot 2 + 4y = 18$ için $4y = 12$, $y = 3$. Çözüm $(2, 3)$. **Sağlama:** $2 \cdot 2 - 3 \cdot 3 = -5$.

**Kural.** Bir bilinmeyenin iki denklemdeki katsayılarını **mutlak değerce eşit, işaretçe zıt** yap; sonra taraf tarafa topla. Çarparken denklemin **bütün terimlerini**, sağ taraf dahil, çarp.

## Yerine koyma yöntemi

**Örnek.** $\begin{cases} y = 2x - 3 \\ 4x + 3y = 21 \end{cases}$

$y$ zaten yalnız. İkinci denklemde $y$ yerine $2x - 3$ yaz, **parantez kullanarak**:

$$4x + 3(2x - 3) = 21 \;\Rightarrow\; 4x + 6x - 9 = 21 \;\Rightarrow\; 10x = 30 \;\Rightarrow\; x = 3$$

$y = 2 \cdot 3 - 3 = 3$. Çözüm $(3, 3)$.

**Kural.** Denklemlerden birinde bir bilinmeyen yalnızsa (ya da katsayısı $1$ ise kolayca yalnız bırakılabiliyorsa) onu öbür denklemde yerine yaz. Tek bilinmeyenli bir denklem kalır.

Hangi yolu seçeceğine şöyle karar ver:

![Karar şeması: Bir bilinmeyen yalnız mı? Evet ise yerine koy. Hayır ise katsayılar zıt mı? Evet ise taraf tarafa topla; hayır ise önce uygun sayılarla çarp, sonra topla. En sonda diğer bilinmeyeni bul ve sağla.](gorsel/tyt-matematik/03-04-yontem.svg "İki yöntem de aynı sonucu verir; şema yalnızca hangisinin daha kısa olduğunu gösterir.")

## Kısa yol: $x + y$ sorulursa

**Örnek.** $\begin{cases} 3x + 5y = 21 \\ 5x + 3y = 19 \end{cases}$ ise $x + y$ kaçtır?

Katsayılar çapraz yer değiştirmiş. İki denklemi taraf tarafa **topla**:

$$8x + 8y = 40 \;\Rightarrow\; x + y = 5$$

$x$ ile $y$'yi ayrı ayrı bulmana gerek kalmadı. İstersen **çıkar**: $-2x + 2y = 2$, yani $y - x = 1$. İkisinden $x = 2$, $y = 3$.

**Kural.** Soru $x$ ya da $y$'yi değil bir ifadeyi ($x + y$, $x - y$) soruyorsa önce denklemleri toplamayı ve çıkarmayı dene.

## Grafik yorumu: kaç çözüm var?

İki denklemin her biri bir doğrudur. İki doğru ya bir noktada kesişir, ya paraleldir, ya da çakışıktır.

![Üç grafik alt alta. Birincide x + y = 5 ve x − y = 1 doğruları (3, 2) noktasında kesişiyor. İkincide x + 2y = 4 ve 2x + 4y = 12 paralel. Üçüncüde x + 2y = 4 ve 2x + 4y = 8 üst üste.](gorsel/tyt-matematik/03-04-uc-durum.svg "Ortak nokta sayısı = çözüm sayısı. Paralel doğruların ortak noktası yok; çakışık doğruların her noktası ortak.")

Karar katsayıların oranından verilir. $\begin{cases} ax + by = c \\ dx + ey = f \end{cases}$ sisteminde (sabitler iki denklemde de **aynı tarafta**):

| Oranlar | Doğrular | Çözüm kümesi |
|---|---|---|
| $\dfrac{a}{d} \ne \dfrac{b}{e}$ | Tek noktada kesişir | Tek elemanlı |
| $\dfrac{a}{d} = \dfrac{b}{e} \ne \dfrac{c}{f}$ | Paralel | Boş küme |
| $\dfrac{a}{d} = \dfrac{b}{e} = \dfrac{c}{f}$ | Çakışık | Sonsuz elemanlı |

**Örnek.** $\begin{cases} 3x + ay = 6 \\ 6x + 8y = b \end{cases}$ sistemi sonsuz çözümlü ise $a$ ve $b$ kaçtır?

Üç oran eşit olmalı: $\dfrac{3}{6} = \dfrac{a}{8} = \dfrac{6}{b}$. $\dfrac{1}{2} = \dfrac{a}{8}$ için $a = 4$; $\dfrac{1}{2} = \dfrac{6}{b}$ için $b = 12$.

- Çözüm kümesi **boş** olsaydı: $a = 4$ ve $b \ne 12$.
- **Tek çözüm** olsaydı: $a \ne 4$ ($b$ ne olursa olsun).

## ÖSYM tuzakları

> **Oranı yanlış kurmak:** $2x - 3y = 4$ ile $ax + 9y = b$ için $\frac{2}{a} = \frac{-3}{9}$ olur, eksiyi atarsan $a = 6$ bulursun; doğrusu $a = -6$. Katsayıyı işaretiyle al. Sabitlerden biri sol tarafa geçirilmişse önce ikisini aynı tarafa topla.

> **Paralel için yalnızca iki oranı kontrol etmek:** $\frac{a}{d} = \frac{b}{e}$ olması tek başına "çözüm yok" demek değildir; üçüncü oran da eşitse doğrular çakışıktır ve sonsuz çözüm vardır.

> **Çarparken sağ tarafı unutmak:** $3x + 4y = 18$ denklemini $3$ ile çarpınca $9x + 12y = 54$ olur, $9x + 12y = 18$ değil.

> **Doğal sayı ile pozitif tam sayıyı karıştırmak:** Doğal sayılarda $0$ vardır. "Her üründen en az bir tane" ifadesi $0$'ı dışarıda bırakır, çözüm sayısı azalır.

## Kendini dene

### Soru 1
$\begin{cases} 2x + 3y = 12 \\ 4x - 3y = 6 \end{cases}$ olduğuna göre $x \cdot y$ çarpımı kaçtır?

A) 1
B) 5
C) 6
D) 8
E) 9

**Cevap:** C
**Çözüm:** $y$'nin katsayıları zıt; taraf tarafa topla: $6x = 18$, $x = 3$. Birinci denklemde yerine yaz: $6 + 3y = 12$, $y = 2$. $x \cdot y = 6$. Sağlama: $4 \cdot 3 - 3 \cdot 2 = 6$. $x + y = 5$ değeri B seçeneğindedir.

### Soru 2
$\begin{cases} 2x - 3y = 4 \\ ax + 9y = b \end{cases}$ denklem sisteminin çözüm kümesi sonsuz elemanlı olduğuna göre $a + b$ toplamı kaçtır?

A) $-18$
B) $-10$
C) $-2$
D) $6$
E) $18$

**Cevap:** A
**Çözüm:** Çakışık doğrular için $\frac{2}{a} = \frac{-3}{9} = \frac{4}{b}$. $\frac{-3}{9} = -\frac{1}{3}$ olduğundan $a = -6$ ve $b = -12$. $a + b = -18$. Eksiyi atan $a = 6$, $b = 12$ bulur ve E'yi işaretler.

### Soru 3
Bir otoparkta yalnızca otomobil ve motosiklet vardır. Toplam araç sayısı 30, toplam tekerlek sayısı 100'dür. Otoparkta kaç motosiklet vardır?

A) 5
B) 10
C) 15
D) 20
E) 25

**Cevap:** B
**Çözüm:** Otomobil sayısı $x$, motosiklet sayısı $y$ olsun: $x + y = 30$ ve $4x + 2y = 100$. İlk denklemi $2$ ile çarpıp ikinciden çıkar: $2x = 40$, $x = 20$. O halde $y = 10$. Sağlama: $4 \cdot 20 + 2 \cdot 10 = 100$. $20$ otomobil sayısıdır.

## Özet kartı

- $ax + by = c$ denkleminin sonsuz çözümü vardır; çözümler bir doğru oluşturur.
- Sistemin çözümü iki denklemi birden sağlayan $(x, y)$, yani iki doğrunun kesim noktasıdır.
- Yok etme: bir bilinmeyenin katsayılarını zıt yap, taraf tarafa topla. Yerine koyma: yalnız bilinmeyeni öbür denkleme yaz.
- $x + y$ sorulursa önce denklemleri toplamayı ya da çıkarmayı dene.
- $\frac{a}{d} \ne \frac{b}{e}$: tek çözüm. $\frac{a}{d} = \frac{b}{e} \ne \frac{c}{f}$: boş küme. Üçü eşit: sonsuz çözüm.
- Doğal sayı çözümlerini sayarken $0$'ı unutma; "en az bir" denirse $0$'ı çıkar.

## Sonraki adım

Alıştırmaya geç (aşağıdaki düğme). Sonraki ders **Birinci Dereceden İki Bilinmeyenli Eşitsizlikler**; burada çizdiğin doğrular orada düzlemi iki bölgeye ayıracak.
