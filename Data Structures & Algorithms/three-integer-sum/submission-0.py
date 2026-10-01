class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()  # Sorts in-place
        output = []
        
        for i in range(len(nums)):
            # Skip duplicate starting elements
            if i > 0 and nums[i] == nums[i - 1]:
                continue
                
            left = i + 1
            right = len(nums) - 1
            
            # Inner two-pointer loop
            while left < right:
                temp_total = nums[i] + nums[left] + nums[right]
                
                if temp_total == 0:
                    output.append([nums[i], nums[left], nums[right]])
                    left += 1
                    right -= 1
                    
                    # Skip duplicate inner elements
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1
                        
                elif temp_total < 0:
                    left += 1  # Need a larger sum
                else:
                    right -= 1  # Need a smaller sum
                    
        return output


                

