class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        n1, n = len(strs[0]), len(strs)
        ans = ''
        if n == 1:
            return strs[0]

        for i in range(n1):
            a = strs[0][i]
            for str in strs[1:]:
                if i >= len(str):
                    return ans
                if str[i] != a:
                    return ans
            ans += a
        return ans