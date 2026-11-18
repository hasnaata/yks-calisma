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


# Soru 12: ayrıtı 6 olan küpün sağ-ön-üst köşesinden ayrıtı 2 olan küp çıkarılmış
fig, ax = sekil(4.4, 4.2)
def yuz(pts, renk):
    ax.add_patch(patches.Polygon([P(p) for p in pts], closed=True, facecolor=renk, edgecolor=YAZI, lw=1.9, joinstyle="round", zorder=3))
# arkadaki görünmeyen ayrıtlar
for p, q in (((0, 6, 0), (6, 6, 0)), ((0, 6, 0), (0, 0, 0)), ((0, 6, 0), (0, 6, 6))):
    a_, b_ = P(p), P(q); ax.plot([a_[0], b_[0]], [a_[1], b_[1]], color=SOLUK, lw=1.3, ls=(0, (4, 3)), zorder=2)
yuz([(0, 0, 0), (6, 0, 0), (6, 0, 4), (4, 0, 4), (4, 0, 6), (0, 0, 6)], SARI_ACIK)          # ön yüz
yuz([(6, 0, 0), (6, 6, 0), (6, 6, 6), (6, 2, 6), (6, 2, 4), (6, 0, 4)], MAVI_ACIK)          # sağ yüz
yuz([(0, 0, 6), (4, 0, 6), (4, 2, 6), (6, 2, 6), (6, 6, 6), (0, 6, 6)], MAVI_ACIK)          # üst yüz
yuz([(4, 0, 4), (6, 0, 4), (6, 2, 4), (4, 2, 4)], KIRMIZI_ACIK)                             # oyuğun tabanı
yuz([(4, 0, 4), (4, 2, 4), (4, 2, 6), (4, 0, 6)], KIRMIZI_ACIK)                             # oyuğun sol duvarı
yuz([(4, 2, 4), (6, 2, 4), (6, 2, 6), (4, 2, 6)], KIRMIZI_ACIK)                             # oyuğun arka duvarı
yaz(ax, (3, 0, 0), "6", dy=-0.5)
yaz(ax, (0, 0, 3), "6", dx=-0.45)
yaz(ax, (6, 3, 0), "6", dx=0.5, dy=-0.2)
yaz(ax, (5, 0, 4), "2", dy=-0.4)
yaz(ax, (4, 0, 5), "2", dx=-0.35)
ax.set_xlim(-0.9, 9.0); ax.set_ylim(-1.0, 8.4)
ax.set_aspect("equal"); ax.axis("off")
kaydet(fig, __file__)
