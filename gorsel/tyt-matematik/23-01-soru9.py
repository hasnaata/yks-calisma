import sys; sys.path.insert(0, "tools")
from cizim import *

# P noktasında bir kare (90°) ve iki eş düzgün çokgen (her biri 135°, düzgün sekizgen) boşluksuz birleşir.
# Şekilde yalnızca P çevresi gösterilir: kare tam, öbür iki parçanın P'den çıkan kenarları ve açıları.
P = np.array([0.0, 0.0]); L = 2.4
def u(t): return np.array([np.cos(np.radians(t)), np.sin(np.radians(t))])
fig, ax = sekil(4.6, 4.6)
ax.set_aspect("equal"); ax.axis("off")
kare = [P, P + L * u(0), P + L * u(0) + L * u(90), P + L * u(90)]
ax.add_patch(patches.Polygon(kare, closed=True, facecolor=SARI_ACIK, edgecolor=YAZI, lw=2.4))
ax.text(*(P + 0.5 * L * (u(0) + u(90))), "kare", ha="center", va="center", fontsize=13, color=SARI)
# öbür iki parça: düzgün çokgenin P'deki iki kenarı + bir sonraki kenarların başlangıcı (kesik)
dis = 45
for bas, renk in ((90, MAVI_ACIK), (225, YESIL_ACIK)):
    # Sektör bas .. bas+135. Saat yönünün tersine yürüyüş: P -> P + L u(bas), sonra u(bas+45) yönü (kesik başlangıç).
    # Son kenar P + L u(bas+135) -> P; ondan önceki kenar u(bas+90) yönünde o köşeden geriye uzanır (kesik).
    pts = [P + L * u(bas + 135), P, P + L * u(bas)]
    Q1 = pts[2] + 0.6 * L * u(bas + dis); Q0 = pts[0] + 0.6 * L * u(bas + 90)
    poly = [Q0, pts[0], P, pts[2], Q1]
    ax.add_patch(patches.Polygon(poly, closed=False, facecolor=renk, edgecolor="none"))
    ax.plot(*zip(pts[0], P, pts[2]), color=YAZI, lw=2.4)
    ax.plot(*zip(pts[2], Q1), color=YAZI, lw=2.0, ls=(0, (4, 3)))
    ax.plot(*zip(pts[0], Q0), color=YAZI, lw=2.0, ls=(0, (4, 3)))
    aci(ax, P, pts[2], pts[0], r=0.45, ad="", renk=MAVI)
    ax.text(*(P + 0.95 * u(bas + 67.5)), "?", ha="center", va="center", fontsize=15, color=MAVI)
k = 0.32
ax.plot(*zip(P + k * u(0), P + k * (u(0) + u(90)), P + k * u(90)), color=SARI, lw=1.6)
nokta(ax, *P, ""); ax.text(*(P + 0.8 * u(58)), "P", ha="center", va="center", fontsize=14)
ax.set_xlim(-3.6, 3.7); ax.set_ylim(-3.3, 3.6)
kaydet(fig, __file__)
