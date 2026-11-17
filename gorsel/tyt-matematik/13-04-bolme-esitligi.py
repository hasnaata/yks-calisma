import sys; sys.path.insert(0, "tools")
from cizim import *

# Bölme eşitliği P(x) = (x − 3)·B(x) + K içinde x = 3 yazılınca (x − 3) çarpanı 0 olur,
# B(3) ne olursa olsun çarpım 0'dır; geriye yalnızca K kalır: P(3) = K.
fig, ax = sekil(6, 3.6)
ax.set_xlim(0, 10); ax.set_ylim(0, 6); ax.axis("off")
# 1. satır: bölme eşitliği
ax.text(0.3, 5.2, r"$P(x)\ =\ (x-3)\cdot B(x)\ +\ K$", fontsize=19, va="center")
ax.text(9.7, 4.3, "bölme eşitliği", fontsize=12, color=SOLUK, ha="right", va="center")
ax.annotate("", xy=(2.6, 3.95), xytext=(2.6, 4.65), arrowprops=dict(arrowstyle="->", color=MAVI, lw=1.8))
ax.text(2.85, 4.3, "x = 3 yaz", fontsize=13, color=MAVI, va="center")
# 2. satır: x = 3
ax.add_patch(patches.FancyBboxPatch((1.95, 2.85), 2.75, 0.85, boxstyle="round,pad=0.06", fc=KIRMIZI_ACIK, ec=KIRMIZI, lw=1.3))
ax.text(0.3, 3.27, r"$P(3)\ =\ (3-3)\cdot B(3)\ +\ K$", fontsize=19, va="center")
ax.text(3.3, 2.25, "0 olur", fontsize=13, color=KIRMIZI, ha="center", va="center")
ax.text(6.5, 2.25, "B(3) bilinmese de\nçarpım 0", fontsize=12, color=SOLUK, ha="left", va="center")
# 3. satır: sonuç
ax.add_patch(patches.FancyBboxPatch((0.3, 0.45), 4.6, 0.95, boxstyle="round,pad=0.06", fc=YESIL_ACIK, ec=YESIL, lw=1.3))
ax.text(2.6, 0.92, r"$P(3)\ =\ K$", fontsize=20, va="center", ha="center", color=YESIL)
ax.text(5.3, 0.92, "kalan = P(3)", fontsize=14, color=YESIL, va="center")
kaydet(fig, __file__)
