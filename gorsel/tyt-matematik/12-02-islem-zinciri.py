import sys; sys.path.insert(0, "tools")
from cizim import *

# f(x) = 3x − 2: önce 3 ile çarp, sonra 2 çıkar. f⁻¹: önce 2 ekle, sonra 3'e böl (ters sırada, ters işlem).
fig, ax = sekil(6.2, 3.0)
ax.axis("off"); ax.set_xlim(0, 10); ax.set_ylim(0, 5)
def kutu(x, y, s, renk, zemin):
    ax.text(x, y, s, ha="center", va="center", fontsize=15, color=YAZI,
            bbox=dict(boxstyle="round,pad=0.45", facecolor=zemin, edgecolor=renk, lw=1.5))
def ok(x1, x2, y, s, renk):
    ax.annotate("", xy=(x2, y), xytext=(x1, y), arrowprops=dict(arrowstyle="->", color=renk, lw=1.8))
    ax.text((x1 + x2) / 2, y + 0.45, s, ha="center", fontsize=14, color=renk, fontweight="bold")
# üst satır: f
ax.text(0.1, 4.6, "f", fontsize=16, color=YESIL, fontweight="bold")
kutu(1.0, 3.6, "2", YESIL, YESIL_ACIK); kutu(5.0, 3.6, "6", YESIL, YESIL_ACIK); kutu(9.0, 3.6, "4", YESIL, YESIL_ACIK)
ok(1.6, 4.4, 3.6, "· 3", YESIL); ok(5.6, 8.4, 3.6, "− 2", YESIL)
# alt satır: f⁻¹ (sağdan sola)
ax.text(0.1, 2.0, "f⁻¹", fontsize=16, color=SARI, fontweight="bold")
kutu(9.0, 1.0, "4", SARI, SARI_ACIK); kutu(5.0, 1.0, "6", SARI, SARI_ACIK); kutu(1.0, 1.0, "2", SARI, SARI_ACIK)
ok(8.4, 5.6, 1.0, "+ 2", SARI); ok(4.4, 1.6, 1.0, "÷ 3", SARI)
kaydet(fig, __file__)
