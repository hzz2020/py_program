# 直接插入排序:
# 时间复杂度O(n²)  最好情况下时间复杂度为O(n)、最坏情况下时间复杂度为O(n²)
# 空间复杂度O(1)
# 插入排序就是保证前面的序列是有序的，只需要把当前数插入前面的某一个位置即可。
#
# 思路分析：
# 1.从第二位开始遍历，
# 2.当前数（第一趟是第二位数）与前面的数依次比较，如果前面的数大于当前数，则将这个数放在当前数的位置上，当前数的下标-1，
# 3.重复以上步骤，直到当前数不大于前面的某一个数为止，这时，将当前数，放到这个位置，
# 　　1-3步就是保证当前数的前面的数都是有序的，内层循环的目的就是将当前数插入到前面的有序序列里
# 4.重复以上3步，直到遍历到最后一位数，并将最后一位数插入到合适的位置，插入排序结束。

# 方法一
def insert_sort(arr):
    for i in range(1, len(arr)):
        temp = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > temp:
            arr[j + 1] = arr[j]
            j = j - 1
        arr[j + 1] = temp
        print(arr)  # 这里打印看变化
    print("*" * 10 + "最后结果：" + "*" * 10)
    print(arr)


# 方法二
def insert_sort2(arr):
    for i in range(1, len(arr)):
        temp = arr[i]
        for j in range(i, 0, -1):  # for循环递减
            if arr[j - 1] > temp:
                arr[j] = arr[j - 1]
                if j == 1:
                    arr[j - 1] = temp
                    break
            else:
                arr[j] = temp
                break
        print(arr)  # 这里打印看变化
    print("*" * 10 + "最后结果：" + "*" * 10)
    print(arr)


A = [5, 2, 4, 6, 1, 3]
B = [5, 2, 4, 6, 1, 3]

# 执行1
insert_sort(A)
# 执行2
insert_sort2(B)
