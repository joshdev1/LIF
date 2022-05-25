import unittest
from lif_neuron import LIFNeuron


class TestLifNeuron(unittest.TestCase):

    def setUp(self) -> None:
        self.neuron = LIFNeuron(5e-9, 0.1e-3, 1.5, 15e-3)

    # TODO add mocks to test functions with no returns (neuron.run_neuron())

    def test_get_rate(self):
        self.neuron.run_neuron()
        self.assertEqual(self.neuron.get_rate(), 166)
