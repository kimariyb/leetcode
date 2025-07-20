"""
元组是一系列不可变的 Python 对象。 元组是序列，就像列表一样。
元组和列表之间的区别是，元组不能像列表和元组使用括号更改，而列表使用方括号。

=== 元组基本操作测试 ===

1. 元组索引和切片:
tup1[0]: physics
tup2[1:5]: (2, 3, 4, 5)
tup2[-3:]: (5, 6, 7)
tup2[::2]: (1, 3, 5, 7)

2. 元组不可变性测试:
错误信息: 'tuple' object does not support item assignment

3. 元组运算:
元组拼接: ('physics', 'chemistry', 1997, 2000, 1, 2, 3, 4, 5, 6, 7)
元组重复: (1, 2, 3, 4, 5, 6, 7, 1, 2, 3, 4, 5, 6, 7)

4. 元组方法演示:
元素4的索引: 1
元素2的出现次数: 2

5. 元组解包:
解包结果: x=10, y=20

6. 元组与列表转换:
转为列表: ['physics', 'chemistry', 1997, 2000]
转为元组: (1, 2, 3)

7. 元组遍历:
索引0: physics
索引1: chemistry
索引2: 1997
索引3: 2000

=== 测试结束 ===
"""
# 元组基本操作测试
print("=== 元组基本操作测试 ===")

# 1. 元组定义和索引访问
tup1 = ('physics', 'chemistry', 1997, 2000)
tup2 = (1, 2, 3, 4, 5, 6, 7)

print("\n1. 元组索引和切片:")
print("tup1[0]:", tup1[0])          # 输出第一个元素
print("tup2[1:5]:", tup2[1:5])      # 输出索引1到4的元素（切片不包含结束索引）
print("tup2[-3:]:", tup2[-3:])      # 输出最后3个元素
print("tup2[::2]:", tup2[::2])      # 步长为2的切片

# 2. 元组不可变性验证
print("\n2. 元组不可变性测试:")
try:
    tup1[2] = 2001  # 尝试修改元组元素
except TypeError as e:
    print("错误信息:", e)  # 输出错误信息：'tuple' object does not support item assignment

# 3. 元组拼接和重复
print("\n3. 元组运算:")
new_tup = tup1 + tup2  # 元组拼接
print("元组拼接:", new_tup)

double_tup = tup2 * 2  # 元组重复
print("元组重复:", double_tup)

# 4. 元组常用方法
print("\n4. 元组方法演示:")
numbers = (2, 4, 6, 8, 10, 4, 2)

print("元素4的索引:", numbers.index(4))         # 返回第一个匹配项的索引
print("元素2的出现次数:", numbers.count(2))    # 统计元素出现次数

# 5. 元组解包
print("\n5. 元组解包:")
point = (10, 20)
x, y = point
print(f"解包结果: x={x}, y={y}")

# 6. 元组与列表转换
print("\n6. 元组与列表转换:")
list_from_tup = list(tup1)
print("转为列表:", list_from_tup)

tup_from_list = tuple([1, 2, 3])
print("转为元组:", tup_from_list)

# 7. 元组遍历
print("\n7. 元组遍历:")
for i, item in enumerate(tup1):
    print(f"索引{i}: {item}")

print("\n=== 测试结束 ===")