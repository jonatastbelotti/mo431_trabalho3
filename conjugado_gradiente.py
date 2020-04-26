from otimizador import OtimizadorScipyMinimize


class ConjugadoGradiente(OtimizadorScipyMinimize):

    NOME_METODO = "Conjugado gradiente"
    SCIPY_METODO = "CG"

    def __init__(self):
        super().__init__()



# CÓDIGO PRINCIPAL
if __name__ == "__main__":
    conjugado = ConjugadoGradiente()

    conjugado.otimizar([4, 4], passar_gradiente=False)
    conjugado.imprimir_resultado()
    print("")
    print("")

    conjugado = ConjugadoGradiente()
    conjugado.otimizar([4, 4], passar_gradiente=True)
    conjugado.imprimir_resultado()