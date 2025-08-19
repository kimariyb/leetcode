"""
问题描述：

给定两个字符串 s1 和 s2，给出 s1 字符串中的最短子串，
要能够包含 s2 字符串中的所有字符
"""
from collections import Counter, defaultdict


class Solution:
    def minWindow(self, s1: str, s2: str) -> str:
        # 边界条件
        if not s1 or not s2:
            return ""

        
        need = Counter(s2) # s2 的字符频率
        window = defaultdict(int) # 窗口中的字符频率

        left, valid = 0, 0 # 窗口左边界和匹配的字符数
        min_len = float('inf') # 最短字符串的长度
        start = 0 # 最短字符串的起始位置

        for right in range(len(s1)):
            # 右边界字符加入窗口
            c = s1[right]
            if c in need:
                window[c] += 1
                if window[c] == need[c]:
                    valid += 1

            # 当窗口覆盖 s2 时，尝试收缩左边界
            while valid == len(need):
                # 更新最短子串
                if right - left + 1 < min_len:
                    min_len = right - left + 1
                    start = left

                # 左边界字符移出窗口
                d = s1[left]
                if d in need:
                    if window[d] == need[d]:
                        valid -= 1
                    window[d] -= 1
                left += 1

        return "" if min_len == float('inf') else s1[start: start + min_len]


if __name__ == '__main__':
    s1 = "ADOBECODEBANC"
    s2 = "ABC"
    print(Solution().minWindow(s1, s2))
    # 输出：BANC