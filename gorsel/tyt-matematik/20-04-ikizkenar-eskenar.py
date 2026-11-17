import sys; sys.path.insert(0, "tools")
from cizim import *

def uz(P, Q): return round(float(np.linalg.norm(np.asarray(P) - np.asarray(Q))), 3)
def kenar(ax, P, Q, metin, G, d=0.45, renk=YAZI, fs=13):
    """[PQ] kenarının ortasına, G'nin ters tarafına etiket."""
    P, Q = np.asarray(P, float), np.asarray(Q, float); M = (P + Q) / 2
    u = (Q - P) / np.linalg.norm(Q - P); v = np.array([-u[1], u[0]])
    if np.dot(v, M - np.asarray(G)) < 0: v = -v
    ax.text(*(M + d * v), metin, ha="center", va="center", color=renk, fontsize=fs)
def dik_ayak(P, Q, R):
    """R noktasından PQ doğrusuna inen dikmenin ayağı."""
    P, Q, R = (np.asarray(t, float) for t in (P, Q, R))
    u = (Q - P) / np.linalg.norm(Q - P); return P + np.dot(R - P, u) * u
def dik(ax, ayak, p1, p2, k=0.3, renk=YAZI):
    """ayak noktasında, ayak->p1 ve ayak->p2 yönleri arasında dik açı karesi."""
    ayak = np.asarray(ayak, float)
    u = (np.asarray(p1) - ayak) / np.linalg.norm(np.asarray(p1) - ayak); v = (np.asarray(p2) - ayak) / np.linalg.norm(np.asarray(p2) - ayak)
    ax.plot(*zip(ayak + k * u, ayak + k * (u + v), ayak + k * v), color=renk, lw=1.2)
def centik(ax, P, Q, n=1, renk=YAZI, L=0.18, ara=0.12):
    """[PQ] ortasına n tane eşlik çentiği."""
    P, Q = np.asarray(P, float), np.asarray(Q, float); M = (P + Q) / 2
    u = (Q - P) / np.linalg.norm(Q - P); v = np.array([-u[1], u[0]])
    for i in range(n):
        c = M + (i - (n - 1) / 2) * ara * u
        ax.plot(*zip(c - L * v, c + L * v), color=renk, lw=1.3)

# Sol: |AB|=|AC|=10, |BC|=12 => |BH|=|HC|=6, |AH|=8.
# Sağ: kenarı 6 olan eşkenar üçgen: h = 3√3 ≈ 5,196; G köşeye 2√3, kenara √3.
fig, axs = plt.subplots(1, 2, figsize=(6.4, 3.3), gridspec_kw={"width_ratios": [12, 6.6]})
ax = axs[0]; ax.set_aspect("equal"); ax.axis("off")
B, C, H, A = np.array([0.0, 0.0]), np.array([12.0, 0.0]), np.array([6.0, 0.0]), np.array([6.0, 8.0])
print("AB", uz(A, B), "AC", uz(A, C), "AH", uz(A, H))
G = (A + B + C) / 3
ax.plot(*zip(A, B, C, A), color=YAZI); ax.plot(*zip(A, H), color=KIRMIZI, lw=2.2)
dik(ax, H, A, C, k=0.7, renk=KIRMIZI)
centik(ax, A, B, 1, L=0.35); centik(ax, A, C, 1, L=0.35)
centik(ax, B, H, 2, renk=MAVI, L=0.35, ara=0.3); centik(ax, H, C, 2, renk=MAVI, L=0.35, ara=0.3)
aci(ax, A, B, H, r=1.5, renk=YESIL); aci(ax, A, H, C, r=1.8, renk=YESIL)
for P, ad, d in ((A, "A", (-0.4, 0.4)), (B, "B", (-0.9, -0.9)), (C, "C", (0.25, -0.9))): ax.text(P[0] + d[0], P[1] + d[1], ad, fontsize=13)
ax.text(H[0] - 0.4, -1.3, "H", color=KIRMIZI, fontsize=13)
kenar(ax, A, B, "10", G, d=0.9); kenar(ax, A, C, "10", G, d=0.9)
ax.text(3, -1.2, "6", color=MAVI, fontsize=13, ha="center"); ax.text(9, -1.2, "6", color=MAVI, fontsize=13, ha="center")
ax.text(6.35, 3.2, "8", color=KIRMIZI, fontsize=14)
ax.set_xlim(-1.2, 13.2); ax.set_ylim(-1.8, 9.2)
ax.set_title("İkizkenar", fontsize=13)
ax = axs[1]; ax.set_aspect("equal"); ax.axis("off")
a = 6.0
B, C = np.array([0.0, 0.0]), np.array([a, 0.0]); A = np.array([a / 2, a * np.sqrt(3) / 2])
F, E, D = (B + C) / 2, (A + C) / 2, (A + B) / 2
G = (A + B + C) / 3
print("h", uz(A, F), "AG", uz(A, G), "GF", uz(G, F))
ax.plot(*zip(A, B, C, A), color=YAZI)
ax.plot(*zip(A, F), color=KIRMIZI, lw=2); ax.plot(*zip(B, E), color=MAVI, lw=1.6); ax.plot(*zip(C, D), color=YESIL, lw=1.6)
dik(ax, F, A, C, k=0.4, renk=KIRMIZI)
nokta(ax, *G, "", renk=YAZI)
ax.text(G[0] + 0.15, G[1] - 0.75, "G", fontsize=13, fontweight="bold")
for P, ad, d in ((A, "A", (-0.25, 0.3)), (B, "B", (-0.5, -0.6)), (C, "C", (0.15, -0.6))): ax.text(P[0] + d[0], P[1] + d[1], ad, fontsize=13)
ax.text(F[0] - 0.25, -0.75, "F", color=KIRMIZI, fontsize=13)
P = B + 0.3 * (A - B); ax.text(P[0] - 0.45, P[1] + 0.25, "6", fontsize=13, ha="center")
P = C + 0.3 * (A - C); ax.text(P[0] + 0.45, P[1] + 0.25, "6", fontsize=13, ha="center")
ax.text(1.5, -0.75, "6", fontsize=13, ha="center")
ax.set_xlim(-0.7, 6.7); ax.set_ylim(-1.1, 6.1)
ax.set_title("Eşkenar", fontsize=13)
fig.subplots_adjust(wspace=0.12)
kaydet(fig, __file__)
