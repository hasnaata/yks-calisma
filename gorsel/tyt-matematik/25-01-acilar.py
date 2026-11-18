import sys; sys.path.insert(0, "tools")
from cizim import *

# Örnek 1: ABCD yamuğu, [AB] ∥ [DC]. m(A) = 70°, m(B) = 55° → m(D) = 110°, m(C) = 125°.
a, h, aA, aB = 8.0, 3.2, 70, 55
A = np.array([0.0, 0.0]); B = np.array([a, 0.0])
D = np.array([h / np.tan(np.radians(aA)), h]); C = np.array([a - h / np.tan(np.radians(aB)), h])
def acisi(K, P, Q):
    u, v = P - K, Q - K
    return round(float(np.degrees(np.arccos(np.dot(u, v) / np.linalg.norm(u) / np.linalg.norm(v)))), 3)
print("A", acisi(A, B, D), "B", acisi(B, A, C), "C", acisi(C, B, D), "D", acisi(D, A, C))

def paralel_isareti(P, Q, renk=SOLUK):
    M = (P + Q) / 2
    ax.annotate("", xy=M + np.array([0.18, 0]), xytext=M - np.array([0.18, 0]),
                arrowprops=dict(arrowstyle="-|>", color=renk, lw=1.4, mutation_scale=14))

fig, ax = sekil(6, 3.2)
ax.set_aspect("equal"); ax.axis("off")
ax.plot(*zip(A, B, C, D, A), color=YAZI)
paralel_isareti(A, B); paralel_isareti(D, C)
nokta(ax, *A, ""); nokta(ax, *B, ""); nokta(ax, *C, ""); nokta(ax, *D, "")
ax.text(A[0] - 0.2, A[1] - 0.15, "A", ha="right", va="top")
ax.text(B[0] + 0.2, B[1] - 0.15, "B", ha="left", va="top")
ax.text(C[0] + 0.2, C[1] + 0.1, "C", ha="left", va="bottom")
ax.text(D[0] - 0.2, D[1] + 0.1, "D", ha="right", va="bottom")
aci(ax, A, B, D, r=0.55, ad="70°", renk=MAVI)
aci(ax, D, C, A, r=0.45, ad="110°", renk=MAVI)
aci(ax, B, C, A, r=0.55, ad="55°", renk=YESIL)
aci(ax, C, D, B, r=0.45, ad="125°", renk=YESIL)
ax.text(a / 2, -0.35, "alt taban", ha="center", va="top", color=SOLUK, fontsize=12)
ax.text((D[0] + C[0]) / 2, h + 0.3, "üst taban", ha="center", va="bottom", color=SOLUK, fontsize=12)
ax.set_xlim(-0.8, a + 0.8); ax.set_ylim(-0.9, h + 0.9)
kaydet(fig, __file__)
