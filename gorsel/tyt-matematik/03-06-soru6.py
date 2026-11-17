import sys; sys.path.insert(0, "tools")
from cizim import *

# Alıştırma Soru 6: (4, 0)-(0, 4) düz doğru (x + y = 4) ve (2, 0)-(0, −2) kesikli doğru (x − y = 2). Orijinin bulunduğu sol bölge boyalı.
def kirp(cokgen, a, b, c):
    out = []
    for i in range(len(cokgen)):
        p, q = cokgen[i], cokgen[(i + 1) % len(cokgen)]
        fp, fq = a * p[0] + b * p[1] - c, a * q[0] + b * q[1] - c
        if fp <= 0: out.append(p)
        if fp * fq < 0:
            t = fp / (fp - fq); out.append((p[0] + t * (q[0] - p[0]), p[1] + t * (q[1] - p[1])))
    return out

X, Y = (-4, 6), (-5, 6)
kutu = [(X[0], Y[0]), (X[1], Y[0]), (X[1], Y[1]), (X[0], Y[1])]
fig, ax = sekil(5, 5)
eksenler(ax, x=X, y=Y)
ax.set_xticks([t for t in range(-3, 6) if t]); ax.set_yticks([t for t in range(-4, 6) if t])
ax.set_xticklabels([str(t).replace("-", "−") for t in range(-3, 6) if t])
ax.set_yticklabels([str(t).replace("-", "−") for t in range(-4, 6) if t])
bolge = kirp(kirp(kutu, 1, 1, 4), 1, -1, 2)
ax.add_patch(patches.Polygon(bolge, closed=True, facecolor=MAVI_ACIK, edgecolor="none", zorder=0.2))
xs = np.linspace(X[0], X[1], 100)
ax.plot(xs, 4 - xs, color=MAVI, zorder=3)
ax.plot(xs, xs - 2, color=MAVI, ls=(0, (6, 4)), zorder=3)
kaydet(fig, __file__)
