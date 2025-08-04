
from collections import Counter
from typing import List


class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        r"""
        给你一个整数数组 arr，如果每个数的出现次数都是独一无二的，
        就返回 true；否则返回 false。
        """
        return len(Counter(arr)) == len(set(Counter(arr).values()))

    def closeStrings(self, word1: str, word2: str) -> bool:
        r"""
        如果可以使用以下操作从一个字符串得到另一个字符串，则认为两个字符串 接近 ：

        操作 1：交换任意两个 现有 字符。
        例如，abcde -> aecdb
        
        操作 2：将一个 现有 字符的每次出现转换为另一个 现有 字符，并对另一个字符执行相同的操作。
        例如，aacabb -> bbcbaa（所有 a 转化为 b ，而所有的 b 转换为 a ）
        
        你可以根据需要对任意一个字符串多次使用这两种操作。

        给你两个字符串，word1 和 word2 。
        如果 word1 和 word2 接近 ，就返回 true ；否则，返回 false。
        """
        # 边界条件：如果两个字符串长度不同，则不可能通过交换字符得到
        if len(word1) != len(word2):
            return False
        
        # 统计每个字符出现的次数
        freq1 = Counter(word1)
        freq2 = Counter(word2)

        # 条件1：两个字符串必须包含相同的字符集合
        # 因为操作2只能在现有字符间转换，不能引入新字符
        if set(freq1.keys()) != set(freq2.keys()):
            return False
        
        # 条件2：两个字符串的字符频率集合必须相同
        # 因为操作1可以重排字符顺序，操作2可以交换字符频率
        if sorted(freq1.values()) != sorted(freq2.values()):
            return False
        
        return True
    

    def equalPairs(self, grid: List[List[int]]) -> int:
        r"""
        给你一个下标从 0 开始、大小为 n x n 的整数矩阵 grid ，
        返回满足 Ri 行和 Cj 列相等的行列对 (Ri, Cj) 的数目。

        如果行和列以相同的顺序包含相同的元素（即相等的数组），则认为二者是相等的。
        """
        n = len(grid)

        # 统计所有行模式的频率
        row_patterns = Counter(
            tuple(row) for row in grid
        )

        # 统计所有列模式的频率
        col_patterns = Counter(
            tuple(grid[i][j] for i in range(n)) 
            for j in range(n)
        )

        # 计算匹配的对数
        count = 0
        for pattern, row_freq in row_patterns.items():
            col_freq = col_patterns.get(pattern, 0)
            count += row_freq * col_freq

        return count
    
    def removeStars(self, s: str) -> str:
        r"""
        给你一个包含若干星号 * 的字符串 s 。

        在一步操作中，你可以：
        - 选中 s 中的一个星号。
        - 移除星号 左侧 最近的那个 非星号 字符，并移除该星号自身。

        返回移除 所有 星号之后的字符串。

        注意：
        - 生成的输入保证总是可以执行题面中描述的操作。
        - 可以证明结果字符串是唯一的。
        """
        # 初始化一个栈
        stack = []

        for char in s:
            if char == '*':
                # 如果当前字符是星号，则移除栈顶元素
                if stack:
                    stack.pop()
            else:
                # 如果当前字符不是星号，则将其压入栈中
                stack.append(char)

        # 将栈中的字符拼接成字符串并返回
        return ''.join(stack)
    

    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        r"""
        给定一个整数数组 asteroids，表示在同一行的小行星。
        数组中小行星的索引表示它们在空间中的相对位置。

        对于数组中的每一个元素，其绝对值表示小行星的大小，
        正负表示小行星的移动方向（正表示向右移动，负表示向左移动）。
        每一颗小行星以相同的速度移动。

        找出碰撞后剩下的所有小行星。
        碰撞规则：两个小行星相互碰撞，较小的小行星会爆炸。
        如果两颗小行星大小相同，则两颗小行星都会爆炸。
        两颗移动方向相同的小行星，永远不会发生碰撞。
        """
        # 初始化栈
        stack = []

        for asteroid in asteroids:
            # 处理向左移动的小行星可能引起的碰撞序列
            while stack and asteroid < 0 < stack[-1]:
                # 发生碰撞
                if stack[-1] < -asteroid:
                    # 栈顶小行星爆炸
                    stack.pop()
                    continue
                elif stack[-1] == -asteroid:
                    # 两颗小行星都爆炸
                    stack.pop()
                # 当前小行星爆炸
                break
            else:
                stack.append(asteroid)

        return stack
