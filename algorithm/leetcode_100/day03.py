from typing import Counter, List
from collections import deque


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        r"""
        给你一个整数数组 nums，有一个大小为 k 的滑动窗口从数组的最左侧移动到数组的最右侧。
        你只可以看到在滑动窗口内的 k 个数字。滑动窗口每次只向右移动一位。

        返回 滑动窗口中的最大值 。
        """
        # 边界条件
        if not nums or k == 0:
            return []
        
        # 初始化双端队列
        dq = deque()
        result = []

        for i in range(len(nums)):
            # 移除不在窗口范围内的元素
            while dq and dq[0] <= i - k:
                dq.popleft()

            # 移除队列中所有小于当前元素的元素
            while dq and nums[dq[-1]] < nums[i]:
                dq.pop()

            # 将当前元素添加到队列中
            dq.append(i)

            # 将窗口内的最大值添加到结果中
            if i >= k - 1:
                result.append(nums[dq[0]])

        return result

    def minWindow(self, s: str, t: str) -> str:
        r"""
        给你一个字符串 s 、一个字符串 t 。返回 s 中涵盖 t 所有字符的最小子串。
        如果 s 中不存在涵盖 t 所有字符的子串，则返回空字符串 "" 。

        注意：

        - 对于 t 中重复字符，我们寻找的子字符串中该字符数量必须不少于 t 中该字符数量。
        - 如果 s 中存在这样的子串，我们保证它是唯一的答案。
        """
        # 边界条件
        if not s or not t or len(s) < len(t):
            return ""
        
        # 统计 t 中每个字符的频次
        need = Counter(t)

        # 初始化滑动窗口的左右边界和结果
        left, right = 0, 0
        vaild = 0
        window = {}

        # 记录最小覆盖子串的起始索引和长度
        start = 0
        min_len = float('inf')

        while right < len(s):
            # 将当前字符添加到窗口中
            char = s[right]
            right += 1

            # 更新窗口中的字符频次
            if char in need:
                window[char] = window.get(char, 0) + 1
                # 如果当前字符的数量满足需求，vaild + 1
                if window[char] == need[char]:
                    vaild += 1

            # 当窗口中的字符频次满足需求时，尝试收缩窗口
            while vaild == len(need):
                # 更新最小覆盖子串
                if right - left < min_len:
                    start = left
                    min_len = right - left

                # 将当前字符从窗口中移除
                removed_char = s[left]
                left += 1

                # 更新窗口中的字符频次
                if removed_char in need:
                    if window[removed_char] == need[removed_char]:
                        vaild -= 1
                    window[removed_char] -= 1

        # 返回最小覆盖子串
        return "" if min_len == float('inf') else s[start:start + min_len]

    def maxSubArray(self, nums: List[int]) -> int:
        r"""
        给你一个整数数组 nums ，请你找出一个具有最大和的连续子数组
        （子数组最少包含一个元素），返回其最大和。

        子数组是数组中的一个连续部分。
        """
        # 边界条件
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]

        # 初始化变量
        dp = [0] * len(nums) 
        # dp[i]表示以nums[i]结尾的最大子数组和
        dp[0] = nums[0]
        max_sum = dp[0]

        for i in range(1, len(nums)):
            dp[i] = max(dp[i - 1] + nums[i], nums[i])
            max_sum = max(max_sum, dp[i])

        return max_sum
    
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        r"""
        以数组 intervals 表示若干个区间的集合，其中单个区间为 intervals[i] = [starti, endi] 。
        请你合并所有重叠的区间，并返回 一个不重叠的区间数组，该数组需恰好覆盖输入中的所有区间 。
        """
        # 边界条件
        if not intervals:
            return []
        
        # 按照区间的起始位置排序
        intervals.sort(key=lambda x: x[0])

        # 初始化结果列表
        result = [intervals[0]]

        for interval in intervals[1:]:
            # 如果当前区间的起始位置小于等于结果列表中最后一个区间的结束位置，
            # 则说明有重叠
            last_interval = result[-1]
            if interval[0] <= last_interval[1]:
                # 更新结果列表中最后一个区间的结束位置
                result[-1] = [last_interval[0], max(last_interval[1], interval[1])]
            else:   
                # 否则，将当前区间添加到结果列表中
                result.append(interval)

        return result
    
    def rotate(self, nums: List[int], k: int) -> None:
        r"""
        给定一个整数数组 nums，将数组中的元素向右轮转 k 个位置，其中 k 是非负数。
        """
        # 边界条件
        n = len(nums)
        if n <= 1 or k == 0:
            return

        # 将数组中的元素向右轮转 k 个位置
        k = k % n

        def reverse(start, end):
            """反转数组中[start,end]区间中的元素"""
            while start < end:
                nums[start], nums[end] = nums[end], nums[start]
                start += 1
                end -= 1

        # 反转整个数组
        reverse(0, n - 1)
        # 反转前k个元素
        reverse(0, k - 1)
        # 反转剩余的元素
        reverse(k, n - 1)
        