import sys; sys.path.insert(0, "tools")
from cizim import *
def yon(d): return np.array([np.cos(np.radians(d)), np.sin(np.radians(d))])
def kesis(p, u, q, v):
    s = np.linalg.solve(np.array([u, -v]).T, q - p); return p + s[0] * u
def aciolc(k, p, q):
    return np.degrees(np.arccos(np.dot(p - k, q - k) / np.linalg.norm(p - k) / np.linalg.norm(q - k)))

# Alıştırma 10: iki paralel ayna. Işın üst aynaya P'de çarpar, alt aynaya Q'da çarpar.
# Q'dan çıkan ışın alt aynayla 32° yapar. P'de gelen ve yansıyan ışın arasındaki açı 180 − 64 = 116°.
h = 3.0; Q = np.array([4.6, 0.0]); P = Q + h / np.sin(np.radians(32)) * yon(148)
gel = P - 2.6 * yon(32); cik = Q + 2.6 * yon(32)
print("P", P, "açı", aciolc(P, gel, Q))
fig, ax = sekil(6, 3.6); ax.set_aspect("equal"); ax.axis("off")
for y, ad, dy in ((h, "üst ayna", 0.3), (0, "alt ayna", -0.3)):
    ax.plot([-3.4, 7.6], [y, y], color=MAVI, lw=4, solid_capstyle="butt")
    ax.text(7.6, y + dy, ad, color=MAVI, ha="right", va="bottom" if dy > 0 else "top", fontsize=12)
ok = dict(arrowstyle="-|>", color=KIRMIZI, lw=2, mutation_scale=16)
ax.annotate("", xy=P, xytext=gel, arrowprops=ok)
ax.annotate("", xy=Q, xytext=P, arrowprops=ok)
ax.annotate("", xy=cik, xytext=Q, arrowprops=ok)
nokta(ax, *P, "P", dx=-0.15, dy=0.25); nokta(ax, *Q, "Q", dx=-0.15, dy=-0.55)
aci(ax, Q, Q + yon(0), cik, r=0.8, ad="32°", renk=YESIL)
aci(ax, P, gel, Q, r=0.5, ad="?", renk=YESIL)
ax.set_xlim(-3.6, 7.8); ax.set_ylim(-0.9, h + 0.8)
kaydet(fig, __file__)
