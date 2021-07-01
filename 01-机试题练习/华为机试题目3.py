# -----

print("-"*10 + " 华为2016研发工程师编程题一 " + "-"*10)

print("有一个数组a[N]顺序存放0~N-1，要求每隔两个数删掉一个数，到末尾时循环至开头继续进行，求最后一个被删掉的数的原始下标位置。以8个数(N=7)为例:｛0，1，2，3，4，5，6，7｝，0->1->2(删除)->3->4->5(删除)->6->7->0(删除),如此循环直到最后一个数被删除。")

while True:
    try:
        n = int(input())
        if n > 1000:
            n = 999
        arr = list()
        for i in range(n):
            arr.append(i)
        count = 0
        i = 0
        while True:
            if i == n:  # i == n 时，已到末尾
                i = i % n
            if arr[i] != -1:  # 未标记-1的count+1
                count += 1
            if count == 3:  # 隔3标记一个[-1]
                count = 0  # 重置计数
                arr[i % n] = -1  # 标记
                if arr.count(-1) == len(arr):  # 标记数 == 总数 则最后一个的下标为i
                    print(i)
                    break
            i += 1
    except:
        print('有错误')
        break

print("-"*10 + " 华为2016研发工程师编程题二 " + "-"*10)

print("输入一个字符串，求出该字符串包含的字符集合"
      "输入描述:每组数据输入一个字符串，字符串最大长度为100，且只包含字母，不可能为空串，区分大小写。"
      "输出描述:每组数据一行，按字符串原有的字符顺序，输出字符集合，即重复出现并靠后的字母不输出。"
      "示例1：输入：abcqweracb"
      "输出：abcqwer")

while True:
    try:
        # s = input()
        # res = ''
        # 上述2句代码可以用下面的1句：
        res, s = '', input()
        for w in s:
            if w not in res:
                res += w
        print(res)
    except:
        break


print("-"*10 + " 华为2016研发工程师编程题三 " + "-"*10)
print("数独是一个我们都非常熟悉的经典游戏，运用计算机我们可以很快地解开数独难题，现在有一些简单的数独题目，请编写一个程序求解。如有多解，输出一个解")

import time
t0 = time.time()

class point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.available = []
        self.value = 0


def rowNum(p, sudoku):
    row = set(sudoku[p.y * 9:(p.y + 1) * 9])
    row.remove(0)
    return row  # set type


def colNum(p, sudoku):
    col = []
    length = len(sudoku)
    for i in range(p.x, length, 9):
        col.append(sudoku[i])
    col = set(col)
    col.remove(0)
    return col  # set type


def blockNum(p, sudoku):
    block_x = p.x // 3
    block_y = p.y // 3
    block = []
    start = block_y * 3 * 9 + block_x * 3
    for i in range(start, start + 3):
        block.append(sudoku[i])
    for i in range(start + 9, start + 9 + 3):
        block.append(sudoku[i])
    for i in range(start + 9 + 9, start + 9 + 9 + 3):
        block.append(sudoku[i])
    block = set(block)
    block.remove(0)
    return block  # set type


def initPoint(sudoku):
    pointList = []
    length = len(sudoku)
    for i in range(length):
        if sudoku[i] == 0:
            p = point(i % 9, i // 9)
            for j in range(1, 10):
                if j not in rowNum(p, sudoku) and j not in colNum(p, sudoku) and j not in blockNum(p, sudoku):
                    p.available.append(j)
            pointList.append(p)
    return pointList


def tryInsert(p, sudoku):
    availNum = p.available
    for v in availNum:
        p.value = v
        if check(p, sudoku):
            sudoku[p.y * 9 + p.x] = p.value
            if len(pointList) <= 0:
                t1 = time.time()
                useTime = t1 - t0
                showSudoku(sudoku)
                print('\nuse Time: %f s' % (useTime))
                exit()
            p2 = pointList.pop()
            tryInsert(p2, sudoku)
            sudoku[p2.y * 9 + p2.x] = 0
            sudoku[p.y * 9 + p.x] = 0
            p2.value = 0
            pointList.append(p2)
        else:
            pass


def check(p, sudoku):
    if p.value == 0:
        print('not assign value to point p!!')
        return False
    if p.value not in rowNum(p, sudoku) and p.value not in colNum(p, sudoku) and p.value not in blockNum(p, sudoku):
        return True
    else:
        return False


def showSudoku(sudoku):
    for j in range(9):
        for i in range(9):
            print('%d ' % (sudoku[j * 9 + i]), end='')
        print('')


if __name__ == '__main__':
    sudoku = [
        8, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 3, 6, 0, 0, 0, 0, 0,
        0, 7, 0, 0, 9, 0, 2, 0, 0,
        0, 5, 0, 0, 0, 7, 0, 0, 0,
        0, 0, 0, 0, 4, 5, 7, 0, 0,
        0, 0, 0, 1, 0, 0, 0, 3, 0,
        0, 0, 1, 0, 0, 0, 0, 6, 8,
        0, 0, 8, 5, 0, 0, 0, 1, 0,
        0, 9, 0, 0, 0, 0, 4, 0, 0,
    ]
    pointList = initPoint(sudoku)
    showSudoku(sudoku)
    print('\n')
    p = pointList.pop()
    tryInsert(p, sudoku)

