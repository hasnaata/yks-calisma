import sys; sys.path.insert(0, "tools")
from cizim import *

def uz(P, Q): return round(float(np.linalg.norm(np.asarray(P, float) - np.asarray(Q, float))), 3)
def kenar(ax, P, Q, metin, G, d=0.45, renk=YAZI, fs=13):
    """[PQ] kenarının ortasına, G noktasından uzak tarafa etiket."""
    P, Q = np.asarray(P, float), np.asarray(Q, float); M = (P + Q) / 2
    u = (Q - P) / np.linalg.norm(Q - P); v = np.array([-u[1], u[0]])
    if np.dot(v, M - np.asarray(G, float)) < 0: v = -v
    ax.text(*(M + d * v), metin, ha="center", va="center", color=renk, fontsize=fs)
def dik(ax, K, P, Q, s=0.3, renk=SOLUK):
    """K köşesinde KP ile KQ arasındaki dik açı işareti."""
    K, P, Q = (np.asarray(t, float) for t in (K, P, Q))
    u = (P - K) / np.linalg.norm(P - K) * s; v = (Q - K) / np.linalg.norm(Q - K) * s
    ax.plot(*zip(K + u, K + u + v, K + v), color=renk, lw=1.3)
def aci_olc(K, P, Q):
    u, v = np.asarray(P, float) - K, np.asarray(Q, float) - K
    return round(float(np.degrees(np.arccos(np.dot(u, v) / np.linalg.norm(u) / np.linalg.norm(v)))), 3)

# Açılarına göre özel dik üçgenler (a = 1 birim yerine uygun ölçek).
fig, ax = sekil(6, 5.6); ax.set_aspect("equal"); ax.axis("off")
# 1) 30-60-90: B dik, BC = a, AB = a√3, AC = 2a
a = 1.9; B = np.array([0.0, 3.0]); C = B + [a, 0]; A = B + [0, a * np.sqrt(3)]
print("30-60-90", uz(B, C) / a, uz(A, B) / a, uz(A, C) / a, aci_olc(A, B, C), aci_olc(C, A, B))
ax.plot(*zip(A, B, C, A), color=MAVI); dik(ax, B, A, C, s=0.22); G0 = (A + B + C) / 3
kenar(ax, B, C, "a", G0, d=0.3, renk=MAVI); kenar(ax, A, B, "a√3", G0, d=0.5, renk=MAVI); kenar(ax, A, C, "2a", G0, d=0.38, renk=MAVI)
aci(ax, A, B, C, r=0.55, ad="30°", renk=YAZI); aci(ax, C, A, B, r=0.38, ad="60°", renk=YAZI)
nokta(ax, *A, "A", dx=-0.1, dy=0.15); nokta(ax, *B, "B", dx=-0.42, dy=-0.38); nokta(ax, *C, "C", dx=0.12, dy=-0.38)
# 2) 45-45-90: E dik, DE = EF = a, DF = a√2
a = 2.6; E = np.array([4.0, 3.0]); F = E + [a, 0]; D = E + [0, a]
print("45-45-90", uz(D, F) / a, aci_olc(D, E, F))
ax.plot(*zip(D, E, F, D), color=YESIL); dik(ax, E, D, F, s=0.22); G1 = (D + E + F) / 3
kenar(ax, E, F, "a", G1, d=0.3, renk=YESIL); kenar(ax, D, E, "a", G1, d=0.3, renk=YESIL); kenar(ax, D, F, "a√2", G1, d=0.45, renk=YESIL)
aci(ax, D, E, F, r=0.45, ad="45°", renk=YAZI); aci(ax, F, D, E, r=0.45, ad="45°", renk=YAZI)
nokta(ax, *D, "D", dx=-0.1, dy=0.15); nokta(ax, *E, "E", dx=-0.42, dy=-0.38); nokta(ax, *F, "F", dx=0.12, dy=-0.38)
# 3) 15-75-90: K dik, LM = 4a hipotenüs, KH = a yükseklik
a = 1.6; L = np.array([0.2, 0.0]); M = L + [4 * a, 0]
KL = 4 * a * np.cos(np.radians(15)); K = L + KL * np.array([np.cos(np.radians(15)), np.sin(np.radians(15))]); H = np.array([K[0], 0.0])
print("15-75-90", uz(K, H) / a, aci_olc(K, L, M), aci_olc(L, K, M), aci_olc(M, K, L))
ax.plot(*zip(K, L, M, K), color=KIRMIZI); ax.plot(*zip(K, H), color=SARI, lw=1.8)
dik(ax, K, L, M, s=0.2); dik(ax, H, K, L, s=0.16)
ax.text(H[0] - 0.22, K[1] / 2 - 0.1, "a", color=SARI, fontsize=13, va="center", ha="center")
ax.text((L[0] + M[0]) / 2, -0.35, "4a", color=KIRMIZI, ha="center", va="center")
aci(ax, L, M, K, r=1.1, ad="15°", renk=YAZI); aci(ax, M, K, L, r=0.32, ad="", renk=YAZI)
ax.text(M[0] + 0.5, 0.55, "75°", color=YAZI, fontsize=12, ha="center")
nokta(ax, *K, "K", dx=-0.1, dy=0.15); nokta(ax, *L, "L", dx=-0.42, dy=-0.1); nokta(ax, *M, "M", dx=0.15, dy=-0.4)
nokta(ax, *H, "H", dx=-0.12, dy=-0.5, renk=SARI)
ax.set_xlim(-0.7, 7.4); ax.set_ylim(-0.7, 6.6)
kaydet(fig, __file__)
