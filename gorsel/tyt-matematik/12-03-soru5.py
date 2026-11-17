import sys; sys.path.insert(0, "tools")
from cizim import *

def eksi(v): return str(v).replace("-", "−")

def izdusum(ax, pts, xsol=(), yust=()):
    """Köşelerden eksenlere kesikli çizgi ve eksen etiketleri."""
    gx, gy = set(), set()
    for x, y in pts:
        if x != 0 and y != 0:
            ax.plot([x, x], [0, y], color=SOLUK, ls="--", lw=1)
            ax.plot([0, x], [y, y], color=SOLUK, ls="--", lw=1)
        if x != 0 and x not in gx:
            gx.add(x)
            ust = (y < 0) if x not in xsol else (y > 0)
            ax.text(x, 0.22 if ust else -0.22, eksi(x), color=YAZI, fontsize=13, ha="center", va="bottom" if ust else "top")
        if y != 0 and y not in gy:
            gy.add(y)
            sag = (x < 0) if y not in yust else (x > 0)
            ax.text(0.18 if sag else -0.18, y, eksi(y), color=YAZI, fontsize=13, ha="left" if sag else "right", va="center")

# Doğrusal f: eksenleri (4, 0) ve (0, −2) noktalarında keser. f(x) = x/2 − 2.
fig, ax = sekil(4.8, 3.8)
eksenler(ax, x=(-2.2, 7.2), y=(-3.6, 2.6))
ax.set_aspect("equal"); ax.set_xticks(range(-2, 8)); ax.set_yticks(range(-3, 3)); ax.set_xticklabels([]); ax.set_yticklabels([])
xs = np.array([-1.8, 7]); ax.plot(xs, xs / 2 - 2, color=MAVI)
nokta(ax, 4, 0, renk=MAVI); nokta(ax, 0, -2, renk=MAVI)
ax.text(4, 0.22, "4", color=YAZI, fontsize=13, ha="center", va="bottom")
ax.text(0.2, -2.25, "−2", color=YAZI, fontsize=13, ha="left", va="top")
ax.text(5.6, 1.25, "f", color=MAVI, fontsize=15, fontweight="bold")
kaydet(fig, __file__)
