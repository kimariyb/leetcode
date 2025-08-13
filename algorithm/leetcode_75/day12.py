from typing import List


class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        r"""
        给你两个单词 word1 和 word2， 
        请返回将 word1 转换成 word2 所使用的最少操作数 。

        你可以对一个单词进行如下三种操作：

        - 插入一个字符
        - 删除一个字符
        - 替换一个字符
        """
        # 边界条件
        if not word1:
            return len(word2)
        if not word2:
            return len(word1)
        
        m, n = len(word1), len(word2)
        dp = [[0] * (n + 1) for _ in range(m + 1)]

        # 初始化动态规划
        for i in range(m + 1):
            dp[i][0] = i
        for j in range(n + 1):
            dp[0][j] = j

        
        # 动态规划
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if word1[i-1] == word2[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = min(
                        dp[i-1][j] + 1,     # 删除
                        dp[i][j-1] + 1,     # 插入
                        dp[i-1][j-1] + 1    # 替换
                    )

        return dp[m][n]
    
    def countBits(self, n: int) -> List[int]:
        r"""
        给定一个非负整数 num。对于 0 ≤ i ≤ num 范围中的每个数字 i ，
        计算其二进制数中的 1 的数目并将它们作为数组返回。
        """
        dp = [0] * (n + 1)
        for i in range(1, n + 1):
            # i 的 1 的个数 = i 右移一位后的 1 的个数 + i 的最低位
            dp[i] = dp[i >> 1] + (i & 1)
        return dp
    
    def singleNumber(self, nums: List[int]) -> int:
        r"""
        给你一个 非空 整数数组 nums ，除了某个元素只出现一次以外，
        其余每个元素均出现两次。找出那个只出现了一次的元素。

        你必须设计并实现线性时间复杂度的算法来解决此问题，且该算法只使用常量额外空间。
        """
        ans = 0
        for num in nums:
            # 使用异或操作符
            # 异或操作符的特性：a ^ a = 0; a ^ 0 = a
            ans ^= num
        return ans
    
    def minFlips(self, a: int, b: int, c: int) -> int:
        r"""
        给你三个正整数 a、b 和 c。

        你可以对 a 和 b 的二进制表示进行位翻转操作，返回能够使按位或运算  
         a OR b == c  成立的最小翻转次数。

        「位翻转操作」是指将一个数的二进制表示任何单个位上的 1 变成 0 或者 0 变成 1 。
        """
        flips = 0

        # 处理所有位，直到 a, b, c 都变成 0 
        while a > 0 or b > 0 or c > 0:
            # 获取当前最高位
            bit_a = a & 1
            bit_b = b & 1
            bit_c = c & 1

            # 计算当前位的或运算结果
            or_result = bit_a | bit_b
             # 如果结果不等于c的当前位，需要翻转
            if or_result != bit_c:
                if bit_c == 1:
                    # c的当前位是1，但a|b的结果是0
                    # 只需要翻转a或b中的任意一个
                    flips += 1
                else:
                    # c的当前位是0，但a|b的结果是1
                    # 需要将a和b的当前位都变为0
                    if bit_a == 1:
                        flips += 1
                    if bit_b == 1:
                        flips += 1
            
            # 右移一位，处理下一位
            a >>= 1
            b >>= 1
            c >>= 1
        
        return flips


r"""
Trie（发音类似 "try"）或者说 前缀树 是一种树形数据结构，用于高效地存储和检索字符串数据集中的键。
这一数据结构有相当多的应用情景，例如自动补全和拼写检查。

请你实现 Trie 类：

- Trie() 初始化前缀树对象。
- void insert(String word) 向前缀树中插入字符串 word 。
- boolean search(String word) 如果字符串 word 在前缀树中，
返回 true（即，在检索之前已经插入）；否则，返回 false 。
- boolean startsWith(String prefix) 如果之前已经插入的字符串 word 的前缀之一为 prefix ，
返回 true ；否则，返回 false 。
"""
class TrieNode:
    def __init__(self):
        # 子节点数组，用于存储26个小写字母
        self.children = [None] * 26
        # 标记该节点是否为某个单词的结尾
        self.is_end_of_word = False


class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def _char_to_index(self, char):
        """将字符转换为索引"""
        return ord(char) - ord('a')
    
    def insert(self, word: str) -> None:
        """插入一个单词"""
        node = self.root
        
        # 遍历单词中的每个字符
        for char in word:
            index = self._char_to_index(char)
            
            # 如果子节点不存在，创建新节点
            if node.children[index] is None:
                node.children[index] = TrieNode()
            
            # 移动到子节点
            node = node.children[index]
        
        # 标记单词结尾
        node.is_end_of_word = True

    def search(self, word: str) -> bool:
        """搜索字符串word是否在前缀树中"""
        node = self.root
        
        # 遍历单词中的每个字符
        for char in word:
            index = self._char_to_index(char)
            
            # 如果子节点不存在，说明单词不在树中
            if node.children[index] is None:
                return False
            
            # 移动到子节点
            node = node.children[index]
        
        # 只有当到达单词结尾且该节点标记为单词结尾时才返回True
        return node.is_end_of_word
    
    def startsWith(self, prefix: str) -> bool:
        """判断是否存在以prefix为前缀的字符串"""
        node = self.root
        
        # 遍历前缀中的每个字符
        for char in prefix:
            index = self._char_to_index(char)
            
            # 如果子节点不存在，说明前缀不在树中
            if node.children[index] is None:
                return False
            
            # 移动到子节点
            node = node.children[index]
        
        # 只要能遍历完整个前缀就返回True
        return True