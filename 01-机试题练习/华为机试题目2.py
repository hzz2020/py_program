# -----

print("-"*10 + " 华为研发工程师编程题一 " + "-"*10)

print("有这样一道智力题：“某商店规定：三个空汽水瓶可以换一瓶汽水。小张手上有十个空汽水瓶，她最多可以换多少瓶汽水喝？”答案是5瓶，方法如下：先用9个空瓶子换3瓶汽水，喝掉3瓶满的，喝完以后4个空瓶子，用3个再换一瓶，喝掉这瓶满的，这时候剩2个空瓶子。然后你让老板先借给你一瓶汽水，喝掉这瓶满的，喝完以后用3个空瓶子换一瓶满的还给老板。如果小张手上有n个空汽水瓶，最多可以换多少瓶汽水喝？")

while True:
    try:
        n = int(input('请输入空汽水瓶数:'))
        if n == 0:
            break
        count = 0
        while True:
            if n >= 3:
                count = count + int(n / 3)
                n = int(n / 3) + n % 3
            elif n == 2:
                count += 1
                break  # 用break减少一次循环
            else:
                break
        print("可以兑换%d汽水" % count)
    except:
        break

print("另一解法")
print("2,3 -> 1  4,5 -> 2  6,7 -> 3 ... 可以推导为 n/2 向下取整")
while True:
    try:
        a = int(input())
        if a/2 != 0:
            print(a//2)        #向下取整
    except:
        break


print("-"*10 + " 华为研发工程师编程题二 " + "-"*10)

print("明明想在学校中请一些同学一起做一项问卷调查，为了实验的客观性，他先用计算机生成了N个1到1000之间的随机整数（N≤1000），对于其中重复的数字，只保留一个，把其余相同的数去掉，不同的数对应着不同的学生的学号。然后再把这些数从小到大排序，按照排好的顺序去找同学做调查。请你协助明明完成“去重”与“排序”的工作(同一个测试用例里可能会有多组数据(用于不同的调查)，希望大家能正确处理)。\n注：测试用例保证输入参数的正确性，答题者无需验证。测试用例不止一组。\n当没有新的输入时，说明输入结束。")

while True:
    try:
        res, n = set(), int(input())
        for i in range(n):
            res.add(int(input()))
        for i in sorted(res):
            print(i)
    except:
        break

print("-"*10 + " 华为研发工程师编程题三 " + "-"*10)
print("写出一个程序，接受一个十六进制的数，输出该数值的十进制表示")

while True:
    try:
        n = input()
        s = int(n, 16)
        print(s)
    except:
        break

print("-"*10 + " 补充题1 " + "-"*10)
print("给定任意一个非空字符串，请编程回答存在多少种如下组合式的情况：'S1 + C1 + S2 + C2 + S3'。其中S1/S2/S3为任意非空字符串(三者可以相同也可以不同)，C1/C2为任意字符，且C1=C2。举例一：字符串'duowan'存在0种。举例二：字符串'duowanisgood'存在2种：'du + o + wanisg + o + od'和'du + o + wanisgo + o + d'")

while True:
    try:
        count = 0
        s = input()
        if len(s) < 5:
            print("input error")
            break
        for i in range(1, len(s)-3):
            x = 0
            for j in range(i+2, len(s)-1):
                if s[i] == s[j]:
                    x += 1
                    print("%s, %s, %s, %s, %s" % (s[:i], s[i], s[i+1:j], s[j], s[j+1:]))
            count += x
        print(count)
    except:
        break

print("-"*10 + " 补充题2 " + "-"*10)
print("老师想知道从某某同学当中，分数最高的是多少，现在请你编程模拟老师的询问。当然，老师有时候需要更新某位同学的成绩.\n输入描述:输入包括多组测试数据。 每组输入第一行是两个正整数N和M（0 < N <= 30000,0 < M < 5000）,分别代表学生的数目和操作的数目。 学生ID编号从1编到N。 第二行包含N个整数，代表这N个学生的初始成绩，其中第i个数代表ID为i的学生的成绩 接下来又M行，每一行有一个字符C（只取‘Q’或‘U’），和两个正整数A,B,当C为'Q'的时候, 表示这是一条询问操作，他询问ID从A到B（包括A,B）的学生当中，成绩最高的是多少 当C为‘U’的时候，表示这是一条更新操作，要求把ID为A的学生的成绩更改为B。\n输出描述:对于每一次询问操作，在一行里面输出最高成绩.")


while True:
    try:
        l1 = input().split(' ')
        if len(l1) < 2:
            break
        m, n = int(l1[0]), int(l1[1])
        l2 = list(map(int, input().split(' ')))   # 成绩列表
        if len(l2) < m:
            print("输入数据不合符要求")
            break
        for i in range(n):
            arr = input().split(' ')
            if len(arr) < 3:
                print("格式不符:Q/U 1 2")
                break
            if int(arr[1]) == 0 or int(arr[2]) == 0:
                print("不能传0")
                break
            if arr[0] == 'U':
                l2[int(arr[1])-1] = int(arr[2])
                print(l2)
            elif arr[0] == 'Q':
                a = min(int(arr[1]), int(arr[2])) - 1
                b = max(int(arr[1]), int(arr[2]))
                print(max(l2[a:b]))
    except:
        break