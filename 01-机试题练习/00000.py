while True:
    try:
        a = int(input())
        s = []
        for i in range(0, a):
            s.append(input().lower())
        print(s)
        for each in s:
            print(each)
            sum1 = 0
            c = 26
            count = []
            for i in list(set(each)):
                count.append(each.count(i))
                count = sorted(count, reverse=1)
            print(count)
            for i in count:
                sum1 += int(i)*c
                c -= 1
            print(sum1)
    except:
        break


# -------------- 求最小公倍数
A, B = map(int, input().split())
T = 1  # 初始1便于不影响乘数结果
for i in range(2, min(A, B) + 1):  # 只需遍历到最小的一个数
    while A % i == 0 and B % i == 0:  # 逐一找公共除数
        T = T * i  # 每找到一个公共除数就累乘
        A = A // i
        B = B // i
print(T * A * B)



hex_num = ['0', '1', '2', '3',
           '4', '5', '6', '7',
           '8', '9', 'a', 'b',
           'c', 'd', 'e', 'f',
           'A', 'B', 'C', 'D',
           'E', 'F']


def helper(s):
    ten = int(s, 16)  # 十六进制 --> 十进制
    bc = format(ten, 'b').rjust(4, '0')  # 十进制 --> 二进制 并且左补0
    bc = list(bc)
    bc.reverse()  # 翻转
    ten = int(''.join(bc), 2)  # 二进制 --> 十进制
    hc = format(ten, 'x')  # 十进制 --> 十六进制
    return hc.upper()

n = input()

a = helper(n)
print(a)