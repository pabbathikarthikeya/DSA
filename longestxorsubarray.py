def longestxorsub(arr):
    prefixsum=0
    xorsum=0
    indexmap={0:-1}
    maxlen=0
    for i in range(len(arr)):
        prefixsum+=arr[i]
        xorsum^=arr[i]
        if prefixsum==xorsum:
            maxlen=max(maxlen,i+1)
        if xorsum in indexmap:
            sublen=i-indexmap[xorsum]
            maxlen=max(maxlen,sublen)
        else:
            indexmap[xorsum]=i
    return maxlen
arr = [3, 6, 8, 10, 15, 50]
print(longestxorsub(arr))
