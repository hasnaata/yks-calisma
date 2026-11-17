import sys; sys.path.insert(0, "tools")
from cizim import *

# Alıştırma 9: ABCD dikdörtgen, [AH] ⊥ [BD], |BH| = 4, |HD| = 16.
# ABD üçgeni A'da dik: |AH| = 8, |AB| = √80, |AD| = √320, alan = |AB|·|AD| = 160.
p, k = 4, 16
ab, ad = np.sqrt(p * (p + k)), np.sqrt(k * (p + k))
A = np.array([0.0, 0.0]); B = np.array([0.0, ab]); C = np.array([ad, ab]); D = np.array([ad, 0.0])
t = (D - B) / np.linalg.norm(D - B)
H = B + p * t
uz = lambda P, Q: float(np.linalg.norm(P - Q))
print("AB", round(ab, 4), "AD", round(ad, 4), "BD", round(uz(B, D), 4), "AH", round(uz(A, H), 4),
      "AH.BD", round(float(np.dot(H - A, D - B)), 6), "alan", round(ab * ad, 4))

s = 2.0
fig, ax = sekil(6, 3.2)
ax.set_aspect("equal"); ax.axis("off")
ax.plot(*zip(A, B, C, D, A), color=YAZI)
ax.plot(*zip(B, D), color=YAZI, lw=1.6)
ax.plot(*zip(A, H), color=KIRMIZI, lw=1.8)
def dik(K, P, Q, r=0.6):
    a_ = (P - K) / uz(P, K) * r; b_ = (Q - K) / uz(Q, K) * r
    ax.plot(*zip(K + a_, K + a_ + b_, K + b_), color=SOLUK, lw=1.3)
dik(H, A, D)
for P in (A, B, C, D): nokta(ax, *P, "")
nokta(ax, *H, "", renk=KIRMIZI)
ax.text(-0.4, 0, "A", ha="right", va="center"); ax.text(-0.4, ab, "B", ha="right", va="center")
ax.text(ad + 0.4, ab, "C", ha="left", va="center"); ax.text(ad + 0.4, 0, "D", ha="left", va="center")
ax.text(H[0] + 0.35, H[1] + 0.35, "H", color=KIRMIZI, ha="left", va="bottom")
M1, M2 = (B + H) / 2, (H + D) / 2
ax.text(*(M1 + 0.9 * np.array([0.6, 0.8])), "4", ha="center", va="center")
ax.text(*(M2 + 0.9 * np.array([0.32, 0.95])), "16", ha="center", va="center")
ax.set_xlim(-1.2, ad + 1.2); ax.set_ylim(-0.6, ab + 0.6)
kaydet(fig, __file__)
