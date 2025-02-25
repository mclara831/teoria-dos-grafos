import listaAdjacencias
import matrizAdjacencias

# versao recursiva do DFS (Aula 07 - slide 7):
def dfs(grafo, u):
    R = []
    visitados = [False] * grafo.ordem()
    prev = [0] * grafo.numVertices
    resultado = []
    prev[u] = u
    dfsRecursivo(grafo, R, u, visitados, prev)
    for u in R:
        resultado.append((u, prev[u]))
    return resultado

def dfsRecursivo(grafo, R, u, visitados, prev):
    visitados[u] = True
    R.append(u)
    for (x, y) in grafo.vizinhos(u):
        if not visitados[x]:
            prev[x] = u
            dfsRecursivo(grafo, R, x, visitados, prev)

# versao iterativa do DFS (Aula 07 - slide 8):
def dfsIterativo(grafo, u):
    prev = [0] * grafo.numVertices
    resultado = []
    R = []
    pilha = []
    visitados = [False] * grafo.ordem()
    pilha.append(u)
    visitados[u] = True
    prev[u] = u
    while len(pilha) > 0:
        s = pilha.pop()
        R.append(s)
        for (x, y) in grafo.vizinhos(s):
            if not visitados[x]:
                pilha.append(x)
                visitados[x] = True
                prev[x] = s
    for u in R:
        resultado.append((u, prev[u]))
    return resultado

# BFS (Aula 07 - slide 15):
def bfs(g, s):
    prev = [0] * g.numVertices
    resultado = []
    r = []
    fila = []
    visitado = [False] * g.numVertices
    fila.append(s)
    visitado[s] = True
    prev[s] = s
    while fila:
        u = fila.pop(0)
        r.append((u))
        for v,p in g.vizinhos(u):
            if not visitado[v]:
                fila.append(v)
                visitado[v] = True
                prev[v] = u
    for u in r:
        resultado.append((u, prev[u]))

    return resultado
