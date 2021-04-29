list1 = [1, 2, 3, 4, 7, 2, 6, 8, 10]
x = [8, 9]
n = 5
n1 = n2 = n3 = 0

# list1 * n  列表重复n次
print(list1*n)
# list1[n1:n2] 取出n1到n2-1元素
print(list1[2:4])
# list1[n1:n2:n3] 取出n1到n2-1元素, 间隔n3
print(list1[2:5:2])

# 返回列表元素个数
print(len(list1))
# 返回元素最大值，最小值
print(max(list1))
print(min(list1))
print('*'*20)
# list1.index(n1) 取首个值为n1的下标
print(list1.index(7))
# list1.count(n1) 取n1出现的次数
print(list1.count(2))
print(list1.count(8))
# list1.append(n1) 将n1添加到列表最后
list1.append(200)
print(list1)
# list1.extend(x) 将x中的元素逐一加到列表最后
list1.extend(x)
print(list1)
# list1.insert(n, n1) 将n1添加到n位置
list1.insert(3, 40)
print(list1)
# list1.pop() 取最后一个元素并删除
print(list1.pop())
print(list1)

# list1.remove(n1) 删除首次出现的n1元素
list1.remove(4)
print(list1)

# list1.reverse() 反序
list1.reverse()
print(list1)

# list1.sort() 将列表升序
list1.sort()
print(list1)
list1.sort(reverse=True)
print(list1)

# del list1[n1:n2] 删除n1到n2-1元素
# del list1[2:4]
del list1[2:5:2]

# 元组与列表互换
t = tuple(list1)
print(t)
list2 = list(t)
print(list2)

# 列表的高级方法也可以用于元组，但元组不能改变元素值，所以涉及改变元素个数或元素值的方法都不能用于元组
# append、insert

# 1、元组内部结构比列表简单，执行速度快
# 2、存于元组的数据比较安全：因为其内容无法改变，不会因为程序设计的疏忽而改变数据内容
