import sys; sys.path.insert(0, "tools")
from cizim import *

# Tarh ABC: m(B)=45, m(C)=35, m(A)=100. B ve C açıortayları D'de buluşur: m(BDC)=180-(45+35)/2=140.
B = np.array([0.0, 0.0]); C = np.array([7.0, 0.0])
t = 7 * np.sin(np.radians(35)) / np.sin(np.radians(100))
A = B + t * np.array([np.cos(np.radians(45)), np.sin(np.radians(45))])
a, b, c = np.linalg.norm(B - C), np.linalg.norm(A - C), np.linalg.norm(A - B)
D = (a * A + b * B + c * C) / (a + b + c)   # iç açıortayların kesişimi
print("BDC", np.degrees(np.arccos(np.dot(B - D, C - D) / np.linalg.norm(B - D) / np.linalg.norm(C - D))))

fig, ax = sekil(6, 3.6)
ax.set_aspect("equal"); ax.axis("off")
ax.add_patch(patches.Polygon([A, B, C], closed=True, facecolor=YESIL_ACIK, edgecolor=YAZI, lw=2.2))
ax.plot(*zip(B, D, C), color=MAVI, lw=2)
nokta(ax, *A, "A", dx=-0.12, dy=0.2); nokta(ax, *B, "B", dx=-0.4, dy=-0.3); nokta(ax, *C, "C", dx=0.12, dy=-0.3)
nokta(ax, *D, "D", dx=-0.12, dy=0.22, renk=MAVI)
def isaret(kose, p, q, r, renk, n):
    """kose'deki p-q açısını yay ve ortasında n çentikle işaretler (eş açılar için)."""
    aci(ax, kose, p, q, r=r, renk=renk)
    a1 = np.arctan2(*(p - kose)[::-1]); a2 = np.arctan2(*(q - kose)[::-1])
    o = (a1 + a2) / 2
    for k in range(n):
        oo = o + (k - (n - 1) / 2) * 0.06
        u = np.array([np.cos(oo), np.sin(oo)])
        ax.plot(*zip(kose + (r - 0.12) * u, kose + (r + 0.12) * u), color=renk, lw=1.6)
isaret(B, C, D, 1.1, SARI, 1); isaret(B, D, A, 1.1, SARI, 1)
isaret(C, A, D, 1.4, KIRMIZI, 2); isaret(C, D, B, 1.4, KIRMIZI, 2)
aci(ax, D, C, B, r=0.35, ad="140°", renk=MAVI)
ax.set_xlim(-0.7, 7.7); ax.set_ylim(-0.6, A[1] + 0.6)
kaydet(fig, __file__)
