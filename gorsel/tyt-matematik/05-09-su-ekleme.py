import sys; sys.path.insert(0, "tools")
from cizim import *

# %20'lik 300 g tuzlu su (60 g tuz). +100 g su -> 400 g, %15. 60 g su buharlaşır -> 240 g, %25. Tuz hep 60 g.
fig, ax = sekil(6.0, 3.9)
ax.axis("off")
H = 0.62
satirlar = [(2.4, "başlangıç", 240, "300 g · %20"), (1.2, "+100 g su", 340, "400 g · %15"), (0.0, "60 g su gitti", 180, "240 g · %25")]
for y, ad, su, sonuc in satirlar:
    ax.add_patch(patches.Rectangle((0, y), 60, H, facecolor=MAVI, edgecolor=MAVI, lw=1.2))
    ax.add_patch(patches.Rectangle((60, y), su, H, facecolor=MAVI_ACIK, edgecolor=MAVI, lw=1.2))
    ax.text(30, y + H / 2, "60", ha="center", va="center", color="white", fontsize=12, fontweight="bold")
    ax.text(60 + su / 2, y + H / 2, f"{su} su", ha="center", va="center", color=MAVI, fontsize=11)
    ax.text(0, y + H + 0.08, ad, ha="left", va="bottom", color=SOLUK, fontsize=11)
    ax.text(60 + su + 8, y + H / 2, sonuc, ha="left", va="center", color=YAZI, fontsize=12, fontweight="bold")
ax.text(550, 3.1, "koyu: tuz (g)   açık: su (g)", ha="right", va="bottom", color=SOLUK, fontsize=11)
ax.set_xlim(-2, 560); ax.set_ylim(-0.1, 3.45)
kaydet(fig, __file__)
