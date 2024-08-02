import numpy
from typing import List

matrix = [
    [1, 2, 3, 4, 2,4],
    [5, 6, 7, 8],
    [9, 9, 9, 9]
]

def traverse_matrix_by_rows(matrix: List[List[int]]):
    
    for i_row in range(0, len(matrix)):
        for j_col in range(0, len(matrix[i_row])):
            print(matrix[i_row][j_col])


def traverse_matrix_by_cols_vanilla(matrix: List[List[int]]):
    
    for i_col in range(0, len(matrix[0])):
        for j_row in range(0, len(matrix)):
            if i_col < len(matrix[j_row]):
                print(matrix[j_row][i_col])
            
def traverse_matrix_by_cols_transposed(matrix: List[List[int]]):
    t_matrix = numpy.transpose(matrix)

    print(t_matrix)

def print_matrix(grid: List[List[int]]):
    for row in grid:
        print(row)

#traverse_matrix_by_rows(matrix)
traverse_matrix_by_cols_transposed(matrix)