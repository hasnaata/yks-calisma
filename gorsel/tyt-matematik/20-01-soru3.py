import sys; sys.path.insert(0, "tools")
from cizim import *

# [OB açıortay; |OB| = 13, |BA| = 5 (B'den [OA'ya dikme) → |BC| = 5, |OC| = |OA| = 12. Ölçek: 1 birim = 0,45.
s = 0.45
t = np.arctan2(5, 12)
O = np.array([0.0, 0.0])
u1 = np.array([1.0, 0.0]); u2 = np.array([np.cos(2 * t), np.sin(2 * t)])
B = 13 * s * np.array([np.cos(t), np.sin(t)])
A = 12 * s * u1; C = 12 * s * u2
print("BA", np.linalg.norm(B - A) / s, "BC", np.linalg.norm(B - C) / s, "OC", np.linalg.norm(C) / s, "açı AOC", np.degrees(2 * t))

fig, ax = sekil(6, 3.2)
ax.set_aspect("equal"); ax.axis("off")
for u in (u1, u2):
    ax.annotate("", xy=7.4 * u, xytext=O, arrowprops=dict(arrowstyle="-|>", color=YAZI, lw=2))
ax.annotate("", xy=7.6 * B / np.linalg.norm(B), xytext=O, arrowprops=dict(arrowstyle="-|>", color=MAVI, lw=2))
ax.plot(*zip(B, A), color=KIRMIZI, lw=2); ax.plot(*zip(B, C), color=KIRMIZI, lw=2)
k = 0.22
ax.plot([A[0] - k, A[0] - k, A[0]], [0, k, k], color=KIRMIZI, lw=1.3)
n = np.array([u2[1], -u2[0]])
p1 = C - k * u2; p2 = p1 + k * n; p3 = C + k * n
ax.plot(*zip(p1, p2, p3), color=KIRMIZI, lw=1.3)
nokta(ax, *O, "O", dx=-0.45, dy=-0.15); nokta(ax, *A, "A", dx=-0.1, dy=-0.5)
nokta(ax, *C, "C", dx=-0.25, dy=0.25); nokta(ax, *B, "B", dx=0.15, dy=-0.5, renk=MAVI)
aci(ax, O, A, B, r=1.5, renk=MAVI); aci(ax, O, B, C, r=1.7, renk=MAVI)
ax.text(A[0] + 0.15, A[1] + B[1] / 2 - 0.15, "5", color=KIRMIZI, fontsize=13)
ax.text(*(B / 2 + np.array([0.0, -0.45])), "13", color=MAVI, fontsize=13, ha="center")
ax.text(*(C / 2 + 0.3 * (-n) + np.array([0, 0.05])), "?", color=YAZI, fontsize=14, ha="center", va="center")
ax.set_xlim(-0.8, 7.6); ax.set_ylim(-0.8, 7.4 * u2[1] + 0.3)
kaydet(fig, __file__)
