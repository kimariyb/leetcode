from collections import deque
from typing import List, Optional


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        r"""
        给你一个由 '1'（陆地）和 '0'（水）组成的的二维网格，请你计算网格中岛屿的数量。

        岛屿总是被水包围，并且每座岛屿只能由水平方向和/或竖直方向上相邻的陆地连接形成。

        此外，你可以假设该网格的四条边均被水包围。
        """
        # 边界条件
        if not grid or not grid[0]:
            return 0

        row, col = len(grid), len(grid[0])
        count = 0
        
        def dfs(i, j):
            """深度优先搜索"""
            # 边界条件
            if i < 0 or j < 0 or i >= row or j >= col or grid[i][j] != '1':
                return
            
            # 将当前陆地标记为已访问
            grid[i][j] = '0'
            
            # 递归搜索四个方向
            dfs(i + 1, j)
            dfs(i - 1, j)
            dfs(i, j + 1)
            dfs(i, j - 1)

        for i in range(row):
            for j in range(col):
                if grid[i][j] == '1':
                    count += 1
                    dfs(i, j)

        return count
    
    
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
        
        # 将所有腐烂橘子加入队列
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    fresh_count += 1
                elif grid[i][j] == 2:
                    queue.append((i, j))
        
        # 如果没有新鲜橘子，则返回 0 
        if fresh_count == 0:
            return 0
        
        # 如果没有腐烂的橘子，但是有新鲜橘子，则返回 -1
        if not queue:
            return -1

        # BFS
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        minutes = 0

        while queue:
            minutes += 1
            for _ in range(len(queue)):
                x, y = queue.popleft()
                for dx, dy in directions:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < m and 0 <= ny < n and grid[nx][ny] == 1:
                        grid[nx][ny] = 2
                        fresh_count -= 1
                        queue.append((nx, ny))

        return minutes if fresh_count == 0 else -1

    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        r"""
        你这个学期必须选修 numCourses 门课程，记为 0 到 numCourses - 1 。

        在选修某些课程之前需要一些先修课程。 先修课程按数组 prerequisites 给出，
        其中 prerequisites[i] = [ai, bi] ，表示如果要学习课程 ai 则 必须 先学习课程  bi 。

        例如，先修课程对 [0, 1] 表示：想要学习课程 0 ，你需要先完成课程 1 。
        请你判断是否可能完成所有课程的学习？如果可以，返回 true ；否则，返回 false 。
        """
        # 边界条件
        if not prerequisites:
            return True
        
        # 这个问题可以转化为​判断有向图是否存在环​：
        # 构建邻接表和入度数组
        graph = [[] for _ in range(numCourses)]
        indegree = [0] * numCourses
        
        # 构建图
        for course, prereq in prerequisites:
            graph[prereq].append(course) # prereq -> course
            indegree[course] += 1
            
        # 将所有入度为 0 的课程加入队列
        queue = deque([i for i in range(numCourses) if indegree[i] == 0])
        
        # BFS
        count = 0
        while queue:
            curr_course = queue.popleft()
            count += 1
            
            # 遍历当前课程所有的后续课程
            for next_course in graph[curr_course]:
                indegree[next_course] -= 1 
                # 如果后续课程的入度为 0，则加入队列
                if indegree[next_course] == 0:
                    queue.append(next_course)
                    
        # 如果完成的课程数等于总课程数，说明可以完成所有课程
        return count == numCourses
    
    def permute(self, nums: List[int]) -> List[List[int]]:
        r"""
        给定一个不含重复数字的数组 nums ，返回其 所有可能的全排列 。你可以 按任意顺序 返回答案。
        """
        # 边界条件
        if not nums:
            return []

        result = []

        # 回溯算法
        def backtrack(curr_permu):
            # 递归终止条件：当前排列长度等于原来数组的长度
            if len(curr_permu) == len(nums):
                result.append(curr_permu[:])
                return
            
            # 尝试使用每个未使用的数字
            for num in nums:
                if num not in curr_permu:
                    # 做选择
                    curr_permu.append(num)
                    # 递归
                    backtrack(curr_permu)
                    # 撤销选择（回溯）
                    curr_permu.pop()
        
        backtrack([])
        return result



class TrieNode:
    def __init__(self):
        # 使用字典存储子节点，支持任意字符，节省空间
        self.children = {}
        # 标记该节点是否为某个单词的结尾
        self.is_end_of_word = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def _find_node(self, prefix: str) -> Optional[TrieNode]:
        """
        辅助方法：找到prefix对应的节点
        返回 None 如果 prefix 不存在
        """
        node = self.root
        
        for char in prefix:
            if char not in node.children:
                return None
            node = node.children[char]
        
        return node

    def insert(self, word: str) -> None:
        """插入一个单词到 Trie 树中"""
        if not word:
            return     
           
        node = self.root

        # 遍历单词中的每个字符
        for char in word:
            # 如果子节点不存在，创建新节点
            if char not in node.children:
                node.children[char] = TrieNode()
                
            # 移动到子节点
            node = node.children[char]

        # 如果是新单词，更新计数
        node.is_end_of_word = True

    def search(self, word: str) -> bool:
        """搜索字符串 word 是否在 Trie 树中"""
        if not word:
            return False

        node = self._find_node(word)
        return node is not None and node.is_end_of_word

    def startsWith(self, prefix: str) -> bool:
        """判断是否存在以prefix为前缀的字符串"""
        if not prefix:
            return True
            
        node = self._find_node(prefix)
        return node is not None
