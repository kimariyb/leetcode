from bisect import bisect_left
from typing import List


class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        r"""
        给你一个产品数组 products 和一个字符串 searchWord 
        ，products  数组中每个产品都是一个字符串。

        请你设计一个推荐系统，在依次输入单词 searchWord 的每一个字母后，
        推荐 products 数组中前缀与 searchWord 相同的最多三个产品。
        如果前缀相同的可推荐产品超过三个，请按字典序返回最小的三个。

        请你以二维列表的形式，返回在输入 searchWord 每个字母后相应的推荐产品的列表。
        """
        # 边界条件
        if not products or not searchWord:
            return []
        
        # 对产品数组进行排序
        products.sort()

        # 初始化结果列表
        result = []
        prefix = ""

        # 遍历 searchWord 的每一个字母
        for char in searchWord:
            prefix += char
            # 使用二分查找找到第一个大于等于 prefix 的位置
            start_idx = bisect_left(products, prefix)     
            suggestions = []

            # 从 start_idx 开始检查
            for i in range(start_idx, min(start_idx + 3, len(products))):
                if products[i].startswith(prefix):
                    suggestions.append(products[i])
                else:
                    break

            result.append(suggestions)

        return result
            
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        r"""
        给定一个区间的集合 intervals ，其中 intervals[i] = [starti, endi] 。
        返回 需要移除区间的最小数量，使剩余区间互不重叠 。

        注意 只在一点上接触的区间是 不重叠的。例如 [1, 2] 和 [2, 3] 是不重叠的。
        """
        # 边界条件
        if not intervals:
            return 0
        
        # 按照区间的结束位置进行排序
        intervals.sort(key=lambda x: x[1])
        
        # 初始化计数器和最后一个区间的结束位置
        count = 0
        last_end = intervals[0][1]

        # 遍历区间集合
        for i in range(1, len(intervals)):
            # 如果当前区间的开始位置小于等于最后一个区间的结束位置，则重叠
            if intervals[i][0] < last_end:
                count += 1
            else:
                last_end = intervals[i][1]

        return count

    def findMinArrowShots(self, points: List[List[int]]) -> int:
        r"""
        有一些球形气球贴在一堵用 XY 平面表示的墙面上。墙面上的气球记录在整数数组 points ，
        其中 points[i] = [xstart, xend] 表示水平直径在 xstart 和 xend之间的气球。
        你不知道气球的确切 y 坐标。

        一支弓箭可以沿着 x 轴从不同点 完全垂直 地射出。
        在坐标 x 处射出一支箭，若有一个气球的直径的开始和结束坐标为 xstart，xend， 
        且满足  xstart ≤ x ≤ xend，则该气球会被 引爆 。
        可以射出的弓箭的数量 没有限制 。 弓箭一旦被射出之后，可以无限地前进。

        给你一个数组 points ，返回引爆所有气球所必须射出的 最小 弓箭数 。
        """
        # 边界条件
        if not points:
            return 0

        # 按照区间的结束位置进行排序
        points.sort(key=lambda x: x[1])
        
        # 初始化计数器和最后一个区间的结束位置
        arrow = 1
        arrow_position = points[0][1]
        
        # 从第二个区间开始遍历
        for i in range(1, len(points)):
            # 如果当前区间的开始位置大于箭的位置，则需要新的箭
            if points[i][0] > arrow_position:
                arrow += 1
                arrow_position = points[i][1]

        return arrow
    
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        r"""
        给定一个整数数组 temperatures ，表示每天的温度，返回一个数组 answer ，
        其中 answer[i] 是指对于第 i 天，下一个更高温度出现在几天后。
        如果气温在这之后都不会升高，请在该位置用 0 来代替。
        """
        # 边界条件
        if not temperatures:
            return []
        
        # 因为需要返回的是下一个更高温度，也就是最右边的最大值
        # 使用递减栈，栈中的元素必须单调递减
        # 所以 temp > stack[-1] 时，弹出栈顶元素，并计算天数差
        n = len(temperatures)
        ans = [0] * n
        stack = []

        for i in range(n):
            # 如果栈不为空且当前温度大于栈顶的温度
            while stack and temperatures[i] > temperatures[stack[-1]]:
                # 弹出栈顶元素
                pre_index = stack.pop()
                # 计算天数差
                ans[pre_index] = i - pre_index
            # 将当前索引入栈
            stack.append(i)

        return ans
            


class StockSpanner:
    r"""
    设计一个算法收集某些股票的每日报价，并返回该股票当日价格的 跨度 。

    当日股票价格的 跨度 被定义为股票价格小于或等于今天价格的最大连续日数（从今天开始往回数，包括今天）。

    - 例如，如果未来 7 天股票的价格是 [100,80,60,70,60,75,85]，那么股票跨度将是 [1,1,1,2,1,4,6] 。

    实现 StockSpanner 类：

    - StockSpanner() 初始化类对象。
    - int next(int price) 给出今天的股价 price ，返回该股票当日价格的 跨度 。
    """
    def __init__(self):
        self.stack = []

    def next(self, price: int) -> int:
        # 至少今天包括
        span = 1
        
        # 如果栈不为空且当前价格大于等于栈顶价格
        while self.stack and price >= self.stack[-1][0]:
            # 弹出栈顶元素，并累加跨度
            span += self.stack.pop()[1]

        # 将当前价格和跨度入栈
        self.stack.append((price, span))

        return span