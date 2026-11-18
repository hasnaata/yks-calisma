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
# Üçgen, dörtgen (kare) ve altıgen dik prizma; yükseklik 4
fig, ax = sekil(6.4, 4.2)
h = 4
def cokgen(n, r, ox):
    return [(ox + r * np.cos(2 * np.pi * i / n - np.pi / 2 - (np.pi / n if n % 2 == 0 else 0)) * 1.0,
             1.2 + r * np.sin(2 * np.pi * i / n - np.pi / 2 - (np.pi / n if n % 2 == 0 else 0)) * 1.6, 0) for i in range(n)]
taban3 = [(0, 0, 0), (3, 0, 0), (1.5, 2.6, 0)]
taban4 = [(5, 0, 0), (8, 0, 0), (8, 3, 0), (5, 3, 0)]
r6 = 1.6
taban6 = [(12 + r6 * np.cos(np.radians(60 * i)), 1.6 + r6 * np.sin(np.radians(60 * i)) , 0) for i in range(6)]
taban6 = [(x, y - 1.6 + 1.386, z) for x, y, z in taban6]
for t, n in ((taban3, 3), (taban4, 4), (taban6, 6)):
    prizma(ax, t, (0, 0, h), renkler={1: SARI_ACIK, **{k: MAVI_ACIK for k in range(2, n + 2)}})
yazilar = [(2.0, "üçgen dik prizma", "6 köşe · 9 ayrıt · 5 yüz"),
           (7.0, "dörtgen dik prizma", "8 köşe · 12 ayrıt · 6 yüz"),
           (12.6, "altıgen dik prizma", "12 köşe · 18 ayrıt · 8 yüz")]
for x, s1, s2 in yazilar:
    ax.text(x, -0.7, s1.replace(" dik", "\ndik"), ha="center", va="top", fontsize=11.5, color=YAZI, linespacing=1.2)
    ax.text(x, -2.7, s2.replace(" · ", "\n"), ha="center", va="top", fontsize=11, color=SOLUK, linespacing=1.25)
ax.set_xlim(-0.6, 14.6); ax.set_ylim(-6.6, 5.6)
ax.set_aspect("equal"); ax.axis("off")
kaydet(fig, __file__)
