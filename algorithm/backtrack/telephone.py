"""
问题描述：

给定一个手机拨号盘，不同的按键对应不同的字母
现在给定数字字符串的输入，请你返回所有可能的小写字母组合
输入的数字只会有 2~9

输入："23"
输出：["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]
"""

from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        # 边界条件
        if not digits:
            return []
        
        # 初始化映射
        digit_mapping = {
            '2': ['a', 'b', 'c'],
            '3': ['d', 'e', 'f'],
            '4': ['g', 'h', 'i'],
            '5': ['j', 'k', 'l'],
            '6': ['m', 'n', 'o'],
            '7': ['p', 'q', 'r', 's'],
            '8': ['t', 'u', 'v'],
            '9': ['w', 'x', 'y', 'z']
        }

        # 初始化结果
        res = []

        # 回溯
        def backtrack(start: int, curr_str: list):
            # 循环终止条件
            if start == len(digits):
                res.append("".join(curr_str))
                return
            
            # 循环遍历
            curr_digits = digits[start]
            for char in digit_mapping[curr_digits]:
                # 选择
                curr_str.append(char)
                # 递归
                backtrack(start + 1, curr_str)
                # 撤销选择 
                curr_str.pop()
        
        backtrack(0, [])
        return res
    

if __name__ == '__main__':
    s = Solution()
    print(s.letterCombinations('23'))
    
    
