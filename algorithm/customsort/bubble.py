from typing import List


class Solution:
    def bubbleSort(self, nums: List[int]) -> List[int]:
        # 边界条件
        if len(nums) <= 1:
            return nums

        # 冒泡排序
        for i in range(len(nums) - 1):
            # 第 i 趟冒泡
            is_swap = False
            for j in range(len(nums) - 1 - i):
                if nums[j] > nums[j + 1]:
                    nums[j], nums[j + 1] = nums[j + 1], nums[j]
                    is_swap = True
            # 如果没有发生交换，说明已经有序，可以提前结束
            if not is_swap:
                break

        return nums


if __name__ == '__main__':
    print(Solution().bubbleSort([3, 2, 1, 5, 4]))