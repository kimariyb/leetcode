from typing import List
from collections import Counter, defaultdict


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        r"""
        给你一个整数数组 nums ，判断是否存在三元组 
        [nums[i], nums[j], nums[k]] 满足 i != j、i != k 且 j != k ，
        同时还满足 nums[i] + nums[j] + nums[k] == 0 。
        
        请你返回所有和为 0 且不重复的三元组。

        注意：答案中不可以包含重复的三元组。
        """
        # 边界情况
        if len(nums) < 3:
            return []
        
        # 对数组进行排序
        nums.sort()

        # 初始化结果列表
        res = []

        # 遍历数组
        for i in range(len(nums) - 2):
            # 如果最小值都大于 0，则跳出
            if nums[i] > 0:
                break

            # 如果当前值与前一个值相同，则跳过
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            # 初始化左右指针
            left, right = i + 1, len(nums) - 1
            target = -nums[i]

            while left < right:
                current_sum = nums[left] + nums[right]
                if current_sum == target:
                    res.append([nums[i], nums[left], nums[right]])

                    # 移动左右指针，跳过重复值
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1

                    left += 1
                    right -= 1
                elif current_sum < target:
                    left += 1
                else:
                    right -= 1

        return res
    
    def trap(self, height: List[int]) -> int:
        r"""
        给定 n 个非负整数表示每个宽度为 1 的柱子的高度图，
        计算按此排列的柱子，下雨之后能接多少雨水。
        """
        # 边界条件
        if len(height) < 3 or not height:
            return 0
        
        # 初始化左右指针和结果
        left, right = 0, len(height) - 1
        left_max, right_max = 0, 0
        res = 0
        
        # 遍历数组
        while left < right:
            # 更新左右最大值
            left_max = max(left_max, height[left])
            right_max = max(right_max, height[right])

            # 根据左右最大值决定移动方向
            if left_max < right_max:
                # 左边较小，计算左边位置的雨水
                res += left_max - height[left]
                left += 1
            else:
                # 右边较小，计算右边位置的雨水
                res += right_max - height[right]
                right -= 1

        return res
    
    def lengthOfLongestSubstring(self, s: str) -> int:
        r"""
        给定一个字符串 s ，请你找出其中不含有重复字符的 最长 子串 的长度。
        """
        # 边界条件
        if not s:
            return 0
        
        # 初始化滑动窗口和结果
        window = set()
        left, max_len = 0, 0

        for right, char in enumerate(s):
            # 如果字符在窗口中，则移动左指针
            while char in window:
                window.remove(s[left])
                left += 1
            # 更新窗口和结果
            window.add(char)
            max_len = max(max_len, right - left + 1)

        return max_len
    
    def findAnagrams(self, s: str, p: str) -> List[int]:
        r"""
        给定两个字符串 s 和 p，找到 s 中所有 p 的 异位词 的子串，
        返回这些子串的起始索引。不考虑答案输出的顺序。
        """
        # 边界条件
        s_len, p_len = len(s), len(p)
        if s_len < p_len:
            return []
        
        res = []

        # 初始化统计 p 中每个字符的频次
        p_count = Counter(p)

        # 初始化窗口的字符频次
        window_count = Counter(s[:p_len])

        # 检查初始窗口
        if window_count == p_count:
            res.append(0)

        # 滑动窗口
        for i in range(p_len, len(s)):
            # 添加新字符
            window_count[s[i]] += 1
            
            # 移除旧字符
            window_count[s[i - p_len]] -= 1
            if window_count[s[i - p_len]] == 0:
                del window_count[s[i - p_len]]
            
            # 检查当前窗口
            if window_count == p_count:
                res.append(i - p_len + 1)

        return res
    
    def subarraySum(self, nums: List[int], k: int) -> int:
        r"""
        给你一个整数数组 nums 和一个整数 k ，
        请你统计并返回 该数组中和为 k 的子数组的个数 。

        子数组是数组中元素的连续非空序列。
        """
        prefix_sum_count = defaultdict(int)
        # 前缀和为 0 出现 1 次
        prefix_sum_count[0] = 1

        current_sum = 0
        res = 0

        for num in nums:
            current_sum += num

            # 检查是否存在前缀和为 current_sum - k
            res += prefix_sum_count[current_sum - k]

            # 更新前缀和计数
            prefix_sum_count[current_sum] += 1

        return res