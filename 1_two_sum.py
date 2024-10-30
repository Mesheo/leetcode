from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        result = []

        for i in range(len(nums)):
            if len(result) < 2:
                for j in range(len(nums)):
                    if j != i and nums[i] + nums[j] == target:
                        result.append(i)
                        result.append(j)
                        break
            else:
                break
        return result
