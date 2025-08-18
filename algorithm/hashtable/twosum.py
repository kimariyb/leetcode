from typing import List
from collections import defaultdict

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # {'num': 'index'}
        mapping = defaultdict(int)

        # 遍历数组
        for i, num in enumerate(nums):
            # 计算差值
            diff = target - num
            # 如果差值在字典中，则返回差值的索引和当前索引
            if diff in mapping:
                return [mapping[diff], i]
            # 如果差值不在字典中，则将当前数字和索引存入字典
            mapping[num] = i
            
        return []