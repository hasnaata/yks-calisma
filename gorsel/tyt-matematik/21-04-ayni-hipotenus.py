import sys; sys.path.insert(0, "tools")
from cizim import *

def uz(P, Q): return round(float(np.linalg.norm(np.asarray(P, float) - np.asarray(Q, float))), 3)
def kenar(ax, P, Q, metin, G, d=0.35, renk=YAZI, fs=13):
    """[PQ] kenarının ortasına, G noktasından uzak tarafa etiket."""
    P, Q = np.asarray(P, float), np.asarray(Q, float); M = (P + Q) / 2
    u = (Q - P) / np.linalg.norm(Q - P); v = np.array([-u[1], u[0]])
    if np.dot(v, M - np.asarray(G, float)) < 0: v = -v
    ax.text(*(M + d * v), metin, ha="center", va="center", color=renk, fontsize=fs)
def dik(ax, K, P, Q, s=0.25, renk=SOLUK):
    """K köşesinde KP ile KQ arasındaki dik açı işareti."""
    K, P, Q = (np.asarray(t, float) for t in (K, P, Q))
    u = (P - K) / np.linalg.norm(P - K) * s; v = (Q - K) / np.linalg.norm(Q - K) * s
    ax.plot(*zip(K + u, K + u + v, K + v), color=renk, lw=1.3)
def aci_olc(K, P, Q):
    K = np.asarray(K, float); u, v = np.asarray(P, float) - K, np.asarray(Q, float) - K
    return round(float(np.degrees(np.arccos(np.dot(u, v) / np.linalg.norm(u) / np.linalg.norm(v)))), 3)

# Hipotenüsü 2 olan üç dik üçgen: 30°, 45°, 60°. Karşı kenarlar 1, √2, √3; komşu kenarlar √3, √2, 1.
k = 1.3
fig, ax = sekil(6.2, 3.4); ax.set_aspect("equal"); ax.axis("off")
x0 = 0.0
for derece, kars, koms, renk in ((30, "1", "√3", MAVI), (45, "√2", "√2", YESIL), (60, "√3", "1", KIRMIZI)):
    t = np.radians(derece)
    O = np.array([x0, 0.0]); P = O + 2 * k * np.array([np.cos(t), np.sin(t)]); Q = np.array([P[0], 0.0])
    print(derece, "karşı", uz(P, Q) / k, "komşu", uz(O, Q) / k, "hip", uz(O, P) / k, "açı", aci_olc(O, P, Q))
    ax.plot(*zip(O, Q, P, O), color=renk)
    dik(ax, Q, O, P, s=0.18)
    G0 = (O + P + Q) / 3
    kenar(ax, O, P, "2", G0, d=0.28, renk=renk)
    ax.text(P[0] + 0.12, P[1] / 2, kars, color=renk, fontsize=13, ha="left", va="center")
    ax.text((O[0] + Q[0]) / 2, -0.28, koms, color=renk, fontsize=13, ha="center", va="center")
    aci(ax, O, Q, P, r=0.45, ad="", renk=YAZI)
    ax.text(O[0] + 0.62 * np.cos(t / 2) + 0.05, 0.62 * np.sin(t / 2) + 0.02, f"{derece}°", fontsize=10.5, color=YAZI, ha="left", va="center")
    ax.text((O[0] + Q[0]) / 2 + 0.1, -0.75, f"sin {derece}° = {kars}/2", color=renk, fontsize=12.5, ha="center", va="center")
    x0 = Q[0] + 1.05
ax.set_xlim(-0.3, x0 - 0.5); ax.set_ylim(-1.05, 2 * k * np.sin(np.radians(60)) + 0.25)
kaydet(fig, __file__)
