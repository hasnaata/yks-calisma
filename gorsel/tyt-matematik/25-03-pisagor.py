# Örnek 2: ikizkenar yamuk, |AB| = 14, |DC| = 6, |AD| = |BC| = 5.
# Dikmelerin ayakları H ve K: |AH| = |KB| = (14 − 6) / 2 = 4, |HK| = 6; AHD üçgeninde h = √(25 − 16) = 3. Alan = 10 · 3 = 30.
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

A, B, C, D = P(0, 0), P(14, 0), P(10, 3), P(4, 3)
H, K = P(4, 0), P(10, 0)
print("AD", uz(A, D), "BC", uz(B, C), "h", uz(D, H), "ABCD", alan(A, B, C, D))
fig, ax = cerceve(-1.0, 15.0, -2.0, 4.0)
boya(A, H, D, renk=SARI_ACIK); boya(K, B, C, renk=SARI_ACIK)
ax.plot(*zip(D, H), color=KIRMIZI, lw=1.6, ls="--"); ax.plot(*zip(C, K), color=KIRMIZI, lw=1.6, ls="--")
dik_isareti(H, B, D); dik_isareti(K, A, C)
yamuk(A, B, C, D, fa=0.5, fd=0.5)
cetik(A, D); cetik(B, C)
ad(A, "A", -0.35, -0.3); ad(B, "B", 0.35, -0.3); ad(C, "C", 0.3, 0.3); ad(D, "D", -0.3, 0.3)
ad(H, "H", 0, -0.45, renk=KIRMIZI); ad(K, "K", 0, -0.45, renk=KIRMIZI)
olcu(D, C, "6", d=0.45)
olcu(A, D, "5", d=0.55); olcu(B, C, "5", d=-0.55)
ax.text(2, -0.45, "4", ha="center", va="center", color=SARI); ax.text(12, -0.45, "4", ha="center", va="center", color=SARI)
ax.text(7, -0.45, "6", ha="center", va="center", color=SOLUK)
ax.annotate("", xy=(14, -1.25), xytext=(0, -1.25), arrowprops=dict(arrowstyle="<->", color=SOLUK, lw=1.2))
ax.text(7, -1.6, "14", ha="center", va="center")
ax.text(H[0] + 0.25, 1.5, "h = 3", ha="left", va="center", color=KIRMIZI)
kaydet(fig, __file__)
