import heapq
from typing import List


class MedianFinder:
    r"""
    中位数是有序整数列表中的中间值。如果列表的大小是偶数，则没有中间值，中位数是两个中间值的平均值。

    - 例如 arr = [2,3,4] 的中位数是 3 。
    - 例如 arr = [2,3] 的中位数是 (2 + 3) / 2 = 2.5 。

    实现 MedianFinder 类:

    - MedianFinder() 初始化 MedianFinder 对象。
    - void addNum(int num) 将数据流中的整数 num 添加到数据结构中。
    - double findMedian() 返回到目前为止所有元素的中位数。与实际答案相差 10-5 以内的答案将被接受。
    """
    def __init__(self):
        # 最大堆存储较小的一半元素（Python的heapq是最小堆，所以存储负值来模拟最大堆）
        self.small = [] # 最大堆（存储负值）
        # 最小堆存储较大的一半元素
        self.large = [] # 最小堆
    
    def addNum(self, num: int) -> None:
        # 首先将数字添加到small堆
        heapq.heappush(self.small, -num)

        # 确保small堆的最大值 <= large堆的最小值
        if self.small and self.large and (-self.small[0] > self.large[0]):
            val = -heapq.heappop(self.small)
            heapq.heappush(self.large, val)
            
        # 平衡两个堆的大小
        if len(self.small) > len(self.large) + 1:
            val = -heapq.heappop(self.small)
            heapq.heappush(self.large, val)
        
        if len(self.large) > len(self.small) + 1:
            val = heapq.heappop(self.large)
            heapq.heappush(self.small, -val)
            
    def findMedian(self) -> float:
        if len(self.small) > len(self.large):
            return -self.small[0]
        elif len(self.large) > len(self.small):
            return self.large[0]
        else:
            # 两个堆大小相等，返回平均值
            return (-self.small[0] + self.large[0]) / 2.0
        

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        r"""
        给定一个数组 prices ，它的第 i 个元素 prices[i] 表示一支给定股票第 i 天的价格。

        你只能选择 某一天 买入这只股票，并选择在 未来的某一个不同的日子 卖出该股票。
        设计一个算法来计算你所能获取的最大利润。

        返回你可以从这笔交易中获取的最大利润。如果你不能获取任何利润，返回 0 。
        """
        # 边界条件
        if not prices:
            return 0
        
        # 初始化变量
        min_price = prices[0]
        max_profit = 0

        # 遍历数组
        for price in prices:
            # 更新最小价格
            min_price = min(min_price, price)
            # 计算当前价格与最小价格的差值，并更新最大利润
            max_profit = max(max_profit, price - min_price)

        return max_profit
    
    def canJump(self, nums: List[int]) -> bool:
        r"""
        给你一个非负整数数组 nums ，你最初位于数组的 第一个下标 。
        数组中的每个元素代表你在该位置可以跳跃的最大长度。

        判断你是否能够到达最后一个下标，如果可以，返回 true ；否则，返回 false 。
        """
        # 边界条件
        if not nums:
            return False

        # 初始化变量
        max_reach = 0

        # 遍历数组
        for i, jump in enumerate(nums):
            # 如果当前下标大于最大可达下标，则无法到达最后一个下标
            if i > max_reach:
                return False
            # 更新最大可达下标
            max_reach = max(max_reach, i + jump)
            
            # 如果最大可达下标大于等于最后一个下标，则可以到达最后一个下标
            if max_reach >= len(nums) - 1:
                return True

        return False

    def jump(self, nums: List[int]) -> int:
        r"""
        给定一个长度为 n 的 0 索引整数数组 nums。初始位置为 nums[0]。

        每个元素 nums[i] 表示从索引 i 向后跳转的最大长度。
        换句话说，如果你在索引 i 处，你可以跳转到任意 (i + j) 处：

        - 0 <= j <= nums[i] 且
        - i + j < n

        返回到达 n - 1 的最小跳跃次数。测试用例保证可以到达 n - 1。
        """
        # 边界条件
        if not nums or len(nums) == 1:
            return 0

        # 初始化变量
        jumps = 0
        current_end = 0
        farthest = 0

        # 遍历数组
        for i in range(len(nums) - 1):
            # 更新最远可达下标
            farthest = max(farthest, i + nums[i])

            # 如果到达当前跳跃的终点，则进行下一次跳跃
            if i == current_end:
                jumps += 1
                current_end = farthest

                # 如果当前跳跃的终点已经到达或超过最后一个下标，则返回跳跃次数
                if current_end >= len(nums) - 1:
                    break

        return jumps
    
    def partitionLabels(self, s: str) -> List[int]:
        r"""
        给你一个字符串 s 。我们要把这个字符串划分为尽可能多的片段，同一字母最多出现在一个片段中。
        例如，字符串 "ababcc" 能够被分为 ["abab", "cc"]，
        但类似 ["aba", "bcc"] 或 ["ab", "ab", "cc"] 的划分是非法的。

        注意，划分结果需要满足：将所有划分结果按顺序连接，得到的字符串仍然是 s 。

        返回一个表示每个字符串片段的长度的列表。
        """
        # 边界条件
        if not s:
            return []

        # 初始化变量
        last_occur = {char: i for i, char in enumerate(s)}
        res = []
        start, end = 0, 0

        # 遍历字符串
        for i, char in enumerate(s):
            # 贪心选择
            end = max(end, last_occur[char])

            # 如果到达当前片段的终点，则将当前片段的长度添加到结果中
            if i == end:
                # 添加片段长度
                res.append(end - start + 1)
                # 开始新片段
                start = end + 1

        return res