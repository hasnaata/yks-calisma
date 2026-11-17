import sys; sys.path.insert(0, "tools")
from cizim import *

# Haftanın günleri bir çember üstünde: çarşambadan 90 gün sonra = 12 tam tur + 6 adım = salı.
fig, ax = sekil(5.2, 5.0)
ax.axis("off"); ax.set_aspect("equal")
gunler = ["Pazartesi", "Salı", "Çarşamba", "Perşembe", "Cuma", "Cumartesi", "Pazar"]
R = 2.2
ax.add_patch(patches.Circle((0, 0), R, fill=False, ec=CIZGI, lw=1.6))
def konum(i, r=R):
    a = np.radians(90 - (i - 2) * 360 / 7)   # çarşamba en üstte
    return r * np.cos(a), r * np.sin(a)
for i, g in enumerate(gunler):
    x, y = konum(i)
    renk, dolgu = (MAVI, MAVI_ACIK) if i == 2 else (KIRMIZI, KIRMIZI_ACIK) if i == 1 else (YAZI, "white")
    ax.plot(x, y, "o", ms=13, mfc=dolgu, mec=renk if i in (1, 2) else SOLUK, mew=1.8, zorder=5)
    tx, ty = konum(i, R + 0.45)
    ha = "center" if abs(tx) < 0.5 else ("left" if tx > 0 else "right")
    ax.text(tx, ty + (0.2 if abs(tx) < 0.5 else 0), g, ha=ha, va="center", fontsize=12.5, color=renk,
            fontweight="bold" if i in (1, 2) else "normal")
# Çarşambadan saat yönünde 6 adım (salıya kadar) giden yay
r = R - 0.42
t = np.radians(np.linspace(90 - 7, 90 - 6 * 360 / 7 + 9, 200))
ax.plot(r * np.cos(t[:-8]), r * np.sin(t[:-8]), color=MAVI, lw=1.8)
ax.annotate("", xy=(r * np.cos(t[-1]), r * np.sin(t[-1])), xytext=(r * np.cos(t[-9]), r * np.sin(t[-9])),
            arrowprops=dict(arrowstyle="-|>", color=MAVI, lw=1.8, mutation_scale=16))
ax.text(0, 0.25, "90 = 7 · 12 + 6", ha="center", va="center", fontsize=13, color=YAZI)
ax.text(0, -0.3, "12 tur + 6 adım", ha="center", va="center", fontsize=11.5, color=SOLUK)
ax.set_xlim(-4.2, 4.2); ax.set_ylim(-3.4, 3.4)
kaydet(fig, __file__)
