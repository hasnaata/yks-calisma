import pathlib; exec(pathlib.Path(__file__).with_name("26-03-ortak.py").read_text(encoding="utf8"))
# Örnek 3: kare dik piramidin açınımı, taban ayrıtı 6, yan yüz yüksekliği 5
a, hy = 6, 5
fig, ax = sekil(5, 5)
ax.add_patch(patches.Polygon([(0, 0), (a, 0), (a, a), (0, a)], closed=True, facecolor=MAVI_ACIK, edgecolor=YAZI, lw=2, zorder=2))
ucg = [[(0, 0), (a, 0), (a / 2, -hy)], [(a, 0), (a, a), (a + hy, a / 2)], [(a, a), (0, a), (a / 2, a + hy)], [(0, a), (0, 0), (-hy, a / 2)]]
for u in ucg: ax.add_patch(patches.Polygon(u, closed=True, facecolor=SARI_ACIK, edgecolor=YAZI, lw=2, zorder=1))
ax.plot([a / 2, a / 2], [0, -hy], color=KIRMIZI, lw=2, ls=(0, (4, 3)), zorder=3)
ax.plot([a / 2, a / 2 + 0.4, a / 2 + 0.4], [-0.4, -0.4, 0], color=KIRMIZI, lw=1.3, zorder=3)
ax.text(a / 2 - 0.25, -hy / 2 - 0.3, r"$h_Y = 5$", color=KIRMIZI, fontsize=13, ha="right", va="center")
ax.text(a / 2, a / 2, "taban\n6 · 6", ha="center", va="center", fontsize=13, color=MAVI)
ax.text(a / 2, 0.35, "6", ha="center", va="bottom", fontsize=13)
ax.text(a - 0.35, a / 2 + 1.1, "6", ha="right", va="center", fontsize=13)
for x, y in ((a + hy * 0.42, a / 2), (a / 2, a + hy * 0.42), (-hy * 0.42, a / 2)):
    ax.text(x, y, "yan\nyüz", ha="center", va="center", fontsize=11, color=SARI)
ax.set_xlim(-hy - 0.4, a + hy + 0.4); ax.set_ylim(-hy - 0.4, a + hy + 0.4); bitir(ax)
kaydet(fig, __file__)
