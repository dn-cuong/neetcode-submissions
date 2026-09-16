class Solution:
    def maximumProfit(self, profit: List[int], weight: List[int], capacity: int) -> int:

        N, M = len(profit), capacity

        dp = [[0] * (M + 1) for _ in range(N + 1)]

        for i in range(1, N + 1):
            for j in range(M + 1):

                dp[i][j] = dp[i-1][j]

                if weight[i-1] <= j:
                    dp[i][j] = max(
                        dp[i][j],
                        dp[i-1][j-weight[i-1]] + profit[i-1]
                    )

        return dp[N][M]