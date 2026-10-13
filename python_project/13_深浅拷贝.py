"""
深浅拷贝与可变/不可变类型

1. 可变类型：
    列表、字典、集合等，内容可以被修改。

2. 不可变类型：
    字符串、整数、元组等，内容一旦创建就不能修改。

深浅拷贝的核心：
    - 对于不可变类型来说，通常不需要特别处理，因为它们本身不能原地修改。
    - 对于可变类型来说，浅拷贝和深拷贝的差异就非常明显。
    - 浅拷贝：只复制外层对象，内层对象仍然共享。
    - 深拷贝：递归复制所有层级，完全独立。
    -深浅拷贝主要是针对可变类型来讲的，深拷贝拷贝所有层（可变），浅拷贝拷贝第一层（可变）
     如果是针对不可变类型，则用法与普通赋值一样，并无区别
"""

import copy

# 1. 不可变类型：重新赋值后，原值不会被修改
num1 = 10
num2 = num1
num2 = 20
print("不可变类型 int：")
print("num1 =", num1)
print("num2 =", num2)
print("num1 is num2:", num1 is num2)
print("-" * 30)

# 2. 可变类型：列表是典型的可变类型
list1 = [1, 2, [3, 4]]
list2 = list1      # 赋值：两个变量指向同一个对象
list2.append(5)
list2[2].append(99)
print("赋值示例：")
print("list1:", list1)
print("list2:", list2)
print("list1 is list2:", list1 is list2)
print("-" * 30)

# 3. 浅拷贝：只复制外层容器，内层对象仍然共享
list3 = [1, 2, [3, 4]]
list4 = copy.copy(list3)
list4.append(5)
list4[2].append(99)
print("浅拷贝示例：")
print("list3:", list3)
print("list4:", list4)
print("list3[2] is list4[2]:", list3[2] is list4[2])
print("-" * 30)

# 4. 深拷贝：递归复制所有层级，完全独立
list5 = [1, 2, [3, 4]]
list6 = copy.deepcopy(list5)
list6.append(5)
list6[2].append(99)
print("深拷贝示例：")
print("list5:", list5)
print("list6:", list6)
print("list5[2] is list6[2]:", list5[2] is list6[2])
print("-" * 30)

# 5. 字典的拷贝同理，和列表一致
person = {
    "name": "小明",
    "hobby": ["篮球", "跑步"],
}
person_copy = copy.copy(person)
person_deep = copy.deepcopy(person)

person_copy["hobby"].append("音乐")
person_deep["hobby"].append("电影")

print("字典浅拷贝：")
print(person)
print(person_copy)
print("person['hobby'] is person_copy['hobby']:", person["hobby"] is person_copy["hobby"])
print("-" * 30)

print("字典深拷贝：")
print(person)
print(person_deep)
print("person['hobby'] is person_deep['hobby']:", person["hobby"] is person_deep["hobby"])
print("-" * 30)

# 6. 总结
print("总结：")
print("1. 不可变类型：通常不需要深拷贝，因为无法原地修改")
print("2. 可变类型：浅拷贝只复制外层，内层仍共享")
print("3. 可变类型：深拷贝会递归复制全部内容，完全独立")
