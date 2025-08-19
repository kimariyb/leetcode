"""
问题描述：

数组里的元素组成一个山峰，位于峰顶的元素，总是比它左边和右边的元素大。
请找出这个峰顶元素。
"""
from typing import List


class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        # 边界条件
        if not nums:
            return -1
        
        left, right = 0, len(nums) - 1
        
        # 二分搜索
        while left < right:
            mid = left + (right - left) // 2
            if nums[mid] < nums[mid + 1]:
                left = mid + 1 # 峰顶在右侧
            else:
                right = mid # 峰顶在左侧或 mid 就是峰顶

        return left 


if __name__ == '__main__':
    nums = [1, 2, 3, 1]
    s = Solution()
    print(s.findPeakElement(nums))
    # 输出 2