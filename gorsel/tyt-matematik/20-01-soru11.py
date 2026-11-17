import sys; sys.path.insert(0, "tools")
from cizim import *

# m(A)=80, m(B)=60, m(C)=40. B ve C'deki dış açıortaylar D'de kesişir. x = m(ADB) = m(C)/2 = 20.
B = np.array([0.0, 0.0]); C = np.array([5.0, 0.0])
t = 5 * np.sin(np.radians(40)) / np.sin(np.radians(80))
A = B + t * np.array([np.cos(np.radians(60)), np.sin(np.radians(60))])
a, b, c = np.linalg.norm(B - C), np.linalg.norm(A - C), np.linalg.norm(A - B)
D = (-a * A + b * B + c * C) / (-a + b + c)
def derece(p, k, q):
    v, w = p - k, q - k
    return np.degrees(np.arccos(np.dot(v, w) / np.linalg.norm(v) / np.linalg.norm(w)))
Bx = B + 1.5 * (B - A) / c; Cx = C + 1.5 * (C - A) / b
print("ADB", derece(A, D, B), "BDC", derece(B, D, C), "BAD", derece(B, A, D))

def isaret(kose, p, q, rr, renk, n):
    aci(ax, kose, p, q, r=rr, renk=renk)
    a1 = np.arctan2(*(p - kose)[::-1]); a2 = np.arctan2(*(q - kose)[::-1])
    if (a2 - a1) % (2 * np.pi) > np.pi: a1, a2 = a2, a1
    o = a1 + ((a2 - a1) % (2 * np.pi)) / 2
    for k in range(n):
        oo = o + (k - (n - 1) / 2) * 0.08
        u = np.array([np.cos(oo), np.sin(oo)])
        ax.plot(*zip(kose + (rr - 0.12) * u, kose + (rr + 0.12) * u), color=renk, lw=1.6)

fig, ax = sekil(5.4, 5.2)
ax.set_aspect("equal"); ax.axis("off")
ax.plot(*zip(A, B, C, A), color=YAZI)
ax.plot(*zip(B, Bx), color=YAZI, lw=1.6, ls="--"); ax.plot(*zip(C, Cx), color=YAZI, lw=1.6, ls="--")
ax.plot(*zip(B, D), color=MAVI, lw=2); ax.plot(*zip(C, D), color=MAVI, lw=2)
ax.plot(*zip(A, D), color=YESIL, lw=2)
nokta(ax, *A, "A", dx=-0.12, dy=0.22); nokta(ax, *B, "B", dx=-0.5, dy=0.05); nokta(ax, *C, "C", dx=0.2, dy=0.05)
nokta(ax, *D, "D", dx=0.2, dy=-0.25, renk=MAVI)
isaret(B, Bx, D, 0.7, SARI, 1); isaret(B, D, C, 0.7, SARI, 1)
isaret(C, B, D, 0.7, KIRMIZI, 2); isaret(C, D, Cx, 0.7, KIRMIZI, 2)
aci(ax, A, B, C, r=0.55, renk=YAZI)
ax.text(A[0] + 0.2, A[1] - 1.1, "80°", color=YAZI, fontsize=11, ha="left")
aci(ax, B, C, A, r=0.45, renk=YAZI)
ax.text(B[0] + 0.75, B[1] + 0.3, "60°", color=YAZI, fontsize=11, ha="center")
aci(ax, D, A, B, r=1.3, renk=YESIL)
ax.text(D[0] - 0.62, D[1] + 1.6, "x", color=YESIL, fontsize=14, ha="center")
ax.set_xlim(min(Bx[0], D[0]) - 0.8, max(Cx[0], C[0]) + 0.8); ax.set_ylim(D[1] - 0.6, A[1] + 0.6)
kaydet(fig, __file__)
