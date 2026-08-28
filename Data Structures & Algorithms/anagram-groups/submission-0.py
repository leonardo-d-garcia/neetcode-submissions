from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list) #mapping charCount to list of Anagrams

        for s in strs:
            count = [0] * 26

            for c in s:
                count[ord(c)-ord("a")] += 1 # where the index is the letter and the value is the frequency
            res[tuple(count)].append(s)
        return list(res.values())
        