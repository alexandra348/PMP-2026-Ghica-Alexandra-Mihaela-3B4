
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import gamma
from scipy.optimize import minimize_scalar

# Datele problemei
n = 10
S = 180

# Prior Gamma(alpha, beta) - beta este rate
alpha, beta = 2, 0.1

# Posterior Gamma
a = alpha + S
b = beta + n

# Media si MAP
media = a / b
MAP = (a - 1) / b

# HDI 94% - intervalul cel mai scurt
def latime(q):
    return gamma.ppf(q + 0.94, a, scale=1/b) - \
           gamma.ppf(q, a, scale=1/b)

q = minimize_scalar(latime, bounds=(0, 0.06),
                    method="bounded").x

hdi = gamma.ppf([q, q + 0.94], a, scale=1/b)

print("Posterior: Gamma(", a, ",", b, ")")
print("Media:", media)
print("MAP:", MAP)
print("HDI 94%:", hdi)

# Grafic posterior
x = np.linspace(10, 27, 500)
y = gamma.pdf(x, a, scale=1/b)

plt.plot(x, y, label="Posterior")
plt.axvline(MAP, linestyle="--", label="MAP")
plt.axvspan(hdi[0], hdi[1], alpha=0.2, label="HDI 94%")
plt.xlabel("Apeluri pe ora")
plt.ylabel("Densitate")
plt.legend()
plt.show()
