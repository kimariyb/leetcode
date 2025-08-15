import heapq
from typing import List


def guess(num: int) -> int:
    return 0


class Solution:
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        r"""
        给你两个下标从 0 开始的整数数组 nums1 和 nums2 ，两者长度都是 n ，
        再给你一个正整数 k 。你必须从 nums1 中选一个长度为 k 的 子序列 对应的下标。

        对于选择的下标 i0 ，i1 ，...， ik - 1 ，你的 分数 定义如下：

        - nums1 中下标对应元素求和，乘以 nums2 中下标对应元素的 最小值 。
        - 用公式表示： (nums1[i0] + nums1[i1] +...+ nums1[ik - 1]) * min(nums2[i0] , nums2[i1], ... ,nums2[ik - 1]) 。

        请你返回 最大 可能的分数。

        一个数组的 子序列 下标是集合 {0, 1, ..., n-1} 中删除若干元素得到的剩余集合，
        也可以不删除任何元素。
        """
        # 配对并按 nums2 降序排序
        pairs = sorted(
            zip(nums1, nums2), key=lambda x: x[1], reverse=True
        )

        # 最小堆维护最大的k个nums1元素
        min_heap = []
        current_sum = 0
        max_score = 0

        for num1, num2 in pairs:
            # 添加当前元素
            heapq.heappush(min_heap, num1)
            current_sum += num1

            # 维持堆大小为 k
            if len(min_heap) > k:
                current_sum -= heapq.heappop(min_heap)

            # 计算当前分数
            if len(min_heap) == k:
                max_score = max(max_score, current_sum * num2)

        return max_score
    
    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
        r"""
        给你一个下标从 0 开始的整数数组 costs ，其中 costs[i] 是雇佣第 i 位工人的代价。

        同时给你两个整数 k 和 candidates 。我们想根据以下规则恰好雇佣 k 位工人：

        - 总共进行 k 轮雇佣，且每一轮恰好雇佣一位工人。
        - 在每一轮雇佣中，从最前面 candidates 和最后面 candidates 人中选出代价最小的一位工人，
        如果有多位代价相同且最小的工人，选择下标更小的一位工人。
            - 比方说，costs = [3,2,7,7,1,2] 且 candidates = 2 ，第一轮雇佣中，
            我们选择第 4 位工人，因为他的代价最小 [3,2,7,7,1,2] 。
            - 第二轮雇佣，我们选择第 1 位工人，因为他们的代价与第 4 位工人一样都是最小代价，
            而且下标更小，[3,2,7,7,2] 。注意每一轮雇佣后，剩余工人的下标可能会发生变化。
        - 如果剩余员工数目不足 candidates 人，那么下一轮雇佣他们中代价最小的一人，
        如果有多位代价相同且最小的工人，选择下标更小的一位工人。
        - 一位工人只能被选择一次。

        返回雇佣恰好 k 位工人的总代价。
        """
        n = len(costs)
        # 边界条件：如果 k 为 0，不需要雇佣工人
        if k == 0:
            return 0
        # 边界条件：如果 k 大于等于工人总数，雇佣所有工人
        if k >= n:
            return sum(costs)
        # 边界条件：如果 candidates 足够大，覆盖了所有工人
        if 2 * candidates >= n:
            # 在这种情况下，每轮都是从所有剩余工人中选择
            workers = [(costs[i], i) for i in range(n)]
            workers.sort()
            return sum(cost for cost, _ in workers[:k])

        # 两个最小堆：(cost, original_index)
        left_heap = []
        right_heap = []
        
        # 双指针：left 表示下一个要加入左堆的下标，right 表示下一个要加入右堆的下标
        left = 0
        right = n - 1
        
        # 初始化：将前 candidates 个加入左堆
        while left < candidates:
            heapq.heappush(left_heap, (costs[left], left))
            left += 1
        
        # 将后 candidates 个加入右堆，注意不要和左堆重叠
        while right >= left and right >= n - candidates:
            heapq.heappush(right_heap, (costs[right], right))
            right -= 1
        
        total_cost = 0
        
        # 进行 k 轮雇佣
        for _ in range(k):
            # 获取两个堆的堆顶（如果存在）
            left_val = left_heap[0] if left_heap else (float('inf'), float('inf'))
            right_val = right_heap[0] if right_heap else (float('inf'), float('inf'))
            
            # 按规则选择：代价小优先，代价相同则下标小优先
            if left_val[0] < right_val[0] or (left_val[0] == right_val[0] and left_val[1] < right_val[1]):
                cost, idx = heapq.heappop(left_heap)
                total_cost += cost
                # 如果还有人没加入左堆，则补充
                if left <= right:
                    heapq.heappush(left_heap, (costs[left], left))
                    left += 1
            else:
                cost, idx = heapq.heappop(right_heap)
                total_cost += cost
                # 如果还有人没加入右堆，则补充
                if left <= right:
                    heapq.heappush(right_heap, (costs[right], right))
                    right -= 1
        
        return total_cost
    
    def guessNumber(self, n: int) -> int:
        r"""
        我们正在玩猜数字游戏。猜数字游戏的规则如下：

        我会从 1 到 n 随机选择一个数字。 请你猜选出的是哪个数字。

        如果你猜错了，我会告诉你，我选出的数字比你猜测的数字大了还是小了。

        你可以通过调用一个预先定义好的接口 int guess(int num) 来获取猜测结果，返回值一共有三种可能的情况：

        - -1：你猜的数字比我选出的数字大 （即 num > pick）。
        - 1：你猜的数字比我选出的数字小 （即 num < pick）。
        - 0：你猜的数字与我选出的数字相等。（即 num == pick）。

        返回我选出的数字。
        """
        # 初始化双指针
        left, right = 1, n
        
        while left <= right:
            mid = (left + right) // 2
            # 调用 guess 函数获取猜测结果
            result = guess(mid)

            # 如果等于 0，则猜中了
            if result == 0:
                return mid
            # 如果等于 -1，则说明猜大了，移动右指针
            elif result == -1:
                right = mid - 1
            # 如果等于 1，则说明猜小了，移动左指针
            else:
                left = mid + 1

        return -1
    
    def successfulPairs(self, spells: List[int], 
        potions: List[int], success: int
    ) -> List[int]:
        r"""
        给你两个正整数数组 spells 和 potions ，长度分别为 n 和 m ，
        其中 spells[i] 表示第 i 个咒语的能量强度，potions[j] 表示第 j 瓶药水的能量强度。

        同时给你一个整数 success 。一个咒语和药水的能量强度 相乘 如果 大于等于 success ，
        那么它们视为一对 成功 的组合。

        请你返回一个长度为 n 的整数数组 pairs，其中 pairs[i] 是能跟第 i 个咒语成功组合的 药水 数目。
        """
        # 首先对药水进行排序
        potions.sort()
        m = len(potions)
        
        res = []

        for spell in spells:
            # 计算当前咒语需要的药水数量
            if spell > 0:
                target = success / spell
                left, right = 0, m
                # 使用二分查找找到第一个大于等于 target 的位置
                while left < right:
                    mid = (left + right) // 2
                    if potions[mid] >= target:
                        right = mid
                    else:
                        left = mid + 1
                        
                # 从left位置到末尾的所有药水都满足条件
                res.append(m - left)
            else:
                # 如果咒语能量强度为 0，则不需要药水
                if success <= 0:
                    res.append(m)
                else:
                    res.append(0)

        return res

    def findPeakElement(self, nums: List[int]) -> int:
        r"""
        峰值元素是指其值严格大于左右相邻值的元素。

        给你一个整数数组 nums，找到峰值元素并返回其索引。
        数组可能包含多个峰值，在这种情况下，返回 任何一个峰值 所在位置即可。

        你可以假设 nums[-1] = nums[n] = -∞ 。

        你必须实现时间复杂度为 O(log n) 的算法来解决此问题。
        """
        # 边界条件
        if len(nums) <= 1:
            return 0
        
        # 初始化双指针
        left, right = 0, len(nums) - 1
        
        # 二分搜索
        while left < right:
            mid = (left + right) // 2
            # 如果中间元素大于其右侧元素，说明峰值在左侧
            if nums[mid] > nums[mid + 1]:
                right = mid
            # 否则，峰值在右侧
            else:
                left = mid + 1

        return left