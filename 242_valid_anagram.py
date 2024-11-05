from collections import defaultdict


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sorted_s = sorted(s)
        sorted_t = sorted(t)

        return sorted_s == sorted_t


class Solution2:
    def isAnagram(self, s: str, t: str) -> bool:
        count = defaultdict(int)

        for letter in s:
            count[letter] += 1
        for letter in t:
            count[letter] -= 1

        for val in count.values():
            if val != 0:
                return False
