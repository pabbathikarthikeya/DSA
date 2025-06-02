def splitingthearray(arr):
    total=sum(arr)
    if total % 2!=0:
        return None
    leftsum=0
    halfsum=total//2
    for num in range(len(arr)):
        leftsum+=arr[num]
        if leftsum==halfsum:
            return arr[num+1:],arr[:num+1]
arr=[1, 2, 3, 4, 5, 5]
print(splitingthearray(arr))