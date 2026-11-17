import sys; sys.path.insert(0, "tools")
from cizim import *

# Ders örneği: 2x + y ≤ 6 (düz, mavi taraf) ve x − y < 3 (kesikli, sarı taraf). Ortak bölge yeşil; (3, 0) köşesi dahil değil.
def kirp(cokgen, a, b, c):
    """cokgen içinden a·x + b·y ≤ c tarafını bırakır."""
    out = []
    for i in range(len(cokgen)):
        p, q = cokgen[i], cokgen[(i + 1) % len(cokgen)]
        fp, fq = a * p[0] + b * p[1] - c, a * q[0] + b * q[1] - c
        if fp <= 0: out.append(p)
        if fp * fq < 0:
            t = fp / (fp - fq); out.append((p[0] + t * (q[0] - p[0]), p[1] + t * (q[1] - p[1])))
    return out

X, Y = (-4, 6.5), (-5, 7.5)
kutu = [(X[0], Y[0]), (X[1], Y[0]), (X[1], Y[1]), (X[0], Y[1])]
fig, ax = sekil(5.2, 5.4)
eksenler(ax, x=X, y=Y)
ax.set_xticks([t for t in range(-3, 7) if t]); ax.set_yticks([t for t in range(-4, 8) if t])
ax.set_xticklabels([str(t).replace("-", "−") for t in range(-3, 7) if t])
ax.set_yticklabels([str(t).replace("-", "−") for t in range(-4, 8) if t])
b1 = kirp(kutu, 2, 1, 6)            # 2x + y ≤ 6
b2 = kirp(kutu, 1, -1, 3)           # x − y < 3
ortak = kirp(b1, 1, -1, 3)
ax.add_patch(patches.Polygon(b1, closed=True, facecolor=MAVI_ACIK, edgecolor="none", zorder=0.2))
ax.add_patch(patches.Polygon(b2, closed=True, facecolor=SARI_ACIK, edgecolor="none", zorder=0.2))
ax.add_patch(patches.Polygon(ortak, closed=True, facecolor="#cfe9d8", edgecolor="none", zorder=0.3))
xs = np.linspace(X[0], X[1], 100)
ax.plot(xs, 6 - 2 * xs, color=MAVI, zorder=3)
ax.plot(xs, xs - 3, color=SARI, ls=(0, (6, 4)), zorder=3)
nokta(ax, 3, 0, "", renk=YAZI, dolu=False)
ax.text(-3.7, 6.6, "ortak bölge", color=YESIL, fontsize=13, fontweight="bold")
ax.text(0.55, 6.6, "2x + y = 6", color=MAVI, fontsize=12)
ax.text(3.0, -4.6, "x − y = 3", color=SARI, fontsize=12)
kaydet(fig, __file__)
