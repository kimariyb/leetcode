"""
问题描述：

给定无重复元素的数组 nums，输出这个数组所有的排列
"""

from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        # 边界条件
        if len(nums) <= 1:
            return [nums]
        
        # 初始化结果
        res = []

        # 回溯
        def backtrack(curr_list: List[int]):
            # 循环终止条件：如果当前排列长度等于原来数组的长度
            if len(curr_list) == len(nums):
                res.append(curr_list[:])
                return
            
            for num in nums:
                # 剪枝：如果当前元素已经在当前排列中，则跳过
                if num in curr_list:
                    continue
                
                # 做选择
                curr_list.append(num)
                # 递归
                backtrack(curr_list)
                # 撤销选择
                curr_list.pop()              
                
        backtrack([])
        return res


if __name__ == '__main__':
    s = Solution()
    print(s.permute([1, 2, 3]))
    