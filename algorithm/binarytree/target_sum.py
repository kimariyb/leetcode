"""
问题描述：

给定一颗二叉树，一个目标值
请输出所有路径，需要满足根节点至叶子节点之和等于给定的目标值
"""
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        

class Solution:
    def findTargetSumWays(self, root: Optional[TreeNode], target: int) -> List[List[int]]:
        # 边界条件
        if not root:
            return []
        
        # 用于存储结果
        res = []
        
        def backtrace(node: Optional[TreeNode], path: List[int], current_sum: int, target: int):
            # 终止条件
            if not node:
                return
            
             # 更新当前路径和
            current_sum += node.val
            path.append(node.val)

            # 检查是否是叶子节点且满足条件
            if not node.left and not node.right and current_sum == target:
                res.append(path[:])
            
            # 递归遍历左右子树
            backtrace(node.left, path, current_sum, target)
            backtrace(node.right, path, current_sum, target)
            
            # 回溯
            path.pop()

        backtrace(root, [], 0, target)
        return res
    

if __name__ == '__main__':
    s = Solution()
    root = TreeNode(
        val=5
    )
    root.left = TreeNode(
        val=4
    )
    root.right = TreeNode(
        val=3
    )
    
    root.right.left = TreeNode(
        val=1
    )
    root.right.right = TreeNode(
        val=2
    )
    print(s.findTargetSumWays(root, 9))