from typing import List


class Solution:
    def climbStairs(self, n: int) -> int:
        r"""
        假设你正在爬楼梯。需要 n 阶你才能到达楼顶。

        每次你可以爬 1 或 2 个台阶。你有多少种不同的方法可以爬到楼顶呢？
        """
        # 边界条件
        if n <= 2:
            return n

        # dp[i] 表示到达第 i 阶的方法数
        dp = [0] * (n + 1)
        dp[1] = 1  # 到达第 1 阶只有 1 种方法
        dp[2] = 2  # 到达第 2 阶有 2 种方法

        for i in range(3, n + 1):
            # 状态转移方程
            dp[i] = dp[i - 1] + dp[i - 2]

        return dp[n]
    
    def generate(self, numRows: int) -> List[List[int]]:
        r"""
        给定一个非负整数 numRows，生成「杨辉三角」的前 numRows 行。

        在「杨辉三角」中，每个数是它左上方和右上方的数的和。
        """
        # 边界条件
        if numRows == 0:
            return []

        # dp[i][j] 表示第 i 行第 j 列的元素
        dp = [[0] * (i + 1) for i in range(numRows)]
        dp[0][0] = 1

        # 状态转移方程
        # dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j]
        for i in range(1, numRows):
            for j in range(i + 1):
                if j == 0 or j == i:
                    dp[i][j] = 1
                else:
                    dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j]

        return dp
    
    def rob(self, nums: List[int]) -> int:
        r"""
        你是一个专业的小偷，计划偷窃沿街的房屋。每间房内都藏有一定的现金，
        影响你偷窃的唯一制约因素就是相邻的房屋装有相互连通的防盗系统，
        如果两间相邻的房屋在同一晚上被小偷闯入，系统会自动报警。

        给定一个代表每个房屋存放金额的非负整数数组，计算你 不触动警报装置的情况下 ，
        一夜之内能够偷窃到的最高金额。
        """
        # 边界条件
        if len(nums) <= 2:
            return max(nums)

        # dp[i] 表示偷窃前 i 个房屋可以获得的最大金额
        dp = [0] * len(nums)
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])
        
        # 状态转移方程
        # dp[i] = max(dp[i-1], dp[i-2] + nums[i])
        for i in range(2, len(nums)):
            dp[i] = max(dp[i - 1], dp[i - 2] + nums[i])
            
        return dp[-1]
    
    def numSquares(self, n: int) -> int:
        r"""
        给你一个整数 n ，返回 和为 n 的完全平方数的最少数量 。

        完全平方数 是一个整数，其值等于另一个整数的平方；换句话说，其值等于一个整数自乘的积。
        例如，1、4、9 和 16 都是完全平方数，而 3 和 11 不是。
        """
        # 边界条件
        if n <= 0:
            return 0
        if n <= 3:
            return n

        # dp[i] 表示和为 i 的完全平方数的最少数量
        dp = [float('inf')] * (n + 1)  # 初始化为无穷大
        dp[0] = 0  
        dp[1] = 1
        dp[2] = 2
        dp[3] = 3

        # 状态转移方程
        # dp[i] = min(dp[i - j * j] + 1) for j in range(1, int(i ** 0.5) + 1)
        # dp[i - j * j] + 1 表示组成 i 的完全平方数数量
        for i in range(4, n + 1):
            dp[i] = min(
                (dp[i - j * j] + 1) for j in range(1, int(i ** 0.5) + 1)
            )
            
        return dp[n]
    
    def coinChange(self, coins: List[int], amount: int) -> int:
        r"""
        给你一个整数数组 coins ，表示不同面额的硬币；以及一个整数 amount ，表示总金额。

        计算并返回可以凑成总金额所需的 最少的硬币个数 。如果没有任何一种硬币组合能组成总金额，返回 -1 。

        你可以认为每种硬币的数量是无限的。
        """
        # 边界条件
        if amount == 0:
            return 0

        # dp[i] 表示凑成金额 i 所需的最少硬币数
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0

        # 状态转移方程
        # dp[i] = min(dp[i - coin] + 1) for coin in coins
        # dp[i - coin] + 1 表示 使用一枚面值为 coin 的硬币后，凑成金额 i 还需要的最少硬币数
        for i in range(1, amount + 1):
            for coin in coins:
                if i - coin >= 0:
                    dp[i] = min(dp[i], dp[i - coin] + 1)

        return dp[amount] if dp[amount] != float('inf') else -1
