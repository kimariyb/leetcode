from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        r"""
        给你一个 非空 整数数组 nums ，除了某个元素只出现一次以外，
        其余每个元素均出现两次。找出那个只出现了一次的元素。

        你必须设计并实现线性时间复杂度的算法来解决此问题，且该算法只使用常量额外空间。
        """
        # 使用异或操作符
        # a ^ a = 0; a ^ 0 = a
        ans = 0
        for num in nums:
            ans ^= num
        return ans

    def majorityElement(self, nums: List[int]) -> int:
        r"""
        给定一个大小为 n 的数组 nums ，返回其中的多数元素。
        多数元素是指在数组中出现次数 大于 ⌊ n/2 ⌋ 的元素。

        你可以假设数组是非空的，并且给定的数组总是存在多数元素。
        """
        # 边界条件
        if len(nums) == 1:
            return nums[0]
        
        # 使用 Boyer-Moore 投票算法
        # 1. 初始化候选人和计数器
        # 2. 遍历数组，如果当前元素与候选人相同，计数器加一，否则计数器减一
        # 3. 如果计数器为零，则将当前元素设为新的候选人，并将计数器重置为一
        # 4. 遍历结束后，候选人即为所求
        candidate = None
        count = 0
        
        for num in nums:
            if count == 0:
                candidate = num
            count += (1 if num == candidate else -1)

        return candidate
    
    def sortColors(self, nums: List[int]) -> None:
        r"""
        给定一个包含红色、白色和蓝色、共 n 个元素的数组 nums ，
        原地 对它们进行排序，使得相同颜色的元素相邻，并按照红色、白色、蓝色顺序排列。

        我们使用整数 0、 1 和 2 分别表示红色、白色和蓝色。

        必须在不使用库内置的 sort 函数的情况下解决这个问题。
        """
        # 边界条件
        if len(nums) == 1:
            return nums
        
        # 三向切分问题，荷兰国旗问题
        left, right = 0, len(nums) - 1
        current = 0
        
        # 将小于 pivot 的元素放到左边，大于 pivot 的元素放到右边
        while current <= right:
            if nums[current] == 0:
                # 如果当前元素为 0，则将其放在左边
                nums[left], nums[current] = nums[current], nums[left]
                left += 1
                current += 1
            elif nums[current] == 1:
                # 如果当前元素为 1，则保持不变
                current += 1
            else:
                # 如果当前元素为 2，则将其放在右边
                nums[current], nums[right] = nums[right], nums[current]
                right -= 1
                # 不移动 current，因为当前元素已经被交换到右边

        return nums
    
    def nextPermutation(self, nums: List[int]) -> None:
        r"""
        整数数组的一个 排列  就是将其所有成员以序列或线性顺序排列。

        - 例如，arr = [1,2,3] ，以下这些都可以视作 arr 的排列：
        [1,2,3]、[1,3,2]、[3,1,2]、[2,3,1] 。

        整数数组的 下一个排列 是指其整数的下一个字典序更大的排列。
        更正式地，如果数组的所有排列根据其字典顺序从小到大排列在一个容器中
        ，那么数组的 下一个排列 就是在这个有序容器中排在它后面的那个排列。
        如果不存在下一个更大的排列，那么这个数组必须重排为字典序最小的排列
        （即，其元素按升序排列）。

        - 例如，arr = [1,2,3] 的下一个排列是 [1,3,2] 。
        - 类似地，arr = [2,3,1] 的下一个排列是 [3,1,2] 。
        - 而 arr = [3,2,1] 的下一个排列是 [1,2,3] ，
            因为 [3,2,1] 不存在一个字典序更大的排列。
            
        给你一个整数数组 nums ，找出 nums 的下一个排列。

        必须 原地 修改，只允许使用额外常数空间。
        """
        n = len(nums)
        if n < 2:
            return
        
        i = n - 2
        
        # 1. 从后向前找第一个下降点 nums[i] < nums[i+1]
        while i >= 0 and nums[i] >= nums[i+1]:
            i -= 1
            
        if i >= 0:
            j = n - 1

            # 2. 在 nums[i+1:] 中找到比 nums[i] 大的最小元素
            while j >= 0 and nums[j] <= nums[i]:
                j -= 1

            # 3. 交换 nums[i] 和 nums[j]
            nums[i], nums[j] = nums[j], nums[i]

        # 4. 将 nums[i+1:] 反转
        left, right = i + 1, n - 1
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1

    def findDuplicate(self, nums: List[int]) -> int:
        r"""
        给定一个包含 n + 1 个整数的数组 nums ，
        其数字都在 [1, n] 范围内（包括 1 和 n），可知至少存在一个重复的整数。

        假设 nums 只有 一个重复的整数 ，返回 这个重复的数 。

        你设计的解决方案必须 不修改 数组 nums 且只用常量级 O(1) 的额外空间。
        """
        # Floyd 判圈算法（龟兔赛跑算法）​​
        # 将数组视为一个链表，其中 nums[i]表示节点 i 指向的下一个节点。
        # 由于存在重复数，链表中必然存在环。通过快慢指针找到环的入口，即为重复数。
            
        # 边界条件
        if len(nums) < 2:
            return nums[0]

        # 使用快慢指针，寻找环的入口
        slow = fast = 0
        
        # 1. 找到相遇点
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break

        # 2. 找到环的入口
        slow = 0
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]

        return slow