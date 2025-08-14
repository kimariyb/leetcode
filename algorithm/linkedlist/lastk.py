"""
问题描述：

给定一个链表，删除链表中的倒数第 k 个节点
"""
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # 边界条件
        if not head:
            return head
        
        # 创建一个 dummy
        dummy = ListNode(0)
        dummy.next = head
        
        # 快慢指针
        slow = fast = dummy
        
        # 快指针先走 k 步
        for _ in range(k + 1):
            fast = fast.next

        # 快慢指针同时走，直到快指针到达链表末尾
        while fast.next:
            slow = slow.next
            fast = fast.next

        # 删除倒数第 k 个节点
        slow.next = slow.next.next

        return head