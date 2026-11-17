import sys; sys.path.insert(0, "tools")
from cizim import *

def uz(P, Q): return round(float(np.linalg.norm(np.asarray(P) - np.asarray(Q))), 3)
def ucgen(a, b, c):
    """|BC|=a, |CA|=b, |AB|=c. B orijinde, C x ekseninde."""
    x = (c**2 - b**2 + a**2) / (2 * a)
    return np.array([x, np.sqrt(c**2 - x**2)]), np.array([0.0, 0.0]), np.array([float(a), 0.0])
def kenar(ax, P, Q, metin, G, d=0.45, renk=YAZI, fs=13):
    P, Q = np.asarray(P, float), np.asarray(Q, float); M = (P + Q) / 2
    u = (Q - P) / np.linalg.norm(Q - P); v = np.array([-u[1], u[0]])
    if np.dot(v, M - np.asarray(G)) < 0: v = -v
    ax.text(*(M + d * v), metin, ha="center", va="center", color=renk, fontsize=fs)
def dik_ayak(P, Q, R):
    """R noktasından PQ doğrusuna inen dikmenin ayağı."""
    u = (Q - P) / np.linalg.norm(Q - P); return P + np.dot(R - P, u) * u

def dik(ax, K, P, Q, s=0.3, renk=SOLUK):
    """K köşesinde KP ile KQ arasındaki dik açı işareti."""
    u = (P - K) / np.linalg.norm(P - K) * s; v = (Q - K) / np.linalg.norm(Q - K) * s
    ax.plot(*zip(K + u, K + u + v, K + v), color=renk, lw=1.3)
def aci_olc(K, P, Q):
    u, v = P - K, Q - K
    return round(float(np.degrees(np.arccos(np.dot(u, v) / np.linalg.norm(u) / np.linalg.norm(v)))), 3)

def centik(ax, P, Q, n=1, renk=SOLUK, L=0.18, ara=0.12):
    P, Q = np.asarray(P, float), np.asarray(Q, float)
    u = (Q - P) / np.linalg.norm(Q - P); v = np.array([-u[1], u[0]]); M = (P + Q) / 2
    for k in range(n):
        c = M + (k - (n - 1) / 2) * ara * u
        ax.plot(*zip(c - L * v, c + L * v), color=renk, lw=1.6)

def olcu(ax, P, Q, metin, Gm, d=0.55, renk=SOLUK, yazi=YAZI, ek=0.4):
    """[PQ] boyunca, şeklin dışına doğru oklu ölçü çizgisi ve etiketi."""
    P, Q = np.asarray(P, float), np.asarray(Q, float)
    u = (Q - P) / np.linalg.norm(Q - P); v = np.array([-u[1], u[0]])
    if np.dot(v, (P + Q) / 2 - np.asarray(Gm)) < 0: v = -v
    ax.annotate("", xy=Q + d * v, xytext=P + d * v, arrowprops=dict(arrowstyle="<->", color=renk, lw=1.2))
    ax.text(*((P + Q) / 2 + (d + ek) * v), metin, ha="center", va="center", fontsize=13, color=yazi)

# Soru 8: arsa ABC, |AB|=60 m, |AC|=40 m, alan 1000 m² (sin A = 5/6, A dar). Ölçek: 1 birim = 10 m.
# Çit [AD], A açısının açıortayı: A(ABD)/A(ADC) = 60/40 -> A(ABD) = 600 m².
cosA = np.sqrt(11) / 6
a = np.sqrt(36 + 16 - 2 * 6 * 4 * cosA)
A, B, C = ucgen(a, 4, 6)
D = B + (C - B) * 6 / 10
def alan(P, Q, R): return abs(float((Q - P)[0] * (R - P)[1] - (Q - P)[1] * (R - P)[0])) / 2
print("BC(m)", round(10 * a, 2), "alan m²", round(100 * alan(A, B, C), 3), "ABD", round(100 * alan(A, B, D), 3), "ADC", round(100 * alan(A, D, C), 3), "BAD", aci_olc(A, B, D), "DAC", aci_olc(A, D, C))
Gm = (A + B + C) / 3

fig, ax = sekil(4.6, 3.6)
ax.set_aspect("equal"); ax.axis("off")
ax.add_patch(plt.Polygon([A, B, D], color=MAVI_ACIK, lw=0))
ax.add_patch(plt.Polygon([A, D, C], color=YESIL_ACIK, lw=0))
ax.plot(*zip(A, B, C, A), color=YAZI)
ax.plot(*zip(A, D), color=KIRMIZI, lw=2.4)
aci(ax, A, B, D, r=0.8, ad="α", renk=KIRMIZI); aci(ax, A, D, C, r=0.95, ad="α", renk=KIRMIZI)
nokta(ax, *A, "A", dx=-0.15, dy=0.2); nokta(ax, *B, "B", dx=-0.45, dy=-0.4); nokta(ax, *C, "C", dx=0.12, dy=-0.4)
nokta(ax, *D, "D", dx=-0.12, dy=-0.5, renk=KIRMIZI)
kenar(ax, A, B, "60 m", Gm, d=0.55); kenar(ax, A, C, "40 m", Gm, d=0.85)
ax.text(*(A + 0.72 * (D - A) + np.array([-0.4, 0.0])), "çit", color=KIRMIZI, fontsize=12, ha="center")
ax.set_xlim(-1.4, a + 1.3); ax.set_ylim(-0.7, A[1] + 0.5)
kaydet(fig, __file__)
