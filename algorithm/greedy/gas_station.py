"""
问题描述：

巨大的环形赛道上有 N 个加油站，第 i 个加油站可以加油 gas[i] 升，
而从第 i 个加油站开到下一个加油站，需要 消耗 costs[i] 升汽油。

请你选择一个起始加油站，能够跑完环形赛道一圈

条件：
1. 环形赛道；2. 汽车油箱总是足够大
"""

from typing import List


class Solution:
    def canCompleteCircuit(self, gas: List[int], costs: List[int]) -> int:
        # 边界条件
        if not gas or not costs:
            return -1
        # 如果总油量小于总消耗量，则无法跑完一圈
        if sum(gas) < sum(costs):
            return -1
        
        # 初始化
        start = 0
        curr_gas = 0
        
        for i in range(len(gas)):
            # 当前油量
            curr_gas += gas[i] - costs[i]
            # 如果当前油量小于0，则从下一个加油站重新开始
            if curr_gas < 0:
                start = i + 1
                curr_gas = 0

        return start if start < len(gas) else -1
    
    
if __name__ == '__main__':
    s = Solution()
    gas = [1, 2, 3, 4, 5]
    costs = [3, 4, 5, 1, 2]
    print(s.canCompleteCircuit(gas, costs))
    