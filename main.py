from lif_neuron import LIFNeuron

neuron = LIFNeuron(1.7e-9, 0.1e-3, 1.5, 15e-3)
neuron.run_neuron()
neuron.graph_output()
print(neuron.get_rate())

