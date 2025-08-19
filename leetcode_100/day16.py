import heapq
from typing import List
from collections import Counter


class Solution:
    def decodeString(self, s: str) -> str:
        r"""
        给定一个经过编码的字符串，返回它解码后的字符串。

        编码规则为: k[encoded_string]，表示其中方括号内部的 encoded_string 正好重复 k 次。
        注意 k 保证为正整数。

        你可以认为输入字符串总是有效的；输入字符串中没有额外的空格，且输入的方括号总是符合格式要求的。

        此外，你可以认为原始数据不包含数字，所有的数字只表示重复的次数 k ，例如不会出现像 3a 或 2[4] 的输入。

        测试用例保证输出的长度不会超过 105。
        """
        # 边界条件
        if not s:
            return s
        
        # 初始化
        stack = []
        curr_num = 0
        curr_str = ""
        
        for char in s:
            if char.isdigit():
                # 如果是数字，更新当前数字
                curr_num = curr_num * 10 + int(char)
            elif char == "[":
                # 如果是左括号，将当前数字和当前字符串入栈
                stack.append((curr_str, curr_num))
                # 重置当前数字和当前字符串
                curr_num, curr_str = 0, ""
            elif char == "]":
                # 如果是右括号，将栈顶的字符串和当前字符串重复当前数字次，并更新当前字符串
                prev_str, k = stack.pop()
                curr_str = prev_str + curr_str * k
            else:
                # 如果是字母，更新当前字符串
                curr_str += char

        return curr_str

    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        r"""
        给定一个整数数组 temperatures ，表示每天的温度，返回一个数组 answer ，
        其中 answer[i] 是指对于第 i 天，下一个更高温度出现在几天后。
        如果气温在这之后都不会升高，请在该位置用 0 来代替。
        """
        # 边界条件
        if not temperatures:
            return temperatures

        # 初始化
        n = len(temperatures)
        res = [0] * n
        stack = []

        for i in range(n):
            while stack and temperatures[i] > temperatures[stack[-1]]:
                j = stack.pop()
                res[j] = i - j
            stack.append(i)

        return res

    def largestRectangleArea(self, heights: List[int]) -> int:
        r"""
        给定 n 个非负整数，用来表示柱状图中各个柱子的高度。每个柱子彼此相邻，且宽度为 1 。

        求在该柱状图中，能够勾勒出来的矩形的最大面积。
        """
        # 边界条件
        if not heights:
            return 0

        # 初始化
        # 在末尾添加 0，确保所有元素都能被处理
        heights.append(0)
        stack = []  # 单调递增栈，存储索引
        max_area = 0
        
        for i in range(len(heights)):
            # 当前高度小于栈顶高度时，计算以栈顶为高的矩形面积
            while stack and heights[i] < heights[stack[-1]]:
                # 弹出栈顶元素作为矩形的高度
                h = heights[stack.pop()]
                # 计算矩形宽度
                # 如果栈为空，说明可以扩展到最左边
                # 否则宽度为当前位置到栈顶位置-1
                w = i if not stack else i - stack[-1] - 1
                # 更新最大面积
                max_area = max(max_area, h * w)
            # 当前高度大于等于栈顶高度时，将当前索引入栈
            stack.append(i)
            
        # 移除添加的0
        heights.pop()

        return max_area
    
    def findKthLargest(self, nums: List[int], k: int) -> int:
        r"""
        给定整数数组 nums 和整数 k，请返回数组中第 k 个最大的元素。

        请注意，你需要找的是数组排序后的第 k 个最大的元素，而不是第 k 个不同的元素。

        你必须设计并实现时间复杂度为 O(n) 的算法解决此问题。
        """
        # 边界条件
        if not nums:
            return nums
        
        # 初始化
        n = len(nums)
        # 建堆
        heapq.heapify(nums)

        # 弹出 n - k 个最小值
        for _ in range(n - k):
            heapq.heappop(nums)

        return heapq.heappop(nums)
    
    
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        r"""
        给你一个整数数组 nums 和一个整数 k ，请你返回其中出现频率前 k 高的元素。
        你可以按 任意顺序 返回答案。
        """
        # 边界条件
        if not nums:
            return nums
        
        # 统计每个数字出现的频率
        freq = Counter(nums)
        
        # 使用最小堆维护k个元素
        heap = []        
        
        for num, count in freq.items():
            if len(heap) < k:
                # 堆未满，直接加入
                heapq.heappush(heap, (count, num))
            elif count > heap[0][0]:
                # 堆已满，且当前数字频率大于堆顶数字频率，替换堆顶元素
                heapq.heapreplace(heap, (count, num))

        # 返回堆中的元素
        return [num for _, num in heap]