import sys; sys.path.insert(0, "tools")
from cizim import *

# [OB açıortay; |OB| = 5, B'den kollara dikmeler |BA| = |BC| = 3, |OA| = |OC| = 4 (3-4-5 dik üçgeni).
t = np.arctan2(3, 4)                      # yarım açı
O = np.array([0.0, 0.0])
u1 = np.array([1.0, 0.0]); u2 = np.array([np.cos(2 * t), np.sin(2 * t)])
B = 5 * np.array([np.cos(t), np.sin(t)])
A = 4 * u1; C = 4 * u2
print("BA", np.linalg.norm(B - A), "BC", np.linalg.norm(B - C), "OC", np.linalg.norm(C))

fig, ax = sekil(6, 4.2)
ax.set_aspect("equal"); ax.axis("off")
for u in (u1, u2):
    ax.annotate("", xy=6.3 * u, xytext=O, arrowprops=dict(arrowstyle="-|>", color=YAZI, lw=2))
ax.annotate("", xy=6.6 * B / 5, xytext=O, arrowprops=dict(arrowstyle="-|>", color=MAVI, lw=2))
ax.plot(*zip(B, A), color=KIRMIZI, lw=2); ax.plot(*zip(B, C), color=KIRMIZI, lw=2)
k = 0.28
ax.plot([A[0] - k, A[0] - k, A[0]], [0, k, k], color=KIRMIZI, lw=1.3)
w = -u1 * 0 + (-u2); n = np.array([u2[1], -u2[0]])  # C'de dik açı işareti
p1 = C - k * u2; p2 = p1 + k * n; p3 = C + k * n
ax.plot(*zip(p1, p2, p3), color=KIRMIZI, lw=1.3)
nokta(ax, *O, "O", dx=-0.45, dy=-0.15); nokta(ax, *A, "A", dx=-0.1, dy=-0.5)
nokta(ax, *C, "C", dx=-0.5, dy=0.05); nokta(ax, *B, "B", dx=0.2, dy=-0.45, renk=MAVI)
aci(ax, O, A, B, r=1.3, renk=MAVI); aci(ax, O, B, C, r=1.5, renk=MAVI)
ax.text(1.75, 0.3, "α", color=MAVI, fontsize=13, ha="center", va="center")
m2 = 1.55 * np.array([np.cos(1.5 * t), np.sin(1.5 * t)])
ax.text(*(m2 * 1.25), "α", color=MAVI, fontsize=13, ha="center", va="center")
ax.text(4.25, 1.5, "3", color=KIRMIZI, fontsize=13)
mBC = (B + C) / 2 + 0.4 * u2
ax.text(*mBC, "3", color=KIRMIZI, fontsize=13, ha="center", va="center")
ax.text(2.0, -0.45, "4", color=YAZI, fontsize=13, ha="center")
mOC = C / 2 - 0.35 * n
ax.text(*mOC, "4", color=YAZI, fontsize=13, ha="center", va="center")
ax.text(*(B / 2 + np.array([0.15, -0.38])), "5", color=MAVI, fontsize=13, ha="center")
ax.set_xlim(-0.8, 6.6); ax.set_ylim(-0.8, 6.3 * u2[1] + 0.3)
kaydet(fig, __file__)
