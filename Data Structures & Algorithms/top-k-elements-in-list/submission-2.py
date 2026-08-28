from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        my_dict = Counter(nums) #Turning nums into a dictionary
        #need to turn values into the index of a final output
        buckets = [[] for _ in range(len(nums)+1)]
        for key,value in my_dict.items():
            buckets[value].append(key)
        result=[]
        for i in range(len(nums),0,-1):
            if len(result) == k:
                return result
            result.extend(buckets[i])
        return result
            
