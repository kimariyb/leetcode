
from collections import Counter


class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        # 边界条件
        if len(word1) != len(word2):
            return False

        # 统计两个字符串中每个字符出现的次数
        freq1 = Counter(word1)
        freq2 = Counter(word2)

        # 条件 1：两个字符串必须包含相同的字符集合
        if set(freq1.keys()) != set(freq2.keys()):
            return False

        # 条件 2：两个字符串中每个字符出现的次数必须相同
        if sorted(freq1.values()) != sorted(freq2.values()):
            return False

        return True