"""
问题描述：

给定一个正整数数组 nums 和 k，要求找到子数组，输出其最大平均值
并且子数组长度要满足大于等于 k
"""

from typing import List


class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        # 边界条件：如果数组为空，返回0
        if not nums:
            return 0
        
        def _check(num) -> bool:
            """
            检查是否存在长度为k的子数组，其平均值大于等于num
            通过计算前缀和来判断
            """
            # 构建前缀和数组，每个元素减去num
            prefix = [0] * (len(nums) + 1)
            for i in range(len(nums)):
                prefix[i + 1] = prefix[i] + nums[i] - num
            
            # 维护最小前缀和
            min_prefix = 0
            # 检查是否存在长度为k的子数组满足条件
            for i in range(k, len(nums) + 1):
                if prefix[i] - min_prefix >= 0:
                    return True
                min_prefix = min(min_prefix, prefix[i - k + 1])
            return False
        
        # 初始化二分查找的左右边界为数组的最小值和最大值
        left, right = min(nums), max(nums)
        # 使用二分查找寻找最大平均值
        while left < right:
            mid = (left + right) / 2
            if _check(mid):
                left = mid
            else:
                right = mid
                
        return left
