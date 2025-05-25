# -*- coding: utf-8 -*-
#Bruno Rabelo Torchio de Oliveira 	RA: 10239373
#Guilherme Dias Ferreira Pereira  	RA: 10417684
import networkx as nx 
import matplotlib.pyplot as plt 

class Grafo:
    TAM_MAX_DEFAULT = 130 # qtde de vértices máxima default
    def __init__(self, n=TAM_MAX_DEFAULT):
        self.n = n
        self.m = 0
        self.visual = []
        self.vertices = {}
        self.adj = [[0 for i in range(n)] for j in range(n)]
        self.pesos = {}  # Novo: dicionário para pesos das arestas

    def add_vertex(self, index, name):
        self.vertices[index] = name
        
    def remove_vertex(self, index):
        if index in self.vertices:
            del self.vertices[index]
            
            for i in range(self.n):
                if self.adj[index][i] == 1:
                    self.adj[index][i] = 0
                    self.m -= 1
                if self.adj[i][index] == 1:
                    self.adj[i][index] = 0
                    self.m -= 1
            
            self.visual = [edge for edge in self.visual if index not in edge]
        else:
            print(f"Vértice {index} não encontrado.")
    # Insere uma aresta no Grafo tal que
    # v é adjacente a w
    def insereA(self, v, w, peso=None):
        if self.adj[v][w] == 0:
            temp = [v, w]
            self.visual.append(temp)
            self.adj[v][w] = 1
            self.m += 1
            if peso is not None:
                self.pesos[(v, w)] = peso  # Novo: armazena o peso
    
    # remove uma aresta v->w do Grafo
    def removeA(self, v, w):
        # testa se temos a aresta
        if self.adj[v][w] == 1:
            self.adj[v][w] = 0
            self.m -= 1
            if (v, w) in self.pesos:
                del self.pesos[(v, w)]  # Novo: remove o peso

    #Usado para resgatar as arestas no grafo atual
    def get_arestas(self):
        arestas = []
        for i in range(self.n):
            for j in range(self.n):
                if self.adj[i][j] == 1:
                    peso = self.pesos.get((i, j))
                    arestas.append((i, j, peso))  # Novo: retorna peso
        return arestas
    # Apresenta o Grafo contendo
    # número de vértices, arestas
    # e a matriz de adjacência obtida	
    def show(self):
        print(f"\n n: {self.n:2d} ", end="")
        print(f"m: {self.m:2d}\n")
        for i in range(self.n):
            for w in range(self.n):
                if self.adj[i][w] == 1:
                    print(f"Adj[{i:2d},{w:2d}] = 1 ", end="") 
                else:
                    print(f"Adj[{i:2d},{w:2d}] = 0 ", end="")
            print("\n")
        print("\nfim da impressao do grafo." )
    
    #Usado para checar a conexão do grafo não direcionado
    def eh_conexo(self):
        visitado = [False] * self.n

        def dfs(v):
            visitado[v] = True
            for w in range(self.n):
                if self.adj[v][w] == 1 and not visitado[w]:
                    dfs(w)

        # Encontra o primeiro vértice válido
        for v in range(self.n):
            if v in self.vertices:
                dfs(v)
                break

        # Verifica se todos os vértices válidos foram visitados
        for v in self.vertices:
            if not visitado[v]:
                return False
        return True

    # Apresenta o Grafo contendo
    # número de vértices, arestas
    # e a matriz de adjacência obtida 
    # Apresentando apenas os valores 0 ou 1	
    def showMin(self):
        print(f"\n n: {self.n:2d} ", end="")
        print(f"m: {self.m:2d}\n")
        for i in range(self.n):
            for w in range(self.n):
                if self.adj[i][w] == 1:
                    print(" 1 ", end="") 
                else:
                    print(" 0 ", end="")
            print("\n")
        print("\nfim da impressao do grafo." )
    
    #Visualização pra ser possivel ver o grafo de algum jeito
    def visualize(self): 
        G = nx.Graph() 
        G.add_edges_from(self.visual) 
        nx.draw_networkx(G) 
        plt.show()
        
    def dijkstra(self, origem, destino):
        dist = {v: float('inf') for v in self.vertices}
        anterior = {v: None for v in self.vertices}
        visitado = {v: False for v in self.vertices}
        dist[origem] = 0

        while True:
            # Seleciona o vértice não visitado com menor distância
            u = None
            menor_dist = float('inf')
            for v in self.vertices:
                if not visitado[v] and dist[v] < menor_dist:
                    menor_dist = dist[v]
                    u = v
            if u is None or u == destino:
                break
            visitado[u] = True
            for v in self.vertices:
                if self.adj[u][v]:
                    peso = self.pesos.get((u, v), 1)
                    if dist[u] + peso < dist[v]:
                        dist[v] = dist[u] + peso
                        anterior[v] = u

        # Reconstrói o caminho
        caminho = []
        atual = destino
        if dist[atual] == float('inf'):
            return None, float('inf')
        while atual is not None:
            caminho.insert(0, atual)
            atual = anterior[atual]
        return caminho, dist[destino]