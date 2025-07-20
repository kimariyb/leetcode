"""
树表示由边连接的节点。它是一种非线性数据结构。它具有以下属性

- 一个节点被标记为根节点。
- 除根节点之外的每个节点都与一个父节点相关联。
- 每个节点都可以有一个任意数量的子节点。

二叉搜索树 (BST) 是一种二叉树的树形数据结构，其定义如下：

- 空树是二叉搜索树。
- 若二叉搜索树的左子树不为空，则其左子树上所有点的附加权值均小于其根节点的值。
- 若二叉搜索树的右子树不为空，则其右子树上所有点的附加权值均大于其根节点的值。
- 二叉搜索树的左右子树均为二叉搜索树。

二叉搜索树上的基本操作所花费的时间与这棵树的高度成正比。
对于一个有 n 个结点的二叉搜索树中，这些操作的最优时间复杂度为 O(log n)，最坏为 O(n)。
随机构造这样一棵二叉搜索树的期望高度为 O(log n)。

前序遍历 (栈)
中序遍历 (栈)
后序遍历 (栈)
层次遍历 (队列）
"""
from typing import Optional, List


class BinaryTreeNode(object):
    def __init__(self, data):
        self.data = data
        self.left: Optional[BinaryTreeNode] = None
        self.right: Optional[BinaryTreeNode] = None


class BinaryTree(object):
    def __init__(self, root: Optional[BinaryTreeNode] = None):
        self.root = root
        self.size = self._count_nodes(root) if root else 0

    def __str__(self):
        """返回树的可视化字符串表示"""
        if not self.root:
            return "Empty Tree"

        # 选择你喜欢的可视化方式
        return self._visualize_tree()  # 水平缩进风格

    def _visualize_tree(self) -> str:
        """水平缩进风格的可视化"""
        lines = []
        self._build_tree_visualization(self.root, 0, lines, "ROOT: ")
        return "\n".join(lines)

    def _build_tree_visualization(
        self, node: Optional[BinaryTreeNode],
        level: int,
        lines: List[str],
        prefix: str
    ) -> None:
        if node is not None:
            lines.append(" " * (level * 4) + prefix + str(node.data))
            if node.left or node.right:
                self._build_tree_visualization(
                    node.left, level + 1, lines, "L--- ")
                self._build_tree_visualization(
                    node.right, level + 1, lines, "R--- ")

    def _count_nodes(self, node: Optional[BinaryTreeNode]) -> int:
        """递归计算节点数量"""
        if node is None:
            return 0
        return 1 + self._count_nodes(node.left) + self._count_nodes(node.right)

    def preorder(self) -> List:
        """前序遍历：根->左->右"""
        return self._preorder_helper(self.root)

    def _preorder_helper(self, node: Optional[BinaryTreeNode]) -> List:
        if node is None:
            return []
        return [node.data] + self._preorder_helper(node.left) + self._preorder_helper(node.right)

    def inorder(self) -> List:
        """中序遍历：左->根->右"""
        return self._inorder_helper(self.root)

    def _inorder_helper(self, node: Optional[BinaryTreeNode]) -> List:
        if node is None:
            return []
        return self._inorder_helper(node.left) + [node.data] + self._inorder_helper(node.right)

    def postorder(self) -> List:
        """后序遍历：左->右->根"""
        return self._postorder_helper(self.root)

    def _postorder_helper(self, node: Optional[BinaryTreeNode]) -> List:
        if node is None:
            return []
        return self._postorder_helper(node.left) + self._postorder_helper(node.right) + [node.data]

    def level_order(self) -> List:
        """层序遍历"""
        if not self.root:
            return []

        result = []
        queue = [self.root]

        while queue:
            node = queue.pop(0)
            result.append(node.data)

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        return result

    def height(self) -> int:
        """计算树的高度"""
        return self._height_helper(self.root)

    def _height_helper(self, node: Optional[BinaryTreeNode]) -> int:
        if node is None:
            return 0
        return 1 + max(self._height_helper(node.left), self._height_helper(node.right))

    def insert_left(self, parent: Optional[BinaryTreeNode], data) -> bool:
        """在指定节点的左侧插入节点"""
        if parent is None:
            return False

        new_node = BinaryTreeNode(data)
        if parent.left:
            new_node.left = parent.left
        parent.left = new_node
        self.size += 1
        return True

    def insert_right(self, parent: Optional[BinaryTreeNode], data) -> bool:
        """在指定节点的右侧插入节点"""
        if parent is None:
            return False

        new_node = BinaryTreeNode(data)
        if parent.right:
            new_node.right = parent.right
        parent.right = new_node
        self.size += 1
        return True


class BinarySearchTree(BinaryTree):
    def __init__(self, root: Optional[BinaryTreeNode] = None):
        super().__init__(root)

    def search(self, val) -> bool:
        """在BST中搜索值"""
        return self._search_helper(self.root, val)

    def _search_helper(self, node: Optional[BinaryTreeNode], val) -> bool:
        """递归搜索辅助函数"""
        if node is None:
            return False
        if val == node.data:
            return True
        elif val < node.data:
            return self._search_helper(node.left, val)
        else:
            return self._search_helper(node.right, val)

    def insert(self, val) -> None:
        """向BST插入新值"""
        if self.root is None:
            self.root = BinaryTreeNode(val)
            self.size += 1
        else:
            self._insert_helper(self.root, val)

    def _insert_helper(self, node: BinaryTreeNode, val) -> None:
        """递归插入辅助函数"""
        if val < node.data:
            if node.left is None:
                node.left = BinaryTreeNode(val)
                self.size += 1
            else:
                self._insert_helper(node.left, val)
        elif val > node.data:
            if node.right is None:
                node.right = BinaryTreeNode(val)
                self.size += 1
            else:
                self._insert_helper(node.right, val)


    def delete(self, val) -> bool:
        """从BST删除值，返回是否成功删除"""
        self.root, deleted = self._delete_helper(self.root, val)
        if deleted:
            self.size -= 1
        return deleted

    def _delete_helper(self, node: Optional[BinaryTreeNode], val) -> tuple:
        """递归删除辅助函数，返回(新节点, 是否删除)"""
        if node is None:
            return None, False

        if val < node.data:
            node.left, deleted = self._delete_helper(node.left, val)
            return node, deleted
        elif val > node.data:
            node.right, deleted = self._delete_helper(node.right, val)
            return node, deleted
        else:
            # 找到要删除的节点
            if node.left is None:  # 只有右子节点或没有子节点
                return node.right, True
            elif node.right is None:  # 只有左子节点
                return node.left, True
            else:  # 有两个子节点
                # 找到右子树的最小节点
                min_node = BinarySearchTree._find_min(node.right)
                # 用最小节点的值替换当前节点
                node.data = min_node.data
                # 删除右子树中的最小节点
                node.right, _ = self._delete_helper(node.right, min_node.data)
                return node, True

    @staticmethod
    def _find_min(node: BinaryTreeNode) -> BinaryTreeNode:
        """找到子树中的最小节点"""
        while node.left is not None:
            node = node.left
        return node

    def is_valid(self) -> bool:
        """检查是否是有效的BST"""
        return self._is_valid_helper(self.root, float('-inf'), float('inf'))

    def _is_valid_helper(self, node: Optional[BinaryTreeNode], min_val, max_val) -> bool:
        """递归验证BST有效性"""
        if node is None:
            return True
        if not min_val < node.data < max_val:
            return False
        return (self._is_valid_helper(node.left, min_val, node.data) and
                self._is_valid_helper(node.right, node.data, max_val))


if __name__ == '__main__':
    # 构建二叉树
    a = BinaryTreeNode('A')
    b = BinaryTreeNode('B')
    c = BinaryTreeNode('C')
    d = BinaryTreeNode('D')
    e = BinaryTreeNode('E')
    f = BinaryTreeNode('F')
    g = BinaryTreeNode('G')

    e.left = a
    e.right = g
    a.right = c
    c.left = b
    c.right = d
    g.right = f

    # 创建二叉树实例
    print("\n=== 二叉树测试 ===")
    tree = BinaryTree(e)
    print(f"树结构:\n{tree}")
    print("前序遍历:", tree.preorder())
    print("中序遍历:", tree.inorder())
    print("后序遍历:", tree.postorder())
    print("层序遍历:", tree.level_order())
    print("树高度:", tree.height())
    print("节点数:", tree.size)

    # 创建二叉搜索树实例
    print("\n=== 二叉搜索树测试 ===")
    bst = BinarySearchTree()
    nums = [50, 30, 70, 20, 40, 60, 80]
    for num in nums:
        bst.insert(num)

    print("初始BST:")
    print(f"树结构:\n{bst}")
    print("中序遍历:", bst.inorder())  # 应该是有序的
    print("搜索40:", bst.search(40))
    print("搜索90:", bst.search(90))

    # 测试删除
    print("\n删除节点测试:")
    print("删除20(叶子节点):", bst.delete(20))
    print(f"删除后树结构:\n{bst}")
    print("中序遍历:", bst.inorder())

    print("\n删除30(有一个子节点):", bst.delete(30))
    print(f"删除后树结构:\n{bst}")
    print("中序遍历:", bst.inorder())

    print("\n删除50(有两个子节点):", bst.delete(50))
    print(f"删除后树结构:\n{bst}")
    print("中序遍历:", bst.inorder())

    # 验证BST有效性
    print("\nBST有效性测试:")
    print("当前树是否有效BST:", bst.is_valid())

    # 创建一个无效的BST测试
    root = BinaryTreeNode(10)
    root.left = BinaryTreeNode(15)  # 左子节点大于根节点，无效
    invalid_bst = BinarySearchTree(root)
    print("无效BST是否有效:", invalid_bst.is_valid())