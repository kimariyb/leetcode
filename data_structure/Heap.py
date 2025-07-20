"""
堆是一种特殊的树结构，其中每个父节点都小于或等于其子节点，它被称为最小堆。
如果每个父节点都大于或等于它的子节点，那么它被称为最大堆。
实现优先级队列非常有用，其中权重较高的队列项在处理中具有更高的优先级。

堆是使用 Python 的内置库 heapq 创建的。 该库具有对堆数据结构进行各种操作的相关函数。 

=== 堆操作测试开始 ===

原始列表: [21, 1, 45, 78, 3, 5]
堆化后: [1, 3, 5, 78, 21, 45]  (最小堆，第一个元素是最小值: 1)

验证堆属性:
索引 0: 父节点 1 <= 左子节点 3: True | 父节点 1 <= 右子节点 5: True
索引 1: 父节点 3 <= 左子节点 78: True | 父节点 3 <= 右子节点 21: True
索引 2: 父节点 5 <= 左子节点 45: True

添加元素 8 后: [1, 3, 5, 78, 21, 45, 8]
弹出最小值: 1, 剩余堆: [3, 8, 5, 78, 21, 45]
替换堆顶元素 3 为 6 后: [5, 8, 6, 78, 21, 45]

堆中前3小的元素: [5, 6, 8]
堆中前3大的元素: [78, 45, 21]

合并两个堆 [5, 8, 6, 78, 21, 45] 和 [2, 10, 99]: [2, 5, 8, 6, 10, 78, 21, 45, 99]

=== 边界测试 ===
空堆: []
从空堆弹出元素抛出异常: index out of range
单元素堆: [5]
弹出唯一元素: 5, 剩余: []

=== 堆操作测试结束 ===
"""
import heapq


if __name__ == '__main__':
    print("=== 堆操作测试开始 ===")

    # 1. 初始化列表并转换为堆
    data = [21, 1, 45, 78, 3, 5]
    print(f"\n原始列表: {data}")

    heapq.heapify(data)
    print(f"堆化后: {data}  (最小堆，第一个元素是最小值: {data[0]})")

    # 2. 验证堆属性
    print("\n验证堆属性:")
    for i in range(len(data)):
        left = 2 * i + 1
        right = 2 * i + 2
        parent = (i - 1) // 2

        checks = []
        if left < len(data):
            checks.append(f"父节点 {data[i]} <= 左子节点 {data[left]}: {data[i] <= data[left]}")
        if right < len(data):
            checks.append(f"父节点 {data[i]} <= 右子节点 {data[right]}: {data[i] <= data[right]}")

        if checks:
            print(f"索引 {i}:", " | ".join(checks))

    # 3. 添加元素
    heapq.heappush(data, 8)
    print(f"\n添加元素 8 后: {data}")

    # 4. 弹出最小元素
    min_val = heapq.heappop(data)
    print(f"弹出最小值: {min_val}, 剩余堆: {data}")

    # 5. 替换堆顶元素
    replaced = heapq.heapreplace(data, 6)
    print(f"替换堆顶元素 {replaced} 为 6 后: {data}")

    # 6. 获取前 N 个最小元素
    print(f"\n堆中前3小的元素: {heapq.nsmallest(3, data)}")
    print(f"堆中前3大的元素: {heapq.nlargest(3, data)}")

    # 7. 合并堆
    heap2 = [10, 2, 99]
    heapq.heapify(heap2)
    merged = list(heapq.merge(data, heap2))
    print(f"\n合并两个堆 {data} 和 {heap2}: {list(merged)}")

    # 8. 边界测试
    print("\n=== 边界测试 ===")
    empty_heap = []
    heapq.heapify(empty_heap)
    print(f"空堆: {empty_heap}")

    try:
        heapq.heappop(empty_heap)
    except IndexError as e:
        print(f"从空堆弹出元素抛出异常: {e}")

    single_heap = [5]
    heapq.heapify(single_heap)
    print(f"单元素堆: {single_heap}")
    print(f"弹出唯一元素: {heapq.heappop(single_heap)}, 剩余: {single_heap}")

    print("\n=== 堆操作测试结束 ===")