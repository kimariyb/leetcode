from typing import List


class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        r"""
        给你两个字符串 word1 和 word2 。请你从 word1 开始，通过交替添加字母来合并字符串。
        如果一个字符串比另一个字符串长，就将多出来的字母追加到合并后字符串的末尾。

        返回 合并后的字符串 。
        """
        # 初始化结果
        res = ""
        # 初始化两个指针
        i, j = 0, 0
        
        # 当两个指针都没有到达字符串末尾时，交替添加字符
        while i < len(word1) and j < len(word2):
            res += word1[i]
            res += word2[j]
            i += 1
            j += 1

        # 如果word1还有剩余字符，追加到结果末尾
        while i < len(word1):
            res += word1[i]
            i += 1

        # 如果word2还有剩余字符，追加到结果末尾
        while j < len(word2):
            res += word2[j]
            j += 1

        return res
    
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        r"""
        对于字符串 s 和 t，只有在 s = t + t + t + ... + t + t（t 自身连接 1 次或多次）时，
        我们才认定 “t 能除尽 s”。

        给定两个字符串 str1 和 str2 。
        返回 最长字符串 x，要求满足 x 能除尽 str1 且 x 能除尽 str2 。
        """
        # 验证可行性
        if str1 + str2 != str2 + str1:
            return ""

        # 计算最大公约数
        def gcd(a: int, b: int) -> int:
            # 辗转相除法
            while a:
                a, b = b, a % b
            return a
        
        gcd_len = gcd(len(str1), len(str2))
        
        return str1[:gcd_len]
    
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        r"""
        有 n 个有糖果的孩子。给你一个数组 candies，
        其中 candies[i] 代表第 i 个孩子拥有的糖果数目，
        和一个整数 extraCandies 表示你所有的额外糖果的数量。

        返回一个长度为 n 的布尔数组 result，如果把所有的 extraCandies 给第 i 个孩子之后，
        他会拥有所有孩子中 最多 的糖果，那么 result[i] 为 true，否则为 false。

        注意，允许有多个孩子同时拥有 最多 的糖果数目。
        """
        # 找到 candies 中的最大值
        max_candies = max(candies)

        # 遍历 candies，加上额外糖果后是否能达到最大值
        result = []
        for candy in candies:
            result.append(candy + extraCandies >= max_candies)
            
        return result
    
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        r"""
        假设有一个很长的花坛，一部分地块种植了花，另一部分却没有。
        可是，花不能种植在相邻的地块上，它们会争夺水源，两者都会死去。

        给你一个整数数组 flowerbed 表示花坛，由若干 0 和 1 组成，其中 0 表示没种植花，
        1 表示种植了花。另有一个数 n ，能否在不打破种植规则的情况下种入 n 朵花？
        能则返回 true ，不能则返回 false 。
        """    
        # 边界条件
        if n == 0:
            return True
        
        count = 0
        length = len(flowerbed)
        
        # 遍历 flowerbed
        for i in range(length):
            # 检查当前位置是否可以种花
            if flowerbed[i] == 0:
                # 检查前后位置是否可以种花
                left_empty = (i == 0) or (flowerbed[i - 1] == 0)
                right_empty = (i == length - 1) or (flowerbed[i + 1] == 0)

                # 如果左右都为空，可以种花
                if left_empty and right_empty:
                    flowerbed[i] = 1
                    count += 1

                    # 如果已经种够了 n 朵花，返回 True
                    if count == n:
                        return True

        # 如果遍历完所有位置，仍然没有种够 n 朵花，返回 False
        return False
    
    def reverseVowels(self, s: str) -> str:
        r"""
        给你一个字符串 s ，仅反转字符串中的所有元音字母，并返回结果字符串。

        元音字母包括 'a'、'e'、'i'、'o'、'u'，且可能以大小写两种形式出现不止一次。
        """
        # 定义元音字母集合
        vowels = set("aeiouAEIOU")
        
        # 将字符串转换为列表，便于修改
        s = list(s)

        # 初始化两个指针
        left, right = 0, len(s) - 1
        
        while left < right:
            # 如果左指针指向的字符不是元音字母，向右移动
            while s[left] not in vowels and left < right:
                left += 1

            # 如果右指针指向的字符不是元音字母，向左移动
            while s[right] not in vowels and left < right:
                right -= 1

            # 交换左右指针指向的字符
            if left < right:
                s[left], s[right] = s[right], s[left]
                left += 1
                right -= 1

        # 将列表转换为字符串并返回
        return "".join(s)