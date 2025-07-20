"""
数组是一个容器，可以容纳固定数量的元素，并且这些元素应该是同一类型。
大多数数据结构都使用数组来实现它们的算法。 以下是了解数组概念的重要术语如下

- 元素 element: 存储在数组中的每个项目称为一个元素。
- 索引 index: 数组中元素的每个位置都有一个数字索引，用于标识该元素。

数组支持的基本操作如下

- 遍历: 将所有数组元素一一打印出来。
- 插入: 在给定索引处（在该索引之前）添加一个元素。
- 删除: 删除给定索引处的元素。
- 搜索: 使用给定索引或按值搜索元素。
- 更新: 更新给定索引处的元素。

Type code   C Type             Minimum size in bytes
'b'         signed integer     1
'B'         unsigned integer   1
'u'         Unicode character  2 (see note)
'h'         signed integer     2
'H'         unsigned integer   2
'i'         signed integer     2
'I'         unsigned integer   2
'l'         signed integer     4
'L'         unsigned integer   4
'q'         signed integer     8 (see note)
'Q'         unsigned integer   8 (see note)
'f'         floating point     4
'd'         floating point     8
"""

from array import ArrayType

a = ArrayType('i', [10, 20, 30, 40, 50])

# 遍历
print("遍历数组 a 中的元素")
for i in a:
    print(i)

# 插入
print("插入数组 a 中的元素")
a.insert(0, 60)
print(a)

# 删除
print("删除数组 a 中的元素")
a.remove(60)
print(a)

# 搜索
print("搜索数组 a 中的元素")
print(a.index(40))

# 更新
print("更新数组 a 中的元素")
a[0] = 80
print(a)