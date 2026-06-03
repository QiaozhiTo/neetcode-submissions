class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l, maxF = 0, 0
        window = {}
        res = 0

        for r in range(len(s)):
            window[s[r]] = 1 + window.get(s[r], 0)
            maxF = max(maxF, window[s[r]])

            if (r - l + 1) - maxF > k:
                window[s[l]] -= 1
                l += 1
            res = max(res, r - l + 1)
        return res