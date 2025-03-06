from contextlib import nullcontext

import matrizAdjacencias
import busca
import sys
import time
import logging
import math
import threading

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

def predecesores(inicio, fim, caminho_busca):
    lista = []
    s = inicio
    t = fim
    u = fim

    lista.append(t)
    while not u == s:
        for (x, y) in caminho_busca:
            if x == u:
                u = y
                lista.append(y)
                break
    return lista

def conversao_dos_vertices(lista_vertices, num_colunas):
    saida = []
    while lista_vertices: #convertendo de índice de vértice para posição no labirinto
        pos = lista_vertices.pop()
        l = pos/num_colunas
        c = pos % num_colunas
        saida.insert(0,(math.floor(l),c))
    saida.reverse()
    return saida

def imprimir_caminho(caminho, nomeArquivo, tempoExecucao):
    print('\nCaminho do ' + nomeArquivo + ': ', end="")
    for x in range(len(caminho) - 1):
        print(str(caminho[x]) + " -> ", end="")
    print(str(caminho[len(caminho) - 1]))
    print(f"Tempo: {tempoExecucao: .3f} s\n")

def le_labirinto(nomeArquivo):
    # abrindo arquivos e declarando variáveis da função
    arquivo = open(nomeArquivo)
    logging.basicConfig(filename='Labirintos.log', level=logging.DEBUG,
                        format='%(asctime)s - %(levelname)s - %(message)s')
    
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
    
    inicio = time.time()

    # caminho_busca = busca.dfs(grafo_labirinto,S)
    # alg_busca = "DFS (recursivo)"

    # caminho_busca = busca.dfsIterativo(grafo_labirinto, S)
    # alg_busca = "DFS (iterativo)"

    caminho_busca = busca.bfs(grafo_labirinto, S)
    alg_busca = "BFS"
    
    fim = time.time()
    tempo_execucao = fim - inicio
    logging.info(f'{nomeArquivo}\n'
                 f'Tempo de execução: {tempo_execucao:.2f} segundos\n'
                 f'Busca usada: {alg_busca}\n')

    lista = predecesores(S, E, caminho_busca)

    saida = conversao_dos_vertices(lista, num_colunas)
    
    imprimir_caminho(saida, nomeArquivo, tempo_execucao)

    return grafo_labirinto

if __name__ == "__main__":
    
    if len(sys.argv) != 6:
        print("Numero invalido de parametros! Argumentos esperados: main.py labirinto1.txt labirinto2.txt labirinto3.txt labirinto4.txt labirinto5.txt")
        sys.exit(1)

    # Ler todos os 5 arquivos de labirintos e acha a solução
    for i in range(1, 6):
        var = sys.argv[i]
        grafo = le_labirinto(sys.argv[i])
