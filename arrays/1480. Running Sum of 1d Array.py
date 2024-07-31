from typing import List

metadata = {
    'title': '1480. Running Sum of 1d Array',
    'link': 'https://leetcode.com/problems/running-sum-of-1d-array/description/',
    'difficulty': 'easy',
    'tags': ['array', 'prefix_sum']
}

class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        counter = 0
        arr = []
        for num in nums:
            counter = counter + num
            arr.append(counter)
        
        return arr