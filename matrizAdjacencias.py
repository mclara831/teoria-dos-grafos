# Representacao computacional de um grafo por meio de matriz de adjacencias:
class MatrizAdjacencias:
    # Inicializa o grafo: construtor da classe
    # self: próprio objeto para fazer a chamada, é igual ao this em Java, é padrão em tdo método
    def __init__(self, numVertices):
        self.numVertices = numVertices
        self.numArestas = 0
        self.matriz = [[0] * self.numVertices for i in range(self.numVertices)]
        self.graus = [0] * self.numVertices
        # self.matriz = []      
        # for i in range(self.numVertices):
        #   self.matriz.append([0] * self.numVertices)      

    # retorna a ordem do grafo:
    def ordem(self):
        return self.numVertices
    
    # retorna o tamanho do grafo:
    def tamanho(self):
        return self.numArestas

    # adiciona uma aresta (v1, v2) no grafo:
    # peso é um parametro opcional
    def addAresta(self, v1, v2, peso = 1):
        if self.matriz[v1][v2] == 0:
            self.numArestas += 1
        self.matriz[v1][v2] = peso
    
    # retorna True se existe uma aresta (v1,v2) no grafo:
    def possuiAresta(self, v1, v2):
        return self.matriz[v1][v2] != 0

    # retorna uma lista com os vizinhos de v:
    def vizinhos(self, v):
        vz = []
        for j in range(self.numVertices):
            if self.matriz[v][j] != 0:
                vz.append((j, self.matriz[v][j]))
        return vz
    
    # retorna o grau (saida) de um vertice: o grau é a qtd de vizinhos que o vertice tem.
    def grau(self, v):
        return self.graus[v]
        #return len(self.vizinhos(v))

    # printa o grafo no formato de matriz de adjacencias:
    def printGrafo(self):
        # for i in range(self.numVertices):
          #  for j in range(self.numVertices):
           #     print(self.matriz[i][j], end=" ")
            # print()
        print("    1 2 3 4 5 6 ")
        for i in range(self.numVertices):
            print(f"{i + 1}  ", end=" ")
            for j in range(self.numVertices):
                print(self.matriz[i][j], end=" ")
            print()