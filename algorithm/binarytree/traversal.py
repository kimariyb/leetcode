"""
问题描述：

请分别实现二叉树的前序、中序、后序和层序遍历
"""
from collections import deque
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        

class Solution:
    def preOrder(self, root: Optional[TreeNode]) -> List[int]:
        """前序遍历"""
        # 边界条件
        if not root:
            return []
        
        # 递归
        return [root.val] + self.preOrder(root.left) + self.preOrder(root.right)

    def inOrder(self, root: Optional[TreeNode]) -> List[int]:
        """中序遍历"""
        # 边界条件
        if not root:
            return []

        # 递归
        return self.inOrder(root.left) + [root.val] + self.inOrder(root.right)

    def postOrder(self, root: Optional[TreeNode]) -> List[int]:
        """后序遍历"""
        # 边界条件
        if not root:
            return []

        # 递归
        return self.postOrder(root.left) + self.postOrder(root.right) + [root.val]
    
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        """层序遍历"""
        # 边界条件
        if not root:
            return []

        # 层序遍历
        res = []
        queue = deque([root])

        while queue:
            # 获取当前层的节点数量
            size = len(queue)
            # 存储当前层的节点值
            level = []
            for _ in range(size):
                # 从队列中取出一个节点
                node = queue.popleft()
                # 将节点值加入当前层
                level.append(node.val)
                # 将左子节点加入队列
                if node.left:
                    queue.append(node.left)
                # 将右子节点加入队列
                if node.right:
                    queue.append(node.right)
            # 将当前层加入结果
            res.append(level)

        return res
            