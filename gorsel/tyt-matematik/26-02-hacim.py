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


def kup(ax, a, renkler=None, adlar=True, boy=13):
    k = prizma(ax, [(0, 0, 0), (a, 0, 0), (a, a, 0), (0, a, 0)], (0, 0, a), renkler=renkler)
    if adlar:
        s = a / 4
        kay = [(-0.08, -0.07), (0.07, -0.07), (0.08, 0.0), (-0.07, 0.05), (-0.08, 0.0), (0.07, -0.06), (0.06, 0.06), (-0.06, 0.06)]
        for p, ad, (dx, dy) in zip(k, "ABCDEFGH", kay): yaz(ax, p, ad, dx * s * 4, dy * s * 4, boy=boy)
    return k

def izgara(ax, a, n, renk=SOLUK):
    for i in range(1, n):
        t = a * i / n
        for p, q in (((t, 0, 0), (t, 0, a)), ((0, 0, t), (a, 0, t)), ((a, 0, t), (a, a, t)), ((a, t, 0), (a, t, a)), ((t, 0, a), (t, a, a)), ((0, t, a), (a, t, a))):
            cizgi(ax, p, q, renk=renk, lw=0.9, z=3)

# Ayrıtı 4 olan küp: görünen yüzler 4 × 4 = 16 birim kareye bölünmüş
a = 4
fig, ax = sekil(4.2, 4.0)
kup(ax, a, renkler={0: None, 1: SARI_ACIK, 2: MAVI_ACIK, 3: MAVI_ACIK})
izgara(ax, a, 4)
yaz(ax, (a / 2, 0, 0), "4", dy=-0.45)
yaz(ax, (a, a / 2, 0), "4", dx=0.45, dy=-0.15)
yaz(ax, (0, 0, a / 2), "4", dx=-0.4)
ax.set_xlim(-0.8, 6.2); ax.set_ylim(-0.9, 6.0)
ax.set_aspect("equal"); ax.axis("off")
kaydet(fig, __file__)
