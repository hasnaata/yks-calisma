import sys; sys.path.insert(0, "tools")
from cizim import *

# Alıştırma Soru 8: haftalık satış gelirinin dağılımı. Defter %35, Kalem %20, Çanta %15, Kitap ? (gerçekte %30).
fig, ax = sekil(5, 4)
oranlar = [35, 30, 15, 20]
adlar = ["Defter\n%35", "Kitap\n?", "Çanta\n%15", "Kalem\n%20"]
renkler = [(MAVI_ACIK, MAVI), (SARI_ACIK, SARI), (KIRMIZI_ACIK, KIRMIZI), (YESIL_ACIK, YESIL)]
w, _ = ax.pie(oranlar, startangle=90, counterclock=False, colors=[r[0] for r in renkler],
              wedgeprops=dict(edgecolor="white", linewidth=2))
for parca, (ic, kenar) in zip(w, renkler):
    parca.set_edgecolor(kenar); parca.set_linewidth(1.4)
aci0 = 90
for oran, ad, (ic, kenar) in zip(oranlar, adlar, renkler):
    orta = np.radians(aci0 - oran * 3.6 / 2)
    ax.text(0.6 * np.cos(orta), 0.6 * np.sin(orta), ad, ha="center", va="center", fontsize=13, color=kenar)
    aci0 -= oran * 3.6
ax.set_aspect("equal")
kaydet(fig, __file__)
