def countsort(arr):
    maxelement=max(arr)
    counts=[0]*(maxelement+1)
    output=[0]*len(arr)
    for i in range(1,len(arr)):
        counts[arr[i]]+=1
    
    
    print(counts)
    for i in range(1,len(counts)):
        counts[i]+=counts[i-1]
    for i in range(len(arr)-1,-1,-1):
        output[counts[arr[i]]-1]=arr[i]
        counts[arr[i]]-=1
    return output
        


arr=[4, 2, 2, 8, 3, 3, 1]
print(countsort(arr))  