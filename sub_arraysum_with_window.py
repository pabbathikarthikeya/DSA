def subarraysumwithwindow(k,n,arr,summ):
    currsum=0
    for num in range(k):
        currsum+=arr[num]
        if currsum==summ:
            return "Yes"
    for j in range(k,n):
        currsum=currsum+arr[j]-arr[j-k]
        if currsum==summ:
            return "Yes"
    return "No"
k=4
arr=[ 1, 4, 2, 10, 2,
        3, 1, 0, 20 ]

n=len(arr)
summ=18
print(subarraysumwithwindow(k,n,arr,summ))
