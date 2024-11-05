from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams_group = {}

        for word in strs:
            sorted_word = "".join(sorted(word))

            if sorted_word not in anagrams_group:
                anagrams_group[sorted_word] = []
            anagrams_group[sorted_word].append(word)

        return list(anagrams_group.values())


mock = ["eat", "tea", "tan", "ate", "nat", "bat"]
#  [["bat"],["nat","tan"],["ate","eat","tea"]]

solution = Solution()
solution.groupAnagrams(mock)
