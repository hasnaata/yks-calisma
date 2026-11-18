import sys; sys.path.insert(0, "tools")
from cizim import *

# Dik (ortografik) izdüşüm: cisim z ekseni etrafında FI kadar döndürülür, göz EL kadar yukarıdan bakar.
# Bütün uzunluklar gerçek 3B ölçülerden hesaplanır.
FI, EL = np.radians(-12), np.radians(25)
def don(p):
    x, y, z = p
    return np.array([x * np.cos(FI) - y * np.sin(FI), x * np.sin(FI) + y * np.cos(FI), z])
GOZ = np.array([0.0, -np.cos(EL), np.sin(EL)])  # döndürülmüş koordinatta göze doğru yön
def P(p):
    x, y, z = don(np.array(p, float))
    return np.array([x, z * np.cos(EL) + y * np.sin(EL)])

def cisim(ax, kose, yuzler, renkler=None, lw=2.0):
    """kose: 3B noktalar, yuzler: köşe sıraları (dışbükey cisim). Görünmeyen ayrıtlar kesikli."""
    kose = [np.array(k, float) for k in kose]; m = sum(kose) / len(kose); gor = []
    for y in yuzler:
        a, b, c = kose[y[0]], kose[y[1]], kose[y[2]]
        n = np.cross(b - a, c - a)
        if np.dot(n, sum(kose[i] for i in y) / len(y) - m) < 0: n = -n
        gor.append(np.dot(don(n), GOZ) > 1e-9)
    for k, y in enumerate(yuzler):
        if renkler and k in renkler and gor[k]:
            ax.add_patch(patches.Polygon([P(kose[i]) for i in y], closed=True, facecolor=renkler[k], edgecolor="none", zorder=1))
    ked = {}
    for k, y in enumerate(yuzler):
        for j in range(len(y)):
            e = tuple(sorted((y[j], y[(j + 1) % len(y)]))); ked[e] = ked.get(e, False) or gor[k]
    for (i, j), g in ked.items():
        a, b = P(kose[i]), P(kose[j])
        if g: ax.plot([a[0], b[0]], [a[1], b[1]], color=YAZI, lw=lw, zorder=4, solid_capstyle="round")
        else: ax.plot([a[0], b[0]], [a[1], b[1]], color=SOLUK, lw=1.3, ls=(0, (4, 3)), zorder=2)
    return gor

def dortyuzlu(a):
    """Düzgün dört yüzlü: taban ABC (z=0), tepe T ağırlık merkezinin üstünde."""
    A = np.array([0, 0, 0.]); B = np.array([a, 0, 0.]); C = np.array([a / 2, a * np.sqrt(3) / 2, 0.])
    H = (A + B + C) / 3; T = H + np.array([0, 0, a * np.sqrt(6) / 3])
    return A, B, C, T, H
DY_YUZ = [[0, 1, 2], [0, 1, 3], [1, 2, 3], [2, 0, 3]]

def cizgi(ax, p, q, renk=KIRMIZI, lw=2.4, ls="-", z=5):
    a, b = P(p), P(q); ax.plot([a[0], b[0]], [a[1], b[1]], color=renk, lw=lw, ls=ls, zorder=z, solid_capstyle="round")

def yaz(ax, p, s, dx=0.0, dy=0.0, renk=YAZI, boy=13, **kw):
    q = P(p); ax.text(q[0] + dx, q[1] + dy, s, ha=kw.pop("ha", "center"), va=kw.pop("va", "center"), color=renk, fontsize=boy, zorder=7, **kw)

def dik(ax, k, u, w, r=0.4, renk=YAZI):
    k, u, w = np.array(k, float), np.array(u, float), np.array(w, float)
    u = u / np.linalg.norm(u); w = w / np.linalg.norm(w)
    pts = [P(k + r * u), P(k + r * u + r * w), P(k + r * w)]
    ax.plot([p[0] for p in pts], [p[1] for p in pts], color=renk, lw=1.3, zorder=6)

def nk(ax, p, renk=YAZI):
    q = P(p); ax.plot(q[0], q[1], "o", color=renk, markersize=5, zorder=6)

def bitir(ax, pay=0.6):
    ax.set_aspect("equal"); ax.axis("off"); ax.autoscale_view()
    x0, x1 = ax.get_xlim(); y0, y1 = ax.get_ylim()
    ax.set_xlim(x0 - pay, x1 + pay); ax.set_ylim(y0 - pay, y1 + pay)
# Soru 11: ayrıtı 3 olan iki düzgün dört yüzlü ABC yüzlerinden yapıştırılmış; tepe noktaları T ve S.
A, B, C, T, H = dortyuzlu(3)
S = 2 * H - T
fig, ax = sekil(4.0, 5.0)
cisim(ax, [A, B, C, T, S], [[0, 1, 3], [1, 2, 3], [2, 0, 3], [0, 1, 4], [1, 2, 4], [2, 0, 4]], renkler={0: MAVI_ACIK, 3: MAVI_ACIK})
cizgi(ax, T, S, renk=KIRMIZI, lw=2.0, ls=(0, (5, 3)))

yaz(ax, A, "A", dx=-0.25, dy=0.0); yaz(ax, B, "B", dx=0.25, dy=0.0); yaz(ax, C, "C", dx=0.3, dy=0.04)
yaz(ax, T, "T", dy=0.22); yaz(ax, S, "S", dy=-0.24)
yaz(ax, (A + T) / 2, "3", dx=-0.22, dy=0.05); yaz(ax, (A + B) / 2, "3", dx=-0.3, dy=-0.2)
bitir(ax, 0.3)
kaydet(fig, __file__)
