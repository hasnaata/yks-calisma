"""26-03 (Dik Piramitler) şekillerinin ortak yardımcıları. Tek başına şekil üretmez.
Kullanım: exec(pathlib.Path(__file__).with_name("26-03-ortak.py").read_text(encoding="utf8"))
Eğik izdüşüm: genişlik (x) ve yükseklik (z) gerçek ölçüde, derinlik (y) yarıya kısaltılmış ve 40° eğik."""
import sys; sys.path.insert(0, "tools")
from cizim import *

KD, TETA = 0.5, np.radians(40)
CX, SY = KD * np.cos(TETA), KD * np.sin(TETA)
GOZ = np.array([CX, -1.0, SY])  # bakan göze doğru yön

def P(p):
    x, y, z = p
    return np.array([x + CX * y, z + SY * y])

def cokyuzlu(ax, kose, yuzler, renkler=None, lw=2.0):
    """Dışbükey cisim: kose 3B noktalar, yuzler köşe sıra listeleri. Görünmeyen ayrıtlar kesikli."""
    kose = [np.array(k, float) for k in kose]; merkez = sum(kose) / len(kose); gorunur = []
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
    return kose, gorunur

def piramit(ax, taban, T, renkler=None, lw=2.0):
    """taban: çokgenin köşeleri (z = 0), T: tepe. Yüz 0 taban, yüz i+1 = T, taban[i], taban[i+1]."""
    n = len(taban)
    yuzler = [list(range(n))] + [[n, i, (i + 1) % n] for i in range(n)]
    return cokyuzlu(ax, list(taban) + [T], yuzler, renkler, lw)

def cizgi(ax, p, q, renk=KIRMIZI, lw=2.4, ls="-", z=5):
    a, b = P(p), P(q); ax.plot([a[0], b[0]], [a[1], b[1]], color=renk, lw=lw, ls=ls, zorder=z)

def yaz(ax, p, s, dx=0.0, dy=0.0, renk=YAZI, boy=13, **kw):
    q = P(p); ax.text(q[0] + dx, q[1] + dy, s, ha=kw.pop("ha", "center"), va=kw.pop("va", "center"), color=renk, fontsize=boy, zorder=7, **kw)

def dik(ax, k, u, w, r=0.4, renk=YAZI):
    """k köşesinde u ve w yönleri arasında dik açı işareti."""
    k, u, w = np.array(k, float), np.array(u, float), np.array(w, float)
    u = u / np.linalg.norm(u); w = w / np.linalg.norm(w)
    pts = [P(k + r * u), P(k + r * u + r * w), P(k + r * w)]
    ax.plot([p[0] for p in pts], [p[1] for p in pts], color=renk, lw=1.3, zorder=6)

def nk(ax, p, renk=YAZI):
    q = P(p); ax.plot(q[0], q[1], "o", color=renk, markersize=5, zorder=8)

def bitir(ax):
    ax.set_aspect("equal"); ax.axis("off")

def kare(ax, a, h, adlar=True, G_goster=True):
    """Kare dik piramit (T, ABCD): A önde solda, B önde sağda. Noktaları sözlük olarak döndürür."""
    A, B, C, D = (0, 0, 0), (a, 0, 0), (a, a, 0), (0, a, 0); G = (a / 2, a / 2, 0); T = (a / 2, a / 2, h)
    piramit(ax, [A, B, C, D], T, renkler={1: SARI_ACIK, 2: MAVI_ACIK})
    s = max(a, h) / 14
    if adlar:
        for p, ad, dx, dy in ((A, "A", -1, -0.6), (B, "B", 1, -0.6), (C, "C", 1, 0.1), (D, "D", -1, 0.4), (T, "T", 0, 0.9)):
            yaz(ax, p, ad, dx * s, dy * s, boy=13)
        if G_goster:
            nk(ax, G); yaz(ax, G, "G", -1.1 * s, -0.4 * s, boy=13)
    ax.set_xlim(-2 * s, a + CX * a + 2.2 * s); ax.set_ylim(-1.6 * s, h + SY * a / 2 + 1.6 * s); bitir(ax)
    return dict(A=A, B=B, C=C, D=D, G=G, T=T, s=s)
