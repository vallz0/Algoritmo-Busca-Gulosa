import Grafo as gf
import numpy as np

class vetorOrdenado:

    def __init__(self, capacidade):
        self.capacidade = capacidade
        self.ultima_posicao = -1
        self.valores = np.empty(self.capacidade,dtype=object)

    def insere(self,vertice):
        if self.ultima_posicao == self.capacidade - 1:
            print("capacidade maxima atingida")
            return
    
        posicao = 0
        for i in range(self.ultima_posicao + 1):
            posicao = i 
            if self.valores[i].distancia_objetivo > vertice.distancia_objetivo:
                break
            if i == self.ultima_posicao:
                posicao = i + 1 
        x = self.ultima_posicao
        while x >= posicao:
            self.valores[x+1] = self.valores[x]
            x -= 1
        self.valores[posicao] = vertice
        self.ultima_posicao += 1

    def imprime(self):
        if self.ultima_posicao == -1:
            print("O vetor está vazio")
        else:
            for i in range(self.ultima_posicao + 1):
                print(i, ' - ', self.valores[i].rotulo, ' - ', self.valores[i].distancia_objetivo)

grafo = gf.Grafo()

