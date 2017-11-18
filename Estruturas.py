# -*- coding: UTF-8 -*-

class Vertice:
    nome = None
    cor = None
    cores = None
    vizinhos = None
    alteravel = None
    saturacao = None
    
    def __init__(self, nome, alteravel = True):
        self.nome = nome
        self.alteravel = alteravel
        self.vizinhos = []

class MatrizAdj:
    matriz = None
    
    def __init__(self):
        self.matriz = []
    

class ListaADJ:
    vertices = None
    
    def __init__(self):
        self.vertices = {}
        
        
    def adiciona(self, v):
        self.vertices[v.nome] = v
        
    def liga(self, v1, v2):
        if(v1.nome == v2.nome):
            return
        if(v1.nome in self.vertices and v2.nome in self.vertices):
            if((not(v2 in self.vertices[v1.nome].vizinhos))):
                self.vertices[v1.nome].vizinhos.append(v2)
                self.vertices[v2.nome].vizinhos.append(v1)
    
    def getVizinhos(self, v):
        return self.vertices[v.nome].vizinhos
        
        
    def imprimeLista(self):
        saida = ""
        for v in self.vertices:
            saida += "Vizinhos do vertice " + v + ": \n"
            for viz in self.vertices[v].vizinhos:
                saida += "->" + viz
            saida += "\n"
            
        return saida
