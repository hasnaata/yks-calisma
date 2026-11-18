import sys; sys.path.insert(0, "tools")
from cizim import *

# ABCDE beşgeni: m(A)=100, m(B)=120, m(C)=95, m(D)=110, m(E)=x=115 (toplam 540).
# A'dan çizilen iki köşegen beşgeni 3 üçgene böler.
def cokgen(acilar, kenarlar):
    """İç açıları (sırayla, saat yönünün tersine) ve ilk n−2 kenarı verilen dışbükey çokgenin köşeleri."""
    n = len(acilar); yon = [0.0]
    for a in acilar[1:]: yon.append(yon[-1] + 180 - a)
    u = [np.array([np.cos(np.radians(t)), np.sin(np.radians(t))]) for t in yon]
    s = list(kenarlar)
    kalan = -sum(si * ui for si, ui in zip(s, u))
    M = np.column_stack([u[n - 2], u[n - 1]]); son = np.linalg.solve(M, kalan)
    assert (son > 0).all(), son
    s += list(son); V = [np.zeros(2)]
    for i in range(n - 1): V.append(V[-1] + s[i] * u[i])
    return np.array(V), s

acilar = [100, 120, 95, 110, 115]
V, s = cokgen(acilar, [4.0, 3.2, 3.4])
th = np.radians(-10); R = np.array([[np.cos(th), -np.sin(th)], [np.sin(th), np.cos(th)]]); V = V @ R.T
A, B, C, D, E = V
fig, ax = sekil(5.4, 4.8)
ax.set_aspect("equal"); ax.axis("off")
for ucg, renk in (([A, B, C], MAVI_ACIK), ([A, C, D], YESIL_ACIK), ([A, D, E], SARI_ACIK)):
    ax.add_patch(patches.Polygon(ucg, closed=True, facecolor=renk, edgecolor="none"))
ax.add_patch(patches.Polygon(V, closed=True, fill=False, edgecolor=YAZI, lw=2.4))
for P in (C, D): ax.plot(*zip(A, P), color=SOLUK, lw=1.5, ls="--")
O = V.mean(axis=0)
for k, v in zip("ABCDE", V):
    u = (v - O) / np.linalg.norm(v - O); nokta(ax, *v, "")
    ax.text(*(v + 0.42 * u), k, ha="center", va="center", fontsize=14)
yaz = ["100°", "120°", "95°", "110°", "x"]
for i in range(5):
    aci(ax, V[i], V[(i + 1) % 5], V[(i - 1) % 5], r=0.55, ad=yaz[i], renk=MAVI if i < 4 else KIRMIZI)
for ucg, no in (([A, B, C], "1"), ([A, C, D], "2"), ([A, D, E], "3")):
    m = ucg[0] + 0.48 * ((ucg[1] + ucg[2]) / 2 - ucg[0]); ax.text(*m, no, ha="center", va="center", fontsize=15, color=SOLUK, fontweight="bold")
ax.set_xlim(V[:, 0].min() - 0.8, V[:, 0].max() + 0.8); ax.set_ylim(V[:, 1].min() - 0.8, V[:, 1].max() + 0.8)
kaydet(fig, __file__)
print([round(x, 2) for x in s])
