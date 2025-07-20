"""
在我们等待服务时，我们对日常生活中的队列很熟悉。
队列数据结构与数据元素排列在队列中的含义相同。 队列的独特之处在于添加和删除项目的方式。
这些项目允许在一端但从另一端移除。 所以它是一个先进先出 FIFO 的方法。

队列可以使用 python list 实现，我们可以使用 insert() 和 pop() 方法来添加和删除元素。
它们不是插入，因为数据元素总是添加到队列的末尾。

双端队列支持从任一端添加和删除元素。
在 Python 中，双端队列的容器由 collections.deque 提供。

=== 测试普通队列（先进先出）===
初始化队列：[]

向队列添加'星期一'、'星期二'以及'星期三'...
当前队列内容：['星期三', '星期二', '星期一']
队列长度：3
是否为空：否

向队列头部添加'星期四'...
添加成功
更新后队列：['星期四', '星期三', '星期二', '星期一']

从队列尾部移除元素...
被移除的元素：星期一
更新后队列：['星期四', '星期三', '星期二']

再次从队列尾部移除元素...
被移除的元素：星期二
更新后队列：['星期四', '星期三']

当前队列状态：
是否为空：否
队列长度：2

=== 测试双端队列 ===
初始化双端队列：['星期一', '星期二', '星期三']
当前队列内容：deque(['星期一', '星期二', '星期三'])

从左侧添加'星期四'...
更新后队列：deque(['星期四', '星期一', '星期二', '星期三'])

从右侧添加'星期五'...
更新后队列：deque(['星期四', '星期一', '星期二', '星期三', '星期五'])

从右侧移除元素...
被移除的元素：星期五
更新后队列：deque(['星期四', '星期一', '星期二', '星期三'])

再次从右侧移除元素...
被移除的元素：星期三
更新后队列：deque(['星期四', '星期一', '星期二'])

从左侧移除元素...
被移除的元素：星期四
最终队列：deque(['星期一', '星期二'])
"""

from collections import deque
from typing import Optional


class Queue(object):
    def __init__(self, queue_list: Optional[list] = None):
        """初始化队列，用列表实现"""
        if queue_list is None:
            queue_list = []
        self.queue = queue_list  # 用列表存储队列元素

    def push(self, value):
        """
        在队列头部添加元素
        如果值已存在则不添加（去重功能）
        返回是否添加成功
        """
        if value not in self.queue:
            self.queue.insert(0, value)  # 在列表头部插入
            return True
        return False

    def pop(self):
        """从队列尾部移除元素（先进先出）"""
        if len(self.queue) > 0:
            return self.queue.pop()  # 移除列表最后一个元素
        return "队列为空！"  # 空队列提示

    def size(self):
        """返回队列当前长度"""
        return len(self.queue)

    def is_empty(self):
        """检查队列是否为空"""
        return len(self.queue) == 0

    def __str__(self):
        """返回队列的字符串表示"""
        return str(self.queue)


# 创建deque的别名
DeQueue = deque  # 双端队列

if __name__ == '__main__':
    print("\n=== 测试普通队列（先进先出）===")
    print("初始化队列：[]")
    normal_queue = Queue()
    print("\n向队列添加'星期一'、'星期二'以及'星期三'...")
    normal_queue.push('星期一')
    normal_queue.push('星期二')
    normal_queue.push('星期三')

    print(f"当前队列内容：{normal_queue}")
    print(f"队列长度：{normal_queue.size()}")
    print(f"是否为空：{'是' if normal_queue.is_empty() else '否'}")

    print("\n向队列头部添加'星期四'...")
    result = normal_queue.push('星期四')
    print(f"添加{'成功' if result else '失败（已存在）'}")
    print(f"更新后队列：{normal_queue}")

    print("\n从队列尾部移除元素...")
    popped = normal_queue.pop()
    print(f"被移除的元素：{popped}")
    print(f"更新后队列：{normal_queue}")

    print("\n再次从队列尾部移除元素...")
    popped = normal_queue.pop()
    print(f"被移除的元素：{popped}")
    print(f"更新后队列：{normal_queue}")

    print("\n当前队列状态：")
    print(f"是否为空：{'是' if normal_queue.is_empty() else '否'}")
    print(f"队列长度：{normal_queue.size()}")

    print("\n=== 测试双端队列 ===")
    print("初始化双端队列：['星期一', '星期二', '星期三']")
    de_queue = DeQueue(['星期一', '星期二', '星期三'])
    print(f"当前队列内容：{de_queue}")

    print("\n从左侧添加'星期四'...")
    de_queue.appendleft('星期四')
    print(f"更新后队列：{de_queue}")

    print("\n从右侧添加'星期五'...")
    de_queue.append('星期五')
    print(f"更新后队列：{de_queue}")

    print("\n从右侧移除元素...")
    popped = de_queue.pop()
    print(f"被移除的元素：{popped}")
    print(f"更新后队列：{de_queue}")

    print("\n再次从右侧移除元素...")
    popped = de_queue.pop()
    print(f"被移除的元素：{popped}")
    print(f"更新后队列：{de_queue}")

    print("\n从左侧移除元素...")
    popped = de_queue.popleft()
    print(f"被移除的元素：{popped}")
    print(f"最终队列：{de_queue}")