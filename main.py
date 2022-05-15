from lif_neuron import lif_neuron

spikes, rate = lif_neuron(5e-9, 0.1e-3, 1.5, 15e-3)
print(spikes, rate)

