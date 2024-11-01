from typing import List


## Melhorei pacas
class SolutionReviewed:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return i, j


# BETTER SOLUTION - O(nˆ2)
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        position_map = {}

        # building our hashmap
        for i in range(n):
            position_map[nums[i]] = i

        # finding the complement position
        for i in range(n):
            complement = target - nums[i]
            if complement in position_map and position_map[complement] != i:
                return [i, position_map[complement]]


# BETTER BETTER SOLUTION - O(n)
# Need to study this
class SolutionMax:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numMap = {}
        n = len(nums)

        for i in range(n):
            complement = target - nums[i]
            if complement in numMap:
                return [numMap[complement], i]
            numMap[nums[i]] = i

        return []


nums = [2, 7, 11, 15]
target = 9

nums2 = [3, 2, 4]
target2 = 6

nums3 = [3, 3]
target3 = 6


solution = Solution()
print(solution.twoSum(nums3, target3))
