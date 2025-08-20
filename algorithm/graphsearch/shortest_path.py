"""
问题描述：

给定一个迷宫，其中 0 表示可能通过的地方，1 表示墙壁
请问，从左上角走到右下角的最短路径是怎么样的？请依次输出路径上的点
"""

from typing import List
from collections import deque


class Solution:
    def shortestPath(self, maze: List[List[int]]) -> List[List[int]]:
        # 边界条件
        if not maze or not maze[0]:
            return []

        m, n = len(maze), len(maze[0])
        if maze[0][0] == 1 or maze[m-1][n-1] == 1:
            return []  # 起点或终点是墙壁n
        
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        queue = deque()
        queue.append((0, 0, [(0, 0)]))  # (x, y, path)
        visited = set()
        visited.add((0, 0))
        
        # BFS 标记
        while queue:    
            x, y, path = queue.popleft()
            
            # 到达终点
            if x == m-1 and y == n-1:
                return path
            
            # 遍历四个方向
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                # 判断是否越界
                if not (0 <= nx < m and 0 <= ny < n):
                    continue
                # 判断是否是墙壁
                if maze[nx][ny] == 0 and (nx, ny) not in visited:
                    visited.add((nx, ny))
                    new_path = path + [(nx, ny)]
                    queue.append((nx, ny, new_path))
        
        return []
    

if __name__ == "__main__":
    maze = [    
        [0, 0, 0, 0],
        [1, 1, 0, 1],
        [0, 0, 0, 0],
        [0, 1, 1, 0]
    ]
    s = Solution()
    print(s.shortestPath(maze))
                
                
                
        