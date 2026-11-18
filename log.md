# Günlük (log.md)

Yalnızca sona eklenir. `grep "^## \[" log.md | tail -5` son beş kaydı verir.

## [2026-11-16] kurulum | Repo, site ve müfredat
MEBİ ağacı tarandı: 13 ders, 231 konu, 740 alt konu (`raw/mebi/agac.txt`). 740 konu özeti PDF'i `raw/mebi/` altına indirildi (yerel, git dışı). Site, CLAUDE.md, /teach becerisi ve araçlar kuruldu.

## [2026-11-16] ingest | TYT Biyoloji 1.1, 2.1, 3.1, 3.2, 3.3
İlk beş ders ve alıştırma yazıldı: Canlıların Ortak Özellikleri; İnorganik Bileşikler; Organik Bileşikler ve Karbonhidratlar; Lipitler; Proteinler.

## [2026-11-16] ingest | TYT Biyoloji tamamlandı (50/50)
Kalan 45 ders ve alıştırma yazıldı (konu 3.4–17.1). MEBİ özetlerindeki hatalar düzeltilerek yazıldı (ör. krossing overin homolog olmayan kromozomlar arasında gösterilmesi, alglerde kitin çeper, azot fiksasyonunun ürünü).

## [2026-11-16] lint | TYT Biyoloji cevap anahtarı denetimi
Üç bağımsız gözden geçirme (595 soru) ve cevapları silinmiş 11 dosyada kör çözüm (120 soru): yanlış anahtar yok. 13 ifade düzeltmesi yapıldı (otozomal/X'e bağlı ayrımı, belirsiz bir çeldirici, suyun özellikleri, fosfolipit yönelimi vb.).

## [2026-11-16] site | Görsel ve erişilebilirlik düzeltmeleri
Okuma genişliği, kaydırılabilir tablolar, telefon başlığı, sorularda yazılı durum etiketi, odak ve basma durumları, boş/hata durumları.

## [2026-11-17] görsel | TYT Biyoloji derslerine görseller (50/50)
Her derse 3–5 görsel eklendi: toplam 237 (Pele şemaları, Wikimedia Commons'tan fotoğraf, mikroskop görüntüsü ve 3B modeller). Her görsel ikinci bir gözden geçirmede telefon boyutunda kontrol edildi; 73 düzeltme, 1 çıkarma. Atıflar `gorsel/ATIF.md` içinde. Site açık temaya alındı; ders renkleri, simgeler ve günlük seri eklendi.

## [2026-11-17] güncelle | TYT Biyoloji: 50 derse Mısır Arapçası giriş kutusu (yazım + ikinci okuyucu denetimi); kural CLAUDE.md, stil assets/stil.css

## [2026-11-17] düzelt | TYT Biyoloji: Arapça giriş kutularının 50si tek tek okundu; 1 yazım hatası, 4 tekrar eden süre ifadesi düzeltildi

## [2026-11-17] ders yaz | TYT Matematik: 107 ders + alıştırma yazıldı (toplam 109); kör çözüm ve editör denetimi henüz yapılmadı, yayınlanmadı

## [2026-11-18] denetle | TYT Matematik: 107 ders kör çözüm + editör denetiminden geçti (3 cevap anahtarı düzeltmesi, tümü temiz); yönetmen denetimi: satır içi formül işleme hatası (assets/uygulama.js) ve bir seçenek sırası düzeltildi; yayınlandı

## [2026-11-18] güncelle | TYT Matematik: 109 derse Mısır Arapçası giriş kutusu (Opus yazımı; 109u tek tek okundu, iddialar dersle karşılaştırıldı, 3 küçük düzeltme)

## [2026-11-18] ders yaz | TYT Matematik tamamlandı (128/128): son 19 geometri dersi (Opus yazım + kör çözüm + editör; anahtar değişikliği yok), Arapça giriş kutuları okundu, 256 sayfa işleme denetiminden geçti
