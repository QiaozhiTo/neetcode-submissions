class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t: return ""
        countT = {}
        for i in range(len(t)):
            countT[t[i]] = 1 + countT.get(t[i], 0)

        have, need = 0, len(countT)
        res, resLen = [-1, -1], float("inf")

        window = {}
        l = 0

        for r in range(len(s)):
            c = s[r]
            window[c] = 1 + window.get(c, 0)
            if c in countT and countT[c] == window[c]:
                have += 1

            while have == need:
                #因为要更新res， 只有当发现比resLem更小的length（r-l+1）才更新
                # 而不是每次更新 resLen = min(resLen, r -l + 1), res = [l, r]
                if (r - l + 1) < resLen:
                    resLen = r - l + 1
                    res = [l, r]
                window[s[l]] -= 1
                
                if s[l] in countT and countT[s[l]] - 1 == window[s[l]]:
                    have -= 1
                l += 1
        l, r = res
        return "" if resLen == float("inf") else s[l : r + 1]

