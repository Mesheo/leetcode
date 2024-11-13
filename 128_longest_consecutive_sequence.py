from typing import List


class SolutionBrute:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 1

        longest_consecutive_elements_sequence_size = 0
        sem_repeticao = list(set(nums))
        print(f"aqui a lista sem repeticao {sem_repeticao} ")

        for i in range(len(sem_repeticao)):
            consecutive_number = sem_repeticao[i] + 1
            previous_number = sem_repeticao[i] - 1

            if consecutive_number in sem_repeticao or previous_number in sem_repeticao:
                longest_consecutive_elements_sequence_size += 1

        return longest_consecutive_elements_sequence_size
    

"""
    tentamos achar o inicio de cada sequencia, que eh dado pela condicao de nao existir um 
    membro a esquerda. Com o inicio dado vamos expandindo e atualizando a maior sequencia
    No fim retornamos a maior sequencia 
     
"""   
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        no_repetition = set(nums)
        longest = 0
 
        for number in nums:
            curr_longest = 1 
            if number-1 not in no_repetition:
                while number+curr_longest in no_repetition:
                    curr_longest +=1 
             
            longest = max(longest, curr_longest)

        return longest



mock = [100, 4, 200, 1, 3, 2]  # sair 4
mock2 = [0, 3, 7, 2, 5, 8, 4, 6, 0, 1]  #   sair 9
mock3 = [1] # eh pra sair 1
mock4 = [0, 0]  # eh pra sair 1

solution = Solution()
print(solution.longestConsecutive(mock2))
