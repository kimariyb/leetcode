"""
问题描述：

给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串 s ，判断字符串是否有效。
"""

class Solution:
    def isValid(self, s: str) -> bool:
        # 边界条件，如果字符串为空或者长度为奇数，则返回 False
        if not s or len(s) % 2 != 0:
            return False
        
        # 初始化一个 stack
        stack = []
        # 定义一个字典，用于存储括号对
        bracket_dict = {')': '(', '}': '{', ']': '['}
        # 遍历字符串
        for char in s:
            # 如果是左括号，则入栈
            if char in "([{":
                stack.append(char)
            # 如果是右括号，则判断栈顶元素是否匹配
            else:
                # 如果不是空栈，且最后一个元素匹配，则出栈
                if stack and stack[-1] == bracket_dict[char]:
                    stack.pop()
                else:
                    return False
                
        # 如果栈为空，则说明所有括号都匹配
        return not stack
                
        
if __name__ == '__main__':
    s = Solution()
    
    # 测试用例
    test_cases = ["()", "()[]{}", "(]", "([)]", "{[]}", "([{}])"]
    for case in test_cases:
        print(f"Case: {case}, Result:", s.isValid(case))
