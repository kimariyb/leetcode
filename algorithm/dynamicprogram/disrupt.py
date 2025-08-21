"""
问题描述：

使用下面描述的算法可以扰乱字符串 s 得到字符串 t

1. 如果字符串的长度为 1，算法停止；
2. 如果字符串的长度 > 1，执行下述步骤：
    a. 在一个随机下标处将字符串分割成两个非空的子字符串。即，如果已知字符串 s ，则可以将其分成两个子字符串 x 和 y ，
      其中 s = x + y 。
    b. 随机 决定是要「交换两个子字符串」还是要「保持这两个子字符串的顺序不变」。
    即，在执行这一步骤之后，s 可能是 s = x + y 或者 s = y + x 。
3. 在 x 和 y 这两个子字符串上继续从步骤 2 开始递归执行算法。

给你两个 长度相等 的字符串 s1 和 s2，判断 s2 是否是 s1 的扰乱字符串。
如果是，返回 true ；否则，返回 false 。
"""

class Solution:
    def isScramble(self, s1: str, s2: str) -> bool:
        # 边界条件 1：如果两个字符串相等，直接返回
        if s1 == s2:
            return True
        # 边界条件 2：如果两个字符串不相等，直接返回
        if len(s1) != len(s2):
            return False
        # 边界条件 3：如果两个字符串的字符种类和数量不相等，直接返回
        if sorted(s1) != sorted(s2):
            return False
        # 边界条件 4：如果两个字符串的长度为1，且两个字符串相等
        if len(s1) == 1 and s1 == s2:
            return True
        
        # 三维 DP
        n = len(s1)
        dp = [[[False for _ in range(n+1)
        ] for _ in range(n)] for _ in range(n)]

        # 初始化 dp 数组
        for i in range(n):
            for j in range(n):
                dp[i][j][1] = s1[i] == s2[j]
                
        # 状态转移方程：
        # dp[i][j][length] 表示 s1[i:i+length] 是否是 s2[j:j+length] 的扰乱字符串
        # 如果 s1[i:i+k] -> s2[j:j+k] 且 s1[i+k:i+length] -> s2[j+k:j+length]，则 dp[i][j][length] = True
        # 如果 s1[i:i+k] -> s2[j+length-k:j+length] 且 s1[i+k:i+length] -> s2[j:j+length-k]，则 dp[i][j][length] = True
        # 其中 k 是分割点

        # 遍历 dp 数组
        for length in range(2, n+1):
            # 遍历 s1 的起始位置
            for i in range(n-length+1):
                # 遍历 s2 的起始位置
                for j in range(n-length+1):
                    # 遍历分割点
                    for k in range(1, length):
                        # 情况1：没有交换位置
                        # s1[i:i+k] -> s2[j:j+k] 且 s1[i+k:i+length] -> s2[j+k:j+length]
                        if dp[i][j][k] and dp[i+k][j+k][length-k]:
                            dp[i][j][length] = True
                            break
                        # 情况2：交换位置
                        # s1[i:i+k] -> s2[j+length-k:j+length] 且 s1[i+k:i+length] -> s2[j:j+length-k]
                        if dp[i][j+length-k][k] and dp[i+k][j][length-k]:
                            dp[i][j][length] = True
                            break
                        
        return dp[0][0][n]


if __name__ == '__main__':
    s1 = "great"
    s2 = "rgeat"
    print(Solution().isScramble(s1, s2))