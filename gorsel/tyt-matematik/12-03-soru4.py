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

# f: [−3, 3] → [−2, 4], köşeler (−3, −2), (−2, 0), (0, 3), (3, 4). Artan, bire bir.
fig, ax = sekil(5.0, 4.8)
eksenler(ax, x=(-4, 4.2), y=(-3, 5))
ax.set_aspect("equal"); ax.set_xticks(range(-3, 4)); ax.set_yticks(range(-2, 5)); ax.set_xticklabels([]); ax.set_yticklabels([])
P = [(-3, -2), (-2, 0), (0, 3), (3, 4)]
ax.plot(*zip(*P), color=MAVI)
nokta(ax, -3, -2, renk=MAVI); nokta(ax, 3, 4, renk=MAVI)
izdusum(ax, [(0, 3), (3, 4)])
ax.plot([-3, -3], [0, -2], color=SOLUK, ls="--", lw=1); ax.plot([-3, 0], [-2, -2], color=SOLUK, ls="--", lw=1)
ax.text(-3.12, -0.22, "−3", color=YAZI, fontsize=13, ha="right", va="top")
ax.text(0.18, -2, "−2", color=YAZI, fontsize=13, ha="left", va="center")
ax.text(-2.1, 0.22, "−2", color=YAZI, fontsize=13, ha="right", va="bottom")
ax.text(1.4, 3.75, "f", color=MAVI, fontsize=15, fontweight="bold")
kaydet(fig, __file__)
