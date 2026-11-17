---
baslik: Kombinasyon Problemleri
ders: tyt-matematik
sure: 25 dk
kaynak: MEBİ Konu Özeti 4019557f82
guncelleme: 2026-11-17
---
# Kombinasyon Problemleri

**Bu dersin sonunda:** bir seçme problemini "sıra önemli mi, koşul ne?" sorularıyla çözümleyip gruplardan seçme, "en az / en çok", belirli kişi var ya da yok ve seçip dizme sorularını $C(n, r)$ ile çözebileceksin.

> **TYT'de yeri:** Her sınavda bir sayma sorusu gelir ve çoğu bir seçme sorusudur. Kalıplar bellidir: "en az bir kız bulunan kaç farklı ekip", "Ali ile Berk aynı grupta olmamak üzere", "seçilen kitaplar rafa kaç farklı şekilde dizilir". Zorluk formülde değil, durumu doğru kurmaktadır.

## Önce hatırla

<details><summary>Kombinasyon kavramından: $\binom{10}{7}$ kaçtır? Hesabı nasıl kısaltırsın?</summary>
$\binom{n}{r} = \binom{n}{n-r}$ özelliğinden $\binom{10}{7} = \binom{10}{3} = \frac{10 \cdot 9 \cdot 8}{3 \cdot 2 \cdot 1} = 120$. 7 eleman seçmek, dışarıda kalacak 3 elemanı seçmekle aynı şeydir.
</details>

<details><summary>Kombinasyon kavramından: 8 elemanlı bir kümenin 4 elemanlı alt kümelerinin kaçında $a$ bulunur ama $b$ bulunmaz?</summary>
$a$ kesin alınır, $b$ kümeden çıkarılır. Kalan 6 elemandan 3 eleman daha seçilir: $\binom{6}{3} = 20$.
</details>

## Seçme mi, sıralama mı?

**Örnek.** 5 kişilik bir sınıftan 2 kişi seçilecek.

- 2 kişi bir **nöbet ekibi** olacaksa: Ayşe-Can ekibi ile Can-Ayşe ekibi aynıdır. Sıra önemsiz: $\binom{5}{2} = 10$.
- Biri **başkan**, biri **yardımcı** olacaksa: Ayşe başkan-Can yardımcı ile Can başkan-Ayşe yardımcı farklıdır. Sıra önemli: $P(5, 2) = 20$.

**Kural.** Seçilenlerin görevleri, yerleri ya da sıraları birbirinden farklıysa sıra önemlidir (permütasyon). "Ekip, grup, komisyon, takım, alt küme, tokalaşma, maç" gibi sözcükler genellikle sırasız seçmedir (kombinasyon). Emin değilsen iki kişinin yerini değiştir: sonuç değişiyorsa sıra önemlidir.

Tokalaşma ve tek devreli maç da sırasız seçmedir: her ikili bir kez buluşur. 10 kişi birbiriyle birer kez tokalaşırsa $\binom{10}{2} = 45$ tokalaşma olur.

![Yöntem şeması: kombinasyon problemi, sıra önemli mi sorusuna gidiyor. Evet ise önce seç, sonra diz. Hayır ise yalnızca seç, sonra koşul ne sorusu: gruplardan seçimde çarp, en az ise tümleyen, en çok ise durumları topla.](gorsel/tyt-matematik/09-06-yontem.svg "Her soruda iki karar ver: sıra önemli mi, koşul hangi türden? Formül ancak ondan sonra gelir.")

## Gruplardan seçim: çarp

**Örnek.** 5 kız ve 4 erkek öğrenci arasından 2 kız ve 2 erkekten oluşan 4 kişilik bir ekip kaç farklı şekilde seçilir?

Kızlar kendi aralarından, erkekler kendi aralarından seçilir:

- 2 kız: $\binom{5}{2} = 10$
- 2 erkek: $\binom{4}{2} = 6$

Her kız ikilisi her erkek ikilisiyle eşleşebilir. Kızları **ve** erkekleri seçiyorsun, bu yüzden çarparsın: $10 \cdot 6 = 60$.

**Kural.** Ayrı gruplardan belirli sayıda eleman seçiliyorsa her grubun seçim sayısı ayrı bulunur ve **çarpılır**. Durumlardan biri **ya da** öbürü oluyorsa sayılar **toplanır**.

## En az, en çok: durumlara ayır ya da tümleyeni çıkar

Aynı 5 kız ve 4 erkekten 4 kişilik ekipler kurulsun. Bütün ekiplerin sayısı $\binom{9}{4} = 126$. Bu ekipleri içlerindeki erkek sayısına göre ayırırsak:

| Erkek sayısı | Hesap | Ekip |
|---|---|---|
| 0 | $\binom{4}{0} \cdot \binom{5}{4}$ | 5 |
| 1 | $\binom{4}{1} \cdot \binom{5}{3}$ | 40 |
| 2 | $\binom{4}{2} \cdot \binom{5}{2}$ | 60 |
| 3 | $\binom{4}{3} \cdot \binom{5}{1}$ | 20 |
| 4 | $\binom{4}{4} \cdot \binom{5}{0}$ | 1 |
| Toplam | | 126 |

**Örnek (en az).** En az 1 erkek bulunan kaç ekip vardır?

Dört satırı toplamak yerine tek satırı çıkar. "En az 1 erkek"in tersi "hiç erkek yok"tur:

$$\binom{9}{4} - \binom{5}{4} = 126 - 5 = 121$$

![Sütun grafiği: ekipteki erkek sayısı 0, 1, 2, 3, 4 iken ekip sayıları 5, 40, 60, 20, 1. 0 sütunu kırmızı ve üstünde çıkar yazıyor, diğerleri yeşil. Sağda: en az 1 erkek, 126 eksi 5 eşittir 121.](gorsel/tyt-matematik/09-06-erkek-sayisi.svg "Yeşil sütunların hepsi istenen ekiplerdir. Dördünü toplamak yerine tek kırmızı sütunu toplamdan çıkarmak daha kısadır.")

Sık yapılan yanlış, "önce 1 erkeği koy, kalan 8 kişiden 3 kişi seç" demektir: $4 \cdot \binom{8}{3} = 224$. Bu sayı toplam ekip sayısı olan 126'dan bile büyüktür; çünkü birden çok erkekli ekipler, hangi erkeğin "önce" seçildiğine göre birkaç kez sayılır.

![Üstte: önce seçilen E1, sonra seçilenler E2 K1 K2. Altta: önce seçilen E2, sonra seçilenler E1 K1 K2. İki satırdan çıkan oklar aynı ekip kutusunda birleşiyor.](gorsel/tyt-matematik/09-06-fazla-sayma.svg "İki erkekli ekip iki kez sayıldı. Ekipte sıra yoktur; hangi erkeğin önce seçildiği ekibi değiştirmez.")

**Örnek (en çok).** En çok 1 erkek bulunan kaç ekip vardır?

"En çok 1" demek 0 ya da 1 erkek demektir. İki durum az olduğu için doğrudan topla:

$$\binom{5}{4} + \binom{4}{1} \cdot \binom{5}{3} = 5 + 40 = 45$$

**Kural.** "En az" ya da "en çok" görünce durumları yaz. İstenen durumlar azsa **topla**; istenmeyen durumlar azsa **tümünden çıkar**. "En az 1" sorularında çıkarma neredeyse her zaman kısadır.

## Belirli kişiler: kesin var, kesin yok, birlikte olmaz

**Örnek.** Aralarında Ece ve Ferhat'ın da bulunduğu 8 kişiden 3 kişilik bir komisyon seçilecek.

- **Ece kesin bulunacaksa:** Ece'yi koy; kalan 7 kişiden 2 kişi: $\binom{7}{2} = 21$.
- **Ece bulunmayacaksa:** Ece'yi listeden sil; 7 kişiden 3 kişi: $\binom{7}{3} = 35$.
- **Ece ile Ferhat birlikte bulunmayacaksa:** Tümünden ikisinin birlikte olduğu komisyonları çıkar. İkisi birlikteyse üçüncü kişi kalan 6 kişiden seçilir:

$$\binom{8}{3} - \binom{6}{1} = 56 - 6 = 50$$

**Kural.** Kesin bulunacak kişiyi önce yerleştir ve hem kişi sayısından hem seçilecek sayıdan düş. Kesin bulunmayacak kişiyi yalnızca kişi sayısından düş. "Birlikte olmasın" sorusunda tümünden "birlikte olanları" çıkar.

## Önce seç, sonra diz

**Örnek.** 5 kız ve 4 erkek arasından 2 kız ve 1 erkek seçilip bu 3 kişi bir sıraya yan yana kaç farklı şekilde dizilir?

İki adım vardır:

1. **Seç (sıra yok):** $\binom{5}{2} \cdot \binom{4}{1} = 10 \cdot 4 = 40$
2. **Diz (sıra var):** seçilen 3 kişi $3! = 6$ şekilde dizilir.

$$40 \cdot 6 = 240$$

**Kural.** Bir soru hem seçme hem dizme istiyorsa önce kombinasyonla seç, sonra seçilenleri permütasyonla diz ve çarp. Koşul seçimle ilgiliyse (kaç kız, kaç erkek) seçme adımında, dizilişle ilgiliyse (yan yana, başta) dizme adımında kullanılır.

## ÖSYM tuzakları

> **Sırasız seçimde sıralamak:** "3 kişilik ekip" için $P(7, 3)$ yazmak yanlıştır. Ekipte görev yoksa üyelerin yeri değişince yeni ekip oluşmaz: $\binom{7}{3}$.

> **"En az 1"de kesin birini koymak:** 5 kız 4 erkekten en az 1 erkekli 4 kişilik ekip için "önce 1 erkek seç, sonra kalan 8 kişiden 3 kişi seç": $4 \cdot \binom{8}{3} = 224$ yanlıştır. İki erkekli bir ekip, hangi erkeğin "ilk seçilen" olduğuna göre iki kez sayılır. Doğrusu $126 - 5 = 121$.

> **Çarpacağına toplamak:** 2 kız **ve** 2 erkek için $\binom{5}{2} + \binom{4}{2} = 16$ yazmak yanlıştır. Aynı ekibin iki parçası seçiliyorsa çarp.

> **Seçtikten sonra dizmeyi unutmak:** "Seçilip rafa dizilecek" diyen soruda yalnızca $\binom{n}{r}$ yazıp bırakma; seçilenlerin dizilişiyle de çarp.

## Kendini dene

### Soru 1
6 kız ve 4 erkek öğrenci arasından tam olarak 2 kızın bulunduğu 3 kişilik bir grup kaç farklı şekilde seçilebilir?

A) 19
B) 20
C) 60
D) 80
E) 120

**Cevap:** C
**Çözüm:** 2 kız $\binom{6}{2} = 15$ ve 1 erkek $\binom{4}{1} = 4$ şekilde seçilir; ikisi birlikte istendiği için çarpılır: $15 \cdot 4 = 60$. $19$ toplamak, $80$ "en az 2 kız" saymak ($60 + 20$), $120$ kızları sıralamaktır ($P(6, 2) \cdot 4$).

### Soru 2
Aralarında Ali ve Banu'nun da bulunduğu 7 kişiden 3 kişilik bir ekip seçilecektir. Ali ile Banu aynı ekipte **bulunmayacaksa** kaç farklı ekip seçilebilir?

A) 5
B) 10
C) 20
D) 30
E) 35

**Cevap:** D
**Çözüm:** Tüm ekipler $\binom{7}{3} = 35$. Ali ile Banu birlikteyse üçüncü kişi kalan 5 kişiden seçilir: $\binom{5}{1} = 5$. $35 - 5 = 30$. $10$ ikisinin de olmadığı ekipler ($\binom{5}{3}$), $20$ yalnızca birinin olduğu ekiplerdir ($2 \cdot \binom{5}{2}$); bu ikisinin toplamı da 30 eder.

### Soru 3
3 kadın ve 4 erkekten oluşan bir gruptan en az 1 kadının bulunduğu 3 kişilik bir kurul kaç farklı şekilde seçilebilir?

A) 4
B) 18
C) 31
D) 35
E) 45

**Cevap:** C
**Çözüm:** Tümü $\binom{7}{3} = 35$; hiç kadın olmayan kurullar yalnızca erkeklerden: $\binom{4}{3} = 4$. $35 - 4 = 31$. $45$, "önce 1 kadın seç, sonra 6 kişiden 2 kişi" yöntemiyle aynı kurulları birden çok kez saymaktır ($3 \cdot 15$). $18$ yalnızca tam 1 kadınlı kurullardır.

## Özet kartı

- Yer değiştirince sonuç değişmiyorsa sıra önemsizdir: $\binom{n}{r}$.
- Ayrı gruplardan seçim: her grubu ayrı seç, **çarp**. "Ya da" durumları **topla**.
- "En az 1": tümünden "hiç yok"u çıkar. Asla "önce 1 tane koy, kalanlardan seç" yapma.
- Kesin bulunacak kişiyi yerleştir, kesin bulunmayacağı sil; "birlikte olmasın"da birlikte olanları çıkar.
- Hem seçme hem dizme varsa: $\binom{n}{r}$ ile seç, $r!$ ile diz, çarp.

## Sonraki adım

Alıştırmaya geç (aşağıdaki düğme). Sonraki ders **Kombinasyon ve Geometri**; aynı seçme fikrini noktalara uygulayacaksın: iki nokta bir doğru, doğrusal olmayan üç nokta bir üçgen belirler.
