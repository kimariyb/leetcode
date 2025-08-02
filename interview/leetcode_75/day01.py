from typing import List
from collections import defaultdict


class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        r"""
        给定字符串 s 和 t ，判断 s 是否为 t 的子序列。

        字符串的一个子序列是原始字符串删除一些（也可以不删除）
        字符而不改变剩余字符相对位置形成的新字符串。
        （例如，"ace" 是 "abcde" 的一个子序列，而 "aec" 不是）。
        """
        # 如果 s 为空，则空字符串永远为 t 的子序列
        if not s:
            return True
        # 如果 t 为空，则 s 永远不为 t 的子序列
        if not t:
            return False

        i = 0   # s 的指针
        j = 0   # t 的指针

        while i < len(s) and j < len(t):
            # 如果 s[i] == t[j] 说明有匹配字符
            if s[i] == t[j]:
                i += 1
            # t 的指针永远后移
            j += 1

        # 如果 s 的所有字符都被匹配，则 s 是 t 的子序列
        return i == len(s)
    
    def maxArea(self, height: List[int]) -> int:
        r"""
        给定一个长度为 n 的整数数组 height 。
        有 n 条垂线，第 i 条线的两个端点是 (i, 0) 和 (i, height[i]) 。

        找出其中的两条线，使得它们与 x 轴共同构成的容器可以容纳最多的水。

        返回容器可以储存的最大水量。
        """
        left, right = 0, len(height) - 1
        max_area = 0

        while left < right:
            # 计算当前容器面积
            # 面积 = 宽度 × 高度(取较短的一边)
            w = right - left
            h = min(height[left], height[right])
            area = w * h
            max_area = max(area, max_area)

            # 移动较短的那根线，因为这样才能可能找到更大的面积
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return max_area

    def maxOperations(self, nums: List[int], k: int) -> int:
        r"""
        给你一个整数数组 nums 和一个整数 k。

        每一步操作中，你需要从数组中选出和为 k 的两个整数，并将它们移出数组。

        返回你可以对数组执行的最大操作数。
        """
        # 统计每个数字的出现次数
        count = defaultdict(int)
        operations = 0

        for num in nums:
            need = k - num  # 我们需要的配对数字

            if count[need] > 0:
                # 找到了配对，执行一次操作
                operations += 1
                count[need] -= 1  # 减少配对数字的计数
            else:
                # 没有配对，将当前数字加入等待配对
                count[num] += 1

        return operations

    def findMaxAverage(self, nums: List[int], k: int) -> float:
        r"""
        给你一个由 n 个元素组成的整数数组 nums 和一个整数 k 。

        请你找出平均数最大且 长度为 k 的连续子数组，并输出该最大平均数。

        任何误差小于 10^-5 的答案都将被视为正确答案。
        """
        # 计算第一个窗口的和
        window_sum = sum(nums[:k])
        max_sum = window_sum
        # 滑动窗口：移除左边元素，添加右边元素
        for i in range(k, len(nums)):
            window_sum = window_sum - nums[i - k] + nums[i]
            max_sum = max(max_sum, window_sum)
        
        return max_sum / k
    
    def maxVowels(self, s: str, k: int) -> int:
        r"""
        给你字符串 s 和整数 k 。

        请返回字符串 s 中长度为 k 的单个子字符串中可能包含的最大元音字母数。

        英文中的 元音字母 为 (a, e, i, o, u)。
        """
        vowels = set('aeiou')

        # 计算第一个窗口中的元音字母数
        current_vowels = 0
        for i in range(k):
            if s[i] in vowels:
                current_vowels += 1 
        
        max_vowels = current_vowels

        # 滑动窗口
        for i in range(k, len(s)):
            # 移除窗口左边的字符
            if s[i - k] in vowels:
                current_vowels -= 1
            # 添加窗口右边的新字符
            if s[i] in vowels:
                current_vowels += 1
            
            max_vowels = max(max_vowels, current_vowels)
        
        # 如果已经达到最大可能值，直接返回
        if max_vowels == k:
            return k
    
        return max_vowels

if __name__ == '__main__':
    # create the object
    solve = Solution()

    