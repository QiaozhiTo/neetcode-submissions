class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        window = set()
        l, r = 0, 0
        resLen = 0
        while r < len(s):
            while s[r] in window:
                window.remove(s[l])
                l += 1
            window.add(s[r])
            resLen = max(resLen, r-l+1)
            r += 1
        return resLen
