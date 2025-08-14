"""
问题描述：

给你一个链表的头节点 head ，判断链表中是否有环。

如果有环，请找出环的入口节点
"""
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
        
class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # 边界条件
        if not head or not head.next:
            return None
        
        # 快慢指针
        slow = fast = head
        # 记录是否存在环
        has_cycle = False

        # 使用快慢指针法判断是否存在环
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                has_cycle = True
                break
        
        # 如果不存在环，则返回
        if not has_cycle:
            return None
        
        # 如果存在环，则找到环的入口节点
        slow = head
        while slow != fast:
            slow = slow.next
            fast = fast.next

        return slow