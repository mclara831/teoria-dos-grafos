import listaAdjacencias
import matrizAdjacencias


# retorna a densidade do grafo:
def densidade(grafo):
    densidade = grafo.tamanho() / (grafo.ordem() * (grafo.ordem() - 1))
    return densidade


# retorna o complemento do grafo:
def complemento(grafo):
    if isinstance(grafo, matrizAdjacencias.MatrizAdjacencias):
        grafoComplementar = matrizAdjacencias.MatrizAdjacencias(grafo.ordem())
    else:
        grafoComplementar = listaAdjacencias.ListaAdjacencias(grafo.ordem())

    for i in range(grafo.ordem()):
        for j in range(grafo.ordem()):
            if not grafo.possuiAresta(i, j) and i != j:
                grafoComplementar.addAresta(i, j)
    return grafoComplementar


# retorna True se o grafo eh completo:
def completo(grafo):
    for i in range(grafo.ordem()):
        for j in range(grafo.ordem()):
            if not grafo.possuiAresta(i, j):
                return False
    return True


# retorna True se o grafo eh regular:
def regular(grafo):
    grau = grafo.grau(0)
    for i in range(grafo.ordem()):
        if grafo.grau(i) != grau:
            return False
    return True


# retorna um subgrafo induzido pelo conjunto de vertices:
def subgrafo(grafo, vertices):
    sg = listaAdjacencias.ListaAdjacencias(len(vertices))

    for i in range(len(vertices)):
        for j in range(len(vertices)):
            if i != j and grafo.possuiAresta(vertices[i], vertices[j]):
                sg.addAresta(i, j)
    return sg
