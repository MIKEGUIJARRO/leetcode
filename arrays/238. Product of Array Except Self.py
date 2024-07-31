from typing import List

metadata = {
    'title': '238. Product of Array Except Self',
    'link': 'https://leetcode.com/problems/product-of-array-except-self/description/',
    'difficulty': 'easy',
    'tags': ['array', 'prefix_sum']
}

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix_sum_arr_lr = self.build_prefix_sum_arr(nums)
        prefix_sum_arr_rl = self.build_prefix_sum_arr(nums[::-1])
        prefix_sum_arr_rl = prefix_sum_arr_rl[::-1]

        answer_arr = []

        for i in range(len(nums)):
            if i == 0:
                answer_arr.append(prefix_sum_arr_rl[i + 1]) 
                continue
            if i == len(nums) - 1:
                answer_arr.append(prefix_sum_arr_lr[i - 1])
                continue
            
            answer_arr.append(prefix_sum_arr_lr[i - 1] * prefix_sum_arr_rl[i + 1])

        return answer_arr

    def build_prefix_sum_arr(self, nums: List[int]) -> List[int]:
        prefix_sum_arr = []
        multiplier = 1

        for num in nums:
            multiplier = multiplier * num
            prefix_sum_arr.append(multiplier)
        
        return prefix_sum_arr
