"""
问题描述：

给你一个数组 nums，它是一个大小为 2 \times n 的正整数数组。你必须对这个数组执行 n 次操作
在第 i 次 操作时（编号从 1 开始），你需要：
1. 选择两个元素 x 和 y
2. 获得分数 i \times gcd(x,y)
3. 将 x 和 y 从 nums 中删除

请你返回 n 次操作后你能获得的分数和最大为多少。函数 gcd(x,y) 是 x 和 y 的最大公约数。
"""
from typing import List
from math import gcd

class Solution:
    def maxScore(self, nums: List[int]) -> int:
        # 边界条件
        if len(nums) < 2:
            return 0
    
        # 动态规划初始化
        n = len(nums) // 2  # 需要选择的对数
        # dp[i][mask]表示已经选出i对数字，且选中数字的状态为mask时的最大得分
        # mask是一个二进制数，每一位表示对应位置的数字是否被选中
        # 例如，mask=1010(二进制)表示第1和第3个数字被选中
        dp = [[0] * (1 << (2 * n)) for _ in range(n + 1)]
        
        # 动态规划过程
        # 外层循环：当前选择第几对数字（从1到n）
        for i in range(1, n + 1):
            # 中层循环：遍历所有可能的mask状态
            for mask in range(1 << (2 * n)):
                # 计算当前mask中1的个数（即已经选中的数字数量）
                cnt = bin(mask).count('1')
                # 如果当前选中的数字数量不等于2i（因为每对需要2个数字），则跳过
                if cnt != 2 * i:
                    continue
                
                # 内层循环：遍历所有可能的数字对(j,k)
                for j in range(2 * n):
                    # 如果第j个数字没有被选中，则跳过
                    if mask & (1 << j):
                        for k in range(j + 1, 2 * n):
                            # 如果第k个数字没有被选中，则跳过
                            if mask & (1 << k):
                                # 计算选择j和k这对数字的得分
                                # 1. 计算不包含j和k的mask状态：mask ^ (1 << j) ^ (1 << k)
                                # 2. 获取前i-1对数字的得分：dp[i-1][mask_without_j_and_k]
                                # 3. 计算当前对的得分：i * gcd(nums[j], nums[k])
                                # 4. 更新当前状态的得分
                                dp[i][mask] = max(
                                    dp[i][mask], 
                                    dp[i - 1][mask ^ (1 << j) ^ (1 << k)] + i * gcd(nums[j], nums[k])
                                )
        # 返回结果：选择了n对数字且所有数字都被选中的最大得分
        # (1 << (2 * n)) - 1 表示所有数字都被选中的mask状态
        return dp[n][(1 << (2 * n)) - 1]
        

if __name__ == '__main__':
    nums = [1,2,3,4,5,6]
    s = Solution()
    print(s.maxScore(nums))