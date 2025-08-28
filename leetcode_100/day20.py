from typing import List


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        r"""
        一个机器人位于一个 m x n 网格的左上角 （起始点在下图中标记为 “Start” ）。

        机器人每次只能向下或者向右移动一步。机器人试图达到网格的右下角（在下图中标记为 “Finish” ）。

        问总共有多少条不同的路径？
        """
        # 初始化动态规划
        dp = [[1] * n for _ in range(m)]
        
        # 状态转移方程
        # dp[i][j] = dp[i-1][j] + dp[i][j-1]
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1]

        return dp[-1][-1]
    
    def minPathSum(self, grid: List[List[int]]) -> int:
        r"""
        给定一个包含非负整数的 m x n 网格 grid ，
        请找出一条从左上角到右下角的路径，使得路径上的数字总和为最小。

        说明：每次只能向下或者向右移动一步
        """
        # 边界条件
        if not grid or not grid[0]:
            return 0

        # 初始化动态规划
        m, n = len(grid), len(grid[0])
        dp = [[0] * n for _ in range(m)]

        # 初始化第一行和第一列
        dp[0][0] = grid[0][0]
        
        # 状态转移方程
        # dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + grid[i][j]
        for i in range(1, m):
            dp[i][0] = dp[i - 1][0] + grid[i][0]
        for j in range(1, n):
            dp[0][j] = dp[0][j - 1] + grid[0][j]

        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = min(dp[i - 1][j], dp[i][j - 1]) + grid[i][j]

        return dp[-1][-1]
    
    def longestPalindrome(self, s: str) -> str:
        r"""
        给你一个字符串 s，找到 s 中最长的 回文 子串。
        """
        n = len(s)

        # 边界条件：如果 s 等于 1，则直接返回自己
        if n == 1:
            return s

        # 初始化动态规划
        dp = [[False] * n for _ in range(n)]
        start = 0
        max_len = 1
        
        # 所有长度为 1 的子串都是回文
        for i in range(n):
            dp[i][i] = True
        
        # 检查长度为 2 的子串
        for i in range(n - 1):
            if s[i] == s[i + 1]:
                dp[i][i + 1] = True
                start = i
                max_len = 2

        # 检查长度大于 2 的子串
        for l in range(3, n + 1):
            for i in range(n - l + 1):
                j = i + l - 1
                if s[i] == s[j] and dp[i + 1][j - 1]:
                    dp[i][j] = True
                    if l > max_len:
                        start = i
                        max_len = l

        return s[start:start + max_len]
    
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        r"""
        给定两个字符串 text1 和 text2，返回这两个字符串的最长 公共子序列 的长度。
        如果不存在 公共子序列 ，返回 0 。

        一个字符串的 子序列 是指这样一个新的字符串：它是由原字符串在不改变字符的相对顺序的情况下删除某些字符
        （也可以不删除任何字符）后组成的新字符串。

        - 例如，"ace" 是 "abcde" 的子序列，但 "aec" 不是 "abcde" 的子序列。
        
        两个字符串的 公共子序列 是这两个字符串所共同拥有的子序列。
        """
        # 边界条件
        if text1 == text2:
            return len(text1)
        
        m, n = len(text1), len(text2)
        
        # 初始化动态规划
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        
        # 状态转移方程
        # dp[i][j] = dp[i-1][j-1] + 1 if text1[i-1] == text2[j-1] 
        # else max(dp[i-1][j], dp[i][j-1])
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if text1[i - 1] == text2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    # 
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

        return dp[-1][-1]

    def minDistance(self, word1: str, word2: str) -> int:
        r"""
        给你两个单词 word1 和 word2， 请返回将 word1 转换成 word2 所使用的最少操作数  。

        你可以对一个单词进行如下三种操作：

        - 插入一个字符
        - 删除一个字符
        - 替换一个字符
        """
        # 边界条件 1：如果 word1 == word2
        if word1 == word2:
            return 0
        
        # 边界条件 2：如果 m, n 其中是空字符
        m, n = len(word1), len(word2)
        if m == 0:
            return n
        if n == 0:
            return m
        
        # 初始化动态规划
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        
        # 状态转移方程
        # dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1
        for i in range(1, m + 1):
            dp[i][0] = i
        for j in range(1, n + 1):
            dp[0][j] = j

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if word1[i - 1] == word2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    dp[i][j] = min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]) + 1

        return dp[-1][-1]