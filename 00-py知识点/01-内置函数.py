# type(obj) 返回obj的数据类型

# abs(x) 返回x的绝对值
n = abs(-5)
print(n)
print(type(n))

# chr(x) 返回整数x所表示的字符
n = chr(66)
print(n)
print(type(n))

# divmod(x, y)  返回x除以y的商及余数组成的元组
t = divmod(44, 6)
print(t)
print(type(t))

# float(x) 将x转换成浮点数
f = float('56')
print(f)
print(type(f))

# hex(x) 将x转换成十六进制数
dd = hex(34)
print(dd)
print(type(dd))

# int(x) 将x转换成整数
i = int(34.23)
print(i)
print(type(i))

# len(x) 返回参数x的元素个数
n = len([1, 2, 3, 4, 5])
print(n)

# max(x) 返回列表参数中的最大值
# min(x) 返回列表参数中的最小值

m = max([1, 4, 5, 6, 2, 6, 9])
print(m)
m = min([1, 4, 5, 6, 2, 6, 9])
print(m)

# oct(x) 将x转换成八进制数字
print(oct(34))
# ord(x) 返回字符x的Unicode编码
print(ord('我'))
# pow(x, y) 返回x的y次方
print(pow(3, 3))
# pow(x, y, z) 返回x的y次方除以z的余数
print(pow(3, 5, 4))
# round(x) 返回四舍五入值
print(round(4.34))
# round(x, y) 返回四舍五入值, y为保留小数的位数
print(round(4.36, 1))
print(round(344, 1))
# sorted(列表, reverse) 从小到大排序, reverse反序
print(sorted((4, 5, 22, 55, 11, 44)))
print(sorted((4, 5, 22, 55, 11, 44), reverse=True))
# str(x) 将x转换成字符串
print(str(5431))
# sum(列表) 计算列表中元素的总和
print(sum([1, 3, 5, 6, 8]))

