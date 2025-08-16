from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        r"""
        给你一个整数数组 nums ，数组中的元素 互不相同 。返回该数组所有可能的子集（幂集）。

        解集 不能 包含重复的子集。你可以按 任意顺序 返回解集。
        """
        # 边界条件
        if not nums:
            return [[]]

        res = []

        # 回溯
        def backtrack(start, curr_subset):
            # 将当前子集加入结果
            res.append(curr_subset[:])
            
            # 从start开始遍历，避免重复
            for i in range(start, len(nums)):
                # 做选择
                curr_subset.append(nums[i])
                # 递归处理后续元素
                backtrack(i + 1, curr_subset)
                # 撤销选择  
                curr_subset.pop()

        backtrack(0, [])
        return res

    def letterCombinations(self, digits: str) -> List[str]:
        r"""
        给定一个仅包含数字 2-9 的字符串，返回所有它能表示的字母组合。
        答案可以按 任意顺序 返回。

        给出数字到字母的映射如下（与电话按键相同）。注意 1 不对应任何字母。
        """
        # 边界条件
        if not digits:
            return []

        # 数字到字母的映射
        digit_to_char = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }
        
        res = []

        # 回溯
        def backtrack(start, curr_combination):
            # 如果当前组合的长度等于输入数字的长度，说明已经生成了一个完整的组合
            if len(curr_combination) == len(digits):
                res.append(curr_combination)
                return

            # 获取当前数字对应的字母
            curr_digit = digits[start]
            for char in digit_to_char[curr_digit]:
                # 做选择
                curr_combination += char
                # 递归处理后续数字
                backtrack(start + 1, curr_combination)
                # 撤销选择
                curr_combination = curr_combination[:-1]

        backtrack(0, '')
        return res
    
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        r"""
        给你一个 无重复元素 的整数数组 candidates 和一个目标整数 target ，
        找出 candidates 中可以使数字和为目标数 target 的 所有 不同组合 ，并以列表形式返回。
        你可以按 任意顺序 返回这些组合。

        candidates 中的 同一个 数字可以 无限制重复被选取 。
        如果至少一个数字的被选数量不同，则两种组合是不同的。 

        对于给定的输入，保证和为 target 的不同组合数少于 150 个。 
        """
        # 边界条件
        if not candidates:
            return []

        res = []

        # 回溯
        def backtrack(start, curr_combination, curr_sum):
            # 如果当前组合的和等于目标值，则将当前组合加入结果
            if curr_sum == target:
                res.append(curr_combination[:])
                return
            
            # 遍历
            for i in range(start, len(candidates)):
                num = candidates[i]
                # 如果当前组合的和加上当前数字大于目标值，则跳过当前数字
                if curr_sum + num > target:
                    continue
                # 做选择
                curr_combination.append(num)
                # 递归处理后续元素
                backtrack(i, curr_combination, curr_sum + num)
                # 撤销选择
                curr_combination.pop()

        backtrack(0, [], 0)
        return res

    def generateParenthesis(self, n: int) -> List[str]:
        r"""
        数字 n 代表生成括号的对数，请你设计一个函数，用于能够生成所有可能的并且 有效的 括号组合。
        """
        # 边界条件
        if n <= 0:
            return []

        res = []

        # 回溯
        def backtrack(curr_str, left, right):
            # 如果当前字符串的长度等于 2*n，说明已经生成了一个完整的括号组合
            if len(curr_str) == 2 * n:
                res.append(curr_str)
                return
            
            # 如果左括号数量小于 n，可以添加左括号
            if left < n:
                backtrack(curr_str + "(", left + 1, right)
            
            # 如果右括号数量小于左括号数量，可以添加右括号
            if right < left:
                backtrack(curr_str + ")", left, right + 1)
            
        backtrack("", 0, 0)
        return res
    
    def exist(self, board: List[List[str]], word: str) -> bool:
        r"""
        给定一个 m x n 二维字符网格 board 和一个字符串单词 word 。
        如果 word 存在于网格中，返回 true ；否则，返回 false 。

        单词必须按照字母顺序，通过相邻的单元格内的字母构成，
        其中“相邻”单元格是那些水平相邻或垂直相邻的单元格。同一个单元格内的字母不允许被重复使用。
        """
        # 边界条件
        if not board or not board[0] or not word:
            return False
        
        m, n = len(board), len(board[0])

        # 回溯
        def backtrack(row, col, index):
            # 边界检查
            if row < 0 or row >= m or col < 0 or col >= n or board[row][col] != word[index]:
                return False
            
            # 如果已经匹配到最后一个字符了，说明找到了
            if index == len(word) - 1:
                return True
            
            # 标记当前单元格已经被访问
            temp = board[row][col]
            board[row][col] = "#"

            # 检查当前单元格的上下左右四个方向
            directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
            for dr, dc in directions:
                if backtrack(row + dr, col + dc, index + 1):
                    board[row][col] = temp # 恢复状态
                    return True

            # 恢复状态
            board[row][col] = temp
            return False

        # 遍历网格中的每个单元格
        for i in range(m):
            for j in range(n):
                if backtrack(i, j, 0):
                    return True
        return False