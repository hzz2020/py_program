# 1、字符串最后一个单词的长度

strArr = input().split(" ")  # 将输入的字符串按要求用空格分隔得到数组
print(len(strArr[-1]))  # 数组取最后一个元素，计算长度

# 2、计算某字母出现次数 不区分大小写
instr = input().lower()
word = input().lower()
print(instr.count(word))

# 3、明明的随机数
while True:
    n = int(input())  # 准备随机输入n个数
    res = set()  # set不允许与重复数据
    try:
        for i in range(n):  # 循环n次 输入n个随机数
            res.add(int(input()))
        for j in sorted(res):  # 循环排序后的set 输出数据
            print(j)
    except:
        break

# 番外学习
import random

while True:
    n = int(input())
    res = random.sample(range(1, 1000), n)  # 在1-1000范围内随机生成n个不重复的数
    for i in sorted(res):
        print(i)

'''
描述
•连续输入字符串，请按长度为8拆分每个字符串后输出到新的字符串数组；
•长度不是8整数倍的字符串请在后面补数字0，空字符串不处理。

输入描述：
连续输入字符串(输入多次,每个字符串长度小于100)

输出描述：
输出到长度为8的新字符串数组

示例1
输入：
abc
123456789
输出：
abc00000
12345678
90000000
'''
# 4、字符串分隔

while True:
    try:
        instr = input()
        while len(instr) > 8:
            print(instr[:8])
            instr = instr[8:]
        print(instr.ljust(8, "0"))  # 靠左对齐，右边补0
        print(instr.rjust(8, "0"))  # 靠右对齐，左边补0
        print(instr.center(8, "0"))  # 居中对齐
    except:
        break

# 5、取近似值  2.5 -> 3
# 2.4 -> 2
while True:
    try:
        n = int(float(input())+0.5)
        print(n)
    except:
        break


# 6、质数因子

num = int(input())

def func(num):
    prime_num = 1
    for i in range(2, int(num ** 0.5 + 2)):  # 根据质数的性质 从2开始整除
        if num % i == 0:  # 能整除 则i为质数因子
            prime_num = 0  # 这个整数本身不是质数因子 标记
            b = int(num / i)  # 算出商并继续递归调用
            print(str(i), end=' ')  #i为质数因子打印
            func(b)
            break
    if prime_num == 1:  # 到最后都不能整除，则本身为质数因子
        print(str(num), end=' ')

func(num)


# 7、合并表记录

while True:
    try:
        a = int(input())
        keyRes = set()  # 判断是否有重复的key
        dictRes = dict()  # 结果输出
        for i in range(a):
            strArr = input().split(" ")
            key = int(strArr[0])  # key值int 要不后续排序输出顺序会不对
            value = int(strArr[1])  # value值必须要int，要不后续运算+会有问题

            if key not in keyRes:
                keyRes.add(key)
                dictRes[key] = value
            else:
                dictRes[key] = dictRes[key] + value
        # 排序输出
        for key in sorted(dictRes.keys()):
            print(key, dictRes[key])
    except:
        break


# 8、提取不重复的整数
while True:
    try:
        a = input()
        a = a[::-1]  # 字符串逆序
        y = ''
        for i in a:
            if i not in y:
                y = y + i  # 字符串拼接
        print(y)
    except:
        break

# 9、字符个数统计
n = input()
words = ''
for i in n:
    if i not in words and 0 <= ord(i) <= 127:  #ord 返回对应的ASCII值
        words += i

print(len(words))

# 10、数字颠倒，字符串反转
n = input()
n = n[::-1]
print(n)

# 11、句子逆序
strArr = input().split(' ')  # 输入语句以空格分隔
strArr.reverse()
for i in strArr:
    print(i, end=' ')

# 12、字符串排序
while True:
    try:
        n = int(input())
        res = list()
        for i in range(n):
            res.append(input())
        for i in sorted(res):
            print(i)
    except:
        break

# 13、求int型正整数在内存中存储时1的个数
n = bin(int(input()))
s = n.count('1')
print(s)