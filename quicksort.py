def quicksort(arr):
    n=len(arr)
    if n <= 1:
        return arr
    pivot=arr[0]
    leftpart=[num for num in arr[1:] if num > pivot]
    rightpart=[num for num in arr[1:] if num <= pivot]
    return quicksort(leftpart)+[pivot]+quicksort(rightpart)
arr=[9,8,7,6,5,4,3,2,1]
print(quicksort(arr))