import listaAdjacencias
import matrizAdjacencias

# versao recursiva do DFS (Aula 07 - slide 7):
def dfs(g, s):
    r = []
    visitado = [False] * g.numVertices
    dfsRecursivo(g,r,visitado,s)
    return r

def dfsRecursivo(g, r, visitado, s):
    visitado[s] = True
    r.append(s)
    for v,p in g.vizinhos(s):
        if not visitado[v]:
            dfsRecursivo(g,r,visitado,v)

# versao iterativa do DFS (Aula 07 - slide 8):
def dfsIterativo(g, s, e):
    r = []
    pilha = []
    visitado = [False] * g.numVertices
    pilha.append(s)
    visitado[s] = True
    while pilha:
        u = pilha.pop()
        r.append(u)
        if u == e:
            return r
        for v,p in g.vizinhos(u):
            if not visitado[v]:
                pilha.append(v)
                visitado[v] = True
    return r

# BFS (Aula 07 - slide 15):
def bfs(g, s):
    r = []
    fila = []
    visitado = [False] * g.numVertices
    fila.append(s)
    visitado[s] = True
    while fila:
        u = fila.pop(0)
        r.append(u)
        for v,p in g.vizinhos(u):
            if not visitado[v]:
                fila.append(v)
                visitado[v] = True
    return r
