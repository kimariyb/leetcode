"""
问题描述：

给定一个二叉树，判断其是否是一个有效的二叉搜索树。
"""
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(node, lower=float('-inf'), upper=float('inf')):
            """通过递归判断二叉树是否是二叉搜索树"""
            if not node:
                return True

            # 如果当前节点的值不在合法范围内，则不是二叉搜索树
            val = node.val
            if val <= lower or val >= upper:
                return False

            # 递归判断左子树和右子树
            # 左子树的值一定要小于当前节点的值，
            # 右子树的值一定要大于当前节点的值
            return dfs(node.left, lower, val) and dfs(node.right, val, upper)

        return dfs(root)