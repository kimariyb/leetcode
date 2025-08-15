from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        r"""
        你是一个专业的小偷，计划偷窃沿街的房屋。每间房内都藏有一定的现金，
        影响你偷窃的唯一制约因素就是相邻的房屋装有相互连通的防盗系统，
        如果两间相邻的房屋在同一晚上被小偷闯入，系统会自动报警。

        给定一个代表每个房屋存放金额的非负整数数组，计算你 不触动警报装置的情况下 ，
        一夜之内能够偷窃到的最高金额。
        """
        # 边界条件
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums)

        # 动态规划
        dp = [0] * len(nums)
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])

        # 状态转移方程
        # dp[i] = max(dp[i - 1], dp[i - 2] + nums[i])
        # 解释：对于第 i 个房间，可以选择偷或者不偷
        for i in range(2, len(nums)):
            dp[i] = max(dp[i - 1], dp[i - 2] + nums[i])

        return dp[-1]
    
    def numTilings(self, n: int) -> int:
        r"""
        有两种形状的瓷砖：一种是 2 x 1 的多米诺形，另一种是形如 "L" 的托米诺形。
        两种形状都可以旋转。

        给定整数 n ，返回可以平铺 2 x n 的面板的方法的数量。返回对 109 + 7 取模 的值。

        平铺指的是每个正方形都必须有瓷砖覆盖。两个平铺不同，当且仅当面板上有四个方向上的相邻单元中的两个，
        使得恰好有一个平铺有一个瓷砖占据两个正方形。
        """
        # 边界条件
        if n == 0:
            return 1
        if n == 1:
            return 1
        
        MOD = 10**9 + 7

        # 动态规划
        # Domino: f[0] = 1, f[1] = 1
        # Tromino: g[0] = 0, g[1] = 1
        f = [0] * (n + 1)
        g = [0] * (n + 1)

        f[0], f[1] = 1, 1
        g[0], g[1] = 0, 1

        # 动态规划
        # 状态转移方程：f[i] = f[i - 1] + f[i - 2] + 2 * g[i - 2]
        # g[i] = f[i - 1] + g[i - 1]
        for i in range(2, n + 1):
            f[i] = (f[i - 1] + f[i - 2] + 2 * g[i - 2]) % MOD
            g[i] = (f[i - 1] + g[i - 1]) % MOD

        return f[n]

    def uniquePaths(self, m: int, n: int) -> int:
        r"""
        一个机器人位于一个 m x n 网格的左上角 （起始点在下图中标记为 “Start” ）。

        机器人每次只能向下或者向右移动一步。
        机器人试图达到网格的右下角（在下图中标记为 “Finish” ）。

        问总共有多少条不同的路径？
        """
        # 边界条件
        if m == 1 or n == 1:
            return 1

        # 动态规划
        dp = [[1] * n for _ in range(m)]
        # 状态转移方程
        # dp[i][j] = dp[i-1][j] + dp[i][j-1]
        # 对应只能向下或者向右移动一步
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1]

        return dp[m-1][n-1]
    
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        r"""
        给定两个字符串 text1 和 text2，返回这两个字符串的最长 公共子序列 的长度。
        如果不存在 公共子序列 ，返回 0 。

        一个字符串的 子序列 是指这样一个新的字符串：
        它是由原字符串在不改变字符的相对顺序的情况下删除某些字符（也可以不删除任何字符）后组成的新字符串。

        例如，"ace" 是 "abcde" 的子序列，但 "aec" 不是 "abcde" 的子序列。
        两个字符串的 公共子序列 是这两个字符串所共同拥有的子序列。
        """
        # 边界条件
        if not text1 or not text2:
            return 0

        m, n = len(text1), len(text2)

        # 动态规划
        dp = [[0] * (n + 1) for _ in range(m + 1)]

        # 状态转移方程
        # dp[i][j] = dp[i-1][j-1] + 1, if text1[i-1] == text2[j-1]
        # dp[i][j] = max(dp[i-1][j], dp[i][j-1]), if text1[i-1] != text2[j-1]
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if text1[i - 1] == text2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

        return dp[m][n]
    
    def maxProfit(self, prices: List[int], fee: int) -> int:
        r"""
        给定一个整数数组 prices，其中 prices[i]表示第 i 天的股票价格 ；
        整数 fee 代表了交易股票的手续费用。

        你可以无限次地完成交易，但是你每笔交易都需要付手续费。如果你已经购买了一个股票，
        在卖出它之前你就不能再继续购买股票了。

        返回获得利润的最大值。

        注意：这里的一笔交易指买入持有并卖出股票的整个过程，每笔交易你只需要为支付一次手续费。
        """
        # 边界条件
        if not prices:
            return 0

        n = len(prices)

        # 动态规划
        # dp[i][0] 表示第 i 天交易完后手里没有股票的最大利润
        # dp[i][1] 表示第 i 天交易完后手里持有一支股票的最大利润
        dp = [[0] * 2 for _ in range(n)]

        # 初始状态
        dp[0][0] = 0
        dp[0][1] = -prices[0]

        # 状态转移方程
        # dp[i][0] = max(dp[i-1][0], dp[i-1][1] + prices[i] - fee)
        # dp[i][1] = max(dp[i-1][1], dp[i-1][0] - prices[i])
        for i in range(1, n):
            dp[i][0] = max(dp[i - 1][0], dp[i - 1][1] + prices[i] - fee)
            dp[i][1] = max(dp[i - 1][1], dp[i - 1][0] - prices[i])

        return dp[n - 1][0]