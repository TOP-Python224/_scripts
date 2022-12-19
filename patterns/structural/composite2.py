from typing import Union


Neurons = Union['Neuron', 'NeuronLayer']


class Neuron:
    def __init__(self, name: str):
        self.name = name
        self.inputs: list[Neuron] = []
        self.outputs: list[Neuron] = []

    def connect_to(self, other: 'Neuron'):
        self.outputs += [other]
        other.inputs += [self]

    def __iter__(self):
        yield self

    def __repr__(self):
        return self.name


class NeuronLayer(list):
    def __init__(self, name: str, count: int = 2):
        super().__init__()
        self.name = name
        for i in range(1, count+1):
            self.append(Neuron(f'нейрон {i} слоя {self.name}'))

    def connect_to(self, other: Neurons):
        for neuron_out in self:
            for neuron_in in other:
                neuron_out.connect_to(neuron_in)

    def __repr__(self):
        return '\n'.join(repr(n) for n in self)



n1 = Neuron('нейрон 1')
n2 = Neuron('нейрон 2')
n2.connect_to(n1)

nl1 = NeuronLayer('1', 3)
nl2 = NeuronLayer('2', 2)
print(nl1, nl2, sep='\n\n', end='\n\n')

nl2.connect_to(nl1)
nl1.connect_to(n1)

for n in nl1:
    print(n.name)
    print('\tвходы:', n.inputs)
    print('\tвыходы:', n.outputs)
print()

for n in nl2:
    print(n.name)
    print('\tвходы:', n.inputs)
    print('\tвыходы:', n.outputs)

