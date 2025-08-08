from collections import defaultdict, deque
from typing import List
import heapq


class Solution:
    def calcEquation(
        self, equations: List[List[str]], 
        values: List[float], 
        queries: List[List[str]]
    ) -> List[float]:
        r"""
        给你一个变量对数组 equations 和一个实数值数组 values 作为已知条件，
        其中 equations[i] = [Ai, Bi] 和 values[i] 共同表示等式 Ai / Bi = values[i] 。
        每个 Ai 或 Bi 是一个表示单个变量的字符串。

        另有一些以数组 queries 表示的问题，其中 queries[j] = [Cj, Dj] 表示第 j 个问题，
        请你根据已知条件找出 Cj / Dj = ? 的结果作为答案。

        返回 所有问题的答案 。如果存在某个无法确定的答案，则用 -1.0 替代这个答案。
        如果问题中出现了给定的已知条件中没有出现的字符串，也需要用 -1.0 替代这个答案。

        注意：输入总是有效的。你可以假设除法运算中不会出现除数为 0 的情况，且不存在任何矛盾的结果。

        注意：未在等式列表中出现的变量是未定义的，因此无法确定它们的答案
        """
        # 首先构建图
        graph = defaultdict(list)

        # 添加边和反向边
        for i, (a, b) in enumerate(equations):
            graph[a].append((b, values[i]))  # a / b = values[i]
            graph[b].append((a, 1.0 / values[i]))  # b / a = 1 / values[i]

        def dfs(start, end, visited):
            # 深度优先搜索
            if start not in graph or end not in graph:
                return -1.0
            # 如果起点和终点相同，则返回 1.0
            if start == end:
                return 1.0
            
            visited.add(start)
            
            for neigbor, weight in graph[start]:
                if neigbor not in visited:
                    result = dfs(neigbor, end, visited)
                    if result != -1.0:
                        return weight * result

            return -1.0

        result = []
        for a, b in queries:
            result.append(dfs(a, b, set()))

        return result
    

    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        r"""
        给你一个 m x n 的迷宫矩阵 maze （下标从 0 开始），矩阵中有空格子（用 '.' 表示）和墙（用 '+' 表示）。
        同时给你迷宫的入口 entrance ，用 entrance = [entrancerow, entrancecol] 表示你一开始所在格子的行和列。

        每一步操作，你可以往 上，下，左 或者 右 移动一个格子。你不能进入墙所在的格子，你也不能离开迷宫。
        你的目标是找到离 entrance 最近 的出口。出口 的含义是 maze 边界 上的 空格子。entrance 格子 不算 出口。

        请你返回从 entrance 到最近出口的最短路径的 步数 ，如果不存在这样的路径，请你返回 -1 。
        """
        # 边界条件
        if not maze or not maze[0]:
            return -1

        m, n = len(maze), len(maze[0])
        # BFS 初始化
        queue = deque([(entrance[0], entrance[1], 0)])
        visited = set([(entrance[0], entrance[1])])

        # 四个方向
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        while queue:
            x, y, steps = queue.popleft()
            
            # 探索四个方向
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                
                # 如果到达边界，则返回步数
                if not (0 <= nx < m and 0 <= ny < n):
                    if [x, y] != entrance:
                        return steps
                    continue

                # 检查是否可以到新的位置
                if maze[nx][ny] == '.' and (nx, ny) not in visited:
                    visited.add((nx, ny))
                    queue.append((nx, ny, steps + 1))

        return -1

    def orangesRotting(self, grid: List[List[int]]) -> int:
        r"""
        在给定的 m x n 网格 grid 中，每个单元格可以有以下三个值之一：

        - 值 0 代表空单元格；
        - 值 1 代表新鲜橘子；
        - 值 2 代表腐烂的橘子。

        每分钟，腐烂的橘子 周围 4 个方向上相邻 的新鲜橘子都会腐烂。

        返回 直到单元格中没有新鲜橘子为止所必须经过的最小分钟数。如果不可能，返回 -1 。
        """
        # 边界条件
        if not grid or not grid[0]:
            return -1

        m, n = len(grid), len(grid[0])
        # BFS 初始化
        queue = deque()
        fresh_count = 0

        # 将所有腐烂的橘子加入队列
        for i in range(m):  
            for j in range(n):
                if grid[i][j] == 1:
                    fresh_count += 1
                elif grid[i][j] == 2:
                    queue.append((i, j))

        # 如果没有新鲜橘子，则返回 0
        if fresh_count == 0:
            return 0
        
        # 如果没有腐烂的橘子但有新鲜的橘子，返回 -1
        if not queue:
            return -1

        # BFS 模拟腐烂过程
        minutes = 0
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        while queue and fresh_count > 0:
            minutes += 1
            # 处理当前轮次所有腐烂的橘子
            current = len(queue)
            for _ in range(current):
                x, y = queue.popleft()

                # 感染四个方向上的橘子
                for dx, dy in directions:
                    nx, ny = x + dx, y + dy

                    # 检查是否可以到新的位置
                    if 0 <= nx < m and 0 <= ny < n and grid[nx][ny] == 1:
                        grid[nx][ny] = 2
                        fresh_count -= 1
                        queue.append((nx, ny))
        
        # 如果还有新鲜橘子，返回 -1；否则返回所需时间
        return minutes if fresh_count == 0 else -1

    def findKthLargest(self, nums: List[int], k: int) -> int:
        r"""
        给定整数数组 nums 和整数 k，请返回数组中第 k 个最大的元素。

        请注意，你需要找的是数组排序后的第 k 个最大的元素，而不是第 k 个不同的元素。

        你必须设计并实现时间复杂度为 O(n) 的算法解决此问题。
        """
        # 建堆
        heapq.heapify(nums)
        
        # 弹出 n - k 个最小值，剩下的就是第 k 个最大值
        for _ in range(len(nums) - k):
            heapq.heappop(nums)

        return heapq.heappop(nums)


class SmallestInfiniteSet:
    r"""
    现有一个包含所有正整数的集合 [1, 2, 3, 4, 5, ...] 。

    实现 SmallestInfiniteSet 类：

    - SmallestInfiniteSet() 初始化 SmallestInfiniteSet 对象以包含 所有 正整数。
    - int popSmallest() 移除 并返回该无限集中的最小整数。
    - void addBack(int num) 如果正整数 num 不 存在于无限集中，则将一个 num 添加 到该无限集中。
    """
    def __init__(self) -> None:
        # 使用堆来维护被添加回来的较小数字
        self.min_heap = []
        # 记录堆中已存在的数字，避免重复
        self.in_heap = set()
        # 记录当前连续序列的起始点
        self.current_min = 1
    
    def popSmallest(self):
        # 如果堆不为空且堆顶元素小于当前连续序列起点
        if self.min_heap and self.min_heap[0] < self.current_min:
            smallest = heapq.heappop(self.min_heap)
            self.in_heap.remove(smallest)
            return smallest
        else:
            # 返回连续序列的最小值
            result = self.current_min
            self.current_min += 1
            return result
        
    def addBack(self, num):
        # 只有当num小于当前连续序列起点且不在堆中时才添加
        if num < self.current_min and num not in self.in_heap:
            heapq.heappush(self.min_heap, num)
            self.in_heap.add(num)