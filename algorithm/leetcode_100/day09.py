from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        r"""
        给定一个二叉树的根节点 root ，返回 它的 中序 遍历 。
        """
        # 边界条件
        if not root:
            return []
        
        # 递归 左 -> 根 -> 右
        return (
            self.inorderTraversal(root.left)
            + [root.val] + self.inorderTraversal(root.right)
        )

    def maxDepth(self, root: Optional[TreeNode]) -> int:
        r"""
        给定一个二叉树 root ，返回其最大深度。

        二叉树的 最大深度 是指从根节点到最远叶子节点的最长路径上的节点数。
        """
        # 边界条件
        if not root:
            return 0
        
        # 递归计算左右两子树的深度
        left_depth = self.maxDepth(root.left)
        right_depth = self.maxDepth(root.right)

        # 最大的深度
        return max(left_depth, right_depth) + 1
    
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        r"""
        给你一棵二叉树的根节点 root ，翻转这棵二叉树，并返回其根节点。
        """
        # 边界条件
        if not root:
            return root

        # 递归交换左右子树
        root.left, root.right = self.invertTree(root.right), self.invertTree(root.left)

        return root
    
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        r"""
        给你一个二叉树的根节点 root ， 检查它是否轴对称。
        """
        # 边界条件
        if not root:
            return True

        def isMirror(left: Optional[TreeNode], right: Optional[TreeNode]) -> bool:
            # 递归终止条件
            if not left and not right:
                return True
            if not left or not right:
                return False

            # 递归判断左右子树是否对称
            return (
                left.val == right.val
                and isMirror(left.left, right.right)
                and isMirror(left.right, right.left)
            )
        
        # 递归判断左右子树是否对称
        return isMirror(root.left, root.right)
    
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        r"""
        给你一棵二叉树的根节点，返回该树的 直径 。

        二叉树的 直径 是指树中任意两个节点之间最长路径的 长度 。
        这条路径可能经过也可能不经过根节点 root 。

        两节点之间路径的 长度 由它们之间边数表示。
        """
        # 边界条件
        if not root:
            return 0
        
        self.max_diameter = 0
        
        # 使用 DFS 计算左右子树的深度，并更新最大直径
        def dfs(node: Optional[TreeNode]) -> int:
            if not node:
                return 0

            left_depth = dfs(node.left)
            right_depth = dfs(node.right)

            # 更新最大直径
            self.max_diameter = max(self.max_diameter, left_depth + right_depth)

            return max(left_depth, right_depth) + 1

        dfs(root)
        return self.max_diameter