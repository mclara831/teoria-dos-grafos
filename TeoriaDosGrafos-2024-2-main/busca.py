from collections import deque
import listaAdjacencias
import matrizAdjacencias


def dfs(grafo, u):
    R = []
    visitados = [False] * grafo.ordem()
    dfsRecursivo(grafo, R, u, visitados)
    return R

# versao recursiva do DFS (Aula 07 - slide 7):
def dfsRecursivo(grafo, R, u, visitados):
    visitados[u] = True
    R.append(u)
    for (x, y) in grafo.vizinhos(u):
        if not visitados[x]:
            dfsRecursivo(grafo, R, x, visitados)

# versao iterativa do DFS (Aula 07 - slide 8):
def dfsIterativo(grafo, u):
    R = []
    pilha = []
    visitados = [False] * grafo.ordem()
    pilha.append(u)
    visitados[u] = True
    while len(pilha) > 0:
        s = pilha.pop()
        R.append(s)
        for (x, y) in grafo.vizinhos(s):
            if not visitados[x]:
                pilha.append(x)
                visitados[x] = True
    return R


# BFS (Aula 07 - slide 15):
def bfs(grafo, u):
    R = []
    fila = []
    visitados = []
    visitados = [False] * grafo.ordem()

    fila.append(u)
    visitados[u] = True

    while len(fila) > 0:
        s = fila.pop(0)
        R.append(s)
        for (x, y) in grafo.vizinhos(s):
            if (visitados[x] == False):
                fila.append(x)
                visitados[x] = True
    return R
