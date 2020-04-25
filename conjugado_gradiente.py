import numbers as np
from scipy.optimize import minimize

from otimizador import Otimizador


class ConjugadoGradiente(Otimizador):

    NOME_METODO = "Conjugado gradiente"

    def __init__(self):
        super().__init__()


    def otimizar(self, p_inicial):
        self.ponto_inicial = p_inicial

        self.iniciar_tempo()
        resp = minimize(self.func_himmelblau, self.ponto_inicial, method="CG")
        self.finalizar_tempo()

        self.ponto_final = resp.x
        self.valor_final = self.func_himmelblau(self.ponto_final)
        self.calculos_funcao = resp.nfev
        self.num_iteracoes = self.chamadas_gradiente = resp.nit
        



# CÓDIGO PRINCIPAL
if __name__ == "__main__":
    conjugado = ConjugadoGradiente()

    conjugado.otimizar([4, 4])
    conjugado.imprimir_resultado()