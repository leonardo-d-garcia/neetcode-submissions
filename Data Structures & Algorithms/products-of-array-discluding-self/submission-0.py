class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        #loop through, multiply nums[i] in every spot except its current spot
        suffix = 1
        prefix = 1
        out_arr = [1] * len(nums)
        for i in range(len(nums)):
            out_arr[i] *= prefix
            prefix*= nums[i]
        for i in range(len(nums)-1, -1, -1):
            out_arr[i] *= suffix
            suffix *= nums[i]
        return out_arr
        