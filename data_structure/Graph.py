"""
图表是一组对象的图形表示，其中一些对象对通过边连接。
相互连接的对象由称为顶点的点表示，连接顶点的链接称为边。

根据边是否具有方向性，图可以分为两种类型：「无向图」和「有向图」。
无向图（Undirected Graph）：如果图中每条边都没有方向性，则称为无向图。
例如，表示朋友关系或者城市间双向行驶的路线图常用无向图建模。

有向图（Directed Graph）：如果图中的每条边都具有方向性，则称为有向图。
例如，表示任务流程的流程图或网络请求的依赖图是典型的有向图。

稠密图（Dense Graph）：有很多条边或弧（边的条数 e 接近于完全图的边数）的图称为稠密图。
稀疏图（Sparse Graph）：有很少条边或弧（边的条数 e 远小于完全图的边数）的图称为稀疏图。

=== 无向图测试 ===
Vertices: 1, 2, 3, 4

Edges:
  1 -- 2 (weight: 5)
  1 -- 4 (weight: 10)
  2 -- 3 (weight: 3)
  3 -- 4 (weight: 2)
BFS从1开始: [1, 2, 4, 3]
DFS从1开始: [1, 2, 3, 4]
从1的最短路径: {1: 0, 2: 5, 3: 8, 4: 10}

=== 有向图测试 ===
Vertices: 1, 2, 3, 4

Edges:
  1 -> 2 (weight: 1)
  1 -> 4 (weight: 1)
  2 -> 3 (weight: 1)
  3 -> 4 (weight: 1)
拓扑排序: [1, 2, 3, 4]
从1的最短路径: {1: 0, 2: 1, 3: 2, 4: 1}

有环图的拓扑排序: None
"""
from typing import Optional, Dict, List, Set, Tuple
from collections import deque

import heapq


class Graph:
    def __init__(self):
        """图的基类，使用邻接表存储"""
        self.adj_list: Dict[int, Dict[int, int]] = {}  # {顶点: {邻居: 权重}}
        self.vertices: Set[int] = set()                # 所有顶点集合

    def add_vertex(self, v: int) -> None:
        """添加顶点"""
        if v not in self.vertices:
            self.vertices.add(v)
            self.adj_list[v] = {}

    def remove_vertex(self, v: int) -> None:
        """删除顶点及其所有边"""
        if v in self.vertices:
            # 先删除其他顶点指向它的边
            for neighbor in list(self.adj_list[v].keys()):
                self.remove_edge(v, neighbor)
            # 再删除该顶点
            del self.adj_list[v]
            self.vertices.remove(v)

    def add_edge(self, u: int, v: int, weight: int = 1) -> None:
        """添加边（由子类实现具体逻辑）"""
        raise NotImplementedError

    def remove_edge(self, u: int, v: int) -> None:
        """删除边（由子类实现具体逻辑）"""
        raise NotImplementedError

    def get_neighbors(self, v: int) -> Dict[int, int]:
        """获取顶点的邻居及其权重"""
        return self.adj_list.get(v, {})

    def get_vertices(self) -> List[int]:
        """获取所有顶点"""
        return list(self.vertices)

    def get_edges(self) -> List[Tuple[int, int, int]]:
        """获取所有边及其权重"""
        edges = []
        for u in self.adj_list:
            for v, weight in self.adj_list[u].items():
                edges.append((u, v, weight))
        return edges

    def bfs(self, start: int) -> List[int]:
        """广度优先搜索"""
        visited = []
        queue = deque([start])
        visited_set = {start}

        while queue:
            vertex = queue.popleft()
            visited.append(vertex)
            for neighbor in self.get_neighbors(vertex).keys():
                if neighbor not in visited_set:
                    visited_set.add(neighbor)
                    queue.append(neighbor)
        return visited

    def dfs(self, start: int) -> List[int]:
        """深度优先搜索"""
        visited = []
        self._dfs_helper(start, set(), visited)
        return visited

    def _dfs_helper(self, vertex: int, visited_set: Set[int], visited: List[int]) -> None:
        """DFS递归辅助函数"""
        visited.append(vertex)
        visited_set.add(vertex)
        for neighbor in self.get_neighbors(vertex).keys():
            if neighbor not in visited_set:
                self._dfs_helper(neighbor, visited_set, visited)

    def dijkstra(self, start: int) -> Dict[int, float]:
        """Dijkstra 算法求单源最短路径（仅适用于非负权重）"""
        distances = {v: float('infinity') for v in self.vertices}
        distances[start] = 0
        priority_queue = [(0, start)]

        while priority_queue:
            current_distance, current_vertex = heapq.heappop(priority_queue)

            if current_distance > distances[current_vertex]:
                continue

            for neighbor, weight in self.get_neighbors(current_vertex).items():
                distance = current_distance + weight
                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    heapq.heappush(priority_queue, (distance, neighbor))

        return distances

    def visualize(self) -> str:
        """更简洁美观的可视化展示"""
        result = ["Vertices: " + ", ".join(map(str, sorted(self.vertices)))]

        # 边列表（无向图会自动合并双向边）
        edges = self._get_unique_edges()
        if edges:
            result.append("\nEdges:")
            for u, v, weight in sorted(edges):
                arrow = "--" if isinstance(self, UndirectedGraph) else "->"
                result.append(f"  {u} {arrow} {v} (weight: {weight})")

        return "\n".join(result)

    def _get_unique_edges(self) -> List[Tuple[int, int, int]]:
        """获取唯一边表示（无向图自动合并双向边）"""
        edges = set()
        for u in self.adj_list:
            for v, weight in self.adj_list[u].items():
                if isinstance(self, UndirectedGraph):
                    edge = tuple(sorted((u, v))) + (weight,)
                else:
                    edge = (u, v, weight)
                edges.add(edge)
        return sorted(edges)

    def __str__(self) -> str:
        return self.visualize()


class UndirectedGraph(Graph):
    """无向图（边是双向的）"""
    def add_edge(self, u: int, v: int, weight: int = 1) -> None:
        """添加无向边"""
        self.add_vertex(u)
        self.add_vertex(v)
        self.adj_list[u][v] = weight
        self.adj_list[v][u] = weight

    def remove_edge(self, u: int, v: int) -> None:
        """删除无向边"""
        if u in self.adj_list and v in self.adj_list[u]:
            del self.adj_list[u][v]
            del self.adj_list[v][u]


class DirectedGraph(Graph):
    """有向图（边是单向的）"""
    def add_edge(self, u: int, v: int, weight: int = 1) -> None:
        """添加有向边"""
        self.add_vertex(u)
        self.add_vertex(v)
        self.adj_list[u][v] = weight

    def remove_edge(self, u: int, v: int) -> None:
        """删除有向边"""
        if u in self.adj_list and v in self.adj_list[u]:
            del self.adj_list[u][v]

    def topological_sort(self) -> Optional[List[int]]:
        """拓扑排序（仅适用于有向无环图）"""
        in_degree = {v: 0 for v in self.vertices}
        # 计算入度
        for u in self.adj_list:
            for v in self.adj_list[u]:
                in_degree[v] += 1

        # 初始化队列（入度为0的顶点）
        queue = deque([v for v in self.vertices if in_degree[v] == 0])
        topo_order = []

        while queue:
            u = queue.popleft()
            topo_order.append(u)
            # 减少邻居的入度
            for v in self.get_neighbors(u).keys():
                in_degree[v] -= 1
                if in_degree[v] == 0:
                    queue.append(v)

        if len(topo_order) == len(self.vertices):
            return topo_order
        return None  # 存在环


# 测试代码
if __name__ == "__main__":
    print("=== 无向图测试 ===")
    ug = UndirectedGraph()
    ug.add_edge(1, 2, 5)
    ug.add_edge(2, 3, 3)
    ug.add_edge(3, 4, 2)
    ug.add_edge(1, 4, 10)
    print(ug)
    print("BFS从1开始:", ug.bfs(1))
    print("DFS从1开始:", ug.dfs(1))
    print("从1的最短路径:", ug.dijkstra(1))

    print("\n=== 有向图测试 ===")
    dg = DirectedGraph()
    dg.add_edge(1, 2)
    dg.add_edge(2, 3)
    dg.add_edge(3, 4)
    dg.add_edge(1, 4)
    print(dg)
    print("拓扑排序:", dg.topological_sort())
    print("从1的最短路径:", dg.dijkstra(1))

    # 测试有向图的环检测
    dg_with_cycle = DirectedGraph()
    dg_with_cycle.add_edge(1, 2)
    dg_with_cycle.add_edge(2, 3)
    dg_with_cycle.add_edge(3, 1)
    print("\n有环图的拓扑排序:", dg_with_cycle.topological_sort())  # 应返回None