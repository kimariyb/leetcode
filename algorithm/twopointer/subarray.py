"""
问题描述：

给定一个正数数组 nums，以及一个正整数 k，求乘积小于 k 的子数组的个数
"""
from typing import List

class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        # 边界条件
        if not nums:
            return 0
        if k <= 1:
            return 0
        
        # 初始化
        left, product, count = 0, 1, 0
        
        for right in range(len(nums)):
            product *= nums[right]
            # 如果乘积大于等于 k，则移动左边界
            while product >= k:
                product /= nums[left]
                left += 1
            # 统计以 right 结尾的子数组数量
            count += right - left + 1

        return count
    
    
if __name__ == '__main__':
    s = Solution()
    print(s.numSubarrayProductLessThanK([10, 5, 2, 6], 100))