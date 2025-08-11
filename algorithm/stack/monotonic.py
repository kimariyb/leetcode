"""
问题描述：

一个整数数组 A，找到每个元素: 右边第一个比我小的下标位置，没有则用 -1 表示
"""
from typing import List


class Solution:
    def findRightSmall(self, nums: List[int]) -> List[int]:
        # 边界条件
        if not nums:
            return []
        
        # 初始化栈
        stack = []
        
        # 初始化结果
        res = [-1] * len(nums)

        # 遍历数组
        for i in range(len(nums)):
            # 如果栈不为空，且当前元素小于栈顶元素，则更新结果
            while stack and nums[i] < nums[stack[-1]]:
                res[stack.pop()] = i
            # 将当前元素下标入栈
            stack.append(i)

        return res
    
    
if __name__ == '__main__':
    s = Solution()
    print(s.findRightSmall([3, 4, 2, 5, 1]))