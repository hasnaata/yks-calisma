---
baslik: Köklü İfadeleri İçeren Denklem ve Eşitsizlikler · Alıştırma
ders: tyt-matematik
soru: 12
guncelleme: 2026-11-17
---
# Alıştırma: Köklü İfadeleri İçeren Denklem ve Eşitsizlikler

Sorular özgündür ve ÖSYM soru tarzında yazılmıştır. Derse bakmadan çöz.

## Isınma

### Soru 1 · Kolay
$\sqrt{x - 3} = 5$ olduğuna göre $x$ kaçtır?

A) 8
B) 13
C) 22
D) 25
E) 28

**Cevap:** E
**Çözüm:** İki tarafın karesini al: $x - 3 = 25$, $x = 28$. Sağlama: $\sqrt{25} = 5$. Kare almadan $x - 3 = 5$ yazan $8$, kare yerine iki ile çarpan $2 \cdot 5 + 3 = 13$, $3$'ü yanlış yöne geçiren $22$ bulur.

### Soru 2 · Kolay
$\sqrt[3]{2x + 1} = -3$ olduğuna göre $x$ kaçtır?

A) −14
B) −13
C) −5
D) 4
E) 13

**Cevap:** A
**Çözüm:** Küpkök negatif olabilir; iki tarafın küpünü al: $2x + 1 = (-3)^3 = -27$. $2x = -28$, $x = -14$. Kontrol: $\sqrt[3]{-28 + 1} = \sqrt[3]{-27} = -3$. Küp yerine kare alan $2x + 1 = 9$ ile $4$, işareti kaçırıp $2x + 1 = 27$ yazan $13$, $1$'i karşıya geçirirken işaret hatası yapan $-13$ bulur.

### Soru 3 · Kolay
$\sqrt{75}$ sayısı hangi iki ardışık tam sayı arasındadır?

A) 6 ile 7
B) 7 ile 8
C) 8 ile 9
D) 9 ile 10
E) 37 ile 38

**Cevap:** C
**Çözüm:** 75'in iki yanındaki tam kareler: $64 < 75 < 81$. Karekök al: $8 < \sqrt{75} < 9$. E seçeneği karekök yerine ikiye bölmekten ($75 : 2 = 37{,}5$) gelir.

## Orta

### Soru 4 · Orta
$0 < x < 1$ olmak üzere

$$a = \sqrt{x}, \qquad b = \sqrt[3]{x}, \qquad c = x$$

sayılarının doğru sıralaması aşağıdakilerden hangisidir?

A) $a < b < c$
B) $c < a < b$
C) $b < a < c$
D) $c < b < a$
E) $a < c < b$

**Cevap:** B
**Çözüm:** Kök içi 0 ile 1 arasındayken kök derecesi büyüdükçe sayı 1'e yaklaşır, yani büyür. $x$'i $\sqrt[1]{x}$ gibi düşün: $x < \sqrt{x} < \sqrt[3]{x}$, yani $c < a < b$. Bir sayıyla dene: $x = 0{,}064$ için $c = 0{,}064$, $a \approx 0{,}25$, $b = 0{,}4$. D seçeneği, 1'den büyük sayılar için geçerli sırayı buraya taşımaktır.

### Soru 5 · Orta
$$a = \sqrt{3}, \qquad b = \sqrt[3]{4}, \qquad c = \sqrt[6]{10}$$

sayılarının doğru sıralaması aşağıdakilerden hangisidir?

A) $a < b < c$
B) $a < c < b$
C) $b < a < c$
D) $c < a < b$
E) $c < b < a$

**Cevap:** E
**Çözüm:** Dereceler 2, 3, 6; ortak derece 6. Üç sayının da 6. kuvvetini al: $a^6 = 3^3 = 27$, $b^6 = 4^2 = 16$, $c^6 = 10$. Pozitif sayılarda kuvveti büyük olan büyüktür: $c < b < a$. Kök içlerine bakıp "$3 < 4 < 10$" diyen A seçeneğini işaretler; dereceler farklıyken bu karşılaştırma geçersizdir.

### Soru 6 · Orta
$\sqrt{2x + 3} = x$ denklemini sağlayan $x$ değerlerinin toplamı kaçtır?

A) −1
B) 1
C) 2
D) 3
E) 4

**Cevap:** D
**Çözüm:** Kare al: $2x + 3 = x^2$, yani $x^2 - 2x - 3 = 0$, $(x - 3)(x + 1) = 0$. Adaylar $3$ ve $-1$. Sağlama: $x = 3$ için $\sqrt{9} = 3$, geçerli. $x = -1$ için $\sqrt{1} = 1 \ne -1$, yabancı kök. Tek çözüm $3$, toplam $3$. Sağlama yapmayan $3 + (-1) = 2$ bulur.

### Soru 7 · Orta
$\sqrt{x + 2} \le 4$ eşitsizliğini sağlayan kaç farklı $x$ tam sayısı vardır?

A) 14
B) 15
C) 16
D) 17
E) 18

**Cevap:** D
**Çözüm:** Tanım koşulu: $x + 2 \ge 0$, yani $x \ge -2$. İki taraf da negatif değil, kare al: $x + 2 \le 16$, $x \le 14$. Birlikte $-2 \le x \le 14$. Tam sayı sayısı $14 - (-2) + 1 = 17$. $x$'i pozitif sanan 14, yalnızca negatif olmayanları sayan 15 bulur.

## ÖSYM tarzı

### Soru 8 · ÖSYM tarzı
Hesap makinesi kullanmadan karekök bulmak isteyen Deniz şu yöntemi uyguluyor:

- $a$ sayısından küçük en büyük tam kare $x$, $a$ sayısından büyük en küçük tam kare $y$ olsun.
- $\sqrt{a} \approx \sqrt{x} + \dfrac{a - x}{y - x}$ olarak hesaplanır.

Deniz bu yöntemle bir $a$ tam sayısının karekökünü yaklaşık $7{,}4$ buluyor.

Buna göre $a$ kaçtır?

A) 51
B) 53
C) 55
D) 57
E) 59

**Cevap:** C
**Çözüm:** Sonucun tam kısmı $7$ olduğundan $\sqrt{x} = 7$: $x = 49$, $y = 64$, $y - x = 15$. Kesirli kısım $\frac{a - 49}{15} = 0{,}4$, yani $a - 49 = 6$, $a = 55$. Kontrol: $7 + \frac{6}{15} = 7{,}4$. Paydayı $10$ alıp $a - 49 = 4$ yazan $53$ bulur.

### Soru 9 · ÖSYM tarzı
Hava direnci ihmal edildiğinde, $h$ metre yükseklikten serbest bırakılan bir cismin yere çarpma hızı yaklaşık $v = \sqrt{20h}$ metre/saniyedir.

Bir test düzeneğinde cismin yere çarpma hızının 20 m/s'den büyük, 40 m/s'den küçük olması isteniyor.

Buna göre $h$ yüksekliği metre cinsinden kaç farklı tam sayı değeri alabilir?

A) 59
B) 60
C) 61
D) 79
E) 80

**Cevap:** A
**Çözüm:** $20 < \sqrt{20h} < 40$. Üç taraf da pozitif, kare al: $400 < 20h < 1600$, yani $20 < h < 80$. Tam sayılar $21, 22, \dots, 79$: $79 - 21 + 1 = 59$ tane. Bir ucu dahil eden 60, iki ucu da dahil eden 61, alt sınırı unutup $1$'den $79$'a sayan 79 bulur.

### Soru 10 · ÖSYM tarzı
Bir hesap makinesinin ekranı sonuçların yalnızca tam kısmını gösteriyor; örneğin $\sqrt{10} = 3{,}16\ldots$ için ekranda $3$ görünüyor.

Bu makineye bir $x$ pozitif tam sayısı girilip karekök tuşuna basıldığında ekranda $6$ görünüyor.

Buna göre $x$ kaç farklı değer alabilir?

A) 1
B) 7
C) 12
D) 13
E) 14

**Cevap:** D
**Çözüm:** Ekranda $6$ görünmesi $6 \le \sqrt{x} < 7$ demektir. Kare al: $36 \le x < 49$. Tam sayılar $36, 37, \dots, 48$: $48 - 36 + 1 = 13$ tane. $36$'yı da dışarıda bırakan 12, $49$'u dahil eden 14, yalnızca $x = 36$'yı düşünen 1 bulur.

### Soru 11 · ÖSYM tarzı
Bir karenin alanı $12$ cm², bir küpün hacmi $40$ cm³'tür. Karenin bir kenarının uzunluğu $x$ cm, küpün bir ayrıtının uzunluğu $y$ cm'dir.

Buna göre aşağıdakilerden hangisi doğrudur?

A) $3 < x < y$
B) $3 < y < x$
C) $y < 3 < x$
D) $x < 3 < y$
E) $x < y < 3$

**Cevap:** B
**Çözüm:** $x = \sqrt{12}$, $y = \sqrt[3]{40}$. $9 < 12$ olduğundan $x > 3$; $27 < 40$ olduğundan $y > 3$. Karşılaştırmak için 6. kuvvet al: $x^6 = 12^3 = 1728$, $y^6 = 40^2 = 1600$. $1728 > 1600$, yani $x > y$. Sonuç $3 < y < x$. "40, 12'den büyük" diye düşünen A seçeneğine gider; dereceler farklıyken kök içleri karşılaştırılamaz.

### Soru 12 · ÖSYM tarzı
Bir sayı makinesi kendisine girilen $x$ sayısıyla şu işlemleri sırayla yapıyor:

1. $x$'e $3$ ekleyip toplamın karekökünü alıyor.
2. Bulduğu sonucu $x$'e ekliyor.
3. Bu toplamın karekökünü alıp ekrana yazıyor.

Makineye bir $x$ sayısı girildiğinde ekranda $3$ yazıyor.

Buna göre $x$ kaçtır?

A) 3
B) 6
C) 9
D) 13
E) 19

**Cevap:** B
**Çözüm:** Makinenin çıktısı $\sqrt{x + \sqrt{x + 3}}$. Denklem: $\sqrt{x + \sqrt{x + 3}} = 3$. Kare al: $x + \sqrt{x + 3} = 9$. Kökü yalnız bırak: $\sqrt{x + 3} = 9 - x$. Kare al: $x + 3 = 81 - 18x + x^2$, yani $x^2 - 19x + 78 = 0$, $(x - 6)(x - 13) = 0$. Sağlama: $x = 6$ için $\sqrt{9} = 3$, $6 + 3 = 9$, $\sqrt{9} = 3$; geçerli. $x = 13$ için $9 - 13 = -4$ olur ama karekök negatif olamaz; yabancı kök. Cevap $6$. Sağlama yapmayan 13'ü, köklerin toplamını yazan 19'u seçer.
