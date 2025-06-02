def makingstring(s):
    chunk=[]
    for i in range(0,len(s),2):
        chunk.append(s[i:i+2])
    print(chunk)
    ans=[]
    for word in chunk:
        ans.append(word[::-1])


    return ''.join(ans)

s="abcdefgh"
print(makingstring(s))