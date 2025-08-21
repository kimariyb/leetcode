"""
问题描述

一个只包含正整数的非空数组。
是否可以将这个数组分割成两个子集，使得两个子集的元素和相等

注意：
1. 每个数组中的元素不会超过 100
2. 数组的大小不会超过 200
"""
from typing import List


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        # 边界条件
        if not nums:
            return False
        if len(nums) == 1:
            return False
        
        # 计算数组的总和
        total = sum(nums)
        # 如果总和是奇数，则不可能分割成两个和相等的子集
        if total % 2 != 0:
            return False
        
        # 目标和为总和的一半
        target = total // 2
        # 创建dp数组，dp[i] 表示能否凑成和为 i
        # 状态转移方程：dp[i] = dp[i] or dp[i - num]
        dp = [False] * (target + 1)
        # 初始化 dp[0] 为True，因为和为 0 一定可以凑成
        dp[0] = True

        # 遍历数组中的每一个元素
        for num in nums:
            # 从后往前遍历，防止重复使用同一个元素
            for i in range(target, num - 1, -1):
                # 更新dp数组
                dp[i] = dp[i] or dp[i - num]

        # 返回dp[target]的值
        return dp[target]
    

if __name__ == '__main__':
    nums = [1, 5, 11, 5]
    solution = Solution()
    print(solution.canPartition(nums))