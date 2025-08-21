from typing import List

class Solution:
    def selectSort(self, nums: List[int]) -> List[int]:
        # 边界条件
        if len(nums) <= 1:
            return nums
        
        # 选择排序
        for i in range(len(nums) - 1):
            # 第 i 趟选择，记录未排序区间中最小值的位置
            min_idx = i
            for j in range(i + 1, len(nums)):
                if nums[j] < nums[min_idx]:
                    min_idx = j
            # 如果找到最小值的位置
            if min_idx != i:
                # 将未排序区间最小值交换到已排序区间末尾
                nums[i], nums[min_idx] = nums[min_idx], nums[i]
            
        return nums
    

if __name__ == '__main__':
    nums = [3, 2, 1, 5, 4]
    print(Solution().selectSort(nums))