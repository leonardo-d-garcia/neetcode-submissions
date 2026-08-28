class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        my_dict = {}
        for i in range(len(nums)):
            if nums[i] not in my_dict:
                my_dict[nums[i]] = 1
            else:
                return True
        return False
        
            
        