"""
问题描述：

给定一个字符串 s，找到它的最长无重复字符的子串的长度。
"""
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # 边界条件
        if not s:
            return 0
        if len(s) == 1:
            return 1
        
        # 初始化
        left, max_len = 0, 0
        char_index = {}  # 记录字符的最后出现位置
        
        for right in range(len(s)):
            if s[right] in char_index and char_index[s[right]] >= left:
                # 直接跳到重复字符的下一个位置
                left = char_index[s[right]] + 1
            char_index[s[right]] = right # 更新字符位置
            max_len = max(max_len, right - left + 1) # 更新最大长度

        return max_len
    
    
if __name__ == '__main__':
    s = Solution()
    print(s.lengthOfLongestSubstring("abcabcbb"))  # 输出 3