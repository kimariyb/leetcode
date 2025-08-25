from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        r"""
        给你一个字符串 s 和一个字符串列表 wordDict 作为字典。
        如果可以利用字典中出现的一个或多个单词拼接出 s 则返回 true。

        注意：不要求字典中出现的单词全部都使用，并且字典中的单词可以重复使用。
        """
        # 边界条件
        if not s or not wordDict:
            return False
        
        # 将字典转化为集合
        word_set = set(wordDict)
        n = len(s)

        # 初始化动态规划
        dp = [False] * (n + 1)
        dp[0] = True
        
        # 状态转移方程：
        # dp[i] = dp[j] and s[j:i] in word_set
        for i in range(1, n + 1):
            for j in range(i):
                if dp[j] and s[j:i] in word_set:
                    dp[i] = True
                    break

        return dp[-1]

    def lengthOfLIS(self, nums: List[int]) -> int:
        r"""
        给你一个整数数组 nums ，找到其中最长严格递增子序列的长度。

        子序列 是由数组派生而来的序列，删除（或不删除）数组中的元素而不改变其余元素的顺序。
        例如，[3,6,2,7] 是数组 [0,3,1,6,2,2,7] 的子序列。
        """
        # 边界条件
        if not nums:
            return 0

        n = len(nums)
        # 初始化动态规划
        dp = [1] * n

        # 状态转移方程：
        # dp[i] = max(dp[j] + 1, dp[i])
        for i in range(1, n):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[j] + 1, dp[i])

        return max(dp)
    
    def maxProduct(self, nums: List[int]) -> int:
        r"""
        给你一个整数数组 nums ，请你找出数组中乘积最大的非空连续 子数组
        （该子数组中至少包含一个数字），并返回该子数组所对应的乘积。

        测试用例的答案是一个 32-位 整数。
        """
        # 边界条件
        if not nums:
            return 0

        n = len(nums)
        
        # 初始化动态规划
        dp_max = [0] * n
        dp_min = [0] * n
        dp_max[0] = dp_min[0] = nums[0]

        # 状态转移方程：
        # dp_max[i] = max(dp_max[i-1] * nums[i], dp_min[i-1] * nums[i], nums[i])
        # dp_min[i] = min(dp_max[i-1] * nums[i], dp_min[i-1] * nums[i], nums[i])
        for i in range(1, n):
            dp_max[i] = max(dp_max[i - 1] * nums[i], dp_min[i - 1] * nums[i], nums[i])
            dp_min[i] = min(dp_max[i - 1] * nums[i], dp_min[i - 1] * nums[i], nums[i])

        return max(dp_max)
    
    def canPartition(self, nums: List[int]) -> bool:
        r"""
        给你一个 只包含正整数 的 非空 数组 nums 。
        请你判断是否可以将这个数组分割成两个子集，使得两个子集的元素和相等。
        """
        # 边界条件
        if not nums:
            return False

        total = sum(nums)
        # 边界条件：如果总和为奇数，则不可能分割成两个和相等的子集
        if total % 2 != 0:
            return False

        target = total // 2
        # 初始化动态规划
        dp = [False] * (target + 1)
        dp[0] = True

        # 状态转移方程：
        # dp[i] = dp[i] or dp[i - nums[j]]
        for num in nums:
            for i in range(target, num - 1, -1):
                dp[i] = dp[i] or dp[i - num]

        return dp[target]
    
    def longestValidParentheses(self, s: str) -> int:
        r"""
        给你一个只包含 '(' 和 ')' 的字符串，
        找出最长有效（格式正确且连续）括号 子串 的长度。

        左右括号匹配，即每个左括号都有对应的右括号将其闭合的字符串是格式正确的，
        比如 "(()())"。
        """
        # 边界条件
        if not s:
            return 0

        # 初始化栈
        stack = [-1]
        max_len = 0
        
        for i, char in enumerate(s):
            # 如果是左括号，则入栈
            if char == '(':
                stack.append(i)
            # 如果是右括号，则出栈
            else:
                stack.pop()
                # 如果栈为空，说明当前右括号没有匹配的左括号，
                # 将当前右括号的索引入栈作为新的"基准点"。
                if not stack:
                    stack.append(i)
                # 如果栈不为空，则说明当前右括号有匹配的左括号，
                # 需要计算当前有效括号的长度
                else:
                    max_len = max(max_len, i - stack[-1])
        
        return max_len