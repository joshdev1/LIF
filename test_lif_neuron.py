import unittest
from lif_neuron import lif_neuron


class TestLifNeuron(unittest.TestCase):
    def test_lif_neuron(self):
        _, rate = lif_neuron(5e-9, 0.1e-3, 1.5, 15e-3)
        self.assertEqual(rate, 166)
