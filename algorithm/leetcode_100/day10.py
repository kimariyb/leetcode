from collections import deque
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        r"""
        给你二叉树的根节点 root ，返回其节点值的 层序遍历 。 
        （即逐层地，从左到右访问所有节点）。
        """
        # 边界条件
        if not root:
            return []
        
        # 初始化
        res = []
        queue = [root]

        # 遍历
        while queue:
            # 获取当前层的节点数
            size = len(queue)
            # 保存当前层的节点值
            level = []
            # 遍历当前层的节点
            for _ in range(size):
                # 弹出当前层的节点
                node = queue.pop(0)
                # 将当前层的节点值加入level
                level.append(node.val)
                # 将当前层的节点的左右子节点加入queue
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            # 将当前层的节点值加入res
            res.append(level)
        return res
    
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        r"""
        给你一个整数数组 nums ，其中元素已经按 升序 排列，
        请你将其转换为一棵 平衡 二叉搜索树。
        """
        # 边界条件
        if not nums:
            return None
        
        mid = len(nums) // 2
        root = TreeNode(nums[mid])

        root.left = self.sortedArrayToBST(nums[:mid])
        root.right = self.sortedArrayToBST(nums[mid + 1:])

        return root
    
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        r"""
        给你一个二叉树的根节点 root ，判断其是否是一个有效的二叉搜索树。

        有效 二叉搜索树定义如下：

        - 节点的左子树只包含 严格小于 当前节点的数。
        - 节点的右子树只包含 严格大于 当前节点的数。
        - 所有左子树和右子树自身必须也是二叉搜索树。
        """
        # BST的中序遍历结果应该是严格递增的序列。
        def inOrder(node: Optional[TreeNode]):
            if not node:
                return []
            return (
                inOrder(node.left) 
                + [node.val]
                + inOrder(node.right)
            )
        
        vals = inOrder(root)
        # 检查 vals 是否严格递增
        for i in range(1, len(vals)):
            if vals[i] <= vals[i - 1]:
                return False
        return True
    
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        r"""
        给定一个二叉搜索树的根节点 root ，和一个整数 k ，
        请你设计一个算法查找其中第 k 小的元素（从 1 开始计数）。
        """
        # BST的中序遍历结果应该是严格递增的序列。
        def inOrder(node: Optional[TreeNode]):
            if not node:
                return []
            return (
                inOrder(node.left) 
                + [node.val]
                + inOrder(node.right)
            )

        # 边界条件
        if not root:
            return 0
        
        # 调用中序遍历函数
        vals = inOrder(root)
        # 返回第 k 小的元素
        return vals[k - 1]

    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
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