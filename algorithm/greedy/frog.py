"""
问题描述：

给定一个数组 nums，元素 nums[i] >= 0，一只青蛙站在 index=i，
那它可以跳到 nums[i+1],...,nums[i+nums[i]] （不能跳出数组）。

请问这只青蛙从 index=0 出发，能不能跳到 index=nums.length-1

"""
from typing import List

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # 边界条件
        if len(nums) == 1:
            return True
        if nums[0] == 0:
            return False

        # 初始化
        max_reach = 0 # 当前能跳到的最远距离
        
        for i in range(len(nums)):
            # 如果当前能跳到的最远距离小于当前下标，说明无法跳到终点
            if i > max_reach:
                return False
            # 更新能跳到的最远距离
            max_reach = max(max_reach, i + nums[i])
            # 如果能跳到的最远距离大于等于终点下标，说明可以跳到终点
            if max_reach >= len(nums) - 1:
                return True

        return False