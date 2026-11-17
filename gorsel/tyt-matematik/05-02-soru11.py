import sys; sys.path.insert(0, "tools")
from cizim import *

# Yan yana birbirine geçmiş üç dişli: A 24, B 36, C 16 diş. Yarıçaplar diş sayısıyla orantılı.
fig, ax = sekil(6, 2.8)
ax.axis("off"); ax.set_aspect("equal")
dis = [("A", 24, MAVI, MAVI_ACIK), ("B", 36, YESIL, YESIL_ACIK), ("C", 16, SARI, SARI_ACIK)]
R = [n / 20 for _, n, _, _ in dis]
x = 0; merkez = []
for i, r in enumerate(R):
    if i: x += R[i - 1] + r
    merkez.append(x)
for (ad, n, renk, acik), r, cx in zip(dis, R, merkez):
    t = np.linspace(0, 2 * np.pi, 2000)
    rr = r + 0.07 * (np.sin(n * t) > 0) - 0.07
    ax.fill(cx + rr * np.cos(t), rr * np.sin(t), facecolor=acik, edgecolor=renk, lw=1.2)
    ax.plot(cx, 0, "o", color=renk, markersize=4)
    ax.text(cx, 0.28, ad, ha="center", va="bottom", fontsize=15, color=renk, fontweight="bold")
    ax.text(cx, -0.25, f"{n} diş", ha="center", va="top", fontsize=11, color=YAZI)
ax.set_xlim(-R[0] - 0.1, merkez[-1] + R[-1] + 0.1); ax.set_ylim(-max(R) - 0.1, max(R) + 0.1)
kaydet(fig, __file__)
