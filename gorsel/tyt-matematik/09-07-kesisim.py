import sys; sys.path.insert(0, "tools")
from cizim import *
from itertools import combinations

# Sol: 3 çember, her ikisi 2 noktada kesişir: 2·C(3,2) = 6 nokta.
# Sağ: 2 üçgen en çok 6 noktada kesişir.
fig, (a1, a2) = plt.subplots(1, 2, figsize=(6.4, 3.4))
for ax in (a1, a2): ax.set_aspect("equal"); ax.axis("off")

M = [np.array([0.0, 0.55]), np.array([-0.5, -0.3]), np.array([0.5, -0.3])]; r = 0.8
for m, c in zip(M, (MAVI, YESIL, SARI)): a1.add_patch(patches.Circle(m, r, fill=False, color=c, lw=2))
for m1, m2 in combinations(M, 2):
    d = np.linalg.norm(m2 - m1); a = d / 2; h = np.sqrt(r * r - a * a)
    o = m1 + (m2 - m1) / 2; n = np.array([-(m2 - m1)[1], (m2 - m1)[0]]) / d
    for s in (1, -1): a1.plot(*(o + s * h * n), "o", color=KIRMIZI, markersize=7, zorder=5)
a1.set_xlim(-1.45, 1.45); a1.set_ylim(-1.25, 1.5)
a1.set_title("3 çember → 6 nokta", fontsize=13, color=YAZI)

def ucgen(t0): return [np.array([np.cos(t), np.sin(t)]) for t in np.radians([t0, t0 + 120, t0 + 240])]
T1, T2 = ucgen(90), ucgen(-90)
for T, c in ((T1, MAVI), (T2, YESIL)): a2.add_patch(patches.Polygon(T, closed=True, fill=False, edgecolor=c, lw=2))
def kes(p, q, s, t):
    A = np.array([q - p, s - t]).T
    try: u, v = np.linalg.solve(A, s - p)
    except np.linalg.LinAlgError: return None
    return p + u * (q - p) if 0 <= u <= 1 and 0 <= v <= 1 else None
say = 0
for i in range(3):
    for j in range(3):
        x = kes(T1[i], T1[(i + 1) % 3], T2[j], T2[(j + 1) % 3])
        if x is not None: a2.plot(*x, "o", color=KIRMIZI, markersize=7, zorder=5); say += 1
print("üçgen kesişim", say)
a2.set_xlim(-1.2, 1.2); a2.set_ylim(-1.25, 1.5)
a2.set_title("2 üçgen → 6 nokta", fontsize=13, color=YAZI)
fig.tight_layout()
kaydet(fig, __file__)
