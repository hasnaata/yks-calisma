"""Matematik ve geometri şekilleri için ortak stil (matplotlib).

Her şeklin kaynağı gorsel/<ders-id>/<ad>.py dosyasıdır ve depo kökünden şöyle çalıştırılır:
    .venv/bin/python gorsel/tyt-matematik/11-01-dogru-grafigi.py
Kaynak dosyanın başı:
    import sys; sys.path.insert(0, "tools")
    from cizim import *
    fig, ax = sekil(6, 4)          # inç; genişlik 6'yı geçmesin
    ...
    kaydet(fig, __file__)          # aynı adla .svg yazar

Kurulum (bir kez): python3 -m venv --without-pip .venv, pip kur, sonra .venv/bin/python -m pip install matplotlib sympy
"""
import pathlib
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib import patches

MAVI, MAVI_ACIK = "#1f5fbf", "#e8f0fc"
YESIL, YESIL_ACIK = "#1c7c45", "#e3f4e9"
KIRMIZI, KIRMIZI_ACIK = "#b3261e", "#fbe9e7"
SARI, SARI_ACIK = "#8a5a00", "#fdf3d8"
YAZI, SOLUK, CIZGI = "#1d1f24", "#636a76", "#c9c5bb"

plt.rcParams.update({
    "font.family": "DejaVu Sans", "font.size": 13, "text.color": YAZI, "axes.labelcolor": YAZI,
    "axes.edgecolor": SOLUK, "xtick.color": SOLUK, "ytick.color": SOLUK, "axes.linewidth": 1,
    "lines.linewidth": 2.2, "svg.fonttype": "path", "figure.facecolor": "none", "axes.facecolor": "none",
    "mathtext.fontset": "dejavusans",
})

def sekil(en=6, boy=4):
    """Boş şekil. Geometri çizimleri için eksenleri gizlemek üzere ax.axis('off') ve ax.set_aspect('equal') kullan."""
    fig, ax = plt.subplots(figsize=(min(en, 6.5), boy))
    return fig, ax

def eksenler(ax, x=(-5, 5), y=(-5, 5), izgara=True):
    """Orijinden geçen oklu koordinat eksenleri."""
    ax.set_xlim(*x); ax.set_ylim(*y)
    for s in ("top", "right"): ax.spines[s].set_visible(False)
    ax.spines["left"].set_position("zero"); ax.spines["bottom"].set_position("zero")
    ax.plot(1, 0, ">", color=SOLUK, transform=ax.get_yaxis_transform(), clip_on=False, markersize=6)
    ax.plot(0, 1, "^", color=SOLUK, transform=ax.get_xaxis_transform(), clip_on=False, markersize=6)
    if izgara: ax.grid(True, color=CIZGI, linewidth=0.6, alpha=0.7)
    ax.set_axisbelow(True)
    ax.text(1.02, 0, "x", transform=ax.get_yaxis_transform(), va="center")
    ax.text(0, 1.03, "y", transform=ax.get_xaxis_transform(), ha="center")

def sayi_dogrusu(ax, a, b, isaretler=None):
    """a ile b arasında sayı doğrusu. Üzerine ax.plot / ax.hlines ile aralık çizilir (y=0)."""
    ax.set_xlim(a - 0.6, b + 0.6); ax.set_ylim(-1, 1); ax.axis("off")
    ax.annotate("", xy=(b + 0.55, 0), xytext=(a - 0.55, 0), arrowprops=dict(arrowstyle="<->", color=SOLUK, lw=1.4))
    for t in (isaretler if isaretler is not None else range(int(a), int(b) + 1)):
        ax.plot([t, t], [-0.08, 0.08], color=SOLUK, lw=1.2)
        ax.text(t, -0.32, str(t).replace("-", "−").replace(".", ","), ha="center", va="top", color=YAZI)

def nokta(ax, x, y, ad="", dx=0.15, dy=0.15, renk=YAZI, dolu=True):
    """Etiketli nokta. dolu=False içi boş (açık uç) çizer."""
    ax.plot(x, y, "o", color=renk, markerfacecolor=renk if dolu else "white", markersize=7, zorder=5)
    if ad: ax.text(x + dx, y + dy, ad, color=renk, fontsize=13, zorder=6)

def aci(ax, kose, p1, p2, r=0.5, ad="", renk=MAVI):
    """kose noktasında, kose->p1 ile kose->p2 arasındaki açı yayı ve etiketi."""
    a1 = np.degrees(np.arctan2(p1[1] - kose[1], p1[0] - kose[0])); a2 = np.degrees(np.arctan2(p2[1] - kose[1], p2[0] - kose[0]))
    if (a2 - a1) % 360 > 180: a1, a2 = a2, a1
    ax.add_patch(patches.Arc(kose, 2 * r, 2 * r, theta1=a1, theta2=a1 + (a2 - a1) % 360, color=renk, lw=1.6))
    if ad:
        orta = np.radians(a1 + ((a2 - a1) % 360) / 2)
        ax.text(kose[0] + 1.7 * r * np.cos(orta), kose[1] + 1.7 * r * np.sin(orta), ad, ha="center", va="center", color=renk, fontsize=12)

def kaydet(fig, kaynak):
    """Şekli kaynak dosyayla aynı adda .svg olarak kaydeder."""
    hedef = pathlib.Path(kaynak).with_suffix(".svg")
    fig.savefig(hedef, format="svg", bbox_inches="tight", pad_inches=0.08, transparent=True)
    plt.close(fig); print(hedef)
