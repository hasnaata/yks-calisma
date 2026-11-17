import sys; sys.path.insert(0, "tools")
from cizim import *

# Alıştırma soru 10: robot kolu |OE| = 8, |EH| = 5, dirsekteki açı geniş (çizimde 120°), d = |OH| = sqrt(129) ≈ 11,36.
O = np.array([0.0, 0.0]); E = 8 * np.array([np.cos(np.radians(35)), np.sin(np.radians(35))])
yon = np.radians(35 - 60)  # dirsekte 180 - 60 = 120 derece
H = E + 5 * np.array([np.cos(yon), np.sin(yon)])
v1 = O - E; v2 = H - E
print("dirsek", np.degrees(np.arccos(v1 @ v2 / np.linalg.norm(v1) / np.linalg.norm(v2))), "d", np.linalg.norm(H - O))

fig, ax = sekil(5.6, 3.6)
ax.set_aspect("equal"); ax.axis("off")
ax.add_patch(patches.Rectangle((-0.9, -0.7), 1.8, 0.45, facecolor=CIZGI, edgecolor="none"))
ax.plot(*zip(O, E), color=MAVI, lw=6, solid_capstyle="round")
ax.plot(*zip(E, H), color=MAVI, lw=6, solid_capstyle="round")
ax.plot(*zip(O, H), color=KIRMIZI, lw=1.8, ls="--")
for P in (O, E): ax.plot(*P, "o", color="white", markeredgecolor=YAZI, markersize=9, zorder=6)
ax.plot(*H, "o", color=YAZI, markersize=7, zorder=6)
aci(ax, E, O, H, r=0.8, renk=SARI)
ax.text(O[0] - 0.4, O[1] + 0.35, "O", fontsize=13); ax.text(E[0] - 0.2, E[1] + 0.4, "E", fontsize=13)
ax.text(H[0] + 0.25, H[1] - 0.1, "H", fontsize=13)
m = E / 2; ax.text(m[0] - 1.6, m[1] + 0.6, "8 cm", fontsize=13, color=MAVI)
m = (E + H) / 2; ax.text(m[0] + 0.35, m[1] + 0.2, "5 cm", fontsize=13, color=MAVI)
m = H / 2; ax.text(m[0] + 0.1, m[1] - 0.6, "d", fontsize=14, color=KIRMIZI, fontweight="bold")
ax.set_xlim(-1.2, H[0] + 1.2); ax.set_ylim(-0.9, E[1] + 1.0)
kaydet(fig, __file__)
