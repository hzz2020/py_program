# 冒泡排序:
# 时间复杂度O(n²)
# 空间复杂度O(1)
# 冒泡排序是从最后一位开始确定最大或最小的数，保证后面的数都是有序的且都大于或小于前面的数。

# 思路分析：
# 1.相邻两个数两两相比，n[j]跟n[j+1]比，如果n[j]>n[j+1]，则将进行交换，
# 2.j++, 重复以上步骤，第一趟结束后，最大数就会被确定在最后一位，这就是冒泡排序又称大（小）数沉底，
# 3.i++,重复以上步骤，直到i=n-1结束，排序完成。

def bubble_sort(arr):
    for i in range(len(arr) - 1):
        for j in range(len(arr) - 1 - i):
            if arr[j] > arr[j + 1]:
                arr[j + 1], arr[j] = arr[j], arr[j + 1]  # python交换变量值
        print(arr)  # 这里打印看变化
    print("*" * 10 + "最后结果：" + "*" * 10)
    print(arr)


A = [5, 2, 4, 6, 1, 3]

# 执行
bubble_sort(A)
