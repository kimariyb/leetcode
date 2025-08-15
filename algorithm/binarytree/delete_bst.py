"""
问题描述：

删除二叉搜索树的指定节点。返回删除之后的根节点。
"""
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        

class Solution:
    def deleteNode(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        # 边界条件
        if not root:
            return None
        # 如果这个值比根节点小，则从左子树删除
        if val < root.val:
            root.left = self.deleteNode(root.left, val)
        # 如果这个值比根节点大，则从右子树删除
        elif val > root.val:
            root.right = self.deleteNode(root.right, val)
        else:
            # 找到要删除的节点
            if not root.left:
                return root.right
            elif not root.right:
                return root.left
            else:
                # 左右子树都不为空，找到右子树的最小节点
                successor = root.right
                while successor.left:
                    successor = successor.left
                # 用后继节点的值替换当前节点
                root.val = successor.val
                # 删除后继节点
                root.right = self.deleteNode(root.right, successor.val)
        
        return root

        
        