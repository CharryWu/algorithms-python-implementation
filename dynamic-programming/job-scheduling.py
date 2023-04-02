from typing import List
class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        # Like schedule meeting, sort by end time increasing
        startTime, endTime, profit = zip(*sorted(zip(startTime, endTime, profit), key = lambda x: x[1]))
        n = len(startTime)
        dp = [0] * n
        dp[0] = profit[0] # dp[i] represents max profit up until ith job (sorted by end time)

        # compute dp[i]: we could either include ith job or not include it
        # correspondingly, the profit will be max of (include ith job profit + prev compatible job max profit, i-1th job profit)
        for i in range(1, n):
            withI = profit[i]
            # find the max profit if we decide to include ith job: ith job profit + prev compatible job max profit
            for j in range(i-1, -1, -1):
                if endTime[j] <= startTime[i]:
                    withI += dp[j]
                    break
            dp[i] = max(withI, dp[i-1])
        return dp[i]
