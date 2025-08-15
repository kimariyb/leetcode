from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        r"""
        给你一个整数数组 nums，返回 数组 answer ，
        其中 answer[i] 等于 nums 中除 nums[i] 之外其余各元素的乘积 。

        题目数据 保证 数组 nums之中任意元素的全部前缀元素和后缀的乘积都在 32 位 整数范围内。

        请 不要使用除法，且在 O(n) 时间复杂度内完成此题。
        """
        # 初始化 answer
        answer = [1] * len(nums)

        # 计算每个位置左侧所有元素的乘积（前缀乘积）
        for i in range(1, len(nums)):
            answer[i] = answer[i - 1] * nums[i - 1]

        # 计算右侧所有元素的乘积并合并（后缀乘积）
        right_product = 1
        for i in range(len(nums) - 1, -1, -1):
            answer[i] *= right_product
            right_product *= nums[i]

        return answer
    
    def firstMissingPositive(self, nums: List[int]) -> int:
        r"""
        给你一个未排序的整数数组 nums ，请你找出其中没有出现的最小的正整数。

        请你实现时间复杂度为 O(n) 并且只使用常数级别额外空间的解决方案。
        """
        n = len(nums)

        # 将每个数字放到正确的位置上
        for i in range(n):
            # 持续交换直到当前位置的数字满足以下条件之一：
            # 1. 不在[1,n]范围内
            # 2. 已经在正确位置上
            while nums[i] > 0 and nums[i] <= n and nums[nums[i] - 1] != nums[i]:
                # 交换 nums[i] 和 nums[nums[i] - 1]
                nums[nums[i] - 1], nums[i] = nums[i], nums[nums[i] - 1]

        # 找到第一个不在正确位置上的数字
        for i in range(n):
            if nums[i] != i + 1:
                return i + 1

        # 如果所有数字都在正确位置上，则返回 n + 1
        return n + 1
    
    def setZeroes(self, matrix: List[List[int]]) -> None:
        r"""
        给定一个 m x n 的矩阵，如果一个元素为 0 ，
        则将其所在行和列的所有元素都设为 0 。请使用 原地 算法。
        """
        m, n = len(matrix), len(matrix[0])

        # 使用 hashmap 记录
        row_zero, col_zero = set(), set()

        # 记录所有为 0 的行和列
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    row_zero.add(i)
                    col_zero.add(j)

        # 将所有为 0 的行和列设为 0
        for row in row_zero:
            for j in range(n):
                matrix[row][j] = 0
        for col in col_zero:
            for i in range(m):
                matrix[i][col] = 0

    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        r"""
        给你一个 m 行 n 列的矩阵 matrix ，
        请按照 顺时针螺旋顺序 ，返回矩阵中的所有元素。
        """
        # 边界条件
        if not matrix or not matrix[0]:
            return []

        m, n = len(matrix), len(matrix[0])
        # 定义四个边界
        left, right, top, bottom = 0, n - 1, 0, m - 1
        result = []

        while top <= bottom and left <= right:
            # 从左到右遍历
            for j in range(left, right + 1):
                result.append(matrix[top][j])
            top += 1 # 上边界下移

            # 从上到下遍历
            for i in range(top, bottom + 1):
                result.append(matrix[i][right])
            right -= 1 # 右边界左移

            # 从右到左遍历下边界（如果还有行）
            if top <= bottom:
                for j in range(right, left - 1, -1):
                    result.append(matrix[bottom][j])
                bottom -= 1  # 下边界上移

            # 从下到上遍历左边界（如果还有列）
            if left <= right:
                for i in range(bottom, top - 1, -1):
                    result.append(matrix[i][left])
                left += 1  # 左边界右移

        return result
    
    def rotate(self, matrix: List[List[int]]) -> None:
        r"""
        给定一个 n × n 的二维矩阵 matrix 表示一个图像。
        请你将图像顺时针旋转 90 度。

        你必须在 原地 旋转图像，这意味着你需要直接修改输入的二维矩阵。
        请不要 使用另一个矩阵来旋转图像。
        """
        # 边界条件
        if not matrix or not matrix[0]:
            return
        
        n = len(matrix)

        # 转置矩阵（沿主对角线翻转）
        for i in range(n):
            for j in range(i + 1, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        # 每行反转
        for i in range(n):
            for j in range(n // 2):
                matrix[i][j], matrix[i][n - j - 1] = matrix[i][n - j - 1], matrix[i][j]
