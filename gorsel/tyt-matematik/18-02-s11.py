import sys; sys.path.insert(0, "tools")
from cizim import *
def yon(d): return np.array([np.cos(np.radians(d)), np.sin(np.radians(d))])
def kesis(p, u, q, v):
    s = np.linalg.solve(np.array([u, -v]).T, q - p); return p + s[0] * u
def aciolc(k, p, q):
    return np.degrees(np.arccos(np.dot(p - k, q - k) / np.linalg.norm(p - k) / np.linalg.norm(q - k)))

# Alıştırma 11: k doğrusu yatayla 68°. d1 ve d2 yatay (paralel). d3 yatayla −2° eğik (paralel değil).
# d1'de sağ üst 68°; d2'de sağ alt 112° (sağ üst 68°); d3'te sol üst 110° (sağ üst 70°).
k = yon(68)
P1 = np.array([4.0 / np.tan(np.radians(68)), 4.0]); P2 = np.array([2.0 / np.tan(np.radians(68)), 2.0]); P3 = np.array([0.0, 0.0])
d3 = yon(-2)
print("d3 sağ üst", aciolc(P3, P3 + k, P3 + d3), "sol üst", aciolc(P3, P3 + k, P3 - d3))
fig, ax = sekil(6, 4.8); ax.set_aspect("equal"); ax.axis("off")
for P, ad in ((P1, "d₁"), (P2, "d₂")):
    ax.plot([-3.4, 4.6], [P[1], P[1]], color=YAZI); ax.text(-3.7, P[1], ad, ha="right", va="center")
ax.plot(*zip(P3 - 3.4 * d3, P3 + 4.6 * d3), color=YAZI); ax.text(*(P3 - 3.4 * d3 + np.array([-0.3, 0])), "d₃", ha="right", va="center")
ax.plot(*zip(P3 - 1.3 * k, P1 + 1.3 * k), color=YAZI); ax.text(*(P1 + 1.4 * k), "k", ha="left", va="bottom")
for P in (P1, P2, P3): nokta(ax, *P)
aci(ax, P1, P1 + yon(0), P1 + k, r=0.5, ad="68°", renk=MAVI)
aci(ax, P2, P2 - k, P2 + yon(0), r=0.42, renk=KIRMIZI); ax.text(P2[0] + 0.75, P2[1] - 0.45, "112°", color=KIRMIZI, va="center")
aci(ax, P3, P3 + k, P3 - d3, r=0.42, renk=YESIL); ax.text(P3[0] - 0.75, P3[1] + 0.45, "110°", color=YESIL, ha="right", va="center")
ax.set_xlim(-4.2, 4.8); ax.set_ylim(-1.4, 5.6)
kaydet(fig, __file__)
