from typing import List


# Solucao que Primeiro me veio a cabeça
class Solution:
    def find_median(self, array: List[int]) -> int:
        is_length_pair = len(array) % 2 == 0
        middle_position = len(array) // 2
        median = array[middle_position]

        if is_length_pair:
            middle_position = int(len(array) / 2)
            center_values = array[middle_position] + array[middle_position - 1]

            median = center_values / 2

        return median

    def sort_array(self, array: List[int]) -> List[int]:
        sorted_array = []

        while array:
            smallest_number = array[0]

            for current_number in array:
                if current_number < smallest_number:
                    smallest_number = current_number

            sorted_array.append(smallest_number)
            array.remove(smallest_number)

        return sorted_array

    def merge_arrays(self, nums1: List[int], nums2: List[int]) -> List[int]:
        result_array = nums1

        for number in nums2:
            result_array.append(number)

        return result_array

    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        merged_array = []

        # 1. Une os dois arrays
        merged_array = self.merge_arrays(nums1, nums2)

        # 2. Organiza o array
        sorted_array = self.sort_array(merged_array)

        # 3. retorna a mediana
        return self.find_median(sorted_array)


mock_input = [1, 3]
mock_input2 = [2]

mock_input3 = [1, 5, 4, 2, 3]

solution = Solution()
print(solution.findMedianSortedArrays(mock_input, mock_input2))
