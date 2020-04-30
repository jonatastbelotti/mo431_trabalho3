from otimizador import OtimizadorScipyMinimize


class NelderMead(OtimizadorScipyMinimize):

    NOME_METODO = "Nelder-Mead"
    SCIPY_METODO = "Nelder-Mead"

    def __init__(self):
        super().__init__()
        



# CÓDIGO PRINCIPAL
if __name__ == "__main__":
    conjugado = NelderMead()

    conjugado.otimizar([4, 4], passar_gradiente=False, options={'initial_simplex': [[-4,-4], [-4,1], [4,-1]]})
    conjugado.imprimir_resultado()
