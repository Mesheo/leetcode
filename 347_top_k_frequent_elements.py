from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency_map = {}

        for num in nums:
            if num in frequency_map:
                frequency_map[num] += 1
            else:
                frequency_map[num] = 1

        most_frequent = 0
        for number in frequency_map:
            
                
        pass



nums = [1,1,1,2,2,3]
solution = Solution()   
print(solution.topKFrequent(nums))