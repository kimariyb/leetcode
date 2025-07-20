"""
列表是 Python 中可用的最通用的数据类型，可以写成方括号之间以逗号分隔的值（项）列表。
关于列表的重要一点是列表中的项目不必是同一类型。创建列表就像将不同的逗号分隔值放在方括号之间一样简单。

=== 列表基本操作测试 ===

1. 列表索引和切片:
list1[0]: physics
list2[1:5]: [2, 3, 4, 5]
list2[-3:]: [5, 6, 7]
list2[::2]: [1, 3, 5, 7]

2. 列表元素修改:
原始list3: ['physics', 'chemistry', 1997, 2000]
list3[2]: 1997
修改后的list3[2]: 2001
完整list3: ['physics', 'chemistry', 2001, 2000]

3. 列表元素删除:
原始list4: ['physics', 'chemistry', 1997, 2000]
删除索引2后的list4: ['physics', 'chemistry', 2000]
删除切片后的list4: ['physics']

4. 列表常用方法演示:
append添加后: ['apple', 'banana', 'cherry', 'orange']
insert插入后: ['apple', 'grape', 'banana', 'cherry', 'orange']
pop移除的元素: orange, 剩余列表: ['apple', 'grape', 'banana', 'cherry']
remove后的列表: ['apple', 'grape', 'cherry']

5. 列表运算和其他操作:
列表相加: [1, 2, 3, 4, 5, 6]
列表重复: [1, 2, 3, 1, 2, 3]
元素存在性检查: True
列表长度: 3

6. 列表遍历:
索引0: apple
索引1: banana
索引2: cherry

7. 列表推导式:
平方数列表: [0, 1, 4, 9, 16]

=== 测试结束 ===
"""

# 列表基本操作测试
print("=== 列表基本操作测试 ===")

# 1. 列表定义和索引访问
list1 = ['physics', 'chemistry', 1997, 2000]
list2 = [1, 2, 3, 4, 5, 6, 7]

print("\n1. 列表索引和切片:")
print("list1[0]:", list1[0])          # 输出第一个元素
print("list2[1:5]:", list2[1:5])      # 输出索引1到4的元素（切片不包含结束索引）
print("list2[-3:]:", list2[-3:])      # 输出最后3个元素
print("list2[::2]:", list2[::2])      # 步长为2的切片

# 2. 列表元素修改
print("\n2. 列表元素修改:")
list3 = ['physics', 'chemistry', 1997, 2000]
print("原始list3:", list3)
print("list3[2]:", list3[2])          # 访问索引2的元素

list3[2] = 2001                       # 修改索引2的元素
print("修改后的list3[2]:", list3[2])
print("完整list3:", list3)

# 3. 列表元素删除
print("\n3. 列表元素删除:")
list4 = ['physics', 'chemistry', 1997, 2000]
print("原始list4:", list4)

del list4[2]                          # 删除索引2的元素
print("删除索引2后的list4:", list4)

del list4[1:3]                        # 删除切片范围内的元素
print("删除切片后的list4:", list4)

# 4. 列表常用方法
print("\n4. 列表常用方法演示:")
fruits = ['apple', 'banana', 'cherry']

# 添加元素
fruits.append('orange')               # 在末尾添加
print("append添加后:", fruits)

fruits.insert(1, 'grape')             # 在指定位置插入
print("insert插入后:", fruits)

# 移除元素
removed = fruits.pop()                # 移除并返回最后一个元素
print(f"pop移除的元素: {removed}, 剩余列表: {fruits}")

fruits.remove('banana')               # 移除第一个匹配项
print("remove后的列表:", fruits)

# 5. 列表运算和其他操作
print("\n5. 列表运算和其他操作:")
a = [1, 2, 3]
b = [4, 5, 6]

print("列表相加:", a + b)              # 列表拼接
print("列表重复:", a * 2)             # 列表重复
print("元素存在性检查:", 3 in a)      # 成员检查
print("列表长度:", len(a))           # 列表长度

# 6. 列表遍历
print("\n6. 列表遍历:")
for i, item in enumerate(['apple', 'banana', 'cherry']):
    print(f"索引{i}: {item}")

# 7. 列表推导式
print("\n7. 列表推导式:")
squares = [x**2 for x in range(5)]
print("平方数列表:", squares)

print("\n=== 测试结束 ===")