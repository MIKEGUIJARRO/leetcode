from typing import List

metadata = {
    'title': '3096. Minimum Levels to Gain More Points',
    'link': 'https://leetcode.com/problems/minimum-levels-to-gain-more-points/',
    'difficulty': 'medium',
    'tags': ['array', 'prefix_sum']
}


class Solution:
    def minimumLevels(self, possible: List[int]) -> int:
        possible_prefix_sum_lr = self.build_prefix_sum_arr(possible)
        possible_prefix_sum_rl = self.build_prefix_sum_arr(possible[::-1])[::-1]

        min_levels = None

        for i in range(0, len(possible) - 1):
            alice_points = possible_prefix_sum_lr[i]
            bob_points = possible_prefix_sum_rl[i+1]

            if alice_points > bob_points: 
                return i + 1
        
        return -1



    def build_prefix_sum_arr(self, nums: List[int]) -> List[int]:
        prefix_sum_arr = []
        counter = 0

        for num in nums:
            point = None
            if num == 1:
                point = 1
            elif num == 0:
                point = -1
            
            counter = counter + point 
            prefix_sum_arr.append(counter)
        
        return prefix_sum_arr