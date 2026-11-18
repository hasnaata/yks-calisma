# Örnek 5: |AB| = 11, |DC| = 5, h = 4, E ∈ [AB], |AE| = 4, |EB| = 7.
# A(AED) = 8, A(EBC) = 14, A(DEC) = 10; toplam 32.
import sys; sys.path.insert(0, "tools")
from cizim import *

S = 1.0  # ölçek: yazı ve işaret boşlukları bu birimle çarpılır
P = lambda x, y: np.array([float(x), float(y)])
uz = lambda U, V: round(float(np.linalg.norm(U - V)), 4)
def alan(*K):
    x = [k[0] for k in K]; y = [k[1] for k in K]
    return round(abs(sum(x[i] * y[i - 1] - x[i - 1] * y[i] for i in range(len(K)))) / 2, 4)
def kesis(p, u, q, v):
    t = np.linalg.solve(np.array([u, -v]).T, q - p); return p + t[0] * u
def paralel_isareti(U, V, renk=SOLUK, k=0.18, f=0.5):
    M = U + f * (V - U); t = (V - U) / np.linalg.norm(V - U)
    ax.annotate("", xy=M + k * S * t, xytext=M - k * S * t, arrowprops=dict(arrowstyle="-|>", color=renk, lw=1.4, mutation_scale=14))
def cetik(U, V, n=1, renk=SOLUK, L=0.16):
    M = (U + V) / 2; t = (V - U) / np.linalg.norm(V - U); m = np.array([-t[1], t[0]])
    for i in range(n):
        c = M + (i - (n - 1) / 2) * 0.13 * S * t
        ax.plot(*zip(c - L * S * m, c + L * S * m), color=renk, lw=1.5)
def olcu(U, V, metin, d=0.3, renk=YAZI, fs=13):
    """[UV] parçasının ortasına, U->V yönünün soluna d kadar uzağa yazı (d < 0: sağına)."""
    M = (U + V) / 2; t = (V - U) / np.linalg.norm(V - U); m = np.array([-t[1], t[0]])
    ax.text(*(M + d * S * m), metin, ha="center", va="center", color=renk, fontsize=fs)
def dik_isareti(K, U, V, r=0.28):
    a_ = (U - K) / np.linalg.norm(U - K) * r * S; b_ = (V - K) / np.linalg.norm(V - K) * r * S
    ax.plot(*zip(K + a_, K + a_ + b_, K + b_), color=SOLUK, lw=1.3)
def boya(*K, renk=MAVI_ACIK):
    ax.add_patch(patches.Polygon(np.array(K), closed=True, facecolor=renk, edgecolor="none", zorder=0))
def ortasi(*K):
    return sum(K) / len(K)
def ad(K, metin, dx, dy, renk=YAZI):
    ax.text(K[0] + dx * S, K[1] + dy * S, metin, ha="center", va="center", color=renk, fontsize=13)
def yamuk(A, B, C, D, fa=0.5, fd=0.5):
    ax.plot(*zip(A, B, C, D, A), color=YAZI, zorder=3)
    paralel_isareti(A, B, f=fa); paralel_isareti(D, C, f=fd)
    for Q in (A, B, C, D): nokta(ax, *Q, "")
def cerceve(xmin, xmax, ymin, ymax, en=6.0):
    fig, ax = sekil(en, en * (ymax - ymin) / (xmax - xmin))
    ax.set_aspect("equal"); ax.axis("off")
    ax.set_xlim(xmin, xmax); ax.set_ylim(ymin, ymax)
    return fig, ax

A, B, C, D = P(0, 0), P(11, 0), P(8, 4), P(3, 4)
E = P(4, 0); H = P(8, 0)
print("AED", alan(A, E, D), "EBC", alan(E, B, C), "DEC", alan(D, E, C), "ABCD", alan(A, B, C, D))
fig, ax = cerceve(-1.0, 12.2, -1.1, 5.0)
boya(A, E, D, renk=SARI_ACIK); boya(E, B, C, renk=YESIL_ACIK); boya(D, E, C, renk=MAVI_ACIK)
ax.plot(*zip(E, D), color=SOLUK, lw=1.5); ax.plot(*zip(E, C), color=SOLUK, lw=1.5)
ax.plot(*zip(C, H), color=KIRMIZI, lw=1.6, ls="--"); dik_isareti(H, B, C)
yamuk(A, B, C, D, fa=0.25, fd=0.5)
nokta(ax, *E, "")
ad(A, "A", -0.35, -0.3); ad(B, "B", 0.35, -0.3); ad(C, "C", 0.3, 0.3); ad(D, "D", -0.3, 0.3)
ad(E, "E", 0, -0.42)
olcu(A, E, "4", d=-0.85); olcu(E, B, "7", d=-0.85); olcu(D, C, "5", d=0.45)
ax.text(H[0] + 0.25, 1.1, "h = 4", ha="left", va="center", color=KIRMIZI)
ax.text(*ortasi(A, E, D) + P(0, -0.2), "8", ha="center", va="center", color=SARI, fontsize=15)
ax.text(*ortasi(E, B, C) + P(-0.5, 0.25), "14", ha="center", va="center", color=YESIL, fontsize=15)
ax.text(*ortasi(D, E, C) + P(0, 0.3), "10", ha="center", va="center", color=MAVI, fontsize=15)
kaydet(fig, __file__)
