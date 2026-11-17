import sys; sys.path.insert(0, "tools")
from cizim import *

# f tek fonksiyon, [−5, 5] aralığında tanımlı. Yalnızca x ≥ 0 parçası çizili: (0, 0) → (2, 4) → (5, −2).
fig, ax = sekil(5, 4.2)
eksenler(ax, (-5.8, 5.8), (-4.8, 4.8))
ax.set_xticks(range(-5, 6)); ax.set_xticklabels([str(t).replace("-", "−") if t else "" for t in range(-5, 6)], fontsize=10)
ax.set_yticks(range(-4, 5)); ax.set_yticklabels([str(t).replace("-", "−") if t else "" for t in range(-4, 5)], fontsize=10)
ax.plot([0, 2, 5], [0, 4, -2], color=MAVI)
nokta(ax, 2, 4, "", renk=MAVI)
nokta(ax, 5, -2, "", renk=MAVI)
ax.text(2.8, 3.3, "y = f(x)", color=MAVI, fontsize=12)
kaydet(fig, __file__)
