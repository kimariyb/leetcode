"""
问题描述：

在一个无向图上，给定点个数 n，编号从 0 ~ n，再给定边的个数 m。其中每条边由
x[i], y[i], w[i] 表示。x[i], y[i] 表示这条边连接的 2 个点的编号，w[i] 表示这条边的危险系数。

现在我们想找到一条路径从 0 ~ n，使得这条路径上最大危险系数最小。
（注意：不是路径和，而是路径上的最大值最小）
"""
import heapq
from typing import List


class Solution:
    def minMaxDanger(self, n: int, edges: List[List[int]]) -> int:
        # 初始化邻接表
        adj = [[] for _ in range(n + 1)]
        for x, y, w in edges:
            adj[x].append((y, w))
            adj[y].append((x, w))
        
        # 初始化 max_w 和优先队列
        max_w = [float('inf')] * (n + 1)
        max_w[0] = 0
        heap = []
        heapq.heappush(heap, (0, 0)) # (当前危险系数, 当前节点)

        # Dijkstra 算法
        while heap:
            # 取出当前最大危险系数最小的节点
            curr_max, curr_node = heapq.heappop(heap)
            # 如果到达目标节点，返回当前路径的最大危险系数
            if curr_node == n:
                return curr_max
            
            # 如果当前路径的最大危险系数大于已知的最小值，跳过
            if curr_max > max_w[curr_node]:
                continue
            
            # 遍历当前节点的所有邻居
            for v, w in adj[curr_node]:
                # 计算经过当前边后的新路径最大危险系数
                new_max = max(curr_max, w)
                # 如果新路径的最大危险系数小于已知的最小值，更新并加入优先队列
                if new_max < max_w[v]:
                    max_w[v] = new_max
                    heapq.heappush(heap, (new_max, v))
                    
        # 如果没有找到路径，返回 -1
        return -1 
    
    
if __name__ == '__main__':
    s = Solution()
    n = 3
    edges = [
        [0, 1, 2],
        [0, 2, 5],
        [1, 2, 3],
        [1, 3, 4],
        [2, 3, 1]
    ]
    print(s.minMaxDanger(n, edges))

