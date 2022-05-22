from lif_neuron import lif_neuron, graph_output

spikes, rate, v, time = lif_neuron(1.7e-9, 0.1e-3, 1.5, 15e-3)
graph_output(time, v)
