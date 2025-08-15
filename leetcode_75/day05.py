from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        r"""
        给你单链表的头节点 head ，请你反转链表，并返回反转后的链表。
        """
        # 边界条件
        if not head or not head.next:
            return head
        
        prev, curr = None, head

        while curr:
            # 保存下一个节点
            next_node = curr.next
            # 反转当前节点的指针
            curr.next = prev
            # 移动指针
            prev = curr
            curr = next_node

        return prev
    
    def pairSum(self, head: Optional[ListNode]) -> int:
        r"""
        在一个大小为 n 且 n 为 偶数 的链表中，对于 0 <= i <= (n / 2) - 1 的 i ，
        第 i 个节点（下标从 0 开始）的孪生节点为第 (n-1-i) 个节点 。

        比方说，n = 4 那么节点 0 是节点 3 的孪生节点，节点 1 是节点 2 的孪生节点。
        这是长度为 n = 4 的链表中所有的孪生节点。

        孪生和 定义为一个节点和它孪生节点两者值之和。

        给你一个长度为偶数的链表的头节点 head ，请你返回链表的 最大孪生和 
        """
        # 将链表转换为数组
        values = []
        current = head
        while current:
            values.append(current.val)
            current = current.next
        
        # 计算最大孪生和
        n = len(values)
        max_sum = 0

        # 对于每个孪生对
        for i in range(n // 2):
            twin_sum = values[i] + values[n - 1 - i]
            max_sum = max(max_sum, twin_sum)
        
        return max_sum
    
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        r"""
        给定一个二叉树 root ，返回其最大深度。

        二叉树的 最大深度 是指从根节点到最远叶子节点的最长路径上的节点数。
        """
        if not root:
            return 0

        left_depth = self.maxDepth(root.left)
        right_depth = self.maxDepth(root.right)

        return max(left_depth, right_depth) + 1
    
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        r"""
        请考虑一棵二叉树上所有的叶子，这些叶子的值按从左到右的顺序排列形成一个 叶值序列 。

        如果有两棵二叉树的叶值序列是相同，那么我们就认为它们是 叶相似 的。

        如果给定的两个根结点分别为 root1 和 root2 的树是叶相似的，
        则返回 true；否则返回 false 
        """
        def get_leaf_sequence(root: Optional[TreeNode]) -> list[int]:
            """获取叶子序列"""
            if not root:
                return []
            
            # 如果是叶子节点，返回包含该节点值的列表
            if not root.left and not root.right:
                return [root.val]
            
            # 递归获取左子树和右子树的叶子序列
            left_sequence = get_leaf_sequence(root.left)
            right_sequence = get_leaf_sequence(root.right)

            # 合并左右子树的叶子序列
            return left_sequence + right_sequence

        # 获取两棵树的叶子序列
        leaf_sequence1 = get_leaf_sequence(root1)
        leaf_sequence2 = get_leaf_sequence(root2)

        # 比较叶子序列是否相同
        return leaf_sequence1 == leaf_sequence2

    def goodNodes(self, root: Optional[TreeNode]) -> int:
        r"""
        给你一棵根为 root 的二叉树，请你返回二叉树中好节点的数目。

        「好节点」X 定义为：从根到该节点 X 所经过的节点中，没有任何节点的值大于 X 的值。
        """
        # 边界条件
        if not root:
            return 0
        
        def dfs(node: Optional[TreeNode], max_val: int) -> int:
            if not node:
                return 0

            # 判断当前节点是否为好节点
            count = 1 if node.val >= max_val else 0

            # 更新最大值
            max_val = max(max_val, node.val)

            # 递归遍历左右子树
            count += dfs(node.left, max_val)
            count += dfs(node.right, max_val)

            return count

        return dfs(root, root.val)
