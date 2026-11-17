import sys; sys.path.insert(0, "tools")
from cizim import *

# Toplamı 58, farkı 14 olan iki sayı: küçük x, büyük x + 14. Şerit modeli.
fig, ax = sekil(6.2, 2.9)
ax.axis("off"); ax.set_aspect("equal")
X, F, H = 3.0, 1.4, 0.7          # x şeridinin ve 14 parçasının genişliği, şerit yüksekliği
y_b, y_k = 1.3, 0.2              # büyük ve küçük sayı şeritlerinin alt kenarı
ax.text(-0.15, y_b + H / 2, "Büyük", ha="right", va="center", fontsize=13)
ax.text(-0.15, y_k + H / 2, "Küçük", ha="right", va="center", fontsize=13)
ax.add_patch(patches.Rectangle((0, y_b), X, H, facecolor=MAVI_ACIK, edgecolor=MAVI, lw=1.5))
ax.text(X / 2, y_b + H / 2, "x", ha="center", va="center", fontsize=15, color=MAVI)
ax.add_patch(patches.Rectangle((X, y_b), F, H, facecolor=SARI_ACIK, edgecolor=SARI, lw=1.5))
ax.text(X + F / 2, y_b + H / 2, "14", ha="center", va="center", fontsize=15, color=SARI, fontweight="bold")
ax.add_patch(patches.Rectangle((0, y_k), X, H, facecolor=MAVI_ACIK, edgecolor=MAVI, lw=1.5))
ax.text(X / 2, y_k + H / 2, "x", ha="center", va="center", fontsize=15, color=MAVI)
# toplam parantezi (sağda)
xr = X + F + 0.25
ax.plot([xr, xr + 0.2, xr + 0.2, xr], [y_b + H, y_b + H, y_k, y_k], color=YAZI, lw=1.4)
ax.text(xr + 0.35, (y_b + H + y_k) / 2, "toplam\n58", ha="left", va="center", fontsize=13)
# denklem
ax.text((X + F) / 2, -0.35, "2x + 14 = 58   →   x = 22,  büyük = 36", ha="center", va="top", fontsize=13, color=YAZI)
ax.set_xlim(-1.5, X + F + 1.6); ax.set_ylim(-0.9, 2.15)
kaydet(fig, __file__)
