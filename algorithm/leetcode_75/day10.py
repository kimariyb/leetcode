from typing import List
import math


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        r"""
        珂珂喜欢吃香蕉。这里有 n 堆香蕉，第 i 堆中有 piles[i] 根香蕉。
        警卫已经离开了，将在 h 小时后回来。

        珂珂可以决定她吃香蕉的速度 k （单位：根/小时）。
        每个小时，她将会选择一堆香蕉，从中吃掉 k 根。
        如果这堆香蕉少于 k 根，她将吃掉这堆的所有香蕉，然后这一小时内不会再吃更多的香蕉。  

        珂珂喜欢慢慢吃，但仍然想在警卫回来前吃掉所有的香蕉。

        返回她可以在 h 小时内吃掉所有香蕉的最小速度 k（k 为整数）。
        """
        # 初始化左右指针
        left, right = 1, max(piles)
        res = right
        
        # 二分查找
        while left <= right:
            mid = (left + right) // 2
            # 计算当前速度下需要的时间
            total_time = 0
            for pile in piles:
                total_time += math.ceil(pile / mid)
            
            # 如果时间小于等于 h，说明速度可以更快
            if total_time <= h:
                res = mid
                right = mid - 1
            # 如果时间大于 h，说明速度太慢
            else:
                left = mid + 1

        return res
        
    def letterCombinations(self, digits: str) -> List[str]:
        r"""
        给定一个仅包含数字 2-9 的字符串，返回所有它能表示的字母组合。
        答案可以按 任意顺序 返回。

        给出数字到字母的映射如下（与电话按键相同）。注意 1 不对应任何字母。
        """
        # 边界条件
        if not digits:
            return []

        # 数字到字母的映射
        phone_map = {
            '2': ['a', 'b', 'c'],
            '3': ['d', 'e', 'f'],
            '4': ['g', 'h', 'i'],
            '5': ['j', 'k', 'l'],
            '6': ['m', 'n', 'o'],
            '7': ['p', 'q', 'r', 's'],
            '8': ['t', 'u', 'v'],
            '9': ['w', 'x', 'y', 'z']
        }
        
        res = []

        def backtrack(index, path):
            """回溯算法"""
            # 如果路径长度等于数字长度，说明找到了一种组合
            if index == len(digits):
                res.append(''.join(path))
                return

            # 获取当前数字对应的字母列表
            current_digits = digits[index]
            current_letters = phone_map[current_digits]

            # 遍历字母列表，将每个字母加入到路径中，并继续递归
            for letter in current_letters:
                path.append(letter)
                backtrack(index + 1, path)
                path.pop()

        # 回溯
        backtrack(0, [])
        return res
    
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        r"""
        找出所有相加之和为 n 的 k 个数的组合，且满足下列条件：

        - 只使用数字 1 到 9
        - 每个数字 最多使用一次 

        返回 所有可能的有效组合的列表。该列表不能包含相同的组合两次，
        组合可以以任何顺序返回。
        """
        res = []
        
        def backtrack(start, path, target, count):
            # 找到符合条件的组合
            if target == 0 and count == 0:
                res.append(path[:])
                return
            # 如果已经超过目标和或者组合数量超过 k，则返回
            if target <= 0 or count == 0:
                return
            
            # 从 start 开始遍历
            for i in range(start, 10):
                # 如果当前数字已经大于剩余目标和，则说明已经不可能继续了，直接跳出
                if i > target:
                    break
                
                # 将当前数字加入到路径中
                path.append(i)
                # 递归调用，继续寻找下一个数字
                backtrack(i + 1, path, target - i, count - 1)
                # 回溯，将当前数字从路径中移除
                path.pop()
        
        # 回溯
        backtrack(1, [], n, k)
        return res
    
    def tribonacci(self, n: int) -> int:
        r"""
        泰波那契序列 Tn 定义如下： 

        T0 = 0, T1 = 1, T2 = 1, 且在 n >= 0 的条件下 Tn+3 = Tn + Tn+1 + Tn+2

        给你整数 n，请返回第 n 个泰波那契数 Tn 的值。
        """
        # 边界条件
        if n == 0:
            return 0
        if n == 1 or n == 2:
            return 1
        
        # 动态规划
        dp = [0] * (n + 1)
        dp[1], dp[2] = 1, 1
        # 状态转移方程：dp[i] = dp[i-1] + dp[i-2] + dp[i-3]
        for i in range(3, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2] + dp[i - 3]

        return dp[n]
    
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        r"""
        给你一个整数数组 cost ，其中 cost[i] 是从楼梯第 i 个台阶向上爬需要支付的费用。
        一旦你支付此费用，即可选择向上爬一个或者两个台阶。

        你可以选择从下标为 0 或下标为 1 的台阶开始爬楼梯。

        请你计算并返回达到楼梯顶部的最低花费。
        """
        # 边界条件
        if len(cost) == 0:
            return 0
        if len(cost) == 1:
            return cost[0]

        # 动态规划
        dp = [0] * len(cost)
        dp[0] = cost[0]
        dp[1] = cost[1]
        # 状态转移方程：dp[i] = min(dp[i-1], dp[i-2]) + cost[i]
        # 对于每个台阶，可以选择从前面 1 个或 2 个台阶到达
        for i in range(2, len(cost)):
            dp[i] = min(dp[i - 1], dp[i - 2]) + cost[i]

        return min(dp[-1], dp[-2])
