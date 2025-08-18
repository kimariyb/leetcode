from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        r"""
        整数数组 nums 按升序排列，数组中的值 互不相同 。

        在传递给函数之前，nums 在预先未知的某个下标 k（0 <= k < nums.length）上进行了 旋转，
        使数组变为 [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]]（下标 从 0 开始 计数）。
        例如， [0,1,2,4,5,6,7] 向左旋转 3 次后可能变为 [4,5,6,7,0,1,2] 。

        给你 旋转后 的数组 nums 和一个整数 target ，如果 nums 中存在这个目标值 target ，
        则返回它的下标，否则返回 -1 。

        你必须设计一个时间复杂度为 O(log n) 的算法解决此问题。
        """
        # 边界条件
        if not nums:
            return -1
        if len(nums) == 1:
            return 0 if nums[0] == target else -1
        
        # 二分查找
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            
            # 判断左边部分是否有序
            if nums[left] <= nums[mid]:
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            else:
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1

        return -1
    
    def findMin(self, nums: List[int]) -> int:
        r"""
        已知一个长度为 n 的数组，预先按照升序排列，经由 1 到 n 次 旋转 后，得到输入数组。
        例如，原数组 nums = [0,1,2,4,5,6,7] 在变化后可能得到：
        
        - 若旋转 4 次，则可以得到 [4,5,6,7,0,1,2]
        - 若旋转 7 次，则可以得到 [0,1,2,4,5,6,7]
        
        注意，数组 [a[0], a[1], a[2], ..., a[n-1]] 旋转一次 的结果为数组 [a[n-1], a[0], a[1], a[2], ..., a[n-2]] 。

        给你一个元素值 互不相同 的数组 nums ，它原来是一个升序排列的数组，并按上述情形进行了多次旋转。
        请你找出并返回数组中的 最小元素 。

        你必须设计一个时间复杂度为 O(log n) 的算法解决此问题。
        """
        # 边界条件
        if not nums:
            return -1
        if len(nums) == 1:
            return nums[0]

        # 二分查找
        left, right = 0, len(nums) - 1
        while left < right:
            mid = (left + right) // 2
            # 如果中间的值比右边的值小
            # 说明右边是有序的，最小值在左边
            if nums[mid] < nums[right]:
                right = mid
            # 否则需要在右边查找
            else:
                left = mid + 1

        return nums[left]
    
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        r"""
        给定两个大小分别为 m 和 n 的正序（从小到大）数组 nums1 和 nums2。
        请你找出并返回这两个正序数组的 中位数 。

        算法的时间复杂度应该为 O(log (m+n)) 。
        """
        # 边界条件
        if not nums1 and not nums2:
            return 0
        # 优化时间复杂度
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        
        m, n = len(nums1), len(nums2)
        left, right = 0, m
        
        # 二分查找合适的分割点
        while left <= right:
            # nums1 的分割点
            cut1 = (left + right) // 2
            # nums2 的分割点
            cut2 = (m + n + 1) // 2 - cut1

            max_left1 = float('-inf') if cut1 == 0 else nums1[cut1 - 1]
            min_right1 = float('inf') if cut1 == m else nums1[cut1]

            max_left2 = float('-inf') if cut2 == 0 else nums2[cut2 - 1]
            min_right2 = float('inf') if cut2 == n else nums2[cut2]
        
            # 检查是否找到正确的分割点
            if max_left1 <= min_right2 and max_left2 <= min_right1:
                # 找到了正确的分割点
                if (m + n) % 2 == 1:
                    # 奇数个元素，放回左半部分的最大值
                    return max(max_left1, max_left2)
                else:
                    # 偶数个元素，放回左半部分的最大值和右半部分的最小值的平均值
                    return (max(max_left1, max_left2) + min(min_right1, min_right2)) / 2
            elif max_left1 > min_right2:
                # 分割点太靠右，需要左移
                right = cut1 - 1
            else:
                # 分割点太靠左，需要右移
                left = cut1 + 1

        return 0
    
    def isValid(self, s: str) -> bool:
        r"""
        给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串 s ，判断字符串是否有效。

        有效字符串需满足：

        1. 左括号必须用相同类型的右括号闭合。
        2. 左括号必须以正确的顺序闭合。
        3. 每个右括号都有一个对应的相同类型的左括号。
        """
        # 边界条件
        if not s:
            return True

        # 使用栈来存储左括号
        stack = []
        # 右 -> 左 mapping
        mapping = {")": "(", "}": "{", "]": "["}

        for char in s:
            # 如果是右括号，检查栈顶是否是对应的左括号
            if char in mapping:
                top_element = stack.pop() if stack else '#'
                if mapping[char] != top_element:
                    return False
            else:
                stack.append(char)

        return not stack
    
    
class MinStack:
    r"""
    设计一个支持 push ，pop ，top 操作，并能在常数时间内检索到最小元素的栈。

    实现 MinStack 类:

    - MinStack() 初始化堆栈对象。
    - void push(int val) 将元素val推入堆栈。
    - void pop() 删除堆栈顶部的元素。
    - int top() 获取堆栈顶部的元素。
    - int getMin() 获取堆栈中的最小元素。
    """
    def __init__(self):
        self.stack = []      # 存储实际数据
        self.min_stack = []  # 存储每个位置的最小值

    def push(self, val: int) -> None:
        """将元素推入栈"""
        self.stack.append(val)
        # 更新最小值栈
        if not self.min_stack:
            self.min_stack.append(val)
        else:
            # 保存当前最小值
            self.min_stack.append(min(val, self.min_stack[-1]))

    def pop(self) -> None:
        """删除栈顶元素"""
        if self.stack:
            self.stack.pop()
            self.min_stack.pop()

    def top(self) -> int:
        """获取栈顶元素"""
        if self.stack:
            return self.stack[-1]

    def getMin(self) -> int:
        """获取栈中最小元素"""
        if self.min_stack:
            return self.min_stack[-1]
