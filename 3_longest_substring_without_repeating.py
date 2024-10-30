## FUNCIONA mas tem a complexidade fudida vai estourar em strings muito longas
class SolutionOld:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maior_substring = []

        for i in range(len(s)):
            substring_atual = []

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
        maxLength = 0
        charSet = set()
        left_pointer = 0

        for right_pointer in range(len(s)):
            current_char = s[right_pointer]
            current_length = right_pointer - left_pointer + 1

            if current_char not in charSet:
                charSet.add(current_char)

                maxLength = max(maxLength, current_length)
            else:
                while current_char in charSet:
                    charSet.remove(s[left_pointer])
                    left_pointer += 1
                charSet.add(current_char)

        return maxLength


s = "abcabcbb"
solution = Solution()
print(solution.lengthOfLongestSubstring(s))
