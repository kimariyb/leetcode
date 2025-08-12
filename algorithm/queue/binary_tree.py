"""
问题描述：

给定一个二叉树，返回其按层次遍历的节点值（即逐层从左到右遍历）。
"""
from typing import List
from collections import deque


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        
        
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        # 边界条件
        if not root:
            return []

        # 初始化队列
        queue = deque([root])
        res = []

        while queue:
            # 当前层的节点数
            size = len(queue)
            # 存储当前层的节点值
            level = []
            for _ in range(size):
                # 弹出当前层的节点
                node = queue.popleft()
                # 将当前节点的值加入当前层的节点值列表
                level.append(node.val)
                
                # 将当前节点的左右子节点加入队列
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                    
            # 将当前层的节点值列表加入结果列表
            res.append(level)
            
        return res
    

if __name__ == "__main__":
    # 构造二叉树
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)

    # 测试
    solution = Solution()
    print(solution.levelOrder(root))  # 输出: [[3], [9, 20], [15, 7]]