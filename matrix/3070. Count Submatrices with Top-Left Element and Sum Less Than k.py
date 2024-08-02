from typing import List

metadata = {
    'title': '3070. Count Submatrices with Top-Left Element and Sum Less Than k',
    'link': 'https://leetcode.com/problems/count-submatrices-with-top-left-element-and-sum-less-than-k/',
    'difficulty': 'medium',
    'tags': ['array', 'prefix_sum', 'matrix']
}


class Solution:
    def countSubmatrices(self, grid: List[List[int]], k: int) -> int:
        self.print_matrix(grid)
        print()
        prefix_sum_grid_lr = self.build_prefix_sum_range_matrix_lr(grid)
        self.print_matrix(prefix_sum_grid_lr)
        print()
        prefix_sum_grid_lr_tb = self.build_prefix_sum_range_matrix_tb(prefix_sum_grid_lr)
        self.print_matrix(prefix_sum_grid_lr_tb)
        print()

        counter = 0 
        for row in prefix_sum_grid_lr_tb:
            for cell in row:
                if cell <= k:
                    counter = counter + 1

        return counter

    def build_prefix_sum_range_matrix_lr(self, grid: List[List[int]]) -> List[List[int]]:
        prefix_sum_grid = []
        
        for row in grid:
            prefix_sum_row = []
            counter = 0
            for num in row:
                counter = counter + num
                prefix_sum_row.append(counter)
            prefix_sum_grid.append(prefix_sum_row)

        return prefix_sum_grid
    
    def build_prefix_sum_range_matrix_tb(self, grid: List[List[int]]) -> List[List[int]]:
        prefix_sum_grid = grid.copy()

        for col_i in range(0, len(grid[0])):
            counter = 0
            for row_j in range(0, len(grid)):
                cell = grid[row_j][col_i]
                counter = counter + cell
                prefix_sum_grid[row_j][col_i] = counter
                
        return prefix_sum_grid
    
    def print_matrix(self, grid: List[List[int]]):
        for row in grid:
            print(row)
        
grid = [[7,2,9],[1,5,0],[2,6,6]]
k = 20

solution = Solution()

response = solution.countSubmatrices(grid, k)
print(response)