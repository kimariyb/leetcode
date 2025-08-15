from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        r"""
        给定一个链表的头节点  head ，返回链表开始入环的第一个节点。 如果链表无环，则返回 null。

        如果链表中有某个节点，可以通过连续跟踪 next 指针再次到达，则链表中存在环。
        为了表示给定链表中的环，评测系统内部使用整数 pos 来表示链表尾连接到链表中的位置（索引从 0 开始）。
        如果 pos 是 -1，则在该链表中没有环。
        
        注意：pos 不作为参数进行传递，仅仅是为了标识链表的实际情况。

        不允许修改 链表。
        """
        # 边界条件
        if not head or not head.next:
            return None
        
        # 快慢指针
        slow = fast = head
        # 记录是否存在环
        has_cycle = False

        # 快慢指针法判断是否存在环
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                has_cycle = True
                break

        # 如果不存在环，返回None
        if not has_cycle:
            return None
        
        # 如果存在环则找到这个环的入口
        slow = head
        while slow != fast:
            slow = slow.next
            fast = fast.next

        return slow
    
    def mergeTwoLists(
        self, list1: Optional[ListNode], list2: Optional[ListNode]
    ) -> Optional[ListNode]:
        r"""
        将两个升序链表合并为一个新的 升序 链表并返回。
        新链表是通过拼接给定的两个链表的所有节点组成的。 
        """
        # 边界条件
        if not list1:
            return list2
        if not list2:
            return list1

        # 通过递归解决问题
        if list1.val <= list2.val:
            list1.next = self.mergeTwoLists(list1.next, list2)
            return list1
        else:
            list2.next = self.mergeTwoLists(list1, list2.next)
            return list2
    
    def addTwoNumbers(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:
        r"""
        给你两个 非空 的链表，表示两个非负的整数。
        它们每位数字都是按照 逆序 的方式存储的，并且每个节点只能存储 一位 数字。

        请你将两个数相加，并以相同形式返回一个表示和的链表。

        你可以假设除了数字 0 之外，这两个数都不会以 0 开头。
        """
        # 边界条件
        if not l1:
            return l2
        if not l2:
            return l1

        # 创建一个虚拟头节点
        dummy = ListNode(0)
        curr = dummy
        carry = 0

        while l1 or l2 or carry:
            # 计算当前位的和
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            curr_sum = val1 + val2 + carry

            # 更新进位
            carry, digit = divmod(curr_sum, 10)

            # 创建新节点并连接到链表
            curr.next = ListNode(digit)
            curr = curr.next

            # 移动指针
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        return dummy.next
    
    def removeNthFromEnd(
        self, head: Optional[ListNode], n: int
    ) -> Optional[ListNode]:
        r"""
        给你一个链表，删除链表的倒数第 n 个结点，并且返回链表的头结点。
        """
        # 边界条件
        if not head:
            return None

        # 创建一个虚拟头节点
        dummy = ListNode(0)
        dummy.next = head

        # 使用快慢指针法找到倒数第 n 个节点
        slow = fast = dummy
        for _ in range(n + 1):
            fast = fast.next

        while fast:
            slow = slow.next
            fast = fast.next

        # 删除倒数第 n 个节点
        slow.next = slow.next.next

        return dummy.next
    
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        r"""
        给你一个链表，两两交换其中相邻的节点，并返回交换后链表的头节点。
        你必须在不修改节点内部的值的情况下完成本题（即，只能进行节点交换）。
        """
        # 边界条件
        if not head or not head.next:
            return head

        # 当前要交换的两个节点
        first, second = head, head.next

        # 递归交换后续节点
        first.next = self.swapPairs(second.next)

        # 交换当前两个节点
        second.next = first

        return second