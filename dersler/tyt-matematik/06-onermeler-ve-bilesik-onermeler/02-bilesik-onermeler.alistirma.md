---
baslik: Bileşik Önermeler · Alıştırma
ders: tyt-matematik
soru: 12
guncelleme: 2026-11-17
---
# Alıştırma: Bileşik Önermeler

Sorular özgündür ve ÖSYM soru tarzında yazılmıştır. Derse bakmadan çöz.

## Isınma

### Soru 1 · Kolay
$p \equiv 1$ ve $q \equiv 0$ olduğuna göre aşağıdaki önermelerden hangisinin doğruluk değeri 1'dir?

A) $p \wedge q$
B) $p' \vee q$
C) $(p \vee q)'$
D) $p \wedge q'$
E) $p' \wedge q'$

**Cevap:** D
**Çözüm:** $p' \equiv 0$, $q' \equiv 1$. A) $1 \wedge 0 \equiv 0$. B) $0 \vee 0 \equiv 0$. C) $p \vee q \equiv 1$, değili 0. D) $1 \wedge 1 \equiv 1$. E) $0 \wedge 1 \equiv 0$. Değeri 1 olan yalnız D'dir.

### Soru 2 · Kolay
Aşağıdaki önermeler veriliyor.

- $p$: "7 bir asal sayıdır."
- $q$: "$2^3 = 6$"
- $r$: "$-5 < -2$"

Buna göre aşağıdaki bileşik önermelerden hangisinin doğruluk değeri 0'dır?

A) $p \wedge q$
B) $p \vee q$
C) $q \vee r$
D) $p \wedge r$
E) $q \veebar r$

**Cevap:** A
**Çözüm:** 7 asaldır: $p \equiv 1$. $2^3 = 8$ olduğundan $q \equiv 0$. Sayı doğrusunda $-5$, $-2$'nin solundadır: $r \equiv 1$. A) $1 \wedge 0 \equiv 0$. B) $1 \vee 0 \equiv 1$. C) $0 \vee 1 \equiv 1$. D) $1 \wedge 1 \equiv 1$. E) değerler farklı, $q \veebar r \equiv 1$. $2^3$'ü $2 \cdot 3 = 6$ diye hesaplayan $q \equiv 1$ bulur ve doğru cevabı kaçırır.

### Soru 3 · Kolay
$(p \wedge q')'$ önermesi aşağıdakilerden hangisine denktir?

A) $p \wedge q$
B) $p' \wedge q$
C) $p' \vee q$
D) $p \vee q'$
E) $p' \vee q'$

**Cevap:** C
**Çözüm:** De Morgan: $(p \wedge q')' \equiv p' \vee (q')' \equiv p' \vee q$. Bağlacı çevirmeyi unutan B'yi, $(q')' \equiv q$ olduğunu gözden kaçıran E'yi seçer.

## Orta

### Soru 4 · Orta
$(p' \vee q) \vee r \equiv 0$ olduğuna göre $p$, $q$ ve $r$ önermelerinin doğruluk değerleri sırasıyla aşağıdakilerden hangisidir?

A) 0, 0, 0
B) 0, 1, 0
C) 0, 1, 1
D) 1, 0, 0
E) 1, 1, 0

**Cevap:** D
**Çözüm:** Sonucu 0 olan bir "veya" zincirinde bütün parçalar 0'dır: $p' \equiv 0$, $q \equiv 0$, $r \equiv 0$. $p' \equiv 0$ ise $p \equiv 1$. Sonuç: 1, 0, 0. $p'$ yerine $p$'yi 0 alan A'yı seçer.

### Soru 5 · Orta
$[(p \wedge q') \vee (p \wedge q)] \vee p'$ önermesi aşağıdakilerden hangisine denktir?

A) $0$
B) $1$
C) $p$
D) $p'$
E) $q$

**Cevap:** B
**Çözüm:** Köşeli parantezde $p \wedge$ ortaktır: $p \wedge (q' \vee q) \equiv p \wedge 1 \equiv p$. Önerme $p \vee p'$ olur ve bu her zaman 1'dir. Yalnızca köşeli parantezi sadeleştirip duran C'yi seçer.

### Soru 6 · Orta
$p$, $q$ ve $r$ önermelerinin doğruluk tablosunda $(p \veebar q) \vee r$ bileşik önermesi kaç satırda 1 değerini alır?

A) 3
B) 4
C) 5
D) 6
E) 7

**Cevap:** D
**Çözüm:** Tabloda 8 satır vardır. $r \equiv 1$ olan 4 satırın hepsinde "veya" 1 olur. $r \equiv 0$ olan 4 satırda sonuç $p \veebar q$'ya bağlıdır; $p$ ile $q$'nun farklı olduğu 2 satırda 1 olur. Toplam $4 + 2 = 6$. $\veebar$ bağlacını $\vee$ gibi okuyan $4 + 3 = 7$ bulur; yalnızca $r \equiv 1$ satırlarını sayan 4 bulur.

### Soru 7 · Orta
$(p \wedge q') \vee r \equiv 0$ ve $p \vee r \equiv 1$ olduğu biliniyor.

Buna göre aşağıdakilerden hangisinin doğruluk değeri 1'dir?

A) $(p \vee r) \wedge q$
B) $p \wedge r$
C) $q' \vee r$
D) $p \veebar q$
E) $p' \vee r$

**Cevap:** A
**Çözüm:** İlk bilgi 0 olan bir "veya": $p \wedge q' \equiv 0$ ve $r \equiv 0$. İkinci bilgide $r \equiv 0$ olduğundan $p \equiv 1$. O hâlde $p \wedge q' \equiv 1 \wedge q' \equiv 0$, yani $q' \equiv 0$ ve $q \equiv 1$. Değerler: $p \equiv 1$, $q \equiv 1$, $r \equiv 0$. A) $1 \wedge 1 \equiv 1$. B) $1 \wedge 0 \equiv 0$. C) $0 \vee 0 \equiv 0$. D) değerler aynı, 0. E) $0 \vee 0 \equiv 0$.

## ÖSYM tarzı

### Soru 8 · ÖSYM tarzı
Bir dükkânın alarm sistemi için şu önermeler tanımlanıyor:

- $p$: "Kapı açıktır."
- $q$: "Sistem kuruludur."
- $r$: "Cam kırıktır."

Alarm yalnızca $(p \wedge q) \vee r \equiv 1$ olduğunda çalar. Bir gece alarmın **çalmadığı** biliniyor.

Buna göre aşağıdakilerden hangisi kesinlikle doğrudur?

A) Kapı açıktır.
B) Cam kırıktır.
C) Kapı kapalıdır veya sistem kurulu değildir.
D) Sistem kurulu değildir.
E) Kapı kapalıdır ve sistem kurulu değildir.

**Cevap:** C
**Çözüm:** Alarm çalmadıysa $(p \wedge q) \vee r \equiv 0$; "veya" 0 olduğundan $p \wedge q \equiv 0$ ve $r \equiv 0$. $r \equiv 0$: cam kırık değildir, B yanlıştır. $p \wedge q \equiv 0$ bilgisinin De Morgan ile karşılığı $p' \vee q' \equiv 1$: "Kapı kapalıdır veya sistem kurulu değildir." Bu kesindir. A, D ve E kesin değildir: örneğin kapı açık, sistem kurulu değilken alarm çalmaz (A doğru, E yanlış olur); kapı kapalı, sistem kuruluyken de çalmaz (D yanlış olur).

### Soru 9 · ÖSYM tarzı
Her $p$ ve $q$ önermesi için $\ast$ bağlacı

$$p \ast q \equiv p' \vee q'$$

biçiminde tanımlanıyor.

Buna göre $(p \ast q) \ast (p \ast q)$ önermesi aşağıdakilerden hangisine denktir?

A) $p \vee q$
B) $p' \wedge q'$
C) $p' \vee q'$
D) $p \veebar q$
E) $p \wedge q$

**Cevap:** E
**Çözüm:** $s \equiv p \ast q$ de. Tanımdan $s \ast s \equiv s' \vee s' \equiv s'$ (tek kuvvet). O hâlde sonuç $(p \ast q)' \equiv (p' \vee q')'$. De Morgan: $(p')' \wedge (q')' \equiv p \wedge q$. Değil almayı unutan C'yi, De Morgan'da bağlacı çevirmeyen A'yı seçer.

### Soru 10 · ÖSYM tarzı
10 ile 30 arasındaki tam sayılardan (10 ve 30 dahil) biri $x$ olarak seçiliyor ve

- $p$: "$x$ sayısı 4'ün katıdır."
- $q$: "$x$ sayısı 6'nın katıdır."

önermeleri tanımlanıyor.

Buna göre $(p \vee q) \wedge (p \wedge q)'$ önermesini doğru yapan kaç farklı $x$ değeri vardır?

A) 2
B) 3
C) 5
D) 7
E) 9

**Cevap:** C
**Çözüm:** $(p \vee q) \wedge (p \wedge q)'$: "en az biri doğru ama ikisi birden değil", yani $p \veebar q$. 4'ün katları: 12, 16, 20, 24, 28. 6'nın katları: 12, 18, 24, 30. İkisinin de katı olanlar: 12, 24. Yalnız birinin katı olanlar: 16, 20, 28, 18, 30; toplam **5**. Yalnızca $p \vee q$'ya bakan 7, $p \wedge q$'ya bakan 2, ortakları iki kez sayan $5 + 4 = 9$ bulur.

### Soru 11 · ÖSYM tarzı
Şekildeki devrede $p$ anahtarı tek başına, $q$ ve $r$ anahtarları ise iki ayrı kolda bulunmaktadır. Her anahtar açık ya da kapalı olabilir; lamba, pilden çıkan akım lambaya ulaşabiliyorsa yanar.

![Devre şeması: pilden çıkan tel önce p anahtarından geçiyor, sonra ikiye ayrılıyor. Üst kolda q, alt kolda r anahtarı var. Kollar yeniden birleşip lambaya, oradan pile dönüyor.](gorsel/tyt-matematik/06-02-soru11.svg "q ve r anahtarları birbirine paralel, p anahtarı bu ikiliye seri bağlı.")

Üç anahtarın açık ya da kapalı olma durumlarının oluşturduğu 8 farklı durumun kaçında lamba yanar?

A) 2
B) 3
C) 4
D) 5
E) 6

**Cevap:** B
**Çözüm:** Kapalı anahtar 1, açık anahtar 0 olsun. Seri bağlantı "ve", paralel bağlantı "veya" gibi çalışır: lamba $p \wedge (q \vee r) \equiv 1$ iken yanar. Bunun için $p \equiv 1$ olmalı ve $q \vee r \equiv 1$ olmalı. $q \vee r$, 4 durumun 3'ünde 1'dir (yalnız ikisi de açıkken 0). Toplam $1 \cdot 3 = 3$ durum. Devreyi $p \vee (q \wedge r)$ gibi okuyan 5 bulur.

### Soru 12 · ÖSYM tarzı
Bir kutuda kırmızı, mavi ve yeşil toplardan bazıları vardır. Aşağıdaki önermeler tanımlanıyor:

- $p$: "Kutuda kırmızı top vardır."
- $q$: "Kutuda mavi top vardır."
- $r$: "Kutuda yeşil top vardır."

Kutuyu açan biri şunları söylüyor ve iki bilgi de doğrudur:

- I. $p \vee q' \equiv 0$
- II. $q \veebar r \equiv 1$

Buna göre kutuda hangi renk toplar vardır?

A) Yalnız kırmızı
B) Yalnız yeşil
C) Kırmızı ve yeşil
D) Mavi ve yeşil
E) Yalnız mavi

**Cevap:** E
**Çözüm:** I: "veya" 0 olduğundan $p \equiv 0$ ve $q' \equiv 0$; yani kırmızı yok, mavi var ($q \equiv 1$). II: "ya da" 1 ise değerler farklıdır; $q \equiv 1$ olduğundan $r \equiv 0$, yeşil yok. Kutuda yalnız mavi top vardır. $\veebar$ bağlacını $\vee$ gibi okuyan yeşil için karar veremez ve D'ye kayabilir; I'de $q'$ yerine $q$'yu 0 alan B'yi bulur.
