# Funciona mas TimeLimit porque a complexidade total ficou em O(nˆ3)
class SolutionOld:
    def isPalindrome(self, s: str) -> bool:
        list_str = list(s)
        og_str = list(s)
        reverse_str = []

        while list_str:
            reverse_str.append(list_str.pop())

        return og_str == reverse_str

    def longestPalindrome(self, s: str) -> str:
        longest_palindrome = ""

        for i in range(len(s)):
            for j in range(i, len(s) + 1):
                current_substr = s[i:j]
                if self.isPalindrome(current_substr) and len(current_substr) > len(
                    longest_palindrome
                ):
                    longest_palindrome = current_substr

        return longest_palindrome


# Solucao mais eficaz
class Solution:
    def longestPalindrome(self, s: str) -> str:
        longest_palindrome = ""

        for position in range(len(s)):
            ## odd
            left_pointer, right_pointer = position, position

            def pointers_position_in_bounds():
                return left_pointer >= 0 and right_pointer < len(s)

            while pointers_position_in_bounds() and s[left_pointer] == s[right_pointer]:
                curr_substring = s[left_pointer : right_pointer + 1]
                if len(curr_substring) > len(longest_palindrome):
                    longest_palindrome = curr_substring

                left_pointer -= 1
                right_pointer += 1

            # even
            left_pointer, right_pointer = position, position + 1

            def pointers_position_in_bounds():
                return left_pointer >= 0 and right_pointer < len(s)

            while pointers_position_in_bounds() and s[left_pointer] == s[right_pointer]:
                curr_substring = s[left_pointer : right_pointer + 1]

                if len(curr_substring) > len(longest_palindrome):
                    longest_palindrome = curr_substring

                left_pointer -= 1
                right_pointer += 1

        return longest_palindrome


t = "abb"  # output: "bb"
z = "bb"
x = "a"
y = "ac"

solution = Solution()
print(solution.longestPalindrome(t))
