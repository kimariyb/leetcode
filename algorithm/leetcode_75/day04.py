from collections import deque
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def decodeString(self, s: str) -> str:
        r"""
        给定一个经过编码的字符串，返回它解码后的字符串。

        编码规则为: k[encoded_string]，表示其中方括号内部的 encoded_string 正好重复 k 次。
        注意 k 保证为正整数。

        你可以认为输入字符串总是有效的；输入字符串中没有额外的空格，
        且输入的方括号总是符合格式要求的。

        此外，你可以认为原始数据不包含数字，所有的数字只表示重复的次数 k ，
        例如不会出现像 3a 或 2[4] 的输入。
        """
        # 初始化栈
        stack = []
        # 初始化当前数字
        cur_num = 0
        # 初始化当前字符串
        cur_str = ''

        for char in s:
            if char.isdigit():
                # 如果是数字，更新当前数字
                cur_num = cur_num * 10 + int(char)
            elif char == '[':
                # 如果是左括号，将当前数字和当前字符串入栈
                stack.append((cur_str, cur_num))
                # 重置当前数字和当前字符串
                cur_num, cur_str = 0, ''
            elif char == ']':
                # 如果是右括号，从栈中取出数字和字符串，并更新当前字符串
                prev_str, k = stack.pop()
                cur_str = prev_str + cur_str * k
            else:
                # 如果是字母，更新当前字符串
                cur_str += char

        return cur_str
    
    def predictPartyVictory(self, senate: str) -> str:
        r"""
        Dota2 的世界里有两个阵营：Radiant（天辉）和 Dire（夜魇）

        Dota2 参议院由来自两派的参议员组成。
        现在参议院希望对一个 Dota2 游戏里的改变作出决定。他们以一个基于轮为过程的投票进行。
        在每一轮中，每一位参议员都可以行使两项权利中的 一 项：

        - 禁止一名参议员的权利：参议员可以让另一位参议员在这一轮和随后的几轮中丧失 所有的权利 。
        - 宣布胜利：如果参议员发现有权利投票的参议员都是 同一个阵营的 ，
        他可以宣布胜利并决定在游戏中的有关变化。

        给你一个字符串 senate 代表每个参议员的阵营。字母 'R' 和 'D'分别代表了 Radiant（天辉）和 Dire（夜魇）。
        然后，如果有 n 个参议员，给定字符串的大小将是 n。

        以轮为基础的过程从给定顺序的第一个参议员开始到最后一个参议员结束。
        这一过程将持续到投票结束。所有失去权利的参议员将在过程中被跳过。

        假设每一位参议员都足够聪明，会为自己的政党做出最好的策略，你需要预测哪一方最终会宣布胜利并在 Dota2 游戏中决定改变。
        输出应该是 "Radiant" 或 "Dire" 。
        """
        n = len(senate)
        radiant_queue = deque()
        dire_queue = deque()

        # 初始化队列
        for i, party in enumerate(senate):
            if party == 'R':
                radiant_queue.append(i)
            elif party == 'D':
                dire_queue.append(i)

        # 开始投票
        while radiant_queue and dire_queue:
            # 比较两个队列的队首位置
            r_index = radiant_queue.popleft()
            d_index = dire_queue.popleft()

            # 位置小的先行动，禁止对方的参议员
            if r_index < d_index:
                # Radiant 参议员禁止 Dire 参议员，Radiant 参议员进入下一轮
                radiant_queue.append(r_index + n)
            else:
                # Dire 参议员禁止 Radiant 参议员，Dire 参议员进入下一轮
                dire_queue.append(d_index + n)

        # 返回胜利方
        return 'Radiant' if radiant_queue else 'Dire'
    
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        r"""
        给你一个链表的头节点 head 。
        删除 链表的 中间节点 ，并返回修改后的链表的头节点 head 。

        长度为 n 链表的中间节点是从头数起第 ⌊n / 2⌋ 个节点（下标从 0 开始），
        其中 ⌊x⌋ 表示小于或等于 x 的最大整数。

        对于 n = 1、2、3、4 和 5 的情况，中间节点的下标分别是 0、1、1、2 和 2 。
        """
        # 边界情况
        if not head or not head.next:
            return None

        # 使用快慢指针找到中间节点
        slow, fast = head, head.next.next
        
        while fast and fast.next:
            slow = slow.next # pyright: ignore[reportOptionalMemberAccess]
            fast = fast.next.next

        # 删除中间节点
        slow.next = slow.next.next # pyright: ignore[reportOptionalMemberAccess]

        return head
        
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        r"""
        给定单链表的头节点 head ，将所有索引为奇数的节点和索引为偶数的节点分别分组，
        保持它们原有的相对顺序，然后把偶数索引节点分组连接到奇数索引节点分组之后，
        返回重新排序的链表。

        第一个节点的索引被认为是 奇数 ， 第二个节点的索引为 偶数 ，以此类推。

        请注意，偶数组和奇数组内部的相对顺序应该与输入时保持一致。

        你必须在 O(1) 的额外空间复杂度和 O(n) 的时间复杂度下解决这个问题。
        """
        # 边界情况  
        if not head or not head.next:
            return head
        
        # 初始化奇偶链表指针
        odd, even = head, head.next
        even_head = even

        # 遍历链表，将奇偶节点分别连接到奇偶链表上
        while even and even.next:
            # 连接奇数结点
            odd.next = even.next
            odd = odd.next
            # 连接偶数结点
            even.next = odd.next
            even = even.next

        # 将偶数链表连接到奇数链表后
        odd.next = even_head

        return head


class RecentCounter:
    r"""
    写一个 RecentCounter 类来计算特定时间范围内最近的请求。

    请你实现 RecentCounter 类：

    - RecentCounter() 初始化计数器，请求数为 0 。
    - int ping(int t) 在时间 t 添加一个新请求，其中 t 表示以毫秒为单位的某个时间，
    并返回过去 3000 毫秒内发生的所有请求数（包括新请求）。
    确切地说，返回在 [t-3000, t] 内发生的请求数。

    保证 每次对 ping 的调用都使用比之前更大的 t 值。
    """
    def __init__(self) -> None:
        self.queue = []
    
    def ping(self, t: int) -> int:
        # 将当前时间加入队列
        self.queue.append(t)
        # 移除队列中所有小于 t-3000 的时间
        while self.queue[0] < t - 3000:
            self.queue.pop(0)
        # 返回队列中剩余的请求数
        return len(self.queue)

