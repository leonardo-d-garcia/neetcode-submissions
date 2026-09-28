class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        still_increasing = True
        num_set = set(nums)
        if len(num_set) == 0:
            return 0
        temp_count = 1
        count = 0
        for num in num_set:
            if num-1 in num_set:
                continue
            else:
                while num+1 in num_set:
                    temp_count += 1
                    num = num+1
                count = max(temp_count, count)
            temp_count = 1
        return count


                    
        