# Teoria dos Grafos - Projeto de Algoritmos de Busca e Caminho Mínimo

Este projeto implementa algoritmos fundamentais de teoria dos grafos para resolver dois tipos principais de problemas: **busca em labirintos** e **encontrar caminhos mínimos em grafos ponderados**.

## 🎯 Funcionalidades Principais

### 1. Resolução de Labirintos (main.py)
- **Busca em Profundidade (DFS)**: Versões recursiva e iterativa
- **Busca em Largura (BFS)**: Para encontrar caminhos em labirintos
- **Conversão de coordenadas**: Transforma índices de vértices em posições do labirinto
- **Logging automático**: Registra tempos de execução e algoritmos utilizados

### 2. Algoritmos de Caminho Mínimo (main2.py)
- **Algoritmo de Dijkstra**: Para grafos com pesos não-negativos
- **Algoritmo de Bellman-Ford**: Para grafos com pesos negativos
- **Algoritmo de Floyd-Warshall**: Para todos os pares de vértices
- **Análise comparativa**: Tempo de execução e custos dos caminhos

## 📋 Conceitos Aplicados

### Representação de Grafos
- **Matriz de Adjacências**: Estrutura principal para representar grafos
- **Conversão Labirinto → Grafo**: Cada célula livre do labirinto vira um vértice

### Algoritmos de Busca
- **DFS (Depth-First Search)**: Busca em profundidade para exploração completa
- **BFS (Breadth-First Search)**: Busca em largura para caminhos mais curtos

### Algoritmos de Caminho Mínimo
- **Dijkstra**: O(V²) - ideal para grafos densos sem pesos negativos
- **Bellman-Ford**: O(VE) - detecta ciclos negativos
- **Floyd-Warshall**: O(V³) - todos os pares de vértices

## 🚀 Como Executar

### Resolução de Labirintos
```bash
python main.py labirinto1.txt labirinto2.txt labirinto3.txt labirinto4.txt labirinto5.txt
```

**Formato do arquivo de labirinto:**
```
#####
#S..#
#.#.#
#..E#
#####
```
- `#`: Parede
- `S`: Start (início)
- `E`: End (fim)
- `.`: Caminho livre

### Análise de Grafos Ponderados
```bash
python main2.py grafo.txt vertice_origem vertice_destino
```

**Formato do arquivo de grafo:**
```
5 7
0 1 4
0 2 2
1 2 1
1 3 5
2 3 8
2 4 10
3 4 2
```
- Primeira linha: `num_vertices num_arestas`
- Demais linhas: `origem destino peso`

## 📊 Saída e Logging

### Console
- **Labirintos**: Caminho encontrado em coordenadas (linha, coluna) e tempo de execução
- **Grafos**: Comparação entre os três algoritmos de caminho mínimo

### Arquivos de Log
- **`Labirintos.log`**: Detalhes da execução dos algoritmos de busca
- **`Grafos.log`**: Resultados completos dos algoritmos de caminho mínimo

## 🔍 Problemas Resolvidos

1. **Navegação em Labirintos**: Encontrar qualquer caminho válido entre início e fim
2. **Otimização de Rotas**: Encontrar o caminho de menor custo entre dois pontos
3. **Análise de Conectividade**: Verificar se existe caminho entre vértices
4. **Comparação de Eficiência**: Avaliar performance de diferentes algoritmos

## 🛠️ Dependências

O projeto utiliza apenas bibliotecas padrão do Python:
- `sys`: Argumentos da linha de comando
- `time`: Medição de tempo de execução
- `logging`: Sistema de logs
- `math`: Operações matemáticas

## 📈 Complexidade dos Algoritmos

| Algoritmo | Complexidade de Tempo | Complexidade de Espaço |
|-----------|----------------------|----------------------|
| DFS | O(V + E) | O(V) |
| BFS | O(V + E) | O(V) |
| Dijkstra | O(V²) | O(V) |
| Bellman-Ford | O(VE) | O(V) |
| Floyd-Warshall | O(V³) | O(V²) |

Este projeto demonstra a aplicação prática de conceitos fundamentais de teoria dos grafos na resolução de problemas reais de navegação e otimização.