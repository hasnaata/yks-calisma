import sys; sys.path.insert(0, "tools")
from cizim import *

# Düzgün beşgen ve düzgün altıgen. Bir köşede iç açı (mavi) ve dış açı (kırmızı): 108° + 72°, 120° + 60°.
def duzgun(n, merkez, r, bas=-90):
    t = np.radians(bas + 180 / n + 360 / n * np.arange(n))  # alt kenar yatay
    return np.column_stack([merkez[0] + r * np.cos(t), merkez[1] + r * np.sin(t)])

def centik(ax, P, Q, renk=SOLUK):
    m = (P + Q) / 2; d = (Q - P) / np.linalg.norm(Q - P); nrm = np.array([-d[1], d[0]])
    ax.plot(*zip(m - 0.13 * nrm, m + 0.13 * nrm), color=renk, lw=1.6)

fig, ax = sekil(6.4, 3.6)
ax.set_aspect("equal"); ax.axis("off")
for n, M, ic, dis, ad in ((5, (0, 0), "108°", "72°", "düzgün beşgen"), (6, (5.0, 0), "120°", "60°", "düzgün altıgen")):
    r = 1.0 / (2 * np.sin(np.pi / n)) * 2.0     # kenar 2
    V = duzgun(n, M, r)
    ax.add_patch(patches.Polygon(V, closed=True, facecolor=MAVI_ACIK, edgecolor=YAZI, lw=2.4))
    for i in range(n): centik(ax, V[i], V[(i + 1) % n])
    # sağ alt köşe V[0]; alt kenar V[n-1] -> V[0], uzantısı V[0]'ın ötesine
    P, Q = V[n - 1], V[0]; u = (Q - P) / np.linalg.norm(Q - P); U = Q + 1.4 * u
    ax.plot(*zip(Q, U), color=SOLUK, lw=1.6, ls="--")
    aci(ax, Q, P, V[1], r=0.5, ad=ic, renk=MAVI)
    aci(ax, Q, U, V[1], r=0.5, ad=dis, renk=KIRMIZI)
    ax.text(M[0], V[:, 1].min() - 0.55, ad, ha="center", va="top", fontsize=13)
ax.set_xlim(-2.2, 7.6); ax.set_ylim(-2.5, 2.4)
kaydet(fig, __file__)
