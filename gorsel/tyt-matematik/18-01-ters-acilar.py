import sys; sys.path.insert(0, "tools")
from cizim import *

# O'da kesişen iki doğru: d1 yatay, d2 yatayla 70° yapıyor. Ters açılar 70° ve 110°.
def yon(d): return np.array([np.cos(np.radians(d)), np.sin(np.radians(d))])
O = np.array([0.0, 0.0]); L = 2.2
fig, ax = sekil(5, 3.6)
ax.set_aspect("equal"); ax.axis("off")
for d, ad in ((0, "d₁"), (70, "d₂")):
    P, Q = O + L * yon(d), O - L * yon(d)
    ax.annotate("", xy=P, xytext=Q, arrowprops=dict(arrowstyle="<|-|>", color=YAZI, lw=2, mutation_scale=14))
    ax.text(*(P + 0.25 * yon(d) + [0, 0.05]), ad, color=SOLUK, ha="center", va="center")
ax.plot(*O, "o", color=YAZI, markersize=6); ax.text(-0.3, -0.22, "O", fontsize=13, ha="center", va="center")
for a1, a2, r, renk in ((0, 70, 0.55, MAVI), (180, 250, 0.55, MAVI), (70, 180, 0.4, KIRMIZI), (250, 360, 0.4, KIRMIZI)):
    ax.add_patch(patches.Arc(O, 2 * r, 2 * r, theta1=a1, theta2=a2, color=renk, lw=1.8))
    m = np.radians((a1 + a2) / 2); rr = 1.0 if renk == MAVI else 0.85
    ax.text(*(O + rr * np.array([np.cos(m), np.sin(m)])), f"{a2 - a1}°", color=renk, fontsize=13, ha="center", va="center")
ax.set_xlim(-2.6, 2.7); ax.set_ylim(-2.3, 2.4)
kaydet(fig, __file__)
