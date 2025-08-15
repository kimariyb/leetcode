from typing import List
from collections import defaultdict


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        r"""
        给定一个整数数组 nums 和一个整数目标值 target，
        请你在该数组中找出 和为目标值 target  的那 两个 整数，
        并返回它们的数组下标。

        你可以假设每种输入只会对应一个答案，并且你不能使用两次相同的元素。

        你可以按任意顺序返回答案。
        """
        # 创建一个 hash map 用于存储
        # {'num': 'index'}
        mapping = defaultdict(int)

        # 遍历数组
        for i, num in enumerate(nums):
            # 计算差值
            diff = target - num
            # 如果差值在 hash map 中，则返回
            if diff in mapping:
                return [mapping[diff], i]
            # 否则将当前值和索引存入 hash map
            mapping[num] = i

        return []
    
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        r"""
        给你一个字符串数组，请你将 字母异位词 组合在一起。
        可以按任意顺序返回结果列表。
        """
        # 初始化一个 hashmap 用于存储
        # {'sorted string': ['anagrams']}
        mapping = defaultdict(list)

        # 遍历字符串数组
        for s in strs:
            # 对字符串排序
            sorted_s = ''.join(sorted(s))
            # 将排序后的字符串和原字符串存入 hashmap
            mapping[sorted_s].append(s)

        # 返回 hashmap 的值
        return list(mapping.values())

    def longestConsecutive(self, nums: List[int]) -> int:
        r"""
        给定一个未排序的整数数组 nums ，
        找出数字连续的最长序列（不要求序列元素在原数组中连续）的长度。

        请你设计并实现时间复杂度为 O(n) 的算法解决此问题。
        """
        # 初始化一个集合
        nums_set = set(nums)

        # 初始化最长连续序列长度
        longest_streak = 0

        # 遍历数组
        for num in nums_set:
            # 如果当前数字的前一个数字不在集合中，则说明当前数字是连续序列的起点
            if num - 1 not in nums_set:
                current_num = num
                current_streak = 1

                # 继续寻找连续序列
                while current_num + 1 in nums_set:
                    current_num += 1
                    current_streak += 1

                # 更新最长连续序列长度
                longest_streak = max(longest_streak, current_streak)

        return longest_streak
    
    def moveZeroes(self, nums: List[int]) -> None:
        r"""
        给定一个数组 nums，编写一个函数将所有 0 移动到数组的末尾，
        同时保持非零元素的相对顺序。

        请注意 ，必须在不复制数组的情况下原地对数组进行操作。
        """
        left = 0  # 指向下一个0应该被替换的位置
        
        # 第一步：将所有非零元素移动到前面
        for right in range(len(nums)):
            if nums[right] != 0:
                if left != right:
                    nums[left] = nums[right]
                left += 1
        
        # 第二步：将剩余位置设为0
        while left < len(nums):
            nums[left] = 0
            left += 1

    def maxArea(self, height: List[int]) -> int:
        r"""
        给定一个长度为 n 的整数数组 height 。
        有 n 条垂线，第 i 条线的两个端点是 (i, 0) 和 (i, height[i]) 。

        找出其中的两条线，使得它们与 x 轴共同构成的容器可以容纳最多的水。

        返回容器可以储存的最大水量。

        说明：你不能倾斜容器。
        """
        # 初始化
        left, right = 0, len(height) - 1
        max_area = 0

        while left < right:
            # 计算当前容器面积
            # 面积 = 宽度 × 高度(取较短的一边)
            h = min(height[left], height[right])
            w = right - left
            cur_area = h * w

            # 更新最大面积
            max_area = max(max_area, cur_area)

            # 移动较短的一边
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return max_area
