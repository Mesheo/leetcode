

from typing import List

 # TODO: ajeitar isso 
 # estou satisfeito ja com a solucao que eu fiz
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 1: 
            return  1

        longest_consecutive_elements_sequence_size = 0
        sem_repeticao = list(set(nums))

        for i in range(len(sem_repeticao)):  
            consecutive_number = sem_repeticao[i] + 1 
            previous_number = sem_repeticao[i] -1  

            if consecutive_number in sem_repeticao or previous_number in sem_repeticao:  
                longest_consecutive_elements_sequence_size += 1
 
        return longest_consecutive_elements_sequence_size

 

mock  = [100,4,200,1,3,2] #  
mock2 = [0,3,7,2,5,8,4,6,0,1] # nao funcionou | deve sair 9
mock3 = [1]

solution = Solution( )       
print(solution.longestConsecutive(mock3)) 