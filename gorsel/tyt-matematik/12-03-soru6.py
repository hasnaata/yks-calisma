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

# f: [−3, 4] → [−4, 5], köşeler (−3, −4), (0, −1), (2, 3), (4, 5). Artan, bire bir ve örten.
fig, ax = sekil(4.8, 5.6)
eksenler(ax, x=(-4, 5.2), y=(-5, 6))
ax.set_aspect("equal"); ax.set_xticks(range(-3, 5)); ax.set_yticks(range(-4, 6)); ax.set_xticklabels([]); ax.set_yticklabels([])
P = [(-3, -4), (0, -1), (2, 3), (4, 5)]
ax.plot(*zip(*P), color=MAVI)
nokta(ax, -3, -4, renk=MAVI); nokta(ax, 4, 5, renk=MAVI)
izdusum(ax, P)
ax.text(2.8, 4.6, "f", color=MAVI, fontsize=15, fontweight="bold")
kaydet(fig, __file__)
