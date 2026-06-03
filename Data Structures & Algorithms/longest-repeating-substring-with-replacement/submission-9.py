class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        maxF, l = 0, 0
        res = 0
        count = {}
        for r in range(len(s)):
            count[s[r]] = 1 + count.get(s[r], 0)
            maxF = max(maxF, count[s[r]])

            if (r - l + 1) - maxF > k:
                count[s[l]] -= 1
                l += 1
        return r - l + 1