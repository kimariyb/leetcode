from typing import Dict, List, Optional
import heapq


class DLinkedNode:
    def __init__(self, key=0, value=0):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Node:
    def __init__(self, x: int, next=None, random=None):
        self.val = int(x)
        self.next: Node = next
        self.random: Node = random

        
class Solution:
    def reverseKGroup(
        self, head: Optional[ListNode], k: int
    ) -> Optional[ListNode]:
        r"""
        给你链表的头节点 head ，每 k 个节点一组进行翻转，请你返回修改后的链表。

        k 是一个正整数，它的值小于或等于链表的长度。
        如果节点总数不是 k 的整数倍，那么请将最后剩余的节点保持原有顺序。

        你不能只是单纯的改变节点内部的值，而是需要实际进行节点交换。
        """
        def hasKNodes(node, k):
            """辅助函数：检查剩余节点是否足够k个"""
            count = 0
            while node and count < k:
                node = node.next
                count += 1
            return count == k
        
        def reverseKNodes(head, k):
            """辅助函数：翻转k个节点，并返回新的头和尾"""
            prev = None
            curr = head
            # 翻转k个节点
            for _ in range(k):
                next_temp = curr.next
                curr.next = prev
                prev = curr
                curr = next_temp
            # prev是翻转后的头，head是翻转后的尾
            return prev, head, curr  # 新头，新尾，下一组的开始
        
        # 创建虚拟头节点
        dummy = ListNode(0)
        dummy.next = head
        prev_group_tail = dummy  # 前一组的尾节点
        
        while hasKNodes(prev_group_tail.next, k):
            # 当前组的头节点
            group_head = prev_group_tail.next
            
            # 翻转当前组的k个节点
            new_head, new_tail, next_group_head = reverseKNodes(group_head, k)
            
            # 连接前一组和当前组
            prev_group_tail.next = new_head
            new_tail.next = next_group_head
            
            # 更新前一组的尾节点
            prev_group_tail = new_tail
        
        return dummy.next
    
    def copyRandomList(self, head: Optional[Node]) -> Optional[Node]:
        r"""
        给你一个长度为 n 的链表，每个节点包含一个额外增加的随机指针 random ，该指针可以指向链表中的任何节点或空节点。

        构造这个链表的 深拷贝。 深拷贝应该正好由 n 个 全新 节点组成，其中每个新节点的值都设为其对应的原节点的值。
        新节点的 next 指针和 random 指针也都应指向复制链表中的新节点，并使原链表和复制链表中的这些指针能够表示相同的链表状态。
        复制链表中的指针都不应指向原链表中的节点 

        返回复制链表的头节点。

        用一个由 n 个节点组成的链表来表示输入/输出中的链表。每个节点用一个 [val, random_index] 表示：

        - val：一个表示 Node.val 的整数。
        - random_index：随机指针指向的节点索引（范围从 0 到 n-1）；
        如果不指向任何节点，则为  null 。

        你的代码 只 接受原链表的头节点 head 作为传入参数。
        """
        # 边界条件
        if not head:
            return None

        # 创建一个字典，用于存储原节点和新节点的映射关系
        node_map = {}

        # 第一次遍历链表，创建新节点并存储映射关系
        curr = head
        while curr:
            new_node = Node(curr.val)
            node_map[curr] = new_node
            curr = curr.next
        
        # 第二次遍历链表，设置新节点的 next 和 random 指针
        curr = head
        while curr:
            new_node = node_map[curr]
            new_node.next = node_map[curr.next] if curr.next else None
            new_node.random = node_map[curr.random] if curr.random else None
            curr = curr.next

        # 返回新链表的头节点
        return node_map[head]
    
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        r"""
        给你链表的头结点 head ，请将其按 升序 排列并返回 排序后的链表 。
        """
        # 归并排序
        if not head or not head.next:
            return head 
        
        def getMid(head: Optional[ListNode]):
            """使用快慢指针找到中点"""
            slow = fast = head
            prev = None

            while fast and fast.next:
                prev = slow
                slow = slow.next
                fast = fast.next.next

            # 断开链表
            prev.next = None
            return slow
        
        def merge(list1, list2):
            """合并两个有序链表"""
            dummy = ListNode(0)
            tail = dummy
            
            while list1 and list2:
                if list1.val <= list2.val:
                    tail.next = list1
                    list1 = list1.next
                else:
                    tail.next = list2
                    list2 = list2.next
                tail = tail.next
            
            # 连接剩余节点
            tail.next = list1 if list1 else list2
            
            return dummy.next
        
        # 找到链表的中间节点，并断开链表
        mid = getMid(head)
        
        # 递归排序左右两个部分
        left = self.sortList(head)
        right = self.sortList(mid)

        # 合并两个有序链表
        return merge(left, right)
    
    def mergeKLists(
        self, lists: List[Optional[ListNode]]
    ) -> Optional[ListNode]:
        r"""
        给你一个链表数组，每个链表都已经按升序排列。

        请你将所有链表合并到一个升序链表中，返回合并后的链表。
        """
        # 边界条件
        if not lists or len(lists) == 0:
            return None

        # 使用优先队列（最小堆）来合并链表
        min_heap = []
        for i, node in enumerate(lists):
            if node:
                heapq.heappush(min_heap, (node.val, i, node))
        
        # 创建虚拟头节点
        dummy = ListNode(0)
        curr = dummy

        # 合并链表
        while min_heap:
            val, i, node = heapq.heappop(min_heap)
            curr.next = node
            curr = curr.next

            # 将下一个节点加入堆中
            if node.next:
                heapq.heappush(min_heap, (node.next.val, i, node.next))

        return dummy.next
        

class LRUCache:
    r"""
    请你设计并实现一个满足  LRU (最近最少使用) 缓存 约束的数据结构。
    
    实现 LRUCache 类：
    - LRUCache(int capacity) 以 正整数 作为容量 capacity 初始化 LRU 缓存
    - int get(int key) 如果关键字 key 存在于缓存中，则返回关键字的值，否则返回 -1 。
    - void put(int key, int value)
        如果关键字 key 已经存在，则变更其数据值 value ；
        如果不存在，则向缓存中插入该组 key-value 。
        如果插入操作导致关键字数量超过 capacity ，则应该 逐出 最久未使用的关键字。

    函数 get 和 put 必须以 O(1) 的平均时间复杂度运行。
    """
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache: Dict[int, DLinkedNode] = {} # hashmap: key -> listnode

        self.head = DLinkedNode()   # 最近使用的节点
        self.tail = DLinkedNode()   # 最久未使用的节点
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key: int) -> int:
        if key in self.cache:
            # 获取节点
            node = self.cache[key]
            # 将节点移动到头部 (标记为最近使用)
            self._move_to_head(node)
            return node.value
        else:
            return -1
    
    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            # 获取节点
            node = self.cache[key]
            # 更新节点的值
            node.value = value
            # 将节点移动到头部（标记为最近使用）
            self._move_to_head(node)
        else:
            # 创建新节点
            new_node = DLinkedNode(key, value)
            
            # 添加到缓存中
            if len(self.cache) >= self.capacity:
                # 缓存已满，删除尾部节点（最久未使用）
                tail_node = self._pop_tail()
                del self.cache[tail_node.key]
            
            # 添加到新的节点到头部
            self.cache[key] = new_node
            self._add_to_head(new_node)
    
    def _add_node(self, node: DLinkedNode) -> None:
        """在头部添加节点"""
        node.prev = self.head
        node.next = self.head.next

        self.head.next.prev = node
        self.head.next = node

    def _remove_node(self, node: DLinkedNode) -> None:
        """删除节点"""
        prev_node = node.prev
        next_node = node.next
        
        prev_node.next = next_node
        next_node.prev = prev_node

    def _move_to_head(self, node: DLinkedNode) -> None:
        """将节点移动到头部"""
        self._remove_node(node)
        self._add_node(node)
    
    def _pop_tail(self) -> DLinkedNode:
        """删除尾部节点并返回"""
        tail_node = self.tail.prev
        self._remove_node(tail_node)
        return tail_node