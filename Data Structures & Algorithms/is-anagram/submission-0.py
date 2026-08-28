class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        counts = {}
        for a, b in zip(s, t):
            counts[a] = counts.get(a, 0) + 1
            counts[b] = counts.get(b, 0) - 1
        return all(v == 0 for v in counts.values())
