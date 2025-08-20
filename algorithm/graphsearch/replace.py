"""
问题描述：

给你一个矩阵 matrix，里面只包含字母 'O' 和 'X'，
如果一个 'O' 上下左右四周都被 'X' 包围，那么这个 'O' 会被替换成 'X'

请你实现这一过程
"""
from typing import List


class Solution:
    def replaceLetters(self, matrix: List[List[str]]) -> List[List[str]]:
        # 边界条件
        if not matrix or not matrix[0]:
            return matrix
        
        m, n = len(matrix), len(matrix[0])

        # 深度优先遍历
        def dfs(i, j) -> bool:
            directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
            for dx, dy in directions:
                nx, ny = i + dx, j + dy
                # 检查是否越界或者不是 'X'
                if nx < 0 or nx >= m or ny < 0 or ny >=n or matrix[nx][ny] != 'X':
                    return False
            return True
        
        # 第一步：将需要替换的'O'标记为临时字符
        TEMP = '#'  # 临时标记
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 'O' and dfs(i, j):
                    matrix[i][j] = TEMP
                    
        # 第二步：将临时标记替换为'X'
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == TEMP:
                    matrix[i][j] = 'X'

        return matrix
    
    
if __name__ == '__main__':
    matrix = [
        ['X', 'X', 'X', 'X'],
        ['X', 'O', 'O', 'X'],
        ['X', 'X', 'O', 'X'],
        ['X', 'O', 'X', 'X']
    ]
    solution = Solution()
    print(solution.replaceLetters(matrix))
