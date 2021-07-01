# 快速排序:
# 时间复杂度O(nlog2n)
# 空间复杂度O(log2n)
#
# 快速排序的思想就是，选一个数作为基数（这里我选的是第一个数），大于这个基数的放到右边，小于这个基数的放到左边，等于这个基数的数可以放到左边或右边。
#
# 思路分析：
# 一趟结束后，将基数放到中间分隔的位置，第二趟将数组从基数的位置分成两半，分割后的两个的数组继续重复以上步骤，选基数，将小数放在基数左边，将大数放到基数的右边，在分割数组，，，直到数组不能再分为止，排序结束。
# 例如从小到大排序:
# 1.  第一趟，第一个数为基数temp，设置两个指针left = 0，right = n.length，
# 　　①从right开始与基数temp比较，如果n[right]>基数temp，则right指针向前移一位，继续与基数temp比较，直到不满足n[right]>基数temp
# 　　②将n[right]赋给n[left]
# 　　③从left开始与基数temp比较，如果n[left]<=基数temp，则left指针向后移一位，继续与基数temp比较，直到不满足n[left]<=基数temp
# 　　④将n[left]赋给n[right]
# 　　⑤重复①-④步，直到left==right结束，将基数temp赋给n[left]
# 2.  第二趟，将数组从中间分隔，每个数组再进行第1步的操作，然后再将分隔后的数组进行分隔再快排，
# 3.  递归重复分隔快排，直到数组不能再分，也就是只剩下一个元素的时候，结束递归，排序完成

def quickSort(arr, start, end):
    if start < end:
        left, right = start, end
        temp = arr[start]
        while left < right:
            while left < right and arr[right] > temp:
                right -= 1
            arr[left] = arr[right]
            print(arr)  # 这里打印看变化
            while left < right and arr[left] <= temp:
                left += 1
            arr[right] = arr[left]
            print(arr)  # 这里打印看变化
        # 此时left == right
        arr[left] = temp
        print(arr)  # 这里打印看变化
        quickSort(arr, start, left - 1)
        quickSort(arr, left + 1, end)


A = [5, 2, 4, 6, 1, 3]
B = [10, 6, 3, 8, 33, 27, 66, 9, 7, 88]
# 执行
quickSort(A, 0, len(A) - 1)
quickSort(B, 0, len(B) - 1)
print("*" * 10 + "最后结果：" + "*" * 10)
print(A)
print(B)