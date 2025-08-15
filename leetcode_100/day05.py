from typing import List, Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        r"""
        编写一个高效的算法来搜索 m x n 矩阵 matrix 中的一个目标值 target 。
        该矩阵具有以下特性：

        - 每行的元素从左到右升序排列。
        - 每列的元素从上到下升序排列。
        """
        # 边界条件
        if not matrix or not matrix[0]:
            return False

        m, n = len(matrix), len(matrix[0])
        # 从右上角开始查找
        left, right = 0, n - 1

        while left < m and right >= 0:
            if matrix[left][right] == target:
                return True
            elif matrix[left][right] > target:
                # 如果当前值要比 target 大
                # 那么需要检索的 target 不可能在当前列
                right -= 1
            else:
                # 如果当前值要比 target 小
                # 那么需要检索的 target 不可能在当前行
                left += 1

        return False
    
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        r"""
        给你两个单链表的头节点 headA 和 headB ，请你找出并返回两个单链表相交的起始节点。
        如果两个链表不存在相交节点，返回 null 。
        """
        # 边界条件
        if not headA or not headB:
            return None

        # 两个指针分别指向两个链表的头节点
        pA, pB = headA, headB

        # 当两个指针不相等时，继续遍历
        while pA != pB:
            # 如果指针 pA 不为空，则移动到下一个节点；否则移动到链表 B 的头节点
            pA = pA.next if pA else headB
            # 如果指针 pB 不为空，则移动到下一个节点；否则移动到链表 A 的头节点
            pB = pB.next if pB else headA

        # 当两个指针相等时，返回相交的节点
        return pA
    
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        r"""
        给你单链表的头节点 head ，请你反转链表，并返回反转后的链表。
        """
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
            curr.next = prev # type: ignore
            # 将前一个节点移动到当前节点
            prev = curr
            # 将当前节点移动到下一个节点
            curr = next_node

        # 返回反转后的链表头节点
        return prev
    
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        r"""
        给你一个单链表的头节点 head ，请你判断该链表是否为回文链表。
        如果是，返回 true ；否则，返回 false 。
        """
        # 边界条件
        if not head or not head.next:
            return True

        # 使用数组保存
        values = []
        current = head
        while current:
            values.append(current.val)
            current = current.next

        # 判断是否为回文
        return values == values[::-1]

    def hasCycle(self, head: Optional[ListNode]) -> bool:
        r"""
        给你一个链表的头节点 head ，判断链表中是否有环。

        如果链表中有某个节点，可以通过连续跟踪 next 指针再次到达，则链表中存在环。
        为了表示给定链表中的环，评测系统内部使用整数 pos 来表示链表尾连接到链表中的位置（索引从 0 开始）。
        注意：pos 不作为参数进行传递 。仅仅是为了标识链表的实际情况。

        如果链表中存在环 ，则返回 true 。 否则，返回 false 。
        """
        # 边界条件
        if not head or not head.next:
            return False

        # 使用快慢指针
        slow = fast = head
        while fast and fast.next:
            slow = slow.next # type: ignore
            fast = fast.next.next
            if slow == fast:
                return True

        return False