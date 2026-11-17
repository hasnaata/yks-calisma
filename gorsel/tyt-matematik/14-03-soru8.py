import sys; sys.path.insert(0, "tools")
from cizim import *

# Kenarı a = 7 cm olan küpün sağ üst ön köşesinden kenarı b = 5 cm olan küp çıkarılmış (ölçekli).
# Üst ön kenarın kesilmeyen parçası a - b = 2 cm.
A, B = 7.0, 5.0
C, S = 0.55 * np.cos(np.radians(32)), 0.55 * np.sin(np.radians(32))
def p(x, y, z): return (x + C * y, z + S * y)

fig, ax = sekil(4.6, 4.4)
ax.axis("off"); ax.set_aspect("equal")
def yuz(noktalar, dolgu, kenar=MAVI):
    ax.add_patch(patches.Polygon([p(*n) for n in noktalar], closed=True, facecolor=dolgu, edgecolor=kenar, lw=1.8, joinstyle="round"))

k = A - B
# oyuğun iç yüzleri (önce çizilir)
yuz([(k, B, k), (A, B, k), (A, B, A), (k, B, A)], "#d5e3f7")          # arka duvar
yuz([(k, 0, k), (A, 0, k), (A, B, k), (k, B, k)], "white")            # taban
yuz([(k, 0, k), (k, B, k), (k, B, A), (k, 0, A)], "#d5e3f7")          # sol duvar
# dış yüzler
yuz([(0, 0, 0), (A, 0, 0), (A, 0, k), (k, 0, k), (k, 0, A), (0, 0, A)], MAVI_ACIK)          # ön
yuz([(0, 0, A), (k, 0, A), (k, B, A), (A, B, A), (A, A, A), (0, A, A)], "white")            # üst
yuz([(A, 0, 0), (A, A, 0), (A, A, A), (A, B, A), (A, B, k), (A, 0, k)], MAVI_ACIK)          # sağ

# ölçüler
x0, x1 = p(0, 0, A), p(k, 0, A)
ax.annotate("", xy=(x1[0], A - 0.3), xytext=(x0[0], A - 0.3), arrowprops=dict(arrowstyle="<->", color=KIRMIZI, lw=1.3))
ax.text((x0[0] + x1[0]) / 2, A - 0.5, "2 cm", ha="center", va="top", fontsize=14, color=KIRMIZI)
ax.annotate("", xy=(A, -0.55), xytext=(0, -0.55), arrowprops=dict(arrowstyle="<->", color=SOLUK, lw=1.3))
ax.text(A / 2, -0.75, "?", ha="center", va="top", fontsize=17)
ax.set_xlim(-0.4, A + C * A + 0.4); ax.set_ylim(-1.8, A + S * A + 0.4)
kaydet(fig, __file__)
