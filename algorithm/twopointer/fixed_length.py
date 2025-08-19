"""
问题描述：

给定两个字符串 s1 和 s2，判断 s2 字符串是否包含 s1 字符串的任意排列
"""
from collections import Counter, defaultdict


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # 边界条件：如果 s1 为空，返回 True
        if not s1:
            return True
        # 边界条件：如果 s2 为空，返回 False
        if not s2:
            return False
        
        need = Counter(s1) # s1 的字符频率
        window = defaultdict(int) # 窗口内的字符频率
        left, valid = 0, 0 # 窗口左边界和匹配的字符数

        for right in range(len(s2)):
            c = s2[right]
            if c in need:
                window[c] += 1
                if window[c] == need[c]:
                    valid += 1
            # 窗口长度 >= s1 的长度时，开始收缩窗口
            while (right - left + 1) >= len(s1):
                # 如果窗口内的字符频率与 s1 的字符频率完全匹配，返回 True
                if valid == len(need):
                    return True
                # 窗口左边界字符
                d = s2[left]
                # 如果该字符是 s1 需要的字符
                if d in need:
                    if window[d] == need[d]:
                        valid -= 1 # 如果之前是完美匹配，现在不再匹配
                    window[d] -= 1 # 从窗口频率中移除该字符
                left += 1
        return False


if __name__ == '__main__':
    s1 = "ab"
    s2 = "eidbaooo"
    s = Solution()
    print(s.checkInclusion(s1, s2))