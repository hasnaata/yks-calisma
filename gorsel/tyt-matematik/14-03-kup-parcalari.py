import sys; sys.path.insert(0, "tools")
from cizim import *

# (a + b)^3 küpü 8 parçaya ayrılır: 1 tane a³, 3 tane a²b, 3 tane ab², 1 tane b³.
# a = 2, b = 1 birim (orantılı). Eğik izdüşüm: derinlik yukarı-sağa.
A, B, ARA = 2.0, 1.0, 0.5
C, S = 0.8 * np.cos(np.radians(32)), 0.8 * np.sin(np.radians(32))
def p(x, y, z): return (x + C * y, z + S * y)

RENK = {3: (MAVI_ACIK, MAVI), 2: (YESIL_ACIK, YESIL), 1: (SARI_ACIK, SARI), 0: (KIRMIZI_ACIK, KIRMIZI)}

def kutu(ax, x0, y0, z0, gx, gy, gz, dolgu, kenar):
    X, Y, Z = x0 + gx, y0 + gy, z0 + gz
    yuzler = [
        [p(x0, y0, z0), p(X, y0, z0), p(X, y0, Z), p(x0, y0, Z)],      # ön
        [p(x0, y0, Z), p(X, y0, Z), p(X, Y, Z), p(x0, Y, Z)],          # üst
        [p(X, y0, z0), p(X, Y, z0), p(X, Y, Z), p(X, y0, Z)],          # sağ
    ]
    tonlar = [dolgu, "white", dolgu]
    for yuz, ton in zip(yuzler, tonlar):
        ax.add_patch(patches.Polygon(yuz, closed=True, facecolor=ton, edgecolor=kenar, lw=1.6))

fig, ax = sekil(6.2, 3.6)
ax.axis("off"); ax.set_aspect("equal")
# Parçalar: her eksende "a" ya da "b" seçilir; a sayısı rengi belirler.
parcalar = []
for ix, gx in ((0, A), (1, B)):
    for iy, gy in ((0, A), (1, B)):
        for iz, gz in ((0, A), (1, B)):
            x0 = 0 if ix == 0 else A + ARA
            y0 = 0 if iy == 0 else A + ARA
            z0 = 0 if iz == 0 else A + ARA
            kac_a = (gx == A) + (gy == A) + (gz == A)
            parcalar.append((y0, z0, x0, gx, gy, gz, kac_a))
# çizim sırası: arkadan öne (büyük y önce), alttan üste, soldan sağa
for y0, z0, x0, gx, gy, gz, k in sorted(parcalar, key=lambda t: (-t[0], t[1], t[2])):
    kutu(ax, x0, y0, z0, gx, gy, gz, *RENK[k])

# sağda açıklama
satirlar = [(3, r"$1 \times a^3$"), (2, r"$3 \times a^2b$"), (1, r"$3 \times ab^2$"), (0, r"$1 \times b^3$")]
for i, (k, yazi) in enumerate(satirlar):
    yy = 4.3 - i * 1.05
    ax.add_patch(patches.Rectangle((6.5, yy - 0.3), 0.6, 0.6, facecolor=RENK[k][0], edgecolor=RENK[k][1], lw=1.6))
    ax.text(7.35, yy, yazi, va="center", fontsize=17, color=RENK[k][1])
ax.set_xlim(-0.2, 9.3); ax.set_ylim(-0.3, 5.3)
kaydet(fig, __file__)
