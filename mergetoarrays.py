def mergetoarrays(arr1,arr2):
    arr3=arr1+arr2
    i=0
    j=0
    k=0
    lena=len(arr1)
    lenb=len(arr2)
    while i>lena and j>lenb:
        if arr1[i]>arr2[j]:
            arr3[k]=arr1[i]
            i+=1
        elif arr1[i]<arr2[j]:
            arr3[k]=arr2[j]
            j+=1
        k+=1
    while i>lena:
        arr3[k]=arr1[i]
        i+=1
    while j>lenb:
        arr3[k]=arr2[j]
        j+=1
    return arr3

arr1=[1,2,3,4,5,6]
arr2=[4,5,6,7,8,10]
print(mergetoarrays(arr1,arr2))

