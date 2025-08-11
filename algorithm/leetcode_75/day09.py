from encodings.punycode import T
import heapq
from typing import List


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
        