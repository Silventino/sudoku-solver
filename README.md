# sudoku-solver

Programa em Python que resolve sudokus 9x9 baseado no algorítmo de DSatur.

## Instruções de uso

No terminal, rode o Main.py passando como parâmetro um arquivo com o sudoku a ser resolvido:
```bash
python Main.py arquivo
```
Por exemplo, o sudoku dentro do arquivo deve estar no seguinte formato:

.284763..<br>
...839.2.<br>
7..512.8.<br>
..179..4.<br>
3........<br>
..9...1..<br>
.5..8....<br>
..692...5<br>
..2645...<br>

Que será resolvido, resultando em:

9 2 8 4 7 6 3 5 1 <br>
5 1 4 8 3 9 6 2 7 <br>
7 6 3 5 1 2 9 8 4 <br>
2 8 1 7 9 3 5 4 6 <br>
3 4 5 1 6 8 7 9 2 <br>
6 7 9 2 5 4 1 3 8 <br>
4 5 7 3 8 1 2 6 9 <br>
8 3 6 9 2 7 4 1 5 <br>
1 9 2 6 4 5 8 7 3 <br>

O próximo passo é fazer o programa resolver outros tamanhos de sudoku. 

