from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k=2) -> List[int]:
        mapa_num_freq = {}
        top_k_frequent = []

        # criando o mapa
        for num in nums:
            if num not in mapa_num_freq:
                mapa_num_freq[str(num)] = 1

            else:
                mapa_num_freq[num] += 1

        # ordenando as chaves baseado nos valores
        for _ in range(k):

            max_freq = -1
            num_maior_freq = None

            for num, freq in mapa_num_freq.items():
                if freq > max_freq:
                    max_freq = freq
                    num_maior_freq = num

            top_k_frequent.append(num_maior_freq)
            del mapa_num_freq[num_maior_freq]

        return top_k_frequent


nums = [1, 1, 1, 1, 2, 2, 3]
solution = Solution()
print(solution.topKFrequent(nums))
