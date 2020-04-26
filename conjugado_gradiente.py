import numbers as np
from scipy.optimize import minimize

from otimizador import Otimizador


class ConjugadoGradiente(Otimizador):

    NOME_METODO = "Conjugado gradiente passando gradiente"

    def __init__(self):
        super().__init__()


    def otimizar(self, p_inicial):
        self.ponto_inicial = p_inicial

        resp = self.exec_minimize()

        self.ponto_final = resp.x
        self.valor_final = self.func_himmelblau(self.ponto_final, contar=False)
        self.chamadas_func_obj = resp.nfev
        self.chamadas_gradiente = resp.njev
        self.num_iteracoes = resp.nit
    

    def exec_minimize(self):
        self.iniciar_tempo()
        resp = minimize(self.func_himmelblau, self.ponto_inicial, method="CG", jac=self.gradiente_himmelblau)
        self.finalizar_tempo()

        return resp


class ConjugadoGradienteSemGradiente(ConjugadoGradiente):

    NOME_METODO = "Conjugado gradiente não passando gradiente"

    def __init__(self):
        super().__init__()


    def exec_minimize(self):
        self.iniciar_tempo()
        resp = minimize(self.func_himmelblau, self.ponto_inicial, method="CG")
        self.finalizar_tempo()

        return resp
        



# CÓDIGO PRINCIPAL
if __name__ == "__main__":
    conjugado = ConjugadoGradiente()

    conjugado.otimizar([4, 4])
    conjugado.imprimir_resultado()
    print("")
    print("")

    conjugado = ConjugadoGradienteSemGradiente()
    conjugado.otimizar([4, 4])
    conjugado.imprimir_resultado()