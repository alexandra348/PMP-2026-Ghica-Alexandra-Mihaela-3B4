
import numpy as np
from hmmlearn.hmm import CategoricalHMM

# a) Construirea modelului HMM
model = CategoricalHMM(n_components=3, init_params="")

model.startprob_ = np.array([0.4, 0.3, 0.3])

model.transmat_ = np.array([
    [0.6, 0.3, 0.1],
    [0.2, 0.7, 0.1],
    [0.3, 0.2, 0.5]
])

model.emissionprob_ = np.array([
    [0.1, 0.7, 0.2],
    [0.05, 0.25, 0.7],
    [0.8, 0.15, 0.05]
])

model.n_features = 3

# Observatii: Low=0, Medium=1, High=2
obs = np.array([1, 2, 0]).reshape(-1, 1)

# b) Forward - probabilitatea observatiilor
p = np.exp(model.score(obs))
print("Forward:", p)

# c) Viterbi - cel mai probabil traseu ascuns
logp, traseu = model.decode(obs, algorithm="viterbi")
stari = ["Walking", "Running", "Resting"]

print("Viterbi:", [stari[i] for i in traseu])
print("Probabilitatea traseului:", np.exp(logp))

# d) Simulare - 10000 secvente
rng = np.random.default_rng(42)
aparitii = 0

for _ in range(10000):
    stare = rng.choice(3, p=model.startprob_)
    secventa = [rng.choice(3, p=model.emissionprob_[stare])]

    for i in range(2):
        stare = rng.choice(3, p=model.transmat_[stare])
        secventa.append(rng.choice(3, p=model.emissionprob_[stare]))

    if secventa == [1, 2, 0]:
        aparitii += 1

print("Aparitii:", aparitii)
print("Probabilitatea simulata:", aparitii / 10000)
