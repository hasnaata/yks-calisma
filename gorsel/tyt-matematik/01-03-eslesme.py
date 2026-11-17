import sys; sys.path.insert(0, "tools")
from cizim import *

# Çift sayı = noktalar ikişerli eşleşir. Tek sayıda bir nokta (kırmızı) eşsiz kalır.
SATIRLAR = [(6, 4), (5, 7), (5, 4)]
fig, ax = sekil(6, 4.2)
ax.axis("off"); ax.set_aspect("equal")
ARA = 0.55

def grup(x0, y0, n):
    """n noktayı iki sıra halinde çizer; eşsiz kalan son nokta kırmızı. Bitiş x'ini ve eşsiz noktayı döndürür."""
    cift = n // 2
    for i in range(cift):
        for j in range(2):
            ax.plot(x0 + i * ARA, y0 - j * ARA, "o", color=MAVI, markersize=11)
    eşsiz = None
    if n % 2:
        eşsiz = (x0 + cift * ARA, y0)
        ax.plot(*eşsiz, "o", color=KIRMIZI, markersize=11)
    genislik = (cift + (n % 2)) * ARA
    ax.add_patch(patches.FancyBboxPatch((x0 - 0.3, y0 - ARA - 0.3), genislik + 0.05, ARA + 0.6,
                 boxstyle="round,pad=0.02,rounding_size=0.15", fill=False, edgecolor=CIZGI, lw=1.2))
    return x0 + genislik, eşsiz

for k, (a, b) in enumerate(SATIRLAR):
    y = -k * 2.0
    ax.text(-0.5, y - ARA / 2, f"{a} + {b}", ha="right", va="center", fontsize=14)
    x1, e1 = grup(0.3, y, a)
    ax.text(x1 + 0.1, y - ARA / 2, "+", ha="center", va="center", fontsize=16, color=SOLUK)
    x2, e2 = grup(x1 + 0.55, y, b)
    toplam = a + b
    renk = MAVI if toplam % 2 == 0 else KIRMIZI
    ax.text(x2 + 0.15, y - ARA / 2, f"= {toplam}  {'çift' if toplam % 2 == 0 else 'tek'}",
            ha="left", va="center", fontsize=14, color=renk, fontweight="bold")
    if e1 and e2:
        ax.annotate("", xy=(e2[0], e2[1] + 0.22), xytext=(e1[0], e1[1] + 0.22),
                    arrowprops=dict(arrowstyle="<->", color=KIRMIZI, lw=1.6, linestyle="--",
                                    connectionstyle="arc3,rad=-0.35"))
ax.set_xlim(-2.4, 9.2); ax.set_ylim(-5.1, 1.1)
kaydet(fig, __file__)
