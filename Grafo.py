
class Vertice:
    def __init__(self, rotulo,distancia_objetivo):
        self.rotulo = rotulo
        self.visitado = False
        self.distancia_objetivo = distancia_objetivo
        self.adjacentes = []

    def adiciona_adjacente(self, adjacente):
        self.adjacentes.append(adjacente)

    def mostra_adjacentes(self):
        print("\n")
        print(f"Cidade: {self.rotulo}")
        print("")
        print("Adjacentes: ")
        for adj in self.adjacentes:
            print(f"{adj.vertice.rotulo} - Distância: {adj.custo}")


class Adjacente:
    def __init__(self, vertice, custo):
        self.vertice = vertice
        self.custo = custo


class Grafo:
    def __init__(self):
        self.arad = Vertice('Arad', 366)
        self.zerind = Vertice('Zerind', 374)
        self.oradea = Vertice('Oradea', 380)
        self.sibiu = Vertice('Sibiu', 253)
        self.timisoara = Vertice('Timisoara', 329)
        self.lugoj = Vertice('Lugoj', 244)
        self.mehadia = Vertice('Mehadia', 241)
        self.dobreta = Vertice('Dobreta', 242)
        self.craiova = Vertice('Craiova', 160)
        self.rimnicu = Vertice('Rimnicu', 193)
        self.fagaras = Vertice('Fagaras', 178)
        self.pitesti = Vertice('Pitesti', 98)
        self.bucharest = Vertice('Bucharest', 0)
        self.giurgiu = Vertice('Giurgiu', 77)

        self.arad.adiciona_adjacente(Adjacente(self.zerind, 75))
        self.arad.adiciona_adjacente(Adjacente(self.sibiu, 140))
        self.arad.adiciona_adjacente(Adjacente(self.timisoara, 118))

        self.zerind.adiciona_adjacente(Adjacente(self.arad, 75))
        self.zerind.adiciona_adjacente(Adjacente(self.oradea, 71))

        self.oradea.adiciona_adjacente(Adjacente(self.zerind, 71))
        self.oradea.adiciona_adjacente(Adjacente(self.sibiu, 151))

        self.sibiu.adiciona_adjacente(Adjacente(self.arad, 140))
        self.sibiu.adiciona_adjacente(Adjacente(self.oradea, 151))
        self.sibiu.adiciona_adjacente(Adjacente(self.rimnicu, 80))
        self.sibiu.adiciona_adjacente(Adjacente(self.fagaras, 99))

        self.timisoara.adiciona_adjacente(Adjacente(self.arad, 118))
        self.timisoara.adiciona_adjacente(Adjacente(self.lugoj, 111))

        self.lugoj.adiciona_adjacente(Adjacente(self.timisoara, 111))
        self.lugoj.adiciona_adjacente(Adjacente(self.mehadia, 70))

        self.mehadia.adiciona_adjacente(Adjacente(self.lugoj, 70))
        self.mehadia.adiciona_adjacente(Adjacente(self.dobreta, 75))

        self.dobreta.adiciona_adjacente(Adjacente(self.mehadia, 75))
        self.dobreta.adiciona_adjacente(Adjacente(self.craiova, 120))

        self.craiova.adiciona_adjacente(Adjacente(self.dobreta, 120))
        self.craiova.adiciona_adjacente(Adjacente(self.rimnicu, 146))
        self.craiova.adiciona_adjacente(Adjacente(self.pitesti, 138))

        self.rimnicu.adiciona_adjacente(Adjacente(self.sibiu, 80))
        self.rimnicu.adiciona_adjacente(Adjacente(self.craiova, 146))
        self.rimnicu.adiciona_adjacente(Adjacente(self.pitesti, 97))

        self.fagaras.adiciona_adjacente(Adjacente(self.sibiu, 99))
        self.fagaras.adiciona_adjacente(Adjacente(self.bucharest, 211))

        self.pitesti.adiciona_adjacente(Adjacente(self.rimnicu, 97))
        self.pitesti.adiciona_adjacente(Adjacente(self.craiova, 138))
        self.pitesti.adiciona_adjacente(Adjacente(self.bucharest, 101))

        self.bucharest.adiciona_adjacente(Adjacente(self.fagaras, 211))
        self.bucharest.adiciona_adjacente(Adjacente(self.pitesti, 101))
        self.bucharest.adiciona_adjacente(Adjacente(self.giurgiu, 90))

        self.giurgiu.adiciona_adjacente(Adjacente(self.bucharest, 90))

    def mostra_grafo(self):
        for vertice in [
            self.arad, self.zerind, self.oradea, self.sibiu, self.timisoara,
            self.lugoj, self.mehadia, self.dobreta, self.craiova, self.rimnicu,
            self.fagaras, self.pitesti, self.bucharest, self.giurgiu
        ]:
            vertice.mostra_adjacentes()


