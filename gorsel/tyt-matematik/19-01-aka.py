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

# A.K.A.: A, B, C doğrusal; DA ⟂ AC, EC ⟂ AC, |DB| = |BE|, DB ⟂ BE. |AD| = 4, |CE| = 9 -> |AB| = 9, |BC| = 4, |AC| = 13.
A = np.array([0.0, 0.0]); B = np.array([9.0, 0.0]); C = np.array([13.0, 0.0]); D = np.array([0.0, 4.0]); E = np.array([13.0, 9.0])
print("DB", uz(D, B), "BE", uz(B, E), "DBE", olc(B, D, E), "ADB", olc(D, A, B), "CBE", olc(B, C, E), "ABD", olc(B, A, D), "CEB", olc(E, C, B))
fig, ax = sekil(5.6, 4.2)
ax.set_aspect("equal"); ax.axis("off")
ax.add_patch(patches.Polygon([A, B, D], closed=True, facecolor=MAVI_ACIK, edgecolor="none", zorder=0))
ax.add_patch(patches.Polygon([B, C, E], closed=True, facecolor=YESIL_ACIK, edgecolor="none", zorder=0))
ax.plot(*zip(A, C), color=YAZI); ax.plot(*zip(A, D), color=YAZI); ax.plot(*zip(C, E), color=YAZI)
ax.plot(*zip(D, B), color=YAZI); ax.plot(*zip(B, E), color=YAZI)
centik(ax, D, B, 1, L=0.25); centik(ax, B, E, 1, L=0.25)
dik(ax, A, B, D, k=0.55); dik(ax, C, A, E, k=0.55); dik(ax, B, D, E, k=0.55)
aci(ax, D, A, B, r=1.0, ad="α", renk=KIRMIZI); aci(ax, B, C, E, r=1.0, ad="α", renk=KIRMIZI)
aci(ax, B, A, D, r=1.6, ad="β", renk=SARI); aci(ax, E, C, B, r=1.6, ad="β", renk=SARI)
nokta(ax, *A, "A", dx=-0.7, dy=-0.8); nokta(ax, *B, "B", dx=-0.3, dy=-1.0); nokta(ax, *C, "C", dx=0.25, dy=-0.8)
nokta(ax, *D, "D", dx=-0.8, dy=0.1); nokta(ax, *E, "E", dx=0.25, dy=0.1)
ax.text(-0.35, 2.0, "4", ha="right", va="center"); ax.text(13.35, 4.5, "9", ha="left", va="center")
ax.set_xlim(-1.4, 14.4); ax.set_ylim(-1.3, 10.0)
kaydet(fig, __file__)
