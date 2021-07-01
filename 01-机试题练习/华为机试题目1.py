# 1、字符串最后一个单词的长度

a = input().split(' ')
print(len(a[-1]))

# 2、计算某字符出现的次数（不区分大小写）

s = input().lower()
word = input().lower()
print(s.count(word))

# 3、明明的随机数（去重 + 排序）

while True:
    try:
        n = int(input())
        res = set()  # 去重
        for i in range(n):
            res.add(int(input()))
        for i in sorted(res):  # 排序
            print(i)
    except:
        break


# 4、字符串分隔
while True:
    try:
        s = input()
        while len(s) > 8:
            print(s[:8])
            s = s[8:]
        print(s.ljust(8, '0'))
    except:
        break

# 5、进制转换

dec = input('10进制数为：')
print("转换为二进制为：", bin(dec))
print("转换为八进制为：", oct(dec))
print("转换为十六进制为：", hex(dec))

# 字符转成数字 ord chr
print("字符转成数字", ord('a'))
print("数字转成字符", chr(127))

string1 = '101010'
print('二进制字符串转换成十进制数为：', int(string1, 2))
string1 = '367'
print('八进制字符串转换成十进制数为：', int(string1, 8))
string3 = 'FFF'
print('十六进制字符串转换成十进制数为：', int(string1, 16))

# 6、质数因子
n = int(input())

def fun(sum):
    flg = 1
    for i in range(2, int(sum**0.5+2)):
        if sum % i == 0:
            b = int(sum / i)
            flg = 0
            print(str(i), end=' ')  # 循环内打印i
            fun(b)
            break
    # 没进循环内，或循环内没有满足条件的数据
    if flg == 1:
        print(str(sum), end=' ')  # 循环外打印sum

fun(n)


# 7、取近似值
print(int(float(input())+0.5))


# 8、合并表记录
while True:
    try:
        n = int(input())
        d = dict()
        for i in range(n):
            arr = input().split(' ')
            m = int(arr[0])
            n = int(arr[1])
            if m not in d.keys():
                d[m] = n
            else:
                d[m] = d[m] + n

        for k in sorted(d):
            print(k, d[k])
    except:
        break

# 变形题目【简单错误记录】
# E:\V1R2\product\fpgadrive.c 1325
d = dict()
while True:
    try:
        s = input().split('\\')[-1]  # 取【fpgadrive.c 1325】这段
        if s not in d.keys():
            d[s] = 1
        else:
            d[s] = d[s] + 1
        # 对d进行排序
        h = sorted(d.items(), key=lambda kv: kv[1], reverse=True)
        n = min(8, len(h))
        for i in range(n):
            name = h[i][0].split(' ')
            print("%s %s %s" % (name[0][-16:], name[1], h[i][1]))
    except:
        break




# 9、提取不重复的整数

n = input()
n = n[::-1]  # 11、数字颠倒 逆序
res = ''
for i in n:
    if i not in res:
        res = res + i
print(res)

# 10、字符个数统计
n = input()
res = ''
for i in n:
    if i not in res and ord(i) >= 0 and ord(i) <= 127:
        res  = res + i

print(len(res))

# 12、句子逆序
arr = input().split(' ')
arr.reverse()
for i in arr:
    print(i, end=' ')


# 13、字符串排序
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

# 14、求int型正整数在内存中存储时1的个数 (int 转为 二进制 后 1的个数)

n = int(input())
s = bin(n)
print(s.count('1'))


# 15、汽水瓶
res = list()
while True:
    try:
        n = int(input())
        if n == 0:
            break
        res.append(n)
    except:
        break

for i in res:
    count = 0
    while True:
        if i >= 3:
            count = count + int(i / 3)
            i = int(i / 3) + i % 3
        elif i == 2:
            count += 1
            break
        else:
            break
    print(count)







while True:
    try:
        arr = input().split(',')
        if len(arr) != 2:
            print(-1)
            break
        m = int(arr[0])  # 裁判数
        n = int(arr[1])  # 运动员数
        scores = list()
        for i in range(m):
            ml = list(map(int, input().split(',')))
            scores.append(ml)
        if m not in range(2, 10) or n not in range(3, 100):
            # 人数不在范围内
            print(-1)
            break
        for l in scores:
            if max(l) > 10 or min(l) < 1:
                # 所打分数不在范围内
                print(-1)
                break
    except:
        break











#
'''
给定任意一个非空字符串, 请编程回答存在多少种如下组合式的情况："S1 + C1 + S2 + C2 + S3"。其中S1/S2/S3为任意非空字符串(三者可以相同也可以不同), C1/C2为任意字符, 且C1=C2。举例一：字符串"duowan"存在0种。举例二：字符串"duowanisgood"存在2种："du + o + wanisg + o + od"和"du + o + wanisgo + o + d"。请按如下函数定义编程：
'''
# while True:
#     count = 0
#     try:
#         s = input()
#         if len(s) < 5:
#             print("input error")
#             break
#         for i in range(1, len(s)-3):
#             x = 0
#             for j in range(i+2, len(s)-1):
#                 if s[i] == s[j]:
#                     x += 1
#                     print('%s %s %s %s %s' % (s[0:i], s[i], s[i+1:j], s[j], s[j+1:]))
#             count += x
#         print(count)
#     except:
#         break



#
# n = input().split(',[[')
# target = int(n[0])
# print(n[1])
# tmp = n[1].replace('[[', '').replace(']]', '').split('],[')
# print(tmp)
# arr = list()
# for i in tmp:
#     if len(i) > 0:
#         arr.append(list(map(int, i.split(","))))
# # 7,[[1,2,8,9],[2,4,9,12],[4,7,10,13],[6,8,11,15]]
# print(arr)
# for i in range(len(arr)):
#     a = arr[i]
#     if a.count(target):
#         print('True')
#         break
#     elif i == len(arr)-1:
#         print('False')
