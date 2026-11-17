import sys; sys.path.insert(0, "tools")
from cizim import *
from sympy import isprime

# Ders: 1'den 50'ye kadar sayılar; asallar mavi, 1 gri, bileşikler soluk.
fig, ax = sekil(6, 3.4)
ax.axis("off"); ax.set_aspect("equal")
for n in range(1, 51):
    i, j = (n - 1) % 10, (n - 1) // 10
    x, y = i * 1.0, -j * 1.0
    if isprime(n):
        yuz, ken, renk, kalin = MAVI_ACIK, MAVI, MAVI, "bold"
    elif n == 1:
        yuz, ken, renk, kalin = "#eeeeee", SOLUK, SOLUK, "normal"
    else:
        yuz, ken, renk, kalin = "white", CIZGI, SOLUK, "normal"
    ax.add_patch(patches.FancyBboxPatch((x + 0.05, y + 0.05), 0.9, 0.9, boxstyle="round,pad=0,rounding_size=0.1",
                                        facecolor=yuz, edgecolor=ken, lw=1.3))
    ax.text(x + 0.5, y + 0.5, str(n), ha="center", va="center", fontsize=14, color=renk, fontweight=kalin)
ax.set_xlim(-0.05, 10.05); ax.set_ylim(-4.05, 1.05)
kaydet(fig, __file__)
