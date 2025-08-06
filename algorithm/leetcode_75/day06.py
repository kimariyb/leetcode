from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        r"""
        给定一个二叉树的根节点 root ，和一个整数 targetSum ，
        求该二叉树里节点值之和等于 targetSum 的 路径 的数目。

        路径 不需要从根节点开始，也不需要在叶子节点结束，
        但是路径方向必须是向下的（只能从父节点到子节点）。
        """
        def dfs(
            node: Optional[TreeNode], 
            current_sum: int,
            prefix_sum_map: dict
        ):
            if not node:
                return 0

            # 更新当前路径和
            current_sum += node.val

            # 查找是否存在前缀和使得 current_sum - prefix_sum = targetSum
            count = prefix_sum_map.get(current_sum - targetSum, 0)

            # 将当前前缀和加入map
            prefix_sum_map[current_sum] = prefix_sum_map.get(current_sum, 0) + 1

            # 递归处理左右子树
            count += dfs(node.left, current_sum, prefix_sum_map)
            count += dfs(node.right, current_sum, prefix_sum_map)

            # 回溯，恢复状态
            prefix_sum_map[current_sum] -= 1

            return count
        
        return dfs(root, 0, {0: 1})
    
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        r"""
        给你一棵以 root 为根的二叉树，二叉树中的交错路径定义如下：

        - 选择二叉树中 任意 节点和一个方向（左或者右）。
        - 如果前进方向为右，那么移动到当前节点的的右子节点，否则移动到它的左子节点。
        - 改变前进方向：左变右或者右变左。
        - 重复第二步和第三步，直到你在树中无法继续移动。

        交错路径的长度定义为：访问过的节点数目 - 1（单个节点的路径长度为 0 ）。

        请你返回给定树中最长 交错路径 的长度。
        """
        def dfs(node: Optional[TreeNode], goLeft: bool, steps: int):
            if not node:
                return steps - 1
            
            if goLeft:
                # 向左走（延续路径）vs 向右重新开始
                return max(
                    dfs(node.left, False, steps + 1), # 向左走，下一次应该向右
                    dfs(node.right, True, 1) # 向右重新开始
                )
            else:
                # 向右走（延续路径）vs 向左重新开始
                return max(
                    dfs(node.right, True, steps + 1), # 向右走，下一次应该向左
                    dfs(node.left, False, 1) # 向左重新开始
                )
            
        if not root:
            return 0

        return max(
            dfs(root, True, 0), 
            dfs(root, False, 0)
        )
    
    def lowestCommonAncestor(
        self, root: Optional[TreeNode], 
        p: Optional[TreeNode], q: Optional[TreeNode]
    ) -> Optional[TreeNode]:
        r"""
        给定一个二叉树, 找到该树中两个指定节点的最近公共祖先。

        百度百科中最近公共祖先的定义为：
        “对于有根树 T 的两个节点 p、q，最近公共祖先表示为一个节点 x，
        满足 x 是 p、q 的祖先且 x 的深度尽可能大（一个节点也可以是它自己的祖先）。”
        """
        # 边界条件
        if not root or root == p or root == q:
            return root
        
        # 递归处理左右子树
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)

        # 如果左右子树都找到了p或q，说明当前节点就是最近公共祖先
        if left and right:
            return root

        # 如果只有左子树找到了p或q，说明最近公共祖先在左子树
        return left if left else right
    
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        r"""
        给定二叉搜索树（BST）的根节点 root 和一个整数值 val。

        你需要在 BST 中找到节点值等于 val 的节点。 
        返回以该节点为根的子树。 如果节点不存在，则返回 null 。
        """
        # 边界条件
        if not root or root.val == val:
            return root
        
        current = root

        # 二叉搜索树的性质：
        # 1. 左子树的所有节点值都小于根节点值
        # 2. 右子树的所有节点值都大于根节点值
        while current:
            if current.val == val:
                return current
            elif current.val > val:  # 在左子树中查找
                current = current.left
            else:  # 在右子树中查找
                current = current.right

        return None
    
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        r"""
        给定一个二叉搜索树的根节点 root 和一个值 key，删除二叉搜索树中的 key 对应的节点，
        并保证二叉搜索树的性质不变。返回二叉搜索树（有可能被更新）的根节点的引用。

        一般来说，删除节点可分为两个步骤：

        1. 首先找到需要删除的节点；
        2. 如果找到了，删除它。
        """
        def findMin(node: TreeNode) -> TreeNode:
            """找到子树中的最小节点"""
            while node.left: 
                node = node.left 
            return node
        
        # 边界条件
        if not root:
            return None
        
        # 查找要删除的节点
        if key < root.val:
            root.left = self.deleteNode(root.left, key)
        elif key > root.val:
            root.right = self.deleteNode(root.right, key)
        else:
            # 找到了要删除的节点

            # 如果没有子叶节点
            if not root.left and not root.right:
                return None

            # 如果只有一个子叶节点
            if not root.left:
                return root.right
            if not root.right:
                return root.left

            # 如果有两个子叶节点
            # 找到右子树中的最小节点
            min_node = findMin(root.right)
            # 用后继节点的值替换当前节点的值
            root.val = min_node.val
            # 删除后继节点
            root.right = self.deleteNode(root.right, min_node.val)

        return root