from typing import List


# BRUTE FORCE
class SolutionBruteForce:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # creating hashmap
        nums_dict = {}
        for i in range(len(nums)):
            print(nums[i])
            if nums[i] in nums_dict:
                nums_dict[nums[i]] += 1
            else:
                nums_dict[nums[i]] = 1

        print(nums_dict)
        return 2 in nums_dict.values()


# Hashtable not so efficient
class SolutionHashtable:
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums_dict = {}
        for i in range(len(nums)):
            if nums[i] in nums_dict:
                nums_dict[nums[i]] += 1
            else:
                nums_dict[nums[i]] = 1

        repeated = False
        for value in nums_dict.values():
            if value >= 2:
                repeated = True

        return repeated


# Aqui ja foi foda
class SolutionBoaJa:
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums_dict = {}
        for i in range(len(nums)):
            if nums[i] in nums_dict:
                return True
            nums_dict[nums[i]] = i

        return False


# Parece mais performatico mas vc precisa criar o set inteiro
class SolutionALmost:
    def containsDuplicate(self, nums: List[int]) -> bool:
        if len(set(nums)) == len(nums):
            return False
        return True


# Com Set fica mais performatico
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        seen = set()
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False


nums = [2, 14, 18, 22, 22]
solution = Solution()
print(solution.containsDuplicate(nums))
