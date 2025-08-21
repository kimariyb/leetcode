from typing import List


class Solution:
    def mergeSort(self, nums: List[int]) -> List[int]:
        # 边界条件
        if len(nums) <= 1:
            return nums
        
        def _merge(left_nums: List[int], right_nums: List[int]) -> List[int]:
            res = []
            i = j = 0
            
            # 比较两个数组的元素，将较小的元素加入结果
            while i < len(left_nums) and j < len(right_nums):
                if left_nums[i] <= right_nums[j]:
                    res.append(left_nums[i])
                    i += 1
                else:
                    res.append(right_nums[j])
                    j += 1

            # 将剩余的元素加入结果
            while i < len(left_nums):
                res.append(left_nums[i])
                i += 1
            while j < len(right_nums):
                res.append(right_nums[j])
                j += 1

            return res

        # 分治
        mid = len(nums) // 2
        left_nums = self.mergeSort(nums[:mid])
        right_nums = self.mergeSort(nums[mid:])

        # 合并
        return _merge(left_nums, right_nums)
    

if __name__ == '__main__':
    nums = [5, 2, 4, 4, 6, 1, 3]
    print(Solution().mergeSort(nums))
    