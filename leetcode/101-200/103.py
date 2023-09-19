class Solution:

    def coinChange(self, coins: list[int], amount: int) -> int:
        # 边界情况处理
        if amount == 0: return 0
        coins.sort()
        if coins[0] > amount: return -1

        dp = [0] + [float('inf')] * amount  # dp[i]: 硬币能组成金额为i所需最小个数
        for coin in coins:  # 每次新拿一种硬币
            for i in range(coin, amount + 1):  # 从大于等于这个硬币的面值开始，这个硬币才可能开始起作用
                dp[i] = min(dp[i], dp[i - coin] + 1)

        return dp[-1] if dp[-1] != float('inf') else -1
