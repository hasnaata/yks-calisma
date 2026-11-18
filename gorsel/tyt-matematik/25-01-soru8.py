# Alıştırma 8: yan kenarları düz, 5 rafı eşit aralıklı yamuk kitaplık. Alt raf 90 cm, üst raf 50 cm → raflar 90, 80, 70, 60, 50; toplam 350 cm.
import sys; sys.path.insert(0, "tools")
from cizim import *

P = lambda x, y: np.array([float(x), float(y)])
uz = lambda U, V: round(float(np.linalg.norm(U - V)), 4)
def acisi(K, U, V):
    u, v = U - K, V - K
    return round(float(np.degrees(np.arccos(np.dot(u, v) / np.linalg.norm(u) / np.linalg.norm(v)))), 3)
def kesis(p, u, q, v):
    t = np.linalg.solve(np.array([u, -v]).T, q - p); return p + t[0] * u
def paralel_isareti(U, V, renk=SOLUK, k=0.18, f=0.5):
    M = U + f * (V - U); t = (V - U) / np.linalg.norm(V - U)
    ax.annotate("", xy=M + k * t, xytext=M - k * t, arrowprops=dict(arrowstyle="-|>", color=renk, lw=1.4, mutation_scale=14))
def cetik(U, V, n=1, renk=SOLUK, L=0.16):
    M = (U + V) / 2; t = (V - U) / np.linalg.norm(V - U); m = np.array([-t[1], t[0]])
    for i in range(n):
        c = M + (i - (n - 1) / 2) * 0.13 * t
        ax.plot(*zip(c - L * m, c + L * m), color=renk, lw=1.5)
def olcu(U, V, metin, d=0.3, renk=YAZI, fs=13):
    """[UV] parçasının ortasına, U→V yönünün soluna d kadar uzağa yazı (d < 0: sağına)."""
    M = (U + V) / 2; t = (V - U) / np.linalg.norm(V - U); m = np.array([-t[1], t[0]])
    ax.text(*(M + d * m), metin, ha="center", va="center", color=renk, fontsize=fs)
def dik_isareti(K, U, V, r=0.28):
    a_ = (U - K) / np.linalg.norm(U - K) * r; b_ = (V - K) / np.linalg.norm(V - K) * r
    ax.plot(*zip(K + a_, K + a_ + b_, K + b_), color=SOLUK, lw=1.3)

A, B, C, D = P(0, 0), P(90, 0), P(70, 100), P(20, 100)
raflar = []
for i in range(5):
    y = 25 * i
    sol = A + (D - A) * y / 100; sag = B + (C - B) * y / 100
    raflar.append((sol, sag))
print("raflar", [uz(s_, g_) for s_, g_ in raflar], "toplam", sum(uz(s_, g_) for s_, g_ in raflar))

fig, ax = sekil(4.6, 4.6)
ax.set_aspect("equal"); ax.axis("off")
ax.plot(*zip(A, D), color=SARI, lw=4, solid_capstyle="round"); ax.plot(*zip(B, C), color=SARI, lw=4, solid_capstyle="round")
for i, (s_, g_) in enumerate(raflar):
    ax.plot(*zip(s_, g_), color=MAVI if i in (0, 4) else YAZI, lw=3 if i in (0, 4) else 2.4)
ax.text(45, -5, "90 cm", ha="center", va="top", color=MAVI, fontsize=13)
ax.text(45, 105, "50 cm", ha="center", va="bottom", color=MAVI, fontsize=13)
for i in range(1, 4):
    ax.text(45, 25 * i + 3, "?", ha="center", va="bottom", color=SOLUK, fontsize=13)
# eşit aralık işareti (sağda)
x = 100
ax.plot([x, x], [0, 100], color=SOLUK, lw=1)
for i in range(5): ax.plot([x - 2, x + 2], [25 * i, 25 * i], color=SOLUK, lw=1.2)
for i in range(4):
    yy = 25 * i + 12.5
    ax.plot([x - 1.6, x + 1.6], [yy - 1.2, yy + 1.2], color=SOLUK, lw=1.2)
ax.set_xlim(-6, 108); ax.set_ylim(-16, 116)
kaydet(fig, __file__)
