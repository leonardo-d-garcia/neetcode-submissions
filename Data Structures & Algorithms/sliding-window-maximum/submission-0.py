from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        dq = deque()
        result = []
        for i in range(len(nums)):
            #Remove element if it's out of range
            if dq and dq[0] <= i-k:
                dq.popleft()
            #Remove smaller elements from the back, they can't be a max
            while dq and nums[dq[-1]] < nums[i]:
                dq.pop()
            #Add a new element on the right
            dq.append(i)
            #If a full window forms, the front is the max, so add to result
            if i >= k -1:
                result.append(nums[dq[0]])
        return result
        



