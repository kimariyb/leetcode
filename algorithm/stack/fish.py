"""
问题描述：

在水中有许多的鱼，可以认为这些鱼停放在x轴上。
再给定两个数组 Size，Dir，Size[i] 表示第i条鱼的大小，Dir[i] 表示鱼的方向
(0 表示向左游，1表示向右游)。
这两个数组分别表示鱼的大小和游动的方向，并且这两个数组的长度相等。
这些鱼的行为都符合以下几个条件:

1. 所有的鱼都同时开始游动，每次按照鱼的方向，都游动一个单位距离
2. 当方向相对时，大鱼会吃掉小鱼
3. 鱼的大小都不一样

请完成以下接口来计算还剩下几条鱼?
"""
from typing import List


class Solution:
    def fish(self, size: List[int], direction: List[int]) -> int:
        # 边界条件，如果只有一条鱼，则返回鱼的数量
        if len(size) <= 1:
            return len(size)

        # 初始化栈
        stack = []

        # 遍历每条鱼
        for i in range(len(size)):
            curr_size, curr_dir = size[i], direction[i]

            if curr_dir == 1:
                # 如果当前鱼向右游动，则直接入栈
                stack.append((curr_size, curr_dir))
            else:  # 向左游，可能与栈顶鱼相遇
                while stack and stack[-1][1] == 1:  # 栈顶鱼向右
                    if stack[-1][0] > curr_size:  # 栈顶鱼更大，当前鱼被吃
                        break
                    else:  # 当前鱼更大，吃掉栈顶鱼
                        stack.pop()
                else:  # 栈空或栈顶鱼向左，当前鱼存活
                    stack.append((curr_size, curr_dir))

        return len(stack)

if __name__ == '__main__':
    size = [4, 3, 2, 1, 5]
    dir = [1, 1, 1, 1, 0]
    
    print(Solution().fish(size, dir))