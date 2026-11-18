# Örnek 2: [AB] ∥ [DC], m(DAB) = 64°, |AD| = 6. A'nın açıortayı [DC]'yi E'de keser → |DE| = 6.
# D'nin açıortayı [AE]'yi P'de keser → m(DPA) = 90°.
import sys; sys.path.insert(0, "tools")
from cizim import *

P = lambda x, y: np.array([float(x), float(y)])
uz = lambda U, V: round(float(np.linalg.norm(U - V)), 4)
def acisi(K, U, V):
    u, v = U - K, V - K
    return round(float(np.degrees(np.arccos(np.dot(u, v) / np.linalg.norm(u) / np.linalg.norm(v)))), 3)
def kesis(p, u, q, v):
    t = np.linalg.solve(np.array([u, -v]).T, q - p); return p + t[0] * u
def paralel_isareti(U, V, renk=SOLUK, k=0.18):
    M = (U + V) / 2; t = (V - U) / np.linalg.norm(V - U)
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

A = P(0, 0); D = 6 * P(np.cos(np.radians(64)), np.sin(np.radians(64)))
E = D + P(6, 0); C = P(10.4, D[1]); B = P(12.6, 0)
Pn = kesis(A, E - A, D, P(np.cos(np.radians(-58)), np.sin(np.radians(-58))))
print("A", acisi(A, B, D), "DAE", acisi(A, D, E), "EAB", acisi(A, E, B), "DEA", acisi(E, D, A),
      "ADC", acisi(D, A, C), "ADP", acisi(D, A, Pn), "PDC", acisi(D, Pn, C), "DPA", acisi(Pn, D, A), "AD", uz(A, D), "DE", uz(D, E))

fig, ax = sekil(6, 3.4)
ax.set_aspect("equal"); ax.axis("off")
ax.add_patch(patches.Polygon([A, D, E], closed=True, facecolor=SARI_ACIK, edgecolor="none"))
ax.plot(*zip(A, B, C, D, A), color=YAZI)
ax.plot(*zip(A, E), color=MAVI, lw=1.8)
ax.plot(*zip(D, Pn), color=YESIL, lw=1.8)
paralel_isareti(E, C); paralel_isareti(A, B)
dik_isareti(Pn, D, E)
for Q in (A, B, C, D): nokta(ax, *Q, "")
nokta(ax, *E, "", renk=MAVI); nokta(ax, *Pn, "", renk=YESIL)
ax.text(A[0] - 0.2, -0.15, "A", ha="right", va="top")
ax.text(B[0] + 0.2, -0.15, "B", ha="left", va="top")
ax.text(C[0] + 0.2, C[1] + 0.1, "C", ha="left", va="bottom")
ax.text(D[0] - 0.2, D[1] + 0.1, "D", ha="right", va="bottom")
ax.text(E[0], E[1] + 0.25, "E", ha="center", va="bottom", color=MAVI)
ax.text(Pn[0] + 0.15, Pn[1] - 0.3, "P", ha="left", va="top", color=YESIL)
aci(ax, A, E, B, r=1.5, ad="32°", renk=MAVI)
aci(ax, A, D, E, r=1.1, ad="32°", renk=MAVI)
aci(ax, E, D, A, r=1.2, ad="", renk=MAVI)
ax.text(E[0] - 1.75, E[1] - 0.32, "32°", ha="center", va="center", color=MAVI, fontsize=12)
aci(ax, D, A, Pn, r=0.55, ad="58°", renk=YESIL)
aci(ax, D, Pn, C, r=0.75, ad="", renk=YESIL)
ax.text(D[0] + 1.3, D[1] - 0.3, "58°", ha="center", va="center", color=YESIL, fontsize=12)
olcu(A, D, "6", d=0.35)
olcu(D, E, "6", d=0.3)
ax.set_xlim(-0.9, B[0] + 0.9); ax.set_ylim(-0.8, D[1] + 0.8)
kaydet(fig, __file__)
