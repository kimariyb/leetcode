"""
问题描述：

你是一个专业的小偷，计划去沿街的住户家里偷盗。每间房内都藏有一定的现金，
影响你偷盗的唯一制约元素就是相邻的房屋装有相互连通的防盗系统，
如果两间相邻的房屋在同一晚上被小偷闯入，系统会自动报警。

给定一个代表每个房屋存放金额的非负整数数组，要求你计算不触动报警装置的情况下，
一夜之内能够偷窃到的最高金额
"""

from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        # 边界条件
        if not nums:
            return 0
        if len(nums) == 1:  
            return nums[0]

        # dp[i] 表示前i个房屋能偷到的最大金额
        # dp[i] = max(dp[i-1], dp[i-2] + nums[i])
        dp = [0] * len(nums)
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])
        
        for i in range(2, len(nums)):
            # 最后一步：处理第 N 个房间
            # 如果选择偷 N 个房间，收益就是 dp[i-2] + nums[i]
            # 如果选择不偷 N 个房间，收益就是 dp[i-1]
            dp[i] = max(dp[i-1], dp[i-2] + nums[i])

        return dp[-1]
    

if __name__ == '__main__':
    nums = [1, 2, 3, 1]
    print(Solution().rob(nums))
    
