from collections import defaultdict, deque
from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        r"""
        给定一个二叉树的 根节点 root，想象自己站在它的右侧，
        按照从顶部到底部的顺序，返回从右侧所能看到的节点值。
        """
        # 边界条件
        if not root:
            return []
        
        res = []
        dq = deque([root])

        while dq:
            level_size = len(dq)
            # 遍历当前层的所有节点
            for i in range(level_size):
                node = dq.popleft()
                # 如果是当前层的最后一个节点（最右侧），加入结果
                if i == level_size - 1:
                    res.append(node.val)
                # 将当前节点的左右子节点加入队列
                if node.left:
                    dq.append(node.left)
                if node.right:
                    dq.append(node.right)

        return res

    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        r"""
        给你一个二叉树的根节点 root。设根节点位于二叉树的第 1 层，
        而根节点的子节点位于第 2 层，依此类推。

        请返回层内元素之和 最大 的那几层（可能只有一层）的层号，并返回其中 最小 的那个。
        """
        # 边界条件
        if not root:
            return 0

        res = []
        dq = deque([root])

        while dq:
            level_size = len(dq)
            level_sum = 0
            # 遍历当前层的所有节点
            for i in range(level_size):
                node = dq.popleft()
                # 计算当前层的节点和
                level_sum += node.val
                # 将当前节点的左右子节点加入队列
                if node.left:
                    dq.append(node.left)
                if node.right:
                    dq.append(node.right)
            # 将当前层的节点和加入结果
            res.append(level_sum)

        # 找到节点和最大的层
        max_sum = max(res)
        # 找到节点和最大的层中最小的层号
        return res.index(max_sum) + 1
    
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        r"""
        有 n 个房间，房间按从 0 到 n - 1 编号。
        最初，除 0 号房间外的其余所有房间都被锁住。你的目标是进入所有的房间。、
        然而，你不能在没有获得钥匙的时候进入锁住的房间。

        当你进入一个房间，你可能会在里面找到一套 不同的钥匙，每把钥匙上都有对应的房间号，
        即表示钥匙可以打开的房间。你可以拿上所有钥匙去解锁其他房间。

        给你一个数组 rooms 其中 rooms[i] 是你进入 i 号房间可以获得的钥匙集合。
        如果能进入 所有 房间返回 true，否则返回 false。
        """
        # 边界条件
        if not rooms:
            return False
        
        # 记录已访问的房间
        visited = set()

        def dfs(room):
            # 标记当前房间为已访问
            visited.add(room)

            # 遍历当前房间的所有钥匙
            for key in rooms[room]:
                # 如果钥匙对应的房间未访问，则继续访问
                if key not in visited:
                    dfs(key)
        
        dfs(0)
        return len(visited) == len(rooms)
    
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        r"""
        有 n 个城市，其中一些彼此相连，另一些没有相连。
        如果城市 a 与城市 b 直接相连，且城市 b 与城市 c 直接相连
        那么城市 a 与城市 c 间接相连。

        省份 是一组直接或间接相连的城市，组内不含其他没有相连的城市。

        给你一个 n x n 的矩阵 isConnected ，
        其中 isConnected[i][j] = 1 表示第 i 个城市和第 j 个城市直接相连，
        而 isConnected[i][j] = 0 表示二者不直接相连。

        返回矩阵中 省份 的数量。
        """
        # 边界条件
        if not isConnected:
            return 0
        
        n = len(isConnected)
        # 记录已访问的城市
        visited = [False] * n
        provinces = 0

        def dfs(city):
            # 标记当前城市为已访问
            visited[city] = True

            # 遍历当前城市的所有邻居城市
            for neighbor in range(n):
                # 如果邻居城市未访问，则继续访问
                if isConnected[city][neighbor] == 1 and not visited[neighbor]:
                    dfs(neighbor)
        
        for i in range(n):
            # 如果当前城市未访问，则说明找到了一个新的省份
            if not visited[i]:
                dfs(i)
                provinces += 1

        return provinces    
    
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        r"""
        n 座城市，从 0 到 n-1 编号，其间共有 n-1 条路线。
        因此，要想在两座不同城市之间旅行只有唯一一条路线可供选择（路线网形成一颗树）。
        去年，交通运输部决定重新规划路线，以改变交通拥堵的状况。

        路线用 connections 表示，其中 connections[i] = [a, b] 表示从城市 a 到 b 的一条有向路线。

        今年，城市 0 将会举办一场大型比赛，很多游客都想前往城市 0 。

        请你帮助重新规划路线方向，使每个城市都可以访问城市 0 。返回需要变更方向的最小路线数。

        题目数据 保证 每个城市在重新规划路线方向后都能到达城市 0 。
        """
        # 边界条件
        if not connections:
            return 0
        
        # 记录已访问的城市
        visited = set()
        changes = 0

        # 构建 adj matrix 
        adj_graph = defaultdict(list)

        for a, b in connections:
            # 正向边标记为 1，反向边标记为 0
            adj_graph[a].append((b, 1))
            adj_graph[b].append((a, 0))

        def dfs(node):
            nonlocal changes
            visited.add(node)

            for neighbor, direction in adj_graph[node]:
                if neighbor not in visited:
                    changes += direction  # 如果是原始方向边，需要反转
                    dfs(neighbor)
                    
        dfs(0)
        return changes
