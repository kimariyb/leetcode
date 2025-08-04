from typing import List


class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        r"""
        给定一个二进制数组 nums 和一个整数 k，假设最多可以翻转 k 个 0 ，
        则返回执行操作后 数组中连续 1 的最大个数 。
        """
        # 处理边界情况
        if not nums:
            return 0
        if k >= len(nums):
            return len(nums)

        left = 0
        zero_count = 0
        max_len = 0

        # 滑动窗口
        for right in range(len(nums)):
            # 扩展窗口
            if nums[right] == 0:
                zero_count += 1
            # 缩小窗口
            while zero_count > k:
                if nums[left] == 0:
                    zero_count -= 1
                left += 1
            # 更新结果
            max_len = max(max_len, right - left + 1)

        return max_len

    def longestSubarray(self, nums: List[int]) -> int:
        r"""
        给你一个二进制数组 nums ，你需要从中删掉一个元素。

        请你在删掉元素的结果数组中，返回最长的且只包含 1 的非空子数组的长度。

        如果不存在这样的子数组，请返回 0 。
        """
        # 边界情况
        if not nums:
            return 0
        if len(nums) == 1:
            return 0
        # 特殊情况，如果全为 1
        if all(num == 1 for num in nums):
            return len(nums) - 1
        
        left = 0
        zero_count = 0
        max_len = 0

        # 滑动窗口法
        for right in range(len(nums)):
            # 扩展窗口
            if nums[right] == 0:
                zero_count += 1
            # 缩小窗口
            while zero_count > 1:
                if nums[left] == 0:
                    zero_count -= 1
                left += 1
            # 更新结果，有效长度 = 窗口长度 - 1（删除一个元素）
            max_len = max(max_len, right - left + 1 - 1)

        return max_len

    def largestAltitude(self, gain: List[int]) -> int:
        r"""
        有一个自行车手打算进行一场公路骑行，这条路线总共由 n + 1 个不同海拔的点组成。
        自行车手从海拔为 0 的点 0 开始骑行。

        给你一个长度为 n 的整数数组 gain ，
        其中 gain[i] 是点 i 和点 i + 1 的 净海拔高度差（0 <= i < n）。
        
        请你返回 最高点的海拔 。
        """
        # 边界条件
        if not gain:
            return 0
        
        current_altitude = 0
        max_altitude = 0

        for diff in gain:
            current_altitude += diff
            max_altitude = max(max_altitude, current_altitude)
        
        return max_altitude
    
    def pivotIndex(self, nums: List[int]) -> int:
        r"""
        给你一个整数数组 nums ，请计算数组的 中心下标 。

        数组 中心下标 是数组的一个下标，其左侧所有元素相加的和等于右侧所有元素相加的和。

        如果中心下标位于数组最左端，那么左侧数之和视为 0 ，因为在下标的左侧不存在元素。
        这一点对于中心下标位于数组最右端同样适用。

        如果数组有多个中心下标，应该返回 最靠近左边 的那一个。如果数组不存在中心下标，返回 -1 。
        """
        # 边界条件
        if not nums:
            return -1
        if len(nums) == 1:
            return 0
        
        total_sum = sum(nums)
        left_sum = 0

        for i in range(len(nums)):
            # 右侧和 = 总和 - 左侧和 - 当前元素
            if left_sum == total_sum - left_sum - nums[i]:
                return i
            left_sum += nums[i]

        return -1

    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        r"""
        给你两个下标从 0 开始的整数数组 nums1 和 nums2 ，
        请你返回一个长度为 2 的列表 answer ，其中：

        - answer[0] 是 nums1 中所有 不 存在于 nums2 中的 不同 整数组成的列表。
        - answer[1] 是 nums2 中所有 不 存在于 nums1 中的 不同 整数组成的列表。

        注意：列表中的整数可以按 任意 顺序返回。
        """
        return [
            list(set(nums1) - set(nums2)),
            list(set(nums2) - set(nums1))
        ]
