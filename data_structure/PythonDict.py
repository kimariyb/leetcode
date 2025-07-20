"""
在字典中，每个键和它的值用冒号 (:) 分隔，项目用逗号分隔，整个内容用花括号括起来。
一个没有任何项目的空字典只用两个大括号写成，就像这样 − {}.

Keys 键在字典中是唯一的，而值可能不是。
字典的值可以是任何类型，但键必须是不可变的数据类型，例如字符串、数字或元组。

1. 初始字典操作:
d['Name']: Zara
d['Age']: 7

2. 修改和添加操作:
修改后的d['Age']: 8
新增的d['School']: DPS School

3. 删除操作:
删除'Name'后的字典: {'Age': 8, 'Class': 'First', 'School': 'DPS School'}

4. 清空操作:
清空后的字典: {}

5. 安全访问测试:
尝试访问d['Age']: 键不存在！
使用get方法访问d['School']: 键不存在

6. 其他字典操作:
所有键: dict_keys(['Name', 'Age', 'Class'])
所有值: dict_values(['Tom', 10, 'Second'])
键值对: dict_items([('Name', 'Tom'), ('Age', 10), ('Class', 'Second')])

7. 字典合并:
合并后的字典: {'Name': 'Tom', 'Age': 11, 'Class': 'Second', 'School': 'ABC School'}
"""

d = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}

# 1. 正常访问键值
print("1. 初始字典操作:")
print("d['Name']:", d['Name'])  # 输出: Zara
print("d['Age']:", d['Age'])   # 输出: 7

# 2. 修改和添加键值
print("\n2. 修改和添加操作:")
d['Age'] = 8
d['School'] = "DPS School"
print("修改后的d['Age']:", d['Age'])       # 输出: 8
print("新增的d['School']:", d['School'])  # 输出: DPS School

# 3. 删除键值
print("\n3. 删除操作:")
del d['Name']
print("删除'Name'后的字典:", d)  # 输出: {'Age': 8, 'Class': 'First', 'School': 'DPS School'}

# 4. 清空字典
print("\n4. 清空操作:")
d.clear()
print("清空后的字典:", d)  # 输出: {}

# 5. 安全访问已删除的键（使用get方法避免异常）
print("\n5. 安全访问测试:")
print("尝试访问d['Age']:", end=' ')
try:
    print(d['Age'])  # 这会引发KeyError
except KeyError:
    print("键不存在！")

print("使用get方法访问d['School']:", d.get('School', '键不存在'))  # 输出: 键不存在

# 6. 其他常用操作
print("\n6. 其他字典操作:")
d = {'Name': 'Tom', 'Age': 10, 'Class': 'Second'}
print("所有键:", d.keys())      # 输出: dict_keys(['Name', 'Age', 'Class'])
print("所有值:", d.values())    # 输出: dict_values(['Tom', 10, 'Second'])
print("键值对:", d.items())     # 输出: dict_items([('Name', 'Tom'), ('Age', 10), ('Class', 'Second')])

# 7. 字典合并
print("\n7. 字典合并:")
new_data = {'School': 'ABC School', 'Age': 11}  # 注意Age会被更新
d.update(new_data)
print("合并后的字典:", d)  # 输出: {'Name': 'Tom', 'Age': 11, 'Class': 'Second', 'School': 'ABC School'}