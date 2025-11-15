import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

# Parameter model
r = 0.1       # laju pertumbuhan
K = 1000      # kapasitas maksimum
P0 = 100      # populasi awal
t = np.linspace(0, 50, 500)  # waktu simulasi (0-50 tahun)

# Persamaan model logistik
def logistic_model(P, t, r, K):
    dPdt = r * P * (1 - P / K)
    return dPdt

# Solusi numerik menggunakan odeint
P = odeint(logistic_model, P0, t, args=(r, K))

# Plot hasil simulasi
plt.figure(figsize=(9,6))
plt.plot(t, P, label='Populasi (P)', color='blue')
plt.title('Pemodelan Pertumbuhan Populasi (Model Logistik)')
plt.xlabel('Waktu (tahun)')
plt.ylabel('Jumlah Populasi')
plt.grid(True)
plt.legend()
plt.show()
