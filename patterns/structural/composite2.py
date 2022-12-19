
class Neuron:
    def __init__(self, name: str):
        self.name = name
        self.inputs: list[Neuron] = []
        self.outputs: list[Neuron] = []

    def connect_to(self, other: 'Neuron'):
        self.outputs += [other]
        other.inputs += [self]

    def __repr__(self):
        return self.name


n1 = Neuron('нейрон 1')
n2 = Neuron('нейрон 2')
n2.connect_to(n1)

print(n1.name)
print(n1.inputs)
print(n1.outputs, end='\n\n')

print(n2.name)
print(n2.inputs)
print(n2.outputs, end='\n\n')

