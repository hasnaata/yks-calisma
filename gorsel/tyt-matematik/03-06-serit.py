import sys; sys.path.insert(0, "tools")
from cizim import *

# Ders örneği: 2x − y ≥ −2 (düz, y = 2x + 2) ve 2x − y < 4 (kesikli, y = 2x − 4). Paralel doğrular arasında şerit.
X, Y = (-4, 5.5), (-5, 6.5)
fig, ax = sekil(5, 5)
eksenler(ax, x=X, y=Y)
ax.set_xticks([t for t in range(-3, 6) if t]); ax.set_yticks([t for t in range(-4, 7) if t])
ax.set_xticklabels([str(t).replace("-", "−") for t in range(-3, 6) if t])
ax.set_yticklabels([str(t).replace("-", "−") for t in range(-4, 7) if t])
xs = np.linspace(X[0], X[1], 200)
ust, alt = 2 * xs + 2, 2 * xs - 4
ax.fill_between(xs, np.clip(alt, Y[0], Y[1]), np.clip(ust, Y[0], Y[1]), color=MAVI_ACIK, zorder=0.2)
ax.plot(xs, ust, color=MAVI, zorder=3)
ax.plot(xs, alt, color=MAVI, ls=(0, (6, 4)), zorder=3)
nokta(ax, -1, 0, "", renk=MAVI); nokta(ax, 0, 2, "", renk=MAVI)
nokta(ax, 2, 0, "", renk=MAVI, dolu=False); nokta(ax, 0, -4, "", renk=MAVI, dolu=False)
ax.set_ylim(*Y)
ax.text(-3.8, 3.6, "2x − y = −2", color=MAVI, fontsize=12)
ax.text(2.7, -2.6, "2x − y = 4", color=MAVI, fontsize=12)
kaydet(fig, __file__)
