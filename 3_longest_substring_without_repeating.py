 
## FUNCIONA mas tem a complexidade fudida vai estourar em strings muito longas
class SolutionOld:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maior_substring = []  

        for i in range(len(s)):
            substring_atual = [ ]

            for j in range(i, len(s)):
                char_atual = s[j]

                if char_atual not in substring_atual:
                     substring_atual.append(char_atual)
                else: 
                    substring_atual = [char_atual]    
 
                if len(substring_atual) > len(maior_substring):         
                    maior_substring = substring_atual
            
        return len(maior_substring)  


## Usando Sliding window  
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
       pass

 


s = "abcabcbb"
solution = Solution()
print(solution.lengthOfLongestSubstring(s))