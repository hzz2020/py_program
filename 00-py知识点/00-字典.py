dict1 = {'joe': 1, 'mary': 8}
n = 0
b = False

# 返回字典元素个数
print(len(dict1))

# 复制字典
dict2 = dict1.copy()
print(dict2)
# 删除所有字典中的元素
dict3 = dict1.clear()
print(dict3)

# 返回 “键”对应的 “值”，
# 若“键”不存在 ， 就返回参数中的“值”
n = dict2.get('joe', 100)
print(n)
n = dict2.get('haha', 101)
print(n)

# 键 in dict2 检查键是否存在
b = 'joe' in dict2
print(b)

dict2.setdefault('joe', 100)
dict2.setdefault('hehe', 101)

print(dict2.keys())
print(dict2.values())
print(dict2.items())