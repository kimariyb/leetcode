from typing import List


class Solution:
    def reverseWords(self, s: str) -> str:
        r"""
        给你一个字符串 s ，请你反转字符串中 单词 的顺序。

        单词 是由非空格字符组成的字符串。s 中使用至少一个空格将字符串中的 单词 分隔开。

        返回 单词 顺序颠倒且 单词 之间用单个空格连接的结果字符串。

        注意：输入字符串 s中可能会存在前导空格、尾随空格或者单词间的多个空格。
        返回的结果字符串中，单词间应当仅用单个空格分隔，且不包含任何额外的空格。
        """
        # 去除多余的空格并分割单词
        words = s.split()
        # 反转单词列表
        words.reverse()
        # 用单个空格连接
        return ' '.join(words)

    def productExceptSelf(self, nums: List[int]) -> List[int]:
        r"""
        给你一个整数数组 nums，返回 数组 answer ，
        其中 answer[i] 等于 nums 中除 nums[i] 之外其余各元素的乘积 。

        题目数据 保证 数组 nums之中任意元素的全部前缀元素和后缀的乘积都在  32 位 整数范围内。

        请 不要使用除法，且在 O(n) 时间复杂度内完成此题。
        """
        # 初始化结果数组
        res = [1] * len(nums)
        
        # 计算前缀乘积
        for i in range(1, len(nums)):
            res[i] = res[i - 1] * nums[i - 1]

        # 计算后缀乘积并累乘到结果数组中
        suffix_product = 1
        for i in range(len(nums) - 1, -1, -1):
            res[i] *= suffix_product
            suffix_product *= nums[i]
        
        return res

    def increasingTriplet(self, nums: List[int]) -> bool:
        r"""
        给你一个整数数组 nums ，判断这个数组中是否存在长度为 3 的递增子序列。

        如果存在这样的三元组下标 (i, j, k) 且满足 i < j < k ，
        使得 nums[i] < nums[j] < nums[k] ，返回 true ；否则，返回 false 。
        """
        # 边界条件
        if len(nums) < 3:
            return False
        
        # 初始化两个最小值
        first, second = float('inf'), float('inf')
        
        # 遍历数组
        for num in nums:
            # 更新第一个最小值
            if num <= first:
                # 更新 first
                first = num
            elif num <= second:
                # 更新 second
                second = num
            else:
                # 找到递增三元组，满足 first < second < num
                return True

        return False

    def compress(self, chars: List[str]) -> int:
        r"""
        给你一个字符数组 chars ，请使用下述算法压缩：

        从一个空字符串 s 开始。对于 chars 中的每组 连续重复字符 ：

        - 如果这一组长度为 1 ，则将字符追加到 s 中。
        - 则，需要向 s 追加字符，后跟这一组的长度。
        
        压缩后得到的字符串 s 不应该直接返回 ，需要转储到字符数组 chars 中。
        需要注意的是，如果组长度为 10 或 10 以上，则在 chars 数组中会被拆分为多个字符。

        请在 修改完输入数组后 ，返回该数组的新长度。

        你必须设计并实现一个只使用常量额外空间的算法来解决此问题。

        注意：数组中超出返回长度的字符无关紧要，应予忽略。
        """
        # 边界条件
        if len(chars) < 2:
            return len(chars)
        
        # 初始化指针和计数器
        write = 0
        read = 0

        # 遍历数组
        while read < len(chars):
            # 获取当前字符
            cur = chars[read]
            # 计数器加一
            count = 0
            
            # 统计当前字符的连续出现次数
            while read < len(chars) and chars[read] == cur:
                read += 1
                count += 1

            # 将当前字符写入结果数组
            chars[write] = cur
            write += 1

            # 如果当前字符的连续出现次数大于1，则将计数器写入结果数组
            if count > 1:
                # 将数字转换为字符串，然后写入
                for digit in str(count):
                    chars[write] = digit
                    write += 1

        # 返回结果数组的长度
        return write
    
    def moveZeroes(self, nums: List[int]) -> None:
        r"""
        给定一个数组 nums，编写一个函数将所有 0 移动到数组的末尾，同时保持非零元素的相对顺序。

        请注意 ，必须在不复制数组的情况下原地对数组进行操作。       
        """
        # 双指针法
        
        left = 0
        
        # 1. 将所有的非零元素移动到前面
        for right in range(len(nums)):
            if nums[right] != 0:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1

        # 2. 将后面的元素全部置为0
        while left < len(nums):
            nums[left] = 0
            left += 1