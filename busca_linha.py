import numpy as np
from scipy.optimize import line_search

from otimizador import Otimizador


class DGBuscaLinha(Otimizador):

    NOME_METODO = "Descida do gradiente com busca em linha"

    def __init__(self):
        super().__init__()


    def otimizar(self, p_inicial):
        # Definindo valores iniciais
        self.ponto_inicial = np.array(p_inicial)
        self.tolerancia = 1000000
        self.num_iteracoes = 0
        self.chamadas_func_obj = 0
        self.chamadas_gradiente = 0
        ponto_anterior = None
        ponto = np.array(p_inicial)

        self.iniciar_tempo()

        while self.tolerancia >= 1e-6:
            self.num_iteracoes += 1
            direcao = - self.gradiente_himmelblau(ponto)

            resp = line_search(f=self.func_himmelblau, myfprime=self.gradiente_himmelblau, xk=ponto, pk=direcao)
            ponto_anterior = ponto
            ponto = ponto + resp[0] * direcao

            self.tolerancia = np.linalg.norm(ponto - ponto_anterior) / np.linalg.norm(ponto_anterior)

            self.chamadas_func_obj += resp[1]
            self.chamadas_gradiente += resp[2]
        
        self.finalizar_tempo()

        self.ponto_final = ponto
        self.valor_final = self.func_himmelblau(self.ponto_final)
        



# CÓDIGO PRINCIPAL
if __name__ == "__main__":
    dg_busca_linha = DGBuscaLinha()

    dg_busca_linha.otimizar([4, 4])
    dg_busca_linha.imprimir_resultado()