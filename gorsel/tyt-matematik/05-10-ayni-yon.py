import sys; sys.path.insert(0, "tools")
from cizim import *

# Arkadaki araç A'da 90 km/sa, öndeki araç B'de 70 km/sa; |AB| = 60 km; ikisi aynı yönde aynı anda çıkıyor.
# Yetişme süresi 60 / (90 - 70) = 3 saat. Arkadaki 270 km, öndeki 210 km gider; C noktasında yan yana gelirler.
s = 1 / 45
fig, ax = sekil(6.2, 3.0)
ax.axis("off")
A, B, C = 0, 60 * s, 270 * s
ax.plot([A, C + 0.5], [0, 0], color=YAZI, lw=2)
for x, ad in ((A, "A"), (B, "B"), (C, "C")):
    ax.plot([x, x], [-0.12, 0.12], color=YAZI, lw=2)
    ax.text(x, -0.25, ad, ha="center", va="top", fontsize=13, fontweight="bold")
nokta(ax, C, 0, renk=KIRMIZI)

def arac(x, renk, acik):
    ax.add_patch(patches.FancyBboxPatch((x - 0.3, 0.3), 0.6, 0.3, boxstyle="round,pad=0.02,rounding_size=0.08",
                                        facecolor=acik, edgecolor=renk, lw=1.6))
    ax.annotate("", xy=(x + 1.0, 0.45), xytext=(x + 0.36, 0.45), arrowprops=dict(arrowstyle="->", color=renk, lw=1.8))

arac(A, MAVI, MAVI_ACIK); arac(B + 0.25, SARI, SARI_ACIK)
ax.text(A - 0.3, 0.8, "90 km/sa", ha="left", va="bottom", fontsize=12, color=MAVI)
ax.text(B + 0.6, 0.8, "70 km/sa", ha="left", va="bottom", fontsize=12, color=SARI)
ax.text(C, 0.4, "3 saat sonra\nC'de yetişir", ha="center", va="bottom", fontsize=11, color=KIRMIZI)
for x1, x2, y, yazi, renk in ((A, B, -0.8, "60 km", YAZI), (B, C, -0.8, "70 · 3 = 210 km", SARI),
                              (A, C, -1.55, "90 · 3 = 270 km = 60 + 210", MAVI)):
    ax.annotate("", xy=(x1, y), xytext=(x2, y), arrowprops=dict(arrowstyle="<->", color=renk, lw=1.3))
    ax.text((x1 + x2) / 2, y - 0.1, yazi, ha="center", va="top", fontsize=11, color=renk)
ax.set_xlim(-0.4, C + 0.7); ax.set_ylim(-2.1, 1.5)
kaydet(fig, __file__)
