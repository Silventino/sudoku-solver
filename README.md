# sudoku-solver

Python program to solve 9x9 sudoku based in DSatur algorithm.

## Instructions

In the terminal, run Main.py passing the file name with the sudoku to be solved:
```bash
python Main.py file.txt
```
The sudoku must be in a specific format in the file, as this exemple:

```
.284763..
...839.2.
7..512.8.
..179..4.
3........
..9...1..
.5..8....
..692...5
..2645...
```
The program will then write the result as follow:

```
9 2 8 4 7 6 3 5 1
5 1 4 8 3 9 6 2 7
7 6 3 5 1 2 9 8 4
2 8 1 7 9 3 5 4 6
3 4 5 1 6 8 7 9 2
6 7 9 2 5 4 1 3 8
4 5 7 3 8 1 2 6 9
8 3 6 9 2 7 4 1 5
1 9 2 6 4 5 8 7 3
```

Next step is to make this code run to every size of Sudoku.


