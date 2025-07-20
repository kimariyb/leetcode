"""
在英语词典中，单词 stack 的意思是将对象排列在另一个之上。 这与在此数据结构中分配内存的方式相同。
它以类似的方式存储数据元素，就像一堆盘子在厨房里一个叠一个地存储一样。
所以堆栈数据结构允许在可以称为堆栈顶部的一端进行操作。我们只能从堆栈的这一端添加元素或移除元素。

在堆栈中，顺序最后插入的元素将首先出现，因为我们只能从堆栈顶部移除。
这种功能被称为后进先出（LIFO）功能。添加和删除元素的操作称为 PUSH 和 POP。

=== 测试堆栈（后进先出）===
初始化堆栈：[]

向堆栈添加'星期一'、'星期二'以及'星期三'...
当前堆栈内容：['星期三', '星期二', '星期一']
堆栈长度：3
是否为空：否

向堆栈添加'星期四'...
添加成功
更新后堆栈：['星期四', '星期三', '星期二', '星期一']

从堆栈移除元素...
被移除的元素：星期四
更新后堆栈：['星期三', '星期二', '星期一']

再次从堆栈移除元素...
被移除的元素：星期三
更新后堆栈：['星期二', '星期一']

当前堆栈状态：
是否为空：否
堆栈长度：2
"""
from typing import Optional


class Stack(object):
    def __init__(self, stack_list: Optional[list] =None):
        if stack_list is None:
            stack_list = []
        self.stack = stack_list

    def push(self, data):
        if data not in self.stack:
            self.stack.insert(0, data)
            return True
        else:
            return False

    def pop(self):
        if len(self.stack) <= 0:
            return "No element in the Stack"
        else:
            return self.stack.pop(0)

    def peek(self):
        if len(self.stack) <= 0:
            return "No element in the Stack"
        else:
            return self.stack[-1]

    def __str__(self):
        return str(self.stack)

    def size(self):
        return len(self.stack)

    def is_empty(self):
        return len(self.stack) == 0


if __name__ == "__main__":
    print("\n=== 测试堆栈（后进先出）===")
    print("初始化堆栈：[]")
    stack = Stack()

    print("\n向堆栈添加'星期一'、'星期二'以及'星期三'...")
    stack.push('星期一')
    stack.push('星期二')
    stack.push('星期三')
    print(f"当前堆栈内容：{stack}")
    print(f"堆栈长度：{stack.size()}")
    print(f"是否为空：{'是' if stack.is_empty() else '否'}")

    print("\n向堆栈添加'星期四'...")
    result = stack.push('星期四')
    print(f"添加{'成功' if result else '失败（已存在）'}")
    print(f"更新后堆栈：{stack}")

    print("\n从堆栈移除元素...")
    popped = stack.pop()
    print(f"被移除的元素：{popped}")
    print(f"更新后堆栈：{stack}")

    print("\n再次从堆栈移除元素...")
    popped = stack.pop()
    print(f"被移除的元素：{popped}")
    print(f"更新后堆栈：{stack}")

    print("\n当前堆栈状态：")
    print(f"是否为空：{'是' if stack.is_empty() else '否'}")
    print(f"堆栈长度：{stack.size()}")