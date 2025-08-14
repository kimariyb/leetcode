from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
    def __str__(self):
        return str(self.val)
        

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # 边界条件
        if not head or not head.next:
            return head

        # 初始化指针
        prev, curr = None, head

        # 遍历链表
        while curr:
            # 保存当前节点的下一个节点
            next_node = curr.next
            # 将当前节点的 next 指针指向前一个节点
            curr.next = prev 
            # 将前一个节点移动到当前节点
            prev = curr
            # 将当前节点移动到下一个节点
            curr = next_node

        # 返回反转后的链表头节点
        return prev
    

if __name__ == '__main__':
    s = Solution()
    head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
    print(head)