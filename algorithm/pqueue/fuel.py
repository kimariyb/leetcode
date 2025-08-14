"""
问题描述：

一辆汽车携带 startFuel 升汽油从位置 0 出发前往位置 target，
按顺序有一系列加油站 stations。

第i个加油站位于 stations[i][0]，可以加 stations[i][1]升油(一个加油站只能加一次)。

如果想要到达 target，输出最少加油次数。如果不能到达 target，那么返回-1

两个条件:
1.假设汽车油箱总是很大
2.假设行走一单位距离，消耗一升汽油
"""
import heapq
from typing import List


class Solution:
    def minRefuelStops(
        self, 
        target: int, 
        startFuel: int, 
        stations: List[List[int]]
    ) -> int:
        # 边界条件1：初始油量足够直接到达目标        
        if startFuel >= target:
            return 0
        
        # 边界条件2：没有加油站且初始油量不足
        if not stations:
            return -1
        
        # 初始化优先队列，存储油量
        max_heap = []
        curr_fuel = startFuel
        curr_pos = 0
        res = 0
        
        # 处理所有加油站
        for pos, fuel in stations + [[target, 0]]:
            # 边界条件3：忽略超过目标的加油站
            if pos > target:
                continue

            dist = pos - curr_pos
            # 油量不足以到达下一个位置时，从堆中取油
            while curr_fuel < dist:
                # 边界条件4：无油可加且无法到达
                if not max_heap:
                    return -1
                curr_fuel += -heapq.heappop(max_heap)
                res += 1

            # 将当前加油站油量加入堆中
            curr_fuel -= dist
            curr_pos = pos
            heapq.heappush(max_heap, -fuel)

        return res if curr_pos == target else -1
    
    
if __name__ == '__main__':
    s = Solution()
    print(s.minRefuelStops(
        100,
        10, 
        [[10, 60], [20, 30], [30, 30], [60, 40]])
    )