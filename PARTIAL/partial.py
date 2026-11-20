
import numpy as np
from hmmlearn.hmm import CategoricalHMM

# a) Construirea modelului HMM
model = CategoricalHMM(n_components=4, init_params="")

model.startprob_ = np.array([0.2, 0.4, 0.4, 0])

# 0 este probabilitatea de a merge in starea care nu este vecina
model.transmat_ = np.array([
    [0.2, 0.4, 0.4, 0],
    [0.4, 0.2, 0.4, 0],
    [0, 0.4, 0.2, 0.4 ],
    [0.4, 0, 0.4 , 0.2]
])

model.emissionprob_ = np.array([
    [0.7, 0.2, 0.1, 0],
    [0.2, 0.6, 0.2, 0],
    [0.1, 0.3, 0.6, 0],
    [0.5, 0.2, 0.3, 0]
])

model.n_features = 4

# Observatii: red=0, green=1, blue=2
obs = np.array([0, 1, 2, 2, 0]).reshape(-1, 1)

#Forward - probabilitatea observatiilor
p = np.exp(model.score(obs))
print("Forward:", p)

# a) Viterbi - cel mai probabil traseu ascuns
logp, traseu = model.decode(obs, algorithm="viterbi")
stari = ["1", "2", "3", "4"]

print("Viterbi:", [stari[i] for i in traseu])
print("Probabilitatea traseului:", np.exp(logp))





#robotul nu mai poate ramane pe loc
# a) Construirea modelului HMM
model2 = CategoricalHMM(n_components=4, init_params="")

model2.startprob_ = np.array([0, 0.5, 0.5, 0])

# 0 este probabilitatea de a merge in starea care nu este vecina
model2.transmat_ = np.array([
    [0, 0.5, 0.5, 0],
    [0.5, 0, 0.5, 0],
    [0, 0.5, 0, 0.5 ],
    [0.5, 0, 0.5 , 0]
])

model2.emissionprob_ = np.array([
    [0.7, 0.2, 0.1, 0],
    [0.2, 0.6, 0.2, 0],
    [0.1, 0.3, 0.6, 0],
    [0.5, 0.2, 0.3, 0]
])

model2.n_features = 4

# Observatii: red=0, green=1, blue=2
obs2 = np.array([0, 1, 2, 2, 0]).reshape(-1, 1)

#Forward - probabilitatea observatiilor
p2 = np.exp(model2.score(obs2))
print("Forward:", p2)

# a) Viterbi - cel mai probabil traseu ascuns
logp2, traseu2 = model2.decode(obs2, algorithm="viterbi")
stari2 = ["1", "2", "3", "4"]

print("Viterbi:", [stari[i] for i in traseu2])
print("Probabilitatea traseului:", np.exp(logp2))

print("Diferenta rezultate:", abs(np.exp(logp2)-np.exp(logp)))
