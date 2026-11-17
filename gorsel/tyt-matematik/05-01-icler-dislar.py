import sys; sys.path.insert(0, "tools")
from cizim import *

# 4 : 6 = 10 : 15 orantısında içler (6 ve 10) ile dışlar (4 ve 15).
fig, ax = sekil(6, 3.2)
ax.axis("off"); ax.set_xlim(0, 10); ax.set_ylim(-0.5, 5.2)
X = {"4": 1.2, ":1": 2.5, "6": 3.7, "=": 5.0, "10": 6.4, ":2": 7.6, "15": 8.8}
Y = 2.6
for s, x in X.items():
    renk = KIRMIZI if s in ("4", "15") else (MAVI if s in ("6", "10") else YAZI)
    ax.text(x, Y, s.rstrip("12") if s.startswith(":") else s, ha="center", va="center", fontsize=30, color=renk, fontweight="bold" if renk != YAZI else "normal")
# içler: üstte mavi yay
ax.add_patch(patches.Arc((5.05, Y + 0.55), 2.7, 1.6, theta1=0, theta2=180, color=MAVI, lw=2.4))
ax.text(5.0, Y + 1.65, "içler", ha="center", va="center", color=MAVI, fontsize=15)
# dışlar: altta kırmızı yay
ax.add_patch(patches.Arc((5.0, Y - 0.55), 7.6, 2.6, theta1=180, theta2=360, color=KIRMIZI, lw=2.4))
ax.text(5.0, Y - 2.15, "dışlar", ha="center", va="center", color=KIRMIZI, fontsize=15)
ax.text(5.0, 4.9, "6 · 10 = 60", ha="center", va="center", color=MAVI, fontsize=15)
ax.text(5.0, -0.25, "4 · 15 = 60", ha="center", va="center", color=KIRMIZI, fontsize=15)
kaydet(fig, __file__)
