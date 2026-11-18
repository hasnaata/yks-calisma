import pathlib; exec(pathlib.Path(__file__).with_name("26-03-ortak.py").read_text(encoding="utf8"))
# Örnek 2: kare dik piramit, taban ayrıtı 6, yükseklik 4.
# Üstte TGM (M, [BC]'nin orta noktası): 4, 3, hY = 5. Altta TGB: 4, 3√2, √34.
a, h = 6, 4
fig, axs = plt.subplots(2, 1, figsize=(5.2, 7.4))
for ax, tur in zip(axs, ("yuz", "ayrit")):
    A, B, C, D = (0, 0, 0), (a, 0, 0), (a, a, 0), (0, a, 0); G = (3, 3, 0); T = (3, 3, h); M = (6, 3, 0)
    piramit(ax, [A, B, C, D], T, renkler={1: SARI_ACIK, 2: MAVI_ACIK}, lw=1.8)
    cizgi(ax, T, G, renk=MAVI, lw=2.6, ls=(0, (5, 2.5))); nk(ax, G, YAZI)
    yaz(ax, (3, 3, 2), "4", -0.35, 0.2, renk=MAVI)
    if tur == "yuz":
        cizgi(ax, G, M, renk=YESIL, lw=2.6, ls=(0, (5, 2.5))); cizgi(ax, T, M, renk=KIRMIZI, lw=3)
        dik(ax, G, (1, 0, 0), (0, 0, 1), r=0.45)
        dik(ax, M, (0, 1, 0), (-3, 0, 4), r=0.45, renk=KIRMIZI)
        yaz(ax, (4.0, 3, 0), "3", 0, 0.3, renk=YESIL)
        yaz(ax, (4.5, 3, 2), r"$h_Y = 5$", 1.3, 0.35, renk=KIRMIZI)
        yaz(ax, M, "M", 0.45, -0.25)
        ax.text(-1, 6.0, "TGM: yan yüz yüksekliği", fontsize=12.5, color=KIRMIZI)
    else:
        cizgi(ax, G, B, renk=YESIL, lw=2.6, ls=(0, (5, 2.5))); cizgi(ax, T, B, renk=KIRMIZI, lw=3)
        yaz(ax, (4.5, 1.5, 0), r"$3\sqrt{2}$", -1.05, -0.17, renk=YESIL, boy=12.5)
        yaz(ax, (4.5, 1.5, 2), r"$\sqrt{34}$", 0.95, 0.15, renk=KIRMIZI, boy=12.5)
        ax.text(-1, 6.0, "TGB: yanal ayrıt", fontsize=12.5, color=KIRMIZI)
    for p, s, dx, dy in ((A, "A", -0.4, -0.2), (B, "B", 0.4, -0.25), (C, "C", 0.4, 0.05), (D, "D", -0.4, 0.15), (T, "T", 0, 0.35), (G, "G", -0.45, -0.1)):
        yaz(ax, p, s, dx, dy, boy=12.5)
    ax.set_xlim(-1, 9.2); ax.set_ylim(-0.8, 6.5); bitir(ax)
fig.subplots_adjust(hspace=0.08)
kaydet(fig, __file__)
