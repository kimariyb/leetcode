"""
问题描述：

给定一个数组 nums 和滑动窗口的大小 k，请找出所有滑动窗口里的最大值。
"""

from typing import List
from collections import deque


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # 边界条件
        if not nums or k <= 0:
            return []
        
        # 初始化双端队列（利用单调队列）
        dq = deque()
        res = []
        
        for i in range(len(nums)):
            # 移除超出窗口范围的元素
            while dq and dq[0] <= i - k:
                dq.popleft()
                
            # 维护递减队列
            while dq and nums[dq[-1]] < nums[i]:
                dq.pop()
                
            dq.append(i)
            
            # 记录当前窗口最大值
            if i >= k - 1:
                res.append(nums[dq[0]])
                
        return res
                    
        
        
        