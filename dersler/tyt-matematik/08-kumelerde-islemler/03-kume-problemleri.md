---
baslik: Küme Problemleri
ders: tyt-matematik
sure: 20 dk
kaynak: MEBİ Konu Özeti 828737039b
guncelleme: 2026-11-17
---
# Küme Problemleri

**Bu dersin sonunda:** bir günlük hayat problemini Venn şemasına ya da tabloya döküp "en az biri", "en çok biri", "yalnız biri", "hiçbiri" gibi ifadelerin hangi bölgeleri anlattığını bilerek istenen sayıyı bulabileceksin.

> **TYT'de yeri:** Her yıl en az bir küme problemi gelir. Kalıplar: "iki etkinlikten hiçbirine katılmayan kaç kişi?", bölgelerin bilinmeyenle verildiği Venn şeması, "en az kaç kişi ikisini birden yapar?" ve kız/erkek gibi iki gruplu bir tablodan "veya" ile sorulan sayı.

## Önce hatırla

<details><summary>Fark işleminden: $s(A) = 12$ ve $s(A \cap B) = 5$ ise $s(A \setminus B)$ kaçtır?</summary>
$A \setminus B$, $A$'da olup $B$'de olmayanlardır; yani $A$'dan ortak bölge çıkar: $12 - 5 = $ <b>7</b>.
</details>

<details><summary>Tümlemeden: $s(E) = 30$ ve $s(A') = 12$ ise $s(A)$ kaçtır?</summary>
$A$ ile $A'$ ayrıktır ve birleşimleri $E$'dir: $s(A) + s(A') = s(E)$. Buradan $s(A) = 30 - 12 = $ <b>18</b>.
</details>

## Dört bölge, dört sayı

**Örnek.** 40 kişilik bir sınıfta 22 öğrenci futbol, 15 öğrenci voleybol oynuyor; 7 öğrenci ikisini de oynuyor.

Önce **ortak bölgeyi** yaz: $b = 7$. Sonra "yalnız" bölgeleri çıkararak doldur:

- Yalnız futbol: $a = 22 - 7 = 15$
- Yalnız voleybol: $c = 15 - 7 = 8$
- En az birini oynayan: $a + b + c = 15 + 7 + 8 = 30$
- Hiçbirini oynamayan: $d = 40 - 30 = 10$

![Dikdörtgen içinde kesişen iki elips. Sol elipsin yalnız kısmında a, ortak kısımda b, sağ elipsin yalnız kısmında c, dikdörtgenin elips dışı köşesinde d yazıyor.](gorsel/tyt-matematik/08-03-bolgeler.svg "Bütün grup E dikdörtgenidir. Her kişi bu dört bölgeden tam birindedir: a + b + c + d = s(E).")

Bu dört sayıyla her soru cevaplanır. Sınıf örneğiyle:

| Soruda geçen ifade | Bölgeler | Sınıf örneği |
|---|---|---|
| Futbol oynayan | $a + b$ | $22$ |
| Yalnız futbol oynayan | $a$ | $15$ |
| İkisini de oynayan | $b$ | $7$ |
| Yalnız birini oynayan | $a + c$ | $23$ |
| En az birini oynayan | $a + b + c$ | $30$ |
| Hiçbirini oynamayan | $d$ | $10$ |
| En çok birini oynayan | $a + c + d$ | $33$ |
| Futbol oynamayan | $c + d$ | $18$ |
| Voleybol oynamayan | $a + d$ | $25$ |

**Kural.** Önce ortak bölge, sonra yalnız bölgeler, en son dışarıdaki bölge. Toplam her zaman $a + b + c + d$'dir. "Futbol oynamayan" bir **tümleyendir**: futbolun dışındaki iki bölge, $c + d$.

## "En az biri" ile "en çok biri"

İki ifade birbirine benzer ama farklı bölgeleri anlatır:

- **En az biri** = 1 ya da 2 sporu yapan = $a + b + c$ = toplam − hiçbiri.
- **En çok biri** = 0 ya da 1 sporu yapan = $a + c + d$ = toplam − ikisi de.

![Yan yana iki Venn şeması. Solda, başlığı en az biri olan şemada iki elipsin tamamı boyalı, altında a artı b artı c. Sağda, başlığı en çok biri olan şemada ortak bölge dışındaki her yer boyalı, altında a artı c artı d.](gorsel/tyt-matematik/08-03-en-az-en-cok.svg "En az biri: iki elipsin tamamı. En çok biri: ortak bölge hariç her yer, dışarıdaki d dahil.")

**Kural.** "En çok biri" sorulduğunda hiçbirini yapmayanları (d) da say. En kısa yol: en çok biri $=$ toplam $-$ ikisini birden yapanlar. Sınıfta $40 - 7 = 33$.

## Bölgelerde bilinmeyen

**Örnek.** Bir grupta İngilizce bilenlerin sayısı Almanca bilenlerin sayısının 2 katıdır. İki dili de bilen 6, yalnız İngilizce bilen 20 kişi vardır. Yalnız Almanca bilen kaç kişidir?

1. İngilizce bilen: $20 + 6 = 26$.
2. "2 katı" bilgisi **toplamlar** için verildi: Almanca bilen $26 : 2 = 13$.
3. Yalnız Almanca: $13 - 6 = 7$.

Kontrol: en az bir dili bilen $20 + 6 + 7 = 33$ kişi.

**Kural.** Bilinmeyeni çoğu zaman ortak bölgeye ya da en küçük bölgeye ver, diğer bölgeleri onunla yaz, sonra toplamı eşitle. Oran ya da kat bilgisinin bütün kümeye mi, yalnız bölgeye mi ait olduğunu kökten oku.

## En az kaç kişi ikisini birden yapar?

**Örnek.** 30 kişilik bir sınıfta 18 kişi çay, 20 kişi kahve seviyor. İkisini de seven en az kaç, en çok kaç kişidir?

İkisini de sevenler $b$ olsun. En az birini sevenler $18 + 20 - b = 38 - b$ kişidir ve bu sayı sınıfı aşamaz:

$$38 - b \le 30 \quad \Rightarrow \quad b \ge 8$$

En çok durumda çay sevenlerin hepsi kahve de sever: $b \le 18$. Yani $8 \le b \le 18$.

Hiçbirini sevmeyenler $d = 30 - (38 - b) = b - 8$ olur. $b$ en küçükken $d = 0$, $b$ en büyükken $d = 10$.

**Kural.** $s(A) + s(B) > s(E)$ ise iki kümede birden en az $s(A) + s(B) - s(E)$ eleman vardır. Ortak eleman en çok küçük kümenin eleman sayısı kadardır. Ortak bölge büyüdükçe dışarıda kalanlar da artar.

## Tablo yöntemi

Bazı problemlerde kişiler iki ayrı yoldan gruplanır ve her gruplamada **tam bir** seçenektedir: herkes ya kız ya erkektir, ya sabah ya akşam grubundadır. "Kız" ile "erkek" kümelerinin kesişimi boştur. Bu durumda Venn şeması yerine **tablo** kurulur.

![Akış şeması: Problemi oku, sonra ortak eleman olabilir mi sorusu. Evet ise Venn şeması çiz, ortak bölgeden başla, bölgeleri doldur ve toplamı eşitle. Hayır ise tablo çiz, satır ve sütun toplamlarını kullan.](gorsel/tyt-matematik/08-03-yontem.svg "Bir kişi iki özelliğe birden sahip olabiliyorsa Venn, iki seçenekten yalnız birinde olabiliyorsa tablo.")

**Örnek.** Bir kursta 48 kursiyer var; her biri ya sabah ya akşam grubunda. Kursiyerlerin 26'sı kızdır. Sabah grubunda 9 erkek vardır. Akşam grubundaki kız sayısı, sabah grubundaki kız sayısının 2 katından 1 eksiktir. Akşam grubunda kaç kursiyer vardır?

1. Sabah grubundaki kızlar $x$ olsun; akşam grubundaki kızlar $2x - 1$.
2. Kız satırı: $x + 2x - 1 = 26$, yani $3x = 27$, $x = 9$. Akşam kız: $17$.
3. Erkek satırı: $48 - 26 = 22$ erkek; akşam erkek $22 - 9 = 13$.
4. Akşam sütunu: $17 + 13 = $ **30**.

![İki satır iki sütunlu tablo ve toplamları. Kız satırı sabah 9, akşam 17, toplam 26. Erkek satırı sabah 9, akşam 13, toplam 22. Toplam satırı 18, 30, 48. Akşam erkek hücresi kırmızı, diğer üç iç hücre yeşil.](gorsel/tyt-matematik/08-03-tablo.svg "Kız veya sabah grubunda olanlar yeşil hücrelerdir. Dışarıda kalan tek hücre akşam grubundaki erkekler (kırmızı).")

Aynı tabloda "kız **veya** sabah grubunda olan" kaç kişi? Kızlar (26) ile sabah grubunu (18) toplayınca sabah grubundaki 9 kız iki kez sayılır: $26 + 18 - 9 = 35$. Daha kısası, koşula uymayan tek hücreyi toplamdan çıkar: $48 - 13 = 35$.

**Kural.** Tabloda her satır ve her sütun bir toplam verir; bilinmeyeni bir hücreye ver, eksik hücreleri satır ve sütun toplamlarından bul. "Veya" sorulursa koşulu sağlamayan hücreyi toplamdan çıkar; "ve" sorulursa tek hücreyi oku.

## ÖSYM tuzakları

> **"En çok biri"nde hiçbiri bölgesini unutmak:** En çok bir sporu yapanlar $a + c$ değil $a + c + d$'dir. Sıfır spor da "en çok bir"dir.

> **Ortak bölgeyi iki kez saymak:** "Futbol oynayan 22, voleybol oynayan 15" ise en az birini oynayan $37$ değildir; ikisini birden oynayanlar çıkarılır.

> **Katı yanlış bölgeye uygulamak:** "İngilizce bilenler Almanca bilenlerin 2 katı" bütün kümeler içindir; yalnız bölgeler arasında kurulmaz.

> **"Yapmayan" ile "hiçbirini yapmayan"ı karıştırmak:** Futbol oynamayanlar $c + d$'dir; içinde yalnız voleybol oynayanlar da var. Hiçbirini oynamayanlar yalnızca $d$'dir.

> **Tabloda "veya"yı toplamak:** Kızlar ile sabah grubunu doğrudan toplamak sabah grubundaki kızları iki kez sayar.

## Kendini dene

### Soru 1
50 kişilik bir grupta 28 kişi kitap, 19 kişi dergi okuyor; 9 kişi ikisini de okuyor. Bu grupta ne kitap ne dergi okuyan kaç kişi vardır?

A) 3
B) 9
C) 12
D) 22
E) 31

**Cevap:** C
**Çözüm:** En az birini okuyan: $28 + 19 - 9 = 38$. Hiçbirini okumayan: $50 - 38 = 12$. 3, ortak bölgeyi çıkarmadan $50 - 28 - 19$ işleminden; 22 ve 31 yalnız bir kümeyi toplamdan çıkarmaktan gelir.

### Soru 2
35 kişilik bir sınıfta 14 öğrenci satranç, 17 öğrenci yüzme kursuna gidiyor; 6 öğrenci iki kursa da gidiyor. Bu kurslardan en çok birine giden kaç öğrenci vardır?

A) 6
B) 10
C) 19
D) 25
E) 29

**Cevap:** E
**Çözüm:** En çok birine gidenler, iki kursa birden gidenler dışındaki herkestir: $35 - 6 = 29$. Bölgelerle: yalnız satranç $8$, yalnız yüzme $11$, hiçbiri $35 - 25 = 10$; $8 + 11 + 10 = 29$. 19 yalnız birine gidenlerdir; hiçbirine gitmeyen 10 kişiyi unutan 19 bulur.

### Soru 3
Bir otobüsteki 40 yolcunun her biri ya öğrenci ya yetişkindir. Yolcuların 22'si kadındır. Öğrenci olan erkek yolcu sayısı 8, yetişkin kadın yolcu sayısı 15'tir. Bu otobüste öğrenci veya kadın olan kaç yolcu vardır?

A) 10
B) 15
C) 22
D) 30
E) 37

**Cevap:** D
**Çözüm:** Erkek yolcu $40 - 22 = 18$; yetişkin erkek $18 - 8 = 10$. Öğrenci veya kadın olmayan tek hücre yetişkin erkeklerdir: $40 - 10 = 30$. Öğrenci kadın $22 - 15 = 7$, öğrenci $8 + 7 = 15$; $15 + 22 = 37$ öğrenci kadınları iki kez sayar.

## Özet kartı

- İki kümeli problemde dört bölge vardır: yalnız A ($a$), ikisi ($b$), yalnız B ($c$), hiçbiri ($d$); toplam $a + b + c + d$.
- Doldurma sırası: ortak bölge → yalnız bölgeler → dışarısı.
- En az biri $= a + b + c$ = toplam − hiçbiri. En çok biri $= a + c + d$ = toplam − ikisi de.
- İkisini birden yapan en az $s(A) + s(B) - s(E)$, en çok küçük kümenin sayısı kadardır.
- İki seçenekten yalnız birinde olunan gruplamalarda (kız/erkek, sabah/akşam) tablo kur.
- Tabloda "veya" = toplam − koşulu sağlamayan hücre.

## Sonraki adım

Alıştırmaya geç (aşağıdaki düğme). Bu dersle **Kümelerde İşlemler** konusu biter. Sonraki ders **Saymanın Temel İlkesi**; orada da "ve" ile "veya"nın farkı, seçenekleri çarpıp çarpmayacağını ya da toplayacağını belirleyecek.
