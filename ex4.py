import pyagrum as gum
import pyagrum.lib.notebook as gnb

model = gum.MarkovRandomField()

for i in range(1, 6):
    model.add(gum.LabelizedVariable(f"A{i}", f"A{i}", 2))

edges = [
    ("A1", "A2"),
    ("A1", "A3"),
    ("A2", "A3"),
    ("A2", "A4"),
    ("A3", "A5"),
    ("A4", "A5")
]

for a, b in edges:
    model.addFactor([a, b])

gnb.show(model)