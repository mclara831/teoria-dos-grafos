import listaAdjacencias
import matrizAdjacencias

# retorna a densidade do grafo:
def densidade(grafo):
    return grafo.numArestas / (grafo.numVertices * (grafo.numVertices - 1))

# retorna o complemento do grafo:
def complemento(grafo):
    comp = listaAdjacencias.ListaAdjacencias(grafo.numVertices)
    for i in range(grafo.numVertices):
        for j in range(grafo.numVertices):
            if i != j and not grafo.possuiAresta(i, j):
                comp.addAresta(i, j)
    return comp

# retorna True se o grafo eh completo:
def completo(grafo):
    for i in range(grafo.numVertices):
        for j in range(grafo.numVertices):
            if i != j and not grafo.possuiAresta(i, j):
                return False
    return True

# retorna True se o grafo eh regular:
def regular(grafo):
    grauVertice = grafo.grau(0)
    for i in range(grafo.numVertices):
        if grafo.grau(i) != grauVertice:
            return False
    return True


# retorna um subgrafo induzido pelo conjunto
# de vertices:
def subgrafo(grafo, vertices):
    sg = listaAdjacencias.ListaAdjacencias(len(vertices))
    
    for i in range(len(vertices)):
        for j in range(len(vertices)):
            if i != j and grafo.possuiAresta(vertices[i], vertices[j]):
                sg.addAresta(i, j)
    return sg