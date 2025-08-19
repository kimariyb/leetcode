"""
问题描述：

给定一个有序数组，返回指定元素的最左边的位置
"""
from typing import List


class Solution:
    def findLeftMost(self, nums: List[int], target: int) -> int:
        # 边界条件
        if not nums:
            return -1
        
        left, right = 0, len(nums) - 1
        result = -1  # 用于记录最左边的索引
        
        # 二分搜索
        while left <= right:
            mid = left + (right - left) // 2 # 避免整数溢出
            if nums[mid] == target:
                result = mid # 记录当前位置
                right = mid - 1 # 继续往左搜索
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1

        return result
    
    
if __name__ == '__main__':
    nums = [1, 2, 2, 2, 3, 4, 5]
    target = 2
    solution = Solution()
    print(solution.findLeftMost(nums, target))