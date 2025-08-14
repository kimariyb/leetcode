"""
问题描述：

给定一个数组，找出其中最小的 k 个数
"""

from typing import List
import heapq


class Solution:
    def getLeastNumbers(self, nums: List[int], k: int) -> List[int]:
        # 边界条件
        if k == 0:
            return []
        if not nums:
            return []
        if k >= len(nums):
            return nums

        # 使用堆排序
        max_heap = []
        for num in nums:
            if len(max_heap) < k:
                heapq.heappush(max_heap, -num)
            else:
                if -num > max_heap[0]:
                    heapq.heappop(max_heap)
                    heapq.heappush(max_heap, -num)
                    
        # 将堆中的负数转换回正数
        return [-num for num in max_heap]
    

if __name__ == '__main__':
    nums = [3, 2, 1]
    k = 2
    s = Solution()
    print(s.getLeastNumbers(nums, k))