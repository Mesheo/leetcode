from typing import List


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)

        complete_array = [number for number in range( n+1)]

        for number in complete_array:
            if number not in nums:
                return number
  


nums = [3, 0, 1]  # 2
nums2 = [0, 1] # 2
nums3 = [1,2] # 
solution = Solution()
print(solution.missingNumber(nums3))
