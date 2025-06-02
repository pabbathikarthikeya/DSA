def findingmiddle(arr):
    left=0
    right=len(arr)-1
    mid=(left+right)//2
    if mid % 2 == 0:
        return [arr[mid]]
    elif mid % 2 != 0:
        return [arr[mid],arr[mid+1]]
arr=['K','A','R','T','H','I','K','E','Y','A','N']
print(findingmiddle(arr))
