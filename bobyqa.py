import numpy as np
import pybobyqa

from otimizador import Otimizador


class BOBYQA(Otimizador):

    NOME_METODO = "BOBYQA"

    def __init__(self):
        super().__init__()


    def otimizar(self, p_inicial):
        self.ponto_inicial = np.array(p_inicial)

        self.iniciar_tempo()
        sol = pybobyqa.solve(self.func_himmelblau, self.ponto_inicial)
        self.finalizar_tempo()

        self.ponto_final = sol.x
        self.valor_final = sol.f
        self.chamadas_func_obj = sol.nf



# CÓDIGO PRINCIPAL
if __name__ == "__main__":
    bobyqa = BOBYQA()

    bobyqa.otimizar([4, 4])
    bobyqa.imprimir_resultado()
