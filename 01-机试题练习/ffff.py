'''
2.求坐标轴上画出图形的面积
从(0,0)开始，指定终点x坐标，y轴坐标以偏移量呈现，-表示向下偏移
第1行：n e ，n表示有几组数据，e表示终点坐标
第2-n行：x offsety 每次x都会递增
比如：
3 8
0 1
2 1
4 -4
构成图形：
'''

while True:
    try:
        mlx = list()
        mly = list()
        res = 0
        arr = input().split(' ')
        m = int(arr[0])
        n = int(arr[1])

        for i in range(m):
            tmp = input().split(' ')
            mlx.append(int(tmp[0]))
            mly.append(int(tmp[1]))
        mlx.append(n)
        mly.append(0)
        print(mlx)
        print(mly)
        for i in range(min(len(mlx), len(mly))-1):
            l = mlx[i+1] - mlx[i]
            print(l)
            h = abs(sum(mly[:i+1]))
            print(h)
            count = l * h
            print(count)
            res += count
        print(res)
    except:
        print("出错了")
        break