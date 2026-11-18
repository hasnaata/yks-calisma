import sys; sys.path.insert(0, "tools")
from cizim import *

# Ayrıtı 4 olan düzgün dört yüzlünün açınımı: kenarı 8 olan eşkenar üçgen, orta noktalar birleştirilmiş.
# Ortadaki üçgen taban (ABC); dıştaki üç üçgen katlanınca üç köşe de T'de buluşur. Üst yüzde yan yüz yüksekliği 2√3.
a = 4
s3 = np.sqrt(3)
T1, T2, T3 = np.array([0, 0.]), np.array([2 * a, 0.]), np.array([a, a * s3])   # büyük üçgen (köşeler T)
C = (T1 + T2) / 2; B = (T2 + T3) / 2; A = (T1 + T3) / 2                       # orta noktalar
fig, ax = sekil(4.6, 4.2)
for uc in ((T1, C, A), (T2, B, C), (T3, A, B)):
    ax.add_patch(patches.Polygon(uc, closed=True, facecolor=MAVI_ACIK, edgecolor="none", zorder=2))
ax.add_patch(patches.Polygon((T1, T2, T3), closed=True, facecolor="none", edgecolor=YAZI, lw=2.2, zorder=3))
ax.add_patch(patches.Polygon((A, B, C), closed=True, facecolor=SARI_ACIK, edgecolor="none", zorder=2.5))
for p, q in ((A, B), (B, C), (C, A)):
    ax.plot([p[0], q[0]], [p[1], q[1]], color=SARI, lw=2, ls=(0, (5, 3)), zorder=3)
M = (A + B) / 2
ax.plot([T3[0], M[0]], [T3[1], M[1]], color=KIRMIZI, lw=2.6, zorder=4)
u = np.array([1.0, 0]); w = np.array([0, 1.0]); r = 0.3
ax.plot([M[0] + r, M[0] + r, M[0]], [M[1], M[1] + r, M[1] + r], color=KIRMIZI, lw=1.3, zorder=5)
ax.text(M[0] - 0.22, (T3[1] + M[1]) / 2, "2√3", color=KIRMIZI, ha="right", va="center", fontsize=12)
for p, ad, dx, dy in ((T1, "T", -0.3, -0.2), (T2, "T", 0.3, -0.2), (T3, "T", 0, 0.32), (A, "A", -0.35, 0.05), (B, "B", 0.35, 0.05), (C, "C", 0, -0.35)):
    ax.text(p[0] + dx, p[1] + dy, ad, ha="center", va="center", fontsize=13)
for p, q, dx, dy in ((T1, C, 0, -0.32), (C, T2, 0, -0.32), (A, C, 0.32, 0.05), (B, C, -0.32, 0.05)):
    m = (p + q) / 2; ax.text(m[0] + dx, m[1] + dy, "4", ha="center", va="center", fontsize=12, color=MAVI)
ax.text(a, a * s3 / 2 - 0.55, "taban", ha="center", va="center", fontsize=11, color=SARI)
ax.set_xlim(-0.7, 2 * a + 0.7); ax.set_ylim(-0.7, a * s3 + 0.6)
ax.set_aspect("equal"); ax.axis("off")
kaydet(fig, __file__)
