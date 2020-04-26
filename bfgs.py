from otimizador import OtimizadorScipyMinimize


class BFGS(OtimizadorScipyMinimize):

    NOME_METODO = "BFGS"
    SCIPY_METODO = "BFGS"

    def __init__(self):
        super().__init__()



# CÓDIGO PRINCIPAL
if __name__ == "__main__":
    bfgs = BFGS()

    bfgs.otimizar([4, 4], passar_gradiente=False)
    bfgs.imprimir_resultado()
    print("")
    print("")

    bfgs = BFGS()
    bfgs.otimizar([4, 4], passar_gradiente=True)
    bfgs.imprimir_resultado()