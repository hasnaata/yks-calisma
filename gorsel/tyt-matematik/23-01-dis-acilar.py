import sys; sys.path.insert(0, "tools")
from cizim import *

# Beşgen; iç açılar 110, 100, 115, 105, 110 -> dış açılar 70, 80, 65, 75, x=70 (toplam 360).
# Her kenar, yürüme yönünde bir sonraki köşenin ötesine uzatılır (kesikli); dış açı uzantı ile sonraki kenar arasıdır.
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

ic = [110, 100, 115, 105, 110]
V, s = cokgen(ic, [3.6, 3.0, 3.2])
th = np.radians(-8); R = np.array([[np.cos(th), -np.sin(th)], [np.sin(th), np.cos(th)]]); V = V @ R.T
n = 5
fig, ax = sekil(5.6, 5.0)
ax.set_aspect("equal"); ax.axis("off")
ax.add_patch(patches.Polygon(V, closed=True, facecolor=MAVI_ACIK, edgecolor=YAZI, lw=2.4))
yaz = {0: "70°", 1: "80°", 2: "65°", 3: "75°", 4: "x"}
for i in range(n):
    P, Q = V[(i - 1) % n], V[i]           # P -> Q kenarı Q'nun ötesine uzatılır
    u = (Q - P) / np.linalg.norm(Q - P); R2 = Q + 1.5 * u
    ax.plot(*zip(Q, R2), color=SOLUK, lw=1.6, ls="--")
    aci(ax, Q, R2, V[(i + 1) % n], r=0.55, ad=yaz[i], renk=KIRMIZI)
    print(i, 180 - ic[i])
for i in range(n): nokta(ax, *V[i], "")
pad = 1.9
ax.set_xlim(V[:, 0].min() - pad, V[:, 0].max() + pad); ax.set_ylim(V[:, 1].min() - pad, V[:, 1].max() + pad)
kaydet(fig, __file__)
