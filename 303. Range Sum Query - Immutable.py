from typing import List


metadata = {
    'title': '303. Range Sum Query - Immutable',
    'link': 'https://leetcode.com/problems/range-sum-query-immutable/description/',
    'difficulty': 'easy',
    'tags': ['array', 'prefix_sum', 'design']
}


class NumArray:
    prefix_sum_nums = []
    def __init__(self, nums: List[int]):
        counter = 0
        prefix_sum_nums = [0]
        for num in nums:
            counter = counter + num
            prefix_sum_nums.append(counter)

        self.prefix_sum_nums = prefix_sum_nums      

    def sumRange(self, left: int, right: int) -> int:
        prefix_sum_num_left = self.prefix_sum_nums[left]
        prefix_sum_num_right = self.prefix_sum_nums[right + 1]

        return prefix_sum_num_right - prefix_sum_num_left


        
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)