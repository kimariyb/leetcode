"""
问题描述：

给定一个数组 heights，表示不同的木板的高度，在装水的时候，你可以选择两根木板，
然后装满水，在不能倾斜的情况下，里面能装多少水，应该由较短的木板决定。请问最多能装多少水？
"""
from typing import List

class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # 边界条件
        if len(heights) < 2:
            return 0
        
        # 初始化左右指针
        left, right = 0, len(heights) - 1
        max_area = 0
        
        while left < right:
            # 计算当前面积
            curr_area = min(heights[left], heights[right]) * (right - left)
            max_area = max(max_area, curr_area)

            # 移动较短的木板
            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1

        return max_area
    
    
if __name__ == '__main__':
    heights = [1, 8, 6, 2, 5, 4, 8, 3, 7]
    solution = Solution()
    print(solution.maxArea(heights))
    # 输出：49