"""
并查集是一种用于管理元素所属集合的数据结构，实现为一个森林，其中每棵树表示一个集合，树中的节点表示对应集合中的元素。

顾名思义，并查集支持两种操作：

- 合并（Union）：合并两个元素所属集合（合并对应的树）
- 查询（Find）：查询某个元素所属集合（查询对应的树的根节点），这可以用于判断两个元素是否属于同一集合

=== 并查集测试 ===
初始集合数量: 5

合并0和1:
集合数量: 4
0和1是否连通: True
0和2是否连通: False

合并1和2:
集合数量: 3
0和2现在是否连通: True

尝试重复合并1和2:
合并结果: False

合并3和4:
集合数量: 2

合并2和3:
最终集合数量: 1
所有元素是否连通: True
"""


class DSU:
    """并查集类 (Disjoint Set Union)"""
    def __init__(self, n: int):
        """
        初始化并查集
        :param n: 元素数量 (元素编号从0到n-1)
        """
        self.parent = list(range(n))  # 父节点数组，初始时每个元素的父节点是自己
        self.rank = [0] * n  # 秩数组（树高度的上界）
        self.set_count = n  # 当前集合数量（初始时每个元素独立为一个集合）

    def find(self, x: int) -> int:
        """
        查找元素x的根节点（代表元），包含路径压缩优化
        :param x: 要查找的元素
        :return: 根节点
        """
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])  # 路径压缩：将x的父节点直接指向根
        return self.parent[x]

    def union(self, x: int, y: int) -> bool:
        """
        合并x和y所在的集合，按秩合并优化
        :param x: 元素x
        :param y: 元素y
        :return: 如果x和y原本不在同一集合则返回True，否则返回False
        """
        x_root, y_root = self.find(x), self.find(y)
        if x_root == y_root:
            return False  # 已经在同一集合中，无需合并

        # 按秩合并：将小树合并到大树下
        if self.rank[x_root] < self.rank[y_root]:
            x_root, y_root = y_root, x_root  # 保证x_root的秩较大

        self.parent[y_root] = x_root
        if self.rank[x_root] == self.rank[y_root]:
            self.rank[x_root] += 1  # 若两树高度相同，合并后高度+1

        self.set_count -= 1  # 集合数量减少
        return True

    def is_connected(self, x: int, y: int) -> bool:
        """
        判断x和y是否属于同一集合
        :param x: 元素x
        :param y: 元素y
        :return: 是否连通
        """
        return self.find(x) == self.find(y)

    def get_set_count(self) -> int:
        """
        获取当前集合的数量
        :return: 集合数量
        """
        return self.set_count

    def get_set_size(self, x: int) -> int:
        """
        获取x所在集合的大小（需要额外遍历，时间复杂度O(n)）
        :param x: 元素x
        :return: 集合大小
        """
        root = self.find(x)
        return sum(1 for i in range(len(self.parent)) if self.find(i) == root)


if __name__ == "__main__":
    print("=== 并查集测试 ===")
    n = 5  # 假设有5个元素（0-4）
    dsu = DSU(n)

    print(f"初始集合数量: {dsu.get_set_count()}")  # 5

    # 合并操作
    print("\n合并0和1:")
    dsu.union(0, 1)
    print(f"集合数量: {dsu.get_set_count()}")  # 4
    print(f"0 和 1 是否连通: {dsu.is_connected(0, 1)}")  # True
    print(f"0 和 2 是否连通: {dsu.is_connected(0, 2)}")  # False

    print("\n合并1和2:")
    dsu.union(1, 2)
    print(f"集合数量: {dsu.get_set_count()}")  # 3
    print(f"0和2现在是否连通: {dsu.is_connected(0, 2)}")  # True

    print("\n尝试重复合并1和2:")
    print(f"合并结果: {dsu.union(1, 2)}")  # False（已连通）

    print("\n合并3和4:")
    dsu.union(3, 4)
    print(f"集合数量: {dsu.get_set_count()}")  # 2

    print("\n合并2和3:")
    dsu.union(2, 3)
    print(f"最终集合数量: {dsu.get_set_count()}")  # 1
    print(f"所有元素是否连通: {all(dsu.is_connected(0, i) for i in range(n))}")  # True