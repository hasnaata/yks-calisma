import sys; sys.path.insert(0, "tools")
from cizim import *

# Alıştırma 12: çadır, |AH| = 2,4, |BC| = 5, |BH| = 1,8, |HC| = 3,2, |AC| = 4.
# A'da dik açı, [AH] ⊥ [BC]. p = |BH|, k = |HC|; A noktası (p, √(p·k)) olur, böylece AB ⊥ AC kendiliğinden sağlanır.
p, k = 1.8, 3.2
E = {'b': '?', 'h': '2,4 m', 'a': '5 m'}          # kenar etiketleri (None: yazma)
DOLGU, RENKLI_KENAR, EK = False, False, []

B = np.array([0.0, 0.0]); H = np.array([p, 0.0]); C = np.array([p + k, 0.0]); A = np.array([p, np.sqrt(p * k)])
uz = lambda P, Q: float(np.linalg.norm(P - Q))
u, v = B - A, C - A
print("AB", round(uz(A, B), 4), "AC", round(uz(A, C), 4), "AH", round(uz(A, H), 4), "BC", round(uz(B, C), 4),
      "A açısı", round(float(np.degrees(np.arccos(np.dot(u, v) / uz(A, B) / uz(A, C)))), 4))

s = (p + k) / 10
G = (A + B + C) / 3
def kenar(P, Q, metin, renk=YAZI, d=0.42):
    M = (P + Q) / 2; t = (Q - P) / uz(P, Q); n = np.array([-t[1], t[0]])
    if np.dot(n, M - G) < 0: n = -n
    ax.text(*(M + d * s * n), metin, ha="center", va="center", color=renk, fontsize=13)
def dik(K, P, Q, r=0.32):
    a_ = (P - K) / uz(P, K) * r * s; b_ = (Q - K) / uz(Q, K) * r * s
    ax.plot(*zip(K + a_, K + a_ + b_, K + b_), color=SOLUK, lw=1.3)

x0, x1 = -0.6 * s, p + k + 0.6 * s
y0, y1 = (-1.9 if E.get("a") else -1.0) * s, A[1] + 0.6 * s
fig, ax = sekil(6, max(2.2, 6 * (y1 - y0) / (x1 - x0)))
ax.set_aspect("equal"); ax.axis("off")
if DOLGU:
    ax.add_patch(patches.Polygon([A, B, H], closed=True, facecolor=YESIL_ACIK, edgecolor="none"))
    ax.add_patch(patches.Polygon([A, H, C], closed=True, facecolor=SARI_ACIK, edgecolor="none"))
rc, rb = (MAVI, YESIL) if RENKLI_KENAR else (YAZI, YAZI)
ax.plot(*zip(A, B), color=rc); ax.plot(*zip(B, H), color=rc)
ax.plot(*zip(A, C), color=rb); ax.plot(*zip(H, C), color=rb)
ax.plot(*zip(A, H), color=KIRMIZI, lw=1.8)
dik(H, A, C); dik(A, B, C)
nokta(ax, *A, ""); nokta(ax, *B, ""); nokta(ax, *C, ""); nokta(ax, *H, "", renk=KIRMIZI)
ax.text(A[0], A[1] + 0.3 * s, "A", ha="center", va="bottom", fontsize=13)
ax.text(B[0] - 0.25 * s, 0, "B", ha="right", va="center", fontsize=13)
ax.text(C[0] + 0.25 * s, 0, "C", ha="left", va="center", fontsize=13)
ax.text(H[0], -0.3 * s, "H", ha="center", va="top", fontsize=13, color=KIRMIZI)
if E.get("c"): kenar(A, B, E["c"], rc)
if E.get("b"): kenar(A, C, E["b"], rb)
if E.get("h"):
    sag = k >= p
    ax.text(p + (0.15 if sag else -0.15) * s, A[1] * 0.45, E["h"], ha="left" if sag else "right", va="center", color=KIRMIZI, fontsize=13)
if E.get("p"): ax.text(p / 2, 0.22 * s, E["p"], ha="center", va="bottom", color=rc, fontsize=13)
if E.get("k"): ax.text(p + k / 2, 0.22 * s, E["k"], ha="center", va="bottom", color=rb, fontsize=13)
if E.get("a"):
    ax.annotate("", xy=(p + k, -1.05 * s), xytext=(0, -1.05 * s), arrowprops=dict(arrowstyle="<->", color=SOLUK, lw=1.2))
    for x in (0, p + k): ax.plot([x, x], [-0.85 * s, -1.25 * s], color=SOLUK, lw=1)
    ax.text((p + k) / 2, -1.25 * s, E["a"], ha="center", va="top", fontsize=13)
for (fx, fy, metin, renk) in EK:
    ax.text(fx, fy, metin, ha="center", va="center", color=eval(renk), fontsize=12)
ax.set_xlim(x0, x1); ax.set_ylim(y0, y1)
kaydet(fig, __file__)
