import sys; sys.path.insert(0, "tools")
from cizim import *

def centik(ax, P, Q, n=1, renk=SOLUK, L=0.13, ara=0.09):
    """[PQ] kenarının ortasına n çentik (eş kenar işareti)."""
    P, Q = np.asarray(P, float), np.asarray(Q, float)
    u = (Q - P) / np.linalg.norm(Q - P); v = np.array([-u[1], u[0]]); M = (P + Q) / 2
    for k in range(n):
        c = M + (k - (n - 1) / 2) * ara * u
        ax.plot(*zip(c - L * v, c + L * v), color=renk, lw=1.6)

def olc(K, P, Q):
    a, b = np.asarray(P) - K, np.asarray(Q) - K
    return round(float(np.degrees(np.arccos(np.dot(a, b) / np.linalg.norm(a) / np.linalg.norm(b)))), 3)

def uz(P, Q): return round(float(np.linalg.norm(np.asarray(P) - np.asarray(Q))), 3)

def dik(ax, K, P, Q, k=0.25, renk=YAZI):
    K = np.asarray(K, float)
    a = (np.asarray(P) - K) / np.linalg.norm(np.asarray(P) - K); b = (np.asarray(Q) - K) / np.linalg.norm(np.asarray(Q) - K)
    ax.plot(*zip(K + k * a, K + k * (a + b), K + k * b), color=renk, lw=1.3)

def yon(d): return np.array([np.cos(np.radians(d)), np.sin(np.radians(d))])

# K.A.K.: |AO| = |OC| = 40, |BO| = |OD| = 25, ters açılar eş, |CD| = 52 -> |AB| = 52.
t = np.degrees(np.arccos((40**2 + 25**2 - 52**2) / (2 * 40 * 25)))
Oo = np.array([0.0, 0.0]); s = 0.1  # 1 birim = 10 m
A = Oo + 4.0 * yon(150); C = Oo - 4.0 * yon(150)
B = Oo + 2.5 * yon(150 + t); D = Oo - 2.5 * yon(150 + t)
print("AOB", round(t, 2), "AB", uz(A, B) * 10, "CD", uz(C, D) * 10, "OAB", olc(A, Oo, B), "OCD", olc(C, Oo, D))

fig, ax = sekil(6, 4.2)
ax.set_aspect("equal"); ax.axis("off")
M = (A + B) / 2; aci_ = np.degrees(np.arctan2(*(B - A)[::-1]))
ax.add_patch(patches.Ellipse(M, uz(A, B), 2.0, angle=aci_, facecolor=MAVI_ACIK, edgecolor=MAVI, lw=1, zorder=0))
ax.text(*(M + 0.55 * yon(aci_ + 90) * -1 + np.array([-0.3, 0])), "göl", color=MAVI, ha="center", va="center", fontsize=12, style="italic")
ax.plot(*zip(A, C), color=YAZI); ax.plot(*zip(B, D), color=YAZI)
ax.plot(*zip(A, B), color=MAVI, ls="--", lw=1.8); ax.plot(*zip(C, D), color=YESIL, lw=2.4)
centik(ax, A, Oo, 1); centik(ax, Oo, C, 1); centik(ax, B, Oo, 2); centik(ax, Oo, D, 2)
aci(ax, Oo, A, B, r=0.45, renk=KIRMIZI); aci(ax, Oo, C, D, r=0.45, renk=KIRMIZI)
nokta(ax, *A, "A", dx=-0.2, dy=0.2); nokta(ax, *B, "B", dx=-0.45, dy=-0.25); nokta(ax, *C, "C", dx=0.15, dy=-0.3)
nokta(ax, *D, "D", dx=0.15, dy=0.1); nokta(ax, *Oo, "O", dx=0.55, dy=-0.1)
ax.text(*((A + Oo) / 2 + np.array([0.1, 0.32])), "40 m", ha="center", fontsize=12)
ax.text(*((C + Oo) / 2 + np.array([0.1, 0.3])), "40 m", ha="center", fontsize=12)
ax.text(*((B + Oo) / 2 + np.array([0.38, -0.05])), "25 m", ha="left", fontsize=12)
ax.text(*((D + Oo) / 2 + np.array([-0.38, 0.0])), "25 m", ha="right", fontsize=12)
ax.text(*((C + D) / 2 + np.array([0.3, 0.0])), "52 m", ha="left", color=YESIL, fontsize=12)
ax.text(*((A + B) / 2 + np.array([0.35, 0.0])), "?", ha="left", color=MAVI, fontsize=14)
ax.set_xlim(-4.6, 4.3); ax.set_ylim(-2.9, 3.0)
kaydet(fig, __file__)
