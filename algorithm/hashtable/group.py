from collections import defaultdict
from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # 初始化一个字典，
        # 用于存储每个字符串的排序后的字符串作为键，
        # 对应的字符串列表作为值
        # {'sorted string': ['anagram1', 'anagram2', ...]}
        anagram_dict = defaultdict(list)
        
        # 遍历输入的字符串列表
        for s in strs:
            # 对每个字符串进行排序
            sorted_s = ''.join(sorted(s))
            # 将排序后的字符串作为键，将原始字符串添加到对应的值列表中
            anagram_dict[sorted_s].append(s)

        # 返回字典中所有值列表的并集
        return list(anagram_dict.values())