from typing import List


class Solution:
    def quickSort(self, nums: List[int]) -> List[int]:
        # 边界条件
        if len(nums) <= 1:
            return nums

        def randomPartition(nums: List[int], low: int, high: int) -> int:
            """随机选择一个基准点，将数组分为两部分，左边小于基准点，右边大于基准点"""
            import random
            # 随机选择一个基准点
            random_index = random.randint(low, high)
            # 将基准点放到最右边
            nums[random_index], nums[high] = nums[high], nums[random_index]
            
            # 以最后一个元素为基准点（关键修正）
            pivot = nums[high]
            i = low - 1  # 小于基准的区域的边界
            
            # 遍历数组，将小于基准的元素移到左边
            for j in range(low, high):
                if nums[j] <= pivot:
                    i += 1
                    nums[i], nums[j] = nums[j], nums[i]
            
            # 将基准元素放到正确位置
            nums[i + 1], nums[high] = nums[high], nums[i + 1]
            return i + 1
        
        def _qSort(nums: List[int], low: int, high: int) -> None:
            if low < high:
                # 随机选择一个基准点，将数组分为两部分，左边小于基准点，右边大于基准点
                pivot = randomPartition(nums, low, high)
                # 对左边部分进行排序
                _qSort(nums, low, pivot - 1)
                # 对右边部分进行排序
                _qSort(nums, pivot + 1, high)

        _qSort(nums, 0, len(nums) - 1)
        return nums

    
# 测试
if __name__ == '__main__':
    nums = [3, 6, 8, 10, 1, 2, 1]
    solution = Solution()
    print(solution.quickSort(nums))
    # 输出: [1, 1, 2, 3, 6, 8, 10]