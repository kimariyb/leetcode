from typing import List


class Solution:
    def partition(self, s: str) -> List[List[str]]:
        r"""
        给你一个字符串 s，请你将 s 分割成一些 子串，使每个子串都是 回文串 。
        返回 s 所有可能的分割方案。
        """
        # 边界条件
        if not s:
            return []
        if len(s) == 1:
            return [[s]]

        # 回溯
        res = []
        def backtrack(start, curr_str):
            # 终止条件：当 start 索引到达字符串末尾时，说明已经遍历完字符串
            if start == len(s):
                res.append(curr_str)
                return

            # 遍历字符串，从 start 索引开始
            for i in range(start, len(s)):
                # 如果子串是回文串，则继续递归
                if s[start:i+1] == s[start:i+1][::-1]:
                    backtrack(i+1, curr_str + [s[start:i+1]])

        backtrack(0, [])
        return res
    
    def solveNQueens(self, n: int) -> List[List[str]]:
        r"""
        按照国际象棋的规则，皇后可以攻击与之处在同一行或同一列或同一斜线上的棋子。

        n 皇后问题 研究的是如何将 n 个皇后放置在 n×n 的棋盘上，并且使皇后彼此之间不能相互攻击。

        给你一个整数 n ，返回所有不同的 n 皇后问题 的解决方案。

        每一种解法包含一个不同的 n 皇后问题 的棋子放置方案，该方案中 'Q' 和 '.' 分别代表了皇后和空位。
        """
        # 边界条件
        if n < 1:
            return []
        if n == 1:
            return [["Q"]]

        # 回溯
        res = []
        def backtrack(row, col, diag, anti_diag, curr_queens):
            # 终止条件：当 row 索引到达棋盘的最后一行时，说明已经找到了一种解决方案
            if row == n:
                res.append(curr_queens)
                return

            # 遍历棋盘的每一列
            for i in range(n):
                # 如果当前位置所在的列、主对角线、副对角线上没有皇后，则可以放置皇后
                if i not in col and (row + i) not in diag and (row - i) not in anti_diag:
                    # 递归调用回溯函数，继续放置下一行的皇后
                    backtrack(
                        row + 1, 
                        col + [i], 
                        diag + [row + i], 
                        anti_diag + [row - i], 
                        curr_queens + ["." * i + "Q" + "." * (n - i - 1)]
                    )

        backtrack(0, [], [], [], [])
        return res
    
    def searchInsert(self, nums: List[int], target: int) -> int:
        r"""
        给定一个排序数组和一个目标值，在数组中找到目标值，并返回其索引。
        如果目标值不存在于数组中，返回它将会被按顺序插入的位置。

        请必须使用时间复杂度为 O(log n) 的算法。
        """
        # 边界条件
        if not nums:
            return 0
        
        n = len(nums)
        left, right = 0, n - 1

        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1

        return left
    
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        r"""
        给你一个满足下述两条属性的 m x n 整数矩阵：

        - 每行中的整数从左到右按非严格递增顺序排列。
        - 每行的第一个整数大于前一行的最后一个整数。
        
        给你一个整数 target ，如果 target 在矩阵中，返回 true ；否则，返回 false 。
        """
        # 边界条件
        if not matrix or not matrix[0]:
            return False

        m, n = len(matrix), len(matrix[0])
        left, right = 0, n - 1

        # 从矩阵的右上角开始搜索
        while left < m and right >= 0:
            if matrix[left][right] == target:
                return True
            # 如果当前元素小于目标值，说明没有值会比当前元素更小，因此可以向下移动一行
            elif matrix[left][right] < target:
                left += 1
            # 如果当前元素大于目标值，说明没有值会比当前元素更大，因此可以向左移动一列
            else:
                right -= 1

        return False
    

    def searchRange(self, nums: List[int], target: int) -> List[int]:
        r"""
        给你一个按照非递减顺序排列的整数数组 nums，和一个目标值 target。
        请你找出给定目标值在数组中的开始位置和结束位置。

        如果数组中不存在目标值 target，返回 [-1, -1]。

        你必须设计并实现时间复杂度为 O(log n) 的算法解决此问题。
        """
        # 边界条件
        if not nums:
            return [-1, -1]

        # 二分查找
        def findLeftBound(nums, target):
            """查找目标值的左边界"""
            left, right = 0, len(nums) - 1
            result = -1
            
            while left <= right:
                mid = left + (right - left) // 2
                if nums[mid] == target:
                    result = mid  # 记录找到的位置
                    right = mid - 1  # 继续向左查找
                elif nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
            
            return result
        
        def findRightBound(nums, target):
            """查找目标值的右边界"""
            left, right = 0, len(nums) - 1
            result = -1
            
            while left <= right:
                mid = left + (right - left) // 2
                if nums[mid] == target:
                    result = mid  # 记录找到的位置
                    left = mid + 1  # 继续向右查找
                elif nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
            
            return result

        left_bound = findLeftBound(nums, target)
        if left_bound == -1:
            return [-1, -1]
        
        right_bound = findRightBound(nums, target)

        return [left_bound, right_bound]