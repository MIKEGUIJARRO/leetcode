from typing import List

metadata = {
    'title': '724. Find Pivot Index',
    'link': 'https://leetcode.com/problems/find-pivot-index/description/',
    'difficulty': 'easy',
    'tags': ['array', 'prefix_sum']
}

class Solution:

    def pivotIndex(self, nums: List[int]) -> int:
        prefix_sum_arr_l_r = self.build_prefix_sum_arr(nums)
        prefix_sum_arr_r_l = self.build_prefix_sum_arr(nums[::-1])
        prefix_sum_arr_r_l = prefix_sum_arr_r_l[::-1]

        if len(nums) == 1:
            return 0

        for i in range(len(nums)):

            # Case 1 - Left edge
            if i == 0:
                if prefix_sum_arr_r_l[i + 1] == 0:
                    return i
                continue

            # Case 2 - Right edge
            if i == len(nums) - 1:
                if prefix_sum_arr_l_r[i - 1] == 0:
                    return i
                continue
            
            left_sum = prefix_sum_arr_l_r[i - 1]
            right_sum = prefix_sum_arr_r_l[i + 1]

            # Case 3 - Right == Left
            if left_sum == right_sum:
                return i         

        # Case 4 - Not found
        return - 1

    def build_prefix_sum_arr(self, nums: List[int]) -> List[int]:
        prefix_sum_arr = []
        counter = 0

        for num in nums:
            counter = counter + num
            prefix_sum_arr.append(counter)
        
        return prefix_sum_arr

