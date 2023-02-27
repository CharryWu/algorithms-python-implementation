class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        startTime, endTime, profit = zip(*sorted(zip(startTime, endTime, profit), key = lambda x: x[1]))
        n = len(startTime)
        dp = [0] * n
        dp[0] = profit[0]
        
        for i in range(1, n):
            withI = profit[i]
            for j in range(i-1, -1, -1):
                if endTime[j] <= startTime[i]:
                    withI += dp[j]
                    break
            dp[i] = max(withI, dp[i-1])
        return dp[i]
