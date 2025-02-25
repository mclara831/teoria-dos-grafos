import listaAdjacencias
import matrizAdjacencias
import heapq
import time

#calcula de 1 pra todos
def dijkstra(g, s, e): #passa como parametro o grafo lido, o vertice de origem e o de destino
    inicio = time.time() #começa o timer
    dist = [float('inf')] * g.numVertices #inicializa todas as distâncias com infinito (inf(infinity) é para isso)
    dist[s] = 0 #o vertice de origem sempre começa com o valor 0 na sua distancia
    prev = [None] * g.numVertices #prev é igual ao predecessor, todos são inicializados com none que é referente a nada
    filadeprioridade = [(0, s)] #fila de prioridade 
    
    while filadeprioridade:
        #"u" é o nó e "d" é a menor distância
        (d, u) = heapq.heappop(filadeprioridade)
        if u == e: #se o nó "u" for igual ao "e" destino saimos do loop
            break
        if d > dist[u]: #ingora "u", uma vez que já encontramos o melhor caminho
            continue
        for(v, peso) in g.vizinhos(u): #para cada vizinho do nó a ser explorado, calculamos uma nova distância (distância alternativa)
            novadist = dist[u] + peso
            if novadist < dist[v]: #se a distância nova for melhor que a que já temos para o vizinho x, entramos na condição
                dist[v] = novadist 
                prev[v] = u #indicamos que o melhor caminho para o vizinho x é passar por u
                heapq.heappush(filadeprioridade, (novadist, v)) #insere na fila de prioridade
                
        caminhominimo = []
        u = e #inicia no vertice de destino e voltamos de tras pra frente até a origem, moldando o caminho
        while prev[u] is not None:
            caminhominimo.insert(0, u)
            u = prev[u]
        if caminhominimo:
            caminhominimo.insert(0, s) #se o caminho não estver vazio, colocamos s no inicio
        
        fim = time.time() #termina o timer
        tempo_execucao = fim - inicio #faz o calculo do tempo de execucao
        
    return caminhominimo, dist[e], tempo_execucao
    
def bellmanford (g, s, e): 
    inicio = time.time() #começa o timer
    numVertices = g.numVertices
    dist = [float('inf')] * g.numVertices #inicializa todas as distâncias com infinito (inf(infinity) é para isso)
    dist[s] = 0 #o vertice de origem sempre começa com o valor 0 na sua distancia
    prev = [None] * g.numVertices #prev é igual ao predecessor, todos são inicializados com none que é referente a nada
        
    for _ in range(numVertices - 1):
        for u in range(numVertices):
            for (v, peso) in g.vizinhos(u): #percorre todas as arestas do nó "u"
                if dist[u] + peso < dist[v]:
                    dist[v] = dist[u] + peso
                    prev[v] = u
                    
    #verificador de ciclo negativo no grafo escolhido    
    for u in range(numVertices):
        for(v, peso) in g.vizinhos(u):
            if dist[u] + peso < dist[v]:
                print("Ciclo negativo encontrado")
                return None, None, None
        
    caminhominimo = []
    u = e #inicia no vertice de destino e voltamos de tras pra frente até a origem, moldando o caminho
    while prev[u] is not None:
        caminhominimo.insert(0, u)
        u = prev[u]
    if caminhominimo:
        caminhominimo.insert(0, s) #se o caminho não estver vazio, colocamos s no inicio
        
    fim = time.time() #termina o timer
    tempo_execucao = fim - inicio #faz o calculo do tempo de execucao
           
    return caminhominimo, dist[e], tempo_execucao