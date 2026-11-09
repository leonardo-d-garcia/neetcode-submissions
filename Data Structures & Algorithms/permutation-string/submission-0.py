from collections import Counter

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        need = Counter(s1)
        window = Counter()
        left = 0
        for right, c in enumerate(s2):
            if c not in need:
                window.clear()
                left = right + 1
                continue
            window[c] += 1
            while window[c] > need[c]:
                window[s2[left]] -= 1
                left += 1
            if right - left + 1 == len(s1):
                return True
        return False
         


