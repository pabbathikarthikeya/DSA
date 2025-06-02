def cyclicsort(arr):
    i=0
    while i<=len(arr)-1:
        correct_index=arr[i]-1
        if arr[i] != arr[correct_index]:
            arr[i],arr[correct_index]=arr[correct_index],arr[i]
        else:
            i+=1
    return arr
arr=[3,1,5,4,2]
print(cyclicsort(arr))