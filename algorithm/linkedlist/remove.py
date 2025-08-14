from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        

class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        # 边界条件
        if not head:
            return head

        # 创建哑节点
        dummy = ListNode(0, head)
        curr = dummy
        
        # 遍历链表
        while curr.next:
            # 如果当前节点的下一个节点的值等于 val
            if curr.next.val == val:
                # 删除下一个节点
                curr.next = curr.next.next
            else:
                curr = curr.next

        return dummy.next
        
        
        