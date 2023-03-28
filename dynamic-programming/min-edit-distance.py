from functools import cache
# https://leetcode.com/problems/edit-distance/
class Solution:
    # using recursion + caching
    def minDistance1(self, word1: str, word2: str) -> int:
        @cache  # this decorator will automatically cache the function result
        def minD(w1, w2):
            if w1 == "":
                return len(w2)
            if w2 == "":
                return len(w1)
            if w1[0] == w2[0]:
                return minD(w1[1:], w2[1:])
            replace = 1 + minD(w1[1:], w2[1:])
            delete = 1 + minD(w1[1:], w2)
            insert = 1 + minD(w1, w2[1:])
            return min(replace, delete, insert)

        return minD(word1, word2)

    # using buttom-up dp
    def minDistance2(self, word1: str, word2: str) -> int:
        n, m = len(word1), len(word2)
        # 1-n and 1-m
        # min edit distance of word starting from (i-tj,j-th)
        dp = [[0] * (m+1) for _ in range(n+1)]

        # initilization
        for i in range(1, n+1):
            dp[i][0] = i
        for j in range(1, m+1):
            dp[0][j] = j

        for i in range(n):
            for j in range(m):
                if word1[i] == word2[j]:
                    dp[i+1][j+1] = dp[i][j]
                else:
                    dp[i+1][j+1] = 1 + min(dp[i][j], dp[i][j+1], dp[i+1][j])
        return dp[-1][-1]
