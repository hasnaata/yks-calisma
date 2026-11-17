import sys; sys.path.insert(0, "tools")
from cizim import *

# A ile B arası 420 km. A'dan 80 km/sa, B'den 60 km/sa aynı anda birbirine doğru çıkıyor.
# Karşılaşma süresi 420 / (80 + 60) = 3 saat. A'dan çıkan 80 * 3 = 240 km, B'den çıkan 60 * 3 = 180 km gider.
s = 1 / 60  # 60 km = 1 birim
fig, ax = sekil(6.2, 3.0)
ax.axis("off")
A, C, B = 0, 240 * s, 420 * s
ax.plot([A, B], [0, 0], color=YAZI, lw=2)
for x, ad in ((A, "A"), (C, "C"), (B, "B")):
    ax.plot([x, x], [-0.12, 0.12], color=YAZI, lw=2)
    ax.text(x, -0.25, ad, ha="center", va="top", fontsize=13, fontweight="bold")
nokta(ax, C, 0, renk=KIRMIZI)

def arac(x, renk, acik, yon):
    ax.add_patch(patches.FancyBboxPatch((x - 0.35, 0.3), 0.7, 0.32, boxstyle="round,pad=0.02,rounding_size=0.08",
                                        facecolor=acik, edgecolor=renk, lw=1.6))
    ax.annotate("", xy=(x + yon * 1.15, 0.46), xytext=(x + yon * 0.42, 0.46), arrowprops=dict(arrowstyle="->", color=renk, lw=1.8))

arac(A + 0.35, MAVI, MAVI_ACIK, 1)
arac(B - 0.35, SARI, SARI_ACIK, -1)
ax.text(A + 0.35, 0.8, "80 km/sa", ha="center", va="bottom", fontsize=12, color=MAVI)
ax.text(B - 0.35, 0.8, "60 km/sa", ha="center", va="bottom", fontsize=12, color=SARI)
ax.text(C, 0.95, "3 saat sonra\nC'de karşılaşırlar", ha="center", va="bottom", fontsize=11, color=KIRMIZI)
# alt ölçüler
for x1, x2, y, yazi, renk in ((A, C, -0.8, "80 · 3 = 240 km", MAVI), (C, B, -0.8, "60 · 3 = 180 km", SARI),
                              (A, B, -1.55, "|AB| = 420 km = (80 + 60) · 3", YAZI)):
    ax.annotate("", xy=(x1, y), xytext=(x2, y), arrowprops=dict(arrowstyle="<->", color=renk, lw=1.3))
    ax.text((x1 + x2) / 2, y - 0.1, yazi, ha="center", va="top", fontsize=11, color=renk)
ax.set_xlim(-0.3, B + 0.3); ax.set_ylim(-2.1, 1.75)
kaydet(fig, __file__)
