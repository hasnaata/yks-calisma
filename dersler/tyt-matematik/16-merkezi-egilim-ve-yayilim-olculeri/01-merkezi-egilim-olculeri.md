---
baslik: Merkezi Eğilim Ölçüleri
ders: tyt-matematik
sure: 20 dk
kaynak: MEBİ Konu Özeti e0e804535c
guncelleme: 2026-11-17
---
# Merkezi Eğilim Ölçüleri

**Bu dersin sonunda:** bir veri grubunun aritmetik ortalamasını, ortancasını ve tepe değerini liste, tablo ya da sütun grafiğinden bulabilecek; bir veri eklenince, çıkarılınca ya da değişince bu ölçülerin nasıl değiştiğini hesaplayabileceksin.

> **TYT'de yeri:** "Bir kişi gruba katılınca ortalama kaç olur?", "yanlış yazılan not düzeltilince ortalama ne olur?", "grafikteki verilerin ortancası kaçtır?" ve "ortalama, ortanca ve tepe değerin sıralaması nedir?" kalıpları gelir. İşlem az, dikkat çoktur: sıralamayı unutmak ve toplamı bulmadan ortalamayla işlem yapmak en sık hatadır.

## Önce hatırla

<details><summary>Karmaşık sayılardan: $i^{2027}$ kaçtır?</summary>
Üssü $4$'e böl: $2027 = 4 \cdot 506 + 3$, kalan $3$. Kalan $3$ ise $i^3 = -i$. Sonuç: <b>$-i$</b>.
</details>

<details><summary>Karmaşık sayılardan: $x^2 + 2x + 10 = 0$ denkleminin kökleri nelerdir?</summary>
$\Delta = 2^2 - 4 \cdot 1 \cdot 10 = -36$, $\sqrt{-36} = 6i$. $x = \dfrac{-2 \pm 6i}{2} = -1 \pm 3i$. Kökler eşleniktir: <b>$-1 - 3i$ ve $-1 + 3i$</b>.
</details>

## Veri

Gözlem, deney ya da araştırmayla toplanan ve bir sonuca ulaşmak için kullanılan her bilgiye **veri** denir.

| Veri türü | Ne demek? | Örnek |
|---|---|---|
| Kesikli veri | Bir aralıktaki her değeri alamaz, sayılarak bulunur | Kardeş sayısı, sınıftaki öğrenci sayısı |
| Sürekli veri | Bir aralıktaki her gerçek sayı değerini alabilir, ölçülerek bulunur | Boy, kütle, sıcaklık, süre |

Bir veri grubunu tek bir sayıyla özetlemek için **merkezi eğilim ölçüleri** kullanılır: aritmetik ortalama, ortanca ve tepe değer. Grubun **en küçük değeri** ve **en büyük değeri** de verinin nerede başlayıp nerede bittiğini söyler.

## Aritmetik ortalama

**Örnek.** Bir öğrencinin beş deneme netleri: $70, 85, 60, 90, 75$. Ortalaması kaçtır?

Toplam: $70 + 85 + 60 + 90 + 75 = 380$. Veri sayısı $5$. Ortalama $\dfrac{380}{5} = 76$.

**Kural.**

$$\overline{x} = \frac{\text{verilerin toplamı}}{\text{veri sayısı}} = \frac{x_1 + x_2 + \dots + x_n}{n} \qquad\Longrightarrow\qquad \text{toplam} = n \cdot \overline{x}$$

İkinci eşitlik, ortalama sorularının anahtarıdır: ortalama verilince önce **toplamı** bul.

**Örnek.** 6 kişilik bir grubun yaş ortalaması 15'tir. Gruba bir kişi katılınca ortalama 16 oluyor. Gelen kişi kaç yaşındadır?

1. Eski toplam: $6 \cdot 15 = 90$.
2. Yeni toplam: $7 \cdot 16 = 112$.
3. Gelen kişi: $112 - 90 = 22$.

"Ortalama 1 arttı, gelen kişi 16 yaşında" demek yanlıştır: gelen kişi kendi yaşını getirir, ayrıca eski 6 kişinin ortalamasını da birer yükseltir: $16 + 6 \cdot 1 = 22$.

**Her veriye aynı işlem.** Yukarıdaki netlerin her birine $5$ eklenirse toplam $5 \cdot 5 = 25$ artar, ortalama $76 + 5 = 81$ olur. Her net $2$ ile çarpılırsa toplam da $2$ katına çıkar, ortalama $2 \cdot 76 = 152$ olur.

**Kural.** Her veri $k$ ile çarpılıp üstüne $m$ eklenirse yeni ortalama $k \cdot \overline{x} + m$ olur. Sıralama bozulmadığı için ($k > 0$) ortanca da aynı biçimde değişir.

## Ortanca (medyan)

**Örnek.** $12, 5, 9, 20, 7, 9, 15$ verilerinin ortancası kaçtır?

Önce **sırala**: $5, 7, 9, 9, 12, 15, 20$. Veri sayısı $n = 7$ tek; tam ortadaki terim $\frac{7 + 1}{2} = 4$. terimdir. Ortanca $9$.

Gruba $30$ eklenirse $n = 8$ çift olur: $5, 7, 9, 9, 12, 15, 20, 30$. Tam ortada tek terim yok; ortadaki iki terim $4.$ ve $5.$ terimlerdir. Ortanca $\dfrac{9 + 12}{2} = 10{,}5$.

![Üstte yedi kutu: 5, 7, 9, 9, 12, 15, 20; dördüncü kutu olan 9 vurgulu. Altta sekiz kutu: 5, 7, 9, 9, 12, 15, 20, 30; dördüncü ve beşinci kutular, 9 ve 12, vurgulu.](gorsel/tyt-matematik/16-01-ortanca.svg "Önce sırala, sonra ortaya bak. Tek sayıda veride ortada bir kutu, çift sayıda veride iki kutu kalır; ikisinin ortalaması alınır.")

**Kural.** Veriler küçükten büyüğe (ya da büyükten küçüğe) sıralanır.

| $n$ | Ortanca |
|---|---|
| Tek | $\left(\dfrac{n + 1}{2}\right)$. terim |
| Çift | $\left(\dfrac{n}{2}\right)$. terim ile $\left(\dfrac{n}{2} + 1\right)$. terimin ortalaması |

Her veri grubunun **tek bir** ortancası vardır. Çift sayıda veride ortanca, verilerden biri olmayabilir ($10{,}5$ gibi).

## Tepe değer (mod)

**Örnek.** $12, 5, 9, 20, 7, 9, 15$ verilerinde $9$ iki kez, diğerleri birer kez geçiyor. Tepe değer $9$'dur.

- $2, 3, 3, 5, 5, 8$ verilerinde $3$ ve $5$ ikişer kez geçer; **iki tepe değer** vardır: $3$ ve $5$.
- $4, 6, 7, 10$ verilerinde her sayı bir kez geçer; öne çıkan bir değer yoktur, tepe değerden söz edilmez.

**Kural.** En çok tekrar eden veri **tepe değerdir**. Bir grubun birden fazla tepe değeri olabilir. Tepe değer bir **veridir**, kaç kez tekrar ettiği (sıklığı) değil.

## Tablo ve grafikten okumak

**Örnek.** Bir sınıftaki 20 öğrencinin kardeş sayıları aşağıdaki grafikte verilmiştir. Ortalama, ortanca ve tepe değeri bul.

![Sütun grafiği: yatay eksende kardeş sayısı 0'dan 4'e, dikey eksende öğrenci sayısı. Sütun yükseklikleri sırasıyla 3, 8, 6, 2, 1; en yüksek sütun 1 kardeşe ait.](gorsel/tyt-matematik/16-01-sutun-grafigi.svg "Yatay eksendeki sayılar veridir, sütunların boyu o verinin kaç kez geçtiğidir. Tepe değer en uzun sütunun altındaki sayıdır: 8 değil, 1.")

- **Tepe değer:** en uzun sütun 1 kardeşe ait. Tepe değer $1$ (8 değil).
- **Ortalama:** her değeri kaç kez geçtiğiyle çarp, topla, öğrenci sayısına böl:
  $$\overline{x} = \frac{0 \cdot 3 + 1 \cdot 8 + 2 \cdot 6 + 3 \cdot 2 + 4 \cdot 1}{20} = \frac{30}{20} = 1{,}5$$
- **Ortanca:** $n = 20$ çift; $10.$ ve $11.$ terimlere bakılır. Sıralı dizide 1.–3. terimler $0$, 4.–11. terimler $1$'dir. İki terim de $1$, ortanca $1$.

**Kural.** Tablo ya da grafikte veri sayısı **sıklıkların toplamıdır** ($3 + 8 + 6 + 2 + 1 = 20$). Ortanca için sıklıkları soldan biriktirerek say; ortalama için her değeri sıklığıyla çarp.

## Uç değerin etkisi

**Örnek.** Küçük bir işyerinde 5 kişinin aylık maaşı (bin TL): $20, 22, 24, 25, 109$. Ortanca $24$'tür. Ortalama ise $\dfrac{200}{5} = 40$; beş kişiden dördü bu "ortalamanın" çok altında kazanıyor.

![Sayı doğrusu 20'den 110'a. 20, 22, 24 ve 25'te dört boş daire yan yana, 109'da kırmızı dolu daire, yanında uç değer yazısı. Altta yeşil üçgen 24'te ortanca, mavi üçgen 40'ta ortalama.](gorsel/tyt-matematik/16-01-uc-deger.svg "Tek bir büyük maaş ortalamayı 40'a çekiyor; ortanca 24'te kalıyor. Uç değer varsa grubu ortanca daha iyi anlatır.")

**Kural.** Aritmetik ortalama bütün verileri kullanır, bu yüzden **uç değerlerden çok etkilenir**. Ortanca ve tepe değer uç değerlerden daha az etkilenir: en büyük veri $109$ yerine $200$ olsaydı ortanca yine $24$ kalırdı.

## ÖSYM tuzakları

> **Sıralamadan ortanca almak:** $4, 9, 2, 8$ verilerinde yazıldığı sıradaki orta iki terim $9$ ve $2$'dir ($5{,}5$ bulunur). Sıralayınca $2, 4, 8, 9$ olur; ortanca $\frac{4 + 8}{2} = 6$. Her zaman önce sırala.

> **Konum ile değeri karıştırmak:** $\frac{n + 1}{2}$ ortancanın **kaçıncı terim** olduğunu verir, ortancanın kendisini değil. $n = 7$ için ortanca $4$ değil, $4.$ terimdir.

> **Ortalamayla doğrudan işlem:** "Ortalama 15'ten 16'ya çıktı, gelen kişi 16 yaşında" yanlıştır. Ortalamalar toplanmaz, çıkarılmaz; önce toplamlara geç ($n \cdot \overline{x}$).

> **İki grubun ortalaması:** 12 kişinin ortalaması 70, 8 kişinin ortalaması 85 ise 20 kişinin ortalaması $\frac{70 + 85}{2}$ değildir. Doğrusu $\frac{12 \cdot 70 + 8 \cdot 85}{20} = 76$; kalabalık grup sonucu kendine çeker.

> **Grafikte sıklığı veri sanmak:** Tepe değer en uzun sütunun **altındaki** sayıdır, sütunun boyu değil.

## Kendini dene

### Soru 1
$4, 9, 2, 8, 9, 5$ verilerinin ortancası kaçtır?

A) 5
B) 6
C) 6,5
D) 8
E) 9

**Cevap:** C
**Çözüm:** Sırala: $2, 4, 5, 8, 9, 9$. $n = 6$ çift; $3.$ ve $4.$ terimler $5$ ve $8$. Ortanca $\frac{5 + 8}{2} = 6{,}5$. Sıralamadan ortadaki $2$ ve $8$'i alan $5$ bulur; $9$ tepe değerdir.

### Soru 2
8 sayının aritmetik ortalaması 12'dir. Bu sayılardan biri çıkarılınca kalan sayıların aritmetik ortalaması 11 oluyor.

Buna göre çıkarılan sayı kaçtır?

A) 1
B) 11
C) 12
D) 15
E) 19

**Cevap:** E
**Çözüm:** İlk toplam $8 \cdot 12 = 96$. Kalan 7 sayının toplamı $7 \cdot 11 = 77$. Çıkarılan sayı $96 - 77 = 19$. Ortalamaların farkını alan $12 - 11 = 1$ bulur.

### Soru 3
Bir mağazada bir günde satılan 20 ayakkabının numaraları aşağıdaki tabloda verilmiştir.

| Numara | 38 | 39 | 40 | 41 | 42 |
|---|---|---|---|---|---|
| Satılan çift | 4 | 7 | 5 | 3 | 1 |

Buna göre satılan ayakkabı numaralarının ortancası kaçtır?

A) 38
B) 39
C) 39,5
D) 40
E) 41

**Cevap:** B
**Çözüm:** $n = 20$ çift; $10.$ ve $11.$ terimlere bakılır. Sıklıkları biriktir: 1.–4. terimler $38$, 5.–11. terimler $39$. İki terim de $39$, ortanca $39$. Tablodaki beş numaranın ortasındaki $40$'ı seçmek, sıklıkları hesaba katmamaktır.

## Özet kartı

- Ortalama $= \dfrac{\text{toplam}}{n}$; sorularda önce toplamı bul: toplam $= n \cdot \overline{x}$.
- Her veri $k$ ile çarpılıp $m$ eklenirse ortalama da ortanca da $k \cdot (\ldots) + m$ olur ($k > 0$).
- Ortanca: önce sırala. $n$ tekse $\frac{n + 1}{2}$. terim; $n$ çiftse $\frac{n}{2}$. ve $\left(\frac{n}{2} + 1\right)$. terimlerin ortalaması.
- Tepe değer en çok tekrar eden veridir; birden fazla olabilir.
- Tablo ve grafikte $n$ = sıklıkların toplamı; ortalama için değer $\times$ sıklık.
- Uç değer ortalamayı çeker; ortanca ve tepe değer daha az etkilenir.

## Sonraki adım

Alıştırmaya geç (aşağıdaki düğme). Sonraki ders **Merkezi Yayılım Ölçüleri**; orada bu dersteki en küçük ve en büyük değeri, ortalamayı ve ortancayı kullanarak verilerin ne kadar dağınık olduğunu ölçeceksin.
