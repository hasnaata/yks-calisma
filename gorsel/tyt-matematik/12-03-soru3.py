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

# f: [−4, 5] → R, köşeler (−4, 2), (−1, −1), (2, 2), (5, −1). x eksenini −2, 0, 4'te keser.
fig, ax = sekil(5.6, 3.8)
eksenler(ax, x=(-5, 6.2), y=(-2, 3))
ax.set_aspect("equal"); ax.set_xticks(range(-4, 6)); ax.set_yticks(range(-1, 3)); ax.set_xticklabels([]); ax.set_yticklabels([])
P = [(-4, 2), (-1, -1), (2, 2), (5, -1)]
ax.plot(*zip(*P), color=MAVI)
nokta(ax, -4, 2, renk=MAVI); nokta(ax, 5, -1, renk=MAVI)
izdusum(ax, P, xsol=(), yust=())
for t in ax.texts:
    if t.get_text() in ("2", "−1") and t.get_position()[0] > 0 and t.get_position()[0] < 1:
        t.set_bbox(dict(facecolor="white", edgecolor="none", pad=0.5))  # y eksenindeki 2 ve −1, kesikli çizginin üstünde okunsun
ax.text(-2.1, -0.22, "−2", color=YAZI, fontsize=13, ha="right", va="top")
ax.text(4, -0.22, "4", color=YAZI, fontsize=13, ha="center", va="top")
ax.text(3.3, 1.5, "f", color=MAVI, fontsize=15, fontweight="bold")
kaydet(fig, __file__)
