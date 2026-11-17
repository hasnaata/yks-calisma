---
baslik: Tekrarlı Permütasyon
ders: tyt-matematik
sure: 25 dk
kaynak: MEBİ Konu Özeti 2d7a05988e
guncelleme: 2026-11-18
---
# Tekrarlı Permütasyon

<div class="giris" dir="rtl" lang="ar">

**الدرس ده عن إيه؟** عن التباديل مع التكرار (tekrarlı permütasyon): إزاي تعدّ الترتيبات لما يكون فيه حاجات متشابهة زي حروف متكررة في كلمة أو كور بنفس اللون.

- هتفهم ليه بنقسم على مضروب (faktöriyel) عدد التكرار، وتطبّق ده على الكلمات والأرقام.
- هتحل الأسئلة اللي فيها شرط: حرف في الأول، حروف جنب بعض، الصفر ميجيش في أول الرقم، أو ناس لازم يقفوا بترتيب معيّن.
- هتعدّ أقصر الطرق (en kısa yol) على شبكة مربعات، وتعرف تتصرف لما تختار جزء بس من الحروف.

**ليه مهم؟** في TYT تقريبًا كل امتحان فيه سؤال عدّ مبني على القاعدة دي، والأشكال بتاعته معروفة وبتتكرر.

الدرس ٢٥ دقيقة، وأغلبه أمثلة محلولة خطوة بخطوة. ابدأ بهدوء، وهتلاقيه أسهل ما انت متخيل.

</div>

**Bu dersin sonunda:** içinde özdeş nesneler bulunan bir dizilişi (tekrarlı harfli kelime, aynı renkli bilyeler, tekrarlı rakamlı sayı, ızgarada en kısa yol) $\frac{n!}{n_1! \cdot n_2! \cdot \ldots}$ ile sayabilecek ve koşullu soruları bu kurala bağlayabileceksin.

> **TYT'de yeri:** Neredeyse her sınavda bir sayma sorusu bu kurala dayanır. Kalıplar bellidir: "KAPAK kelimesinin harfleriyle kaç farklı kelime yazılır?", "rakamların tamamı kullanılarak kaç farklı sayı yazılır?" (0 başa gelemez), "A'dan B'ye en kısa yollar kaç tanedir?", "bu kişiler bu sırayla yer almak koşuluyla…".

## Önce hatırla

<details><summary>Permütasyondan: 6 kişilik bir kulüpte bir başkan ve bir başkan yardımcısı kaç farklı şekilde seçilir?</summary>
Görevler farklı, yani sıra önemli: $P(6, 2) = \frac{6!}{4!} = 6 \cdot 5 = 30$.
</details>

<details><summary>Permütasyondan: 5 kişi bir sıraya, belirli 2 kişi yan yana olmak koşuluyla kaç farklı şekilde dizilir?</summary>
Yan yana olacak 2 kişiyi tek blok say: blok ve diğer 3 kişi, $4! = 24$. Blok içinde 2 kişi yer değiştirir: $2! = 2$. Toplam $24 \cdot 2 = 48$.
</details>

## Özdeş nesneler neden bölünür?

**Örnek.** ADA kelimesinin harfleri yan yana kaç farklı şekilde dizilir?

Önce iki A'yı farklıymış gibi düşün: $A_1$, D, $A_2$. Üç farklı harf $3! = 6$ şekilde dizilir. Ama $A_1 D A_2$ ile $A_2 D A_1$ kâğıtta aynı görünür: ikisi de ADA. Her gerçek diziliş, A'ların kendi aralarında yer değiştirmesi kadar, yani $2! = 2$ kez sayılmıştır.

$$\frac{3!}{2!} = \frac{6}{2} = 3 \quad (\text{ADA, AAD, DAA})$$

![Solda üç kutu, her birinde A1 D A2 ve A2 D A1 gibi A'ların yeri değişmiş iki diziliş; oklar sağdaki tek dizilişe gidiyor: ADA, AAD, DAA. Altta: her diziliş 2 faktöriyel kez sayılmış, 6 bölü 2 eşittir 3.](gorsel/tyt-matematik/09-04-ozdes-gruplama.svg "Her yeşil kutu, mavi kutudaki iki dizilişin birleşmesidir. Özdeşler kendi aralarında yer değiştirince yeni diziliş oluşmaz.")

**Örnek.** KAPAK kelimesinin harfleriyle anlamlı ya da anlamsız 5 harfli kaç farklı kelime yazılır?

Harfleri say: 5 harf; K 2 tane, A 2 tane, P 1 tane. Hepsi farklı olsaydı $5! = 120$ olurdu. K'ların kendi arasındaki $2!$ ve A'ların kendi arasındaki $2!$ yer değişimi yeni kelime vermez:

$$\frac{5!}{2! \cdot 2! \cdot 1!} = \frac{120}{4} = 30$$

**Kural.** $n$ nesnenin $n_1$ tanesi kendi arasında özdeş, $n_2$ tanesi kendi arasında özdeş, …, $n_r$ tanesi kendi arasında özdeş ($n_1 + n_2 + \ldots + n_r = n$) ise farklı dizilişlerin sayısı

$$\frac{n!}{n_1! \cdot n_2! \cdot \ldots \cdot n_r!}$$

"Özdeş", aynı büyüklükte ve aynı özellikte, ayırt edilemeyen demektir: aynı harf, aynı renkteki bilyeler, aynı rakam. Bir kez geçen nesne için $1! = 1$ yazılır, sonucu değiştirmez.

| Dizilecekler | Tekrarlar | Sayı |
|---|---|---|
| ADA | A: 2 | $\frac{3!}{2!} = 3$ |
| KAPAK | K: 2, A: 2 | $\frac{5!}{2! \cdot 2!} = 30$ |
| 4 kırmızı, 2 beyaz, 1 mavi bilye | 4, 2, 1 | $\frac{7!}{4! \cdot 2!} = 105$ |

## Koşullu dizilişler

Koşul varsa **önce koşulu yerine koy**, sonra kalanları aynı kuralla diz.

**Örnek (başta ya da sonda).** KAPAK kelimesinin harfleriyle P ile başlayan kaç kelime yazılır?

P başa sabitlenir. Kalan harfler K, A, A, K: 4 harf, K 2 tane, A 2 tane.

$$\frac{4!}{2! \cdot 2!} = \frac{24}{4} = 6$$

**Örnek (yan yana).** KAPAK kelimesinin harfleriyle A'ların yan yana olduğu kaç kelime yazılır?

İki A'yı tek blok yap: [AA], K, P, K. Dört nesne, K 2 tane: $\frac{4!}{2!} = 12$. Blok içinde iki **özdeş** A yer değiştirince yeni kelime oluşmaz, bu yüzden $2!$ ile çarpılmaz.

"Yan yana **olmayan**" sorulursa tümünden çıkar: $30 - 12 = 18$.

**Örnek (rakamlar ve 0).** 2, 0, 0, 5, 5 rakamlarının tamamı kullanılarak beş basamaklı kaç farklı sayı yazılır?

Önce 0 başa gelebilir gibi say: 5 rakam, 0 iki tane, 5 iki tane: $\frac{5!}{2! \cdot 2!} = 30$.
0 ile başlayanlar beş basamaklı değildir. 0'ı başa koy; kalan 2, 0, 5, 5: $\frac{4!}{2!} = 12$.

$$30 - 12 = 18$$

**Kural.** Rakam sorularında "0 başta olamaz": ya tümünden 0 ile başlayanları çıkar ya da ilk basamağı ayrı ayrı durumlara bölerek say.

## Belirli sırada olma

**Örnek.** 6 farklı kişi bir sıraya dizilecek. Bunlardan Ali, Can ve Ece **bu sırayla** (Ali önde, Ece arkada; aralarında başka kişiler olabilir) yer almak zorunda. Kaç farklı diziliş vardır?

Ali, Can ve Ece'nin oturduğu 3 yer hangisi olursa olsun, bu üç kişi o yerlere yalnızca **bir** şekilde (Ali, Can, Ece sırasıyla) yerleşir. Yani bu üç kişi sayma bakımından özdeş gibidir: üçünün yerine X, X, X yaz, sonra X'leri soldan sağa Ali, Can, Ece diye adlandır.

$$\frac{6!}{3!} = \frac{720}{6} = 120$$

**Kural.** $n$ farklı nesneden $k$ tanesinin kendi arasındaki sırası sabitse diziliş sayısı $\frac{n!}{k!}$'dir.

## Izgarada en kısa yol

**Örnek.** Şekildeki ızgarada yalnızca sağa (S) ve yukarı (Y) ilerleyerek A'dan B'ye kaç farklı en kısa yoldan gidilir?

![4 sütun 3 satırlık kare ızgara; sol alt köşe A, sağ üst köşe B. Mavi oklarla bir yol çizilmiş: sağ, sağ, yukarı, sağ, yukarı, yukarı, sağ. Altında: 4 tane S, 3 tane Y.](gorsel/tyt-matematik/09-04-izgara.svg "Her en kısa yol 4 S ve 3 Y harfinden oluşan bir kelimedir. Yolu saymak, bu harflerin dizilişini saymaktır.")

En kısa yolda geri adım yoktur: her yolda tam 4 kez sağa, 3 kez yukarı gidilir. Her yol, 4 S ve 3 Y harfinden oluşan 7 harfli bir kelimeyle eşleşir (şekildeki yol SSYSYYS). Farklı kelime sayısı:

$$\frac{7!}{4! \cdot 3!} = \frac{5040}{24 \cdot 6} = 35$$

**Kural.** $m$ birim sağa, $k$ birim yukarı giden en kısa yolların sayısı $\frac{(m+k)!}{m! \cdot k!}$'dir. "C noktasından geçerek" denirse A'dan C'ye ve C'den B'ye olan yolları **çarp**; "D'den geçmeden" denirse tümünden D'den geçenleri **çıkar**.

## Harflerin bir kısmını sıralamak

Formül yalnızca **bütün** nesneler dizildiğinde çalışır. Bir kısmı seçiliyorsa, tekrarlı harfin kaç kez kullanıldığına göre durumlara ayır.

**Örnek.** TATLI kelimesinin harflerinden 3 tanesi kullanılarak 3 harfli kaç farklı kelime yazılır?

Harfler: T, T, A, L, I. Tekrar eden yalnızca T.

- **İki T de kullanılırsa:** üçüncü harf A, L, I'dan biri (3 seçenek). Her biri, örneğin T, T, A, $\frac{3!}{2!} = 3$ şekilde dizilir: $3 \cdot 3 = 9$.
- **En çok bir T kullanılırsa:** T, A, L, I farklı harflerinden 3'ü sıralanır: $P(4, 3) = 4 \cdot 3 \cdot 2 = 24$.

Toplam: $9 + 24 = 33$.

![Yöntem şeması: özdeş nesneli sıralama, hepsi kullanılıyor mu sorusuna gidiyor. Evet ise koşulu önce yerleştir, sonra n faktöriyel bölü tekrarların faktöriyeli. Hayır ise tekrara göre durumlara ayır, durumları say ve topla.](gorsel/tyt-matematik/09-04-yontem.svg "Önce bütün nesnelerin dizilip dizilmediğine bak. Bir kısmı seçiliyorsa tek formül yetmez; durumları ayır.")

## ÖSYM tuzakları

> **Bölmeyi unutmak:** KAPAK için $5! = 120$ demek yanlıştır. Her tekrar eden harf için onun tekrar sayısının faktöriyeline böl: $\frac{5!}{2! \cdot 2!} = 30$.

> **Özdeş bloğu kendi içinde çarpmak:** A'lar yan yana denince [AA] bloğu $2!$ ile çarpılmaz; özdeş harfler yer değiştirince kelime değişmez. Blok farklı nesnelerden oluşsaydı çarpılırdı.

> **0 ile başlayan sayıları saymak:** "Beş basamaklı sayı" sorusunda 0 ile başlayanlar sayı değildir. Tümünü bulduktan sonra 0'ı başa koyup kalanları say ve çıkar.

> **Koşulu yerleştirince tekrarı güncellememek:** KAPAK'ta K ile başlayanlar için kalan harfler A, P, A, K'dır; artık tek K kaldı. $\frac{4!}{2! \cdot 2!}$ değil, $\frac{4!}{2!} = 12$.

> **Bir kısmı seçilirken formülü kullanmak:** TATLI'dan 3 harf için $\frac{5!}{2!}$ ya da $\frac{P(5,3)}{2!}$ yazmak yanlıştır. Durumlara ayır.

## Kendini dene

### Soru 1
KARAR kelimesinin harflerinin tamamı kullanılarak anlamlı ya da anlamsız 5 harfli kaç farklı kelime yazılabilir?

A) 10
B) 20
C) 30
D) 60
E) 120

**Cevap:** C
**Çözüm:** 5 harf; A 2 tane, R 2 tane, K 1 tane. $\frac{5!}{2! \cdot 2!} = \frac{120}{4} = 30$. Yalnızca bir $2!$'e bölen $60$, hiç bölmeyen $120$ bulur.

### Soru 2
Bir robot her hamlede ya 1 birim sağa ya da 1 birim yukarı gidebilmektedir. Robot başladığı noktanın 5 birim sağında ve 2 birim yukarısındaki noktaya en kısa yoldan kaç farklı şekilde gidebilir?

A) 7
B) 10
C) 14
D) 21
E) 42

**Cevap:** D
**Çözüm:** Her en kısa yol 5 S ve 2 Y harfinden oluşan 7 harfli bir kelimedir: $\frac{7!}{5! \cdot 2!} = \frac{7 \cdot 6}{2} = 21$. $42$, $2!$'e bölmeyi unutmaktır; $7$, yalnızca toplam adım sayısıdır.

### Soru 3
A, B, C, D, E adlı 5 kişi bir sıraya dizilecektir. A'nın B'den, B'nin de C'den önde olması koşuluyla (aralarında başka kişiler olabilir) kaç farklı diziliş vardır?

A) 10
B) 20
C) 40
D) 60
E) 120

**Cevap:** B
**Çözüm:** A, B, C'nin kendi arasındaki sırası sabit; üçü özdeş gibi sayılır: $\frac{5!}{3!} = \frac{120}{6} = 20$. $60$, $3!$ yerine $2!$'e bölmektir; $120$, koşulu yok saymaktır.

## Özet kartı

- Özdeş nesneler kendi aralarında yer değiştirince yeni diziliş oluşmaz; bu yüzden bölünür.
- $n$ nesne, tekrarlar $n_1, n_2, \ldots$: $\frac{n!}{n_1! \cdot n_2! \cdot \ldots}$
- Koşul varsa önce koşulu yerleştir, kalanların tekrar sayısını yeniden say.
- Rakam sorularında 0 ile başlayanları çıkar.
- Sırası sabit $k$ nesne özdeş gibidir: $\frac{n!}{k!}$. Izgarada en kısa yol: $\frac{(m+k)!}{m! \cdot k!}$.
- Nesnelerin yalnızca bir kısmı seçiliyorsa durumlara ayır ve topla.

## Sonraki adım

Alıştırmaya geç (aşağıdaki düğme). Sonraki ders **Kombinasyon Kavramı ve Özellikleri**; sıranın önemli olmadığı seçmeyi göreceksin. Bu dersteki $\frac{7!}{4! \cdot 3!}$ ifadesi orada "7'nin 3'lü kombinasyonu" adını alacak.
