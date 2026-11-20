from pgmpy.models import DiscreteBayesianNetwork
from pgmpy.factors.discrete import TabularCPD
from pgmpy.inference import VariableElimination
import networkx as nx
import matplotlib.pyplot as plt

# Construirea grafului
model = DiscreteBayesianNetwork([
    ('O', 'H'), ('O', 'W'),
    ('H', 'R'), ('W', 'R'),
    ('H', 'E'), ('R', 'C')
])

# Desenarea grafului
pos = nx.circular_layout(model)
nx.draw(model, with_labels=True, pos=pos,
        alpha=0.5, node_size=2000)
plt.show()

# P(O)
CPD_O = TabularCPD(variable='O', variable_card=2,
                   values=[[0.3], [0.7]])

# P(H | O)
CPD_H = TabularCPD(variable='H', variable_card=2,
                   values=[[0.9, 0.2],
                           [0.1, 0.8]],
                   evidence=['O'], evidence_card=[2])

# P(W | O)
CPD_W = TabularCPD(variable='W', variable_card=2,
                   values=[[0.1, 0.6],
                           [0.9, 0.4]],
                   evidence=['O'], evidence_card=[2])

# P(R | H, W)
CPD_R = TabularCPD(variable='R', variable_card=2,
                   values=[[0.6, 0.9, 0.3, 0.5],
                           [0.4, 0.1, 0.7, 0.5]],
                   evidence=['H', 'W'],
                   evidence_card=[2, 2])

# P(E | H)
CPD_E = TabularCPD(variable='E', variable_card=2,
                   values=[[0.8, 0.2],
                           [0.2, 0.8]],
                   evidence=['H'], evidence_card=[2])

# P(C | R)
CPD_C = TabularCPD(variable='C', variable_card=2,
                   values=[[0.85, 0.40],
                           [0.15, 0.60]],
                   evidence=['R'], evidence_card=[2])

# Atasarea tabelelor
model.add_cpds(CPD_O, CPD_H, CPD_W,
               CPD_R, CPD_E, CPD_C)

# Afisarea tabelelor
print(model.get_cpds())

# Verificarea modelului
print(model.check_model())

#b)


ve = VariableElimination(model)

# P(H=yes | C=comfortable)
print(ve.query(variables=['H'], evidence={'C': 0}))

# P(E=high | C=comfortable)
print(ve.query(variables=['E'], evidence={'C': 0}))

# MAP(H,W | C=comfortable)
print(ve.map_query(variables=['H', 'W'],
                   evidence={'C': 0}))


