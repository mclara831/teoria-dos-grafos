from contextlib import nullcontext

import matrizAdjacencias
import caminhoMinimo
import sys
import time
import logging
import math

def leitura(nomeArquivo):
    arquivo = open(nomeArquivo)

    str = arquivo.readline()
    str = str.split(" ")
    numVertices = int(str[0])
    numArestas = int(str[1])

    #grafo = listaAdjacencias.ListaAdjacencias(numVertices)
    grafo = matrizAdjacencias.MatrizAdjacencias(numVertices)

    for i in range(numArestas):
        str = arquivo.readline()
        str = str.split(" ")
        origem = int(str[0])
        destino = int(str[1])
        peso = int(str[2])
        grafo.addAresta(origem, destino, peso)

    return grafo

def le_grafo(nomeArquivo, origem, destino):
    grafo = leitura(nomeArquivo)
    
    print("\nExecutando o algoritmo de Dijkstra...\n")
    caminho_dijkstra, custo_dijkstra, tempo_dijkstra = caminhoMinimo.dijkstra(grafo, origem, destino)
    print("Algoritmo de Dijkstra finalizado\n")
    
    print("----------------------------------------------------------")

    print("\nExecutando o algoritmo de Bellman-Ford...\n")
    caminho_bellmanford, custo_bellmanford, tempo_bellmanford = caminhoMinimo.bellmanford(grafo, origem, destino)
    print("Algoritmo de Bellman-Ford finalizado\n")
    
    print("----------------------------------------------------------")

    print("\nExecutando o algoritmo de Floyd-Warshall...\n")
    caminho_floydwarshall, custo_floydwarshall, tempo_floydwarshall = caminhoMinimo.floydwarshall(grafo, origem, destino)
    print("Algoritmo de Floyd-Warshall finalizado\n")
    print("----------------------------------------------------------\n\n")
    print("Os três algoritmos de caminho minimo foram realizados para o grafo escolhido. :)")
    
    logging.basicConfig(filename='Grafos.log', level=logging.DEBUG,
                        format='%(asctime)s - %(levelname)s - %(message)s')
    
    logging.info(f'{nomeArquivo}\n'
                f"Algoritmo de Dijkstra:\n"
                f"Caminho mínimo: {caminho_dijkstra}\n"
                f"Custo: {custo_dijkstra}\n"
                f"Tempo de Execução: {tempo_dijkstra: .4f} segundos\n")
    
    logging.info(f'{nomeArquivo}\n'
                f"Algoritmo de Bellman-Ford:\n"
                f"Caminho mínimo: {caminho_bellmanford}\n"
                f"Custo: {custo_bellmanford}\n"
                f"Tempo de Execução: {tempo_bellmanford: .4f} segundos\n")

    logging.info(f'{nomeArquivo}\n'
                f"Algoritmo de Floyd-Warshall:\n"
                f"Caminho mínimo: {caminho_floydwarshall}\n"
                f"Custo: {custo_floydwarshall}\n"
                f"Tempo de Execução: {tempo_floydwarshall: .4f} segundos\n")

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Numero invalido de parametros! Argumentos esperados: main2.py grafo.txt vértice_origem vértice_destino")
        sys.exit(1)

    grafo = sys.argv[1]
    varOrigem = int(sys.argv[2])
    varDestino = int(sys.argv[3])
    grafo = le_grafo(grafo, varOrigem, varDestino)