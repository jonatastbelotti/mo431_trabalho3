import numbers as np
from scipy.optimize import minimize

from otimizador import Otimizador


class BFGS(Otimizador):

    NOME_METODO = "BFGS passando gradiente"

    def __init__(self):
        super().__init__()


    # Documentação em https://docs.scipy.org/doc/scipy/reference/generated/scipy.optimize.minimize.html
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
        resp = minimize(self.func_himmelblau, self.ponto_inicial, method="BFGS", jac=self.gradiente_himmelblau)
        self.finalizar_tempo()

        return resp


class BFGSSemGradiente(BFGS):

    NOME_METODO = "BFGS não passando gradiente"

    def __init__(self):
        super().__init__()


    def exec_minimize(self):
        self.iniciar_tempo()
        resp = minimize(self.func_himmelblau, self.ponto_inicial, method="BFGS")
        self.finalizar_tempo()

        return resp
        



# CÓDIGO PRINCIPAL
if __name__ == "__main__":
    bfgs = BFGS()

    bfgs.otimizar([4, 4])
    bfgs.imprimir_resultado()
    print("")
    print("")

    bfgs = BFGSSemGradiente()
    bfgs.otimizar([4, 4])
    bfgs.imprimir_resultado()