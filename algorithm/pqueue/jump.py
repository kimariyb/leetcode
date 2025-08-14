"""
问题描述：

假设你正在玩跳跃游戏，从低处往高处跳的时候，可以有两种方法

- 方法一:塞砖块，但是你拥有砖块数是有限制的。为了简单起见，
高度差就是你需要砖块数
- 方法二:用梯子，梯子可以无视高度差(你可以认为再高也能爬上去)，
但是梯子的个数是有限的(个只能用一次)

其他无论是平着跳，还是从高处往低处跳，不需要借助什么就可以完成
(在这道题中我们默认无论从多高跳下来，也摔不死)

给你一个数组，用来表示不同的高度。
假设你总是站在 index=0 的高度开始。那么请问，你最远能跳到哪里?
"""
from typing import List
import heapq

class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, landers: int) -> int:
        # 边界条件
        if not heights:
            return -1
        
        # 初始化最大堆
        max_heap = []
        for i in range(len(heights) - 1):
            diff = heights[i + 1] - heights[i]
            if diff <= 0:
                continue
            
            # 使用梯子优先处理最大的高度差
            if landers > 0:
                heapq.heappush(max_heap, diff)
                landers -= 1
            else:
                # 如果没有梯子，尝试用砖块
                if max_heap and diff > max_heap[0]:
                    # 当前高度差比堆顶大，替换堆顶的高度差用砖块处理
                    smaller_ladder = heapq.heappop(max_heap)
                    if bricks >= smaller_ladder:
                        bricks -= smaller_ladder
                        heapq.heappush(max_heap, diff)
                        
                    else:
                        return i
                else:
                    # 当前高度差比堆顶小，或者堆为空，用砖块处理
                    if bricks >= diff:
                        bricks -= diff
                    else:
                        return i

        return len(heights) - 1


if __name__ == '__main__':
    s = Solution()
    print(s.furthestBuilding([3, 1, 6, 20, 10, 20], 5, 1))

    

        