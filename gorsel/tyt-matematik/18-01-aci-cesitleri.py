import sys; sys.path.insert(0, "tools")
from cizim import *

# Açının öğeleri ve ölçüsüne göre açı türleri: dar 40°, dik 90°, geniş 130°, doğru 180°, tam 360°.
def yon(d): return np.array([np.cos(np.radians(d)), np.sin(np.radians(d))])
def isin(ax, O, d, L=1.6, renk=YAZI):
    P = O + L * yon(d)
    ax.annotate("", xy=P, xytext=O, arrowprops=dict(arrowstyle="-|>", color=renk, lw=2, mutation_scale=14))
    return P

fig, axs = plt.subplots(2, 3, figsize=(6.5, 4.4))
O = np.array([0.0, 0.0])
for ax in axs.flat:
    ax.set_aspect("equal"); ax.axis("off"); ax.set_xlim(-1.9, 1.9); ax.set_ylim(-1.0, 1.9)

# 1) Açının öğeleri
ax = axs[0, 0]
O1 = np.array([-1.3, -0.3])
A = isin(ax, O1, 45, 2.2); B = isin(ax, O1, 0, 2.6)
nokta(ax, *O1, "O", dx=-0.35, dy=-0.1)
ax.text(*(A + [0.05, 0.05]), "A", fontsize=12); ax.text(*(B + [-0.1, 0.15]), "B", fontsize=12)
aci(ax, O1, B, A, r=0.45, renk=MAVI)
ax.text(-0.15, -0.72, "kol [OB", fontsize=11, color=SOLUK, ha="center")
ax.text(-1.25, 1.1, "kol [OA", fontsize=11, color=SOLUK, ha="center")
ax.text(-1.45, -0.85, "köşe", fontsize=11, color=SOLUK, ha="center")
ax.set_title("Açı: AOB", fontsize=12, color=YAZI)

# 2) Dar  3) Dik  4) Geniş
for ax, d, ad, ren in ((axs[0, 1], 40, "Dar açı", MAVI), (axs[0, 2], 90, "Dik açı", YESIL), (axs[1, 0], 130, "Geniş açı", SARI)):
    Ox = np.array([-0.7 if d < 100 else 0.1, -0.6])
    P1 = isin(ax, Ox, 0, 1.6); P2 = isin(ax, Ox, d, 1.6)
    ax.plot(*Ox, "o", color=YAZI, markersize=5)
    if d == 90:
        s = 0.28
        ax.plot([Ox[0] + s, Ox[0] + s, Ox[0]], [Ox[1], Ox[1] + s, Ox[1] + s], color=ren, lw=1.6)
        ax.text(Ox[0] + 0.6, Ox[1] + 0.55, "90°", color=ren, fontsize=12)
    else:
        aci(ax, Ox, P1, P2, r=0.5, renk=ren)
        m = np.radians(d / 2); ax.text(Ox[0] + 0.95 * np.cos(m), Ox[1] + 0.95 * np.sin(m), f"{d}°", color=ren, fontsize=12, ha="center", va="center")
    ax.set_title(ad, fontsize=12, color=YAZI)

# 5) Doğru açı
ax = axs[1, 1]
Ox = np.array([0.0, -0.3])
isin(ax, Ox, 0, 1.7); isin(ax, Ox, 180, 1.7)
ax.plot(*Ox, "o", color=YAZI, markersize=5)
ax.add_patch(patches.Arc(Ox, 0.9, 0.9, theta1=0, theta2=180, color=KIRMIZI, lw=1.6))
ax.text(0, 0.35, "180°", color=KIRMIZI, ha="center", fontsize=12)
ax.set_title("Doğru açı", fontsize=12, color=YAZI)

# 6) Tam açı
ax = axs[1, 2]
Ox = np.array([-0.6, 0.2])
isin(ax, Ox, 0, 1.9)
ax.text(Ox[0] + 1.75, Ox[1] + 0.15, "A = B", fontsize=11, color=SOLUK, ha="center")
ax.plot(*Ox, "o", color=YAZI, markersize=5)
ax.add_patch(patches.Arc(Ox, 0.9, 0.9, theta1=8, theta2=352, color=MAVI, lw=1.6))
ax.text(Ox[0], Ox[1] + 0.65, "360°", color=MAVI, ha="center", fontsize=12)
ax.set_title("Tam açı", fontsize=12, color=YAZI)

fig.tight_layout()
kaydet(fig, __file__)
