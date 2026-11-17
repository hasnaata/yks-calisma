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

# Alıştırma Soru 8: iki okulun ulaşım grafiği. A (600): Servis 120, Otobüs 150, Yürüyerek 90. B (400): Servis 162, Otobüs 108, Yürüyerek 90.
fig, (a1, a2) = plt.subplots(1, 2, figsize=(6.4, 3.4))
daire(a1, ["Servis", "Otobüs", "Yürüyerek"], [120, 150, 90], ["120°", "150°", "90°"], fs=11)
daire(a2, ["Servis", "Otobüs", "Yürüyerek"], [162, 108, 90], ["162°", "108°", "90°"], fs=11)
a1.set_title("A okulu", fontsize=13); a2.set_title("B okulu", fontsize=13)
fig.tight_layout(w_pad=1.5)
kaydet(fig, __file__)
