class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        num_set = set(numbers)
        index1 = -1001
        index2 = -1001
        for i in range(len(numbers)):
            if target-numbers[i] in num_set:
                if index1 != -1001:
                    index2 = i
                else:
                    index1 = i
        return [index1+1, index2+1]
