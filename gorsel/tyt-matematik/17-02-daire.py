import sys; sys.path.insert(0, "tools")
from cizim import *

# Ders örneği: 120 öğrencinin ulaşım tercihi. Otobüs 45 (135°), Yürüyerek 30 (90°), Servis 25 (75°), Özel araç 20 (60°).
adlar = ["Otobüs", "Yürüyerek", "Servis", "Özel araç"]; aci_ = [135, 90, 75, 60]
renk = [MAVI_ACIK, YESIL_ACIK, SARI_ACIK, KIRMIZI_ACIK]; kenar = [MAVI, YESIL, SARI, KIRMIZI]
fig, ax = sekil(4.6, 4.6)
bas = 90
for ad, a, r, k in zip(adlar, aci_, renk, kenar):
    ax.add_patch(patches.Wedge((0, 0), 1, bas - a, bas, facecolor=r, edgecolor="white", lw=2))
    orta = np.radians(bas - a / 2)
    ax.text(0.58 * np.cos(orta), 0.58 * np.sin(orta), f"{ad}\n{a}°", ha="center", va="center", color=k, fontsize=13)
    bas -= a
ax.add_patch(patches.Circle((0, 0), 1, fill=False, edgecolor=SOLUK, lw=1))
ax.plot(0, 0, "o", color=SOLUK, markersize=3)
ax.set_xlim(-1.05, 1.05); ax.set_ylim(-1.05, 1.05); ax.set_aspect("equal"); ax.axis("off")
kaydet(fig, __file__)
