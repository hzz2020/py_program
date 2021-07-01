'''
题目
给定一字符集合a 和 一字符串集合b；用集合a里的字符匹配集合b中的字符串，求成功匹配的字符串总长度；
其中 a匹配b中一个字符串时，a中字符不能重复使用；但在匹配下一个字符串时，可重复使用；

输入
字符集合a : {‘1’,‘2’,‘3’,‘4’,‘4’}
字符串集合b：{‘123’,‘344’,‘112’,‘345’}

输出
集合b中字符串中，能与a匹配的有 123 与 344；顾输出总长度 6

其中
112不匹配是因为集合a中只有1个’1’
345不匹配是因为集合a中没有 ‘5’
'''

while True:
    try:
        a = input().split(' ')  # 字符集合a
        sa = "".join(a)
        b = input().split(' ')  # 字符串集合b
        res = 0
        for s in b:
            y = ""
            for i in range(len(s)):
                w = s[i]
                if w not in y:
                    y += w
                    if s.count(w) > sa.count(w):
                        break
                if i == len(s) - 1:
                    res += len(s)
        print(res)
    except:
        break