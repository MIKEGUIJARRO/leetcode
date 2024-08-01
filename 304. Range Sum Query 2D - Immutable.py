from typing import List

metadata = {
    'title': '304. Range Sum Query 2D - Immutable',
    'link': 'https://leetcode.com/problems/range-sum-query-2d-immutable/description/',
    'difficulty': 'medium',
    'tags': ['array', 'prefix_sum', 'design', 'matrix']
}


class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        prefix_sum_matrix = []

        for rows in matrix:
            prefix_sum_row = self.build_prefix_sum_arr(rows)
            prefix_sum_matrix.append(prefix_sum_row)

        self.prefix_sum_matrix = prefix_sum_matrix


    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        counter = 0
        for i in range(row1, row2 + 1, 1):
            right_sum = self.prefix_sum_matrix[i][col2 + 1]
            left_sum = self.prefix_sum_matrix[i][col1]
            counter = counter + right_sum - left_sum

        return counter

    def build_prefix_sum_arr(self, nums:List[int]) -> List[int]:
        prefix_sum_arr = [0]
        counter = 0
        
        for num in nums:
            counter = counter + num
            prefix_sum_arr.append(counter)
        
        return prefix_sum_arr

# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)