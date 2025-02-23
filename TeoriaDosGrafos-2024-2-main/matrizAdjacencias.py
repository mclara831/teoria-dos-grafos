# Representacao computacional de um grafo por meio de matriz de adjacencias:
class MatrizAdjacencias:
    # inicializa o grafo:    
    def __init__(self, numVertices):
        self.numVertices = numVertices
        self.numArestas = 0   
        self.graus = [0] * self.numVertices
        self.matriz = [[0]* self.numVertices for i in range(self.numVertices)]

    # retorna a ordem do grafo:
    def ordem(self):
        return self.numVertices
    
    # retorna o tamanho do grafo:
    def tamanho(self):
        return self.numArestas

    # adiciona uma aresta (v1, v2) no grafo:
    # peso eh um parametro opcional
    def addAresta(self, v1, v2, peso = 1):
        if self.matriz[v1][v2] == 0:
            self.numArestas += 1
            self.graus[v1] += 1
        self.matriz[v1][v2] = peso

    # retorna True se existe uma aresta (v1,v2) no grafo:
    def possuiAresta(self, v1, v2):
        return self.matriz[v1][v2] != 0

    # retorna uma lista de tuplas (vertice, peso)
    # com os vizinhos de v:
    def vizinhos(self, v):
        vz = []
        for j in range(self.numVertices):
            if self.matriz[v][j] != 0:
                vz.append((j, self.matriz[v][j]))
        return vz
    
    # retorna o grau (saida) de um vertice:
    def grau(self, v):
        return self.graus[v]

    # printa o grafo no formato de matriz de adjacencias:
    def printGrafo(self):
        for i in range(self.numVertices):
            for j in range(self.numVertices):
                print(self.matriz[i][j], end=" ")
            print()