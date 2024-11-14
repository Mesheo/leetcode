from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = []
        n = len(nums)

        for current_position in range(n): 
            product_for_this_number = 1 
            
            for next_position in range(n): 
                if next_position != current_position:
                    product_for_this_number *= nums[next_position] 

            result.append(product_for_this_number)

        return result  



         
    
mock = [1,2,3,4]   # [24,12,8,6]
mock2 = [0,0] #  [0,0]
mock3 = [-1,1,0,-3,3] # [0,0,9,0,0]
solution = Solution()
print(solution.productExceptSelf(mock3))
