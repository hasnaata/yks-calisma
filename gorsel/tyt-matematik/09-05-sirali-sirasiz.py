import sys; sys.path.insert(0, "tools")
from cizim import *

# {a, b, c, d}: 6 tane 2 elemanlı alt küme (kombinasyon), her biri 2! = 2 sıralı diziliş verir (permütasyon).
fig, ax = sekil(6, 4.6)
ax.axis("off"); ax.set_aspect("equal")
def kutu(x, y, w, yazi, dolgu, kenar, fs=15):
    ax.add_patch(patches.FancyBboxPatch((x, y), w, 0.7, boxstyle="round,pad=0.02,rounding_size=0.1",
                                        facecolor=dolgu, edgecolor=kenar, lw=1.5))
    ax.text(x + w / 2, y + 0.35, yazi, ha="center", va="center", fontsize=fs, color=kenar, fontweight="bold")
ciftler = ["ab", "ac", "ad", "bc", "bd", "cd"]
ax.text(0.8, 0.55, "Alt küme", ha="center", fontsize=13, color=MAVI, fontweight="bold")
ax.text(4.35, 0.55, "Sıralı dizilişler", ha="center", fontsize=13, color=SARI, fontweight="bold")
for i, c in enumerate(ciftler):
    y = -0.9 - i * 0.95
    kutu(-0.3, y, 2.1, "{" + c[0] + ", " + c[1] + "}", MAVI_ACIK, MAVI)
    ax.annotate("", xy=(2.55, y + 0.35), xytext=(1.9, y + 0.35), arrowprops=dict(arrowstyle="->", color=SOLUK, lw=1.4))
    kutu(2.7, y, 1.4, c[0] + c[1], SARI_ACIK, SARI)
    kutu(4.6, y, 1.4, c[1] + c[0], SARI_ACIK, SARI)
yalt = -0.9 - 6 * 0.95
ax.text(0.8, yalt + 0.3, "C(4, 2) = 6", ha="center", va="top", fontsize=14, color=MAVI, fontweight="bold")
ax.text(4.35, yalt + 0.3, "P(4, 2) = 12", ha="center", va="top", fontsize=14, color=SARI, fontweight="bold")
ax.text(3.0, yalt - 0.45, "12 = 6 · 2!", ha="center", va="top", fontsize=16, color=YESIL, fontweight="bold")
ax.set_xlim(-0.5, 6.2); ax.set_ylim(yalt - 1.2, 1.0)
kaydet(fig, __file__)
