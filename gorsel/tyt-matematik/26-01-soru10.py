import sys; sys.path.insert(0, "tools")
from cizim import *

# Eğik izdüşüm: genişlik (x) ve yükseklik (z) gerçek ölçüde, derinlik (y) yarıya kısaltılmış ve 40° eğik.
KD, TETA = 0.5, np.radians(40)
CX, SY = KD * np.cos(TETA), KD * np.sin(TETA)
GOZ = np.array([CX, -1.0, SY])  # bakan göze doğru yön

def P(p):
    x, y, z = p
    return np.array([x + CX * y, z + SY * y])

def prizma(ax, taban, v, renkler=None, lw=2.0):
    """taban: dışbükey çokgenin 3B köşeleri, v: öteleme vektörü (yanal ayrıt). Görünmeyen ayrıtlar kesikli."""
    taban = [np.array(t, float) for t in taban]; v = np.array(v, float); n = len(taban)
    ust = [t + v for t in taban]; merkez = sum(taban) / n + v / 2
    yuzler = [list(range(n)), list(range(n, 2 * n))] + [[i, (i + 1) % n, n + (i + 1) % n, n + i] for i in range(n)]
    kose = taban + ust; gorunur = []
    for y in yuzler:
        a, b, c = kose[y[0]], kose[y[1]], kose[y[2]]
        nor = np.cross(b - a, c - a)
        if np.dot(nor, sum(kose[i] for i in y) / len(y) - merkez) < 0: nor = -nor
        gorunur.append(np.dot(nor, GOZ) > 1e-9)
    renkler = renkler or {}
    for k, y in enumerate(yuzler):
        if k in renkler and gorunur[k]:
            ax.add_patch(patches.Polygon([P(kose[i]) for i in y], closed=True, facecolor=renkler[k], edgecolor="none", zorder=1))
    kenarlar = {}
    for k, y in enumerate(yuzler):
        for j in range(len(y)):
            e = tuple(sorted((y[j], y[(j + 1) % len(y)])))
            kenarlar[e] = kenarlar.get(e, False) or gorunur[k]
    for (i, j), g in kenarlar.items():
        a, b = P(kose[i]), P(kose[j])
        if g: ax.plot([a[0], b[0]], [a[1], b[1]], color=YAZI, lw=lw, zorder=4, solid_capstyle="round")
        else: ax.plot([a[0], b[0]], [a[1], b[1]], color=SOLUK, lw=1.3, ls=(0, (4, 3)), zorder=2)
    return kose

def cizgi(ax, p, q, renk=KIRMIZI, lw=2.4, ls="-", z=5):
    a, b = P(p), P(q); ax.plot([a[0], b[0]], [a[1], b[1]], color=renk, lw=lw, ls=ls, zorder=z)

def yaz(ax, p, s, dx=0.0, dy=0.0, renk=YAZI, boy=13, **kw):
    q = P(p); ax.text(q[0] + dx, q[1] + dy, s, ha=kw.pop("ha", "center"), va=kw.pop("va", "center"), color=renk, fontsize=boy, zorder=7, **kw)

def dik(ax, k, u, w, r=0.4, renk=YAZI):
    k, u, w = np.array(k, float), np.array(u, float), np.array(w, float)
    u = u / np.linalg.norm(u); w = w / np.linalg.norm(w)
    pts = [P(k + r * u), P(k + r * u + r * w), P(k + r * w)]
    ax.plot([p[0] for p in pts], [p[1] for p in pts], color=renk, lw=1.3, zorder=6)

def bitir(ax, pay=0.6):
    ax.set_aspect("equal"); ax.axis("off"); ax.autoscale_view(); ax.margins(0.04)
# Alıştırma 10: soldaki kap 12 × 10 tabanlı, sıvı 15 cm; sağdaki kap tabanı dik kenarları 12 ve 15 olan dik üçgen
fig, ax = sekil(6, 3.8)
# sol kap: 12 (x) × 10 (y) × 20 (z), sıvı 15
prizma(ax, [(0, 0, 0), (12, 0, 0), (12, 0, 15), (0, 0, 15)], (0, 10, 0), renkler={0: MAVI_ACIK, 1: MAVI_ACIK, 4: MAVI_ACIK, 2: MAVI_ACIK, 3: MAVI_ACIK, 5: MAVI_ACIK}, lw=1.2)
prizma(ax, [(0, 0, 0), (12, 0, 0), (12, 10, 0), (0, 10, 0)], (0, 0, 20), lw=1.9)
yaz(ax, (6, 0, 0), "12", dy=-1.1, boy=12)
yaz(ax, (12, 5, 0), "10", dx=1.6, dy=-0.4, boy=12)
yaz(ax, (0, 0, 7.5), "15", dx=-2.4, renk=MAVI, boy=12)
ax.annotate("", xy=(-1.0, 15), xytext=(-1.0, 0), arrowprops=dict(arrowstyle="<->", color=MAVI, lw=1.2))
# sağ kap: taban dik üçgen (x yönünde 12, y yönünde 15), yükseklik 24
ox = 22
prizma(ax, [(ox, 0, 0), (ox + 12, 0, 0), (ox + 12, 15, 0)], (0, 0, 24), lw=1.9)
dik(ax, (ox + 12, 0, 0), (-1, 0, 0), (0, 1, 0), r=2.4)
yaz(ax, (ox + 6, 0, 0), "12", dy=-1.1, boy=12)
yaz(ax, (ox + 12, 7.5, 0), "15", dx=1.6, dy=-0.5, boy=12)
ax.set_xlim(-5, 42); ax.set_ylim(-3, 30)
ax.set_aspect("equal"); ax.axis("off")
kaydet(fig, __file__)
