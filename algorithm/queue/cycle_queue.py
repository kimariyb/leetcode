"""
问题描述：

实现一个循环队列，支持以下操作：
- 入队：将一个元素添加到队列的末尾。
- 出队：从队列的头部移除一个元素。
- 获取队首元素：返回队列的头部元素。
- 获取队尾元素：返回队列的尾部元素。
- 判断队列是否为空：如果队列为空，返回 True；否则，返回 False。
- 判断队列是否已满：如果队列已满，返回 True；否则，返回 False。
"""

class MyCircularQueue:
    def __init__(self, size):
        self.size = size + 1
        self.queue = [None] * self.size
        self.front = 0
        self.rear = 0
        
    def is_empty(self):
        """判断队列是否为空"""
        return self.front == self.rear
    
    def is_full(self):
        """判断队列是否已满"""
        return (self.rear + 1) % self.size == self.front
    
    def enqueue(self, value):
        """入队操作"""
        if self.is_full():  
            raise Exception("Queue is full")
        else:
            self.rear = (self.rear + 1) % self.size
            self.queue[self.rear] = value

    def dequeue(self):
        """出队操作"""
        if self.is_empty():
            raise Exception("Queue is empty")
        else:
            self.front = (self.front + 1) % self.size
            return self.queue[self.front]

    def get_front(self):
        """获取队首元素"""
        if self.is_empty():
            raise Exception("Queue is empty")
        else:
            self.front = (self.front + 1) % self.size
            return self.queue[self.front]

    def get_rear(self):
        """获取队尾元素"""
        if self.is_empty():
            raise Exception("Queue is empty")
        else:
            return self.queue[self.rear]
        

if __name__ == '__main__':
    queue = MyCircularQueue(5)
    print(queue.is_empty())
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    queue.enqueue(4)
    queue.enqueue(5)
    print(queue.is_full())
    print(queue.dequeue())
    print(queue.get_front())
    print(queue.get_rear())
    print(queue.is_empty())