 # -*- coding: UTF-8 -*-
from Estruturas import *
import time

class Sudoku:
    matriz = None
    estrutura = None
    
    def __init__(self, matrizTexto):
        self.estrutura = ListaADJ()
        self.matriz = []
        contador = 1
        for i in range(0,9):
            vetor = []
            for j in range(0,9):
                alteravel = False
                if(matrizTexto[i][j] == "."):
                    alteravel = True
                v = Vertice(str(i) + "-" + str(j), alteravel)
                self.estrutura.vertices[str(contador)] = v
                contador += 1
                if(not alteravel):
                    v.cor = matrizTexto[i][j]
                self.estrutura.adiciona(v)
                vetor.append(v)
            self.matriz.append(vetor)
            
            
                
        for i in range(0,9):
            for j in range(0,9):
                k = None
                l = None
                if(i < 3 and j < 3):
                    k = 3
                    l = 3
                elif(i < 6 and j < 3):
                    k = 6
                    l = 3
                elif(i < 9 and j < 3):
                    k = 9
                    l = 3
                elif(i < 3 and j < 6):
                    k = 3
                    l = 6
                elif(i < 6 and j < 6):
                    k = 6
                    l = 6
                elif(i < 9 and j < 6):
                    k = 9
                    l = 6
                elif(i < 3 and j < 9):
                    k = 3
                    l = 9
                elif(i < 6 and j < 9):
                    k = 6
                    l = 9
                elif(i < 9 and j < 9):
                    k = 9
                    l = 9
                else:
                    print ("Sudoku errado")
                self.ligaBloco(i, j, k, l)
                    
        for i in range(0, 9):
            for j in range(0, 9):
                for k in range(j + 1, 9):
                    self.estrutura.liga(self.matriz[i][j], self.matriz[i][k])
                for l in range(i + 1, 9):
                    self.estrutura.liga(self.matriz[i][j], self.matriz[l][j])
        
        for i in range(0, 9):
            for j in range(0, 9):
                self.possiveisCores(self.matriz[i][j])
                self.estrutura.adiciona(self.matriz[i][j])
                
    
    def colorir (self, contador):
        if(contador == 82):
            return True
        vertice = self.estrutura.vertices[str(contador)]
        self.possiveisCores(vertice)
        if(vertice.alteravel == False):
            if(self.colorir(contador+1)):
                return True
            else:
                return False
        for i in range(1,10):
            if(i in vertice.cores):
                if(vertice.cor == None):
                    vertice.cor = i
                if(self.colorir(contador+1)):
                    vertice.alteravel = False
                    return True
                vertice.cor = None
                vertice.alteravel = True
                
        return False

    def possiveisCores(self, v):
        if(v.alteravel == False):
            v.cores = None
            return
        cores = [1,2,3,4,5,6,7,8,9]
        for vizinho in v.vizinhos:
            if(vizinho.cor != None):
                aux = int(vizinho.cor)
                if (aux in cores):
                    cores.remove(aux)
        # if(len(cores) == 1):
        #     v.cor = cores[0]
        #     v.alteravel = False
        #     return
        # else:
        v.cores = cores



    def ligaBloco(self, i, j, k, l):
        for o in range(k-3, k):
            for p in range(l-3, l):
                self.estrutura.liga(self.matriz[i][j], self.matriz[o][p])

    def contaVizinhos(self):
        saida = ""
        for i in range(0,9):
            for j in range(0,9):
                if(not self.matriz[i][j].alteravel):
                    saida += str(self.matriz[i][j].cor) + " "
                else:
                    saida += "." + " "
            saida += "\n"
        print(saida)
    
    def contaCores(self):
        saida = ""
        for i in range(0,9):
            for j in range(0,9):
                    saida += str(self.matriz[i][j].cores) + " "
            saida += "\n"
        print(saida)

  
    def terminou(self):
        for i in range(9):
            for j in range(9):
                if (self.matriz[i][j].saturacao != -1):
                    return False
        return True

    def getMaiorSaturacao(self):
        maior = self.matriz[0][0]
        for i in range(1,81):
            vertice = self.estrutura.vertices[str(i)]
            if (vertice.saturacao > maior.saturacao):
                maior = vertice
        return maior

    def atualizaSaturacao(self):
        for i in range(1,82):
            vertice = self.estrutura.vertices[str(i)]
            if(vertice.cor != None):
                vertice.saturacao = -1;
            else:
                self.possiveisCores(vertice)
                if(vertice.cores != None):
                    vertice.saturacao = 9 - len(vertice.cores)           

    def atualizaSaturacaoVertice(self, vertice):
        if(vertice.cor != None):
            vertice.saturacao = -1;
        else:
            self.possiveisCores(vertice)
            if(vertice.cores != None):
                vertice.saturacao = 20 - len(vertice.cores)

    def colorir2(self):     
        self.atualizaSaturacao()        
        if self.colorirAux() == False:
            return False;
        else:
            return True;
    

    
    def colorirAux(self):
        if (self.terminou() == True):
            return True
        vertice = self.getMaiorSaturacao()
        self.possiveisCores(vertice)
        if(vertice.cor != None):
            vertice.saturacao = -1
            if(self.colorirAux()):
                return True
            else:
                return False
        
        for i in range(1,10):
            if(i in vertice.cores):
                if(vertice.cor == None):
                    vertice.cor = i
                    vertice.saturacao = -1
                    self.incrementaSaturacao(vertice)
                if(self.colorirAux()):
                    vertice.alteravel = False
                    return True
                vertice.cor = None
                vertice.alteravel = True
                self.decrementaSaturacao(vertice)
                self.possiveisCores(vertice)
                self.atualizaSaturacaoVertice(vertice)
                
        return False
    
    def decrementaSaturacao(self, vertice):
        for i in range(len(vertice.vizinhos)):
            if(vertice.vizinhos[i].saturacao != -1):
                vertice.vizinhos[i].saturacao -= 1
    
    def incrementaSaturacao(self, vertice):
        for i in range(len(vertice.vizinhos)):
            if(vertice.vizinhos[i].saturacao != -1):
                vertice.vizinhos[i].saturacao += 1
        
    def contaSaturacao(self):
        saida = ""
        for i in range(0,9):
            for j in range(0,9):
                saida += str(self.matriz[i][j].saturacao) + " "
            saida += "\n"
        print(saida)
