def mergesort(arr):
    n = len(arr)
    if n <= 1:
        return arr
    mid = n // 2
    left = mergesort(arr[:mid])
    right = mergesort(arr[mid:])
    return merge(left, right)

def merge(arr1, arr2):
    arr3 = []
    i = j = 0
    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            arr3.append(arr1[i])
            i += 1
        else:
            arr3.append(arr2[j])
            j += 1
    arr3.extend(arr1[i:])
    arr3.extend(arr2[j:])
    return arr3

arr = [3, 1, 5, 4, 2]
print(mergesort(arr))
