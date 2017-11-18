# -*- coding: UTF-8 -*-
import sys
from Sudoku import *

def main():
    nome = sys.argv[1]
    arquivo = open(nome, "r")
    
    linhas = arquivo.read().splitlines()
    
    entrada = []
    for i in range(0, 9):
        vetor = []
        for j in range(0, 9):
            caracter = linhas[i][j]
            vetor.append(caracter)
        entrada.append(vetor)
            
    sudoku = Sudoku(entrada)
    sudoku.contaVizinhos()
    print("")
    t = time.time()
    sudoku.colorir2()
    print(time.time() - t)
    sudoku.contaVizinhos()
    
    # for i in range(0, 9):
    #     vetor = []
    #     for j in range(0, 9):
    #         caracter = linhas[i][j]
    #         vetor.append(caracter)
    #     entrada.append(vetor)
    #         
    # sudoku = Sudoku(entrada)
    # sudoku.contaVizinhos()
    # print("")
    # t = time.time()
    # sudoku.colorir(1)
    # print(time.time() - t)
    # sudoku.contaVizinhos()

main()
