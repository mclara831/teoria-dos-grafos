from contextlib import nullcontext

import matrizAdjacencias
import listaAdjacencias
import info
import busca
import sys
import time
import logging
import math

# cria um grafo a partir de um arquivo:
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

def le_labirinto(nomeArquivo):
    # abrindo arquivos e declarando variáveis da função
    arquivo = open(nomeArquivo)
    logging.basicConfig(filename='Labirintos.log', level=logging.DEBUG,
                        format='%(asctime)s - %(levelname)s - %(message)s')
    inicio = time.time()
    global S, E

    #lendo as linhas do arquivo e separando como posições em um vetor
    #o texto é um vetor de linhas
    #cada linha é um vetor de caracteres
    linhas = arquivo.readlines()
    num_linhas = len(linhas)
    num_colunas = len(linhas[0].rstrip("\n"))

    #gernado matriz onde cada elemento do labirinto será um vértice
    area_matriz = num_linhas * num_colunas
    grafo_labirinto = matrizAdjacencias.MatrizAdjacencias(area_matriz)

    #estrutura que relaciona cada elemento do labirinto com o grafo criado
    #apenas os vértices que não são paredes terão arestas entre si
    #cada vértice verifica um vizinho nas 4 direções básicas em busca de estabelecer arestas
    for i in range(num_linhas):
        linha_corrente = linhas[i].rstrip("\n")

        for j in range(num_colunas):
            if linha_corrente[j] != '#':
                #pos.corrente será o índice do elemento no grafo
                posicao_corrente = i *  num_colunas + j

                if linha_corrente[j] == 'S':
                    S = posicao_corrente
                if linha_corrente[j] == 'E':
                    E = posicao_corrente

                if j+1 < num_colunas: #verifica o vizinho a direita
                    if linha_corrente[j+1] != '#':
                        grafo_labirinto.addAresta(posicao_corrente,posicao_corrente+1,1)

                if i+1 < num_linhas: #verifica o vizinho abaixo
                    linha_abaixo = linhas[i+1].rstrip("\n")
                    if linha_abaixo[j] != '#':
                        grafo_labirinto.addAresta(posicao_corrente,posicao_corrente+num_colunas,1)

                if j-1 >= 0: #verifica o vizinho a esquerda
                    if linha_corrente[j-1] != '#':
                        grafo_labirinto.addAresta(posicao_corrente,posicao_corrente-1,1)

                if i-1 >= 0: #verifica o vizinho acima
                    linha_acima = linhas[i-1].rstrip("\n")
                    if linha_acima[j] != '#':
                        grafo_labirinto.addAresta(posicao_corrente,posicao_corrente-num_colunas,1)
    print("Iniciando busca...\n")
    #ta comentado pq o que funciona melhor é o dfs iterativo, retornando o caminho exato, sem desvios

    # caminho_busca = busca.dfs(grafo_labirinto,S)
    # alg_busca = "DFS (recursivo)"

    caminho_busca = busca.dfsIterativo(grafo_labirinto,S,E)
    alg_busca = "DFS (iterativo)"

    # caminho_busca = busca.bfs(grafo_labirinto,S)
    # alg_busca = "BFS"

    saida = []
    while caminho_busca: #convertendo de índice de vértice para posição no labirinto
        pos = caminho_busca.pop()
        l = pos/num_colunas
        c = pos % num_colunas
        saida.insert(0,(math.floor(l),c))
    print("Busca finalizada\n")
    print("saída: ", saida)

    fim = time.time()
    tempo_execucao = fim - inicio
    logging.info(f'{nomeArquivo}\n'
                 f'tempo de execução: {tempo_execucao:.2f} segundos\n'
                 f'busca usada: {alg_busca}\n')

    return grafo_labirinto

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Numero invalido de parametros! Argumentos esperados: main.py grafo.txt")
        sys.exit(1)

    var = sys.argv[1]
    grafo = le_labirinto(sys.argv[1])
