import listaAdjacencias
import matrizAdjacencias
import heapq

def dijkstra(g, s, e): #passa como parametro o grafo lido, o vertice de origem e o de destino
    dist = [float('inf')] * g.numVertices #inicializa todas as distâncias com infinito (inf(infinity) é para isso)
    dist[s] = 0 #o vertice de origem sempre começa com o valor 0 na sua distancia
    prev = [None] * g.numVertices #prev é igual ao predecessor, todos são inicializados com none que é referente a nada
    pq = [(0, s)] #fila de prioridade 
    
    while pq:
        #"u" é o nó e "d" é a menor distância
        (d, u) = heapq.heappop(pq)
        if u == e: #se o nó "u" for igual ao "e" destino saimos do loop
            break
        if d > dist[u]: #ingora "u", uma vez que já encontramos o melhor caminho
            continue
        for(v, peso) in g.vizinhos(u): #para cada vizinho do nó a ser explorado, calculamos uma nova distância (distância alternativa)
            novadist = dist[u] + peso
            if novadist < dist[v]: #se a distância nova for melhor que a que já temos para o vizinho x, entramos na condição
                dist[v] = novadist 
                prev[v] = u #indicamos que o melhor caminho para o vizinho x é passar por u
                heapq.heappush(pq, (novadist, v)) #insere na fila de prioridade
                
        caminhominimo = []
        u = e #inicia no vertice de destino e voltamos de tras pra frente até a origem, moldando o caminho
        while prev[u] is not None:
            caminhominimo.insert(0, u)
            u = prev[u]
        if caminhominimo:
            caminhominimo.insert(0, s) #se o caminho não estver vazio, colocamos s no inicio
            
        return caminhominimo, dist[e]