class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        count_s = defaultdict(int)
        count_t = defaultdict(int)
        for i in s:
            count_s[i] += 1
        for j in t:
            count_t[j] += 1
        return count_t == count_s