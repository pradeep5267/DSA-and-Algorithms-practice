def recursiveBinary(arr, item, low, high):
    arr = sorted(arr)

    mid = (high + low)//2
    if low  > high:
        return False
    elif (item == arr[low] or item == arr[high - 1] or item == mid):
        print('item found') 
    elif item < mid:
        recursiveBinary(arr, item, low, mid)
    elif item > mid:
        recursiveBinary(arr, item, mid, high - 1)

arr = [10,45,33,2,16,21,9,64,5]
recursiveBinary(arr, 33, 0, len(arr))
# print(len(arr))
