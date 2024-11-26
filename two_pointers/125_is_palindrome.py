class Solution:
    def isPalindrome(self, s: str) -> bool:
        clean_s =  ''.join(char for char in s if char.isalnum()).lower()
        right_pointer = len(clean_s)-1
 
        for left_pointer in range( len(clean_s)): 
            if (clean_s[left_pointer] != clean_s[right_pointer]):
                return False
            right_pointer -= 1

        return True         


mock = "A man, a plan, a canal: Panama"
mock1 = "race a car"
solution = Solution()

print(solution.isPalindrome(mock1))
