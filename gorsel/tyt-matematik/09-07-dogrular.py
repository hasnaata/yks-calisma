import sys; sys.path.insert(0, "tools")
from cizim import *
from itertools import combinations

# Sol: herhangi üçü doğrusal olmayan 5 nokta, C(5,2)=10 doğru.
# Sağ: 4'ü d doğrusu üzerinde, 2'si dışarıda 6 nokta: C(6,2)-C(4,2)+1 = 10 doğru.
fig, (a1, a2) = plt.subplots(1, 2, figsize=(6.4, 3.6))
for ax in (a1, a2): ax.set_aspect("equal"); ax.axis("off")

def uzat(ax, p, q, renk, lw=1.3, k=0.18):
    p, q = np.array(p), np.array(q); u = q - p
    ax.plot(*zip(p - k * u, q + k * u), color=renk, lw=lw, zorder=1)

aci_ = np.radians(90 + 72 * np.arange(5))
P = [(np.cos(t), np.sin(t)) for t in aci_]
for p, q in combinations(P, 2): uzat(a1, p, q, MAVI, k=0.12)
for i, p in enumerate(P):
    a1.plot(*p, "o", color=YAZI, markersize=7, zorder=5)
a1.set_xlim(-1.45, 1.45); a1.set_ylim(-1.35, 1.35)
a1.set_title("5 nokta → 10 doğru", fontsize=13, color=YAZI)

D = [(0, 0), (1, 0), (2, 0), (3, 0)]
E = [(0.7, 1.9), (2.4, 1.3)]
a2.plot([-0.6, 3.6], [0, 0], color=KIRMIZI, lw=2.6, zorder=2)
a2.text(3.62, 0.08, "d", color=KIRMIZI, fontsize=13)
for e in E:
    for p in D: uzat(a2, e, p, MAVI, k=0.12)
uzat(a2, E[0], E[1], MAVI, k=0.35)
for p in D + E: a2.plot(*p, "o", color=YAZI, markersize=7, zorder=5)
a2.set_xlim(-0.7, 3.9); a2.set_ylim(-0.5, 2.4)
a2.set_title("4'ü doğrusal 6 nokta → 10 doğru", fontsize=13, color=YAZI)
fig.tight_layout()
kaydet(fig, __file__)
