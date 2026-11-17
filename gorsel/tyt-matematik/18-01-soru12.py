import sys; sys.path.insert(0, "tools")
from cizim import *

def yon(d): return np.array([np.cos(np.radians(d)), np.sin(np.radians(d))])
O = np.array([0.0, 0.0])
def isin(ax, d, ad="", L=2.3, renk=YAZI, ls="-", dxy=(0, 0)):
    P = O + L * yon(d)
    ax.annotate("", xy=P, xytext=O, arrowprops=dict(arrowstyle="-|>", color=renk, lw=2, ls=ls, mutation_scale=14))
    if ad: ax.text(*(P + 0.25 * yon(d) + np.array(dxy)), ad, color=renk, ha="center", va="center", fontsize=13)
def dogru(ax, d, ad="", L=2.3):
    P, Q = O + L * yon(d), O - L * yon(d)
    ax.annotate("", xy=P, xytext=Q, arrowprops=dict(arrowstyle="<|-|>", color=YAZI, lw=2, mutation_scale=14))
    if ad: ax.text(*(P + 0.28 * yon(d)), ad, color=SOLUK, ha="center", va="center")
def yay(ax, a1, a2, r, ad="", renk=MAVI, rr=None, centik=0, fs=12):
    ax.add_patch(patches.Arc(O, 2 * r, 2 * r, theta1=a1, theta2=a2, color=renk, lw=1.7))
    m = (a1 + a2) / 2
    for k in range(centik):
        t = np.radians(m + (k - (centik - 1) / 2) * 5)
        ax.plot([(r - 0.09) * np.cos(t), (r + 0.09) * np.cos(t)], [(r - 0.09) * np.sin(t), (r + 0.09) * np.sin(t)], color=renk, lw=1.5)
    if ad:
        rr = rr if rr is not None else r + 0.4
        ax.text(*(rr * yon(m)), ad, color=renk, fontsize=fs, ha="center", va="center")
def kose(ax, ad="O", dxy=(0, -0.35)):
    ax.plot(*O, "o", color=YAZI, markersize=6); ax.text(dxy[0], dxy[1], ad, ha="center", va="center", fontsize=13)

# Soru 12: AOB=40°, BOC=60° (oran 2:3). [OD ve [OE açıortaylar; m(DOE)=20+30=50°.
fig, ax = sekil(5, 3.6); ax.set_aspect("equal"); ax.axis("off")
isin(ax, 0, "A", dxy=(0, -0.3)); isin(ax, 40, "B"); isin(ax, 100, "C")
isin(ax, 20, "D", renk=MAVI, ls="--"); isin(ax, 70, "E", renk=KIRMIZI, ls="--")
kose(ax)
yay(ax, 0, 20, 0.9, renk=MAVI, centik=1); yay(ax, 20, 40, 0.9, renk=MAVI, centik=1)
yay(ax, 40, 70, 0.9, renk=KIRMIZI, centik=2); yay(ax, 70, 100, 0.9, renk=KIRMIZI, centik=2)
yay(ax, 20, 70, 1.55, renk=YESIL)
ax.text(*(1.95 * yon(58)), "50°", color=YESIL, fontsize=12, ha="center", va="center")
ax.set_xlim(-1.2, 2.9); ax.set_ylim(-0.6, 2.8)
kaydet(fig, __file__)
