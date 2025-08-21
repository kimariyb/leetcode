from typing import List


class Solultion:
    def insertSort(self, nums: List[int]) -> List[int]:
        # 边界条件
        if len(nums) <= 1:
            return nums
        
        # 遍历无序区间，从第二个元素遍历
        for i in range(1, len(nums)):
            # 记录当前元素
            cur = nums[i]
            # 记录当前元素的前一个元素
            pre = i - 1
            # 如果当前元素小于前一个元素，则将前一个元素后移一位
            while pre >= 0 and cur < nums[pre]:
                nums[pre + 1] = nums[pre]
                pre -= 1
            # 将当前元素插入到合适的位置
            nums[pre + 1] = cur
            
        return nums
    

if __name__ == '__main__':
    s = Solultion()
    print(s.insertSort([5, 4, 3, 2, 1]))
            
