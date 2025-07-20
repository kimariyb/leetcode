"""
哈希表是一种数据结构，其中数据元素的地址或索引值由哈希函数生成。
这使得访问数据更快，因为索引值充当数据值的键。
换句话说，哈希表存储键值对，但键是通过哈希函数生成的。

在 Python 中，Dictionary 数据类型代表哈希表的实现。 字典中的 Key 满足以下要求。

- 字典的 Key 是可哈希的，即由哈希函数生成，哈希函数为提供给哈希函数的每个唯一值生成唯一的结果。
- 字典中数据元素的顺序是不固定的。

假设我们用数组 a 存放数据，哈希函数是 f，那键值对 (key, value) 就应该放在 a[f(key)] 上。
不论键值是什么类型，范围有多大，f(key) 都是在可接受范围内的整数，可以作为数组的下标。

一般把键值模一个较大的质数作为索引，也就是取 f(x)=x mod M 作为哈希函数。

我们可以使用双哈希的方法：选取两个大质数 a, b。
当且仅当两个字符串的哈希值对 a 和对 b 取模都相等时，我们才认为这两个字符串相等。
这样可以大大降低哈希冲突的概率。
"""
from typing import List, Tuple, Any


class HashMap(object):
    def __init__(self, size: int):
        self.size = size
        self.map: List[List[Tuple[Any, Any]]] = [[] for _ in range(size)]

    def _get_hash(self, key):
        """计算 key 的 hash """
        return hash(key) % self.size

    def put(self, key, value):
        """添加键值对"""
        hash_key = self._get_hash(key)
        bucket = self.map[hash_key]

        # 检查key是否已存在
        for i, (k, v) in enumerate(bucket):
            if k == key:
                bucket[i] = (key, value)
                return

        # 如果key不存在，添加新键值对
        bucket.append((key, value))

    def get(self, key):
        """获取键对应的值"""
        hash_key = self._get_hash(key)
        bucket = self.map[hash_key]

        for k, v in bucket:
            if k == key:
                return v

        raise KeyError(key)

    def remove(self, key):
        """删除键值对"""
        hash_key = self._get_hash(key)
        bucket = self.map[hash_key]

        for i, (k, v) in enumerate(bucket):
            if k == key:
                del bucket[i]
                return

        raise KeyError(key)

    def __str__(self):
        """打印HashMap内容"""
        items = []
        for bucket in self.map:
            for k, v in bucket:
                items.append(f"{k}: {v}")
        return "{" + ", ".join(items) + "}"

    def __contains__(self, key):
        """支持in操作符"""
        try:
            self.get(key)
            return True
        except KeyError:
            return False

    def __len__(self):
        """返回HashMap中键值对的数量"""
        count = 0
        for bucket in self.map:
            count += len(bucket)
        return count


if __name__ == "__main__":
    print("\n=== 哈希表测试 ===")
    hash_map = HashMap(10)
    print(f"初始化哈希表：{hash_map}")
    print(f"当前哈希表大小：{len(hash_map)}")

    print("\n1. 测试添加键值对...")
    hash_map.put("apple", 10)
    hash_map.put("banana", 20)
    hash_map.put("orange", 30)
    hash_map.put("grape", 40)
    print(f"添加后哈希表内容：{hash_map}")
    print(f"当前哈希表大小：{len(hash_map)}")

    print("\n2. 测试获取值...")
    print("apple的值:", hash_map.get("apple"))
    print("banana的值:", hash_map.get("banana"))
    try:
        print("pear 的值:", hash_map.get("pear"))
    except KeyError as e:
        print(f"获取不存在的键 pear 时抛出KeyError: {e}")

    print("\n3. 测试更新值...")
    print("更新前apple的值:", hash_map.get("apple"))
    hash_map.put("apple", 15)
    print("更新后apple的值:", hash_map.get("apple"))

    print("\n4. 测试删除键值对...")
    print("删除前哈希表内容:", hash_map)
    hash_map.remove("banana")
    print("删除banana后哈希表内容:", hash_map)
    try:
        hash_map.remove("pear")
    except KeyError as e:
        print(f"删除不存在的键pear时抛出KeyError: {e}")
    print(f"当前哈希表大小：{len(hash_map)}")

    print("\n5. 测试in操作符...")
    print("apple是否在哈希表中:", "apple" in hash_map)
    print("pear是否在哈希表中:", "pear" in hash_map)

    print("\n6. 测试哈希冲突处理...")
    # 创建一个小的哈希表来更容易产生冲突
    small_map = HashMap(2)
    small_map.put("a", 1)
    small_map.put("b", 2)
    small_map.put("c", 3)  # 这个会和 a 或 b 产生冲突
    print("小哈希表内容:", small_map)
    print("获取冲突键a的值:", small_map.get("a"))
    print("获取冲突键c的值:", small_map.get("c"))

    print("\n7. 测试不同类型键...")
    hash_map.put(123, "数字键")
    hash_map.put(3.14, "浮点数键")
    hash_map.put((1, 2), "元组键")
    print("添加不同类型键后哈希表内容:", hash_map)
    print("获取数字键123的值:", hash_map.get(123))
    print("获取元组键(1, 2)的值:", hash_map.get((1, 2)))

    print("\n8. 测试哈希表大小...")
    print(f"最终哈希表大小：{len(hash_map)}")
    print("最终哈希表内容:", hash_map)