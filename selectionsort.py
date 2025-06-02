def selectionsort(arr):
    n=len(arr)
    for i in range(n-1):
        minindex=i
        for j in range(i+1,n):
            if arr[j] < arr[minindex]:
                minindex=j
        arr[i],arr[minindex]=arr[minindex],arr[i]
    return arr
arr=[4,2,2,8,3,3,1]
print(selectionsort(arr))