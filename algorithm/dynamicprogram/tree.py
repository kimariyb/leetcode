"""
问题描述：

有一个地区只有一个入口，我们称为“根”。 
除了“根”之外，每栋房子有且只有一个“父“房子与之相连。
一番侦察之后，聪明的小偷意识到“这个地方的所有房屋的排列类似于一棵二叉树”。
如果两个直接相连的房子在同一天晚上被打劫，房屋将自动报警。
计算在不触动警报的情况下，小偷一晚能够盗取的最高金额
"""
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        
        
class Solution:
    def rob(self, root: TreeNode) -> int:
        # 边界条件
        if not root:
            return 0
        
        def postOrder(node: TreeNode):
            if not node:
                return [0, 0]
            
            left = postOrder(node.left)
            right = postOrder(node.right)

            # 如果不偷当前节点，那么左右子节点都可以偷
            rob = node.val + left[1] + right[1]
            # 如果要偷当前节点，那么左右子节点就不能偷
            not_rob = max(left) + max(right)
            
            return [rob, not_rob]

        return max(postOrder(root))
    

if __name__ == '__main__':
    tree = TreeNode(3)
    tree.left = TreeNode(2)
    tree.right = TreeNode(3)
    tree.left.right = TreeNode(3)
    tree.right.right = TreeNode(1)
    print(Solution().rob(tree))
    