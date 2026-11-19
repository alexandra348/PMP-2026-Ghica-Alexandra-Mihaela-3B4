
from pgmpy.models import DiscreteBayesianNetwork
from pgmpy.factors.discrete import TabularCPD
from pgmpy.inference import VariableElimination
import networkx as nx
import matplotlib.pyplot as plt

# a) Construirea retelei Bayesiene
model = DiscreteBayesianNetwork([
    ('S', 'O'), ('S', 'L'),
    ('S', 'M'), ('L', 'M')
])

pos = nx.circular_layout(model)
nx.draw(model, with_labels=True, pos=pos,
        alpha=0.5, node_size=2000)
plt.show()

# P(S)
CPD_S = TabularCPD(variable='S', variable_card=2,
                   values=[[0.6], [0.4]])

# P(O | S)
CPD_O = TabularCPD(variable='O', variable_card=2,
                   values=[[0.9, 0.3],
                           [0.1, 0.7]],
                   evidence=['S'],
                   evidence_card=[2])

# P(L | S)
CPD_L = TabularCPD(variable='L', variable_card=2,
                   values=[[0.7, 0.2],
                           [0.3, 0.8]],
                   evidence=['S'],
                   evidence_card=[2])

# P(M | S,L)
CPD_M = TabularCPD(variable='M', variable_card=2,
                   values=[[0.8, 0.4, 0.5, 0.1],
                           [0.2, 0.6, 0.5, 0.9]],
                   evidence=['S', 'L'],
                   evidence_card=[2, 2])

# Atasam probabilitatile
model.add_cpds(CPD_S, CPD_O, CPD_L, CPD_M)

print(model.get_cpds())
print("Model valid:", model.check_model())

# b) Clasificarea emailului
ve = VariableElimination(model)

rezultat = ve.query(
    variables=['S'],
    evidence={'O': 1, 'L': 1, 'M': 1}
)

print(rezultat)
print("Probabilitate spam:", rezultat.get_value(S=1))
