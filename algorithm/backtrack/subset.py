"""
问题描述：

给定一个数组 nums，其中元素互不相同，
返回这个数组里面所有的可能的子集（包括空集）。要求子集不能重复
"""

from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # 边界条件
        if not nums:
            return [[]]
        
        # 初始化结果
        res = []

        # 回溯
        def backtrack(start: int, curr_set: List[int]):  
            # 将当前子集添加到结果中
            # curr_set[:] 是 curr_set 的一个拷贝，
            # 因为 curr_set 是一个可变对象，如果不拷贝，
            # curr_set 中的元素会被清空
            res.append(curr_set[:])  
            
            # 遍历数组，从 start 开始
            for i in range(start, len(nums)):
                # 将当前元素添加到当前子集中
                curr_set.append(nums[i])
                # 递归调用 backtrack，从下一个元素开始
                backtrack(i + 1, curr_set)
                # 回溯，将当前元素从当前子集中移除
                curr_set.pop()

        backtrack(0, [])
        return res
        
    
if __name__ == '__main__':
    nums = [1, 2, 3]
    print(Solution().subsets(nums))