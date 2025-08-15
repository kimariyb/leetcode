# Definition for a binary tree node.
from collections import defaultdict
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

        
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        r"""
        给你二叉树的根结点 root ，请你将它展开为一个单链表：

        展开后的单链表应该同样使用 TreeNode ，其中 right 子指针指向链表中下一个结点，而左子指针始终为 null 。
        展开后的单链表应该与二叉树 先序遍历 顺序相同。
        """
        if not root:
            return
        
        # 递归展开左右子树
        self.flatten(root.left)
        self.flatten(root.right)
        
        # 保存右子树
        right_subtree = root.right
        
        # 将左子树移到右边
        if root.left:
            root.right = root.left
            root.left = None
            
            # 找到左子树的最右节点
            current = root.right
            while current.right:
                current = current.right
            
            # 将原来的右子树接在后面
            current.right = right_subtree

    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        r"""
        给定两个整数数组 preorder 和 inorder ，其中 preorder 是二叉树的先序遍历， 
        inorder 是同一棵树的中序遍历，请构造二叉树并返回其根节点。
        """
        # 创建中序遍历值到索引的映射
        inorder_map = {val: idx for idx, val in enumerate(inorder)}
        
        # 边界条件
        if not preorder or not inorder:
            return None

        def buildTreeHelper(pre_start, pre_end, in_start, in_end):
            """用于递归构建二叉树"""
            if pre_start > pre_end or in_start > in_end:
                return None

            # 根节点值
            root_val = preorder[pre_start]
            root = TreeNode(root_val)

            # 根节点在中序遍历中的索引
            root_idx = inorder_map[root_val]

            # 左子树节点个数
            left_size = root_idx - in_start

            # 递归构建左子树和右子树
            root.left = buildTreeHelper(pre_start + 1, pre_start + left_size, in_start, root_idx - 1)
            root.right = buildTreeHelper(pre_start + left_size + 1, pre_end, root_idx + 1, in_end)

            return root

        # 构建二叉树
        return buildTreeHelper(0, len(preorder) - 1, 0, len(inorder) - 1)


    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        r"""
        给定一个二叉树的根节点 root ，和一个整数 targetSum ，
        求该二叉树里节点值之和等于 targetSum 的 路径 的数目。

        路径 不需要从根节点开始，也不需要在叶子节点结束，但是路径方向必须是向下的（只能从父节点到子节点）。
        """
        # 边界条件
        if not root:
            return 0
        
        # 哈希表存储前缀和及其出现次数
        prefix_sum_count = defaultdict(int)
        prefix_sum_count[0] = 1  # 初始化，前缀和为0出现1次

        def dfs(node: TreeNode, curr_sum: int) -> int:
            if not node:
                return 0

            # 当前路径和
            curr_sum += node.val

            # 计算路径数
            count = prefix_sum_count[curr_sum - targetSum]

            # 更新当前前缀和的计数
            prefix_sum_count[curr_sum] += 1

            # 递归计算左右子树的路径数
            count += dfs(node.left, curr_sum)
            count += dfs(node.right, curr_sum)

            # 回溯，恢复当前前缀和的计数
            prefix_sum_count[curr_sum] -= 1

            return count

        # 从根节点开始DFS
        return dfs(root, 0)
    
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        r"""
        给定一个二叉树, 找到该树中两个指定节点的最近公共祖先。

        百度百科中最近公共祖先的定义为：“对于有根树 T 的两个节点 p、q，最近公共祖先表示为一个节点 x，
        满足 x 是 p、q 的祖先且 x 的深度尽可能大（一个节点也可以是它自己的祖先）。”
        """
        # 边界条件
        if not root or root == p or root == q:
            return root
        
        # 递归查找左子树和右子树
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)

        # 如果左右子树都找到了 p 或 q，说明当前节点就是最近公共祖先
        if left and right:
            return root

        # 否则返回找到的那个节点
        return left if left else right


    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        r"""
        二叉树中的 路径 被定义为一条节点序列，序列中每对相邻节点之间都存在一条边。
        同一个节点在一条路径序列中 至多出现一次 。该路径 至少包含一个 节点，且不一定经过根节点。

        路径和 是路径中各节点值的总和。

        给你一个二叉树的根节点 root ，返回其 最大路径和 。
        """
        # 边界条件
        if not root:
            return 0

        # 初始化最大路径和
        self.max_sum = float('-inf')

        def dfs(node: TreeNode) -> int:
            if not node:
                return 0
            
            left_gain = max(dfs(node.left), 0)
            right_gain = max(dfs(node.right), 0)

            # 更新全局最大值
            curr_sum = node.val + left_gain + right_gain
            self.max_sum = max(self.max_sum, curr_sum)

            # 返回当前节点的最大贡献值
            return node.val + max(left_gain, right_gain)

        # 从根节点开始DFS
        dfs(root)
        return self.max_sum