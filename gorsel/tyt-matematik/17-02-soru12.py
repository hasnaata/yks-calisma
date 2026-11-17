import sys; sys.path.insert(0, "tools")
from cizim import *

def daire(ax, adlar, acilar, yaz=None, r_yazi=0.58, fs=13):
    renk = [MAVI_ACIK, YESIL_ACIK, SARI_ACIK, KIRMIZI_ACIK]; kenar = [MAVI, YESIL, SARI, KIRMIZI]
    bas = 90
    for i, (ad, a) in enumerate(zip(adlar, acilar)):
        ax.add_patch(patches.Wedge((0, 0), 1, bas - a, bas, facecolor=renk[i], edgecolor="white", lw=2))
        orta = np.radians(bas - a / 2)
        t = ad + ("\n" + yaz[i] if yaz and yaz[i] else "")
        ax.text(r_yazi * np.cos(orta), r_yazi * np.sin(orta), t, ha="center", va="center", color=kenar[i], fontsize=fs)
        bas -= a
    ax.add_patch(patches.Circle((0, 0), 1, fill=False, edgecolor=SOLUK, lw=1))
    ax.plot(0, 0, "o", color=SOLUK, markersize=3)
    ax.set_xlim(-1.05, 1.05); ax.set_ylim(-1.05, 1.05); ax.set_aspect("equal"); ax.axis("off")

# Alıştırma Soru 12: 180 çalışan. Üretim 160, Satış 100, Ar-Ge 60, Yönetim 40.
fig, ax = sekil(4.4, 4.4)
daire(ax, ["Üretim", "Satış", "Ar-Ge", "Yönetim"], [160, 100, 60, 40], ["160°", "100°", "60°", "40°"])
kaydet(fig, __file__)
