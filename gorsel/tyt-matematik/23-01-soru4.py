import sys; sys.path.insert(0, "tools")
from cizim import *

# ABCDE beşgeni: m(A)=2x, m(B)=x+25, m(C)=130, m(D)=100, m(E)=x+5. x=70 -> 140, 95, 130, 100, 75 (toplam 540).
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

acilar = [140, 95, 130, 100, 75]
V, s = cokgen(acilar, [3.0, 3.4, 2.6])
th = np.radians(-20); R = np.array([[np.cos(th), -np.sin(th)], [np.sin(th), np.cos(th)]]); V = V @ R.T
fig, ax = sekil(5.2, 4.6)
ax.set_aspect("equal"); ax.axis("off")
ax.add_patch(patches.Polygon(V, closed=True, facecolor=MAVI_ACIK, edgecolor=YAZI, lw=2.4))
O = V.mean(axis=0)
yaz = ["2x", "x + 25°", "130°", "100°", "x + 5°"]
for i, k in enumerate("ABCDE"):
    v = V[i]; u = (v - O) / np.linalg.norm(v - O); nokta(ax, *v, "")
    ax.text(*(v + 0.4 * u), k, ha="center", va="center", fontsize=14)
    # açı etiketi: köşeden içeri, açıortay yönünde
    p1, p2 = V[(i + 1) % 5], V[(i - 1) % 5]
    b = (p1 - v) / np.linalg.norm(p1 - v) + (p2 - v) / np.linalg.norm(p2 - v); b /= np.linalg.norm(b)
    aci(ax, v, p1, p2, r=0.5, ad="", renk=MAVI)
    ax.text(*(v + 1.15 * b), yaz[i], ha="center", va="center", color=MAVI, fontsize=12)
ax.set_xlim(V[:, 0].min() - 0.8, V[:, 0].max() + 0.8); ax.set_ylim(V[:, 1].min() - 0.8, V[:, 1].max() + 0.8)
kaydet(fig, __file__)
print([round(float(x), 2) for x in s])
