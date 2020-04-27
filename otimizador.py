import numpy as np
from scipy.optimize import minimize
import time


class Otimizador():

    NOME_METODO = "Sem nome"

    def __init__(self):
        self.ponto_inicial = None
        self.ponto_final = None
        self.valor_final = None
        self.tempo_inicial = None
        self.tempo_final = None
        self.tempo_total = None
        self.chamadas_func_obj = None
        self.chamadas_gradiente = None
        self.num_iteracoes = None


    def func_himmelblau(self, ponto, contar=True):
        x = ponto[0]
        y = ponto[1]
        resp = ((x**2) + y - 11) ** 2
        resp += (x + (y ** 2) - 7) ** 2

        return resp
    
    def gradiente_himmelblau(self, ponto, *args, contar=True):
        x = ponto[0]
        y = ponto[1]

        grad_x = 2 * (2 * x * (x**2 + y - 11) + x + y**2 - 7)

        grad_y = 2 * (x**2 + 2*y*(x + y**2 - 7) + y - 11)

        return np.array([grad_x, grad_y])


    def otimizar(self):
        pass


    def iniciar_tempo(self):
        self.tempo_inicial = time.time()


    def finalizar_tempo(self):
        self.tempo_final = time.time()
        self.tempo_total = self.tempo_final - self.tempo_inicial


    def imprimir_resultado(self):
        print("Método: %s" % self.NOME_METODO)
        print("Ponto de mínimo: x=%.16f y=%.16f" % (self.ponto_final[0], self.ponto_final[1]))
        print("Valor função: %.32f" % self.valor_final)

        for obj in [
            {'texto': "Número chamadas função:", 'formato': "%d", 'valor': self.chamadas_func_obj},
            {'texto': "Número chamadas gradiente:", 'formato': "%d", 'valor': self.chamadas_gradiente},
            {'texto': "Número de iterações:", 'formato': "%d", 'valor': self.num_iteracoes}
        ]:
            if obj['valor']:
                print((obj['texto'] + " " + obj['formato']) % (obj['valor']))
            else:
                print(obj['texto'])

        print("Tempo execução: %.16f segundos" % self.tempo_total)



class OtimizadorScipyMinimize(Otimizador):

    SCIPY_METODO = ""

    def __init__(self):
        super().__init__()
    

    def otimizar(self, p_inicial, passar_gradiente=False):
        self.ponto_inicial = p_inicial
        self.NOME_METODO = self.NOME_METODO + " PASSANDO GRADIENTE" if passar_gradiente else self.NOME_METODO + " NÃO PASSANDO GRADIENTE"
        self.func_gradiente = self.gradiente_himmelblau if passar_gradiente else None

        self.iniciar_tempo()
        resp = minimize(self.func_himmelblau, self.ponto_inicial, method=self.SCIPY_METODO, jac=self.func_gradiente)
        self.finalizar_tempo()

        self.ponto_final = resp.x
        self.valor_final = self.func_himmelblau(self.ponto_final)
        self.chamadas_func_obj = resp.nfev if hasattr(resp, "nfev") else None
        self.chamadas_gradiente = resp.njev if hasattr(resp, "njev") else None
        self.num_iteracoes = resp.nit if hasattr(resp, "nit") else None

