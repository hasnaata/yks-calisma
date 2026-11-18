import sys; sys.path.insert(0, "tools")
from cizim import *

# Solda dışbükey ABCD (bütün iç açılar < 180°), sağda içbükey ABCD (D'deki iç açı > 180°). Köşegenler kesikli.
fig, ax = sekil(6, 3.4)
ax.set_aspect("equal"); ax.axis("off")

def ciz(V, adlar, kaydir, renk, dolgu):
    ax.add_patch(patches.Polygon(V, closed=True, facecolor=dolgu, edgecolor=YAZI, lw=2.2))
    for v, ad, k in zip(V, adlar, kaydir):
        nokta(ax, *v, ""); ax.text(v[0] + k[0], v[1] + k[1], ad, ha="center", va="center", fontsize=14)

# Dışbükey
A1, B1, C1, D1 = np.array([0.4, 3.0]), np.array([0.0, 0.3]), np.array([3.2, 0.0]), np.array([3.4, 2.6])
ciz([A1, B1, C1, D1], "ABCD", [(-0.3, 0.2), (-0.35, -0.2), (0.3, -0.25), (0.3, 0.2)], YAZI, MAVI_ACIK)
ax.plot(*zip(A1, C1), color=SOLUK, lw=1.5, ls="--"); ax.plot(*zip(B1, D1), color=SOLUK, lw=1.5, ls="--")
ax.text(1.7, -0.75, "dışbükey", ha="center", fontsize=13, color=MAVI)

# İçbükey: D noktası ABC üçgeninin içinde
o = 4.6
A2, B2, C2, D2 = np.array([o + 1.6, 3.1]), np.array([o, 0.0]), np.array([o + 3.6, 0.4]), np.array([o + 1.9, 1.35])
ciz([A2, B2, C2, D2], "ABCD", [(0.0, 0.3), (-0.35, -0.2), (0.35, -0.2), (0.38, 0.1)], YAZI, SARI_ACIK)
ax.plot(*zip(A2, C2), color=SOLUK, lw=1.5, ls="--"); ax.plot(*zip(B2, D2), color=SOLUK, lw=1.5, ls="--")
# D'deki 180°'den büyük iç açı (dörtgenin içinden geçen yay)
a1 = np.degrees(np.arctan2(*(C2 - D2)[::-1])); a2 = np.degrees(np.arctan2(*(A2 - D2)[::-1]))
ax.add_patch(patches.Arc(D2, 0.7, 0.7, theta1=a2, theta2=a1 + 360, color=KIRMIZI, lw=1.8))
ax.text(o + 2.05, 0.72, "> 180°", color=KIRMIZI, fontsize=11, ha="center", va="center")
ax.text(o + 1.8, -0.75, "içbükey", ha="center", fontsize=13, color=SARI)

def ic(P, Q, R):
    u, w = Q - P, R - P
    return np.degrees(np.arccos(u @ w / np.linalg.norm(u) / np.linalg.norm(w)))
print("içbükey D (küçük taraf):", ic(D2, A2, C2), "iç açı:", 360 - ic(D2, A2, C2))
ax.set_xlim(-0.7, o + 4.2); ax.set_ylim(-1.0, 3.6)
kaydet(fig, __file__)
