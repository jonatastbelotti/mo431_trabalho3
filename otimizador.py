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
        self.calculos_funcao = 0
        self.chamadas_gradiente = 0
        self.num_iteracoes = None


    def func_himmelblau(self, ponto):
        x = ponto[0]
        y = ponto[1]
        resp = ((x**2) + y - 11) ** 2
        resp += (x + (y ** 2) - 7) ** 2

        return resp


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
        print("Valor função: %.16f" % self.valor_final)
        print("Número chamadas função: %d" % self.calculos_funcao)
        print("Número chamadas gradiente: %d" % self.chamadas_gradiente)
        print("Tempo execução: %.16f segundos" % self.tempo_total)