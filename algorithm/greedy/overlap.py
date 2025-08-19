"""
问题描述：

给定一系列区间，请你选一个子集，使得这个子集中的区间都不相互重叠，
并且这个子集里面的元素个数最多
"""
from typing import List


class Solution:
    def maxNonOverlapping(self, intervals: List[List[int]]) -> int:
        # 边界条件
        if not intervals:
            return 0
        
        # 按结束时间升序排序
        intervals.sort(key=lambda x: x[1])
        
        # 初始化结果和第一个区间的结束时间
        res = 1
        last_end = intervals[0][1]

        # 遍历区间
        for start, end in intervals[1:]:
            # 如果当前区间的开始时间大于等于上一个区间的结束时间，则不重叠
            if start >= last_end:
                res += 1
                last_end = end

        return res
    

if __name__ == '__main__':
    s = Solution()
    intervals = [[1, 2], [2, 3], [3, 4], [1, 3]]
    print(s.maxNonOverlapping(intervals))
    