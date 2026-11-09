from collections import Counter
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        need = Counter(t)
        window = Counter()
        have, required = 0, len(need)
        best_len, best_start = float("inf"), 0

        left = 0
        for right, c in enumerate(s):
            window[c] += 1
            if c in need and window[c] == need[c]:
                have += 1 #letter satisfies
            while have == required: #try to shrink
                if right - left + 1 < best_len:
                    best_len = right - left + 1
                    best_start = left
                d = s[left]
                window[d] -= 1
                if d in need and window[d] < need[d]:
                    have -= 1 #d no longer in the window
                left+=1
        return "" if best_len == float("inf") else s[best_start: best_start + best_len]
        