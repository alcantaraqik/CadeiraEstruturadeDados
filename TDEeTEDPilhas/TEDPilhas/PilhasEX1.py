import numpy as np


class pilhas:
    def __init__(self, capacidade):
        self.capacidade = capacidade

        self.topo = -1
        self.valores = np.empty(self.capacidade, dtype=int)

    def ver_topo(self):
        return self.topo

