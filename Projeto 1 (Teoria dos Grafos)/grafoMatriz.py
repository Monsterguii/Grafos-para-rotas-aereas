# -*- coding: utf-8 -*-
"""
Created on Mon Feb 13 13:59:10 2023

@author: icalc
"""
import networkx as nx 
import matplotlib.pyplot as plt 

class Grafo:
    TAM_MAX_DEFAULT = 100 # qtde de vértices máxima default
    # construtor da classe grafo
    def __init__(self, n=TAM_MAX_DEFAULT):
        self.n = n # número de vértices
        self.m = 0 # número de arestas
        self.visual = []
        self.vertices = {}
        # matriz de adjacência
        self.adj = [[0 for i in range(n)] for j in range(n)]

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
    def insereA(self, v, w):
        if self.adj[v][w] == 0:
            temp = [v, w]
            self.visual.append(temp)
            self.adj[v][w] = 1
            self.m+=1 # atualiza qtd arestas
    
    # remove uma aresta v->w do Grafo
    def removeA(self, v, w):
        # testa se temos a aresta
        if self.adj[v][w] == 1:
            self.adj[v][w] = 0
            self.m-=1; # atualiza qtd arestas

    def get_arestas(self):
        arestas = []
        for i in range(self.n):
            for j in range(self.n):
                if self.adj[i][j] == 1:
                    arestas.append((i, j))
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
        
    def visualize(self): 
        G = nx.Graph() 
        G.add_edges_from(self.visual) 
        nx.draw_networkx(G) 
        plt.show()