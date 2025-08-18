

class HashTable:
    def __init__(self, capacity: int, load_factor: float = .75):
        """初始化哈希表"""
        self.capacity = capacity # 底层数组的大小
        self.load_factor = load_factor # 负载因子阈值
        self.size = 0 # 哈希表中元素的数量
        self.buckets = [[] for _ in range(self.capacity)] # 底层数组，每个元素是一个链表

    def _hash(self, key) -> int:
        """哈希函数，将键值映射到索引"""
        return hash(key) % self.capacity
    
    def put(self, key, value) -> None:
        """插入键值对"""
        # 1. 计算桶的索引
        index = self._hash(key)
        bucket = self.buckets[index]

        # 2. 检查键是否已经存在
        for i, (k, v) in enumerate(bucket):
            if k == key:
                # 3. 如果键已经存在，更新值
                bucket[i] = (key, value)
                return

        # 4. 如果键不存在，添加新的键值对
        bucket.append((key, value))
        self.size += 1
        
        # 5. 检查负载因子，如果超过阈值，则扩容
        if self.size / self.capacity > self.load_factor:
            self._resize()
    
    def get(self, key):
        """获取键对应的值"""
        index = self._hash(key)
        bucket = self.buckets[index]

        for k, v in bucket:
            if k == key:
                return v

        # 未找到键
        raise KeyError(f"Key '{key}' not found")
    
    def _resize(self) -> None:
        """扩容哈希表"""
        old_buckets = self.buckets  # 保存旧桶数据
        self.capacity *= 2
        self.size = 0
        self.buckets = [[] for _ in range(self.capacity)]

        # 将旧桶中的所有键值对重新插入新桶
        for bucket in old_buckets:
            for key, value in bucket:
                self.put(key, value)  # 复用 put 方法（自动处理哈希和冲突）