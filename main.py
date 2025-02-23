import matrizAdjacencias
import listaAdjacencias
import info
import busca
import sys

# cria um grafo a partir de um arquivo:
def leitura(nomeArquivo):
    arquivo = open(nomeArquivo)

    str = arquivo.readline()
    str = str.split(" ")
    numVertices = int(str[0])
    numArestas = int(str[1])

    grafo = listaAdjacencias.ListaAdjacencias(numVertices)
    # grafo = matrizAdjacencias.MatrizAdjacencias(numVertices)

    for i in range(numArestas):
        str = arquivo.readline()
        str = str.split(" ")
        origem = int(str[0])
        destino = int(str[1])
        peso = int(str[2])
        grafo.addAresta(origem, destino, peso)

    return grafo

if __name__ == "__main__":
    grafo = matrizAdjacencias.MatrizAdjacencias(9)

    grafo.addAresta(0, 3)
    grafo.addAresta(0, 6)
    grafo.addAresta(3, 6)
    grafo.addAresta(6, 8)
    grafo.addAresta(0, 5)
    grafo.addAresta(5, 7)
    grafo.addAresta(7, 0)
    grafo.addAresta(7, 1)
    grafo.addAresta(1, 4)
    grafo.addAresta(2, 1)
    grafo.addAresta(2, 4)

    R = busca.dfs(grafo, 0)
    print("Ordem de percusão do DFS Recusivo: " + str(R))
    R = busca.dfsIterativo(grafo, 0)
    print("Ordem de percusão do DFS Iterativo: " + str(R))
    R = busca.bfs(grafo, 0)
    print("Ordem de percusão do BFS: " + str(R))

    grafo = listaAdjacencias.ListaAdjacencias(5)

    grafo.addAresta(0, 1, 2)
    grafo.addAresta(0, 2, 4)
    grafo.addAresta(1, 4, 7)
    grafo.addAresta(3, 2, 6)
    grafo.addAresta(3, 4, 4)
    grafo.addAresta(4, 0, 3)
    grafo.addAresta(4, 3, 1)

    if len(sys.argv) != 2:
        print("Numero invalido de parametros! Argumentos esperados: main.py grafo.txt")
        sys.exit(1)

    # sys.argv[1] contem o nome do arquivo a ser lido
    grafo = leitura(sys.argv[1])

