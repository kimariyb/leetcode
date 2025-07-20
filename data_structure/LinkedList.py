"""
链表是一系列数据元素，它们通过链接连接在一起。 每个数据元素都以指针的形式包含到另一个数据元素的连接。
它的特点是插入与删除数据十分方便，但寻找与读取数据的表现欠佳。Python 的标准库中没有链表。

链表分为单向链表和双向链表。

单向链表只能从第一个数据元素开始向前遍历。任意两个数据元素之间只有一个链接。

双向链表具有一下特点：
- 包含一个名为 first 和 last 的链接元素。
- 每个链接都带有一个数据字段和两个名为 next 和 prev 的链接字段。
- 每个链接都使用其 next 链接与其下一个链接链接。
- 每个链接都使用其 prev 链接与其上一个链接链接。
- 最后一个链接携带一个 None 链接来标记列表的结尾。

=== 单向链表 ===
初始化单向链表：None

向单向链表前添加'星期一'、'星期二'...
更新后单向链表：星期二 -> 星期一 -> None

向单向链表后添加'星期三'...
更新后单向链表：星期二 -> 星期一 -> 星期三 -> 星期四 -> None

从单向链表移除元素...
更新后单向链表：星期二 -> 星期一 -> 星期三 -> None

再次从单向链表移除元素...
更新后单向链表：星期一 -> 星期三 -> None

向单向链表中的第二个位置添加'星期五'...
更新后单向链表：星期一 -> 星期三 -> 星期五 -> None

=== 双向链表 ===
初始化双向链表：None

向双向链表前添加'星期一'、'星期二'、'星期三'...
更新后双向链表： None <-> 星期三 <-> 星期二 <-> 星期一 <-> None

向双向链表后添加'星期四'、'星期五'...
更新后双向链表： None <-> 星期三 <-> 星期二 <-> 星期一 <-> 星期四 <-> 星期五 <-> None

从单向链表移除元素'星期四'...
更新后单向链表： None <-> 星期三 <-> 星期二 <-> 星期一 <-> 星期五 <-> None

向单向链表中的第二个位置添加'星期四'...
更新后单向链表： None <-> 星期三 <-> 星期二 <-> 星期四 <-> 星期一 <-> 星期五 <-> None
"""
from typing import Optional


class UnidirectNode(object):
    def __init__(self, data=None):
        self.data = data
        self.next: Optional[UnidirectNode] = None


class BidirectNode(object):
    def __init__(self, data=None):
        self.data = data
        self.prev: Optional[BidirectNode] = None
        self.next: Optional[BidirectNode] = None


class SinglyLinkedList(object):
    def __init__(self):
        self.head: Optional[UnidirectNode] = None

    def __str__(self):
        if self.head is None:
            return 'Empty Linked List'

        nodes = []
        current = self.head
        while current is not None:
            nodes.append(str(current.data))
            current = current.next

        return ' -> '.join(nodes) + ' -> None'

    def __len__(self):
        current = self.head
        count = 0
        while current is not None:
            count += 1
            current = current.next
        return count

    def iter_list(self):
        current = self.head
        while current is not None:
            print(current.data)
            current = current.next

    def push(self, val):
        # 在链表头部添加数据
        new_node = UnidirectNode(val)
        new_node.next = self.head
        self.head = new_node

    def append(self, val):
        # 在链表尾部添加数据
        new_node = UnidirectNode(val)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next is not None:
                current = current.next # 获取最后一个节点

            current.next = new_node

    def is_exist(self, val) -> bool:
        current = self.head
        while current is not None:
            if current.data == val:
                return True
            current = current.next
        return False

    def is_empty(self) -> bool:
        return self.head is None

    def remove(self, val):
        current = self.head  # 当前检查的节点
        prev_node = None  # 当前节点的前驱节点

        # 处理头节点就是要删除的节点的情况
        if current is not None and current.data == val:
            self.head = current.next  # 将头节点指向下一个节点
            current = None  # 原头节点将被垃圾回收
            return

        # 遍历链表寻找要删除的节点
        while current is not None:
            if current.data == val:
                break  # 找到要删除的节点
            prev_node = current  # 保存前驱节点
            current = current.next  # 移动到下一个节点

        if current is None:
            return

        prev_node.next = current.next
        current = None  # 当前节点将被垃圾回收

    def insert(self, index: int, value):
        # 如果 index 小于 0 则插入在链表头
        if index <= 0:
            self.push(value)
            return

        # 处理索引大于等于链表长度的情况（插入尾部）
        if index >= len(self):
            self.append(value)  # 使用已有的尾部插入方法
            return

        # 常规情况：在链表中间插入
        current = self.head
        count = 0
        # 遍历到要插入位置的前一个节点
        while current is not None and count < index - 1:
            current = current.next
            count += 1

        # 创建新节点并插入
        new_node = UnidirectNode(value)
        new_node.next = current.next  # 新节点指向原位置的节点
        current.next = new_node  # 前一个节点指向新节点


class DoublyLinkedList(object):
    def __init__(self):
        self.head: Optional[BidirectNode] = None
        self.tail: Optional[BidirectNode] = None

    def __str__(self):
        if self.head is None:
            return 'Empty Doubly Linked List'
        nodes = []
        current = self.head

        while current is not None:
            nodes.append(str(current.data))
            current = current.next

        return ' None <-> ' + ' <-> '.join(nodes) + ' <-> None'

    def __len__(self):
        current = self.head
        count = 0
        while current is not None:
            count += 1
            current = current.next

        return count

    def iter_list(self):
        if self.is_empty():
            print("Empty Doubly Linked List")
            return

        current = self.head
        print("None <-> ", end="")
        while current is not None:
            print(current.data, end=" <-> ")
            current = current.next
        print("None")

    def push(self, val):
        """在链表头部插入节点(头插法)"""
        new_node = BidirectNode(val)

        if self.is_empty():
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

    def append(self, val):
        """在链表尾部追加节点(尾插法)"""
        new_node = BidirectNode(val)

        if self.is_empty():
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node

    def insert(self, index: int, val):
        """在指定位置插入节点"""
        if index < 0 or index > len(self):
            raise IndexError("Index out of range")

        if index == 0:
            self.push(val)
        elif index == len(self):
            self.append(val)
        else:
            new_node = BidirectNode(val)
            current = self.head

            # 移动到要插入位置的前一个节点
            for _ in range(index - 1):
                current = current.next

            # 更新节点指针
            new_node.next = current.next
            new_node.prev = current
            current.next.prev = new_node
            current.next = new_node

    def remove(self, val):
        """删除链表中第一个匹配值的节点"""
        if self.is_empty():
            raise ValueError("Cannot remove from empty list")

        current = self.head

        while current is not None:
            if current.data == val:
                if current.prev is not None:  # 不是头节点
                    current.prev.next = current.next
                else:  # 是头节点
                    self.head = current.next

                if current.next is not None:  # 不是尾节点
                    current.next.prev = current.prev
                else:  # 是尾节点
                    self.tail = current.prev

                return

            current = current.next

        raise ValueError(f"Value {val} not found in the list")

    def is_empty(self) -> bool:
        """检查链表是否为空"""
        return self.head is None

    def is_exist(self, val) -> bool:
        current = self.head

        while current is not None:
            if current.data == val:
                return True
            current = current.next
        return False


if __name__ == "__main__":
    print("\n=== 单向链表 ===")
    print("初始化单向链表：None")
    linked_list = SinglyLinkedList()

    print("\n向单向链表前添加'星期一'、'星期二'...")
    linked_list.push('星期一')
    linked_list.push('星期二')
    print(f"更新后单向链表：{linked_list}")

    print("\n向单向链表后添加'星期三'...")
    linked_list.append('星期三')
    linked_list.append('星期四')
    print(f"更新后单向链表：{linked_list}")

    print("\n从单向链表移除元素...")
    linked_list.remove('星期四')
    print(f"更新后单向链表：{linked_list}")

    print("\n再次从单向链表移除元素...")
    linked_list.remove('星期二')
    print(f"更新后单向链表：{linked_list}")

    print("\n向单向链表中的第二个位置添加'星期五'...")
    linked_list.insert(2, '星期五')
    print(f"更新后单向链表：{linked_list}")

    print("\n=== 双向链表 ===")
    print("初始化双向链表：None")
    linked_list = DoublyLinkedList()

    print("\n向双向链表前添加'星期一'、'星期二'、'星期三'...")
    linked_list.push('星期一')
    linked_list.push('星期二')
    linked_list.push('星期三')
    print(f"更新后双向链表：{linked_list}")

    print("\n向双向链表后添加'星期四'、'星期五'...")
    linked_list.append('星期四')
    linked_list.append('星期五')
    print(f"更新后双向链表：{linked_list}")

    print("\n从单向链表移除元素'星期四'...")
    linked_list.remove('星期四')
    print(f"更新后单向链表：{linked_list}")

    print("\n向单向链表中的第二个位置添加'星期四'...")
    linked_list.insert(2, '星期四')
    print(f"更新后单向链表：{linked_list}")
