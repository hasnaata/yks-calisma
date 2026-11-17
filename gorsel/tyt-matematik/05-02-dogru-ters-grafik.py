import sys; sys.path.insert(0, "tools")
from cizim import *

# Sol: doğru orantı (elma kg - fiyat TL), y = 15x. Sağ: ters orantı (işçi - gün), x·y = 180.
fig, (a1, a2) = plt.subplots(1, 2, figsize=(6.5, 3.4))
for ax in (a1, a2):
    for s in ("top", "right"): ax.spines[s].set_visible(False)
    ax.grid(True, color=CIZGI, linewidth=0.6, alpha=0.7); ax.set_axisbelow(True)
    ax.tick_params(labelsize=10)

x = np.linspace(0, 11, 50)
a1.plot(x, 15 * x, color=MAVI)
for px, py in ((6, 90), (10, 150)):
    a1.plot([px, px], [0, py], "--", color=SOLUK, lw=1); a1.plot([0, px], [py, py], "--", color=SOLUK, lw=1)
    a1.plot(px, py, "o", color=MAVI, markersize=6, zorder=5)
a1.set_xlim(0, 11.5); a1.set_ylim(0, 175)
a1.set_xticks([0, 2, 4, 6, 8, 10]); a1.set_yticks([0, 30, 60, 90, 120, 150])
a1.set_xlabel("Elma (kg)", fontsize=11); a1.set_ylabel("Fiyat (TL)", fontsize=11)
a1.set_title("Doğru orantı", fontsize=12, color=MAVI)
a1.text(0.6, 122, "fiyat ÷ kg = 15", fontsize=10, color=MAVI)

x = np.linspace(7, 31, 200)
a2.plot(x, 180 / x, color=YESIL)
for px, py in ((12, 15), (20, 9)):
    a2.plot([px, px], [0, py], "--", color=SOLUK, lw=1); a2.plot([5, px], [py, py], "--", color=SOLUK, lw=1)
    a2.plot(px, py, "o", color=YESIL, markersize=6, zorder=5)
a2.set_xlim(5, 31); a2.set_ylim(0, 27)
a2.set_xticks([5, 10, 15, 20, 25, 30]); a2.set_yticks([0, 5, 9, 15, 20, 25])
a2.set_xlabel("İşçi sayısı", fontsize=11); a2.set_ylabel("Gün", fontsize=11)
a2.set_title("Ters orantı", fontsize=12, color=YESIL)
a2.text(17, 21, "işçi × gün = 180", fontsize=10, color=YESIL)
fig.tight_layout(w_pad=2)
kaydet(fig, __file__)
