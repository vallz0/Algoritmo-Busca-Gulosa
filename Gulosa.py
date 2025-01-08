from VetorOrdenado import vetorOrdenado
from Grafo import Grafo

class Gulosa:
    def __init__(self, objetivo):
        self.objetivo = objetivo
        self.encontrado = False

    def buscar(self, atual):
        print("--------")
        print('Atual: {}'.format(atual.rotulo))
        atual.visitado = True

        if atual == self.objetivo:
            self.encontrado = True
            print("Objetivo encontrado!")
        else:
            vetor_ordenado = vetorOrdenado(len(atual.adjacentes))
            for adjacente in atual.adjacentes:
                if not adjacente.vertice.visitado:
                    vetor_ordenado.insere(adjacente.vertice)

            vetor_ordenado.imprime()

            if not self.encontrado and vetor_ordenado.valores[0] is not None:
                self.buscar(vetor_ordenado.valores[0])

grafo = Grafo()
busca_gulosa = Gulosa(grafo.bucharest)
busca_gulosa.buscar(grafo.arad)
